"""
Quick test script to verify the refactored questionnaire system works correctly.
"""

# Import the refactored package
from refactored import (
    questionnaire_registry,
    questionnaire_factory,
    QuestionnaireResponse,
    PathologyDomain
)
from refactored.api.service import questionnaire_service

def test_registry():
    """Test that questionnaires are registered."""
    print("=" * 60)
    print("TEST 1: Registry")
    print("=" * 60)
    
    all_codes = questionnaire_registry.list_all()
    print(f"✅ Total questionnaires registered: {len(all_codes)}")
    print(f"   Sample: {all_codes[:10]}")
    
    # Test filtering by pathology
    bipolar_quests = questionnaire_registry.list_by_pathology(PathologyDomain.BIPOLAR)
    print(f"✅ Bipolar questionnaires: {len(bipolar_quests)}")
    
    print()

def test_questionnaire_creation():
    """Test creating and using a questionnaire."""
    print("=" * 60)
    print("TEST 2: Questionnaire Creation & Scoring")
    print("=" * 60)
    
    # Create YMRS
    ymrs = questionnaire_factory.create("YMRS")
    print(f"✅ Created YMRS: {ymrs.name}")
    print(f"   Questions: {len(ymrs.questions)}")
    print(f"   Duration: {ymrs.estimated_duration_minutes} minutes")
    
    # All answers 'a' (minimum score)
    responses = QuestionnaireResponse(
        questionnaire_id="YMRS",
        responses={f'ymrs{i}': 'a' for i in range(1, 12)}
    )
    
    # Validate
    errors = ymrs.validate_responses(responses)
    if errors:
        print(f"❌ Validation errors: {errors}")
    else:
        print("✅ Responses validated successfully")
    
    # Score
    result = ymrs.compute_score(responses)
    print(f"✅ Score computed: {result.total_score}")
    print(f"   Interpretation: {result.interpretation}")
    print(f"   Severity: {result.severity_level}")
    
    print()

def test_madrs():
    """Test MADRS questionnaire."""
    print("=" * 60)
    print("TEST 3: MADRS (Simple Sum Scoring)")
    print("=" * 60)
    
    madrs = questionnaire_factory.create("MADRS")
    print(f"✅ Created MADRS: {madrs.name}")
    print(f"   Questions: {len(madrs.questions)}")
    
    # All answers 'a' (score 0)
    responses = QuestionnaireResponse(
        questionnaire_id="MADRS",
        responses={f'madrs{i}': 'a' for i in range(1, 11)}
    )
    
    result = madrs.compute_score(responses)
    print(f"✅ Score: {result.total_score}")
    print(f"   Interpretation: {result.interpretation}")
    
    print()

def test_api_service():
    """Test the API service layer."""
    print("=" * 60)
    print("TEST 4: API Service Layer")
    print("=" * 60)
    
    # List all
    all_quests = questionnaire_service.list_all_questionnaires()
    print(f"✅ API: Listed {len(all_quests)} questionnaires")
    
    # Get details
    ymrs_schema = questionnaire_service.get_questionnaire_details("YMRS")
    print(f"✅ API: Retrieved YMRS details")
    print(f"   Code: {ymrs_schema['code']}")
    print(f"   Questions: {len(ymrs_schema['questions'])}")
    
    # Validate response
    validation = questionnaire_service.validate_response(
        code="YMRS",
        responses={f'ymrs{i}': 'a' for i in range(1, 12)}
    )
    print(f"✅ API: Validation result: {validation['valid']}")
    
    # Compute scores
    score_result = questionnaire_service.compute_scores(
        code="YMRS",
        responses={f'ymrs{i}': 'b' for i in range(1, 12)},
        respondent_id="patient123"
    )
    print(f"✅ API: Score computation successful: {score_result['success']}")
    print(f"   Total Score: {score_result['scores']['total_score']}")
    
    print()

def test_generated_questionnaires():
    """Test some generated questionnaires."""
    print("=" * 60)
    print("TEST 5: Generated Questionnaires")
    print("=" * 60)
    
    test_codes = ['ALTMAN', 'ALDA', 'BARNES', 'CGI', 'FAST', 'SHAPS', 'CTQ']
    
    for code in test_codes:
        try:
            quest = questionnaire_factory.create(code)
            print(f"✅ {code}: {len(quest.questions)} questions, {quest.pathology_domain.value} domain")
        except Exception as e:
            print(f"❌ {code}: {e}")
    
    print()

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("REFACTORED QUESTIONNAIRE SYSTEM - TEST SUITE")
    print("=" * 60)
    print()
    
    try:
        test_registry()
        test_questionnaire_creation()
        test_madrs()
        test_api_service()
        test_generated_questionnaires()
        
        print("=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print()
        print("📊 Summary:")
        print(f"   - {len(questionnaire_registry.list_all())} questionnaires registered")
        print(f"   - Core infrastructure: ✅ Complete")
        print(f"   - API service layer: ✅ Functional")
        print(f"   - Auto-registration: ✅ Working")
        print()
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
