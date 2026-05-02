---
type: map
title: "Map — Biomarkers × Pathology"
tags: [map, mermaid, biomarkers, pathology]
---

# Map — Biomarkers × Pathology

How the four canonical biomarkers map onto pathology axes.

```mermaid
graph LR
    classDef biomarker fill:#d62728,stroke:#7a1414,color:#fff;
    classDef pathology fill:#9467bd,stroke:#4b2c66,color:#fff;
    classDef concept   fill:#17becf,stroke:#0a6770,color:#fff;

    AB[Aβ42/40]:::biomarker
    PT[p-tau-181]:::biomarker
    NF[NfL]:::biomarker
    GF[GFAP]:::biomarker

    AMY>"Amyloid plaques"]:::pathology
    TAU>"Tau tangles"]:::pathology
    NEU>"Neurodegeneration"]:::pathology
    INF>"Astrogliosis / inflammation"]:::pathology
    SYN>"α-synuclein"]:::pathology
    TDP>"TDP-43"]:::pathology
    CVD>"Cerebrovascular"]:::pathology

    A[/A — Amyloid/]:::concept
    T[/T — Tau/]:::concept
    N[/N — Neurodegeneration/]:::concept

    AB --> AMY --> A
    PT --> TAU --> T
    NF --> NEU --> N
    GF --> INF
    GF --> NEU
    GF -.elevated in.-> CVD
    NF -.elevated in.-> CVD

    %% multiplex panel covers what canonical four don't
    PANEL{{"NULISA panel<br/>Ch 7, 8"}}
    PANEL -.detects.-> SYN
    PANEL -.detects.-> TDP
    PANEL -.detects.-> CVD
```

The four canonical biomarkers cover [[ATN Framework|ATN]] for AD; α-syn, [[TDP-43 Pathology|TDP-43]], and CVD require the multiplex panel — see [[Chapter 08 - Co-pathologies]].
