# report.py
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

import datetime
import logging
import os
import pathlib

import matplotlib
import matplotlib.dates
import matplotlib.pyplot
import matplotlib.transforms
import matplotlib.patheffects
import matplotlib.style
import matplotlib.ticker
import matplotlib.units
import pandas
import seaborn
import seaborn.objects
from tabulate import tabulate

import sysrapl

logger = logging.getLogger(__name__)


def _get_iqr(df: pandas.DataFrame, column: str) -> (int, int, int):
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1

    return (q1, q3, iqr)


def _norm(df: pandas.DataFrame, column: str) -> pandas.DataFrame:
    min = df[column].min()
    max = df[column].max()

    df[column] = (df[column] - min) / (max - min)
    return df


def _iqr_energy_domains(
    df: pandas.DataFrame, energy_domains: list[str]
) -> pandas.DataFrame:
    wdf = df
    wdf = wdf.melt(id_vars=["id", "name"], value_vars=energy_domains)

    q1, q3, iqr = _get_iqr(wdf, "value")

    for domain in energy_domains:
        df = df.query(f"(@q1 - 1.5 * @iqr) <= {domain} <= (@q3 + 1.5 * @iqr)")

    return df


def _plot_waterfall_graph(df: pandas.DataFrame, title: str, filename: str) -> None:
    def draw_subplot(
        data: pandas.DataFrame,
        color: matplotlib.colors.ListedColormap,
        label: str,
        **kwargs,
    ):
        ax: matplotlib.pyplot.Axes = seaborn.lineplot(
            data=data,
            x="entry_time",
            y="value",
            hue="group",
            clip_on=False,
            alpha=0.5,
            lw=1.5,
            color=color,
            errorbar=None,
            n_boot=0,
            estimator=None,
            **kwargs,
        )

        # Fill under the line
        line: matplotlib.pyplot.Line2D = ax.lines[0]
        ax.fill_between(
            line.get_xdata(), line.get_ydata(), color=color, alpha=0.5, **kwargs
        )

        # Outline to separate the diffeerent plots
        seaborn.lineplot(
            data=data,
            x="entry_time",
            y="value",
            clip_on=False,
            color="black",
            alpha=0.7,
            lw=2,
            errorbar=None,
            n_boot=0,
            estimator=None,
            **kwargs,
        )

    def draw_labels(
        data: pandas.DataFrame,
        color: matplotlib.colors.ListedColormap,
        label: str,
        **kwargs,
    ):
        ax: matplotlib.pyplot.Axes = matplotlib.pyplot.gca()

        txt: matplotlib.text = ax.text(
            0,
            0.2,
            label,
            fontweight="bold",
            color=color,
            ha="left",
            va="center",
            transform=ax.transAxes,
        )
        txt.set_path_effects(
            [
                matplotlib.patheffects.Stroke(linewidth=1, foreground="w"),
                matplotlib.patheffects.Normal(),
            ]
        )

    with seaborn.axes_style(style="white", rc={"axes.facecolor": (0, 0, 0, 0)}):
        pal: matplotlib.colors.ListedColormap = seaborn.cubehelix_palette(
            25, rot=0, dark=0.3, light=0.7, reverse=True
        )

        g: seaborn.FacetGrid = seaborn.FacetGrid(
            df,
            row="group",
            hue="group",
            aspect=15,
            height=0.5,
            sharex=True,
            legend_out=True,
            palette=pal,
            despine=True,
        )

        g.map_dataframe(draw_subplot)
        g.map_dataframe(draw_labels)

        g.figure.suptitle(title)
        g.set_titles("")
        g.set(xlabel="time [hh:mm:ss]", yticks=[], ylabel="")
        g.despine(bottom=True, left=True)
        g.figure.subplots_adjust(hspace=-0.5)

        g.savefig(filename)


def _plot_syscall(data: dict, output_dir: pathlib.Path, rapl_domains: list[str] = sysrapl.RAPL_DOMAIN_LIST,
                  syscall_num: int = 5, sample_width: int = 100):
    df: pandas.DataFrame = pandas.DataFrame(
        data["syscalls"],
    )

    # We can try to make the dataframe smaller.
    df[["id", "cpu", "tid"]] = df[["id", "cpu", "tid"]].apply(
        pandas.to_numeric, downcast="unsigned"
    )

    df["entry_time"] -= df["entry_time"].iat[0]
    df["exit_time"] -= df["exit_time"].iat[0]
    df[["entry_time", "exit_time"]] = df[["entry_time", "exit_time"]].apply(
        pandas.to_datetime
    )

    # Drop filtered out RAPL domains
    excluded_rapl_domains = [
        domain for domain in sysrapl.RAPL_DOMAIN_LIST if domain not in rapl_domains
    ]
    df = df.drop(columns=excluded_rapl_domains)

    # Apply IQR across energy domains
    df = _iqr_energy_domains(df, rapl_domains)

    # Scale the RAPL values to milijoules
    # FIXME: Should work with different scaling as well.
    for domain in rapl_domains:
        df[domain] = df[domain] / 10**6

    # Get the top consuming syscalls
    wdf = df

    wdf = wdf.groupby(by=["name"]).sum(numeric_only=True)

    top_syscalls_df = wdf.sort_values(by=rapl_domains, ascending=False).head(
        n=syscall_num
    )
    top_syscalls = top_syscalls_df.index.to_list()

    # Keep in the list only the top consuming syscalls
    df = df[df["name"].isin(top_syscalls) == True]
    df = df.reset_index().drop(columns="index")

    # Consumption per-domain per-syscall - Bar plot

    wdf = df

    wdf = wdf.melt(
        id_vars=["id", "name"],
        var_name="energy domain",
        value_vars=rapl_domains,
        value_name="energy consumption [mJ]",
    )
    wdf = wdf.reset_index()

    ax = seaborn.barplot(
        data=wdf, x="name", hue="energy domain", y="energy consumption [mJ]"
    )

    ax.set(
        title="Total consumption (per-syscall per-domain)", xlabel="system call name"
    )
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
    seaborn.move_legend(ax, loc="center left", bbox_to_anchor=(1, 0.5))
    matplotlib.pyplot.savefig(
        f"{output_dir}/consumption_per_syscall_per_domain_barplot.png",
        bbox_inches="tight",
    )
    matplotlib.pyplot.clf()

    # Distribution of min/max energy consumptions - Box plot

    wdf = df

    wdf = wdf.drop(columns=["cpu", "tid", "entry_time", "exit_time"])

    wdf = wdf.melt(
        id_vars=["id", "name"],
        var_name="energy domain",
        value_vars=rapl_domains,
        value_name="energy consumption [mJ]",
    )

    wdf = wdf.reset_index()

    ax = seaborn.boxplot(
        wdf, x="name", y="energy consumption [mJ]", hue="energy domain"
    )

    ax.set(
        label="Distribution of energy consumption (per-syscall per-domain)",
        xlabel="system call name",
    )
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
    seaborn.move_legend(ax, loc="center left", bbox_to_anchor=(1, 0.5))
    matplotlib.pyplot.savefig(
        f"{output_dir}/consumption_distribution_across_syscalls_boxplot.png",
        bbox_inches="tight",
    )
    matplotlib.pyplot.clf()

    # Number of different syscalls - Bar plot

    wdf = df

    wdf = (
        wdf.value_counts("name", ascending=True)
        .to_frame()
        .reset_index()
        .rename(columns={0: "count"})
    )

    ax = seaborn.barplot(data=wdf, x="name", y="count", order=wdf["name"])

    ax.set(title="Number of system calls", xlabel="system call name")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
    matplotlib.pyplot.savefig(
        f"{output_dir}/number_of_syscalls_barplot.png", bbox_inches="tight"
    )

    # Energy consumption across syscalls/consumption domains in time - Heatmap

    wdf = df

    wdf = wdf.drop(columns=["id", "cpu", "tid", "exit_time"])

    wdf = (
        wdf.set_index("entry_time")
        .groupby("name")
        .resample(f"{sample_width}ms")
        .sum(numeric_only=True)
    )
    wdf = wdf.reset_index()

    wdf["entry_time"] = wdf["entry_time"].apply(lambda x: x.strftime("%M:%S:%f"))

    wdf = wdf.melt(
        id_vars=["name", "entry_time"],
        var_name="energy domain",
        value_name="energy consumption (normalized)",
    )

    # Normalize values to (0,1) range
    wdf = _norm(wdf, "energy consumption (normalized)")
    wdf = wdf.pivot(index=["name", "energy domain"], columns=["entry_time"])

    wdf = wdf["energy consumption (normalized)"]
    wdf = wdf.fillna(0)

    cg = seaborn.clustermap(
        data=wdf,
        row_cluster=False,
        col_cluster=False,
        dendrogram_ratio=(0.2, 0.001),
        cbar_pos=(0.02, 0.2, 0.1, 0.7),
        xticklabels=round(len(wdf.columns) / 25),
        yticklabels=True,
    )

    cg._figure.axes[2].set_xticklabels(
        cg._figure.axes[2].get_xticklabels(), rotation=40, ha="right"
    )
    cg._figure.axes[2].hlines(
        range(0, len(rapl_domains) * syscall_num, len(rapl_domains)),
        *cg._figure.axes[2].get_xlim(),
    )
    cg._figure.axes[2].set(
        title="Consumption in time (normalized)",
        xlabel="time [mm:ss:µs]",
        ylabel="system call name-energy domain",
    )
    cg.savefig(
        f"{output_dir}/consumption_in_time_heatmap.png", bbox_inches="tight"
    )

    # Cumulative energy consumption across syscalls/consumption domains in time - Tsunami graph

    wdf = df

    wdf = wdf.reset_index()

    # Replace negative values with zeroes as negative energy consumption is not
    # valid.
    wdf[domain] = wdf[domain].clip(lower=0)

    # Melt the columns into a structure the plotting library understands
    wdf = wdf.melt(
        id_vars=["name", "entry_time"],
        value_vars=rapl_domains,
    )

    # Group together the name of syscalls and energy domains
    wdf["group"] = wdf["name"] + "-" + wdf["variable"]
    wdf = wdf.drop(columns=["name", "variable"])

    # We want to show the data in a cumulative manner
    wdf["value"] = wdf.groupby(by=["group"])["value"].transform(pandas.Series.cumsum)

    # Normalize values to (0,1) range
    wdf = _norm(wdf, "value")
    wdf = wdf.fillna(0)

    # Order from the highest consumption to the lowest
    waterfall_sort_order = (
        wdf.groupby("group")["value"].max().sort_values(ascending=False).index.to_list()
    )
    wdf = wdf.sort_values(
        by="group",
        key=lambda column: column.map(lambda elem: waterfall_sort_order.index(elem)),
    )

    _plot_waterfall_graph(
        wdf,
        "Cumulative consumption in time (normalized)",
        f"{output_dir}/consumption_in_time_tsunami_graph.png",
    )

    # Energy consumption across syscalls/consumption domains in time - Waterfall graph

    wdf = df

    # Resample the data to control the density
    # First downsample to cut down the samples and then upsample to interpolate between
    wdf = (
        wdf.set_index("entry_time")
        .groupby("name")
        .resample(f"{sample_width}ms")
        .sum(numeric_only=True)
        .reset_index()
    )
    wdf = (
        wdf.set_index("entry_time")
        .groupby("name")
        .resample(f"{sample_width * 1000 / 10}us")
        .asfreq()
        .drop(columns=["name"])
        .reset_index()
    )
    for domain in rapl_domains:
        wdf[domain] = wdf.groupby("name")[domain].transform(
            lambda g: g.interpolate(method="akima")
        )

    # Replace negative values with zeroes as negative energy consumption is not
    # valid.
    wdf[domain] = wdf[domain].clip(lower=0)

    # Melt the columns into a structure the plotting library understands
    wdf = wdf.melt(
        id_vars=["name", "entry_time"],
        value_vars=rapl_domains,
    )

    # Group together the name of syscalls and energy domains
    wdf["group"] = wdf["name"] + "-" + wdf["variable"]
    wdf = wdf.drop(columns=["name", "variable"])

    # Normalize values to (0,1) range
    wdf = _norm(wdf, "value")
    wdf = wdf.fillna(0)

    # Order from the highest consumption to the lowest
    wdf = wdf.sort_values(
        by="group",
        key=lambda column: column.map(lambda elem: waterfall_sort_order.index(elem)),
    )

    _plot_waterfall_graph(
        wdf,
        "Consumption in time (normalized)",
        f"{output_dir}/consumption_in_time_waterfall_graph.png",
    )


def _plot_rapl(data: dict, output_dir: pathlib.Path, rapl_domains: list[str] = sysrapl.RAPL_DOMAIN_LIST):
    df = pandas.DataFrame(data["rapl"]["events"])

    df["time"] -= df["time"].iat[0]
    df["time"] = pandas.to_datetime(df["time"])

    excluded_rapl_domains = [
        domain for domain in sysrapl.RAPL_DOMAIN_LIST if domain not in rapl_domains
    ]
    df = df.drop(columns=excluded_rapl_domains)
    for domain in rapl_domains:
        df[domain] = df[domain] / 10**6

    # Consumption in time

    wdf = df
    wdf = wdf.melt(
        id_vars=["time"],
        var_name="energy domain",
        value_vars=rapl_domains,
        value_name="energy consumption [mJ]",
    )

    p = seaborn.objects.Plot(data=wdf)
    p = p.add(
        seaborn.objects.Area(),
        seaborn.objects.Stack(),
        x="time",
        y="energy consumption [mJ]",
        color="energy domain",
    )
    p = p.label(
        title="Consumption per-domain in time",
        x="time [hh:mm:ss]",
        y="energy consumption [mJ]",
    )
    p = p.theme({"legend.loc": "lower center"})
    p.save(
        output_dir.joinpath("rapl_per_domain_in_time.png"), bbox_inches="tight", dpi=300
    )

    wdf = df
    wdf[rapl_domains] = wdf[rapl_domains].cumsum()
    wdf = wdf.melt(
        id_vars=["time"],
        var_name="energy domain",
        value_vars=rapl_domains,
        value_name="energy consumption [J]",
    )
    wdf["energy consumption [J]"] /= 10**3

    ax = seaborn.lineplot(
        wdf, x="time", y="energy consumption [J]", hue="energy domain"
    )
    ax.set(xlabel="time [hh:mm:ss]")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
    seaborn.move_legend(ax, loc="center left", bbox_to_anchor=(1, 0.5))
    matplotlib.pyplot.savefig(
        output_dir.joinpath("rapl_in_time.png"), bbox_inches="tight"
    )
    matplotlib.pyplot.clf()


def print_report(data: dict, output_dir: pathlib.Path, rapl_domains: list[str] = sysrapl.RAPL_DOMAIN_LIST,
                 syscall_num: int = 5, sample_width: int = 100, plot_rapl: bool = True, plot_syscalls: bool = True, force: bool = False):
    info: dict = data["info"]
    rapl: dict = data["rapl"]

    if os.access(output_dir.name, os.O_DIRECTORY) and not force:
        logger.error("output directory already exists")
        raise FileExistsError

    frequency = data["info"]["frequency"]
    if sample_width < 1000 / frequency:
        logger.error("The sample width can not be lower than the sampling frequency of the source data")
        raise ValueError

    try:
        os.makedirs(output_dir, exist_ok=True)
    except:
        logger.error("failed to prepare output directory")
        raise

    report_file_name = output_dir.joinpath("report.txt")
    with open(report_file_name, "w") as f:
        # Information about the profiled process
        info_general = [
            ["Process", info["process-name"]],
            ["Profile time", info["time"]],
            [
                "Profile duration",
                datetime.timedelta(microseconds=info["duration"] / 1000),
            ],
            ["Energy profile frequency", f"{info['frequency']} Hz"],
        ]
        print(
            "# General information:\n" + tabulate(info_general, tablefmt="plain"),
            file=f,
            end="\n\n",
        )

        info_machine = []
        for key in info["host-info"]:
            info_machine.append([key, info["host-info"][key]])
        print(
            "# System information:\n" + tabulate(info_machine, tablefmt="plain"),
            file=f,
            end="\n\n",
        )

        # Drop filtered out RAPL domains
        rapl_domains = [
            domain for domain in sysrapl.RAPL_DOMAIN_LIST if domain in rapl_domains
        ]

        # Consumption of top syscalls
        df: pandas.DataFrame = pandas.DataFrame(data["syscalls"])

        df = _iqr_energy_domains(df, rapl_domains)

        # Ratio of <process consumption>/<total consumption>
        wdf: pandas.DataFrame = df

        wdf_sum = wdf.sum(numeric_only=True)

        for domain in rapl_domains:
            wdf_sum[domain] = wdf_sum[domain] / 10**9

        info_ratio = []
        for domain in rapl_domains:
            total_domain = rapl["total"][domain] / 10**9
            ratio = wdf[domain] / total_domain
            info_ratio.append(
                [
                    domain,
                    total_domain,
                    wdf[domain],
                    f"{ratio:.2%}",
                ]
            )
        print(
            "# Ratio of energy consumption (total/process):\n"
            + tabulate(
                info_ratio,
                headers=[
                    "energy domain",
                    "system [J]",
                    "process [J]",
                    "ratio",
                ],
                tablefmt="plain",
                floatfmt=",.3f",
            ),
            file=f,
            end="\n\n",
        )

        # Get the top consuming syscalls
        wdf = df

        wdf = wdf.groupby(by=["name"]).sum(numeric_only=True)

        top_syscalls_df = wdf.sort_values(by=rapl_domains, ascending=False).head(
            n=syscall_num
        )
        top_syscalls = top_syscalls_df.index.to_list()

        # Keep in the list only the top consuming syscalls
        df = df[df["name"].isin(top_syscalls) == True]
        df = df.reset_index().drop(columns="index")

        df = df.groupby("name").sum(numeric_only=True)

        # Scale the RAPL values to milijoules
        # FIXME: Should work with different scaling as well.
        for domain in rapl_domains:
            df[domain] = df[domain] / 10**6

        info_syscall = []
        info_syscall_headers = ["system call"]
        for domain in rapl_domains:
            info_syscall_headers.append(f"{domain} [mJ]")
        for name, row in df.iterrows():
            table_row = [name]
            for domain in rapl_domains:
                table_row.append(row[domain])
            info_syscall.append(table_row)
        print(
            "# Top consuming system calls:\n"
            + tabulate(
                info_syscall,
                headers=info_syscall_headers,
                tablefmt="plain",
                floatfmt=",.3f",
            ),
            file=f,
        )

    if plot_rapl:
        _plot_rapl(data, output_dir, rapl_domains, syscall_num, sample_width)

    if plot_syscalls:
        _plot_syscall(data, output_dir, rapl_domains, syscall_num, sample_width)
