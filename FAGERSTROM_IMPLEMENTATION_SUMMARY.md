# Fagerström Test for Nicotine Dependence (FTND) - Implementation Summary

## ✅ Implementation Complete

### Questionnaire: Fagerström Test for Nicotine Dependence (FTND)
**French version** - Tobacco/nicotine dependence assessment scale

## Scoring Methodology

### Simple Additive Scoring
The FTND uses a straightforward additive scoring system:

**Total Score = Q1 + Q2 + Q3 + Q4 + Q5 + Q6**

Where:
- **Q1** (Time to first cigarette): 0-3 points
  - 0 = After 60 minutes
  - 1 = 31-60 minutes  
  - 2 = 6-30 minutes
  - 3 = Within 5 minutes
  
- **Q2** (Difficult to refrain): 0-1 points
  - 0 = No
  - 1 = Yes
  
- **Q3** (Hardest cigarette to give up): 0-1 points
  - 0 = Any other
  - 1 = The first one
  
- **Q4** (Cigarettes per day): 0-3 points
  - 0 = 10 or less
  - 1 = 11-20
  - 2 = 21-30
  - 3 = 31 or more
  
- **Q5** (Smoke more in morning): 0-1 points
  - 0 = No
  - 1 = Yes
  
- **Q6** (Smoke when ill): 0-1 points
  - 0 = No
  - 1 = Yes

### Score Range: 0-10

### Dependence Levels:
- **0-2**: No dependence or very weak dependence
- **3-4**: Weak dependence  
- **5**: Medium dependence
- **≥6**: Strong dependence

### Example Calculation:
```python
answers = {"q1": 2, "q2": 1, "q3": 1, "q4": 1, "q5": 0, "q6": 0}
# Score = 2 + 1 + 1 + 1 + 0 + 0 = 5
# Interpretation: "Dépendance moyenne" (Medium dependence)
```

## Files Created

### 1. Core Implementation
- **`questionnaires/fagerstrom/fagerstrom.py`** (503 lines)
  - `Fagerstrom` class
  - Complete scoring methodology documentation in header
  - Clinical interpretation with recommendations
  
### 2. Test Suite  
- **`tests/test_fagerstrom.py`** (436 lines)
  - 6 test classes
  - 37 test methods
  - Test coverage:
    - Metadata and structure
    - Answer validation
    - Scoring calculation
    - Dependence level cutoffs
    - Edge cases
    - Integration workflows

### 3. Package Structure
- **`questionnaires/fagerstrom/__init__.py`** - Module exports
  
## Key Features

### ✅ Validation
- Required fields check (all 6 questions)
- Range validation:
  - Q1, Q4: Must be 0-3
  - Q2, Q3, Q5, Q6: Must be 0-1
- Type checking (integers only)

### ⚠️ Clinical Warnings
- **High score warning (≥8)**: Flags very strong dependence
- **Early morning smoking (Q1=3)**: Physical dependence indicator
- **High consumption (Q4=3)**: Major health risk (≥31 cigarettes/day)

### 📊 Clinical Recommendations
Automatically generated based on score:
- **0-2**: Cessation possible without nicotine replacement
- **3-4**: Low-dose nicotine replacement may help
- **5**: Nicotine replacement recommended
- **≥6**: Nicotine replacement strongly recommended + therapeutic support

## API Methods

- `get_metadata()` - Instrument information, cutoffs
- `get_sections()` - Section structure (single section)
- `get_questions()` - All 6 questions with options
- `validate_answers(answers)` - Validation with clinical warnings
- `calculate_score(answers)` - Total score + dependence level + interpretation
- `get_full_questionnaire()` - Complete structure for frontend

## Test Coverage

### Test Classes (6)
1. **TestFagerstromMetadata** - Metadata, sections, questions
2. **TestFagerstromValidation** - Answer validation, warnings
3. **TestFagerstromScoring** - Score calculation, interpretation
4. **TestFagerstromCutoffs** - Dependence level boundaries
5. **TestFagerstromEdgeCases** - Consistency, edge cases
6. **TestFagerstromIntegration** - Complete workflows

### Test Methods (37)
- Metadata retrieval
- Question structure validation
- Valid/invalid answer scenarios
- All dependence levels (0-10)
- Cutoff boundaries
- Clinical warnings
- Integration workflows

## Usage Example

```python
from questionnaires import Fagerstrom

# Initialize
fager = Fagerstrom()

# Patient answers
answers = {
    "q1": 2,  # 6-30 minutes to first cigarette
    "q2": 1,  # Yes - difficult to refrain
    "q3": 1,  # First cigarette hardest
    "q4": 1,  # 11-20 cigarettes/day
    "q5": 0,  # No - not more in morning
    "q6": 0   # No - not when ill
}

# Validate
validation = fager.validate_answers(answers)
if validation.warnings:
    print("Warnings:", validation.warnings)

# Calculate score
result = fager.calculate_score(answers)
print(f"Score: {result.total_score}/10")  # 5
print(f"Level: {result.dependence_level}")  # Dépendance moyenne
print(f"Interpretation: {result.interpretation}")
# Includes: "Substitution nicotinique recommandée pour le sevrage"
```

## Integration Ready

✅ FastAPI compatible (Pydantic models)
✅ Frontend ready (complete questionnaire structure)
✅ Type-safe (type hints throughout)
✅ Validated (comprehensive test suite)
✅ Documented (inline documentation + scoring guide)
✅ Consistent with other questionnaires

## Clinical Notes

### Reference Period
**Current smoking habits** (Habitudes actuelles de tabagisme)

### Key Clinical Points
1. **Physical dependence indicators**:
   - Time to first cigarette (Q1) - strongest predictor
   - First cigarette hardest to give up (Q3)
   
2. **Consumption patterns**:
   - Cigarettes per day (Q4)
   - Morning smoking intensity (Q5)
   
3. **Behavioral dependence**:
   - Difficulty refraining in forbidden places (Q2)
   - Smoking when ill (Q6)

### Interpretation Guidelines
- **Q1 = 3 (within 5 min)**: Strong physical dependence
- **Q4 = 3 (≥31 cigs/day)**: Major health risk, urgent intervention
- **Score ≥6**: Consider combination therapy (NRT + counseling)
- **Score ≥8**: High-intensity intervention recommended

## References

1. **Original Publication**:
   - Fagerström K.O. "Measuring degree of physical dependence to tobacco smoking with reference to individualization of treatment." Br J Addict. 1991;86(6):543-547.

2. **French Version**:
   - Validated French translation
   - FAGERSTROM.pdf (version FR)
   - FAGERSTROM_CotationScore.docx

## Modified Files

1. **`questionnaires/__init__.py`** - Added Fagerstrom exports
2. **`tests/conftest.py`** - Added Fagerstrom fixtures
3. **`verify_tests.py`** - Added Fagerstrom verification

## Statistics

- **Python code**: ~500 lines (class + tests)
- **Test methods**: 37
- **Test classes**: 6
- **Score range**: 0-10
- **Questions**: 6 items
- **Dependencies**: pydantic (same as other questionnaires)

## Total Project Status

The QuestionnairesAPI now includes **6 validated questionnaires**:
1. QIDS-SR16 (Depression)
2. MDQ (Bipolar screening)
3. ASRM (Mania)
4. Epworth (Sleepiness)
5. EQ-5D-EL (Quality of life)
6. **Fagerström (Nicotine dependence)** ← NEW

All questionnaires follow the same architecture and are fully integrated.
