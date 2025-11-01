import random
from typing import Any, Dict, List, Optional

class LEAPSQuestionnaire:
    """LEAPS - Work Productivity Assessment
    
    Self-report questionnaire assessing work productivity and functioning.
    
    Structure:
    - 4 informational items (job type, expected hours, missed hours, employment status)
    - 7 scored items assessing work impairment:
      4a. Low energy and motivation
      4b. Poor concentration or memory
      4c. Anxiety or irritability
      4d. Reduced quantity of work
      4e. Poor quality work
      4f. Making more errors
      4g. Relationship difficulties or avoidance
    
    Scoring:
    - Items 4a-4g: 0-4 scale
      0 = Never (0%)
      1 = Sometimes (25%)
      2 = Half the time (50%)
      3 = Most of the time (75%)
      4 = All the time (100%)
    - Total score: 0-28 (sum of items 4a-4g)
    
    Interpretation:
    - Higher scores indicate greater work impairment
    - Scores calculated only when currently employed
    
    Clinical Use:
    - Work functioning assessment
    - Occupational disability evaluation
    - Treatment outcome measurement
    """

    def __init__(self):
        self.name = "LEAPS - Work Productivity Assessment"
        self.description = "Évaluation de la productivité au travail."
        self.num_scored_items = 7
        self.used_in_applications = ['cedr']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize LEAPS items."""
        
        questions = [
            # Informational items (not scored)
            {
                "id": "LEAPS1",
                "number": 1,
                "text": "Quel genre du travail rémunéré faites-vous ?",
                "type": "text",
                "scored": False
            },
            {
                "id": "LEAPS2",
                "number": 2,
                "text": "Au cours des 2 dernières semaines, combien d'heures de travail aviez-vous prévus ou attendiez-vous ?",
                "type": "numeric",
                "unit": "Heures",
                "scored": False
            },
            {
                "id": "LEAPS3",
                "number": 3,
                "text": "Au cours des 2 dernières semaines, combien d'heures de travail avez-vous manqué à cause de la manière dont vous vous sentiez ?",
                "type": "numeric",
                "unit": "Heures",
                "scored": False
            },
            {
                "id": "LEAPS3BIS",
                "number": "3bis",
                "text": "En inactivité professionnelle actuelle (arrêt de travail, invalidité, retraite)",
                "type": "boolean",
                "options": {"Oui": 1, "Non": 0},
                "scored": False
            },
            # Scored items
            {
                "id": "LEAPS4A",
                "number": "4a",
                "text": "Énergie et motivation basse",
                "category": "work_impairment",
                "options": {
                    "Jamais (0%)": 0,
                    "Parfois (25%)": 1,
                    "La moitié du temps (50%)": 2,
                    "La plupart du temps (75%)": 3,
                    "Tout le temps (100%)": 4
                },
                "scored": True
            },
            {
                "id": "LEAPS4B",
                "number": "4b",
                "text": "Faible capacité de concentration ou de mémoire",
                "category": "work_impairment",
                "options": {
                    "Jamais (0%)": 0,
                    "Parfois (25%)": 1,
                    "La moitié du temps (50%)": 2,
                    "La plupart du temps (75%)": 3,
                    "Tout le temps (100%)": 4
                },
                "scored": True
            },
            {
                "id": "LEAPS4C",
                "number": "4c",
                "text": "Anxiété ou irritabilité",
                "category": "work_impairment",
                "options": {
                    "Jamais (0%)": 0,
                    "Parfois (25%)": 1,
                    "La moitié du temps (50%)": 2,
                    "La plupart du temps (75%)": 3,
                    "Tout le temps (100%)": 4
                },
                "scored": True
            },
            {
                "id": "LEAPS4D",
                "number": "4d",
                "text": "Réduction de la quantité de travail effectué",
                "category": "work_impairment",
                "options": {
                    "Jamais (0%)": 0,
                    "Parfois (25%)": 1,
                    "La moitié du temps (50%)": 2,
                    "La plupart du temps (75%)": 3,
                    "Tout le temps (100%)": 4
                },
                "scored": True
            },
            {
                "id": "LEAPS4E",
                "number": "4e",
                "text": "Travail réalisé de mauvaise qualité",
                "category": "work_impairment",
                "options": {
                    "Jamais (0%)": 0,
                    "Parfois (25%)": 1,
                    "La moitié du temps (50%)": 2,
                    "La plupart du temps (75%)": 3,
                    "Tout le temps (100%)": 4
                },
                "scored": True
            },
            {
                "id": "LEAPS4F",
                "number": "4f",
                "text": "Faire plus d'erreur",
                "category": "work_impairment",
                "options": {
                    "Jamais (0%)": 0,
                    "Parfois (25%)": 1,
                    "La moitié du temps (50%)": 2,
                    "La plupart du temps (75%)": 3,
                    "Tout le temps (100%)": 4
                },
                "scored": True
            },
            {
                "id": "LEAPS4G",
                "number": "4g",
                "text": "Avoir des difficultés relationnelles ou éviter autrui",
                "category": "work_impairment",
                "options": {
                    "Jamais (0%)": 0,
                    "Parfois (25%)": 1,
                    "La moitié du temps (50%)": 2,
                    "La plupart du temps (75%)": 3,
                    "Tout le temps (100%)": 4
                },
                "scored": True
            }
        ]
        
        return questions

    def calculate_score(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate LEAPS work impairment score.

        Args:
            responses (Dict[str, Any]): A dictionary of responses. For scored items (4a-4g),
                                       values should be response option text. For informational
                                       items, values can be text or numeric.

        Returns:
            Dict[str, Any]: A dictionary containing total score, interpretation, and item details.
        """
        total_score = 0
        item_scores = {}
        informational_data = {}
        
        # Process informational items
        for question in self.questions:
            if not question.get("scored", False):
                q_id = question["id"]
                if q_id in responses:
                    informational_data[q_id] = responses[q_id]
        
        # Check if currently unemployed
        is_unemployed = informational_data.get("LEAPS3BIS") == "Oui"
        
        # Process scored items
        for question in self.questions:
            if question.get("scored", False):
                q_id = question["id"]
                if q_id not in responses:
                    raise ValueError(f"Missing response for scored question {q_id}")
                
                response_text = responses[q_id]
                if response_text not in question["options"]:
                    raise ValueError(
                        f"Invalid response for question {q_id}. "
                        f"Expected one of: {list(question['options'].keys())}"
                    )
                
                score = question["options"][response_text]
                item_scores[q_id] = score
                total_score += score

        interpretation = self._interpret_score(total_score, is_unemployed)
        impairment_level = self._get_impairment_level(total_score)

        return {
            "total_score": total_score,
            "max_score": 28,
            "interpretation": interpretation,
            "impairment_level": impairment_level,
            "is_unemployed": is_unemployed,
            "item_scores": item_scores,
            "informational_data": informational_data
        }

    def _interpret_score(self, score: int, is_unemployed: bool) -> str:
        """Interpret LEAPS score."""
        if is_unemployed:
            return "Non applicable - Patient en inactivité professionnelle"
        
        if score >= 21:
            return "Altération sévère du fonctionnement au travail"
        elif score >= 14:
            return "Altération modérée à sévère du fonctionnement au travail"
        elif score >= 7:
            return "Altération légère à modérée du fonctionnement au travail"
        elif score >= 1:
            return "Altération minimale du fonctionnement au travail"
        else:
            return "Pas d'altération du fonctionnement au travail"

    def _get_impairment_level(self, score: int) -> str:
        """Get impairment level."""
        if score >= 21:
            return "severe"
        elif score >= 14:
            return "moderate_to_severe"
        elif score >= 7:
            return "mild_to_moderate"
        elif score >= 1:
            return "minimal"
        else:
            return "none"

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "Ce questionnaire évalue votre activité professionnelle et votre productivité "
            "au travail lors des 2 dernières semaines.\n\n"
            "Pour la question 4, limitez s'il vous plaît vos réponses au temps où vous "
            "étiez au travail."
        )


if __name__ == '__main__':
    leaps = LEAPSQuestionnaire()
    print(f"Questionnaire: {leaps.name}")
    print(f"Number of scored items: {leaps.num_scored_items}")
    print()
    
    # Test: Moderate impairment
    test_responses = {
        "LEAPS1": "Employé de bureau",
        "LEAPS2": "35",
        "LEAPS3": "5",
        "LEAPS3BIS": "Non",
        "LEAPS4A": "La moitié du temps (50%)",
        "LEAPS4B": "Parfois (25%)",
        "LEAPS4C": "La moitié du temps (50%)",
        "LEAPS4D": "Parfois (25%)",
        "LEAPS4E": "Parfois (25%)",
        "LEAPS4F": "Jamais (0%)",
        "LEAPS4G": "Parfois (25%)"
    }
    
    result = leaps.calculate_score(test_responses)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Impairment Level: {result['impairment_level']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    print("✓ LEAPS implementation complete - 7 scored items, work productivity assessment")

