---
type: map
title: "Brain Map — full thesis graph"
tags: [map, mermaid, graph]
---

# Brain Map

A Mermaid-rendered "brain map" of the thesis. View this in [Obsidian](https://obsidian.md), GitHub (which renders Mermaid natively), or any Markdown viewer with Mermaid support.

For an interactive force-directed version, open [`vault-graph.html`](../../vault-graph.html) at the repo root in a browser.

## Whole-thesis graph

```mermaid
graph LR
    %% ----- styling -----
    classDef chapter   fill:#1f77b4,stroke:#0b3d69,color:#fff,stroke-width:1px;
    classDef biomarker fill:#d62728,stroke:#7a1414,color:#fff;
    classDef cohort    fill:#2ca02c,stroke:#0f4f0f,color:#fff;
    classDef disease   fill:#9467bd,stroke:#4b2c66,color:#fff;
    classDef method    fill:#ff7f0e,stroke:#8a4304,color:#fff;
    classDef concept   fill:#17becf,stroke:#0a6770,color:#fff;
    classDef person    fill:#7f7f7f,stroke:#3d3d3d,color:#fff;

    %% ----- chapters -----
    C1[Ch 1<br/>Introduction]:::chapter
    C2[Ch 2<br/>Reference Intervals]:::chapter
    C3[Ch 3<br/>Reference Curves]:::chapter
    C4[Ch 4<br/>Cross-Lot QC]:::chapter
    C5[Ch 5<br/>Cognitive Resilience]:::chapter
    C6[Ch 6<br/>APOE4 and p-tau-181]:::chapter
    C7[Ch 7<br/>Autopsy ADNC]:::chapter
    C8[Ch 8<br/>Co-pathologies]:::chapter
    C9[Ch 9<br/>COMPASS-ND Prevalence]:::chapter
    C10[Ch 10<br/>Discussion]:::chapter

    %% ----- biomarkers -----
    AB[Aβ42/40]:::biomarker
    PT[p-tau-181]:::biomarker
    NF[NfL]:::biomarker
    GF[GFAP]:::biomarker

    %% ----- cohorts -----
    CHMS([CHMS — normative]):::cohort
    SS([Super Seniors]):::cohort
    CARD([CARD — autopsy]):::cohort
    CND([COMPASS-ND]):::cohort

    %% ----- methods / platforms -----
    SIM{{Quanterix Simoa}}:::method
    AL{{Alamar ARGO / NULISA}}:::method
    RC{{Reference Curve Modelling<br/>GAMLSS / LMS}}:::method
    LE{{LASSO / Elastic Net}}:::method

    %% ----- diseases / pathology -----
    AD>"Alzheimer's Disease"]:::disease
    FTD>"FTD"]:::disease
    DLB>"DLB"]:::disease
    VAD>"Vascular Dementia"]:::disease
    ADNC>"ADNC"]:::disease
    COP>"Co-pathologies"]:::disease
    TDP>"TDP-43"]:::disease

    %% ----- concepts -----
    ATN[/ATN Framework/]:::concept
    RES[/Cognitive Resilience/]:::concept
    APOE[/APOE4/]:::concept
    PPS[/Plasma Probability Scores/]:::concept
    CIC[/Clinical Implementation in Canada/]:::concept

    %% ----- chapter flow -----
    C1 --> C2 --> C3 --> C4
    C4 --> C5 --> C6
    C6 --> C7 --> C8 --> C9 --> C10

    %% ----- biomarkers measured by chapters -----
    C2 --- AB & PT & NF & GF
    C3 --- AB & PT & NF & GF
    C5 --- AB & PT & NF & GF
    C7 --- AB & PT & NF & GF
    C9 --- AB & PT & NF & GF

    %% ----- cohorts used by chapters -----
    C2 -.uses.-> CHMS
    C3 -.uses.-> CHMS
    C5 -.uses.-> SS
    C5 -.compares to.-> CHMS
    C6 -.uses.-> SS
    C7 -.uses.-> CARD
    C8 -.uses.-> CARD
    C9 -.uses.-> CND
    C9 -.derives RC-PPS from.-> CHMS
    C9 -.derives ADNC-PPS from.-> CARD

    %% ----- methods used by chapters -----
    C2 -.platform.-> SIM
    C3 -.modelled by.-> RC
    C4 -.platform.-> SIM
    C5 -.platform.-> SIM
    C6 -.platform.-> SIM
    C7 -.platform.-> SIM
    C7 -.platform.-> AL
    C8 -.platform.-> AL
    C8 -.method.-> LE
    C9 -.platform.-> SIM

    %% ----- diseases addressed -----
    C1 --- AD & FTD & DLB & VAD
    C7 --- ADNC
    C8 --- COP & TDP

    %% ----- concept anchors -----
    C1 -.introduces.-> ATN
    C5 -.embodies.-> RES
    C6 -.modulated by.-> APOE
    C9 -.delivers.-> PPS
    C10 -.synthesises into.-> CIC
    PPS --> CIC

    %% ----- biomarker → concept -----
    AB --> ATN
    PT --> ATN
    NF --> ATN
```

## Reading the map

- **Blue rectangles** = chapters (the spine, left to right)
- **Red rectangles** = the four canonical plasma biomarkers
- **Green ovals** = cohorts
- **Orange hexagons** = methods / platforms
- **Purple flags** = diseases / pathologies
- **Teal parallelograms** = unifying concepts

The chapter flow runs C1 → C10 across the top; everything else attaches to chapters.

## Smaller views

If the full graph is too dense, see:

- [[Map - Chapters and Cohorts]]
- [[Map - Biomarkers and Pathology]]

## Per-chapter detailed maps

One Mermaid map per chapter showing sub-section structure, methods, key findings, and forward links:

- [[Chapter 01 - Map]] — Introduction (12 sub-sections, biomarker/method anchors)
- [[Chapter 02 - Map]] — Reference Intervals (U-shaped curves, cross-lot agreement)
- [[Chapter 03 - Map]] — Reference Curves (GAMLSS/LMS, web app, sex-modified p-tau-181)
- [[Chapter 04 - Map]] — Cross-Lot QC (within/between-lot bias, harmonisation)
- [[Chapter 05 - Map]] — Cognitive Resilience (38% biomarker-super, female enrichment)
- [[Chapter 06 - Map]] — APOE4 × p-tau-181 (published)
- [[Chapter 07 - Map]] — Autopsy ADNC (AUROCs 0.84/0.88/0.91, Thal/Braak/CERAD/ABC)
- [[Chapter 08 - Map]] — Co-pathologies (LASSO α=1, elastic-net α=0.5, NULISA 120-plex)
- [[Chapter 09 - Map]] — COMPASS-ND Prevalence (RC-PPS + ADNC-PPS pipeline)
- [[Chapter 10 - Map]] — Discussion (Canadian implementation pull-throughs)
