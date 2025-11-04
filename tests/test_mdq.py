# -*- coding: utf-8 -*-
"""
Comprehensive unit tests for MDQ questionnaire
Tests metadata, questions, validation, screening logic, and edge cases
"""

import pytest
from questionnaires.auto.mdq import MDQ, MDQError, ScreeningResult, ValidationResult


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
        assert "Q1 manquants" in validation.errors[0]
    
    def test_missing_q2_error(self):
        """Test validation fails when Q2 is missing but required (Q1 >= 2)"""
        answers = {f"q1_{i}": 1 if i <= 2 else 0 for i in range(1, 14)}  # sum=2, Q2 required
        answers['q3'] = 0  # Q2 missing
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is False
        assert "Q2" in validation.errors[0]
    
    def test_missing_q3_error(self):
        """Test validation fails when Q3 is missing but required (Q1 >= 2)"""
        answers = {f"q1_{i}": 1 if i <= 2 else 0 for i in range(1, 14)}  # sum=2, Q3 required
        answers['q2'] = 0  # Q3 missing
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is False
        assert "Q3" in validation.errors[0]
    
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
        
        assert "Q1 manquants" in str(exc_info.value)


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
        assert result.q1_total == 8
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
        # With conditional logic, Q2 and Q3 should trigger warnings since Q1 sum < 2
        assert len(validation.warnings) == 2
        
        # 4. Calculate screening
        result = self.mdq.calculate_screening(answers)
        assert result.screening_result == "NEGATIF"
        assert result.q1_total == 0


class TestMDQBranchingLogic:
    """Test MDQ branching logic and conditional display/requirements"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mdq = MDQ()
    
    def test_get_branching_logic(self):
        """Test branching logic method returns proper structure"""
        logic = self.mdq.get_branching_logic()
        
        assert logic is not None
        assert logic['schema_version'] == '1.0'
        assert logic['type'] == 'answer_dependent'
        assert 'rules' in logic
        assert 'context_variables' in logic
        assert 'fallback_behavior' in logic
        assert 'scoring_impact' in logic
    
    def test_branching_logic_has_q2_rules(self):
        """Test Q2 has visibility and requirement rules"""
        logic = self.mdq.get_branching_logic()
        rules = logic['rules']
        
        # Find Q2 rules
        q2_visibility = next((r for r in rules if r['rule_id'] == 'q2_visibility'), None)
        q2_requirement = next((r for r in rules if r['rule_id'] == 'q2_requirement'), None)
        
        assert q2_visibility is not None
        assert q2_visibility['question_id'] == 'q2'
        assert q2_visibility['rule_type'] == 'display'
        assert 'condition' in q2_visibility
        
        assert q2_requirement is not None
        assert q2_requirement['question_id'] == 'q2'
        assert q2_requirement['rule_type'] == 'required'
    
    def test_branching_logic_has_q3_rules(self):
        """Test Q3 has visibility and requirement rules"""
        logic = self.mdq.get_branching_logic()
        rules = logic['rules']
        
        # Find Q3 rules
        q3_visibility = next((r for r in rules if r['rule_id'] == 'q3_visibility'), None)
        q3_requirement = next((r for r in rules if r['rule_id'] == 'q3_requirement'), None)
        
        assert q3_visibility is not None
        assert q3_visibility['question_id'] == 'q3'
        assert q3_visibility['rule_type'] == 'display'
        
        assert q3_requirement is not None
        assert q3_requirement['question_id'] == 'q3'
        assert q3_requirement['rule_type'] == 'required'
    
    def test_branching_logic_context_variables(self):
        """Test context variables are properly defined"""
        logic = self.mdq.get_branching_logic()
        context = logic['context_variables']
        
        assert 'q1_sum' in context
        assert context['q1_sum']['source'] == 'calculated'
        assert context['q1_sum']['type'] == 'integer'
        assert context['q1_sum']['range'] == [0, 13]
        assert 'formula' in context['q1_sum']
    
    def test_branching_logic_fallback_behavior(self):
        """Test fallback behavior is defined"""
        logic = self.mdq.get_branching_logic()
        fallback = logic['fallback_behavior']
        
        assert 'when_q1_sum_lt_2' in fallback
        assert fallback['when_q1_sum_lt_2']['q2'] == 'hide'
        assert fallback['when_q1_sum_lt_2']['q3'] == 'hide'
        assert 'validation' in fallback
    
    def test_branching_logic_scoring_impact(self):
        """Test scoring impact is documented"""
        logic = self.mdq.get_branching_logic()
        scoring = logic['scoring_impact']
        
        assert 'description' in scoring
        assert 'screening_threshold' in scoring
        assert 'positive_if' in scoring['screening_threshold']
    
    def test_display_if_present_on_q2(self):
        """Test Q2 has display_if condition"""
        questions = self.mdq.get_questions()
        q2 = next(q for q in questions if q['id'] == 'q2')
        
        assert 'display_if' in q2
        assert q2['display_if'] is not None
        assert '>=' in q2['display_if']
    
    def test_display_if_present_on_q3(self):
        """Test Q3 has display_if condition"""
        questions = self.mdq.get_questions()
        q3 = next(q for q in questions if q['id'] == 'q3')
        
        assert 'display_if' in q3
        assert q3['display_if'] is not None
        assert '>=' in q3['display_if']
    
    def test_required_if_present_on_q2(self):
        """Test Q2 has required_if condition"""
        questions = self.mdq.get_questions()
        q2 = next(q for q in questions if q['id'] == 'q2')
        
        assert 'required_if' in q2
        assert q2['required_if'] is not None
        assert '>=' in q2['required_if']
    
    def test_required_if_present_on_q3(self):
        """Test Q3 has required_if condition"""
        questions = self.mdq.get_questions()
        q3 = next(q for q in questions if q['id'] == 'q3')
        
        assert 'required_if' in q3
        assert q3['required_if'] is not None
        assert '>=' in q3['required_if']
    
    def test_q2_required_is_false_by_default(self):
        """Test Q2 is not hard-required (conditional requirement)"""
        questions = self.mdq.get_questions()
        q2 = next(q for q in questions if q['id'] == 'q2')
        
        assert q2['required'] is False
    
    def test_q3_required_is_false_by_default(self):
        """Test Q3 is not hard-required (conditional requirement)"""
        questions = self.mdq.get_questions()
        q3 = next(q for q in questions if q['id'] == 'q3')
        
        assert q3['required'] is False
    
    def test_q1_items_always_required(self):
        """Test Q1 items are always required (no conditions)"""
        questions = self.mdq.get_questions()
        q1_items = [q for q in questions if q['id'].startswith('q1_')]
        
        for q1 in q1_items:
            assert q1['required'] is True
            assert q1.get('display_if') is None
            assert q1.get('required_if') is None
    
    def test_full_questionnaire_includes_logic_by_default(self):
        """Test get_full_questionnaire includes logic by default"""
        full = self.mdq.get_full_questionnaire()
        
        assert 'logic' in full
        assert full['logic']['type'] == 'answer_dependent'
    
    def test_full_questionnaire_can_exclude_logic(self):
        """Test get_full_questionnaire can exclude logic"""
        full = self.mdq.get_full_questionnaire(include_logic=False)
        
        assert 'logic' not in full
        assert 'metadata' in full
        assert 'questions' in full


class TestMDQConditionalValidation:
    """Test conditional validation based on Q1 sum"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mdq = MDQ()
    
    def test_validation_q1_lt_2_q2_not_required(self):
        """Test Q2 is not required when Q1 sum < 2"""
        answers = {f"q1_{i}": 0 for i in range(1, 14)}  # All no (sum=0)
        # Intentionally omit Q2 and Q3
        
        validation = self.mdq.validate_answers(answers)
        
        # With conditional logic, Q2 and Q3 are NOT required when Q1 sum < 2
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_validation_q1_exactly_1_q2_not_required(self):
        """Test Q2 is not required when Q1 sum = 1"""
        answers = {f"q1_{i}": 0 for i in range(1, 14)}
        answers['q1_1'] = 1  # Only 1 yes (sum=1)
        # Omit Q2 and Q3
        
        validation = self.mdq.validate_answers(answers)
        
        # With conditional logic, Q2 and Q3 are NOT required when Q1 sum < 2
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_validation_q1_exactly_2_q2_required(self):
        """Test Q2 is required when Q1 sum = 2"""
        answers = {f"q1_{i}": 0 for i in range(1, 14)}
        answers['q1_1'] = 1
        answers['q1_2'] = 1  # sum=2
        # Omit Q2 and Q3
        
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is False
        assert any('Q2' in e for e in validation.errors)
    
    def test_validation_q1_gte_2_both_required(self):
        """Test Q2 and Q3 are both required when Q1 sum >= 2"""
        answers = {f"q1_{i}": 1 if i <= 3 else 0 for i in range(1, 14)}  # sum=3
        # Omit Q2 and Q3
        
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is False
        assert any('Q2' in e for e in validation.errors)
        assert any('Q3' in e for e in validation.errors)
    
    def test_validation_q1_lt_2_with_q2_warning(self):
        """Test warning when Q2 provided but Q1 sum < 2"""
        answers = {f"q1_{i}": 0 for i in range(1, 14)}  # sum=0
        answers['q2'] = 0
        answers['q3'] = 0
        
        validation = self.mdq.validate_answers(answers)
        
        # Should have warning that Q2/Q3 shouldn't be present
        assert validation.valid is True  # No hard error
        assert len(validation.warnings) > 0
        assert any('Q2' in w for w in validation.warnings)
    
    def test_validation_q1_lt_2_with_q3_warning(self):
        """Test warning when Q3 provided but Q1 sum < 2"""
        answers = {f"q1_{i}": 0 for i in range(1, 14)}
        answers['q1_1'] = 1  # sum=1
        answers['q2'] = 0
        answers['q3'] = 1
        
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) > 0
        assert any('Q3' in w for w in validation.warnings)
    
    def test_validation_q1_gte_2_with_all_answers_valid(self):
        """Test valid when Q1 >= 2 and Q2/Q3 provided"""
        answers = {f"q1_{i}": 1 if i <= 3 else 0 for i in range(1, 14)}  # sum=3
        answers['q2'] = 1
        answers['q3'] = 2
        
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_validation_boundary_q1_2_with_q2_only(self):
        """Test Q1=2 with only Q2 (missing Q3)"""
        answers = {f"q1_{i}": 1 if i <= 2 else 0 for i in range(1, 14)}  # sum=2
        answers['q2'] = 1
        # Omit Q3
        
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is False
        assert any('Q3' in e for e in validation.errors)
    
    def test_validation_boundary_q1_2_with_q3_only(self):
        """Test Q1=2 with only Q3 (missing Q2)"""
        answers = {f"q1_{i}": 1 if i <= 2 else 0 for i in range(1, 14)}  # sum=2
        answers['q3'] = 2
        # Omit Q2
        
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is False
        assert any('Q2' in e for e in validation.errors)
    
    def test_validation_q1_7_requires_q2_q3(self):
        """Test Q1=7 (screening threshold) still requires Q2/Q3"""
        answers = {f"q1_{i}": 1 if i <= 7 else 0 for i in range(1, 14)}  # sum=7
        # Omit Q2 and Q3
        
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is False
        assert any('Q2' in e for e in validation.errors)
        assert any('Q3' in e for e in validation.errors)


class TestMDQConditionalLogicEdgeCases:
    """Test edge cases for conditional logic"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.mdq = MDQ()
    
    def test_q1_all_zeros_no_q2_q3_warnings(self):
        """Test all Q1 zeros with provided Q2/Q3 generates warnings"""
        answers = {f"q1_{i}": 0 for i in range(1, 14)}  # sum=0
        answers['q2'] = 0
        answers['q3'] = 0
        
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) == 2  # Both Q2 and Q3 shouldn't be present
    
    def test_q1_exactly_13_requires_q2_q3(self):
        """Test Q1 all ones (sum=13) requires Q2/Q3"""
        answers = {f"q1_{i}": 1 for i in range(1, 14)}  # sum=13
        answers['q2'] = 1
        answers['q3'] = 3
        
        validation = self.mdq.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_screening_with_hidden_q2_q3(self):
        """Test screening calculation when Q2/Q3 should be hidden"""
        answers = {f"q1_{i}": 0 for i in range(1, 14)}  # sum=0, Q2/Q3 hidden
        answers['q2'] = 0
        answers['q3'] = 0
        
        # Should still calculate (with warnings)
        result = self.mdq.calculate_screening(answers)
        
        assert result.q1_total == 0
        assert result.screening_result == "NEGATIF"
    
    def test_screening_with_visible_q2_q3(self):
        """Test screening calculation when Q2/Q3 should be visible"""
        answers = {f"q1_{i}": 1 if i <= 8 else 0 for i in range(1, 14)}  # sum=8
        answers['q2'] = 1
        answers['q3'] = 3
        
        result = self.mdq.calculate_screening(answers)
        
        assert result.q1_total == 8
        assert result.screening_result == "POSITIF"
    
    def test_consistency_validation_then_screening(self):
        """Test validation and screening are consistent"""
        answers = {f"q1_{i}": 1 if i <= 5 else 0 for i in range(1, 14)}  # sum=5
        answers['q2'] = 1
        answers['q3'] = 2
        
        validation = self.mdq.validate_answers(answers)
        assert validation.valid is True
        
        result = self.mdq.calculate_screening(answers)
        assert result.q1_total == 5
        assert result.screening_result == "NEGATIF"  # < 7
    
    def test_jsonlogic_condition_structure_q2(self):
        """Test Q2 JSONLogic condition has correct structure"""
        questions = self.mdq.get_questions()
        q2 = next(q for q in questions if q['id'] == 'q2')
        
        condition = q2['display_if']
        
        # Should be: {">=" : [{"+": [...]}, 2]}
        assert '>=' in condition
        assert isinstance(condition['>='], list)
        assert len(condition['>=']) == 2
        assert '+' in condition['>='][0]
        assert condition['>='][1] == 2
    
    def test_jsonlogic_condition_structure_q3(self):
        """Test Q3 JSONLogic condition has correct structure"""
        questions = self.mdq.get_questions()
        q3 = next(q for q in questions if q['id'] == 'q3')
        
        condition = q3['display_if']
        
        # Same structure as Q2
        assert '>=' in condition
        assert isinstance(condition['>='], list)
        assert len(condition['>=']) == 2
        assert '+' in condition['>='][0]
        assert condition['>='][1] == 2
    
    def test_required_if_matches_display_if_q2(self):
        """Test Q2 required_if matches display_if"""
        questions = self.mdq.get_questions()
        q2 = next(q for q in questions if q['id'] == 'q2')
        
        assert q2['display_if'] == q2['required_if']
    
    def test_required_if_matches_display_if_q3(self):
        """Test Q3 required_if matches display_if"""
        questions = self.mdq.get_questions()
        q3 = next(q for q in questions if q['id'] == 'q3')
        
        assert q3['display_if'] == q3['required_if']


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

