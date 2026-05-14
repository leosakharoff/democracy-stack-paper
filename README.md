# Building the Democracy Stack

> What software architecture decisions matter for democratic digital infrastructure?

Research project (7.5 ECTS) at the IT University of Copenhagen, MSc Software Design (KIREPRO1PE, Spring 2026).

A comparative case study of Decidim and Consul — two civic technology platforms with shared origins in Spain's 15M movement but opposite architectural paths — through a software architecture quality-attribute framework, Christensen et al.'s three-structures lens, and a fork-divergence shape diagnostic.

## Read the paper

**[LeoSakharov_ResearchProject_KIREPRO1PE_2026.pdf](./LeoSakharov_ResearchProject_KIREPRO1PE_2026.pdf)**

## Repository contents

| Path | Description |
|---|---|
| `main.tex` | Paper source (LaTeX) |
| `references.bib` | Bibliography |
| `figures/` | Generated figures (PDF) |
| `data/` | Empirical data: engine dependencies, commit metadata, fork populations |
| `scripts/` | Analysis scripts: architectural recovery, evolutionary analysis, fork-divergence |
| `logs/` | Session findings logs |

## Reproducibility

Upstream snapshots used for the analysis:

- Decidim: [`decidim/decidim`](https://github.com/decidim/decidim) at `be39c244` (2026-05-12)
- Consul: [`consuldemocracy/consuldemocracy`](https://github.com/consuldemocracy/consuldemocracy) at `3c3b5c4a` (2026-05-11)

Scripts in `scripts/` operate on the data in `data/` to regenerate the figures and findings reported in the paper.

## Author

Leo William Engholm Sakharov
Supervisor: Konstantinos Manikas
IT University of Copenhagen, 2026
