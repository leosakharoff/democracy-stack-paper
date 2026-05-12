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
DATA = ROOT / "data" / "consul_forks_compare.json"
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
    ax.text(0.02, 0.98,
            f"{total:,} forks total · {recent} pushed in last 3 years "
            f"({recent / total:.0%})",
            fontsize=8, color="0.3",
            ha="left", va="top", transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig(out, bbox_inches="tight", pad_inches=0.15)
    print(f"wrote {out}")


def plot_divergence(records: list[dict], out: Path):
    """Scatter ahead vs behind on log axes."""
    ok = [r for r in records if "ahead_by" in r and "behind_by" in r]
    if not ok:
        print("no compare data, skipping divergence plot")
        return

    aheads = np.array([r["ahead_by"] for r in ok])
    behinds = np.array([r["behind_by"] for r in ok])

    fig, ax = plt.subplots(figsize=(7.5, 5.5))

    # Replace 0s with 0.5 for log display, but mark them visually distinct.
    plot_ahead = np.where(aheads > 0, aheads, 0.5)
    plot_behind = np.where(behinds > 0, behinds, 0.5)

    # Mark each fork by category for colour
    is_active = np.array([
        bool(r.get("pushed_at")) and parse_iso(r["pushed_at"]) >=
        datetime(2024, 1, 1, tzinfo=timezone.utc)
        for r in ok
    ])

    ax.scatter(plot_behind[~is_active], plot_ahead[~is_active],
               s=20, color="#888888", alpha=0.35, edgecolor="none",
               label="pushed before 2024 (dormant)")
    ax.scatter(plot_behind[is_active], plot_ahead[is_active],
               s=30, color="#c44e52", alpha=0.7, edgecolor="white",
               linewidth=0.5, label="pushed 2024+")

    ax.set_xscale("symlog", linthresh=1)
    ax.set_yscale("symlog", linthresh=1)
    ax.set_xlim(0.3, plot_behind.max() * 1.5)
    ax.set_ylim(0.3, plot_ahead.max() * 1.8)

    # Reference lines marking the "modified vs unmodified" boundary
    ax.axhline(1, color="0.7", linestyle=":", linewidth=0.8)
    ax.text(0.4, 1.15, "ahead ≥ 1 (modified)", fontsize=7, color="0.5",
            ha="left", va="bottom", style="italic")
    ax.text(0.4, 0.85, "unmodified", fontsize=7, color="0.5",
            ha="left", va="top", style="italic")

    ax.set_xlabel("Behind upstream  (commits)", fontsize=9, labelpad=8)
    ax.set_ylabel("Ahead of upstream  (commits)", fontsize=9, labelpad=8)
    ax.tick_params(labelsize=8)
    ax.legend(loc="upper left", frameon=False, fontsize=8.5,
              bbox_to_anchor=(0.02, 0.98))
    ax.grid(linestyle=":", color="0.93", linewidth=0.6)
    ax.set_axisbelow(True)

    # Stats banner
    total = len(ok)
    unmodified = sum(1 for r in ok if r["ahead_by"] == 0)
    diverged = sum(1 for r in ok if r["ahead_by"] > 0 and r["behind_by"] > 0)
    ahead_only = sum(1 for r in ok if r["ahead_by"] > 0 and r["behind_by"] == 0)
    in_sync = sum(1 for r in ok if r["ahead_by"] == 0 and r["behind_by"] == 0)

    msg = (
        f"{total:,} forks · "
        f"unmodified: {unmodified} ({unmodified/total:.0%}) · "
        f"in sync: {in_sync} · "
        f"ahead-only: {ahead_only} · "
        f"diverged: {diverged} ({diverged/total:.0%})"
    )
    ax.set_title(msg, fontsize=9, pad=10, color="0.3", loc="left")

    plt.tight_layout()
    plt.savefig(out, bbox_inches="tight", pad_inches=0.15)
    print(f"wrote {out}")


def main():
    data = json.loads(DATA.read_text())
    records = data["results"]
    print(f"loaded {len(records)} fork records")

    plot_activity(records, FIGS / "consul_fork_activity.pdf")
    plot_divergence(records, FIGS / "consul_fork_divergence.pdf")


if __name__ == "__main__":
    main()
