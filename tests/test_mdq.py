# -*- coding: utf-8 -*-
"""
Comprehensive unit tests for MDQ questionnaire
Tests metadata, questions, validation, screening logic, and edge cases
"""

import pytest
from questionnaires.mdq import MDQ, MDQError, ScreeningResult, ValidationResult


class TestMDQMetadata:
    """Test MDQ metadata and structure retrieval"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mdq = MDQ()
    
    def test_get_metadata(self):
        """Test metadata retrieval"""
        metadata = self.mdq.get_metadata()
        
        assert metadata['id'] == 'MDQ.fr'
        assert metadata['abbreviation'] == 'MDQ'
        assert metadata['language'] == 'fr-FR'
        assert metadata['version'] == '1.0'
        assert metadata['total_questions'] == 15  # 13 + Q2 + Q3
        assert 'sources' in metadata
        assert 'screening_criteria' in metadata
    
    def test_get_sections(self):
        """Test sections retrieval"""
        sections = self.mdq.get_sections()
        
        assert len(sections) == 2
        assert sections[0]['id'] == 'sec1'
        assert sections[0]['label'] == 'Question 1 (13 items)'
        assert len(sections[0]['question_ids']) == 13
        
        assert sections[1]['id'] == 'sec2'
        assert sections[1]['label'] == 'Questions 2 et 3'
        assert len(sections[1]['question_ids']) == 2
    
    def test_get_all_questions(self):
        """Test retrieving all questions"""
        questions = self.mdq.get_questions()
        
        assert len(questions) == 15  # 13 Q1 items + Q2 + Q3
        assert questions[0]['id'] == 'q1_1'
        assert questions[12]['id'] == 'q1_13'
        assert questions[13]['id'] == 'q2'
        assert questions[14]['id'] == 'q3'
        
        # Check Q1 structure (yes/no)
        q1_1 = questions[0]
        assert len(q1_1['options']) == 2
        assert q1_1['options'][0]['label'] in ['Oui', 'Non']
        
        # Check Q3 structure (0-3 scale)
        q3 = questions[14]
        assert len(q3['options']) == 4
    
    def test_get_questions_by_section(self):
        """Test retrieving questions filtered by section"""
        sec1_questions = self.mdq.get_questions(section_id='sec1')
        sec2_questions = self.mdq.get_questions(section_id='sec2')
        
        assert len(sec1_questions) == 13
        assert len(sec2_questions) == 2
        assert all(q['section_id'] == 'sec1' for q in sec1_questions)
        assert all(q['section_id'] == 'sec2' for q in sec2_questions)
    
    def test_get_question_by_id(self):
        """Test retrieving specific question by ID"""
        q1_1 = self.mdq.get_question_by_id('q1_1')
        assert q1_1 is not None
        assert q1_1['id'] == 'q1_1'
        assert 'bien et si remonté' in q1_1['text']
        
        q2 = self.mdq.get_question_by_id('q2')
        assert q2 is not None
        assert 'même période' in q2['text']
        
        # Non-existent question
        invalid = self.mdq.get_question_by_id('q99')
        assert invalid is None
    
    def test_q1_texts_count(self):
        """Test that all 13 Q1 texts are present"""
        assert len(self.mdq.Q1_TEXTS) == 13
        
        # Verify some key symptom texts
        texts = ' '.join(self.mdq.Q1_TEXTS)
        assert 'irritable' in texts
        assert 'énergie' in texts
        assert 'sommeil' in texts or 'dormiez' in texts
    
    def test_get_full_questionnaire(self):
        """Test getting complete questionnaire structure"""
        full = self.mdq.get_full_questionnaire()
        
        assert 'metadata' in full
        assert 'sections' in full
        assert 'questions' in full
        assert len(full['questions']) == 15
        assert len(full['sections']) == 2


class TestMDQValidation:
    """Test MDQ answer validation"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mdq = MDQ()
    
    def test_valid_answers_all_no(self):
        """Test validation with all 'no' answers"""
        answers = {f"q1_{i}": 0 for i in range(1, 14)}
        answers.update({"q2": 0, "q3": 0})
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_all_yes(self):
        """Test validation with all 'yes' Q1 answers"""
        answers = {f"q1_{i}": 1 for i in range(1, 14)}
        answers.update({"q2": 1, "q3": 3})
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_mixed(self):
        """Test validation with mixed valid answers"""
        answers = {
            "q1_1": 1, "q1_2": 0, "q1_3": 1, "q1_4": 1,
            "q1_5": 0, "q1_6": 1, "q1_7": 0, "q1_8": 1,
            "q1_9": 0, "q1_10": 0, "q1_11": 1, "q1_12": 0,
            "q1_13": 1, "q2": 1, "q3": 2
        }
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_missing_items_error(self):
        """Test validation fails with missing items"""
        answers = {"q1_1": 0, "q1_2": 1, "q2": 0}  # Missing most items
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
        assert "Items manquants" in validation.errors[0]
    
    def test_missing_q2_error(self):
        """Test validation fails when Q2 is missing"""
        answers = {f"q1_{i}": 0 for i in range(1, 14)}
        answers['q3'] = 0  # Q2 missing
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is False
        assert "q2" in validation.errors[0].lower()
    
    def test_missing_q3_error(self):
        """Test validation fails when Q3 is missing"""
        answers = {f"q1_{i}": 0 for i in range(1, 14)}
        answers['q2'] = 0  # Q3 missing
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is False
        assert "q3" in validation.errors[0].lower()
    
    def test_invalid_q1_value_too_high(self):
        """Test validation fails with Q1 values > 1"""
        answers = {f"q1_{i}": 0 for i in range(1, 14)}
        answers['q1_5'] = 2  # Invalid for binary
        answers.update({"q2": 0, "q3": 0})
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
    
    def test_invalid_q2_value(self):
        """Test validation fails with invalid Q2 value"""
        answers = {f"q1_{i}": 0 for i in range(1, 14)}
        answers.update({"q2": 5, "q3": 0})  # Invalid Q2
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is False
        assert "Q2" in validation.errors[0]
    
    def test_invalid_q3_value(self):
        """Test validation fails with invalid Q3 value"""
        answers = {f"q1_{i}": 0 for i in range(1, 14)}
        answers.update({"q2": 0, "q3": 5})  # Invalid Q3 (should be 0-3)
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is False
        assert "Q3" in validation.errors[0]
    
    def test_warning_q3_impact_with_no_symptoms(self):
        """Test warning when Q3 indicates problem but no Q1 symptoms"""
        answers = {f"q1_{i}": 0 for i in range(1, 14)}  # All no
        answers.update({"q2": 0, "q3": 2})  # But moderate problem?
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is True  # Still valid
        assert len(validation.warnings) > 0
        assert any('Q3' in w for w in validation.warnings)
    
    def test_warning_q2_yes_with_few_symptoms(self):
        """Test warning when Q2=yes but <2 symptoms"""
        answers = {f"q1_{i}": 0 for i in range(1, 14)}
        answers['q1_1'] = 1  # Only 1 symptom
        answers.update({"q2": 1, "q3": 0})  # But concurrent?
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is True  # Still valid
        assert len(validation.warnings) > 0
        assert any('Q2' in w for w in validation.warnings)
    
    def test_no_warnings_with_consistent_data(self):
        """Test no warnings with clinically consistent data"""
        answers = {f"q1_{i}": 1 for i in range(1, 8)}  # 7 symptoms
        answers.update({f"q1_{i}": 0 for i in range(8, 14)})
        answers.update({"q2": 1, "q3": 3})
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) == 0


class TestMDQScreening:
    """Test MDQ screening calculation"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mdq = MDQ()
    
    def test_screening_negative_all_no(self):
        """Test negative screening with all 'no' answers"""
        answers = {f"q1_{i}": 0 for i in range(1, 14)}
        answers.update({"q2": 0, "q3": 0})
        
        result = self.mdq.calculate_screening(answers)
        
        assert result.q1_total == 0
        assert result.q2_concurrent is False
        assert result.q3_impact_level == 0
        assert result.q3_impact_label == "Pas de problème"
        assert result.screening_result == "NEGATIF"
    
    def test_screening_negative_insufficient_symptoms(self):
        """Test negative screening with <7 symptoms"""
        answers = {f"q1_{i}": 1 if i <= 6 else 0 for i in range(1, 14)}  # Only 6 yes
        answers.update({"q2": 1, "q3": 3})
        
        result = self.mdq.calculate_screening(answers)
        
        assert result.q1_total == 6
        assert result.screening_result == "NEGATIF"
    
    def test_screening_negative_no_concurrence(self):
        """Test negative screening with symptoms but no concurrence"""
        answers = {f"q1_{i}": 1 for i in range(1, 11)}  # 10 symptoms
        answers.update({f"q1_{i}": 0 for i in range(11, 14)})
        answers.update({"q2": 0, "q3": 3})  # Not concurrent
        
        result = self.mdq.calculate_screening(answers)
        
        assert result.q1_total == 10
        assert result.q2_concurrent is False
        assert result.screening_result == "NEGATIF"
    
    def test_screening_negative_low_impact(self):
        """Test negative screening with symptoms but low impact"""
        answers = {f"q1_{i}": 1 for i in range(1, 11)}  # 10 symptoms
        answers.update({f"q1_{i}": 0 for i in range(11, 14)})
        answers.update({"q2": 1, "q3": 1})  # Minor problem only
        
        result = self.mdq.calculate_screening(answers)
        
        assert result.q1_total == 10
        assert result.q2_concurrent is True
        assert result.q3_impact_level == 1
        assert result.screening_result == "NEGATIF"
    
    def test_screening_positive_minimum_criteria(self):
        """Test positive screening with exactly 7 symptoms"""
        answers = {f"q1_{i}": 1 if i <= 7 else 0 for i in range(1, 14)}  # Exactly 7
        answers.update({"q2": 1, "q3": 2})  # Moderate problem
        
        result = self.mdq.calculate_screening(answers)
        
        assert result.q1_total == 7
        assert result.q2_concurrent is True
        assert result.q3_impact_level == 2
        assert result.q3_impact_label == "Problème moyen"
        assert result.screening_result == "POSITIF"
    
    def test_screening_positive_serious_impact(self):
        """Test positive screening with serious impact"""
        answers = {f"q1_{i}": 1 for i in range(1, 11)}  # 10 symptoms
        answers.update({f"q1_{i}": 0 for i in range(11, 14)})
        answers.update({"q2": 1, "q3": 3})  # Serious problem
        
        result = self.mdq.calculate_screening(answers)
        
        assert result.q1_total == 10
        assert result.q3_impact_level == 3
        assert result.q3_impact_label == "Problème sérieux"
        assert result.screening_result == "POSITIF"
    
    def test_screening_positive_all_symptoms(self):
        """Test positive screening with all 13 symptoms"""
        answers = {f"q1_{i}": 1 for i in range(1, 14)}
        answers.update({"q2": 1, "q3": 3})
        
        result = self.mdq.calculate_screening(answers)
        
        assert result.q1_total == 13
        assert result.screening_result == "POSITIF"
    
    def test_q1_total_calculation(self):
        """Test Q1 total is calculated correctly"""
        answers = {f"q1_{i}": 1 if i % 2 == 1 else 0 for i in range(1, 14)}
        answers.update({"q2": 0, "q3": 0})
        
        result = self.mdq.calculate_screening(answers)
        
        # Odd numbers: 1,3,5,7,9,11,13 = 7 items
        assert result.q1_total == 7
    
    def test_interpretation_positive(self):
        """Test interpretation text for positive screening"""
        answers = {f"q1_{i}": 1 for i in range(1, 11)}
        answers.update({f"q1_{i}": 0 for i in range(11, 14)})
        answers.update({"q2": 1, "q3": 3})
        
        result = self.mdq.calculate_screening(answers)
        
        assert "POSITIF" in result.interpretation
        assert "bipolaire" in result.interpretation.lower()
        assert "évaluation clinique" in result.interpretation.lower()
    
    def test_interpretation_negative(self):
        """Test interpretation text for negative screening"""
        answers = {f"q1_{i}": 0 for i in range(1, 14)}
        answers.update({"q2": 0, "q3": 0})
        
        result = self.mdq.calculate_screening(answers)
        
        assert "NEGATIF" in result.interpretation
    
    def test_interpretation_negative_with_note(self):
        """Test interpretation includes notes for specific negative patterns"""
        # High symptoms but not concurrent
        answers = {f"q1_{i}": 1 for i in range(1, 11)}
        answers.update({f"q1_{i}": 0 for i in range(11, 14)})
        answers.update({"q2": 0, "q3": 0})
        
        result = self.mdq.calculate_screening(answers)
        
        assert result.screening_result == "NEGATIF"
        assert "Note" in result.interpretation or "simultané" in result.interpretation.lower()
    
    def test_screening_with_invalid_answers_raises_error(self):
        """Test that invalid answers raise MDQError"""
        answers = {"q1_1": 0, "q1_2": 1}  # Missing most items
        
        with pytest.raises(MDQError) as exc_info:
            self.mdq.calculate_screening(answers)
        
        assert "Items manquants" in str(exc_info.value)


class TestMDQBoundaryConditions:
    """Test boundary conditions and edge cases"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mdq = MDQ()
    
    def test_boundary_exactly_7_symptoms_positive(self):
        """Test boundary: exactly 7 symptoms with all criteria met"""
        answers = {f"q1_{i}": 1 if i <= 7 else 0 for i in range(1, 14)}
        answers.update({"q2": 1, "q3": 2})
        
        result = self.mdq.calculate_screening(answers)
        assert result.q1_total == 7
        assert result.screening_result == "POSITIF"
    
    def test_boundary_exactly_6_symptoms_negative(self):
        """Test boundary: exactly 6 symptoms (below threshold)"""
        answers = {f"q1_{i}": 1 if i <= 6 else 0 for i in range(1, 14)}
        answers.update({"q2": 1, "q3": 2})
        
        result = self.mdq.calculate_screening(answers)
        assert result.q1_total == 6
        assert result.screening_result == "NEGATIF"
    
    def test_boundary_q3_level_2_moderate_positive(self):
        """Test boundary: Q3=2 (moderate) is sufficient for positive"""
        answers = {f"q1_{i}": 1 for i in range(1, 11)}
        answers.update({f"q1_{i}": 0 for i in range(11, 14)})
        answers.update({"q2": 1, "q3": 2})  # Moderate = sufficient
        
        result = self.mdq.calculate_screening(answers)
        assert result.screening_result == "POSITIF"
    
    def test_boundary_q3_level_1_minor_negative(self):
        """Test boundary: Q3=1 (minor) is not sufficient"""
        answers = {f"q1_{i}": 1 for i in range(1, 11)}
        answers.update({f"q1_{i}": 0 for i in range(11, 14)})
        answers.update({"q2": 1, "q3": 1})  # Minor = insufficient
        
        result = self.mdq.calculate_screening(answers)
        assert result.screening_result == "NEGATIF"
    
    def test_q3_impact_labels_all_levels(self):
        """Test all Q3 impact level labels"""
        base_answers = {f"q1_{i}": 0 for i in range(1, 14)}
        base_answers['q2'] = 0
        
        expected_labels = {
            0: "Pas de problème",
            1: "Problème mineur",
            2: "Problème moyen",
            3: "Problème sérieux"
        }
        
        for level, expected_label in expected_labels.items():
            answers = base_answers.copy()
            answers['q3'] = level
            result = self.mdq.calculate_screening(answers)
            assert result.q3_impact_label == expected_label
    
    def test_all_criteria_must_be_met(self):
        """Test that ALL three criteria must be met for positive"""
        base = {f"q1_{i}": 1 for i in range(1, 11)}  # 10 symptoms
        base.update({f"q1_{i}": 0 for i in range(11, 14)})
        
        # Missing Q2
        answers = base.copy()
        answers.update({"q2": 0, "q3": 3})
        assert self.mdq.calculate_screening(answers).screening_result == "NEGATIF"
        
        # Missing Q3
        answers = base.copy()
        answers.update({"q2": 1, "q3": 0})
        assert self.mdq.calculate_screening(answers).screening_result == "NEGATIF"
        
        # Missing Q1 count
        answers = {f"q1_{i}": 1 if i <= 5 else 0 for i in range(1, 14)}
        answers.update({"q2": 1, "q3": 3})
        assert self.mdq.calculate_screening(answers).screening_result == "NEGATIF"
        
        # All three present
        answers = base.copy()
        answers.update({"q2": 1, "q3": 2})
        assert self.mdq.calculate_screening(answers).screening_result == "POSITIF"
    
    def test_consistent_screening_multiple_calls(self):
        """Test that screening is consistent across multiple calls"""
        answers = {
            "q1_1": 1, "q1_2": 1, "q1_3": 0, "q1_4": 1,
            "q1_5": 1, "q1_6": 0, "q1_7": 1, "q1_8": 1,
            "q1_9": 1, "q1_10": 0, "q1_11": 1, "q1_12": 0,
            "q1_13": 0, "q2": 1, "q3": 2
        }
        
        result1 = self.mdq.calculate_screening(answers)
        result2 = self.mdq.calculate_screening(answers)
        result3 = self.mdq.calculate_screening(answers)
        
        assert result1.q1_total == result2.q1_total == result3.q1_total
        assert result1.screening_result == result2.screening_result == result3.screening_result


class TestMDQSpecialCases:
    """Test special cases and clinical scenarios"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mdq = MDQ()
    
    def test_classic_manic_symptoms_pattern(self):
        """Test classic manic symptom pattern"""
        # Elevated mood, decreased sleep, increased energy, impulsivity, etc.
        answers = {
            "q1_1": 1,  # Elevated mood
            "q1_2": 0,  # Not irritable
            "q1_3": 1,  # More self-confident
            "q1_4": 1,  # Less sleep
            "q1_5": 1,  # More talkative
            "q1_6": 1,  # Racing thoughts
            "q1_7": 1,  # Distractible
            "q1_8": 1,  # More energy
            "q1_9": 1,  # More active
            "q1_10": 0, # Not more social
            "q1_11": 0, # Not more sexual
            "q1_12": 0, # Not risky behavior
            "q1_13": 0, # Not spending money
            "q2": 1,
            "q3": 3
        }
        
        result = self.mdq.calculate_screening(answers)
        assert result.q1_total == 9
        assert result.screening_result == "POSITIF"
    
    def test_irritable_manic_symptoms_pattern(self):
        """Test irritable/dysphoric manic symptom pattern"""
        answers = {
            "q1_1": 0,  # Not elevated
            "q1_2": 1,  # Irritable
            "q1_3": 1,  # More self-confident
            "q1_4": 1,  # Less sleep
            "q1_5": 1,  # More talkative
            "q1_6": 1,  # Racing thoughts
            "q1_7": 1,  # Distractible
            "q1_8": 1,  # More energy
            "q1_9": 0,
            "q1_10": 0,
            "q1_11": 0,
            "q1_12": 0,
            "q1_13": 0,
            "q2": 1,
            "q3": 2
        }
        
        result = self.mdq.calculate_screening(answers)
        assert result.q1_total == 7
        assert result.screening_result == "POSITIF"
    
    def test_subclinical_symptoms(self):
        """Test subclinical symptoms (not enough for positive)"""
        # Few symptoms, low impact
        answers = {
            "q1_1": 1, "q1_2": 0, "q1_3": 1, "q1_4": 0,
            "q1_5": 1, "q1_6": 0, "q1_7": 0, "q1_8": 1,
            "q1_9": 0, "q1_10": 0, "q1_11": 0, "q1_12": 0,
            "q1_13": 0, "q2": 1, "q3": 1
        }
        
        result = self.mdq.calculate_screening(answers)
        assert result.q1_total == 4
        assert result.screening_result == "NEGATIF"
    
    def test_non_concurrent_episodes(self):
        """Test symptoms that occurred at different times"""
        # Many symptoms but not concurrent
        answers = {f"q1_{i}": 1 for i in range(1, 12)}  # 11 symptoms
        answers.update({f"q1_{i}": 0 for i in range(12, 14)})
        answers.update({"q2": 0, "q3": 2})  # Not same time
        
        result = self.mdq.calculate_screening(answers)
        assert result.q1_total == 11
        assert result.q2_concurrent is False
        assert result.screening_result == "NEGATIF"
        assert "simultané" in result.interpretation.lower()
    
    def test_symptoms_without_impairment(self):
        """Test symptoms without functional impairment"""
        # Many concurrent symptoms but no/minor problem
        answers = {f"q1_{i}": 1 for i in range(1, 11)}
        answers.update({f"q1_{i}": 0 for i in range(11, 14)})
        answers.update({"q2": 1, "q3": 0})  # No problem
        
        result = self.mdq.calculate_screening(answers)
        assert result.q1_total == 10
        assert result.q2_concurrent is True
        assert result.screening_result == "NEGATIF"
        assert "impact" in result.interpretation.lower()


class TestMDQIntegration:
    """Integration tests for complete MDQ workflow"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mdq = MDQ()
    
    def test_complete_workflow_positive_case(self):
        """Test complete workflow for a positive case"""
        # 1. Get questionnaire
        full = self.mdq.get_full_questionnaire()
        assert len(full['questions']) == 15
        
        # 2. Simulate user filling out questionnaire
        answers = {f"q1_{i}": 1 for i in range(1, 10)}
        answers.update({f"q1_{i}": 0 for i in range(10, 14)})
        answers.update({"q2": 1, "q3": 3})
        
        # 3. Validate
        validation = self.mdq.validate_answers(answers)
        assert validation.valid is True
        
        # 4. Calculate screening
        result = self.mdq.calculate_screening(answers)
        assert result.screening_result == "POSITIF"
        assert "clinique" in result.interpretation.lower()
    
    def test_complete_workflow_negative_case(self):
        """Test complete workflow for a negative case"""
        # 1. Get questionnaire structure
        questions = self.mdq.get_questions()
        assert len(questions) == 15
        
        # 2. User answers (mostly no)
        answers = {f"q1_{i}": 0 for i in range(1, 14)}
        answers.update({"q2": 0, "q3": 0})
        
        # 3. Validate
        validation = self.mdq.validate_answers(answers)
        assert validation.valid is True
        assert len(validation.warnings) == 0
        
        # 4. Calculate screening
        result = self.mdq.calculate_screening(answers)
        assert result.screening_result == "NEGATIF"
        assert result.q1_total == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

