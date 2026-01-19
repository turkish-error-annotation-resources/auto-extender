## Folder Structure & File Descriptions

This repository contains annotations for learner essays (Label Studio's json export format), organized into a **Mini Corpus**, a **Main Corpus**, and aggregated files (`merged` and `entire`).

### 1. Mini Corpus
The mini-corpus serves as a pilot set where the same tasks were labeled by two annotators to measure agreement.

* **`mini_corpus_annotator1.json`**
* **`mini_corpus_annotator4.json`**

> **Note:** These files contain annotations for the **same set of 147 tasks** (learner essays). They overlap completely to facilitate inter-annotator agreement analysis.

---

### 2. Main Corpus
The main corpus consists of essays labeled by five distinct annotators. There is **no overlap** between these files; each annotator labeled a unique set of tasks.

| Filename | Annotator ID | Task Count |
| :--- | :---: | :---: |
| `main_corpus_annotator1.json` | #1 | 119 |
| `main_corpus_annotator2.json` | #2 | 105 |
| `main_corpus_annotator3.json` | #3 | 51 |
| `main_corpus_annotator4.json` | #4 | 101 |
| `main_corpus_annotator5.json` | #5 | 149 |

---

### 3. Aggregated Datasets

These files represent the combined versions of the corpora described above.

#### **`main_corpus_merged.json`**
* **Description:** This is the concatenated version of the 5 individual files from the Main Corpus.
* **Total Tasks:** **525** learner essays.

#### **`entire_corpus.json`**
* **Description:** This file represents the complete dataset, combining both the **Mini Corpus** and the **Main Corpus**.
* **Selection Logic:** For the Mini Corpus portion included in this file, the annotations from **Annotator #1** (`mini_corpus_annotator1.json`) were selected, as this annotator is designated as the expert.
* **Total Tasks:** **672** learner essays (525 from Main + 147 from Mini).

### 4. Metadata
The dataset includes a metadata file located in the `input` directory, providing demographic and task-specific details for the essays.

* **`_metadata.xlsx`**
* **Description:** This spreadsheet contains attribute data linking to the learner essays.
* **Key Attributes:** `Task ID`, `Nationality`, `Gender`, and `Essay Topic`.
* **Usage:** This file enables the analysis of the corpus based on learner demographics or specific essay prompts.