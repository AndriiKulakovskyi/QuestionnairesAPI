# QIDS-SR16 - Explicit Scoring Rules Example

**Questionnaire**: Quick Inventory of Depressive Symptomatology - Self-Report 16 (QIDS-SR16)  
**Date**: 2025-11-04  
**Purpose**: Demonstrate frontend-friendly explicit scoring rules for mutually exclusive symptom groups

---

## Overview

The QIDS-SR16 has **mutually exclusive symptom groups** where only the **maximum score** from each group contributes to the total, not the sum. This document provides usage examples for frontend developers implementing score calculators and validators.

---

## Key Features

### 1. **Mutually Exclusive Domains**

Three symptom domains use `max()` aggregation instead of summing:

| Domain | Questions | Rationale |
|--------|-----------|-----------|
| **Sleep** | Q1-Q4 | Patient experiences either insomnia OR hypersomnia, not both |
| **Appetite/Weight** | Q6-Q9 | Patient experiences either appetite/weight loss OR gain, not both |
| **Psychomotor** | Q15-Q16 | Patient experiences either slowing OR agitation, not both |

### 2. **Direct Items**

Six questions contribute directly to the total (no grouping):
- Q5: Tristesse (Sadness)
- Q10: Concentration/Décisions
- Q11: Opinion de soi (Self-view)
- Q12: Pensées de mort/suicide (Suicidal ideation)
- Q13: Intérêt général (Interest)
- Q14: Niveau d'énergie (Energy)

### 3. **Total Score Formula**

```
Total = max(Q1-Q4) + Q5 + max(Q6-Q9) + Q10 + Q11 + Q12 + Q13 + Q14 + max(Q15-Q16)
Range: [0, 27]
```

---

## API Usage Examples

### Example 1: Retrieve Scoring Rules

```python
from questionnaires.auto.qids import QIDSSR16

qids = QIDSSR16()
rules = qids.get_scoring_rules()

print(rules['type'])  # "mutually_exclusive_groups"
print(rules['schema_version'])  # "1.0"

# Check sleep domain
sleep_domain = next(d for d in rules['domains'] if d['id'] == 'sleep')
print(sleep_domain)
# {
#     'id': 'sleep',
#     'label': 'Sommeil',
#     'items': ['q1', 'q2', 'q3', 'q4'],
#     'aggregation': 'max',
#     'range': [0, 3],
#     'rationale': 'Patient experiences either difficulty sleeping OR excessive sleep, not both simultaneously'
# }
```

### Example 2: Get Question-Level Scoring Metadata

```python
from questionnaires.auto.qids import QIDSSR16

qids = QIDSSR16()
questions = qids.get_questions()

# Check sleep questions (Q1-4)
for q_id in ['q1', 'q2', 'q3', 'q4']:
    q = next(q for q in questions if q['id'] == q_id)
    print(f"{q_id}: group={q.get('scoring_group_id')}, agg={q.get('scoring_aggregation')}")
    # q1: group=sleep, agg=max
    # q2: group=sleep, agg=max
    # q3: group=sleep, agg=max
    # q4: group=sleep, agg=max

# Check direct item (Q5)
q5 = next(q for q in questions if q['id'] == 'q5')
print(f"q5: group={q5.get('scoring_group_id')}, agg={q5.get('scoring_aggregation')}")
# q5: group=None, agg=None (direct scoring)
```

### Example 3: Calculate Score (Backend)

```python
from questionnaires.auto.qids import QIDSSR16

qids = QIDSSR16()

answers = {
    "q1": 2, "q2": 3, "q3": 1, "q4": 0,  # Sleep: max(2,3,1,0) = 3
    "q5": 2,  # Sadness: 2
    "q6": 1, "q7": 0, "q8": 3, "q9": 2,  # Appetite/Weight: max(1,0,3,2) = 3
    "q10": 1, "q11": 2, "q12": 0, "q13": 1, "q14": 2,  # Direct: 1+2+0+1+2 = 6
    "q15": 2, "q16": 1  # Psychomotor: max(2,1) = 2
}

result = qids.calculate_score(answers)

print(result.total_score)  # 16 (= 3 + 2 + 3 + 6 + 2)
print(result.severity)  # "Dépression sévère"
print(result.domain_scores)
# {
#     'sleep': 3,
#     'sadness': 2,
#     'appetite_weight': 3,
#     'concentration': 1,
#     'self_view': 2,
#     'suicidal_ideation': 0,
#     'interest': 1,
#     'energy': 2,
#     'psychomotor': 2
# }
```

### Example 4: Validation Warnings for Mutual Exclusivity

```python
from questionnaires.auto.qids import QIDSSR16

qids = QIDSSR16()
rules = qids.get_scoring_rules()

# Check validation warnings structure
warnings = rules['validation']['warning_if_both_endorsed']

# Sleep group warnings
sleep_warnings = next(g for g in warnings if g['group'] == 'sleep')
print(sleep_warnings['pairs'])
# [
#     {
#         'items': ['q1', 'q2', 'q3'],
#         'vs': ['q4'],
#         'warning': 'Patient endorsed both insomnia symptoms and hypersomnia'
#     }
# ]

# Appetite/weight warnings
appetite_warnings = next(g for g in warnings if g['group'] == 'appetite_weight')
print(appetite_warnings['pairs'])
# [
#     {'items': ['q6'], 'vs': ['q7'], 'warning': '...appetite decrease and increase'},
#     {'items': ['q8'], 'vs': ['q9'], 'warning': '...weight loss and gain'}
# ]
```

---

## Scoring Logic Breakdown

### Sleep Domain (Q1-Q4)

**Items**:
- Q1: Endormissement (Difficulty falling asleep)
- Q2: Sommeil pendant la nuit (Nighttime awakenings)
- Q3: Réveil avant l'heure prévue (Early morning awakening)
- Q4: Sommeil excessif (Hypersomnia)

**Aggregation**: `max(Q1, Q2, Q3, Q4)`

**Rationale**: A patient typically experiences either:
- **Insomnia** (Q1, Q2, Q3 > 0, Q4 = 0), OR
- **Hypersomnia** (Q1, Q2, Q3 = 0, Q4 > 0)

Not both simultaneously. Taking the max captures the worst sleep disturbance.

**Example**:
```python
# Insomnia pattern
q1, q2, q3, q4 = 3, 2, 2, 0
sleep_score = max(3, 2, 2, 0)  # 3

# Hypersomnia pattern
q1, q2, q3, q4 = 0, 0, 0, 3
sleep_score = max(0, 0, 0, 3)  # 3

# Both patterns yield the same contribution
```

### Appetite/Weight Domain (Q6-Q9)

**Items**:
- Q6: Diminution de l'appétit (Decreased appetite)
- Q7: Augmentation de l'appétit (Increased appetite)
- Q8: Perte de poids (Weight loss)
- Q9: Prise de poids (Weight gain)

**Aggregation**: `max(Q6, Q7, Q8, Q9)`

**Rationale**: A patient experiences either:
- **Appetite/weight loss** (Q6, Q8 > 0, Q7, Q9 = 0), OR
- **Appetite/weight gain** (Q7, Q9 > 0, Q6, Q8 = 0)

**Example**:
```python
# Decreased appetite + weight loss
q6, q7, q8, q9 = 3, 0, 2, 0
appetite_weight_score = max(3, 0, 2, 0)  # 3

# Increased appetite + weight gain
q6, q7, q8, q9 = 0, 3, 0, 2
appetite_weight_score = max(0, 3, 0, 2)  # 3
```

### Psychomotor Domain (Q15-Q16)

**Items**:
- Q15: Impression de ralentissement (Psychomotor slowing)
- Q16: Impression d'agitation (Psychomotor agitation)

**Aggregation**: `max(Q15, Q16)`

**Rationale**: A patient experiences either slowing OR agitation, not both.

**Example**:
```python
# Slowing
q15, q16 = 3, 0
psychomotor_score = max(3, 0)  # 3

# Agitation
q15, q16 = 0, 3
psychomotor_score = max(0, 3)  # 3
```

---

## Frontend Implementation Guide

### Step 1: Load Scoring Rules

```typescript
const response = await fetch('/api/questionnaires/qids-sr16');
const data = await response.json();

const questions = data.questions;
const rules = data.scoring_rules;  // from get_scoring_rules()
```

### Step 2: Calculate Score (Frontend Calculator)

```typescript
function calculateQIDSScore(answers: Record<string, number>) {
  const rules = data.scoring_rules;
  let total = 0;
  
  // Process domains (max aggregation)
  for (const domain of rules.domains) {
    const domainScores = domain.items.map(id => answers[id] || 0);
    const domainMax = Math.max(...domainScores);
    total += domainMax;
    
    console.log(`${domain.label}: max(${domainScores.join(',')}) = ${domainMax}`);
  }
  
  // Process direct items (simple sum)
  for (const item of rules.direct_items) {
    const score = answers[item.id] || 0;
    total += score;
    
    console.log(`${item.label}: ${score}`);
  }
  
  return total;
}

// Example usage
const answers = {
  q1: 2, q2: 3, q3: 1, q4: 0,  // max = 3
  q5: 2,
  q6: 1, q7: 0, q8: 3, q9: 2,  // max = 3
  q10: 1, q11: 2, q12: 0, q13: 1, q14: 2,  // sum = 6
  q15: 2, q16: 1  // max = 2
};

const score = calculateQIDSScore(answers);
console.log(`Total Score: ${score}/27`);  // 16
```

### Step 3: Validate Mutual Exclusivity (Frontend Warnings)

```typescript
function checkMutualExclusivity(answers: Record<string, number>) {
  const warnings = [];
  const validationRules = data.scoring_rules.validation.warning_if_both_endorsed;
  
  for (const group of validationRules) {
    for (const pair of group.pairs) {
      const itemsScores = pair.items.map(id => answers[id] || 0);
      const vsScores = pair.vs.map(id => answers[id] || 0);
      
      const itemsEndorsed = itemsScores.some(s => s > 0);
      const vsEndorsed = vsScores.some(s => s > 0);
      
      if (itemsEndorsed && vsEndorsed) {
        warnings.push({
          group: group.group,
          items: [...pair.items, ...pair.vs],
          message: pair.warning
        });
      }
    }
  }
  
  return warnings;
}

// Example usage
const warningsExample = checkMutualExclusivity({
  q1: 3,  // Insomnia
  q4: 2,  // Hypersomnia (conflicting!)
  q6: 2,  // Decreased appetite
  q7: 1,  // Increased appetite (conflicting!)
  q15: 0,
  q16: 0,
  // ... rest of answers
});

console.log(warningsExample);
// [
//   { group: 'sleep', items: ['q1','q2','q3','q4'], message: '...' },
//   { group: 'appetite_weight', items: ['q6','q7'], message: '...' }
// ]
```

### Step 4: Display Warnings to User

```vue
<template>
  <div>
    <!-- Display warnings if mutual exclusivity violated -->
    <div v-if="warnings.length > 0" class="alert alert-warning">
      <h4>⚠️ Attention: Réponses contradictoires</h4>
      <ul>
        <li v-for="(warning, idx) in warnings" :key="idx">
          {{ warning.message }}
          <br>
          <small>Questions concernées: {{ warning.items.join(', ') }}</small>
        </li>
      </ul>
      <p><small>
        Note: Le score utilisera la valeur maximale parmi les réponses contradictoires.
      </small></p>
    </div>
    
    <!-- Questions... -->
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const answers = ref({});

const warnings = computed(() => checkMutualExclusivity(answers.value));
</script>
```

---

## Interpretation Thresholds

From `get_scoring_rules()['interpretation_thresholds']`:

| Severity | Score Range | Label |
|----------|-------------|-------|
| **None** | 0-5 | Aucune dépression |
| **Mild** | 6-10 | Dépression légère |
| **Moderate** | 11-15 | Dépression modérée |
| **Severe** | 16-20 | Dépression sévère |
| **Very Severe** | 21-27 | Dépression très sévère |

### Frontend Severity Display

```typescript
function getSeverity(score: number): string {
  const thresholds = data.scoring_rules.interpretation_thresholds;
  
  if (score <= thresholds.none[1]) return 'Aucune dépression';
  if (score <= thresholds.mild[1]) return 'Dépression légère';
  if (score <= thresholds.moderate[1]) return 'Dépression modérée';
  if (score <= thresholds.severe[1]) return 'Dépression sévère';
  return 'Dépression très sévère';
}

console.log(getSeverity(3));   // "Aucune dépression"
console.log(getSeverity(8));   // "Dépression légère"
console.log(getSeverity(13));  // "Dépression modérée"
console.log(getSeverity(18));  // "Dépression sévère"
console.log(getSeverity(25));  // "Dépression très sévère"
```

---

## Complete Frontend Example (React)

```tsx
import React, { useState, useMemo } from 'react';

function QIDSCalculator({ questionnaire }) {
  const [answers, setAnswers] = useState({});
  
  // Calculate total score
  const totalScore = useMemo(() => {
    const rules = questionnaire.scoring_rules;
    let total = 0;
    
    // Domains (max aggregation)
    for (const domain of rules.domains) {
      const scores = domain.items.map(id => answers[id] || 0);
      total += Math.max(...scores);
    }
    
    // Direct items
    for (const item of rules.direct_items) {
      total += answers[item.id] || 0;
    }
    
    return total;
  }, [answers, questionnaire]);
  
  // Calculate severity
  const severity = useMemo(() => {
    const t = questionnaire.scoring_rules.interpretation_thresholds;
    if (totalScore <= t.none[1]) return { level: 'none', label: 'Aucune dépression', color: 'green' };
    if (totalScore <= t.mild[1]) return { level: 'mild', label: 'Dépression légère', color: 'yellow' };
    if (totalScore <= t.moderate[1]) return { level: 'moderate', label: 'Dépression modérée', color: 'orange' };
    if (totalScore <= t.severe[1]) return { level: 'severe', label: 'Dépression sévère', color: 'red' };
    return { level: 'very_severe', label: 'Dépression très sévère', color: 'darkred' };
  }, [totalScore, questionnaire]);
  
  // Check mutual exclusivity
  const warnings = useMemo(() => {
    const warningsList = [];
    const rules = questionnaire.scoring_rules.validation.warning_if_both_endorsed;
    
    for (const group of rules) {
      for (const pair of group.pairs) {
        const itemsEndorsed = pair.items.some(id => (answers[id] || 0) > 0);
        const vsEndorsed = pair.vs.some(id => (answers[id] || 0) > 0);
        
        if (itemsEndorsed && vsEndorsed) {
          warningsList.push(pair.warning);
        }
      }
    }
    
    return warningsList;
  }, [answers, questionnaire]);
  
  return (
    <div>
      <h2>QIDS-SR16 Score Calculator</h2>
      
      {/* Questions... (omitted for brevity) */}
      
      {/* Warnings */}
      {warnings.length > 0 && (
        <div className="alert alert-warning">
          <strong>⚠️ Réponses contradictoires détectées:</strong>
          <ul>
            {warnings.map((warning, idx) => (
              <li key={idx}>{warning}</li>
            ))}
          </ul>
        </div>
      )}
      
      {/* Score display */}
      <div className="score-panel" style={{ borderColor: severity.color }}>
        <h3>Score Total: {totalScore}/27</h3>
        <p className="severity" style={{ color: severity.color }}>
          {severity.label}
        </p>
      </div>
    </div>
  );
}

export default QIDSCalculator;
```

---

## Key Takeaways for Frontend Developers

1. **Use `get_scoring_rules()`** to retrieve explicit scoring logic
2. **Process domains with max()**, not sum()
3. **Check `scoring_group_id` and `scoring_aggregation`** on each question
4. **Validate mutual exclusivity** and display warnings (non-blocking)
5. **Frontend and backend must use identical formulas** (single source of truth)
6. **Reference thresholds** from `interpretation_thresholds` for severity labels

---

## Reference Implementation

**Backend**: `questionnaires/auto/qids/qids_sr16.py`  
**Tests**: `tests/test_qids_sr16.py` (see `TestQIDSSR16ScoringRules` and `TestQIDSSR16MutualExclusivity`)

---

## Questions?

If you encounter ambiguity or edge cases not covered here, refer to:
1. The `get_scoring_rules()` method output
2. The `validation` section in scoring rules
3. The comprehensive test suite in `tests/test_qids_sr16.py`

