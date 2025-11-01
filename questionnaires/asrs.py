"""
Questionnaire: ASRS (Adult ADHD Self-Report Scale)
Échelle d'auto-évaluation du TDAH adulte
"""

from typing import Dict, List, Optional, Any


class ASRSQuestionnaire:
    """ASRS - Adult ADHD Self-Report Scale (Version 1.1)
    
    Auto-questionnaire de dépistage du TDAH chez l'adulte en 18 items.
    Évalue les symptômes au cours des 6 derniers mois.
    
    Développé par l'OMS et Kessler et al. (2005)
    
    Structure:
    - Partie A (items 1-6): Screener - symptômes les plus prédictifs
    - Partie B (items 7-18): Symptômes additionnels
    
    Chaque item: 5 réponses de fréquence
    - Jamais
    - Rarement
    - Quelquefois
    - Souvent
    - Très souvent
    
    Scoring:
    - Partie A: Chaque item marqué "Souvent" ou "Très souvent" = 1 point
      * Items 1-3: Seuil = Souvent/Très souvent
      * Items 4-6: Seuil = Très souvent uniquement
    - Cutoff Partie A: ≥ 4/6 suggère fortement TDAH adulte
    - Score total (0-18): Nombre d'items ≥ seuil
    """
    
    def __init__(self):
        self.name = "ASRS - Adult ADHD Self-Report Scale"
        self.description = ("Échelle d'auto-évaluation du TDAH adulte en 18 items. "
                           "Évalue les symptômes sur les 6 derniers mois.")
        self.used_in_applications = ["ebipolar", "eschizo"]
        self.questions = self._init_questions()
        
    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 18 ASRS items"""
        
        # Response options (same for all items)
        response_options = {
            'Jamais': 0,
            'Rarement': 1,
            'Quelquefois': 2,
            'Souvent': 3,
            'Très souvent': 4
        }
        
        # Part A: Screener items (most predictive)
        part_a_items = [
            {
                'id': 'rad_ASRS01',
                'number': 1,
                'part': 'A',
                'text': "A quelle fréquence vous arrive-t-il d'avoir des difficultés à finaliser les derniers détails d'un projet une fois que les parties les plus stimulantes ont été faites ?",
                'domain': 'Inattention',
                'threshold': 'Souvent',  # For Part A items 1-3
                'options': response_options
            },
            {
                'id': 'rad_ASRS02',
                'number': 2,
                'part': 'A',
                'text': "A quelle fréquence vous arrive-t-il d'avoir des difficultés à mettre les choses en ordre lorsque vous devez faire quelque chose qui demande de l'organisation ?",
                'domain': 'Inattention',
                'threshold': 'Souvent',
                'options': response_options
            },
            {
                'id': 'rad_ASRS03',
                'number': 3,
                'part': 'A',
                'text': "A quelle fréquence vous arrive-t-il d'avoir des difficultés à vous rappeler vos rendez-vous ou vos obligations ?",
                'domain': 'Inattention',
                'threshold': 'Souvent',
                'options': response_options
            },
            {
                'id': 'rad_ASRS04',
                'number': 4,
                'part': 'A',
                'text': "Quand vous devez faire quelque chose qui demande beaucoup de réflexion, à quelle fréquence vous arrive-t-il d'éviter de le faire ou de le remettre à plus tard ?",
                'domain': 'Inattention',
                'threshold': 'Très souvent',  # For Part A items 4-6
                'options': response_options
            },
            {
                'id': 'rad_ASRS05',
                'number': 5,
                'part': 'A',
                'text': "A quelle fréquence vous arrive-t-il de remuer ou de tortiller les mains ou les pieds lorsque vous devez rester assis pendant une période prolongée ?",
                'domain': 'Hyperactivité',
                'threshold': 'Très souvent',
                'options': response_options
            },
            {
                'id': 'rad_ASRS06',
                'number': 6,
                'part': 'A',
                'text': "A quelle fréquence vous arrive-t-il de vous sentir excessivement actif et contraint de faire quelque chose, comme si vous étiez entraîné malgré vous par un moteur ?",
                'domain': 'Hyperactivité',
                'threshold': 'Très souvent',
                'options': response_options
            }
        ]
        
        # Part B: Additional symptoms
        part_b_items = [
            {
                'id': 'rad_ASRS07',
                'number': 7,
                'part': 'B',
                'text': "Avec quelle fréquence faites-vous des erreurs d'étourderie lorsque vous travaillez sur un projet ennuyeux ou difficile?",
                'domain': 'Inattention',
                'threshold': 'Souvent',
                'options': response_options
            },
            {
                'id': 'rad_ASRS08',
                'number': 8,
                'part': 'B',
                'text': "Avec quelle fréquence avez-vous des difficultés à rester attentif lorsque vous faites un travail ennuyeux ou répétitif?",
                'domain': 'Inattention',
                'threshold': 'Souvent',
                'options': response_options
            },
            {
                'id': 'rad_ASRS09',
                'number': 9,
                'part': 'B',
                'text': "A quelle fréquence vous arrive-t-il d'avoir des difficultés à vous concentrer sur les propos de votre interlocuteur, même s'il s'adresse directement à vous?",
                'domain': 'Inattention',
                'threshold': 'Souvent',
                'options': response_options
            },
            {
                'id': 'rad_ASRS10',
                'number': 10,
                'part': 'B',
                'text': "A la maison ou au travail, à quelle fréquence vous arrive-t-il d'égarer des choses ou d'avoir des difficultés à les retrouver?",
                'domain': 'Inattention',
                'threshold': 'Souvent',
                'options': response_options
            },
            {
                'id': 'rad_ASRS11',
                'number': 11,
                'part': 'B',
                'text': "Avec quelle fréquence êtes-vous distrait par de l'activité ou du bruit autour de vous?",
                'domain': 'Inattention',
                'threshold': 'Souvent',
                'options': response_options
            },
            {
                'id': 'rad_ASRS12',
                'number': 12,
                'part': 'B',
                'text': "A quelle fréquence vous arrive-t-il de quitter votre siège pendant des réunions ou d'autres situations ou vous devriez rester assis?",
                'domain': 'Hyperactivité',
                'threshold': 'Souvent',
                'options': response_options
            },
            {
                'id': 'rad_ASRS13',
                'number': 13,
                'part': 'B',
                'text': "A quelle fréquence vous arrive-t-il d'avoir des difficultés à vous tenir tranquille?",
                'domain': 'Hyperactivité',
                'threshold': 'Souvent',
                'options': response_options
            },
            {
                'id': 'rad_ASRS14',
                'number': 14,
                'part': 'B',
                'text': "Avec quelle fréquence avez-vous des difficultés à vous détendre et à vous reposer pendant votre temps libre?",
                'domain': 'Hyperactivité',
                'threshold': 'Très souvent',
                'options': response_options
            },
            {
                'id': 'rad_ASRS15',
                'number': 15,
                'part': 'B',
                'text': "A quelle fréquence vous arrive-t-il de parler de façon excessive à l'occasion de rencontres sociales?",
                'domain': 'Hyperactivité/Impulsivité',
                'threshold': 'Souvent',
                'options': response_options
            },
            {
                'id': 'rad_ASRS16',
                'number': 16,
                'part': 'B',
                'text': "Pendant une conversation, à quelle fréquence vous arrive-t-il de terminer les phrases de vos interlocuteurs avant que ces derniers aient le temps de les finir?",
                'domain': 'Impulsivité',
                'threshold': 'Souvent',
                'options': response_options
            },
            {
                'id': 'rad_ASRS17',
                'number': 17,
                'part': 'B',
                'text': "A quelle fréquence vous arrive-t-il d'avoir des difficultés à attendre votre tour lorsque vous devriez le faire?",
                'domain': 'Impulsivité',
                'threshold': 'Souvent',
                'options': response_options
            },
            {
                'id': 'rad_ASRS18',
                'number': 18,
                'part': 'B',
                'text': "A quelle fréquence vous arrive-t-il d'interrompre les gens lorsqu'ils sont occupés?",
                'domain': 'Impulsivité',
                'threshold': 'Souvent',
                'options': response_options
            }
        ]
        
        return part_a_items + part_b_items
    
    def get_instructions(self) -> str:
        """Return the questionnaire instructions"""
        return (
            "Cochez la case qui décrit le mieux ce que vous avez ressenti et comment vous "
            "vous êtes comporté au cours des 6 derniers mois.\n\n"
            "Veuillez remettre le questionnaire rempli à votre médecin ou un autre professionnel "
            "lors de votre prochain rendez-vous afin d'en discuter les résultats."
        )
    
    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """Calculate ASRS scores
        
        Scoring:
        1. Part A (Screener): Count items meeting threshold
           - Items 1-3: "Souvent" or "Très souvent" = 1 point
           - Items 4-6: "Très souvent" only = 1 point
           - Cutoff: ≥ 4/6 suggests ADHD
        
        2. Part B: Count items with "Souvent" or "Très souvent"
        
        3. Total: Part A + Part B (max 18)
        
        Args:
            responses: Dictionary mapping item IDs to frequency responses
            
        Returns:
            Dictionary with Part A, Part B, total scores and interpretation
        """
        errors = []
        
        # Validate all responses
        valid_responses = ['Jamais', 'Rarement', 'Quelquefois', 'Souvent', 'Très souvent']
        for question in self.questions:
            q_id = question['id']
            if q_id not in responses:
                errors.append(f"Item {question['number']} manquant")
            elif responses[q_id] not in valid_responses:
                errors.append(f"Item {question['number']}: réponse invalide")
        
        if errors:
            return {
                'valid': False,
                'errors': errors
            }
        
        # Calculate scores
        part_a_score = 0
        part_b_score = 0
        item_details = {}
        
        for question in self.questions:
            q_id = question['id']
            response = responses[q_id]
            
            # Determine if item meets threshold
            meets_threshold = False
            if question['threshold'] == 'Souvent':
                meets_threshold = response in ['Souvent', 'Très souvent']
            elif question['threshold'] == 'Très souvent':
                meets_threshold = response == 'Très souvent'
            
            item_details[f"Item {question['number']}"] = {
                'response': response,
                'meets_threshold': meets_threshold,
                'domain': question['domain']
            }
            
            if question['part'] == 'A':
                if meets_threshold:
                    part_a_score += 1
            else:  # Part B
                if meets_threshold:
                    part_b_score += 1
        
        total_score = part_a_score + part_b_score
        
        return {
            'part_a_score': part_a_score,
            'part_a_max': 6,
            'part_b_score': part_b_score,
            'part_b_max': 12,
            'total_score': total_score,
            'total_max': 18,
            'screener_positive': part_a_score >= 4,
            'item_details': item_details,
            'interpretation': self._interpret_score(part_a_score, total_score),
            'valid': True,
            'errors': []
        }
    
    def _interpret_score(self, part_a_score: int, total_score: int) -> str:
        """Interpret ASRS scores"""
        interpretation = []
        
        # Part A (Screener)
        if part_a_score >= 4:
            interpretation.append(
                f"✓ Screener POSITIF (Partie A: {part_a_score}/6) - "
                f"Symptômes de TDAH adulte hautement suggestifs. "
                f"Une évaluation diagnostique complète est fortement recommandée."
            )
        else:
            interpretation.append(
                f"Screener négatif (Partie A: {part_a_score}/6) - "
                f"TDAH moins probable, mais n'exclut pas le diagnostic."
            )
        
        # Total score
        if total_score >= 12:
            severity = "nombreux symptômes de TDAH"
        elif total_score >= 8:
            severity = "symptômes modérés de TDAH"
        elif total_score >= 4:
            severity = "quelques symptômes de TDAH"
        else:
            severity = "peu de symptômes de TDAH"
        
        interpretation.append(f"Score total: {total_score}/18 - {severity}")
        
        return "\n".join(interpretation)


# Example usage
if __name__ == "__main__":
    questionnaire = ASRSQuestionnaire()
    
    print(f"=== {questionnaire.name} ===\n")
    print(f"{questionnaire.description}\n")
    print(f"Instructions:\n{questionnaire.get_instructions()}\n")
    print("=" * 70)
    
    # Example: Person with ADHD symptoms
    print("\n📋 Exemple: Patient avec symptômes TDAH")
    responses_adhd = {
        # Part A - High frequency symptoms
        'rad_ASRS01': 'Très souvent',
        'rad_ASRS02': 'Souvent',
        'rad_ASRS03': 'Souvent',
        'rad_ASRS04': 'Très souvent',
        'rad_ASRS05': 'Très souvent',
        'rad_ASRS06': 'Souvent',
        # Part B
        'rad_ASRS07': 'Souvent',
        'rad_ASRS08': 'Très souvent',
        'rad_ASRS09': 'Souvent',
        'rad_ASRS10': 'Quelquefois',
        'rad_ASRS11': 'Très souvent',
        'rad_ASRS12': 'Rarement',
        'rad_ASRS13': 'Souvent',
        'rad_ASRS14': 'Quelquefois',
        'rad_ASRS15': 'Souvent',
        'rad_ASRS16': 'Souvent',
        'rad_ASRS17': 'Rarement',
        'rad_ASRS18': 'Quelquefois'
    }
    
    result = questionnaire.calculate_score(responses_adhd)
    
    print(f"\nPartie A (Screener): {result['part_a_score']}/{result['part_a_max']}")
    print(f"Partie B: {result['part_b_score']}/{result['part_b_max']}")
    print(f"Score Total: {result['total_score']}/{result['total_max']}")
    print(f"Screener Positif: {'OUI' if result['screener_positive'] else 'NON'}")
    print(f"\n{result['interpretation']}\n")
    
    print("=" * 70)
    print("\n📊 Propriétés psychométriques:")
    print("   • Sensibilité: 68.7%")
    print("   • Spécificité: 99.5%")
    print("   • Cutoff Partie A: ≥ 4/6")
    print("   • Corrélation test-retest: r = 0.84")

