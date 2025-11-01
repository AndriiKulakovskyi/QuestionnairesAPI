import random
from typing import Any, Dict, List

class BASQuestionnaire:
    """BAS - Behavioral Activation System / Bech Anxiety Scale
    
    Clinician-rated scale assessing anxiety symptoms.
    
    Structure:
    - 10 items assessing anxiety dimensions:
      * Inner tension
      * Hostile feelings
      * Hypochondria
      * Phobias
      * Worrying over trifles
      * Sleep reduction
      * Neurovegetative symptoms (subjective)
      * Pain
      * Autonomic disturbances (observed)
      * Muscular tension
    
    Scoring:
    - Each item scored 0-6
    - 0, 2, 4, 6 = clearly defined points
    - 1, 3, 5 = intermediate points
    - Total score: 0-60
    - Higher scores indicate greater anxiety
    
    Clinical Use:
    - Assessment of anxiety in depression
    - Treatment monitoring
    - Research on anxiety disorders
    """

    def __init__(self):
        self.name = "BAS - Bech Anxiety Scale"
        self.description = "Échelle d'anxiété de Bech (évaluation clinicienne)."
        self.num_items = 10
        self.used_in_applications = ['cedr']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 10 BAS items."""
        
        # Standard 0-6 scoring options
        options = {str(i): i for i in range(7)}
        
        items_text = [
            "Tension intérieure - Sentiments de malaise, irritabilité, tension nerveuse, panique",
            "Sentiments hostiles - Colère, hostilité, sentiments agressifs",
            "Hypocondrie - Préoccupation exagérée concernant la santé",
            "Phobies - Peur injustifiée dans des situations spécifiques",
            "Inquiétude pour des \"riens\" - Soucis excessifs difficiles à dissiper",
            "Réduction du sommeil - Durée ou profondeur du sommeil réduite",
            "Troubles neuro-végétatifs (subjectifs) - Palpitations, vertiges, sueurs",
            "Douleurs - Céphalées, douleurs musculaires ou articulaires",
            "Troubles neuro-végétatifs (observés) - Signes autonomes visibles",
            "Tension musculaire - Tension observable dans mimique et posture"
        ]
        
        questions = []
        for i, text in enumerate(items_text, 1):
            questions.append({
                "id": f"BAS{i}",
                "number": i,
                "text": f"{i}. {text}",
                "options": options
            })
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        Calculate BAS total score.

        Args:
            responses (Dict[str, str]): A dictionary of responses, where the key is the question ID
                                       (e.g., "BAS1") and the value is the score (0-6 as string).

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
                    f"Valid options are: 0-6"
                )
            
            score = question["options"][response_text]
            item_scores[q_id] = score
            total_score += score

        # Interpret score
        interpretation = self._interpret_score(total_score)

        return {
            "total_score": total_score,
            "max_score": 60,
            "interpretation": interpretation,
            "severity": self._get_severity(total_score),
            "item_scores": item_scores
        }

    def _interpret_score(self, score: int) -> str:
        """Interpret BAS total score."""
        if score >= 40:
            return "Anxiété très sévère - Symptômes anxieux invalidants"
        elif score >= 30:
            return "Anxiété sévère - Symptômes anxieux importants"
        elif score >= 20:
            return "Anxiété modérée - Symptômes anxieux significatifs"
        elif score >= 10:
            return "Anxiété légère - Symptômes anxieux mineurs"
        else:
            return "Anxiété minimale ou absente"

    def _get_severity(self, score: int) -> str:
        """Get severity level."""
        if score >= 40:
            return "very_severe"
        elif score >= 30:
            return "severe"
        elif score >= 20:
            return "moderate"
        elif score >= 10:
            return "mild"
        else:
            return "minimal"

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
            "Échelle d'évaluation clinique de l'anxiété.\n\n"
            "La cotation doit se fonder sur l'entretien clinique allant de questions générales "
            "sur les symptômes à des questions plus précises qui permettent une cotation exacte "
            "de la sévérité.\n\n"
            "Le cotateur doit décider si la note est à un des points nettement définis de l'échelle "
            "(0, 2, 4, 6) ou à un point intermédiaire (1, 3, 5).\n\n"
            "Échelle de réponse:\n"
            "0, 1, 2, 3, 4, 5, 6\n"
            "(0 = absent, 6 = très sévère)\n\n"
            "Période évaluée: Les 7 derniers jours"
        )


if __name__ == '__main__':
    bas = BASQuestionnaire()
    print(f"Questionnaire: {bas.name}")
    print(f"Description: {bas.description}")
    print(f"Number of items: {bas.num_items}")
    print()
    
    # Test case: Severe anxiety
    print("Example: Severe Anxiety")
    severe = {}
    for q in bas.questions:
        severe[q['id']] = "5"  # High anxiety
    
    result = bas.calculate_score(severe)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Severity: {result['severity']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    
    print("="*80)
    print("✓ BAS implementation complete")
    print("  - 10 items")
    print("  - 0-60 scoring range")
    print("  - Clinician-rated anxiety assessment")

