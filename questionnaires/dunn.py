"""
Dunn Sensory Profile - Short Form
Assesses sensory processing patterns in children and adults.
"""

from typing import Dict, Any


class DunnSensoryProfileTest:
    """Dunn Sensory Profile - Profil Sensoriel Abrégé
    
    A 38-item questionnaire assessing sensory processing across multiple modalities.
    
    Structure:
    - 7 sections: Tactile Sensitivity, Taste/Smell Sensitivity, Movement Sensitivity,
      Underresponsive/Sensation Seeking, Auditory Filtering, Low Energy/Weak, Visual/Auditory Sensitivity
    - Each item rated 1-5 (1=Toujours, 2=Fréquemment, 3=Parfois, 4=Rarement, 5=Jamais)
    - Section scores and total score
    - Clinical interpretation based on normative data
    """
    
    def __init__(self):
        """Initialize Dunn Sensory Profile test."""
        self.name = "Dunn Sensory Profile"
        self.full_name = "Dunn Sensory Profile - Profil Sensoriel Abrégé"
        self.description = "Questionnaire d'évaluation du traitement sensoriel"
        
        self.sections = {
            "tactile_sensitivity": {"name": "Sensibilité tactile", "items": list(range(1, 8))},
            "taste_smell": {"name": "Sensibilité au goût/à l'odorat", "items": list(range(8, 12))},
            "movement_sensitivity": {"name": "Sensibilité au mouvement", "items": list(range(12, 15))},
            "underresponsive_seeking": {"name": "Hyporéactivité/Recherche de sensations", "items": list(range(15, 22))},
            "auditory_filtering": {"name": "Filtrage auditif", "items": list(range(22, 28))},
            "low_energy": {"name": "Faible énergie/Faible tonus", "items": list(range(28, 34))},
            "visual_auditory": {"name": "Sensibilité visuelle/auditive", "items": list(range(34, 39))}
        }
        
        self.total_items = 38
    
    def calculate_score(self, responses: Dict[str, int]) -> Dict[str, Any]:
        """
        Calculate Dunn Sensory Profile scores.
        
        Args:
            responses: Dictionary mapping item IDs (DUNN1-DUNN38) to responses (1-5)
        
        Returns:
            Dictionary containing section scores, total score, and interpretation
        """
        section_scores = {}
        total_score = 0
        
        for section_key, section_info in self.sections.items():
            section_score = 0
            for item_num in section_info["items"]:
                item_id = f"DUNN{item_num}"
                section_score += responses.get(item_id, 0)
            section_scores[section_info["name"]] = section_score
            total_score += section_score
        
        # Simplified interpretation (actual norms depend on age)
        if total_score < 100:
            interpretation = "Différences sensorielles marquées - Sensibilités multiples"
        elif total_score < 130:
            interpretation = "Différences sensorielles modérées - Quelques sensibilités"
        elif total_score < 155:
            interpretation = "Traitement sensoriel typique - Performance moyenne"
        else:
            interpretation = "Traitement sensoriel optimal - Peu ou pas de sensibilités"
        
        return {
            "total_score": total_score,
            "total_possible": self.total_items * 5,
            "section_scores": section_scores,
            "interpretation": interpretation,
            "note": "Interpretation requires age-specific normative tables from Dunn manual"
        }


if __name__ == '__main__':
    dunn = DunnSensoryProfileTest()
    
    print(f"Test: {dunn.full_name}")
    print(f"Total items: {dunn.total_items}\n")
    
    print("Sections:")
    for section_info in dunn.sections.values():
        print(f"  - {section_info['name']}: {len(section_info['items'])} items")
    
    # Example: Moderate sensory sensitivities
    print("\nExample: Moderate sensory sensitivities")
    responses = {}
    for i in range(1, 39):
        # Simulate mixed responses (2-4 range)
        if i <= 14:  # Hypersensitive items
            responses[f"DUNN{i}"] = 2  # Fréquemment
        else:  # Hyposensitive/seeking items
            responses[f"DUNN{i}"] = 3  # Parfois
    
    result = dunn.calculate_score(responses)
    print(f"Total score: {result['total_score']}/{result['total_possible']}")
    print("\nSection scores:")
    for section, score in result['section_scores'].items():
        print(f"  {section}: {score}")
    print(f"\nInterprétation: {result['interpretation']}")

