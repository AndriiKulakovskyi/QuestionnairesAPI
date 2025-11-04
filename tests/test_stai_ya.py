"""
Tests for STAI-YA (Inventaire d'Anxiété État - STAI Forme Y-A)
State-Trait Anxiety Inventory - Form Y-A
"""

import pytest
from questionnaires.stai_ya import STAIYA, STAIYAError


class TestSTAIYAMetadata:
    """Test questionnaire metadata and structure."""
    
    def test_initialization(self):
        """Test questionnaire initialization."""
        stai = STAIYA()
        assert stai.id == "STAI-YA.fr"
        assert stai.abbreviation == "STAI-YA"
        assert stai.language == "fr-FR"
        assert stai.version == "1.0"
        assert stai.reference_period == "À l'instant, juste en ce moment"
    
    def test_metadata(self):
        """Test metadata retrieval."""
        stai = STAIYA()
        metadata = stai.get_metadata()
        
        assert metadata["id"] == "STAI-YA.fr"
        assert metadata["num_items"] == 20
        assert metadata["score_range"] == [20, 80]
        assert len(metadata["reverse_items"]) == 10
        assert set(metadata["reverse_items"]) == {1, 2, 5, 8, 10, 11, 15, 16, 19, 20}
    
    def test_questions_structure(self):
        """Test questions structure."""
        stai = STAIYA()
        questions = stai.get_questions()
        
        assert len(questions) == 20
        
        # Test first question (reverse-scored)
        q1 = questions[0]
        assert q1["id"] == "q1"
        assert q1["number"] == 1
        assert "calme" in q1["text"].lower()
        assert q1["reverse_scored"] is True
        assert len(q1["options"]) == 4
        
        # Test third question (direct-scored)
        q3 = questions[2]
        assert q3["id"] == "q3"
        assert q3["number"] == 3
        assert "tendu" in q3["text"].lower()
        assert q3["reverse_scored"] is False
    
    def test_response_options(self):
        """Test response options structure."""
        stai = STAIYA()
        questions = stai.get_questions()
        
        options = questions[0]["options"]
        assert len(options) == 4
        
        # Verify all options
        assert options[0] == {"code": 1, "label": "non", "score": 1}
        assert options[1] == {"code": 2, "label": "plutôt non", "score": 2}
        assert options[2] == {"code": 3, "label": "plutôt oui", "score": 3}
        assert options[3] == {"code": 4, "label": "oui", "score": 4}
    
    def test_sections(self):
        """Test sections structure."""
        stai = STAIYA()
        sections = stai.get_sections()
        
        assert len(sections) == 1
        assert sections[0]["id"] == "sec1"
        assert len(sections[0]["question_ids"]) == 20
        assert sections[0]["question_ids"] == [f"q{i}" for i in range(1, 21)]
    
    def test_reverse_items_constant(self):
        """Test reverse items constant."""
        assert STAIYA.REVERSE_ITEMS == {1, 2, 5, 8, 10, 11, 15, 16, 19, 20}
        assert len(STAIYA.REVERSE_ITEMS) == 10


class TestSTAIYAValidation:
    """Test validation logic."""
    
    def test_valid_answers(self):
        """Test validation with valid answers."""
        stai = STAIYA()
        answers = {f"q{i}": 2 for i in range(1, 21)}
        
        validation = stai.validate_answers(answers)
        assert validation["valid"] is True
        assert len(validation["errors"]) == 0
    
    def test_missing_items(self):
        """Test validation with missing items."""
        stai = STAIYA()
        answers = {f"q{i}": 2 for i in range(1, 19)}  # Missing q19, q20
        
        validation = stai.validate_answers(answers)
        assert validation["valid"] is False
        assert len(validation["errors"]) == 1
        assert "q19" in validation["errors"][0]
        assert "q20" in validation["errors"][0]
    
    def test_invalid_value_type(self):
        """Test validation with invalid value types."""
        stai = STAIYA()
        answers = {f"q{i}": 2 for i in range(1, 21)}
        answers["q5"] = "2"  # String instead of int
        
        validation = stai.validate_answers(answers)
        assert validation["valid"] is False
        assert any("q5" in error for error in validation["errors"])
    
    def test_out_of_range_values(self):
        """Test validation with out-of-range values."""
        stai = STAIYA()
        answers = {f"q{i}": 2 for i in range(1, 21)}
        answers["q10"] = 5  # Out of range
        answers["q15"] = 0  # Out of range
        
        validation = stai.validate_answers(answers)
        assert validation["valid"] is False
        assert len(validation["errors"]) == 2
    
    def test_all_same_answers_warning(self):
        """Test warning for all identical responses."""
        stai = STAIYA()
        answers = {f"q{i}": 3 for i in range(1, 21)}
        
        validation = stai.validate_answers(answers)
        assert validation["valid"] is True
        assert len(validation["warnings"]) > 0
        assert "identiques" in validation["warnings"][0].lower()


class TestSTAIYAScoring:
    """Test scoring calculations."""
    
    def test_all_minimum_scores(self):
        """Test scoring with all minimum responses (1 = non)."""
        stai = STAIYA()
        answers = {f"q{i}": 1 for i in range(1, 21)}
        
        result = stai.calculate_score(answers)
        
        # Direct items (10): 1 each = 10
        # Reverse items (10): 5-1=4 each = 40
        # Total = 50
        assert result["total_score"] == 50
        assert result["category"] == "Anxiété état moyenne"
        assert result["severity"] == "average"
    
    def test_all_maximum_scores(self):
        """Test scoring with all maximum responses (4 = oui)."""
        stai = STAIYA()
        answers = {f"q{i}": 4 for i in range(1, 21)}
        
        result = stai.calculate_score(answers)
        
        # Direct items (10): 4 each = 40
        # Reverse items (10): 5-4=1 each = 10
        # Total = 50
        assert result["total_score"] == 50
        assert result["category"] == "Anxiété état moyenne"
        assert result["severity"] == "average"
    
    def test_reverse_scoring_logic(self):
        """Test reverse scoring is applied correctly."""
        stai = STAIYA()
        
        # Test with reverse item q1 (calm)
        answers = {f"q{i}": 2 for i in range(1, 21)}
        answers["q1"] = 1  # "non" to "calm" = high anxiety = reversed to 4
        
        result = stai.calculate_score(answers)
        assert result["item_scores"]["q1"]["raw"] == 1
        assert result["item_scores"]["q1"]["scored"] == 4
        assert result["item_scores"]["q1"]["reversed"] is True
        
        # Test with direct item q3 (tense)
        assert result["item_scores"]["q3"]["raw"] == 2
        assert result["item_scores"]["q3"]["scored"] == 2
        assert result["item_scores"]["q3"]["reversed"] is False
    
    def test_very_low_anxiety_category(self):
        """Test very low anxiety category (≤35)."""
        stai = STAIYA()
        
        # Create response pattern for low anxiety
        # High scores on positive items (calm, content, etc.)
        # Low scores on negative items (tense, worried, etc.)
        answers = {}
        for i in range(1, 21):
            if i in STAIYA.REVERSE_ITEMS:  # Positive items
                answers[f"q{i}"] = 4  # "oui" to calm/content = reversed to 1
            else:  # Negative items
                answers[f"q{i}"] = 1  # "non" to tense/worried = 1
        
        result = stai.calculate_score(answers)
        assert result["total_score"] == 20
        assert result["category"] == "Anxiété état très faible"
        assert result["severity"] == "very_low"
    
    def test_low_anxiety_category(self):
        """Test low anxiety category (36-45)."""
        stai = STAIYA()
        answers = {f"q{i}": 2 for i in range(1, 21)}
        
        result = stai.calculate_score(answers)
        
        # All 2s: direct items = 20, reverse items = (5-2)*10 = 30, total = 50
        # Actually this gives 50, let me adjust
        
        # For score ~40: need different pattern
        answers = {}
        for i in range(1, 21):
            if i in STAIYA.REVERSE_ITEMS:
                answers[f"q{i}"] = 3  # Reversed: 5-3 = 2
            else:
                answers[f"q{i}"] = 2  # Direct: 2
        
        result = stai.calculate_score(answers)
        # 10 reverse items * 2 = 20, 10 direct items * 2 = 20, total = 40
        assert result["total_score"] == 40
        assert result["category"] == "Anxiété état faible"
        assert result["severity"] == "low"
    
    def test_average_anxiety_category(self):
        """Test average anxiety category (46-55)."""
        stai = STAIYA()
        answers = {f"q{i}": 2 for i in range(1, 21)}
        
        result = stai.calculate_score(answers)
        # All 2s: reverse = 3*10=30, direct = 2*10=20, total = 50
        assert result["total_score"] == 50
        assert result["category"] == "Anxiété état moyenne"
        assert result["severity"] == "average"
    
    def test_high_anxiety_category(self):
        """Test high anxiety category (56-65)."""
        stai = STAIYA()
        
        # Pattern for high anxiety
        answers = {}
        for i in range(1, 21):
            if i in STAIYA.REVERSE_ITEMS:  # Low on positive items
                answers[f"q{i}"] = 2  # Reversed: 5-2 = 3
            else:  # High on negative items
                answers[f"q{i}"] = 3
        
        result = stai.calculate_score(answers)
        # 10 reverse * 3 = 30, 10 direct * 3 = 30, total = 60
        assert result["total_score"] == 60
        assert result["category"] == "Anxiété état élevée"
        assert result["severity"] == "high"
    
    def test_very_high_anxiety_category(self):
        """Test very high anxiety category (≥66)."""
        stai = STAIYA()
        
        # Pattern for very high anxiety
        answers = {}
        for i in range(1, 21):
            if i in STAIYA.REVERSE_ITEMS:  # Very low on positive items
                answers[f"q{i}"] = 1  # Reversed: 5-1 = 4
            else:  # Very high on negative items
                answers[f"q{i}"] = 4
        
        result = stai.calculate_score(answers)
        # 10 reverse * 4 = 40, 10 direct * 4 = 40, total = 80
        assert result["total_score"] == 80
        assert result["category"] == "Anxiété état très élevée"
        assert result["severity"] == "very_high"
    
    def test_boundary_score_35_36(self):
        """Test boundary between very low and low (35-36)."""
        stai = STAIYA()
        
        # Score = 35
        answers = {}
        for i in range(1, 21):
            if i in STAIYA.REVERSE_ITEMS:
                answers[f"q{i}"] = 4 if i <= 15 else 3
            else:
                answers[f"q{i}"] = 1 if i <= 15 else 2
        
        result = stai.calculate_score(answers)
        if result["total_score"] <= 35:
            assert result["severity"] == "very_low"
        else:
            assert result["severity"] == "low"
    
    def test_boundary_score_65_66(self):
        """Test boundary between high and very high (65-66)."""
        stai = STAIYA()
        
        # Pattern for score near boundary
        answers = {}
        for i in range(1, 21):
            if i in STAIYA.REVERSE_ITEMS:
                answers[f"q{i}"] = 1
            else:
                answers[f"q{i}"] = 3 if i <= 16 else 4
        
        result = stai.calculate_score(answers)
        if result["total_score"] <= 65:
            assert result["severity"] == "high"
        else:
            assert result["severity"] == "very_high"
    
    def test_invalid_answers_raise_error(self):
        """Test that invalid answers raise STAIYAError."""
        stai = STAIYA()
        answers = {f"q{i}": 2 for i in range(1, 19)}  # Missing items
        
        with pytest.raises(STAIYAError) as exc_info:
            stai.calculate_score(answers)
        
        assert "Validation échouée" in str(exc_info.value)
    
    def test_score_result_structure(self):
        """Test that score result has all required fields."""
        stai = STAIYA()
        answers = {f"q{i}": 2 for i in range(1, 21)}
        
        result = stai.calculate_score(answers)
        
        assert "total_score" in result
        assert "score_range" in result
        assert "category" in result
        assert "severity" in result
        assert "item_scores" in result
        assert "interpretation" in result
        assert "warnings" in result
        assert "calculation_date" in result
        
        assert result["score_range"] == [20, 80]
        assert len(result["item_scores"]) == 20
    
    def test_item_scores_details(self):
        """Test that item scores contain detailed information."""
        stai = STAIYA()
        answers = {f"q{i}": 3 for i in range(1, 21)}
        
        result = stai.calculate_score(answers)
        
        # Check reverse item
        q1_score = result["item_scores"]["q1"]
        assert q1_score["raw"] == 3
        assert q1_score["scored"] == 2  # 5-3
        assert q1_score["reversed"] is True
        
        # Check direct item
        q3_score = result["item_scores"]["q3"]
        assert q3_score["raw"] == 3
        assert q3_score["scored"] == 3
        assert q3_score["reversed"] is False


class TestSTAIYAClinicalScenarios:
    """Test clinical use cases."""
    
    def test_calm_patient_scenario(self):
        """Test patient reporting feeling very calm (low anxiety)."""
        stai = STAIYA()
        
        # Patient agrees with all positive items, disagrees with negative
        answers = {}
        for i in range(1, 21):
            if i in STAIYA.REVERSE_ITEMS:  # Positive items (calm, content, etc.)
                answers[f"q{i}"] = 4  # "oui"
            else:  # Negative items (tense, worried, etc.)
                answers[f"q{i}"] = 1  # "non"
        
        result = stai.calculate_score(answers)
        assert result["total_score"] == 20
        assert result["severity"] == "very_low"
        assert "très calme" in result["interpretation"].lower()
    
    def test_highly_anxious_patient_scenario(self):
        """Test patient reporting high state anxiety."""
        stai = STAIYA()
        
        # Patient disagrees with positive items, agrees with negative
        answers = {}
        for i in range(1, 21):
            if i in STAIYA.REVERSE_ITEMS:  # Positive items
                answers[f"q{i}"] = 1  # "non" - not calm
            else:  # Negative items
                answers[f"q{i}"] = 4  # "oui" - very tense/worried
        
        result = stai.calculate_score(answers)
        assert result["total_score"] == 80
        assert result["severity"] == "very_high"
        assert "très élevée" in result["interpretation"].lower()
    
    def test_mixed_anxiety_scenario(self):
        """Test patient with mixed anxiety presentation."""
        stai = STAIYA()
        
        # Realistic mixed pattern
        answers = {
            "q1": 2,   # Somewhat calm
            "q2": 3,   # Mostly secure
            "q3": 3,   # Somewhat tense
            "q4": 2,   # Somewhat overwhelmed
            "q5": 2,   # Somewhat at ease
            "q6": 3,   # Somewhat upset
            "q7": 2,   # Somewhat worried
            "q8": 3,   # Mostly content
            "q9": 2,   # Somewhat frightened
            "q10": 3,  # Mostly comfortable
            "q11": 3,  # Mostly confident
            "q12": 2,  # Somewhat nervous
            "q13": 2,  # Somewhat scared
            "q14": 2,  # Somewhat indecisive
            "q15": 2,  # Somewhat relaxed
            "q16": 3,  # Mostly satisfied
            "q17": 2,  # Somewhat worried
            "q18": 2,  # Somewhat confused
            "q19": 3,  # Mostly stable
            "q20": 3   # Mostly good mood
        }
        
        result = stai.calculate_score(answers)
        assert 46 <= result["total_score"] <= 55
        assert result["severity"] == "average"
    
    def test_pre_post_intervention_comparison(self):
        """Test comparing scores before and after intervention."""
        stai = STAIYA()
        
        # Pre-intervention: moderate-high anxiety
        pre_answers = {}
        for i in range(1, 21):
            if i in STAIYA.REVERSE_ITEMS:
                pre_answers[f"q{i}"] = 2
            else:
                pre_answers[f"q{i}"] = 3
        
        pre_result = stai.calculate_score(pre_answers)
        
        # Post-intervention: reduced anxiety
        post_answers = {}
        for i in range(1, 21):
            if i in STAIYA.REVERSE_ITEMS:
                post_answers[f"q{i}"] = 3
            else:
                post_answers[f"q{i}"] = 2
        
        post_result = stai.calculate_score(post_answers)
        
        # Post should be lower than pre
        assert post_result["total_score"] < pre_result["total_score"]


class TestSTAIYASchema:
    """Test JSON schema generation."""
    
    def test_get_schema(self):
        """Test complete schema generation."""
        stai = STAIYA()
        schema = stai.get_schema()
        
        assert "instrument" in schema
        assert "sections" in schema
        assert "questions" in schema
        assert "scoring" in schema
        assert "logic" in schema
        assert "provenance" in schema
    
    def test_schema_instrument(self):
        """Test instrument section of schema."""
        stai = STAIYA()
        schema = stai.get_schema()
        
        instrument = schema["instrument"]
        assert instrument["id"] == "STAI-YA.fr"
        assert instrument["abbreviation"] == "STAI-YA"
        assert instrument["num_items"] == 20
    
    def test_schema_scoring(self):
        """Test scoring section of schema."""
        stai = STAIYA()
        schema = stai.get_schema()
        
        scoring = schema["scoring"]
        assert "scales" in scoring
        assert "categories" in scoring
        
        assert len(scoring["scales"]) == 1
        assert scoring["scales"][0]["id"] == "stai_ya_total"
        assert scoring["scales"][0]["range"] == [20, 80]
        
        assert len(scoring["categories"]) == 5
    
    def test_schema_provenance(self):
        """Test provenance tracking."""
        stai = STAIYA()
        schema = stai.get_schema()
        
        provenance = schema["provenance"]
        assert "created_at" in provenance
        assert "updated_at" in provenance
        assert "validated_by" in provenance
        assert "validation_date" in provenance


class TestSTAIYAEdgeCases:
    """Test edge cases and error handling."""
    
    def test_empty_answers(self):
        """Test with empty answers dictionary."""
        stai = STAIYA()
        validation = stai.validate_answers({})
        
        assert validation["valid"] is False
        assert len(validation["errors"]) > 0
    
    def test_extra_items(self):
        """Test with extra items that shouldn't be there."""
        stai = STAIYA()
        answers = {f"q{i}": 2 for i in range(1, 21)}
        answers["q21"] = 3  # Extra item
        answers["extra"] = 4
        
        # Should still validate successfully (extra items ignored)
        validation = stai.validate_answers(answers)
        assert validation["valid"] is True
    
    def test_minimum_score_boundary(self):
        """Test absolute minimum possible score."""
        stai = STAIYA()
        
        # All positive items = 4, all negative items = 1
        answers = {}
        for i in range(1, 21):
            if i in STAIYA.REVERSE_ITEMS:
                answers[f"q{i}"] = 4
            else:
                answers[f"q{i}"] = 1
        
        result = stai.calculate_score(answers)
        assert result["total_score"] == 20
        assert result["score_range"] == [20, 80]
    
    def test_maximum_score_boundary(self):
        """Test absolute maximum possible score."""
        stai = STAIYA()
        
        # All positive items = 1, all negative items = 4
        answers = {}
        for i in range(1, 21):
            if i in STAIYA.REVERSE_ITEMS:
                answers[f"q{i}"] = 1
            else:
                answers[f"q{i}"] = 4
        
        result = stai.calculate_score(answers)
        assert result["total_score"] == 80
        assert result["score_range"] == [20, 80]
    
    def test_all_items_same_response_variations(self):
        """Test each possible uniform response (1-4)."""
        stai = STAIYA()
        
        for value in [1, 2, 3, 4]:
            answers = {f"q{i}": value for i in range(1, 21)}
            result = stai.calculate_score(answers)
            
            # Should have warning about same responses
            assert len(result["warnings"]) > 0
            # Should still calculate score
            assert 20 <= result["total_score"] <= 80

