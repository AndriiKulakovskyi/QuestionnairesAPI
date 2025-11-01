import random
from typing import Any, Dict, List

class TypeCircadienQuestionnaire:
    """ITC - Individual Circadian Type / Type Circadien Individuel
    
    Self-report questionnaire assessing individual circadian type preferences.
    Measures flexibility/rigidity and languid/vigorous dimensions of circadian rhythms.
    
    Structure:
    - 11 items with 5-point response scale
    - 2 subscales:
      * FR (Flexibility/Rigidity): items 2, 4, 6, 8, 10 (5 items)
      * LV (Languid/Vigorous): items 1, 3, 5, 7, 9, 11 (6 items)
    
    Scoring:
    - Each item: 1-5 scale
      ("Presque jamais"=1, "Rarement"=2, "Parfois"=3, "En général"=4, "Presque toujours"=5)
    - FR score: sum of items 2, 4, 6, 8, 10 (range 5-25)
    - LV score: sum of items 1, 3, 5, 7, 9, 11 (range 6-30)
    
    Interpretation:
    - FR (Flexibility/Rigidity): Higher scores indicate more flexibility
    - LV (Languid/Vigorous): Higher scores indicate more languid/fatigued tendency
    """

    def __init__(self):
        self.name = "ITC - Type Circadien Individuel"
        self.description = "Questionnaire d'évaluation du type circadien individuel."
        self.num_items = 11
        self.used_in_applications = ['ebipolar']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 11 ITC items with their subscale assignments."""
        
        # Response options (same for all items)
        options = {
            "Presque jamais": 1,
            "Rarement": 2,
            "Parfois": 3,
            "En général": 4,
            "Presque toujours": 5
        }

        items_data = [
            (1, "Avez vous tendance à avoir besoin de plus de sommeil que les autres personnes ?", "lv"),
            (2, "Si vous aviez à faire un certain travail au milieu de la nuit, pensez vous que vous pourriez le faire presque aussi facilement qu'à une heure plus normale de la journée ?", "fr"),
            (3, "Est-ce que vous trouvez qu'il est difficile de vous réveiller correctement si vous êtes réveillé à une heure inhabituelle?", "lv"),
            (4, "Aimez vous travailler à des heures inhabituelles du jour ou de la nuit ?", "fr"),
            (5, "Si vous allez au lit très tard, avez vous besoin de dormir plus tard le lendemain matin ?", "lv"),
            (6, "Si vous avez beaucoup à faire, pouvez vous travailler tard le soir pour terminer sans être trop fatigué ?", "fr"),
            (7, "Vous sentez-vous endormi pendant un certain temps après le réveil le matin ?", "lv"),
            (8, "Trouvez vous aussi facile de travailler tard la nuit que tôt le matin ?", "fr"),
            (9, "Si vous devez vous lever très tôt un matin, avez vous tendance à vous sentir fatigué toute la journée ?", "lv"),
            (10, "Seriez-vous aussi content de faire quelque chose au milieu de la nuit que pendant la journée ?", "fr"),
            (11, "Devez-vous compter sur un réveil, ou sur quelqu'un d'autre, pour vous réveiller le matin ?", "lv")
        ]

        questions = []
        for num, text, subscale in items_data:
            questions.append({
                "id": f"ITC{num}",
                "number": num,
                "text": f"{num}. {text}",
                "options": options,
                "subscale": subscale
            })
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        Calculate ITC subscale scores.

        Args:
            responses (Dict[str, str]): A dictionary of responses, where the key is the question ID
                                       (e.g., "ITC1") and the value is the response option text.

        Returns:
            Dict[str, Any]: A dictionary containing subscale scores and interpretations.
        """
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")

        # Initialize subscale scores
        fr_score = 0  # Flexibility/Rigidity
        lv_score = 0  # Languid/Vigorous
        
        item_scores = {}
        
        # Calculate scores
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
            
            score = question["options"][response_text]
            item_scores[q_id] = score
            
            # Add to appropriate subscale
            if question["subscale"] == "fr":
                fr_score += score
            elif question["subscale"] == "lv":
                lv_score += score

        # Interpret FR score (Flexibility/Rigidity)
        if fr_score >= 20:
            fr_interp = "Très flexible (adaptabilité élevée aux horaires variables)"
        elif fr_score >= 15:
            fr_interp = "Flexible (bonne adaptabilité)"
        elif fr_score >= 10:
            fr_interp = "Intermédiaire"
        else:
            fr_interp = "Rigide (préférence pour des horaires fixes)"

        # Interpret LV score (Languid/Vigorous)
        if lv_score >= 24:
            lv_interp = "Très languide (besoin élevé de sommeil, fatigue matinale)"
        elif lv_score >= 18:
            lv_interp = "Languide (tendance à la fatigue)"
        elif lv_score >= 12:
            lv_interp = "Intermédiaire"
        else:
            lv_interp = "Vigoureux (peu de sommeil nécessaire, éveillé facilement)"

        return {
            "subscales": {
                "flexibility_rigidity": fr_score,
                "languid_vigorous": lv_score
            },
            "subscale_ranges": {
                "flexibility_rigidity": "5-25",
                "languid_vigorous": "6-30"
            },
            "interpretations": {
                "flexibility_rigidity": fr_interp,
                "languid_vigorous": lv_interp
            },
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
            "Les questions suivantes concernent vos habitudes quotidiennes et vos préférences. "
            "Merci d'indiquer ce que vous préférez faire ou pouvez faire mais pas ce que vous êtes "
            "forcés de faire en raison d'engagements professionnels. "
            "Merci de répondre aux questions le plus rapidement possible "
            "(entourez une seule réponse par question)."
        )


if __name__ == '__main__':
    itc = TypeCircadienQuestionnaire()
    print(f"Questionnaire: {itc.name}")
    print(f"Description: {itc.description}")
    print(f"Number of items: {itc.num_items}")
    print(f"Used in applications: {itc.used_in_applications}")
    print()
    print("="*80)
    print("INSTRUCTION:")
    print(itc.get_instruction())
    print("="*80)
    print()
    
    print("Sample items (first 4):")
    for q in itc.questions[:4]:
        print(f"\n{q['text']}")
        print(f"  Subscale: {q['subscale'].upper()}")
    print()
    print("="*80)
    
    # Test with flexible, vigorous profile
    print("\nExample 1: Flexible and Vigorous")
    flexible_vigorous = {}
    for q in itc.questions:
        # FR items: high scores (flexible), LV items: low scores (vigorous)
        if q['subscale'] == 'fr':
            flexible_vigorous[q['id']] = "Presque toujours"
        else:  # lv
            flexible_vigorous[q['id']] = "Presque jamais"
    
    result = itc.calculate_score(flexible_vigorous)
    print(f"FR (Flexibility/Rigidity): {result['subscales']['flexibility_rigidity']}/25")
    print(f"  → {result['interpretations']['flexibility_rigidity']}")
    print(f"LV (Languid/Vigorous): {result['subscales']['languid_vigorous']}/30")
    print(f"  → {result['interpretations']['languid_vigorous']}")
    print()
    
    # Test with rigid, languid profile
    print("Example 2: Rigid and Languid")
    rigid_languid = {}
    for q in itc.questions:
        # FR items: low scores (rigid), LV items: high scores (languid)
        if q['subscale'] == 'fr':
            rigid_languid[q['id']] = "Presque jamais"
        else:  # lv
            rigid_languid[q['id']] = "Presque toujours"
    
    result = itc.calculate_score(rigid_languid)
    print(f"FR (Flexibility/Rigidity): {result['subscales']['flexibility_rigidity']}/25")
    print(f"  → {result['interpretations']['flexibility_rigidity']}")
    print(f"LV (Languid/Vigorous): {result['subscales']['languid_vigorous']}/30")
    print(f"  → {result['interpretations']['languid_vigorous']}")
    print()
    
    # Test with random responses
    print("Example 3: Random profile")
    random_responses = itc.get_random_responses()
    result = itc.calculate_score(random_responses)
    print(f"FR (Flexibility/Rigidity): {result['subscales']['flexibility_rigidity']}/25")
    print(f"  → {result['interpretations']['flexibility_rigidity']}")
    print(f"LV (Languid/Vigorous): {result['subscales']['languid_vigorous']}/30")
    print(f"  → {result['interpretations']['languid_vigorous']}")
    print()
    
    print("="*80)
    print("✓ Type Circadien (ITC) implementation complete")
    print("  - 11 items with 5-point scale")
    print("  - 2 subscales: FR (Flexibility/Rigidity), LV (Languid/Vigorous)")
    print("  - Assesses individual circadian preferences")
    print("  - Useful for understanding sleep-wake patterns")

