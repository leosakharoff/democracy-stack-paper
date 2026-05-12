# Plan — strengthening the paper

Working document. Living. Add to the decision log as we go; mark tasks done.

## Where we are

The paper is drafted. Two agent reviews (`03_method.md` plus a later overall review pasted into chat) landed on the same weakness from different angles: the method is too thin to support the analytical claims, and the analysis is asymmetric — Decidim is genuinely recovered, Consul and Polis are paraphrased from grey literature. Trade-offs read as pre-decided categories rather than findings. The shared-DB tension contradicts the modular-monolith framing and gets one sentence.

Supervisor is Konstantinos Manikas. SECO is his focus, not architecture recovery (Mircea Lungu's four-lecture arc on recovery is adjacent training, not the centre of gravity for this paper).

## Strategy

Empirical work is cheap with pair work — clone, `git log`, parse, plot. Most of the perceived "expensive" items are an afternoon's scripting.

Plan: run all five empirical sessions below. See what the data says. Keep what tells a story, drop what doesn't. We're not committing to publishing every result — we're committing to looking. Filter-after-running.

The supervisor's slide deck (three structures + health + Iansiti roles + interaction types + decision-making) is reference, not template. Use sub-dimensions where they sharpen the analysis. Skip business-model-canvas-on-civic-tech and similar force-fits.

Architecture-recovery course material gets cited only where it directly frames what we did — Gall 1998 if we do logical coupling, Symphony in one sentence if it helps. No anchoring the whole paper there.

## Diagnosed problems (consolidated)

Method section:

- 17 lines, too thin. Names vocabulary but not procedure.
- No case-selection criteria. Why these three, not Loomio / CitizenLab / vTaiwan / Demos.
- No snapshot SHAs or access dates.
- Recovery procedure hand-waved (lists inputs, not steps).
- Method promises "contributor distribution, fork activity, module-level commit patterns". Analysis delivers approximate star/fork counts.
- No methodological tradition cited (this is fine — we're not adding Yin etc.).

Analysis section:

- Decidim is genuinely recovered (engines, gemspec, registry, listing). Real work.
- Consul = two grey-literature reports paraphrased. No code-level recovery, no repo pointers for structural claims.
- Polis = half a page. The FAccT 2025 paper that method promises is missing from `references.bib`.
- Shared-DB finding (l. 298) contradicts "modular monolith" framing and gets dropped in one sentence.

Trade-offs framing:

- Appear in abstract, background, synthesis, discussion, conclusion as findings.
- Also the lenses the cases were sorted into.
- Abstract version doesn't match synthesis table version exactly.
- Read as pre-decided categories, not discoveries.

Concrete bugs:

- FAccT 2025 cite missing from `references.bib` despite being promised in method.
- Some title / voice tightenings already done — see decision log.

## Five empirical sessions

Goal of each session: data that either supports a claim the paper already makes, or surfaces a tension worth confronting. If the data turns out boring or contradicts the paper without enriching it, we drop the analysis and note the absence as a limitation.

### Session 1 — Decidim repo recovery (scripted)

~2–4 hours.

Steps:

1. Clone `decidim/decidim` at a fixed SHA. Record the SHA.
2. Parse all 23 `*.gemspec` files. Extract gem name, dependencies (`add_dependency` calls).
3. Parse `lib/decidim/*/engine.rb` files. Extract `Decidim.register_component` and `Decidim.register_participatory_space` calls.
4. Build a NetworkX dependency graph from the gemspec data.
5. Regenerate Figure 2 from real data, replacing the TikZ-asserted version.
6. Sanity-check: does every engine actually depend on `decidim-core`? Are there cross-engine dependencies that bypass core?

Outputs:

- `scripts/recover_decidim.py` (in repo)
- `figures/decidim_dependency_graph.pdf` (real graph)
- A short log of decisions: which files were read, what was logged, what surprised us
- This log becomes the recovery-procedure paragraph in the method section

What the data might say:

- All-clean hub-and-spoke → confirms the asserted architecture
- Cross-engine deps bypass core → drift evidence, write a paragraph
- Engine count differs from 23 → fact-check the paper

### Session 2 — Evolutionary analysis on three repos

~3–5 hours.

Steps:

1. Clone `decidim/decidim`, `consul/consul`, `compdemocracy/polis` at fixed SHAs.
2. For each repo, run `git log` analysis (PyDriller or plain shell):
   - Total commits, contributors, time range
   - Top-N contributor share (top 10 as % of total commits) — bus-factor proxy
   - Commits per year — is the project alive, declining, dead
3. For Decidim only: per-engine commit counts (`git log --follow decidim-*/`). Which engines are alive, which are dormant.
4. Plot: contributor concentration bar (one bar per repo, top-10 share); commit-timeline line plot; Decidim per-engine activity bar.

Outputs:

- `scripts/evolutionary_analysis.py`
- 2–3 plots saved to `figures/`
- New short subsection in Section 4 (ecosystem evolution / health) — ~half a page

What the data might say:

- Decidim concentration verifies Cobos2025's "activity concentrates on a few contributors" claim — or refines it
- Consul commit timeline shows whether the upstream is still maintained or effectively dead
- Decidim per-engine activity shows which spaces/components are alive (and might surface that some engines mentioned in the paper barely move)

### Session 3 — Logical coupling on Decidim (Gall 1998)

~2–3 hours.

Steps:

1. From Decidim git history, build a file-pair co-change matrix (pairs of files changed in the same commit).
2. Aggregate to engine pairs: which Decidim engines change together?
3. Threshold (e.g., engines that co-change in >X% of commits where either was changed).
4. Visualize as a heatmap or a coupling graph.

Outputs:

- `scripts/logical_coupling.py`
- One figure
- A paragraph that confronts the shared-DB tension empirically: if engines co-change above the threshold, the manifest pattern doesn't fully isolate them — and that's the modular-monolith tension made visible

What the data might say:

- High cross-engine co-change → modularity is partly an illusion at the development level; shared-DB tension is real and quantified
- Low co-change → modularity holds; isolated engines confirmed; shared DB is a coupling vector that hasn't materialised
Either result is publishable — both sharpen the paper.

### Session 4 — Consul fork divergence

~2–3 hours. Feasibility depends on GitHub API rate limits.

Steps:

1. Use GitHub API to list forks of `consul/consul`. Sample by recent activity.
2. For each sampled fork: clone, measure `git rev-list --count upstream..fork` (commits ahead) and `upstream..fork --count` (commits behind).
3. Aggregate: distribution of divergence, recency of last sync, evidence of contributions flowing back upstream.
4. Plot: divergence distribution, sync recency.

Outputs:

- `scripts/consul_fork_divergence.py`
- One figure
- Quantifies "~250 diverging forks" claim — turns it from assertion to data

What the data might say:

- High divergence + no upstream contributions → fragmentation story confirmed
- Surprisingly low divergence → claim needs softening

### Session 5 — Method section rewrite (write-up, no new code)

~3–4 hours. Depends on Sessions 1–4.

Steps:

1. Rewrite Section 3 (Method) to ~2 pages.
2. Include: case-selection criteria (eligibility, why these three, why not the others); recovery procedure (what we actually did in Session 1); evolutionary analysis procedure (what we did in Session 2); trade-off identification (specified up front, observed in cases); honest scope statement (Decidim deep, Consul-Polis lighter); snapshot SHAs; FAccT cite or removal.
3. Move "as of May 2026" out of Analysis and into Method, with SHAs.
4. Cite Gall 1998 if Session 3 produced anything publishable.
5. One sentence on Symphony / Ducasse if it helps frame the procedure — otherwise skip.

## Cross-cutting write-up tasks

These run alongside or after the empirical sessions.

- **Shared-DB tension as a paragraph**, not a sentence (Section 4.1). Backed by Session 3 data.
- **Trade-offs reframed** as "specified up front, observed in cases". Identical naming everywhere — abstract, background, synthesis table, discussion, conclusion. One pass through the doc.
- **Polis asymmetric depth** acknowledged up front in Method, not retroactively in §5.4.
- **Consul honest framing**: either we add the recovery work (not planned — too expensive) or we explicitly call Consul a literature-based comparison case. Pick the second. Update Method language.
- **SECO depth where it fits**:
  - Sharpen Iansiti role analysis per case (keystone / dominator / niche-creator) backed by Session 2 data
  - Add Manikas/Wnuk/Shollo 2015 on decision-making strategies if the comparison material is there
  - Three-structure table (`tab:threestructure`) deepened where empirical work gives us new material — not as a checklist
  - Skip business-model canvas, full SECO health tree, and other force-fits
- **FAccT 2025 cite** — find the actual paper, add to `references.bib`, or remove the reference from Method.

## Out of scope

Confirmed not doing:

- Full architecture recovery of Consul. Cheaper to do fork divergence (Session 4) and explicitly rebrand Consul as a literature-based foil.
- Doubling Polis. Half a page is fine — flag asymmetric depth up front.
- Yin / Stake / Eisenhardt formal case-study methodology citations.
- ATAM / SAAM as the trade-off identification method.
- Positionality statement.
- Replication package as a deliverable (the scripts themselves go in the repo, that's enough).
- Architecture-recovery course as primary framing. Use only where directly relevant (Gall, possibly one Symphony sentence).
- Konstantinos's slide-deck sub-dimensions applied as a checklist. Use only where they sharpen the analysis.

## Sequencing

Suggested order:

1. Session 1 (Decidim recovery) — foundational, feeds Method rewrite and Figure 2 replacement.
2. Session 2 (Evolutionary) — broadest data, supports multiple write-up tasks.
3. Session 3 (Logical coupling) — needs Session 2's clone of Decidim; produces the shared-DB paragraph material.
4. Session 4 (Consul forks) — independent, can run in parallel with anything else.
5. Session 5 (Method rewrite) — last, depends on everything else.

Cross-cutting write-ups happen as the corresponding empirical sessions complete.

## Open questions

- **Time horizon** — when's this due? Decides how aggressively to sequence. Default assumption: a few weeks.
- **GitHub API access** — Session 4 may hit rate limits. Confirm we have a token, or accept a smaller fork sample.

## Decision log

Newest at the top.

- **2026-05-12** — Plan written. Five empirical sessions chosen. Filter-after-running approach: run all, keep what tells a story.
- **2026-05-12** — Architecture-recovery course framing deprioritised. Supervisor is SECO-focused. Use Gall, possibly Symphony in one sentence, skip the rest.
- **2026-05-12** — Konstantinos's slide-deck framework treated as reference, not template. Apply where it sharpens analysis. No force-fit.
- **2026-05-12** — Consul will be rebranded as literature-based comparison foil (not recovered to Decidim's depth). Polis stays a short contrast with depth acknowledged up front.
- **2026-05-12** — Section 2 (Background) edits applied in this session: figure redesign + caption fix, paragraph 3 list dropped, voice tightenings, subsection titles plain.
