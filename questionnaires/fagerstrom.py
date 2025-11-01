from typing import Dict, List, Any

class FagerstromQuestionnaire:
    """
    Fagerstrom Test for Nicotine Dependence (FTND)
    
    Description:
    6-item scale measuring nicotine dependence severity in cigarette smokers.
    
    Scoring varies by item:
    - Item 1: 0-3 points
    - Items 2, 3, 5, 6: 0-1 points  
    - Item 4: 0-3 points
    
    Total range: 0-10
    
    Interpretation:
    - 0-2: Very low dependence
    - 3-4: Low dependence
    - 5: Medium dependence
    - 6-7: High dependence
    - 8-10: Very high dependence
    """
    
    def __init__(self):
        self.name = "Fagerstrom"
        self.description = "Fagerstrom Test for Nicotine Dependence"
        self.num_items = 6
        self.questions = []
        self._init_questions()
    
    def _init_questions(self):
        """Initialize the 6 Fagerstrom items."""
        self.questions = [
            {
                'id': 'FAG_1',
                'text': "Combien de temps après votre réveil fumez-vous votre première cigarette ?",
                'responses': {
                    3: "dans les 5 minutes",
                    2: "de 6 à 30 minutes",
                    1: "de 31 à 60 minutes",
                    0: "après 60 minutes"
                }
            },
            {
                'id': 'FAG_2',
                'text': "Trouvez-vous difficile de vous abstenir de fumer dans les endroits où c'est interdit ?",
                'responses': {1: "Oui", 0: "Non"}
            },
            {
                'id': 'FAG_3',
                'text': "A quelle cigarette de la journée vous serait-il le plus difficile de renoncer ?",
                'responses': {1: "La première", 0: "n'importe quelle autre"}
            },
            {
                'id': 'FAG_4',
                'text': "Combien de cigarettes fumez-vous par jour ?",
                'responses': {
                    0: "10 ou moins",
                    1: "11-20",
                    2: "21-30",
                    3: "31 ou plus"
                }
            },
            {
                'id': 'FAG_5',
                'text': "Fumez-vous à un rythme plus soutenu le matin que l'après-midi ?",
                'responses': {1: "Oui", 0: "Non"}
            },
            {
                'id': 'FAG_6',
                'text': "Fumez-vous lorsque vous êtes si malade que vous devez rester au lit ?",
                'responses': {1: "Oui", 0: "Non"}
            }
        ]
    
    def calculate_score(self, responses: List[int]) -> Dict[str, Any]:
        """Calculate Fagerstrom score."""
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, got {len(responses)}")
        
        # Validate ranges for each item
        valid_ranges = [[0,1,2,3], [0,1], [0,1], [0,1,2,3], [0,1], [0,1]]
        for i, (r, valid) in enumerate(zip(responses, valid_ranges)):
            if r not in valid:
                raise ValueError(f"Item {i+1} has invalid value {r}, expected one of {valid}")
        
        total_score = sum(responses)
        
        return {
            'total_score': total_score,
            'interpretation': self._interpret(total_score),
            'max_score': 10,
            'details': {
                'time_to_first_cigarette': responses[0],
                'difficulty_refraining': responses[1],
                'first_most_difficult': responses[2],
                'cigarettes_per_day': responses[3],
                'morning_smoking': responses[4],
                'smoking_when_ill': responses[5]
            }
        }
    
    def _interpret(self, score: int) -> str:
        """Interpret Fagerstrom score."""
        if score <= 2:
            return "Very low nicotine dependence"
        elif score <= 4:
            return "Low nicotine dependence"
        elif score == 5:
            return "Medium nicotine dependence"
        elif score <= 7:
            return "High nicotine dependence"
        else:
            return "Very high nicotine dependence"


if __name__ == '__main__':
    fag = FagerstromQuestionnaire()
    print(f"Questionnaire: {fag.name} - {fag.num_items} items\n")
    
    # Example 1: Very low dependence
    print("Example 1: Very Low Dependence")
    responses1 = [0, 0, 0, 0, 0, 0]
    result1 = fag.calculate_score(responses1)
    print(f"Total: {result1['total_score']}/10 - {result1['interpretation']}\n")
    
    # Example 2: Medium dependence
    print("Example 2: Medium Dependence")
    responses2 = [1, 1, 1, 1, 1, 0]
    result2 = fag.calculate_score(responses2)
    print(f"Total: {result2['total_score']}/10 - {result2['interpretation']}\n")
    
    # Example 3: Very high dependence
    print("Example 3: Very High Dependence")
    responses3 = [3, 1, 1, 3, 1, 1]
    result3 = fag.calculate_score(responses3)
    print(f"Total: {result3['total_score']}/10 - {result3['interpretation']}")
