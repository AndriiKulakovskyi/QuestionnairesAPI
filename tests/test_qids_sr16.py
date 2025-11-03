# -*- coding: utf-8 -*-
"""
Comprehensive unit tests for QIDS-SR16 questionnaire
Tests metadata, questions, validation, scoring logic, and edge cases
"""

import pytest
from questionnaires.qids import QIDSSR16, QIDSError, ScoreResult, ValidationResult


class TestQIDSSR16Metadata:
    """Test QIDS-SR16 metadata and structure retrieval"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.qids = QIDSSR16()
    
    def test_get_metadata(self):
        """Test metadata retrieval"""
        metadata = self.qids.get_metadata()
        
        assert metadata['id'] == 'QIDS-SR16.fr'
        assert metadata['abbreviation'] == 'QIDS-SR16'
        assert metadata['language'] == 'fr-FR'
        assert metadata['version'] == '1.0'
        assert metadata['total_questions'] == 16
        assert metadata['scoring_range'] == [0, 27]
        assert 'sources' in metadata
        assert len(metadata['sources']) > 0
    
    def test_get_sections(self):
        """Test sections retrieval"""
        sections = self.qids.get_sections()
        
        assert len(sections) == 2
        assert sections[0]['id'] == 'part1'
        assert sections[0]['label'] == 'PARTIE 1'
        assert len(sections[0]['question_ids']) == 9
        
        assert sections[1]['id'] == 'part2'
        assert sections[1]['label'] == 'PARTIE 2'
        assert len(sections[1]['question_ids']) == 7
    
    def test_get_all_questions(self):
        """Test retrieving all questions"""
        questions = self.qids.get_questions()
        
        assert len(questions) == 16
        assert questions[0]['id'] == 'q1'
        assert questions[15]['id'] == 'q16'
        
        # Check question structure
        q1 = questions[0]
        assert 'id' in q1
        assert 'section_id' in q1
        assert 'text' in q1
        assert 'type' in q1
        assert 'required' in q1
        assert 'options' in q1
        assert 'constraints' in q1
        assert len(q1['options']) == 4  # 0-3 scale
    
    def test_get_questions_by_section(self):
        """Test retrieving questions filtered by section"""
        part1_questions = self.qids.get_questions(section_id='part1')
        part2_questions = self.qids.get_questions(section_id='part2')
        
        assert len(part1_questions) == 9
        assert len(part2_questions) == 7
        assert all(q['section_id'] == 'part1' for q in part1_questions)
        assert all(q['section_id'] == 'part2' for q in part2_questions)
    
    def test_get_question_by_id(self):
        """Test retrieving specific question by ID"""
        q1 = self.qids.get_question_by_id('q1')
        assert q1 is not None
        assert q1['id'] == 'q1'
        assert q1['text'] == 'Endormissement'
        
        q12 = self.qids.get_question_by_id('q12')
        assert q12 is not None
        assert q12['id'] == 'q12'
        assert 'help' in q12  # Suicidal ideation has help text
        
        # Non-existent question
        invalid = self.qids.get_question_by_id('q99')
        assert invalid is None
    
    def test_get_full_questionnaire(self):
        """Test getting complete questionnaire structure"""
        full = self.qids.get_full_questionnaire()
        
        assert 'metadata' in full
        assert 'sections' in full
        assert 'questions' in full
        assert len(full['questions']) == 16
        assert len(full['sections']) == 2


class TestQIDSSR16Validation:
    """Test QIDS-SR16 answer validation"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.qids = QIDSSR16()
    
    def test_valid_answers_all_zeros(self):
        """Test validation with all zero answers"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        validation = self.qids.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_all_threes(self):
        """Test validation with all maximum answers"""
        answers = {f"q{i}": 3 for i in range(1, 17)}
        validation = self.qids.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_mixed(self):
        """Test validation with mixed valid answers"""
        answers = {
            "q1": 0, "q2": 1, "q3": 2, "q4": 3,
            "q5": 2, "q6": 1, "q7": 0, "q8": 1,
            "q9": 0, "q10": 2, "q11": 1, "q12": 0,
            "q13": 2, "q14": 3, "q15": 1, "q16": 0
        }
        validation = self.qids.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_missing_items_error(self):
        """Test validation fails with missing items"""
        answers = {"q1": 0, "q2": 1, "q3": 2}  # Only 3 items
        validation = self.qids.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
        assert "Items manquants" in validation.errors[0]
    
    def test_invalid_value_too_high(self):
        """Test validation fails with values > 3"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        answers['q5'] = 5  # Invalid value
        validation = self.qids.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
        assert "Valeurs invalides" in validation.errors[0]
    
    def test_invalid_value_negative(self):
        """Test validation fails with negative values"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        answers['q10'] = -1  # Invalid value
        validation = self.qids.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
    
    def test_invalid_value_non_integer(self):
        """Test validation fails with non-integer values"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        answers['q7'] = "2"  # String instead of int
        validation = self.qids.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
    
    def test_appetite_consistency_warning(self):
        """Test warning for conflicting appetite answers"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        answers['q6'] = 2  # Decreased appetite
        answers['q7'] = 2  # Increased appetite - conflicting!
        validation = self.qids.validate_answers(answers)
        
        assert validation.valid is True  # Still valid, just warning
        assert len(validation.warnings) > 0
        assert any('appétit' in w.lower() for w in validation.warnings)
    
    def test_weight_consistency_warning(self):
        """Test warning for conflicting weight answers"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        answers['q8'] = 2  # Weight loss
        answers['q9'] = 2  # Weight gain - conflicting!
        validation = self.qids.validate_answers(answers)
        
        assert validation.valid is True  # Still valid, just warning
        assert len(validation.warnings) > 0
        assert any('poids' in w.lower() for w in validation.warnings)
    
    def test_multiple_warnings(self):
        """Test multiple warnings can be triggered"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        answers['q6'] = 3  # Decreased appetite
        answers['q7'] = 3  # Increased appetite
        answers['q8'] = 3  # Weight loss
        answers['q9'] = 3  # Weight gain
        validation = self.qids.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) >= 2  # Both appetite and weight warnings


class TestQIDSSR16Scoring:
    """Test QIDS-SR16 scoring calculation"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.qids = QIDSSR16()
    
    def test_score_no_depression(self):
        """Test scoring with no depression (score 0)"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        result = self.qids.calculate_score(answers)
        
        assert result.total_score == 0
        assert result.severity == "Pas de dépression"
        assert result.domain_scores['sleep'] == 0
        assert result.domain_scores['sadness'] == 0
        assert result.domain_scores['appetite_weight'] == 0
        assert result.domain_scores['psychomotor'] == 0
    
    def test_score_mild_depression(self):
        """Test scoring with mild depression (score 6-10)"""
        answers = {
            "q1": 1, "q2": 0, "q3": 0, "q4": 0,  # Sleep: max = 1
            "q5": 1,  # Sadness: 1
            "q6": 1, "q7": 0, "q8": 0, "q9": 0,  # Appetite/weight: max = 1
            "q10": 1,  # Concentration: 1
            "q11": 1,  # Self-view: 1
            "q12": 0,  # Suicidal ideation: 0
            "q13": 1,  # Interest: 1
            "q14": 1,  # Energy: 1
            "q15": 1, "q16": 0   # Psychomotor: max = 1
        }
        result = self.qids.calculate_score(answers)
        
        # Total: 1 + 1 + 1 + 1 + 1 + 0 + 1 + 1 + 1 = 8
        assert result.total_score == 8
        assert result.severity == "Dépression légère"
    
    def test_score_moderate_depression(self):
        """Test scoring with moderate depression (score 11-15)"""
        answers = {
            "q1": 2, "q2": 1, "q3": 0, "q4": 0,  # Sleep: max = 2
            "q5": 2,  # Sadness: 2
            "q6": 0, "q7": 1, "q8": 0, "q9": 0,  # Appetite/weight: max = 1
            "q10": 2,  # Concentration: 2
            "q11": 1,  # Self-view: 1
            "q12": 1,  # Suicidal ideation: 1
            "q13": 2,  # Interest: 2
            "q14": 2,  # Energy: 2
            "q15": 1, "q16": 0   # Psychomotor: max = 1
        }
        result = self.qids.calculate_score(answers)
        
        # Total: 2 + 2 + 1 + 2 + 1 + 1 + 2 + 2 + 1 = 14
        assert result.total_score == 14
        assert result.severity == "Dépression modérée"
    
    def test_score_severe_depression(self):
        """Test scoring with severe depression (score 16-20)"""
        answers = {
            "q1": 2, "q2": 2, "q3": 1, "q4": 0,  # Sleep: max = 2
            "q5": 3,  # Sadness: 3
            "q6": 0, "q7": 0, "q8": 2, "q9": 0,  # Appetite/weight: max = 2
            "q10": 2,  # Concentration: 2
            "q11": 2,  # Self-view: 2
            "q12": 2,  # Suicidal ideation: 2
            "q13": 2,  # Interest: 2
            "q14": 3,  # Energy: 3
            "q15": 2, "q16": 0   # Psychomotor: max = 2
        }
        result = self.qids.calculate_score(answers)
        
        # Total: 2 + 3 + 2 + 2 + 2 + 2 + 2 + 3 + 2 = 20
        assert result.total_score == 20
        assert result.severity == "Dépression sévère"
    
    def test_score_very_severe_depression(self):
        """Test scoring with very severe depression (score 21-27)"""
        answers = {f"q{i}": 3 for i in range(1, 17)}
        result = self.qids.calculate_score(answers)
        
        # Total: 3 (sleep) + 3 + 3 (appetite) + 3 + 3 + 3 + 3 + 3 + 3 (psychomotor) = 27
        assert result.total_score == 27
        assert result.severity == "Dépression très sévère"
    
    def test_sleep_domain_max_logic(self):
        """Test that sleep domain uses max of Q1-Q4"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        answers['q1'] = 1
        answers['q2'] = 3  # Maximum
        answers['q3'] = 0
        answers['q4'] = 2
        
        result = self.qids.calculate_score(answers)
        assert result.domain_scores['sleep'] == 3  # Should be max, not sum
    
    def test_appetite_weight_domain_max_logic(self):
        """Test that appetite/weight domain uses max of Q6-Q9"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        answers['q6'] = 1
        answers['q7'] = 0
        answers['q8'] = 3  # Maximum
        answers['q9'] = 2
        
        result = self.qids.calculate_score(answers)
        assert result.domain_scores['appetite_weight'] == 3  # Should be max
    
    def test_psychomotor_domain_max_logic(self):
        """Test that psychomotor domain uses max of Q15-Q16"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        answers['q15'] = 2
        answers['q16'] = 3  # Maximum
        
        result = self.qids.calculate_score(answers)
        assert result.domain_scores['psychomotor'] == 3  # Should be max
    
    def test_suicidal_ideation_alert(self):
        """Test that suicidal ideation triggers alert in interpretation"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        answers['q12'] = 3  # High suicidal ideation
        
        result = self.qids.calculate_score(answers)
        assert result.domain_scores['suicidal_ideation'] == 3
        assert "ALERTE" in result.interpretation or "suicidaire" in result.interpretation.lower()
    
    def test_domain_scores_structure(self):
        """Test that all domain scores are present"""
        answers = {f"q{i}": 1 for i in range(1, 17)}
        result = self.qids.calculate_score(answers)
        
        expected_domains = [
            'sleep', 'sadness', 'appetite_weight', 'concentration',
            'self_view', 'suicidal_ideation', 'interest', 'energy', 'psychomotor'
        ]
        
        for domain in expected_domains:
            assert domain in result.domain_scores
            assert isinstance(result.domain_scores[domain], int)
            assert 0 <= result.domain_scores[domain] <= 3
    
    def test_score_with_invalid_answers_raises_error(self):
        """Test that invalid answers raise QIDSError"""
        answers = {"q1": 0, "q2": 1}  # Missing items
        
        with pytest.raises(QIDSError) as exc_info:
            self.qids.calculate_score(answers)
        
        assert "Items manquants" in str(exc_info.value)
    
    def test_score_boundary_mild_moderate(self):
        """Test boundary between mild and moderate (10-11)"""
        # Score exactly 10
        answers = {
            "q1": 2, "q2": 0, "q3": 0, "q4": 0,
            "q5": 1, "q6": 1, "q7": 0, "q8": 0,
            "q9": 0, "q10": 2, "q11": 1, "q12": 1,
            "q13": 1, "q14": 1, "q15": 1, "q16": 0
        }
        result = self.qids.calculate_score(answers)
        assert result.total_score == 10
        assert result.severity == "Dépression légère"
        
        # Score exactly 11
        answers['q5'] = 2
        result = self.qids.calculate_score(answers)
        assert result.total_score == 11
        assert result.severity == "Dépression modérée"
    
    def test_score_boundary_moderate_severe(self):
        """Test boundary between moderate and severe (15-16)"""
        # Score exactly 15
        answers = {
            "q1": 2, "q2": 0, "q3": 0, "q4": 0,
            "q5": 2, "q6": 2, "q7": 0, "q8": 0,
            "q9": 0, "q10": 2, "q11": 2, "q12": 1,
            "q13": 2, "q14": 1, "q15": 1, "q16": 0
        }
        result = self.qids.calculate_score(answers)
        assert result.total_score == 15
        assert result.severity == "Dépression modérée"
        
        # Score exactly 16
        answers['q14'] = 2
        result = self.qids.calculate_score(answers)
        assert result.total_score == 16
        assert result.severity == "Dépression sévère"


class TestQIDSSR16EdgeCases:
    """Test edge cases and special scenarios"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.qids = QIDSSR16()
    
    def test_all_sleep_items_same_value(self):
        """Test when all sleep items have same value"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        answers['q1'] = answers['q2'] = answers['q3'] = answers['q4'] = 2
        
        result = self.qids.calculate_score(answers)
        assert result.domain_scores['sleep'] == 2
    
    def test_insomnia_vs_hypersomnia(self):
        """Test that only one type of sleep problem counts (max logic)"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        # Insomnia symptoms
        answers['q1'] = 3  # Difficulty falling asleep
        answers['q2'] = 2  # Restless sleep
        answers['q3'] = 1  # Early morning awakening
        # Hypersomnia
        answers['q4'] = 2  # Sleeping too much
        
        result = self.qids.calculate_score(answers)
        # Should use max (3), not sum (8)
        assert result.domain_scores['sleep'] == 3
        assert result.total_score <= 27
    
    def test_weight_loss_vs_gain(self):
        """Test that only one type of weight change counts"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        answers['q8'] = 3  # Weight loss
        answers['q9'] = 2  # Weight gain
        
        result = self.qids.calculate_score(answers)
        assert result.domain_scores['appetite_weight'] == 3  # Max, not sum
    
    def test_retardation_vs_agitation(self):
        """Test that only one psychomotor symptom counts"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        answers['q15'] = 3  # Retardation
        answers['q16'] = 2  # Agitation
        
        result = self.qids.calculate_score(answers)
        assert result.domain_scores['psychomotor'] == 3  # Max, not sum
    
    def test_minimal_suicidal_ideation(self):
        """Test minimal suicidal ideation (score 1) doesn't trigger alert"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        answers['q12'] = 1  # Thinking about life's value
        
        result = self.qids.calculate_score(answers)
        # Alert should only trigger at score >= 2
        if answers['q12'] < 2:
            assert "ALERTE" not in result.interpretation
    
    def test_score_result_has_range(self):
        """Test that ScoreResult includes the valid range"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        result = self.qids.calculate_score(answers)
        
        assert result.range == (0, 27)
    
    def test_consistent_scoring_multiple_calls(self):
        """Test that scoring is consistent across multiple calls"""
        answers = {
            "q1": 2, "q2": 1, "q3": 1, "q4": 0,
            "q5": 2, "q6": 1, "q7": 0, "q8": 0,
            "q9": 1, "q10": 2, "q11": 1, "q12": 1,
            "q13": 2, "q14": 2, "q15": 1, "q16": 0
        }
        
        result1 = self.qids.calculate_score(answers)
        result2 = self.qids.calculate_score(answers)
        result3 = self.qids.calculate_score(answers)
        
        assert result1.total_score == result2.total_score == result3.total_score
        assert result1.severity == result2.severity == result3.severity


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

