# Round 2 — Citation-level review (07)

## 1. Verdict

Citations are in much better shape than Round 1. The four session logs are paraphrased accurately — every quantitative claim I spot-checked matches the log to the digit. The FAccT 2025 gap is closed (the Polis-via-FAccT cite has been dropped from Method; `bono2025artificial` carries the remaining Polis-side citation work). Repo names are correctly updated to `consuldemocracy/consuldemocracy`. Two real problems remain. First, five Round-1 orphan citations are still in `references.bib` and still uncited: DeNardis, Weyl, Roy, Aragón, Behrendt. Second, two empirical claims in the Introduction (DESI/UN rankings; Polis "200,000 participants / 26 pieces of legislation") rest on a footnote-only source or no source at all.

## 2. Per-claim audit (empirical numbers)

| Claim | Location | Source / log | Verdict |
|---|---|---|---|
| DESI #1, UN e-gov top | l.110 | Footnote to "DESI 2022 / UN 2024" — not in bib | Undersourced. Footnote is fine for a paper of this scope but the documents should be in `references.bib`. |
| Decidim 450+ institutions, 30 countries | l.114, l.295, l.416 | `barandiaran2024decidim` (l.295 only) | Cited once at l.295 via the institutional-funding sentence. The earlier claim at l.114 has no citation. |
| Polis 200,000 participants, 26 pieces of legislation | l.114 | None | **Uncited.** Not in any log, not in `bono2025artificial`. Needs a Polis-specific or vTaiwan source. |
| Decidim 27 first-party engines, 24 user-facing | l.203, l.206 | Session 1 (matches) | Correct. |
| Sortitions removed 2025-11-19 | l.206 | Session 1 (matches) | Correct. |
| 13 of 27 engines have cross-engine deps; comments 6 dependents, forms 5 | l.209 | Session 1 (matches) | Correct. |
| `decidim-conferences` → `decidim-meetings` runtime dep | l.209, l.219 | Session 1 (matches) | Correct. |
| 7,078 human commits, 64% single-engine, Jaccard up to 0.43 (spaces), 0.11–0.20 flagship cluster, J<0.06 for comments/forms consumers | l.279 | Session 3 (matches exactly — 3,525/7,078 = 64%, processes↔assemblies J=0.43) | Correct, properly attributed to `gall1998detection`. |
| 1,748 stars, 469 forks (Decidim) | l.295, l.410 | GitHub at snapshot | Should be tagged with the SHA; currently asserted with no inline anchor. |
| 7,078 commits / 183 authors / top-3 36% / top-10 68% / Gini 0.85 (Decidim) | l.295 | Session 2 (matches) | Correct. |
| Polis 250 forks, 1,153 stars at 2026-04-26 | l.360 | Session 2 snapshot | Matches. |
| Polis top-3 82%, top-10 97%, Bjorkegren 56% | l.360, l.374 | Session 2 (matches) | Correct. |
| Consul 1,123 reported forks, 1,030 enumerable, 746 unmodified, 280 modified, 147<10, 39≥100, 5≥1000 | l.309 | Session 4 (matches) | Correct. |
| AyuntamientoMadrid 12,725 ahead, 11,540 behind, abandoned 2023 | l.311, l.349, l.467 | Session 4 (matches; last push 2023-05-23) | Correct. |
| 14% pushed in last three years; 2019 peak | l.313 | Session 4 (149/1,030 = 14.5%) | Correct. |
| Consul 14,372 commits, top-3 52%, top-10 87% | Table l.412–414, l.374 | Session 2 (matches) | Correct. |
| 2,800/year peak; 80% drop to 600 in 2020 (Consul) | l.384, l.477 | Session 2 (matches) | Correct. |
| Ahora Madrid lost mayoralty May 2019 | l.384 | `barandiaran2024decidim` | Citation present and load-bearing — verify the page reference if possible (currently no `p.~`). |
| Polis 8,454 commits, 79 authors | Table l.412–413 | Session 2 (matches) | Correct. |
| Conferences→meetings dep "framework exception" | l.219 | Session 1 confirms gemspec dep | Correct. |
| Borgerforslag is closed-source single-purpose | l.110, l.118, l.512 | No citation; assertion of public fact | Defensible but a footnote to borgerforslag.dk would close the loop. |

## 3. Orphan citations

Round 1 flagged five orphans. Current state checked by `grep` for each bib key in `main.tex`:

- `aragon2017deliberative` — **still orphaned** (0 cites).
- `behrendt2025supporting` — **still orphaned** (0 cites).
- `denardis2009protocol` — **still orphaned** (0 cites). Round-1 review specifically suggested pulling DeNardis into §2.3 for the infrastructure-as-governance bridge; not done.
- `roy2025conversation` — **still orphaned** (0 cites).
- `weyl2025plurality` — **still orphaned** (0 cites). Relevant to Polis discussion in §4.3 / §5.1; not used.

No new orphans introduced. All three new entries flagged in the brief (`gall1998detection`, `jansen2014measuring`, `iansiti2004strategy`) are cited (2, 4, and 1 times respectively).

Fix: drop the five orphans, or use them. Five unused entries in a 33-entry bib is sloppy and will be visible at the surface level.

## 4. FAccT 2025 cite resolution

**Resolved.** The Round-1-flagged FAccT 2025 reference has been removed from Method (no instance of `FAccT` or `facct` in either `main.tex` or `references.bib`). Polis is now cited through `bono2025artificial` (l.366) and the architectural claims are self-anchored via the session logs. Confirmed clean.

## 5. Repo name audit

- `consuldemocracy/consuldemocracy` appears at l.184, l.300, l.309 — correct.
- `consul/consul` appears at l.184 (in the explicit "formerly X" parenthetical) and l.300 (in the rename sentence). Both are legitimate uses describing the rename itself, not stale references.
- `decidim/decidim` at l.203, l.295 — correct.
- `compdemocracy/polis` at l.360 (implicit via "GitHub" rather than full slug) — the Polis URL is not given inline. Minor.

No stale `consul/consul` URLs anywhere. Clean.

## 6. Other findings

**Citation style.** `\citet` and `\citep` are used appropriately throughout. `\citeyearpar` is used twice for IDEA and Manikas 2016 — both correct. `\citet[p.~68]{barandiaran2024decidim}` and `\citet[p.~75]{...}` and `\citet[Fig.~3.1]{...}` show page/figure pinning where load-bearing — good practice. No bare references (e.g., naked "(Author 2024)") found.

**Grey-lit attribution.** OSOR is properly cited as `linaker2025consul`. NTARI is cited as `ntari2025consul`. CEPS and IDEA are bib entries. Codegram is now flagged in Method (l.193) as a Decidim-affiliated source — Round-1 disclosure issue is closed. The l.300 use of the Codegram quote is the most load-bearing partisan-source citation in the paper, and the surrounding prose now does attribute it explicitly ("According to the Codegram architecture blog").

**Methodological-lineage cites.** All present and used in the right places:
- `gall1998detection` — Method l.181 and Analysis l.279. Load-bearing.
- `tyree2005architecture` — Method l.187 (ADR tradition) and Discussion l.495 (Symphony recovery). Slight stretch: Tyree & Akerman cover ADRs but not Symphony specifically; the Symphony attribution at l.495 should probably be a separate cite (Riva 2002 / Stoermer 2004) or rephrased. Flag, not a blocker.
- `manikas2013systematic`, `manikas2016revisiting`, `jansen2014measuring`, `iansiti2004strategy`, `christensen2014analysis` — all used in §2.2 and Analysis. Solid SECO spine.

**Spot-checks of load-bearing citations.**
- `cobos2025comparison` at l.295 and l.374: the paper paraphrases "tends to concentrate on a few contributors" and then explicitly softens this with the comparison data. The framing is honest and the citation supports what it claims.
- `palacin2024configurations` at l.118, l.159, l.479: the "25 distinct configurations across 31 PB cases" number is sourced. The "which political values should be enforced" quote is used three times — borderline overuse, but each instance is doing different work.
- `bono2025artificial` at l.366 carries Polis's lone third-party citation. Round-1 noted Bono et al. is about AI in participation generally, not Polis specifically. Still technically correct (Polis pre-dates the AI-in-participation framing, which is exactly what the paper says), but Polis remains under-cited as a case.

## 7. Prioritized fix list

1. **Drop or use the five orphans** (DeNardis, Weyl, Roy, Aragón, Behrendt). Easiest fix: delete from `references.bib`. Best fix: pull DeNardis into §2.3 (infrastructure-as-governance) and Weyl & Tang into §4.3 or §5.1 (Polis / Plurality).
2. **Cite the Polis "200,000 participants, 26 pieces of legislation" claim at l.114.** This is a hard empirical number with no source. Either find the vTaiwan / g0v / Polis published source, or hedge the number.
3. **Add a Decidim deployment citation at l.114** ("more than 450 institutions in 30 countries") rather than only citing the same number at l.295.
4. **Promote the DESI / UN-E-Gov footnote to proper bib entries** (or accept the footnote as sufficient for an introductory anecdote — defensible but inconsistent with the rest of the paper).
5. **Re-check the Symphony attribution at l.495.** Tyree & Akerman are ADRs, not Symphony recovery; if the Symphony framing is load-bearing add the original Symphony cite, otherwise rephrase.
6. **Optional:** add an inline SHA anchor to the "1,748 stars / 469 forks" GitHub claim at l.295 (the SHA is documented in Session 1 but the prose currently asserts it without anchoring).
