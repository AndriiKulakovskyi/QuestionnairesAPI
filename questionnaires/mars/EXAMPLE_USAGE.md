# MARS Questionnaire - Example Usage

## Installation

Ensure you have the required dependencies installed:

```bash
pip install pydantic>=2.5.0
```

## Basic Usage

### 1. Import and Initialize

```python
from questionnaires.mars import MARS, MARSError

# Create MARS instance
mars = MARS()
```

### 2. Get Questionnaire Metadata

```python
metadata = mars.get_metadata()
print(f"Questionnaire: {metadata['name']}")
print(f"Language: {metadata['language']}")
print(f"Total Questions: {metadata['total_questions']}")
print(f"Score Range: {metadata['scoring_range']}")
```

**Output:**
```
Questionnaire: Medication Adherence Rating Scale (MARS) – Version française
Language: fr-FR
Total Questions: 10
Score Range: [0, 10]
```

### 3. Get All Questions

```python
questions = mars.get_questions()
for q in questions:
    print(f"{q['id']}: {q['text']}")
    print(f"  Options: {[opt['label'] for opt in q['options']]}")
```

**Output:**
```
q1: 1. Vous est-il parfois arrivé d'oublier de prendre vos médicaments ?
  Options: ['OUI', 'NON']
q2: 2. Négligez-vous parfois l'heure de prise d'un de vos médicaments ?
  Options: ['OUI', 'NON']
...
```

### 4. Validate Answers

```python
# Example answers (1 = OUI, 0 = NON)
answers = {
    "q1": 0,  # NON - je n'oublie pas
    "q2": 0,  # NON
    "q3": 0,  # NON
    "q4": 0,  # NON
    "q5": 0,  # NON
    "q6": 0,  # NON
    "q7": 1,  # OUI - mes idées sont plus claires
    "q8": 1,  # OUI - je continue pour éviter rechute
    "q9": 0,  # NON
    "q10": 0  # NON
}

# Validate
validation = mars.validate_answers(answers)
print(f"Valid: {validation.valid}")
print(f"Errors: {validation.errors}")
print(f"Warnings: {validation.warnings}")
```

**Output:**
```
Valid: True
Errors: []
Warnings: ['Score très élevé (≥9/10) suggérant une excellente adhérence médicamenteuse.']
```

### 5. Calculate Score

```python
try:
    result = mars.calculate_score(answers)
    print(f"Total Score: {result.total_score}/10")
    print(f"Interpretation: {result.interpretation}")
    print(f"Recoded Scores: {result.recoded_scores}")
except MARSError as e:
    print(f"Error: {e}")
```

**Output:**
```
Total Score: 10/10
Interpretation: Score total MARS: 10/10. Adhérence médicamenteuse excellente (au-dessus de l'IQR supérieur). Le score MARS est un continuum : plus le score est élevé, meilleure est l'adhérence médicamenteuse. Score très élevé (≥9/10) suggérant une excellente adhérence médicamenteuse.
Recoded Scores: {'q1': 1, 'q2': 1, 'q3': 1, 'q4': 1, 'q5': 1, 'q6': 1, 'q7': 1, 'q8': 1, 'q9': 1, 'q10': 1}
```

## Clinical Scenarios

### Scenario 1: Perfect Adherence (Score = 10)

```python
answers = {
    "q1": 0, "q2": 0, "q3": 0, "q4": 0, "q5": 0,
    "q6": 0, "q7": 1, "q8": 1, "q9": 0, "q10": 0
}

result = mars.calculate_score(answers)
# Score: 10/10 - Adhérence excellente
```

**Interpretation:**
- Patient never forgets medications
- Never neglects timing
- Doesn't stop when feeling better or worse
- Takes medication consistently
- Has positive attitude toward medication
- Recognizes benefits (clearer thinking, relapse prevention)
- No side effects (zombie feeling, fatigue)

### Scenario 2: Poor Adherence (Score = 0)

```python
answers = {
    "q1": 1, "q2": 1, "q3": 1, "q4": 1, "q5": 1,
    "q6": 1, "q7": 0, "q8": 0, "q9": 1, "q10": 1
}

result = mars.calculate_score(answers)
# Score: 0/10 - Adhérence très faible
```

**Interpretation:**
- Patient frequently forgets medication
- Neglects timing
- Stops when feeling better or worse
- Only takes when feeling sick
- Negative attitude toward medication
- Doesn't recognize benefits
- Experiences side effects

### Scenario 3: Good Adherence with Occasional Forgetfulness (Score = 9)

```python
answers = {
    "q1": 1,  # Sometimes forgets (OUI)
    "q2": 0, "q3": 0, "q4": 0, "q5": 0,
    "q6": 0, "q7": 1, "q8": 1, "q9": 0, "q10": 0
}

result = mars.calculate_score(answers)
# Score: 9/10 - Adhérence excellente
```

**Interpretation:**
- Overall excellent adherence
- Occasional forgetfulness (common, minor issue)
- Strong positive attitude
- Recognizes benefits
- No side effects

### Scenario 4: Moderate Adherence (Score = 5-6)

```python
answers = {
    "q1": 0, "q2": 0, "q3": 1, "q4": 0, "q5": 1,
    "q6": 1, "q7": 1, "q8": 0, "q9": 0, "q10": 0
}

result = mars.calculate_score(answers)
# Score: 6/10 - Adhérence modérée
```

**Interpretation:**
- Mixed adherence pattern
- Some behavioral issues (stops when better, only takes when sick)
- Ambivalent attitude (doesn't think it's natural)
- Some positive effects recognized
- No side effects

### Scenario 5: Poor Adherence Due to Side Effects (Score = 2-3)

```python
answers = {
    "q1": 1, "q2": 1, "q3": 0, "q4": 1, "q5": 0,
    "q6": 0, "q7": 0, "q8": 0, "q9": 1, "q10": 1
}

result = mars.calculate_score(answers)
# Score: 2/10 - Adhérence faible
```

**Interpretation:**
- Poor adherence
- Multiple behavioral issues
- Doesn't recognize benefits
- Significant side effects (zombie feeling, fatigue)
- Stops medication when feeling worse
- **Clinical action**: Address side effects, consider medication adjustment

## Understanding Reverse Scoring

The MARS uses reverse scoring for different items:

### Negative Items (Items 1-6, 9-10): NO = 1 point, YES = 0 points

These items represent **poor adherence behaviors** or **negative attitudes**:
- q1: Forgetting to take medications
- q2: Neglecting timing
- q3: Stopping when feeling better
- q4: Stopping when feeling worse
- q5: Only taking when sick
- q6: Feeling it's not natural
- q9: Zombie feeling
- q10: Feeling heavy/tired

**Scoring logic**: Answering "NO" indicates good adherence → 1 point

### Positive Items (Items 7-8): YES = 1 point, NO = 0 points

These items represent **positive attitudes**:
- q7: Clearer thinking with medication
- q8: Continuing medication prevents relapse

**Scoring logic**: Answering "YES" indicates good adherence → 1 point

## Error Handling

### Missing Items

```python
answers = {"q1": 0, "q2": 1}  # Missing q3-q10

try:
    result = mars.calculate_score(answers)
except MARSError as e:
    print(f"Error: {e}")
    # Output: "Error: Items manquants: q3, q4, q5, q6, q7, q8, q9, q10"
```

### Invalid Values

```python
answers = {
    "q1": 0, "q2": 0, "q3": 0, "q4": 0, "q5": 0,
    "q6": 0, "q7": 2, "q8": 1, "q9": 0, "q10": 0  # q7=2 is invalid
}

validation = mars.validate_answers(answers)
print(validation.errors)
# Output: ["Valeurs invalides (doivent être 0 (NON) ou 1 (OUI)): {'q7': 2}"]
```

## Clinical Interpretation Guidelines

### Score Ranges

| Score | Interpretation | Clinical Action |
|-------|---------------|-----------------|
| 8-10  | Excellente adhérence | Reinforcement, maintenance |
| 6-7   | Bonne adhérence | Encouragement, monitoring |
| 4-5   | Adhérence modérée | Explore barriers, provide support |
| 0-3   | Adhérence faible | **Urgent intervention required** |

### Typical Distribution

- **Median**: ≈6 (IQR: 4-8)
- **Interpretation**: Continuous scale (no diagnostic cutoff)
- Higher scores = Better adherence

### Clinical Recommendations

**For low scores (≤5)**:
1. Explore barriers to adherence:
   - Forgetfulness → Reminder systems
   - Side effects → Medication adjustment
   - Negative attitudes → Psychoeducation
   - Intentional non-adherence → Motivational interviewing

2. Consider:
   - Medication review
   - Dose adjustment
   - Alternative medications
   - Adherence support interventions

**For high scores (≥8)**:
- Reinforce positive behaviors
- Maintain current support
- Use as baseline for monitoring

## Integration with Clinical Workflow

### Pre-Consultation

```python
# Patient completes questionnaire
mars = MARS()
questions = mars.get_full_questionnaire()
# Send to patient interface

# Patient submits answers
patient_answers = receive_patient_answers()

# Validate before storing
validation = mars.validate_answers(patient_answers)
if validation.valid:
    result = mars.calculate_score(patient_answers)
    store_results(patient_id, result)
else:
    notify_incomplete(patient_id, validation.errors)
```

### During Consultation

```python
# Retrieve results
result = retrieve_mars_results(patient_id)

print(f"Score: {result.total_score}/10")

# Review specific items
if result.recoded_scores['q9'] == 0 or result.recoded_scores['q10'] == 0:
    print("Alert: Patient reports side effects (zombie feeling or fatigue)")
    # Discussion: Consider medication adjustment

if result.recoded_scores['q7'] == 0 or result.recoded_scores['q8'] == 0:
    print("Alert: Patient doesn't recognize benefits")
    # Discussion: Psychoeducation about medication benefits
```

### Longitudinal Monitoring

```python
# Track adherence over time
scores = [
    (baseline_date, 5),      # Baseline: moderate
    (follow_up_1_date, 7),   # 1 month: good
    (follow_up_2_date, 9),   # 3 months: excellent
]

# Analyze trend
print("Adherence improved from 5 to 9 over 3 months")
# Intervention was successful
```

## API Integration Example

```python
from fastapi import APIRouter, HTTPException
from questionnaires.mars import MARS, MARSError

router = APIRouter()
mars = MARS()

@router.get("/mars/metadata")
def get_mars_metadata():
    """Get MARS questionnaire metadata"""
    return mars.get_metadata()

@router.get("/mars/questions")
def get_mars_questions():
    """Get all MARS questions"""
    return mars.get_full_questionnaire()

@router.post("/mars/calculate")
def calculate_mars_score(answers: dict):
    """Calculate MARS score from answers"""
    try:
        # Validate
        validation = mars.validate_answers(answers)
        if not validation.valid:
            raise HTTPException(
                status_code=400,
                detail={"errors": validation.errors}
            )
        
        # Calculate
        result = mars.calculate_score(answers)
        
        return {
            "total_score": result.total_score,
            "interpretation": result.interpretation,
            "recoded_scores": result.recoded_scores,
            "warnings": validation.warnings
        }
    except MARSError as e:
        raise HTTPException(status_code=400, detail=str(e))
```

## References

1. **Thompson K, Kulkarni J, Sergejew AA.** Reliability and validity of a new Medication Adherence Rating Scale (MARS) for the psychoses. *Schizophrenia Research*, 2000;42(3):241–247.

2. **MARS.pdf** - French version questionnaire

3. **MARS_CotationScore.docx** - Scoring rules documentation

## Notes

- The MARS is a **self-report** measure
- Should be complemented with other adherence measures (e.g., pill counts, pharmacy records)
- Useful for identifying adherence barriers
- Can guide targeted interventions
- Suitable for longitudinal monitoring

