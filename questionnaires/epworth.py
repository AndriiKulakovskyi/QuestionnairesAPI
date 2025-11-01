"""
Questionnaire: Epworth Sleepiness Scale (ESS)
Échelle de somnolence d'Epworth
"""

from typing import Dict, List, Optional, Any


class EpworthQuestionnaire:
    """Epworth Sleepiness Scale (ESS)
    
    Auto-questionnaire d'évaluation de la somnolence diurne en 8 items.
    Mesure la propension à s'endormir dans différentes situations de la vie quotidienne.
    
    Développé par Murray Johns (1991)
    
    8 situations évaluées:
    1. Assis en train de lire
    2. En train de regarder la télévision
    3. Assis inactif dans un lieu public
    4. Passager dans une voiture pendant 1 heure
    5. Allongé l'après-midi pour se reposer
    6. Assis en train de parler à quelqu'un
    7. Assis calmement après un repas sans alcool
    8. Dans une auto immobilisée quelques minutes
    
    Chaque item: 4 réponses (0-3 points)
    - 0 = Ne somnolerait jamais
    - 1 = Faible chance de s'endormir
    - 2 = Chance moyenne de s'endormir
    - 3 = Forte chance de s'endormir
    
    Score total: 0-24
    Interprétation:
    - 0-10: Somnolence normale
    - 11-14: Somnolence excessive légère
    - 15-17: Somnolence excessive modérée
    - 18-24: Somnolence excessive sévère
    """
    
    def __init__(self):
        self.name = "ESS - Epworth Sleepiness Scale"
        self.description = ("Échelle d'évaluation de la somnolence diurne en 8 items. "
                           "Mesure la propension à s'endormir dans diverses situations quotidiennes.")
        self.used_in_applications = ["ebipolar", "eschizo", "cedr"]
        self.questions = self._init_questions()
        
    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 8 Epworth items"""
        
        # Response options (same for all items)
        response_options = {
            "Ne somnolerait jamais": 0,
            "Faible chance de s'endormir": 1,
            "Chance moyenne de s'endormir": 2,
            "Forte chance de s'endormir": 3
        }
        
        questions = [
            {
                'id': 'rad_epw1',
                'number': 1,
                'situation': "Assis en train de lire",
                'options': response_options
            },
            {
                'id': 'rad_epw2',
                'number': 2,
                'situation': "En train de regarder la télévision",
                'options': response_options
            },
            {
                'id': 'rad_epw3',
                'number': 3,
                'situation': "Assis, inactif, dans un endroit public (au théâtre, en réunion)",
                'options': response_options
            },
            {
                'id': 'rad_epw4',
                'number': 4,
                'situation': "Comme passager dans une voiture roulant sans arrêt pendant une heure",
                'options': response_options
            },
            {
                'id': 'rad_epw5',
                'number': 5,
                'situation': "Allongé l'après-midi pour se reposer quand les circonstances le permettent",
                'options': response_options
            },
            {
                'id': 'rad_epw6',
                'number': 6,
                'situation': "Assis en train de parler à quelqu'un",
                'options': response_options
            },
            {
                'id': 'rad_epw7',
                'number': 7,
                'situation': "Assis calmement après un repas sans alcool",
                'options': response_options
            },
            {
                'id': 'rad_epw8',
                'number': 8,
                'situation': "Dans une auto immobilisée quelques minutes dans un encombrement",
                'options': response_options
            }
        ]
        
        return questions
    
    def get_instructions(self) -> str:
        """Return the questionnaire instructions"""
        return (
            "Vous arrive-t-il de somnoler ou de vous endormir - et pas seulement de vous sentir fatigué - "
            "dans les situations suivantes ? Cette question s'adresse à votre vie dans les mois derniers.\n\n"
            "Même si vous ne vous êtes pas trouvé récemment dans l'une des situations suivantes, "
            "essayez de vous représenter comme elles auraient pu vous affecter.\n\n"
            "Choisissez dans l'échelle suivante le nombre le plus approprié à chaque situation."
        )
    
    def get_timing_question(self) -> Dict[str, Any]:
        """Return the qualitative timing question (not scored)"""
        return {
            'id': 'rad_epw_dorm',
            'question': "Ces envies de dormir surviennent-elles ?",
            'options': [
                "Seulement après les repas",
                "A certaines heures du jour toujours les mêmes",
                "La nuit",
                "A n'importe quelle heure du jour"
            ],
            'scored': False
        }
    
    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """Calculate Epworth total score
        
        Scoring: Simple summation of 8 items (0-3 each)
        Total score range: 0-24
        
        Interpretation:
        - 0-10: Normal daytime sleepiness
        - 11-14: Mild excessive daytime sleepiness (EDS)
        - 15-17: Moderate EDS
        - 18-24: Severe EDS (high risk for sleep disorder)
        
        Note: Score >10 suggests possible sleep disorder (e.g., sleep apnea, narcolepsy)
        and warrants clinical evaluation
        
        Args:
            responses: Dictionary mapping item IDs to response strings
            
        Returns:
            Dictionary with total score, interpretation, and validation status
        """
        errors = []
        
        # Validate all responses
        for question in self.questions:
            q_id = question['id']
            if q_id not in responses:
                errors.append(f"Item {question['number']} ({question['situation'][:30]}...) manquant")
            elif responses[q_id] not in question['options']:
                errors.append(f"Item {question['number']}: réponse invalide")
        
        if errors:
            return {
                'valid': False,
                'errors': errors
            }
        
        # Calculate total score
        total_score = 0
        item_scores = {}
        
        for question in self.questions:
            q_id = question['id']
            response = responses[q_id]
            score = question['options'][response]
            item_scores[f"Item {question['number']}"] = {
                'situation': question['situation'],
                'response': response,
                'score': score
            }
            total_score += score
        
        return {
            'total_score': total_score,
            'max_score': 24,
            'item_scores': item_scores,
            'interpretation': self._interpret_score(total_score),
            'clinical_significance': self._clinical_significance(total_score),
            'valid': True,
            'errors': []
        }
    
    def _interpret_score(self, score: int) -> str:
        """Interpret Epworth total score"""
        if score <= 10:
            return f"Somnolence normale ({score}/24) - Pas de somnolence excessive"
        elif score <= 14:
            return f"Somnolence excessive légère ({score}/24) - Surveillance recommandée"
        elif score <= 17:
            return f"Somnolence excessive modérée ({score}/24) - Évaluation clinique recommandée"
        else:
            return f"Somnolence excessive sévère ({score}/24) - Évaluation urgente recommandée"
    
    def _clinical_significance(self, score: int) -> str:
        """Provide clinical significance interpretation"""
        if score > 10:
            return (
                "Score suggestif d'une somnolence diurne excessive (SDE). "
                "Rechercher : apnée du sommeil, narcolepsie, syndrome des jambes sans repos, "
                "privation de sommeil, médicaments sédatifs, dépression."
            )
        else:
            return "Pas de somnolence diurne excessive significative."


# Example usage
if __name__ == "__main__":
    questionnaire = EpworthQuestionnaire()
    
    print(f"=== {questionnaire.name} ===\n")
    print(f"{questionnaire.description}\n")
    print(f"Instructions:\n{questionnaire.get_instructions()}\n")
    print("=" * 70)
    
    # Example 1: Normal sleepiness
    print("\n📋 Exemple 1: Somnolence normale")
    responses_normal = {
        'rad_epw1': 'Ne somnolerait jamais',
        'rad_epw2': 'Faible chance de s\'endormir',
        'rad_epw3': 'Ne somnolerait jamais',
        'rad_epw4': 'Chance moyenne de s\'endormir',
        'rad_epw5': 'Chance moyenne de s\'endormir',
        'rad_epw6': 'Ne somnolerait jamais',
        'rad_epw7': 'Faible chance de s\'endormir',
        'rad_epw8': 'Ne somnolerait jamais'
    }
    
    result = questionnaire.calculate_score(responses_normal)
    print(f"Score Total: {result['total_score']}/{result['max_score']}")
    print(f"{result['interpretation']}")
    print(f"{result['clinical_significance']}\n")
    
    # Example 2: Moderate excessive daytime sleepiness
    print("📋 Exemple 2: Somnolence excessive modérée")
    responses_moderate = {
        'rad_epw1': 'Chance moyenne de s\'endormir',
        'rad_epw2': 'Forte chance de s\'endormir',
        'rad_epw3': 'Faible chance de s\'endormir',
        'rad_epw4': 'Forte chance de s\'endormir',
        'rad_epw5': 'Forte chance de s\'endormir',
        'rad_epw6': 'Faible chance de s\'endormir',
        'rad_epw7': 'Chance moyenne de s\'endormir',
        'rad_epw8': 'Chance moyenne de s\'endormir'
    }
    
    result = questionnaire.calculate_score(responses_moderate)
    print(f"Score Total: {result['total_score']}/{result['max_score']}")
    print(f"{result['interpretation']}")
    print(f"{result['clinical_significance']}\n")
    
    # Example 3: Severe excessive daytime sleepiness
    print("📋 Exemple 3: Somnolence excessive sévère")
    responses_severe = {
        'rad_epw1': 'Forte chance de s\'endormir',
        'rad_epw2': 'Forte chance de s\'endormir',
        'rad_epw3': 'Forte chance de s\'endormir',
        'rad_epw4': 'Forte chance de s\'endormir',
        'rad_epw5': 'Forte chance de s\'endormir',
        'rad_epw6': 'Chance moyenne de s\'endormir',
        'rad_epw7': 'Forte chance de s\'endormir',
        'rad_epw8': 'Forte chance de s\'endormir'
    }
    
    result = questionnaire.calculate_score(responses_severe)
    print(f"Score Total: {result['total_score']}/{result['max_score']}")
    print(f"{result['interpretation']}")
    print(f"{result['clinical_significance']}\n")
    
    # Show timing question
    timing_q = questionnaire.get_timing_question()
    print("=" * 70)
    print(f"\n📝 Question complémentaire (non cotée):")
    print(f"{timing_q['question']}")
    for opt in timing_q['options']:
        print(f"  • {opt}")
    
    print("\n=" * 70)
    print("\n📊 Propriétés psychométriques:")
    print("   • Cohérence interne: α = 0.88")
    print("   • Test-retest: r = 0.82")
    print("   • Cutoff: > 10 pour SDE")
    print("   • Sensibilité à l'apnée du sommeil: 93.5%")

