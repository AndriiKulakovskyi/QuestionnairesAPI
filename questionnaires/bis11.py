import random
from typing import Any, Dict, List

class BIS11Questionnaire:
    """BIS-11 - Barratt Impulsiveness Scale (Version 11)
    
    Self-report questionnaire assessing impulsiveness across three dimensions.
    
    Structure:
    - 34 items total
    - 30 items scored across 3 subscales:
      1. Motor Impulsiveness (11 items) - Acting without thinking
      2. Attentional Impulsiveness (8 items) - Difficulty concentrating
      3. Non-planning Impulsiveness (11 items) - Present orientation, lack of future planning
    - 4 items (19, 26, 27, 29) not included in subscale scoring
    
    Scoring:
    - 4-point scale: 1-4
    - Some items are reverse-scored
    - Total score: sum of all 30 scored items (34-120)
    - Higher scores indicate greater impulsiveness
    
    Clinical Use:
    - Widely used in ADHD, substance abuse, personality disorders
    - Normative data available for various populations
    """

    def __init__(self):
        self.name = "BIS-11 - Barratt Impulsiveness Scale"
        self.description = "Échelle d'impulsivité de Barratt (version 11)."
        self.num_items = 34
        self.num_scored_items = 30
        self.used_in_applications = ['cedr']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 34 BIS-11 items with their subscale assignments."""
        
        # Subscale assignments (30 scored items)
        motor_items = [2, 3, 4, 16, 17, 20, 22, 23, 24, 28, 34]
        attention_items = [5, 6, 9, 11, 21, 25, 30, 32]
        nonplanning_items = [1, 7, 8, 10, 12, 13, 14, 15, 18, 31, 33]
        excluded_items = [19, 26, 27, 29]  # Not included in subscale scoring
        
        items_text = [
            "Je prépare soigneusement les tâches à accomplir",
            "Je fais les choses sans y penser",
            "Je me décide rapidement",
            "J'ai tendance à ne pas m'en faire",
            "Je ne fais pas attention",
            "J'ai des idées qui fusent",
            "Je projette mes voyages longtemps à l'avance",
            "Je suis maître de moi",
            "Je me concentre facilement",
            "Je mets de l'argent de côté régulièrement",
            "\"J'ai la bougeotte\" aux spectacles ou aux conférences",
            "Je réfléchis soigneusement",
            "Je veille à ma sécurité d'emploi",
            "Je dis les choses sans y penser",
            "J'aime réfléchir à des problèmes complexes",
            "Je change de travail",
            "J'agis sur un \"coup de tête\"",
            "Réfléchir à un problème m'ennuie vite",
            "Je me fais faire régulièrement des bilans de santé",
            "J'agis selon l'inspiration du moment",
            "Je suis quelqu'un de réfléchi",
            "Je change de domicile",
            "J'achète les choses sur \"un coup de tête\"",
            "Je ne peux penser qu'à un problème à la fois",
            "Je change de passe-temps",
            "Je marche et bouge vite",
            "Je résous les problèmes par tâtonnements",
            "Je dépense ou paye à crédit plus que je ne gagne",
            "Je parle vite",
            "Quand je réfléchis, mes pensées s'égarent souvent",
            "Je m'intéresse plus au présent qu'à l'avenir",
            "Je me sens agité(e) au spectacle ou lors de conférences",
            "J'aime les \"casse-tête\"",
            "Je pense à l'avenir"
        ]
        
        # Items with reverse scoring (higher number = less impulsive)
        # These have response options: 4=Rarely, 3=Occasionally, 2=Often, 1=Almost always
        reverse_items = [1, 7, 8, 9, 10, 12, 13, 15, 21, 33, 34]
        
        questions = []
        for i, text in enumerate(items_text, 1):
            # Determine subscale
            if i in motor_items:
                subscale = "motor"
            elif i in attention_items:
                subscale = "attention"
            elif i in nonplanning_items:
                subscale = "nonplanning"
            else:
                subscale = "excluded"  # Items 19, 26, 27, 29
            
            # Response options depend on whether item is reverse-scored
            if i in reverse_items:
                options = {
                    "Rarement/Jamais": 4,
                    "Occasionnellement.": 3,
                    "Souvent.": 2,
                    "Presque toujours/Toujours.": 1
                }
            else:
                options = {
                    "Rarement/Jamais": 1,
                    "Occasionnellement.": 2,
                    "Souvent.": 3,
                    "Presque toujours/Toujours.": 4
                }
            
            questions.append({
                "id": f"BARATT{i}",
                "number": i,
                "text": f"{i}. {text}",
                "options": options,
                "subscale": subscale,
                "reverse_scored": i in reverse_items
            })
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        Calculate BIS-11 total and subscale scores.

        Args:
            responses (Dict[str, str]): A dictionary of responses, where the key is the question ID
                                       (e.g., "BARATT1") and the value is the response option text.

        Returns:
            Dict[str, Any]: A dictionary containing total and subscale scores with interpretations.
        """
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")

        # Initialize subscale scores
        subscale_scores = {
            'motor': 0,
            'attention': 0,
            'nonplanning': 0
        }
        
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
            
            # Only add to total and subscales if not excluded
            if question["subscale"] != "excluded":
                total_score += score
                subscale_scores[question["subscale"]] += score

        # Interpret scores
        interpretation = self._interpret_total(total_score)

        return {
            "total_score": total_score,
            "min_score": self.num_scored_items,
            "max_score": self.num_scored_items * 4,
            "interpretation": interpretation,
            "severity": self._get_severity(total_score),
            "subscales": {
                "motor": subscale_scores['motor'],
                "attention": subscale_scores['attention'],
                "nonplanning": subscale_scores['nonplanning']
            },
            "subscale_interpretations": {
                "motor": self._interpret_subscale(subscale_scores['motor'], 11),
                "attention": self._interpret_subscale(subscale_scores['attention'], 8),
                "nonplanning": self._interpret_subscale(subscale_scores['nonplanning'], 11)
            },
            "item_scores": item_scores
        }

    def _interpret_total(self, score: int) -> str:
        """Interpret total BIS-11 score."""
        if score >= 72:
            return "Impulsivité élevée - Difficulté marquée de contrôle impulsif"
        elif score >= 52:
            return "Impulsivité normale à modérée"
        else:
            return "Impulsivité faible - Bon contrôle impulsif"

    def _get_severity(self, score: int) -> str:
        """Get severity level."""
        if score >= 72:
            return "high"
        elif score >= 52:
            return "normal_to_moderate"
        else:
            return "low"

    def _interpret_subscale(self, score: int, num_items: int) -> str:
        """Interpret subscale score."""
        mean_score = score / num_items
        if mean_score >= 3.0:
            return "Élevé"
        elif mean_score >= 2.0:
            return "Modéré"
        else:
            return "Faible"

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
            "Les gens agissent et réfléchissent différemment devant des situations variées. "
            "Ce questionnaire a pour but d'évaluer certaines de vos façons d'agir et de réfléchir.\n\n"
            "Lisez chaque énoncé et remplissez la case appropriée située sur la droite de la page. "
            "Ne passez pas trop de temps sur chaque énoncé. Répondez vite et honnêtement.\n\n"
            "Échelle de réponse:\n"
            "- Rarement/Jamais\n"
            "- Occasionnellement\n"
            "- Souvent\n"
            "- Presque toujours/Toujours"
        )


if __name__ == '__main__':
    bis = BIS11Questionnaire()
    print(f"Questionnaire: {bis.name}")
    print(f"Description: {bis.description}")
    print(f"Number of items: {bis.num_items} ({bis.num_scored_items} scored)")
    print(f"Used in applications: {bis.used_in_applications}")
    print()
    print("="*80)
    print("Sample items (first 5):")
    for q in bis.questions[:5]:
        reverse_note = " [REVERSE]" if q['reverse_scored'] else ""
        print(f"\n{q['text']}{reverse_note}")
        print(f"  Subscale: {q['subscale']}")
    print()
    print("="*80)
    
    # Test case 1: High impulsiveness
    print("\nExample 1: High Impulsiveness")
    high_imp = {}
    for q in bis.questions:
        # Choose impulsive responses
        if q['reverse_scored']:
            high_imp[q['id']] = "Rarement/Jamais"
        else:
            high_imp[q['id']] = "Presque toujours/Toujours."
    
    result = bis.calculate_score(high_imp)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Severity: {result['severity']}")
    print(f"Interpretation: {result['interpretation']}")
    print("\nSubscale Scores:")
    for subscale, score in result['subscales'].items():
        print(f"  {subscale}: {score} - {result['subscale_interpretations'][subscale]}")
    print()
    
    # Test case 2: Low impulsiveness
    print("Example 2: Low Impulsiveness")
    low_imp = {}
    for q in bis.questions:
        # Choose controlled responses
        if q['reverse_scored']:
            low_imp[q['id']] = "Presque toujours/Toujours."
        else:
            low_imp[q['id']] = "Rarement/Jamais"
    
    result = bis.calculate_score(low_imp)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Severity: {result['severity']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    
    print("="*80)
    print("✓ BIS-11 implementation complete")
    print("  - 34 items (30 scored)")
    print("  - 3 subscales: Motor, Attention, Non-planning")
    print("  - Reverse scoring on 11 items")
    print("  - Gold standard impulsivity assessment")

