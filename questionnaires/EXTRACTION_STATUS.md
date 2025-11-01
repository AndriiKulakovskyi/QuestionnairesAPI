# Questionnaire Extraction Status Report

## Summary

**Total Questionnaires Identified**: 146
- Asperger (easperger): 56 questionnaires
- CEDR (ecedr): 29 questionnaires  
- eBipolar: 32 questionnaires
- eSchizo: 29 questionnaires

**Extraction Progress**: 11/146 completed (7.5%)

## Completed Questionnaires

### 1. ✅ Systematisation Quotient (SQ) - Baron-Cohen
- **File**: `systematisation_quotient_sq.py`
- **Source**: Asperger app (form/209.php)
- **Type**: Auto-questionnaire
- **Items**: 60 questions
- **Scoring**: Complex reverse scoring with two different scoring functions
- **Applications**: asperger
- **Complexity**: Medium - reverse scoring on 40 items

### 2. ✅ MADRS (Montgomery-Åsberg Depression Rating Scale)
- **File**: `madrs.py`
- **Source**: CEDR app (form/100.php), eBipolar SQL, eSchizo SQL
- **Type**: Hétéro-évaluation
- **Items**: 10 items
- **Scoring**: Simple sum (0-60 range)
- **Applications**: cedr, ebipolar, eschizo
- **Complexity**: Low - straightforward summation
- **Status**: Shared across 3 applications (deduplicated)

### 3. ✅ QIDS-SR16 (Quick Inventory of Depressive Symptomatology)
- **File**: `qids_sr16.py`
- **Source**: CEDR app (form/121.php)
- **Type**: Auto-questionnaire  
- **Items**: 16 items with conditional logic
- **Scoring**: Complex with maximum selection from item groups
- **Applications**: cedr
- **Complexity**: High - conditional items, grouped maximums

### 4. ✅ YMRS (Young Mania Rating Scale)
- **File**: `ymrs.py`
- **Source**: eBipolar SQL, eSchizo SQL  
- **Type**: Hétéro-évaluation
- **Items**: 11 items
- **Scoring**: Simple sum (0-44 range)
- **Applications**: ebipolar, eschizo
- **Complexity**: Low - straightforward summation
- **Status**: Shared across 2 applications (deduplicated)

### 5. ✅ CTQ (Childhood Trauma Questionnaire)
- **File**: `ctq.py`
- **Source**: eBipolar SQL, eSchizo SQL
- **Type**: Auto-questionnaire
- **Items**: 28 items with 5 subscales
- **Scoring**: Complex with reverse-scored items and subscale calculations
- **Applications**: ebipolar, eschizo
- **Complexity**: Medium-High - subscales (Physical Abuse, Emotional Neglect, Physical Neglect, Sexual Abuse, Emotional Abuse), reverse scoring, denial scale
- **Status**: Shared across 2 applications (deduplicated)

### 6. ✅ PSQI (Pittsburgh Sleep Quality Index)
- **File**: `psqi.py`
- **Source**: eBipolar SQL, eSchizo SQL
- **Type**: Auto-questionnaire
- **Items**: 10 primary questions with 7 component scores
- **Scoring**: Very complex - time calculations, sleep efficiency, 7 components
- **Applications**: ebipolar, eschizo
- **Complexity**: High - time parsing (HH:MM), sleep efficiency calculation, 7 component scores (Duration, Disturbance, Latency, Efficiency, Quality, Medication, Dysfunction)
- **Status**: Shared across 2 applications (deduplicated)

### 7. ✅ MARS (Medication Adherence Rating Scale)
- **File**: `mars.py`
- **Source**: eBipolar SQL, eSchizo SQL
- **Type**: Auto-questionnaire
- **Items**: 10 yes/no items
- **Scoring**: Simple with reverse scoring on 2 items
- **Applications**: ebipolar, eschizo
- **Complexity**: Low-Medium - binary responses with selective reverse scoring (items 7-8)
- **Status**: Shared across 2 applications (deduplicated)

### 8. ✅ WURS-25 (Wender Utah Rating Scale)
- **File**: `wurs.py`
- **Source**: eBipolar SQL, eSchizo SQL
- **Type**: Auto-questionnaire rétrospectif
- **Items**: 25 items (subset of 61-item full scale)
- **Scoring**: Simple summation, range 0-100
- **Applications**: ebipolar, eschizo
- **Complexity**: Low - 5-point Likert scale, retrospective ADHD symptoms
- **Cutoff**: ≥ 46 indicates probable childhood ADHD
- **Status**: Shared across 2 applications (deduplicated)

### 9. ✅ CGI-EGF (Clinical Global Impression + Global Functioning)
- **File**: `cgi_egf.py`
- **Source**: eBipolar SQL, eSchizo SQL
- **Type**: Hétéro-évaluation clinique
- **Components**: 4 separate ratings (CGI-S, EGF, CGI-I, Therapeutic Index)
- **Scoring**: CGI-S (0-7), EGF (1-100), CGI-I (0-7), Index composite
- **Applications**: ebipolar, eschizo
- **Complexity**: Medium - multiple independent clinical ratings
- **Status**: Shared across 2 applications (deduplicated)

### 10. ✅ EQ-5D (EuroQol-5 Dimensions)
- **File**: `eq5d.py`
- **Source**: eBipolar SQL, eSchizo SQL, Asperger PHP
- **Type**: Auto-questionnaire de qualité de vie
- **Items**: 5 dimensions + EQ-VAS (0-100)
- **Scoring**: Complex - health state code + utility index lookup table
- **Applications**: ebipolar, eschizo, asperger
- **Complexity**: High - French value set with 3,125 possible states
- **Status**: Shared across 3 applications (deduplicated)

### 11. ✅ YMRS N+1 (Young Mania Rating Scale - Follow-up)
- **File**: `ymrs_n1.py`
- **Source**: eBipolar SQL, eSchizo SQL
- **Type**: Hétéro-évaluation clinique (follow-up)
- **Items**: 11 items (identical to baseline YMRS)
- **Scoring**: Same as YMRS (0-44)
- **Applications**: ebipolar, eschizo
- **Complexity**: Low - same as YMRS, just for follow-up visits
- **Status**: Shared across 2 applications (deduplicated)

## Questionnaires by Application

### Asperger/TSA (easperger) - 56 total

#### Completed (1/56)
1. ✅ 209 - Systematisation Quotient (SQ)

#### Identified but Not Yet Extracted (55)
- 119 - QI/EVIP/PEP/VINELAND
- 120, 121, 122 - (To be analyzed)
- 158, 191-203 - (To be analyzed)
- 209-234 - (To be analyzed)
- 240-280 - (To be analyzed)
- 331-345 - (To be analyzed)

**Key Questionnaires to Prioritize**:
- AQ (Autism Quotient)
- ADOS items
- ADI-R items
- SPQ (Schizotypal Personality Questionnaire)
- Empathy Quotient
- Theory of Mind assessments

### CEDR (ecedr) - 29 total

#### Completed (2/29)
1. ✅ 100 - MADRS
2. ✅ 121 - QIDS-SR16

#### Identified but Not Yet Extracted (27)
- 112 - (To be analyzed)
- 124-126 - (To be analyzed)
- 130-144 - (To be analyzed)
- 153-228 - (To be analyzed)

**Key Questionnaires to Prioritize**:
- MDQ (Mood Disorder Questionnaire)
- PHQ-9
- GAD-7
- PSQI (Pittsburgh Sleep Quality Index)
- Other depression/anxiety scales

### eBipolar - 32 total

#### Self-Questionnaires (autoq_*) - 23 tables
- autoq_aim - Acceptance of Illness Medication
- autoq_als - Affective Lability Scale
- autoq_als18 - ALS 18-item version
- autoq_altman - Altman Self-Rating Mania Scale
- autoq_aq12 - Autism Quotient 12
- autoq_asrs - Adult ADHD Self-Report Scale
- autoq_bdhi - Buss-Durkee Hostility Inventory
- autoq_bis - Barratt Impulsiveness Scale
- autoq_csm - Compliance Self-Management
- autoq_ctq - Childhood Trauma Questionnaire
- autoq_date - Date questionnaire
- autoq_epworth - Epworth Sleepiness Scale
- autoq_ids - Inventory of Depressive Symptomatology
- autoq_mars - Medication Adherence Rating Scale
- autoq_mathys - Mathys scale
- autoq_mathys_slide - Mathys sliding scale
- autoq_mdq - Mood Disorder Questionnaire
- autoq_prisem - PRISEM
- autoq_psqi - Pittsburgh Sleep Quality Index
- autoq_stay_a - STAI-A (State-Trait Anxiety Inventory)
- autoq_type_circadien - Circadian Type
- autoq_wurs - Wender Utah Rating Scale
- autoq_wurs25 - WURS 25-item version

#### Clinician-Administered (hetero_*) - 9 tables
- hetero_alda - Alda Scale
- hetero_cgi_egf - CGI-EGF
- hetero_eq5d - EQ-5D Quality of Life
- hetero_etat_patient - Patient State
- hetero_fast - FAST (Functioning Assessment Short Test)
- hetero_madrs - MADRS (✅ already extracted)
- hetero_madrs_n1 - MADRS N+1
- hetero_ymrs - Young Mania Rating Scale
- hetero_ymrs_n1 - YMRS N+1

### eSchizo - 29 total

#### Self-Questionnaires (autoq_*) - 16 tables
- autoq_actphys - Physical Activity
- autoq_alimentaire - Dietary/Eating
- autoq_birchwood - Birchwood Insight Scale
- autoq_buss_perry - Buss-Perry Aggression
- autoq_ctq - Childhood Trauma Questionnaire (shared with eBipolar)
- autoq_fagerstrom - Fagerström Test
- autoq_mars - Medication Adherence (shared with eBipolar)
- autoq_piuq - Problematic Internet Use
- autoq_presenteism - Presenteeism
- autoq_psp - Personal and Social Performance
- autoq_psqi - Pittsburgh Sleep Quality Index (shared with eBipolar)
- autoq_qualite_vie - Quality of Life
- autoq_sogs - South Oaks Gambling Screen
- autoq_stori - STORI
- autoq_wurs - WURS (shared with eBipolar)
- autoq_yalebrown - Yale-Brown OCD Scale

#### Clinician-Administered (hetero_*) - 13 tables
- hetero_aims - AIMS (Abnormal Involuntary Movement Scale)
- hetero_barnes - Barnes Akathisia Rating Scale
- hetero_bars - BARS
- hetero_calgary - Calgary Depression Scale
- hetero_cgi_egf - CGI-EGF (shared with eBipolar)
- hetero_ephp - EPHP
- hetero_eq5d - EQ-5D (shared with eBipolar)
- hetero_extrapyramidaux - Extrapyramidal Symptoms
- hetero_niemanpick - Niemann-Pick
- hetero_panss - PANSS (Positive and Negative Syndrome Scale)
- hetero_sumd - SUMD (Scale to assess Unawareness of Mental Disorder)
- hetero_ymrs - YMRS (shared with eBipolar)
- hetero_ymrs_n1 - YMRS N+1 (shared with eBipolar)

## Shared Questionnaires Identified

These questionnaires appear in multiple applications and should be deduplicated:

1. **MADRS** - cedr, ebipolar, eschizo (✅ completed)
2. **YMRS** - ebipolar, eschizo (✅ completed)
3. **CTQ** - ebipolar, eschizo (✅ completed)
4. **MARS** - ebipolar, eschizo (✅ completed)
5. **PSQI** - ebipolar, eschizo (✅ completed)
6. **WURS** - ebipolar, eschizo (✅ completed)
7. **CGI-EGF** - ebipolar, eschizo (✅ completed)
8. **EQ-5D** - ebipolar, eschizo, asperger (✅ completed)
9. **YMRS N+1** - ebipolar, eschizo (✅ completed)

**🎉 ALL SHARED QUESTIONNAIRES COMPLETE (9/9 = 100%)**

## Extraction Tools Created

1. **extraction_utils.py** - Core parsing functions for PHP, JavaScript, and SQL
2. **batch_extractor.py** - Batch processing script for systematic extraction
3. **Example questionnaires** - Three complete implementations showing different patterns

## Next Steps

### Phase 1: High Priority Shared Questionnaires (8 remaining)
Extract and create Python classes for questionnaires used in multiple applications:
- YMRS (Young Mania Rating Scale)
- CTQ (Childhood Trauma Questionnaire)  
- PSQI (Pittsburgh Sleep Quality Index)
- MARS (Medication Adherence Rating Scale)
- WURS (Wender Utah Rating Scale)
- CGI-EGF
- EQ-5D
- YMRS N+1

### Phase 2: Asperger Application (55 remaining)
Process all Asperger-specific questionnaires, prioritizing:
- AQ (Autism Quotient)
- Empathy Quotient
- SPQ (Schizotypal Personality Questionnaire)
- ADOS/ADI-R related forms
- Theory of Mind assessments

### Phase 3: CEDR Application (27 remaining)
Process CEDR depression/anxiety questionnaires:
- MDQ (Mood Disorder Questionnaire)
- PHQ-9
- GAD-7
- Additional sleep/mood scales

### Phase 4: eBipolar Remaining (29 remaining)
Process eBipolar-specific questionnaires:
- ALS (Affective Lability Scale)
- ASRS (Adult ADHD)
- BIS (Barratt Impulsiveness)
- BDHI (Buss-Durkee Hostility)
- Altman Mania Scale
- And others

### Phase 5: eSchizo Remaining (28 remaining)
Process eSchizo-specific questionnaires:
- PANSS
- SUMD
- Calgary Depression Scale
- AIMS, Barnes scales
- And others

## Technical Considerations

### Complexity Levels

**Low Complexity** (Simple summation):
- MADRS, basic symptom scales
- Estimated: ~30 questionnaires

**Medium Complexity** (Reverse scoring, subscales):
- SQ, personality inventories
- Estimated: ~60 questionnaires  

**High Complexity** (Conditional logic, branching, multiple algorithms):
- QIDS-SR16, PANSS, complex diagnostic tools
- Estimated: ~40 questionnaires

**Very High Complexity** (Multiple forms, extensive branching):
- QI/VINELAND, ADOS, ADI-R
- Estimated: ~16 questionnaires

### Extraction Challenges

1. **SQL-based questionnaires**: Need to extract from multiple related tables (_nom_champ for metadata)
2. **Complex JavaScript scoring**: Some scoring functions have intricate logic requiring careful translation
3. **Branching logic**: Conditional questions based on previous responses
4. **Missing documentation**: Some questionnaires lack clear scoring documentation
5. **Language**: Ensuring all text is properly extracted in French

## Quality Assurance Strategy

For each extracted questionnaire:
1. ✅ Extract all questions with correct text
2. ✅ Extract all answer options  
3. ✅ Implement scoring logic accurately
4. ✅ Implement branching/conditional logic
5. ✅ Add validation
6. ✅ Test with sample data
7. ✅ Document in class docstring
8. ✅ List applications using it

## Estimated Time to Completion

Based on complexity distribution and current progress:
- **Low complexity**: ~10-15 minutes each x 30 = 5-7.5 hours
- **Medium complexity**: ~20-30 minutes each x 60 = 20-30 hours  
- **High complexity**: ~45-60 minutes each x 40 = 30-40 hours
- **Very high complexity**: ~90-120 minutes each x 16 = 24-32 hours

**Total estimated time**: 79-109.5 hours of focused extraction work

**Recommendation**: Continue systematic extraction in batches, prioritizing shared questionnaires first, then processing by application.

## Files Generated

```
Questionnaires/
├── __init__.py (✅ Complete - Module registry with 11 questionnaires)
├── systematisation_quotient_sq.py (✅ Complete)
├── madrs.py (✅ Complete)  
├── qids_sr16.py (✅ Complete)
├── ymrs.py (✅ Complete)
├── ymrs_n1.py (✅ Complete - Follow-up YMRS)
├── ctq.py (✅ Complete)
├── psqi.py (✅ Complete)
├── mars.py (✅ Complete)
├── wurs.py (✅ Complete - WURS-25)
├── cgi_egf.py (✅ Complete - CGI + EGF)
├── eq5d.py (✅ Complete - Quality of Life)
├── extraction_utils.py (✅ Tool)
├── batch_extractor.py (✅ Tool)
├── EXTRACTION_STATUS.md (This file)
├── SESSION_SUMMARY.md (✅ Documentation)
└── README.md (✅ Complete - Documentation)
```

## Notes

- All questionnaires are in French as requested
- Flat directory structure (no subdirectories by app)
- Each questionnaire includes `used_in_applications` metadata
- Deduplication performed for shared questionnaires
- Full scoring logic and validation included in each class

---

*Last updated: Current session*  
*Progress: 11/146 questionnaires (7.5%)*  
*Phase 1 (Shared questionnaires): ✅ **100% COMPLETE** - All 9 shared questionnaires extracted*  
*Completed: MADRS, YMRS, YMRS N+1, CTQ, PSQI, MARS, WURS, CGI-EGF, EQ-5D*  
*+ 2 reference questionnaires: SQ (Asperger), QIDS-SR16 (CEDR)*  
*Ready for Phase 2: High-priority clinical scales*

