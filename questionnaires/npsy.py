"""
NPSY - Neuropsychological Evaluation Battery
Comprehensive neuropsychological assessment battery including multiple executive function tests.
"""

from typing import Dict, Any, Optional


class NPSYTest:
    """NPSY - Neuropsychological Evaluation Battery
    
    A comprehensive neuropsychological evaluation form collecting data on:
    - Socio-cultural level
    - Learning disabilities
    - Clinical criteria for neuropsych testing
    
    This is primarily a data collection form rather than a scored test.
    """
    
    def __init__(self):
        """Initialize NPSY evaluation form."""
        self.name = "NPSY"
        self.full_name = "Evaluation Neuropsychologique - Critères et Antécédents"
        self.description = "Formulaire d'évaluation neuropsychologique (antécédents et critères)"
        
        self.learning_disabilities = [
            "dyslex", "dysor", "dyscal", "dysph", "dyspra",
            "parol", "begai", "march", "conv", "precoc"
        ]
    
    def collect_data(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        """
        Collect neuropsychological evaluation data.
        
        Args:
            responses: Dictionary containing all form responses
        
        Returns:
            Dictionary with organized neuropsych evaluation data
        """
        return {
            "socio_cultural": {
                "profession": responses.get("W4_profession"),
                "education_level": responses.get("W4_nivetude"),
                "laterality": responses.get("neuro_lateral")
            },
            "learning_disabilities": {
                "dyslexia": responses.get("neuro_dyslex"),
                "dysorthography": responses.get("neuro_dysor"),
                "dyscalculia": responses.get("neuro_dyscal"),
                "dysphasia": responses.get("neuro_dysph"),
                "dyspraxia": responses.get("neuro_dyspra"),
                "speech_delay": responses.get("neuro_parol"),
                "stuttering": responses.get("neuro_begai"),
                "walking_delay": responses.get("neuro_march"),
                "febrile_convulsions": responses.get("neuro_conv"),
                "precociousness": responses.get("neuro_precoc")
            },
            "testing_criteria": {
                "french_proficiency": responses.get("NPSY_1"),
                "clinical_state_compatible": responses.get("NPSY_2"),
                "no_visual_impairment": responses.get("NPSY_3")
            }
        }


class NPSYComplementaryBattery:
    """NPSY Complementary - Comprehensive Executive Function Battery
    
    A collection of executive function tests including:
    - Wisconsin Card Sorting Test (WCST)
    - Stroop Test
    - Trail Making Test (TMT)
    - Tower of London
    - CPT-II (Continuous Performance Test)
    - Reading the Mind in the Eyes Test
    """
    
    def __init__(self):
        """Initialize NPSY Complementary Battery."""
        self.name = "NPSY-Complementary"
        self.full_name = "Evaluation Complémentaire Neuropsychologique"
        self.description = "Batterie complémentaire de tests exécutifs"
        
        self.subtests = {
            "wisconsin": {"name": "Wisconsin Card Sorting Test", "items": 128},
            "stroop": {"name": "Stroop Test", "sections": 3},
            "tmt": {"name": "Trail Making Test", "parts": ["A", "B"]},
            "tower_london": {"name": "Tower of London"},
            "cpt2": {"name": "CPT-II"},
            "eyes": {"name": "Reading the Mind in the Eyes"}
        }
    
    def calculate_wisconsin_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """Calculate Wisconsin Card Sorting Test scores."""
        categories_completed = 0
        perseverative_errors = 0
        total_errors = 0
        
        # Count categories, errors, and perseverative errors
        for i in range(1, 129):
            response = responses.get(f"WISCONSIN{i}")
            if response in ["C", "F", "N"]:  # C=Correct, F=Failure, N=Not administered
                if response == "C":
                    pass  # Correct response
                elif response == "F":
                    total_errors += 1
            # Additional logic for perseverative errors would go here
        
        return {
            "categories_completed": categories_completed,
            "perseverative_errors": perseverative_errors,
            "total_errors": total_errors,
            "note": "Full WCST scoring requires detailed response pattern analysis"
        }
    
    def collect_data(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        """
        Collect complementary neuropsych battery data.
        
        Args:
            responses: Dictionary containing all test responses
        
        Returns:
            Dictionary with test results
        """
        return {
            "age": responses.get("NPSY_COMP_AGA"),
            "years_education": responses.get("annees_etudes"),
            "evaluator": responses.get("NPSY_COMP_NOM"),
            "tests": {
                "wisconsin": self.calculate_wisconsin_score(responses) if responses.get("WISCONSIN_NF") != 1 else {"status": "Not administered"},
                "stroop": {"status": "Administered"} if responses.get("STROP_NF") != 1 else {"status": "Not administered"},
                "tmt": {"status": "Administered"} if responses.get("TMT_NF") != 1 else {"status": "Not administered"},
                "tower_london": {"status": "Administered"} if responses.get("LONDON_NF") != 1 else {"status": "Not administered"},
                "cpt2": {"status": "Administered"} if responses.get("CPT_NF") != 1 else {"status": "Not administered"},
                "eyes": {"status": "Administered"} if responses.get("EYES_NF") != 1 else {"status": "Not administered"}
            }
        }


if __name__ == '__main__':
    npsy = NPSYTest()
    npsy_comp = NPSYComplementaryBattery()
    
    print(f"Form 1: {npsy.full_name}")
    print(f"Assesses: Socio-cultural level, learning disabilities, testing criteria\n")
    
    print(f"Form 2: {npsy_comp.full_name}")
    print("Tests included:")
    for test_info in npsy_comp.subtests.values():
        print(f"  - {test_info['name']}")
    
    # Example
    print("\nExample data collection:")
    example_responses = {
        "W4_profession": 7,  # Professions intellectuelles supérieures
        "W4_nivetude": 7,  # Diplôme universitaire 2e/3e cycle
        "neuro_lateral": 2,  # Droitier
        "neuro_dyslex": 0,  # No dyslexia
        "NPSY_1": 1,  # French proficiency: Yes
        "NPSY_2": 1,  # Clinical state compatible: Yes
        "NPSY_3": 1   # No visual impairment: Yes
    }
    
    result = npsy.collect_data(example_responses)
    print("Socio-cultural level:")
    print(f"  Education: Level {result['socio_cultural']['education_level']}")
    print(f"  Laterality: {result['socio_cultural']['laterality']}")
    print(f"\nTesting criteria met: {all(result['testing_criteria'].values())}")

