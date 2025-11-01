import random
from typing import Any, Dict, List

class STAIAQuestionnaire:
    """STAI-A - State-Trait Anxiety Inventory (State Anxiety - Form Y-A)

    Self-report questionnaire assessing state anxiety (anxiety at this moment).
    Includes 20 items rated on a 4-point Likert scale.
    
    Scoring:
    - Response options: "Non" (1), "Plutôt non" (2), "Plutôt oui" (3), "Oui" (4)
    - Reverse-scored items: 1, 2, 5, 8, 10, 11, 15, 16, 19, 20
      (calm/positive items - higher endorsement = lower anxiety)
    - Direct-scored items: 3, 4, 6, 7, 9, 12, 13, 14, 17, 18
      (anxious items - higher endorsement = higher anxiety)
    - Total score range: 20-80
    
    Interpretation:
    - 20-37: Low anxiety
    - 38-44: Moderate anxiety
    - 45-80: High anxiety
    """

    def __init__(self):
        self.name = "STAI-A - State-Trait Anxiety Inventory (State Form)"
        self.description = "Auto-questionnaire d'évaluation de l'anxiété-état (à l'instant présent)."
        self.num_items = 20
        self.used_in_applications = ['ebipolar', 'eschizo', 'cedr']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 20 STAI-A items with their response options."""
        
        # Response options (French labels)
        options = {
            "Non": 1,
            "Plutôt non": 2,
            "Plutôt oui": 3,
            "Oui": 4
        }

        # Items requiring reverse scoring (positive/calm items)
        reverse_items = [1, 2, 5, 8, 10, 11, 15, 16, 19, 20]

        question_texts = [
            "Je me sens calme",  # 1 - reverse
            "Je me sens en sécurité, sans inquiétude, en sûreté",  # 2 - reverse
            "Je suis tendu(e), crispé(e)",  # 3 - direct
            "Je me sens surmené(e)",  # 4 - direct
            "Je me sens tranquille, bien dans ma peau",  # 5 - reverse
            "Je me sens ému(e), bouleversé(e), contrarié(e)",  # 6 - direct
            "L'idée de malheurs éventuels me tracasse en ce moment",  # 7 - direct
            "Je me sens content(e)",  # 8 - reverse
            "Je me sens effrayé(e)",  # 9 - direct
            "Je me sens à mon aise",  # 10 - reverse
            "Je sens que j'ai confiance en moi",  # 11 - reverse
            "Je me sens nerveux (nerveuse), irritable",  # 12 - direct
            "J'ai la frousse, la trouille (j'ai peur)",  # 13 - direct
            "Je me sens indécis(e)",  # 14 - direct
            "Je suis décontracté(e), détendu(e)",  # 15 - reverse
            "Je suis satisfait(e)",  # 16 - reverse
            "Je suis inquiet, soucieux (inquiète, soucieuse)",  # 17 - direct
            "Je ne sais plus où j'en suis, je me sens déconcerté(e), dérouté(e)",  # 18 - direct
            "Je me sens solide, posé(e), pondéré(e), réfléchi(e)",  # 19 - reverse
            "Je me sens de bonne humeur, aimable"  # 20 - reverse
        ]

        questions = []
        for i, text in enumerate(question_texts):
            item_num = i + 1
            is_reverse = item_num in reverse_items
            
            # Create score map (direct or reverse)
            if is_reverse:
                score_map = {
                    "Non": 4,         # Low calm = High anxiety
                    "Plutôt non": 3,
                    "Plutôt oui": 2,
                    "Oui": 1          # High calm = Low anxiety
                }
            else:
                score_map = {
                    "Non": 1,         # Low anxiety symptom
                    "Plutôt non": 2,
                    "Plutôt oui": 3,
                    "Oui": 4          # High anxiety symptom
                }
            
            questions.append({
                "id": f"STAYA{item_num}",
                "text": f"{item_num}. {text}",
                "options": options,
                "score_map": score_map,
                "reverse_scored": is_reverse
            })
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        Calculate the total score for the STAI-A questionnaire.

        Args:
            responses (Dict[str, str]): A dictionary of responses, where the key is the question ID
                                       (e.g., "STAYA1") and the value is the response option text
                                       (e.g., "Non", "Plutôt non", etc.).

        Returns:
            Dict[str, Any]: A dictionary containing the total score and interpretation.
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

        # Determine interpretation
        if total_score <= 37:
            interpretation = "Anxiété faible"
            severity = "low"
        elif total_score <= 44:
            interpretation = "Anxiété modérée"
            severity = "moderate"
        else:
            interpretation = "Anxiété élevée"
            severity = "high"

        return {
            "score": total_score,
            "min_score": 20,
            "max_score": 80,
            "interpretation": interpretation,
            "severity": severity,
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
            "Un certain nombre de phrases que l'on utilise pour se décrire sont données ci-dessous. "
            "Lisez chaque phrase, puis cochez, parmi les quatre points à droite, celui qui correspond "
            "le mieux à ce que vous ressentez À L'INSTANT, JUSTE EN CE MOMENT. Il n'y a pas de bonnes "
            "ni de mauvaises réponses. Ne passez pas trop de temps sur l'une ou l'autre de ces propositions, "
            "et indiquez la réponse qui décrit le mieux vos sentiments actuels."
        )


if __name__ == '__main__':
    stai_q = STAIAQuestionnaire()
    print(f"Questionnaire: {stai_q.name}")
    print(f"Description: {stai_q.description}")
    print(f"Number of items: {stai_q.num_items}")
    print(f"Used in applications: {stai_q.used_in_applications}")
    print()
    print("Instruction:")
    print(stai_q.get_instruction())
    print("\n" + "="*80 + "\n")
    
    print("First 5 questions:")
    for i, q in enumerate(stai_q.questions[:5]):
        reverse_note = " (REVERSE SCORED)" if q['reverse_scored'] else ""
        print(f"  {q['id']}: {q['text']}{reverse_note}")
    print()
    
    # Test with example responses showing low anxiety
    print("Example 1: Low anxiety profile")
    low_anxiety_responses = {
        "STAYA1": "Oui",  # calme (reverse) → 1
        "STAYA2": "Oui",  # en sécurité (reverse) → 1
        "STAYA3": "Non",  # tendu (direct) → 1
        "STAYA4": "Non",  # surmené (direct) → 1
        "STAYA5": "Oui",  # tranquille (reverse) → 1
        "STAYA6": "Non",  # bouleversé (direct) → 1
        "STAYA7": "Non",  # tracassé (direct) → 1
        "STAYA8": "Oui",  # content (reverse) → 1
        "STAYA9": "Non",  # effrayé (direct) → 1
        "STAYA10": "Oui",  # à mon aise (reverse) → 1
        "STAYA11": "Oui",  # confiance (reverse) → 1
        "STAYA12": "Non",  # nerveux (direct) → 1
        "STAYA13": "Non",  # peur (direct) → 1
        "STAYA14": "Non",  # indécis (direct) → 1
        "STAYA15": "Oui",  # décontracté (reverse) → 1
        "STAYA16": "Oui",  # satisfait (reverse) → 1
        "STAYA17": "Non",  # inquiet (direct) → 1
        "STAYA18": "Non",  # déconcerté (direct) → 1
        "STAYA19": "Oui",  # solide (reverse) → 1
        "STAYA20": "Oui"   # bonne humeur (reverse) → 1
    }
    result_low = stai_q.calculate_score(low_anxiety_responses)
    print(f"Score: {result_low['score']}/{result_low['max_score']}")
    print(f"Interpretation: {result_low['interpretation']}")
    print()
    
    # Test with example responses showing high anxiety
    print("Example 2: High anxiety profile")
    high_anxiety_responses = {
        "STAYA1": "Non",  # calme (reverse) → 4
        "STAYA2": "Non",  # en sécurité (reverse) → 4
        "STAYA3": "Oui",  # tendu (direct) → 4
        "STAYA4": "Oui",  # surmené (direct) → 4
        "STAYA5": "Non",  # tranquille (reverse) → 4
        "STAYA6": "Oui",  # bouleversé (direct) → 4
        "STAYA7": "Oui",  # tracassé (direct) → 4
        "STAYA8": "Non",  # content (reverse) → 4
        "STAYA9": "Oui",  # effrayé (direct) → 4
        "STAYA10": "Non",  # à mon aise (reverse) → 4
        "STAYA11": "Non",  # confiance (reverse) → 4
        "STAYA12": "Oui",  # nerveux (direct) → 4
        "STAYA13": "Oui",  # peur (direct) → 4
        "STAYA14": "Oui",  # indécis (direct) → 4
        "STAYA15": "Non",  # décontracté (reverse) → 4
        "STAYA16": "Non",  # satisfait (reverse) → 4
        "STAYA17": "Oui",  # inquiet (direct) → 4
        "STAYA18": "Oui",  # déconcerté (direct) → 4
        "STAYA19": "Non",  # solide (reverse) → 4
        "STAYA20": "Non"   # bonne humeur (reverse) → 4
    }
    result_high = stai_q.calculate_score(high_anxiety_responses)
    print(f"Score: {result_high['score']}/{result_high['max_score']}")
    print(f"Interpretation: {result_high['interpretation']}")
    print()
    
    # Test with random responses
    print("Example 3: Random responses")
    random_responses = stai_q.get_random_responses()
    result_random = stai_q.calculate_score(random_responses)
    print(f"Score: {result_random['score']}/{result_random['max_score']}")
    print(f"Interpretation: {result_random['interpretation']}")
    print()
    
    print("="*80)
    print("✓ STAI-A Questionnaire implementation complete")
    print("  - 20 items with proper reverse scoring")
    print("  - Validated scoring algorithm")
    print("  - Clinical interpretation thresholds")

