# Review: Section 3 — Method (Round 2)

## Verdict

A real method section now exists where there was a gesture. Eight paragraphs, named procedures, scripts pinned to a SHA. Most of what §4 does is traceable back to §3, and the procedures match the session logs. That is the round-1 ceiling cleared. The remaining problems are smaller and concentrated in three places: the snapshot is under-pinned (only Decidim's SHA appears in §3, Consul and Polis pins live nowhere in the paper), positionality and methodological tradition are still absent, and a few procedures are described in §3 in language that does not quite match what §4 reports. For 7.5 ECTS this is a defensible method. It is not yet a tidy one.

## 1. Argument and rigor

Each `\paragraph` block now points at a real procedure the session logs reproduce. Case selection has actual criteria (l. 172). Recovery names files, scripts, and what they extract (l. 175). Evolutionary analysis specifies `git log --no-merges` on partial clones, bot filters, and the metric list (l. 178). Logical coupling cites Gall and defines Jaccard, mega-commit exclusion, and the hypothesis (l. 181). Fork divergence cites the GitHub compare endpoint and the two-axis classification (l. 184). A reader could replicate, especially with the `logs/` and `scripts/` directories alongside.

The asymmetric design (l. 190) is honestly named — "Decidim is the deep case … Consul is the comparison case … Polis is a contrasting paradigm rather than a third equal case." This was a round-1 weakness and is now addressed. The "natural experiment" hedge is properly defused: "approximates --- though does not constitute --- a natural experiment" (l. 190) and the Barandiaran cite acknowledges the organisational confound.

The "specified up front" framing of the four quality attributes (l. 187) is defensible — they appear in the abstract (l. 98), the intro (l. 120), the background (l. 134), and the synthesis table (l. 449). The story holds. The minor crack is the explanation "they are where civic tech platforms most clearly diverge from commercial systems" — that is itself an observation from the cases, which weakens the up-front claim. Either tighten to "from the architecture-as-governance literature" (which §2 already does) or drop the post-hoc justification.

Limitations (l. 193) are not cosmetic. The "quality-attribute-to-democracy mappings are analytical arguments, not empirically validated causal claims" sentence is the right limitation and is what the discussion (l. 161) needs. Email-conflation, runtime-vs-dependency-structure, and private-fork invisibility are the right three concrete limits.

Three rigor gaps remain:

- **Pinned snapshots, plural.** §3 paragraph 8 says "the public GitHub repositories of all three platforms at pinned snapshots." Method gives no SHAs. §4.1 supplies Decidim's `be39c244` (l. 203). Consul's `3c3b5c4a` (session 2) and Polis's `e8c2b46d` (session 2) appear nowhere in the paper, even though §4.2 and §4.3 quote numbers derived from those snapshots. Fix: one sentence in paragraph 8 listing all three SHAs and access dates.
- **Positionality.** Round 1 flagged this and it is still unaddressed. Single coder, no reflexive note, no statement that the author is a developer / Decidim deployer / unaffiliated student. One sentence in paragraph 8 would close it.
- **Methodological tradition.** Round 1 asked for Yin / Stake / Eisenhardt and at least one architecture-recovery citation. None has appeared. Manikas and Jansen carry the SECO side; Gall carries the coupling side; Tyree carries the decision-record side. The case-study scaffolding sits citation-less. Given the supervisor's centre of gravity is SECO, this is a survivable omission, but one Yin (or Runeson & Höst, more SE-flavoured) cite is cheap.

## 2. Clarity and structure

Each paragraph is now self-contained. A reader can extract the procedure on first pass. One residual issue: paragraph 6 (quality attribute scope) sits awkwardly between methodological procedure and conceptual justification — it is doing the work the background section partially did. Consider moving its first half into §2 and keeping only the "scoping choice, identify trade-offs per case" mechanical part in §3.

Paragraph 7 (asymmetric design) recapitulates what §3 paragraph 1 (l. 169) already said about Decidim deep, Consul lighter, Polis lightest. One of the two can go.

## 3. Writing style

Plain register, no wind-ups or wrap-ups. The slop tells from round 1 ("lightweight architectural recovery", "the most architecturally rich civic tech platform available") are gone. Three small flags:

- "deepest treatment" (l. 169) and "deep case" (l. 190) — fine on first use, slightly repetitive across the section.
- "Reproducibility scripts and findings logs are kept alongside the paper source" (l. 169) — vague. Either point at the path (`scripts/`, `logs/`) or drop. A reader has no way to find them.
- "approximates --- though does not constitute --- a natural experiment" (l. 190) — the hedge now has the right shape. Good edit since round 1.

## 4. Academic conventions

- Gall 1998 cited correctly as `gall1998detection`; the citation triggers on the right claim (l. 181). Bib entry checks out.
- Tyree & Akerman 2005 cited as scaffolding for the decision-record framing (l. 187); honest about "without producing formal ADRs."
- Manikas 2013 and Jansen 2014 carry the SECO ecosystem-health citation in paragraph 3 (l. 178). Correct pairing.
- Christensen 2014 is used in §4 synthesis (l. 422) but not in §3 — fine, the method doesn't need it.
- "To the best of our knowledge" still appears in §1 (l. 98, l. 118). Method does not describe a literature search. At this paper length the claim is defensible if softened or scoped; round 1 made this point and it has not been actioned. Out of scope for this review file but flagged.
- No replication-package statement. The session logs and `scripts/` directory effectively are the package. Mention this explicitly in paragraph 8.

## Procedure-by-procedure checklist

| § Para | Procedure | Matches log? | Replicable from §3 alone? |
|---|---|---|---|
| 1 Overview | Four kinds of empirical work, asymmetric depth | n/a | yes |
| 2 Case selection | Two criteria, Decidim/Consul/Polis | n/a | yes — criteria named |
| 3 Architectural recovery | 27 gemspecs, `add_dependency`, manifest calls | session 1 verbatim | yes for Decidim; Consul/Polis described in one sentence each |
| 4 Evolutionary analysis | `git log --no-merges`, bot filter, top-N/Gini/timeline | session 2 verbatim | yes |
| 5 Logical coupling | Gall 1998, Jaccard, >8-engine exclusion | session 3 verbatim | yes |
| 6 Fork divergence | GitHub compare API, two-axis classification | session 4 verbatim | yes |
| 7 QA scope | Four attributes specified up front | n/a (conceptual) | yes |
| 8 Asymmetric design | Deep / comparison / contrast | n/a | yes |
| 9 Data sources & limits | Primary technical + secondary, four limits | partial | mostly — SHAs missing |

## Cross-reference findings

- **§3 paragraph 3 ↔ §4.1:** "27 first-party gemspecs" matches Analysis l. 203 ("27 first-party engines") and l. 209 ("the 27 gemspec files"). Fig. 2 caption uses the same SHA. Consistent.
- **§3 paragraph 4 ↔ §4 evolution subsection:** Top-3 / top-10 / Gini / commits-per-year all delivered in §4.4 (l. 374) and Table 7. Consistent.
- **§3 paragraph 5 ↔ §4.1 module-isolation paragraph:** "Gall 1998 logical coupling, Jaccard similarity" both used (l. 278–279). The "mega-commits >8 engines excluded" filter is in §3 but not stated in §4 prose — minor inconsistency; either add to §4.1 or just to the figure caption.
- **§3 paragraph 6 ↔ §4.2 fork section:** "modified vs unmodified, active vs dormant" matches l. 309 (746 unmodified, 280 modified) and l. 313 (14% pushed in last three years). Consistent.
- **Quality attributes (§3 paragraph 7) ↔ §4 and §5:** Same four named in §1 abstract (l. 98), §2 background (l. 134), §4.1 (l. 292), §4.2 (l. 346), §4.3 (l. 363), §4.5 synthesis (l. 449), §5 (l. 485), §6 (l. 505). The cross-section consistency is now solid — this was a round-1 worry.
- **Asymmetric depth (§3 paragraph 8) ↔ §4 depth:** Decidim §4.1 runs l. 201–296 (~95 lines). Consul §4.2 runs l. 298–349 (~52 lines). Polis §4.3 runs l. 352–366 (~15 lines). The stated asymmetry matches the actual asymmetry.
- **SHAs:** Decidim `be39c244` matches session 1 and §4.1. Consul `3c3b5c4a` and Polis `e8c2b46d` from session 2 are absent from `main.tex`. Either §3 paragraph 8 or §4.4 should list them with dates.

## Round-1 follow-up

| Round-1 finding | Status |
|---|---|
| Method is a 17-line gesture, no procedure | **Addressed** — now 8 paragraphs with procedures |
| Inclusion/exclusion criteria missing | **Addressed** (l. 172 — public codebase, active deployment, architectural variation) |
| Architectural recovery hand-waved | **Addressed** (l. 175 — files, script, dependency classification) |
| "How" of trade-off identification | **Addressed** (l. 187, via Tyree ADR framing) |
| Method/analysis mismatch (promised metrics not delivered) | **Addressed** — promised metrics now delivered |
| Recovery artifacts not flagged as outputs of step 1 | **Addressed** — l. 175 names the dependency graph |
| Methodological tradition (Yin / Stake / Eisenhardt) | **Unaddressed** |
| Architectural-recovery literature (Garcia, Ducasse, Murphy) | **Unaddressed**, possibly obsolete given supervisor's SECO emphasis |
| ATAM / SAAM for trade-off analysis | **Unaddressed**; Tyree partially substitutes |
| Unit of analysis undefined | **Partially addressed** — implicit at "platform" and "decision" level, not stated |
| Positionality / researcher bias | **Unaddressed** |
| Temporal scope, SHAs, access dates in method | **Partially addressed** — Decidim SHA appears in §4.1, others missing |
| Replication package | **Partially addressed** — l. 169 alludes to scripts/logs; path not given |
| Limitations stated in §3 instead of deferred | **Addressed** (l. 193) |
| "Lightweight architectural recovery" hedge | **Addressed** (gone) |
| Empty superlative "most architecturally rich" | **Addressed** (cut) |
| "Approximates a natural experiment" hedge | **Addressed** (now properly framed l. 190) |

Most of the round-1 checklist is closed. The remainder is procedural polish (SHAs, paths, positionality) and one substantive omission (case-study tradition citation).

## Prioritized fix list

1. **Pin the snapshots.** Add one sentence in paragraph 8 listing all three SHAs and access dates: Decidim `be39c244` 2026-05-12, Consul `3c3b5c4a` 2026-05-11, Polis `e8c2b46d` 2026-04-26. The session logs already have these.
2. **Name the replication artifacts.** Replace "Reproducibility scripts and findings logs are kept alongside the paper source" (l. 169) with the explicit paths — `scripts/` and `logs/` in the paper repository.
3. **One sentence on positionality.** Single coder, the author's relationship to the cases (developer? deployer? unaffiliated student?). Two lines in paragraph 8.
4. **One case-study citation.** Add Yin or Runeson & Höst at the head of paragraph 1 to anchor the multi-case design. Cheap, closes a round-1 gap.
5. **Trim the QA scope paragraph.** Either move the conceptual justification into §2 or cut the comma-spliced "they are where civic tech platforms most clearly diverge from commercial systems" — it weakens the "specified up front" framing.
6. **De-duplicate paragraphs 1 and 7.** The asymmetric-depth point is now made twice. Keep paragraph 7, shorten paragraph 1's last two sentences.
7. **Mention the mega-commit filter in §4.1 prose**, not just the method, so the reader sees the same procedure where the result lands.
