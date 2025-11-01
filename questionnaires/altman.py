"""
Questionnaire: Altman Self-Rating Mania Scale (ASRM)
Échelle d'auto-évaluation de la manie d'Altman
"""

from typing import Dict, List, Optional, Any


class AltmanQuestionnaire:
    """Altman Self-Rating Mania Scale (ASRM)
    
    Auto-questionnaire de dépistage de l'hypomanie/manie en 5 items.
    Évalue les symptômes maniaques sur la semaine dernière.
    
    Développé par Altman et al. (1997)
    
    5 dimensions évaluées:
    1. Humeur euphorique/joyeuse
    2. Confiance en soi
    3. Besoin de sommeil réduit
    4. Logorrhée (parler plus)
    5. Hyperactivité (sociale, sexuelle, professionnelle)
    
    Chaque item: 5 réponses (0-4 points)
    - 0 = Pas plus que d'habitude
    - 1 = Parfois plus que d'habitude
    - 2 = Souvent plus que d'habitude
    - 3 = Fréquemment / la plupart du temps
    - 4 = Tout le temps / constamment
    
    Score total: 0-20
    Cutoff: ≥ 6 suggère hypomanie/manie (sensibilité 85.5%, spécificité 87.3%)
    """
    
    def __init__(self):
        self.name = "ASRM - Altman Self-Rating Mania Scale"
        self.description = ("Échelle d'auto-évaluation de la manie en 5 items. "
                           "Évalue les symptômes maniaques sur la semaine dernière.")
        self.used_in_applications = ["ebipolar", "eschizo"]
        self.questions = self._init_questions()
        
    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 5 Altman items"""
        
        questions = [
            {
                'id': 'radhtml_altman1',
                'number': 1,
                'topic': 'Humeur euphorique',
                'text': "Je ne me sens pas plus heureux(se) ou plus joyeux(se) que d'habitude",
                'options': {
                    'a': 0,
                    'b': 1,
                    'c': 2,
                    'd': 3,
                    'e': 4
                },
                'labels': {
                    'a': "Je ne me sens pas plus heureux(se) ou plus joyeux(se) que d'habitude",
                    'b': "Je me sens parfois plus heureux(se) ou plus joyeux(se) que d'habitude",
                    'c': "Je me sens souvent plus heureux(se) ou plus joyeux(se) que d'habitude",
                    'd': "Je me sens plus heureux(se) ou plus joyeux(se) que d'habitude la plupart du temps",
                    'e': "Je me sens plus heureux(se) ou plus joyeux(se) que d'habitude tout le temps"
                }
            },
            {
                'id': 'radhtml_altman2',
                'number': 2,
                'topic': 'Confiance en soi',
                'text': "Je ne me sens pas plus sûr(e) de moi que d'habitude",
                'options': {
                    'a': 0,
                    'b': 1,
                    'c': 2,
                    'd': 3,
                    'e': 4
                },
                'labels': {
                    'a': "Je ne me sens pas plus sûr(e) de moi que d'habitude",
                    'b': "Je me sens parfois plus sûr(e) de moi que d'habitude",
                    'c': "Je me sens souvent plus sûr(e) de moi que d'habitude",
                    'd': "Je me sens plus sûr(e) de moi que d'habitude la plupart du temps",
                    'e': "Je me sens extrêmement sûr de moi tout le temps"
                }
            },
            {
                'id': 'radhtml_altman3',
                'number': 3,
                'topic': 'Besoin de sommeil',
                'text': "Je n'ai pas besoin de moins de sommeil que d'habitude",
                'options': {
                    'a': 0,
                    'b': 1,
                    'c': 2,
                    'd': 3,
                    'e': 4
                },
                'labels': {
                    'a': "Je n'ai pas besoin de moins de sommeil que d'habitude",
                    'b': "J'ai parfois besoin de moins de sommeil que d'habitude",
                    'c': "J'ai souvent besoin de moins de sommeil que d'habitude",
                    'd': "J'ai fréquemment besoin de moins de sommeil que d'habitude",
                    'e': "Je peux passer toute la journée et toute la nuit sans dormir et ne toujours pas être fatigué(e)"
                }
            },
            {
                'id': 'radhtml_altman4',
                'number': 4,
                'topic': 'Logorrhée',
                'text': "Je ne parle pas plus que d'habitude",
                'options': {
                    'a': 0,
                    'b': 1,
                    'c': 2,
                    'd': 3,
                    'e': 4
                },
                'labels': {
                    'a': "Je ne parle pas plus que d'habitude",
                    'b': "Je parle parfois plus que d'habitude",
                    'c': "Je parle souvent plus que d'habitude",
                    'd': "Je parle fréquemment plus que d'habitude",
                    'e': "Je parle sans arrêt et je ne peux être interrompu(e)"
                }
            },
            {
                'id': 'radhtml_altman5',
                'number': 5,
                'topic': 'Hyperactivité',
                'text': "Je n'ai pas été plus actif(ve) que d'habitude",
                'options': {
                    'a': 0,
                    'b': 1,
                    'c': 2,
                    'd': 3,
                    'e': 4
                },
                'labels': {
                    'a': "Je n'ai pas été plus actif(ve) (que ce soit socialement, sexuellement, au travail, à la maison ou à l'école) que d'habitude",
                    'b': "J'ai parfois été plus actif(ve) que d'habitude",
                    'c': "J'ai souvent été plus actif(ve) que d'habitude",
                    'd': "J'ai fréquemment été plus actif(ve) que d'habitude",
                    'e': "Je suis constamment actif(ve), ou en mouvement tout le temps"
                }
            }
        ]
        
        return questions
    
    def get_instructions(self) -> str:
        """Return the questionnaire instructions"""
        return (
            "Consignes : Choisir la proposition dans chaque groupe qui correspond le mieux "
            "à la manière dont vous vous êtes senti(e) la semaine dernière.\n\n"
            "Veuillez noter :\n"
            "- Le mot « parfois » utilisé ici signifie une ou deux fois\n"
            "- « Souvent » signifie plusieurs fois\n"
            "- « Fréquemment » signifie la plupart du temps"
        )
    
    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """Calculate Altman total score
        
        Scoring: Each item scored 0-4 based on response letter:
        - 'a' = 0 points (not more than usual)
        - 'b' = 1 point (sometimes)
        - 'c' = 2 points (often)
        - 'd' = 3 points (frequently / most of the time)
        - 'e' = 4 points (all the time / constantly)
        
        Total score range: 0-20
        
        Interpretation:
        - 0-5: Pas d'hypomanie/manie
        - ≥ 6: Hypomanie/manie probable (cutoff validé)
          * Sensibilité: 85.5%
          * Spécificité: 87.3%
          * VPP (dans population bipolaire): 87.5%
        
        Args:
            responses: Dictionary mapping 'radhtml_altman1'-'radhtml_altman5' to 'a'-'e'
            
        Returns:
            Dictionary with total score, interpretation, and validation status
        """
        errors = []
        
        # Validate all responses
        for question in self.questions:
            q_id = question['id']
            if q_id not in responses:
                errors.append(f"Item {question['number']} ({question['topic']}) manquant")
            elif responses[q_id] not in ['a', 'b', 'c', 'd', 'e']:
                errors.append(f"Item {question['number']}: réponse doit être a, b, c, d ou e")
        
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
            item_scores[question['topic']] = score
            total_score += score
        
        return {
            'total_score': total_score,
            'item_scores': item_scores,
            'range': '0-20',
            'interpretation': self._interpret_score(total_score),
            'valid': True,
            'errors': []
        }
    
    def _interpret_score(self, score: int) -> str:
        """Interpret Altman total score"""
        if score < 6:
            return f"Score négatif ({score}/20) - Pas d'hypomanie/manie"
        else:
            return (f"Score positif ({score}/20) - Hypomanie/manie probable. "
                   f"Une évaluation clinique approfondie est recommandée.")


# Example usage
if __name__ == "__main__":
    questionnaire = AltmanQuestionnaire()
    
    print(f"=== {questionnaire.name} ===\n")
    print(f"{questionnaire.description}\n")
    print(f"Instructions:\n{questionnaire.get_instructions()}\n")
    print("=" * 70)
    
    # Example 1: No manic symptoms
    print("\n📋 Exemple 1: Patient sans symptômes maniaques")
    responses_normal = {
        'radhtml_altman1': 'a',
        'radhtml_altman2': 'a',
        'radhtml_altman3': 'a',
        'radhtml_altman4': 'a',
        'radhtml_altman5': 'a'
    }
    
    result = questionnaire.calculate_score(responses_normal)
    print(f"Score Total: {result['total_score']}/{result['range']}")
    print(f"{result['interpretation']}\n")
    
    # Example 2: Moderate manic symptoms
    print("📋 Exemple 2: Patient avec symptômes maniaques modérés")
    responses_moderate = {
        'radhtml_altman1': 'c',  # Often happier (2)
        'radhtml_altman2': 'b',  # Sometimes more confident (1)
        'radhtml_altman3': 'c',  # Often less sleep (2)
        'radhtml_altman4': 'b',  # Sometimes talk more (1)
        'radhtml_altman5': 'c'   # Often more active (2)
    }
    
    result = questionnaire.calculate_score(responses_moderate)
    print(f"Score Total: {result['total_score']}/{result['range']}")
    print(f"Scores par dimension: {result['item_scores']}")
    print(f"{result['interpretation']}\n")
    
    # Example 3: Severe manic symptoms
    print("📋 Exemple 3: Patient avec symptômes maniaques sévères")
    responses_severe = {
        'radhtml_altman1': 'e',  # All the time happier (4)
        'radhtml_altman2': 'd',  # Most of time confident (3)
        'radhtml_altman3': 'e',  # No sleep needed (4)
        'radhtml_altman4': 'd',  # Frequently talk more (3)
        'radhtml_altman5': 'e'   # Constantly active (4)
    }
    
    result = questionnaire.calculate_score(responses_severe)
    print(f"Score Total: {result['total_score']}/{result['range']}")
    print(f"Scores par dimension: {result['item_scores']}")
    print(f"{result['interpretation']}\n")
    
    print("=" * 70)
    print("\n📊 Propriétés psychométriques:")
    print("   • Sensibilité: 85.5%")
    print("   • Spécificité: 87.3%")
    print("   • Cutoff validé: ≥ 6")
    print("   • Corrélation avec YMRS: r = 0.72")

