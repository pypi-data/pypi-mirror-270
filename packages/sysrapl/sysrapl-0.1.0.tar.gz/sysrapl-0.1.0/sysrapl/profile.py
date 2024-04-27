# profile.py
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

from __future__ import annotations

import bisect
import ctypes
import datetime
import itertools
import logging
import os
import platform
import signal
import sys

from typing import IO

import system_calls

import sysrapl


_KNOWN_SYSCALLS: dict[int, str] = {}
_SYSRAPL_EVENT_SYS: int = 0
_SYSRAPL_EVENT_RAPL: int = 1


logger = logging.getLogger(__name__)


libsysrapl: ctypes.CDLL = ctypes.CDLL(
    os.path.join(os.path.dirname(__file__), "libsysrapl.so")
)


def _diff_rapl_value(prev: int, next: int) -> int:
    if prev > next:
        padding = sysrapl.RAPL_MAX_VALUE - prev
        return next + padding
    else:
        return next - prev


def _sigint_empty_handler(signum, frame):
    pass


def _get_process_name(pid: int) -> str:
    with open(f"/proc/{pid}/comm", "r") as f:
        return f.read().strip()

    return "<Unknown>"


def _get_processor_model() -> str:
    try:
        with open("/proc/cpuinfo", "r") as f:
            for line in f:
                if not line.startswith("model name"):
                    continue

                return line.split(":", 1)[1].strip()
    except Exception:
        pass

    return "<Unknown>"


def _get_syscall_id_name(syscall_id: int) -> str:
    if syscall_id in _KNOWN_SYSCALLS:
        return _KNOWN_SYSCALLS[syscall_id]

    try:
        syscalls = system_calls.syscalls()

        for name in syscalls.names():
            try:
                if syscall_id == syscalls.get(name):
                    _KNOWN_SYSCALLS[syscall_id] = name
                    return name
            except system_calls.NotSupportedSystemCall:
                pass
            except system_calls.NoSuchSystemCall:
                pass
    except ImportError:
        pass

    return ""


class SysraplProfileOpts(ctypes.Structure):
    _fields_ = [
        ("output_file", ctypes.c_char_p),
        ("delay", ctypes.c_int64),
        ("filter_pid", ctypes.c_int64),
        ("frequency", ctypes.c_int64),
        ("enable_syscalls", ctypes.c_bool),
    ]


class RaplData(dict):
    def __init__(
        self,
        time: int = 0,
        cores: int = 0,
        pkg: int = 0,
        ram: int = 0,
        gpu: int = 0,
        psys: int = 0,
    ):
        super().__init__(
            time=time,
            cores=cores,
            pkg=pkg,
            ram=ram,
            gpu=gpu,
            psys=psys,
        )

    @staticmethod
    def diff(prev, next) -> RaplData:
        new = RaplData(0, 0, 0, 0, 0, 0)

        new["time"] = prev["time"]  # TODO: Why?
        for domain in sysrapl.RAPL_DOMAIN_LIST:
            new[domain] = _diff_rapl_value(prev[domain], next[domain])

        return new

    def add(self, other):
        for domain in sysrapl.RAPL_DOMAIN_LIST:
            self[domain] += other[domain]

    def ratio(self, ratio):
        for domain in sysrapl.RAPL_DOMAIN_LIST:
            self[domain] *= ratio


class SyscallData(dict):
    def __init__(
        self,
        id: int,
        name: str,
        cpu: int,
        tid: int,
        entry_time: int,
        exit_time: int,
    ):
        super().__init__(
            id=id,
            name=name,
            cpu=cpu,
            tid=tid,
            entry_time=entry_time,
            exit_time=exit_time,
        )


class RaplWindow:
    _left_index = 0
    _right_index = None

    def __call__(self, rapl_events: list[RaplData], entry_time: int, exit_time: int):
        """
        Finds and returns a list of RAPL readings matching the entry and exit times
        of a system call.

        Parameters
        ==========
        rapl_events
            List of processed RAPL events.
        entry_time
            Entry time (in nanoseconds) of a system call.
        exit_time
            Exit time (in nanoseconds) of a system call.

        Returns
        =======
        rapl_data_window
            list of processed RAPL events.
        """

        # There are no RAPL data that we can use to score the system call
        if entry_time < rapl_events[0]["time"] or exit_time < rapl_events[0]["time"]:
            return

        self._left_index = bisect.bisect_left(
            rapl_events, entry_time, lo=self._left_index, key=lambda i: i["time"]
        )
        self._right_index = bisect.bisect_right(
            rapl_events, exit_time, hi=self._right_index, key=lambda i: i["time"]
        )

        # At least one sample should be used
        if self._left_index == self._right_index:
            self._right_index += 1

        return rapl_events[self._left_index : self._right_index]


def _score_syscall(rapl_data_window: list, syscall_data: dict, rapl_sample_width: int):
    """
    Algorithm for giving an energy score to a system call.

    Parameters
    ==========
    rapl_data_window
        RAPL time window during which the system call ran.
    syscall_data
        System call data.
    rapl_sample_width
        Width of a RAPL time window (nanoseconds).
    """
    entry_time = syscall_data["entry_time"]
    exit_time = syscall_data["exit_time"]

    syscall_duration = exit_time - entry_time

    ratio = syscall_duration / (rapl_sample_width * len(rapl_data_window))

    # Use the duration of the system call as the time information
    syscall_rapl_data = RaplData(exit_time - entry_time)
    for rapl_data in rapl_data_window:
        # TODO: The edge entries need to be interpolated because the syscall
        # most likely did not start the moment the RAPL sampl was made. For now
        # that is not a concern.
        syscall_rapl_data.add(rapl_data)

    syscall_rapl_data.ratio(ratio)

    for domain in sysrapl.RAPL_DOMAIN_LIST:
        syscall_data[domain] = syscall_rapl_data[domain]


class SyscallProcessor:
    _rapl_window = RaplWindow()

    def __call__(
        self, rapl_events: list[RaplData], values: list[str], rapl_sample_width: int
    ):
        """
        Procesesses raw system call trace by looking up its name based on its ID
        and gives it an energy score using a scoring algorithm.

        Parameters
        ==========
        rapl_events
            List of processed RAPL events.
        values
            Raw system call trace.
        rapl_sample_width
            Width of a RAPL time window (nanoseconds).

        Returns
        =======
        syscall_data
            Processed syscall event.
        """
        cpu: int = int(values[1])
        tid: int = int(values[2])
        syscall_id: int = int(values[3])
        entry_time_ns: int = int(values[4])
        exit_time_ns: int = int(values[5])

        # The system_calls library is not sure to know a syscall's name, so
        # syscall_name can be an empty string.
        syscall_name = _get_syscall_id_name(syscall_id)

        rapl_data_window = self._rapl_window(rapl_events, entry_time_ns, exit_time_ns)

        # FIXME: rapl_window() should never return None
        # But this is a much quicker fix for the time being
        if not rapl_data_window:
            return

        syscall_data = SyscallData(
            syscall_id,
            syscall_name,
            cpu,
            tid,
            entry_time_ns,
            exit_time_ns,
        )

        _score_syscall(rapl_data_window, syscall_data, rapl_sample_width)

        return syscall_data


class RaplProcessor:
    _prev_rapl_event = None

    def __call__(self, values: list[str]):
        """
        Processes raw rapl energy readings by scaling the values and calculating
        energy consumed in between the different samples.

        Parameters
        ==========
        values
            Raw rapl energy readings.

        Returns
        =======
        rapl_data
            Processed RAPL event.
        """
        time: int = int(values[1])
        cores: int = int(int(values[2]) * sysrapl.RAPL_SCALE)
        pkg: int = int(int(values[3]) * sysrapl.RAPL_SCALE)
        ram: int = int(int(values[4]) * sysrapl.RAPL_SCALE)
        gpu: int = int(int(values[5]) * sysrapl.RAPL_SCALE)
        psys: int = int(int(values[6]) * sysrapl.RAPL_SCALE)

        # Total consumption
        if not self._prev_rapl_event:
            self.prev_rapl_event = RaplData(time, cores, pkg, ram, gpu, psys)

        prev_rapl_event: RaplData = self.prev_rapl_event
        next_rapl_event: RaplData = RaplData(time, cores, pkg, ram, gpu, psys)

        self.prev_rapl_event = next_rapl_event

        return RaplData.diff(prev_rapl_event, next_rapl_event)


def post_process(raw_profile_file: IO) -> dict:
    """
    Processes raw profiling data from an energy profiling session.

    Parameters
    ==========
    raw_profile_file
        File containing the raw profiling data.
    frequency
        Frequency at which RAPL values were sampled.

    Returns
    =======
    dict
        Dictionary with the processed profile data.

    Raises
    ======
    FileFormatMismatch
        For unknown passed data.
    """
    # TODO: Output configuration of the profiling session into the raw profile, so it can be picked up during
    # post-processing.

    pid = -1
    frequency = -1

    timestamp = raw_profile_file.readline().strip()

    profile: dict = {
        "info": {
            "process-name": _get_process_name(pid),
            "pid": pid,
            "time": timestamp,
            "frequency": frequency,
            "host-info": platform.uname()._asdict(),
        },
        "unit": "Joules",
        "scale": sysrapl.RAPL_SCALE,
        # TODO: Should be made into a parameter and the profiler should
        # filter out unsupported ones.
        "domains": sysrapl.RAPL_DOMAIN_LIST,
        "rapl": {
            "total": RaplData(),
            "events": [],
        },
        "syscalls": [],
    }

    profile["info"]["host-info"]["processor"] = _get_processor_model()

    rapl_processor = RaplProcessor()
    syscall_processor = SyscallProcessor()
    rapl_sample_width: int = int(1_000_000_000 / frequency)

    logger.info("Processing profiled data - RAPL events")

    # TODO: Make this into a single run through the raw profile file

    lines = 0
    for line in raw_profile_file:
        line = line.strip()
        values: list[str] = line.split(" ")
        record_type: int = int(values[0])

        lines += 1

        if record_type != _SYSRAPL_EVENT_RAPL:
            continue

        rapl_data: RaplData = rapl_processor(values)

        logger.debug(rapl_data)

        profile["events"].append(rapl_data)
        profile["total"].add(rapl_data)

    if len(profile["rapl"]["events"]) > 0:
        profile["rapl"]["total"]["time"] = (
            profile["rapl"]["events"][-1]["time"] - profile["rapl"]["events"][0]["time"]
        )

    raw_profile_file.seek(0)

    logger.info("Processing profiled data - system call events")

    for line in itertools.islice(raw_profile_file, lines):
        line = line.strip()
        values = line.split(" ")
        record_type = int(values[0])

        if record_type != _SYSRAPL_EVENT_SYS:
            continue

        syscall_data = syscall_processor(
            profile["rapl"]["events"], values, rapl_sample_width
        )

        logger.debug(syscall_data)

        # Consumption profile in time (chronological order of syscalls with
        # context and energy price
        profile["syscalls"].append(syscall_data)

    logger.debug(profile)

    return profile


def profile(
    output_file: IO,
    pid: int = -1,
    delay: int = 0,
    frequency: int = 99,
    enable_syscalls: bool = True,
):
    """
    Starts an energy profiling session using eBPF. The result of this session
    are raw profiling data writen to output_file that need to be further processed
    (see post_process()). The function is blocking and needs to be cancelled using
    the SIGINT signal.

    Parameters
    ==========
    output_file : IO
        Output file for the raw profiling data.
    pid
        PID of the profiled process.
    delay
        Delay before starting the profiling (in seconds).
    frequency
        Frequency at which RAPL consumption will be read.
    enable_syscalls
        Profile system calls.

    Raises
    ======
    FileNotFoundError
    PermissionError
    RuntimeError
    """
    if not os.access(output_file.name, os.F_OK):
        logger.error("output file does not exist")
        raise FileNotFoundError

    if not os.access(output_file.name, os.W_OK):
        logger.error("output file is not writeable")
        raise PermissionError


    profile_opts: SysraplProfileOpts = SysraplProfileOpts(
        ctypes.c_char_p(str.encode(output_file.name)),
        ctypes.c_int64(delay),
        ctypes.c_int64(pid),
        ctypes.c_int64(frequency),
        ctypes.c_bool(enable_syscalls),
    )

    # Log the beginning of the profiling session (for post-processing)
    curr_time = datetime.datetime.now().isoformat(timespec="seconds")
    output_file.write(curr_time)

    # The C library implements its own SIGINT handler. Suppress the default one
    # for the duration of the collection, so that the post-processing phase is
    # not skipped.
    orig_sigint_handler = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, _sigint_empty_handler)

    print("Profiling. Press Ctrl+C to stop.", file=sys.stderr, end=None)

    if libsysrapl.sysrapl_profile(ctypes.byref(profile_opts)) != 0:
        logger.error("profiling failed")
        raise RuntimeError("profiling failed")

    signal.signal(signal.SIGINT, orig_sigint_handler)
