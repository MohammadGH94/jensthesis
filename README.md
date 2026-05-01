# Jennifer Cooper Thesis — Second Brain Map

A linked knowledge vault and visual brain map of the dissertation
**"Plasma Biomarkers of Neurodegeneration Across the Spectrum of Brain Health"**
(Jennifer Cooper, PhD, UBC Pathology and Laboratory Medicine, March 2026).

## Contents

```
vault/                     # Obsidian-style markdown vault
  00-Index/                # Home, Map of Content, Thesis Overview
  10-Chapters/             # one note per chapter (1–10)
  20-Biomarkers/           # Aβ42/40, p-tau-181, NfL, GFAP
  30-Cohorts/              # CHMS, Super Seniors, CARD, COMPASS-ND
  40-Diseases/             # AD, FTD, DLB, VaD, ADNC, co-pathologies, …
  50-Methods/              # Quanterix Simoa, Alamar ARGO, NULISA, GAMLSS, LASSO/EN
  60-Concepts/             # ATN, resilience, APOE4, plasma probability scores, Cdn implementation
  70-People/               # author, supervisor, committee, key collaborators
  90-Maps/                 # Mermaid brain-map diagrams + word cloud
vault-graph.html           # standalone interactive force-directed graph (d3)
scripts/build_wordcloud.py # regenerates vault/90-Maps/word-cloud.png from PDF
ubc_2026_may_cooper_jennifer.pdf.pdf  # source PDF
```

Notes use Obsidian-style `[[wikilinks]]` and YAML frontmatter so the graph view, backlinks, and tag pane all work.

## How to use it

### As a vault in Obsidian
1. Install [Obsidian](https://obsidian.md).
2. *Open folder as vault* → select the `vault/` directory.
3. Open `00-Index/Home.md`. Toggle the graph view (Ctrl/Cmd-G) to see the live link graph.

### On GitHub
- Open [`vault/90-Maps/Brain Map.md`](vault/90-Maps/Brain%20Map.md) — GitHub renders the Mermaid diagrams natively.
- Browse the chapter notes under [`vault/10-Chapters/`](vault/10-Chapters).

### As an interactive map
- Open `vault-graph.html` in any browser. Drag nodes, scroll to zoom, click to focus a sub-graph, toggle node types from the sidebar.

### As a word cloud
- See [`vault/90-Maps/Word Cloud.md`](vault/90-Maps/Word%20Cloud.md) for the rendered PNG plus the top-200 term frequencies. Re-run `python3 scripts/build_wordcloud.py` after PDF/text changes to refresh.

## How this was built

Inspired by the [obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) skill, which is designed to evolve an existing Obsidian vault. Since the source repo only contained the thesis PDF, the vault here was scaffolded once from the PDF's table of contents, abbreviations list, and preface (chapter authorship and cohort details). To then **continue** evolving this vault using that skill, install it:

```bash
curl -sL https://raw.githubusercontent.com/eugeniughelbur/obsidian-second-brain/main/scripts/quick-install.sh | bash
```

…and from a Claude Code session pointed at this repo, run its slash commands (e.g. `/ingest`, `/synthesise`, `/vault-map`) to keep the vault current as new chapters or co-author drafts come in.

## Branch

Developed on `claude/thesis-second-brain-map-yVrQB`.
