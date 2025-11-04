# ASRM (Altman Self-Rating Mania Scale) - French Version

## Overview

The ASRM is a 5-item self-report questionnaire designed to assess manic and hypomanic symptoms over the past 7 days. Each item is scored from 0 to 4, with higher scores indicating more severe symptoms.

## Structure

- **Items**: 5 questions
- **Scale**: 0-4 per item (0 = no symptom, 4 = severe symptom)
- **Total Score**: 0-20 (sum of all items)
- **Reference Period**: Last 7 days

## Items

1. **Happiness/Cheerfulness** (Humeur/Joie)
2. **Self-Confidence** (Confiance en soi)
3. **Sleep Need** (Besoin de sommeil)
4. **Talkativeness** (Loquacité)
5. **Activity Level** (Niveau d'activité)

## Scoring

### Total Score Calculation
Simple sum of all 5 items: Score = Q1 + Q2 + Q3 + Q4 + Q5

### Interpretation

| Score Range | Interpretation |
|-------------|----------------|
| 0-5 | Low probability of manic/hypomanic episode |
| 6-20 | High probability of manic/hypomanic episode |

### Clinical Cutoffs

- **Cutoff**: ≥6 indicates high probability of manic/hypomanic episode
- **Severe symptoms**: Score ≥12 suggests severe manic symptoms requiring urgent evaluation

## Usage Example

```python
from questionnaires.auto.asrm import ASRM

# Initialize questionnaire
asrm = ASRM()

# Get questionnaire structure
questionnaire = asrm.get_full_questionnaire()

# Example answers (score 11 - high probability)
answers = {
    "q1": 3,  # Happiness: most of the time
    "q2": 2,  # Confidence: often
    "q3": 2,  # Sleep: often less sleep
    "q4": 2,  # Talkativeness: often more
    "q5": 2   # Activity: often more active
}

# Validate answers
validation = asrm.validate_answers(answers)
if validation.valid:
    # Calculate score
    result = asrm.calculate_score(answers)
    print(f"Total Score: {result.total_score}/20")
    print(f"Probability: {result.probability}")
    print(f"Interpretation: {result.interpretation}")
```

## Response Options

Each question has 5 response options (0-4):

### Question 1: Happiness/Cheerfulness
- 0: I do not feel happier or more cheerful than usual
- 1: I occasionally feel happier or more cheerful than usual
- 2: I often feel happier or more cheerful than usual
- 3: I feel happier or more cheerful than usual most of the time
- 4: I feel happier or more cheerful than usual all of the time

### Question 2: Self-Confidence
- 0: I do not feel more self-confident than usual
- 1: I occasionally feel more self-confident than usual
- 2: I often feel more self-confident than usual
- 3: I feel more self-confident than usual most of the time
- 4: I feel extremely self-confident all of the time

### Question 3: Sleep Need
- 0: I do not need less sleep than usual
- 1: I occasionally need less sleep than usual
- 2: I often need less sleep than usual
- 3: I frequently need less sleep than usual
- 4: I can go all day and all night without sleep and not feel tired

### Question 4: Talkativeness
- 0: I do not talk more than usual
- 1: I occasionally talk more than usual
- 2: I often talk more than usual
- 3: I frequently talk more than usual
- 4: I talk constantly and cannot be interrupted

### Question 5: Activity Level
- 0: I have not been more active than usual (socially, sexually, at work, at home or at school)
- 1: I have occasionally been more active than usual
- 2: I have often been more active than usual
- 3: I have frequently been more active than usual
- 4: I am constantly active or on the go all the time

## Clinical Notes

1. **Screening Tool**: ASRM is a screening tool, not a diagnostic instrument
2. **Positive Screen**: Score ≥6 requires clinical follow-up
3. **Severe Symptoms**: Score ≥12 suggests urgent evaluation needed
4. **Multiple Maximums**: 3+ items at maximum score (4) triggers warning for severe symptoms
5. **Recent Period**: Assesses symptoms over last 7 days only

## Validation Rules

- All 5 items must be answered
- Each item must be an integer between 0 and 4
- Clinical consistency warnings triggered for severe patterns

## API Methods

### Core Methods

- `get_metadata()`: Returns instrument metadata
- `get_sections()`: Returns section structure
- `get_questions()`: Returns all questions with options
- `get_question_by_id(question_id)`: Returns specific question
- `validate_answers(answers)`: Validates answer dictionary
- `calculate_score(answers)`: Calculates total score and interpretation
- `get_full_questionnaire()`: Returns complete structure for frontend

### Response Models

- `ScoreResult`: Contains total_score, probability, interpretation, range
- `ValidationResult`: Contains valid (bool), errors (list), warnings (list)

## References

- Altman EG, Hedeker D, Peterson JL, Davis JM. The Altman Self-Rating Mania Scale. Biol Psychiatry. 1997;42(10):948-55.
- DOI: 10.1016/s0006-3223(97)00238-0

## Implementation Details

- **Language**: French (fr-FR)
- **Version**: 1.0
- **Framework**: Pydantic models for type safety
- **Testing**: 45+ comprehensive unit tests
- **Coverage**: >95%

