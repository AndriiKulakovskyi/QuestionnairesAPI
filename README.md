# Questionnaires API

A Python implementation of clinical questionnaires (QIDS-SR16, MDQ, ASRM, Epworth, and EQ-5D-EL) designed for FastAPI integration.

## Questionnaires Included

### 1. QIDS-SR16 (Quick Inventory of Depressive Symptomatology - Self Report 16)
- **Purpose**: Self-assessment scale measuring depression severity
- **Language**: French (fr-FR)
- **Structure**: 16 items across 2 sections covering 9 DSM domains
- **Scoring**: 0-27 total score with severity levels:
  - 0-5: No depression
  - 6-10: Mild depression
  - 11-15: Moderate depression
  - 16-20: Severe depression
  - 21-27: Very severe depression

### 2. MDQ (Mood Disorder Questionnaire)
- **Purpose**: Screening tool for bipolar disorder spectrum
- **Language**: French (fr-FR)
- **Structure**: 13 yes/no items + 2 follow-up questions
- **Screening**: Positive if ≥7 "yes" answers + concurrent + moderate/serious impact

### 3. ASRM (Altman Self-Rating Mania Scale)
- **Purpose**: Self-assessment scale for manic/hypomanic symptoms
- **Language**: French (fr-FR)
- **Structure**: 5 items, each scored 0-4
- **Scoring**: 0-20 total score with probability levels:
  - 0-5: Low probability of manic/hypomanic episode
  - 6-20: High probability of manic/hypomanic episode

### 4. Epworth Sleepiness Scale (ESS)
- **Purpose**: Self-assessment scale for daytime sleepiness
- **Language**: French (fr-FR)
- **Structure**: 8 scored items (0-3 each) + 1 optional timing question
- **Scoring**: 0-24 total score with severity levels:
  - 0-10: Normal sleepiness
  - 11-24: Excessive daytime sleepiness (EDS)

### 5. EQ-5D-EL (EuroQol 5 Dimensions 5 Levels)
- **Purpose**: Generic measure of health-related quality of life
- **Language**: French (fr-FR)
- **Structure**: 5 dimensions (1-5 scale) + Visual Analog Scale (0-100)
- **Output**: Health state profile (e.g., "21341") + VAS score
- **Dimensions**: Mobility, Self-care, Usual activities, Pain/Discomfort, Anxiety/Depression

## Installation

```bash
pip install -r requirements.txt
```

## Project Structure

```
QuestionnairesAPI/
├── questionnaires/
│   ├── __init__.py
│   ├── qids/
│   │   ├── __init__.py
│   │   └── qids_sr16.py
│   └── mdq/
│       ├── __init__.py
│       └── mdq.py
├── requirements.txt
├── example_usage.py
└── README.md
```

## Usage

### Basic Usage

```python
from questionnaires import QIDSSR16, MDQ, ASRM, Epworth, EQ5DEL

# Initialize questionnaires
qids = QIDSSR16()
mdq = MDQ()
asrm = ASRM()
epworth = Epworth()
eq5d = EQ5DEL()

# Get questionnaire structure (for frontend)
qids_data = qids.get_full_questionnaire()
mdq_data = mdq.get_full_questionnaire()
asrm_data = asrm.get_full_questionnaire()
epworth_data = epworth.get_full_questionnaire()
eq5d_data = eq5d.get_full_questionnaire()

# Calculate depression score
answers_qids = {f"q{i}": 0 for i in range(1, 17)}
result = qids.calculate_score(answers_qids)
print(f"Score: {result.total_score}, Severity: {result.severity}")

# Screen for bipolar disorder
answers_mdq = {f"q1_{i}": 0 for i in range(1, 14)}
answers_mdq.update({"q2": 0, "q3": 0})
screening = mdq.calculate_screening(answers_mdq)
print(f"Screening: {screening.screening_result}")

# Assess manic symptoms
answers_asrm = {f"q{i}": 0 for i in range(1, 6)}
result_asrm = asrm.calculate_score(answers_asrm)
print(f"Score: {result_asrm.total_score}, Probability: {result_asrm.probability}")

# Assess daytime sleepiness
answers_epworth = {f"q{i}": 1 for i in range(1, 9)}
result_epworth = epworth.calculate_score(answers_epworth)
print(f"Score: {result_epworth.total_score}, Severity: {result_epworth.severity}")

# Assess health-related quality of life
answers_eq5d = {f"q{i}": 2 for i in range(1, 6)}
answers_eq5d['vas'] = 75
result_eq5d = eq5d.calculate_score(answers_eq5d)
print(f"Profile: {result_eq5d.profile}, VAS: {result_eq5d.vas_score}")
```

### FastAPI Integration

```python
from fastapi import FastAPI, HTTPException
from questionnaires import QIDSSR16, QIDSError, MDQ, MDQError, ASRM, ASRMError

app = FastAPI()
qids = QIDSSR16()
mdq = MDQ()
asrm = ASRM()

@app.get("/api/questionnaires/qids-sr16")
async def get_qids_questionnaire():
    """Get complete QIDS-SR16 questionnaire structure"""
    return qids.get_full_questionnaire()

@app.post("/api/questionnaires/qids-sr16/score")
async def calculate_qids_score(answers: dict):
    """Calculate QIDS-SR16 score from submitted answers"""
    try:
        result = qids.calculate_score(answers)
        return result.dict()
    except QIDSError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/questionnaires/mdq")
async def get_mdq_questionnaire():
    """Get complete MDQ questionnaire structure"""
    return mdq.get_full_questionnaire()

@app.post("/api/questionnaires/mdq/screen")
async def calculate_mdq_screening(answers: dict):
    """Calculate MDQ screening result"""
    try:
        result = mdq.calculate_screening(answers)
        return result.dict()
    except MDQError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/questionnaires/asrm")
async def get_asrm_questionnaire():
    """Get complete ASRM questionnaire structure"""
    return asrm.get_full_questionnaire()

@app.post("/api/questionnaires/asrm/score")
async def calculate_asrm_score(answers: dict):
    """Calculate ASRM score"""
    try:
        result = asrm.calculate_score(answers)
        return result.dict()
    except ASRMError as e:
        raise HTTPException(status_code=400, detail=str(e))
```

## API Methods

### QIDSSR16 Class

#### Methods:
- `get_metadata()`: Returns instrument metadata
- `get_sections()`: Returns all sections
- `get_questions(section_id=None)`: Returns questions, optionally filtered by section
- `get_question_by_id(question_id)`: Returns a specific question
- `validate_answers(answers)`: Validates answer dictionary
- `calculate_score(answers)`: Calculates total score and severity
- `get_full_questionnaire()`: Returns complete questionnaire structure

#### Response Models:
- `ScoreResult`: Contains total_score, severity, domain_scores, interpretation
- `ValidationResult`: Contains valid (bool), errors (list), warnings (list)

### MDQ Class

#### Methods:
- `get_metadata()`: Returns instrument metadata
- `get_sections()`: Returns all sections
- `get_questions(section_id=None)`: Returns questions, optionally filtered by section
- `get_question_by_id(question_id)`: Returns a specific question
- `validate_answers(answers)`: Validates answer dictionary
- `calculate_screening(answers)`: Calculates screening result
- `get_full_questionnaire()`: Returns complete questionnaire structure

#### Response Models:
- `ScreeningResult`: Contains q1_total, q2_concurrent, q3_impact_level, q3_impact_label, screening_result, interpretation
- `ValidationResult`: Contains valid (bool), errors (list), warnings (list)

## Example Output

### QIDS-SR16 Score Result

```json
{
  "total_score": 12,
  "severity": "Dépression modérée",
  "domain_scores": {
    "sleep": 2,
    "sadness": 2,
    "appetite_weight": 1,
    "concentration": 2,
    "self_view": 1,
    "suicidal_ideation": 0,
    "interest": 2,
    "energy": 2,
    "psychomotor": 0
  },
  "interpretation": "Score total: 12/27 - Dépression modérée.",
  "range": [0, 27]
}
```

### MDQ Screening Result

```json
{
  "q1_total": 8,
  "q2_concurrent": true,
  "q3_impact_level": 3,
  "q3_impact_label": "Problème sérieux",
  "screening_result": "POSITIF",
  "interpretation": "MDQ POSITIF. Symptômes Q1: 8/13. Simultanéité (Q2): Oui. Impact fonctionnel (Q3): Problème sérieux. Ce résultat suggère la présence possible d'un trouble du spectre bipolaire. Une évaluation clinique approfondie est recommandée."
}
```

## Features

- ✅ Complete questionnaire structure retrieval for frontend
- ✅ Answer validation with clinical consistency checks
- ✅ Score calculation with domain breakdowns
- ✅ Clinical interpretation generation
- ✅ Type-safe with Pydantic models
- ✅ Ready for FastAPI integration
- ✅ French language support
- ✅ Clinical alerts (e.g., suicidal ideation)

## Testing

### Running Tests

The project includes comprehensive unit tests (97+ test cases) covering all functionality:

```bash
# Using the test runner script (recommended)
python run_tests.py all          # Run all tests with coverage
python run_tests.py qids         # Run only QIDS-SR16 tests
python run_tests.py mdq          # Run only MDQ tests
python run_tests.py coverage     # Generate HTML coverage report

# Using pytest directly
pytest                           # Run all tests
pytest -v                        # Verbose output
pytest tests/test_qids_sr16.py   # Run specific test file
pytest -k "validation"           # Run tests matching keyword
```

See [TESTING.md](TESTING.md) for detailed testing documentation.

### Test Coverage

- **QIDS-SR16**: 44 test cases covering metadata, validation, scoring, and edge cases
- **MDQ**: 53 test cases covering metadata, validation, screening, and clinical scenarios
- **ASRM**: 45 test cases covering metadata, validation, scoring, and manic symptom patterns
- **Epworth**: 54 test cases covering metadata, validation, scoring, and sleepiness patterns
- **EQ-5D-EL**: 50+ test cases covering metadata, validation, profile calculation, and health states
- **Expected coverage**: >95%
- **Execution time**: <7 seconds

### Running Examples

Run the example usage script:

```bash
python example_usage.py
```

## Clinical Notes

### QIDS-SR16
- Items 1-4 (sleep): Maximum score used (insomnia or hypersomnia)
- Items 6-9 (appetite/weight): Maximum score used (decrease or increase)
- Items 15-16 (psychomotor): Maximum score used (retardation or agitation)
- Item 12 (suicidal ideation): Triggers clinical alert if ≥2

### MDQ
- Positive screening criteria: Q1≥7 AND Q2=yes AND Q3≥moderate
- Questions assess lifetime manic/hypomanic symptoms
- Not diagnostic, requires clinical follow-up if positive

### ASRM
- Reference period: Last 7 days
- Cutoff score: ≥6 indicates high probability of manic/hypomanic episode
- Simple sum of 5 items (no domain calculations)
- Scores ≥12 suggest severe manic symptoms

### Epworth
- Reference period: Recent months
- Cutoff score: ≥11 indicates excessive daytime sleepiness
- 8 scored items (situations), 1 optional timing question (not scored)
- High scores in driving situations trigger safety warnings

### EQ-5D-EL
- Reference period: TODAY (AUJOURD'HUI)
- Generates 5-digit health state profile (11111-55555)
- Each dimension scored 1-5 (Mobility, Self-care, Usual activities, Pain/Discomfort, Anxiety/Depression)
- VAS: 0-100 (self-rated health)
- Index calculation requires EQ-5D-EL Crosswalk table (France value set)
- Warns about profile-VAS inconsistencies

## License

This implementation follows the original questionnaire guidelines and scoring rules from published research.

## References

### QIDS-SR16
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2929841/
- https://med-fom-ubcsad.sites.olt.ubc.ca/files/2013/11/QIDS-SR.pdf

### MDQ
- Hirschfeld RM et al., Am J Psychiatry, 2000
- Official MDQ documentation

### ASRM
- Altman EG, Hedeker D, Peterson JL, Davis JM. The Altman Self-Rating Mania Scale. Biol Psychiatry. 1997;42(10):948-55.

### Epworth
- Johns MW. A new method for measuring daytime sleepiness: the Epworth sleepiness scale. Sleep. 1991;14(6):540-5.

### EQ-5D-EL
- EuroQol Group. EQ-5D-EL User Guide (2019). https://euroqol.org/
- French value set via EQ-5D-EL Crosswalk Index Value Calculator

