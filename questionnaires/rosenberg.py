import random
from typing import Any, Dict, List

class RosenbergQuestionnaire:
    """Rosenberg Self-Esteem Scale
    
    Self-report questionnaire assessing global self-esteem.
    
    Structure:
    - 10 items assessing self-worth and self-acceptance
    - Items 3, 5, 8, 9, 10 are reverse-scored
    
    Scoring:
    - 4-point Likert scale
    - Total score: 10-40
    - Higher scores indicate higher self-esteem
    
    Clinical Use:
    - Widely used measure of self-esteem
    - Treatment outcome assessment
    - Research on self-concept
    """

    def __init__(self):
        self.name = "Rosenberg Self-Esteem Scale"
        self.description = "Échelle d'estime de soi de Rosenberg."
        self.num_items = 10
        self.used_in_applications = ['cedr']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 10 Rosenberg items."""
        
        # Items with reverse scoring (3, 5, 8, 9, 10)
        reverse_items = [3, 5, 8, 9, 10]
        
        items_text = [
            "Je pense que j'ai autant de valeur que les autres",
            "Je pense avoir beaucoup de qualités",
            "Tout compte fait, j'ai tendance à me considérer comme un(e) raté(e)",
            "Je suis aussi capable que la plupart des gens",
            "Je pense que je n'ai pas grand chose dont je pourrais être fier(e)",
            "Je me vois de manière positive",
            "Dans l'ensemble, je suis satisfait(e) de moi",
            "J'aimerais pouvoir avoir plus de respect pour moi-même",
            "Parfois je me sens vraiment inutile",
            "Il m'arrive de penser que je suis un(e) bon(ne) à rien"
        ]
        
        questions = []
        for i, text in enumerate(items_text, 1):
            # Reverse-scored items have inverted response values
            if i in reverse_items:
                options = {
                    "Tout à fait en accord": 1,
                    "Plutôt en accord": 2,
                    "Plutôt en désaccord": 3,
                    "Tout à fait en désaccord": 4
                }
            else:
                options = {
                    "Tout à fait en accord": 4,
                    "Plutôt en accord": 3,
                    "Plutôt en désaccord": 2,
                    "Tout à fait en désaccord": 1
                }
            
            questions.append({
                "id": f"E_ROSEN{i}",
                "number": i,
                "text": f"{i}. {text}",
                "options": options,
                "reverse_scored": i in reverse_items
            })
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        Calculate Rosenberg total score.

        Args:
            responses (Dict[str, str]): A dictionary of responses, where the key is the question ID
                                       (e.g., "E_ROSEN1") and the value is the response option text.

        Returns:
            Dict[str, Any]: A dictionary containing total score and interpretation.
        """
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")

        total_score = 0
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
            total_score += score

        # Interpret score
        interpretation = self._interpret_score(total_score)

        return {
            "total_score": total_score,
            "min_score": 10,
            "max_score": 40,
            "interpretation": interpretation,
            "level": self._get_level(total_score),
            "item_scores": item_scores
        }

    def _interpret_score(self, score: int) -> str:
        """Interpret Rosenberg total score."""
        if score >= 31:
            return "Estime de soi élevée - Perception positive de soi"
        elif score >= 26:
            return "Estime de soi normale - Auto-évaluation équilibrée"
        elif score >= 15:
            return "Estime de soi faible - Perception négative de soi"
        else:
            return "Estime de soi très faible - Dévalorisation importante"

    def _get_level(self, score: int) -> str:
        """Get self-esteem level."""
        if score >= 31:
            return "high"
        elif score >= 26:
            return "normal"
        elif score >= 15:
            return "low"
        else:
            return "very_low"

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
            "Les phrases qui suivent décrivent les sentiments que l'on peut ressentir "
            "vis-à-vis de soi. Il n'y a pas de bonne ou mauvaise réponse, seulement des opinions.\n\n"
            "Cochez la case appropriée selon que vous êtes:\n"
            "- Tout à fait en accord\n"
            "- Plutôt en accord\n"
            "- Plutôt en désaccord\n"
            "- Tout à fait en désaccord"
        )


if __name__ == '__main__':
    rosenberg = RosenbergQuestionnaire()
    print(f"Questionnaire: {rosenberg.name}")
    print(f"Number of items: {rosenberg.num_items}")
    print()
    
    # Test: High self-esteem
    print("Example: High Self-Esteem")
    high_esteem = {}
    for q in rosenberg.questions:
        if q['reverse_scored']:
            high_esteem[q['id']] = "Tout à fait en désaccord"
        else:
            high_esteem[q['id']] = "Tout à fait en accord"
    
    result = rosenberg.calculate_score(high_esteem)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Level: {result['level']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    print("✓ Rosenberg implementation complete - 10 items, 10-40 scoring range")

