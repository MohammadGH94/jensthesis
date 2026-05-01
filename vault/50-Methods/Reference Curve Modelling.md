---
type: method
name: "Reference Curve Modelling"
techniques: ["GAMLSS", "LMS"]
tags: [method, statistics, reference-intervals]
---

# Reference Curve Modelling

Statistical methods for building age-specific reference curves — moving beyond bin-based reference intervals to **continuous percentile curves**.

## Techniques

- **LMS** (Lambda-Mu-Sigma) — classical method for growth-curve-style references
- **GAMLSS** (Generalized Additive Models for Location, Scale, and Shape) — flexible, handles non-Gaussian and skewed distributions
- **GAIC** (Generalized Akaike Information Criterion) for model selection

## Used in

- [[Chapter 03 - Reference Curves]] — primary methodology chapter
- Outputs feed [[Chapter 05 - Cognitive Resilience]] (percentile binning of [[Super Seniors]]) and [[Chapter 09 - COMPASS-ND Prevalence]] ([[Plasma Probability Scores|RC-PPS]])

## Linked
- [[CHMS]] — input data
- [[Aβ42-40]], [[p-tau-181]], [[NfL]], [[GFAP]] — outputs (one curve per analyte)
