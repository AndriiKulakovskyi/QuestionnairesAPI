"""
Questionnaire: MARS (Medication Adherence Rating Scale)
Échelle d'Observance Médicamenteuse
"""

from typing import Dict, List, Optional, Any


class MARSQuestionnaire:
    """MARS - Medication Adherence Rating Scale
    
    Auto-questionnaire d'évaluation de l'observance médicamenteuse en 10 items.
    Questions binaires (Oui/Non) avec scoring direct et inverse.
    """
    
    def __init__(self):
        self.name = "MARS - Medication Adherence Rating Scale"
        self.description = ("Échelle d'observance médicamenteuse en 10 items. "
                           "Ce questionnaire permet de mieux comprendre les difficultés liées "
                           "à la prise de médicaments.")
        self.used_in_applications = ["ebipolar", "eschizo"]
        self.questions = self._init_questions()
        
    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 10 MARS items"""
        
        questions = [
            {
                'id': 'rad_mars_1',
                'number': 1,
                'text': "Vous est-il parfois arrivé d'oublier de prendre vos médicaments",
                'type': 'radio',
                'options': ['Oui', 'Non'],
                'required': True,
                'reverse_scored': False  # Direct scoring: Oui=1 (poor adherence)
            },
            {
                'id': 'rad_mars_2',
                'number': 2,
                'text': "Négligez vous parfois l'heure de prise d'un de vos médicaments",
                'type': 'radio',
                'options': ['Oui', 'Non'],
                'required': True,
                'reverse_scored': False  # Direct scoring: Oui=1 (poor adherence)
            },
            {
                'id': 'rad_mars_3',
                'number': 3,
                'text': "Lorsque vous vous sentez mieux, interrompez vous parfois votre traitement",
                'type': 'radio',
                'options': ['Oui', 'Non'],
                'required': True,
                'reverse_scored': False  # Direct scoring: Oui=1 (poor adherence)
            },
            {
                'id': 'rad_mars_4',
                'number': 4,
                'text': "Vous est il arrivé d'arrêter le traitement parce que vous vous sentiez moins bien en le prenant",
                'type': 'radio',
                'options': ['Oui', 'Non'],
                'required': True,
                'reverse_scored': False  # Direct scoring: Oui=1 (poor adherence)
            },
            {
                'id': 'rad_mars_5',
                'number': 5,
                'text': "Je ne prends les médicaments que lorsque je me sens malade",
                'type': 'radio',
                'options': ['Oui', 'Non'],
                'required': True,
                'reverse_scored': False  # Direct scoring: Oui=1 (poor adherence)
            },
            {
                'id': 'rad_mars_6',
                'number': 6,
                'text': "Ce n'est pas naturel pour mon corps et mon esprit d'être équilibré par des médicaments",
                'type': 'radio',
                'options': ['Oui', 'Non'],
                'required': True,
                'reverse_scored': False  # Direct scoring: Oui=1 (negative attitude)
            },
            {
                'id': 'rad_mars_7',
                'number': 7,
                'text': "Mes idées sont plus claires avec les médicaments",
                'type': 'radio',
                'options': ['Oui', 'Non'],
                'required': True,
                'reverse_scored': True  # Reverse scoring: Oui=1 (positive attitude)
            },
            {
                'id': 'rad_mars_8',
                'number': 8,
                'text': "En continuant à prendre les médicaments, je peux éviter de tomber à nouveau malade",
                'type': 'radio',
                'options': ['Oui', 'Non'],
                'required': True,
                'reverse_scored': True  # Reverse scoring: Oui=1 (positive attitude)
            },
            {
                'id': 'rad_mars_9',
                'number': 9,
                'text': "Avec les médicaments, je me sens bizarre, comme un « zombie »",
                'type': 'radio',
                'options': ['Oui', 'Non'],
                'required': True,
                'reverse_scored': False  # Direct scoring: Oui=1 (negative perception)
            },
            {
                'id': 'rad_mars_10',
                'number': 10,
                'text': "Les médicaments me rendent lourd (e) et fatigué (e)",
                'type': 'radio',
                'options': ['Oui', 'Non'],
                'required': True,
                'reverse_scored': False  # Direct scoring: Oui=1 (negative perception)
            }
        ]
        
        return questions
    
    def validate_responses(self, responses: Dict[str, str]) -> Dict[str, List[str]]:
        """Validate responses and return any errors
        
        Args:
            responses: Dictionary mapping question IDs to response strings ('Oui' or 'Non')
            
        Returns:
            Dictionary with 'errors' key containing list of error messages
        """
        errors = []
        
        for question in self.questions:
            q_id = question['id']
            if q_id not in responses or responses[q_id] is None:
                errors.append(f"La question {question['number']} doit être renseignée")
            elif responses[q_id] not in question['options']:
                errors.append(f"Valeur invalide pour la question {question['number']} (attendu: Oui ou Non)")
        
        return {'errors': errors, 'valid': len(errors) == 0}
    
    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """Calculate MARS total score
        
        Scoring:
        - Direct scoring (items 1-6, 9-10): Oui = 1, Non = 0 (poor adherence/attitude)
        - Reverse scoring (items 7-8): Oui = 0, Non = 1 (positive attitude inverted)
        
        Total score range: 0-10
        - Higher scores indicate POORER medication adherence
        - Lower scores indicate BETTER medication adherence
        
        Args:
            responses: Dictionary mapping question IDs to response strings ('Oui' or 'Non')
            
        Returns:
            Dictionary containing:
                - 'score': Total MARS score (0-10)
                - 'valid': Whether calculation was possible
                - 'errors': List of error messages if any
                - 'interpretation': Adherence level interpretation
        """
        # Validate responses first
        validation = self.validate_responses(responses)
        if not validation['valid']:
            return {
                'score': None,
                'valid': False,
                'errors': validation['errors']
            }
        
        # Calculate total score
        total_score = 0
        for question in self.questions:
            q_id = question['id']
            response = responses.get(q_id)
            
            if question['reverse_scored']:
                # Reverse scoring: Oui=0, Non=1
                # (For positive attitude statements - we want "Oui" to indicate better adherence,
                # but since higher total = worse adherence, we invert)
                if response == 'Oui':
                    total_score += 0  # Good attitude, don't add to poor adherence score
                else:  # Non
                    total_score += 1  # Negative attitude, add to poor adherence score
            else:
                # Direct scoring: Oui=1, Non=0
                # (For negative behaviors/attitudes - "Oui" indicates poor adherence)
                if response == 'Oui':
                    total_score += 1  # Poor adherence behavior
                else:  # Non
                    total_score += 0  # Good adherence behavior
        
        return {
            'score': total_score,
            'valid': True,
            'errors': [],
            'interpretation': self._interpret_score(total_score)
        }
    
    def _interpret_score(self, score: int) -> str:
        """Interpret MARS total score
        
        IMPORTANT: Higher MARS scores indicate POORER adherence
        
        Cutoffs (commonly used in literature):
        - 0-2: Bonne observance
        - 3-5: Observance modérée
        - 6-10: Mauvaise observance
        
        Args:
            score: Total MARS score (0-10)
            
        Returns:
            Interpretation text
        """
        if score <= 2:
            return "Bonne observance médicamenteuse"
        elif score <= 5:
            return "Observance médicamenteuse modérée"
        else:
            return "Mauvaise observance médicamenteuse (risque élevé de non-adhérence)"


# Example usage
if __name__ == "__main__":
    questionnaire = MARSQuestionnaire()
    
    # Example responses (moderate adherence with some issues)
    example_responses = {
        'rad_mars_1': "Oui",   # Sometimes forget (poor adherence)
        'rad_mars_2': "Non",   # Don't neglect timing (good)
        'rad_mars_3': "Non",   # Don't stop when feeling better (good)
        'rad_mars_4': "Non",   # Don't stop when feeling worse (good)
        'rad_mars_5': "Non",   # Don't take only when sick (good)
        'rad_mars_6': "Oui",   # Think it's not natural (negative attitude)
        'rad_mars_7': "Oui",   # Ideas clearer with meds (positive - reverse scored)
        'rad_mars_8': "Oui",   # Believe meds prevent relapse (positive - reverse scored)
        'rad_mars_9': "Non",   # Don't feel like zombie (good)
        'rad_mars_10': "Oui"   # Feel heavy/tired (negative perception)
    }
    
    result = questionnaire.calculate_score(example_responses)
    print(f"Score MARS: {result['score']}/10")
    print(f"Interprétation: {result['interpretation']}")
    print(f"\nNote: Score élevé = mauvaise observance")

