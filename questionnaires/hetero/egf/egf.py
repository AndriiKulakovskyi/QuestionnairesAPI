"""
EGF (GAF) - Global Assessment of Functioning

This module implements the Global Assessment of Functioning scale (GAF), known in French
as Échelle d'Évaluation Globale du Fonctionnement (EGF). It's a single-item clinician-rated
measure of overall functioning on a 0-100 continuum.

The GAF/EGF is one of the most widely used global outcome measures in psychiatry,
providing a quick assessment of psychological, social, and occupational functioning.
"""

from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime


class EGFError(Exception):
    """Custom exception for EGF scale errors."""
    pass


class EGF:
    """
    EGF (GAF) - Global Assessment of Functioning
    
    A single-item clinician-rated scale that provides a global assessment of
    psychological, social, and occupational functioning on a 0-100 continuum.
    
    Key principles:
    - Rate current functioning at time of evaluation
    - Consider psychological, social, and occupational functioning
    - Do NOT include impairment from physical or environmental limitations
    - Use intermediate codes (e.g., 45, 68, 72) for precision
    - Higher scores indicate better functioning
    
    Score ranges are typically grouped into 10-point bands with distinct
    clinical interpretations.
    
    Attributes:
        id: Unique identifier for the scale
        name: Full name in French
        abbreviation: Short form (EGF/GAF)
        language: Language code
        version: Version number
        reference_period: Time frame for assessment
        description: Brief description of the scale
    """
    
    # Score bands with clinical descriptions
    BANDS = {
        "91-100": "Functioning supérieur",
        "81-90": "Symptômes absents ou minimes",
        "71-80": "Symptômes transitoires",
        "61-70": "Symptômes légers",
        "51-60": "Symptômes modérés",
        "41-50": "Symptômes graves",
        "31-40": "Altération importante",
        "21-30": "Altération majeure",
        "11-20": "Danger ou incapacité majeure",
        "1-10": "Danger persistant",
        "0": "Information inadéquate"
    }
    
    def __init__(self):
        """Initialize the EGF scale."""
        self.id = "EGF.fr"
        self.name = "Échelle d'Évaluation Globale du Fonctionnement (EGF) – GAF"
        self.abbreviation = "EGF (GAF)"
        self.language = "fr-FR"
        self.version = "1.0"
        self.reference_period = "Fonctionnement actuel (au moment de l'évaluation)"
        self.description = (
            "Notation unique 0–100 du fonctionnement psychologique, social et "
            "professionnel, hors limitations physiques/environnementales."
        )
    
    def get_metadata(self) -> Dict[str, Any]:
        """
        Get scale metadata.
        
        Returns:
            Dictionary containing scale metadata
        """
        return {
            "id": self.id,
            "name": self.name,
            "abbreviation": self.abbreviation,
            "language": self.language,
            "version": self.version,
            "reference_period": self.reference_period,
            "description": self.description,
            "num_items": 1,
            "response_scale": "0-100 continuous integer scale",
            "score_range": [0, 100],
            "intermediate_codes_allowed": True,
            "bands": list(self.BANDS.keys()),
            "clinical_note": (
                "Évaluer le fonctionnement psychologique, social et professionnel. "
                "Ne pas tenir compte des limitations physiques ou environnementales."
            )
        }
    
    def get_questions(self) -> List[Dict[str, Any]]:
        """
        Get scale items.
        
        Returns:
            List containing the single EGF question
        """
        return [
            {
                "id": "egf_score",
                "section_id": "sec1",
                "text": "Score EGF / GAF (0–100)",
                "description": (
                    "Évaluer le fonctionnement global du patient sur un continuum de 0 à 100. "
                    "Codes intermédiaires possibles (p. ex. 45, 68, 72)."
                ),
                "type": "integer",
                "required": True,
                "constraints": {
                    "value_type": "integer",
                    "min_value": 0,
                    "max_value": 100
                },
                "guidelines": [
                    "Considérer le fonctionnement psychologique, social et professionnel",
                    "Ne PAS inclure les limitations dues à des facteurs physiques ou environnementaux",
                    "Utiliser le niveau de fonctionnement le plus bas de la période d'évaluation",
                    "Les codes intermédiaires sont autorisés et encouragés pour la précision",
                    "En cas de doute entre deux valeurs, choisir la plus basse"
                ],
                "band_descriptions": self._get_band_descriptions()
            }
        ]
    
    def get_sections(self) -> List[Dict[str, Any]]:
        """
        Get scale sections.
        
        Returns:
            List containing the single section
        """
        return [
            {
                "id": "sec1",
                "label": "Évaluation globale",
                "description": "Coter le niveau de fonctionnement (0–100)",
                "question_ids": ["egf_score"]
            }
        ]
    
    def _get_band_descriptions(self) -> List[Dict[str, str]]:
        """Get detailed descriptions for each 10-point band."""
        return [
            {
                "range": "91-100",
                "label": "Fonctionnement supérieur",
                "description": (
                    "Fonctionnement supérieur dans une grande variété d'activités. "
                    "Aucun symptôme. Recherché par les autres en raison de ses qualités positives."
                )
            },
            {
                "range": "81-90",
                "label": "Symptômes absents ou minimes",
                "description": (
                    "Symptômes absents ou minimes (p. ex. anxiété légère avant un examen). "
                    "Fonctionnement satisfaisant dans tous les domaines. Socialement efficace."
                )
            },
            {
                "range": "71-80",
                "label": "Symptômes transitoires",
                "description": (
                    "Symptômes transitoires et réactions prévisibles à des facteurs de stress. "
                    "Difficultés légères dans le fonctionnement social, professionnel ou scolaire."
                )
            },
            {
                "range": "61-70",
                "label": "Symptômes légers",
                "description": (
                    "Quelques symptômes légers OU difficultés dans le fonctionnement social, "
                    "professionnel ou scolaire, mais fonctionnement assez bon dans l'ensemble."
                )
            },
            {
                "range": "51-60",
                "label": "Symptômes modérés",
                "description": (
                    "Symptômes modérés (p. ex. affect aplati, discours circonstanciel, "
                    "attaques de panique occasionnelles) OU difficultés modérées dans le "
                    "fonctionnement social, professionnel ou scolaire."
                )
            },
            {
                "range": "41-50",
                "label": "Symptômes graves",
                "description": (
                    "Symptômes graves (p. ex. idéation suicidaire, rituels obsessionnels sévères, "
                    "vols à l'étalage fréquents) OU altération grave du fonctionnement social, "
                    "professionnel ou scolaire."
                )
            },
            {
                "range": "31-40",
                "label": "Altération importante",
                "description": (
                    "Altération importante dans plusieurs domaines : travail, relations familiales, "
                    "jugement, pensée ou humeur (p. ex. homme déprimé évite ses amis, néglige sa "
                    "famille, incapable de travailler)."
                )
            },
            {
                "range": "21-30",
                "label": "Altération majeure",
                "description": (
                    "Le comportement est considérablement influencé par des idées délirantes ou "
                    "hallucinations OU altération majeure dans plusieurs domaines (travail, "
                    "relations familiales, jugement, pensée ou humeur)."
                )
            },
            {
                "range": "11-20",
                "label": "Danger ou incapacité majeure",
                "description": (
                    "Danger de se blesser ou de blesser autrui (p. ex. tentatives de suicide, "
                    "violence fréquente) OU incapacité occasionnelle à maintenir l'hygiène "
                    "corporelle minimale OU altération massive de la communication."
                )
            },
            {
                "range": "1-10",
                "label": "Danger persistant",
                "description": (
                    "Danger persistant de se blesser gravement soi-même ou autrui OU incapacité "
                    "persistante à maintenir l'hygiène corporelle minimale OU geste suicidaire "
                    "grave avec expectation claire de la mort."
                )
            },
            {
                "range": "0",
                "label": "Information inadéquate",
                "description": "Information inadéquate pour évaluer le fonctionnement."
            }
        ]
    
    def validate_answers(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Validate EGF answers from dictionary format.
        
        Args:
            answers: Dictionary mapping question IDs to response values
        
        Returns:
            Dictionary containing validation results with 'valid', 'errors', and 'warnings' keys
        """
        errors = []
        warnings = []
        
        # Check if egf_score is present
        if "egf_score" not in answers:
            errors.append("Item manquant: egf_score")
            return {"valid": False, "errors": errors, "warnings": warnings}
        
        score = answers["egf_score"]
        
        # Validate the score using existing method
        validation = self.validate_score(score)
        
        return validation
    
    def validate_score(self, score: int) -> Dict[str, Any]:
        """
        Validate EGF score.
        
        Args:
            score: EGF score value
        
        Returns:
            Dictionary containing validation results with 'valid', 'errors', and 'warnings' keys
        """
        errors = []
        warnings = []
        
        # Type validation
        if not isinstance(score, int):
            errors.append(f"Le score doit être un entier (reçu: {type(score).__name__})")
            return {"valid": False, "errors": errors, "warnings": warnings}
        
        # Range validation
        if score < 0 or score > 100:
            errors.append(f"Le score doit être entre 0 et 100 (reçu: {score})")
        
        # Clinical warnings based on score
        if not errors:
            if score == 0:
                warnings.append(
                    "Score = 0 indique une information inadéquate. "
                    "Assurer une évaluation complète si possible."
                )
            elif score <= 10:
                warnings.append(
                    "ALERTE CRITIQUE: Danger persistant (score 1-10). "
                    "Risque suicidaire ou d'auto/hétéro-agression élevé. "
                    "Surveillance constante et hospitalisation généralement nécessaires."
                )
            elif score <= 20:
                warnings.append(
                    "ALERTE URGENTE: Altération massive (score 11-20). "
                    "Danger potentiel. Hospitalisation fortement recommandée."
                )
            elif score <= 30:
                warnings.append(
                    "SÉVÈRE: Altération majeure (score 21-30). "
                    "Fonctionnement gravement compromis. Traitement intensif nécessaire."
                )
            elif score <= 40:
                warnings.append(
                    "GRAVE: Altération importante (score 31-40). "
                    "Fonctionnement sérieusement compromis dans plusieurs domaines. "
                    "Traitement actif recommandé."
                )
            elif score <= 50:
                warnings.append(
                    "MODÉRÉ À GRAVE: Symptômes graves (score 41-50). "
                    "Altération significative nécessitant traitement structuré."
                )
            elif score <= 60:
                warnings.append(
                    "MODÉRÉ: Symptômes ou difficultés modérés (score 51-60). "
                    "Traitement recommandé."
                )
            elif score <= 70:
                warnings.append(
                    "LÉGER: Symptômes légers (score 61-70). "
                    "Fonctionnement globalement satisfaisant avec quelques difficultés."
                )
            # Scores 71+ are generally good functioning, no warnings needed
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def get_band(self, score: int) -> str:
        """
        Get the 10-point band for a given score.
        
        Args:
            score: EGF score (0-100)
        
        Returns:
            Band label as string (e.g., "61-70", "91-100", "0")
        
        Raises:
            EGFError: If score is out of range
        """
        if score < 0 or score > 100:
            raise EGFError(f"Le score doit être entre 0 et 100 (reçu: {score})")
        
        if score == 0:
            return "0"
        elif score <= 10:
            return "1-10"
        elif score <= 20:
            return "11-20"
        elif score <= 30:
            return "21-30"
        elif score <= 40:
            return "31-40"
        elif score <= 50:
            return "41-50"
        elif score <= 60:
            return "51-60"
        elif score <= 70:
            return "61-70"
        elif score <= 80:
            return "71-80"
        elif score <= 90:
            return "81-90"
        else:  # score >= 91
            return "91-100"
    
    def calculate_score(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Calculate and interpret EGF score.
        
        Args:
            answers: Dictionary mapping question IDs to response values (expects 'egf_score' key)
        
        Returns:
            Dictionary containing:
                - score: The input score
                - band: 10-point band classification
                - band_label: Clinical label for the band
                - severity: Severity category
                - interpretation: Detailed clinical interpretation
                - warnings: List of clinical warnings
        
        Raises:
            EGFError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation["valid"]:
            raise EGFError(f"Validation échouée: {'; '.join(validation['errors'])}")
        
        # Extract score from answers
        score = answers["egf_score"]
        
        # Get band
        band = self.get_band(score)
        band_label = self.BANDS.get(band, "Unknown")
        
        # Determine severity
        severity = self._get_severity(score)
        
        # Generate interpretation
        interpretation = self._generate_interpretation(score, band, band_label, severity)
        
        return {
            "score": score,
            "band": band,
            "band_label": band_label,
            "severity": severity,
            "interpretation": interpretation,
            "warnings": validation["warnings"],
            "calculation_date": datetime.utcnow().isoformat() + "Z"
        }
    
    def _get_severity(self, score: int) -> str:
        """Get severity category based on score."""
        if score == 0:
            return "Non évalué"
        elif score <= 20:
            return "Extrêmement sévère"
        elif score <= 40:
            return "Sévère"
        elif score <= 60:
            return "Modéré"
        elif score <= 70:
            return "Léger"
        elif score <= 80:
            return "Minimal"
        else:  # score > 80
            return "Excellent/Bon"
    
    def _generate_interpretation(
        self,
        score: int,
        band: str,
        band_label: str,
        severity: str
    ) -> str:
        """Generate detailed clinical interpretation."""
        interpretation = "=== ÉCHELLE D'ÉVALUATION GLOBALE DU FONCTIONNEMENT (EGF/GAF) ===\n\n"
        
        interpretation += f"Score: {score}/100\n"
        interpretation += f"Bande: {band}\n"
        interpretation += f"Catégorie: {band_label}\n"
        interpretation += f"Sévérité: {severity}\n\n"
        
        # Detailed interpretation by band
        if score == 0:
            interpretation += (
                "=== INFORMATION INADÉQUATE ===\n"
                "Le score de 0 indique que l'information disponible est insuffisante pour "
                "évaluer le niveau de fonctionnement du patient.\n\n"
                "Actions recommandées:\n"
                "• Obtenir plus d'informations sur le fonctionnement actuel\n"
                "• Consulter les proches, dossiers médicaux antérieurs\n"
                "• Réévaluer dès que possible avec information adéquate\n"
            )
        elif score <= 10:
            interpretation += (
                "DANGER PERSISTANT - URGENCE MAXIMALE\n\n"
                "Le patient présente un danger persistant grave de se blesser ou de blesser "
                "autrui, OU une incapacité persistante à maintenir l'hygiène corporelle minimale.\n\n"
                "Signes cliniques typiques:\n"
                "• Gestes suicidaires graves avec expectation claire de mort\n"
                "• Violence grave et récurrente envers autrui\n"
                "• Incapacité totale d'auto-soins (hygiène, alimentation)\n"
                "• Désorganisation psychotique massive\n"
                "• Risque imminent pour soi-même ou autrui\n\n"
                "Actions URGENTES requises:\n"
                "• HOSPITALISATION IMMÉDIATE (généralement involontaire)\n"
                "• Surveillance constante (1:1) 24h/24\n"
                "• Évaluation psychiatrique urgente\n"
                "• Mesures de protection (retrait objets dangereux, chambre sécurisée)\n"
                "• Traitement pharmacologique intensif\n"
                "• Notification de la famille/proches\n"
                "• Documentation médico-légale complète\n"
            )
        elif score <= 20:
            interpretation += (
                "ALTÉRATION MASSIVE - DANGER IMMINENT\n\n"
                "Le patient présente un danger potentiel de se blesser ou de blesser autrui, "
                "OU une incapacité occasionnelle à maintenir l'hygiène minimale, OU une "
                "altération massive de la communication.\n\n"
                "Signes cliniques typiques:\n"
                "• Tentatives de suicide ou menaces sérieuses\n"
                "• Violence fréquente, agressivité non contrôlée\n"
                "• Négligence grave de l'hygiène personnelle\n"
                "• Communication gravement altérée (mutisme, incohérence totale)\n"
                "• Isolement social complet\n\n"
                "Actions URGENTES requises:\n"
                "• HOSPITALISATION FORTEMENT RECOMMANDÉE\n"
                "• Évaluation du risque suicidaire/agressif\n"
                "• Surveillance rapprochée\n"
                "• Traitement psychiatrique intensif\n"
                "• Support infirmier pour soins de base\n"
                "• Plan de sécurité détaillé\n"
            )
        elif score <= 30:
            interpretation += (
                "ALTÉRATION MAJEURE - INTERVENTION INTENSIVE NÉCESSAIRE\n\n"
                "Le comportement est considérablement influencé par des idées délirantes ou "
                "hallucinations, OU altération majeure dans plusieurs domaines.\n\n"
                "Signes cliniques typiques:\n"
                "• Délires ou hallucinations influençant fortement le comportement\n"
                "• Incapacité de maintenir un emploi ou études\n"
                "• Rupture des relations familiales et sociales\n"
                "• Jugement et pensée gravement altérés\n"
                "• Troubles de l'humeur sévères et envahissants\n\n"
                "Actions recommandées:\n"
                "• Traitement psychiatrique intensif (souvent hospitalisation)\n"
                "• Médication antipsychotique ou thymorégulatrice\n"
                "• Suivi quotidien ou bihebdomadaire\n"
                "• Programme de jour ou hospitalisation partielle\n"
                "• Support social et familial structuré\n"
                "• Évaluation des besoins en termes de logement/ressources\n"
            )
        elif score <= 40:
            interpretation += (
                "ALTÉRATION IMPORTANTE - TRAITEMENT ACTIF REQUIS\n\n"
                "Altération importante dans plusieurs domaines : travail, relations familiales, "
                "jugement, pensée ou humeur.\n\n"
                "Signes cliniques typiques:\n"
                "• Évitement social marqué\n"
                "• Négligence des responsabilités familiales\n"
                "• Incapacité de travailler ou d'étudier\n"
                "• Dépression sévère avec retrait\n"
                "• Anxiété paralysante dans plusieurs contextes\n\n"
                "Actions recommandées:\n"
                "• Traitement psychiatrique ambulatoire intensif\n"
                "• Psychothérapie structurée (TCC, TIP, etc.)\n"
                "• Médication appropriée avec suivi rapproché\n"
                "• Réhabilitation psychosociale\n"
                "• Support familial et psychoéducation\n"
                "• Considérer arrêt de travail temporaire\n"
                "• Suivi hebdomadaire minimum\n"
            )
        elif score <= 50:
            interpretation += (
                "SYMPTÔMES GRAVES - TRAITEMENT STRUCTURÉ NÉCESSAIRE\n\n"
                "Symptômes graves (idéation suicidaire, rituels obsessionnels sévères, "
                "comportements antisociaux fréquents) OU altération grave du fonctionnement.\n\n"
                "Signes cliniques typiques:\n"
                "• Idées suicidaires (sans plan imminent)\n"
                "• Rituels obsessionnels très envahissants\n"
                "• Attaques de panique fréquentes et invalidantes\n"
                "• Difficultés majeures au travail/école\n"
                "• Peu ou pas d'amis\n"
                "• Conflits interpersonnels graves\n\n"
                "Actions recommandées:\n"
                "• Traitement psychiatrique ambulatoire régulier\n"
                "• Psychothérapie (TCC recommandée)\n"
                "• Médication avec ajustement posologique\n"
                "• Évaluation régulière du risque suicidaire\n"
                "• Interventions psychosociales\n"
                "• Suivi bihebdomadaire à hebdomadaire\n"
            )
        elif score <= 60:
            interpretation += (
                "SYMPTÔMES MODÉRÉS - TRAITEMENT RECOMMANDÉ\n\n"
                "Symptômes modérés (affect aplati, discours circonstanciel, attaques de panique "
                "occasionnelles) OU difficultés modérées dans le fonctionnement.\n\n"
                "Signes cliniques typiques:\n"
                "• Symptômes dépressifs ou anxieux modérés\n"
                "• Difficultés dans les relations interpersonnelles\n"
                "• Performance diminuée au travail/école\n"
                "• Vie sociale limitée\n"
                "• Difficulté à gérer le stress quotidien\n\n"
                "Actions recommandées:\n"
                "• Traitement psychiatrique ambulatoire\n"
                "• Psychothérapie (TCC, TIP, ou autre approche)\n"
                "• Médication si indiqué (antidépresseurs, anxiolytiques)\n"
                "• Interventions de gestion du stress\n"
                "• Suivi mensuel à bihebdomadaire\n"
                "• Maintien des activités professionnelles/scolaires avec adaptations\n"
            )
        elif score <= 70:
            interpretation += (
                "SYMPTÔMES LÉGERS - FONCTIONNEMENT GLOBALEMENT SATISFAISANT\n\n"
                "Quelques symptômes légers OU difficultés légères dans le fonctionnement, "
                "mais fonctionnement assez bon dans l'ensemble.\n\n"
                "Signes cliniques typiques:\n"
                "• Symptômes légers persistants (humeur légèrement dépressive, anxiété minime)\n"
                "• Difficultés légères dans un ou deux domaines seulement\n"
                "• Capacité de maintenir relations et activités avec effort\n"
                "• Bon fonctionnement global avec quelques limites\n\n"
                "Actions recommandées:\n"
                "• Traitement ambulatoire de soutien\n"
                "• Psychothérapie brève ou de soutien\n"
                "• Médication à faible dose si nécessaire\n"
                "• Stratégies d'adaptation et prévention rechute\n"
                "• Suivi espacé (mensuel ou moins fréquent)\n"
                "• Encourager maintien des activités normales\n"
            )
        elif score <= 80:
            interpretation += (
                "SYMPTÔMES TRANSITOIRES - BON FONCTIONNEMENT\n\n"
                "Symptômes transitoires et réactions prévisibles à des facteurs de stress. "
                "Difficultés légères uniquement.\n\n"
                "Signes cliniques typiques:\n"
                "• Anxiété ou irritabilité en réaction à stress identifiable\n"
                "• Symptômes brefs et limités dans le temps\n"
                "• Difficultés mineures temporaires\n"
                "• Bon fonctionnement habituel\n"
                "• Bonnes capacités d'adaptation\n\n"
                "Actions recommandées:\n"
                "• Surveillance de l'évolution\n"
                "• Interventions brèves si nécessaire (counseling, gestion stress)\n"
                "• Support psychologique ponctuel\n"
                "• Suivi espacé ou au besoin\n"
                "• Renforcement des stratégies d'adaptation\n"
                "• Généralement pas de traitement médicamenteux nécessaire\n"
            )
        elif score <= 90:
            interpretation += (
                "EXCELLENT FONCTIONNEMENT - SYMPTÔMES ABSENTS OU MINIMES\n\n"
                "Symptômes absents ou minimes (p. ex. anxiété légère avant un examen). "
                "Fonctionnement satisfaisant dans tous les domaines.\n\n"
                "Signes cliniques typiques:\n"
                "• Aucun symptôme ou symptômes très minimes\n"
                "• Fonctionnement optimal dans tous les domaines\n"
                "• Bonnes relations interpersonnelles\n"
                "• Performance satisfaisante au travail/études\n"
                "• Bonne gestion du stress\n"
                "• Socialement efficace\n\n"
                "Actions recommandées:\n"
                "• Aucun traitement actif généralement nécessaire\n"
                "• Suivi de prévention si antécédents psychiatriques\n"
                "• Maintien des facteurs protecteurs\n"
                "• Consultation au besoin\n"
                "• Encourager poursuite des activités valorisantes\n"
            )
        else:  # score >= 91
            interpretation += (
                "FONCTIONNEMENT SUPÉRIEUR - OPTIMAL\n\n"
                "Fonctionnement supérieur dans une grande variété d'activités. Aucun symptôme. "
                "Recherché par les autres en raison de ses nombreuses qualités positives.\n\n"
                "Caractéristiques:\n"
                "• Absence totale de symptômes\n"
                "• Excellence dans plusieurs domaines de vie\n"
                "• Relations interpersonnelles riches et satisfaisantes\n"
                "• Haute performance professionnelle/académique\n"
                "• Capacités d'adaptation exceptionnelles\n"
                "• Leadership et qualités sociales reconnues\n"
                "• Résilience élevée face au stress\n\n"
                "Actions recommandées:\n"
                "• Aucun traitement nécessaire\n"
                "• Encourager maintien de l'équilibre actuel\n"
                "• Consultation uniquement si changement de situation\n"
            )
        
        # Add general notes
        interpretation += (
            "\n=== NOTES IMPORTANTES ===\n"
            "• L'EGF/GAF évalue le fonctionnement GLOBAL, pas seulement les symptômes\n"
            "• Ne pas inclure les limitations physiques ou environnementales\n"
            "• Utiliser le niveau de fonctionnement le PLUS BAS de la période évaluée\n"
            "• Les codes intermédiaires (p. ex. 45, 68) sont encouragés pour la précision\n"
            "• Réévaluer régulièrement pour suivre l'évolution clinique\n"
        )
        
        return interpretation
    
    def get_schema(self) -> Dict[str, Any]:
        """
        Get complete scale schema in JSON format for frontend integration.
        
        Returns:
            Complete scale schema
        """
        return {
            "instrument": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions(),
            "logic": {
                "validators": [
                    {
                        "id": "range_check",
                        "level": "error",
                        "message": "Le score EGF doit être un entier entre 0 et 100."
                    },
                    {
                        "id": "clinical_warning",
                        "level": "warning",
                        "message": "Scores ≤ 50 indiquent altération significative nécessitant intervention."
                    }
                ]
            },
            "scoring": {
                "variables": [],
                "scales": [
                    {
                        "id": "egf_value",
                        "label": "EGF – Valeur (0–100)",
                        "items": ["egf_score"],
                        "formula": {"var": "egf_score"},
                        "range": [0, 100]
                    },
                    {
                        "id": "egf_band",
                        "label": "EGF – Bande (10 points)",
                        "items": ["egf_score"],
                        "formula": {
                            "if": [
                                {">=": [{"var": "egf_score"}, 91]}, "91-100",
                                {"if": [
                                    {">=": [{"var": "egf_score"}, 81]}, "81-90",
                                    {"if": [
                                        {">=": [{"var": "egf_score"}, 71]}, "71-80",
                                        {"if": [
                                            {">=": [{"var": "egf_score"}, 61]}, "61-70",
                                            {"if": [
                                                {">=": [{"var": "egf_score"}, 51]}, "51-60",
                                                {"if": [
                                                    {">=": [{"var": "egf_score"}, 41]}, "41-50",
                                                    {"if": [
                                                        {">=": [{"var": "egf_score"}, 31]}, "31-40",
                                                        {"if": [
                                                            {">=": [{"var": "egf_score"}, 21]}, "21-30",
                                                            {"if": [
                                                                {">=": [{"var": "egf_score"}, 11]}, "11-20",
                                                                {"if": [
                                                                    {">=": [{"var": "egf_score"}, 1]}, "1-10",
                                                                    "0"
                                                                ]}
                                                            ]}
                                                        ]}
                                                    ]}
                                                ]}
                                            ]}
                                        ]}
                                    ]}
                                ]}
                            ]
                        },
                        "range": ["0", "1-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90", "91-100"]
                    }
                ]
            },
            "provenance": {
                "created_at": datetime.utcnow().isoformat() + "Z",
                "updated_at": datetime.utcnow().isoformat() + "Z",
                "validated_by": "IngénieurQuestionnaire",
                "validation_date": datetime.utcnow().date().isoformat()
            }
        }
    
    def get_full_questionnaire(self) -> Dict[str, Any]:
        """
        Get complete questionnaire structure for frontend rendering.
        
        Returns:
            Dictionary with metadata, sections, and questions
        """
        return {
            "metadata": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions()
        }

