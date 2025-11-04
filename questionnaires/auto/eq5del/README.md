# EQ-5D-5L (EuroQol 5 Dimensions 5 Levels)

## Overview

The EQ-5D-5L is a standardized, generic measure of health-related quality of life developed by the EuroQol Group. It provides a simple, generic measure of health for clinical and economic appraisal.

## Structure

### Part 1: Descriptive System (5 Dimensions)

Each dimension is rated on a 5-level scale (1-5):

1. **Mobility** (Mobilité)
   - Walking about
   - Levels: No problems → Unable to walk

2. **Self-Care** (Autonomie de la personne)
   - Washing and dressing
   - Levels: No problems → Unable to wash/dress

3. **Usual Activities** (Activités courantes)
   - Work, study, housework, family or leisure activities
   - Levels: No problems → Unable to do usual activities

4. **Pain/Discomfort** (Douleurs / Gêne)
   - Levels: No pain/discomfort → Extreme pain/discomfort

5. **Anxiety/Depression** (Anxiété / Dépression)
   - Levels: Not anxious/depressed → Extremely anxious/depressed

### Part 2: Visual Analog Scale (VAS)

- Scale: 0-100
- 0 = Worst imaginable health
- 100 = Best imaginable health
- Patient rates their current health "TODAY"

## Health State Profile

The 5 dimensions create a 5-digit health state profile:
- Range: `11111` (perfect health) to `55555` (worst health)
- Example: `21341` means:
  - 2 = Slight mobility problems
  - 1 = No self-care problems
  - 3 = Moderate problems with usual activities
  - 4 = Severe pain/discomfort
  - 1 = Not anxious/depressed

## Index Values

Health state profiles can be converted to index values using country-specific value sets:
- **France**: Uses EQ-5D-5L Crosswalk methodology
- Index range: -0.59 to 1.0
  - 1.0 = Full health (11111)
  - 0 = Death
  - Negative values = States worse than death
- Requires: EQ-5D-5L Crosswalk Index Value Calculator (Excel file)

## Scoring

### Profile Generation
```python
from questionnaires import EQ5D5L

eq5d = EQ5D5L()

answers = {
    "q1": 2,  # Slight mobility problems
    "q2": 1,  # No self-care problems
    "q3": 3,  # Moderate usual activity problems
    "q4": 4,  # Severe pain
    "q5": 1,  # Not anxious/depressed
    "vas": 75
}

result = eq5d.calculate_score(answers)
print(result.profile)  # "21341"
print(result.vas_score)  # 75
print(result.dimensions)  # Dict with dimension names and values
```

### Validation Features

The implementation includes:
- **Missing data detection**: Ensures all 5 dimensions + VAS are provided
- **Range validation**: Dimensions must be 1-5, VAS must be 0-100
- **Consistency checks**: Warns if profile and VAS are highly inconsistent
  - Severe problems but high VAS
  - Few problems but very low VAS
- **Worst state warning**: Flags profile 55555 for review

## Clinical Interpretation

### Profile Analysis
- **11111**: Perfect health, no problems in any dimension
- **55555**: Worst possible health, extreme problems in all dimensions
- Count dimensions with problems (>1) for severity assessment
- Identify dimensions with severe/extreme problems (≥4)

### VAS Interpretation
- **80-100**: Good perceived health
- **50-79**: Moderate perceived health
- **0-49**: Poor perceived health

### Consistency
- Profile and VAS should generally correlate
- Inconsistencies may indicate:
  - Misunderstanding of questions
  - Psychological factors (denial, acceptance)
  - Cultural differences in health perception
  - Need for clinical review

## API Methods

### `get_metadata()`
Returns instrument information, dimensions, ranges.

### `get_sections()`
Returns the 2 sections (Dimensions + VAS).

### `get_questions()`
Returns all 6 questions (Q1-Q5 + VAS) with options and constraints.

### `validate_answers(answers)`
Validates answer dictionary, returns validation result with errors/warnings.

### `calculate_score(answers)`
Generates profile, VAS score, dimensions dict, and interpretation.

### `get_profile_description(profile)`
Converts 5-digit profile to human-readable descriptions for each dimension.

## Example Usage

```python
from questionnaires import EQ5D5L

# Initialize
eq5d = EQ5D5L()

# Get questionnaire for frontend
questionnaire = eq5d.get_full_questionnaire()

# Patient completes questionnaire
answers = {
    "q1": 1,  # Mobility
    "q2": 1,  # Self-care
    "q3": 2,  # Usual activities
    "q4": 2,  # Pain/Discomfort
    "q5": 1,  # Anxiety/Depression
    "vas": 80
}

# Validate
validation = eq5d.validate_answers(answers)
if not validation.valid:
    print("Errors:", validation.errors)
if validation.warnings:
    print("Warnings:", validation.warnings)

# Calculate profile
result = eq5d.calculate_score(answers)
print(f"Profile: {result.profile}")  # "11221"
print(f"VAS: {result.vas_score}")  # 80
print(f"Interpretation: {result.interpretation}")

# Get profile description
description = eq5d.get_profile_description(result.profile)
for dimension, text in description.items():
    print(f"{dimension}: {text}")
```

## Clinical Notes

### Reference Period
- **TODAY** (AUJOURD'HUI) - current health state only
- Not retrospective or future-oriented

### Important Considerations
1. **Simple and quick**: Takes 1-2 minutes to complete
2. **Generic instrument**: Applies across conditions and treatments
3. **Cultural adaptation**: French version is culturally validated
4. **Value sets**: Index calculation requires appropriate national value set
5. **Not diagnostic**: Measures health status, not specific conditions

### Limitations
- Generic (may miss condition-specific issues)
- Self-reported (subject to bias)
- May have ceiling effects in healthy populations
- Index values require additional data (crosswalk table)

## References

1. **EuroQol Group**
   - EQ-5D-5L User Guide (2019)
   - Website: https://euroqol.org/

2. **French Value Set**
   - Crosswalk Index Value Calculator
   - French tariff for health state valuation

3. **Methodology**
   - Herdman M, et al. Development and preliminary testing of the new five-level version of EQ-5D (EQ-5D-5L). Qual Life Res. 2011;20(10):1727-36.
   - van Hout B, et al. Interim scoring for the EQ-5D-5L: mapping the EQ-5D-5L to EQ-5D-3L value sets. Value Health. 2012;15(5):708-15.

## License

This implementation follows the EuroQol Group guidelines. For commercial use, please review EuroQol's terms at https://euroqol.org/

