import random
from typing import Any, Dict, List

class SPINQuestionnaire:
    """SPIN - Social Phobia Inventory
    
    Self-report questionnaire assessing social anxiety disorder.
    
    Structure:
    - 17 items assessing three dimensions of social phobia:
      * Fear (items 1, 3, 5, 10, 14, 15)
      * Avoidance (items 4, 6, 8, 9, 11, 12)
      * Physiological arousal (items 2, 7, 13, 16, 17)
    
    Scoring:
    - 5-point scale (0-4):
      * 0 = Pas du tout (Not at all)
      * 1 = Légèrement (A little bit)
      * 2 = Moyennement (Somewhat)
      * 3 = Beaucoup (Very much)
      * 4 = Extrêmement (Extremely)
    - Total score: 0-68
    - Higher scores indicate greater social anxiety
    
    Clinical Interpretation:
    - 0-20: Minimal/no social anxiety
    - 21-30: Mild social anxiety
    - 31-40: Moderate social anxiety
    - 41-50: Severe social anxiety
    - 51+: Very severe social anxiety
    
    Clinical Use:
    - Screening for social anxiety disorder
    - Treatment monitoring
    - Research on social phobia
    """

    def __init__(self):
        self.name = "SPIN - Social Phobia Inventory"
        self.description = "Inventaire de la phobie sociale."
        self.num_items = 17
        self.used_in_applications = ['cedr']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 17 SPIN items."""
        
        # Standard response options
        options = {
            "Pas du tout": 0,
            "Légèrement": 1,
            "Moyennement": 2,
            "Beaucoup": 3,
            "Extrêmement": 4
        }
        
        # Fear items: 1, 3, 5, 10, 14, 15
        # Avoidance items: 4, 6, 8, 9, 11, 12
        # Physiological items: 2, 7, 13, 16, 17
        
        items_text = [
            "J'ai peur des gens en position d'autorité.",
            "Je suis mal à l'aise de rougir en public",
            "Les soirées et les autres événements en groupe me font peur.",
            "J'évite de parler aux gens que je ne connais pas.",
            "Me faire critiquer m'effraie beaucoup.",
            "La peur d'être dans l'embarras me pousse à éviter de faire des choses ou de parler aux gens.",
            "Transpirer devant les gens me perturbe.",
            "J'évite d'aller dans les soirées.",
            "J'évite les activités où je suis le centre d'attention.",
            "Parler à des inconnus me fait peur.",
            "J'évite d'avoir à parler en public.",
            "Je ferais n'importe quoi pour éviter d'être critiqué.",
            "Avoir des palpitations cardiaques me dérange quand il y a des gens près de moi.",
            "Cela me gêne de faire certaines choses quand des gens pourraient être en train de regarder.",
            "Être embarrassé en public ou avoir l'air stupide fait partie de mes pires craintes.",
            "J'évite de parler à des gens en position d'autorité.",
            "Trembler ou frissonner devant les autres est une source de détresse pour moi."
        ]
        
        # Subscale assignments
        fear_items = [1, 3, 5, 10, 14, 15]
        avoidance_items = [4, 6, 8, 9, 11, 12]
        physiological_items = [2, 7, 13, 16, 17]
        
        questions = []
        for i, text in enumerate(items_text, 1):
            # Determine subscale
            if i in fear_items:
                subscale = "fear"
            elif i in avoidance_items:
                subscale = "avoidance"
            else:
                subscale = "physiological"
            
            questions.append({
                "id": f"SPIN{i}",
                "number": i,
                "text": f"{i}. {text}",
                "options": options,
                "subscale": subscale
            })
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        Calculate SPIN total and subscale scores.

        Args:
            responses (Dict[str, str]): A dictionary of responses, where the key is the question ID
                                       (e.g., "SPIN1") and the value is the response option text.

        Returns:
            Dict[str, Any]: A dictionary containing total and subscale scores with interpretations.
        """
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")

        total_score = 0
        subscale_scores = {
            'fear': 0,
            'avoidance': 0,
            'physiological': 0
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
            total_score += score
            subscale_scores[question["subscale"]] += score

        # Interpret score
        interpretation = self._interpret_total(total_score)

        return {
            "total_score": total_score,
            "max_score": self.num_items * 4,
            "interpretation": interpretation,
            "severity": self._get_severity(total_score),
            "subscales": subscale_scores,
            "subscale_max": {
                "fear": 6 * 4,
                "avoidance": 6 * 4,
                "physiological": 5 * 4
            },
            "item_scores": item_scores
        }

    def _interpret_total(self, score: int) -> str:
        """Interpret SPIN total score."""
        if score >= 51:
            return "Anxiété sociale très sévère - Handicap social majeur"
        elif score >= 41:
            return "Anxiété sociale sévère - Évitement social important"
        elif score >= 31:
            return "Anxiété sociale modérée - Impact fonctionnel significatif"
        elif score >= 21:
            return "Anxiété sociale légère - Impact fonctionnel limité"
        else:
            return "Anxiété sociale minimale ou absente"

    def _get_severity(self, score: int) -> str:
        """Get severity level."""
        if score >= 51:
            return "very_severe"
        elif score >= 41:
            return "severe"
        elif score >= 31:
            return "moderate"
        elif score >= 21:
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
            "Dans quelle mesure les problèmes décrits dans cette liste vous ont-ils "
            "dérangé(e) durant les dernières semaines.\n\n"
            "Assurez-vous de bien répondre à toutes les questions.\n\n"
            "Échelle de réponse:\n"
            "- Pas du tout\n"
            "- Légèrement\n"
            "- Moyennement\n"
            "- Beaucoup\n"
            "- Extrêmement"
        )


if __name__ == '__main__':
    spin = SPINQuestionnaire()
    print(f"Questionnaire: {spin.name}")
    print(f"Description: {spin.description}")
    print(f"Number of items: {spin.num_items}")
    print(f"Used in applications: {spin.used_in_applications}")
    print()
    print("="*80)
    print("INSTRUCTION:")
    print(spin.get_instruction())
    print("="*80)
    print()
    
    print("Sample items (first 5):")
    for q in spin.questions[:5]:
        print(f"\n{q['text']}")
        print(f"  Subscale: {q['subscale']}")
    print()
    print("="*80)
    
    # Test case 1: Very severe social anxiety
    print("\nExample 1: Very Severe Social Anxiety")
    severe = {}
    for q in spin.questions:
        severe[q['id']] = "Extrêmement"
    
    result = spin.calculate_score(severe)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Severity: {result['severity']}")
    print(f"Interpretation: {result['interpretation']}")
    print("\nSubscale Scores:")
    for subscale, score in result['subscales'].items():
        max_score = result['subscale_max'][subscale]
        print(f"  {subscale}: {score}/{max_score}")
    print()
    
    # Test case 2: No social anxiety
    print("Example 2: No Social Anxiety")
    none_anxiety = {}
    for q in spin.questions:
        none_anxiety[q['id']] = "Pas du tout"
    
    result = spin.calculate_score(none_anxiety)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Severity: {result['severity']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    
    # Test case 3: Moderate social anxiety
    print("Example 3: Moderate Social Anxiety")
    moderate = {}
    for q in spin.questions:
        moderate[q['id']] = "Moyennement"  # All "Somewhat" = 2 × 17 = 34
    
    result = spin.calculate_score(moderate)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Severity: {result['severity']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    
    print("="*80)
    print("✓ SPIN implementation complete")
    print("  - 17 items across 3 subscales")
    print("  - Fear, Avoidance, Physiological arousal")
    print("  - 0-68 scoring range")
    print("  - Clinical cutoff: 19 (Connor et al., 2000)")

