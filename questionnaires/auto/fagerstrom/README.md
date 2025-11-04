# Fagerström Test for Nicotine Dependence (FTND)

## Overview

The Fagerström Test for Nicotine Dependence (FTND) is a standardized 6-item questionnaire designed to assess the intensity of physical addiction to nicotine. It is widely used in clinical and research settings to evaluate tobacco dependence and guide treatment decisions.

## Structure

### 6-Item Assessment

1. **Q1: Time to First Cigarette** (0-3 points)
   - After 60 minutes: 0
   - 31-60 minutes: 1
   - 6-30 minutes: 2
   - Within 5 minutes: 3

2. **Q2: Difficult to Refrain** (0-1 points)
   - No: 0
   - Yes: 1

3. **Q3: Hardest Cigarette to Give Up** (0-1 points)
   - Any other: 0
   - The first one: 1

4. **Q4: Cigarettes Per Day** (0-3 points)
   - 10 or less: 0
   - 11-20: 1
   - 21-30: 2
   - 31 or more: 3

5. **Q5: Smoke More in Morning** (0-1 points)
   - No: 0
   - Yes: 1

6. **Q6: Smoke When Ill** (0-1 points)
   - No: 0
   - Yes: 1

## Scoring

### Calculation
**Total Score = Q1 + Q2 + Q3 + Q4 + Q5 + Q6**

### Score Range: 0-10

### Interpretation

| Score | Dependence Level | Clinical Recommendation |
|-------|-----------------|-------------------------|
| 0-2 | No/Very Weak | Cessation possible without NRT |
| 3-4 | Weak | Low-dose NRT may help |
| 5 | Medium | NRT recommended |
| ≥6 | Strong | NRT strongly recommended + counseling |

## Usage

### Basic Example

```python
from questionnaires import Fagerstrom

# Initialize
fager = Fagerstrom()

# Patient answers
answers = {
    "q1": 2,  # 6-30 minutes to first cigarette
    "q2": 1,  # Difficult to refrain
    "q3": 1,  # First cigarette hardest
    "q4": 1,  # 11-20 cigarettes/day
    "q5": 0,  # Not more in morning
    "q6": 0   # Not when ill
}

# Validate
validation = fager.validate_answers(answers)
print(f"Valid: {validation.valid}")
if validation.warnings:
    for warning in validation.warnings:
        print(f"⚠️  {warning}")

# Calculate score
result = fager.calculate_score(answers)
print(f"Total Score: {result.total_score}/10")  # 5
print(f"Dependence Level: {result.dependence_level}")  # Dépendance moyenne
print(f"Interpretation: {result.interpretation}")
```

### Output
```
Valid: True
Total Score: 5/10
Dependence Level: Dépendance moyenne
Interpretation: Score FTND: 5/10. Niveau de dépendance: Dépendance moyenne. 
Cigarette matinale précoce (dépendance physique). Première cigarette difficilement 
remplaçable. Dépendance moyenne. Substitution nicotinique recommandée pour le sevrage.
```

## Clinical Interpretation

### Key Indicators

#### Physical Dependence
- **Q1 (Time to first cigarette)**: Most predictive item
  - ≤5 minutes: Strong physical dependence
  - 6-30 minutes: Moderate physical dependence
  
#### Behavioral Dependence
- **Q2 (Difficult to refrain)**: Compulsive use
- **Q6 (Smoke when ill)**: Overriding health concerns

#### Consumption Level
- **Q4 (Cigarettes per day)**: Direct health risk indicator
  - ≥31/day: Major health risk, urgent intervention needed

### Clinical Warnings

The implementation automatically flags:

1. **Very High Score (≥8)**
   - Indicates very strong dependence
   - Suggests need for intensive intervention

2. **Early Morning Smoking (Q1=3)**
   - Within 5 minutes of waking
   - Strong indicator of physical dependence
   - May need higher NRT doses

3. **High Consumption (Q4=3)**
   - ≥31 cigarettes/day
   - Major health risk
   - Urgent intervention recommended

## Treatment Recommendations

### By Dependence Level

#### 0-2: No/Very Weak Dependence
- Behavioral support may be sufficient
- NRT not systematically required
- Focus on motivation and triggers

#### 3-4: Weak Dependence
- Consider low-dose NRT (patch 7-14 mg)
- Behavioral counseling
- Address psychological aspects

#### 5: Medium Dependence
- NRT recommended (patch 14-21 mg or combination)
- Regular follow-up
- Behavioral support

#### ≥6: Strong Dependence
- NRT strongly recommended (patch 21 mg + short-acting form)
- Consider combination therapy
- Intensive counseling
- Close monitoring

### Special Considerations

- **High Q1 score**: May need higher NRT doses initially
- **High Q4 score**: Screen for other substance use
- **Multiple high scores**: Consider referral to specialist

## API Methods

### Core Methods

- **`get_metadata()`** - Instrument information, cutoffs, sources
- **`get_sections()`** - Single section structure
- **`get_questions()`** - All 6 questions with options and scoring
- **`validate_answers(answers)`** - Validation with clinical warnings
- **`calculate_score(answers)`** - Total score, level, interpretation
- **`get_full_questionnaire()`** - Complete structure for frontend

### Return Models

All methods return Pydantic models for type safety:
- `ValidationResult`: valid, errors, warnings
- `ScoreResult`: total_score, dependence_level, interpretation, item_scores

## Validation

### Required
- All 6 questions must be answered
- Q1, Q4: Must be 0, 1, 2, or 3
- Q2, Q3, Q5, Q6: Must be 0 or 1

### Type Checking
- All responses must be integers
- Out-of-range values trigger errors
- Missing questions trigger errors

## Research Background

### Development
- **Author**: Karl Fagerström
- **Year**: 1991 (revision of Fagerström Tolerance Questionnaire)
- **Original**: "Measuring degree of physical dependence to tobacco smoking with reference to individualization of treatment"
- **Journal**: British Journal of Addiction, 86(6), 543-547

### Validation
- Extensively validated across populations
- Correlates with:
  - Biochemical markers (cotinine)
  - Difficulty quitting
  - Withdrawal severity
- Predicts treatment outcomes

### French Version
- Validated French translation
- Widely used in French-speaking clinical settings
- Maintains psychometric properties of original

## Clinical Notes

### Reference Period
**Current smoking habits** (Habitudes actuelles de tabagisme)
- Assesses present behavior, not past
- Should reflect typical daily pattern

### Limitations
- Self-report measure (subject to bias)
- Focuses on cigarette smoking (not other tobacco products)
- Does not assess psychological dependence comprehensively
- Not diagnostic alone - should be part of comprehensive assessment

### Best Practices
1. **Use as screening tool**, not sole diagnostic criterion
2. **Combine with**: Smoking history, quit attempts, motivation
3. **Reassess**: After quit attempts or treatment changes
4. **Consider context**: Stress, mental health, other substances

## References

1. **Original FTND**:
   - Fagerström, K. O. (1991). Measuring degree of physical dependence to tobacco smoking with reference to individualization of treatment. British Journal of Addiction, 86(6), 543-547.

2. **French Version**:
   - Validated French translation
   - FAGERSTROM.pdf (version FR)
   - FAGERSTROM_CotationScore.docx

3. **Clinical Guidelines**:
   - WHO Guidelines on smoking cessation
   - HAS (Haute Autorité de Santé) recommendations

## Integration

### FastAPI Example

```python
from fastapi import FastAPI, HTTPException
from questionnaires import Fagerstrom, FagerstromError

app = FastAPI()
fager = Fagerstrom()

@app.get("/fagerstrom/questions")
async def get_questions():
    """Get questionnaire structure"""
    return fager.get_full_questionnaire()

@app.post("/fagerstrom/score")
async def calculate_score(answers: dict):
    """Calculate FTND score"""
    try:
        result = fager.calculate_score(answers)
        return result.dict()
    except FagerstromError as e:
        raise HTTPException(status_code=400, detail=str(e))
```

## License

This implementation follows the original questionnaire guidelines. The FTND is in the public domain and freely available for clinical and research use.

