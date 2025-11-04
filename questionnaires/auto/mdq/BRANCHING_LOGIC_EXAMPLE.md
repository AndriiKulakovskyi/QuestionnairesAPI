# MDQ - Explicit Branching Logic Example

**Questionnaire**: Mood Disorder Questionnaire (MDQ)  
**Date**: 2025-11-04  
**Purpose**: Demonstrate frontend-friendly explicit branching logic for conditional questions

---

## Overview

The MDQ questionnaire has **conditional questions** (Q2 and Q3) that are only displayed and required when the sum of Q1 responses is ≥ 2. This document provides usage examples for frontend developers.

---

## Key Features

### 1. **Conditional Display**
- Q2 and Q3 are **hidden** when Q1 sum < 2
- Q2 and Q3 are **shown** when Q1 sum ≥ 2

### 2. **Conditional Requirements**
- Q2 and Q3 are **optional** when hidden (Q1 sum < 2)
- Q2 and Q3 are **required** when visible (Q1 sum ≥ 2)

### 3. **No Required-But-Hidden Paradox**
- The `required` field on Q2/Q3 is set to `False` by default
- The `required_if` condition makes them required only when visible
- This eliminates validation conflicts

---

## API Usage Examples

### Example 1: Retrieve Branching Logic

```python
from questionnaires.auto.mdq import MDQ

mdq = MDQ()
logic = mdq.get_branching_logic()

print(logic['type'])  # "answer_dependent"
print(logic['schema_version'])  # "1.0"

# Check Q2 visibility rule
q2_visibility = next(r for r in logic['rules'] if r['rule_id'] == 'q2_visibility')
print(q2_visibility)
# {
#     'rule_id': 'q2_visibility',
#     'question_id': 'q2',
#     'rule_type': 'display',
#     'condition': {'>=' : [{'+': [{'var': 'answers.q1_1'}, ...]}, 2]},
#     'description': 'Show Q2 only if at least 2 yes answers in Q1',
#     'action_if_true': 'show',
#     'action_if_false': 'hide'
# }
```

### Example 2: Get Full Questionnaire with Logic

```python
from questionnaires.auto.mdq import MDQ

mdq = MDQ()

# Get questionnaire WITH branching logic (default)
full_with_logic = mdq.get_full_questionnaire()
print('logic' in full_with_logic)  # True

# Get questionnaire WITHOUT logic (lightweight)
full_without_logic = mdq.get_full_questionnaire(include_logic=False)
print('logic' in full_without_logic)  # False
```

### Example 3: Check Question-Level Conditions

```python
from questionnaires.auto.mdq import MDQ

mdq = MDQ()
questions = mdq.get_questions()

# Find Q2
q2 = next(q for q in questions if q['id'] == 'q2')

print(q2['required'])  # False (not hard-required)
print(q2['display_if'])  # JSONLogic condition
print(q2['required_if'])  # Same as display_if

# Q2 becomes required ONLY when displayed
# Frontend should evaluate display_if and required_if at runtime
```

### Example 4: Validation with Conditional Logic

```python
from questionnaires.auto.mdq import MDQ

mdq = MDQ()

# Case 1: Q1 sum < 2 (Q2/Q3 not required)
answers_low = {f"q1_{i}": 0 for i in range(1, 14)}  # All no
validation_low = mdq.validate_answers(answers_low)
print(validation_low.valid)  # True (Q2/Q3 not required)

# Case 2: Q1 sum >= 2 (Q2/Q3 required)
answers_high = {f"q1_{i}": 1 if i <= 3 else 0 for i in range(1, 14)}  # 3 yes
validation_high = mdq.validate_answers(answers_high)
print(validation_high.valid)  # False (missing Q2 and Q3)
print(validation_high.errors)  # ["Q2 est requise...", "Q3 est requise..."]

# Case 3: Q1 sum >= 2 with Q2/Q3 provided
answers_complete = {f"q1_{i}": 1 if i <= 3 else 0 for i in range(1, 14)}
answers_complete.update({"q2": 1, "q3": 2})
validation_complete = mdq.validate_answers(answers_complete)
print(validation_complete.valid)  # True
```

---

## JSONLogic Condition Structure

The conditions use [JSONLogic](https://jsonlogic.com/) format for machine-readable evaluation.

### Q2 Display Condition

```json
{
  ">=": [
    {
      "+": [
        {"var": "answers.q1_1"},
        {"var": "answers.q1_2"},
        {"var": "answers.q1_3"},
        ...
        {"var": "answers.q1_13"}
      ]
    },
    2
  ]
}
```

**Interpretation**: Show Q2 if (q1_1 + q1_2 + ... + q1_13) >= 2

### Q2 Requirement Condition

```json
{
  ">=": [
    {"+": [...]},
    2
  ]
}
```

**Interpretation**: Q2 is required if the same condition is true

---

## Frontend Implementation Guide

### Step 1: Load Questionnaire and Logic

```typescript
const response = await fetch('/api/questionnaires/mdq');
const data = await response.json();

const questions = data.questions;
const logic = data.logic;
```

### Step 2: Evaluate Display Conditions (Reactive)

```typescript
import jsonLogic from 'json-logic-js';

// User answers (reactive state)
const answers = reactive({
  q1_1: 0,
  q1_2: 1,
  q1_3: 1,
  // ...
});

// Find Q2
const q2 = questions.find(q => q.id === 'q2');

// Evaluate display condition
const shouldShowQ2 = jsonLogic.apply(q2.display_if, { answers });

console.log(shouldShowQ2);  // true if sum >= 2, false otherwise
```

### Step 3: Evaluate Requirement Conditions (Reactive)

```typescript
// Evaluate requirement condition
const isQ2Required = jsonLogic.apply(q2.required_if, { answers });

// Render with conditional validation
<input
  v-if="shouldShowQ2"
  :required="isQ2Required"
  v-model="answers.q2"
/>
```

### Step 4: Validation Before Submit

```typescript
function validateBeforeSubmit() {
  const errors = [];
  
  for (const question of questions) {
    const isVisible = question.display_if
      ? jsonLogic.apply(question.display_if, { answers })
      : true;
    
    const isRequired = question.required_if
      ? jsonLogic.apply(question.required_if, { answers })
      : question.required;
    
    if (isVisible && isRequired && !answers[question.id]) {
      errors.push(`Question ${question.id} is required`);
    }
  }
  
  return errors;
}
```

---

## Fallback Behavior

The `fallback_behavior` section in `get_branching_logic()` explicitly defines edge cases:

```json
{
  "when_q1_sum_lt_2": {
    "q2": "hide",
    "q3": "hide",
    "description": "Hide Q2 and Q3 if less than 2 yes answers in Q1"
  },
  "validation": {
    "hidden_questions_not_required": true,
    "description": "Hidden questions (Q2, Q3) are not validated when Q1 sum < 2"
  }
}
```

### Frontend Handling

```typescript
// If Q1 sum < 2, explicitly skip Q2/Q3 validation
if (q1_sum < 2) {
  // Remove Q2/Q3 from validation checks
  delete answers.q2;
  delete answers.q3;
}
```

---

## Complete Working Example (Vue 3)

```vue
<template>
  <div>
    <!-- Q1 Items (always shown) -->
    <div v-for="i in 13" :key="`q1_${i}`">
      <label>
        {{ getQuestion(`q1_${i}`).text }}
        <select v-model.number="answers[`q1_${i}`]">
          <option :value="0">Non</option>
          <option :value="1">Oui</option>
        </select>
      </label>
    </div>

    <!-- Q2 (conditional) -->
    <div v-if="shouldShowQ2">
      <label>
        {{ getQuestion('q2').text }}
        <span v-if="isQ2Required" class="required">*</span>
        <select v-model.number="answers.q2" :required="isQ2Required">
          <option :value="0">Non</option>
          <option :value="1">Oui</option>
        </select>
      </label>
    </div>

    <!-- Q3 (conditional) -->
    <div v-if="shouldShowQ3">
      <label>
        {{ getQuestion('q3').text }}
        <span v-if="isQ3Required" class="required">*</span>
        <select v-model.number="answers.q3" :required="isQ3Required">
          <option :value="0">Pas de problème</option>
          <option :value="1">Problème mineur</option>
          <option :value="2">Problème moyen</option>
          <option :value="3">Problème sérieux</option>
        </select>
      </label>
    </div>

    <button @click="handleSubmit">Submit</button>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import jsonLogic from 'json-logic-js';

const mdqData = ref(null);
const answers = ref({});

// Load MDQ data
async function loadMDQ() {
  const response = await fetch('/api/mdq');
  mdqData.value = await response.json();
  
  // Initialize answers
  for (let i = 1; i <= 13; i++) {
    answers.value[`q1_${i}`] = 0;
  }
}

// Helper to get question by ID
function getQuestion(id) {
  return mdqData.value.questions.find(q => q.id === id);
}

// Computed: Should show Q2
const shouldShowQ2 = computed(() => {
  const q2 = getQuestion('q2');
  if (!q2?.display_if) return true;
  return jsonLogic.apply(q2.display_if, { answers: answers.value });
});

// Computed: Is Q2 required
const isQ2Required = computed(() => {
  const q2 = getQuestion('q2');
  if (!q2?.required_if) return q2.required;
  return jsonLogic.apply(q2.required_if, { answers: answers.value });
});

// Similar for Q3
const shouldShowQ3 = computed(() => {
  const q3 = getQuestion('q3');
  if (!q3?.display_if) return true;
  return jsonLogic.apply(q3.display_if, { answers: answers.value });
});

const isQ3Required = computed(() => {
  const q3 = getQuestion('q3');
  if (!q3?.required_if) return q3.required;
  return jsonLogic.apply(q3.required_if, { answers: answers.value });
});

// Handle submit
async function handleSubmit() {
  // Frontend validation
  const errors = [];
  
  // Q1 validation
  for (let i = 1; i <= 13; i++) {
    if (answers.value[`q1_${i}`] === undefined) {
      errors.push(`Q1_${i} is required`);
    }
  }
  
  // Q2/Q3 conditional validation
  if (shouldShowQ2.value && isQ2Required.value && !answers.value.q2) {
    errors.push('Q2 is required');
  }
  if (shouldShowQ3.value && isQ3Required.value && !answers.value.q3) {
    errors.push('Q3 is required');
  }
  
  if (errors.length > 0) {
    alert('Validation errors: ' + errors.join(', '));
    return;
  }
  
  // Submit to backend
  const response = await fetch('/api/mdq/submit', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(answers.value)
  });
  
  const result = await response.json();
  console.log('Screening result:', result);
}

// Load data on mount
loadMDQ();
</script>
```

---

## Key Takeaways for Frontend Developers

1. **Always check `display_if`** before rendering a question
2. **Evaluate `required_if`** (not just `required`) for validation
3. **Use JSONLogic library** to evaluate conditions consistently
4. **Remove hidden answers** before submission (or backend will warn)
5. **Leverage reactive computed properties** for automatic condition evaluation
6. **Reference `get_branching_logic()`** for comprehensive rules and fallback behavior

---

## Reference Implementation

**Backend**: `questionnaires/auto/mdq/mdq.py`  
**Tests**: `tests/test_mdq.py` (see `TestMDQBranchingLogic` and `TestMDQConditionalValidation`)

---

## Questions?

If you encounter ambiguity or edge cases not covered here, refer to:
1. The `get_branching_logic()` method output
2. The `fallback_behavior` section
3. The comprehensive test suite in `tests/test_mdq.py`

