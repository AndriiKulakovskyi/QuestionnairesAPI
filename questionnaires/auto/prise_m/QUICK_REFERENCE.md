# PRISE-M - Quick Reference Card

## Basic Info

- **Name**: Profil des effets indésirables médicamenteux (PRISE-M)
- **Version**: French (PRISE-M.fr)
- **Items**: 32 (score based on 31)
- **Time**: 5-10 minutes
- **Score**: 0-62 (31 items × 2)
- **Key Feature**: **Gender-specific items** with automatic exclusion

## ⭐ Gender-Specific Branching Logic

### The Special Items

| Item | Description | Gender | Question ID |
|------|-------------|--------|-------------|
| **Q20** | Règles irrégulières (Irregular periods) | ♀ FEMALE | Used for women |
| **Q25** | Troubles de l'érection (Erectile dysfunction) | ♂ MALE | Used for men |

### Scoring Rule

**Score = Sum of 31 items** (32 total minus 1 based on gender)

- **Female patients**: Exclude Q25, include Q20 → Range: 0-62
- **Male patients**: Exclude Q20, include Q25 → Range: 0-62

### Automatic Gender Detection

If gender is not explicitly provided, the system infers it:

```python
# Inference Logic:
if Q20 ≠ 0 and Q25 == 0:
    → Assume FEMALE, exclude Q25
    
elif Q25 ≠ 0 and Q20 == 0:
    → Assume MALE, exclude Q20
    
elif both == 0:
    → Default: exclude Q25 (with warning)
    
elif both ≠ 0:
    → Warning: both items endorsed (check consistency)
```

## Scoring at a Glance

### Response Scale (All 32 Items)

| Code | Label | Score | Description |
|------|-------|-------|-------------|
| **0** | Absent | 0 | Side effect not present |
| **1** | Tolérable | 1 | Present but bearable |
| **2** | Pénible | 2 | Present and burdensome |

### Score Interpretation

| Score | Level | Action |
|-------|-------|--------|
| **0-14** | 🟢 Low | Continue monitoring |
| **15-24** | 🟡 Moderate | Follow-up, symptom management |
| **25-39** | 🟠 High | **Review treatment required** |
| **≥40** | 🔴 Very High | **Urgent intervention** |

## Sections (9 Categories)

| # | Section | Items | Examples |
|---|---------|-------|----------|
| **1** | GI troubles | Q1-Q4 | Diarrhea, constipation, dry mouth, nausea |
| **2** | Cardiac | Q5-Q7 | Palpitations, dizziness, chest pain |
| **3** | Skin | Q8-Q10 | Sweating, itching, dry skin |
| **4** | Neurological | Q11-Q14 | Headache, tremors, motor control, lightheadedness |
| **5** | Vision/Hearing | Q15-Q16 | Blurred vision, tinnitus |
| **6** | Urogenital | Q17-Q20 | Urination issues, **irregular periods (F)** |
| **7** | Sleep | Q21-Q22 | Insomnia, hypersomnia |
| **8** | Sexual | Q23-Q25 | Loss of desire, orgasm issues, **erectile dysfunction (M)** |
| **9** | Other | Q26-Q32 | Anxiety, concentration, fatigue, weight gain |

## Quick Code

### Basic Usage

```python
from questionnaires import PRISEM

# Initialize
prisem = PRISEM()

# Get questions (filtered by gender)
questions_female = prisem.get_questions(gender="F")  # 31 items
questions_male = prisem.get_questions(gender="M")    # 31 items

# Score with explicit gender
answers = {f"q{i}": 0 for i in range(1, 33)}
validation = prisem.validate_answers(answers, gender="F")

if validation.valid:
    result = prisem.calculate_score(answers, gender="F")
    print(f"Total: {result.total_score}/62")
    print(f"Excluded: {result.excluded_item}")
```

### Gender Inference Example

```python
# No gender provided - system infers from responses
answers = {f"q{i}": 0 for i in range(1, 33)}
answers['q20'] = 2  # Irregular periods (pénible)
answers['q25'] = 0  # No erectile issues

result = prisem.calculate_score(answers)  # No gender arg
# → gender_used: "F" (inferred)
# → excluded_item: "q25"
# → warning: "Sexe non fourni: exclusion de q25..."
```

## Clinical Red Flags

⚠️ **Score ≥25**: Treatment review needed  
⚠️ **≥10 items at "2" (Pénible)**: High burden  
⚠️ **Both Q20 and Q25 endorsed**: Check gender/consistency  
⚠️ **Cardiac symptoms (Q5-Q7) severe**: Cardiology evaluation  
⚠️ **Sexual dysfunction severe**: Major adherence risk  
⚠️ **Weight gain severe (Q32)**: Metabolic monitoring  

## Gender-Specific Workflow

### For Female Patients

```python
# Option 1: Explicit gender
questions = prisem.get_questions(gender="F")
# → Returns 31 questions (Q1-Q24, Q26-Q32)
# → Excludes Q25 (erectile dysfunction)

result = prisem.calculate_score(answers, gender="F")
# → Sums Q1-Q24, Q26-Q32 (31 items)
```

### For Male Patients

```python
# Option 2: Explicit gender
questions = prisem.get_questions(gender="M")
# → Returns 31 questions (Q1-Q19, Q21-Q32)
# → Excludes Q20 (irregular periods)

result = prisem.calculate_score(answers, gender="M")
# → Sums Q1-Q19, Q21-Q32 (31 items)
```

### Without Gender (Auto-Inference)

```python
# Option 3: No gender, system infers
result = prisem.calculate_score(answers)
# → Examines Q20 and Q25 values
# → Infers gender and excludes appropriate item
# → Provides warning if ambiguous
```

## Section Scoring

```python
result = prisem.calculate_score(answers, gender="F")

# View section scores
for sec_id, score in result.section_scores.items():
    print(f"{sec_id}: {score}")

# Example output:
# sec1: 3  (GI: moderate issues)
# sec2: 0  (Cardiac: none)
# sec3: 1  (Skin: minimal)
# sec4: 2  (Neuro: mild)
# sec5: 0  (Vision/hearing: none)
# sec6: 4  (Urogenital: significant)
# sec7: 1  (Sleep: minimal)
# sec8: 3  (Sexual: moderate)
# sec9: 5  (Other: significant)
```

## Interpretation Examples

### Low Burden (Score = 8)

```
"Score total PRISE-M: 8/62 (sexe: FEMME). 
Score bas (<15) suggérant peu d'effets indésirables."
```

### Moderate Burden (Score = 18)

```
"Score total PRISE-M: 18/62 (sexe: HOMME). 
Score modéré (15-24) avec effets indésirables présents mais modérés. 
Suivi régulier recommandé pour surveiller l'évolution."
```

### High Burden (Score = 32)

```
"Score total PRISE-M: 32/62 (sexe: FEMME). 
Score élevé (25-39) suggérant des effets indésirables significatifs. 
Sections problématiques: Troubles uro-génital (5/8), Autres troubles (8/14). 
Révision du traitement médicamenteux recommandée."
```

## Common Patterns

### Pattern A: GI + Sedation
- Q1-Q4 elevated (GI)
- Q21-Q22 elevated (sleep)
- Q26, Q30-Q31 elevated (anxiety, fatigue)
- → Consider timing/formulation changes

### Pattern B: Sexual + Weight
- Q23-Q25 elevated (sexual)
- Q32 elevated (weight gain)
- → Major adherence risk, consider alternatives

### Pattern C: Neurological
- Q11-Q14 elevated (neuro)
- → Dose reduction or change indicated

## Best Practices

### Administration
1. ✅ Emphasize "due to current medication"
2. ✅ Last week reference period
3. ✅ Provide gender or let system infer
4. ✅ Review section scores, not just total

### Follow-up
- **Baseline**: Before starting treatment
- **Regular**: Monthly or after dose changes
- **Ad hoc**: When patient reports issues

### Intervention Priorities
1. 🔴 Items scored "2" (Pénible)
2. 🟠 Sections with high burden (>60% of max)
3. 🟡 Total score ≥25

## Reference

- **PRISE-M.pdf** - French questionnaire form
- **PRISE-M_CotationScore.docx** - Scoring instructions

---

**For detailed information, see:**
- Clinical use → `README.md`
- Implementation → Main code file
- Tests → `test_prise_m.py`

**Key Takeaway**: PRISE-M uses **conditional item exclusion based on gender** - a unique feature among these questionnaires that demonstrates **branching logic in scoring** rather than in question display.

