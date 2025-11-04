# PRISE-M Gender-Specific Branching Logic Implementation

## Overview

PRISE-M has two gender-specific questions that require conditional display:
- **Q20** (Section 6): "Règles irrégulières" - Female-specific
- **Q25** (Section 8): "Troubles de l'érection" - Male-specific

## Backend Implementation (✅ COMPLETE)

### Architecture

The backend uses a three-tier approach for branching logic:

1. **Question-Level Metadata**
   - `gender_specific`: "F", "M", or None
   - `display_if`: JSONLogic condition for visibility
   - `required_if`: JSONLogic condition for requirement

2. **Respondent Schema** (`get_respondent_schema()`)
   - Defines required demographics (gender)
   - Documents gender options: F (Female), M (Male), X (Other/Non-binary)

3. **Branching Logic API** (`get_branching_logic()`)
   - Machine-readable rules for frontend implementation
   - Visibility rules, requirement rules, scoring adjustments

### Key Backend Features

```python
# Gender handling
- Gender "F": Shows q20, hides q25, scores 31 items (range 0-62)
- Gender "M": Shows q25, hides q20, scores 31 items (range 0-62)  
- Gender "X": Hides both, scores 30 items (range 0-60)

# API Methods
questionnaire.get_questions(gender="F")  # Returns filtered questions
questionnaire.calculate_score(answers, gender="F")  # Gender-aware scoring
```

### Scoring Logic

```python
def calculate_score(answers, gender):
    # Determines which items to exclude based on gender
    if gender == "F":
        excluded = ["q25"]  # Exclude male-specific
    elif gender == "M":
        excluded = ["q20"]  # Exclude female-specific
    elif gender == "X":
        excluded = ["q20", "q25"]  # Exclude both
    
    # Sum only non-excluded items
    total = sum(answers[f"q{i}"] for i in range(1, 33) if f"q{i}" not in excluded)
```

## Frontend Implementation (🔧 TO IMPLEMENT)

### Strategy: Two-Phase Questionnaire Flow

**Phase 1: Demographics Collection**
- Before showing questions, collect gender
- Required for PRISE-M and other questionnaires with branching logic

**Phase 2: Questionnaire with Conditional Questions**
- Filter questions based on gender
- Only show applicable questions
- Submit with gender context

### Components to Create/Update

#### 1. Demographics Component (`components/Demographics.tsx`)
```typescript
interface DemographicsProps {
  schema: RespondentSchema;  // From get_respondent_schema()
  onComplete: (demographics: Record<string, any>) => void;
}

// Shows gender selection before questionnaire
// Validates required fields
```

#### 2. Update Question Page (`questionnaire/[category]/[id]/page.tsx`)
```typescript
// Add state for demographics
const [demographics, setDemographics] = useState<Record<string, any>>({});
const [showDemographics, setShowDemographics] = useState(false);

// Check if questionnaire requires demographics
useEffect(() => {
  if (questionnaire?.respondent) {
    setShowDemographics(true);
  }
}, [questionnaire]);

// Filter questions based on demographics
const visibleQuestions = filterQuestionsByLogic(
  questionnaire.questions,
  demographics,
  questionnaire.logic
);

// Submit with demographics
await submitAnswers(category, id, {
  ...answers,
  gender: demographics.gender  // Include in API call
});
```

#### 3. API Update (`api/routes/auto.py`)
```python
@router.post("/questionnaires/{questionnaire_id}/submit")
def submit_auto_questionnaire_answers(
    questionnaire_id: str,
    answers_request: AnswersRequest,
    gender: Optional[str] = None,  # Add gender parameter
    registry: QuestionnaireRegistry = Depends(get_registry)
):
    # Extract gender from answers if provided
    gender_value = answers_request.answers.pop('gender', None) or gender
    
    # Calculate score with gender
    result = questionnaire.calculate_score(
        answers_request.answers,
        gender=gender_value
    )
```

### JSONLogic Evaluation

Questions with `display_if` conditions need evaluation:

```typescript
import jsonLogic from 'json-logic-js';

function shouldShowQuestion(question: Question, context: Record<string, any>): boolean {
  if (!question.display_if) return true;
  return jsonLogic.apply(question.display_if, context);
}

// Example:
// question.display_if = {"==": [{"var": "gender"}, "F"]}
// context = {gender: "F"}
// Result: true (show question)
```

### User Experience Flow

```
1. User selects PRISE-M questionnaire
   ↓
2. System detects questionnaire requires demographics
   ↓
3. Show gender selection screen:
   "This questionnaire requires demographic information"
   [ ] Femme (Female)
   [ ] Homme (Male)
   [ ] Autre / Préfère ne pas dire (Other)
   [Continue →]
   ↓
4. User selects gender
   ↓
5. System filters questions:
   - Female: Shows q1-q19, q20, q21-q24, q26-q32 (31 questions)
   - Male: Shows q1-q19, q21-q25, q26-q32 (31 questions)
   - Other: Shows q1-q19, q21-q24, q26-q32 (30 questions)
   ↓
6. User answers visible questions
   ↓
7. Submit answers + gender to API
   ↓
8. Backend scores with proper exclusions
```

## Implementation Benefits

### 1. **Maintainability**
- All branching logic defined in backend
- Frontend just follows rules
- Easy to add new conditional questionnaires

### 2. **Consistency**
- Same logic for visibility and scoring
- Reduces bugs from frontend/backend mismatch

### 3. **Scalability**
- JSONLogic supports complex conditions
- Can handle multi-level branching
- Extensible to other demographic factors (age, diagnosis, etc.)

### 4. **User Experience**
- Only shows relevant questions
- Faster completion time
- Less confusion for respondents

## Testing Strategy

### Backend Tests
```python
# Test gender-based filtering
def test_female_questions():
    prisem = PRISEM()
    questions = prisem.get_questions(gender="F")
    question_ids = [q['id'] for q in questions]
    assert 'q20' in question_ids  # Female item included
    assert 'q25' not in question_ids  # Male item excluded

# Test scoring
def test_female_scoring():
    answers = {f"q{i}": 1 for i in range(1, 33)}
    result = prisem.calculate_score(answers, gender="F")
    assert result.items_scored == 31
    assert result.range == (0, 62)
    assert 'q25' in result.excluded_items
```

### Frontend Tests
```typescript
// Test conditional rendering
test('shows only female questions when gender is F', () => {
  const {getByText, queryByText} = render(
    <QuestionnairePage demographics={{gender: 'F'}} />
  );
  
  expect(getByText('Règles irrégulières')).toBeInTheDocument();
  expect(queryByText('Troubles de l\'érection')).not.toBeInTheDocument();
});
```

## API Updates Required

### 1. Update AnswersRequest Schema
```python
class AnswersRequest(BaseModel):
    answers: Record[str, Any]
    demographics: Optional[Dict[str, str]] = None  # Add demographics field
```

### 2. Update GET questionnaire endpoint
```python
@router.get("/questionnaires/{questionnaire_id}")
def get_auto_questionnaire(
    questionnaire_id: str,
    gender: Optional[str] = None,  # Add gender query parameter
    registry: QuestionnaireRegistry = Depends(get_registry)
):
    # Get questionnaire with filtered questions
    full_structure = questionnaire.get_full_questionnaire(gender=gender)
    return QuestionnaireDetail(**full_structure)
```

### 3. Update submit endpoint
```python
@router.post("/questionnaires/{questionnaire_id}/submit")
def submit_auto_questionnaire_answers(
    questionnaire_id: str,
    answers_request: AnswersRequest,
    registry: QuestionnaireRegistry = Depends(get_registry)
):
    # Extract demographics
    demographics = answers_request.demographics or {}
    gender = demographics.get('gender')
    
    # Calculate score with context
    result = questionnaire.calculate_score(
        answers_request.answers,
        gender=gender
    )
```

## Migration Path

### Phase 1: Backend API Updates (Priority: HIGH)
1. Update API schemas to accept demographics
2. Update submit endpoint to use gender parameter
3. Test with existing PRISE-M implementation

### Phase 2: Frontend Basic Support (Priority: HIGH)
1. Create Demographics component
2. Update questionnaire page to collect demographics
3. Submit demographics with answers

### Phase 3: Frontend Advanced Features (Priority: MEDIUM)
1. Implement JSONLogic evaluation
2. Dynamic question filtering
3. Conditional validation

### Phase 4: Enhanced UX (Priority: LOW)
1. Progress bar accounting for hidden questions
2. Section headers showing question counts
3. Help text explaining why questions are hidden

## Success Criteria

✅ Users can complete PRISE-M questionnaire
✅ Correct questions shown based on gender
✅ Scores calculated correctly (31 or 30 items)
✅ Clear indication of which item was excluded
✅ Works for all three gender options (F, M, X)
✅ No breaking changes to existing questionnaires
✅ Extensible to future branching logic needs

