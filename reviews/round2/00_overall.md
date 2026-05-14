# Holistic review (round 2): Building the Democracy Stack

## Verdict

Round 2 is a real upgrade. The Method is no longer a 17-line liability — it is now eight paragraphs (~30 lines) that describe specific procedures producing specific artefacts. The Analysis is no longer a Decidim section with two thinner appendices; the new §4.4 Ecosystem Evolution makes the cross-case comparison empirical rather than rhetorical. Three of the four trade-offs are now demonstrated, not just asserted: contributor concentration (Polis vs. Decidim), fork divergence (Madrid 12,725 ahead), and intra-Decidim isolation (64% single-engine commits). The paper has earned its central claim in the case it cares most about.

What still doesn't work: the paper continues to load-bear on the Decidim/Consul refrain (11 sentences across abstract, intro, method, §4.2, §4.5, §5.1, §5.4, conclusion — see drift map below), and the four trade-off pairs still drift between abstract phrasing and the synthesis table. The Polis case is empirically strengthened on the contributor side but is still doing rhetorical work the architectural analysis cannot quite support — §4.3 is the shortest case section by a wide margin and the only one without a recovered diagram, yet §5.1 lifts a Bowker/Star reading that the §4.3 evidence does not by itself supply. The asymmetry that §3 and §5.4 honestly flag is real and the Polis treatment is the thinnest. The interoperability lens is still the weakest of the four — it is named in lists but never separately evidenced in the case sections; §4.5 still leans on "civic tech platforms otherwise as silos" with no measurement behind it. And the gap-claim has been narrowed in §2.2 (Manikas 2016 backs it for SECO) but the abstract still phrases it as the broader "SA or SECO methods" version.

Single most important fix: collapse the Decidim/Consul refrain. It now appears in essentially every front-matter section. After round 1 the author cut some instances, but most of the round-1 mentions still sit in place, and the round-2 Madrid 12,725 number has been added on top in three more places. Pick the two locations where it does the work — §4.2 fork paragraph and §5.1 — and let those two carry it.

## Lens 1 — Argument & rigor (paper-level)

**One paper or two?** Still one paper, more tightly woven than round 1. The empirical work in §4.4 and the logical-coupling result in §4.1 are the seam that now closes between the SA/SECO and the STS/governance halves. The Polis paragraph in §5.1 (Bowker/Star + PCA-as-classification) is the one place where the STS register does load-bearing analytical work, not just framing — that paragraph is in better shape than it was in round 1. The SECO half is still better-evidenced than the STS half, but the gap has narrowed.

**Does everything answer the same RQ?** The RQ on line 120 maps onto the conclusion on line 505. The abstract still overpromises against the conclusion: abstract says "the strongest evidence", conclusion says "the clearest demonstration", §4.5 says "the clearest evidence". Three flavours of the same superlative in three places. The "provides the kind of architectural analysis IDEA calls for" line in the intro (line 122) is the same overpromise round 1 flagged — it has not been pulled back; §5.3 ("our cases point to some concrete lessons", line 485) is the honest version, and the intro and conclusion should match that register.

**Thesis demonstrated or assumed?** Decidim/Consul is now genuinely demonstrated, with three independent pieces of evidence pointing in the same direction: contributor distribution (§4.4), commit timeline cliff (§4.4), and fork divergence (§4.2). Polis is partially demonstrated: §4.3 supplies the contributor-concentration finding (top-3 82%, Bjorkegren 56%) but the architecture-as-governance reading still hinges on the §5.1 PCA paragraph, which is a Bowker/Star point about classification rather than a finding about Polis specifically. §5.4 admits the Polis treatment is the thinnest — that admission is good, but it does not solve the §4.3-to-§5.1 gap. The paper does not show what specific democratic outcome differs in a Polis deployment because of the PCA choice — Heeks-style cases of the algorithm mis-aggregating opinion, the cluster boundaries silencing a minority position, deployer audit limitations. The §4.3 evidence is real and round-1 only had less. The §5.1 reach is the same as round 1.

**Madrid 12,725 audit.** New refrain to flag. Appears at: abstract (line 98), §4.2 narrative (line 311), §4.2 democratic consequence (line 349), §5.1 (line 467). Four times. It is doing different work each time (sharpening the abstract claim; introducing the fork-divergence finding; closing the Consul subsection; opening the governance-in-practice section), so the repetition is *acceptable* but at the upper limit. Cut the abstract mention or the §4.2 second mention — the number is the same number both times.

**Decidim/Consul refrain.** Still around 10 occurrences after the round-2 edits: abstract (98), intro (120, 122), method (172, 190), §4.2 opener (300), §4.5 close (457), §5.1 (471), §5.4 (491), conclusion (509). Round 1 flagged eight. Two have come down (the §4.2 second invocation and the §5.4 wording are restructured), three new ones have arrived (the method case-selection paragraph and the method asymmetric-depth paragraph each reuse the refrain). Net: still too many.

**Contribution in one sentence.** "A multi-case architectural analysis of three civic-tech platforms, with empirical recovery, evolutionary analysis, and fork-divergence quantification, showing that quality-attribute trade-offs in this domain function as governance choices and that the Decidim/Consul divergence is the strongest evidence for that claim." This is supported by the round-2 paper. The bigger framing ("provides the architectural analysis IDEA calls for") is still overclaimed and should be retired.

## Lens 2 — Clarity & structure (paper-level)

**Section weights.** Background ~30 lines, Method ~30 lines (8 paragraphs), Analysis ~270 lines across five subsections, Discussion ~50 lines (four subsections), Conclusion ~15 lines. The Method/Analysis ratio is now adequate; in round 1 it was the structural risk. The Analysis is still the largest section by a wide margin — appropriate for the genre and the empirical contribution. The Discussion is on the short side for the load it carries (4 subsections, several big claims) but each subsection is doing distinct work, so the proportion holds. §5.2 and §5.3 are still the most padded; round 1 flagged this and round 2 has not trimmed them.

**Does §4.4 earn separation from §4.5?** Yes, on balance. §4.4 carries the cross-case figures (contributor concentration, commit timeline) that are the empirical backbone of the synthesis. §4.5 is the trade-off map table plus the three-structure table — analytic synthesis built on §4.4's quantitative substrate. They could merge by promoting the §4.4 figures into §4.5, but the current split is cleaner: §4.4 = "what the data says about all three", §4.5 = "what it adds up to". Keep the split. One real risk: §4.4's closing paragraph (line 393) and §4.5's opening paragraph (line 397) both state the same headline — "Decidim modular ecosystem, Consul fragmented forks, Polis thin algorithmic" — back to back. Cut one.

**Repetition.**
- The "shared origin / opposite architecture" refrain — discussed in Lens 1, still ~10 instances.
- "To the best of our knowledge" — now only at abstract (98) and intro (118). Down from four in round 1. Addressed.
- IDEA "democracy stack" — at intro (112, 122), §5.3 (483), conclusion partial. Four locations, each doing different work; acceptable.
- The "we hypothesize / does not prove it" pattern — line 149 (hypothesis stated), line 422 (hypothesis recovered with the "does not prove it" hedge), line 471 ("this relationship is especially strong in civic tech" — hedge dropped). Round 1 flagged the disappearing hedge; it has not been fixed.

**Figures.** Now 8 figure/listing/table objects. References resolve. Two orphans exist on disk but are not in the paper:
- `figures/consul_fork_divergence.pdf` — exists, not used.
- `figures/decidim_engine_activity.pdf` — exists, not used.
Neither is missed in the argument; the activity histogram (consul_fork_activity) and the contributor concentration figure cover the same ground. Either delete the unused PDFs from `figures/` or, if you want them, add `\includegraphics` references — currently they will confuse anyone browsing the repo. The matrix figure (Fig. 3) is good in round 2 — the dot/circle distinction is clearer than round 1's block markers. The coupling heatmap is the strongest new figure: it does analytical work (the SPACES block jumps out) that no other figure does.

## Lens 3 — Writing style (paper-level)

Voice is consistent end-to-end and matches the round-1 voice — the same author, same register. The empirical sessions read as written by the same person, which is harder than it sounds across four log files and 270 lines of analysis prose.

**AI-slop patterns at the paper level (not instances — those are for section reviewers):**

- *The "X is Y — and Z" em-dash construction* round 1 flagged is the persistent tic. `grep -c -- "---"` returns 60 em-dashes in main.tex. For a paper that runs ~3,000 lines of body text not counting captions, that is on the high side but not extreme. The clusters are in the abstract (5 em-dashes in one paragraph) and §5.1 (5 across two paragraphs). Spot-rewrite half the abstract em-dashes as full sentences.
- *Hedging-then-asserting* still alternates with claim-flattening, but the hedges are slightly better calibrated than round 1 — §3 "Asymmetric case design" paragraph (line 190) is the right tone, and the §5.4 admission is sharper.
- *"This is not abstract / these are not abstract observations"* still appears at line 507 ("These are not abstract observations") — same construction round 1 flagged. One instance left.
- *Adjective slop* — "comprehensive", "robust", "seamless" — none. Clean.
- *The "what the data says" / "the numbers say" trick* now appears in §4.4, §4.5, §5.4. Three is fine.

**Length proportionality.** §5.2 ("What SECO Research Gains from Democratic Analysis") is two paragraphs doing one paragraph of work. §5.3 ("Implications for the Democracy Stack") is similar. Trim both.

## Lens 4 — Academic conventions (paper-level)

**Citation balance.** SECO side: Bass, Christensen, Manikas (2013, 2016), Jansen, Iansiti, Tyree, Koskinen, Knutas, Cobos, Noori, Gall — 11 sources, mostly load-bearing. STS side: Winner, Lessig, Schneider (2024, 2021), Zhang, Bowker & Star — 6 sources, with Winner/Lessig/Schneider 2024 cited together as a trio in three places (lines 116, 509). The Bowker & Star addition in §5.1 (line 469) is new and does real work — best STS citation use in the paper. The "STS, law, and platform studies" framing on line 116 still implies broader engagement than the citation list supports. Narrow to "platform studies and STS" or add one source from law (Hildebrandt, Pasquale, even a second Lessig piece).

**"To the best of our knowledge."** Used twice: line 98 (abstract, broad) and line 118 (intro, slightly narrower). The intro version is well-supported by the Manikas 2016 review evidence in §2.2. The abstract version is still phrased as "no study has applied software architecture or software ecosystem methods to civic technology platforms" — the SA side of that is hard to defend given the HCI/CSCW literature (Aragón 2017 is in the bib, uncited; Behrendt 2025 likewise). Round 1 asked for this tightening. Round 2 has not done it. Either narrow the abstract claim to match the intro ("SECO methods and quality-attribute analysis") or engage with the orphan citations.

**Orphan citations.** I count five citations in references.bib that never appear in main.tex:
- `aragon2017deliberative` — orphan (round 1 flagged this)
- `behrendt2025supporting` — orphan (round 1 flagged this)
- `denardis2009protocol` — orphan (round 1 flagged this)
- `roy2025conversation` — orphan (round 1 flagged this)
- `weyl2025plurality` — orphan (round 1 flagged this)

All five are still in the bib, all five are still uncited. Either cite them — DeNardis would strengthen §2.3, Aragón would shore up the SA-on-civic-tech gap claim, Weyl & Tang fits Polis — or remove them.

**Reference list quality.** 30 entries (unchanged from round 1). Recent (15+ from 2024–2026). Grey-literature heavy (CEPS, OSOR, NTARI, IDEA, Codegram, Roskilde) which is appropriate. `heeks2025three` and `knutas2020local` still have "and others" placeholders for the author lists — should be expanded if the full lists are recoverable. The new round-2 citation `gall1998detection` is correct and load-bearing.

**MSc-genre fit.** The paper hits ITU MSc Research Project conventions: clear RQ, multi-case study, reproducibility script references, method/data/limitations sections, GenAI disclosure block. The ambition is now appropriate for the empirical depth — round 1 had ambition outrunning evidence, round 2 has closed that gap on Decidim and Consul. The "European policymakers" framing in the conclusion still overreaches one notch.

## Load-bearing claims audit

| Claim | Locations | Status |
|---|---|---|
| No prior SA or SECO study of civic tech | Abs (98), §2.2 (153), §2.3 (161) | **Partially supported.** Defensible for SECO (Manikas 2016 explicit). Still hard to defend for SA — orphan HCI citations in bib (Aragón, Behrendt) plus Palacin engagement only partial. |
| Decidim and Consul share an origin in 15M | §1, §3, §4.2 | **Fully supported.** Codegram blog + Barandiaran corroborate. |
| Decidim is modular monolith with 27 engines, manifest pattern | §4.1 | **Fully supported.** Session 1 gemspec recovery; gemspec file evidence concrete; the conferences→meetings exception is honestly flagged. |
| 64% of Decidim commits are single-engine; comments/forms APIs are stable | §4.1 (line 279) | **Fully supported.** Session 3 logical coupling. New in round 2; well-executed. |
| Consul has 1,030 enumerable forks, 280 modified, 39 with 100+ ahead | §4.2 (line 309) | **Fully supported.** Session 4 direct measurement. |
| Madrid maintains a fork 12,725 commits ahead of upstream | §4.2 (line 311), §4.2 (line 349), §5.1 (line 467), abstract | **Fully supported.** Session 4 data. Mentioned in 4 places — load-bearing and earns each mention but the abstract instance could be cut for compression. |
| Consul's 2019 cliff coincides with Ahora Madrid losing power | §4.4 (line 384), §5.4 (line 491) | **Partially supported.** Timeline is real and visible; the causal attribution is honestly hedged in §5.4 ("Separating what the architecture caused from what politics caused would need interview-based research we did not do"). Good. |
| Polis is dominated by one developer (Bjorkegren 56%, top-10 97%) | §4.3 (line 360), §4.4 (line 374) | **Fully supported.** Session 2 evolutionary metrics. |
| The four quality-attribute trade-offs structure the comparison | Abs, §1, §2, §3, §4.5, §5, §6 | **Partially supported on naming consistency.** The four QAs are stable as names (modifiability, interoperability, deployability, transparency). The *paired tensions* (modifiability vs. sustainability, etc.) appear in the abstract and conclusion but the synthesis table uses "democratic benefit vs. architectural cost" with different right-hand-side wording. Round 1 flagged this. Round 2 has not aligned. |
| Software structure shapes organizational and business structures (especially in civic tech) | §2.2 (149), §4.5 (422), §5.1 (471) | **Partially supported.** Hedge held in §4.5 ("does not prove it"); hedge dropped in §5.1 ("This relationship is especially strong"). Round 1 flagged this; not fixed. |
| Polis's PCA + k-means embeds an epistemological assumption | §4.3 (line 366), §5.1 (line 469) | **Partially supported.** Bowker/Star reading is sound as a *general* point about classification systems. The §4.3 evidence does not specifically demonstrate which Polis-deployment outcomes flow from the choice. Honest in §5.4. |
| The paper provides the architectural analysis IDEA's framework calls for | §1 (122) | **Overclaimed.** Same as round 1. Not fixed. |
| Architecture is the governance decision in civic tech | Abstract, §1, §4.5, §5.1, §6 | **Partially supported.** Demonstrated for Decidim/Consul; asserted for Polis; generalised in conclusion. Round 1 found same; round 2 sharpened the Decidim/Consul demonstration but did not narrow the generalisation. |

## Drift map

1. **The Decidim/Consul superlative.** Abstract: "the strongest evidence" (98). Intro: "the clearest demonstration" (122). §4.5: "the clearest evidence" (457). §5.1: "the clearest example" (471). Conclusion: "the clearest demonstration" (509). Five locations, four different adjectives. Pick one and use it.

2. **What the paper delivers to IDEA / European policy.** Intro (122): "provides the kind of architectural analysis IDEA's framework calls for". §5.3 (485): "Our cases point to some concrete lessons" — modest. Conclusion (509): "architecture is not a procurement detail — it is a governance choice" — assertive. §5.3 is the honest register; pull the others toward it.

3. **The four trade-off pairs.** Abstract (98): "modifiability vs. sustainability, interoperability vs. autonomy, deployability vs. transparency, algorithmic depth vs. ecosystem breadth." Conclusion (505): "sustainability burden, reduced autonomy, lost transparency, ecosystem thinness". Table tradeoffs (449–452): "Sustainability burden, partial isolation" / "Standardization pressure, reduced autonomy" / "Reduced local control, potential opacity" / "Design complexity, performance cost". Three different ways of naming the architectural costs. Round 1 flagged this. Round 2 has not aligned the three lists. The third trade-off in particular — "deployability vs. transparency" in the abstract, "Reduced local control, potential opacity" in the table, "lost transparency" in the conclusion — has three different right-hand sides.

4. **Asymmetric depth.** Method (190): "intentionally treated with different depth" — up front, good. §5.4 (495): "only the Decidim case clears the bar of full architectural recovery" — same register. The abstract still describes the method as if uniform across the three cases ("multi-case analysis"). Minor — the abstract is allowed to compress — but the §3-and-§5.4 honesty earns at least a half-sentence in the abstract.

5. **The hedging on software-structure dominance.** §2.2 (149): hypothesis hedged ("We hypothesize"). §4.5 (422): hedge held ("does not prove it — the organizational and political contexts differed too"). §5.1 (471): hedge dropped ("this relationship is especially strong in civic tech"). Round 1 flagged this exact drift; not fixed.

6. **Polis's role in the comparison.** Method (190): "contrasting paradigm rather than a third equal case". §4.3 (354): "not as a third case in the same comparison". §4.5: appears as a third column in three comparative tables (ecosystem, three-structure, trade-offs) as if equivalent. §5.4 (495): "the thinnest, relying mostly on published descriptions". The textual register has fixed the round-1 problem; the tables have not. Either footnote the Polis column in the trade-off table or restructure the tables to acknowledge the asymmetry.

## Cross-reference checklist

- **Four trade-offs named identically in abstract, §2, §4.5, §5, §6?** *No.* See drift item 3. QA names are consistent; cost names drift.
- **Promise → delivery → reflection → return.** Promise (RQ in §1) is delivered by §4, reflected in §5.4, returned in §6. *Yes.* The §1 IDEA-delivery promise is the one that delivery does not match.
- **Method ↔ Analysis match.** Every procedure in §3 produces an artefact §4 cites. Architectural recovery → §4.1 dependency graph (fig:dependency). Evolutionary analysis → §4.4 (fig:contributor-concentration, fig:commit-timeline). Logical coupling → §4.1 (fig:coupling). Fork divergence → §4.2 (fig:consul-forks). *Yes — all four procedures produce artefacts used in the analysis.* The lone caveat: §4.4 cites a per-engine activity figure (decidim_engine_activity.pdf exists on disk) that the method describes (line 178) but the paper does not actually display. Either include the figure or drop "per-engine commit counts" from the method.
- **Snapshot dates / SHAs consistent.** Method paragraph (192): "pinned snapshots." §4.1 (203, 214, 284): SHA `be39c244`, 2026-05-12. §4.2 (318): "snapshot 2026-05-12." §4.3 (360): Polis snapshot 2026-04-26. Session logs: Decidim be39c244 (2026-05-12), Consul 3c3b5c4a (2026-05-11), Polis e8c2b46d (2026-04-26). *Mostly consistent.* The Consul SHA (3c3b5c4a) and the Polis SHA (e8c2b46d) are in the session logs but **not** in main.tex. The method (line 192) says "all three platforms at pinned snapshots" but only the Decidim SHA is given in the paper. The §4.5 table caption "at the SHAs listed in Section method" (line 401) is a forward reference to SHAs the section does not actually list. *Flag for fix.*
- **Figure references resolve, prose around each figure describes what figure shows.** *Yes,* all eight in-paper figures. The two orphan PDFs on disk (consul_fork_divergence, decidim_engine_activity) are not referenced — see Lens 2.
- **Session log findings ↔ paper claims fidelity.** Spot-checked: 7,078 commits (log: matches), 183 authors (log: matches), 64% single-engine (log: 3,525/5,517 = 64%, matches), 1,030 enumerable forks (log: matches), 280 modified (log: matches), 39 with 100+ commits ahead (log: matches), Madrid 12,725 ahead 11,540 behind (log: matches), Polis top-3 82%, top-10 97%, Bjorkegren 56% (log: matches), Consul 2019 → 2020 80% drop (log: matches). *No invented numbers or exaggeration found.* This is a real strength of the round-2 work.
- **Repo rename `consul/consul` → `consuldemocracy/consuldemocracy`.** Method (184) and §4.2 (300) both acknowledge the rename. Table `tab:consul-decidim` does not need updating because it uses the platform name not the repo path. *Resolved.* The Madrid fork is still labelled `AyuntamientoMadrid/consul` in §4.2 (311) and §4.2 (349) — that is correct because the fork name is `consul`, not `consuldemocracy`.
- **Stale entities: sortitions only as a removed-finding, not as current engine.** §4.1 line 206: "decidim-sortitions existed in earlier versions but was removed on 2025-11-19." Mentioned only as a removed feature, not in the matrix or dependency graph. *Resolved.* Round 1 flagged sortitions still appeared as an active component; round 2 has cleaned this up correctly.

## Round-1 follow-up

Comparing against the round-1 findings in `reviews/00_overall.md`:

- **Trade-off naming consistency** (round-1 §argument-rigor): **Partially addressed.** Round 1 said "lock down the four trade-off names." Round 2 has consistent QA names but the cost names still drift between abstract, table, and conclusion.
- **Method section was 17 lines** (round 1: "fix priority 2"): **Addressed.** Now 30 lines, 8 paragraphs, each procedure named.
- **Decidim/Consul refrain repetition** (round 1 counted 8 instances, recommended cutting at least 2): **Partially addressed.** Some restructuring of where it appears, but my count is still ~10 occurrences after round 2; the Madrid-12,725 number has been added on top.
- **Polis weakest link** (round 1: "Polis is doing too much rhetorical work for how little is actually shown"): **Partially addressed.** §4.3 now has real ecosystem data (top-3 82%, Bjorkegren 56%). The architectural reading still rests on the §5.1 Bowker/Star paragraph rather than on Polis-specific evidence. Better than round 1; not solved.
- **"To the best of our knowledge" overclaim** (round 1: tighten to SECO + quality-attribute): **Partially addressed.** §2.2 (line 153) now ties the gap-claim to the Manikas 2016 review. Abstract phrasing (line 98) still broad.
- **Orphan citations** (round 1 listed 5: denardis, weyl, roy, aragon, behrendt): **Unaddressed.** All five still in bib, all five still uncited.
- **IDEA / policy overclaim in intro** (round 1: pull intro toward §5.3's modest register): **Unaddressed.** Line 122 still claims the paper "provides the kind of architectural analysis IDEA's framework calls for".
- **§5.2 and §5.3 padding** (round 1: trim ~30% each): **Unaddressed.** Both still the most padded subsections.
- **Disappearing hedge on software-structure dominance** (round 1: §4.4 honest, §5.1 asserted): **Unaddressed.** §4.5 (422) holds the hedge; §5.1 (471) drops it.
- **The "X is Y — and Z" em-dash construction** (round 1: persistent tic): **Unaddressed.** 60 em-dashes in main.tex; the abstract has 5.
- **Heeks et al. and Knutas et al. bib entries with "and others"** (round 1: expand to full author lists): **Unaddressed.**
- **One-paragraph roadmap at end of §2 or start of §3** (round 1 recommended): **Unaddressed.** The transition into §3 is still direct from §2.3 to "this study uses a multi-case architectural decision analysis".
- **"To the best of our knowledge" claims** for SA-on-civic-tech specifically (round 1: cite or scope): **Unaddressed.** Same overclaim, same orphan citations.
- **Sortitions as stale entity** (round 1: drop from current-features text): **Addressed.** Now only mentioned as a removed engine.
- **Asymmetric depth admitted up front** (round 1: surface in §3, not retrospectively in §5.4): **Addressed.** The "Asymmetric case design" paragraph (line 190) does exactly this.
- **Honesty about politics/architecture confound earlier** (round 1: surface in §3 or §4.2): **Partially addressed.** §3.190 acknowledges the political-divergence confound; §4.4.384 ties the cliff to Ahora Madrid losing power. The §4.2 case section itself does not raise the confound — it is left to §5.4.

## Prioritised fix list

1. **Align the four trade-off cost terms across abstract, table, conclusion.** Pick one set of right-hand-side terms — `sustainability / autonomy / transparency-cost / ecosystem-breadth` is the abstract version; align the table and conclusion to that, or pick the table's wording and propagate. Three different lists is the worst single drift left in the paper.
2. **Cut the Decidim/Consul refrain by at least three.** Keep abstract, §4.2 (where the data lives), §5.1 (where the governance reading lives), conclusion. Cut from §1.122, §3.172, §3.190, §4.5.457, §5.1.471 — pick three.
3. **Pull back the IDEA/policymaker framing in §1.122 and §6.509** to match §5.3's "our cases point to some concrete lessons" register. Same fix round 1 asked for.
4. **Narrow the abstract gap-claim** to "no SECO analysis and no quality-attribute analysis" — matches the §2.2 evidence; the broader phrasing the abstract still uses contradicts the uncited HCI/CSCW work in the bib.
5. **Cite or remove the five orphan references** (Aragón, Behrendt, DeNardis, Roy/Lessig/Tang, Weyl/Tang). DeNardis fits §2.3; Aragón fits §2.2 or §1; Weyl/Tang fits §4.3.
6. **List Consul and Polis SHAs in §3** alongside the Decidim one. The table caption (line 401) forward-references SHAs the section does not contain.
7. **Decide what to do with the two orphan figure PDFs** on disk (`consul_fork_divergence.pdf`, `decidim_engine_activity.pdf`). Either reference them in the text or delete from `figures/`.
8. **Restore the hedge on §5.1.471.** Either keep "this relationship is especially strong" or, better, "the three cases are consistent with that pattern, though n=3 and §5.4 discusses the confounds." Otherwise the §4.5.422 honesty is undone two pages later.
9. **Trim §5.2 and §5.3 each by 25–30%.** Both have one paragraph of real content stretched to two-plus.
10. **Footnote the Polis column in the trade-off table** (or restructure) to acknowledge the asymmetric depth that §3 and §5.4 are otherwise honest about. Same point about the ecosystem table and the three-structure table.
11. **Rewrite half the abstract em-dashes** as two sentences. Five em-dashes in one paragraph is the round-1 tic at its loudest.
12. **Add one Polis-specific architectural finding** that lands the §5.1 PCA reading on something Polis does in deployments — even a paragraph on the `math/conv.py` parameters, the default `k` selection rule, or what is exposed to deployers in the admin UI. Otherwise §5.1.469 is a Bowker/Star point with a Polis label.
13. **Add a one-paragraph map** at the end of §2 or start of §3 telling the reader: here is the RQ, here is the method, here is the case order, here is where the trade-offs are synthesised. Round 1 asked for this.
14. **Expand `heeks2025three` and `knutas2020local` bib entries** to full author lists; "and others" reads as placeholder.
15. **Cut one of the two consecutive headline sentences at the §4.4/§4.5 boundary** (line 393 vs. line 397) — they say the same thing back-to-back.
