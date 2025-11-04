# CGI Quick Reference

## 📊 Scale Overview

**CGI (Clinical Global Impressions)** - Brief clinician-rated assessment in 3 parts

| Component | Items | Range | Visit Type |
|-----------|-------|-------|------------|
| **CGI-S** (Severity) | 1 | 0-7 | ✅ Baseline + Follow-up |
| **CGI-I** (Improvement) | 1 | 0-7 | ❌ Follow-up ONLY |
| **Therapeutic Index** | 2 | 0-16 | ❌ Follow-up ONLY |

## 🎯 Quick Usage

```python
from questionnaires.hetero import CGI

cgi = CGI()

# Baseline
answers = {'cgi01': 5, 'cgi02': 0, 'cgi03a': 0, 'cgi03b': 0}
result = cgi.calculate_score(answers, visit_type='baseline')

# Follow-up
answers = {'cgi01': 3, 'cgi02': 2, 'cgi03a': 1, 'cgi03b': 2}
result = cgi.calculate_score(answers, visit_type='followup')
```

## 📝 Items

### cgi01: CGI-S (Severity)
```
0 = Not assessed
1 = Normal, not ill
2 = Borderline
3 = Mildly ill
4 = Moderately ill
5 = Markedly ill
6 = Severely ill
7 = Extremely ill
```

### cgi02: CGI-I (Improvement) - Follow-up only
```
0 = Not assessed
1 = Very much improved
2 = Much improved
3 = Minimally improved
4 = No change
5 = Minimally worse
6 = Much worse
7 = Very much worse
```

### cgi03a: Therapeutic Effect - Follow-up only
```
0 = Not assessed
1 = Major
2 = Moderate
3 = Minimal
4 = None/worse
```

### cgi03b: Side Effects - Follow-up only
```
0 = Not assessed
1 = None
2 = Don't interfere
3 = Interfere significantly
4 = Outweigh benefit
```

## 🧮 Therapeutic Index Formula

```
if effect == 0: TI = 0
if effect == 1: TI = side_effects
if effect == 2: TI = side_effects + 4
if effect == 3: TI = side_effects + 8
if effect == 4: TI = side_effects + 12
```

**Range:** 0-16 (lower is better)

## 🚦 Interpretation

### CGI-S
- **1-2**: Minimal ✅
- **3**: Mild 🟡
- **4**: Moderate 🟠
- **5**: Marked 🔴
- **6-7**: Severe 🆘

### CGI-I
- **1-2**: Significant improvement ✅
- **3**: Minimal improvement ⚠️
- **4**: No change ❌
- **5-7**: Worsening 🚨

### Therapeutic Index
- **0-4**: Excellent/Good ✅
- **5-8**: Acceptable/Problematic 🟡
- **9-11**: Unfavorable 🔴
- **12-16**: Very poor 🆘

## 🎨 Frontend Integration

### Visibility Rules
```javascript
// Baseline visit
show: ['cgi01']
hide: ['cgi02', 'cgi03a', 'cgi03b']

// Follow-up visit
show: ['cgi01', 'cgi02', 'cgi03a', 'cgi03b']
```

### Get Schema
```python
schema = cgi.get_schema()
# Returns complete JSON with:
# - questions (with visibility rules)
# - validation rules
# - scoring formulas
```

### Validation
```python
validation = cgi.validate_answers(answers, visit_type='followup')
if validation['valid']:
    result = cgi.calculate_score(answers, visit_type='followup')
else:
    # Handle errors
    errors = validation['errors']
    warnings = validation['warnings']
```

## ⚠️ Common Warnings

- CGI-S ≥ 6 → Severe illness
- CGI-I ≥ 5 → Clinical worsening
- CGI-I = 4 with high CGI-S → No improvement, adjust treatment
- Effect ≥ 3 → Minimal/no therapeutic effect
- Side effects ≥ 3 → Significant interference
- Side effects = 4 → Outweigh benefits (URGENT)

## 📤 Output Structure

```python
{
    'cgi_s': int,              # 0-7
    'cgi_i': int or None,      # 0-7 (None at baseline)
    'therapeutic_effect': int or None,  # 0-4 (None at baseline)
    'side_effects': int or None,        # 0-4 (None at baseline)
    'therapeutic_index': int or None,   # 0-16 (None at baseline)
    'visit_type': str,         # 'baseline' or 'followup'
    'interpretation': str,     # Detailed French interpretation
    'warnings': list,          # Clinical warnings
    'calculation_date': str    # ISO timestamp
}
```

## 📚 Example Scenarios

### Scenario 1: Good Response
```python
answers = {
    'cgi01': 2,  # Borderline
    'cgi02': 2,  # Much improved
    'cgi03a': 1, # Major effect
    'cgi03b': 1  # No side effects
}
# TI = 1 → Excellent!
```

### Scenario 2: No Response
```python
answers = {
    'cgi01': 6,  # Severely ill
    'cgi02': 4,  # No change
    'cgi03a': 3, # Minimal effect
    'cgi03b': 3  # Significant side effects
}
# TI = 11 → Unfavorable, change treatment
```

### Scenario 3: Worsening
```python
answers = {
    'cgi01': 7,  # Extremely ill
    'cgi02': 6,  # Much worse
    'cgi03a': 4, # No effect/worse
    'cgi03b': 4  # Side effects outweigh benefit
}
# TI = 16 → URGENT: Stop treatment
```

## 🔑 Key Points

1. **CGI-I and Therapeutic Index** → Follow-up ONLY
2. **Therapeutic Index** = Complex formula (not simple sum)
3. **Lower TI** = Better benefit/risk ratio
4. **CGI-I ≥ 5** = Clinical emergency (worsening)
5. **Side effects = 4** = Immediate action required
6. **Context matters** = Visit type affects validation

## 📞 API Methods

```python
cgi.get_metadata()          # Scale info
cgi.get_questions()         # Items with options
cgi.get_sections()          # Section structure
cgi.validate_answers(...)   # Validate responses
cgi.calculate_score(...)    # Compute scores
cgi.get_schema()            # Complete JSON schema
cgi.calculate_therapeutic_index(effect, se)  # Direct TI calc
```

## 🎯 Clinical Decision Support

| CGI-S | CGI-I | TI | Action |
|-------|-------|-----|--------|
| ≤3 | ≤2 | ≤4 | ✅ Continue |
| ≤4 | 3-4 | ≤8 | ⚠️ Consider adjust |
| ≥5 | 4 | >8 | 🔴 Modify treatment |
| ≥5 | ≥5 | any | 🚨 Urgent action |
| any | any | ≥12 | 🆘 Change treatment |

---

**Most Common Error:** Trying to assess CGI-I at baseline → Should be 0 (not assessed)

**Most Important Feature:** Visit type awareness for proper validation

