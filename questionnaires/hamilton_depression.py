from typing import Dict, List, Any

class HamiltonDepressionQuestionnaire:
    """
    HAM-D-21 (Hamilton Depression Rating Scale - 21 items)
    
    Description:
    21-item clinician-rated scale assessing severity of depressive symptoms.
    The first 17 items are the standard HAM-D-17, with 4 additional items (18-21).
    
    Scoring varies by item:
    - Items 1-3, 10-11, 15, 19-20: 0-4
    - Items 4-6, 8, 12-14, 16-18, 21: 0-2
    - Item 7: 0-4
    - Item 9: 0-4
    
    Primary score: Sum of items 1-17 (HAM-D-17)
    Total score: Sum of all 21 items (HAM-D-21)
    
    Interpretation (HAM-D-17):
    - 0-7: Normal
    - 8-16: Mild depression
    - 17-23: Moderate depression
    - ≥24: Severe depression
    """
    
    def __init__(self):
        self.name = "HAM-D-21"
        self.description = "Hamilton Depression Rating Scale - 21-item"
        self.num_items = 21
        self.questions = []
        self._init_questions()
    
    def _init_questions(self):
        """Initialize the 21 HAM-D items."""
        items = [
            ("Humeur dépressive", "0-4"),
            ("Sentiments de culpabilité", "0-4"),
            ("Suicide", "0-4"),
            ("Insomnie du début de la nuit", "0-2"),
            ("Insomnie du milieu de la nuit", "0-2"),
            ("Insomnie du matin", "0-2"),
            ("Travail et activités", "0-4"),
            ("Ralentissement", "0-4"),
            ("Agitation", "0-4"),
            ("Anxiété psychique", "0-4"),
            ("Anxiété somatique", "0-4"),
            ("Symptômes somatiques gastro-intestinaux", "0-2"),
            ("Symptômes somatiques généraux", "0-2"),
            ("Symptômes génitaux", "0-2"),
            ("Hypocondrie", "0-4"),
            ("Perte de poids A", "0-2"),
            ("Prise de conscience", "0-2"),
            ("Variations diurnes A", "0-2"),
            ("Dépersonnalisation et déréalisation", "0-4"),
            ("Symptômes délirants", "0-4"),
            ("Symptômes obsessionnels et compulsionnels", "0-2")
        ]
        
        for i, (text, scale) in enumerate(items):
            self.questions.append({
                'id': f'HAMD{i+1}',
                'text': text,
                'scale': scale
            })
    
    def calculate_score(self, responses: List[int]) -> Dict[str, Any]:
        """Calculate HAM-D scores."""
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, got {len(responses)}")
        
        # Validate each item's range
        ranges = [4, 4, 4, 2, 2, 2, 4, 4, 4, 4, 4, 2, 2, 2, 4, 2, 2, 2, 4, 4, 2]
        for i, (r, max_val) in enumerate(zip(responses, ranges)):
            if r < 0 or r > max_val:
                raise ValueError(f"Item {i+1} must be 0-{max_val}, got {r}")
        
        # HAM-D-17 (items 1-17)
        hamd_17 = sum(responses[:17])
        
        # HAM-D-21 (all items)
        hamd_21 = sum(responses)
        
        return {
            'hamd_17': hamd_17,
            'hamd_21': hamd_21,
            'interpretation_17': self._interpret_17(hamd_17),
            'interpretation_21': self._interpret_21(hamd_21),
            'max_17': 52,
            'max_21': 62
        }
    
    def _interpret_17(self, score: int) -> str:
        """Interpret HAM-D-17 score."""
        if score <= 7:
            return "Normal/No depression"
        elif score <= 16:
            return "Mild depression"
        elif score <= 23:
            return "Moderate depression"
        else:
            return "Severe depression"
    
    def _interpret_21(self, score: int) -> str:
        """Interpret HAM-D-21 score."""
        if score <= 10:
            return "Normal/No depression"
        elif score <= 20:
            return "Mild depression"
        elif score <= 30:
            return "Moderate depression"
        else:
            return "Severe depression"

if __name__ == '__main__':
    hamd = HamiltonDepressionQuestionnaire()
    print(f"Questionnaire: {hamd.name} - {hamd.num_items} items\n")
    
    # Example 1: Minimal depression
    print("Example 1: Minimal Depression")
    responses1 = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    result1 = hamd.calculate_score(responses1)
    print(f"HAM-D-17: {result1['hamd_17']}/52 - {result1['interpretation_17']}")
    print(f"HAM-D-21: {result1['hamd_21']}/62 - {result1['interpretation_21']}\n")
    
    # Example 2: Moderate depression
    print("Example 2: Moderate Depression")
    responses2 = [2, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 0, 0, 0]
    result2 = hamd.calculate_score(responses2)
    print(f"HAM-D-17: {result2['hamd_17']}/52 - {result2['interpretation_17']}")
    print(f"HAM-D-21: {result2['hamd_21']}/62 - {result2['interpretation_21']}\n")
    
    # Example 3: Severe depression
    print("Example 3: Severe Depression")
    responses3 = [4, 4, 3, 2, 2, 2, 4, 3, 3, 4, 4, 2, 2, 2, 3, 2, 2, 2, 2, 3, 2]
    result3 = hamd.calculate_score(responses3)
    print(f"HAM-D-17: {result3['hamd_17']}/52 - {result3['interpretation_17']}")
    print(f"HAM-D-21: {result3['hamd_21']}/62 - {result3['interpretation_21']}")
