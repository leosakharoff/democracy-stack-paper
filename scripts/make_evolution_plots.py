"""Render evolution plots from data/evolutionary.json.

Outputs:
- figures/contributor_concentration.pdf
- figures/commit_timeline.pdf
- figures/decidim_engine_activity.pdf
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "evolutionary.json"
FIGS = ROOT / "figures"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    "pdf.fonttype": 42,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

PLATFORM_ORDER = ["decidim", "consul", "polis"]
PLATFORM_LABELS = {"decidim": "Decidim", "consul": "Consul", "polis": "Polis"}
PLATFORM_COLOURS = {
    "decidim": "#4c72b0",
    "consul":  "#dd8452",
    "polis":   "#8172b3",
}


def short_sha(s: str) -> str:
    return s[:10]


def plot_concentration(data: dict, out: Path) -> None:
    """Stacked horizontal bar: top-3 / top-4-10 / rest, per repo."""
    fig, ax = plt.subplots(figsize=(7, 2.8))

    rows = []
    for key in PLATFORM_ORDER:
        r = data[key]
        top3 = r["top3_share"]
        top10 = r["top10_share"]
        top10_minus_top3 = top10 - top3
        rest = 1 - top10
        rows.append({
            "label": PLATFORM_LABELS[key],
            "top3": top3,
            "top4_10": top10_minus_top3,
            "rest": rest,
            "humans": r["unique_human_authors"],
            "gini": r["gini"],
        })

    y_positions = np.arange(len(rows))
    height = 0.5

    for i, row in enumerate(rows):
        # top3
        ax.barh(i, row["top3"], height=height, left=0,
                color="#404040", edgecolor="white", linewidth=0.6)
        # top4..10
        ax.barh(i, row["top4_10"], height=height, left=row["top3"],
                color="#888", edgecolor="white", linewidth=0.6)
        # rest (everyone else)
        ax.barh(i, row["rest"], height=height,
                left=row["top3"] + row["top4_10"],
                color="#dfdfdf", edgecolor="white", linewidth=0.6)

        # right-hand annotation
        ax.text(1.02, i,
                f"  {row['humans']} authors · Gini {row['gini']:.2f}",
                fontsize=8.5, color="0.35", va="center", ha="left")

        # in-bar labels for top3 and top10
        ax.text(row["top3"] / 2, i, f"top 3: {row['top3']:.0%}",
                fontsize=7.5, color="white", ha="center", va="center")
        if row["top4_10"] > 0.05:
            ax.text(row["top3"] + row["top4_10"] / 2, i,
                    f"next 7: {row['top4_10']:.0%}",
                    fontsize=7.5, color="white", ha="center", va="center")

    ax.set_yticks(y_positions)
    ax.set_yticklabels([r["label"] for r in rows], fontsize=10, fontweight="bold")
    ax.invert_yaxis()
    ax.set_xlim(0, 1)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"], fontsize=8)
    ax.set_xlabel("Share of human commits", fontsize=9, labelpad=8)
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)

    plt.tight_layout()
    plt.savefig(out, bbox_inches="tight", pad_inches=0.15)
    print(f"wrote {out}")


def plot_timeline(data: dict, out: Path) -> None:
    """Commits per year, one line per repo."""
    fig, ax = plt.subplots(figsize=(7.5, 3.6))

    # Build common year axis
    years = set()
    for key in PLATFORM_ORDER:
        years.update(int(y) for y in data[key]["commits_per_year"])
    years = sorted(years)

    for key in PLATFORM_ORDER:
        cpy = data[key]["commits_per_year"]
        ys = [cpy.get(str(y), 0) for y in years]
        ax.plot(years, ys, marker="o", markersize=4.5,
                color=PLATFORM_COLOURS[key], linewidth=1.6,
                label=PLATFORM_LABELS[key])

    ax.set_xlabel("Year", fontsize=9)
    ax.set_ylabel("Human commits per year (no merges)", fontsize=9)
    ax.set_xticks(years)
    ax.tick_params(axis="x", labelsize=8, rotation=0)
    ax.tick_params(axis="y", labelsize=8)
    ax.grid(axis="y", linestyle=":", color="0.85", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, fontsize=9, loc="upper right")

    ax.text(0.99, -0.18,
            "2026 is partial (cut-off at clone date, May 2026)",
            fontsize=7, color="0.5", style="italic",
            ha="right", va="top", transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig(out, bbox_inches="tight", pad_inches=0.15)
    print(f"wrote {out}")


def plot_decidim_per_engine(data: dict, out: Path) -> None:
    """Horizontal bar: last 12mo commits per Decidim engine."""
    per_engine = data["decidim"]["per_engine"]["recent_12mo_commits_per_engine"]
    all_time = data["decidim"]["per_engine"]["all_time_commits_per_engine"]
    cutoff = data["decidim"]["per_engine"]["recent_cutoff"]

    # Skip dev-only engines for the figure (consistent with Figure 2)
    skip = {"decidim-design", "decidim-dev", "decidim-generators"}
    items = [(eng, c) for eng, c in per_engine.items() if eng not in skip]
    items.sort(key=lambda x: x[1], reverse=True)

    labels = [eng.replace("decidim-", "").replace("participatory_processes", "processes")
              for eng, _ in items]
    values = [c for _, c in items]
    totals = [all_time[eng] for eng, _ in items]

    fig, ax = plt.subplots(figsize=(7.5, 5.4))
    y = np.arange(len(items))
    bars = ax.barh(y, values, height=0.7, color="#4c72b0",
                   edgecolor="white", linewidth=0.5)

    # annotations: total commits to the right of each bar
    max_v = max(values) if values else 1
    for i, (v, total) in enumerate(zip(values, totals)):
        ax.text(v + max_v * 0.012, i, f"  ({total:,} all-time)",
                fontsize=7.5, color="0.45", va="center")

    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8.5)
    ax.invert_yaxis()
    ax.set_xlabel(f"Commits since {cutoff} (no merges)", fontsize=9, labelpad=8)
    ax.tick_params(axis="x", labelsize=8)
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.grid(axis="x", linestyle=":", color="0.85", linewidth=0.6)
    ax.set_axisbelow(True)
    # Add right margin for annotations
    ax.set_xlim(0, max_v * 1.35)

    plt.tight_layout()
    plt.savefig(out, bbox_inches="tight", pad_inches=0.15)
    print(f"wrote {out}")


def main():
    data = json.loads(DATA.read_text())
    plot_concentration(data, FIGS / "contributor_concentration.pdf")
    plot_timeline(data, FIGS / "commit_timeline.pdf")
    plot_decidim_per_engine(data, FIGS / "decidim_engine_activity.pdf")


if __name__ == "__main__":
    main()
