# Session 2 log — Evolutionary analysis

**Snapshots:**
- `decidim/decidim @ be39c244` (2026-05-12)
- `consul/consul @ 3c3b5c4a` (2026-05-11)
- `compdemocracy/polis @ e8c2b46d` (2026-04-26)

**Scripts:** `scripts/evolutionary_analysis.py`, `scripts/make_evolution_plots.py`
**Data:** `data/evolutionary.json`
**Figures:** `figures/contributor_concentration.pdf`, `figures/commit_timeline.pdf`, `figures/decidim_engine_activity.pdf`

## What we set out to verify

The paper makes several ecosystem-health claims:

1. Decidim is a "productive" ecosystem with broad participation (Section 4.1, 5.2).
2. Cobos2025 claim that Decidim activity "concentrates on a few contributors" (line 330).
3. Consul deployers maintain "isolated forks" with "little getting contributed back upstream" (Section 4.2).
4. Polis has a "thin contributor ecosystem" (Section 4.3).
5. Consul's institutional backing collapsed when Ahora Madrid lost power in 2019 (Section 5.4).

The first four are framed as architecture-as-governance consequences. The fifth is mentioned as a causal complication (politics, not just architecture).

## Method

For each repo we used `git log --no-merges` to extract author/email/date for every commit. Authors classified as bots if email matches dependabot, crowdin, weblate, github-actions, `[bot]@` patterns, or if name contains "bot", "crowdin", "weblate". Human commits aggregated by lowercase email (canonical identity).

Metrics:
- Total commits (no merges), split human vs bot
- Unique human authors
- First/last human commit dates
- Top-3 and top-10 contributor share (bus-factor proxies)
- Gini coefficient on the commit distribution
- Commits per year

For Decidim only: per-engine commit counts via `git rev-list --count HEAD -- decidim-*/`.

## Findings

### Contributor concentration — all three are top-heavy, Decidim is the most distributed

| Repo    | Humans | Top-3 share | Top-10 share | Gini |
|---------|--------|-------------|--------------|------|
| Decidim | 7,078  | **36%**     | **68%**      | 0.85 |
| Consul  | 14,372 | 52%         | 87%          | 0.93 |
| Polis   | 8,454  | 82%         | 97%          | 0.94 |

Open-source ecosystems usually have a long tail with top-heavy distribution (Gini 0.7–0.95 is common). All three are within that range.

**Within the comparison**:

- **Polis is extremely concentrated.** Top 3 authors did 82% of all human commits. Top 10 did 97%. Mike Bjorkegren alone has 4,699 commits — 56% of the entire history. Polis is a 1–2 person project with sporadic external contributions. **Strongly supports the paper's "thin contributor ecosystem" claim.**

- **Consul is also highly concentrated** despite having a similar number of unique authors as Decidim (186 vs 183). Top 3 = 52%, top 10 = 87%. Javi Martín alone has 3,923 commits (27% of all human commits) — the Madrid municipal team's signature.

- **Decidim is the most distributed.** Top 10 share 68% (versus 87%/97% for the others). 953 commits/author at peak, but the top 5 are within a 956–537 range — no single dominant author. This refines Cobos2025: the framing "activity concentrates on a few contributors" is directionally right, but Decidim is *relatively* the most distributed of the three.

### Commit timeline — Consul's 2019 cliff is empirically visible

`figures/commit_timeline.pdf` shows human commits per year. Three patterns:

- **Consul** ramps fast 2015 → peaks at ~2,800/year 2017–2019 → **drops 80% to 600/year in 2020**, slow further decline since. The 2019 → 2020 cliff is striking and matches the paper's claim about Ahora Madrid losing the Madrid mayoralty in 2019. This is no longer anecdote — the timeline plot is direct evidence.

- **Decidim** starts late 2016, ramps to ~1,200/year 2017–2018, drops in 2019 (450/year), then **stabilises around 600–770/year 2020–2025**. A steady plateau is unusual for OSS projects — they typically follow a hump-shaped curve. Decidim's stability is a real artefact, worth flagging.

- **Polis** spikes hard in 2013–2014 (peaks at 2,650 in 2014 alone — likely the initial vTaiwan engagement era), drops sharply by 2017, and stays at 50–340/year for almost a decade. Anomalous bounce to 1,000 in 2025 (worth investigating in a future pass — likely Mike Bjorkegren doing a focused sprint).

### Decidim per-engine activity — modularity is alive across the board

`figures/decidim_engine_activity.pdf`. All 24 user-facing engines have commits in the last 12 months. The distribution:

- `core` leads at 332 last-12mo commits (3,892 all-time)
- `proposals`, `admin`, `meetings` cluster at ~140/year
- The four spaces (`processes`, `assemblies`, `initiatives`, `conferences`) all 87–120/year — balanced
- Three brand-new engines visible in the data: `decidim-demographics` (32 all-time, all in the last 12 months), `decidim-ai` (22 all-time), `decidim-collaborative_texts` (66 all-time, 53 in last 12 months). Lehman's law in action — the platform is absorbing new feature areas as the world changes around it.
- No dormant engines. The modular architecture is matched by modular maintenance.

This is good evidence for the paper's "productive ecosystem with module-level activity" framing. The asymmetric pattern is genuinely informative — `core` and `proposals` dominate, but ten other engines see 80+ commits/year.

## What this means for the paper

### New analysis to add (Section 4.1 and/or new subsection)

**Add an "Ecosystem evolution" subsection** to Section 4 (Analysis), probably as 4.4 (Synthesis) or as a new 4.4 before Synthesis. Three figures, ~half a page of prose. Headline numbers:

- Decidim: 7,078 human commits across 183 authors since 2016; top-10 share 68%; modular maintenance verified across all 24 user-facing engines.
- Consul: 14,372 human commits across 186 authors since 2015; top-10 share 87%; cliff-pattern timeline with the drop in 2019.
- Polis: 8,454 human commits across 79 authors since 2012; top-10 share 97%; one-developer-dominated.

### Refines existing claims

- **Cobos2025 reference** (line 330) is correct directionally but understates. The paper currently reads as if Decidim has a concerning concentration; in fact Decidim's concentration is mild relative to the comparison cases. Suggest: cite Cobos with a comparative softener — "even Decidim's concentration (top-10: 68%) is markedly lower than Consul's (87%) or Polis's (97%)".

- **Madrid 2019 collapse** (Section 5.4) — currently a textual claim. Now backed by a visible cliff in `commit_timeline.pdf`. Either reference the figure inline or move the discussion to where the figure sits.

- **"Thin contributor ecosystem" claim for Polis** (Section 4.3) is correct and quantifiable: 79 unique authors, top-3 = 82%.

### Method section additions

- Mention the evolutionary procedure briefly: "We extracted commit metadata via `git log --no-merges` on partial clones (`--filter=blob:none`), filtered automation by author email pattern, and computed contributor concentration (top-N share, Gini), per-year commit timelines, and (for Decidim) per-engine activity."
- List the three pinned SHAs in the snapshot statement.

### Outstanding questions / future work

- **Polis 2025 spike (1,000 commits, up from <200 the prior year).** Likely a single sprint by one author. Worth a sentence acknowledging the anomaly rather than smoothing over it.
- **Logical coupling on Decidim** (Session 3) will test whether the modular architecture is matched by modular *change patterns* — i.e., do engines actually evolve independently, or do they co-change despite the gem boundaries? The shared-DB tension is the empirical hypothesis.
- **Consul fork divergence** (Session 4) will quantify the "isolated forks, no upstream contributions" claim.

## Reproducibility

```
git clone --filter=blob:none https://github.com/decidim/decidim.git ~/Dev/decidim
git clone --filter=blob:none https://github.com/consul/consul.git ~/Dev/consul
git clone --filter=blob:none https://github.com/compdemocracy/polis.git ~/Dev/polis
# Then in each clone:
#   git checkout <SHA listed above>
cd ~/Dev/report
python scripts/evolutionary_analysis.py ~/Dev/decidim ~/Dev/consul ~/Dev/polis
python scripts/make_evolution_plots.py
```
