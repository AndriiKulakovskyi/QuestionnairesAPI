import random
from typing import Any, Dict, List

class BFIQuestionnaire:
    """BFI - Big Five Inventory (45-item version)
    
    Self-report questionnaire assessing the Big Five personality dimensions.
    
    Structure:
    - 45 items total across 5 dimensions:
      1. Extraversion (8 items): items 1,6,11,16,21,26,31,36
      2. Agreeableness (10 items): items 2,7,12,17,22,27,32,37,42,45
      3. Conscientiousness (9 items): items 3,8,13,18,23,28,33,38,43
      4. Neuroticism/Emotional Negativity (8 items): items 4,9,14,19,24,29,34,39
      5. Openness to Experience (10 items): items 5,10,15,20,25,30,35,40,41,44
    
    Scoring:
    - 5-point scale (1-5)
    - Some items reverse-scored
    - Mean scores calculated for each dimension (not totals)
    - Mean range: 1.0-5.0 per dimension
    
    Clinical Use:
    - Personality assessment in research and clinical practice
    - Treatment planning
    - Understanding individual differences
    """

    def __init__(self):
        self.name = "BFI - Big Five Inventory"
        self.description = "Inventaire des Cinq Grands facteurs de personnalité."
        self.num_items = 45
        self.used_in_applications = ['cedr']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 45 BFI items."""
        
        # Subscale assignments
        extraversion_items = [1, 6, 11, 16, 21, 26, 31, 36]
        agreeableness_items = [2, 7, 12, 17, 22, 27, 32, 37, 42, 45]
        conscientiousness_items = [3, 8, 13, 18, 23, 28, 33, 38, 43]
        neuroticism_items = [4, 9, 14, 19, 24, 29, 34, 39]
        openness_items = [5, 10, 15, 20, 25, 30, 35, 40, 41, 44]
        
        # Reverse-scored items (based on response option order in PHP)
        reverse_items = [2, 6, 8, 9, 12, 18, 21, 23, 24, 27, 31, 34, 35, 37, 41, 43, 45]
        
        items_text = [
            "est bavard",
            "a tendance à critiquer les autres",
            "travaille consciencieusement",
            "est déprimé, cafardeux",
            "est créatif, plein d'idées originales",
            "est réservé",
            "est serviable et n'est pas égoïste avec les autres",
            "peut être parfois négligent",
            "est \"relaxe\", détendu, gère bien les stress",
            "s'intéresse à de nombreux sujets",
            "est plein d'énergie",
            "commence facilement à se disputer avec les autres",
            "est fiable dans son travail",
            "peut être angoissé",
            "est ingénieux, une grosse tête",
            "communique beaucoup d'enthousiasme",
            "est indulgent de nature",
            "a tendance à être désorganisé",
            "se tourmente beaucoup",
            "a une grande imagination",
            "a tendance à être silencieux",
            "fait généralement confiance aux autres",
            "a tendance à être paresseux",
            "est quelqu'un de tempéré, pas facilement troublé",
            "est inventif",
            "a une forte personnalité, s'exprime avec assurance",
            "est parfois dédaigneux, méprisant",
            "persévère jusqu'à ce que sa tâche soit finie",
            "peut être lunatique d'humeur changeante",
            "apprécie les activités artistiques et esthétiques",
            "est quelquefois timide, inhibé",
            "est prévenant et gentil avec presque tout le monde",
            "est efficace dans son travail",
            "reste calme dans les situations angoissantes",
            "préfère un travail simple et routinier",
            "est sociable, extraverti",
            "est parfois impoli avec les autres",
            "fait des projets et les poursuit",
            "est facilement anxieux",
            "aime réfléchir et jouer avec des idées",
            "est peu intéressé par tout ce qui est artistique",
            "aime coopérer avec les autres",
            "est facilement distrait",
            "a de bonnes connaissances en art, musique ou en littérature",
            "cherche des histoires aux autres"
        ]
        
        questions = []
        for i, text in enumerate(items_text, 1):
            # Determine subscale
            if i in extraversion_items:
                subscale = "extraversion"
            elif i in agreeableness_items:
                subscale = "agreeableness"
            elif i in conscientiousness_items:
                subscale = "conscientiousness"
            elif i in neuroticism_items:
                subscale = "neuroticism"
            else:
                subscale = "openness"
            
            # Response options depend on reverse scoring
            if i in reverse_items:
                options = {
                    "désapprouve fortement": 5,
                    "désapprouve un peu": 4,
                    "n'approuve ni ne désapprouve": 3,
                    "approuve un peu": 2,
                    "approuve fortement": 1
                }
            else:
                options = {
                    "désapprouve fortement": 1,
                    "désapprouve un peu": 2,
                    "n'approuve ni ne désapprouve": 3,
                    "approuve un peu": 4,
                    "approuve fortement": 5
                }
            
            questions.append({
                "id": f"BFI{i}",
                "number": i,
                "text": f"{i}. Je me vois comme quelqu'un qui {text}",
                "options": options,
                "subscale": subscale,
                "reverse_scored": i in reverse_items
            })
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        Calculate BFI mean scores for each personality dimension.

        Args:
            responses (Dict[str, str]): A dictionary of responses, where the key is the question ID
                                       (e.g., "BFI1") and the value is the response option text.

        Returns:
            Dict[str, Any]: A dictionary containing mean scores for each dimension with interpretations.
        """
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")

        # Initialize subscale scores
        subscale_sums = {
            'extraversion': 0,
            'agreeableness': 0,
            'conscientiousness': 0,
            'neuroticism': 0,
            'openness': 0
        }
        subscale_counts = {
            'extraversion': 0,
            'agreeableness': 0,
            'conscientiousness': 0,
            'neuroticism': 0,
            'openness': 0
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
            
            score = question["options"][response_text]
            item_scores[q_id] = score
            
            subscale = question["subscale"]
            subscale_sums[subscale] += score
            subscale_counts[subscale] += 1

        # Calculate mean scores
        subscale_means = {}
        for subscale in subscale_sums:
            subscale_means[subscale] = round(subscale_sums[subscale] / subscale_counts[subscale], 2)

        return {
            "subscale_means": subscale_means,
            "subscale_interpretations": {
                "extraversion": self._interpret_subscale(subscale_means['extraversion']),
                "agreeableness": self._interpret_subscale(subscale_means['agreeableness']),
                "conscientiousness": self._interpret_subscale(subscale_means['conscientiousness']),
                "neuroticism": self._interpret_subscale(subscale_means['neuroticism']),
                "openness": self._interpret_subscale(subscale_means['openness'])
            },
            "item_scores": item_scores
        }

    def _interpret_subscale(self, mean_score: float) -> str:
        """Interpret subscale mean score."""
        if mean_score >= 4.5:
            return "Très élevé"
        elif mean_score >= 4.0:
            return "Élevé"
        elif mean_score >= 3.0:
            return "Moyen"
        elif mean_score >= 2.0:
            return "Faible"
        else:
            return "Très faible"

    def get_random_responses(self) -> Dict[str, str]:
        """Generates random valid responses for testing purposes."""
        responses = {}
        for question in self.questions:
            responses[question["id"]] = random.choice(list(question["options"].keys()))
        return responses

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "Vous allez trouver un certain nombre de qualificatifs qui peuvent ou non "
            "s'appliquer à vous. Choisissez pour chaque affirmation combien vous "
            "approuvez ou désapprouvez l'affirmation.\n\n"
            "Échelle de réponse:\n"
            "- désapprouve fortement\n"
            "- désapprouve un peu\n"
            "- n'approuve ni ne désapprouve\n"
            "- approuve un peu\n"
            "- approuve fortement"
        )


if __name__ == '__main__':
    bfi = BFIQuestionnaire()
    print(f"Questionnaire: {bfi.name}")
    print(f"Description: {bfi.description}")
    print(f"Number of items: {bfi.num_items}")
    print()
    
    # Test case: High extraversion, low neuroticism
    print("Example: Testing BFI scoring")
    test_responses = {}
    for q in bfi.questions:
        # High scores on extraversion, low on neuroticism
        if q['subscale'] == 'extraversion':
            if q['reverse_scored']:
                test_responses[q['id']] = "approuve fortement"  # Will be scored as 1
            else:
                test_responses[q['id']] = "approuve fortement"  # Will be scored as 5
        elif q['subscale'] == 'neuroticism':
            if q['reverse_scored']:
                test_responses[q['id']] = "approuve fortement"  # Will be scored high
            else:
                test_responses[q['id']] = "désapprouve fortement"  # Will be scored as 1
        else:
            # Moderate responses for others
            test_responses[q['id']] = "n'approuve ni ne désapprouve"
    
    result = bfi.calculate_score(test_responses)
    print("\nSubscale Mean Scores (1.0-5.0):")
    for subscale, mean in result['subscale_means'].items():
        interpretation = result['subscale_interpretations'][subscale]
        print(f"  {subscale.capitalize()}: {mean:.2f} - {interpretation}")
    
    print()
    print("="*80)
    print("✓ BFI implementation complete")
    print("  - 45 items across Big Five personality dimensions")
    print("  - Mean scores (not totals) for each dimension")
    print("  - Extraversion, Agreeableness, Conscientiousness, Neuroticism, Openness")

