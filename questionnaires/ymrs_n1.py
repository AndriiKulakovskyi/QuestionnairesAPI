"""
Questionnaire: YMRS N+1 (Young Mania Rating Scale - Follow-up)
Échelle de Manie de Young - Visite de suivi
"""

from typing import Dict, List, Optional, Any
from .ymrs import YMRSQuestionnaire


class YMRSN1Questionnaire(YMRSQuestionnaire):
    """YMRS N+1 - Young Mania Rating Scale (Follow-up Visit)
    
    Identical to YMRS but used for follow-up visits (N+1).
    Héteéro-évaluation clinique de la manie en 11 items.
    Chaque item est coté de 0 à 4.
    
    This is the exact same questionnaire as YMRS, just labeled differently
    to indicate it's for subsequent visits rather than baseline.
    """
    
    def __init__(self):
        # Initialize with parent class
        super().__init__()
        # Override name to indicate this is follow-up version
        self.name = "YMRS N+1 - Young Mania Rating Scale (Visite de suivi)"
        self.description = ("Échelle de manie de Young pour les visites de suivi. "
                           "Identique à la YMRS mais utilisée lors des visites N+1 (suivi). "
                           "11 items cotés de 0 à 4, score total 0-44.")
        # Same applications as regular YMRS
        self.used_in_applications = ["ebipolar", "eschizo"]


# Example usage
if __name__ == "__main__":
    questionnaire = YMRSN1Questionnaire()
    
    # Example: Patient with moderate mania at follow-up visit
    example_responses = {
        'radhtml_ymrs1': 'c',  # Elévation subjective nette
        'radhtml_ymrs2': 'c',  # Animé, expression gestuelle plus élevée
        'radhtml_ymrs3': 'b',  # Augmentation légère de l'intérêt sexuel
        'radhtml_ymrs4': 'c',  # Sommeil réduit > 1h
        'radhtml_ymrs5': 'b',  # Subjectivement irritable
        'radhtml_ymrs6': 'b',  # Se sent bavard
        'radhtml_ymrs7': 'b',  # Légère distractivité
        'radhtml_ymrs8': 'b',  # Projets discutables
        'radhtml_ymrs9': 'a',  # Coopératif
        'radhtml_ymrs10': 'b',  # Légèrement négligé
        'radhtml_ymrs11': 'b'   # Eventuellement malade
    }
    
    result = questionnaire.calculate_score(example_responses)
    print(f"Score YMRS N+1: {result['score']}/44")
    print(f"Interprétation: {result['interpretation']}")
    print(f"\nNote: N+1 indique une visite de suivi (même questionnaire que YMRS baseline)")

