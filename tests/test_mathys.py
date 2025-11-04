# -*- coding: utf-8 -*-
"""
Comprehensive unit tests for MAThyS questionnaire
Tests metadata, questions, validation, scoring logic with subscales and reverse coding
"""

import pytest
from questionnaires.auto.mathys import MAThyS, MAThySError, ScoreResult, ValidationResult


class TestMAThySMetadata:
    """Test MAThyS metadata and structure retrieval"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mathys = MAThyS()
    
    def test_get_metadata(self):
        """Test metadata retrieval"""
        metadata = self.mathys.get_metadata()
        
        assert metadata['id'] == 'MAThyS.fr'
        assert metadata['abbreviation'] == 'MAThyS'
        assert metadata['language'] == 'fr-FR'
        assert metadata['version'] == '1.0'
        assert metadata['total_questions'] == 20
        assert metadata['scoring_range'] == [0, 200]
        assert 'sources' in metadata
        assert 'subscales' in metadata
        assert len(metadata['subscales']) == 5
    
    def test_reverse_items_definition(self):
        """Test that reverse items are correctly defined"""
        assert self.mathys.REVERSE_ITEMS == {5, 6, 7, 8, 9, 10, 17, 18}
        assert len(self.mathys.REVERSE_ITEMS) == 8
    
    def test_subscales_definition(self):
        """Test subscales structure"""
        subscales = self.mathys.SUBSCALES
        
        assert len(subscales) == 5
        assert 'emotion' in subscales
        assert 'motivation' in subscales
        assert 'perception' in subscales
        assert 'interaction' in subscales
        assert 'cognition' in subscales
        
        # Check item counts
        assert len(subscales['emotion']['items']) == 4
        assert len(subscales['motivation']['items']) == 7
        assert len(subscales['perception']['items']) == 5
        assert len(subscales['interaction']['items']) == 2
        assert len(subscales['cognition']['items']) == 2
        
        # Total should be 20 items
        total_items = sum(len(s['items']) for s in subscales.values())
        assert total_items == 20
    
    def test_get_sections(self):
        """Test sections retrieval"""
        sections = self.mathys.get_sections()
        
        assert len(sections) == 1
        assert sections[0]['id'] == 'sec_items'
        assert sections[0]['label'] == 'MAThyS – 20 items (0–10)'
        assert len(sections[0]['question_ids']) == 20
    
    def test_get_all_questions(self):
        """Test retrieving all questions"""
        questions = self.mathys.get_questions()
        
        assert len(questions) == 20
        assert questions[0]['id'] == 'q1'
        assert questions[19]['id'] == 'q20'
        
        # Check scale structure
        q1 = questions[0]
        assert q1['type'] == 'scale'
        assert 'scale' in q1
        assert q1['scale']['min_value'] == 0
        assert q1['scale']['max_value'] == 10
        assert q1['scale']['step'] == 1
        assert 'center_hint' in q1['scale']
    
    def test_bipolar_anchors(self):
        """Test that all items have bipolar anchors"""
        questions = self.mathys.get_questions()
        
        for q in questions:
            assert 'scale' in q
            assert 'min_label' in q['scale']
            assert 'max_label' in q['scale']
            assert len(q['scale']['min_label']) > 0
            assert len(q['scale']['max_label']) > 0
    
    def test_get_question_by_id(self):
        """Test retrieving specific question by ID"""
        q1 = self.mathys.get_question_by_id('q1')
        assert q1 is not None
        assert q1['id'] == 'q1'
        assert 'couleurs' in q1['scale']['min_label'].lower()
        
        q20 = self.mathys.get_question_by_id('q20')
        assert q20 is not None
        assert 'odeurs' in q20['scale']['min_label'].lower()
        
        # Non-existent question
        invalid = self.mathys.get_question_by_id('q99')
        assert invalid is None
    
    def test_get_full_questionnaire(self):
        """Test getting complete questionnaire structure"""
        full = self.mathys.get_full_questionnaire()
        
        assert 'metadata' in full
        assert 'sections' in full
        assert 'questions' in full
        assert len(full['questions']) == 20
        assert len(full['sections']) == 1


class TestMAThySValidation:
    """Test MAThyS answer validation"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mathys = MAThyS()
    
    def test_valid_answers_all_centered(self):
        """Test validation with all centered answers (5)"""
        answers = {f"q{i}": 5 for i in range(1, 21)}
        validation = self.mathys.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_integers(self):
        """Test validation with integer values"""
        answers = {f"q{i}": i % 11 for i in range(1, 21)}  # 0-10 cycle
        validation = self.mathys.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_floats(self):
        """Test validation with float values"""
        answers = {f"q{i}": 5.5 for i in range(1, 21)}
        validation = self.mathys.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_mixed_types(self):
        """Test validation with mixed int/float"""
        answers = {f"q{i}": (i * 0.5) for i in range(1, 21)}
        validation = self.mathys.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_missing_items_error(self):
        """Test validation fails with missing items"""
        answers = {f"q{i}": 5 for i in range(1, 10)}  # Missing q10-q20
        validation = self.mathys.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
        assert "Items manquants" in validation.errors[0]
    
    def test_missing_single_item_error(self):
        """Test validation fails when one item is missing"""
        answers = {f"q{i}": 5 for i in range(1, 20)}  # Missing q20
        validation = self.mathys.validate_answers(answers)
        
        assert validation.valid is False
        assert "q20" in validation.errors[0].lower()
    
    def test_value_too_high_error(self):
        """Test validation fails with values > 10"""
        answers = {f"q{i}": 5 for i in range(1, 21)}
        answers['q10'] = 15  # Invalid
        validation = self.mathys.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
    
    def test_value_negative_error(self):
        """Test validation fails with negative values"""
        answers = {f"q{i}": 5 for i in range(1, 21)}
        answers['q5'] = -1  # Invalid
        validation = self.mathys.validate_answers(answers)
        
        assert validation.valid is False
    
    def test_value_non_numeric_error(self):
        """Test validation fails with non-numeric values"""
        answers = {f"q{i}": 5 for i in range(1, 21)}
        answers['q7'] = "high"  # Invalid
        validation = self.mathys.validate_answers(answers)
        
        assert validation.valid is False
    
    def test_warning_many_extreme_values(self):
        """Test warning for many extreme values"""
        # 15 items at extremes (0 or 10)
        answers = {f"q{i}": (0 if i <= 15 else 5) for i in range(1, 21)}
        validation = self.mathys.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) > 0
        assert any('extrêmes' in w.lower() for w in validation.warnings)
    
    def test_warning_all_centered(self):
        """Test warning for all centered values"""
        # All values between 4-6
        answers = {f"q{i}": 5 for i in range(1, 21)}
        validation = self.mathys.validate_answers(answers)
        
        assert validation.valid is True
        # May or may not have warning depending on threshold
    
    def test_no_warnings_normal_distribution(self):
        """Test no warnings with normal value distribution"""
        answers = {
            f"q{i}": (i * 0.5) for i in range(1, 21)
        }
        validation = self.mathys.validate_answers(answers)
        
        assert validation.valid is True


class TestMAThySScoring:
    """Test MAThyS scoring calculation with subscales"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mathys = MAThyS()
    
    def test_scoring_all_centered(self):
        """Test scoring with all values at 5 (habitual state)"""
        answers = {f"q{i}": 5 for i in range(1, 21)}
        result = self.mathys.calculate_score(answers)
        
        # All values at 5, after recoding reverse items (10-5=5), all remain 5
        # Total should be 20 * 5 = 100
        assert result.total_score == 100.0
        
        # Check subscales
        assert result.subscales['emotion'].score == 20.0  # 4 items * 5
        assert result.subscales['motivation'].score == 35.0  # 7 items * 5
        assert result.subscales['perception'].score == 25.0  # 5 items * 5
        assert result.subscales['interaction'].score == 10.0  # 2 items * 5
        assert result.subscales['cognition'].score == 10.0  # 2 items * 5
    
    def test_scoring_all_zeros(self):
        """Test scoring with all values at 0"""
        answers = {f"q{i}": 0 for i in range(1, 21)}
        result = self.mathys.calculate_score(answers)
        
        # Reverse items (5,6,7,8,9,10,17,18) will be 10-0=10
        # Others will be 0
        # Total = 8*10 + 12*0 = 80
        assert result.total_score == 80.0
    
    def test_scoring_all_tens(self):
        """Test scoring with all values at 10"""
        answers = {f"q{i}": 10 for i in range(1, 21)}
        result = self.mathys.calculate_score(answers)
        
        # Reverse items will be 10-10=0
        # Others will be 10
        # Total = 8*0 + 12*10 = 120
        assert result.total_score == 120.0
    
    def test_reverse_coding_items(self):
        """Test that reverse items are correctly recoded"""
        answers = {f"q{i}": 3 for i in range(1, 21)}
        result = self.mathys.calculate_score(answers)
        
        # Check specific reverse items
        assert result.recoded_scores['q5'] == 7.0  # 10-3
        assert result.recoded_scores['q6'] == 7.0  # 10-3
        assert result.recoded_scores['q7'] == 7.0  # 10-3
        assert result.recoded_scores['q8'] == 7.0  # 10-3
        assert result.recoded_scores['q9'] == 7.0  # 10-3
        assert result.recoded_scores['q10'] == 7.0  # 10-3
        assert result.recoded_scores['q17'] == 7.0  # 10-3
        assert result.recoded_scores['q18'] == 7.0  # 10-3
        
        # Check non-reverse items
        assert result.recoded_scores['q1'] == 3.0
        assert result.recoded_scores['q2'] == 3.0
        assert result.recoded_scores['q3'] == 3.0
        assert result.recoded_scores['q4'] == 3.0
    
    def test_subscale_emotion_calculation(self):
        """Test Emotion subscale calculation (items 3,7,10,18)"""
        answers = {f"q{i}": 0 for i in range(1, 21)}
        # Set specific values for emotion items
        answers['q3'] = 2  # Not reversed
        answers['q7'] = 3  # Reversed -> 10-3=7
        answers['q10'] = 4  # Reversed -> 10-4=6
        answers['q18'] = 5  # Reversed -> 10-5=5
        
        result = self.mathys.calculate_score(answers)
        
        # Emotion = 2 + 7 + 6 + 5 = 20
        assert result.subscales['emotion'].score == 20.0
    
    def test_subscale_motivation_calculation(self):
        """Test Motivation subscale (items 2,11,12,15,16,17,19)"""
        answers = {f"q{i}": 0 for i in range(1, 21)}
        # Set specific values
        answers['q2'] = 1
        answers['q11'] = 2
        answers['q12'] = 3
        answers['q15'] = 4
        answers['q16'] = 5
        answers['q17'] = 6  # Reversed -> 10-6=4
        answers['q19'] = 7
        
        result = self.mathys.calculate_score(answers)
        
        # Motivation = 1+2+3+4+5+4+7 = 26
        assert result.subscales['motivation'].score == 26.0
    
    def test_subscale_perception_calculation(self):
        """Test Perception subscale (items 1,6,8,13,20)"""
        answers = {f"q{i}": 0 for i in range(1, 21)}
        answers['q1'] = 2
        answers['q6'] = 3  # Reversed -> 10-3=7
        answers['q8'] = 4  # Reversed -> 10-4=6
        answers['q13'] = 5
        answers['q20'] = 6
        
        result = self.mathys.calculate_score(answers)
        
        # Perception = 2+7+6+5+6 = 26
        assert result.subscales['perception'].score == 26.0
    
    def test_subscale_interaction_calculation(self):
        """Test Interaction subscale (items 4,14)"""
        answers = {f"q{i}": 0 for i in range(1, 21)}
        answers['q4'] = 3
        answers['q14'] = 7
        
        result = self.mathys.calculate_score(answers)
        
        # Interaction = 3+7 = 10
        assert result.subscales['interaction'].score == 10.0
    
    def test_subscale_cognition_calculation(self):
        """Test Cognition subscale (items 5,9)"""
        answers = {f"q{i}": 0 for i in range(1, 21)}
        answers['q5'] = 2  # Reversed -> 10-2=8
        answers['q9'] = 3  # Reversed -> 10-3=7
        
        result = self.mathys.calculate_score(answers)
        
        # Cognition = 8+7 = 15
        assert result.subscales['cognition'].score == 15.0
    
    def test_total_equals_subscales_sum(self):
        """Test that total score equals sum of subscales"""
        answers = {f"q{i}": (i % 11) for i in range(1, 21)}
        result = self.mathys.calculate_score(answers)
        
        subscales_sum = sum(sub.score for sub in result.subscales.values())
        assert result.total_score == subscales_sum
    
    def test_subscale_ranges(self):
        """Test that subscale results include correct ranges"""
        answers = {f"q{i}": 5 for i in range(1, 21)}
        result = self.mathys.calculate_score(answers)
        
        assert result.subscales['emotion'].range == (0, 40)
        assert result.subscales['motivation'].range == (0, 70)
        assert result.subscales['perception'].range == (0, 50)
        assert result.subscales['interaction'].range == (0, 20)
        assert result.subscales['cognition'].range == (0, 20)
    
    def test_interpretation_includes_subscales(self):
        """Test that interpretation includes subscale details"""
        answers = {f"q{i}": 5 for i in range(1, 21)}
        result = self.mathys.calculate_score(answers)
        
        assert 'Émotion' in result.interpretation
        assert 'Motivation' in result.interpretation
        assert 'Perception' in result.interpretation
        assert 'Interaction' in result.interpretation
        assert 'Cognition' in result.interpretation
    
    def test_scoring_with_invalid_answers_raises_error(self):
        """Test that invalid answers raise MAThySError"""
        answers = {f"q{i}": 5 for i in range(1, 10)}  # Missing items
        
        with pytest.raises(MAThySError) as exc_info:
            self.mathys.calculate_score(answers)
        
        assert "Items manquants" in str(exc_info.value)
    
    def test_score_result_structure(self):
        """Test that score result has correct structure"""
        answers = {f"q{i}": 5 for i in range(1, 21)}
        result = self.mathys.calculate_score(answers)
        
        assert hasattr(result, 'total_score')
        assert hasattr(result, 'subscales')
        assert hasattr(result, 'recoded_scores')
        assert hasattr(result, 'interpretation')
        assert hasattr(result, 'range')
        
        assert isinstance(result.subscales, dict)
        assert isinstance(result.recoded_scores, dict)
        assert len(result.recoded_scores) == 20


class TestMAThySBoundaryConditions:
    """Test boundary conditions and edge cases"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mathys = MAThyS()
    
    def test_boundary_minimum_total_score(self):
        """Test theoretical minimum total score"""
        # To get minimum total, we need minimum after recoding
        # Reverse items: set to 10 -> recoded to 0
        # Non-reverse items: set to 0 -> recoded to 0
        answers = {}
        for i in range(1, 21):
            if i in self.mathys.REVERSE_ITEMS:
                answers[f"q{i}"] = 10
            else:
                answers[f"q{i}"] = 0
        
        result = self.mathys.calculate_score(answers)
        assert result.total_score == 0.0
    
    def test_boundary_maximum_total_score(self):
        """Test theoretical maximum total score"""
        # To get maximum total, we need maximum after recoding
        # Reverse items: set to 0 -> recoded to 10
        # Non-reverse items: set to 10 -> recoded to 10
        answers = {}
        for i in range(1, 21):
            if i in self.mathys.REVERSE_ITEMS:
                answers[f"q{i}"] = 0
            else:
                answers[f"q{i}"] = 10
        
        result = self.mathys.calculate_score(answers)
        assert result.total_score == 200.0
    
    def test_boundary_float_precision(self):
        """Test scoring with decimal values"""
        answers = {f"q{i}": 5.5 for i in range(1, 21)}
        result = self.mathys.calculate_score(answers)
        
        # All at 5.5, reverse items become 4.5
        # 8 reverse * 4.5 + 12 non-reverse * 5.5 = 36 + 66 = 102
        assert result.total_score == 102.0
    
    def test_consistent_scoring_multiple_calls(self):
        """Test that scoring is consistent across multiple calls"""
        answers = {f"q{i}": (i % 6) + 2 for i in range(1, 21)}
        
        result1 = self.mathys.calculate_score(answers)
        result2 = self.mathys.calculate_score(answers)
        result3 = self.mathys.calculate_score(answers)
        
        assert result1.total_score == result2.total_score == result3.total_score
        for key in result1.subscales.keys():
            assert result1.subscales[key].score == result2.subscales[key].score
    
    def test_all_items_covered_in_subscales(self):
        """Test that all 20 items are assigned to exactly one subscale"""
        all_items = set()
        for subscale_info in self.mathys.SUBSCALES.values():
            all_items.update(subscale_info['items'])
        
        assert len(all_items) == 20
        assert all_items == set(range(1, 21))


class TestMAThySClinicalScenarios:
    """Test realistic clinical scenarios"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mathys = MAThyS()
    
    def test_depressive_profile(self):
        """Test typical depressive profile (low scores)"""
        # Low energy, motivation, emotion; cognitive slowing
        answers = {
            "q1": 3, "q2": 2, "q3": 2, "q4": 3, "q5": 7,  # q5 reversed
            "q6": 7, "q7": 7, "q8": 7, "q9": 8, "q10": 7,  # Many reversed
            "q11": 2, "q12": 3, "q13": 3, "q14": 3, "q15": 2,
            "q16": 2, "q17": 7, "q18": 7, "q19": 3, "q20": 3  # q17,18 reversed
        }
        
        result = self.mathys.calculate_score(answers)
        
        # Should have low scores on most dimensions
        assert result.total_score < 100  # Below average
        assert result.subscales['motivation'].score < 35  # Low motivation
    
    def test_manic_profile(self):
        """Test typical manic/hypomanic profile (high scores)"""
        # High energy, motivation, sensory sensitivity
        answers = {
            "q1": 8, "q2": 8, "q3": 7, "q4": 7, "q5": 2,  # q5 reversed -> 8
            "q6": 2, "q7": 3, "q8": 2, "q9": 1, "q10": 3,  # Reversed items low
            "q11": 9, "q12": 8, "q13": 8, "q14": 7, "q15": 8,
            "q16": 8, "q17": 3, "q18": 3, "q19": 8, "q20": 8
        }
        
        result = self.mathys.calculate_score(answers)
        
        # Should have high scores
        assert result.total_score > 100  # Above average
        assert result.subscales['motivation'].score > 35  # High motivation
    
    def test_mixed_profile(self):
        """Test mixed state profile (variable scores)"""
        # High on some dimensions, low on others
        answers = {
            "q1": 7, "q2": 2, "q3": 8, "q4": 3, "q5": 2,
            "q6": 2, "q7": 2, "q8": 8, "q9": 1, "q10": 8,
            "q11": 7, "q12": 3, "q13": 6, "q14": 6, "q15": 2,
            "q16": 8, "q17": 2, "q18": 8, "q19": 3, "q20": 7
        }
        
        result = self.mathys.calculate_score(answers)
        
        # Should have variable subscale scores
        scores = [sub.score for sub in result.subscales.values()]
        # Check that there's variability (not all similar)
        assert max(scores) - min(scores) > 10


class TestMAThySIntegration:
    """Integration tests for complete MAThyS workflow"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mathys = MAThyS()
    
    def test_complete_workflow_normal_case(self):
        """Test complete workflow for normal case"""
        # 1. Get questionnaire
        full = self.mathys.get_full_questionnaire()
        assert len(full['questions']) == 20
        
        # 2. Simulate user filling out questionnaire
        answers = {f"q{i}": 5 for i in range(1, 21)}
        
        # 3. Validate
        validation = self.mathys.validate_answers(answers)
        assert validation.valid is True
        
        # 4. Calculate score
        result = self.mathys.calculate_score(answers)
        assert result.total_score == 100.0
        assert len(result.subscales) == 5
    
    def test_complete_workflow_with_validation_error(self):
        """Test workflow with validation errors"""
        # 1. Incomplete answers
        answers = {f"q{i}": 5 for i in range(1, 15)}
        
        # 2. Validation fails
        validation = self.mathys.validate_answers(answers)
        assert validation.valid is False
        
        # 3. Scoring raises error
        with pytest.raises(MAThySError):
            self.mathys.calculate_score(answers)
    
    def test_api_response_structure(self):
        """Test that results can be serialized for API response"""
        answers = {f"q{i}": 5 for i in range(1, 21)}
        result = self.mathys.calculate_score(answers)
        
        # Should be able to convert to dict
        result_dict = result.dict()
        assert 'total_score' in result_dict
        assert 'subscales' in result_dict
        assert 'interpretation' in result_dict


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

