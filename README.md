# QuestionnairesAPI

A comprehensive Python package for psychological and psychiatric questionnaires with automated scoring capabilities.

## Overview

This package provides a unified framework for implementing, managing, and scoring various psychological questionnaires used in clinical and research settings. It includes over 150 questionnaires covering multiple domains including depression, anxiety, bipolar disorder, autism, ADHD, and more.

## Installation

```bash
pip install questionnaires-api
```

## Quick Start

```python
from questionnaires_api import get_questionnaire

# Get a questionnaire instance
alda = get_questionnaire("ALDA")

# Get questions for display
questions = alda.get_questions()

# Score responses
responses = {"radhtml_alda_a": "2", "radhtml_alda_b": "1"}  # User responses
result = alda.score_responses(responses)

print(f"Total score: {result.total_score}")
print(f"Interpretation: {result.interpretation}")
```

## Available Questionnaires

### Depression & Mood

| Name | Code | Items | Ready Level | Scoring |
|------|------|-------|-------------|---------|
| Beck Depression Inventory-II | BDI2 | 21 | ✅ Complete | Simple Sum (0-63) |
| Hamilton Depression Rating Scale | HAM_DEPRES | 17 | ✅ Complete | Simple Sum |
| Montgomery-Åsberg Depression Rating Scale | MADRS | 10 | ✅ Complete | Simple Sum |
| Quick Inventory of Depressive Symptomatology | QIDS | 16 | ✅ Complete | Simple Sum |
| Patient Health Questionnaire-9 | PHQ9 | 9 | ✅ Complete | Simple Sum |

### Bipolar Disorder

| Name | Code | Items | Ready Level | Scoring |
|------|------|-------|-------------|---------|
| Young Mania Rating Scale | YMRS | 11 | ✅ Complete | Weighted Sum (0-60) |
| Mood Disorder Questionnaire | MDQ | 13 | ✅ Complete | Conditional |
| Altman Self-Rating Mania Scale | ALTMAN | 5 | ✅ Complete | Simple Sum |
| ALDA | ALDA | 6 | ✅ Complete | Simple Sum |

### Anxiety

| Name | Code | Items | Ready Level | Scoring |
|------|------|-------|-------------|---------|
| Hamilton Anxiety Rating Scale | HAM_ANX | 14 | ✅ Complete | Simple Sum |
| State-Trait Anxiety Inventory | STAIC | 40 | ✅ Complete | Subscale |
| Liebowitz Social Anxiety Scale | LSAS | 24 | ✅ Complete | Simple Sum |

### Autism & ADHD

| Name | Code | Items | Ready Level | Scoring |
|------|------|-------|-------------|---------|
| Autism-Spectrum Quotient | AUT_ABC | 50 | ✅ Complete | Simple Sum |
| ADHD Rating Scale | AUT_ADHDRS | 18 | ✅ Complete | Simple Sum |
| RAADS-R | RAADS | 80 | ✅ Complete | Subscale |
| Wender Utah Rating Scale | WURS | 25 | ✅ Complete | Simple Sum |

### Sleep & Fatigue

| Name | Code | Items | Ready Level | Scoring |
|------|------|-------|-------------|---------|
| Pittsburgh Sleep Quality Index | PSQI | 19 | ✅ Complete | Subscale |
| Epworth Sleepiness Scale | EPWORTH | 8 | ✅ Complete | Simple Sum |
| Fatigue Severity Scale | FSS | 9 | ✅ Complete | Simple Sum |

### Psychosis & Schizophrenia

| Name | Code | Items | Ready Level | Scoring |
|------|------|-------|-------------|---------|
| Brief Psychiatric Rating Scale | AUT_BRIEF | 24 | ✅ Complete | Simple Sum |
| Positive and Negative Syndrome Scale | AUT_SPQ | 30 | ✅ Complete | Subscale |
| Calgary Depression Scale | CALGARY | 9 | ✅ Complete | Simple Sum |

### Personality & Behavior

| Name | Code | Items | Ready Level | Scoring |
|------|------|-------|-------------|---------|
| Barratt Impulsiveness Scale | BIS | 30 | ✅ Complete | Subscale |
| Big Five Inventory | BFI | 44 | ✅ Complete | Subscale |
| Temperament and Character Inventory | AUT_TCI | 240 | ✅ Complete | Subscale |

### Clinical Assessment Forms

| Name | Code | Items | Ready Level | Scoring |
|------|------|-------|-------------|---------|
| Clinical Global Impression | CGI | 3 | ✅ Complete | Simple Sum |
| Mini International Neuropsychiatric Interview | MINI | 120 | ✅ Complete | Conditional |
| Columbia-Suicide Severity Rating Scale | CSSRS | 6 | ✅ Complete | Simple Sum |

### Additional Questionnaires (150+ total)

The package includes many additional questionnaires covering:
- Eating disorders (EAT, SCOFF)
- Obsessive-compulsive disorder (Y-BOCS)
- Post-traumatic stress (PCL-5)
- Substance abuse (AUDIT, DAST)
- Quality of life (EQ-5D, SF-36)
- Cognitive assessments (MoCA, MMSE)
- And many more...

## Scoring Strategies

The package implements multiple scoring strategies:

### SimpleSumStrategy
Most common strategy - sums all question scores.
```python
# Example: BDI2 scoring
# 0-13: Minimal depression
# 14-19: Mild depression  
# 20-28: Moderate depression
# 29-63: Severe depression
```

### WeightedSumStrategy
Applies different weights to specific questions.
```python
# Example: YMRS scoring
# Items 5,6,8,9 have double weight (×2)
# Total range: 0-60
```

### SubscaleStrategy
Calculates scores for multiple domains.
```python
# Example: PSQI scoring
# - Sleep quality
# - Sleep latency  
# - Sleep duration
# - Sleep efficiency
# - Sleep disturbances
# - Sleep medication
# - Daytime dysfunction
```

### ConditionalScoringStrategy
Implements complex conditional logic.
```python
# Example: MDQ screening
# Positive if:
# - ≥7 "yes" answers AND
# - Symptoms occurred together AND
# - Functional impairment ≥2
```

### PercentageStrategy
Converts scores to 0-100 percentage scale.
```python
# Example: Quality of life measures
# Percentage = (actual_score / max_possible) × 100
```

## Usage Examples

### Basic Questionnaire Usage

```python
from questionnaires_api import get_questionnaire

# Get questionnaire
bdi2 = get_questionnaire("BDI2")

# Display questions
for question in bdi2.get_questions():
    print(f"Q{question.id}: {question.text}")
    for option in question.options:
        print(f"  {option.value}: {option.label}")

# Score responses
responses = {
    "bdi2_1": "1",  # Sadness
    "bdi2_2": "2",  # Pessimism
    # ... more responses
}

result = bdi2.score_responses(responses)
print(f"Score: {result.total_score}")
print(f"Interpretation: {result.interpretation}")
```

### Advanced Scoring with Subscales

```python
# Get questionnaire with subscales
psqi = get_questionnaire("PSQI")

result = psqi.score_responses(responses)

# Access subscale scores
for subscale, score in result.subscale_scores.items():
    print(f"{subscale}: {score}")

# Get overall interpretation
print(f"Global sleep quality: {result.interpretation}")
```

### Custom Scoring Logic

```python
from questionnaires_api.core.scoring import ConditionalScoringStrategy

def custom_mdq_scoring(responses, questions):
    yes_count = 0
    for qid, response in responses.responses.items():
        if response == "a":  # "Yes" response
            yes_count += 1
    
    together = responses.get_response("mdq14") == "a"  # Occurred together
    functional_impairment = int(responses.get_response("mdq15", "0"))
    
    if yes_count >= 7 and together and functional_impairment >= 2:
        return ScoreResult(total_score=1, interpretation="Positive for bipolar disorder")
    else:
        return ScoreResult(total_score=0, interpretation="Negative for bipolar disorder")

# Use custom strategy
mdq = get_questionnaire("MDQ")
mdq.scoring_strategy = ConditionalScoringStrategy(custom_mdq_scoring)
```

## API Reference

### Core Functions

- `get_questionnaire(code: str)`: Get questionnaire by code
- `list_questionnaires()`: List all available questionnaires
- `get_questionnaire_metadata(code: str)`: Get questionnaire metadata

### Questionnaire Methods

- `get_questions()`: Get list of questions
- `score_responses(responses: dict)`: Score questionnaire responses
- `validate_responses(responses: dict)`: Validate response format

### Response Format

```python
responses = {
    "question_id": "answer_value",
    # Example:
    "bdi2_1": "1",  # Selected option value
    "ymrs_5": "2",  # Another question
}
```

### Score Result

```python
@dataclass
class ScoreResult:
    total_score: int
    subscale_scores: Dict[str, int] = None
    interpretation: str = None
    warnings: List[str] = None
    raw_values: Dict[str, Any] = None
```

## Architecture

The package follows a modular architecture:

- **Core Models**: Base classes for questions, questionnaires, and responses
- **Scoring Strategies**: Pluggable scoring algorithms
- **Registry System**: Automatic questionnaire registration and discovery
- **Validation**: Input validation and error handling

## Contributing

1. Add new questionnaire in `questionnaires/` directory
2. Implement scoring strategy in `core/scoring.py`
3. Register questionnaire using `@register_questionnaire` decorator
4. Add tests and documentation

## License

© Fondation FondaMental - Version 2.0.0

## Support

For questions or support, please contact Fondation FondaMental or open an issue on the project repository.
