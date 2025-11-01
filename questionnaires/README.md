# Questionnaires Directory

This directory contains Python implementations of clinical questionnaires extracted from four EMR applications for psychiatric disorders: eBipolar, eSchizo, Asperger (TSA), and CEDR (Depression).

## Overview

All questionnaires have been extracted from legacy PHP/SQL code and converted to standalone Python classes for reusability across applications.

- **Total Questionnaires**: 146
- **Status**: 3 completed, 143 in progress
- **Language**: French (all questions and answer options)
- **Structure**: Flat directory (no subdirectories)

## Completed Questionnaires

1. **`systematisation_quotient_sq.py`** - Quotient de Systématisation (SQ) - 60 items
2. **`madrs.py`** - Montgomery-Åsberg Depression Rating Scale - 10 items  
3. **`qids_sr16.py`** - Quick Inventory of Depressive Symptomatology - 16 items

## Questionnaire Class Structure

Each questionnaire is implemented as a Python class with the following structure:

```python
class QuestionnaireNameQuestionnaire:
    """Questionnaire description (in French)"""
    
    def __init__(self):
        self.name = "Nom du Questionnaire"
        self.description = "Description du questionnaire"
        self.used_in_applications = ["app1", "app2"]  # Which EMR apps use it
        self.questions = self._init_questions()
        
    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all questions with:
        - id: Question identifier
        - number: Question number
        - text: Question text in French
        - type: Input type (radio, select, textbox, etc.)
        - options: Dict of answer options
        - required: Boolean
        - Any conditional/branching logic
        """
        
    def validate_responses(self, responses: Dict[str, Any]) -> Dict[str, List[str]]:
        """Validate responses and check required fields"""
        
    def calculate_score(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate questionnaire score(s) with original scoring algorithm
        
        Returns:
            - score: Calculated score value
            - valid: Whether calculation succeeded
            - errors: List of errors if any
            - interpretation: Score interpretation (severity levels, etc.)
        """
```

## Usage Examples

### Example 1: MADRS (Simple Scoring)

```python
from madrs import MADRSQuestionnaire

# Initialize questionnaire
madrs = MADRSQuestionnaire()

# Provide responses (0-6 for each of 10 items)
responses = {
    'MADRS1': 3,
    'MADRS2': 4,
    'MADRS3': 2,
    # ... items 4-10
}

# Calculate score
result = madrs.calculate_score(responses)
print(f"Score: {result['score']}")  # 0-60
print(f"Sévérité: {result['interpretation']}")  # e.g., "Dépression modérée"
```

### Example 2: QIDS-SR16 (Complex Scoring with Conditional Logic)

```python
from qids_sr16 import QIDSSR16Questionnaire

qids = QIDSSR16Questionnaire()

# Responses with conditional items
responses = {
    'QIDS1': 2,
    'QIDS2': 1,
    # Items 6 and 7 are mutually exclusive (appetite)
    'QIDS6': 2,  # Decreased appetite
    'QIDS7': None,  # Not increased
    # Items 8 and 9 are mutually exclusive (weight)
    'QIDS8': 1,  # Weight loss
    'QIDS9': None,  # Not weight gain
    # ... other items
}

result = qids.calculate_score(responses)
print(f"Score: {result['score']}")  # 0-27
print(f"Sous-scores: {result['subscores']}")
```

### Example 3: SQ (Reverse Scoring)

```python
from systematisation_quotient_sq import SystematisationQuotientQuestionnaire

sq = SystematisationQuotientQuestionnaire()

# All 60 items (1-4 scale)
responses = {f'SYSTE{i}': 1 for i in range(1, 61)}

result = sq.calculate_score(responses)
print(f"Score SQ: {result['score']}")  # 0-120
```

## Extraction Tools

### `extraction_utils.py`

Utility functions for parsing PHP, JavaScript, and SQL source files:
- `parse_php_qcm_question()` - Extract questions from PHP QCM objects
- `extract_questionnaire_from_php()` - Full PHP form extraction
- `parse_javascript_scoring()` - Extract scoring logic from JavaScript
- `extract_sql_questionnaire()` - Extract from SQL CREATE TABLE statements
- `list_questionnaires_to_extract()` - Inventory all questionnaires in codebase

### `batch_extractor.py`

Batch processing script for systematic extraction:
- Identifies all 146 questionnaires across 4 applications
- Detects shared/duplicate questionnaires
- Processes in batches with error handling
- Generates extraction progress reports

Usage:
```bash
python batch_extractor.py
```

## Questionnaire Categories

### By Application

- **Asperger/TSA**: 56 questionnaires (autism, social cognition, executive function)
- **CEDR**: 29 questionnaires (depression, anxiety, sleep)
- **eBipolar**: 32 questionnaires (mood, impulsivity, medication adherence)
- **eSchizo**: 29 questionnaires (psychosis, negative symptoms, side effects)

### By Type

- **Auto-questionnaires** (~80): Self-report questionnaires
- **Hétéro-évaluations** (~35): Clinician-administered assessments
- **Mixed** (~31): Forms with both components

### By Complexity

- **Simple** (~30): Direct summation scoring
- **Medium** (~60): Reverse scoring, subscales
- **Complex** (~40): Conditional logic, grouped calculations
- **Very Complex** (~16): Multi-form, extensive branching

## Shared Questionnaires

These questionnaires are used in multiple applications (deduplicated):

1. **MADRS** - cedr, ebipolar, eschizo (✅ completed)
2. **YMRS** - ebipolar, eschizo
3. **CTQ** - ebipolar, eschizo
4. **MARS** - ebipolar, eschizo
5. **PSQI** - ebipolar, eschizo
6. **WURS** - ebipolar, eschizo
7. **CGI-EGF** - ebipolar, eschizo
8. **EQ-5D** - ebipolar, eschizo

## Key Features

### Accurate Scoring

All scoring algorithms have been carefully extracted from the original JavaScript and PHP code:
- Complex reverse scoring (e.g., SQ)
- Conditional logic (e.g., QIDS appetite/weight items)
- Maximum selection from groups (e.g., QIDS sleep items)
- Subscale calculations
- Weighted items

### Branching Logic

Questionnaires with conditional/dependent questions properly implement:
- Mutually exclusive items
- Skip logic
- Dynamic question display
- Conditional validation

### Validation

Each questionnaire includes:
- Required field checking
- Response option validation
- Conditional logic validation
- Clear error messages in French

### Metadata

Every questionnaire tracks:
- Original source application(s)
- Table/form identifiers
- Which EMR apps use it
- Questionnaire type (auto vs. hetero)

## Next Questionnaires to Extract

### Priority 1: Shared Questionnaires
- YMRS (Young Mania Rating Scale)
- CTQ (Childhood Trauma Questionnaire)
- PSQI (Pittsburgh Sleep Quality Index)
- MARS (Medication Adherence)

### Priority 2: Key Clinical Scales
- PANSS (Positive and Negative Syndrome Scale)
- AQ (Autism Quotient)
- MDQ (Mood Disorder Questionnaire)
- PHQ-9, GAD-7

### Priority 3: Specialized Assessments
- ADOS/ADI-R items
- Cognitive assessments
- Side effect scales

## Development Guidelines

When adding new questionnaires:

1. **Naming**: Use descriptive snake_case filenames (e.g., `beck_depression_inventory_bdi.py`)
2. **Class Name**: Format as `QuestionnaireNameQuestionnaire`
3. **Language**: All text in French
4. **Documentation**: Include clear docstrings
5. **Scoring**: Implement exact original algorithm
6. **Testing**: Add example usage in `if __name__ == "__main__"` block
7. **Metadata**: Set `used_in_applications` list

## Testing

Test each questionnaire with:
1. Complete valid responses
2. Missing required fields
3. Invalid response values
4. Edge cases in scoring logic
5. Conditional/branching scenarios

## Status Tracking

See `EXTRACTION_STATUS.md` for:
- Complete progress report
- Questionnaire inventory by application
- Complexity analysis
- Time estimates
- Detailed extraction plan

## Support

For questions about specific questionnaires or extraction issues, refer to:
- Original source files in `apps/{app}/www/form/` (PHP forms)
- Scoring logic in `apps/{app}/www/js_scores/` (JavaScript)
- Database schemas in `db_data/{app}/*.sql` (SQL tables)

---

*Last updated: Current session*
*Extraction progress: 3/146 questionnaires (2%)*

