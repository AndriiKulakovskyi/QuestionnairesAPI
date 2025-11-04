# -*- coding: utf-8 -*-
"""
Comprehensive unit tests for ASRM questionnaire
Tests metadata, questions, validation, scoring logic, and edge cases
"""

import pytest
from questionnaires.asrm import ASRM, ASRMError, ScoreResult, ValidationResult


class TestASRMMetadata:
    """Test ASRM metadata and structure retrieval"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.asrm = ASRM()
    
    def test_get_metadata(self):
        """Test metadata retrieval"""
        metadata = self.asrm.get_metadata()
        
        assert metadata['id'] == 'ASRM.fr'
        assert metadata['abbreviation'] == 'ASRM'
        assert metadata['language'] == 'fr-FR'
        assert metadata['version'] == '1.0'
        assert metadata['reference_period'] == '7 derniers jours'
        assert metadata['total_questions'] == 5
        assert metadata['scoring_range'] == [0, 20]
        assert metadata['cutoff'] == 6
        assert 'sources' in metadata
        assert len(metadata['sources']) > 0
    
    def test_get_sections(self):
        """Test sections retrieval"""
        sections = self.asrm.get_sections()
        
        assert len(sections) == 1
        assert sections[0]['id'] == 'sec1'
        assert sections[0]['label'] == 'ASRM – 5 items'
        assert len(sections[0]['question_ids']) == 5
    
    def test_get_all_questions(self):
        """Test retrieving all questions"""
        questions = self.asrm.get_questions()
        
        assert len(questions) == 5
        assert questions[0]['id'] == 'q1'
        assert questions[4]['id'] == 'q5'
        
        # Check question structure
        q1 = questions[0]
        assert 'id' in q1
        assert 'section_id' in q1
        assert 'text' in q1
        assert 'type' in q1
        assert 'required' in q1
        assert 'options' in q1
        assert 'constraints' in q1
        assert len(q1['options']) == 5  # 0-4 scale
    
    def test_question_options_structure(self):
        """Test that each question has 5 options (0-4)"""
        questions = self.asrm.get_questions()
        
        for q in questions:
            assert len(q['options']) == 5
            codes = [opt['code'] for opt in q['options']]
            scores = [opt['score'] for opt in q['options']]
            assert codes == [0, 1, 2, 3, 4]
            assert scores == [0, 1, 2, 3, 4]
            # Check all options have labels
            for opt in q['options']:
                assert 'label' in opt
                assert len(opt['label']) > 0
    
    def test_get_question_by_id(self):
        """Test retrieving specific question by ID"""
        q1 = self.asrm.get_question_by_id('q1')
        assert q1 is not None
        assert q1['id'] == 'q1'
        assert 'Humeur' in q1['text'] or 'Question 1' in q1['text']
        
        q5 = self.asrm.get_question_by_id('q5')
        assert q5 is not None
        assert q5['id'] == 'q5'
        
        # Non-existent question
        invalid = self.asrm.get_question_by_id('q99')
        assert invalid is None
    
    def test_get_full_questionnaire(self):
        """Test getting complete questionnaire structure"""
        full = self.asrm.get_full_questionnaire()
        
        assert 'metadata' in full
        assert 'sections' in full
        assert 'questions' in full
        assert len(full['questions']) == 5
        assert len(full['sections']) == 1
    
    def test_items_text_content(self):
        """Test that item texts are in French and make sense"""
        questions = self.asrm.get_questions()
        
        # Q1 should mention happiness/joy
        q1_text = ' '.join([opt['label'] for opt in questions[0]['options']])
        assert 'heureux' in q1_text.lower() or 'joyeux' in q1_text.lower()
        
        # Q2 should mention confidence
        q2_text = ' '.join([opt['label'] for opt in questions[1]['options']])
        assert 'sûr' in q2_text.lower()
        
        # Q3 should mention sleep
        q3_text = ' '.join([opt['label'] for opt in questions[2]['options']])
        assert 'sommeil' in q3_text.lower() or 'dormir' in q3_text.lower()
        
        # Q4 should mention talking
        q4_text = ' '.join([opt['label'] for opt in questions[3]['options']])
        assert 'parle' in q4_text.lower()
        
        # Q5 should mention activity
        q5_text = ' '.join([opt['label'] for opt in questions[4]['options']])
        assert 'actif' in q5_text.lower()


class TestASRMValidation:
    """Test ASRM answer validation"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.asrm = ASRM()
    
    def test_valid_answers_all_zeros(self):
        """Test validation with all zero answers"""
        answers = {f"q{i}": 0 for i in range(1, 6)}
        validation = self.asrm.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_all_fours(self):
        """Test validation with all maximum answers"""
        answers = {f"q{i}": 4 for i in range(1, 6)}
        validation = self.asrm.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_mixed(self):
        """Test validation with mixed valid answers"""
        answers = {"q1": 0, "q2": 1, "q3": 2, "q4": 3, "q5": 4}
        validation = self.asrm.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_missing_items_error(self):
        """Test validation fails with missing items"""
        answers = {"q1": 0, "q2": 1}  # Only 2 items
        validation = self.asrm.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
        assert "Items manquants" in validation.errors[0]
    
    def test_invalid_value_too_high(self):
        """Test validation fails with values > 4"""
        answers = {f"q{i}": 0 for i in range(1, 6)}
        answers['q3'] = 5  # Invalid value
        validation = self.asrm.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
        assert "Valeurs invalides" in validation.errors[0]
    
    def test_invalid_value_negative(self):
        """Test validation fails with negative values"""
        answers = {f"q{i}": 0 for i in range(1, 6)}
        answers['q2'] = -1  # Invalid value
        validation = self.asrm.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
    
    def test_invalid_value_non_integer(self):
        """Test validation fails with non-integer values"""
        answers = {f"q{i}": 0 for i in range(1, 6)}
        answers['q4'] = "2"  # String instead of int
        validation = self.asrm.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
    
    def test_warning_multiple_max_scores(self):
        """Test warning when 3+ items at maximum score"""
        answers = {"q1": 4, "q2": 4, "q3": 4, "q4": 2, "q5": 1}
        validation = self.asrm.validate_answers(answers)
        
        assert validation.valid is True  # Still valid
        assert len(validation.warnings) > 0
        assert any('sévère' in w.lower() for w in validation.warnings)
    
    def test_no_warning_with_two_max_scores(self):
        """Test no warning with only 2 items at maximum"""
        answers = {"q1": 4, "q2": 4, "q3": 2, "q4": 1, "q5": 0}
        validation = self.asrm.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) == 0


class TestASRMScoring:
    """Test ASRM scoring calculation"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.asrm = ASRM()
    
    def test_score_minimum(self):
        """Test scoring with minimum score (0)"""
        answers = {f"q{i}": 0 for i in range(1, 6)}
        result = self.asrm.calculate_score(answers)
        
        assert result.total_score == 0
        assert result.probability == "Probabilité faible d'épisode maniaque/hypomaniaque"
        assert "sous le seuil" in result.interpretation.lower()
    
    def test_score_maximum(self):
        """Test scoring with maximum score (20)"""
        answers = {f"q{i}": 4 for i in range(1, 6)}
        result = self.asrm.calculate_score(answers)
        
        assert result.total_score == 20
        assert result.probability == "Probabilité élevée d'épisode maniaque/hypomaniaque"
        assert "très élevé" in result.interpretation.lower()
    
    def test_score_just_below_cutoff(self):
        """Test scoring just below cutoff (score 5)"""
        answers = {"q1": 1, "q2": 1, "q3": 1, "q4": 1, "q5": 1}
        result = self.asrm.calculate_score(answers)
        
        assert result.total_score == 5
        assert result.probability == "Probabilité faible d'épisode maniaque/hypomaniaque"
    
    def test_score_at_cutoff(self):
        """Test scoring at cutoff (score 6)"""
        answers = {"q1": 2, "q2": 1, "q3": 1, "q4": 1, "q5": 1}
        result = self.asrm.calculate_score(answers)
        
        assert result.total_score == 6
        assert result.probability == "Probabilité élevée d'épisode maniaque/hypomaniaque"
    
    def test_score_moderate_high(self):
        """Test scoring in moderate high range (7-11)"""
        answers = {"q1": 2, "q2": 2, "q3": 2, "q4": 1, "q5": 2}
        result = self.asrm.calculate_score(answers)
        
        assert result.total_score == 9
        assert result.probability == "Probabilité élevée d'épisode maniaque/hypomaniaque"
        assert "élevé" in result.interpretation.lower()
    
    def test_score_very_high(self):
        """Test scoring in very high range (12+)"""
        answers = {"q1": 3, "q2": 3, "q3": 3, "q4": 2, "q5": 2}
        result = self.asrm.calculate_score(answers)
        
        assert result.total_score == 13
        assert result.probability == "Probabilité élevée d'épisode maniaque/hypomaniaque"
        assert "très élevé" in result.interpretation.lower()
    
    def test_score_calculation_accuracy(self):
        """Test that scoring is simple sum (no domains)"""
        answers = {"q1": 1, "q2": 2, "q3": 3, "q4": 4, "q5": 0}
        result = self.asrm.calculate_score(answers)
        
        # Should be simple sum: 1 + 2 + 3 + 4 + 0 = 10
        assert result.total_score == 10
    
    def test_score_range_in_result(self):
        """Test that result includes valid score range"""
        answers = {f"q{i}": 0 for i in range(1, 6)}
        result = self.asrm.calculate_score(answers)
        
        assert result.range == (0, 20)
    
    def test_score_with_invalid_answers_raises_error(self):
        """Test that invalid answers raise ASRMError"""
        answers = {"q1": 0, "q2": 1}  # Missing items
        
        with pytest.raises(ASRMError) as exc_info:
            self.asrm.calculate_score(answers)
        
        assert "Items manquants" in str(exc_info.value)
    
    def test_interpretation_includes_recommendation(self):
        """Test that high scores include clinical recommendation"""
        answers = {"q1": 3, "q2": 2, "q3": 2, "q4": 2, "q5": 2}
        result = self.asrm.calculate_score(answers)
        
        assert result.total_score == 11
        assert "évaluation clinique" in result.interpretation.lower()
    
    def test_interpretation_for_low_score(self):
        """Test interpretation for low scores"""
        answers = {"q1": 1, "q2": 0, "q3": 0, "q4": 1, "q5": 0}
        result = self.asrm.calculate_score(answers)
        
        assert result.total_score == 2
        assert "sous le seuil" in result.interpretation.lower()


class TestASRMBoundaryConditions:
    """Test boundary conditions and edge cases"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.asrm = ASRM()
    
    def test_boundary_score_5_vs_6(self):
        """Test boundary between low and high probability"""
        # Score 5 - below cutoff
        answers = {"q1": 1, "q2": 1, "q3": 1, "q4": 1, "q5": 1}
        result = self.asrm.calculate_score(answers)
        assert result.total_score == 5
        assert "faible" in result.probability.lower()
        
        # Score 6 - at cutoff
        answers['q1'] = 2
        result = self.asrm.calculate_score(answers)
        assert result.total_score == 6
        assert "élevée" in result.probability.lower()
    
    def test_cutoff_constant(self):
        """Test that cutoff is correctly defined"""
        assert self.asrm.CUTOFF_HIGH_PROBABILITY == 6
    
    def test_all_items_at_same_level(self):
        """Test when all items have same score"""
        for score in range(5):
            answers = {f"q{i}": score for i in range(1, 6)}
            result = self.asrm.calculate_score(answers)
            assert result.total_score == score * 5
    
    def test_single_item_variations(self):
        """Test score changes with single item variation"""
        base_answers = {"q1": 1, "q2": 1, "q3": 1, "q4": 1, "q5": 1}
        base_result = self.asrm.calculate_score(base_answers)
        base_score = base_result.total_score
        
        # Change one item
        answers = base_answers.copy()
        answers['q3'] = 2
        result = self.asrm.calculate_score(answers)
        assert result.total_score == base_score + 1
    
    def test_consistent_scoring_multiple_calls(self):
        """Test that scoring is consistent across multiple calls"""
        answers = {"q1": 2, "q2": 3, "q3": 1, "q4": 2, "q5": 3}
        
        result1 = self.asrm.calculate_score(answers)
        result2 = self.asrm.calculate_score(answers)
        result3 = self.asrm.calculate_score(answers)
        
        assert result1.total_score == result2.total_score == result3.total_score
        assert result1.probability == result2.probability == result3.probability


class TestASRMSpecialCases:
    """Test special cases and clinical scenarios"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.asrm = ASRM()
    
    def test_mild_manic_symptoms(self):
        """Test mild manic symptoms pattern"""
        answers = {"q1": 2, "q2": 1, "q3": 1, "q4": 1, "q5": 1}
        result = self.asrm.calculate_score(answers)
        
        assert result.total_score == 6
        assert "élevée" in result.probability.lower()
    
    def test_moderate_manic_symptoms(self):
        """Test moderate manic symptoms pattern"""
        answers = {"q1": 2, "q2": 2, "q3": 2, "q4": 2, "q5": 2}
        result = self.asrm.calculate_score(answers)
        
        assert result.total_score == 10
        assert "élevée" in result.probability.lower()
    
    def test_severe_manic_symptoms(self):
        """Test severe manic symptoms pattern"""
        answers = {"q1": 4, "q2": 4, "q3": 3, "q4": 4, "q5": 3}
        result = self.asrm.calculate_score(answers)
        
        assert result.total_score == 18
        assert "très élevé" in result.interpretation.lower()
    
    def test_isolated_symptom_pattern(self):
        """Test pattern with one or two isolated symptoms"""
        # Only elevated mood
        answers = {"q1": 3, "q2": 0, "q3": 0, "q4": 0, "q5": 0}
        result = self.asrm.calculate_score(answers)
        
        assert result.total_score == 3
        assert "faible" in result.probability.lower()
    
    def test_mixed_severity_pattern(self):
        """Test mixed severity across items"""
        answers = {"q1": 4, "q2": 0, "q3": 3, "q4": 1, "q5": 0}
        result = self.asrm.calculate_score(answers)
        
        assert result.total_score == 8
        assert "élevée" in result.probability.lower()
    
    def test_subclinical_pattern(self):
        """Test subclinical symptoms (below cutoff)"""
        answers = {"q1": 1, "q2": 1, "q3": 1, "q4": 0, "q5": 1}
        result = self.asrm.calculate_score(answers)
        
        assert result.total_score == 4
        assert "faible" in result.probability.lower()


class TestASRMIntegration:
    """Integration tests for complete ASRM workflow"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.asrm = ASRM()
    
    def test_complete_workflow_low_probability(self):
        """Test complete workflow for low probability case"""
        # 1. Get questionnaire
        full = self.asrm.get_full_questionnaire()
        assert len(full['questions']) == 5
        
        # 2. Simulate user filling out questionnaire
        answers = {"q1": 1, "q2": 0, "q3": 1, "q4": 0, "q5": 1}
        
        # 3. Validate
        validation = self.asrm.validate_answers(answers)
        assert validation.valid is True
        
        # 4. Calculate score
        result = self.asrm.calculate_score(answers)
        assert result.total_score == 3
        assert "faible" in result.probability.lower()
    
    def test_complete_workflow_high_probability(self):
        """Test complete workflow for high probability case"""
        # 1. Get questionnaire structure
        questions = self.asrm.get_questions()
        assert len(questions) == 5
        
        # 2. User answers (high scores)
        answers = {"q1": 3, "q2": 2, "q3": 2, "q4": 2, "q5": 2}
        
        # 3. Validate
        validation = self.asrm.validate_answers(answers)
        assert validation.valid is True
        
        # 4. Calculate score
        result = self.asrm.calculate_score(answers)
        assert result.total_score == 11
        assert "élevée" in result.probability.lower()
        assert "évaluation clinique" in result.interpretation.lower()
    
    def test_workflow_with_warnings(self):
        """Test workflow that triggers warnings"""
        # Answers with 3+ items at maximum
        answers = {"q1": 4, "q2": 4, "q3": 4, "q4": 1, "q5": 1}
        
        # Validate
        validation = self.asrm.validate_answers(answers)
        assert validation.valid is True
        assert len(validation.warnings) > 0
        
        # Calculate score
        result = self.asrm.calculate_score(answers)
        assert result.total_score == 14
        assert "très élevé" in result.interpretation.lower()


class TestASRMDataIntegrity:
    """Test data integrity and consistency"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.asrm = ASRM()
    
    def test_five_items_exactly(self):
        """Test that there are exactly 5 items"""
        assert len(self.asrm.ITEMS) == 5
        assert len(self.asrm.QUESTION_LABELS) == 5
    
    def test_each_item_has_five_options(self):
        """Test that each item has exactly 5 options"""
        for item in self.asrm.ITEMS:
            assert len(item) == 5
    
    def test_question_labels_meaningful(self):
        """Test that question labels are meaningful"""
        labels = self.asrm.QUESTION_LABELS
        
        # Should cover key manic symptoms
        all_labels = ' '.join(labels).lower()
        assert 'humeur' in all_labels or 'bonheur' in all_labels
        assert 'confiance' in all_labels
        assert 'sommeil' in all_labels
        assert 'discours' in all_labels or 'loquacité' in all_labels
        assert 'activité' in all_labels
    
    def test_metadata_consistency(self):
        """Test that metadata is internally consistent"""
        metadata = self.asrm.get_metadata()
        questions = self.asrm.get_questions()
        
        assert metadata['total_questions'] == len(questions)
        assert metadata['scoring_range'][0] == 0
        assert metadata['scoring_range'][1] == 20


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

