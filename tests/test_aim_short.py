"""
Tests for AIM-short (Affect Intensity Measure - Version courte)
"""

import pytest
from questionnaires.aim_short import AIMShort, AIMShortError


class TestAIMShortMetadata:
    """Test questionnaire metadata and structure."""
    
    def test_initialization(self):
        """Test questionnaire initialization."""
        aim = AIMShort()
        assert aim.id == "AIM-short.fr"
        assert aim.abbreviation == "AIM-20"
        assert aim.language == "fr-FR"
        assert aim.version == "1.0"
    
    def test_metadata(self):
        """Test metadata retrieval."""
        aim = AIMShort()
        metadata = aim.get_metadata()
        
        assert metadata["id"] == "AIM-short.fr"
        assert metadata["num_items"] == 20
        assert metadata["score_range"] == [1.0, 6.0]
        assert metadata["score_type"] == "mean"
        assert len(metadata["reverse_items"]) == 6
        assert set(metadata["reverse_items"]) == {5, 10, 13, 15, 18, 20}
    
    def test_questions_structure(self):
        """Test questions structure."""
        aim = AIMShort()
        questions = aim.get_questions()
        
        assert len(questions) == 20
        
        # Test first question (direct-scored)
        q1 = questions[0]
        assert q1["id"] == "q1"
        assert q1["number"] == 1
        assert "exubérance" in q1["text"].lower()
        assert q1["reverse_scored"] is False
        assert len(q1["options"]) == 6
        
        # Test fifth question (reverse-scored)
        q5 = questions[4]
        assert q5["id"] == "q5"
        assert q5["number"] == 5
        assert q5["reverse_scored"] is True
    
    def test_response_options(self):
        """Test response options structure."""
        aim = AIMShort()
        questions = aim.get_questions()
        
        options = questions[0]["options"]
        assert len(options) == 6
        
        # Verify all options
        assert options[0] == {"code": 1, "label": "1 – Jamais", "score": 1}
        assert options[1] == {"code": 2, "label": "2 – Presque jamais", "score": 2}
        assert options[2] == {"code": 3, "label": "3 – Occasionnellement", "score": 3}
        assert options[3] == {"code": 4, "label": "4 – Habituellement", "score": 4}
        assert options[4] == {"code": 5, "label": "5 – Presque toujours", "score": 5}
        assert options[5] == {"code": 6, "label": "6 – Toujours", "score": 6}
    
    def test_sections(self):
        """Test sections structure."""
        aim = AIMShort()
        sections = aim.get_sections()
        
        assert len(sections) == 1
        assert sections[0]["id"] == "sec1"
        assert len(sections[0]["question_ids"]) == 20
        assert sections[0]["question_ids"] == [f"q{i}" for i in range(1, 21)]
    
    def test_reverse_items_constant(self):
        """Test reverse items constant."""
        assert AIMShort.REVERSE_ITEMS == {5, 10, 13, 15, 18, 20}
        assert len(AIMShort.REVERSE_ITEMS) == 6


class TestAIMShortValidation:
    """Test validation logic."""
    
    def test_valid_answers(self):
        """Test validation with valid answers."""
        aim = AIMShort()
        answers = {f"q{i}": 3 for i in range(1, 21)}
        
        validation = aim.validate_answers(answers)
        assert validation["valid"] is True
        assert len(validation["errors"]) == 0
    
    def test_missing_items(self):
        """Test validation with missing items."""
        aim = AIMShort()
        answers = {f"q{i}": 3 for i in range(1, 18)}  # Missing q18, q19, q20
        
        validation = aim.validate_answers(answers)
        assert validation["valid"] is False
        assert len(validation["errors"]) == 1
        assert "q18" in validation["errors"][0]
        assert "q19" in validation["errors"][0]
        assert "q20" in validation["errors"][0]
    
    def test_invalid_value_type(self):
        """Test validation with invalid value types."""
        aim = AIMShort()
        answers = {f"q{i}": 3 for i in range(1, 21)}
        answers["q5"] = "3"  # String instead of int
        
        validation = aim.validate_answers(answers)
        assert validation["valid"] is False
        assert any("q5" in error for error in validation["errors"])
    
    def test_out_of_range_values(self):
        """Test validation with out-of-range values."""
        aim = AIMShort()
        answers = {f"q{i}": 3 for i in range(1, 21)}
        answers["q10"] = 7  # Out of range
        answers["q15"] = 0  # Out of range
        
        validation = aim.validate_answers(answers)
        assert validation["valid"] is False
        assert len(validation["errors"]) == 2
    
    def test_all_same_answers_warning(self):
        """Test warning for all identical responses."""
        aim = AIMShort()
        answers = {f"q{i}": 4 for i in range(1, 21)}
        
        validation = aim.validate_answers(answers)
        assert validation["valid"] is True
        assert len(validation["warnings"]) > 0
        assert "identiques" in validation["warnings"][0].lower()
    
    def test_all_minimum_warning(self):
        """Test warning for all minimum responses."""
        aim = AIMShort()
        answers = {f"q{i}": 1 for i in range(1, 21)}
        
        validation = aim.validate_answers(answers)
        assert validation["valid"] is True
        assert len(validation["warnings"]) > 0
        assert any("jamais" in w.lower() for w in validation["warnings"])
    
    def test_all_maximum_warning(self):
        """Test warning for all maximum responses."""
        aim = AIMShort()
        answers = {f"q{i}": 6 for i in range(1, 21)}
        
        validation = aim.validate_answers(answers)
        assert validation["valid"] is True
        assert len(validation["warnings"]) > 0
        assert any("toujours" in w.lower() for w in validation["warnings"])


class TestAIMShortScoring:
    """Test scoring calculations."""
    
    def test_all_middle_scores(self):
        """Test scoring with all responses at midpoint (3)."""
        aim = AIMShort()
        answers = {f"q{i}": 3 for i in range(1, 21)}
        
        result = aim.calculate_score(answers)
        
        # All items score 3 after recoding (3 -> 4 for reversed, 3 -> 3 for direct)
        # Direct items (14): 3 each = 42
        # Reverse items (6): 7-3=4 each = 24
        # Total = 66, Mean = 3.3
        assert result["sum_score"] == 66
        assert result["mean_score"] == 3.3
    
    def test_all_minimum_scores(self):
        """Test scoring with all minimum responses (1)."""
        aim = AIMShort()
        answers = {f"q{i}": 1 for i in range(1, 21)}
        
        result = aim.calculate_score(answers)
        
        # Direct items (14): 1 each = 14
        # Reverse items (6): 7-1=6 each = 36
        # Total = 50, Mean = 2.5
        assert result["sum_score"] == 50
        assert result["mean_score"] == 2.5
    
    def test_all_maximum_scores(self):
        """Test scoring with all maximum responses (6)."""
        aim = AIMShort()
        answers = {f"q{i}": 6 for i in range(1, 21)}
        
        result = aim.calculate_score(answers)
        
        # Direct items (14): 6 each = 84
        # Reverse items (6): 7-6=1 each = 6
        # Total = 90, Mean = 4.5
        assert result["sum_score"] == 90
        assert result["mean_score"] == 4.5
    
    def test_reverse_scoring_logic(self):
        """Test reverse scoring is applied correctly."""
        aim = AIMShort()
        
        # Test with specific values
        answers = {f"q{i}": 3 for i in range(1, 21)}
        answers["q5"] = 2   # Reverse item: 7-2 = 5
        answers["q10"] = 6  # Reverse item: 7-6 = 1
        
        result = aim.calculate_score(answers)
        
        # Check reverse item q5
        assert result["item_scores"]["q5"]["raw"] == 2
        assert result["item_scores"]["q5"]["scored"] == 5
        assert result["item_scores"]["q5"]["reversed"] is True
        
        # Check reverse item q10
        assert result["item_scores"]["q10"]["raw"] == 6
        assert result["item_scores"]["q10"]["scored"] == 1
        assert result["item_scores"]["q10"]["reversed"] is True
        
        # Check direct item q1
        assert result["item_scores"]["q1"]["raw"] == 3
        assert result["item_scores"]["q1"]["scored"] == 3
        assert result["item_scores"]["q1"]["reversed"] is False
    
    def test_very_low_intensity_category(self):
        """Test very low intensity category."""
        aim = AIMShort()
        
        # Pattern for very low intensity (mean ~1.5)
        answers = {}
        for i in range(1, 21):
            if i in AIMShort.REVERSE_ITEMS:
                answers[f"q{i}"] = 6  # Reversed: 7-6 = 1
            else:
                answers[f"q{i}"] = 2  # Direct: 2
        
        result = aim.calculate_score(answers)
        # 6 reverse * 1 = 6, 14 direct * 2 = 28, total = 34, mean = 1.7
        assert result["mean_score"] < 2.0
        assert result["severity"] == "very_low"
    
    def test_low_intensity_category(self):
        """Test low intensity category."""
        aim = AIMShort()
        
        # Pattern for low intensity (mean ~2.5)
        answers = {f"q{i}": 1 for i in range(1, 21)}
        
        result = aim.calculate_score(answers)
        assert 2.0 <= result["mean_score"] < 3.0
        assert result["severity"] == "low"
        assert "Presque jamais intense" in result["category"]
    
    def test_moderate_intensity_category(self):
        """Test moderate intensity category."""
        aim = AIMShort()
        
        # Pattern for moderate intensity
        answers = {f"q{i}": 3 for i in range(1, 21)}
        
        result = aim.calculate_score(answers)
        assert 3.0 <= result["mean_score"] < 4.0
        assert result["severity"] == "moderate"
        assert "Occasionnellement intense" in result["category"]
    
    def test_high_intensity_category(self):
        """Test high intensity category."""
        aim = AIMShort()
        
        # Pattern for high intensity
        answers = {f"q{i}": 4 for i in range(1, 21)}
        
        result = aim.calculate_score(answers)
        # All 4s: reverse = 7-4=3, direct = 4
        # 6*3 + 14*4 = 18 + 56 = 74, mean = 3.7
        assert 3.0 <= result["mean_score"] < 5.0
        assert result["severity"] in ["moderate", "high"]
    
    def test_very_high_intensity_category(self):
        """Test very high intensity category."""
        aim = AIMShort()
        
        # Pattern for very high intensity
        answers = {}
        for i in range(1, 21):
            if i in AIMShort.REVERSE_ITEMS:
                answers[f"q{i}"] = 1  # Reversed: 7-1 = 6
            else:
                answers[f"q{i}"] = 6  # Direct: 6
        
        result = aim.calculate_score(answers)
        # 6 reverse * 6 = 36, 14 direct * 6 = 84, total = 120, mean = 6.0
        assert result["mean_score"] >= 5.0
        assert result["severity"] == "very_high"
    
    def test_boundary_categories(self):
        """Test boundary between categories."""
        aim = AIMShort()
        
        # Test mean = 2.0 boundary
        answers = {}
        for i in range(1, 21):
            if i in AIMShort.REVERSE_ITEMS:
                answers[f"q{i}"] = 5  # 7-5 = 2
            else:
                answers[f"q{i}"] = 2
        
        result = aim.calculate_score(answers)
        assert result["mean_score"] == 2.0
        
        # Test mean = 4.0 boundary
        answers2 = {}
        for i in range(1, 21):
            if i in AIMShort.REVERSE_ITEMS:
                answers2[f"q{i}"] = 3  # 7-3 = 4
            else:
                answers2[f"q{i}"] = 4
        
        result2 = aim.calculate_score(answers2)
        assert result2["mean_score"] == 4.0
    
    def test_invalid_answers_raise_error(self):
        """Test that invalid answers raise AIMShortError."""
        aim = AIMShort()
        answers = {f"q{i}": 3 for i in range(1, 18)}  # Missing items
        
        with pytest.raises(AIMShortError) as exc_info:
            aim.calculate_score(answers)
        
        assert "Validation échouée" in str(exc_info.value)
    
    def test_score_result_structure(self):
        """Test that score result has all required fields."""
        aim = AIMShort()
        answers = {f"q{i}": 3 for i in range(1, 21)}
        
        result = aim.calculate_score(answers)
        
        assert "mean_score" in result
        assert "sum_score" in result
        assert "score_range" in result
        assert "sum_range" in result
        assert "category" in result
        assert "severity" in result
        assert "item_scores" in result
        assert "interpretation" in result
        assert "warnings" in result
        assert "calculation_date" in result
        
        assert result["score_range"] == [1.0, 6.0]
        assert result["sum_range"] == [20, 120]
        assert len(result["item_scores"]) == 20
    
    def test_item_scores_details(self):
        """Test that item scores contain detailed information."""
        aim = AIMShort()
        answers = {f"q{i}": 4 for i in range(1, 21)}
        
        result = aim.calculate_score(answers)
        
        # Check reverse item
        q5_score = result["item_scores"]["q5"]
        assert q5_score["raw"] == 4
        assert q5_score["scored"] == 3  # 7-4
        assert q5_score["reversed"] is True
        
        # Check direct item
        q1_score = result["item_scores"]["q1"]
        assert q1_score["raw"] == 4
        assert q1_score["scored"] == 4
        assert q1_score["reversed"] is False
    
    def test_mean_score_precision(self):
        """Test that mean score is properly rounded."""
        aim = AIMShort()
        
        # Create pattern that results in non-integer mean
        answers = {}
        for i in range(1, 21):
            answers[f"q{i}"] = 3 if i <= 10 else 4
        
        result = aim.calculate_score(answers)
        
        # Mean should be rounded to 2 decimal places
        assert isinstance(result["mean_score"], float)
        assert len(str(result["mean_score"]).split('.')[-1]) <= 2


class TestAIMShortClinicalScenarios:
    """Test clinical use cases."""
    
    def test_low_emotional_reactivity_scenario(self):
        """Test patient with low emotional reactivity."""
        aim = AIMShort()
        
        # Patient reports rarely experiencing intense emotions
        answers = {}
        for i in range(1, 21):
            if i in AIMShort.REVERSE_ITEMS:
                # High agreement with calm/satisfied items
                answers[f"q{i}"] = 5
            else:
                # Low agreement with intense emotion items
                answers[f"q{i}"] = 2
        
        result = aim.calculate_score(answers)
        assert result["mean_score"] < 3.0
        assert "faible" in result["interpretation"].lower()
    
    def test_high_emotional_reactivity_scenario(self):
        """Test patient with high emotional reactivity."""
        aim = AIMShort()
        
        # Patient reports frequently experiencing intense emotions
        answers = {}
        for i in range(1, 21):
            if i in AIMShort.REVERSE_ITEMS:
                # Low agreement with calm/satisfied items
                answers[f"q{i}"] = 2
            else:
                # High agreement with intense emotion items
                answers[f"q{i}"] = 5
        
        result = aim.calculate_score(answers)
        assert result["mean_score"] > 4.0
        assert "élevée" in result["interpretation"].lower()
    
    def test_bipolar_screening_high_intensity(self):
        """Test pattern suggestive of bipolar features."""
        aim = AIMShort()
        
        # Very high intensity on happiness items, moderate on others
        answers = {
            "q1": 6, "q2": 6, "q3": 5, "q4": 4, "q5": 1,  # High exuberance, low calm
            "q6": 3, "q7": 5, "q8": 6, "q9": 6, "q10": 2,  # High energy, low calm satisfaction
            "q11": 4, "q12": 6, "q13": 2, "q14": 4, "q15": 1,  # High "top of world", low calm
            "q16": 6, "q17": 4, "q18": 1, "q19": 5, "q20": 1   # High energy, low calm/satisfaction
        }
        
        result = aim.calculate_score(answers)
        assert result["mean_score"] > 4.5
        assert result["severity"] in ["high", "very_high"]
    
    def test_depression_low_intensity(self):
        """Test pattern suggestive of depression (emotional blunting)."""
        aim = AIMShort()
        
        # Low intensity across all emotional experiences
        answers = {}
        for i in range(1, 21):
            if i in AIMShort.REVERSE_ITEMS:
                # High on calm/satisfaction (indicating lack of intensity)
                answers[f"q{i}"] = 5
            else:
                # Low on intense emotions
                answers[f"q{i}"] = 2
        
        result = aim.calculate_score(answers)
        assert result["mean_score"] < 3.0
        assert "faible" in result["category"].lower()
    
    def test_typical_functioning_scenario(self):
        """Test typical/average emotional reactivity."""
        aim = AIMShort()
        
        # Moderate scores across items
        answers = {
            "q1": 3, "q2": 3, "q3": 4, "q4": 3, "q5": 4,
            "q6": 3, "q7": 3, "q8": 3, "q9": 4, "q10": 4,
            "q11": 3, "q12": 3, "q13": 4, "q14": 3, "q15": 4,
            "q16": 3, "q17": 3, "q18": 4, "q19": 3, "q20": 4
        }
        
        result = aim.calculate_score(answers)
        assert 3.0 <= result["mean_score"] <= 4.0
        assert result["severity"] == "moderate"


class TestAIMShortSchema:
    """Test JSON schema generation."""
    
    def test_get_schema(self):
        """Test complete schema generation."""
        aim = AIMShort()
        schema = aim.get_schema()
        
        assert "instrument" in schema
        assert "sections" in schema
        assert "questions" in schema
        assert "logic" in schema
        assert "scoring" in schema
        assert "provenance" in schema
    
    def test_schema_instrument(self):
        """Test instrument section of schema."""
        aim = AIMShort()
        schema = aim.get_schema()
        
        instrument = schema["instrument"]
        assert instrument["id"] == "AIM-short.fr"
        assert instrument["abbreviation"] == "AIM-20"
        assert instrument["num_items"] == 20
    
    def test_schema_scoring(self):
        """Test scoring section of schema."""
        aim = AIMShort()
        schema = aim.get_schema()
        
        scoring = schema["scoring"]
        assert "variables" in scoring
        assert "scales" in scoring
        
        # Check reverse coding variables
        assert len(scoring["variables"]) == 6  # 6 reverse items
        
        # Check scale definition
        assert len(scoring["scales"]) == 1
        assert scoring["scales"][0]["id"] == "aim_total_mean"
        assert scoring["scales"][0]["range"] == [1, 6]
    
    def test_schema_logic(self):
        """Test logic section of schema."""
        aim = AIMShort()
        schema = aim.get_schema()
        
        logic = schema["logic"]
        assert "validators" in logic
        assert len(logic["validators"]) == 2
    
    def test_schema_provenance(self):
        """Test provenance tracking."""
        aim = AIMShort()
        schema = aim.get_schema()
        
        provenance = schema["provenance"]
        assert "created_at" in provenance
        assert "updated_at" in provenance
        assert "validated_by" in provenance
        assert "validation_date" in provenance


class TestAIMShortEdgeCases:
    """Test edge cases and error handling."""
    
    def test_empty_answers(self):
        """Test with empty answers dictionary."""
        aim = AIMShort()
        validation = aim.validate_answers({})
        
        assert validation["valid"] is False
        assert len(validation["errors"]) > 0
    
    def test_extra_items(self):
        """Test with extra items that shouldn't be there."""
        aim = AIMShort()
        answers = {f"q{i}": 3 for i in range(1, 21)}
        answers["q21"] = 4  # Extra item
        answers["extra"] = 5
        
        # Should still validate successfully (extra items ignored)
        validation = aim.validate_answers(answers)
        assert validation["valid"] is True
    
    def test_minimum_possible_mean(self):
        """Test absolute minimum possible mean score."""
        aim = AIMShort()
        
        # All direct items = 1, all reverse items = 6
        answers = {}
        for i in range(1, 21):
            if i in AIMShort.REVERSE_ITEMS:
                answers[f"q{i}"] = 6  # 7-6 = 1
            else:
                answers[f"q{i}"] = 1  # 1
        
        result = aim.calculate_score(answers)
        assert result["sum_score"] == 20
        assert result["mean_score"] == 1.0
    
    def test_maximum_possible_mean(self):
        """Test absolute maximum possible mean score."""
        aim = AIMShort()
        
        # All direct items = 6, all reverse items = 1
        answers = {}
        for i in range(1, 21):
            if i in AIMShort.REVERSE_ITEMS:
                answers[f"q{i}"] = 1  # 7-1 = 6
            else:
                answers[f"q{i}"] = 6  # 6
        
        result = aim.calculate_score(answers)
        assert result["sum_score"] == 120
        assert result["mean_score"] == 6.0
    
    def test_all_reverse_items_coding(self):
        """Test that all 6 reverse items are correctly coded."""
        aim = AIMShort()
        
        # Set all items to 3, check reverse coding
        answers = {f"q{i}": 3 for i in range(1, 21)}
        result = aim.calculate_score(answers)
        
        # Verify each reverse item
        for i in AIMShort.REVERSE_ITEMS:
            item_score = result["item_scores"][f"q{i}"]
            assert item_score["raw"] == 3
            assert item_score["scored"] == 4  # 7-3 = 4
            assert item_score["reversed"] is True
        
        # Verify direct items
        direct_items = set(range(1, 21)) - AIMShort.REVERSE_ITEMS
        for i in direct_items:
            item_score = result["item_scores"][f"q{i}"]
            assert item_score["raw"] == 3
            assert item_score["scored"] == 3
            assert item_score["reversed"] is False

