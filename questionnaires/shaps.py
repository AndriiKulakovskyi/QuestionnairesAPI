import random
from typing import Any, Dict, List

class SHAPSQuestionnaire:
    """SHAPS - Snaith-Hamilton Pleasure Scale
    
    Self-report questionnaire assessing anhedonia (inability to experience pleasure).
    A core symptom of depression and other mood disorders.
    
    Structure:
    - 14 items assessing different pleasure domains:
      * Entertainment (TV, reading, hobbies)
      * Social interaction (family, friends)
      * Sensory experiences (food, smells, scenery)
      * Self-care (appearance, bathing)
      * Simple pleasures (sunny day, phone call, compliments)
    
    Scoring:
    - 4-point response scale:
      * "Fortement en désaccord" (0)
      * "En désaccord" (1)
      * "D'accord" (2)
      * "Fortement d'accord" (3)
    - Scoring conversion:
      * Responses 0-1 (disagree) → 1 point (anhedonia present)
      * Responses 2-3 (agree) → 0 points (pleasure capacity preserved)
    - Total score: 0-14
    - Higher scores indicate greater anhedonia
    
    Clinical Interpretation:
    - 0-2: Normal hedonic capacity
    - 3-7: Mild to moderate anhedonia
    - 8+: Severe anhedonia (clinical concern)
    """

    def __init__(self):
        self.name = "SHAPS - Snaith-Hamilton Pleasure Scale"
        self.description = "Échelle de plaisir de Snaith-Hamilton - Évaluation de l'anhédonie."
        self.num_items = 14
        self.used_in_applications = ['cedr']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 14 SHAPS items."""
        
        # Response options (same for all items)
        options = [
            "Fortement en désaccord",
            "En désaccord", 
            "D'accord",
            "Fortement d'accord"
        ]
        
        items_text = [
            "Mon émission de télévision ou de radio me procure beaucoup de plaisir",
            "J'apprécie beaucoup d'être avec ma famille ou avec des amis intimes",
            "Je trouve du plaisir dans mes hobbies ou passe-temps",
            "Je suis capable d'apprécier mon plat favori",
            "J'aime beaucoup prendre un bain chaud ou une douche rafraîchissante",
            "Je trouve du plaisir dans le parfum des fleurs ou dans l'odeur d'une fraîche brise de mer ou du pain fraîchement cuit",
            "J'aime beaucoup voir des visages souriants autour de moi",
            "J'apprécie beaucoup de paraître élégant(e) quand j'ai fait un effort pour soigner mon apparence",
            "J'aime beaucoup lire un livre, un magazine ou un journal",
            "J'apprécie beaucoup une tasse de thé ou de café ou un verre de ma boisson favorite",
            "Je trouve du plaisir dans de petits riens tels que par exemple, une journée fortement ensoleillée ou un coup de téléphone d'un ami",
            "Je suis capable d'apprécier un très beau paysage ou une très belle vue",
            "Je prends plaisir à aider les autres",
            "Je ressens du plaisir à recevoir des éloges d'autres personnes"
        ]
        
        # Pleasure domains for each item
        domains = [
            "entertainment",
            "social",
            "hobbies",
            "food",
            "sensory_care",
            "sensory_smell",
            "social",
            "self_care",
            "reading",
            "food_beverage",
            "simple_pleasures",
            "scenery",
            "helping_others",
            "praise"
        ]
        
        questions = []
        for i, text in enumerate(items_text, 1):
            questions.append({
                "id": f"SHAPS{i}",
                "number": i,
                "text": f"{i}. {text}",
                "options": options,
                "domain": domains[i-1]
            })
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        Calculate SHAPS total score.

        Args:
            responses (Dict[str, str]): A dictionary of responses, where the key is the question ID
                                       (e.g., "SHAPS1") and the value is the response option text.

        Returns:
            Dict[str, Any]: A dictionary containing the total score and interpretation.
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
                    f"Valid options are: {question['options']}"
                )
            
            # Get response value (0-3)
            response_value = question["options"].index(response_text)
            
            # Apply SHAPS scoring logic:
            # 0-1 (disagree) = 1 point (anhedonia present)
            # 2-3 (agree) = 0 points (pleasure capacity preserved)
            if response_value <= 1:
                score = 1
            else:
                score = 0
            
            item_scores[q_id] = score
            total_score += score

        # Interpret score
        interpretation = self._interpret_score(total_score)

        return {
            "total_score": total_score,
            "max_score": self.num_items,
            "interpretation": interpretation,
            "severity": self._get_severity(total_score),
            "item_scores": item_scores
        }

    def _interpret_score(self, score: int) -> str:
        """Interpret SHAPS total score."""
        if score >= 8:
            return "Anhédonie sévère - Difficulté marquée à éprouver du plaisir"
        elif score >= 3:
            return "Anhédonie légère à modérée - Capacité hédonique diminuée"
        else:
            return "Capacité hédonique normale - Pas d'anhédonie cliniquement significative"

    def _get_severity(self, score: int) -> str:
        """Get severity level."""
        if score >= 8:
            return "severe"
        elif score >= 3:
            return "mild_to_moderate"
        else:
            return "normal"

    def get_random_responses(self) -> Dict[str, str]:
        """Generates random valid responses for testing purposes."""
        responses = {}
        for question in self.questions:
            responses[question["id"]] = random.choice(question["options"])
        return responses

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "Ce questionnaire est destiné à mesurer votre capacité à éprouver du plaisir, "
            "au cours de ces derniers jours. Il est important de lire très attentivement "
            "chaque énoncé.\n\n"
            "Cochez une des cases pour préciser votre degré d'accord ou de désaccord "
            "pour chacun des énoncés.\n\n"
            "Échelle de réponse:\n"
            "- Fortement en désaccord\n"
            "- En désaccord\n"
            "- D'accord\n"
            "- Fortement d'accord"
        )


if __name__ == '__main__':
    shaps = SHAPSQuestionnaire()
    print(f"Questionnaire: {shaps.name}")
    print(f"Description: {shaps.description}")
    print(f"Number of items: {shaps.num_items}")
    print(f"Used in applications: {shaps.used_in_applications}")
    print()
    print("="*80)
    print("INSTRUCTION:")
    print(shaps.get_instruction())
    print("="*80)
    print()
    
    print("Sample items (first 5):")
    for q in shaps.questions[:5]:
        print(f"\n{q['text']}")
        print(f"  Domain: {q['domain']}")
    print()
    print("="*80)
    
    # Test case 1: Severe anhedonia (all disagree)
    print("\nExample 1: Severe Anhedonia")
    severe = {}
    for q in shaps.questions:
        severe[q['id']] = "Fortement en désaccord"
    
    result = shaps.calculate_score(severe)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Severity: {result['severity']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    
    # Test case 2: Normal hedonic capacity (all agree)
    print("Example 2: Normal Hedonic Capacity")
    normal = {}
    for q in shaps.questions:
        normal[q['id']] = "Fortement d'accord"
    
    result = shaps.calculate_score(normal)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Severity: {result['severity']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    
    # Test case 3: Mild anhedonia (mixed responses)
    print("Example 3: Mild Anhedonia")
    mild = {}
    for i, q in enumerate(shaps.questions, 1):
        # First 4 items show anhedonia, rest are normal
        if i <= 4:
            mild[q['id']] = "En désaccord"
        else:
            mild[q['id']] = "D'accord"
    
    result = shaps.calculate_score(mild)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Severity: {result['severity']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    
    print("="*80)
    print("✓ SHAPS implementation complete")
    print("  - 14 items across multiple pleasure domains")
    print("  - Binary scoring (anhedonia present/absent per item)")
    print("  - Core symptom assessment for depression")
    print("  - Highly sensitive to treatment effects")

