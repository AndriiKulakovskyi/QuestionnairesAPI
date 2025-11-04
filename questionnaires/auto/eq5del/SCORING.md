# EQ-5D-EL Scoring Methodology

## Overview

The EQ-5D-EL produces **three types of outputs** from patient responses:

1. **Health State Profile** (5-digit code)
2. **VAS Score** (0-100)
3. **Index Value** (optional, requires external data)

---

## 1. Health State Profile

### What it is
A 5-digit code representing the patient's health status across 5 dimensions.

### How it's calculated
Simply concatenate the responses to Q1 through Q5 in order.

### Example
**Patient Responses:**
- Q1 (Mobility): 2 (slight problems)
- Q2 (Self-care): 1 (no problems)
- Q3 (Usual activities): 3 (moderate problems)
- Q4 (Pain/Discomfort): 4 (severe problems)
- Q5 (Anxiety/Depression): 1 (not anxious/depressed)

**Profile:** `"21341"`

### Interpretation
- **11111** = Perfect health (no problems in any dimension)
- **55555** = Worst possible health (extreme problems in all dimensions)
- Each digit position corresponds to a specific dimension
- Higher digits = more severe problems

### Total Possible States
- **3,125 unique profiles** (5^5 = 5 × 5 × 5 × 5 × 5)

---

## 2. VAS Score

### What it is
The patient's self-rated overall health on a visual analog scale.

### How it's calculated
**Direct value** from the VAS question (no calculation needed).

### Range
- **0** = Worst imaginable health state
- **100** = Best imaginable health state

### Interpretation
| Score | Interpretation |
|-------|---------------|
| 80-100 | Good perceived health |
| 50-79  | Moderate perceived health |
| 0-49   | Poor perceived health |

### Example
```python
answers = {
    "q1": 2, "q2": 1, "q3": 3, "q4": 4, "q5": 1,
    "vas": 75  # ← Direct VAS score
}
# VAS score = 75 (no calculation)
```

---

## 3. Index Value (Utility Score)

### What it is
A single summary number representing the **societal value** of a health state.
Used in health economics (QALYs for cost-effectiveness studies).

### Range
- **1.0** = Perfect health (profile 11111)
- **0.0** = Dead
- **Negative values** = States considered worse than death

### How it's calculated

**IMPORTANT:** Index calculation is **NOT performed automatically** by this implementation.

It requires an **external crosswalk table** specific to each country:

#### Process:
1. **Input:** Health state profile (e.g., "21341")
2. **Look up** in: `EQ-5D-EL_Crosswalk_Index_Value_Calculator.xls`
3. **Find** the row matching "21341"
4. **Extract** the value from the "France" column
5. **Output:** Index value (e.g., 0.474)

#### Example (from documentation):
| Profile | France Index |
|---------|--------------|
| 11111   | 1.000        |
| 21341   | 0.474        |
| 55555   | -0.590       |

### Why it's not automatic
- Requires large Excel file (value sets for multiple countries)
- Different value sets for different populations
- Licensing considerations for value set data
- Implementation choice: keep library lightweight

### How to add index calculation

If you need index values, you can extend the implementation:

```python
import pandas as pd

def calculate_index(profile: str, crosswalk_path: str) -> float:
    """Calculate EQ-5D-EL index value for France"""
    # Load crosswalk Excel file
    df = pd.read_excel(crosswalk_path, sheet_name="EQ-5D-EL Value Sets")
    
    # Find profile
    row = df[df['state'] == profile]
    
    if row.empty:
        raise ValueError(f"Profile {profile} not found")
    
    # Extract France column
    index = float(row['france_index'].iloc[0])
    
    return index

# Usage
profile = "21341"
index = calculate_index(profile, "EQ-5D-EL_Crosswalk_Index_Value_Calculator.xls")
print(f"Profile {profile} = Index {index}")  # 0.474
```

---

## Complete Scoring Example

### Input
```python
from questionnaires import EQ5DEL

eq5del = EQ5DEL()

answers = {
    "q1": 2,  # Mobility: slight problems
    "q2": 1,  # Self-care: no problems  
    "q3": 3,  # Usual activities: moderate problems
    "q4": 4,  # Pain/Discomfort: severe
    "q5": 1,  # Anxiety/Depression: not anxious/depressed
    "vas": 75 # Overall health perception
}
```

### Output
```python
result = eq5del.calculate_score(answers)

print(result.profile)       # "21341"
print(result.vas_score)     # 75
print(result.dimensions)    # {
                            #   "Mobilité": 2,
                            #   "Autonomie": 1,
                            #   "Activités courantes": 3,
                            #   "Douleurs/Gêne": 4,
                            #   "Anxiété/Dépression": 1
                            # }
print(result.index_value)   # None (not calculated)
print(result.interpretation) # "Profil de santé: 21341. Score VAS: 75/100. ..."
```

### Clinical Interpretation
```
Profile: 21341
- Slight mobility problems (level 2)
- No self-care problems (level 1) 
- Moderate problems with usual activities (level 3)
- Severe pain or discomfort (level 4)
- Not anxious or depressed (level 1)

VAS: 75/100 - Moderate to good perceived health

Dimensions with problems: 3 out of 5
Severe problems detected: 1 dimension (Pain/Discomfort)

Note: Severe pain (level 4) may require clinical attention.
```

---

## Validation and Warnings

### Input Validation
- Q1-Q5: Must be integers 1-5
- VAS: Must be integer 0-100
- All questions required

### Clinical Warnings

The implementation automatically flags:

1. **Worst health state (55555)**
   - Flags for clinical review
   - Suggests checking VAS consistency

2. **Profile-VAS inconsistency**
   - **Severe problems but high VAS** (e.g., 55555 with VAS=90)
   - **Few problems but very low VAS** (e.g., 11111 with VAS=20)
   - May indicate: misunderstanding, denial, cultural factors, or data error

### Example Warning
```python
answers = {"q1": 5, "q2": 5, "q3": 5, "q4": 5, "q5": 5, "vas": 90}

validation = eq5del.validate_answers(answers)
# validation.warnings:
# ["Profil 55555 - état de santé le plus défavorable. Vérifier la cohérence avec le score VAS.",
#  "Incohérence possible: profil indique des problèmes sévères mais VAS élevé."]
```

---

## Clinical Use

### When to use each score

| Score Type | Use For |
|------------|---------|
| **Profile** | Identifying specific problem areas; tracking changes over time in specific dimensions |
| **VAS** | Quick overall assessment; patient's subjective view; monitoring treatment satisfaction |
| **Index** | Economic evaluations (QALYs); comparing across different conditions; population health studies |

### Interpreting discrepancies

**Profile says "bad" but VAS says "good":**
- Patient may be adapting/coping well
- Psychological resilience
- Effective pain management despite disability

**Profile says "good" but VAS says "bad":**
- Psychological distress not captured by dimensions
- Recent acute problem
- Fear/worry about future
- Cultural factors in rating

---

## References

1. **EuroQol Group (2019)**
   - EQ-5D-EL User Guide
   - https://euroqol.org/

2. **Crosswalk Methodology**
   - van Hout B, et al. "Interim scoring for the EQ-5D-EL: mapping the EQ-5D-EL to EQ-5D-3L value sets." *Value Health.* 2012;15(5):708-15.

3. **French Value Set**
   - EQ-5D-EL Crosswalk Index Value Calculator
   - France-specific tariff values

