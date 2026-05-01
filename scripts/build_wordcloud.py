#!/usr/bin/env python3
"""Generate a word cloud from Jennifer Cooper's thesis PDF.

- Body text only (cuts off before the References section so journal noise
  like "doi", "vol", "pp", "alzheimer's" co-authors don't dominate)
- Domain-aware stopword list on top of the standard English one
- Outputs:
    vault/90-Maps/word-cloud.png      (high-res, for embedding)
    vault/90-Maps/word-cloud-words.tsv (top-200 token + count, for transparency)
"""
import re
from pathlib import Path
from collections import Counter
from wordcloud import WordCloud, STOPWORDS

ROOT = Path(__file__).resolve().parent.parent
TXT  = Path("/tmp/thesis.txt")
OUT_PNG = ROOT / "vault" / "90-Maps" / "word-cloud.png"
OUT_TSV = ROOT / "vault" / "90-Maps" / "word-cloud-words.tsv"

EXTRA_STOP = {
    # generic academic noise
    "et", "al", "etal", "table", "figure", "fig", "tables", "figures",
    "chapter", "chapters", "section", "appendix", "ie", "eg", "vs",
    "page", "pages", "supplementary", "supplemental",
    # statistical / methods filler
    "n", "p", "ci", "sd", "iqr", "mean", "median", "value", "values",
    "data", "results", "result", "analysis", "analyses", "analyzed",
    "measured", "measurement", "measurements", "based", "using", "used",
    "use", "show", "shown", "showed", "shows", "found", "find",
    "studies", "study", "different", "previous", "previously", "current",
    "well", "may", "could", "would", "also", "however", "although",
    "thus", "therefore", "across", "within", "compared", "comparison",
    "level", "levels", "high", "low", "higher", "lower", "increased",
    "decreased", "due", "remained", "remain", "given", "provided",
    "determine", "determined", "performed", "conducted", "evaluated",
    "assessed", "observed", "associated", "association", "associations",
    "including", "include", "included", "respectively", "either", "one",
    "two", "three", "four", "five", "six", "seven", "ten", "first",
    "second", "third", "non", "pre", "post", "per", "vs", "versus",
    "see", "shows", "demonstrated", "demonstrate", "indicate", "indicated",
    "et", "al", "et al",
    # bibliography / citation residue
    "doi", "https", "http", "www", "org", "com", "vol", "pp", "issue",
    "journal", "lancet", "neurol", "neurology", "jama", "nature",
    "pubmed", "pmid", "abstract", "review", "press",
    # PDF-extraction noise
    "ǻǻ", "—", "–", "•", "·",
    # over-represented but not informative on their own
    "patient", "patients", "subject", "subjects", "participant",
    "participants", "individual", "individuals", "group", "groups",
    "year", "years", "old", "age", "aged", "adult", "adults",
    "blood", "plasma", "sample", "samples", "test", "tests", "testing",
    "presence", "concentrations", "concentration", "specific", "additional",
    "potential", "particularly", "significantly", "expected", "likely",
    # signal: keep biomarker / disease words
}

# merge near-duplicate forms into a single canonical token
MERGE = {
    "biomarkers": "biomarker",
    "cohorts": "cohort",
    "diagnoses": "diagnosis",
    "diagnosed": "diagnosis",
    "pathologies": "pathology",
    "neuropathologies": "neuropathology",
    "score": "scores",
    "controls": "control",
    "carriers": "carrier",
    "percentile": "percentiles",
    "curve": "curves",
    "marker": "markers",
    "lots": "lot",
    "stage": "stages",
}
STOPWORDS_ALL = set(STOPWORDS) | EXTRA_STOP

raw = TXT.read_text(encoding="utf-8", errors="ignore")

# cut off at the References heading; keep everything before it
cut = re.search(r"\n\s*References\s*\n", raw)
body = raw[:cut.start()] if cut else raw
print(f"Body chars: {len(body):,}  (full PDF chars: {len(raw):,})")

# normalise: lowercase, tokenise on word chars (keep hyphens and digits to
# preserve things like "p-tau-181", "aβ42", "apoe4"); strip pure-numeric tokens
text = body.lower()
# protect known multi-token concepts so they survive as single tokens
protect = {
    "p-tau-181": "ptau181term",
    "p-tau181":  "ptau181term",
    "aβ42/40":   "abeta4240term",
    "aβ42":      "abeta42term",
    "aβ40":      "abeta40term",
    "apoe ε4":   "apoe4term",
    "apoe4":     "apoe4term",
    "alzheimer's disease": "alzheimersdiseaseterm",
    "alzheimer’s disease": "alzheimersdiseaseterm",
    "reference curve": "referencecurveterm",
    "reference curves": "referencecurveterm",
    "reference interval": "referenceintervalterm",
    "reference intervals": "referenceintervalterm",
    "cognitive resilience": "cognitiveresilienceterm",
    "super seniors": "superseniorsterm",
    "super-seniors": "superseniorsterm",
    "co-pathology": "copathologyterm",
    "co-pathologies": "copathologyterm",
    "neurofilament light": "nflterm",
}
for src, dst in sorted(protect.items(), key=lambda kv: -len(kv[0])):
    text = re.sub(r"\b" + re.escape(src) + r"\b", dst, text)
display = {v: k.title().replace("’s", "'s") for k, v in protect.items()}
# better display names
display.update({
    "ptau181term": "p-tau-181",
    "abeta4240term": "Aβ42/40",
    "abeta42term": "Aβ42",
    "abeta40term": "Aβ40",
    "apoe4term": "APOE4",
    "alzheimersdiseaseterm": "Alzheimer's Disease",
    "referencecurveterm": "Reference Curve",
    "referenceintervalterm": "Reference Interval",
    "cognitiveresilienceterm": "Cognitive Resilience",
    "superseniorsterm": "Super Seniors",
    "copathologyterm": "Co-pathology",
    "nflterm": "NfL",
})

tokens = re.findall(r"[a-zβα0-9][a-zβα0-9\-/]*[a-zβα0-9]", text)
counts = Counter()
for tok in tokens:
    if tok in STOPWORDS_ALL: continue
    if len(tok) < 3: continue
    if tok.isdigit(): continue
    if re.fullmatch(r"[\d\-/]+", tok): continue
    tok = MERGE.get(tok, tok)
    counts[tok] += 1

# remap protected tokens to display form
remapped = Counter()
for tok, c in counts.items():
    remapped[display.get(tok, tok)] += c

print(f"Unique tokens kept: {len(remapped):,}")
print("Top 25:")
for w, c in remapped.most_common(25):
    print(f"  {c:6d}  {w}")

# write top-200 tsv for transparency
OUT_TSV.write_text(
    "rank\tcount\tterm\n" +
    "\n".join(f"{i+1}\t{c}\t{w}" for i, (w, c) in enumerate(remapped.most_common(200))),
    encoding="utf-8",
)

# render the cloud
wc = WordCloud(
    width=2400, height=1500,
    background_color="white",
    colormap="tab20c",
    max_words=220,
    relative_scaling=0.45,
    prefer_horizontal=0.78,
    collocations=False,
    min_font_size=8,
    margin=4,
    random_state=7,
).generate_from_frequencies(remapped)

wc.to_file(str(OUT_PNG))
print(f"Wrote {OUT_PNG} ({OUT_PNG.stat().st_size:,} bytes)")
print(f"Wrote {OUT_TSV}")
