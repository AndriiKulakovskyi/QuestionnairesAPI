import random
from typing import Any, Dict, List

class AQ12Questionnaire:
    """AQ-12 - Aggression Questionnaire (Short Form)
    
    Brief self-report measure of aggressive behavior over the past 6 months.
    This is a short form derived from the Buss-Perry Aggression Questionnaire.
    
    Structure:
    - 12 items rated on a 6-point scale (1-6)
    - Response options: 1="Pas du tout moi" to 6="Tout à fait moi"
    - 4 subscales with 3 items each:
      * Physical Aggression (items 1, 5, 9)
      * Verbal Aggression (items 2, 6, 10)
      * Anger (items 3, 7, 11)
      * Hostility (items 4, 8, 12)
    
    Scoring:
    - Each subscale: sum of 3 items (range 3-18)
    - Total score: sum of all items (range 12-72)
    - Higher scores indicate greater aggression
    """

    def __init__(self):
        self.name = "AQ-12 - Aggression Questionnaire (Short Form)"
        self.description = "Questionnaire d'évaluation de l'agressivité (version courte 12 items)."
        self.num_items = 12
        self.used_in_applications = ['ebipolar']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 12 AQ items with their subscale assignments."""
        
        # Response options (French labels with numeric values)
        options = {
            "1 Pas du tout moi": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6 Tout à fait moi": 6
        }

        # Define questions with their subscale assignments
        items_data = [
            (1, "Si on me provoque, je peux cogner.", "physical"),
            (2, "J'exprime souvent mon désaccord avec les autres.", "verbal"),
            (3, "Je m'emporte rapidement.", "anger"),
            (4, "Parfois, j'ai l'impression que je n'ai pas été gâté par la vie comme les autres.", "hostility"),
            (5, "Il y a des personnes qui me gonflent tellement qu'on peut en arriver aux mains.", "physical"),
            (6, "Je ne peux pas m'empêcher d'entrer en conflit quand les autres ne sont pas d'accord avec moi.", "verbal"),
            (7, "Parfois, je pète un câble sans raison.", "anger"),
            (8, "Je me demande parfois pourquoi je ressens tant d'amertume.", "hostility"),
            (9, "J'ai déjà menacé quelqu'un.", "physical"),
            (10, "Mes amis disent que j'ai l'esprit de contradiction.", "verbal"),
            (11, "J'ai du mal à contrôler mon humeur.", "anger"),
            (12, "Les autres semblent toujours avoir plus de chances que moi.", "hostility")
        ]

        questions = []
        for item_num, text, subscale in items_data:
            questions.append({
                "id": f"AQ12_{item_num}",
                "number": item_num,
                "text": f"{item_num}. {text}",
                "options": options,
                "subscale": subscale
            })
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        Calculate subscale and total scores for the AQ-12.

        Args:
            responses (Dict[str, str]): A dictionary of responses, where the key is the question ID
                                       (e.g., "AQ12_1") and the value is the response option text
                                       (e.g., "1 Pas du tout moi", "6 Tout à fait moi").

        Returns:
            Dict[str, Any]: A dictionary containing subscale scores, total score, and interpretation.
        """
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")

        # Initialize subscale scores
        subscale_scores = {
            "physical": 0,
            "verbal": 0,
            "anger": 0,
            "hostility": 0
        }
        
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
            
            item_score = question["options"][response_text]
            item_scores[q_id] = item_score
            subscale_scores[question["subscale"]] += item_score

        # Calculate total score
        total_score = sum(subscale_scores.values())

        # Interpret subscale scores
        interpretations = {}
        for subscale, score in subscale_scores.items():
            if score >= 15:
                level = "Élevé"
            elif score >= 12:
                level = "Modérément élevé"
            elif score >= 9:
                level = "Moyen"
            else:
                level = "Faible"
            interpretations[subscale] = level

        # Overall interpretation
        if total_score >= 60:
            overall_interpretation = "Niveau d'agressivité très élevé"
            risk_level = "very_high"
        elif total_score >= 48:
            overall_interpretation = "Niveau d'agressivité élevé"
            risk_level = "high"
        elif total_score >= 36:
            overall_interpretation = "Niveau d'agressivité modéré"
            risk_level = "moderate"
        elif total_score >= 24:
            overall_interpretation = "Niveau d'agressivité faible"
            risk_level = "low"
        else:
            overall_interpretation = "Niveau d'agressivité très faible"
            risk_level = "very_low"

        return {
            "subscales": {
                "physical_aggression": subscale_scores["physical"],
                "verbal_aggression": subscale_scores["verbal"],
                "anger": subscale_scores["anger"],
                "hostility": subscale_scores["hostility"]
            },
            "subscale_interpretations": interpretations,
            "total_score": total_score,
            "min_score": 12,
            "max_score": 72,
            "interpretation": overall_interpretation,
            "risk_level": risk_level,
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
            "Cochez la case qui décrit le mieux ce que vous avez ressenti et comment vous "
            "vous êtes comporté(e) au cours des 6 derniers mois.\n\n"
            "Échelle:\n"
            "1 - Pas du tout moi\n"
            "2, 3, 4, 5 - Niveaux intermédiaires\n"
            "6 - Tout à fait moi"
        )


if __name__ == '__main__':
    aq12 = AQ12Questionnaire()
    print(f"Questionnaire: {aq12.name}")
    print(f"Description: {aq12.description}")
    print(f"Number of items: {aq12.num_items}")
    print(f"Used in applications: {aq12.used_in_applications}")
    print()
    print("="*80)
    print("INSTRUCTION:")
    print(aq12.get_instruction())
    print("="*80)
    print()
    
    print("Questions by subscale:")
    subscales = {"physical": "Physical Aggression", "verbal": "Verbal Aggression", 
                 "anger": "Anger", "hostility": "Hostility"}
    for subscale, name in subscales.items():
        print(f"\n{name}:")
        for q in aq12.questions:
            if q["subscale"] == subscale:
                print(f"  {q['text']}")
    print()
    print("="*80)
    
    # Test with high aggression profile
    print("\nExample 1: High aggression profile")
    high_aggression = {}
    for question in aq12.questions:
        high_aggression[question['id']] = "6 Tout à fait moi"
    
    result = aq12.calculate_score(high_aggression)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Interpretation: {result['interpretation']}")
    print("\nSubscale scores:")
    subscale_map = {"physical_aggression": "physical", "verbal_aggression": "verbal", 
                    "anger": "anger", "hostility": "hostility"}
    for subscale, score in result['subscales'].items():
        interp_key = subscale_map.get(subscale, subscale)
        print(f"  {subscale}: {score}/18 ({result['subscale_interpretations'][interp_key]})")
    print()
    
    # Test with low aggression profile
    print("Example 2: Low aggression profile")
    low_aggression = {}
    for question in aq12.questions:
        low_aggression[question['id']] = "1 Pas du tout moi"
    
    result = aq12.calculate_score(low_aggression)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Interpretation: {result['interpretation']}")
    print("\nSubscale scores:")
    for subscale, score in result['subscales'].items():
        interp_key = subscale_map.get(subscale, subscale)
        print(f"  {subscale}: {score}/18 ({result['subscale_interpretations'][interp_key]})")
    print()
    
    # Test with random responses
    print("Example 3: Random responses")
    random_responses = aq12.get_random_responses()
    result = aq12.calculate_score(random_responses)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Interpretation: {result['interpretation']}")
    print("\nSubscale scores:")
    for subscale, score in result['subscales'].items():
        interp_key = subscale_map.get(subscale, subscale)
        print(f"  {subscale}: {score}/18 ({result['subscale_interpretations'][interp_key]})")
    print()
    
    print("="*80)
    print("✓ AQ-12 Aggression Questionnaire implementation complete")
    print("  - 12 items with 6-point scale")
    print("  - 4 subscales: Physical, Verbal, Anger, Hostility")
    print("  - Validated scoring algorithm")
    print("  - Clinical interpretation for subscales and total")

