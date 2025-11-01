from typing import Dict, List, Any

class HamiltonAnxietyQuestionnaire:
    """
    HAM-A (Hamilton Anxiety Rating Scale)
    
    Description:
    14-item clinician-rated scale assessing severity of anxiety symptoms.
    Each item is rated 0-4 based on severity.
    
    Subscales:
    - Psychic Anxiety (items 1-6, 14): Mental anxiety symptoms
    - Somatic Anxiety (items 7-13): Physical anxiety symptoms
    
    Scoring: 0-4 per item
    Total range: 0-56
    
    Interpretation:
    - < 17: Mild anxiety
    - 18-24: Mild to moderate anxiety  
    - 25-30: Moderate to severe anxiety
    - > 30: Severe anxiety
    """
    
    def __init__(self):
        self.name = "HAM-A"
        self.description = "Hamilton Anxiety Rating Scale - 14-item clinician-rated assessment"
        self.num_items = 14
        self.questions = []
        self._init_questions()
    
    def _init_questions(self):
        """Initialize the 14 HAM-A items."""
        items = [
            ("Humeur anxieuse", "psychic"),
            ("Tension nerveuse", "psychic"),
            ("Craintes", "psychic"),
            ("Insomnie", "psychic"),
            ("Troubles de la concentration et de la mémoire", "psychic"),
            ("Humeur dépressive", "psychic"),
            ("Symptômes somatiques généraux: musculaires", "somatic"),
            ("Symptômes somatiques généraux: sensoriels", "somatic"),
            ("Symptômes cardio-vasculaires", "somatic"),
            ("Symptômes respiratoires", "somatic"),
            ("Symptômes gastro-intestinaux", "somatic"),
            ("Symptômes génito-urinaires", "somatic"),
            ("Symptômes du système nerveux autonome", "somatic"),
            ("Comportement pendant l'entretien", "psychic")
        ]
        
        response_options = {
            0: "Absent",
            1: "Léger",
            2: "Moyen",
            3: "Fort",
            4: "Invalidant/Maximal"
        }
        
        for i, (text, subscale) in enumerate(items):
            self.questions.append({
                'id': f'HAMANX{i+1}',
                'text': text,
                'responses': response_options,
                'subscale': subscale
            })
    
    def calculate_score(self, responses: List[int]) -> Dict[str, Any]:
        """Calculate HAM-A scores."""
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, got {len(responses)}")
        
        if any(r < 0 or r > 4 for r in responses):
            raise ValueError("All responses must be between 0 and 4")
        
        # Subscale scores
        psychic_items = [0, 1, 2, 3, 4, 5, 13]
        somatic_items = [6, 7, 8, 9, 10, 11, 12]
        
        psychic_score = sum(responses[i] for i in psychic_items)
        somatic_score = sum(responses[i] for i in somatic_items)
        total_score = sum(responses)
        
        return {
            'total_score': total_score,
            'psychic_anxiety': psychic_score,
            'somatic_anxiety': somatic_score,
            'interpretation': self._interpret(total_score),
            'max_score': 56
        }
    
    def _interpret(self, score: int) -> str:
        """Interpret HAM-A total score."""
        if score < 17:
            return "Mild anxiety"
        elif score < 25:
            return "Mild to moderate anxiety"
        elif score < 31:
            return "Moderate to severe anxiety"
        else:
            return "Severe anxiety"

if __name__ == '__main__':
    ham_a = HamiltonAnxietyQuestionnaire()
    print(f"Questionnaire: {ham_a.name} - {ham_a.num_items} items\n")
    
    # Example 1: Mild anxiety
    print("Example 1: Mild Anxiety")
    responses1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    result1 = ham_a.calculate_score(responses1)
    print(f"Total: {result1['total_score']}/56 - {result1['interpretation']}")
    print(f"Psychic: {result1['psychic_anxiety']}, Somatic: {result1['somatic_anxiety']}\n")
    
    # Example 2: Moderate anxiety
    print("Example 2: Moderate Anxiety")
    responses2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    result2 = ham_a.calculate_score(responses2)
    print(f"Total: {result2['total_score']}/56 - {result2['interpretation']}")
    print(f"Psychic: {result2['psychic_anxiety']}, Somatic: {result2['somatic_anxiety']}\n")
    
    # Example 3: Severe anxiety
    print("Example 3: Severe Anxiety")
    responses3 = [4, 4, 3, 3, 3, 3, 4, 4, 3, 3, 2, 2, 2, 3]
    result3 = ham_a.calculate_score(responses3)
    print(f"Total: {result3['total_score']}/56 - {result3['interpretation']}")
    print(f"Psychic: {result3['psychic_anxiety']}, Somatic: {result3['somatic_anxiety']}")
