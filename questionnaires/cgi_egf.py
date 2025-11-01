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
        errors = []
        result = {}
        
        # CGI-S (Severity)
        if 'radhtml_cgi_1' in responses:
            try:
                cgi_severity = int(responses['radhtml_cgi_1'])
                if cgi_severity < 0 or cgi_severity > 7:
                    errors.append("CGI-S doit être entre 0 et 7")
                else:
                    result['cgi_severity'] = cgi_severity
                    result['cgi_severity_interpretation'] = self._interpret_cgi_severity(cgi_severity)
            except (ValueError, TypeError):
                errors.append("CGI-S invalide")
        
        # EGF (Global Functioning)
        if 'egf_score' in responses:
            try:
                egf = int(responses['egf_score'])
                if egf < 1 or egf > 100:
                    errors.append("EGF doit être entre 1 et 100")
                else:
                    result['egf_score'] = egf
                    result['egf_interpretation'] = self._interpret_egf(egf)
            except (ValueError, TypeError):
                errors.append("EGF score invalide")
        
        # CGI-I (Improvement)
        if 'radhtml_cgi_2' in responses:
            try:
                cgi_improvement = int(responses['radhtml_cgi_2'])
                if cgi_improvement < 0 or cgi_improvement > 7:
                    errors.append("CGI-I doit être entre 0 et 7")
                else:
                    result['cgi_improvement'] = cgi_improvement
                    result['cgi_improvement_interpretation'] = self._interpret_cgi_improvement(cgi_improvement)
            except (ValueError, TypeError):
                errors.append("CGI-I invalide")
        
        # CGI Therapeutic Index
        if ('rad_cgi_3_effet_therapeutique' in responses and 
            'rad_cgi_3_effet_secondaire' in responses):
            therapeutic_effect = responses['rad_cgi_3_effet_therapeutique']
            side_effects = responses['rad_cgi_3_effet_secondaire']
            result['therapeutic_index'] = self._calculate_therapeutic_index(
                therapeutic_effect, side_effects
            )
        
        result['valid'] = len(errors) == 0
        result['errors'] = errors
        
        return result
    
    def _interpret_cgi_severity(self, score: int) -> str:
        """Interpret CGI-S severity score"""
        interpretations = {
            0: "Non évalué",
            1: "Normal, pas du tout malade",
            2: "À la limite",
            3: "Légèrement malade",
            4: "Modérément malade",
            5: "Manifestement malade",
            6: "Gravement malade",
            7: "Parmi les patients les plus malades"
        }
        return interpretations.get(score, "Score invalide")
    
    def _interpret_egf(self, score: int) -> str:
        """Interpret EGF (Global Functioning) score"""
        if score >= 81:
            return "90-81: Symptômes absents ou minimes, fonctionnement satisfaisant"
        elif score >= 71:
            return "80-71: Symptômes transitoires, handicap léger"
        elif score >= 61:
            return "70-61: Quelques symptômes légers ou difficultés légères"
        elif score >= 51:
            return "60-51: Symptômes d'intensité moyenne ou difficultés moyennes"
        elif score >= 41:
            return "50-41: Symptômes importants ou handicap important"
        elif score >= 31:
            return "40-31: Altération de la réalité ou handicap majeur"
        elif score >= 21:
            return "30-21: Troubles graves de la communication ou du jugement"
        elif score >= 11:
            return "20-11: Danger d'auto/hétéro-agression ou incapacité d'hygiène"
        else:
            return "10-1: Danger persistant grave"
    
    def _interpret_cgi_improvement(self, score: int) -> str:
        """Interpret CGI-I improvement score"""
        interpretations = {
            0: "Non évalué",
            1: "Très fortement amélioré",
            2: "Fortement amélioré",
            3: "Légèrement amélioré",
            4: "Pas de changement",
            5: "Légèrement aggravé",
            6: "Fortement aggravé",
            7: "Très fortement aggravé"
        }
        return interpretations.get(score, "Score invalide")
    
    def _calculate_therapeutic_index(self, therapeutic_effect: str, side_effects: str) -> Dict[str, Any]:
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
        # Therapeutic effect scoring
        effect_scores = {
            "Non évalué": 0,
            "Important": 3,
            "Modéré": 2,
            "Minime": 1,
            "Nul ou aggravation": 0
        }
        
        # Side effect scoring (higher = worse)
        side_effect_scores = {
            "Aucun": 0,
            "N'interfèrent pas significativement avec le fonctionnement du patient": 1,
            "Interfèrent significativement avec le fonctionnement du patient": 2,
            "Dépassent l'effet thérapeutique": 3
        }
        
        effect = effect_scores.get(therapeutic_effect, 0)
        side_fx = side_effect_scores.get(side_effects, 0)
        
        # Generate interpretation
        if effect == 0:
            interpretation = "Non évalué ou traitement inefficace"
        elif effect == 3 and side_fx == 0:
            interpretation = "Traitement optimal: effet important sans effets secondaires"
        elif effect >= 2 and side_fx <= 1:
            interpretation = "Traitement favorable: bon rapport bénéfice/risque"
        elif side_fx >= effect:
            interpretation = "Traitement problématique: effets secondaires ≥ bénéfice thérapeutique"
        else:
            interpretation = "Traitement acceptable avec effets secondaires modérés"
        
        return {
            'therapeutic_effect': effect,
            'side_effects': side_fx,
            'interpretation': interpretation
        }


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

