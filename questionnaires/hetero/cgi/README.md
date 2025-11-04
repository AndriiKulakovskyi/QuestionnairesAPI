# CGI (Clinical Global Impressions)

## Overview

The **Clinical Global Impressions (CGI)** scale is one of the most widely used brief assessment tools in psychiatry. It provides a quick, clinician-rated evaluation of:

1. **Severity of illness** (CGI-S)
2. **Global improvement/change** (CGI-I)  
3. **Therapeutic efficacy** vs. side effects (Therapeutic Index)

The CGI is used across virtually all psychiatric disorders and is a standard outcome measure in clinical trials and routine clinical practice.

## Scale Structure

### Three Main Components

#### 1. CGI-S: Severity of Illness (Item cgi01)
**Scale:** 0-7
- **0** = Not assessed
- **1** = Normal, not at all ill
- **2** = Borderline mentally ill
- **3** = Mildly ill
- **4** = Moderately ill
- **5** = Markedly ill
- **6** = Severely ill
- **7** = Among the most extremely ill patients

**Assessment:** Current state at time of rating

#### 2. CGI-I: Global Improvement (Item cgi02)
**Scale:** 0-7
- **0** = Not assessed
- **1** = Very much improved
- **2** = Much improved
- **3** = Minimally improved
- **4** = No change
- **5** = Minimally worse
- **6** = Much worse
- **7** = Very much worse

**Assessment:** Change compared to baseline
**Important:** NOT assessed at baseline visit!

#### 3. Therapeutic Index (Items cgi03a + cgi03b)

**Therapeutic Effect (cgi03a):** 0-4
- **0** = Not assessed
- **1** = Major (improvement marked)
- **2** = Moderate
- **3** = Minimal
- **4** = None or makes patient worse

**Side Effects (cgi03b):** 0-4
- **0** = Not assessed
- **1** = None
- **2** = Do not significantly interfere with functioning
- **3** = Significantly interfere with functioning
- **4** = Outweigh therapeutic effect

**Calculation Formula:**
```
If Effect = 0 → Therapeutic Index = 0
If Effect = 1 → Therapeutic Index = Side Effects
If Effect = 2 → Therapeutic Index = Side Effects + 4
If Effect = 3 → Therapeutic Index = Side Effects + 8
If Effect = 4 → Therapeutic Index = Side Effects + 12
```

**Range:** 0-16 (lower = better benefit/risk ratio)

## Visit Type Protocol

### Baseline Visit
✅ **Assess:**
- CGI-S (Severity)

❌ **Do NOT assess:**
- CGI-I (no baseline for comparison)
- Therapeutic Index (no treatment effect yet)

### Follow-up Visits
✅ **Assess all three:**
- CGI-S (current severity)
- CGI-I (change from baseline)
- Therapeutic Index (treatment effect vs. side effects)

## Usage Examples

### Example 1: Baseline Assessment

```python
from questionnaires.hetero import CGI

cgi = CGI()

# Baseline: Only assess severity
answers_baseline = {
    'cgi01': 5,  # Markedly ill
    'cgi02': 0,  # Not assessed
    'cgi03a': 0,  # Not assessed
    'cgi03b': 0   # Not assessed
}

result = cgi.calculate_score(answers_baseline, visit_type='baseline')

print(f"CGI-S: {result['cgi_s']}/7")
# Output: CGI-S: 5/7 (Markedly ill)
```

### Example 2: Follow-up - Good Response

```python
# Follow-up: Assess all three components
answers_followup = {
    'cgi01': 2,  # Borderline
    'cgi02': 2,  # Much improved
    'cgi03a': 1,  # Major therapeutic effect
    'cgi03b': 2   # Minor side effects
}

result = cgi.calculate_score(answers_followup, visit_type='followup')

print(f"CGI-S: {result['cgi_s']}/7")  # 2 (Borderline)
print(f"CGI-I: {result['cgi_i']}/7")  # 2 (Much improved)
print(f"Therapeutic Index: {result['therapeutic_index']}/16")  # 2 (Excellent)
```

### Example 3: Follow-up - Poor Response

```python
answers_poor = {
    'cgi01': 6,  # Severely ill
    'cgi02': 5,  # Minimally worse
    'cgi03a': 3,  # Minimal effect
    'cgi03b': 3   # Significant side effects
}

result = cgi.calculate_score(answers_poor, visit_type='followup')

# Will trigger multiple warnings:
# - High severity (CGI-S ≥ 6)
# - Clinical worsening (CGI-I ≥ 5)
# - Minimal therapeutic effect
# - Significant side effects
```

## Therapeutic Index Interpretation

| TI Score | Therapeutic Effect | Side Effects | Clinical Meaning |
|----------|-------------------|--------------|------------------|
| **0** | Not assessed | - | - |
| **1** | Major | None | ✅ Excellent |
| **2** | Major | Minor | ✅ Excellent |
| **3** | Major | Significant | ⚠️ Monitor |
| **4** | Major | Severe OR Moderate/None | ⚠️ Adjust |
| **5** | Moderate | None | ✅ Good |
| **6-7** | Moderate | Minor-Significant | 🟡 Acceptable |
| **8** | Moderate | Severe OR Minimal/None | ⚠️ Problematic |
| **9-11** | Minimal | Any | 🔴 Unfavorable |
| **12+** | None/Worse | Any | 🆘 Change treatment |

## Frontend Integration

### Get Schema for Frontend
```python
cgi = CGI()
schema = cgi.get_schema()

# Returns complete JSON schema with:
# - Question definitions with response options
# - Visibility rules (visit_type != 'baseline')
# - Validation rules
# - Scoring formulas
# - Metadata
```

### Visibility Rules for UI

The frontend should implement these visibility rules:

```javascript
// Items visible at baseline
if (visit_type === 'baseline') {
  show: ['cgi01']  // Only CGI-S
  hide: ['cgi02', 'cgi03a', 'cgi03b']
}

// Items visible at follow-up
if (visit_type === 'followup') {
  show: ['cgi01', 'cgi02', 'cgi03a', 'cgi03b']  // All items
}
```

### Validation

```python
# Validate before calculating score
validation = cgi.validate_answers(answers, visit_type='followup')

if not validation['valid']:
    for error in validation['errors']:
        print(f"Error: {error}")

for warning in validation['warnings']:
    print(f"Warning: {warning}")
```

## Clinical Warnings

The CGI implementation provides automatic clinical warnings for:

### Severity (CGI-S)
- ⚠️ CGI-S ≥ 6: Severe illness → Consider hospitalization

### Improvement (CGI-I)
- 🚨 CGI-I ≥ 5: Clinical worsening → Urgent treatment modification
- ⚠️ CGI-I = 4 with CGI-S ≥ 4: No improvement → Consider adjustment

### Therapeutic Effect
- ⚠️ Effect ≥ 3: Minimal/no effect → Reevaluate treatment

### Side Effects
- ⚠️ Side effects ≥ 3: Significant interference → Adjust treatment
- 🆘 Side effects = 4: Outweigh benefits → Change treatment

### Consistency Checks
- Discrepancy: Much improved but still severe
- Discrepancy: Much worse but low severity

## Score Interpretation

### CGI-S Categories
- **1-2**: Minimal/borderline illness
- **3**: Mild illness
- **4**: Moderate illness  
- **5**: Marked illness
- **6-7**: Severe to extreme illness

### CGI-I Treatment Response
- **1-2**: Clinically significant improvement
- **3**: Minimal improvement
- **4**: No change (treatment failure)
- **5-7**: Clinical worsening (urgent action needed)

### Therapeutic Index
- **0-4**: Excellent to good benefit/risk
- **5-8**: Acceptable to problematic
- **9+**: Unfavorable, change recommended

## Common Use Cases

### Clinical Trials
- **Primary endpoint**: CGI-I (proportion with score ≤ 2)
- **Secondary endpoint**: CGI-S (mean change from baseline)
- **Safety measure**: Therapeutic Index

### Clinical Practice
- **Treatment decisions**: CGI-I guides treatment changes
- **Severity tracking**: CGI-S tracks disease course
- **Tolerability**: Therapeutic Index guides dose adjustments

### Quality Measures
- **Outcome tracking**: CGI-I for treatment response rates
- **Benchmarking**: CGI-S for severity distribution

## Key Features

✅ **Visit-type aware:** Different items at baseline vs. follow-up  
✅ **Comprehensive validation:** Context-sensitive error checking  
✅ **Clinical warnings:** Automatic alerts for concerning patterns  
✅ **Therapeutic Index:** Complex formula correctly implemented  
✅ **Frontend ready:** Complete schema with visibility rules  
✅ **Interpretations:** Detailed clinical guidance in French  

## References

Guy W. ECDEU Assessment Manual for Psychopharmacology. Rockville, MD: US Department of Health, Education, and Welfare; 1976. NIH publication 76-338.

Busner J, Targum SD. The clinical global impressions scale: applying a research tool in clinical practice. Psychiatry (Edgmont). 2007;4(7):28-37.

## Notes

- The CGI is **not** diagnosis-specific; it's used across all psychiatric conditions
- The CGI is a **clinician-rated** scale, not self-report
- **Training** is recommended for consistent ratings across clinicians
- The Therapeutic Index is **less commonly used** than CGI-S and CGI-I in practice
- CGI-I requires a **defined baseline** for comparison

