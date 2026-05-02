---
type: chapter-map
chapter: 1
title: "Chapter 1 Map — Introduction"
tags: [map, mermaid, chapter-detail, introduction]
---

# Chapter 1 — Detailed Map

The chapter's full sub-section structure with cross-references into other chapters and the canonical entity notes.

## Section structure

```mermaid
graph TD
    classDef sec    fill:#1f77b4,stroke:#0b3d69,color:#fff,stroke-width:1px;
    classDef sub    fill:#2a4d70,stroke:#0b3d69,color:#cfe2ff;
    classDef ent    fill:#d62728,stroke:#7a1414,color:#fff;
    classDef coh    fill:#2ca02c,stroke:#0f4f0f,color:#fff;
    classDef meth   fill:#ff7f0e,stroke:#8a4304,color:#fff;
    classDef con    fill:#17becf,stroke:#0a6770,color:#fff;
    classDef link   fill:#444,stroke:#222,color:#fff,stroke-dasharray:3 3;

    %% backbone
    C1[Ch 1 · Introduction]:::sec
    S11[1.1 Summary]:::sec
    S12[1.2 Alzheimer's Disease]:::sec
    S13[1.3 Neuropathology of AD]:::sec
    S14[1.4 Treatment of AD]:::sec
    S15[1.5 Non-AD Dementias]:::sec
    S16[1.6 Dementia Resilience]:::sec
    S17[1.7 Current Diagnosis of AD/ADRD]:::sec
    S18[1.8 Neurological Blood-Based Biomarkers]:::sec
    S19[1.9 Analytical Technologies]:::sec
    S110[1.10 Current Use and Implementation]:::sec
    S111[1.11 Pathway to Clinical Implementation]:::sec
    S112[1.12 Hypothesis and Objectives]:::sec

    C1 --> S11 --> S12 --> S13 --> S14 --> S15 --> S16 --> S17 --> S18 --> S19 --> S110 --> S111 --> S112

    %% 1.2 AD sub
    S121[1.2.1 Epidemiology]:::sub
    S122[1.2.2 Clinical Presentation and Variants]:::sub
    S123[1.2.3 Risk factors]:::sub
    S12 --> S121 & S122 & S123

    %% 1.3 Neuropathology sub
    S131[1.3.1 Amyloid Pathology]:::sub
    S132[1.3.2 Tau Pathology]:::sub
    S133[1.3.3 Neurodegeneration]:::sub
    S134[1.3.4 Neuroinflammation]:::sub
    S13 --> S131 & S132 & S133 & S134

    %% 1.4 Treatment
    S141[1.4.1 Disease-modifying therapies]:::sub
    S14 --> S141

    %% 1.5 Non-AD
    S151[1.5.1 Frontotemporal Dementias]:::sub
    S152[1.5.2 Dementia with Lewy Bodies]:::sub
    S153[1.5.3 Vascular Dementia]:::sub
    S154[1.5.4 Co-pathologies Across Dementias]:::sub
    S15 --> S151 & S152 & S153 & S154

    %% 1.7 Diagnosis
    S171[1.7.1 Cognitive testing]:::sub
    S172[1.7.2 ATN Framework]:::sub
    S173[1.7.3 Neuroimaging]:::sub
    S174[1.7.4 Fluid Biomarkers]:::sub
    S17 --> S171 & S172 & S173 & S174

    %% 1.8 Blood biomarkers
    S181[1.8.1 Amyloid Beta]:::sub
    S182[1.8.2 Phosphorylated Tau]:::sub
    S183[1.8.3 Neurofilament Light]:::sub
    S184[1.8.4 Glial Fibrillary Acidic Protein]:::sub
    S18 --> S181 & S182 & S183 & S184

    %% 1.9 Tech
    S191[1.9.1 Quanterix Simoa]:::sub
    S192[1.9.2 Alamar ARGO]:::sub
    S193[1.9.3 Clinical platforms]:::sub
    S19 --> S191 & S192 & S193

    %% 1.10 Use
    S1101[1.10.1 AD Blood Biomarkers]:::sub
    S1102[1.10.2 Other Dementias]:::sub
    S1103[1.10.3 Other Contexts]:::sub
    S110 --> S1101 & S1102 & S1103

    %% 1.11 Pathway
    S1111[1.11.1 Implementation of lab tests]:::sub
    S1112[1.11.2 Clinical validation]:::sub
    S1113[1.11.3 Canadian-specific approval]:::sub
    S111 --> S1111 & S1112 & S1113

    %% 1.12 Objectives
    S1121[1.12.1 Summary]:::sub
    S1122[1.12.2 Research hypothesis]:::sub
    S1123[1.12.3 Specific objectives]:::sub
    S112 --> S1121 & S1122 & S1123
```

## Concepts introduced in Ch 1 and where they're operationalised

```mermaid
graph LR
    classDef sub  fill:#2a4d70,stroke:#0b3d69,color:#cfe2ff;
    classDef ent  fill:#d62728,stroke:#7a1414,color:#fff;
    classDef coh  fill:#2ca02c,stroke:#0f4f0f,color:#fff;
    classDef meth fill:#ff7f0e,stroke:#8a4304,color:#fff;
    classDef con  fill:#17becf,stroke:#0a6770,color:#fff;
    classDef chap fill:#1f77b4,stroke:#0b3d69,color:#fff;

    %% subsections that anchor concepts
    S172[1.7.2 ATN Framework]:::sub
    S181[1.8.1 Aβ]:::sub
    S182[1.8.2 p-tau]:::sub
    S183[1.8.3 NfL]:::sub
    S184[1.8.4 GFAP]:::sub
    S191[1.9.1 Simoa]:::sub
    S192[1.9.2 Alamar ARGO]:::sub
    S15[1.5 Non-AD Dementias]:::sub
    S154[1.5.4 Co-pathologies]:::sub
    S141[1.4.1 Disease-modifying therapies]:::sub
    S1113[1.11.3 Canadian approval]:::sub

    %% canonical entities
    AB[Aβ42/40]:::ent
    PT[p-tau-181]:::ent
    NF[NfL]:::ent
    GF[GFAP]:::ent
    SIM{{Quanterix Simoa}}:::meth
    AL{{Alamar ARGO / NULISA}}:::meth
    ATN[/ATN Framework/]:::con
    CIC[/Clinical Implementation in Canada/]:::con
    COP>"Co-pathologies"]:::ent

    %% downstream chapters where concepts are used
    C2[Ch 2]:::chap
    C3[Ch 3]:::chap
    C4[Ch 4]:::chap
    C7[Ch 7]:::chap
    C8[Ch 8]:::chap
    C10[Ch 10]:::chap

    S172 --> ATN
    AB --> ATN
    PT --> ATN
    NF --> ATN
    S181 --> AB --> C2 & C3 & C7
    S182 --> PT --> C2 & C3 & C7
    S183 --> NF --> C2 & C3 & C7
    S184 --> GF --> C2 & C3 & C7
    S191 --> SIM --> C2 & C3 & C4 & C7
    S192 --> AL --> C7 & C8
    S15 --> COP
    S154 --> COP --> C8
    S141 --> CIC
    S1113 --> CIC --> C10
```

## Reading list — concept notes referenced

- Diseases: [[Alzheimer's Disease]] · [[Frontotemporal Dementia]] · [[Dementia with Lewy Bodies]] · [[Vascular Dementia]] · [[Cerebral Amyloid Angiopathy]] · [[neuroinflammation]]
- Pathology: [[ADNC]] · [[Co-pathologies]] · [[TDP-43 Pathology]]
- Biomarkers: [[Aβ42-40]] · [[p-tau-181]] · [[NfL]] · [[GFAP]]
- Methods: [[Quanterix Simoa]] · [[Alamar ARGO]] · [[NULISA]]
- Concepts: [[ATN Framework]] · [[NIA-AA]] · [[Cognitive Resilience]] · [[Clinical Implementation in Canada]] · [[CADTH]]

## Forward links

| §     | Concept introduced                | Used in chapter(s) |
|-------|-----------------------------------|--------------------|
| 1.7.2 | [[ATN Framework]]                 | implicit throughout 2–9 |
| 1.8   | The four canonical biomarkers     | 2, 3, 4, 5, 6, 7, 9 |
| 1.9.1 | [[Quanterix Simoa]]               | 2, 3, 4, 5, 6, 7, 9 |
| 1.9.2 | [[Alamar ARGO]] / [[NULISA]]      | 7, 8 |
| 1.5.4 | [[Co-pathologies]]                | 8 |
| 1.6   | [[Cognitive Resilience]]          | 5, 6 |
| 1.11  | [[Clinical Implementation in Canada]] | 9, 10 |
