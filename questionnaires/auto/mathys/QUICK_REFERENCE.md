# MAThyS - Quick Reference Card

## Basic Info

- **Name**: Évaluation Multidimensionnelle des états thymiques (MAThyS)
- **Version**: French (MAThyS.fr)
- **Items**: 20 with 0-10 bipolar scales
- **Time**: 5-7 minutes
- **Score**: 0-200 (sum of 5 subscales)

## Scoring at a Glance

### Reverse-Coded Items (8 items)

Items that require **recoding** (score = 10 - raw value):

**5, 6, 7, 8, 9, 10, 17, 18**

### Subscales

| Subscale | Items | Range | Description |
|----------|-------|-------|-------------|
| **Émotion** | 3, 7, 10, 18 | 0-40 | Intensity & variability of emotions |
| **Motivation** | 2, 11, 12, 15, 16, 17, 19 | 0-70 | Energy, drive, psychomotor activity |
| **Perception** | 1, 6, 8, 13, 20 | 0-50 | Sensory sensitivity (5 senses) |
| **Interaction** | 4, 14 | 0-20 | Social withdrawal vs. disinhibition |
| **Cognition** | 5, 9 | 0-20 | Distractibility, thought pace |

**Total Score** = Sum of all 5 subscales (0-200)

## Item Anchors Summary

### Sensory Items (Perception)
- **Q1**: Less sensitive to colors ↔ More sensitive to colors
- **Q6**: More sensitive to touch ↔ Less sensitive to touch (R)
- **Q8**: Sensitive to music ↔ Indifferent to music (R)
- **Q13**: Food tasteless ↔ Gastronomic pleasures
- **Q20**: Less sensitive to smells ↔ More sensitive to smells

### Energy/Motivation Items
- **Q2**: Lack of tone ↔ Internal tension
- **Q11**: No energy ↔ Great energy
- **Q12**: Thoughts slowed ↔ Thoughts racing
- **Q15**: Lack of motivation ↔ Multiple new projects
- **Q16**: Loss of interest ↔ Want to do more
- **Q17**: Decisions faster ↔ Difficulty deciding (R)
- **Q19**: Slowed movements ↔ Physically agitated

### Emotional Items
- **Q3**: Emotionally anesthetized ↔ Losing emotional control
- **Q7**: Mood variable with environment ↔ Monotonous mood (R)
- **Q10**: More reactive to environment ↔ Less reactive (R)
- **Q18**: Intense emotions ↔ Attenuated emotions (R)

### Cognitive Items
- **Q5**: Easily distracted ↔ Not attentive to environment (R)
- **Q9**: Brain never stops ↔ Brain slowed down (R)

### Social Items
- **Q4**: Withdrawn ↔ Disinhibited
- **Q14**: Less desire to communicate ↔ More desire to communicate

**(R) = Reverse-coded**

## Quick Code

```python
from questionnaires import MAThyS

# Initialize
mathys = MAThyS()

# Get questions
questions = mathys.get_questions()

# Score
answers = {f"q{i}": 5 for i in range(1, 21)}  # All centered
validation = mathys.validate_answers(answers)

if validation.valid:
    result = mathys.calculate_score(answers)
    print(f"Total: {result.total_score}/200")
    print(f"Émotion: {result.subscales['emotion'].score}/40")
    print(f"Motivation: {result.subscales['motivation'].score}/70")
```

## Interpretation Guide

### Score Positioning

| Position | Interpretation |
|----------|---------------|
| **100/200 (50%)** | Average/habitual state |
| **<50/200 (<25%)** | Very low intensity overall |
| **>150/200 (>75%)** | Very high intensity overall |

### Subscale Interpretation

**Low scores** on a dimension (< 20% of range):
- May indicate reduced intensity on that dimension
- Context-dependent interpretation

**High scores** on a dimension (> 80% of range):
- May indicate elevated intensity on that dimension
- Consider clinical context

### Clinical Profiles

**Depressive Profile:**
- Low Motivation (< 25/70)
- Low Émotion (< 15/40)
- Low Cognition (indicating slowing)
- Reduced Perception sensitivity

**Manic/Hypomanic Profile:**
- High Motivation (> 50/70)
- High Émotion (> 30/40)
- High Cognition (indicating acceleration)
- Heightened Perception

**Mixed Profile:**
- Variable scores across dimensions
- High scores on some, low on others
- Indicates complex thymic state

## Clinical Red Flags

⚠️ **All scores at extremes (0-1 or 9-10)**: Check response validity  
⚠️ **All scores centered (4-6)**: Possible non-engagement  
⚠️ **Very low total (<50)**: Severe dampening of thymic states  
⚠️ **Very high total (>150)**: Severe intensification  
⚠️ **Extreme discrepancy between subscales**: Consider mixed state

## Reverse Coding Reminder

**Why reverse coding?**

Some items are worded so that high scores indicate opposite poles:
- Q5: "Distracted" (high) vs "Not attentive" (high) - both extremes
- Q6: "More sensitive touch" (low value) vs "Less sensitive" (high value)
- Q7-10, Q17-18: Similar bipolar inversions

**Recoding formula**: `recoded_value = 10 - raw_value`

## Practical Usage

### Pre-Assessment
1. Explain bipolar scale concept
2. Emphasize center (~5) = habitual state
3. No right/wrong answers

### During Assessment
- Patient rates current state (last week)
- Can use slider or numeric entry
- Encourage honest self-assessment

### Post-Assessment
1. Calculate all 5 subscales
2. Review profile visually (radar chart)
3. Identify extreme dimensions
4. Discuss in clinical context
5. Use for treatment planning

## Reference

**Henry C, et al.** Construction and validation of a dimensional scale exploring mood disorders: MAThyS (Multidimensional Assessment of Thymic States). *BMC Psychiatry* 2008;8:82.

---

**For detailed information, see:**
- Clinical use → `README.md`
- Code examples → `EXAMPLE_USAGE.md`
- Implementation → Main code file

