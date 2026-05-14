# Background (Section 2) — round 2 review

## Verdict

Materially stronger than round 1. The four quality attributes are tighter; §2.2 now actually uses Iansiti and Christensen rather than just naming them; §2.3 has stopped pretending to synthesise what it never synthesised. Three problems remain. First, §2.3 is still gap-restatement plus contribution-statement — the conceptual bridge between SA quality attributes and SECO three-structure analysis is still not there. Second, and worse than round 1: the four trade-off costs the paper's central claim hangs on are named three different ways across the abstract, Table 6, and the conclusion, and are not introduced at all in §2.1. Third, the analytical techniques the empirical chapters depend on (logical coupling, fork divergence, contributor concentration, Gini) are still not previewed anywhere in §2. DeNardis 2009 is in the bib and still unused.

## 1. Argument & rigor

§2.3 has been honestly downgraded rather than fixed. Line 161 — "Our contribution is to apply architecture-as-governance using software architecture and SECO methods in civic technology --- a combination that has not been tried" — is announcement, not synthesis. The paper needs one paragraph that says, operationally, how quality attributes and three-structure analysis jointly cash out the architecture-as-governance thesis. The reader is told it will happen and meets Table 7 (l.428) cold.

Christensen 2014 is now substantive — l.149 names the three structures and l.422 makes them the spine of Table 7. Iansiti 2004 is now properly introduced (l.151) and applied in §2.2 itself (Decidim-as-keystone, Madrid-as-dominator). Biggest single improvement since round 1. But keystone/dominator then disappears from Analysis. Jansen's productivity/robustness/niche-creation are named at l.151 and operationalised at l.475, still not *defined* where first used. The §2.2 hypothesis ("the software structure shapes the other two", l.149) is still mid-paragraph and unlabeled even though §4.5 treats it as the tested claim.

The big new problem is the four trade-off costs. The abstract has "(sustainability, autonomy, transparency, ecosystem breadth)" (l.98); the conclusion has "sustainability burden, reduced autonomy, lost transparency, ecosystem thinness" (l.505); Table 6 has "Sustainability burden, partial isolation / Standardization pressure, reduced autonomy / Reduced local control, potential opacity / Design complexity, performance cost" (l.449–452). Three different vocabularies. §2.1 introduces the four *benefits* (l.134) and pairs no costs at all. Single most important fix.

Analytical techniques the empirical chapters depend on — logical coupling (Gall 1998), fork divergence, contributor concentration, Gini, Jaccard — are still not previewed in §2. Gall is cited for the first time in Method (l.181). Round-1 unaddressed.

DeNardis 2009 is at line 77 of the bib and still uncited. The architecture-as-governance spine has a designated infrastructure-as-governance authority sitting unused.

## 2. Clarity & structure

Each subsection now has a clearer job. But §2.3 is still three paragraphs (l.157–161); two recapitulate the introduction and only the third does §2.3-specific work. §2.1 paragraph 2 (l.134) is still one dense block of four italicised-lead-in definitions, asymmetric in length: modifiability gets a full causal chain, interoperability and deployability one sentence each, transparency gets justification-for-inclusion plus example. Real list or rebalance. "Modular monolith" used at l.203 and undefined in §2 — flagged in round 1, still missing. Figure 1 at l.136 introduces the three cases in the same paragraph as the four attributes and forward-references §4.2 — too much forward-pointing for Background.

## 3. Writing style

Most round-1 slop gone. Residuals: l.134 "if they cannot, the platform can only accommodate one way of doing things, which limits how many different communities can use it meaningfully" is two restatements of one point; cut to "if they cannot, only communities whose practices match the platform's defaults can use it." Same line, "Citizens need to understand what the system does and how it handles their input" is filler. L.151 mixes tense ("operates as a keystone" / "functioned more as a dominator"). L.153 "Ecosystem thinking is clearly useful for civic tech, but the literature has a gap" is the same wind-up round 1 flagged, shortened — cut to "The literature has a gap." L.161 says the same hedge three times. "To the best of our knowledge" still appears at l.98 and l.118 with an implicit third pass at l.161.

## 4. Academic conventions

DeNardis 2009 in bib, not cited — unchanged. Schneider 2021 ("Modular Politics") in §5.1 (l.467), not in §2.3 where it would do the most work. Bowker & Star 1999 in §5.1 (l.469), again belongs in §2.3. No Yin / Flyvbjerg / Eisenhardt — "natural experiment" framing (l.190) stands ungrounded. SECO governance literature beyond Jansen on health is absent. The "combination that has not been tried" claim (l.161) is mildly overclaimed; "we have not found prior work combining" matches the rest of the paper's tone.

## Subsection notes

**§2.1 (l.130–143).** Strongest. Bass anchor solid (l.132); commercial-to-democratic pivot is right. Carried problems: four attributes asserted not argued ("especially important", l.132); transparency definition loose; ADRs only in Method; four-attribute paragraph still one block; "modular monolith" undefined. New: the four paired costs are nowhere in §2.1.

**§2.2 (l.145–153).** Most improved. Iansiti now applied; Christensen 2014 now spine of Table 7; Jansen dimensions named and hedged. §2.2 hypothesis (l.149) still buried mid-paragraph. SECO health dimensions still not defined where introduced. OSSECO (l.153) still unexpanded.

**§2.3 (l.155–161).** Weakest, as in round 1. Synthesis absent. Paragraph 1 (l.157) recapitulates intro; paragraph 2 (l.159) is the Barandiaran/Palacin paragraph that fits §2.3 well; paragraph 3 (l.161) is contribution, not bridge. DeNardis, Schneider 2021, Bowker & Star — the citations that would do work here — are all deferred or unused.

## Cross-reference findings

- **Trade-offs named consistently across §2, §4.5, §5, §6?** No. The four attributes are consistent. The four costs are named three different ways and §2.1 names none of them. Central inconsistency.
- **Analytical techniques previewed?** No. Logical coupling, fork divergence, contributor concentration, Gini, Jaccard all first appear in §3.
- **SECO concepts defined where used?** Partly. Three-structure and keystone/dominator are now defined in §2.2. Productivity/robustness/niche-creation named at l.151 but operationalised only at l.475.
- **Christensen 2014 substantive / Iansiti 2004 introduced?** Both yes — proper improvements.

## Round-1 follow-up

| Round-1 fix | Status |
|---|---|
| Rewrite §2.3 as real synthesis (Schneider 2021, DeNardis) | Unaddressed |
| Argue four-attribute selection in §2.1 | Unaddressed |
| Promote §2.2 hypothesis | Partly addressed (used in Table 7 but still unlabeled) |
| Introduce architectural recovery and ADRs in §2.1 | Unaddressed |
| Define SECO health dimensions where introduced | Partly addressed (operational definition at l.475) |
| Define "modular monolith" | Unaddressed |
| Comparative case methodology citation | Unaddressed |
| Cut gap-restatement triplication | Unaddressed |
| Iansiti roles actually used | Addressed in §2.2, but absent from Analysis |
| Christensen 2014 substantive use | Addressed |

Obsolete from round 1: none.

## Prioritized fix list

1. Name the four trade-off costs in §2.1 and use the same names in abstract, Table 6, and conclusion. The conclusion's vocabulary ("sustainability burden, reduced autonomy, lost transparency, ecosystem thinness") is the cleanest; propagate. Single most damaging inconsistency.
2. Add one synthesis paragraph to §2.3 explaining how quality attributes (the SA unit) and three-structure analysis (the SECO unit) jointly operationalise architecture-as-governance. Pull Schneider 2021, DeNardis 2009, and Bowker & Star 1999 forward.
3. Preview the analytical techniques. One sentence in §2.1 on architectural recovery; one in §2.2 on logical coupling, fork divergence, and contributor concentration. Cite Gall 1998 in §2.2, not first in Method.
4. Define "modular monolith" in §2.1 (one sentence).
5. Label the §2.2 hypothesis instead of burying it.
6. Cite DeNardis 2009 in §2.3.
7. Add comparative case method citation (Yin / Flyvbjerg / Eisenhardt) in §2 or §3.
8. Tighten §2.1 paragraph 2: real list or rebalance. Drop the citizen filler sentence at l.134.
9. Cut the gap-restatement triplication. One location only.
