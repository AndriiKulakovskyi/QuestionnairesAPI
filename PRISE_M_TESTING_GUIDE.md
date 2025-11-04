# PRISE-M Branching Logic - Testing Guide

## Implementation Complete ✅

The PRISE-M questionnaire now has full support for gender-specific branching logic in both backend and frontend.

## What Was Implemented

### Backend (API)
1. **Updated API Schemas** (`api/schemas.py`)
   - Added `demographics` field to `AnswersRequest`
   - Allows passing gender information with answers

2. **Updated API Routes** (`api/routes/auto.py`)
   - `GET /api/auto/questionnaires/{id}` accepts optional `gender` parameter
   - `POST /api/auto/questionnaires/{id}/submit` accepts demographics in request body
   - Automatically detects and uses gender parameter for scoring

3. **PRISE-M Backend** (Already Complete)
   - `get_respondent_schema()` - Defines gender collection requirements
   - `get_branching_logic()` - Provides machine-readable rules
   - `get_questions(gender="F"|"M"|"X")` - Returns filtered questions
   - `calculate_score(answers, gender)` - Gender-aware scoring

### Frontend
1. **TypeScript Types** (`app/types/questionnaire.ts`)
   - Added `RespondentSchema`, `BranchingLogic` interfaces
   - Updated `Question` to include `display_if`, `required_if`, `gender_specific`
   - Updated `AnswersRequest` to include optional `demographics`

2. **Demographics Component** (`app/components/Demographics.tsx`)
   - Collects demographic information before questionnaire
   - Displays respondent schema fields dynamically
   - Shows helpful notes and field purposes
   - Validates required fields

3. **JSONLogic Utility** (`app/lib/jsonlogic.ts`)
   - Evaluates conditional display rules
   - Supports operators: `==`, `!=`, `var`, `and`, `or`, `not`, `in`, `>`, `<`, etc.
   - Helper functions: `shouldDisplayQuestion()`, `isQuestionRequired()`

4. **API Client** (`app/lib/api.ts`)
   - Updated `submitAnswers()` to accept optional demographics parameter

5. **Questionnaire Page** (`app/questionnaire/[category]/[id]/page.tsx`)
   - Two-phase flow: Demographics → Questionnaire
   - Filters questions based on demographics
   - Shows/hides questions dynamically
   - Validates only visible required questions
   - Displays demographics summary in questionnaire form

## Testing Results

### Backend Tests ✅
```
✓ Respondent schema correctly defines gender collection
✓ Questions filtered by gender (F=31, M=31, X=30)
✓ Branching logic rules defined and accessible
✓ Scoring excludes correct gender-specific items
  - Female (F): Scores 31 items, excludes q25, range 0-62
  - Male (M): Scores 31 items, excludes q20, range 0-62
  - Other (X): Scores 30 items, excludes q20 and q25, range 0-60
✓ API integration ready (get_full_questionnaire with gender)
```

### Frontend Tests ✅
```
✓ JSONLogic evaluates variable access correctly
✓ Equality comparisons work (==, !=)
✓ Q20 visibility correct: shown for Female, hidden for Male
✓ Q25 visibility correct: shown for Male, hidden for Female
✓ All conditional logic evaluates as expected
```

## How to Test Manually

### 1. Start the Backend
```bash
cd /Users/andriikulakovskyi/Documents/Code/QuestionnairesAPI
poetry run python run_api.py
```

Backend will run on: `http://localhost:8000`

### 2. Start the Frontend
```bash
cd /Users/andriikulakovskyi/Documents/Code/QuestionnairesAPI/app
npm run dev
```

Frontend will run on: `http://localhost:3000`

### 3. Test PRISE-M with Different Genders

#### Test Scenario 1: Female
1. Navigate to `http://localhost:3000`
2. Click "Auto Questionnaires"
3. Find and select "PRISE-M – Profil des effets indésirables médicamenteux"
4. **Demographics Screen** should appear
5. Select "Femme" (Female)
6. Click "Continue to Questionnaire"
7. **Verify**:
   - Demographics banner shows: `Demographics: gender=F`
   - Section 6 includes "Règles irrégulières (pour les femmes)" - Q20 ✅
   - Section 8 does NOT include "Troubles de l'érection (pour les hommes)" - Q25 ❌
   - Total: 31 questions visible
8. Answer all questions (can use value 0 or 1 for all)
9. Submit and verify results show:
   - Items scored: 31
   - Excluded items: ['q25']
   - Range: 0-62

#### Test Scenario 2: Male
1. Restart from PRISE-M selection
2. Select "Homme" (Male)
3. Click "Continue to Questionnaire"
4. **Verify**:
   - Demographics banner shows: `Demographics: gender=M`
   - Section 6 does NOT include "Règles irrégulières" - Q20 ❌
   - Section 8 includes "Troubles de l'érection (pour les hommes)" - Q25 ✅
   - Total: 31 questions visible
5. Answer all questions
6. Submit and verify results show:
   - Items scored: 31
   - Excluded items: ['q20']
   - Range: 0-62

#### Test Scenario 3: Other/Non-binary
1. Restart from PRISE-M selection
2. Select "Autre / Préfère ne pas dire" (Other)
3. Click "Continue to Questionnaire"
4. **Verify**:
   - Demographics banner shows: `Demographics: gender=X`
   - Section 6 does NOT include "Règles irrégulières" - Q20 ❌
   - Section 8 does NOT include "Troubles de l'érection" - Q25 ❌
   - Total: 30 questions visible
5. Answer all questions
6. Submit and verify results show:
   - Items scored: 30
   - Excluded items: ['q20', 'q25']
   - Range: 0-60

### 4. Test API Directly

#### Get Questionnaire (Filtered by Gender)
```bash
# Female
curl "http://localhost:8000/api/auto/questionnaires/PRISE-M.fr?gender=F" | jq '.questions | length'
# Expected: 31

# Male
curl "http://localhost:8000/api/auto/questionnaires/PRISE-M.fr?gender=M" | jq '.questions | length'
# Expected: 31

# Other
curl "http://localhost:8000/api/auto/questionnaires/PRISE-M.fr?gender=X" | jq '.questions | length'
# Expected: 30
```

#### Submit Answers with Demographics
```bash
# Female submission
curl -X POST "http://localhost:8000/api/auto/questionnaires/PRISE-M.fr/submit" \
  -H "Content-Type: application/json" \
  -d '{
    "answers": {
      "q1": 0, "q2": 0, "q3": 0, "q4": 0, "q5": 0, "q6": 0, "q7": 0, "q8": 0,
      "q9": 0, "q10": 0, "q11": 0, "q12": 0, "q13": 0, "q14": 0, "q15": 0, 
      "q16": 0, "q17": 0, "q18": 0, "q19": 0, "q20": 0, "q21": 0, "q22": 0,
      "q23": 0, "q24": 0, "q26": 0, "q27": 0, "q28": 0, "q29": 0, "q30": 0,
      "q31": 0, "q32": 0
    },
    "demographics": {
      "gender": "F"
    }
  }' | jq '.score_data.excluded_items'
# Expected: ["q25"]
```

## Key Features

### 1. **Automatic Question Filtering**
   - Questions are filtered based on demographics
   - Gender-specific questions only shown when relevant
   - Sections with no visible questions are hidden

### 2. **Dynamic Validation**
   - Only visible questions are validated
   - Required status evaluated based on context
   - Clear error messages for missing answers

### 3. **Progress Tracking**
   - Progress bar accounts for visible questions only
   - Accurate count of answered vs required questions

### 4. **User Experience**
   - Clear two-phase flow (Demographics → Questionnaire)
   - Demographics summary displayed in form
   - Gender-specific question text clearly marked
   - Helpful notes explain why information is needed

### 5. **Backward Compatibility**
   - Questionnaires without branching logic work as before
   - Demographics are optional (only collected when needed)
   - No breaking changes to existing questionnaires

## Architecture Benefits

### 1. **Separation of Concerns**
   - Backend defines all branching logic
   - Frontend just follows the rules
   - Easy to add new conditional questionnaires

### 2. **Extensibility**
   - JSONLogic supports complex conditions
   - Can handle multi-level branching
   - Not limited to gender (age, diagnosis, etc.)

### 3. **Maintainability**
   - Single source of truth (backend)
   - Type-safe TypeScript implementation
   - Well-tested components

### 4. **Clinical Accuracy**
   - Ensures correct questions shown to correct respondents
   - Prevents scoring errors from inappropriate items
   - Clear documentation of logic in code

## Next Steps (Optional Enhancements)

1. **Add visual indicators** for gender-specific questions
2. **Implement question dependencies** (show Q if Q-1 is certain value)
3. **Add age-based branching** for other questionnaires
4. **Create admin UI** to configure branching logic
5. **Add validation rules** for cross-question consistency
6. **Implement skip patterns** for complex clinical logic

## Documentation

- Implementation details: `BRANCHING_LOGIC_IMPLEMENTATION.md`
- This testing guide: `PRISE_M_TESTING_GUIDE.md`
- Backend code: `questionnaires/auto/prise_m/prise_m.py`
- Frontend components:
  - `app/components/Demographics.tsx`
  - `app/lib/jsonlogic.ts`
  - `app/questionnaire/[category]/[id]/page.tsx`

## Status: ✅ PRODUCTION READY

All tests passing, no linter errors, ready for deployment.

