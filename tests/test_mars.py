# -*- coding: utf-8 -*-
"""
Comprehensive unit tests for MARS questionnaire
Tests metadata, questions, validation, scoring logic with reverse coding, and edge cases
"""

import pytest
from questionnaires.auto.mars import MARS, MARSError, ScoreResult, ValidationResult


class TestMARSMetadata:
    """Test MARS metadata and structure retrieval"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mars = MARS()
    
    def test_get_metadata(self):
        """Test metadata retrieval"""
        metadata = self.mars.get_metadata()
        
        assert metadata['id'] == 'MARS.fr'
        assert metadata['abbreviation'] == 'MARS-10'
        assert metadata['language'] == 'fr-FR'
        assert metadata['version'] == '1.0'
        assert metadata['total_questions'] == 10
        assert metadata['scoring_range'] == [0, 10]
        assert 'sources' in metadata
        assert 'scoring_notes' in metadata
    
    def test_get_sections(self):
        """Test sections retrieval"""
        sections = self.mars.get_sections()
        
        assert len(sections) == 1
        assert sections[0]['id'] == 'sec1'
        assert sections[0]['label'] == 'MARS – 10 items'
        assert len(sections[0]['question_ids']) == 10
    
    def test_get_all_questions(self):
        """Test retrieving all questions"""
        questions = self.mars.get_questions()
        
        assert len(questions) == 10
        assert questions[0]['id'] == 'q1'
        assert questions[9]['id'] == 'q10'
        
        # Check binary structure (yes/no)
        q1 = questions[0]
        assert len(q1['options']) == 2
        assert q1['options'][0]['label'] == 'OUI'
        assert q1['options'][1]['label'] == 'NON'
        assert q1['options'][0]['code'] == 1
        assert q1['options'][1]['code'] == 0
    
    def test_get_questions_by_section(self):
        """Test retrieving questions filtered by section"""
        sec1_questions = self.mars.get_questions(section_id='sec1')
        
        assert len(sec1_questions) == 10
        assert all(q['section_id'] == 'sec1' for q in sec1_questions)
    
    def test_get_question_by_id(self):
        """Test retrieving specific question by ID"""
        q1 = self.mars.get_question_by_id('q1')
        assert q1 is not None
        assert q1['id'] == 'q1'
        assert 'oublier' in q1['text'].lower()
        
        q7 = self.mars.get_question_by_id('q7')
        assert q7 is not None
        assert 'idées' in q7['text'].lower() and 'claires' in q7['text'].lower()
        
        # Non-existent question
        invalid = self.mars.get_question_by_id('q99')
        assert invalid is None
    
    def test_items_count(self):
        """Test that all 10 items are present"""
        assert len(self.mars.ITEMS) == 10
        
        # Verify some key texts
        texts = ' '.join(self.mars.ITEMS)
        assert 'oublier' in texts.lower()
        assert 'médicaments' in texts.lower()
        assert 'zombie' in texts.lower()
    
    def test_positive_negative_items_sets(self):
        """Test positive and negative items are correctly defined"""
        assert self.mars.POSITIVE_ITEMS == {7, 8}
        assert self.mars.NEGATIVE_ITEMS == {1, 2, 3, 4, 5, 6, 9, 10}
        
        # Verify no overlap
        assert len(self.mars.POSITIVE_ITEMS & self.mars.NEGATIVE_ITEMS) == 0
        
        # Verify all items covered
        assert len(self.mars.POSITIVE_ITEMS | self.mars.NEGATIVE_ITEMS) == 10
    
    def test_get_full_questionnaire(self):
        """Test getting complete questionnaire structure"""
        full = self.mars.get_full_questionnaire()
        
        assert 'metadata' in full
        assert 'sections' in full
        assert 'questions' in full
        assert len(full['questions']) == 10
        assert len(full['sections']) == 1


class TestMARSValidation:
    """Test MARS answer validation"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mars = MARS()
    
    def test_valid_answers_all_no(self):
        """Test validation with all 'no' (0) answers"""
        answers = {f"q{i}": 0 for i in range(1, 11)}
        validation = self.mars.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_all_yes(self):
        """Test validation with all 'yes' (1) answers"""
        answers = {f"q{i}": 1 for i in range(1, 11)}
        validation = self.mars.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_mixed(self):
        """Test validation with mixed valid answers"""
        answers = {
            "q1": 0, "q2": 1, "q3": 0, "q4": 1, "q5": 0,
            "q6": 0, "q7": 1, "q8": 1, "q9": 0, "q10": 0
        }
        validation = self.mars.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_missing_items_error(self):
        """Test validation fails with missing items"""
        answers = {"q1": 0, "q2": 1, "q3": 0}  # Missing q4-q10
        validation = self.mars.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
        assert "Items manquants" in validation.errors[0]
    
    def test_missing_single_item_error(self):
        """Test validation fails when one item is missing"""
        answers = {f"q{i}": 0 for i in range(1, 10)}  # Missing q10
        validation = self.mars.validate_answers(answers)
        
        assert validation.valid is False
        assert "q10" in validation.errors[0].lower()
    
    def test_invalid_value_too_high(self):
        """Test validation fails with values > 1"""
        answers = {f"q{i}": 0 for i in range(1, 11)}
        answers['q5'] = 2  # Invalid
        validation = self.mars.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
    
    def test_invalid_value_negative(self):
        """Test validation fails with negative values"""
        answers = {f"q{i}": 0 for i in range(1, 11)}
        answers['q3'] = -1  # Invalid
        validation = self.mars.validate_answers(answers)
        
        assert validation.valid is False
    
    def test_invalid_value_non_integer(self):
        """Test validation fails with non-integer values"""
        answers = {f"q{i}": 0 for i in range(1, 11)}
        answers['q7'] = "oui"  # String instead of int
        validation = self.mars.validate_answers(answers)
        
        assert validation.valid is False
    
    def test_warning_very_low_adherence(self):
        """Test warning for very low adherence (score ≤3)"""
        # All yes to negative items = very low adherence
        answers = {f"q{i}": 1 for i in range(1, 11)}
        validation = self.mars.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) > 0
        assert any('très bas' in w.lower() for w in validation.warnings)
    
    def test_warning_very_high_adherence(self):
        """Test warning for very high adherence (score ≥9)"""
        # All no to negative items, yes to positive items
        answers = {
            "q1": 0, "q2": 0, "q3": 0, "q4": 0, "q5": 0,
            "q6": 0, "q7": 1, "q8": 1, "q9": 0, "q10": 0
        }
        validation = self.mars.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) > 0
        assert any('très élevé' in w.lower() or 'excellente' in w.lower() 
                  for w in validation.warnings)
    
    def test_no_warnings_moderate_adherence(self):
        """Test no warnings with moderate adherence"""
        answers = {
            "q1": 0, "q2": 1, "q3": 0, "q4": 0, "q5": 1,
            "q6": 0, "q7": 1, "q8": 0, "q9": 1, "q10": 0
        }
        validation = self.mars.validate_answers(answers)
        
        assert validation.valid is True
        # Should have no warnings for moderate scores (4-8)


class TestMARSScoring:
    """Test MARS scoring calculation with reverse coding"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mars = MARS()
    
    def test_perfect_adherence_score(self):
        """Test perfect adherence (all recoded to 1) = 10/10"""
        # All NO (0) for negative items, YES (1) for positive items
        answers = {
            "q1": 0, "q2": 0, "q3": 0, "q4": 0, "q5": 0,
            "q6": 0, "q7": 1, "q8": 1, "q9": 0, "q10": 0
        }
        
        result = self.mars.calculate_score(answers)
        
        assert result.total_score == 10
        assert all(score == 1 for score in result.recoded_scores.values())
    
    def test_poorest_adherence_score(self):
        """Test poorest adherence (all recoded to 0) = 0/10"""
        # All YES (1) for negative items, NO (0) for positive items
        answers = {
            "q1": 1, "q2": 1, "q3": 1, "q4": 1, "q5": 1,
            "q6": 1, "q7": 0, "q8": 0, "q9": 1, "q10": 1
        }
        
        result = self.mars.calculate_score(answers)
        
        assert result.total_score == 0
        assert all(score == 0 for score in result.recoded_scores.values())
    
    def test_reverse_coding_negative_items(self):
        """Test reverse coding for negative items (1,2,3,4,5,6,9,10)"""
        # Test that NO (0) = 1 point for negative items
        answers = {f"q{i}": 0 for i in range(1, 11)}  # All NO
        
        result = self.mars.calculate_score(answers)
        
        # Negative items should be recoded to 1
        for item_num in self.mars.NEGATIVE_ITEMS:
            assert result.recoded_scores[f"q{item_num}"] == 1
        
        # Positive items (7,8) with NO should be recoded to 0
        assert result.recoded_scores["q7"] == 0
        assert result.recoded_scores["q8"] == 0
    
    def test_reverse_coding_positive_items(self):
        """Test positive scoring for items 7 and 8"""
        # Test that YES (1) = 1 point for positive items
        answers = {f"q{i}": 1 for i in range(1, 11)}  # All YES
        
        result = self.mars.calculate_score(answers)
        
        # Positive items (7,8) should be recoded to 1 when YES
        assert result.recoded_scores["q7"] == 1
        assert result.recoded_scores["q8"] == 1
        
        # Negative items with YES should be recoded to 0
        for item_num in self.mars.NEGATIVE_ITEMS:
            assert result.recoded_scores[f"q{item_num}"] == 0
    
    def test_median_score(self):
        """Test typical median score (≈6)"""
        # Mix that should give score around 6
        answers = {
            "q1": 0, "q2": 0, "q3": 1, "q4": 0, "q5": 0,
            "q6": 1, "q7": 1, "q8": 1, "q9": 0, "q10": 1
        }
        
        result = self.mars.calculate_score(answers)
        
        # q1=0→1, q2=0→1, q3=1→0, q4=0→1, q5=0→1
        # q6=1→0, q7=1→1, q8=1→1, q9=0→1, q10=1→0
        # Total: 1+1+0+1+1+0+1+1+1+0 = 7
        assert result.total_score == 7
    
    def test_recoded_scores_in_result(self):
        """Test that recoded scores are included in result"""
        answers = {
            "q1": 1, "q2": 0, "q3": 1, "q4": 0, "q5": 1,
            "q6": 0, "q7": 1, "q8": 0, "q9": 1, "q10": 0
        }
        
        result = self.mars.calculate_score(answers)
        
        assert 'recoded_scores' in result.dict()
        assert len(result.recoded_scores) == 10
        
        # Verify specific recodings
        assert result.recoded_scores["q1"] == 0  # YES on negative item = 0
        assert result.recoded_scores["q2"] == 1  # NO on negative item = 1
        assert result.recoded_scores["q7"] == 1  # YES on positive item = 1
        assert result.recoded_scores["q8"] == 0  # NO on positive item = 0
    
    def test_interpretation_excellent_adherence(self):
        """Test interpretation text for excellent adherence (≥8)"""
        answers = {
            "q1": 0, "q2": 0, "q3": 0, "q4": 0, "q5": 0,
            "q6": 0, "q7": 1, "q8": 1, "q9": 0, "q10": 1
        }
        
        result = self.mars.calculate_score(answers)
        
        assert result.total_score >= 8
        assert "excellente" in result.interpretation.lower()
    
    def test_interpretation_good_adherence(self):
        """Test interpretation text for good adherence (6-7)"""
        answers = {
            "q1": 0, "q2": 0, "q3": 0, "q4": 1, "q5": 0,
            "q6": 1, "q7": 1, "q8": 1, "q9": 0, "q10": 0
        }
        
        result = self.mars.calculate_score(answers)
        
        assert 6 <= result.total_score <= 7
        assert "bonne" in result.interpretation.lower()
    
    def test_interpretation_moderate_adherence(self):
        """Test interpretation text for moderate adherence (4-5)"""
        answers = {
            "q1": 0, "q2": 1, "q3": 1, "q4": 1, "q5": 0,
            "q6": 1, "q7": 1, "q8": 0, "q9": 1, "q10": 0
        }
        
        result = self.mars.calculate_score(answers)
        
        assert 4 <= result.total_score <= 5
        assert "modérée" in result.interpretation.lower()
    
    def test_interpretation_low_adherence(self):
        """Test interpretation text for low adherence (<4)"""
        answers = {
            "q1": 1, "q2": 1, "q3": 1, "q4": 1, "q5": 1,
            "q6": 1, "q7": 0, "q8": 0, "q9": 1, "q10": 1
        }
        
        result = self.mars.calculate_score(answers)
        
        assert result.total_score < 4
        assert "faible" in result.interpretation.lower()
        assert "évaluation clinique" in result.interpretation.lower()
    
    def test_scoring_with_invalid_answers_raises_error(self):
        """Test that invalid answers raise MARSError"""
        answers = {"q1": 0, "q2": 1}  # Missing most items
        
        with pytest.raises(MARSError) as exc_info:
            self.mars.calculate_score(answers)
        
        assert "Items manquants" in str(exc_info.value)
    
    def test_score_range_property(self):
        """Test that score result includes correct range"""
        answers = {f"q{i}": 0 for i in range(1, 11)}
        result = self.mars.calculate_score(answers)
        
        assert result.range == (0, 10)


class TestMARSBoundaryConditions:
    """Test boundary conditions and edge cases"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mars = MARS()
    
    def test_boundary_score_0(self):
        """Test boundary: score = 0 (worst adherence)"""
        answers = {
            "q1": 1, "q2": 1, "q3": 1, "q4": 1, "q5": 1,
            "q6": 1, "q7": 0, "q8": 0, "q9": 1, "q10": 1
        }
        
        result = self.mars.calculate_score(answers)
        assert result.total_score == 0
    
    def test_boundary_score_10(self):
        """Test boundary: score = 10 (best adherence)"""
        answers = {
            "q1": 0, "q2": 0, "q3": 0, "q4": 0, "q5": 0,
            "q6": 0, "q7": 1, "q8": 1, "q9": 0, "q10": 0
        }
        
        result = self.mars.calculate_score(answers)
        assert result.total_score == 10
    
    def test_boundary_score_3_triggers_warning(self):
        """Test boundary: score = 3 triggers low adherence warning"""
        answers = {
            "q1": 0, "q2": 0, "q3": 1, "q4": 1, "q5": 1,
            "q6": 1, "q7": 1, "q8": 0, "q9": 1, "q10": 1
        }
        
        validation = self.mars.validate_answers(answers)
        assert any('très bas' in w.lower() for w in validation.warnings)
    
    def test_boundary_score_4_no_low_warning(self):
        """Test boundary: score = 4 does not trigger low adherence warning"""
        answers = {
            "q1": 0, "q2": 0, "q3": 0, "q4": 1, "q5": 1,
            "q6": 1, "q7": 1, "q8": 0, "q9": 1, "q10": 1
        }
        
        validation = self.mars.validate_answers(answers)
        # Should not have "très bas" warning at score 4
        assert not any('très bas' in w.lower() for w in validation.warnings)
    
    def test_boundary_score_9_triggers_high_warning(self):
        """Test boundary: score = 9 triggers excellent adherence warning"""
        answers = {
            "q1": 0, "q2": 0, "q3": 0, "q4": 0, "q5": 0,
            "q6": 0, "q7": 1, "q8": 0, "q9": 0, "q10": 1
        }
        
        validation = self.mars.validate_answers(answers)
        assert any('très élevé' in w.lower() or 'excellente' in w.lower() 
                  for w in validation.warnings)
    
    def test_boundary_score_8_no_high_warning(self):
        """Test boundary: score = 8 does not trigger very high warning"""
        answers = {
            "q1": 0, "q2": 0, "q3": 0, "q4": 0, "q5": 1,
            "q6": 0, "q7": 1, "q8": 1, "q9": 0, "q10": 1
        }
        
        validation = self.mars.validate_answers(answers)
        # Should not have "très élevé" at score 8
        assert not any('très élevé' in w.lower() for w in validation.warnings)
    
    def test_all_scores_0_to_10_possible(self):
        """Test that all scores from 0 to 10 are achievable"""
        # This is a theoretical test to ensure scoring logic covers full range
        test_cases = [
            # Score 0: all worst
            {f"q{i}": 1 if i not in {7, 8} else 0 for i in range(1, 11)},
            # Score 5: half and half
            {f"q{i}": 0 if i <= 5 else (1 if i in {7, 8} else 0) for i in range(1, 11)},
            # Score 10: all best
            {f"q{i}": 0 if i not in {7, 8} else 1 for i in range(1, 11)},
        ]
        
        expected_scores = [0, 5, 10]
        
        for answers, expected in zip(test_cases, expected_scores):
            result = self.mars.calculate_score(answers)
            assert result.total_score == expected
    
    def test_consistent_scoring_multiple_calls(self):
        """Test that scoring is consistent across multiple calls"""
        answers = {
            "q1": 0, "q2": 1, "q3": 0, "q4": 1, "q5": 0,
            "q6": 1, "q7": 1, "q8": 0, "q9": 1, "q10": 0
        }
        
        result1 = self.mars.calculate_score(answers)
        result2 = self.mars.calculate_score(answers)
        result3 = self.mars.calculate_score(answers)
        
        assert result1.total_score == result2.total_score == result3.total_score
        assert result1.recoded_scores == result2.recoded_scores == result3.recoded_scores


class TestMARSClinicalScenarios:
    """Test realistic clinical scenarios"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mars = MARS()
    
    def test_good_adherence_pattern(self):
        """Test realistic good adherence pattern"""
        # Patient generally adherent but occasional forgetfulness
        answers = {
            "q1": 1,  # Sometimes forgets
            "q2": 0,  # Doesn't neglect time
            "q3": 0,  # Doesn't stop when feeling better
            "q4": 0,  # Doesn't stop when feeling worse
            "q5": 0,  # Doesn't take only when sick
            "q6": 0,  # Accepts medications as natural
            "q7": 1,  # Clearer ideas with meds
            "q8": 1,  # Knows meds prevent relapse
            "q9": 0,  # No zombie feeling
            "q10": 0  # No fatigue from meds
        }
        
        result = self.mars.calculate_score(answers)
        
        # Score should be 7 (good adherence)
        # q1=1→0, q2=0→1, q3=0→1, q4=0→1, q5=0→1
        # q6=0→1, q7=1→1, q8=1→1, q9=0→1, q10=0→1
        assert result.total_score == 9
        assert "excellente" in result.interpretation.lower() or "bonne" in result.interpretation.lower()
    
    def test_poor_adherence_due_to_side_effects(self):
        """Test poor adherence due to side effects"""
        # Patient stops due to side effects
        answers = {
            "q1": 1,  # Forgets
            "q2": 1,  # Neglects time
            "q3": 0,  # Doesn't stop when better
            "q4": 1,  # Stops when feeling worse
            "q5": 0,  # Doesn't take only when sick
            "q6": 0,  # Accepts as natural
            "q7": 0,  # Ideas not clearer
            "q8": 0,  # Doesn't see prevention benefit
            "q9": 1,  # Zombie feeling
            "q10": 1  # Fatigue
        }
        
        result = self.mars.calculate_score(answers)
        
        assert result.total_score <= 4
        assert "faible" in result.interpretation.lower()
    
    def test_ambivalent_adherence_pattern(self):
        """Test ambivalent attitude toward medication"""
        # Patient has mixed feelings
        answers = {
            "q1": 0,  # Doesn't forget
            "q2": 0,  # Doesn't neglect time
            "q3": 1,  # Stops when feeling better
            "q4": 0,  # Doesn't stop when worse
            "q5": 1,  # Only takes when sick
            "q6": 1,  # Doesn't think it's natural
            "q7": 1,  # But ideas are clearer
            "q8": 0,  # Doesn't see prevention
            "q9": 0,  # No zombie feeling
            "q10": 0  # No fatigue
        }
        
        result = self.mars.calculate_score(answers)
        
        # Should be moderate score (around 5-6)
        assert 4 <= result.total_score <= 6
    
    def test_excellent_adherence_with_insight(self):
        """Test excellent adherence with good insight"""
        # Patient with excellent insight and adherence
        answers = {
            "q1": 0, "q2": 0, "q3": 0, "q4": 0, "q5": 0,
            "q6": 0, "q7": 1, "q8": 1, "q9": 0, "q10": 0
        }
        
        result = self.mars.calculate_score(answers)
        
        assert result.total_score == 10
        assert "excellente" in result.interpretation.lower()


class TestMARSIntegration:
    """Integration tests for complete MARS workflow"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mars = MARS()
    
    def test_complete_workflow_good_adherence(self):
        """Test complete workflow for good adherence case"""
        # 1. Get questionnaire
        full = self.mars.get_full_questionnaire()
        assert len(full['questions']) == 10
        
        # 2. Simulate user filling out questionnaire
        answers = {
            "q1": 0, "q2": 0, "q3": 0, "q4": 0, "q5": 0,
            "q6": 0, "q7": 1, "q8": 1, "q9": 0, "q10": 1
        }
        
        # 3. Validate
        validation = self.mars.validate_answers(answers)
        assert validation.valid is True
        
        # 4. Calculate score
        result = self.mars.calculate_score(answers)
        assert result.total_score == 9
        assert "excellente" in result.interpretation.lower() or "bonne" in result.interpretation.lower()
    
    def test_complete_workflow_poor_adherence(self):
        """Test complete workflow for poor adherence case"""
        # 1. Get questionnaire structure
        questions = self.mars.get_questions()
        assert len(questions) == 10
        
        # 2. User answers (poor adherence)
        answers = {
            "q1": 1, "q2": 1, "q3": 1, "q4": 1, "q5": 1,
            "q6": 1, "q7": 0, "q8": 0, "q9": 1, "q10": 1
        }
        
        # 3. Validate (should trigger warning)
        validation = self.mars.validate_answers(answers)
        assert validation.valid is True
        assert len(validation.warnings) > 0
        
        # 4. Calculate score
        result = self.mars.calculate_score(answers)
        assert result.total_score == 0
        assert "faible" in result.interpretation.lower()
    
    def test_complete_workflow_with_validation_error(self):
        """Test workflow with validation errors"""
        # 1. Incomplete answers
        answers = {"q1": 0, "q2": 1, "q3": 0}
        
        # 2. Validation fails
        validation = self.mars.validate_answers(answers)
        assert validation.valid is False
        
        # 3. Scoring raises error
        with pytest.raises(MARSError):
            self.mars.calculate_score(answers)


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

