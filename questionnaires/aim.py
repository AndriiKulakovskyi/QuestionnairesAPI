import random
from typing import Any, Dict, List

class AIMQuestionnaire:
    """AIM - Affective Intensity Measure
    
    Self-report questionnaire assessing the intensity and variability of emotional experiences.
    Developed to measure stable individual differences in the strength with which individuals
    typically experience their emotions.
    
    Scoring:
    - 20 items rated on a 6-point scale (1-6)
    - Response options: 1=Jamais, 2=Presque jamais, 3=Occasionnellement, 
      4=Habituellement, 5=Presque toujours, 6=Toujours
    - Reverse-scored items: 5, 10, 13, 15, 18, 20
      (items describing calm/moderate emotional responses)
    - Direct-scored items: 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 14, 16, 17, 19
      (items describing intense emotional responses)
    - Total score: Average of all items (sum / 20)
    - Score range: 1.0 to 6.0
    
    Interpretation:
    - Higher scores indicate more intense emotional experiences
    - Lower scores indicate more moderate/calm emotional responses
    """

    def __init__(self):
        self.name = "AIM - Affective Intensity Measure"
        self.description = "Questionnaire d'évaluation de l'intensité des expériences émotionnelles."
        self.num_items = 20
        self.used_in_applications = ['ebipolar']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 20 AIM items with their response options."""
        
        # Response options (French labels with numeric values)
        options = {
            "1 - Jamais": 1,
            "2 - Presque jamais": 2,
            "3 - Occasionnellement": 3,
            "4 - Habituellement": 4,
            "5 - Presque toujours": 5,
            "6 - Toujours": 6
        }

        # Items requiring reverse scoring (calm/moderate emotional responses)
        reverse_items = [5, 10, 13, 15, 18, 20]

        question_texts = [
            "Quand je suis heureux(se), c'est avec une forte exubérance",  # 1 - direct
            "Mes périodes d'humeur joyeuse sont si fortes que j'ai l'impression d'être au paradis",  # 2 - direct
            "Si je termine une tâche que je jugeais impossible à faire, je me sens en extase",  # 3 - direct
            "Les films tristes me touchent profondément",  # 4 - direct
            "Quand je suis heureux(se), c'est un sentiment d'être sans inquiétude et content(e) plutôt qu'excité(e) et plein d'enthousiasme",  # 5 - reverse
            "Quand je parle devant un groupe pour la première fois, ma voix devient tremblante et mon cœur bat vite",  # 6 - direct
            "Quand je me sens bien, c'est facile pour moi d'osciller entre des périodes de bonne humeur et des moments où je suis très joyeux(se)",  # 7 - direct
            "Quand je suis heureux(se), je me sens comme si j'éclatais de joie",  # 8 - direct
            "Quand je suis heureux(se), je me sens pleine d'énergie",  # 9 - direct
            "Quand je réussis quelque chose, ma réaction est une satisfaction calme",  # 10 - reverse
            "Quand je fais quelque chose de mal, j'ai un sentiment très fort de culpabilité et de honte",  # 11 - direct
            "Quand les choses vont bien, je me sens comme si j'étais « au sommet du monde »",  # 12 - direct
            "Quand je sais que j'ai fait quelque chose très bien, je me sens détendu(e) et content(e) plutôt qu'excité(e) et exalté(e)",  # 13 - reverse
            "Quand je suis anxieux(se), c'est habituellement très fort",  # 14 - direct
            "Quand je me sens heureux(se), c'est un sentiment de bonheur calme",  # 15 - reverse
            "Quand je suis heureux(se), je déborde d'énergie",  # 16 - direct
            "Quand je me sens coupable, cette émotion est forte",  # 17 - direct
            "Je décrirai mes émotions heureuses comme étant plus proches de la satisfaction que de la joie",  # 18 - reverse
            "Quand je suis heureux(se), je tremble",  # 19 - direct
            "Quand je suis heureux(se), mes sentiments sont plus proches de la satisfaction et du calme interne que de l'excitation et de la joie de vivre"  # 20 - reverse
        ]

        questions = []
        for i, text in enumerate(question_texts):
            item_num = i + 1
            is_reverse = item_num in reverse_items
            
            # Create score map (direct or reverse)
            if is_reverse:
                score_map = {
                    "1 - Jamais": 6,
                    "2 - Presque jamais": 5,
                    "3 - Occasionnellement": 4,
                    "4 - Habituellement": 3,
                    "5 - Presque toujours": 2,
                    "6 - Toujours": 1
                }
            else:
                score_map = options.copy()
            
            questions.append({
                "id": f"AIM{item_num}",
                "text": f"{item_num}. {text}",
                "options": options,
                "score_map": score_map,
                "reverse_scored": is_reverse
            })
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        Calculate the average score for the AIM questionnaire.

        Args:
            responses (Dict[str, str]): A dictionary of responses, where the key is the question ID
                                       (e.g., "AIM1") and the value is the response option text
                                       (e.g., "1 - Jamais", "6 - Toujours").

        Returns:
            Dict[str, Any]: A dictionary containing the average score and interpretation.
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
            if response_text not in question["score_map"]:
                raise ValueError(
                    f"Invalid response '{response_text}' for question {q_id}. "
                    f"Valid options are: {list(question['score_map'].keys())}"
                )
            
            item_score = question["score_map"][response_text]
            item_scores[q_id] = item_score
            total_score += item_score

        # Calculate average score
        average_score = round(total_score / self.num_items, 2)

        # Determine interpretation
        if average_score >= 5.0:
            interpretation = "Intensité émotionnelle très élevée"
            level = "very_high"
        elif average_score >= 4.0:
            interpretation = "Intensité émotionnelle élevée"
            level = "high"
        elif average_score >= 3.0:
            interpretation = "Intensité émotionnelle modérée"
            level = "moderate"
        elif average_score >= 2.0:
            interpretation = "Intensité émotionnelle faible"
            level = "low"
        else:
            interpretation = "Intensité émotionnelle très faible"
            level = "very_low"

        return {
            "average_score": average_score,
            "total_score": total_score,
            "min_score": 1.0,
            "max_score": 6.0,
            "interpretation": interpretation,
            "intensity_level": level,
            "item_scores": item_scores
        }

    def get_random_responses(self) -> Dict[str, str]:
        """Generates random valid responses for testing purposes."""
        responses = {}
        for question in self.questions:
            q_id = question["id"]
            # Select a random response option
            responses[q_id] = random.choice(list(question["options"].keys()))
        return responses

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "Pour remplir ce questionnaire, basez-vous sur votre mode de fonctionnement habituel, "
            "c'est à dire en dehors des périodes où votre humeur est anormalement dépressive ou "
            "euphorique/exaltée.\n\n"
            "Les questions suivantes portent sur les réactions émotionnelles aux événements de vie "
            "habituels. Merci d'indiquer comment vous réagissez à ces événements en inscrivant un "
            "nombre entre 1 et 6 dans l'espace vide précédant chaque item. Merci de baser votre "
            "réponse sur la manière dont vous réagissez et NON PAS sur la manière dont les autres "
            "réagissent ou sur comment vous pensez qu'une personne devrait réagir.\n\n"
            "Échelle:\n"
            "1 - Jamais\n"
            "2 - Presque jamais\n"
            "3 - Occasionnellement\n"
            "4 - Habituellement\n"
            "5 - Presque toujours\n"
            "6 - Toujours"
        )


if __name__ == '__main__':
    aim_q = AIMQuestionnaire()
    print(f"Questionnaire: {aim_q.name}")
    print(f"Description: {aim_q.description}")
    print(f"Number of items: {aim_q.num_items}")
    print(f"Used in applications: {aim_q.used_in_applications}")
    print()
    print("="*80)
    print("INSTRUCTION:")
    print(aim_q.get_instruction())
    print("="*80)
    print()
    
    print("First 5 questions:")
    for i, q in enumerate(aim_q.questions[:5]):
        reverse_note = " (REVERSE SCORED)" if q['reverse_scored'] else ""
        print(f"  {q['id']}: {q['text']}{reverse_note}")
    print()
    
    # Test with high intensity profile
    print("Example 1: High emotional intensity profile")
    high_intensity = {}
    for i, question in enumerate(aim_q.questions):
        # High intensity: "6 - Toujours" for direct items, "1 - Jamais" for reverse items
        if question['reverse_scored']:
            high_intensity[question['id']] = "1 - Jamais"
        else:
            high_intensity[question['id']] = "6 - Toujours"
    
    result = aim_q.calculate_score(high_intensity)
    print(f"Average Score: {result['average_score']}/6.0")
    print(f"Interpretation: {result['interpretation']}")
    print()
    
    # Test with low intensity profile
    print("Example 2: Low emotional intensity profile")
    low_intensity = {}
    for i, question in enumerate(aim_q.questions):
        # Low intensity: "1 - Jamais" for direct items, "6 - Toujours" for reverse items
        if question['reverse_scored']:
            low_intensity[question['id']] = "6 - Toujours"
        else:
            low_intensity[question['id']] = "1 - Jamais"
    
    result = aim_q.calculate_score(low_intensity)
    print(f"Average Score: {result['average_score']}/6.0")
    print(f"Interpretation: {result['interpretation']}")
    print()
    
    # Test with random responses
    print("Example 3: Random responses")
    random_responses = aim_q.get_random_responses()
    result = aim_q.calculate_score(random_responses)
    print(f"Average Score: {result['average_score']}/6.0")
    print(f"Interpretation: {result['interpretation']}")
    print()
    
    print("="*80)
    print("✓ AIM Questionnaire implementation complete")
    print("  - 20 items with 6-point intensity scale")
    print("  - Validated reverse scoring")
    print("  - Clinical interpretation based on average score")

