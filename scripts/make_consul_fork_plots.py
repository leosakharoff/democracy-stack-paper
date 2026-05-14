"""Plot Consul fork divergence and activity.

Reads data/consul_forks_compare.json. Produces:

- figures/consul_fork_activity.pdf:
    Last-push-date histogram. Tells the abandoned-vs-active story.

- figures/consul_fork_divergence.pdf:
    Scatter of ahead_by vs behind_by on log axes. Each fork is one
    point. Identifies four regimes:
      - in-sync forks (origin),
      - upstream-tracking forks (low ahead, high behind),
      - deeply diverged forks (high ahead, high behind),
      - unmodified forks (ahead=0, behind=0 or behind small).
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
DATA_CONSUL = ROOT / "data" / "consul_forks_compare.json"
DATA_DECIDIM = ROOT / "data" / "decidim_forks_compare.json"
FIGS = ROOT / "figures"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    "pdf.fonttype": 42,
    "axes.spines.top": False,
    "axes.spines.right": False,
})


def parse_iso(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def plot_activity(records: list[dict], out: Path):
    """Histogram of forks by year of last push."""
    pushed_years = []
    for r in records:
        if r.get("pushed_at"):
            try:
                pushed_years.append(parse_iso(r["pushed_at"]).year)
            except ValueError:
                pass

    if not pushed_years:
        print("no pushed_at data, skipping activity plot")
        return

    years = sorted(set(pushed_years))
    counts = [pushed_years.count(y) for y in years]

    fig, ax = plt.subplots(figsize=(7.5, 3.2))
    ax.bar(years, counts, width=0.8, color="#dd8452", edgecolor="white",
           linewidth=0.6)

    for x, c in zip(years, counts):
        if c >= 25:
            ax.text(x, c + max(counts) * 0.02, str(c), ha="center",
                    fontsize=7.5, color="0.3")

    ax.set_xlabel("Year of last push", fontsize=9, labelpad=8)
    ax.set_ylabel("Forks", fontsize=9)
    ax.set_xticks(years)
    ax.tick_params(axis="x", labelsize=8, rotation=0)
    ax.tick_params(axis="y", labelsize=8)
    ax.grid(axis="y", linestyle=":", color="0.85", linewidth=0.6)
    ax.set_axisbelow(True)

    total = len(pushed_years)
    recent_cutoff = max(pushed_years) - 2
    recent = sum(1 for y in pushed_years if y >= recent_cutoff)
    ax.text(0.98, 0.98,
            f"{total:,} forks total · {recent} pushed in last 3 years "
            f"({recent / total:.0%})",
            fontsize=8, color="0.3",
            ha="right", va="top", transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig(out, bbox_inches="tight", pad_inches=0.15)
    print(f"wrote {out}")


# Diagnostic standard axes for fork-divergence shape: one log decade
# above the largest observed civic-tech fork (Madrid/Consul, 12,725 ahead).
# Fixing the axes makes plots from different platforms directly comparable
# and the diagnostic itself reproducible.
DIAGNOSTIC_XMAX = 30_000
DIAGNOSTIC_YMAX = 30_000


def plot_divergence(records: list[dict], out: Path, *,
                    highlight_substring: str,
                    highlight_label_template: str,
                    annotation_xytext: tuple,
                    annotation_rad: float = -0.25,
                    diverged_word: str = "diverged silos",
                    behind_only_word: str = "dormant copies",
                    xmax: float = DIAGNOSTIC_XMAX,
                    ymax: float = DIAGNOSTIC_YMAX):
    """Scatter ahead vs behind on log axes, with quadrant storytelling."""
    from matplotlib.patches import Rectangle

    ok = [r for r in records if "ahead_by" in r and "behind_by" in r]
    if not ok:
        print("no compare data, skipping divergence plot")
        return

    # Quadrant counts (used in the labels)
    n_ahead_only = sum(1 for r in ok if r["ahead_by"] > 0 and r["behind_by"] == 0)
    n_diverged = sum(1 for r in ok if r["ahead_by"] > 0 and r["behind_by"] > 0)
    n_in_sync = sum(1 for r in ok if r["ahead_by"] == 0 and r["behind_by"] == 0)
    n_behind_only = sum(1 for r in ok if r["ahead_by"] == 0 and r["behind_by"] > 0)

    aheads = np.array([r["ahead_by"] for r in ok])
    behinds = np.array([r["behind_by"] for r in ok])

    fig, ax = plt.subplots(figsize=(8.6, 6.0))

    # Replace 0s with 0.5 for log display.
    plot_ahead = np.where(aheads > 0, aheads, 0.5)
    plot_behind = np.where(behinds > 0, behinds, 0.5)

    xmin = ymin = 0.3
    # xmax / ymax come from the function arguments (fixed diagnostic axes)

    # --- Quadrant background tints ----------------------------------------
    quadrants = [
        # (x0, y0, x1, y1, facecolor)
        (xmin, 1,    1,    ymax, "#d8ecd8"),   # ahead-only  (healthy, top-left)
        (1,    1,    xmax, ymax, "#f5d9dc"),   # ahead-and-behind  (silos, top-right)
        (xmin, ymin, 1,    1,    "#e9ecef"),   # in-sync  (bottom-left)
        (1,    ymin, xmax, 1,    "#fbeacc"),   # behind-only  (dormant, bottom-right)
    ]
    for x0, y0, x1, y1, color in quadrants:
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0,
                               facecolor=color, alpha=0.55,
                               edgecolor="none", zorder=0))

    # Quadrant dividers
    ax.axhline(1, color="0.45", linestyle="--", linewidth=0.7, zorder=1)
    ax.axvline(1, color="0.45", linestyle="--", linewidth=0.7, zorder=1)

    # --- Scatter ----------------------------------------------------------
    is_active = np.array([
        bool(r.get("pushed_at")) and parse_iso(r["pushed_at"]) >=
        datetime(2024, 1, 1, tzinfo=timezone.utc)
        for r in ok
    ])

    ax.scatter(plot_behind[~is_active], plot_ahead[~is_active],
               s=20, color="#555555", alpha=0.45, edgecolor="none",
               label="pushed before 2024", zorder=2)
    ax.scatter(plot_behind[is_active], plot_ahead[is_active],
               s=32, color="#c44e52", alpha=0.8, edgecolor="white",
               linewidth=0.5, label="pushed 2024+", zorder=3)

    ax.set_xscale("symlog", linthresh=1)
    ax.set_yscale("symlog", linthresh=1)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    # --- Quadrant labels (small boxes anchored top-left of each quadrant) -
    def quad_label(x, y, text, color="0.18"):
        ax.text(x, y, text,
                fontsize=7, color=color, ha="left", va="top",
                linespacing=1.45,
                bbox=dict(boxstyle="round,pad=0.32", fc="white",
                          ec="0.7", lw=0.5, alpha=0.94),
                zorder=4)

    fork_word = lambda n: "fork" if n == 1 else "forks"
    quad_label(0.36, ymax * 0.65,
               f"AHEAD-ONLY\n{n_ahead_only} {fork_word(n_ahead_only)}",
               color="#1f5d2e")
    quad_label(1.35, ymax * 0.65,
               f"AHEAD-AND-BEHIND\n{n_diverged} {diverged_word}",
               color="#7a1e23")
    quad_label(0.36, 0.93,
               f"IN-SYNC\n{n_in_sync} {fork_word(n_in_sync)}",
               color="0.35")
    quad_label(1.35, 0.93,
               f"BEHIND-ONLY\n{n_behind_only} {behind_only_word}",
               color="#7a5a1e")

    # --- Highlight annotation --------------------------------------------
    highlight = next((r for r in ok
                      if highlight_substring in r.get("full_name", "")),
                     None)
    if highlight:
        # Map zero counts to the 0.5 placeholder used for log display.
        ax_y = highlight["ahead_by"] if highlight["ahead_by"] > 0 else 0.5
        ax_x = highlight["behind_by"] if highlight["behind_by"] > 0 else 0.5
        ax.annotate(
            highlight_label_template.format(
                ahead=highlight["ahead_by"],
                behind=highlight["behind_by"],
            ),
            xy=(ax_x, ax_y),
            xytext=annotation_xytext,
            fontsize=7.5, color="0.15",
            ha="left", va="center",
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="0.65",
                      lw=0.6, alpha=0.92),
            arrowprops=dict(arrowstyle="->", color="0.35", lw=0.7,
                            connectionstyle=f"arc3,rad={annotation_rad}"),
            zorder=5,
        )

    # --- Axis cosmetics ---------------------------------------------------
    ax.set_xlabel("Behind upstream  (commits)", fontsize=9, labelpad=8)
    ax.set_ylabel("Ahead of upstream  (commits)", fontsize=9, labelpad=8)
    ax.tick_params(labelsize=8)
    ax.grid(linestyle=":", color="0.8", linewidth=0.35, zorder=0.5)
    ax.set_axisbelow(True)

    # --- Activity legend (outside the plot, below the x-axis) ------------
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13),
              ncol=2, frameon=False, fontsize=8, handletextpad=0.5,
              columnspacing=1.5)

    plt.tight_layout()
    plt.savefig(out, bbox_inches="tight", pad_inches=0.15)
    print(f"wrote {out}")


def main():
    # --- Consul ---
    consul = json.loads(DATA_CONSUL.read_text())["results"]
    print(f"loaded {len(consul)} Consul fork records")
    plot_activity(consul, FIGS / "consul_fork_activity.pdf")
    plot_divergence(
        consul, FIGS / "consul_fork_divergence.pdf",
        highlight_substring="AyuntamientoMadrid",
        highlight_label_template=("Madrid (Consul originator)\n"
                                  "{ahead:,} ahead · {behind:,} behind"),
        annotation_xytext=(120, 250),
        annotation_rad=-0.25,
        diverged_word="diverged silos",
        behind_only_word="dormant copies",
    )

    # --- Decidim ---
    if DATA_DECIDIM.exists():
        decidim = json.loads(DATA_DECIDIM.read_text())["results"]
        print(f"loaded {len(decidim)} Decidim fork records")
        plot_divergence(
            decidim, FIGS / "decidim_fork_divergence.pdf",
            highlight_substring="AjuntamentdeBarcelona",
            highlight_label_template=("Barcelona (Decidim originator)\n"
                                      "{ahead:,} ahead · {behind:,} behind"),
            annotation_xytext=(3, 12),
            annotation_rad=0.3,
            diverged_word="diverged forks",
            behind_only_word="dormant or learner copies",
        )


if __name__ == "__main__":
    main()
