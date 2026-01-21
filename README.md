# Annotation Extender for Turkish Learner Corpus

This repository contains the **Annotation Extender (Auto-Extender)** described in:

> Sayar, E., Türker, T., Golynskaia, A., Dereli, B., Demirhas, A., Nicolas, L., & Eryiğit, G. (2025). *From Labels to Facets: Building a Taxonomically Enriched Turkish Learner Corpus*. [Journal Name TBD].

> Eryiğit, G., Golynskaia, A., Sayar, E. et al. Error annotation: a review and faceted taxonomy. Lang Resources & Evaluation 59, 3385–3409 (2025). https://doi.org/10.1007/s10579-024-09794-0

Please cite the papers above when using this repository.

# Overview
**Auto-Extender** is a semi-automated framework designed to enrich human-annotated learner corpora with a multi-dimensional **faceted taxonomy** (Eryiğit et al., 2025).

Originally developed for a **Turkish Learner Corpus**, this tool automatically infers linguistic properties and metadata for error annotations, transforming flat error labels into a taxonomically enriched corpus. This tool serves as the bridge between manual annotation and deep linguistic analysis.

## Features
* **Semi-Automatic Enrichment:** Extends manual error tags (e.g., `SPELL`, `CASE`) with six linguistic facets: *Identifier, Morphological Feature, Unit, Phenomenon, Linguistic Level, and Metadata*.
* **Hybrid Inference Strategy:**
    * **Static Mapping:** Deterministic assignment based on error types (e.g., `Vowel Harmony` → `Unit: Affix`) provided in Pre-defined Tagset Mapping Schema.
    * **Context-Aware Mapping:** Uses heuristic rules and morphological analysis to resolve ambiguities (e.g., distinguishing `Lemma` vs. `Affix` for spelling errors) by utilizing the Pre-defined Tagset Mapping Schema.
* **Universal Dependencies (UD) Integration:** Utilizes **UDPipe** to generate standardized POS tags and morphological features.
* **Metadata Injection:** Merges task-level metadata (learner gender, nationality, topic) directly into individual error instances.

## System Architecture
The extender operates on a pipeline that processes human annotations and metadata to produce a taxonomically enriched corpus.

1.  **Data Validation:** Verifies consistency of Label Studio exports.
2.  **Task-Level Reconstruction:** Reconstructs the "corrected" text from error spans and applies index realignment.
3.  **Morphological Analysis:** Processes texts using **UDPipe** (`turkish-imst-ud` model).
4.  **Facet Inference:** Applies the **Pre-defined Tagset Mapping Schema** to infer facet values.

## Prerequisites
* **Python 3.13.5+**
* **UDPipe v2:** The system requires the `ufal.udpipe` binding.
* **Pre-trained Model:** `turkish-imst-ud-2.15-241121` (or compatible UD model).

To install the required dependencies run the following command:

```bash
pip install -r requirements.txt
```

## Input Data Format
The tool requires two specific input files:

1. **Human-Annotated Corpus (JSON):** The export file from Label Studio containing the manual annotations.

2. **Corpus Metadata (CSV):** A CSV file containing demographic and task information for the learners.

## Output - Taxonomically Enriched Corpus (for an error instance)

```json
{
  "id": "45ID60k62",
  "errType": "SPE",
  "rawText": "başarlı",
  "corrText": "başarılı",
  "errTax": {
    "pos": [{"form": "başarılı", "pos": "ADJ"}],
    "lexFeat": [{"feats": "Typo=Yes"}],
    "unit": "Lemma",
    "phenomenon": "Omission",
    "level": "Orthography"
  },
  "metadata": {
    "nationality": "azerbaijan",
    "gender": "male",
    "topic": "success and pride"
  }
}
```

## Usage

To run the annotation extender:

```bash
python src/main.py "<path to corpus (e.g., /input/entire_corpus.json)>"
```

## Contact

If you have any questions, suggestions or any feedback, you can contact the turkert21@itu.edu.tr



