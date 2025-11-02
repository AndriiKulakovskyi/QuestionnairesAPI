"""
Questionnaire: CGI-EGF (Clinical Global Impression - Echelle Globale de Fonctionnement)
Impressions Cliniques Globales + Échelle de Fonctionnement Global
"""

from typing import Dict, List, Optional, Any


class CGIEGFQuestionnaire:
    """CGI-EGF - Clinical Global Impression + Global Functioning Scale
    
    Hétéro-évaluation clinique comprenant :
    - CGI-S (Severity): Gravité de la maladie (0-7)
    - EGF (GAF): Echelle de Fonctionnement Global (1-100)
    - CGI-I (Improvement): Amélioration globale (0-7)
    - CGI-Index thérapeutique: Effet thérapeutique vs effets secondaires
    """
    
    def __init__(self):
        self.name = "CGI-EGF - Clinical Global Impression + Échelle de Fonctionnement Global"
        self.description = ("Évaluation clinique globale comprenant la gravité de la maladie (CGI-S), "
                           "l'amélioration (CGI-I), le fonctionnement global (EGF) et l'index thérapeutique.")
        self.used_in_applications = ["ebipolar", "eschizo"]
        self.severity_scale = {
            0: "Non évalué",
            1: "Normal, pas du tout malade",
            2: "À la limite",
            3: "Légèrement malade",
            4: "Modérément malade",
            5: "Manifestement malade",
            6: "Gravement malade",
            7: "Parmi les patients les plus malades"
        }
        self.improvement_scale = {
            0: "Non évalué",
            1: "Très fortement amélioré",
            2: "Fortement amélioré",
            3: "Légèrement amélioré",
            4: "Pas de changement",
            5: "Légèrement aggravé",
            6: "Fortement aggravé",
            7: "Très fortement aggravé"
        }
        self.therapeutic_effect_labels = [
            "Non évalué",
            "Important",
            "Modéré",
            "Minime",
            "Nul ou aggravation"
        ]
        self.side_effect_labels = [
            "Aucun",
            "N'interfèrent pas significativement avec le fonctionnement du patient",
            "Interfèrent significativement avec le fonctionnement du patient",
            "Dépassent l'effet thérapeutique"
        ]
        self.therapeutic_index_matrix = {
            "Important": {self.side_effect_labels[0]: 1, self.side_effect_labels[1]: 2,
                           self.side_effect_labels[2]: 3, self.side_effect_labels[3]: 4},
            "Modéré": {self.side_effect_labels[0]: 5, self.side_effect_labels[1]: 6,
                        self.side_effect_labels[2]: 7, self.side_effect_labels[3]: 8},
            "Minime": {self.side_effect_labels[0]: 9, self.side_effect_labels[1]: 10,
                        self.side_effect_labels[2]: 11, self.side_effect_labels[3]: 12},
            "Nul ou aggravation": {self.side_effect_labels[0]: 13, self.side_effect_labels[1]: 14,
                                     self.side_effect_labels[2]: 15, self.side_effect_labels[3]: 16}
        }
        
    def calculate_score(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate CGI-EGF scores
        
        Components:
        1. CGI-S (Severity): radhtml_cgi_1 (0-7)
           0 = Non évalué
           1 = Normal, pas du tout malade
           2 = À la limite
           3 = Légèrement malade
           4 = Modérément malade
           5 = Manifestement malade
           6 = Gravement malade
           7 = Parmi les patients les plus malades
        
        2. EGF (Global Functioning): egf_score (1-100)
           Similar to GAF (Global Assessment of Functioning)
           90-81: Symptômes absents/minimes
           80-71: Symptômes transitoires
           70-61: Quelques symptômes légers
           60-51: Symptômes d'intensité moyenne
           50-41: Symptômes importants
           40-31: Altération de la réalité
           30-21: Troubles graves
           20-11: Danger pour soi/autrui
           10-1: Danger persistant
        
        3. CGI-I (Improvement): radhtml_cgi_2 (0-7)
           0 = Non évalué
           1 = Très fortement amélioré
           2 = Fortement amélioré
           3 = Légèrement amélioré
           4 = Pas de changement
           5 = Légèrement aggravé
           6 = Fortement aggravé
           7 = Très fortement aggravé
        
        4. CGI Therapeutic Index: Combination of therapeutic effect and side effects
        
        Args:
            responses: Dictionary with 'radhtml_cgi_1', 'egf_score', 'radhtml_cgi_2', etc.
            
        Returns:
            Dictionary with individual scores and interpretations
        """
        errors: List[str] = []
        result: Dict[str, Any] = {}
        
        # CGI-S (Severity)
        if 'radhtml_cgi_1' not in responses:
            errors.append("CGI-S manquant (radhtml_cgi_1)")
            cgi_severity = None
        else:
            try:
                cgi_severity = int(responses['radhtml_cgi_1'])
                if cgi_severity < 0 or cgi_severity > 7:
                    errors.append("CGI-S doit être compris entre 0 et 7")
                else:
                    result['cgi_severity'] = cgi_severity
                    result['cgi_severity_interpretation'] = self._interpret_cgi_severity(cgi_severity)
            except (ValueError, TypeError):
                errors.append("CGI-S invalide (valeur numérique attendue)")
                cgi_severity = None

        # EGF (Global Functioning) - optional but validated if present
        if 'egf_score' in responses and responses['egf_score'] not in (None, ""):
            try:
                egf = int(responses['egf_score'])
                if egf < 1 or egf > 100:
                    errors.append("EGF doit être compris entre 1 et 100")
                else:
                    result['egf_score'] = egf
                    result['egf_interpretation'] = self._interpret_egf(egf)
            except (ValueError, TypeError):
                errors.append("EGF invalide (valeur numérique attendue)")

        # CGI-I (Improvement) - optional but validated if present
        if 'radhtml_cgi_2' in responses and responses['radhtml_cgi_2'] not in (None, ""):
            try:
                cgi_improvement = int(responses['radhtml_cgi_2'])
                if cgi_improvement < 0 or cgi_improvement > 7:
                    errors.append("CGI-I doit être compris entre 0 et 7")
                else:
                    result['cgi_improvement'] = cgi_improvement
                    result['cgi_improvement_interpretation'] = self._interpret_cgi_improvement(cgi_improvement)
            except (ValueError, TypeError):
                errors.append("CGI-I invalide (valeur numérique attendue)")

        # CGI Therapeutic Index - requires both inputs
        effect = responses.get('rad_cgi_3_effet_therapeutique')
        side = responses.get('rad_cgi_3_effet_secondaire')
        if effect or side:
            therapeutic_index = self._calculate_therapeutic_index(effect, side, errors)
            if therapeutic_index is not None:
                result['therapeutic_index'] = therapeutic_index

        result['valid'] = len(errors) == 0
        result['errors'] = errors
        
        return result
    
    def _interpret_cgi_severity(self, score: int) -> str:
        """Interpret CGI-S severity score"""
        return self.severity_scale.get(score, "Score invalide")
    
    def _interpret_egf(self, score: int) -> str:
        """Interpret EGF (Global Functioning) score"""
        if score >= 91:
            return ("100-91 : Niveau supérieur de fonctionnement dans une grande variété d'activités, "
                    "jamais débordé, recherché pour ses qualités, absence de symptômes")
        elif score >= 81:
            return ("90-81 : Symptômes absents ou minimes, fonctionnement satisfaisant dans tous les domaines, "
                    "intégré socialement, préoccupations limitées aux soucis du quotidien")
        elif score >= 71:
            return ("80-71 : Symptômes transitoires et prévisibles face au stress, handicap au plus léger dans le "
                    "fonctionnement social, professionnel ou scolaire")
        elif score >= 61:
            return ("70-61 : Quelques symptômes légers ou difficultés dans le fonctionnement social, professionnel "
                    "ou scolaire mais maintien de relations positives")
        elif score >= 51:
            return ("60-51 : Symptômes d'intensité moyenne ou difficultés moyennes dans le fonctionnement social, "
                    "professionnel ou scolaire")
        elif score >= 41:
            return ("50-41 : Symptômes importants ou handicap notable dans le fonctionnement social, professionnel "
                    "ou scolaire")
        elif score >= 31:
            return ("40-31 : Altération du sens de la réalité ou handicap majeur dans plusieurs domaines "
                    "(travail, relations familiales, jugement, humeur)")
        elif score >= 21:
            return ("30-21 : Comportement influencé par des idées délirantes/hallucinations ou incapacité à "
                    "fonctionner dans tous les domaines")
        elif score >= 11:
            return ("20-11 : Danger d'auto/hétéro-agression, incapacité temporaire d'hygiène ou altération massive "
                    "de la communication")
        else:
            return ("10-1 : Danger persistant d'hétéro-agression grave, incapacité durable d'hygiène ou geste "
                    "suicidaire avec attente précise de la mort")
    
    def _interpret_cgi_improvement(self, score: int) -> str:
        """Interpret CGI-I improvement score"""
        return self.improvement_scale.get(score, "Score invalide")

    def _calculate_therapeutic_index(self, therapeutic_effect: Optional[str],
                                     side_effects: Optional[str], errors: List[str]) -> Optional[Dict[str, Any]]:
        """Calculate CGI therapeutic index
        
        Combines therapeutic effect rating with side effect rating
        to provide overall treatment benefit assessment.
        
        Args:
            therapeutic_effect: One of 'Non évalué', 'Important', 'Modéré', 'Minime', 'Nul ou aggravation'
            side_effects: One of 'Aucun', 'N''interfèrent pas significativement...', 
                          'Interfèrent significativement...', 'Dépassent l''effet thérapeutique'
        
        Returns:
            Dictionary with therapeutic index score and interpretation
        """
        if therapeutic_effect in (None, "") and side_effects in (None, ""):
            return None

        if therapeutic_effect not in self.therapeutic_effect_labels:
            errors.append("Effet thérapeutique invalide pour l'index CGI")
            return None

        if side_effects not in self.side_effect_labels:
            errors.append("Effets secondaires invalides pour l'index CGI")
            return None

        if therapeutic_effect == "Non évalué":
            return {
                'effect_label': therapeutic_effect,
                'side_effects_label': side_effects,
                'index_value': None,
                'interpretation': "Index non évalué"
            }

        index_value = self.therapeutic_index_matrix[therapeutic_effect][side_effects]

        if index_value <= 2:
            interpretation = "Traitement optimal : effet important avec effets secondaires minimes"
        elif index_value <= 6:
            interpretation = "Traitement favorable : bon rapport bénéfice/risque"
        elif index_value <= 8:
            interpretation = "Traitement acceptable avec effets secondaires modérés"
        elif index_value <= 12:
            interpretation = "Effets secondaires notables nécessitant une surveillance"
        else:
            interpretation = "Traitement problématique : effets secondaires > bénéfice"

        return {
            'effect_label': therapeutic_effect,
            'side_effects_label': side_effects,
            'index_value': index_value,
            'interpretation': interpretation
        }

    def get_instructions(self) -> str:
        """Return consolidated CGI-EGF instructions"""
        severity_text = (
            "CGI - 1ère partie\n"
            "Instruction : Compléter l'item (gravité de la maladie) lors de l'évaluation initiale et des visites de suivi. "
            "Les items 2 et 3 sont omis lors de l'évaluation initiale en cochant 0 (non évalué).\n"
            "Gravité de la maladie : En fonction de votre expérience clinique totale avec ce type de patient, quel est le niveau de gravité des troubles mentaux actuels du patient ?"
        )
        improvement_text = (
            "\nCGI - 2ème partie (visites de suivi)\n"
            "Amélioration globale : Évaluer l'amélioration totale, qu'elle soit ou non due entièrement au traitement. Comparé au début du traitement, de quelle façon le patient a-t-il changé ?"
        )
        therapeutic_text = (
            "\nIndex thérapeutique : Évaluer uniquement l'effet du médicament. Choisir la combinaison décrivant le mieux l'efficacité thérapeutique et les effets secondaires (matrice 1-16)."
        )
        egf_text = (
            "\nEGF - Consignes : Évaluer le fonctionnement psychologique, social et professionnel sur un continuum allant de la santé mentale à la maladie. "
            "Ne pas tenir compte des limitations physiques ou environnementales. Utiliser des valeurs intermédiaires si nécessaire (p. ex. 45, 68, 72)."
        )
        return severity_text + improvement_text + therapeutic_text + egf_text


# Example usage
if __name__ == "__main__":
    questionnaire = CGIEGFQuestionnaire()
    
    # Example: Patient with moderate illness, showing improvement
    example_responses = {
        'radhtml_cgi_1': "4",  # Modérément malade
        'egf_score': "58",     # Symptômes d'intensité moyenne
        'radhtml_cgi_2': "3",  # Légèrement amélioré
        'rad_cgi_3_effet_therapeutique': "Modéré",
        'rad_cgi_3_effet_secondaire': "N'interfèrent pas significativement avec le fonctionnement du patient"
    }
    
    result = questionnaire.calculate_score(example_responses)
    
    print(f"CGI-S (Gravité): {result.get('cgi_severity')}/7")
    print(f"  → {result.get('cgi_severity_interpretation')}")
    print(f"\nEGF (Fonctionnement): {result.get('egf_score')}/100")
    print(f"  → {result.get('egf_interpretation')}")
    print(f"\nCGI-I (Amélioration): {result.get('cgi_improvement')}/7")
    print(f"  → {result.get('cgi_improvement_interpretation')}")
    print(f"\nIndex thérapeutique:")
    print(f"  → {result['therapeutic_index']['interpretation']}")

