# Changelog

## v1.0.2 (2026-11-24)

Archive fix. The Zenodo archive of v1.0.1 holds Git LFS pointer files instead of the two corpus files in `output/`. This version has the same data as v1.0.1, and its archive includes both files.

- No change to the corpus or to the behavior of the extender.
- Added `RevisionOfTags.pdf` and `Annotation_Extender_Technical_Details.pdf`, and shortened a comment in `src/main.py`.
- SHA-256 of the corpus files, unchanged since v1.0.1:
  - `output/results_entire_corpus.json`: `f63c9021ba08e9a8a33cba262b76df287b74ba0fed5ce8ee103d04068199ce74`
  - `output/results_entire_corpus_with_reconstructed_tasks.json`: `e80749fd0be3fb168a24826b9e84d75d342728b39a42a63c1ca7fc272d301088`

## v1.0.1 (2026-04-09)

Writer metadata fix.

- Corrected `nationality` from `male` to `albania` in the 23 error instances of one essay, in both corpus files and in `input/_metadata.xlsx`.
- Added `output/results_entire_corpus_with_reconstructed_tasks.json`, which adds the reconstructed (corrected) text of the essay to every error instance.
- Both corpus files are stored with Git LFS from this version on. The Zenodo archive of this version therefore holds LFS pointer files instead of the corpus files; the same data is in the archive of v1.0.2.

## v1.0.0 (2026-01-30)

First stable version: the annotation extender and the taxonomically enriched corpus (`output/results_entire_corpus.json`, 32,202 error instances).
