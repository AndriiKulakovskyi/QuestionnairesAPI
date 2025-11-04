# -*- coding: utf-8 -*-
"""
Comprehensive unit tests for QIDS-SR16 questionnaire
Tests metadata, questions, validation, scoring logic, and edge cases
"""

import pytest
from questionnaires.auto.qids import QIDSSR16, QIDSError, ScoreResult, ValidationResult


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
            "q1": 2, "q2": 0, "q3": 0, "q4": 0,  # max=2
            "q5": 1, "q6": 1, "q7": 0, "q8": 0,  # max=1
            "q9": 0, "q10": 1, "q11": 1, "q12": 1,
            "q13": 1, "q14": 1, "q15": 1, "q16": 0  # max=1
        }
        # Expected: max(2,0,0,0) + 1 + max(1,0,0,0) + 1 + 1 + 1 + 1 + 1 + max(1,0) = 2+1+1+1+1+1+1+1+1 = 10
        result = self.qids.calculate_score(answers)
        assert result.total_score == 10
        assert result.severity == "Dépression légère"
        
        # Score exactly 11 by increasing Q10
        answers['q10'] = 2
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


class TestQIDSSR16ScoringRules:
    """Test QIDS-SR16 explicit scoring rules"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.qids = QIDSSR16()
    
    def test_get_scoring_rules_exists(self):
        """Test get_scoring_rules method exists and returns structure"""
        rules = self.qids.get_scoring_rules()
        
        assert rules is not None
        assert isinstance(rules, dict)
        assert rules['schema_version'] == '1.0'
        assert rules['type'] == 'mutually_exclusive_groups'
    
    def test_scoring_rules_has_sleep_domain(self):
        """Test scoring rules include sleep domain (Q1-4)"""
        rules = self.qids.get_scoring_rules()
        domains = rules['domains']
        
        sleep_domain = next((d for d in domains if d['id'] == 'sleep'), None)
        assert sleep_domain is not None
        assert sleep_domain['label'] == 'Sommeil'
        assert sleep_domain['items'] == ['q1', 'q2', 'q3', 'q4']
        assert sleep_domain['aggregation'] == 'max'
        assert sleep_domain['range'] == [0, 3]
    
    def test_scoring_rules_has_appetite_weight_domain(self):
        """Test scoring rules include appetite/weight domain (Q6-9)"""
        rules = self.qids.get_scoring_rules()
        domains = rules['domains']
        
        appetite_domain = next((d for d in domains if d['id'] == 'appetite_weight'), None)
        assert appetite_domain is not None
        assert appetite_domain['label'] == 'Appétit/Poids'
        assert appetite_domain['items'] == ['q6', 'q7', 'q8', 'q9']
        assert appetite_domain['aggregation'] == 'max'
        assert appetite_domain['range'] == [0, 3]
    
    def test_scoring_rules_has_psychomotor_domain(self):
        """Test scoring rules include psychomotor domain (Q15-16)"""
        rules = self.qids.get_scoring_rules()
        domains = rules['domains']
        
        psychomotor_domain = next((d for d in domains if d['id'] == 'psychomotor'), None)
        assert psychomotor_domain is not None
        assert psychomotor_domain['label'] == 'Psychomoteur'
        assert psychomotor_domain['items'] == ['q15', 'q16']
        assert psychomotor_domain['aggregation'] == 'max'
        assert psychomotor_domain['range'] == [0, 3]
    
    def test_scoring_rules_has_direct_items(self):
        """Test scoring rules include direct items (Q5, Q10-14)"""
        rules = self.qids.get_scoring_rules()
        direct_items = rules['direct_items']
        
        assert len(direct_items) == 6
        direct_ids = [item['id'] for item in direct_items]
        assert 'q5' in direct_ids
        assert 'q10' in direct_ids
        assert 'q11' in direct_ids
        assert 'q12' in direct_ids
        assert 'q13' in direct_ids
        assert 'q14' in direct_ids
        
        # All direct items should have aggregation="direct"
        for item in direct_items:
            assert item['aggregation'] == 'direct'
    
    def test_scoring_rules_total_formula(self):
        """Test scoring rules include total formula"""
        rules = self.qids.get_scoring_rules()
        total = rules['total']
        
        assert 'formula' in total
        assert 'formula_expanded' in total
        assert total['range'] == [0, 27]
        assert 'max(q1,q2,q3,q4)' in total['formula']
        assert 'max(q6,q7,q8,q9)' in total['formula']
        assert 'max(q15,q16)' in total['formula']
    
    def test_scoring_rules_policies(self):
        """Test scoring rules include policies"""
        rules = self.qids.get_scoring_rules()
        policies = rules['policies']
        
        assert 'missing' in policies
        assert policies['missing'] == 'error'
        assert 'ties' in policies
        assert policies['ties'] == 'keep_max'
    
    def test_scoring_rules_validation_structure(self):
        """Test scoring rules include validation structure"""
        rules = self.qids.get_scoring_rules()
        validation = rules['validation']
        
        assert 'check_mutual_exclusivity' in validation
        assert validation['check_mutual_exclusivity'] is True
        assert 'warning_if_both_endorsed' in validation
    
    def test_scoring_rules_validation_sleep_warnings(self):
        """Test scoring rules include sleep domain warnings"""
        rules = self.qids.get_scoring_rules()
        warnings = rules['validation']['warning_if_both_endorsed']
        
        sleep_warnings = next((g for g in warnings if g['group'] == 'sleep'), None)
        assert sleep_warnings is not None
        assert len(sleep_warnings['pairs']) > 0
    
    def test_scoring_rules_validation_appetite_warnings(self):
        """Test scoring rules include appetite/weight warnings"""
        rules = self.qids.get_scoring_rules()
        warnings = rules['validation']['warning_if_both_endorsed']
        
        appetite_warnings = next((g for g in warnings if g['group'] == 'appetite_weight'), None)
        assert appetite_warnings is not None
        assert len(appetite_warnings['pairs']) >= 2  # appetite AND weight pairs
    
    def test_scoring_rules_validation_psychomotor_warnings(self):
        """Test scoring rules include psychomotor warnings"""
        rules = self.qids.get_scoring_rules()
        warnings = rules['validation']['warning_if_both_endorsed']
        
        psychomotor_warnings = next((g for g in warnings if g['group'] == 'psychomotor'), None)
        assert psychomotor_warnings is not None
        assert len(psychomotor_warnings['pairs']) > 0
    
    def test_scoring_rules_interpretation_thresholds(self):
        """Test scoring rules include interpretation thresholds"""
        rules = self.qids.get_scoring_rules()
        thresholds = rules['interpretation_thresholds']
        
        assert 'none' in thresholds
        assert thresholds['none'] == [0, 5]
        assert 'mild' in thresholds
        assert thresholds['mild'] == [6, 10]
        assert 'moderate' in thresholds
        assert thresholds['moderate'] == [11, 15]
        assert 'severe' in thresholds
        assert thresholds['severe'] == [16, 20]
        assert 'very_severe' in thresholds
        assert thresholds['very_severe'] == [21, 27]
    
    def test_scoring_metadata_on_sleep_questions(self):
        """Test Q1-4 have scoring metadata"""
        questions = self.qids.get_questions()
        sleep_questions = [q for q in questions if q['id'] in ['q1', 'q2', 'q3', 'q4']]
        
        assert len(sleep_questions) == 4
        for q in sleep_questions:
            assert q.get('scoring_group_id') == 'sleep'
            assert q.get('scoring_aggregation') == 'max'
    
    def test_scoring_metadata_on_appetite_questions(self):
        """Test Q6-9 have scoring metadata"""
        questions = self.qids.get_questions()
        appetite_questions = [q for q in questions if q['id'] in ['q6', 'q7', 'q8', 'q9']]
        
        assert len(appetite_questions) == 4
        for q in appetite_questions:
            assert q.get('scoring_group_id') == 'appetite_weight'
            assert q.get('scoring_aggregation') == 'max'
    
    def test_scoring_metadata_on_psychomotor_questions(self):
        """Test Q15-16 have scoring metadata"""
        questions = self.qids.get_questions()
        psychomotor_questions = [q for q in questions if q['id'] in ['q15', 'q16']]
        
        assert len(psychomotor_questions) == 2
        for q in psychomotor_questions:
            assert q.get('scoring_group_id') == 'psychomotor'
            assert q.get('scoring_aggregation') == 'max'
    
    def test_scoring_metadata_on_direct_questions(self):
        """Test Q5, Q10-14 don't have scoring_group_id"""
        questions = self.qids.get_questions()
        direct_questions = [q for q in questions if q['id'] in ['q5', 'q10', 'q11', 'q12', 'q13', 'q14']]
        
        assert len(direct_questions) == 6
        for q in direct_questions:
            assert q.get('scoring_group_id') is None
            assert q.get('scoring_aggregation') is None


class TestQIDSSR16MutualExclusivity:
    """Test mutual exclusivity logic in scoring"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.qids = QIDSSR16()
    
    def test_sleep_group_uses_max(self):
        """Test sleep group (Q1-4) uses max scoring"""
        # Q1=3, Q2=1, Q3=2, Q4=0, rest=0
        answers = {f"q{i}": 0 for i in range(1, 17)}
        answers.update({"q1": 3, "q2": 1, "q3": 2, "q4": 0})
        
        result = self.qids.calculate_score(answers)
        
        # Sleep contribution should be max(3,1,2,0) = 3
        # Total = 3 + 0 (all others)
        assert result.total_score == 3
    
    def test_appetite_weight_group_uses_max(self):
        """Test appetite/weight group (Q6-9) uses max scoring"""
        # Q6=0, Q7=3, Q8=1, Q9=2, rest=0
        answers = {f"q{i}": 0 for i in range(1, 17)}
        answers.update({"q6": 0, "q7": 3, "q8": 1, "q9": 2})
        
        result = self.qids.calculate_score(answers)
        
        # Appetite contribution should be max(0,3,1,2) = 3
        assert result.total_score == 3
    
    def test_psychomotor_group_uses_max(self):
        """Test psychomotor group (Q15-16) uses max scoring"""
        # Q15=3, Q16=1, rest=0
        answers = {f"q{i}": 0 for i in range(1, 17)}
        answers.update({"q15": 3, "q16": 1})
        
        result = self.qids.calculate_score(answers)
        
        # Psychomotor contribution should be max(3,1) = 3
        assert result.total_score == 3
    
    def test_all_groups_combined_max_logic(self):
        """Test all groups combined use max logic correctly"""
        answers = {
            "q1": 2, "q2": 3, "q3": 1, "q4": 0,  # max=3
            "q5": 2,  # direct
            "q6": 1, "q7": 0, "q8": 3, "q9": 2,  # max=3
            "q10": 1, "q11": 2, "q12": 0, "q13": 1, "q14": 2,  # direct sum=6
            "q15": 2, "q16": 1  # max=2
        }
        
        result = self.qids.calculate_score(answers)
        
        # Expected: max(2,3,1,0) + 2 + max(1,0,3,2) + 1 + 2 + 0 + 1 + 2 + max(2,1)
        #         = 3 + 2 + 3 + 1 + 2 + 0 + 1 + 2 + 2 = 16
        assert result.total_score == 16
    
    def test_max_score_with_all_threes(self):
        """Test maximum possible score (27)"""
        # Max in each group + all direct items at 3
        answers = {
            "q1": 3, "q2": 0, "q3": 0, "q4": 0,  # max=3
            "q5": 3,
            "q6": 3, "q7": 0, "q8": 0, "q9": 0,  # max=3
            "q10": 3, "q11": 3, "q12": 3, "q13": 3, "q14": 3,  # sum=15
            "q15": 3, "q16": 0  # max=3
        }
        
        result = self.qids.calculate_score(answers)
        
        # Expected: 3 + 3 + 3 + 15 + 3 = 27
        assert result.total_score == 27
        assert result.severity == "Dépression très sévère"
    
    def test_sleep_insomnia_vs_hypersomnia(self):
        """Test insomnia (Q1-3) vs hypersomnia (Q4) mutual exclusivity"""
        # Insomnia pattern
        answers1 = {f"q{i}": 0 for i in range(1, 17)}
        answers1.update({"q1": 3, "q2": 2, "q3": 2, "q4": 0})
        result1 = self.qids.calculate_score(answers1)
        
        # Hypersomnia pattern
        answers2 = {f"q{i}": 0 for i in range(1, 17)}
        answers2.update({"q1": 0, "q2": 0, "q3": 0, "q4": 3})
        result2 = self.qids.calculate_score(answers2)
        
        # Both should contribute max=3 to total
        assert result1.total_score == 3
        assert result2.total_score == 3
    
    def test_appetite_decrease_vs_increase(self):
        """Test appetite decrease (Q6) vs increase (Q7) mutual exclusivity"""
        # Decreased appetite
        answers1 = {f"q{i}": 0 for i in range(1, 17)}
        answers1.update({"q6": 3, "q7": 0, "q8": 0, "q9": 0})
        result1 = self.qids.calculate_score(answers1)
        
        # Increased appetite
        answers2 = {f"q{i}": 0 for i in range(1, 17)}
        answers2.update({"q6": 0, "q7": 3, "q8": 0, "q9": 0})
        result2 = self.qids.calculate_score(answers2)
        
        # Both should contribute max=3
        assert result1.total_score == 3
        assert result2.total_score == 3
    
    def test_weight_loss_vs_gain(self):
        """Test weight loss (Q8) vs gain (Q9) mutual exclusivity"""
        # Weight loss
        answers1 = {f"q{i}": 0 for i in range(1, 17)}
        answers1.update({"q6": 0, "q7": 0, "q8": 3, "q9": 0})
        result1 = self.qids.calculate_score(answers1)
        
        # Weight gain
        answers2 = {f"q{i}": 0 for i in range(1, 17)}
        answers2.update({"q6": 0, "q7": 0, "q8": 0, "q9": 3})
        result2 = self.qids.calculate_score(answers2)
        
        # Both should contribute max=3
        assert result1.total_score == 3
        assert result2.total_score == 3
    
    def test_psychomotor_slowing_vs_agitation(self):
        """Test psychomotor slowing (Q15) vs agitation (Q16) mutual exclusivity"""
        # Slowing
        answers1 = {f"q{i}": 0 for i in range(1, 17)}
        answers1.update({"q15": 3, "q16": 0})
        result1 = self.qids.calculate_score(answers1)
        
        # Agitation
        answers2 = {f"q{i}": 0 for i in range(1, 17)}
        answers2.update({"q15": 0, "q16": 3})
        result2 = self.qids.calculate_score(answers2)
        
        # Both should contribute max=3
        assert result1.total_score == 3
        assert result2.total_score == 3


class TestQIDSSR16ScoringRulesIntegration:
    """Test integration of scoring rules with actual scoring"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.qids = QIDSSR16()
    
    def test_scoring_rules_match_actual_calculation_min(self):
        """Test scoring rules match actual calculation for minimum score"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        result = self.qids.calculate_score(answers)
        rules = self.qids.get_scoring_rules()
        
        assert result.total_score == rules['total']['range'][0]
        assert result.total_score == 0
    
    def test_scoring_rules_match_actual_calculation_max(self):
        """Test scoring rules match actual calculation for maximum score"""
        # Ensure max in each domain
        answers = {
            "q1": 3, "q2": 0, "q3": 0, "q4": 0,
            "q5": 3,
            "q6": 3, "q7": 0, "q8": 0, "q9": 0,
            "q10": 3, "q11": 3, "q12": 3, "q13": 3, "q14": 3,
            "q15": 3, "q16": 0
        }
        result = self.qids.calculate_score(answers)
        rules = self.qids.get_scoring_rules()
        
        assert result.total_score == rules['total']['range'][1]
        assert result.total_score == 27
    
    def test_scoring_rules_thresholds_match_interpretation(self):
        """Test scoring rules thresholds match interpretation"""
        rules = self.qids.get_scoring_rules()
        thresholds = rules['interpretation_thresholds']
        
        # Test each severity level
        test_scores = {
            'none': 3,
            'mild': 8,
            'moderate': 13,
            'severe': 18,
            'very_severe': 25
        }
        
        for severity_key, test_score in test_scores.items():
            answers = self._create_answers_for_score(test_score)
            result = self.qids.calculate_score(answers)
            
            # Check score is within threshold range
            threshold_min, threshold_max = thresholds[severity_key]
            assert threshold_min <= result.total_score <= threshold_max
    
    def _create_answers_for_score(self, target_score: int) -> dict:
        """Helper to create answers that produce a specific score"""
        answers = {f"q{i}": 0 for i in range(1, 17)}
        
        # Distribute score across direct items first
        remaining = target_score
        direct_items = ['q5', 'q10', 'q11', 'q12', 'q13', 'q14']
        
        for item in direct_items:
            if remaining >= 3:
                answers[item] = 3
                remaining -= 3
            else:
                answers[item] = remaining
                remaining = 0
                break
        
        # Add to grouped items if needed
        if remaining > 0:
            if remaining >= 3:
                answers['q1'] = 3
                remaining -= 3
            else:
                answers['q1'] = remaining
                remaining = 0
        
        if remaining > 0:
            if remaining >= 3:
                answers['q6'] = 3
                remaining -= 3
            else:
                answers['q6'] = remaining
                remaining = 0
        
        if remaining > 0:
            answers['q15'] = min(remaining, 3)
        
        return answers


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

