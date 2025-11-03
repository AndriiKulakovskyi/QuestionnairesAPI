"""
Questionnaire: FAST (Functioning Assessment Short Test)
Test d'évaluation du fonctionnement
"""

from typing import Dict, List, Optional, Any


class FASTQuestionnaire:
    """FAST - Functioning Assessment Short Test
    
    Hétéro-évaluation du fonctionnement psychosocial en 24 items.
    Spécifiquement développé pour les troubles bipolaires.
    
    Développé par Rosa et al. (2007)
    
    6 domaines fonctionnels évalués (24 items total):
    1. Autonomie (4 items) - soins personnels, vie indépendante
    2. Activité professionnelle (5 items) - emploi, productivité
    3. Fonctionnement cognitif (5 items) - concentration, mémoire
    4. Finances (2 items) - gestion de l'argent
    5. Relations interpersonnelles (6 items) - famille, amis, sexualité
    6. Loisirs (2 items) - sports, hobbies
    
    Chaque item: 4 réponses (0-3 points)
    - 0 = Aucune difficulté
    - 1 = Difficulté légère
    - 2 = Difficulté modérée
    - 3 = Difficulté sévère
    
    Score total: 0-72 (plus élevé = plus de dysfonctionnement)
    Cutoff: ≥ 12 indique un dysfonctionnement fonctionnel significatif
    """
    
    def __init__(self):
        self.name = "FAST - Functioning Assessment Short Test"
        self.description = ("Évaluation du fonctionnement psychosocial en 24 items répartis en 6 domaines. "
                           "Spécifiquement conçu pour les troubles bipolaires.")
        self.used_in_applications = ["ebipolar", "eschizo", "cedr"]
        self.domains = self._init_domains()
        
    def get_instructions(self) -> str:
        """Return administration instructions"""
        return (
            "Consignes :\n"
            "Évaluer les difficultés rencontrées par le patient au cours des quinze derniers jours dans chaque "
            "situation décrite. Attribuer 0 lorsqu'aucune difficulté n'est observée, 1 pour une difficulté légère, 2 "
            "pour une difficulté modérée et 3 pour une difficulté sévère nécessitant de l'aide. Additionner les scores "
            "de chaque domaine pour obtenir les sous-scores, puis sommer l'ensemble pour obtenir le score total FAST. "
            "Un score total ≥ 12 indique un dysfonctionnement fonctionnel significatif."
        )

    def _init_domains(self) -> Dict[str, Dict[str, Any]]:
        """Initialize all 6 FAST domains with their items"""
        
        # Response options (same for all items)
        response_options = {
            "Aucune difficulté": 0,
            "Difficulté légère": 1,
            "Difficulté modérée": 2,
            "Difficulté sévère": 3
        }
        
        domains = {
            'autonomie': {
                'name': 'Autonomie',
                'score_field': 'fast_aut',
                'items': [
                    {
                        'id': 'rad_autonomie_responsabilite',
                        'text': "Prendre des responsabilités au sein de la maison",
                        'options': response_options
                    },
                    {
                        'id': 'rad_autonomie_seul',
                        'text': "Vivre seul(e)",
                        'options': response_options
                    },
                    {
                        'id': 'rad_autonomie_courses',
                        'text': "Faire les courses",
                        'options': response_options
                    },
                    {
                        'id': 'rad_autonomie_soin',
                        'text': "Prendre soin de soi (aspect physique, hygiène…)",
                        'options': response_options
                    }
                ]
            },
            'professionnelle': {
                'name': 'Activité Professionnelle',
                'score_field': 'fast_actprof',
                'items': [
                    {
                        'id': 'rad_professionnelle_emploi',
                        'text': "Avoir un emploi rémunéré",
                        'options': response_options
                    },
                    {
                        'id': 'rad_professionnelle_termine_tache',
                        'text': "Terminer les tâches le plus rapidement possible",
                        'options': response_options
                    },
                    {
                        'id': 'rad_professionnelle_correspond_formation',
                        'text': "Travailler dans le champ correspondant à votre formation",
                        'options': response_options
                    },
                    {
                        'id': 'rad_professionnelle_salaire_merite',
                        'text': "Recevoir le salaire que vous méritez",
                        'options': response_options
                    },
                    {
                        'id': 'rad_professionnelle_gestion_travail',
                        'text': "Gérer correctement la somme de travail",
                        'options': response_options
                    }
                ]
            },
            'cognitif': {
                'name': 'Fonctionnement Cognitif',
                'score_field': 'fast_cogn',
                'items': [
                    {
                        'id': 'rad_cognitif_livre',
                        'text': "Capacité à se concentrer devant un film, un livre",
                        'options': response_options
                    },
                    {
                        'id': 'rad_cognitif_calcul',
                        'text': "Capacité au calcul mental",
                        'options': response_options
                    },
                    {
                        'id': 'rad_cognitif_resoudre',
                        'text': "Capacité à résoudre des problèmes correctement",
                        'options': response_options
                    },
                    {
                        'id': 'rad_cognitif_nom',
                        'text': "Capacité à se souvenir des noms récemment appris",
                        'options': response_options
                    },
                    {
                        'id': 'rad_cognitif_apprendre',
                        'text': "Capacité à apprendre de nouvelles informations",
                        'options': response_options
                    }
                ]
            },
            'finances': {
                'name': 'Finances',
                'score_field': 'fast_fin',
                'items': [
                    {
                        'id': 'rad_finances_gestion',
                        'text': "Gérer votre propre argent",
                        'options': response_options
                    },
                    {
                        'id': 'rad_finances_depense',
                        'text': "Dépenser de façon équilibrée",
                        'options': response_options
                    }
                ]
            },
            'relations': {
                'name': 'Relations Interpersonnelles',
                'score_field': 'fast_int',
                'items': [
                    {
                        'id': 'rad_relations_conserve',
                        'text': "Conserver des amitiés",
                        'options': response_options
                    },
                    {
                        'id': 'rad_relations_participe',
                        'text': "Participer à des activités sociales",
                        'options': response_options
                    },
                    {
                        'id': 'rad_relations_bonnes',
                        'text': "Avoir de bonnes relations avec vos proches",
                        'options': response_options
                    },
                    {
                        'id': 'rad_relations_habiter',
                        'text': "Habiter avec votre famille",
                        'options': response_options
                    },
                    {
                        'id': 'rad_relations_sexualite',
                        'text': "Avoir des relations sexuelles satisfaisantes",
                        'options': response_options
                    },
                    {
                        'id': 'rad_relations_interet',
                        'text': "Être capable de défendre vos intérêts",
                        'options': response_options
                    }
                ]
            },
            'loisirs': {
                'name': 'Loisirs',
                'score_field': 'fast_lois',
                'items': [
                    {
                        'id': 'rad_loisirs_sport',
                        'text': "Faire de l'exercice ou pratiquer un sport",
                        'options': response_options
                    },
                    {
                        'id': 'rad_loisirs',
                        'text': "Avoir des loisirs",
                        'options': response_options
                    }
                ]
            }
        }
        
        return domains
    
    def get_all_items(self) -> List[Dict[str, Any]]:
        """Get flat list of all 24 items"""
        all_items = []
        for domain_key, domain in self.domains.items():
            for item in domain['items']:
                item_copy = item.copy()
                item_copy['domain'] = domain['name']
                item_copy['domain_key'] = domain_key
                all_items.append(item_copy)
        return all_items
    
    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """Calculate FAST scores
        
        Scoring: 
        - Each item scored 0-3 based on difficulty level
        - Domain scores: Sum of items in each domain
        - Total score: Sum of all 24 items (0-72)
        
        Interpretation:
        - 0-11: No significant functional impairment
        - ≥ 12: Significant functional impairment (cutoff validé)
        - Higher scores indicate greater functional disability
        
        Domain-specific interpretation:
        - Useful for identifying specific areas of difficulty
        - Guides targeted interventions
        
        Args:
            responses: Dictionary mapping item IDs to response strings
            
        Returns:
            Dictionary with total score, domain scores, and interpretation
        """
        errors = []
        all_items = self.get_all_items()
        
        # Validate all responses
        for item in all_items:
            item_id = item['id']
            if item_id not in responses:
                errors.append(f"Item manquant: {item['text'][:50]}...")
            elif responses[item_id] not in item['options']:
                errors.append(f"Réponse invalide pour: {item['text'][:50]}...")
        
        if errors:
            return {
                'valid': False,
                'errors': errors
            }
        
        # Calculate domain scores
        domain_scores = {}
        total_score = 0
        
        for domain_key, domain in self.domains.items():
            domain_score = 0
            domain_max = len(domain['items']) * 3
            
            for item in domain['items']:
                item_id = item['id']
                response = responses[item_id]
                score = item['options'][response]
                domain_score += score
            
            domain_scores[domain['name']] = {
                'score': domain_score,
                'max': domain_max,
                'percentage': (domain_score / domain_max * 100) if domain_max > 0 else 0
            }
            total_score += domain_score
        
        return {
            'total_score': total_score,
            'max_score': 72,
            'domain_scores': domain_scores,
            'interpretation': self._interpret_score(total_score, domain_scores),
            'functional_impairment': total_score >= 12,
            'valid': True,
            'errors': []
        }
    
    def _interpret_score(self, total: int, domains: Dict[str, Dict]) -> str:
        """Interpret FAST scores"""
        interpretation = []
        
        # Overall interpretation
        if total < 12:
            interpretation.append(
                f"Score total: {total}/72 - Pas de dysfonctionnement fonctionnel significatif"
            )
        elif total < 24:
            interpretation.append(
                f"Score total: {total}/72 - Dysfonctionnement fonctionnel léger"
            )
        elif total < 36:
            interpretation.append(
                f"Score total: {total}/72 - Dysfonctionnement fonctionnel modéré"
            )
        else:
            interpretation.append(
                f"Score total: {total}/72 - Dysfonctionnement fonctionnel sévère"
            )
        
        # Identify most impaired domains
        impaired_domains = []
        for domain_name, scores in domains.items():
            if scores['percentage'] >= 50:  # 50% or more of max score
                impaired_domains.append(f"{domain_name} ({scores['score']}/{scores['max']})")
        
        if impaired_domains:
            interpretation.append(
                f"\nDomaines les plus affectés: {', '.join(impaired_domains)}"
            )
        
        return "\n".join(interpretation)


# Example usage
if __name__ == "__main__":
    questionnaire = FASTQuestionnaire()
    
    print(f"=== {questionnaire.name} ===\n")
    print(f"{questionnaire.description}\n")
    print("=" * 70)
    
    # Example 1: No functional impairment
    print("\n📋 Exemple 1: Fonctionnement normal")
    responses_normal = {}
    for item in questionnaire.get_all_items():
        responses_normal[item['id']] = "Aucune difficulté"
    
    result = questionnaire.calculate_score(responses_normal)
    print(f"Score Total: {result['total_score']}/{result['max_score']}")
    print(f"Dysfonctionnement significatif: {'OUI' if result['functional_impairment'] else 'NON'}")
    print(f"\n{result['interpretation']}\n")
    
    # Example 2: Moderate functional impairment
    print("📋 Exemple 2: Dysfonctionnement modéré")
    responses_moderate = {}
    all_items = questionnaire.get_all_items()
    
    for i, item in enumerate(all_items):
        # Simulate mixed difficulties
        if i % 4 == 0:
            responses_moderate[item['id']] = "Difficulté modérée"
        elif i % 3 == 0:
            responses_moderate[item['id']] = "Difficulté légère"
        else:
            responses_moderate[item['id']] = "Aucune difficulté"
    
    result = questionnaire.calculate_score(responses_moderate)
    print(f"Score Total: {result['total_score']}/{result['max_score']}")
    print(f"Dysfonctionnement significatif: {'OUI' if result['functional_impairment'] else 'NON'}")
    print(f"\nScores par domaine:")
    for domain, scores in result['domain_scores'].items():
        print(f"  • {domain}: {scores['score']}/{scores['max']} ({scores['percentage']:.0f}%)")
    print(f"\n{result['interpretation']}\n")
    
    # Example 3: Severe functional impairment
    print("📋 Exemple 3: Dysfonctionnement sévère")
    responses_severe = {}
    for item in all_items:
        # Most items have severe difficulty
        if item['domain_key'] in ['cognitif', 'professionnelle', 'relations']:
            responses_severe[item['id']] = "Difficulté sévère"
        else:
            responses_severe[item['id']] = "Difficulté modérée"
    
    result = questionnaire.calculate_score(responses_severe)
    print(f"Score Total: {result['total_score']}/{result['max_score']}")
    print(f"Dysfonctionnement significatif: {'OUI' if result['functional_impairment'] else 'NON'}")
    print(f"\nScores par domaine:")
    for domain, scores in result['domain_scores'].items():
        print(f"  • {domain}: {scores['score']}/{scores['max']} ({scores['percentage']:.0f}%)")
    print(f"\n{result['interpretation']}\n")
    
    print("=" * 70)
    print("\n📊 Propriétés psychométriques:")
    print("   • Cohérence interne: α = 0.909")
    print("   • Test-retest: ICC = 0.98")
    print("   • Cutoff validé: ≥ 12")
    print("   • Sensibilité au changement: Oui")
    print("   • Temps d'administration: 5-10 minutes")

