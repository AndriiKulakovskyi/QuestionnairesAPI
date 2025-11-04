# -*- coding: utf-8 -*-
"""
Comprehensive unit tests for PRISE-M questionnaire
Tests metadata, questions, validation, scoring logic with gender-specific items
"""

import pytest
from questionnaires.auto.prise_m import PRISEM, PRISEMError, ScoreResult, ValidationResult


class TestPRISEMMetadata:
    """Test PRISE-M metadata and structure retrieval"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.prisem = PRISEM()
    
    def test_get_metadata(self):
        """Test metadata retrieval"""
        metadata = self.prisem.get_metadata()
        
        assert metadata['id'] == 'PRISE-M.fr'
        assert metadata['abbreviation'] == 'PRISE-M'
        assert metadata['language'] == 'fr-FR'
        assert metadata['version'] == '1.0'
        assert metadata['total_questions'] == 32
        assert metadata['scoring_range'] == [0, 62]
        assert 'gender_specific_items' in metadata
        assert metadata['gender_specific_items']['female'] == 'q20'
        assert metadata['gender_specific_items']['male'] == 'q25'
    
    def test_gender_specific_items_constants(self):
        """Test gender-specific item constants"""
        assert self.prisem.ITEM_FEMALE == "q20"
        assert self.prisem.ITEM_MALE == "q25"
    
    def test_get_sections(self):
        """Test sections retrieval"""
        sections = self.prisem.get_sections()
        
        assert len(sections) == 9
        assert sections[0]['id'] == 'sec1'
        assert '1. Troubles gastro-intestinaux' in sections[0]['label']
        assert sections[7]['id'] == 'sec8'
        assert '8. Fonctions sexuelles' in sections[7]['label']
    
    def test_get_all_questions(self):
        """Test retrieving all questions"""
        questions = self.prisem.get_questions()
        
        assert len(questions) == 32
        assert questions[0]['id'] == 'q1'
        assert questions[31]['id'] == 'q32'
        
        # Check 3-level structure
        q1 = questions[0]
        assert q1['type'] == 'single_choice'
        assert len(q1['options']) == 3
        assert q1['options'][0]['label'] == 'Absent'
        assert q1['options'][1]['label'] == 'Tolérable'
        assert q1['options'][2]['label'] == 'Pénible'
    
    def test_get_questions_filtered_by_gender_female(self):
        """Test getting questions filtered for female"""
        questions = self.prisem.get_questions(gender="F")
        
        # Should have 31 questions (32 - q25)
        assert len(questions) == 31
        question_ids = [q['id'] for q in questions]
        assert 'q20' in question_ids  # Règles irrégulières
        assert 'q25' not in question_ids  # Troubles érection excluded
    
    def test_get_questions_filtered_by_gender_male(self):
        """Test getting questions filtered for male"""
        questions = self.prisem.get_questions(gender="M")
        
        # Should have 31 questions (32 - q20)
        assert len(questions) == 31
        question_ids = [q['id'] for q in questions]
        assert 'q25' in question_ids  # Troubles érection
        assert 'q20' not in question_ids  # Règles irrégulières excluded
    
    def test_question_gender_specific_markers(self):
        """Test that gender-specific questions are properly marked"""
        q20 = self.prisem.get_question_by_id('q20')
        q25 = self.prisem.get_question_by_id('q25')
        
        assert q20 is not None
        assert q20['gender_specific'] == 'F'
        assert 'femmes' in q20['text'].lower()
        
        assert q25 is not None
        assert q25['gender_specific'] == 'M'
        assert 'hommes' in q25['text'].lower()
    
    def test_get_full_questionnaire_with_gender(self):
        """Test getting complete questionnaire with gender filter"""
        full_female = self.prisem.get_full_questionnaire(gender="F")
        full_male = self.prisem.get_full_questionnaire(gender="M")
        
        assert len(full_female['questions']) == 31
        assert len(full_male['questions']) == 31


class TestPRISEMValidation:
    """Test PRISE-M answer validation"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.prisem = PRISEM()
    
    def test_valid_answers_all_absent(self):
        """Test validation with all 'absent' (0) answers"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        validation = self.prisem.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_mixed(self):
        """Test validation with mixed valid answers"""
        answers = {
            f"q{i}": (i % 3) for i in range(1, 33)  # 0, 1, 2 pattern
        }
        validation = self.prisem.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_missing_items_error(self):
        """Test validation fails with missing items"""
        answers = {f"q{i}": 0 for i in range(1, 20)}  # Missing q20-q32
        validation = self.prisem.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
        assert "Items manquants" in validation.errors[0]
    
    def test_invalid_value_too_high(self):
        """Test validation fails with values > 2"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        answers['q10'] = 3  # Invalid
        validation = self.prisem.validate_answers(answers)
        
        assert validation.valid is False
        assert "Valeurs invalides" in validation.errors[0]
    
    def test_invalid_value_negative(self):
        """Test validation fails with negative values"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        answers['q5'] = -1  # Invalid
        validation = self.prisem.validate_answers(answers)
        
        assert validation.valid is False
    
    def test_warning_both_gender_items_endorsed(self):
        """Test warning when both gender-specific items are endorsed"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        answers['q20'] = 2  # Règles irrégulières
        answers['q25'] = 2  # Troubles érection
        
        validation = self.prisem.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) > 0
        assert any('spécifiques au sexe' in w for w in validation.warnings)
    
    def test_warning_no_gender_both_items_absent(self):
        """Test warning when gender not provided and both items absent"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        
        validation = self.prisem.validate_answers(answers, gender=None)
        
        assert validation.valid is True
        # Should have warning about default exclusion
    
    def test_warning_many_severe_items(self):
        """Test warning for many items at level 2 (Pénible)"""
        answers = {f"q{i}": 2 for i in range(1, 33)}  # All pénible
        
        validation = self.prisem.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) > 0
        assert any('Pénible' in w for w in validation.warnings)


class TestPRISEMScoring:
    """Test PRISE-M scoring calculation with gender logic"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.prisem = PRISEM()
    
    def test_scoring_all_absent_female(self):
        """Test scoring with all absent, female"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        result = self.prisem.calculate_score(answers, gender="F")
        
        assert result.total_score == 0
        assert result.excluded_item == "q25"
        assert result.gender_used == "F"
        assert result.warning is None
    
    def test_scoring_all_absent_male(self):
        """Test scoring with all absent, male"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        result = self.prisem.calculate_score(answers, gender="M")
        
        assert result.total_score == 0
        assert result.excluded_item == "q20"
        assert result.gender_used == "M"
        assert result.warning is None
    
    def test_scoring_female_excludes_male_item(self):
        """Test that female scoring excludes q25"""
        answers = {f"q{i}": 1 for i in range(1, 33)}
        answers['q20'] = 2  # Règles irrégulières pénible
        answers['q25'] = 2  # This should be excluded
        
        result = self.prisem.calculate_score(answers, gender="F")
        
        # Score = 31 items (excluding q25): 30*1 + 1*2 = 32
        assert result.total_score == 32
        assert result.excluded_item == "q25"
    
    def test_scoring_male_excludes_female_item(self):
        """Test that male scoring excludes q20"""
        answers = {f"q{i}": 1 for i in range(1, 33)}
        answers['q20'] = 2  # This should be excluded
        answers['q25'] = 2  # Troubles érection pénible
        
        result = self.prisem.calculate_score(answers, gender="M")
        
        # Score = 31 items (excluding q20): 30*1 + 1*2 = 32
        assert result.total_score == 32
        assert result.excluded_item == "q20"
    
    def test_scoring_inference_female_from_responses(self):
        """Test gender inference when only female item is endorsed"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        answers['q20'] = 2  # Règles irrégulières pénible
        answers['q25'] = 0  # Pas de troubles érection
        
        result = self.prisem.calculate_score(answers)  # No gender provided
        
        assert result.total_score == 2
        assert result.excluded_item == "q25"  # Inferred female
        assert result.gender_used == "F"
        assert result.warning is not None
        assert "q20" in result.warning
    
    def test_scoring_inference_male_from_responses(self):
        """Test gender inference when only male item is endorsed"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        answers['q20'] = 0  # Pas de règles
        answers['q25'] = 2  # Troubles érection pénible
        
        result = self.prisem.calculate_score(answers)  # No gender provided
        
        assert result.total_score == 2
        assert result.excluded_item == "q20"  # Inferred male
        assert result.gender_used == "M"
        assert result.warning is not None
        assert "q25" in result.warning
    
    def test_scoring_default_exclusion_when_ambiguous(self):
        """Test default exclusion when both items absent"""
        answers = {f"q{i}": 1 for i in range(1, 33)}
        answers['q20'] = 0  # Absent
        answers['q25'] = 0  # Absent
        
        result = self.prisem.calculate_score(answers)  # No gender provided
        
        # Should exclude q25 by default
        assert result.excluded_item == "q25"
        assert result.warning is not None
        assert "défaut" in result.warning.lower()
    
    def test_section_scores_calculation(self):
        """Test that section scores are calculated correctly"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        # Section 1: q1-q4 (gastro-intestinal)
        answers['q1'] = 1
        answers['q2'] = 2
        answers['q3'] = 1
        answers['q4'] = 0
        
        result = self.prisem.calculate_score(answers, gender="F")
        
        assert 'sec1' in result.section_scores
        assert result.section_scores['sec1'] == 4  # 1+2+1+0
    
    def test_interpretation_low_score(self):
        """Test interpretation for low score"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        answers['q3'] = 1  # One tolerable item
        
        result = self.prisem.calculate_score(answers, gender="F")
        
        assert "bas" in result.interpretation.lower()
        assert result.total_score < 15
    
    def test_interpretation_moderate_score(self):
        """Test interpretation for moderate score"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        # Add enough items to reach moderate range (15-24)
        for i in range(1, 16):
            answers[f"q{i}"] = 1
        
        result = self.prisem.calculate_score(answers, gender="F")
        
        assert 15 <= result.total_score <= 24
        assert "modéré" in result.interpretation.lower()
    
    def test_interpretation_high_score(self):
        """Test interpretation for high score"""
        answers = {f"q{i}": 1 for i in range(1, 33)}
        # Add some pénible items to reach high range (25-39)
        for i in range(1, 11):
            answers[f"q{i}"] = 2
        
        result = self.prisem.calculate_score(answers, gender="F")
        
        assert 25 <= result.total_score <= 39
        assert "élevé" in result.interpretation.lower()
        assert "révision" in result.interpretation.lower()
    
    def test_interpretation_very_high_score(self):
        """Test interpretation for very high score"""
        answers = {f"q{i}": 2 for i in range(1, 33)}
        
        result = self.prisem.calculate_score(answers, gender="F")
        
        assert result.total_score >= 40
        assert "très élevé" in result.interpretation.lower()
    
    def test_scoring_range_boundaries(self):
        """Test score boundaries"""
        # Minimum: all absent
        answers_min = {f"q{i}": 0 for i in range(1, 33)}
        result_min = self.prisem.calculate_score(answers_min, gender="F")
        assert result_min.total_score == 0
        
        # Maximum: all pénible
        answers_max = {f"q{i}": 2 for i in range(1, 33)}
        result_max = self.prisem.calculate_score(answers_max, gender="F")
        assert result_max.total_score == 62  # 31 items * 2
    
    def test_scoring_with_invalid_answers_raises_error(self):
        """Test that invalid answers raise PRISEMError"""
        answers = {f"q{i}": 0 for i in range(1, 20)}  # Missing items
        
        with pytest.raises(PRISEMError) as exc_info:
            self.prisem.calculate_score(answers, gender="F")
        
        assert "Items manquants" in str(exc_info.value)


class TestPRISEMGenderLogic:
    """Test gender-specific logic in detail"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.prisem = PRISEM()
    
    def test_gender_explicit_female(self):
        """Test explicit female gender"""
        answers = {f"q{i}": 1 for i in range(1, 33)}
        result = self.prisem.calculate_score(answers, gender="F")
        
        assert result.gender_used == "F"
        assert result.excluded_item == "q25"
        assert result.warning is None  # No warning when explicit
    
    def test_gender_explicit_male(self):
        """Test explicit male gender"""
        answers = {f"q{i}": 1 for i in range(1, 33)}
        result = self.prisem.calculate_score(answers, gender="M")
        
        assert result.gender_used == "M"
        assert result.excluded_item == "q20"
        assert result.warning is None  # No warning when explicit
    
    def test_gender_inference_logic_female(self):
        """Test gender inference prioritizes endorsed item"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        answers['q20'] = 1  # Règles endorsed
        answers['q25'] = 0  # Érection not endorsed
        
        result = self.prisem.calculate_score(answers)
        
        assert result.gender_used == "F"
        assert result.excluded_item == "q25"
    
    def test_gender_inference_logic_male(self):
        """Test gender inference when male item endorsed"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        answers['q20'] = 0  # Règles not endorsed
        answers['q25'] = 1  # Érection endorsed
        
        result = self.prisem.calculate_score(answers)
        
        assert result.gender_used == "M"
        assert result.excluded_item == "q20"
    
    def test_gender_conflict_both_endorsed(self):
        """Test behavior when both gender items are endorsed"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        answers['q20'] = 1
        answers['q25'] = 1
        
        # With explicit gender
        result_f = self.prisem.calculate_score(answers, gender="F")
        assert result_f.excluded_item == "q25"
        
        result_m = self.prisem.calculate_score(answers, gender="M")
        assert result_m.excluded_item == "q20"
        
        # Without gender - should default to excluding q25
        result_default = self.prisem.calculate_score(answers)
        assert result_default.excluded_item == "q25"


class TestPRISEMClinicalScenarios:
    """Test realistic clinical scenarios"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.prisem = PRISEM()
    
    def test_minimal_side_effects(self):
        """Test patient with minimal side effects"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        answers['q3'] = 1  # Bouche sèche tolérable
        answers['q21'] = 1  # Difficultés d'endormissement tolérables
        
        result = self.prisem.calculate_score(answers, gender="M")
        
        assert result.total_score == 2
        assert "bas" in result.interpretation.lower()
    
    def test_moderate_gi_and_sexual_effects(self):
        """Test patient with moderate GI and sexual side effects"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        # GI effects
        answers['q1'] = 1  # Diarrhée tolérable
        answers['q2'] = 2  # Constipation pénible
        answers['q3'] = 2  # Bouche sèche pénible
        # Sexual effects
        answers['q23'] = 2  # Perte désir pénible
        answers['q25'] = 2  # Troubles érection pénible
        
        result = self.prisem.calculate_score(answers, gender="M")
        
        assert result.total_score >= 9
        assert result.section_scores['sec1'] == 5  # GI section
        assert result.section_scores['sec8'] == 4  # Sexual section
    
    def test_severe_metabolic_and_neurological(self):
        """Test patient with severe metabolic and neurological effects"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        # Neurological
        answers['q11'] = 2  # Mal de tête pénible
        answers['q12'] = 2  # Tremblements pénibles
        answers['q13'] = 1  # Mauvais contrôle tolérable
        # Metabolic/other
        answers['q30'] = 2  # Fatigue pénible
        answers['q31'] = 2  # Diminution énergie pénible
        answers['q32'] = 2  # Prise de poids pénible
        
        result = self.prisem.calculate_score(answers, gender="F")
        
        assert result.total_score >= 11
        assert "sec4" in result.section_scores  # Neurological
        assert "sec9" in result.section_scores  # Other
    
    def test_high_burden_requiring_intervention(self):
        """Test high burden case requiring intervention"""
        answers = {f"q{i}": 1 for i in range(1, 33)}  # All tolerable
        # Many pénible items
        for i in [3, 5, 8, 11, 12, 21, 23, 26, 30, 32]:
            answers[f"q{i}"] = 2
        
        result = self.prisem.calculate_score(answers, gender="M")
        
        assert result.total_score >= 25
        assert "révision" in result.interpretation.lower()


class TestPRISEMIntegration:
    """Integration tests for complete PRISE-M workflow"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.prisem = PRISEM()
    
    def test_complete_workflow_female(self):
        """Test complete workflow for female patient"""
        # 1. Get questionnaire for female
        full = self.prisem.get_full_questionnaire(gender="F")
        assert len(full['questions']) == 31
        
        # 2. Simulate responses
        answers = {f"q{i}": 0 for i in range(1, 33)}
        answers['q3'] = 1
        answers['q20'] = 2
        
        # 3. Validate
        validation = self.prisem.validate_answers(answers, gender="F")
        assert validation.valid is True
        
        # 4. Calculate score
        result = self.prisem.calculate_score(answers, gender="F")
        assert result.total_score == 3
        assert result.excluded_item == "q25"
    
    def test_complete_workflow_male(self):
        """Test complete workflow for male patient"""
        full = self.prisem.get_full_questionnaire(gender="M")
        assert len(full['questions']) == 31
        
        answers = {f"q{i}": 0 for i in range(1, 33)}
        answers['q8'] = 1
        answers['q25'] = 2
        
        validation = self.prisem.validate_answers(answers, gender="M")
        assert validation.valid is True
        
        result = self.prisem.calculate_score(answers, gender="M")
        assert result.total_score == 3
        assert result.excluded_item == "q20"
    
    def test_workflow_without_gender_inference(self):
        """Test workflow with gender inference"""
        answers = {f"q{i}": 0 for i in range(1, 33)}
        answers['q20'] = 2  # Only female item endorsed
        
        result = self.prisem.calculate_score(answers)
        
        assert result.gender_used == "F"
        assert result.warning is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

