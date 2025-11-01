# Audit and Modernisation Plan for Questionnaire Catalogue

This document describes the plan executed in this iteration to bring the
questionnaire catalogue closer to parity with the validated French language
instruments.

## Objectives

1. **Eliminate duplicate questionnaire definitions** that register the same
   scale under multiple filenames.
2. **Normalise naming conventions** so each instrument has a single canonical
   module and registry code.
3. **Establish an auditable inventory** enumerating every questionnaire,
   highlighting where question text, answer choices, or scoring rules still
   require verification.
4. **Lay the groundwork for data-driven questionnaire generation** to reduce
   drift between code and source material.
5. **Align scoring strategies with the clinical instrument** or explicitly
   flag questionnaires where validated scoring remains outstanding.

## Execution Strategy

### 1. Catalogue Inventory & Reporting

* Create a reusable tool (`tools/generate_audit_table.py`) that imports the
  questionnaire registry and emits a Markdown summary (`TODO.md`).
* The table lists every registered questionnaire with the number of items,
  the scoring strategy in use, and audit status/notes.
* Known problem areas (e.g., EQ-5D-5L value-set scoring, incomplete YMRS
  translation) are annotated explicitly to prioritise follow-up work.

### 2. Deduplication & Naming Normalisation

* Remove redundant modules that define the same instrument (e.g.,
  `eq5d5l.py` vs `eq_5d_5l.py`).
* Update the import surface (`questionnaires/__init__.py`) to expose a single
  canonical class per instrument.
* Ensure the retained module is factually updated to include all published
  items and answer levels.

### 3. JSON-backed Questionnaire Definitions

* Introduce `core/json_loader.py`, a helper that converts a structured JSON
  definition into `Question` and `AnswerOption` objects plus an appropriate
  scoring strategy instance.
* Convert EQ-5D-5L to the JSON format (`questionnaires/data/eq_5d_5l.json`) to
  demonstrate the approach and make future audits a matter of editing data
  rather than code.

### 4. Scoring Strategy Alignment

* Implement a `NotImplementedStrategy` so questionnaires whose validated
  scoring rules are unknown cannot silently fall back to a simple sum.
* Upgrade YMRS to use `WeightedSumStrategy` with the canonical weighting for
  items 5, 6, 8, and 9, and restore the complete 11-item structure.
* Configure EQ-5D-5L to use the new JSON definition and the
  `NotImplementedStrategy` placeholder, with clear TODO notes referencing the
  requirement for the official French value set.

### 5. Deliverables & Future Work

* Committed artefacts: this plan, the generated `TODO.md` audit matrix, JSON
  data, updated questionnaire modules, and the JSON loader infrastructure.
* Future iterations can progressively replace Python modules with JSON data
  files, enrich the audit table with verification metadata, and implement
  validated scoring strategies as domain experts supply the necessary
  information.

