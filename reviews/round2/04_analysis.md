# Review: Analysis (§4, lines 199–462)

## Verdict

§4.1 is now the part of the paper that earns its keep. The Session 1 gemspec recovery, the Session 3 logical-coupling result, the dependency graph and the coupling heatmap together give the Decidim case a level of empirical anchoring that almost no other student paper in this topic area will have. The framing "modularity at API boundaries, not at implementation" (279) is the single best sentence in the paper. §4.2 is the second-biggest improvement: Madrid's 12,725-commits-ahead fork is now load-bearing evidence rather than a textual aside. §4.3 has been refreshed with real numbers but is still a half-page on a third case and reads that way. §4.4 is new and useful as a synthesis figure-bearer but does not always do the synthesising work it promises — too often it narrates the figures rather than tying them back to architecture. §4.5 is now mostly consistent with "specified up front" framing, but the Table 6 evidence column still has slogans where it should have data, and the four costs are named three different ways across abstract / table / conclusion. Causal language has been hedged in places but slips back at lines 393 and 457. The shared-DB tension is now actually engaged (line 279), which is the biggest single round-1 fix.

## 1. Argument & rigor

**Decidim recovery — §4.1.** Session 1 is folded in properly. The "27 first-party engines, 24 user-facing, 3 dev tooling" claim (203) is correct and traceable to the log. The four-group decomposition (206) lines up with the recovered data. `decidim-sortitions` is mentioned exactly once and only as a removal finding (206) — the round-1 instruction to drop it from the live taxonomy was followed. The conferences→meetings cross-engine dependency (209) is now in the prose. The hub-and-spoke is correctly complicated: "comments (6 dependents) and forms (5 dependents)" are flagged as de-facto Layer-2 hubs (209). The shared-DB tension that round 1 flagged as the most interesting unaddressed finding is now engaged at 279: "The modularity is at API boundaries, not at implementation." That sentence does substantial argumentative work and is empirically earned by the Jaccard 0.43 figure for the four spaces. This is the single biggest improvement of the rewrite.

Two empirical claims still need tightening. Line 279: "Of 7,078 human commits, 64% stay inside a single engine boundary." The Session 3 log says "5,517 touched an engine" out of 7,078, and "3,525 commits (64%) are single-engine." So 64% is of the 5,517 that touched an engine, not of all 7,078. The paper reads as if 64% of all human commits — including commits that touch zero engine directories — stay inside one engine. The denominator slipped. Either restate as "64% of engine-touching commits" or recompute. Line 279 also reports "$J < 0.06$ in most cases" for comments/forms dependents; session 3 reports 0.04–0.16 (forms↔surveys is 0.16). "Most cases" is true but the upper end deserves a "with the exception of forms↔surveys at 0.16" hedge — otherwise a reader who looks at the heatmap will catch the inconsistency.

The four interaction mechanisms (250–255) still have no provenance citation (round-1 finding 1 partially unaddressed). It now reads like code-reading because the script-and-log workflow exists, but the section does not cite back to `recover_decidim.py` or the log. A reader who is not the author cannot tell which mechanisms were observed vs. inferred from Codegram.

**Consul — §4.2.** Session 4 is folded in well. "1,030 enumerable forks; 746 unmodified; 280 modified; 147 < 10 commits ahead; 39 ≥ 100 commits; 5 ≥ 1,000" (309) matches the log exactly. The Madrid 12,725-ahead / 11,540-behind finding (311) is in the right place, with the right tone — "the city that originated the platform ended up maintaining a private copy that drifted away from the public upstream and was eventually abandoned" is one of the best sentences in §4. The "literature-based comparison foil" framing the brief asked for is *mostly* honest now: the method section explicitly says Consul recovery is "lighter and focuses on the points where it contrasts with Decidim" (175). But the §4.2 prose at 303 still asserts a lot of code-level structure about Consul — "no engine isolation", "`config/routes.rb` file defines all feature routes in a single file", "no module-level namespace boundaries enforced at the code level" — without a single repo citation, footnote URL, or pointer to a `consul/consul` commit. This is the same round-1 finding (Consul claims uncited). A reader who trusts the Decidim section because it shows its work will notice that the Consul section does not. Either add footnotes to the relevant files in `consuldemocracy/consuldemocracy` or attribute the structural claims to `linaker2025consul`.

The fork-divergence figure used is the activity histogram (`consul_fork_activity.pdf`, 317). The divergence scatter (`consul_fork_divergence.pdf`) exists in `figures/` but is not used. Session 4 explicitly recommended either-or; this is fine, but the activity histogram is a weaker piece of evidence on its own than the scatter would be. The empty "ahead-only" quadrant — forks that caught up on upstream — would visualise the "almost nothing contributed back" story better than the histogram does. Consider swapping.

**Polis — §4.3.** Session 2 numbers are in (Bjorkegren 56%, 82%/97% top-3/top-10, 250 forks, 1,153 stars). The asymmetric depth is now flagged at 354: "It is included not as a third case in the same comparison, but as evidence of a different trade-off profile." Good. But the architectural description (357) is still one paragraph with no code citation, and `bono2025artificial` (366) is still a generic AI-in-participation citation, not a Polis-specific one. The round-1 "FAccT 2025" issue is now obsolete since the Method section no longer promises that paper, but the citation gap on Polis itself remains. The strongest move in this subsection — "PCA + k-means embeds an epistemological assumption" (366) — survived from round 1 and is the most interesting analytical point in §4 outside §4.1.

Specific claim to check: line 357 says "k-means clustering ... with k selected automatically." Round 1 flagged this as hiding Polis's actual heuristic. The phrasing is unchanged and still slightly misleading — Polis uses a silhouette-based selection, which is not "automatic" in any neutral sense. Either say "selected by silhouette score across k=2..5" or drop the parenthetical.

**§4.4 Ecosystem Evolution — new subsection.** This subsection has the cleanest opening of any in §4 ("each platform's ecosystem in qualitative terms... we mined the commit history of all three repositories", 371) and the two figures (contributor concentration, commit timeline) are the right ones. But the synthesis move at the end (393) is rushed. The paragraph "Decidim's modular architecture admits a broader set of contributors and produces a steady-state pattern of maintenance across many authors; Consul's monolithic architecture concentrated work in a municipal team that was vulnerable to a political shift; Polis's algorithmic monolith concentrated work in a single developer..." is the right move but it is one sentence per case. The architecture-to-distribution causal link deserves more space — that is the actual synthesis. As is, §4.4 is closer to "two more figures across cases" than to "the synthesis that ties cases together."

The Consul 2019 cliff is correctly attributed (384) — Ahora Madrid losing office — with the Section 5.4 confound forwarded. Good. The Polis 2025 spike is flagged honestly (384, "one anomalous burst") rather than smoothed over. Good.

**§4.5 Synthesis: Trade-off Map.** The trade-offs are now framed as specified up front. Line 439: "The three cases navigate the four quality attributes specified in Section~\ref{sec:method} in different directions." That is the right framing. The round-1 problem ("the cases reveal four trade-offs") is gone. Good. The reverse-direction observation about software → organisational/business (422) survived and is correctly hedged: "though it does not prove it — the organizational and political contexts differed too." Better than round 1.

But the trade-offs table (Table 6, 441–455) still has uneven evidence columns. Row 1 (Modifiability) is concrete: "80+ shared modules and 64% single-engine commit rate vs. 280 modified forks." Row 2 (Interoperability): "Decidim's open-source integration stack; civic tech platforms otherwise as silos." The second half is not evidence from this study. Row 3 (Deployability): "Polis Docker ease vs. Decidim's 27-engine setup." Marginal — that is a one-line gesture, not the evidence row 1 provides. Row 4 (Transparency): "Decidim's PX design vs. Polis's opaque PCA." Comparing a marketing concept (PX) to an algorithm. The round-1 critique of Rows 2 and 4 as slogans stands.

Causal language slips back twice. Line 393: "concentrated work in a municipal team that was vulnerable" — fine, hedged elsewhere. Line 397: "Decidim's modular architecture produced a shared-module ecosystem, Consul's monolith produced diverging forks." That "produced" is causal, after the hedge at 422 admits it isn't. Same word, opposite direction. Line 457: "the Decidim/Consul divergence... is the clearest evidence of this." "Evidence" is fine; "the architecture is the governance decision" earlier in the same paragraph is the thesis being argued, but stated as fact. The hedge in §5.4 (491) admits politics also differed — that admission belongs in §4.5 before this closing claim, not retroactively in §5.

## 2. Clarity & structure

§4.1 has the cleanest structure of any subsection in the paper. Engine structure → dependency graph → space/component matrix → interaction mechanisms → module isolation in practice → extension → quality attributes → ecosystem. Each `\paragraph` does a job. The Listing 1 placement is good — the registry pattern is shown rather than described. Figures 2 (dependency) and 3 (matrix) and 4 (coupling) are all in the right place and all do explanatory work.

§4.2 has lost the round-1 "Consul is mirror-image Decidim only" problem because the fork-divergence work gives Consul its own affirmative analytical move. Good. But the "Architecture" paragraph at 303 reads as a list of negatives ("no gem separation", "no engine isolation", "no migration isolation", "no `ARCHITECTURE.md`", "no `Gemfile` separation"). Five "no"s in one paragraph. Once is enough; the rest can be positively phrased.

§4.3 is still short. That is now defensible because the asymmetric design is explicit, but inside the subsection the reader still experiences the thinning. Adding the Session 2 numbers to "The different trade-off" paragraph (360) helped — that paragraph now has real evidence rather than gesture.

§4.4 is the right structural addition. But it lives between Polis and Synthesis, which means the reader gets: Polis (thin) → ecosystem cross-comparison (Session 2 figures) → trade-off synthesis. The cross-comparison would arguably sit better before §4.5 *and* before §4.3, so all three case analyses sit together followed by the two synthesis moves. As ordered, the flow is "Decidim deep, Consul medium, Polis thin, all-three numbers, all-four trade-offs". Acceptable but not optimal.

§4.5 has Tables 4 (ecosystem), 5 (three-structure), 6 (trade-offs) in 60 lines. Round-1 finding 9 "cut one of these tables" not addressed; instead a third was added. Three sorting tables in one subsection is a lot. Table 5 (three-structure) is the most novel; Tables 4 and 6 overlap (both sort cases by architectural choices and ecosystem outcomes).

Figure references all resolve (`fig:dependency`, `fig:matrix`, `fig:coupling`, `fig:consul-forks`, `fig:contributor-concentration`, `fig:commit-timeline`). `fig:tradeoffs` is in Background and is *not* re-referenced from §4.5 — a reader at the synthesis cannot flip back to the positioning map from inside §4. Worth a forward/back reference.

## 3. Writing style

Bolded paragraph labels (`\paragraph{...}`) are still everywhere: seven in §4.1 (205, 208, 218, 247, 278, 288, 291, 294 — that is eight), four in §4.2, three in §4.3, two in §4.4, none in §4.5. Round-1 finding 6 partially unaddressed: §4.5 was de-paragraphed cleanly, but §4.1–4.4 still use them as load-bearing structure. A few are earned (Engine structure, Dependency graph, Quality attribute profile carry the case structure). Most are not.

Em-dash count in §4 is high but not as bad as round 1. Line 311 has two em-dashes in one sentence: "the city that originated the platform ended up maintaining a private copy that drifted away from the public upstream and was eventually abandoned --- the architecture pushed even the originator into the fork pattern that fragmented the wider ecosystem." That one earns it. Line 457 uses three em-dashes: "no architecture maximizes all democratic quality attributes at once. ... The architecture is the governance decision --- and the Decidim/Consul divergence, starting from the same point, is the clearest evidence of this." That paragraph also restates the thesis twice — same round-1 finding, still here.

Wind-ups: line 218 "This is the key architectural pattern." Line 300 "The architectural divergence between the two platforms starts here." Both held over from round 1.

"Want X? Turn it on. Want Y? Turn it on." (219). Still in. Same line-clash with surrounding register that round 1 flagged.

Adjective creep is reduced. "Critically dependent on Catalan institutional funding" (295) is still there, and the closing "its robustness is fragile" is unchanged. The phrase "the ecosystem did not slowly grow and consolidate — it ossified" (313) is good prose; the comparable "the platform is effectively a one-developer codebase with sporadic external contributions" (360) is also good. The voice is more uneven than slop-heavy.

Line 393 closes §4.4: "Taken together, the two figures sharpen the architecture-as-governance reading." This is a wind-up sentence that does no work — cut and let the architecture-to-distribution sentence stand on its own.

## 4. Academic conventions

**Citation discipline.** Decidim GitHub numbers (295: 1,748 stars, 469 forks, 450 institutions, 120,000 Barcelona participants) cite `barandiaran2024decidim` only, but Barandiaran predates the May 2026 numbers. The GitHub numbers need footnotes with URL and access date. Round-1 finding 7 unaddressed.

Polis GitHub numbers (360: 250 forks, 1,153 stars, 14-year history) have no citation. Same problem.

Consul Table 7 numbers (Table 5 at 416: "1,123 (280 with any modification)", "Top-10: 87%", "186 unique authors", "~280 modified forks; 39 with 100+") are not cited inline. They are traceable to §4.4 and §4.2, but the table caption only references "Section 3" — and Section 3 lists Decidim's SHA but not Consul's (`3c3b5c4a`) or Polis's (`e8c2b46d`). Real cross-reference failure: Table 5 caption says "at the SHAs listed in Section 3" but Section 3 lists exactly one SHA (Decidim's at line 175). Either add Consul/Polis SHAs to §3 or change Table 5's caption.

**Hedging.** Substantially improved. Line 161 in Background sets the right tone ("These mappings are reasoned arguments, not proven causal links"), and §4.1 stays in line. §4.2 and §4.4 keep most causal language properly framed. The two slip-throughs are 397 ("produced") and 457 ("the architecture is the governance decision") — both in §4.5.

**Limitations deferred to Discussion.** §5.4 (Evaluating the Approach) still does work that §4.5 should do once. The Madrid political collapse, the Catalan funding, the founder-culture differences — all admitted at 491 but absent from §4.5's closing paragraph at 457. Round-1 finding 5 partially unaddressed.

## Subsection-by-subsection notes

**§4.1 Decidim (201–296).** Strongest part of the paper. Recovery is rigorous, the dependency graph and coupling heatmap do explanatory work, the "modularity at API boundaries, not at implementation" finding is genuinely earned by data. Remaining issues: 64%-of-7,078-vs-of-5,517 denominator slip (279); four interaction mechanisms still without code-citation provenance (250–255); ecosystem GitHub numbers uncited (295); "Want X? Turn it on" tic (219).

**§4.2 Consul (298–349).** Second-strongest. Fork-divergence work is fully integrated; Madrid 12,725-ahead is load-bearing. Remaining issues: code-level structural claims (303) still uncited; `consul_fork_divergence.pdf` exists but is unused — consider swapping in or alongside the activity histogram; "no/no/no/no/no" paragraph at 303 reads as list-of-negatives.

**§4.3 Polis (352–367).** Numbers from Session 2 properly integrated (360); asymmetric depth flagged (354). Remaining issues: no Polis-specific citation (only `bono2025artificial`, which is generic); "k selected automatically" still hides the silhouette heuristic (357); no figure or listing, although given the asymmetric design this is defensible.

**§4.4 Ecosystem Evolution (369–393).** Real synthesis move with both figures. Remaining issues: closing paragraph at 393 narrates rather than synthesises; the architecture-to-distribution causal sentence is one line per case, which is too short for what is the most cross-cutting analytical move in the paper. The 2026-partial cut-off is correctly flagged in Figure 7's caption (389).

**§4.5 Synthesis (395–457).** Trade-offs now correctly framed as specified up front (439). Three-structure table is the standout. Remaining issues: Table 6 evidence column still mixes data with slogans (Rows 2 and 4); two causal slips ("produced" 397, "the architecture is the governance decision" 457); thesis restated twice in the closing paragraph; no Table 4 vs. Table 6 consolidation; no forward link to figure 1 (the tensions positioning map) from inside §4.5.

## Empirical claims flagged

**Possibly miscounted or oversimplified:**
- 279: "Of 7,078 human commits, 64% stay inside a single engine boundary." Session 3 log: 3,525 of 5,517 *engine-touching* commits = 64%. Of *all* human commits the figure is 50%. Either restate or recompute.
- 279: "$J < 0.06$ in most cases" for comments/forms dependents. Session 3 has forms↔surveys at 0.16. Add the exception.
- 357: "k-means clustering ... with k selected automatically." Hides Polis's silhouette heuristic. Either specify or drop.
- 416 (Table 5): "Top-10 contributor share 68% / 87% / 97%" — correct against Session 2 log. Good.
- 309: "53\%" of 280 is 147 — 147/280 = 0.525, rounds to 53%. Good.
- 311: 12,725 ahead / 11,540 behind / 2023-05-23 — matches Session 4 log exactly. Good.

**Causally overreaching:**
- 397: "Decidim's modular architecture *produced* a shared-module ecosystem, Consul's monolith *produced* diverging forks." After 422 admits the confound, "produced" is too strong. "Coincides with" or "is consistent with."
- 457: "The architecture is the governance decision." Thesis stated as fact in the §4 closer; §5.4 walks it back at 491. The hedge belongs here.
- 422: "in all three cases, the software structure seems to have shaped the organizational and business structures, not the other way around" — correctly hedged with "though it does not prove it." Good model for the rest of §4.

## Cross-reference findings

- **Four trade-off naming.** Abstract (98) names costs "sustainability, autonomy, transparency, ecosystem breadth." Conclusion (505) names them "sustainability burden, reduced autonomy, lost transparency, ecosystem thinness." Table 6 row 4 has cost "Design complexity, performance cost" — neither "ecosystem breadth/thinness" nor "transparency." Three different naming schemes. The Transparency-row cost in Table 6 is the most divergent — abstract and conclusion both name an ecosystem-side cost for transparency, but the table itself does not. Reconcile.
- **SHAs.** Decidim `be39c244` is consistent across §3, §4.1 prose, §4.1 figures. Consul SHA (`3c3b5c4a` per Session 2 log) and Polis SHA (`e8c2b46d` per Session 2 log) are not in main.tex anywhere. Table 5 caption (401) says "at the SHAs listed in Section~\ref{sec:method}" — Section 3 only lists Decidim's. Broken cross-reference.
- **Repo rename.** `consul/consul` appears twice (lines 184 and 300). Both are paired with the new name in a "formerly X, now Y" construction, which is the right handling. No stale `consul/consul` references survive.
- **Sortitions.** Mentioned exactly once at line 206 as "existed in earlier versions but was removed on 2025-11-19." That is the right pattern.
- **Figures.** All `\ref{fig:...}` in §4 resolve to extant PDFs in `figures/`. `consul_fork_divergence.pdf` exists in the folder but is not referenced — orphan figure (not a bug, but a missed opportunity).
- **Session-log fidelity.** All numbers spot-checked against the four logs match except the 64%-of-7,078 denominator at line 279 (see above).
- **\ref{fig:tradeoffs} from §4.5.** Figure 1 (positioning map) is in §2.1 and never referenced from inside §4. A reader in §4.5 cannot see the positioning visualisation without flipping back.

## Round-1 follow-up

Marking each round-1 finding:

1. **Decidim recovery rigorous but provenance muddled.** Partially addressed. Recovery is now anchored in the session log and the script. Four interaction mechanisms paragraph (250–255) still lacks inline provenance.
2. **"No engine-to-engine dependency bypasses core" falsifiable but unverified.** Obsolete — the claim is now corrected at 209 with the comments/forms/conferences→meetings cross-deps documented.
3. **Shared-database / ActiveRecord coupling contradicts modularity.** Addressed. Line 279 ("modularity is at API boundaries, not at implementation") engages the tension empirically. Biggest single round-1 fix.
4. **Consul claims undersourced.** Unaddressed for the code-level structural claims at 303. Fork-divergence side is now fully sourced.
5. **Madrid political collapse as confound.** Partially addressed. Mentioned at 384 with forward to §5.4; but §4.5's closing paragraph (457) still asserts the thesis without acknowledging the confound. The hedge belongs *before* the closing claim, not after it.
6. **Polis citation gap / FAccT 2025 missing from bib.** Partially addressed. FAccT 2025 promise is gone from Method (obsolete); but no Polis-specific citation was added. `bono2025artificial` (366) is still the only cite and it is not about Polis.
7. **§4.4 trade-offs framed as "discovered."** Addressed. Line 439 now says "specified in Section~\ref{sec:method}." Round-1 finding 3 in the fix list resolved.
8. **Trade-offs not orthogonal, names inconsistent across paper.** Unaddressed. Three different namings across abstract / table / conclusion (see cross-reference findings).
9. **Causal language outruns evidence.** Partially addressed. Most slips are gone; two survive at 397 ("produced") and 457 ("the architecture is the governance decision").
10. **Bolded paragraph labels everywhere.** Partially addressed. §4.5 was cleaned up; §4.1–4.4 still use them heavily.
11. **Em-dash overuse.** Partially addressed. Reduced but the 457 paragraph still does three.
12. **Figure 1 (positioning map) is in §2, not in synthesis.** Unaddressed.
13. **Quality attribute profiles uneven across cases.** Partially addressed — Consul (345) now has an explicit profile, but interoperability is still skipped. Polis profile (362) is editorial rather than evidence-based.
14. **Limitations deferred to Discussion.** Unaddressed — hedges that should land in §4.5 still land in §5.4.
15. **Table 6 (was tab:tradeoffs) "Primary Evidence" column mixed.** Unaddressed. Rows 2 and 4 still slogans rather than evidence.
16. **"Want X? Turn it on" tic.** Unaddressed (still at 219).
17. **Cut one of the synthesis tables.** Unaddressed — a third sorting table was added (Three-structure).

## Prioritized fix list

1. **Fix the 64% denominator at line 279.** Either restate as "64% of engine-touching commits" or recompute against all 7,078. This is the most directly checkable number in §4.1 and a careful reader will catch it.
2. **Reconcile the four-cost naming across abstract / Table 6 / conclusion.** Pick one set: most useful is probably (sustainability burden, reduced autonomy, opacity, ecosystem thinness). Then propagate. The Transparency row's cost in Table 6 is the most divergent.
3. **Add Consul and Polis SHAs to §3, or remove the "SHAs listed in Section 3" reference from Table 5's caption (401).** Currently broken cross-reference.
4. **Add code-level provenance to Consul §4.2.** Either footnote URLs for `config/routes.rb`, `app/models/custom/`, `Gemfile_custom` in `consuldemocracy/consuldemocracy`, or attribute the structural claims to `linaker2025consul`. Same round-1 finding as before.
5. **Add a Polis-specific citation.** `small2021polis` or one of the Polis project's own technical writeups — pick something. `bono2025artificial` is not a Polis cite.
6. **Tighten the §4.5 close (457).** Drop one of the two thesis restatements; move the Madrid-political-collapse hedge from §5.4 into §4.5 *before* the closing sentence.
7. **Replace "produced" with "coincides with" or similar at 397.** Causal language slip after the 422 hedge admits the confound.
8. **Fix Table 6 evidence column for Rows 2 and 4.** Either supply concrete evidence ("Decidim's GraphQL API, OpenStreetMap/Matomo/Jitsi stack" for interoperability; "Decidim's random proposal sort and no-delete admin policy" for transparency) or admit the row is supported by one case rather than three.
9. **Strip three `\paragraph` labels from §4.1.** Keep the four that carry the case structure (Engine structure, Dependency graph, Quality attribute profile, Ecosystem indicators). Topic-sentence the rest.
10. **Decide on the Consul fork figure.** Either keep the activity histogram or swap in the divergence scatter — the empty "ahead-only" quadrant would visualise "few contribute back upstream" more directly. Or include both, since both are already generated.
11. **Cite Decidim's May 2026 GitHub numbers (295) with footnotes.** Same for Polis numbers at 360.
12. **Rework the §4.4 closing paragraph at 393.** "Taken together..." narrates. Replace with one strong synthesis sentence per case (architecture → distribution) or cut and let the figures stand.
13. **Fix the "k selected automatically" line at 357.** Polis uses silhouette-based selection; "automatically" hides a design choice.
14. **Forward-link to Figure 1 from §4.5.** A reader in the synthesis cannot find the positioning map without flipping back.
15. **Cut "Want proposals inside a participatory process? Turn it on. Want budgets inside an assembly? Turn it on." (219).** Register clash held over from round 1.
