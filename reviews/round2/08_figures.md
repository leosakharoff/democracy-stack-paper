# Round 2 figure review

## 1. Verdict

Seven figures resolve in the build; two PDFs sit unused in `figures/`. Most of the new empirical figures earn their place and tell their part of the story. The biggest problems are (a) the `tensions.pdf` figure still carries pre-empirical-rework numbers that contradict the current prose, (b) the `fig:consul-forks` caption and surrounding prose misread the x-axis as fork-creation year when the data is year of last push, and (c) two real empirical figures — Decidim per-engine activity and the Consul ahead/behind scatter — were generated and never wired into the paper, leaving claims in the prose ungrounded that the figures would back. Captions are uneven: some carry the takeaway (commit timeline, coupling), others act as labels (contributor concentration is thin; engine matrix punts to a citation).

## 2. Per-figure audit

### Fig. tradeoffs (`figures/tensions.pdf`, line 138)
- **Caption standalone:** Partial. Names the axes and explains why those two attributes were chosen, mentions Consul-inside-frontier. OK as standalone.
- **Prose match:** Yes for placement, no for the labels in the image.
- **Legibility:** Fine. Clean SVG.
- **Fidelity:** *Two stale numbers contradict the current paper*. Image says "23 Rails engines" — the paper now says 27 first-party / 24 user-facing engines after Session 1 recovery. Image says "~250 diverging forks" — the paper now says 280 modified out of 1,030 enumerable, after Session 4. The Polis label "no extension model" is fine. These are pre-empirical-rework numbers that the figure source was not updated to match.
- **Recommendation:** **Improve.** Re-render `make_tensions.py` with `27 Rails engines`, `80+ community modules` (already correct), and `280 modified forks / 1,030 total`. Or drop the numbers and keep only the architectural-style labels — the figure is a positioning sketch, not an empirical scoreboard.

### Fig. dependency (`figures/decidim_dependency_graph.pdf`, line 211)
- **Caption standalone:** Yes. Names the snapshot SHA and date, explains the grey bar, names the dashed-arrow encoding, lists the two heaviest cross-engine hubs, says what was omitted.
- **Prose match:** Yes — line 209 lists the same hubs and dependents that the graph encodes.
- **Legibility:** OK. Coloured dashed arrows cluster on `comments` and `forms` clearly. The blue (admin) arrows are easier to miss than the orange/red ones.
- **Fidelity:** Matches Session 1 log exactly (`be39c244`, 27 engines, three dev-tooling omitted, 6 / 5 / 3 dependent counts).
- **Recommendation:** **Keep.** Strongest empirical figure in the paper.

### Fig. matrix (`fig:matrix`, lines 224–245)
- **Caption standalone:** Marginal. Names the encoding ("$N \times M$ combinatorial architecture", polymorphic association) but the "Adapted from Barandiaran 2024 Fig. 3.1" gives no defensible source for the filled-vs-empty circle pattern. Reader cannot tell whether "commonly activated" was empirically measured or asserted.
- **Prose match:** OK in concept — line 219 makes the composition argument.
- **Legibility:** Fine, but the legend uses italic text inside the caption block that floats.
- **Fidelity:** The composition pattern is real (confirmed by Session 1). The filled/empty distinction in the cells is not backed by any data the paper computes; it is inherited from Barandiaran.
- **Recommendation:** **Improve or cut.** This is largely decorative — the prose at line 219 already says "almost any component can attach to almost any space". The four-row, seven-cell illustration adds little. If kept, the caption should be honest that the filled/empty pattern is from the Decidim handbook, not empirically measured here.

### Fig. coupling (`figures/decidim_coupling.pdf`, line 281)
- **Caption standalone:** Yes. Names the metric (Jaccard), the snapshot, the central finding (spaces co-change, shared services stay isolated).
- **Prose match:** Yes — line 279 walks through the three patterns the heatmap shows (spaces block, flagship components, shared-service isolation) with the exact numbers (0.43, 0.11–0.20, <0.06).
- **Legibility:** Good. Block-grouping labels on the right (CORE / INFRA / SHARED / SPACES / COMPONENTS) and the colour ramp work. The triangle-only display avoids duplication.
- **Fidelity:** Matches Session 3 log: 7,078 commits, 64% single-engine, the exact pair values from the table.
- **Recommendation:** **Keep.** Argumentative weight is high — this figure is the empirical backing for the "modularity at API boundaries, not implementation" claim.

### Fig. consul-forks (`figures/consul_fork_activity.pdf`, line 315)
- **Caption standalone:** Marginal. Names the snapshot and the 14% number but does not state what an "active" fork means here or distinguish "last push" from "creation".
- **Prose match:** **No — direct misreading.** Line 313 says "Fork-creation peaked in 2019". The figure x-axis is *year of last push*, not year of fork creation. A fork created in 2017 and last pushed in 2019 contributes to the 2019 bar. Session 4 log correctly calls this "fork activity peaked in 2019"; the paper miscopied. The story (activity peaks 2019, decays) is still true; the specific "fork-creation peaked" claim is unsupported by this figure.
- **Legibility:** Fine. The "1,030 forks total · 149 pushed in last 3 years (14%)" annotation is helpful.
- **Fidelity:** Bar values match Session 4 log exactly.
- **Recommendation:** **Improve.** Edit line 313 to "Fork activity peaked in 2019" or "the latest push for most forks falls in 2018–2019". Tighten the caption to define what each bar counts.

### Fig. contributor-concentration (`figures/contributor_concentration.pdf`, line 376)
- **Caption standalone:** Thin. States that Decidim has the longest tail and Polis is dominated by a single developer, but does not state what the dark / mid / light segments encode (top-3 / next-7 / rest). The reader has to infer.
- **Prose match:** Yes — line 374 quotes the same percentages the bars show.
- **Legibility:** Good. Greyscale segmentation is print-safe.
- **Fidelity:** Matches Session 2 log (36/52/82 top-3; 68/87/97 top-10; 183/186/79 authors; Gini 0.85/0.93/0.94).
- **Recommendation:** **Improve.** Caption should spell out the three segments and the Gini metric.

### Fig. commit-timeline (`figures/commit_timeline.pdf`, line 386)
- **Caption standalone:** Yes. Names the three patterns and flags the partial 2026 cut-off.
- **Prose match:** Yes — line 384 walks through each line with peak/trough numbers that match the curve (Consul ~2,700–2,800 in 2017, Decidim 600–770 plateau, Polis 50–340 with 2025 burst).
- **Legibility:** Good. Three-line plot, clear colours, legend in-figure.
- **Fidelity:** Matches Session 2 log. The "drops 80%" prose at line 384 is from peak-to-2020 not 2019-to-2020 — minor but worth noting; the figure itself is correct.
- **Recommendation:** **Keep.** Pulls the most argumentative weight after the dependency graph — the Consul 2019 cliff *as a visible artefact* is the empirical anchor for the architecture-as-governance story.

## 3. Missing figures

- **None of the prose claims are missing a figure they obviously need.** But two real empirical figures live in `figures/` and never appear in the paper:
  - `figures/decidim_engine_activity.pdf` — bar chart of last-12-months commits per Decidim engine, with all-time totals. Session 2 generated it specifically to back the "modularity is matched by modular maintenance" claim at line 295 ("All 24 user-facing engines see commits in the last 12 months, including three recently added engines"). The paper currently asserts this in prose with no figure. **Wire it in** after line 295 or in the synthesis section.
  - `figures/consul_fork_divergence.pdf` — ahead-vs-behind scatter on log-log axes, separating dormant from 2024+ forks. This is the figure that visually backs the "diverged quadrant populated, ahead-only quadrant empty" claim from Session 4. The paper currently uses `fig:consul-forks` (the histogram) alone and asserts the divergence pattern in text at line 309. **Either replace** `fig:consul-forks` with the scatter (more information-dense; carries the ahead/behind story directly) or **add it as a second figure** alongside the histogram.

## 4. Decorative figures

- **`fig:matrix`** is the one figure where the prose already conveys the claim and the diagram does not add evidence on top of it. The filled/empty pattern is from a secondary source rather than from this paper's empirical work. Either repurpose with empirical fill-rate data (would require querying real Decidim deployments — out of scope) or drop in favour of a sentence about combinatorial composition.

## 5. Prioritised fix list

1. **Fix the prose at line 313**: change "Fork-creation peaked in 2019" to "Fork activity peaked in 2019" (or "Most forks were last pushed in 2018–2019"). This is a factual misreading of the x-axis.
2. **Update `tensions.pdf`** to current numbers: 27 engines (not 23), 280 modified forks of 1,030 total (not ~250). Re-run `figures/make_tensions.py`.
3. **Wire in `decidim_engine_activity.pdf`** after line 295 in Section 4.1 to back the "all 24 user-facing engines see commits in the last 12 months" claim with the actual bar chart.
4. **Wire in `consul_fork_divergence.pdf`** in Section 4.2 — either replacing `consul_fork_activity.pdf` or alongside it. The scatter is the stronger single figure for the "diverged but not contributing upstream" claim.
5. **Tighten the `fig:contributor-concentration` caption** to name what the three bar segments encode and the Gini value.
6. **Tighten the `fig:consul-forks` caption** to define what each bar counts (year of last push to that fork's default branch).
7. **Decide on `fig:matrix`** — keep with an honest caption (encoding is from Barandiaran handbook, not measured here) or cut in favour of prose.
