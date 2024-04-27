# cli.py
#
# Copyright 2023 Ondřej Míchal
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import contextlib
import json
import logging
import pathlib
import sys
import tempfile
import time
import traceback

import click
import sysrapl as sr
import sysrapl.profile as sr_profile

logger = logging.getLogger(__name__)

@click.group()
def sysrapl():
    """Profiler of system call energy consumption"""
    pass


@sysrapl.command()
@click.option(
    "-d", "--delay", default=0, type=int, help="Delay before starting the profiling."
)
@click.option(
    "-f",
    "--frequency",
    default=99,
    type=int,
    help="Frequency at which RAPL consupmtion will be read.",
)
@click.option(
    "-o",
    "--output",
    default=None,
    type=click.Path(exists=False, path_type=pathlib.Path),
    help="File where to store the profile If not provided the profile is printed to stdout",
)
@click.option("-p", "--pid", default=-1, type=int, help="PID of the profiled process")
@click.option(
    "--enable-syscalls/--disable-syscalls", default=True, help="Profile system calls"
)
@click.option(
    "--reevaluate",
    default=None,
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        writable=True,
        path_type=pathlib.Path,
    ),
    help="Path to profile to re-evaluate its content.",
)
def profile(
    delay: int,
    frequency: int,
    output: pathlib.Path,
    pid: int,
    enable_syscalls: bool,
    reevaluate: pathlib.Path,
) -> int:
    """
    Profiler of system call energy consumption
    """

    if reevaluate:
        if not output:
            logger.error("Option --output needs to be set when --reevaluate is used.")
            return 1

        with open(reevaluate, mode="rw") as f:
            profile_data: dict = json.load(f)

            rapl_events = profile_data["rapl"]["events"]
            syscall_data = profile_data["syscalls"]
            rapl_sample_width = 1_000_000_000 / profile_data["info"]["frequency"]

            rapl_window = sr_profile.RaplWindow()

            for syscall in syscall_data:
                rapl_data_window = rapl_window(
                    rapl_events,
                    syscall["entry_time"],
                    syscall["exit_time"],
                )

                sr_profile._score_syscall(rapl_data_window, syscall, rapl_sample_width)

            with open(output, "w") as f:
                print(json.dumps(profile_data), file=f)

            return 0

    if not pid or pid < 1:
        print("The profiled PID has to be greater or equal to 1", file=sys.stderr)
        return 1

    # This is a very unreadable way of passing two closable files using with
    # of which one is either sys.stdout or an actual file.
    with tempfile.NamedTemporaryFile(
        mode="w+t", prefix="sysrapl-", suffix="-raw-profile"
    ) as raw_profile_file:
        with (
            open(output, mode="w+t")
            if output is not None
            else contextlib.nullcontext(sys.stdout)
        ) as profile_file:
            profile_start = time.monotonic_ns()

            # Profile a process using the profiling engine.
            try:
                sr_profile.profile(
                    raw_profile_file, pid, delay, frequency, enable_syscalls
                )
            except Exception:
                logger.error(f"Failed to profile process {pid}")
                print(traceback.format_exc(), file=sys.stderr)
                return 1

            profile_end = time.monotonic_ns()

            profile_data["info"]["duration"] = profile_end - profile_start

            # Process the raw profile data and populate the final profile JSON
            try:
                profile = sr_profile.post_process(raw_profile_file)
            except Exception:
                logger.error("Failed to process profile data")
                print(traceback.format_exc(), file=sys.stderr)
                return 1

            print(json.dumps(profile), file=profile_file)

    return 0


@sysrapl.command()
@click.argument("profile_file", default=None, type=click.Path(exists=True, path_type=pathlib.Path))
@click.option(
    "--sample-width",
    default=100,
    type=int,
    help="RAPL data sample width for plotting in milliseconds. Bound by the sampling frequency.",
)
@click.option(
    "--syscall-num",
    default=5,
    type=int,
    help="Number of top syscalls to show in plots.",
)
@click.option(
    "--rapl-domains",
    default=sr.RAPL_DOMAIN_LIST,
    type=click.Choice(sr.RAPL_DOMAIN_LIST),
    help="List of RAPL domains to show in plots. Order determines ranking of syscall prices.",
)
@click.option(
    "-o",
    "--output-dir",
    default=None,
    type=click.Path(file_okay=False, dir_okay=True, path_type=pathlib.Path),
    help="Directory for storing the report [./<process-name>_<pid>_<datetime>]",
)
@click.option(
    "--enable-rapl/--disable-rapl", default=True, help="Plot RAPL events."
)
@click.option(
    "--enable-syscalls/--disable-syscalls", default=True, help="Plot system calls."
)
@click.option(
    "--force", default=False, help="Overwrite the contents of the used output directory."
)
def report(
    profile_file: pathlib.Path,
    sample_width: int,
    syscall_num: int,
    rapl_domains: list[str],
    output_dir: pathlib.Path,
    plot_rapl: bool,
    plot_syscalls: bool
) -> int:
    """
    Visualizer of sysrapl profiles
    """
    import matplotlib
    import matplotlib.style
    import seaborn
    import sysrapl.report as sr_report

    seaborn.set_theme()
    seaborn.set_context("paper")

    matplotlib.style.use("fast")
    matplotlib.rcParams["path.simplify"] = True
    matplotlib.rcParams["path.simplify_threshold"] = 1.0
    matplotlib.rcParams["agg.path.chunksize"] = 10000
    matplotlib.rcParams["savefig.dpi"] = 300

    with open(profile_file.name, mode="r") as f:
        try:
            profile_data = json.load(f)
        except Exception as e:
            logger.error(f"The profile file could not be loaded: {e}")
            return 1

        if not output_dir:
            info = profile_data["info"]
            output_dir = pathlib.Path(f"{info['process-name']}-{info['pid']}-{info['time']}")

        frequency = profile_data["info"]["frequency"]
        if 1000 / frequency > sample_width:
            logger.error("The sample width can not be lower than the sampling frequency of the source data")
            return 1

        try:
            sr_report.print_report(profile_data, output_dir, rapl_domains, syscall_num, sample_width, plot_rapl, plot_syscalls)
        except:
            return 1

    return 0
