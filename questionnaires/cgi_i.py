import random
from typing import Any, Dict, List

class CGIIQuestionnaire:
    """Clinical Global Impression - Improvement (CGI-I)
    
    Single-item clinician-rated scale assessing global improvement.
    
    Structure:
    - 1 item assessing overall improvement compared to baseline
    
    Scoring:
    - 7-point scale:
      1 = Very much improved
      2 = Much improved
      3 = Minimally improved
      4 = No change
      5 = Minimally worse
      6 = Much worse
      7 = Very much worse
    
    Interpretation:
    - Lower scores indicate improvement
    - Score of 1-2: positive response to treatment
    - Score of 4: no change
    - Score of 5-7: deterioration
    
    Clinical Use:
    - Treatment response assessment
    - Outcome measurement in clinical trials
    - Longitudinal follow-up
    """

    def __init__(self):
        self.name = "Clinical Global Impression - Improvement (CGI-I)"
        self.description = "Évaluation globale de l'amélioration par le clinicien."
        self.num_items = 1
        self.used_in_applications = ['cedr']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize CGI-I item."""
        
        questions = [
            {
                "id": "CGII1",
                "number": 1,
                "text": "Comparé à son état au début du traitement, de quelle façon le patient a-t-il changé ?",
                "instruction": "Evaluez l'amélioration globale qu'elle soit ou non, selon votre opinion, due entièrement au traitement médicamenteux.",
                "options": {
                    "Très fortement amélioré.": 1,
                    "Fortement amélioré.": 2,
                    "Légèrement amélioré.": 3,
                    "Pas de changement.": 4,
                    "Légèrement aggravé.": 5,
                    "Fortement aggravé.": 6,
                    "Très fortement aggravé.": 7
                }
            }
        ]
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        Calculate CGI-I score.

        Args:
            responses (Dict[str, str]): A dictionary with 'CGII1' as key and response text as value.

        Returns:
            Dict[str, Any]: A dictionary containing score and interpretation.
        """
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} response, but got {len(responses)}")

        question = self.questions[0]
        q_id = question["id"]
        
        if q_id not in responses:
            raise ValueError(f"Missing response for question {q_id}")
        
        response_text = responses[q_id]
        if response_text not in question["options"]:
            raise ValueError(
                f"Invalid response. Expected one of: {list(question['options'].keys())}"
            )
        
        score = question["options"][response_text]
        interpretation = self._interpret_score(score)
        response_category = self._get_category(score)

        return {
            "score": score,
            "interpretation": interpretation,
            "response_category": response_category,
            "treatment_response": score <= 2
        }

    def _interpret_score(self, score: int) -> str:
        """Interpret CGI-I score."""
        if score == 1:
            return "Très fortement amélioré"
        elif score == 2:
            return "Fortement amélioré - Réponse positive au traitement"
        elif score == 3:
            return "Légèrement amélioré"
        elif score == 4:
            return "Pas de changement"
        elif score == 5:
            return "Légèrement aggravé"
        elif score == 6:
            return "Fortement aggravé"
        else:  # score == 7
            return "Très fortement aggravé"

    def _get_category(self, score: int) -> str:
        """Get response category."""
        if score <= 2:
            return "improved"
        elif score <= 3:
            return "minimally_improved"
        elif score == 4:
            return "no_change"
        elif score <= 5:
            return "minimally_worse"
        else:
            return "worse"

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "Evaluez l'amélioration globale qu'elle soit ou non, selon votre opinion, "
            "due entièrement au traitement médicamenteux.\n\n"
            "Comparé à son état au début du traitement, de quelle façon le patient a-t-il changé ?"
        )


if __name__ == '__main__':
    cgi_i = CGIIQuestionnaire()
    print(f"Questionnaire: {cgi_i.name}")
    print(f"Number of items: {cgi_i.num_items}")
    print()
    
    # Test: Much improved
    test_responses = {"CGII1": "Fortement amélioré."}
    
    result = cgi_i.calculate_score(test_responses)
    print(f"Score: {result['score']}")
    print(f"Category: {result['response_category']}")
    print(f"Treatment Response: {result['treatment_response']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    print("✓ CGI-I implementation complete - 1 item, 7-point scale")

