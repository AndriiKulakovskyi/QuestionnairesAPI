import random
from typing import Any, Dict, List

class SachsQuestionnaire:
    """Sachs Bipolar Inventory Scale
    
    Clinician-rated scale assessing bipolarity characteristics.
    
    Structure:
    - 5 items with weighted scoring (0-20 points each):
      1. Episode characteristics
      2. Age of onset
      3. Course/associated disorders
      4. Family history
      5. Treatment response
    
    Scoring:
    - Each item has multiple response options with different point values
    - Select highest applicable score if multiple apply
    - Total score: 0-100
    - Higher scores indicate greater bipolarity
    
    Clinical Use:
    - Assessment of bipolar disorder likelihood
    - Differential diagnosis
    - Treatment planning
    """

    def __init__(self):
        self.name = "Sachs - Bipolar Inventory Scale"
        self.description = "Échelle de bipolarité de Sachs (évaluation clinicienne)."
        self.num_items = 5
        self.used_in_applications = ['cedr']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 5 Sachs items with weighted options."""
        
        questions = [
            {
                "id": "SACHS1",
                "number": 1,
                "text": "1. Caractéristiques des épisodes",
                "options": {
                    "20 - Episode maniaque aigu ou mixte (euphorie/grandiosité)": 20,
                    "15 - Episode mixte aigu ou manie dysphorique": 15,
                    "10 - Hypomanie ou cyclothymie franches": 10,
                    "10 - Manie secondaire aux antidépresseurs": 10,
                    "5 - Hypomanie secondaire aux antidépresseurs": 5,
                    "5 - Episodes hypomaniaques atténués": 5,
                    "5 - Dépression avec psychose/signes atypiques": 5,
                    "5 - Dépression du post-partum": 5,
                    "2 - Dépression unipolaire récurrente": 2,
                    "2 - Histoire de psychose": 2,
                    "0 - Absence de troubles": 0
                }
            },
            {
                "id": "SACHS2",
                "number": 2,
                "text": "2. Âge de début (premier épisode)",
                "options": {
                    "20 - 15 à 19 ans": 20,
                    "15 - Avant 15 ou 20-30 ans": 15,
                    "10 - 30 à 45 ans": 10,
                    "5 - Après 45 ans": 5,
                    "0 - Absence de troubles de l'humeur": 0
                }
            },
            {
                "id": "SACHS3",
                "number": 3,
                "text": "3. Évolution et troubles associés",
                "options": {
                    "20 - Intervalle libre entre manies (récupération complète)": 20,
                    "15 - Intervalle libre entre hypomanies (récupération complète)": 15,
                    "15 - Intervalle libre entre manies (récupération partielle)": 15,
                    "10 - Abus de substance": 10,
                    "10 - Psychose durant épisodes aigus": 10,
                    "10 - Antécédents judiciaires liés à manie": 10,
                    "5 - Dépression récurrente (3+ épisodes)": 5,
                    "5 - Hypomanies récurrentes (récupération partielle)": 5,
                    "5 - Mauvaise observance traitement": 5,
                    "5 - Comorbidités (borderline, anxiété, TCA, TDAH)": 5,
                    "5 - Comportements à risque": 5,
                    "5 - Aggravation cyclique (menstruel)": 5,
                    "2 - Personnalité hyperthymique": 2,
                    "2 - 3+ mariages": 2,
                    "2 - Changements professionnels fréquents": 2,
                    "2 - Études supérieures multiples": 2,
                    "0 - Aucune manifestation": 0
                }
            },
            {
                "id": "SACHS4",
                "number": 4,
                "text": "4. Antécédents familiaux",
                "options": {
                    "20 - Trouble bipolaire I chez parent 1er degré": 20,
                    "15 - Trouble bipolaire chez parent 2e degré": 15,
                    "10 - Dépression récurrente chez parent 1er degré": 10,
                    "5 - Suicide ou tentative chez parent 1er degré": 5,
                    "5 - Abus substance chez parent 1er degré": 5,
                    "0 - Pas d'antécédents familiaux": 0
                }
            },
            {
                "id": "SACHS5",
                "number": 5,
                "text": "5. Réponse au traitement",
                "options": {
                    "20 - Virage maniaque sous antidépresseur": 20,
                    "15 - Cycles rapides sous antidépresseur": 15,
                    "10 - Bonne réponse au lithium/anticonvulsivant": 10,
                    "5 - Réponse partielle au lithium": 5,
                    "0 - Pas de traitement thymosabilisateur": 0
                }
            }
        ]
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        Calculate Sachs total score.

        Args:
            responses (Dict[str, str]): A dictionary of responses, where the key is the question ID
                                       and the value is the response option text.

        Returns:
            Dict[str, Any]: A dictionary containing total score and interpretation.
        """
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")

        total_score = 0
        item_scores = {}
        
        for question in self.questions:
            q_id = question["id"]
            if q_id not in responses:
                raise ValueError(f"Missing response for question {q_id}")
            
            response_text = responses[q_id]
            if response_text not in question["options"]:
                raise ValueError(
                    f"Invalid response for question {q_id}. "
                    f"Must match one of the predefined options."
                )
            
            score = question["options"][response_text]
            item_scores[q_id] = score
            total_score += score

        interpretation = self._interpret_score(total_score)

        return {
            "total_score": total_score,
            "max_score": 100,
            "interpretation": interpretation,
            "bipolarity_level": self._get_level(total_score),
            "item_scores": item_scores
        }

    def _interpret_score(self, score: int) -> str:
        """Interpret Sachs total score."""
        if score >= 70:
            return "Probabilité très élevée de trouble bipolaire"
        elif score >= 50:
            return "Probabilité élevée de trouble bipolaire"
        elif score >= 30:
            return "Probabilité modérée de trouble bipolaire"
        elif score >= 15:
            return "Probabilité faible de trouble bipolaire"
        else:
            return "Probabilité très faible de trouble bipolaire"

    def _get_level(self, score: int) -> str:
        """Get bipolarity probability level."""
        if score >= 70:
            return "very_high"
        elif score >= 50:
            return "high"
        elif score >= 30:
            return "moderate"
        elif score >= 15:
            return "low"
        else:
            return "very_low"

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "Échelle d'évaluation de la bipolarité (clinicien).\n\n"
            "Pour chacun des 5 chapitres, cocher le score correspondant à la proposition "
            "vraie concernant le patient.\n\n"
            "Si plusieurs réponses sont vraies, prendre en compte la proposition dont le "
            "score est le plus élevé."
        )


if __name__ == '__main__':
    sachs = SachsQuestionnaire()
    print(f"Questionnaire: {sachs.name}")
    print(f"Number of items: {sachs.num_items}")
    print()
    
    # Test: High bipolarity
    test_responses = {
        "SACHS1": "20 - Episode maniaque aigu ou mixte (euphorie/grandiosité)",
        "SACHS2": "20 - 15 à 19 ans",
        "SACHS3": "20 - Intervalle libre entre manies (récupération complète)",
        "SACHS4": "20 - Trouble bipolaire I chez parent 1er degré",
        "SACHS5": "20 - Virage maniaque sous antidépresseur"
    }
    
    result = sachs.calculate_score(test_responses)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Level: {result['bipolarity_level']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    print("✓ Sachs implementation complete - 5 items, weighted 0-100 scoring")

