# -*- coding: utf-8 -*-
"""
Comprehensive unit tests for Fagerström Test for Nicotine Dependence (FTND)
Tests metadata, questions, validation, scoring, and edge cases
"""

import pytest
from questionnaires.fagerstrom import Fagerstrom, FagerstromError, ScoreResult, ValidationResult


class TestFagerstromMetadata:
    """Test Fagerström metadata and structure retrieval"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.fager = Fagerstrom()
    
    def test_get_metadata(self):
        """Test metadata retrieval"""
        metadata = self.fager.get_metadata()
        
        assert metadata['id'] == 'Fagerstrom.fr'
        assert metadata['abbreviation'] == 'FTND'
        assert metadata['language'] == 'fr-FR'
        assert metadata['version'] == '1.0'
        assert metadata['total_questions'] == 6
        assert metadata['score_range'] == [0, 10]
        assert len(metadata['cutoffs']) == 4
        assert 'sources' in metadata
    
    def test_get_sections(self):
        """Test sections retrieval"""
        sections = self.fager.get_sections()
        
        assert len(sections) == 1
        assert sections[0]['id'] == 'sec1'
        assert sections[0]['label'] == 'FTND – 6 items'
        assert len(sections[0]['question_ids']) == 6
    
    def test_get_all_questions(self):
        """Test retrieving all questions"""
        questions = self.fager.get_questions()
        
        assert len(questions) == 6
        for i, q in enumerate(questions, 1):
            assert q['id'] == f'q{i}'
            assert q['section_id'] == 'sec1'
            assert q['type'] == 'single_choice'
            assert q['required'] is True
            assert 'options' in q
            assert 'constraints' in q
    
    def test_question_1_structure(self):
        """Test Q1 (time to first cigarette) has 4 options (0-3)"""
        q1 = self.fager.get_question_by_id('q1')
        assert q1 is not None
        assert len(q1['options']) == 4
        scores = [opt['score'] for opt in q1['options']]
        codes = [opt['code'] for opt in q1['options']]
        assert scores == [3, 2, 1, 0]
        assert codes == [3, 2, 1, 0]
        assert '5 minutes' in q1['options'][0]['label']
    
    def test_question_4_structure(self):
        """Test Q4 (cigarettes per day) has 4 options (0-3)"""
        q4 = self.fager.get_question_by_id('q4')
        assert q4 is not None
        assert len(q4['options']) == 4
        scores = [opt['score'] for opt in q4['options']]
        assert scores == [0, 1, 2, 3]
        assert '10 ou moins' in q4['options'][0]['label']
    
    def test_binary_questions_structure(self):
        """Test Q2, Q3, Q5, Q6 have 2 options (0-1)"""
        for q_id in ['q2', 'q3', 'q5', 'q6']:
            q = self.fager.get_question_by_id(q_id)
            assert q is not None
            assert len(q['options']) == 2
            scores = [opt['score'] for opt in q['options']]
            assert set(scores) == {0, 1}
    
    def test_get_full_questionnaire(self):
        """Test getting complete questionnaire structure"""
        full = self.fager.get_full_questionnaire()
        
        assert 'metadata' in full
        assert 'sections' in full
        assert 'questions' in full
        assert len(full['questions']) == 6


class TestFagerstromValidation:
    """Test Fagerström answer validation"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.fager = Fagerstrom()
    
    def test_valid_answers_no_dependence(self):
        """Test validation with no dependence (all zeros)"""
        answers = {f"q{i}": 0 for i in range(1, 7)}
        validation = self.fager.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_mixed(self):
        """Test validation with mixed valid answers"""
        answers = {
            "q1": 2, "q2": 1, "q3": 1, "q4": 1, "q5": 0, "q6": 0
        }
        validation = self.fager.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_max_dependence(self):
        """Test validation with maximum dependence"""
        answers = {
            "q1": 3, "q2": 1, "q3": 1, "q4": 3, "q5": 1, "q6": 1
        }
        validation = self.fager.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_missing_question_error(self):
        """Test validation fails with missing question"""
        answers = {"q1": 1, "q2": 0, "q3": 1}  # Missing q4, q5, q6
        validation = self.fager.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
        assert "Items manquants" in validation.errors[0]
    
    def test_invalid_q1_value(self):
        """Test validation fails with invalid Q1 value"""
        answers = {f"q{i}": 0 for i in range(1, 7)}
        answers['q1'] = 4  # Invalid (should be 0-3)
        validation = self.fager.validate_answers(answers)
        
        assert validation.valid is False
        assert any('q1' in err for err in validation.errors)
    
    def test_invalid_q4_value(self):
        """Test validation fails with invalid Q4 value"""
        answers = {f"q{i}": 0 for i in range(1, 7)}
        answers['q4'] = 5  # Invalid (should be 0-3)
        validation = self.fager.validate_answers(answers)
        
        assert validation.valid is False
        assert any('q4' in err for err in validation.errors)
    
    def test_invalid_q2_value(self):
        """Test validation fails with invalid Q2 value"""
        answers = {f"q{i}": 0 for i in range(1, 7)}
        answers['q2'] = 2  # Invalid (should be 0-1)
        validation = self.fager.validate_answers(answers)
        
        assert validation.valid is False
        assert any('q2' in err for err in validation.errors)
    
    def test_warning_high_score(self):
        """Test warning for very high score (≥8)"""
        answers = {
            "q1": 3, "q2": 1, "q3": 1, "q4": 3, "q5": 1, "q6": 0
        }  # Total = 9
        validation = self.fager.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) > 0
        assert any('≥8' in w or '8' in w for w in validation.warnings)
    
    def test_warning_early_morning_smoking(self):
        """Test warning for smoking within 5 minutes"""
        answers = {
            "q1": 3, "q2": 0, "q3": 0, "q4": 0, "q5": 0, "q6": 0
        }
        validation = self.fager.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) > 0
        assert any('5 minutes' in w.lower() for w in validation.warnings)
    
    def test_warning_high_consumption(self):
        """Test warning for high cigarette consumption"""
        answers = {
            "q1": 0, "q2": 0, "q3": 0, "q4": 3, "q5": 0, "q6": 0
        }
        validation = self.fager.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) > 0
        assert any('31' in w for w in validation.warnings)


class TestFagerstromScoring:
    """Test Fagerström scoring calculation"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.fager = Fagerstrom()
    
    def test_score_no_dependence(self):
        """Test scoring with no dependence (score 0)"""
        answers = {f"q{i}": 0 for i in range(1, 7)}
        result = self.fager.calculate_score(answers)
        
        assert result.total_score == 0
        assert "très faible" in result.dependence_level.lower()
    
    def test_score_very_weak_dependence(self):
        """Test scoring with very weak dependence (score 1-2)"""
        answers = {
            "q1": 1, "q2": 1, "q3": 0, "q4": 0, "q5": 0, "q6": 0
        }  # Total = 2
        result = self.fager.calculate_score(answers)
        
        assert result.total_score == 2
        assert "très faible" in result.dependence_level.lower()
    
    def test_score_weak_dependence_lower(self):
        """Test scoring with weak dependence (score 3)"""
        answers = {
            "q1": 2, "q2": 1, "q3": 0, "q4": 0, "q5": 0, "q6": 0
        }  # Total = 3
        result = self.fager.calculate_score(answers)
        
        assert result.total_score == 3
        assert result.dependence_level == "Dépendance faible"
    
    def test_score_weak_dependence_upper(self):
        """Test scoring with weak dependence (score 4)"""
        answers = {
            "q1": 2, "q2": 1, "q3": 1, "q4": 0, "q5": 0, "q6": 0
        }  # Total = 4
        result = self.fager.calculate_score(answers)
        
        assert result.total_score == 4
        assert result.dependence_level == "Dépendance faible"
    
    def test_score_medium_dependence(self):
        """Test scoring with medium dependence (score 5)"""
        answers = {
            "q1": 2, "q2": 1, "q3": 1, "q4": 1, "q5": 0, "q6": 0
        }  # Total = 5
        result = self.fager.calculate_score(answers)
        
        assert result.total_score == 5
        assert result.dependence_level == "Dépendance moyenne"
    
    def test_score_strong_dependence_lower(self):
        """Test scoring with strong dependence (score 6)"""
        answers = {
            "q1": 2, "q2": 1, "q3": 1, "q4": 1, "q5": 1, "q6": 0
        }  # Total = 6
        result = self.fager.calculate_score(answers)
        
        assert result.total_score == 6
        assert result.dependence_level == "Dépendance forte"
    
    def test_score_strong_dependence_upper(self):
        """Test scoring with maximum dependence (score 10)"""
        answers = {
            "q1": 3, "q2": 1, "q3": 1, "q4": 3, "q5": 1, "q6": 1
        }  # Total = 10
        result = self.fager.calculate_score(answers)
        
        assert result.total_score == 10
        assert result.dependence_level == "Dépendance forte"
    
    def test_item_scores_in_result(self):
        """Test that individual item scores are included"""
        answers = {
            "q1": 2, "q2": 1, "q3": 1, "q4": 1, "q5": 0, "q6": 0
        }
        result = self.fager.calculate_score(answers)
        
        assert 'item_scores' in result.dict()
        assert result.item_scores == answers
    
    def test_interpretation_includes_score(self):
        """Test that interpretation includes total score"""
        answers = {
            "q1": 2, "q2": 1, "q3": 1, "q4": 1, "q5": 0, "q6": 0
        }
        result = self.fager.calculate_score(answers)
        
        assert str(result.total_score) in result.interpretation
        assert result.dependence_level in result.interpretation
    
    def test_score_with_invalid_answers_raises_error(self):
        """Test that invalid answers raise FagerstromError"""
        answers = {"q1": 1, "q2": 2}  # Missing items and invalid q2
        
        with pytest.raises(FagerstromError):
            self.fager.calculate_score(answers)


class TestFagerstromCutoffs:
    """Test Fagerström dependence level cutoffs"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.fager = Fagerstrom()
    
    def test_all_cutoff_boundaries(self):
        """Test scoring at all cutoff boundaries"""
        test_cases = [
            (0, "très faible"),
            (1, "très faible"),
            (2, "très faible"),
            (3, "faible"),
            (4, "faible"),
            (5, "moyenne"),
            (6, "forte"),
            (7, "forte"),
            (8, "forte"),
            (9, "forte"),
            (10, "forte")
        ]
        
        for score, expected_level_part in test_cases:
            level = self.fager._get_dependence_level(score)
            assert expected_level_part.lower() in level.lower(), f"Score {score} should contain '{expected_level_part}'"
    
    def test_cutoff_2_to_3(self):
        """Test boundary between very weak and weak (2→3)"""
        # Score 2: very weak
        answers_2 = {"q1": 1, "q2": 1, "q3": 0, "q4": 0, "q5": 0, "q6": 0}
        result_2 = self.fager.calculate_score(answers_2)
        assert result_2.total_score == 2
        assert "très faible" in result_2.dependence_level.lower()
        
        # Score 3: weak
        answers_3 = {"q1": 2, "q2": 1, "q3": 0, "q4": 0, "q5": 0, "q6": 0}
        result_3 = self.fager.calculate_score(answers_3)
        assert result_3.total_score == 3
        assert "faible" in result_3.dependence_level and "très" not in result_3.dependence_level.lower()
    
    def test_cutoff_4_to_5(self):
        """Test boundary between weak and medium (4→5)"""
        # Score 4: weak
        answers_4 = {"q1": 2, "q2": 1, "q3": 1, "q4": 0, "q5": 0, "q6": 0}
        result_4 = self.fager.calculate_score(answers_4)
        assert result_4.total_score == 4
        assert result_4.dependence_level == "Dépendance faible"
        
        # Score 5: medium
        answers_5 = {"q1": 2, "q2": 1, "q3": 1, "q4": 1, "q5": 0, "q6": 0}
        result_5 = self.fager.calculate_score(answers_5)
        assert result_5.total_score == 5
        assert result_5.dependence_level == "Dépendance moyenne"
    
    def test_cutoff_5_to_6(self):
        """Test boundary between medium and strong (5→6)"""
        # Score 5: medium
        answers_5 = {"q1": 2, "q2": 1, "q3": 1, "q4": 1, "q5": 0, "q6": 0}
        result_5 = self.fager.calculate_score(answers_5)
        assert result_5.total_score == 5
        assert result_5.dependence_level == "Dépendance moyenne"
        
        # Score 6: strong
        answers_6 = {"q1": 2, "q2": 1, "q3": 1, "q4": 1, "q5": 1, "q6": 0}
        result_6 = self.fager.calculate_score(answers_6)
        assert result_6.total_score == 6
        assert result_6.dependence_level == "Dépendance forte"


class TestFagerstromEdgeCases:
    """Test edge cases and special scenarios"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.fager = Fagerstrom()
    
    def test_consistent_scoring_multiple_calls(self):
        """Test that scoring is consistent across multiple calls"""
        answers = {
            "q1": 2, "q2": 1, "q3": 1, "q4": 1, "q5": 0, "q6": 0
        }
        
        result1 = self.fager.calculate_score(answers)
        result2 = self.fager.calculate_score(answers)
        result3 = self.fager.calculate_score(answers)
        
        assert result1.total_score == result2.total_score == result3.total_score
        assert result1.dependence_level == result2.dependence_level == result3.dependence_level
    
    def test_all_possible_scores(self):
        """Test that all scores 0-10 produce valid results"""
        for target_score in range(11):
            # Create answer combination for this score
            answers = {"q1": min(3, target_score), "q2": 0, "q3": 0, "q4": 0, "q5": 0, "q6": 0}
            remaining = target_score - answers["q1"]
            
            for q in ["q2", "q3", "q4", "q5", "q6"]:
                if remaining > 0:
                    if q == "q4":
                        answers[q] = min(3, remaining)
                    else:
                        answers[q] = min(1, remaining)
                    remaining -= answers[q]
            
            result = self.fager.calculate_score(answers)
            assert result.total_score == target_score
            assert result.dependence_level is not None
    
    def test_question_ids_are_strings(self):
        """Test that question IDs are strings, not integers"""
        questions = self.fager.get_questions()
        for q in questions:
            assert isinstance(q['id'], str)
            assert q['id'].startswith('q')


class TestFagerstromIntegration:
    """Integration tests for complete Fagerström workflow"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.fager = Fagerstrom()
    
    def test_complete_workflow_no_dependence(self):
        """Test complete workflow for non-dependent smoker"""
        # 1. Get questionnaire
        full = self.fager.get_full_questionnaire()
        assert len(full['questions']) == 6
        
        # 2. Patient answers (no dependence)
        answers = {
            "q1": 0, "q2": 0, "q3": 0, "q4": 0, "q5": 0, "q6": 0
        }
        
        # 3. Validate
        validation = self.fager.validate_answers(answers)
        assert validation.valid is True
        
        # 4. Calculate score
        result = self.fager.calculate_score(answers)
        assert result.total_score == 0
        assert "très faible" in result.dependence_level.lower()
    
    def test_complete_workflow_moderate_smoker(self):
        """Test complete workflow for moderate smoker"""
        # Patient answers (medium dependence)
        answers = {
            "q1": 2, "q2": 1, "q3": 1, "q4": 1, "q5": 0, "q6": 0
        }
        
        # Validate
        validation = self.fager.validate_answers(answers)
        assert validation.valid is True
        
        # Calculate score
        result = self.fager.calculate_score(answers)
        assert result.total_score == 5
        assert result.dependence_level == "Dépendance moyenne"
        assert "substitution nicotinique recommandée" in result.interpretation.lower()
    
    def test_complete_workflow_heavy_smoker(self):
        """Test complete workflow for heavy smoker"""
        # Patient answers (strong dependence)
        answers = {
            "q1": 3, "q2": 1, "q3": 1, "q4": 3, "q5": 1, "q6": 1
        }
        
        # Validate
        validation = self.fager.validate_answers(answers)
        assert validation.valid is True
        assert len(validation.warnings) > 0  # Should have warnings
        
        # Calculate score
        result = self.fager.calculate_score(answers)
        assert result.total_score == 10
        assert result.dependence_level == "Dépendance forte"
        assert "fortement recommandée" in result.interpretation.lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

