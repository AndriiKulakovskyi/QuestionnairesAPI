# -*- coding: utf-8 -*-
"""
Comprehensive unit tests for EQ-5D-5L questionnaire
Tests metadata, questions, validation, profile generation, and edge cases
"""

import pytest
from questionnaires.auto.eq5del import EQ5D5L, EQ5D5LError, ScoreResult, ValidationResult


class TestEQ5D5LMetadata:
    """Test EQ-5D-5L metadata and structure retrieval"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.eq5d = EQ5D5L()
    
    def test_get_metadata(self):
        """Test metadata retrieval"""
        metadata = self.eq5d.get_metadata()
        
        assert metadata['id'] == 'EQ-5D-5L.fr'
        assert metadata['abbreviation'] == 'EQ-5D-5L'
        assert metadata['language'] == 'fr-FR'
        assert metadata['version'] == '1.0'
        assert metadata['reference_period'] == 'AUJOURD\'HUI'
        assert metadata['total_questions'] == 6
        assert metadata['dimensions'] == 5
        assert metadata['profile_range'] == ["11111", "55555"]
        assert metadata['vas_range'] == [0, 100]
        assert metadata['index_range'] == [-0.530, 1.000]
        assert 'sources' in metadata
    
    def test_get_sections(self):
        """Test sections retrieval"""
        sections = self.eq5d.get_sections()
        
        assert len(sections) == 2
        assert sections[0]['id'] == 'sec_dims'
        assert sections[0]['label'] == 'Dimensions (AUJOURD\'HUI)'
        assert len(sections[0]['question_ids']) == 5
        
        assert sections[1]['id'] == 'sec_vas'
        assert sections[1]['label'] == 'EQ VAS'
        assert len(sections[1]['question_ids']) == 1
    
    def test_get_all_questions(self):
        """Test retrieving all questions"""
        questions = self.eq5d.get_questions()
        
        assert len(questions) == 6  # 5 dimensions + VAS
        assert questions[0]['id'] == 'q1'
        assert questions[4]['id'] == 'q5'
        assert questions[5]['id'] == 'vas'
        
        # Check Q1-Q5 structure (dimensions)
        for i in range(5):
            q = questions[i]
            assert 'id' in q
            assert 'section_id' in q
            assert 'text' in q
            assert 'type' in q
            assert 'required' in q
            assert 'options' in q
            assert 'constraints' in q
            assert len(q['options']) == 5  # 1-5 scale
            assert q['required'] is True
        
        # Check VAS structure
        vas = questions[5]
        assert vas['type'] == 'integer'
        assert vas['options'] is None
        assert vas['constraints']['min_value'] == 0
        assert vas['constraints']['max_value'] == 100
    
    def test_dimension_options_structure(self):
        """Test that Q1-Q5 have correct options (1-5 without scores)"""
        questions = self.eq5d.get_questions(section_id='sec_dims')
        
        for q in questions:
            assert len(q['options']) == 5
            codes = [opt['code'] for opt in q['options']]
            scores = [opt['score'] for opt in q['options']]
            assert codes == [1, 2, 3, 4, 5]
            assert all(score is None for score in scores)
            # Check all options have labels
            for opt in q['options']:
                assert 'label' in opt
                assert len(opt['label']) > 0
    
    def test_dimension_texts(self):
        """Test that dimension texts are meaningful"""
        questions = self.eq5d.get_questions(section_id='sec_dims')
        
        texts = [q['text'].lower() for q in questions]
        assert any('mobilité' in t for t in texts)
        assert any('autonomie' in t for t in texts)
        assert any('activités' in t for t in texts)
        assert any('douleur' in t for t in texts)
        assert any('anxiété' in t or 'dépression' in t for t in texts)
    
    def test_get_question_by_id(self):
        """Test retrieving specific question by ID"""
        q1 = self.eq5d.get_question_by_id('q1')
        assert q1 is not None
        assert q1['id'] == 'q1'
        assert 'Mobilité' in q1['text']
        
        vas = self.eq5d.get_question_by_id('vas')
        assert vas is not None
        assert vas['id'] == 'vas'
        assert 'VAS' in vas['text'] or 'santé' in vas['text'].lower()
        
        # Non-existent question
        invalid = self.eq5d.get_question_by_id('q99')
        assert invalid is None
    
    def test_get_full_questionnaire(self):
        """Test getting complete questionnaire structure"""
        full = self.eq5d.get_full_questionnaire()
        
        assert 'metadata' in full
        assert 'sections' in full
        assert 'questions' in full
        assert len(full['questions']) == 6
        assert len(full['sections']) == 2


class TestEQ5D5LValidation:
    """Test EQ-5D-EL answer validation"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.eq5d = EQ5D5L()
    
    def test_valid_answers_all_ones(self):
        """Test validation with perfect health (11111)"""
        answers = {f"q{i}": 1 for i in range(1, 6)}
        answers['vas'] = 100
        validation = self.eq5d.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_all_fives(self):
        """Test validation with worst health (55555)"""
        answers = {f"q{i}": 5 for i in range(1, 6)}
        answers['vas'] = 0
        validation = self.eq5d.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_valid_answers_mixed(self):
        """Test validation with mixed valid answers"""
        answers = {
            "q1": 2, "q2": 1, "q3": 3, "q4": 4, "q5": 1,
            "vas": 75
        }
        validation = self.eq5d.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.errors) == 0
    
    def test_missing_dimension_error(self):
        """Test validation fails with missing dimension"""
        answers = {"q1": 1, "q2": 2, "q3": 3, "vas": 50}  # Missing q4, q5
        validation = self.eq5d.validate_answers(answers)
        
        assert validation.valid is False
        assert len(validation.errors) > 0
        assert "Items manquants" in validation.errors[0]
    
    def test_missing_vas_error(self):
        """Test validation fails with missing VAS"""
        answers = {f"q{i}": 1 for i in range(1, 6)}  # Missing VAS
        validation = self.eq5d.validate_answers(answers)
        
        assert validation.valid is False
        assert "vas" in validation.errors[0].lower()
    
    def test_invalid_dimension_value_too_high(self):
        """Test validation fails with dimension value > 5"""
        answers = {f"q{i}": 1 for i in range(1, 6)}
        answers['q3'] = 6  # Invalid
        answers['vas'] = 50
        validation = self.eq5d.validate_answers(answers)
        
        assert validation.valid is False
        assert "Dimensions" in validation.errors[0]
    
    def test_invalid_dimension_value_zero(self):
        """Test validation fails with dimension value 0"""
        answers = {f"q{i}": 1 for i in range(1, 6)}
        answers['q2'] = 0  # Invalid (must be 1-5)
        answers['vas'] = 50
        validation = self.eq5d.validate_answers(answers)
        
        assert validation.valid is False
    
    def test_invalid_vas_too_high(self):
        """Test validation fails with VAS > 100"""
        answers = {f"q{i}": 1 for i in range(1, 6)}
        answers['vas'] = 150  # Invalid
        validation = self.eq5d.validate_answers(answers)
        
        assert validation.valid is False
        assert "VAS" in validation.errors[0]
    
    def test_invalid_vas_negative(self):
        """Test validation fails with negative VAS"""
        answers = {f"q{i}": 1 for i in range(1, 6)}
        answers['vas'] = -10  # Invalid
        validation = self.eq5d.validate_answers(answers)
        
        assert validation.valid is False
    
    def test_warning_worst_health_state(self):
        """Test warning for worst health state (55555)"""
        answers = {f"q{i}": 5 for i in range(1, 6)}
        answers['vas'] = 90  # High VAS with worst profile
        validation = self.eq5d.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) > 0
        assert any('55555' in w for w in validation.warnings)
    
    def test_warning_inconsistency_bad_profile_high_vas(self):
        """Test warning for inconsistency: bad profile but high VAS"""
        answers = {f"q{i}": 4 for i in range(1, 6)}  # Severe problems
        answers['vas'] = 90  # But high VAS
        validation = self.eq5d.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) > 0
        assert any('incohérence' in w.lower() for w in validation.warnings)
    
    def test_warning_inconsistency_good_profile_low_vas(self):
        """Test warning for inconsistency: good profile but low VAS"""
        answers = {f"q{i}": 1 for i in range(1, 6)}  # No problems
        answers['vas'] = 20  # But very low VAS
        validation = self.eq5d.validate_answers(answers)
        
        assert validation.valid is True
        assert len(validation.warnings) > 0
        assert any('incohérence' in w.lower() for w in validation.warnings)


class TestEQ5D5LScoring:
    """Test EQ-5D-EL profile generation and scoring"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.eq5d = EQ5D5L()
    
    def test_profile_perfect_health(self):
        """Test profile generation for perfect health (11111)"""
        answers = {f"q{i}": 1 for i in range(1, 6)}
        answers['vas'] = 100
        result = self.eq5d.calculate_score(answers)
        
        assert result.profile == "11111"
        assert result.vas_score == 100
        assert "optimal" in result.interpretation.lower()
    
    def test_profile_worst_health(self):
        """Test profile generation for worst health (55555)"""
        answers = {f"q{i}": 5 for i in range(1, 6)}
        answers['vas'] = 0
        result = self.eq5d.calculate_score(answers)
        
        assert result.profile == "55555"
        assert result.vas_score == 0
        assert "défavorable" in result.interpretation.lower()
    
    def test_profile_generation_accuracy(self):
        """Test that profile is correctly generated from answers"""
        answers = {
            "q1": 2, "q2": 1, "q3": 3, "q4": 4, "q5": 1,
            "vas": 75
        }
        result = self.eq5d.calculate_score(answers)
        
        assert result.profile == "21341"
        assert result.vas_score == 75
    
    def test_profile_all_different_levels(self):
        """Test profile with all different levels"""
        answers = {
            "q1": 1, "q2": 2, "q3": 3, "q4": 4, "q5": 5,
            "vas": 50
        }
        result = self.eq5d.calculate_score(answers)
        
        assert result.profile == "12345"
    
    def test_dimensions_in_result(self):
        """Test that dimensions are included in result"""
        answers = {
            "q1": 2, "q2": 3, "q3": 1, "q4": 4, "q5": 2,
            "vas": 60
        }
        result = self.eq5d.calculate_score(answers)
        
        assert 'dimensions' in result.dict()
        dims = result.dimensions
        assert len(dims) == 5
        assert dims['Mobilité'] == 2
        assert dims['Autonomie'] == 3
        assert dims['Activités courantes'] == 1
        assert dims['Douleurs/Gêne'] == 4
        assert dims['Anxiété/Dépression'] == 2
    
    def test_vas_score_in_result(self):
        """Test that VAS score is correctly captured"""
        for vas_val in [0, 25, 50, 75, 100]:
            answers = {f"q{i}": 1 for i in range(1, 6)}
            answers['vas'] = vas_val
            result = self.eq5d.calculate_score(answers)
            assert result.vas_score == vas_val
    
    def test_index_value_calculated(self):
        """Test that index value is calculated from France crosswalk"""
        answers = {
            "q1": 2, "q2": 1, "q3": 3, "q4": 4, "q5": 1,
            "vas": 75
        }
        result = self.eq5d.calculate_score(answers)
        
        # Index should be calculated from France crosswalk table
        # Profile 21341 should have index 0.474
        assert result.index_value is not None
        assert result.profile == "21341"
        assert abs(result.index_value - 0.474) < 0.001
        assert "utilité" in result.interpretation.lower()
    
    def test_interpretation_includes_profile(self):
        """Test that interpretation includes profile"""
        answers = {
            "q1": 3, "q2": 2, "q3": 1, "q4": 2, "q5": 3,
            "vas": 65
        }
        result = self.eq5d.calculate_score(answers)
        
        assert result.profile in result.interpretation
        assert str(result.vas_score) in result.interpretation
    
    def test_interpretation_high_vas(self):
        """Test interpretation for high VAS"""
        answers = {f"q{i}": 1 for i in range(1, 6)}
        answers['vas'] = 90
        result = self.eq5d.calculate_score(answers)
        
        assert "élevé" in result.interpretation.lower() or "bonne" in result.interpretation.lower()
    
    def test_interpretation_low_vas(self):
        """Test interpretation for low VAS"""
        answers = {f"q{i}": 3 for i in range(1, 6)}
        answers['vas'] = 25
        result = self.eq5d.calculate_score(answers)
        
        assert "bas" in result.interpretation.lower() or "défavorable" in result.interpretation.lower()
    
    def test_score_with_invalid_answers_raises_error(self):
        """Test that invalid answers raise EQ5D5LError"""
        answers = {"q1": 1, "q2": 2}  # Missing items
        
        with pytest.raises(EQ5D5LError) as exc_info:
            self.eq5d.calculate_score(answers)
        
        assert "Items manquants" in str(exc_info.value)


class TestEQ5D5LProfileDescription:
    """Test profile description functionality"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.eq5d = EQ5D5L()
    
    def test_get_profile_description_perfect_health(self):
        """Test profile description for perfect health"""
        description = self.eq5d.get_profile_description("11111")
        
        assert len(description) == 5
        assert all("aucun problème" in v.lower() for v in description.values())
    
    def test_get_profile_description_worst_health(self):
        """Test profile description for worst health"""
        description = self.eq5d.get_profile_description("55555")
        
        assert len(description) == 5
        # Check that all describe extreme/incapable
        texts = ' '.join(description.values()).lower()
        assert "incapable" in texts or "extrême" in texts
    
    def test_get_profile_description_mixed(self):
        """Test profile description for mixed profile"""
        description = self.eq5d.get_profile_description("21341")
        
        assert description['Mobilité'] == "J'ai des problèmes légers pour me déplacer à pied"
        assert description['Autonomie de la personne'] == "Je n'ai aucun problème pour me laver ou m'habiller tout seul"
        assert "modérés" in description['Activités courantes']
        assert "sévères" in description['Douleurs / Gêne']
        assert description['Anxiété / Dépression'] == "Je ne suis ni anxieux(se), ni déprimé(e)"
    
    def test_invalid_profile_length(self):
        """Test that invalid profile length raises error"""
        with pytest.raises(EQ5D5LError):
            self.eq5d.get_profile_description("1234")  # Too short
        
        with pytest.raises(EQ5D5LError):
            self.eq5d.get_profile_description("123456")  # Too long
    
    def test_invalid_profile_characters(self):
        """Test that invalid characters raise error"""
        with pytest.raises(EQ5D5LError):
            self.eq5d.get_profile_description("1234a")  # Letter
        
        with pytest.raises(EQ5D5LError):
            self.eq5d.get_profile_description("12346")  # 6 is invalid
    
    def test_invalid_profile_zero(self):
        """Test that 0 in profile raises error"""
        with pytest.raises(EQ5D5LError):
            self.eq5d.get_profile_description("01234")  # 0 is invalid


class TestEQ5D5LEdgeCases:
    """Test edge cases and special scenarios"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.eq5d = EQ5D5L()
    
    def test_all_profiles_use_same_dimensions(self):
        """Test that all profiles use the same 5 dimensions"""
        assert len(self.eq5d.DIMENSIONS) == 5
        assert len(self.eq5d.DIMENSION_NAMES) == 5
    
    def test_each_dimension_has_five_levels(self):
        """Test that each dimension has exactly 5 levels"""
        for title, levels in self.eq5d.DIMENSIONS:
            assert len(levels) == 5
    
    def test_consistent_scoring_multiple_calls(self):
        """Test that scoring is consistent across multiple calls"""
        answers = {
            "q1": 2, "q2": 3, "q3": 1, "q4": 4, "q5": 2,
            "vas": 65
        }
        
        result1 = self.eq5d.calculate_score(answers)
        result2 = self.eq5d.calculate_score(answers)
        result3 = self.eq5d.calculate_score(answers)
        
        assert result1.profile == result2.profile == result3.profile
        assert result1.vas_score == result2.vas_score == result3.vas_score
    
    def test_vas_boundary_values(self):
        """Test VAS at boundary values"""
        base_answers = {f"q{i}": 1 for i in range(1, 6)}
        
        # VAS = 0
        answers = base_answers.copy()
        answers['vas'] = 0
        result = self.eq5d.calculate_score(answers)
        assert result.vas_score == 0
        
        # VAS = 100
        answers = base_answers.copy()
        answers['vas'] = 100
        result = self.eq5d.calculate_score(answers)
        assert result.vas_score == 100
    
    def test_profile_permutations(self):
        """Test different profile permutations"""
        test_profiles = [
            "11111", "12345", "54321", "33333", "24135", "55555"
        ]
        
        for expected_profile in test_profiles:
            answers = {f"q{i}": int(expected_profile[i-1]) for i in range(1, 6)}
            answers['vas'] = 50
            result = self.eq5d.calculate_score(answers)
            assert result.profile == expected_profile


class TestEQ5D5LIntegration:
    """Integration tests for complete EQ-5D-EL workflow"""
    
    def setup_method(self):
        """Setup test fixture"""
        self.eq5d = EQ5D5L()
    
    def test_complete_workflow_healthy_patient(self):
        """Test complete workflow for healthy patient"""
        # 1. Get questionnaire
        full = self.eq5d.get_full_questionnaire()
        assert len(full['questions']) == 6
        
        # 2. Patient answers (mostly healthy)
        answers = {
            "q1": 1, "q2": 1, "q3": 1, "q4": 2, "q5": 1,
            "vas": 85
        }
        
        # 3. Validate
        validation = self.eq5d.validate_answers(answers)
        assert validation.valid is True
        
        # 4. Calculate score
        result = self.eq5d.calculate_score(answers)
        assert result.profile == "11121"
        assert result.vas_score == 85
        
        # 5. Get description
        description = self.eq5d.get_profile_description(result.profile)
        assert len(description) == 5
    
    def test_complete_workflow_sick_patient(self):
        """Test complete workflow for sick patient"""
        # 1. Get questions
        questions = self.eq5d.get_questions()
        assert len(questions) == 6
        
        # 2. Patient answers (moderate problems)
        answers = {
            "q1": 3, "q2": 3, "q3": 4, "q4": 3, "q5": 4,
            "vas": 40
        }
        
        # 3. Validate
        validation = self.eq5d.validate_answers(answers)
        assert validation.valid is True
        
        # 4. Calculate score
        result = self.eq5d.calculate_score(answers)
        assert result.profile == "33434"
        assert result.vas_score == 40
        assert "sévère" in result.interpretation.lower()
    
    def test_workflow_with_warnings(self):
        """Test workflow that triggers warnings"""
        # Worst profile but high VAS
        answers = {f"q{i}": 5 for i in range(1, 6)}
        answers['vas'] = 85
        
        # Validate
        validation = self.eq5d.validate_answers(answers)
        assert validation.valid is True
        assert len(validation.warnings) > 0
        
        # Calculate score
        result = self.eq5d.calculate_score(answers)
        assert result.profile == "55555"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
