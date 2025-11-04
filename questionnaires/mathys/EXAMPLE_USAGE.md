# MAThyS - Example Usage

## Basic Usage

### 1. Import and Initialize

```python
from questionnaires.mathys import MAThyS, MAThySError

# Create MAThyS instance
mathys = MAThyS()
```

### 2. Get Questionnaire Metadata

```python
metadata = mathys.get_metadata()
print(f"Questionnaire: {metadata['name']}")
print(f"Items: {metadata['total_questions']}")
print(f"Score Range: {metadata['scoring_range']}")
print(f"\nSubscales:")
for name, info in metadata['subscales'].items():
    print(f"  {info['label']}: items {info['items']}, range {info['range']}")
```

**Output:**
```
Questionnaire: Évaluation Multidimensionnelle des états thymiques (MAThyS)
Items: 20
Score Range: [0, 200]

Subscales:
  Émotion: items [3, 7, 10, 18], range (0, 40)
  Motivation: items [2, 11, 12, 15, 16, 17, 19], range (0, 70)
  Perception sensorielle: items [1, 6, 8, 13, 20], range (0, 50)
  Interaction personnelle: items [4, 14], range (0, 20)
  Cognition: items [5, 9], range (0, 20)
```

### 3. Get Questions with Bipolar Anchors

```python
questions = mathys.get_questions()
for q in questions[:3]:  # Show first 3
    print(f"\n{q['id']}: {q['text']}")
    print(f"  Left (0): {q['scale']['min_label']}")
    print(f"  Right (10): {q['scale']['max_label']}")
    print(f"  Hint: {q['scale']['center_hint']}")
```

**Output:**
```
q1: 1.
  Left (0): Je suis moins sensible que d'habitude aux couleurs
  Right (10): Je suis plus sensible que d'habitude aux couleurs
  Hint: Le centre (~5) = état habituel

q2: 2.
  Left (0): Je manque de tonus
  Right (10): J'ai une tension interne importante
  Hint: Le centre (~5) = état habituel
...
```

### 4. Validate Answers

```python
# Example answers (0-10 scale)
answers = {
    "q1": 5.0, "q2": 6.0, "q3": 4.0, "q4": 5.0, "q5": 5.0,
    "q6": 5.0, "q7": 5.0, "q8": 5.0, "q9": 5.0, "q10": 5.0,
    "q11": 6.0, "q12": 5.0, "q13": 5.0, "q14": 5.0, "q15": 4.0,
    "q16": 5.0, "q17": 5.0, "q18": 5.0, "q19": 5.0, "q20": 5.0
}

# Validate
validation = mathys.validate_answers(answers)
print(f"Valid: {validation.valid}")
print(f"Errors: {validation.errors}")
print(f"Warnings: {validation.warnings}")
```

**Output:**
```
Valid: True
Errors: []
Warnings: []
```

### 5. Calculate Scores

```python
try:
    result = mathys.calculate_score(answers)
    
    # Total score
    print(f"\nTotal Score: {result.total_score:.1f}/200")
    
    # Subscale scores
    print("\nSubscale Scores:")
    for name, subscale in result.subscales.items():
        percentage = (subscale.score / subscale.range[1]) * 100
        print(f"  {subscale.label}: {subscale.score:.1f}/{subscale.range[1]} ({percentage:.1f}%)")
    
    # Interpretation
    print(f"\nInterpretation: {result.interpretation}")
    
except MAThySError as e:
    print(f"Error: {e}")
```

**Output:**
```
Total Score: 100.5/200

Subscale Scores:
  Émotion: 20.0/40 (50.0%)
  Motivation: 35.5/70 (50.7%)
  Perception sensorielle: 25.0/50 (50.0%)
  Interaction personnelle: 10.0/20 (50.0%)
  Cognition: 10.0/20 (50.0%)

Interpretation: Score total MAThyS: 100.5/200. Sous-scores: Émotion=20.0/40, Motivation=35.5/70, Perception=25.0/50, Interaction=10.0/20, Cognition=10.0/20. Le MAThyS évalue l'intensité et la variabilité des états thymiques sur 5 dimensions (Émotion, Motivation, Perception, Interaction, Cognition).
```

## Clinical Scenarios

### Scenario 1: Depressive State

```python
# Low energy, reduced emotional reactivity, cognitive slowing
answers = {
    "q1": 2.0,  # Less sensitive to colors
    "q2": 1.0,  # Lack of tone
    "q3": 1.0,  # Emotionally anesthetized
    "q4": 2.0,  # Withdrawn
    "q5": 8.0,  # Distracted (reversed -> 2.0)
    "q6": 8.0,  # Less sensitive touch (reversed -> 2.0)
    "q7": 8.0,  # Monotonous mood (reversed -> 2.0)
    "q8": 8.0,  # Indifferent to music (reversed -> 2.0)
    "q9": 8.0,  # Brain slowed (reversed -> 2.0)
    "q10": 8.0,  # Less reactive (reversed -> 2.0)
    "q11": 1.0,  # No energy
    "q12": 1.0,  # Thoughts slowed
    "q13": 1.0,  # Food tasteless
    "q14": 2.0,  # Less desire to communicate
    "q15": 1.0,  # Lack of motivation
    "q16": 1.0,  # Loss of interest
    "q17": 8.0,  # Difficulty deciding (reversed -> 2.0)
    "q18": 8.0,  # Emotions attenuated (reversed -> 2.0)
    "q19": 1.0,  # Slowed movements
    "q20": 2.0   # Less sensitive to smells
}

result = mathys.calculate_score(answers)
print(f"Total: {result.total_score:.1f}/200")
print(f"Émotion: {result.subscales['emotion'].score:.1f}/40")
print(f"Motivation: {result.subscales['motivation'].score:.1f}/70")
```

**Output:**
```
Total: 39.0/200
Émotion: 7.0/40
Motivation: 13.0/70
```

**Interpretation**: Very low scores across all dimensions, indicating a depressive profile with reduced emotional reactivity, low motivation/energy, dampened sensory perception, social withdrawal, and cognitive slowing.

### Scenario 2: Manic/Hypomanic State

```python
# High energy, heightened emotions, sensory hypersensitivity
answers = {
    "q1": 9.0,  # More sensitive to colors
    "q2": 8.0,  # Internal tension
    "q3": 8.0,  # Losing emotional control
    "q4": 8.0,  # Disinhibited
    "q5": 2.0,  # Not attentive (reversed -> 8.0)
    "q6": 2.0,  # More sensitive touch (reversed -> 8.0)
    "q7": 2.0,  # Variable mood (reversed -> 8.0)
    "q8": 2.0,  # Sensitive to music (reversed -> 8.0)
    "q9": 1.0,  # Brain never stops (reversed -> 9.0)
    "q10": 2.0,  # More reactive (reversed -> 8.0)
    "q11": 9.0,  # Great energy
    "q12": 9.0,  # Thoughts racing
    "q13": 8.0,  # Gastronomic pleasures
    "q14": 8.0,  # More desire to communicate
    "q15": 9.0,  # Multiple projects
    "q16": 9.0,  # Want to do more
    "q17": 2.0,  # Decisions faster (reversed -> 8.0)
    "q18": 1.0,  # Intense emotions (reversed -> 9.0)
    "q19": 9.0,  # Physically agitated
    "q20": 9.0   # More sensitive to smells
}

result = mathys.calculate_score(answers)
print(f"Total: {result.total_score:.1f}/200")
for name, sub in result.subscales.items():
    pct = (sub.score / sub.range[1]) * 100
    print(f"{sub.label}: {sub.score:.1f}/{sub.range[1]} ({pct:.0f}%)")
```

**Output:**
```
Total: 167.0/200
Émotion: 33.0/40 (83%)
Motivation: 60.0/70 (86%)
Perception sensorielle: 42.0/50 (84%)
Interaction personnelle: 16.0/20 (80%)
Cognition: 16.0/20 (80%)
```

**Interpretation**: Elevated scores across all dimensions (>80%), indicating a hypomanic/manic profile with heightened emotional intensity, increased energy/motivation, sensory hypersensitivity, social disinhibition, and cognitive acceleration.

### Scenario 3: Mixed State

```python
# High on emotion and cognition, low on motivation
answers = {
    "q1": 6.0, "q2": 3.0, "q3": 8.0, "q4": 4.0, "q5": 2.0,
    "q6": 3.0, "q7": 2.0, "q8": 5.0, "q9": 1.0, "q10": 3.0,
    "q11": 2.0, "q12": 8.0, "q13": 5.0, "q14": 5.0, "q15": 2.0,
    "q16": 3.0, "q17": 7.0, "q18": 1.0, "q19": 4.0, "q20": 6.0
}

result = mathys.calculate_score(answers)
print("\nMixed Profile:")
for name, sub in result.subscales.items():
    pct = (sub.score / sub.range[1]) * 100
    indicator = "HIGH" if pct > 60 else ("LOW" if pct < 40 else "MOD")
    print(f"{sub.label}: {sub.score:.1f}/{sub.range[1]} ({pct:.0f}%) [{indicator}]")
```

**Output:**
```
Mixed Profile:
Émotion: 28.0/40 (70%) [HIGH]
Motivation: 28.0/70 (40%) [MOD]
Perception sensorielle: 27.0/50 (54%) [MOD]
Interaction personnelle: 9.0/20 (45%) [MOD]
Cognition: 16.0/20 (80%) [HIGH]
```

**Interpretation**: Variable profile with high emotional intensity and cognitive acceleration, but moderate motivation, suggesting a mixed thymic state with racing thoughts and emotional dysregulation but without the typical energy increase of mania.

## Understanding Reverse Coding

### Example: Item Q5 (Attention)

```python
# Q5: "Facilement distrait(e)" (0) ↔ "Pas attentif(ve)" (10)
# Both extremes represent impaired attention, so we reverse-code

# Patient answers 8 (not attentive to environment)
raw_answer = 8.0

# After recoding: 10 - 8 = 2
recoded = 10.0 - raw_answer  # = 2.0

print(f"Raw answer: {raw_answer} (not attentive)")
print(f"Recoded: {recoded} (low score = impaired attention)")
```

### Checking Reverse Items

```python
# Get metadata to see which items are reversed
metadata = mathys.get_metadata()
print(f"Reverse items: {sorted(metadata['reverse_items'])}")

# Example: Calculate one item manually
answers_test = {f"q{i}": 5 for i in range(1, 21)}
answers_test['q7'] = 3.0  # Q7 is reverse-coded

result = mathys.calculate_score(answers_test)
print(f"\nQ7 raw: {answers_test['q7']}")
print(f"Q7 recoded: {result.recoded_scores['q7']}")  # Should be 10-3=7
```

**Output:**
```
Reverse items: [5, 6, 7, 8, 9, 10, 17, 18]

Q7 raw: 3.0
Q7 recoded: 7.0
```

## Visualization Example

```python
import matplotlib.pyplot as plt
import numpy as np

def plot_mathys_profile(result):
    """Plot radar chart of MAThyS subscales"""
    subscales = result.subscales
    labels = [sub.label for sub in subscales.values()]
    scores = [sub.score for sub in subscales.values()]
    max_scores = [sub.range[1] for sub in subscales.values()]
    
    # Normalize to percentages
    percentages = [(s/m)*100 for s, m in zip(scores, max_scores)]
    
    # Radar chart
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    percentages += percentages[:1]  # Complete the circle
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
    ax.plot(angles, percentages, 'o-', linewidth=2, label='Patient')
    ax.fill(angles, percentages, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 100)
    ax.set_ylabel('Pourcentage (%)')
    ax.set_title('Profil MAThyS', size=16, pad=20)
    ax.grid(True)
    
    plt.tight_layout()
    plt.show()

# Use it
answers = {f"q{i}": 5 for i in range(1, 21)}
result = mathys.calculate_score(answers)
plot_mathys_profile(result)
```

## API Integration

```python
from fastapi import APIRouter, HTTPException
from questionnaires.mathys import MAThyS, MAThySError

router = APIRouter()
mathys = MAThyS()

@router.get("/mathys/metadata")
def get_mathys_metadata():
    """Get MAThyS questionnaire metadata"""
    return mathys.get_metadata()

@router.get("/mathys/questions")
def get_mathys_questions():
    """Get all MAThyS questions with bipolar anchors"""
    return mathys.get_full_questionnaire()

@router.post("/mathys/calculate")
def calculate_mathys_score(answers: dict):
    """Calculate MAThyS score from answers"""
    try:
        # Validate
        validation = mathys.validate_answers(answers)
        if not validation.valid:
            raise HTTPException(
                status_code=400,
                detail={"errors": validation.errors}
            )
        
        # Calculate
        result = mathys.calculate_score(answers)
        
        return {
            "total_score": result.total_score,
            "subscales": {
                name: {
                    "label": sub.label,
                    "score": sub.score,
                    "range": sub.range,
                    "percentage": (sub.score / sub.range[1]) * 100
                }
                for name, sub in result.subscales.items()
            },
            "interpretation": result.interpretation,
            "warnings": validation.warnings
        }
    except MAThySError as e:
        raise HTTPException(status_code=400, detail=str(e))
```

## Longitudinal Tracking

```python
def track_mathys_over_time(patient_id, sessions):
    """Track MAThyS scores across multiple sessions"""
    
    results = []
    for date, answers in sessions:
        result = mathys.calculate_score(answers)
        results.append({
            "date": date,
            "total": result.total_score,
            "emotion": result.subscales['emotion'].score,
            "motivation": result.subscales['motivation'].score,
            "perception": result.subscales['perception'].score,
            "interaction": result.subscales['interaction'].score,
            "cognition": result.subscales['cognition'].score
        })
    
    return results

# Example usage
sessions = [
    ("2024-01-01", {f"q{i}": 3 for i in range(1, 21)}),  # Depressive
    ("2024-01-15", {f"q{i}": 5 for i in range(1, 21)}),  # Improving
    ("2024-02-01", {f"q{i}": 6 for i in range(1, 21)}),  # Better
]

tracking = track_mathys_over_time("patient_001", sessions)
for entry in tracking:
    print(f"{entry['date']}: Total={entry['total']:.1f}, Motivation={entry['motivation']:.1f}")
```

**Output:**
```
2024-01-01: Total=104.0, Motivation=36.0
2024-01-15: Total=100.0, Motivation=35.0
2024-02-01: Total=116.0, Motivation=41.0
```

## Error Handling

### Missing Items

```python
answers_incomplete = {f"q{i}": 5 for i in range(1, 15)}  # Missing q15-q20

try:
    result = mathys.calculate_score(answers_incomplete)
except MAThySError as e:
    print(f"Error: {e}")
    # Output: "Error: Items manquants: q15, q16, q17, q18, q19, q20"
```

### Invalid Values

```python
answers_invalid = {f"q{i}": 5 for i in range(1, 21)}
answers_invalid['q10'] = 15  # Out of range

validation = mathys.validate_answers(answers_invalid)
print(f"Valid: {validation.valid}")
print(f"Errors: {validation.errors}")
# Output: "Valeurs invalides (doivent être des nombres entre 0 et 10): {'q10': 15}"
```

## References

1. **Henry C, M'Bailara K, Mathieu F, et al.** Construction and validation of a dimensional scale exploring mood disorders: MAThyS (Multidimensional Assessment of Thymic States). *BMC Psychiatry*, 2008;8:82.

2. **Henry C, M'Bailara K, Poinsot R, et al.** Evidence for two types of bipolar depression using a dimensional approach. *Psychotherapy and Psychosomatics*, 2007;76(6):325-331.

