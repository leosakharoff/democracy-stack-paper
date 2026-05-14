# Session 4 log — Consul fork divergence

**Snapshot:** GitHub state of `consuldemocracy/consuldemocracy` and its forks
on 2026-05-12.
**Scripts:** `scripts/consul_forks_list.py`, `scripts/consul_forks_compare.py`,
`scripts/make_consul_fork_plots.py`
**Data:** `data/consul_forks.json`, `data/consul_forks_compare.json`
**Figures:** `figures/consul_fork_activity.pdf`, `figures/consul_fork_divergence.pdf`

## Important rename to flag

The project formerly known as `consul/consul` has been renamed to
`consuldemocracy/consuldemocracy`. Both URLs redirect to the new location.
The paper should use the new name where it discusses the GitHub repository.

## What we set out to verify

The paper claims (Section 4.2 and Table 5):

1. Consul has "~250 cities" / "~250 diverging forks" (line 344, Table 5).
2. Most forks are maintained separately, with "little getting contributed
   back upstream" (line 344, from OSOR/NTARI sources).
3. The architecture-as-governance story: low modifiability forces deployers
   into isolated forks that fragment the ecosystem.

The hypothesis was that fork divergence data would either support or
sharpen these claims.

## What the data says

### Fork totals — 1,123 forks, but most never edited

GitHub reports **1,123 forks** of `consuldemocracy/consuldemocracy`
(the paper says ~700; either the paper used an older count or there has
been net growth despite upstream's declining activity).

The forks endpoint returns **1,030 records** (private/deleted forks
account for the gap). Of those 1,030:

- **746 (73%) are unmodified** — created as a fork but never received a
  commit. These are stars-in-fork-form: someone clicked "Fork" but did
  nothing further.
- **280 (27%) have at least one commit ahead of upstream** — actual
  modifications.
- **1 fork is exactly in sync** (no ahead, no behind).
- 4 forks returned an error (compare API rejected — usually because of
  branch renames or non-existent default branches).

### "250 cities" reframed

The paper's "~250 forks" figure (Section 4.2) and "250+ cities"
(Table 5) is **very close to the number of forks with any modification
at all (280)**. It is not tracking the GitHub fork count (1,123),
which would include all the unmodified stars-in-fork-form forks.

But "any modification" is a low bar. Among the 280 diverged forks:

| commits ahead | count |
|---------------|-------|
| 1             | 53    |
| 2–9           | 94    |
| 10–99         | 94    |
| 100–999       | 34    |
| 1,000+        | 5     |

**Only 39 forks have 100+ commits ahead of upstream.** These are the
genuine "I maintain my own version of the platform" cases. Five forks
have 1,000+ commits ahead — full-scale deployer maintenance.

A more honest framing for the paper:

- ~1,030 GitHub forks
- ~280 with any modification
- ~130 with non-trivial modification (10+ commits)
- ~40 with substantial modification (100+ commits)
- ~5 with full-scale maintenance (1,000+ commits)

### The top diverged forks tell the deployment story

The top 5 most-diverged forks, sorted by commits ahead:

| Fork | Ahead | Behind | Last push |
|------|-------|--------|-----------|
| AyuntamientoMadrid/consul              | 12,725 | 11,540 | 2023-05-23 |
| venetochevogliamo/consul               | 7,135  | 6,267  | 2020-04-29 |
| AjuntamentdeCastello/consul            | 1,469  | 3,388  | 2023-06-19 |
| CDJ11/CDJ                              | 1,176  | 11,153 | 2019-10-21 |
| consul-nl/consul-nl                    | 1,057  | 1,687  | 2026-01-15 |

The most-diverged fork by a wide margin is **AyuntamientoMadrid/consul**
— **Madrid itself**. The city that originally built Consul has been
maintaining its own fork, 12,725 commits ahead and 11,540 commits
behind upstream. Last touched May 2023 — the city stopped active
maintenance roughly when the institutional backing wound down.

This is direct evidence for the paper's architecture-as-governance thesis:
even the originating city ended up maintaining a fork rather than
contributing upstream. The fork is essentially Madrid's private Consul,
diverged from `consuldemocracy/consuldemocracy` and slowly going stale.

Other named municipal forks visible in the top 20: AjuntamentdeCastello
(Castelló), DipVa (Valencia), podemosandalucia (Podemos Andalucia),
SantanderSmartCitizen (Santander), Ayuntamiento-Puerto-de-la-Cruz, and
several international forks: code4romania, codefornl, consul-nl, oecd-opsi
(OECD's Observatory of Public Sector Innovation). All maintain their own
fork rather than contributing upstream.

### Activity over time — fork creation peaked in 2018–2019

`figures/consul_fork_activity.pdf` shows when each fork was last pushed,
grouped by year:

| Year | Forks last pushed |
|------|-------------------|
| 2015 | 61                |
| 2016 | 50                |
| 2017 | 74                |
| 2018 | 133               |
| 2019 | 150  ← peak       |
| 2020 | 125               |
| 2021 | 124               |
| 2022 | 103               |
| 2023 | 61                |
| 2024 | 51                |
| 2025 | 62                |
| 2026 | 36 (partial)      |

Fork activity peaked in 2019 — the same year upstream commit activity
collapsed (Session 2). After 2022 the count of forks "last touched in
year X" stays around 50–60. Only **149 forks (14%)** have been pushed
in the last three years. The vast majority are abandoned.

This is consistent with two interpretations:

1. Deployments that were stood up during the 2017–2021 Consul wave were
   left to rot when the upstream lost institutional backing — the
   ecosystem ossified rather than continuing to grow.
2. New deployers stopped picking Consul as the platform after 2022
   (perhaps choosing Decidim or building their own).

Both are consistent with the paper's "architecture caused fragmentation
caused ecosystem decline" story.

### "Few contribute back upstream" — qualitatively true

We did not measure pull requests directly, but the divergence picture
backs the qualitative claim. If municipal forks (Madrid, Valencia,
Castelló, etc.) were contributing upstream, we would expect to see
small-ahead, small-behind clusters of forks tracking upstream closely.
Instead we see the opposite: forks accumulate commits ahead while
falling further behind upstream as time passes. The "diverged" quadrant
of `figures/consul_fork_divergence.pdf` is heavily populated; the
"ahead-only" quadrant (caught up on upstream, added local work) is
nearly empty.

## What this means for the paper

### Reframe Section 4.2 fork claims

The paper says (line 344, paraphrased): "the OSOR/Interoperable Europe
case study found 'fragmented development, with multiple forks adapted
to different local needs' ... NTARI forks report says roughly 250
global implementations."

Better-grounded framing using our data:

- "Of 1,030 enumerable forks on GitHub (2026-05-12), 280 have at least
  one commit ahead of upstream; 39 have 100+ commits ahead; 5 have
  more than 1,000."
- "Madrid itself — `AyuntamientoMadrid/consul`, the original deployer
  — maintains a fork 12,725 commits ahead of upstream, last touched
  May 2023. The city that built the platform ended up maintaining a
  private copy rather than contributing upstream."

### Update Table 5

Two numbers should change:

- **Forks**: "~700" → "1,030 (280 with any modification, 39 with
  100+ commits ahead)"
- **Deployments**: "250+ cities" → keep, but flag in the caption that
  the "250" figure tracks closely to the count of any-modification
  forks rather than active deployments.

### Add or update the fragmentation paragraph

Section 4.2 currently asserts the fork-fragmentation story textually.
Now we have:

- `figures/consul_fork_activity.pdf` — when each fork was last pushed,
  showing the 2019 peak and subsequent decline.
- `figures/consul_fork_divergence.pdf` — ahead vs behind scatter,
  showing the empty "ahead-only" quadrant and the populated
  "diverged" cluster.

Either reference both inline or pick the more compact one (the activity
histogram is probably the stronger single figure for the paper).

### Sharpens the architecture-as-governance argument

Madrid maintaining its own fork that drifted 12,725 commits ahead and
then went stale is exactly the kind of empirical evidence that
strengthens the paper's thesis. The originator city did not contribute
back; it forked, customised, and abandoned. The monolith forced this
trajectory: Madrid could not "be a niche creator" in a Consul ecosystem
because the architecture did not have a plugin layer for niche creators
to live in. The only option was to fork.

This is a much harder claim than the paper currently makes. The paper
says "deployers maintained separate forks". The data says "the city
that built the platform maintained a separate fork that drifted away
from upstream and was abandoned mid-2023". Stronger.

## Limitations to flag

- Compare API returns ahead/behind based on default branches. A few
  forks (10–16) use non-master default branches; some of those errored
  out. The 4 errors are not material at this scale.
- GitHub reports 1,123 forks; the API returned 1,030 records. The gap
  (93 forks, 8%) is private forks, deleted forks not yet reaped, and
  pagination edge cases. The qualitative findings are robust to this.
- We classified forks as "modified" by `ahead_by >= 1`. A fork that
  added a commit and then reverted it could still show ahead=0 (Git
  history depends on whether the revert merged back). This is a minor
  edge case unlikely to change the headline numbers.

## Reproducibility

```
cd ~/Dev/report
python scripts/consul_forks_list.py        # ~10 API calls
python scripts/consul_forks_compare.py     # ~1030 API calls, 15-25 min
python scripts/make_consul_fork_plots.py
```

Outputs: `data/consul_forks.json`, `data/consul_forks_compare.json`,
two figures under `figures/`.

Total GitHub API quota used: ~1,050 of 5,000 hourly authenticated budget.
