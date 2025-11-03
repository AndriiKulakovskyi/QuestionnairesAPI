# -*- coding: utf-8 -*-
"""
Comprehensive unit tests for Epworth Sleepiness Scale
Tests metadata, questions, validation, scoring logic, and edge cases
"""

import pytest
from questionnaires.epworth import Epworth, EpworthError, ScoreResult, ValidationResult


class TestEpworthMetadata:
    """Test Epworth metadata and structure retrieval"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.epworth = Epworth()
    
    def test_get_metadata(self):
        """Test metadata retrieval"""
        metadata = self.epworth.get_metadata()
        
        assert metadata['id'] == 'Epworth.fr'
        assert metadata['abbreviation'] == 'ESS'
        assert metadata['language'] == 'fr-FR'
        assert metadata['version'] == '1.0'
        assert metadata['reference_period'] == 'Mois récents'
        assert metadata['total_questions'] == 9
        assert metadata['scored_questions'] == 8
        assert metadata['scoring_range'] == [0, 24]
        assert metadata['cutoff'] == 11
        assert 'sources' in metadata
        assert len(metadata['sources']) > 0
    
    def test_get_sections(self):
        """Test sections retrieval"""
        sections = self.epworth.get_sections()
        
        assert len(sections) == 2
        assert sections[0]['id'] == 'sec_items'
        assert sections[0]['label'] == 'Situations'
        assert len(sections[0]['question_ids']) == 8
        
        assert sections[1]['id'] == 'sec_extra'
        assert sections[1]['label'] == 'Complément clinique'
        assert len(sections[1]['question_ids']) == 1
    
    def test_get_all_questions(self):
        """Test retrieving all questions"""
        questions = self.epworth.get_questions()
        
        assert len(questions) == 9  # 8 scored + 1 timing
        assert questions[0]['id'] == 'q1'
        assert questions[7]['id'] == 'q8'
        assert questions[8]['id'] == 'q9'
        
        # Check Q1-Q8 structure (scored items)
        for i in range(8):
            q = questions[i]
            assert 'id' in q
            assert 'section_id' in q
            assert 'text' in q
            assert 'type' in q
            assert 'required' in q
            assert 'options' in q
            assert 'constraints' in q
            assert len(q['options']) == 4  # 0-3 scale
            assert q['required'] is True
        
        # Check Q9 structure (timing - not scored)
        q9 = questions[8]
        assert q9['required'] is False
        assert len(q9['options']) == 4
    
    def test_question_options_structure(self):
        """Test that Q1-Q8 have correct options (0-3 with scores)"""
        questions = self.epworth.get_questions()
        
        for i in range(8):
            q = questions[i]
            assert len(q['options']) == 4
            codes = [opt['code'] for opt in q['options']]
            scores = [opt['score'] for opt in q['options']]
            assert codes == [0, 1, 2, 3]
            assert scores == [0, 1, 2, 3]
            # Check all options have labels
            for opt in q['options']:
                assert 'label' in opt
                assert len(opt['label']) > 0
    
    def test_q9_options_no_scores(self):
        """Test that Q9 options don't have scores"""
        q9 = self.epworth.get_question_by_id('q9')
        assert q9 is not None
        for opt in q9['options']:
            assert opt['score'] is None
    
    def test_get_questions_by_section(self):
        """Test retrieving questions filtered by section"""
        scored_questions = self.epworth.get_questions(section_id='sec_items')
        extra_questions = self.epworth.get_questions(section_id='sec_extra')
        
        assert len(scored_questions) == 8
        assert len(extra_questions) == 1
        assert all(q['section_id'] == 'sec_items' for q in scored_questions)
        assert extra_questions[0]['id'] == 'q9'
    
    def test_get_question_by_id(self):
        """Test retrieving specific question by ID"""
        q1 = self.epworth.get_question_by_id('q1')
        assert q1 is not None
        assert q1['id'] == 'q1'
        assert 'lire' in q1['text'].lower()
        
        q9 = self.epworth.get_question_by_id('q9')
        assert q9 is not None
        assert q9['id'] == 'q9'
        assert 'envies de dormir' in q9['text'].lower()
        
        # Non-existent question
        invalid = self.epworth.get_question_by_id('q99')
        assert invalid is None
    
    def test_get_full_questionnaire(self):
        """Test getting complete questionnaire structure"""
        full = self.epworth.get_full_questionnaire()
        
        assert 'metadata' in full
        assert 'sections' in full
        assert 'questions' in full
        assert len(full['questions']) == 9
        assert len(full['sections']) == 2
    
    def test_situation_texts_meaningful(self):
        """Test that situation texts are meaningful"""
        questions = self.epworth.get_questions(section_id='sec_items')
        
        # Check for key situations
        all_texts = ' '.join([q['text'].lower() for q in questions])
        assert 'lire' in all_texts
        assert 'télévision' in all_texts or 'tv' in all_texts
        assert 'voiture' in all_texts or 'auto' in all_texts
        assert 'parler' in all_texts
        assert 'repas' in all_texts


class TestEpworthValidation:
    """Test Epworth answer validation"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.epworth = Epworth()
    
    def test_valid_answers_all_zeros(self):
        """Test validation with all zero answers"""
        answers = {f"q{i}": 0 for i in range(1, 9)}
        validation = self.epworth.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_all_threes(self):
        """Test validation with all maximum answers"""
        answers = {f"q{i}": 3 for i in range(1, 9)}
        validation = self.epworth.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_mixed(self):
        """Test validation with mixed valid answers"""
        answers = {
            "q1": 0, "q2": 1, "q3": 2, "q4": 3,
            "q5": 1, "q6": 2, "q7": 0, "q8": 1
        }
        validation = self.epworth.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_with_q9_optional(self):
        """Test validation with Q9 included (optional)"""
        answers = {f"q{i}": 1 for i in range(1, 9)}
        answers['q9'] = 2  # Optional timing question
        validation = self.epworth.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_without_q9(self):
        """Test validation without Q9 (optional)"""
        answers = {f"q{i}": 1 for i in range(1, 9)}
        # Q9 not included
        validation = self.epworth.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_missing_items_error(self):
        """Test validation fails with missing items"""
        answers = {"q1": 0, "q2": 1, "q3": 2}  # Only 3 items
        validation = self.epworth.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
        assert "Items manquants" in validation.errors[0]
    
    def test_invalid_value_too_high(self):
        """Test validation fails with values > 3"""
        answers = {f"q{i}": 0 for i in range(1, 9)}
        answers['q4'] = 5  # Invalid value
        validation = self.epworth.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
        assert "Valeurs invalides" in validation.errors[0]
    
    def test_invalid_value_negative(self):
        """Test validation fails with negative values"""
        answers = {f"q{i}": 0 for i in range(1, 9)}
        answers['q6'] = -1  # Invalid value
        validation = self.epworth.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
    
    def test_invalid_q9_value(self):
        """Test validation fails with invalid Q9 value"""
        answers = {f"q{i}": 0 for i in range(1, 9)}
        answers['q9'] = 5  # Invalid Q9 value
        validation = self.epworth.validate_answers(answers)
        
        assert validation.valid is False
        assert "Q9" in validation.errors[0]
    
    def test_warning_many_high_scores(self):
        """Test warning when 6+ situations have score 3"""
        answers = {
            "q1": 3, "q2": 3, "q3": 3, "q4": 3,
            "q5": 3, "q6": 3, "q7": 1, "q8": 1
        }
        validation = self.epworth.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) > 0
        assert any('sévère' in w.lower() for w in validation.warnings)
    
    def test_warning_dangerous_situations(self):
        """Test warning for high sleepiness in driving situations"""
        answers = {f"q{i}": 0 for i in range(1, 9)}
        answers['q4'] = 3  # Car passenger - high
        answers['q8'] = 3  # Car in traffic - high
        validation = self.epworth.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) > 0
        assert any('conduite' in w.lower() or 'routière' in w.lower() for w in validation.warnings)
    
    def test_no_warnings_with_low_scores(self):
        """Test no warnings with low scores"""
        answers = {f"q{i}": 1 for i in range(1, 9)}
        validation = self.epworth.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) == 0


class TestEpworthScoring:
    """Test Epworth scoring calculation"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.epworth = Epworth()
    
    def test_score_minimum(self):
        """Test scoring with minimum score (0)"""
        answers = {f"q{i}": 0 for i in range(1, 9)}
        result = self.epworth.calculate_score(answers)
        
        assert result.total_score == 0
        assert result.severity == "Somnolence dans les limites normales"
    
    def test_score_maximum(self):
        """Test scoring with maximum score (24)"""
        answers = {f"q{i}": 3 for i in range(1, 9)}
        result = self.epworth.calculate_score(answers)
        
        assert result.total_score == 24
        assert result.severity == "Somnolence diurne excessive (SDE) probable"
    
    def test_score_just_below_cutoff(self):
        """Test scoring just below cutoff (score 10)"""
        answers = {f"q{i}": 1 for i in range(1, 9)}
        answers['q1'] = 2
        answers['q2'] = 2
        result = self.epworth.calculate_score(answers)
        
        assert result.total_score == 10
        assert result.severity == "Somnolence dans les limites normales"
    
    def test_score_at_cutoff(self):
        """Test scoring at cutoff (score 11)"""
        answers = {f"q{i}": 1 for i in range(1, 9)}
        answers['q1'] = 2
        answers['q2'] = 2
        answers['q3'] = 1
        result = self.epworth.calculate_score(answers)
        
        assert result.total_score == 11
        assert result.severity == "Somnolence diurne excessive (SDE) probable"
    
    def test_score_moderate(self):
        """Test scoring in moderate range (12-15)"""
        answers = {f"q{i}": 2 for i in range(1, 9)}
        result = self.epworth.calculate_score(answers)
        
        assert result.total_score == 16
        assert result.severity == "Somnolence diurne excessive (SDE) probable"
        assert "très élevé" in result.interpretation.lower()
    
    def test_score_very_high(self):
        """Test scoring in very high range (16+)"""
        answers = {
            "q1": 3, "q2": 3, "q3": 2, "q4": 2,
            "q5": 3, "q6": 2, "q7": 2, "q8": 3
        }
        result = self.epworth.calculate_score(answers)
        
        assert result.total_score == 20
        assert "très élevé" in result.interpretation.lower()
        assert "urgente" in result.interpretation.lower()
    
    def test_score_calculation_accuracy(self):
        """Test that scoring is simple sum"""
        answers = {
            "q1": 1, "q2": 2, "q3": 3, "q4": 0,
            "q5": 2, "q6": 1, "q7": 2, "q8": 1
        }
        result = self.epworth.calculate_score(answers)
        
        # Should be simple sum: 1 + 2 + 3 + 0 + 2 + 1 + 2 + 1 = 12
        assert result.total_score == 12
    
    def test_q9_not_included_in_score(self):
        """Test that Q9 is not included in total score"""
        answers = {f"q{i}": 1 for i in range(1, 9)}
        answers['q9'] = 3  # Should not affect score
        result = self.epworth.calculate_score(answers)
        
        # Score should be 8 (8 items × 1), Q9 not counted
        assert result.total_score == 8
    
    def test_clinical_context_with_q9(self):
        """Test that Q9 appears in clinical context"""
        answers = {f"q{i}": 1 for i in range(1, 9)}
        answers['q9'] = 3  # Any time of day
        result = self.epworth.calculate_score(answers)
        
        assert result.clinical_context is not None
        assert "n'importe quelle heure" in result.clinical_context.lower()
    
    def test_no_clinical_context_without_q9(self):
        """Test no clinical context when Q9 not provided"""
        answers = {f"q{i}": 1 for i in range(1, 9)}
        result = self.epworth.calculate_score(answers)
        
        assert result.clinical_context is None
    
    def test_score_with_invalid_answers_raises_error(self):
        """Test that invalid answers raise EpworthError"""
        answers = {"q1": 0, "q2": 1}  # Missing items
        
        with pytest.raises(EpworthError) as exc_info:
            self.epworth.calculate_score(answers)
        
        assert "Items manquants" in str(exc_info.value)
    
    def test_interpretation_includes_recommendation(self):
        """Test that high scores include medical recommendation"""
        answers = {f"q{i}": 2 for i in range(1, 9)}
        result = self.epworth.calculate_score(answers)
        
        assert result.total_score == 16
        assert "évaluation" in result.interpretation.lower()
        assert "médicale" in result.interpretation.lower()
    
    def test_score_range_in_result(self):
        """Test that result includes valid score range"""
        answers = {f"q{i}": 0 for i in range(1, 9)}
        result = self.epworth.calculate_score(answers)
        
        assert result.range == (0, 24)


class TestEpworthBoundaryConditions:
    """Test boundary conditions and edge cases"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.epworth = Epworth()
    
    def test_boundary_score_10_vs_11(self):
        """Test boundary between normal and excessive"""
        # Score 10 - below cutoff
        answers = {
            "q1": 1, "q2": 1, "q3": 1, "q4": 1,
            "q5": 2, "q6": 2, "q7": 1, "q8": 1
        }
        result = self.epworth.calculate_score(answers)
        assert result.total_score == 10
        assert "limites normales" in result.severity.lower()
        
        # Score 11 - at cutoff
        answers['q8'] = 2
        result = self.epworth.calculate_score(answers)
        assert result.total_score == 11
        assert "excessive" in result.severity.lower()
    
    def test_cutoff_constant(self):
        """Test that cutoff is correctly defined"""
        assert self.epworth.CUTOFF_EXCESSIVE_SLEEPINESS == 11
    
    def test_all_items_at_same_level(self):
        """Test when all items have same score"""
        for score in range(4):
            answers = {f"q{i}": score for i in range(1, 9)}
            result = self.epworth.calculate_score(answers)
            assert result.total_score == score * 8
    
    def test_single_item_variations(self):
        """Test score changes with single item variation"""
        base_answers = {f"q{i}": 1 for i in range(1, 9)}
        base_result = self.epworth.calculate_score(base_answers)
        base_score = base_result.total_score
        
        # Change one item
        answers = base_answers.copy()
        answers['q5'] = 2
        result = self.epworth.calculate_score(answers)
        assert result.total_score == base_score + 1
    
    def test_consistent_scoring_multiple_calls(self):
        """Test that scoring is consistent across multiple calls"""
        answers = {
            "q1": 2, "q2": 3, "q3": 1, "q4": 2,
            "q5": 2, "q6": 1, "q7": 2, "q8": 1
        }
        
        result1 = self.epworth.calculate_score(answers)
        result2 = self.epworth.calculate_score(answers)
        result3 = self.epworth.calculate_score(answers)
        
        assert result1.total_score == result2.total_score == result3.total_score
        assert result1.severity == result2.severity == result3.severity


class TestEpworthSpecialCases:
    """Test special cases and clinical scenarios"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.epworth = Epworth()
    
    def test_mild_sleepiness_pattern(self):
        """Test mild sleepiness pattern"""
        answers = {
            "q1": 2, "q2": 1, "q3": 0, "q4": 1,
            "q5": 2, "q6": 0, "q7": 1, "q8": 0
        }
        result = self.epworth.calculate_score(answers)
        
        assert result.total_score == 7
        assert "limites normales" in result.severity.lower()
    
    def test_moderate_sleepiness_pattern(self):
        """Test moderate sleepiness pattern"""
        answers = {
            "q1": 2, "q2": 2, "q3": 1, "q4": 2,
            "q5": 2, "q6": 1, "q7": 1, "q8": 1
        }
        result = self.epworth.calculate_score(answers)
        
        assert result.total_score == 12
        assert "excessive" in result.severity.lower()
    
    def test_severe_sleepiness_pattern(self):
        """Test severe sleepiness pattern"""
        answers = {f"q{i}": 3 for i in range(1, 9)}
        result = self.epworth.calculate_score(answers)
        
        assert result.total_score == 24
        assert "très élevé" in result.interpretation.lower()
    
    def test_selective_sleepiness_pattern(self):
        """Test selective sleepiness (only passive situations)"""
        # High in passive situations, low in active
        answers = {
            "q1": 3, "q2": 3, "q3": 2, "q4": 2,  # Passive
            "q5": 0, "q6": 0, "q7": 0, "q8": 0   # Active
        }
        result = self.epworth.calculate_score(answers)
        
        assert result.total_score == 10
    
    def test_driving_related_sleepiness(self):
        """Test high sleepiness in driving situations"""
        answers = {f"q{i}": 1 for i in range(1, 9)}
        answers['q4'] = 3  # Car passenger
        answers['q8'] = 3  # Car in traffic
        result = self.epworth.calculate_score(answers)
        
        # Should have safety warning
        assert "conduite" in result.interpretation.lower() or "routière" in result.interpretation.lower()
    
    def test_post_meal_timing(self):
        """Test sleepiness only after meals"""
        answers = {f"q{i}": 2 for i in range(1, 9)}
        answers['q9'] = 0  # Only after meals
        result = self.epworth.calculate_score(answers)
        
        assert "après les repas" in result.clinical_context.lower()
    
    def test_anytime_timing(self):
        """Test sleepiness at any time"""
        answers = {f"q{i}": 2 for i in range(1, 9)}
        answers['q9'] = 3  # Any time of day
        result = self.epworth.calculate_score(answers)
        
        assert "n'importe quelle heure" in result.clinical_context.lower()


class TestEpworthIntegration:
    """Integration tests for complete Epworth workflow"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.epworth = Epworth()
    
    def test_complete_workflow_normal(self):
        """Test complete workflow for normal sleepiness"""
        # 1. Get questionnaire
        full = self.epworth.get_full_questionnaire()
        assert len(full['questions']) == 9
        
        # 2. Simulate user filling out questionnaire
        answers = {
            "q1": 1, "q2": 0, "q3": 0, "q4": 1,
            "q5": 1, "q6": 0, "q7": 1, "q8": 0
        }
        
        # 3. Validate
        validation = self.epworth.validate_answers(answers)
        assert validation.valid is True
        
        # 4. Calculate score
        result = self.epworth.calculate_score(answers)
        assert result.total_score == 4
        assert "limites normales" in result.severity.lower()
    
    def test_complete_workflow_excessive(self):
        """Test complete workflow for excessive sleepiness"""
        # 1. Get questionnaire structure
        questions = self.epworth.get_questions()
        assert len(questions) == 9
        
        # 2. User answers (high scores)
        answers = {
            "q1": 3, "q2": 2, "q3": 2, "q4": 2,
            "q5": 3, "q6": 1, "q7": 2, "q8": 1,
            "q9": 3  # Any time of day
        }
        
        # 3. Validate
        validation = self.epworth.validate_answers(answers)
        assert validation.valid is True
        
        # 4. Calculate score
        result = self.epworth.calculate_score(answers)
        assert result.total_score == 16
        assert "excessive" in result.severity.lower()
        assert result.clinical_context is not None
        assert "évaluation" in result.interpretation.lower()
    
    def test_workflow_with_warnings(self):
        """Test workflow that triggers warnings"""
        # High scores in dangerous situations
        answers = {
            "q1": 1, "q2": 1, "q3": 1, "q4": 3,
            "q5": 1, "q6": 1, "q7": 1, "q8": 3
        }
        
        # Validate
        validation = self.epworth.validate_answers(answers)
        assert validation.valid is True
        assert len(validation.warnings) > 0
        
        # Calculate score
        result = self.epworth.calculate_score(answers)
        assert result.total_score == 10
        assert "conduite" in result.interpretation.lower() or "routière" in result.interpretation.lower()


class TestEpworthDataIntegrity:
    """Test data integrity and consistency"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.epworth = Epworth()
    
    def test_eight_situation_items(self):
        """Test that there are exactly 8 situation items"""
        assert len(self.epworth.SITUATION_ITEMS) == 8
    
    def test_each_item_has_four_options(self):
        """Test that each scored item has exactly 4 options"""
        questions = self.epworth.get_questions(section_id='sec_items')
        for q in questions:
            assert len(q['options']) == 4
    
    def test_response_options_structure(self):
        """Test that response options are correctly structured"""
        opts = self.epworth.RESPONSE_OPTIONS
        assert len(opts) == 4
        codes = [opt['code'] for opt in opts]
        scores = [opt['score'] for opt in opts]
        assert codes == [0, 1, 2, 3]
        assert scores == [0, 1, 2, 3]
    
    def test_timing_options_structure(self):
        """Test that timing options are correctly structured"""
        opts = self.epworth.TIMING_OPTIONS
        assert len(opts) == 4
        # Timing options should not have scores
        for opt in opts:
            assert 'code' in opt
            assert 'label' in opt
    
    def test_metadata_consistency(self):
        """Test that metadata is internally consistent"""
        metadata = self.epworth.get_metadata()
        questions = self.epworth.get_questions()
        
        assert metadata['total_questions'] == len(questions)
        assert metadata['scored_questions'] == 8
        assert metadata['scoring_range'][0] == 0
        assert metadata['scoring_range'][1] == 24


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

