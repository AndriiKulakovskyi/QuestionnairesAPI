# MARS - Quick Reference Card

## Basic Info

- **Name**: Medication Adherence Rating Scale (MARS)
- **Version**: French (MARS.fr)
- **Items**: 10 binary (OUI/NON)
- **Time**: 2-3 minutes
- **Score**: 0-10 (higher = better adherence)

## Scoring at a Glance

### Items & Reverse Coding

| Item | Content | Type | Scoring |
|------|---------|------|---------|
| Q1 | Oublier médicaments | ❌ Neg | NON=1, OUI=0 |
| Q2 | Négliger heure | ❌ Neg | NON=1, OUI=0 |
| Q3 | Arrêter si mieux | ❌ Neg | NON=1, OUI=0 |
| Q4 | Arrêter si pire | ❌ Neg | NON=1, OUI=0 |
| Q5 | Prendre si malade seulement | ❌ Neg | NON=1, OUI=0 |
| Q6 | Pas naturel | ❌ Neg | NON=1, OUI=0 |
| Q7 | Idées plus claires | ✅ Pos | OUI=1, NON=0 |
| Q8 | Éviter rechute | ✅ Pos | OUI=1, NON=0 |
| Q9 | Sensation zombie | ❌ Neg | NON=1, OUI=0 |
| Q10 | Lourd/fatigué | ❌ Neg | NON=1, OUI=0 |

**Remember**: 
- ❌ **Negative items (8)**: Good adherence = "NON" = 1 point
- ✅ **Positive items (2)**: Good adherence = "OUI" = 1 point

## Score Interpretation

| Score | Level | Action |
|-------|-------|--------|
| **8-10** | 🟢 Excellente | Reinforce, maintain |
| **6-7** | 🟡 Bonne | Monitor, encourage |
| **4-5** | 🟠 Modérée | Explore barriers |
| **0-3** | 🔴 Faible | **Urgent intervention** |

**Typical Distribution**: Median ≈6, IQR ≈4–8

## Quick Code

```python
from questionnaires import MARS

# Initialize
mars = MARS()

# Get questions
questions = mars.get_questions()

# Validate & score
answers = {f"q{i}": 0 for i in range(1, 11)}
validation = mars.validate_answers(answers)

if validation.valid:
    result = mars.calculate_score(answers)
    print(f"Score: {result.total_score}/10")
```

## Clinical Red Flags

⚠️ **Score ≤3**: Very poor adherence → Immediate intervention  
⚠️ **Q9 or Q10 = OUI**: Side effects → Consider medication review  
⚠️ **Q7 and Q8 = NON**: Doesn't see benefits → Psychoeducation  
⚠️ **Q3 or Q4 = OUI**: Intentional non-adherence → Motivational work  

## Intervention Guide

### Score 0-3 (Poor)
1. ⚡ **Urgent**: Explore all barriers
2. 💊 Medication review (side effects?)
3. 🧠 Psychoeducation (benefits, risks)
4. 📱 Adherence aids (reminders, pillboxes)

### Score 4-5 (Moderate)
1. 🔍 Identify specific barriers
2. 💬 Motivational interviewing
3. 📊 Regular monitoring
4. 🎯 Targeted support

### Score 6-7 (Good)
1. ✅ Positive reinforcement
2. 👁️ Maintain monitoring
3. 🛡️ Prevent relapse

### Score 8-10 (Excellent)
1. 🎉 Acknowledge success
2. 📈 Use as baseline
3. 🔄 Continue current approach

## Common Patterns

### Pattern A: Side Effects
- Q9=OUI (zombie), Q10=OUI (fatigue)
- Q4=OUI (stops when worse)
- → **Action**: Medication adjustment

### Pattern B: Lack of Insight
- Q7=NON (no clarity), Q8=NON (no prevention)
- Q5=OUI (only when sick)
- → **Action**: Psychoeducation

### Pattern C: Forgetfulness
- Q1=OUI (forgets), Q2=OUI (timing)
- But Q7=OUI, Q8=OUI (recognizes benefits)
- → **Action**: Reminder systems

### Pattern D: Intentional Non-Adherence
- Q3=OUI (stops when better)
- Q6=OUI (not natural)
- → **Action**: Cognitive work, beliefs

## API Endpoints

```python
GET  /mars/metadata     # Get questionnaire info
GET  /mars/questions    # Get all questions
POST /mars/calculate    # Calculate score
```

## Testing

```bash
# Run all tests
pytest tests/test_mars.py -v

# Run specific test class
pytest tests/test_mars.py::TestMARSScoring -v

# Run demo
cd questionnaires/mars && python3 demo.py
```

## Files

```
questionnaires/mars/
├── __init__.py              # Module exports
├── mars.py                  # Main implementation
├── README.md                # Full documentation
├── EXAMPLE_USAGE.md         # Usage examples
├── IMPLEMENTATION_SUMMARY.md # Technical details
├── QUICK_REFERENCE.md       # This file
└── demo.py                  # Demo script

tests/
└── test_mars.py             # Test suite
```

## Key Facts

- ✅ Self-report measure
- ✅ Validated in psychiatric populations
- ✅ Dimensional (not categorical)
- ✅ Covers behavioral + attitudinal adherence
- ✅ Quick administration
- ✅ Suitable for repeated measures
- ⚠️ Complement with objective measures

## Reference

**Thompson K, Kulkarni J, Sergejew AA.** (2000). Reliability and validity of a new Medication Adherence Rating Scale (MARS) for the psychoses. *Schizophrenia Research*, 42(3):241–247.

---

**For detailed information, see:**
- Clinical use → `README.md`
- Code examples → `EXAMPLE_USAGE.md`
- Implementation → `IMPLEMENTATION_SUMMARY.md`

