"""Generate tensions.pdf — positioning map of Decidim, Consul, Polis on
modifiability x algorithmic depth. Used as Figure 1 in main.tex (Section 2.1).

Writes tensions.pdf next to this script regardless of CWD."""

from pathlib import Path

import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent / "tensions.pdf"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    "pdf.fonttype": 42,
})

fig, ax = plt.subplots(figsize=(7.2, 4.6))

# --- Trade-off frontier (subtle dashed diagonal: depth costs modifiability) ---
ax.plot([0.08, 0.92], [0.92, 0.08],
        linestyle=(0, (4, 4)), color="black", alpha=0.18, linewidth=1.2, zorder=1)
ax.text(0.62, 0.42, "trade-off frontier",
        fontsize=8.5, color="black", alpha=0.45, style="italic",
        ha="left", va="bottom", rotation=-30)

# --- Platforms ---
# Positions on (modifiability, algorithmic depth):
#   Decidim — modular, algorithmically shallow → high modifiability, low depth (bottom-right)
#   Polis   — monolithic, algorithmically deep → low modifiability, high depth (top-left)
#   Consul  — monolithic, algorithmically shallow → low on both (bottom-left, dominated)
platforms = [
    ("Polis",   0.20, 0.85,
     ["PCA + k-means at the core",
      "no extension model"], "right"),
    ("Decidim", 0.85, 0.20,
     ["27 Rails engines",
      "80+ community modules"], "left"),
    ("Consul",  0.22, 0.20,
     ["monolithic Rails app",
      "fork to customise",
      "280 modified forks of 1,030"], "right"),
]

for name, x, y, desc_lines, pos in platforms:
    # Dot
    ax.scatter([x], [y], s=180, color="black", zorder=4,
               edgecolor="white", linewidth=1.5)

    if pos == "right":
        tx, ha = x + 0.035, "left"
    else:
        tx, ha = x - 0.035, "right"

    # Bold platform name, vertically centered with dot
    ax.annotate(name, xy=(tx, y), fontsize=13, fontweight="bold",
                ha=ha, va="center", zorder=5)

    # Descriptor block, sitting just below the label
    desc = "\n".join(desc_lines)
    ax.annotate(desc, xy=(tx, y - 0.045), fontsize=9, color="0.32",
                ha=ha, va="top", linespacing=1.4, zorder=5)

# --- Axis labels ---
ax.set_xlabel("Modifiability  →", fontsize=11, labelpad=10, color="0.2")
ax.set_ylabel("Algorithmic depth  →", fontsize=11, labelpad=10, color="0.2")

# --- Frame ---
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
for spine in ("left", "bottom"):
    ax.spines[spine].set_color("0.5")
    ax.spines[spine].set_linewidth(0.8)

plt.tight_layout()
plt.savefig(OUT, bbox_inches="tight", pad_inches=0.15)
print(f"Wrote {OUT}")
