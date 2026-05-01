---
type: method
name: "LASSO and Elastic Net"
tags: [method, statistics, feature-selection]
---

# LASSO and Elastic Net

Penalised regression methods for feature selection on the [[NULISA]] multiplex panel — needed because there are far more proteins than samples.

## Used in

- [[Chapter 08 - Co-pathologies]]:
  - **LASSO** — single-pathology models (n = 84) for α-syn, [[TDP-43 Pathology|TDP-43]], CVD
  - **Elastic net** — co-pathology models within ADNC cases (n = 56)

## Why both

LASSO sparsifies hard; elastic net keeps correlated features together. The choice depends on whether the goal is parsimony or coverage.
