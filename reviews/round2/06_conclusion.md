# Review (Round 2): Conclusion (§6, lines 503–518) + Use of GenAI (§7, lines 524–537)

## Verdict

The conclusion is tighter than in round 1 and now leans on the empirical work in §4 — the 7,000 / 14,000 / 8,000 commit framing in line 507 is earned, not asserted. But two of the round-1 problems are not fixed: the "clearest demonstration" mantra is still there (line 509), and the "architecture is not a procurement detail" plus "SECO needs a normative layer" claims still appear in the conclusion before the discussion has properly built them. The Denmark coda still does its job. GenAI statement is honest and specific. Future work is concrete.

## 1. Argument & rigor

The RQ from line 120 is restated at line 505 and answered with the four trade-offs naming. Clean.

The "clearest demonstration" line is still in. Line 509: "The Decidim/Consul divergence --- same origin, opposite architecture, radically different ecosystem outcomes --- is the clearest demonstration." This phrase or a near-copy now appears at lines 98 (abstract), 122 (intro), 457 (synthesis), 467 (discussion), and 509. Five times. §5.4 line 491 explicitly concedes "architecture was not the only thing that differed" — Madrid's Ahora government lost power in 2019. The conclusion does not carry that hedge forward. Round-1 finding stands.

The "architecture is not a procurement detail --- it is a governance choice" line (509) is still smuggled in. §5.3 (line 485) talks about democracy stack implications but never frames the procurement-vs-governance opposition. The sharpest rhetorical move in the paper still appears for the first time in the conclusion.

The "SECO research needs a normative layer" claim (line 509) is the same upgrade as round 1. §5.2 (line 479) frames it carefully — "adds an evaluative layer" — but the conclusion upgrades it to a prescriptive claim about what SECO research needs. §5.2 line 475 also concedes the SECO health framework was applied "as qualitative lenses rather than with their full operationalized measurement frameworks," which is the opposite of being in a position to prescribe what SECO needs.

The Madrid 12,725-commits-ahead number is *not* in the conclusion (it is in §4.2 line 311 and §5.1 line 467). Good — that was a round-1 risk, now avoided.

Empirical grounding inside the conclusion is much stronger than round 1: line 507 names "7,000 commits of Decidim modules, 14,000 commits of Consul fragmenting into 280 modified forks, 8,000 commits of Polis dominated by one developer." All three numbers trace back to §4 (the 7,078 / 14,372 / 8,454 in Table 3, line 412). This is a real improvement.

Future work (lines 517–518) is concrete, tied to §5.4 explicitly, and offers two named directions (stakeholder interviews; design science for a Nordic municipality). No "further research is needed." Genuinely good.

Limitations (lines 514–515) are honest and specific: depth asymmetry across cases is named, the 25-platform field is acknowledged, Adhocracy and LiquidFeedback get a specific shout-out, GitHub-as-proxy is conceded, and the analytical-not-empirical mapping is owned. This is the strongest paragraph in the section.

## 2. Clarity & structure

Length (16 lines plus headers) is right for a 7.5 ECTS paper. No padding.

Contribution is still not stated in one breath. The reader has to assemble it from line 505 (four trade-offs), line 509 (three different claims jammed into one paragraph), and the Denmark coda. A single "this paper contributes X" sentence would close the deal.

Some duplication with the abstract remains. Line 98 ("provides the strongest evidence that architectural decisions in civic tech function as governance decisions") vs. line 509 ("the clearest demonstration"). Round 1 flagged this; unchanged.

The "Returning to Denmark" coda (lines 511–512) still works — closes the loop the intro opened, and "The architecture is the democratic decision" (line 512) is the strongest sentence in the section.

## 3. Writing style

Em-dash discipline has *not* improved. Line 505 uses dashes three times in one paragraph; line 509 uses them four times; line 511 uses one; line 515 uses two. Several are crutches for commas or colons: "lenses on the architectural decisions in each case. Each attribute trades off against..." would read cleaner as plain prose. The first dash in line 509 ("same origin, opposite architecture, radically different ecosystem outcomes") earns its keep — the parenthetical aside is the right tool. The others are filler.

No "In summary," no "This paper has shown," no "comprehensive analysis." Good.

Line 507 is borderline filler: "These are not abstract observations." Defensive throat-clearing — nobody accused them of being abstract. The follow-up sentence ("If Copenhagen, or any European city...") still hedges Copenhagen with "any European city," which defangs the specificity that round 1 flagged. Unchanged.

"a decade of civic tech experience --- 7,000 commits..." (line 507) is better than round 1 because it now hangs concrete numbers off the abstract phrase. The numbers do real work.

## 4. Academic conventions

Hedging is appropriate in limitations and absent everywhere else. Lines 509 and 512 read as confident pronouncements ("the clearest demonstration," "the architecture is the democratic decision") without an n=3 hedge. Line 491's political-confound concession is not carried forward.

Honest contribution framing is *partial*. The "SA/SECO methods applied to civic tech" claim is defensible and well-supported. The "SECO research needs a normative layer" claim still overreaches given §5.2's explicit hedge.

Future work tied to actual gaps. Yes — both directions in line 518 cite §5.4 (\ref{sec:evaluation}).

## Use of Generative AI statement (§7, lines 524–537)

Substantially better than the boilerplate norm. Specifics that help: model versions are named (claude-sonnet-4-20250514, claude-opus-4-20250514) at line 527; access channel is named (Claude desktop, Cowork mode); five use categories are enumerated at line 529; a sample prompt formulation is given at line 531; and an explicit author/AI line is drawn at line 533.

The figure-generation honesty gap from round 1 is **not** fixed. Line 529 still says "LaTeX formatting and figure generation." The git history (recent commits "Replace TikZ tensions diagram with matplotlib-generated PDF" etc.) shows AI wrote Python plotting code, which is more honest than "figure generation" — that phrasing could be read as the AI drawing the figures itself.

The "literature search and synthesis --- identifying relevant papers and summarizing their arguments" item (line 529) shades into analytical work, and line 533's blanket "all analytical claims developed by the author" is in mild tension with it. A supervisor will press on this. Not dishonest, but the line is doing more work than it admits.

Copyrighted-material clause (line 535) is sensible.

## Cross-reference findings

- Four trade-offs naming consistent: §6 line 505 (modifiability, interoperability, deployability, transparency) matches abstract line 98, §2 (background), §4.5 Table 4 line 446, and §5. Consistent across the paper.
- §6 claims traceable to §4: mostly yes. The 7,000 / 14,000 / 8,000 / 280 figures all trace to §4. The two exceptions are the "SECO needs a normative layer" claim (only in §5.2, hedged) and "architecture is not a procurement detail" (nowhere in the body). These remain new in §6.
- §1 RQ phrasing: line 120's "what software architecture trade-offs must builders of democratic digital infrastructure navigate, and what can we learn from the architectural decisions in existing civic tech ecosystems?" is answered at line 505 with the four trade-offs and the cross-case reading. Good match.

## Round-1 follow-up

| Round-1 finding | Status |
|---|---|
| "Clearest demonstration" line still present, five times in paper | **Unaddressed** (still line 509) |
| "Architecture is not a procurement detail" smuggled in | **Unaddressed** (still line 509, still not in §5.3) |
| "SECO needs a normative layer" upgrade not earned in §5.2 | **Unaddressed** (still line 509; §5.2 line 479 is still hedged) |
| Filler line "These are not abstract observations" | **Unaddressed** (now line 507) |
| Copenhagen specificity defanged by "or any European city" | **Unaddressed** (line 507) |
| Contribution not stated in one sentence | **Unaddressed** |
| Duplication with abstract on "clearest"/"strongest evidence" | **Unaddressed** |
| Future work concrete and tied to §5.4 | **Addressed** (already strong in round 1, still strong) |
| Limitations honest and specific | **Addressed** (now even more specific: 25 platforms, Adhocracy, LiquidFeedback) |
| GenAI: figure-generation phrasing too vague | **Unaddressed** (line 529 still says "figure generation") |
| GenAI: model names, channel, use enumeration | **Addressed** (already strong; unchanged) |
| Empirical grounding inside conclusion | **Addressed** (numbers in line 507 now do real work) |

Net: limitations and empirical anchoring improved. The rhetorical-overreach findings are all still live.

## Prioritized fix list

1. **Drop or hedge "clearest demonstration" in line 509.** Five repetitions across the paper. §5.4 line 491 already conceded the case isn't architecturally pure. "The most legible example, given the political-context caveat in §5.4" would be honest.
2. **Move "architecture is not a procurement detail" into §5.3.** Strongest policy line in the paper. It should not appear for the first time on the last page.
3. **Either earn the "SECO normative layer" prescription in §5.2 or downgrade it in §6.** As written, §5.2 hedges and §6 prescribes. Pick one.
4. **Cut line 507's "These are not abstract observations" sentence.** Defensive throat-clearing. The Copenhagen point can be one declarative sentence.
5. **Add a single contribution sentence.** "This paper contributes (i) the first SA/SECO analysis of civic tech and (ii) four named trade-offs that democracy-stack builders must navigate." Then the Denmark coda.
6. **Fix "figure generation" in line 529.** Say "AI generated Python/matplotlib code that produced the figures" — matches the commit history.
7. **Em-dash audit on lines 505, 509, 515.** Roughly half the dashes are commas in disguise. Keep the parenthetical asides; replace the colon/comma substitutes.
8. **Decide whether "summarizing their arguments" in line 529 contradicts "analytical claims developed by the author" in line 533.** Either re-word line 529 (e.g., "locating relevant papers; the author wrote the synthesis") or add a sentence to line 533 acknowledging that argument summaries were AI-drafted and author-validated.
