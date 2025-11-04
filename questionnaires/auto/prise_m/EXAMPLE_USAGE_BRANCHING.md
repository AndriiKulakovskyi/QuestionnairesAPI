# PRISE-M - Explicit Branching Logic for Frontend Implementation

## Overview

This example demonstrates the enhanced PRISE-M implementation with **explicit branching logic** designed to make frontend implementation straightforward and unambiguous.

## Key Improvements

### 1. Respondent Demographics Schema

The questionnaire now explicitly defines where gender comes from:

```python
from questionnaires.auto.prise_m import PRISEM

prisem = PRISEM()
respondent_schema = prisem.get_respondent_schema()

print(respondent_schema)
```

**Output:**
```json
{
  "schema_version": "1.0",
  "description": "Demographic information required for PRISE-M administration",
  "fields": [
    {
      "id": "gender",
      "label": "Sexe",
      "label_en": "Gender",
      "type": "single_choice",
      "required": true,
      "purpose": "Determines which gender-specific question to display (q20 for F, q25 for M)",
      "options": [
        {
          "code": "F",
          "label": "Femme",
          "label_en": "Female",
          "triggers": "Shows q20 (irregular periods), hides q25 (erectile dysfunction)"
        },
        {
          "code": "M",
          "label": "Homme",
          "label_en": "Male",
          "triggers": "Shows q25 (erectile dysfunction), hides q20 (irregular periods)"
        },
        {
          "code": "X",
          "label": "Autre / Préfère ne pas dire",
          "label_en": "Other / Prefer not to say",
          "triggers": "Hides both q20 and q25, scoring uses 30 items"
        }
      ],
      "validation": {
        "required_message": "Gender is required to determine which questions to display"
      }
    }
  ]
}
```

### 2. Explicit Branching Logic Rules

Machine-readable visibility and requirement rules using JSONLogic:

```python
branching_logic = prisem.get_branching_logic()

print(branching_logic)
```

**Output:**
```json
{
  "schema_version": "1.0",
  "type": "conditional_visibility",
  "rules": [
    {
      "rule_id": "q20_visibility",
      "question_id": "q20",
      "rule_type": "display",
      "condition": {"==": [{"var": "gender"}, "F"]},
      "description": "Show q20 (irregular periods) only for females",
      "action_if_true": "show",
      "action_if_false": "hide"
    },
    {
      "rule_id": "q20_requirement",
      "question_id": "q20",
      "rule_type": "required",
      "condition": {"==": [{"var": "gender"}, "F"]},
      "description": "q20 is required only when visible (female)",
      "action_if_true": "required",
      "action_if_false": "optional"
    },
    {
      "rule_id": "q25_visibility",
      "question_id": "q25",
      "rule_type": "display",
      "condition": {"==": [{"var": "gender"}, "M"]},
      "description": "Show q25 (erectile dysfunction) only for males",
      "action_if_true": "show",
      "action_if_false": "hide"
    },
    {
      "rule_id": "q25_requirement",
      "question_id": "q25",
      "rule_type": "required",
      "condition": {"==": [{"var": "gender"}, "M"]},
      "description": "q25 is required only when visible (male)",
      "action_if_true": "required",
      "action_if_false": "optional"
    }
  ],
  "context_variables": {
    "gender": {
      "source": "respondent.gender",
      "type": "string",
      "allowed_values": ["F", "M", "X"],
      "description": "Gender from respondent demographics"
    }
  },
  "fallback_behavior": {
    "when_gender_is_X": {
      "q20": "hide",
      "q25": "hide",
      "scoring_adjustment": "use_30_items",
      "description": "For non-binary/other gender, hide both items"
    },
    "when_gender_missing": {
      "action": "block_questionnaire",
      "message": "Gender is required to determine which questions to display"
    }
  },
  "scoring_logic": {
    "method": "sum",
    "items_included": "all_visible",
    "conditional_inclusions": [
      {
        "condition": {"==": [{"var": "gender"}, "F"]},
        "include": ["q20"],
        "exclude": ["q25"],
        "expected_item_count": 31,
        "score_range": [0, 62]
      },
      {
        "condition": {"==": [{"var": "gender"}, "M"]},
        "include": ["q25"],
        "exclude": ["q20"],
        "expected_item_count": 31,
        "score_range": [0, 62]
      },
      {
        "condition": {"==": [{"var": "gender"}, "X"]},
        "include": [],
        "exclude": ["q20", "q25"],
        "expected_item_count": 30,
        "score_range": [0, 60]
      }
    ],
    "on_missing_response": "block_submit",
    "validation_message": "All visible questions must be answered before submission"
  }
}
```

### 3. Conditional Requirements in Question Objects

Questions now include `display_if` and `required_if` fields:

```python
# Get gender-specific questions
q20 = prisem.get_question_by_id('q20')
q25 = prisem.get_question_by_id('q25')

print(f"Q20 (Irregular periods):")
print(f"  - required: {q20['required']}")  # False (not hard-required)
print(f"  - display_if: {q20['display_if']}")  # {"==": [{"var": "gender"}, "F"]}
print(f"  - required_if: {q20['required_if']}")  # {"==": [{"var": "gender"}, "F"]}

print(f"\nQ25 (Erectile dysfunction):")
print(f"  - required: {q25['required']}")  # False (not hard-required)
print(f"  - display_if: {q25['display_if']}")  # {"==": [{"var": "gender"}, "M"]}
print(f"  - required_if: {q25['required_if']}")  # {"==": [{"var": "gender"}, "M"]}
```

### 4. Support for Non-Binary/Other Gender

```python
# Get questions for non-binary gender
questions_nonbinary = prisem.get_questions(gender="X")

print(f"Questions for non-binary/other: {len(questions_nonbinary)} items")
# Output: 30 items (excludes both q20 and q25)

# Scoring with non-binary gender
answers = {f"q{i}": 1 for i in range(1, 33) if i not in [20, 25]}
result = prisem.calculate_score(answers, gender="X")

print(f"Total score: {result.total_score}/{result.range[1]}")  # e.g., 30/60
print(f"Items scored: {result.items_scored}")  # 30
print(f"Excluded items: {result.excluded_items}")  # ["q20", "q25"]
print(f"Gender used: {result.gender_used}")  # "X"
```

## Frontend Implementation Guide

### Step 1: Capture Gender First

```javascript
// Get respondent schema
const schema = await fetch('/api/prise-m/respondent-schema');
const respondentSchema = await schema.json();

// Display gender field BEFORE questionnaire
const genderField = respondentSchema.fields.find(f => f.id === 'gender');
// Render gender selection with options F, M, X
```

### Step 2: Fetch Questionnaire with Branching Logic

```javascript
const gender = userSelectedGender; // "F", "M", or "X"

// Get full questionnaire with logic
const response = await fetch(`/api/prise-m/full?gender=${gender}&include_logic=true`);
const questionnaire = await response.json();

// questionnaire contains:
// - metadata: Questionnaire info
// - sections: Section structure
// - questions: Filtered questions (31 for F/M, 30 for X)
// - respondent: Demographic schema
// - logic: Branching rules and scoring logic
```

### Step 3: Apply Visibility Rules

```javascript
// Using json-logic-js library
import jsonLogic from 'json-logic-js';

const context = { gender: userSelectedGender };

questionnaire.questions.forEach(question => {
  if (question.display_if) {
    const shouldDisplay = jsonLogic.apply(question.display_if, context);
    question.visible = shouldDisplay;
  } else {
    question.visible = true; // No condition = always visible
  }
});

// Filter to visible questions
const visibleQuestions = questionnaire.questions.filter(q => q.visible);
```

### Step 4: Apply Conditional Requirements

```javascript
questionnaire.questions.forEach(question => {
  if (question.required_if) {
    const isRequired = jsonLogic.apply(question.required_if, context);
    question.isRequired = isRequired;
  } else {
    question.isRequired = question.required; // Use base required value
  }
});
```

### Step 5: Validation Before Submit

```javascript
function validateQuestionnaire(answers, questionnaire, gender) {
  const errors = [];
  const context = { gender };
  
  questionnaire.questions.forEach(question => {
    // Check if question should be visible
    const shouldDisplay = question.display_if 
      ? jsonLogic.apply(question.display_if, context)
      : true;
    
    if (!shouldDisplay) return; // Skip hidden questions
    
    // Check if question is required
    const isRequired = question.required_if
      ? jsonLogic.apply(question.required_if, context)
      : question.required;
    
    if (isRequired && !answers[question.id]) {
      errors.push(`${question.id} is required`);
    }
  });
  
  return errors;
}
```

### Step 6: Handle Non-Binary Case

```javascript
if (gender === 'X') {
  // Both q20 and q25 are hidden
  // Scoring uses 30 items instead of 31
  // Score range is 0-60 instead of 0-62
  
  const fallback = questionnaire.logic.fallback_behavior.when_gender_is_X;
  console.log(`Scoring adjustment: ${fallback.scoring_adjustment}`);
  // Output: "use_30_items"
}
```

## Complete Example Workflow

```python
from questionnaires.auto.prise_m import PRISEM

prisem = PRISEM()

# ===== Frontend: Initial Load =====
# 1. Get respondent schema
respondent_schema = prisem.get_respondent_schema()
# Display gender selection UI

# ===== User selects gender: Female =====
user_gender = "F"

# 2. Get filtered questionnaire
full_questionnaire = prisem.get_full_questionnaire(gender=user_gender, include_logic=True)

# Questions returned: 31 items (q1-q24, q26-q32)
# q20 is included, q25 is excluded
print(f"Questions to display: {len(full_questionnaire['questions'])}")

# ===== User completes questionnaire =====
answers = {f"q{i}": 0 for i in range(1, 33)}
answers['q3'] = 1  # Dry mouth - tolerable
answers['q20'] = 2  # Irregular periods - burdensome
# q25 is not in the form, so no answer for it

# 3. Validate on backend
validation = prisem.validate_answers(answers, gender=user_gender)
if not validation.valid:
    print(f"Validation errors: {validation.errors}")
else:
    print("Validation passed!")

# 4. Calculate score
result = prisem.calculate_score(answers, gender=user_gender)

print(f"\n===== RESULTS =====")
print(f"Total Score: {result.total_score}/{result.range[1]}")
print(f"Items Scored: {result.items_scored}")
print(f"Excluded Items: {result.excluded_items}")
print(f"Gender: {result.gender_used}")
print(f"\nInterpretation:")
print(result.interpretation)
print(f"\nSection Scores:")
for section_id, score in result.section_scores.items():
    section = next(s for s in prisem.get_sections() if s['id'] == section_id)
    print(f"  {section['label']}: {score}")
```

**Output:**
```
Questions to display: 31
Validation passed!

===== RESULTS =====
Total Score: 3/62
Items Scored: 31
Excluded Items: ['q25']
Gender: F

Interpretation:
Score total PRISE-M: 3/62 (sexe: FEMME, 31 items). Score bas (<15) suggérant peu d'effets indésirables.

Section Scores:
  1. Troubles gastro-intestinaux: 1
  2. Troubles cardiaques: 0
  3. Problèmes cutanés: 0
  4. Troubles neurologiques: 0
  5. Vision/Audition: 0
  6. Troubles uro-génital: 2
  7. Problèmes de sommeil: 0
  8. Fonctions sexuelles: 0
  9. Autres troubles: 0
```

## Addressing the Original Feedback

### ✅ Gender Source Defined

```python
respondent_schema['fields'][0]['id'] == 'gender'
respondent_schema['fields'][0]['purpose'] == "Determines which gender-specific question to display"
```

### ✅ Conditional Requirement (Not Hard-Required)

```python
q20['required'] == False  # Not hard-required
q20['required_if'] == {"==": [{"var": "gender"}, "F"]}  # Required when visible
```

### ✅ Explicit Visibility Contract

```python
q20['display_if'] == {"==": [{"var": "gender"}, "F"]}
q25['display_if'] == {"==": [{"var": "gender"}, "M"]}
```

### ✅ Non-Binary/Unknown Handling

```python
# Gender "X" support built in
questions_x = prisem.get_questions(gender="X")  # Returns 30 items
logic['fallback_behavior']['when_gender_is_X']  # Clear rules defined
```

### ✅ Scoring Logic Explicit

```python
scoring_logic = logic['scoring_logic']
scoring_logic['conditional_inclusions']  # One rule per gender option
# Each rule specifies: condition, include, exclude, expected_item_count, score_range
```

## JSONLogic Evaluation

Frontend can use the `json-logic-js` library to evaluate conditions:

```bash
npm install json-logic-js
```

```javascript
import jsonLogic from 'json-logic-js';

const context = { gender: 'F' };

// Check q20 visibility
const q20_visible = jsonLogic.apply(
  {"==": [{"var": "gender"}, "F"]},
  context
);
// Returns: true

// Check q25 visibility
const q25_visible = jsonLogic.apply(
  {"==": [{"var": "gender"}, "M"]},
  context
);
// Returns: false
```

## Benefits for Frontend Developers

1. **No Guesswork**: All logic is explicit in JSON
2. **Machine-Readable**: JSONLogic can be directly evaluated
3. **Type-Safe**: All conditions are structured data
4. **Self-Documenting**: Each rule includes description
5. **Fallback Handling**: Non-binary and missing gender cases covered
6. **Validation-Ready**: `required_if` prevents hidden-but-required paradox
7. **Scoring Transparency**: Conditional inclusions explicitly defined

## Comparison: Before vs After

### Before (Implicit Logic)

```json
{
  "id": "q20",
  "text": "Règles irrégulières (pour les femmes)",
  "required": true,
  "gender_specific": "F"
}
```

**Problems:**
- How does frontend know to hide this?
- If hidden, validation still requires it (paradox)
- No explicit link to gender source
- Non-binary case undefined

### After (Explicit Logic)

```json
{
  "id": "q20",
  "text": "Règles irrégulières (pour les femmes)",
  "required": false,
  "gender_specific": "F",
  "display_if": {"==": [{"var": "gender"}, "F"]},
  "required_if": {"==": [{"var": "gender"}, "F"]}
}
```

**Plus separate schemas:**
- `respondent_schema`: Defines gender field
- `branching_logic`: Machine-readable rules
- `fallback_behavior`: Non-binary handling

**Result:** Frontend has everything it needs!

## See Also

- [README.md](README.md) - Full clinical documentation
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Quick reference card
- [test_prise_m.py](../../../tests/test_prise_m.py) - Comprehensive tests including branching logic

