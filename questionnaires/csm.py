import random
from typing import Any, Dict, List, Tuple

class CSMQuestionnaire:
    """CSM - Composite Scale of Morningness (Échelle de Matinalité)
    
    Self-report questionnaire assessing circadian preference (chronotype).
    Measures the degree to which individuals prefer morning versus evening activities.
    
    Structure:
    - 13 items assessing sleep/wake preferences and alertness patterns
    - Variable response options per item (4-5 choices)
    - Items use different scoring patterns
    
    Scoring:
    - Total score range: 13-55
    - Higher scores indicate morning preference (morning type)
    - Lower scores indicate evening preference (evening type)
    
    Interpretation:
    - 13-21: Definite evening type
    - 22-30: Moderate evening type
    - 31-43: Neither/Intermediate type
    - 44-52: Moderate morning type
    - 53-55: Definite morning type
    """

    def __init__(self):
        self.name = "CSM - Composite Scale of Morningness"
        self.description = "Questionnaire d'évaluation du chronotype (matinalité-vespéralité)."
        self.num_items = 13
        self.used_in_applications = ['ebipolar']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 13 CSM items with their specific response options and scoring."""
        
        questions = []
        
        # Item 1: Wake time preference (5 options, reverse scored 5-1)
        questions.append({
            "id": "CSM1",
            "number": 1,
            "text": "1. En ne considérant que le rythme de vie qui vous convient le mieux, à quelle heure vous lèveriez-vous en étant entièrement libre d'organiser votre journée",
            "options": {
                "Entre 5h00 et 6h30": 5,
                "Entre 6h30 et 7h45": 4,
                "Entre 7h45 et 9h45": 3,
                "Entre 9h45 et 11h00": 2,
                "Entre 11h00 et midi": 1
            }
        })
        
        # Item 2: Bed time preference (5 options, reverse scored 5-1)
        questions.append({
            "id": "CSM2",
            "number": 2,
            "text": "2. En ne considérant que le rythme de vie qui vous convient le mieux, à quelle heure vous coucheriez-vous sachant que vous êtes entièrement libre d'organiser votre soirée",
            "options": {
                "Entre 20h00 et 21h00": 5,
                "Entre 21h00 et 22h15": 4,
                "Entre 22h15 et 0h30": 3,
                "Entre 0h30 et 1h45": 2,
                "Entre 1h45 et 3h00": 1
            }
        })
        
        # Item 3: Ease of waking (4 options, direct 1-4)
        questions.append({
            "id": "CSM3",
            "number": 3,
            "text": "3. Dans des conditions adéquates (environnement favorable, sans contraintes particulières, etc.), à quel point cela vous est-il facile de vous lever le matin",
            "options": {
                "Pas facile du tout": 1,
                "Pas très facile": 2,
                "Assez facile": 3,
                "Très facile": 4
            }
        })
        
        # Item 4: Alertness after waking (4 options, direct 1-4)
        questions.append({
            "id": "CSM4",
            "number": 4,
            "text": "4. Comment vous sentez-vous durant la demi-heure qui suit votre réveil du matin",
            "options": {
                "Pas du tout réveillé": 1,
                "Peu éveillé": 2,
                "Relativement éveillé": 3,
                "Très éveillé": 4
            }
        })
        
        # Item 5: Energy after waking (4 options, direct 1-4)
        questions.append({
            "id": "CSM5",
            "number": 5,
            "text": "5. Comment vous sentez-vous durant la demi-heure qui suit votre réveil du matin",
            "options": {
                "Très fatigué": 1,
                "Plutôt fatigué": 2,
                "Plutôt en forme": 3,
                "Tout à fait frais et dispos": 4
            }
        })
        
        # Item 6: Early morning exercise (4 options, reverse 4-1)
        questions.append({
            "id": "CSM6",
            "number": 6,
            "text": "6. Vous avez décidé de faire un sport. Un ami vous suggère de faire deux fois par semaine des séances d'une heure. Le meilleur moment pour lui est de 7 à 8 heures du matin. Ne considérant que le rythme qui vous convient le mieux, dans quelle forme pensez-vous être",
            "options": {
                "Bonne forme": 4,
                "Forme raisonnable": 3,
                "Vous trouvez cela difficile": 2,
                "Vous trouvez cela très difficile": 1
            }
        })
        
        # Item 7: Evening tiredness (5 options, reverse 5-1)
        questions.append({
            "id": "CSM7",
            "number": 7,
            "text": "7. A quelle heure dans la soirée vous sentez-vous fatigué au point de devoir aller vous coucher",
            "options": {
                "Entre 20h00 et 21h00": 5,
                "Entre 21h00 et 22h15": 4,
                "Entre 22h15 et 0h30": 3,
                "Entre 0h30 et 1h45": 2,
                "Entre 1h45 et 3h00": 1
            }
        })
        
        # Item 8: Optimal exam time (4 options, reverse 4-1)
        questions.append({
            "id": "CSM8",
            "number": 8,
            "text": "8. Vous devez être à votre maximum de performance pour un examen écrit qui dure 2 heures. On vous laisse libre de choisir l'heure à laquelle vous pensez être le plus efficace. Ce sera",
            "options": {
                "Entre 8h00 et 10h00": 4,
                "Entre 11h00 et 13h00": 3,
                "Entre 15h00 et 17h00": 2,
                "Entre 19h00 et 21h00": 1
            }
        })
        
        # Item 9: Morning/evening person (4 options, reverse 4-1)
        questions.append({
            "id": "CSM9",
            "number": 9,
            "text": "9. On entend souvent dire que telle personne est 'du matin' et que telle autre personne est 'du soir'. En ce qui vous concerne, vous seriez",
            "options": {
                "Tout à fait du matin": 4,
                "Plutôt du matin que du soir": 3,
                "Plutôt du soir que du matin": 2,
                "Tout à fait du soir": 1
            }
        })
        
        # Item 10: Work day wake time (4 options, reverse 4-1)
        questions.append({
            "id": "CSM10",
            "number": 10,
            "text": "10. A quelle heure vous lèveriez-vous en prévision d'une journée de travail de 8 heures que vous êtes totalement libre d'organiser",
            "options": {
                "Avant 6h30": 4,
                "Entre 6h30 et 7h30": 3,
                "Entre 7h30 et 8h30": 2,
                "Après 8h30": 1
            }
        })
        
        # Item 11: Difficulty waking at 6am (4 options, direct 1-4)
        questions.append({
            "id": "CSM11",
            "number": 11,
            "text": "11. Si vous deviez toujours vous lever à 6h00, cela vous paraitrait",
            "options": {
                "Affreusement difficile": 1,
                "Plutôt difficile et déplaisant": 2,
                "Déplaisant sans plus": 3,
                "Sans aucune difficulté": 4
            }
        })
        
        # Item 12: Time to feel fully awake (4 options, reverse 4-1)
        questions.append({
            "id": "CSM12",
            "number": 12,
            "text": "12. Après une bonne nuit de sommeil, combien de temps vous faut-il pour être pleinement réveillé",
            "options": {
                "Moins de 10 minutes": 4,
                "Entre 11 et 20 minutes": 3,
                "Entre 21 et 40 minutes": 2,
                "Plus de 40 minutes": 1
            }
        })
        
        # Item 13: Most active time of day (4 options, reverse 4-1)
        questions.append({
            "id": "CSM13",
            "number": 13,
            "text": "13. Dans quelle partie de la journée êtes-vous le plus actif",
            "options": {
                "Nettement actif le matin (bien réveillé le matin et fatigué le soir)": 4,
                "Plutôt actif le matin": 3,
                "Plutôt actif le soir": 2,
                "Nettement actif le soir (fatigué le matin et bien réveillé le soir)": 1
            }
        })
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        Calculate the CSM total score and determine chronotype.

        Args:
            responses (Dict[str, str]): A dictionary of responses, where the key is the question ID
                                       (e.g., "CSM1") and the value is the response option text.

        Returns:
            Dict[str, Any]: A dictionary containing the total score and chronotype interpretation.
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
                    f"Invalid response '{response_text}' for question {q_id}. "
                    f"Valid options are: {list(question['options'].keys())}"
                )
            
            item_score = question["options"][response_text]
            item_scores[q_id] = item_score
            total_score += item_score

        # Determine chronotype
        if total_score >= 53:
            chronotype = "Définitivement du matin"
            category = "definite_morning"
        elif total_score >= 44:
            chronotype = "Modérément du matin"
            category = "moderate_morning"
        elif total_score >= 31:
            chronotype = "Type intermédiaire (ni du matin ni du soir)"
            category = "intermediate"
        elif total_score >= 22:
            chronotype = "Modérément du soir"
            category = "moderate_evening"
        else:
            chronotype = "Définitivement du soir"
            category = "definite_evening"

        return {
            "total_score": total_score,
            "min_score": 13,
            "max_score": 55,
            "chronotype": chronotype,
            "category": category,
            "item_scores": item_scores
        }

    def get_random_responses(self) -> Dict[str, str]:
        """Generates random valid responses for testing purposes."""
        responses = {}
        for question in self.questions:
            q_id = question["id"]
            responses[q_id] = random.choice(list(question["options"].keys()))
        return responses

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "Les 13 questions suivantes concernent vos rythmes veille-sommeil et activité-repos. "
            "Cochez une seule réponse par question."
        )


if __name__ == '__main__':
    csm = CSMQuestionnaire()
    print(f"Questionnaire: {csm.name}")
    print(f"Description: {csm.description}")
    print(f"Number of items: {csm.num_items}")
    print(f"Used in applications: {csm.used_in_applications}")
    print()
    print("="*80)
    print("INSTRUCTION:")
    print(csm.get_instruction())
    print("="*80)
    print()
    
    print("Sample questions:")
    for i, q in enumerate(csm.questions[:3]):
        print(f"\n{q['text']}")
        print("Options:")
        for option, score in q['options'].items():
            print(f"  {option} → {score}")
    print()
    print("="*80)
    
    # Test with definite morning type
    print("\nExample 1: Definite morning type")
    morning_responses = {}
    for question in csm.questions:
        # Select option with highest score (morning preference)
        max_score_option = max(question['options'].items(), key=lambda x: x[1])[0]
        morning_responses[question['id']] = max_score_option
    
    result = csm.calculate_score(morning_responses)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Chronotype: {result['chronotype']}")
    print()
    
    # Test with definite evening type
    print("Example 2: Definite evening type")
    evening_responses = {}
    for question in csm.questions:
        # Select option with lowest score (evening preference)
        min_score_option = min(question['options'].items(), key=lambda x: x[1])[0]
        evening_responses[question['id']] = min_score_option
    
    result = csm.calculate_score(evening_responses)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Chronotype: {result['chronotype']}")
    print()
    
    # Test with random responses
    print("Example 3: Random responses")
    random_responses = csm.get_random_responses()
    result = csm.calculate_score(random_responses)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Chronotype: {result['chronotype']}")
    print()
    
    print("="*80)
    print("✓ CSM Questionnaire implementation complete")
    print("  - 13 items with variable response options")
    print("  - Complex scoring patterns per item")
    print("  - Chronotype classification (morning/evening preference)")
    print("  - Score range: 13-55")

