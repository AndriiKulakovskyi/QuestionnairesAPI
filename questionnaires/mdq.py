"""
Questionnaire: MDQ (Mood Disorder Questionnaire)
Questionnaire de Trouble de l'Humeur
"""

from typing import Dict, List, Optional, Any


class MDQQuestionnaire:
    """MDQ - Mood Disorder Questionnaire
    
    Auto-questionnaire de dépistage des troubles bipolaires en 13 items.
    Évalue les symptômes maniaques/hypomaniaques passés.
    
    Développé par Hirschfeld et al. (2000)
    
    Critères positifs:
    - ≥ 7 symptômes sur 13 (question 1)
    - Plusieurs symptômes simultanés (question 2 = Oui)
    - Impact fonctionnel modéré à sévère (question 3)
    """
    
    def __init__(self):
        self.name = "MDQ - Mood Disorder Questionnaire"
        self.description = ("Questionnaire de dépistage des troubles bipolaires. "
                           "13 items yes/no sur les symptômes maniaques/hypomaniaques.")
        self.used_in_applications = ["ebipolar"]
        self.questions = self._init_questions()
        
    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize MDQ items"""
        
        # Question 1: 13 symptom items (yes/no)
        symptom_items = [
            {
                'id': 'rad_mdq_remonte',
                'number': '1a',
                'text': "Vous vous sentiez si bien et si remonté que d'autres personnes pensaient que vous n'étiez pas comme d'habitude ou que vous étiez si remonté que vous alliez vous attirer des ennuis",
                'type': 'yes_no',
                'options': {'Oui': 1, 'Non': 0}
            },
            {
                'id': 'rad_mdq_humeur',
                'number': '1b',
                'text': "Vous étiez si irritable que vous criiez après les gens ou que vous provoquiez des bagarres ou des disputes",
                'type': 'yes_no',
                'options': {'Oui': 1, 'Non': 0}
            },
            {
                'id': 'rad_mdq_assurance',
                'number': '1c',
                'text': "Vous vous sentiez beaucoup plus sûr(e) de vous que d'habitude",
                'type': 'yes_no',
                'options': {'Oui': 1, 'Non': 0}
            },
            {
                'id': 'rad_mdq_sommeil',
                'number': '1d',
                'text': "Vous dormiez beaucoup moins que d'habitude et trouviez que cela ne vous manquait pas vraiment",
                'type': 'yes_no',
                'options': {'Oui': 1, 'Non': 0}
            },
            {
                'id': 'rad_mdq_parler',
                'number': '1e',
                'text': "Vous étiez beaucoup plus bavard(e) et parliez beaucoup plus vite que d'habitude",
                'type': 'yes_no',
                'options': {'Oui': 1, 'Non': 0}
            },
            {
                'id': 'rad_mdq_pensee',
                'number': '1f',
                'text': "Des pensées traversaient rapidement votre tête et vous ne pouviez pas les ralentir",
                'type': 'yes_no',
                'options': {'Oui': 1, 'Non': 0}
            },
            {
                'id': 'rad_mdq_concentration',
                'number': '1g',
                'text': "Vous étiez si facilement distrait(e) par ce qui vous entourait que vous aviez des difficultés à vous concentrer ou à poursuivre la même idée",
                'type': 'yes_no',
                'options': {'Oui': 1, 'Non': 0}
            },
            {
                'id': 'rad_mdq_energie',
                'number': '1h',
                'text': "Vous aviez beaucoup plus d'énergie que d'habitude",
                'type': 'yes_no',
                'options': {'Oui': 1, 'Non': 0}
            },
            {
                'id': 'rad_mdq_actif',
                'number': '1i',
                'text': "Vous étiez beaucoup plus actif(ve) ou que vous faisiez beaucoup plus de choses que d'habitude",
                'type': 'yes_no',
                'options': {'Oui': 1, 'Non': 0}
            },
            {
                'id': 'rad_mdq_sociale',
                'number': '1j',
                'text': "Vous étiez beaucoup plus sociable ou extraverti(e) que d'habitude, par exemple, vous téléphoniez à vos amis au milieu de la nuit",
                'type': 'yes_no',
                'options': {'Oui': 1, 'Non': 0}
            },
            {
                'id': 'rad_mdq_sexe',
                'number': '1k',
                'text': "Vous étiez beaucoup plus intéressé(e) par le sexe que d'habitude",
                'type': 'yes_no',
                'options': {'Oui': 1, 'Non': 0}
            },
            {
                'id': 'rad_mdq_gens',
                'number': '1l',
                'text': "Vous faisiez des choses inhabituelles pour vous ou que d'autres gens pensaient être excessives, imprudentes ou risquées",
                'type': 'yes_no',
                'options': {'Oui': 1, 'Non': 0}
            },
            {
                'id': 'rad_mdq_depense',
                'number': '1m',
                'text': "Vous dépensiez de l'argent de manière si inadaptée que cela vous attirait des ennuis ou à votre famille",
                'type': 'yes_no',
                'options': {'Oui': 1, 'Non': 0}
            }
        ]
        
        # Question 2: Co-occurrence
        co_occurrence = {
            'id': 'rad_mdq2',
            'number': '2',
            'text': "Si vous avez coché « oui » à plus d'une des questions précédentes, est-ce que plusieurs d'entre elles sont apparues durant la même période de temps ?",
            'type': 'yes_no',
            'options': {'Oui': 1, 'Non': 0}
        }
        
        # Question 3: Functional impairment
        impairment = {
            'id': 'rad_mdq3',
            'number': '3',
            'text': "À quel point, une de ces questions a été pour vous un problème ?",
            'type': 'severity',
            'options': {
                'Pas de problème': 0,
                'Problème mineur': 1,
                'Problème modéré': 2,
                'Problème sérieux': 3
            }
        }
        
        return symptom_items + [co_occurrence, impairment]
    
    def calculate_score(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate MDQ screen positivity
        
        Positive screen requires ALL THREE:
        1. ≥ 7 "Oui" answers on items 1a-1m (symptom count)
        2. "Oui" to question 2 (co-occurrence during same period)
        3. At least "Problème modéré" on question 3 (functional impairment)
        
        Args:
            responses: Dictionary with:
                - 'rad_mdq_*': 'Oui' or 'Non' for symptom items
                - 'rad_mdq2': 'Oui' or 'Non' for co-occurrence
                - 'rad_mdq3': severity level
                
        Returns:
            Dictionary with symptom count, screen result, and interpretation
        """
        errors = []
        
        # Get symptom items
        symptom_ids = [
            'rad_mdq_remonte', 'rad_mdq_humeur', 'rad_mdq_assurance', 'rad_mdq_sommeil',
            'rad_mdq_parler', 'rad_mdq_pensee', 'rad_mdq_concentration', 'rad_mdq_energie',
            'rad_mdq_actif', 'rad_mdq_sociale', 'rad_mdq_sexe', 'rad_mdq_gens', 'rad_mdq_depense'
        ]
        
        # Count "Oui" responses for symptom items
        symptom_count = 0
        for symptom_id in symptom_ids:
            if symptom_id not in responses:
                errors.append(f"Item {symptom_id} manquant")
            elif responses[symptom_id] == 'Oui':
                symptom_count += 1
        
        # Check co-occurrence (question 2)
        if 'rad_mdq2' not in responses:
            errors.append("Question 2 (co-occurrence) manquante")
            co_occurrence = None
        else:
            co_occurrence = responses['rad_mdq2'] == 'Oui'
        
        # Check functional impairment (question 3)
        if 'rad_mdq3' not in responses:
            errors.append("Question 3 (impact fonctionnel) manquante")
            impairment_level = None
            moderate_impairment = None
        else:
            impairment_level = responses['rad_mdq3']
            # Moderate or serious problem required
            moderate_impairment = impairment_level in ['Problème modéré', 'Problème sérieux']
        
        if errors:
            return {
                'valid': False,
                'errors': errors
            }
        
        # Determine screen positivity
        # All 3 criteria must be met:
        # 1. ≥ 7 symptoms
        # 2. Co-occurrence = Yes
        # 3. At least moderate impairment
        screen_positive = (symptom_count >= 7 and 
                          co_occurrence and 
                          moderate_impairment)
        
        return {
            'symptom_count': symptom_count,
            'symptom_count_interpretation': self._interpret_symptom_count(symptom_count),
            'co_occurrence': co_occurrence,
            'impairment_level': impairment_level,
            'moderate_or_serious_impairment': moderate_impairment,
            'screen_positive': screen_positive,
            'interpretation': self._interpret_screen(screen_positive, symptom_count, 
                                                     co_occurrence, moderate_impairment),
            'valid': True,
            'errors': []
        }
    
    def _interpret_symptom_count(self, count: int) -> str:
        """Interpret number of symptoms endorsed"""
        if count < 4:
            return "Peu de symptômes maniaques/hypomaniaques"
        elif count < 7:
            return "Nombre modéré de symptômes (< seuil de positivité)"
        elif count < 10:
            return "Nombre élevé de symptômes (≥ seuil de positivité)"
        else:
            return "Nombre très élevé de symptômes"
    
    def _interpret_screen(self, positive: bool, symptom_count: int, 
                         co_occurrence: bool, moderate_impairment: bool) -> str:
        """Provide detailed interpretation of screening result"""
        if positive:
            interpretation = ("Dépistage POSITIF pour un trouble bipolaire. "
                            "Le patient remplit tous les critères: "
                            f"≥7 symptômes ({symptom_count}/13), "
                            "co-occurrence durant la même période, "
                            "et impact fonctionnel modéré à sévère. "
                            "→ Évaluation psychiatrique complète recommandée.")
        else:
            reasons = []
            if symptom_count < 7:
                reasons.append(f"nombre de symptômes insuffisant ({symptom_count}/13, seuil=7)")
            if not co_occurrence:
                reasons.append("absence de co-occurrence durant la même période")
            if not moderate_impairment:
                reasons.append("impact fonctionnel insuffisant")
            
            interpretation = (f"Dépistage NÉGATIF pour un trouble bipolaire. "
                            f"Critères non remplis: {', '.join(reasons)}.")
        
        return interpretation


# Example usage
if __name__ == "__main__":
    questionnaire = MDQQuestionnaire()
    
    # Example 1: Positive screen (probable bipolar disorder)
    positive_example = {
        # High symptom count (9/13 yes)
        'rad_mdq_remonte': 'Oui',
        'rad_mdq_humeur': 'Oui',
        'rad_mdq_assurance': 'Oui',
        'rad_mdq_sommeil': 'Oui',
        'rad_mdq_parler': 'Oui',
        'rad_mdq_pensee': 'Oui',
        'rad_mdq_concentration': 'Non',
        'rad_mdq_energie': 'Oui',
        'rad_mdq_actif': 'Oui',
        'rad_mdq_sociale': 'Oui',
        'rad_mdq_sexe': 'Non',
        'rad_mdq_gens': 'Non',
        'rad_mdq_depense': 'Non',
        # Co-occurrence: Yes
        'rad_mdq2': 'Oui',
        # Serious functional impairment
        'rad_mdq3': 'Problème sérieux'
    }
    
    print("=== Exemple 1: Dépistage POSITIF ===\n")
    result = questionnaire.calculate_score(positive_example)
    print(f"Nombre de symptômes: {result['symptom_count']}/13")
    print(f"  → {result['symptom_count_interpretation']}")
    print(f"\nCo-occurrence: {'Oui' if result['co_occurrence'] else 'Non'}")
    print(f"Impact fonctionnel: {result['impairment_level']}")
    print(f"\nRésultat du dépistage: {'POSITIF' if result['screen_positive'] else 'NÉGATIF'}")
    print(f"\n{result['interpretation']}")
    
    print("\n" + "="*70 + "\n")
    
    # Example 2: Negative screen (insufficient symptoms)
    negative_example = {
        # Low symptom count (4/13 yes)
        'rad_mdq_remonte': 'Oui',
        'rad_mdq_humeur': 'Non',
        'rad_mdq_assurance': 'Oui',
        'rad_mdq_sommeil': 'Non',
        'rad_mdq_parler': 'Non',
        'rad_mdq_pensee': 'Non',
        'rad_mdq_concentration': 'Non',
        'rad_mdq_energie': 'Oui',
        'rad_mdq_actif': 'Oui',
        'rad_mdq_sociale': 'Non',
        'rad_mdq_sexe': 'Non',
        'rad_mdq_gens': 'Non',
        'rad_mdq_depense': 'Non',
        # Co-occurrence: Yes
        'rad_mdq2': 'Oui',
        # Moderate impairment
        'rad_mdq3': 'Problème modéré'
    }
    
    print("=== Exemple 2: Dépistage NÉGATIF ===\n")
    result2 = questionnaire.calculate_score(negative_example)
    print(f"Nombre de symptômes: {result2['symptom_count']}/13")
    print(f"  → {result2['symptom_count_interpretation']}")
    print(f"\nCo-occurrence: {'Oui' if result2['co_occurrence'] else 'Non'}")
    print(f"Impact fonctionnel: {result2['impairment_level']}")
    print(f"\nRésultat du dépistage: {'POSITIF' if result2['screen_positive'] else 'NÉGATIF'}")
    print(f"\n{result2['interpretation']}")

