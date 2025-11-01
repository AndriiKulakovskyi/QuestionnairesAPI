"""
Questionnaire: WURS-25 (Wender Utah Rating Scale - Short Form)
Échelle de Wender Utah pour le TDAH rétrospectif
"""

from typing import Dict, List, Optional, Any


class WURSQuestionnaire:
    """WURS-25 - Wender Utah Rating Scale (Short Form)
    
    Auto-questionnaire rétrospectif pour évaluer les symptômes de TDAH dans l'enfance.
    25 items sélectionnés parmi les 61 de la version complète.
    Évalue les comportements et caractéristiques durant l'enfance (jusqu'à 10-12 ans).
    """
    
    def __init__(self):
        self.name = "WURS-25 - Wender Utah Rating Scale"
        self.description = ("Échelle rétrospective d'évaluation du TDAH dans l'enfance en 25 items. "
                           "Les réponses concernent la période de l'enfance (jusqu'à 10-12 ans).")
        self.used_in_applications = ["ebipolar", "eschizo"]
        self.questions = self._init_questions()
        
    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize the 25 WURS items
        
        Items are numbered according to their position in the full 61-item scale.
        Only these 25 specific items are used in the short form scoring.
        """
        
        # Standard response options for all items
        response_options = {
            "Pas du tout, ou très légèrement": 0,
            "Légèrement": 1,
            "Modérément": 2,
            "Assez": 3,
            "Beaucoup": 4
        }
        
        # Items with their original numbering from the full 61-item scale
        questions_data = [
            (3, "Des problèmes de concentration, facilement distrait (e)"),
            (4, "Anxieux (se), se faisant du souci"),
            (5, "Nerveux (se), ne tenant pas en place"),
            (6, "Inattentif (ve), rêveur (se)"),
            (7, "Facilement en colère, « soupe au lait »"),
            (9, "Des éclats d'humeur, des accès de colère"),
            (10, "Des difficultés à me tenir aux choses, à mener mes projets jusqu'à la fin, à finir les choses commencées"),
            (11, "Têtu (e), obstiné (e)"),
            (12, "Triste ou cafardeux (se), déprimé (e), malheureux (se)"),
            (15, "Désobéissant (e) à mes parents, rebelle, effronté (e)"),
            (16, "Une mauvaise opinion de moi-même"),
            (17, "Irritable"),
            (20, "D'humeur changeante, avec des hauts et des bas"),
            (21, "En colère"),
            (24, "Impulsif (ve), agissant sans réfléchir"),
            (25, "Tendance à être immature"),
            (26, "Culpabilisé (e), plein (e) de regrets"),
            (27, "Une perte du contrôle de moi-même"),
            (28, "Tendance à être ou à agir de façon irrationnelle"),
            (29, "Impopulaire auprès des autres enfants, ne gardant pas longtemps mes amis, ne m'entendant pas avec les autres enfants"),
            (40, "Du mal à voir les choses du point de vue de quelqu'un d'autre"),
            (41, "Des ennuis avec les autorités, l'école, convoqué (e) au bureau du proviseur"),
            (51, "Dans l'ensemble un (e) mauvais (e) élève, apprenant lentement"),
            (56, "Des difficultés en mathématiques ou avec les chiffres"),
            (59, "En dessous de son potentiel")
        ]
        
        questions = []
        for original_num, text in questions_data:
            question = {
                'id': f'rad_wurs_{original_num}',
                'number': original_num,  # Keep original numbering for clarity
                'text': f"{original_num}. {text}",
                'type': 'radio',
                'options': response_options,
                'required': True
            }
            questions.append(question)
        
        return questions
    
    def validate_responses(self, responses: Dict[str, str]) -> Dict[str, List[str]]:
        """Validate responses and return any errors
        
        Args:
            responses: Dictionary mapping question IDs to response strings
            
        Returns:
            Dictionary with 'errors' key containing list of error messages
        """
        errors = []
        
        for question in self.questions:
            q_id = question['id']
            if q_id not in responses or responses[q_id] is None:
                errors.append(f"L'item {question['number']} doit être renseigné")
            elif responses[q_id] not in question['options']:
                errors.append(f"Valeur invalide pour l'item {question['number']}")
        
        return {'errors': errors, 'valid': len(errors) == 0}
    
    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """Calculate WURS-25 total score
        
        Scoring: Simple summation of all 25 items.
        Each item scored 0-4, giving total range of 0-100.
        
        Higher scores indicate more ADHD symptoms in childhood.
        
        Cutoff: Score ≥ 46 suggests retrospective diagnosis of ADHD
        (based on Wender et al., 1993)
        
        Args:
            responses: Dictionary mapping question IDs to response strings
            
        Returns:
            Dictionary containing:
                - 'score': Total WURS-25 score (0-100)
                - 'valid': Whether calculation was possible
                - 'errors': List of error messages if any
                - 'interpretation': Clinical interpretation
        """
        # Validate responses first
        validation = self.validate_responses(responses)
        if not validation['valid']:
            return {
                'score': None,
                'valid': False,
                'errors': validation['errors']
            }
        
        # Calculate total score by summing all items
        total_score = 0
        for question in self.questions:
            q_id = question['id']
            response_text = responses.get(q_id)
            total_score += question['options'][response_text]
        
        return {
            'score': total_score,
            'valid': True,
            'errors': [],
            'interpretation': self._interpret_score(total_score)
        }
    
    def _interpret_score(self, score: int) -> str:
        """Interpret WURS-25 total score
        
        Standard cutoff from research literature:
        - < 36: Improbable ADHD in childhood
        - 36-45: Possible ADHD in childhood
        - ≥ 46: Probable ADHD in childhood (high sensitivity/specificity)
        
        Args:
            score: Total WURS-25 score (0-100)
            
        Returns:
            Interpretation text
        """
        if score < 36:
            return "TDAH dans l'enfance peu probable"
        elif score < 46:
            return "TDAH dans l'enfance possible (score intermédiaire)"
        else:
            return "TDAH dans l'enfance probable (score ≥ 46)"


# Example usage
if __name__ == "__main__":
    questionnaire = WURSQuestionnaire()
    
    # Example responses (moderate ADHD symptoms)
    example_responses = {
        'rad_wurs_3': "Assez",           # Concentration problems
        'rad_wurs_4': "Modérément",      # Anxious
        'rad_wurs_5': "Assez",           # Nervous, restless
        'rad_wurs_6': "Beaucoup",        # Inattentive, dreamy
        'rad_wurs_7': "Modérément",      # Easily angry
        'rad_wurs_9': "Légèrement",      # Temper outbursts
        'rad_wurs_10': "Assez",          # Difficulty finishing things
        'rad_wurs_11': "Modérément",     # Stubborn
        'rad_wurs_12': "Légèrement",     # Sad, depressed
        'rad_wurs_15': "Légèrement",     # Disobedient
        'rad_wurs_16': "Modérément",     # Poor self-esteem
        'rad_wurs_17': "Modérément",     # Irritable
        'rad_wurs_20': "Assez",          # Mood swings
        'rad_wurs_21': "Légèrement",     # Angry
        'rad_wurs_24': "Beaucoup",       # Impulsive
        'rad_wurs_25': "Modérément",     # Immature
        'rad_wurs_26': "Légèrement",     # Guilty
        'rad_wurs_27': "Modérément",     # Loss of control
        'rad_wurs_28': "Légèrement",     # Irrational behavior
        'rad_wurs_29': "Assez",          # Unpopular with peers
        'rad_wurs_40': "Modérément",     # Trouble seeing others' viewpoint
        'rad_wurs_41': "Légèrement",     # Trouble with authorities
        'rad_wurs_51': "Modérément",     # Poor student
        'rad_wurs_56': "Assez",          # Difficulties with math
        'rad_wurs_59': "Modérément"      # Below potential
    }
    
    result = questionnaire.calculate_score(example_responses)
    print(f"Score WURS-25: {result['score']}/100")
    print(f"Interprétation: {result['interpretation']}")
    print(f"\nNote: Score ≥ 46 suggère un TDAH probable dans l'enfance")

