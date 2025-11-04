# Questionnaire Explicitness Audit

**Date**: November 4, 2025  
**Purpose**: Assess which questionnaires have implicit branching logic that could cause frontend implementation issues

## Summary

After implementing explicit branching logic for PRISE-M, we audited all questionnaires to identify similar issues where conditional logic is implicit rather than machine-readable.

## Audit Results

### ✅ FULLY EXPLICIT - Ready for Frontend

#### PRISE-M
- **Status**: ✅ **COMPLETE** - Fully explicit branching logic implemented
- **Branching**: Gender-specific questions (q20 for females, q25 for males)
- **Implementation**: 
  - ✅ `display_if` and `required_if` JSONLogic conditions
  - ✅ `get_respondent_schema()` defines gender source
  - ✅ `get_branching_logic()` provides machine-readable rules
  - ✅ Fallback behavior for non-binary/other gender
  - ✅ Conditional scoring logic explicit
- **Test Coverage**: 52 tests, 99% coverage, including branching logic tests

### ⚠️ NEEDS EXPLICIT BRANCHING LOGIC

#### MDQ (Mood Disorder Questionnaire)
- **Status**: ⚠️ **NEEDS UPDATE** - Has implicit branching
- **Current Issue**:
  - Q2 text says "Si ≥2 réponses 'oui' à la Q1..." but is hard-required
  - Q3 also conditionally relevant
  - Frontend has no way to know these are conditional
- **Branching Logic**:
  - Q2: Only show if `sum(q1_1...q1_13) >= 2`
  - Q3: Only show if Q2 is visible (some implementations may require Q1 >= 7)
- **Required Changes**:
  ```python
  # Q2 should have:
  required = False
  display_if = {">=": [{"reduce": [...sum of q1 items...], 2}]}
  required_if = {">=": [{"reduce": [...sum of q1 items...], 2}]}
  
  # Q3 should have:
  required = False
  display_if = {conditional on Q1 count or Q2}
  required_if = {same as display_if}
  ```
- **Impact**: Medium - Could lead to validation errors if Q1 < 2 but Q2/Q3 required

#### QIDS-SR16 (Quick Inventory of Depressive Symptomatology)
- **Status**: ⚠️ **NEEDS CLARIFICATION** - Has mutually exclusive items
- **Current Issue**:
  - Sleep domain: Q1-Q4 are mutually exclusive (only max counts)
  - Appetite: Q6-Q9 are mutually exclusive
  - Psychomotor: Q15-Q16 are mutually exclusive
  - This is implicit in scoring logic, not in question definitions
- **Not True Branching**: All questions are displayed, but scoring has special rules
- **Recommended**: Add metadata to questions indicating mutual exclusivity:
  ```python
  # Add to each question in mutually exclusive groups:
  scoring_note = "mutually_exclusive_group"
  group_id = "sleep_domain"  # or "appetite_domain", "psychomotor_domain"
  scoring_rule = "max_of_group"  # Only maximum value counted
  ```
- **Impact**: Low - Doesn't affect display, but scoring logic should be explicit

#### PSQI (Pittsburgh Sleep Quality Index)
- **Status**: ⚠️ **NEEDS DOCUMENTATION** - Complex but not truly branching
- **Current Situation**:
  - Has complex time inputs (e.g., "What time did you go to bed?")
  - Has calculated fields (sleep efficiency based on multiple inputs)
  - Q5 has sub-items (5a-5j)
- **Not True Branching**: All questions shown, complexity is in input types and calculations
- **Recommended**: Document input validation and calculation dependencies
- **Impact**: Low - Mostly about input validation, not conditional display

### ✅ SIMPLE/LINEAR - No Branching Issues

These questionnaires have no conditional logic and all questions are always displayed:

- **ASRM** (Altman Self-Rating Mania): 5 linear questions
- **Epworth**: 8 linear questions  
- **Fagerstrom**: 6 linear questions
- **MARS** (Medication Adherence): 10 linear questions
- **MATHYS**: Fixed questions
- **STAI-YA**: 20 linear questions (with reverse scoring)
- **AIM-Short**: Linear questions
- **ALS-Short**: Linear questions
- **AQ12**: 12 linear questions
- **ASRS**: 18 linear questions
- **BIS-10**: 30 linear questions
- **CSM**: Linear questions
- **CTI**: Linear questions
- **CTQ**: 28 linear questions with subscales
- **EQ-5D-5L**: 5 dimensions + VAS
- **EQ-5D-EL**: Extended version
- **WURS-25**: 25 linear questions

## Priority Recommendations

### High Priority

1. **MDQ** - Implement explicit branching logic
   - Add `display_if` and `required_if` to Q2 and Q3
   - Add `get_branching_logic()` method
   - Update tests to verify conditional logic
   - **Reason**: Current implementation has a paradox - Q2/Q3 marked required but should be conditional

### Medium Priority

2. **QIDS-SR16** - Document mutually exclusive scoring
   - Add metadata to questions indicating mutual exclusivity
   - Clarify in scoring documentation
   - **Reason**: Scoring logic is implicit, could confuse frontend developers

### Low Priority

3. **PSQI** - Document complex inputs
   - Clarify time input formats
   - Document calculation dependencies
   - **Reason**: More about documentation than logic

## Implementation Checklist for Conditional Logic

When a questionnaire has conditional questions, implement:

- [ ] `display_if` field with JSONLogic condition
- [ ] `required_if` field with JSONLogic condition
- [ ] Set base `required` to `False` for conditional questions
- [ ] `get_branching_logic()` method returning structured rules
- [ ] `get_respondent_schema()` if depends on external data (like gender)
- [ ] Fallback behavior documentation for edge cases
- [ ] Conditional scoring logic explicit in metadata
- [ ] Tests covering all branching scenarios
- [ ] Frontend-friendly documentation with examples

## MDQ Specific Implementation Plan

### Current State
```python
Question(
    id="q2",
    section_id="sec2",
    text="2. Si ≥2 réponses 'oui' à la Q1, ces réponses sont-elles apparues durant la même période ?",
    type="single_choice",
    required=True,  # ❌ PROBLEM: Hard-required but should be conditional
    options=[...],
    constraints={...}
)
```

### Required State
```python
Question(
    id="q2",
    section_id="sec2",
    text="2. Si ≥2 réponses 'oui' à la Q1, ces réponses sont-elles apparues durant la même période ?",
    type="single_choice",
    required=False,  # ✅ Not hard-required
    display_if={  # ✅ Show only if Q1 sum >= 2
        ">=": [
            {"+": [
                {"var": "answers.q1_1"}, {"var": "answers.q1_2"},
                # ... all 13 q1 items ...
            ]},
            2
        ]
    },
    required_if={  # ✅ Required when visible
        ">=": [
            {"+": [
                {"var": "answers.q1_1"}, {"var": "answers.q1_2"},
                # ... all 13 q1 items ...
            ]},
            2
        ]
    },
    options=[...],
    constraints={...}
)
```

### Additional Methods Needed
```python
def get_branching_logic(self) -> Dict[str, Any]:
    """Get explicit branching logic rules"""
    return {
        "schema_version": "1.0",
        "type": "answer_dependent",
        "rules": [
            {
                "rule_id": "q2_visibility",
                "question_id": "q2",
                "rule_type": "display",
                "condition": {">=": [{"sum_of": "q1_items"}, 2]},
                "description": "Show Q2 only if at least 2 'yes' answers in Q1",
                "action_if_true": "show",
                "action_if_false": "hide"
            },
            # Similar for Q3
        ],
        "context_variables": {
            "q1_sum": {
                "source": "calculated",
                "formula": {"sum": ["q1_1", "q1_2", ..., "q1_13"]},
                "type": "integer",
                "range": [0, 13]
            }
        }
    }
```

## Testing Strategy

For questionnaires with branching:

1. **Test visibility logic**
   - Questions hidden when condition not met
   - Questions shown when condition met
   
2. **Test requirement logic**
   - Hidden questions not required
   - Visible questions become required
   
3. **Test validation**
   - Form accepts submission when hidden questions unanswered
   - Form rejects submission when visible questions unanswered
   
4. **Test edge cases**
   - All possible condition states
   - Fallback behaviors

## Next Steps

1. **Update Cursor Rules** - Add explicit requirements for branching logic
2. **Implement MDQ branching** - High priority due to required-but-conditional paradox
3. **Document QIDS-SR16 mutual exclusivity** - Medium priority
4. **Review other questionnaires** - Check hetero-administered questionnaires

## References

- PRISE-M implementation: `questionnaires/auto/prise_m/prise_m.py`
- PRISE-M branching example: `questionnaires/auto/prise_m/EXAMPLE_USAGE_BRANCHING.md`
- Current cursor rules: `.cursor/rules/questionnaires.mdc`
