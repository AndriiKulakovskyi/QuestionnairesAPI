"""
MADRS - Montgomery-Åsberg Depression Rating Scale

This module implements the MADRS, a widely used clinician-rated scale for assessing
the severity of depressive symptoms. Developed by Montgomery and Åsberg in 1979,
it consists of 10 items rated from 0 to 6, with defined anchors at 0, 2, 4, and 6,
and intermediate ratings (1, 3, 5) for values between anchors.

The MADRS is particularly sensitive to change and is frequently used in clinical trials
and treatment monitoring. Rating is based on a clinical interview exploring symptoms
from the past week.
"""

from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime


class MADRSError(Exception):
    """Custom exception for MADRS scale errors."""
    pass


class MADRS:
    """
    MADRS - Montgomery-Åsberg Depression Rating Scale
    
    A 10-item clinician-rated scale for assessing depressive symptom severity.
    Each item is rated 0-6 based on clinical interview, with:
    - Defined anchors at 0, 2, 4, 6
    - Intermediate values at 1, 3, 5
    
    Total score range: 0-60
    
    Clinical cutoffs (Snaith et al., 1986):
    - 0-6: Euthymia (symptom remission)
    - 7-19: Mild depression
    - 20-34: Moderate depression
    - 35-60: Severe depression
    
    The MADRS emphasizes psychological symptoms of depression and is designed
    to be sensitive to change, making it ideal for treatment monitoring.
    
    Attributes:
        id: Unique identifier for the scale
        name: Full name in French
        abbreviation: Short form (MADRS)
        language: Language code
        version: Version number
        reference_period: Time frame for assessment
        description: Brief description of the scale
    """
    
    # Clinical cutoffs (Snaith et al., 1986)
    CUTOFFS = [
        (0, 6, "Euthymie"),
        (7, 19, "Dépression légère"),
        (20, 34, "Dépression modérée"),
        (35, 60, "Dépression sévère")
    ]
    
    # Remission threshold (commonly used in clinical trials)
    REMISSION_THRESHOLD = 10
    
    # Response threshold (≥50% reduction from baseline)
    RESPONSE_REDUCTION_PERCENT = 50
    
    def __init__(self):
        """Initialize the MADRS scale."""
        self.id = "MADRS.fr"
        self.name = "Échelle de Dépression de Montgomery-Åsberg (MADRS) – Version française"
        self.abbreviation = "MADRS"
        self.language = "fr-FR"
        self.version = "1.0"
        self.reference_period = "Semaine écoulée / état actuel"
        self.description = (
            "10 items cotés 0–6 (0,2,4,6 définis; 1,3,5 intermédiaires). "
            "Total 0–60; seuils Snaith 1986 : 0–6 euthymie, 7–19 léger, "
            "20–34 modéré, 35–60 sévère."
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
            "num_items": 10,
            "rating_scale": "0-6 ordinal scale",
            "anchor_points": "Defined at 0, 2, 4, 6 (1, 3, 5 are intermediate)",
            "score_range": [0, 60],
            "administration": "Clinician-rated based on clinical interview",
            "duration": "20-30 minutes",
            "cutoffs": {
                "euthymia": "0-6",
                "mild": "7-19",
                "moderate": "20-34",
                "severe": "35-60"
            },
            "remission_threshold": self.REMISSION_THRESHOLD,
            "response_criterion": f"≥{self.RESPONSE_REDUCTION_PERCENT}% reduction from baseline",
            "key_features": [
                "Sensitive to change",
                "Widely used in clinical trials",
                "Emphasizes psychological symptoms",
                "Good inter-rater reliability"
            ],
            "reference": "Montgomery SA, Åsberg M. Br J Psychiatry. 1979;134:382-389"
        }
    
    def get_questions(self) -> List[Dict[str, Any]]:
        """
        Get all 10 MADRS items.
        
        Returns:
            List of 10 question dictionaries
        """
        # Item texts exactly as in the French MADRS
        item_texts = [
            "Tristesse apparente",
            "Tristesse exprimée",
            "Tension intérieure (angoisse, effroi, panique)",
            "Réduction du sommeil (durée/profondeur)",
            "Réduction de l'appétit",
            "Difficultés de concentration",
            "Lassitude (inertie à se mettre en route)",
            "Incapacité à ressentir (anesthésie affective)",
            "Pensées pessimistes (culpabilité, autodépréciation, ruine)",
            "Idées de suicide (de « la vie ne vaut pas la peine » à projets explicites)"
        ]
        
        # Detailed descriptions for each item (for clinician guidance)
        item_descriptions = [
            "Évaluer la tristesse, la mélancolie, le désespoir reflétés dans la parole, l'expression faciale et la posture. Coter selon la profondeur et l'incapacité à se dérider.",
            "Évaluer comment le patient rapporte subjectivement son humeur dépressive, sans tenir compte si cela est reflété dans son apparence. Inclut abattement, découragement, sentiment de désespoir.",
            "Représente les sentiments de malaise mal défini, d'irritabilité, de tourment intérieur, de tension nerveuse allant jusqu'à la panique, l'effroi ou l'angoisse. Coter selon l'intensité, la fréquence, la durée et le besoin de réassurance.",
            "Représente la réduction de la durée ou de la profondeur du sommeil par rapport aux habitudes du patient en bonne santé.",
            "Représente le sentiment de perte d'appétit. Coter la perte d'envie de manger ou le besoin de se forcer à manger.",
            "Représente les difficultés à rassembler ses pensées allant jusqu'à l'incapacité à se concentrer. Coter selon l'intensité, la fréquence et le degré d'incapacité produite.",
            "Représente une difficulté à se mettre en route ou une lenteur à commencer et à accomplir les activités quotidiennes.",
            "Représente l'expérience subjective de réduction d'intérêt pour l'environnement ou les activités qui normalement donnent du plaisir. L'incapacité à réagir avec une émotion appropriée aux circonstances ou aux gens.",
            "Représente les pensées de culpabilité, d'infériorité, d'autodépréciation, de péché, d'appauvrissement ou de ruine.",
            "Représente le sentiment que la vie ne vaut pas la peine d'être vécue, qu'une mort naturelle serait la bienvenue, des idées de suicide et des préparatifs au suicide. Les tentatives de suicide ne devraient pas en elles-mêmes influencer la cotation."
        ]
        
        questions = []
        
        for i, (text, description) in enumerate(zip(item_texts, item_descriptions), start=1):
            questions.append({
                "id": f"q{i}",
                "section_id": "sec_items",
                "text": f"{i}. {text}",
                "description": description,
                "type": "single_choice",
                "required": True,
                "options": [
                    {"code": 0, "label": "0", "score": 0, "anchor": "defined"},
                    {"code": 1, "label": "1", "score": 1, "anchor": "intermediate"},
                    {"code": 2, "label": "2", "score": 2, "anchor": "defined"},
                    {"code": 3, "label": "3", "score": 3, "anchor": "intermediate"},
                    {"code": 4, "label": "4", "score": 4, "anchor": "defined"},
                    {"code": 5, "label": "5", "score": 5, "anchor": "intermediate"},
                    {"code": 6, "label": "6", "score": 6, "anchor": "defined"}
                ],
                "constraints": {
                    "value_type": "integer",
                    "allowed_values": [0, 1, 2, 3, 4, 5, 6]
                },
                "rating_note": "0, 2, 4, 6 sont des ancrages définis; 1, 3, 5 sont des valeurs intermédiaires"
            })
        
        return questions
    
    def get_sections(self) -> List[Dict[str, Any]]:
        """
        Get scale sections.
        
        Returns:
            List containing the single section
        """
        return [
            {
                "id": "sec_items",
                "label": "Items 1–10",
                "description": "Cotation 0–6 par entretien clinique",
                "question_ids": [f"q{i}" for i in range(1, 11)],
                "instructions": (
                    "Chaque item doit être coté de 0 à 6 en se basant sur un entretien clinique. "
                    "Les ancrages 0, 2, 4 et 6 sont clairement définis. Les valeurs 1, 3 et 5 "
                    "sont utilisées pour les niveaux intermédiaires entre les ancrages."
                )
            }
        ]
    
    def validate_answers(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Validate MADRS responses.
        
        Args:
            answers: Dictionary mapping item IDs to response values
        
        Returns:
            Dictionary containing validation results with 'valid', 'errors', and 'warnings' keys
        """
        errors = []
        warnings = []
        
        # Check all 10 items are present
        expected_items = [f"q{i}" for i in range(1, 11)]
        missing = [item for item in expected_items if item not in answers]
        
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Validate response values
        for item_id, value in answers.items():
            if item_id in expected_items:
                if not isinstance(value, int):
                    errors.append(f"{item_id}: la valeur doit être un entier (reçu: {type(value).__name__})")
                elif value < 0 or value > 6:
                    errors.append(f"{item_id}: la valeur doit être entre 0 et 6 (reçu: {value})")
        
        # Clinical warnings (only if validation passes)
        if not errors:
            # Calculate total for warning thresholds
            total = sum(answers.get(f"q{i}", 0) for i in range(1, 11))
            
            # Severe depression
            if total >= 35:
                warnings.append(
                    "Dépression sévère (score ≥ 35). État dépressif majeur nécessitant "
                    "intervention intensive. Évaluation du risque suicidaire impérative."
                )
            # Moderate depression
            elif total >= 20:
                warnings.append(
                    "Dépression modérée (score 20-34). Symptomatologie dépressive significative "
                    "nécessitant traitement actif."
                )
            
            # Suicidal ideation (item 10)
            if answers.get("q10", 0) >= 4:
                warnings.append(
                    "🚨 ALERTE SÉCURITÉ: Idées suicidaires importantes (item 10 ≥ 4). "
                    "Évaluation approfondie du risque suicidaire immédiate requise. "
                    "Considérer hospitalisation."
                )
            elif answers.get("q10", 0) >= 2:
                warnings.append(
                    "⚠️ Présence d'idées suicidaires (item 10 ≥ 2). "
                    "Évaluation du risque suicidaire nécessaire."
                )
            
            # Severe individual symptoms
            severe_symptoms = []
            item_names = {
                "q1": "Tristesse apparente",
                "q2": "Tristesse exprimée",
                "q3": "Tension intérieure",
                "q4": "Réduction du sommeil",
                "q5": "Réduction de l'appétit",
                "q6": "Difficultés de concentration",
                "q7": "Lassitude",
                "q8": "Incapacité à ressentir",
                "q9": "Pensées pessimistes",
                "q10": "Idées de suicide"
            }
            
            for item_id, name in item_names.items():
                if answers.get(item_id, 0) == 6:
                    severe_symptoms.append(name)
            
            if severe_symptoms:
                warnings.append(
                    f"Symptômes sévères (score 6/6): {', '.join(severe_symptoms)}. "
                    "Ces symptômes sont au maximum de sévérité et nécessitent attention particulière."
                )
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def get_severity_category(self, total_score: int) -> str:
        """
        Get severity category based on Snaith et al. (1986) cutoffs.
        
        Args:
            total_score: Total MADRS score (0-60)
        
        Returns:
            Severity category label
        """
        for min_score, max_score, label in self.CUTOFFS:
            if min_score <= total_score <= max_score:
                return label
        
        # Should not reach here if score is 0-60
        raise MADRSError(f"Score total hors bornes: {total_score}")
    
    def calculate_score(
        self,
        answers: Dict[str, int],
        baseline_score: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Calculate MADRS score and interpretation.
        
        Args:
            answers: Dictionary mapping item IDs (q1-q10) to response values (0-6)
            baseline_score: Optional baseline score for calculating % change and response
        
        Returns:
            Dictionary containing:
                - total_score: Total MADRS score (0-60)
                - severity: Severity category
                - item_scores: Individual item scores
                - remission: Whether score meets remission criteria
                - response: Whether ≥50% reduction from baseline (if baseline provided)
                - percent_change: Percent change from baseline (if baseline provided)
                - interpretation: Detailed clinical interpretation
                - warnings: Clinical warnings
        
        Raises:
            MADRSError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation["valid"]:
            raise MADRSError(
                f"Validation échouée: {'; '.join(validation['errors'])}"
            )
        
        # Calculate total score
        total_score = sum(answers.get(f"q{i}", 0) for i in range(1, 11))
        
        # Get severity category
        severity = self.get_severity_category(total_score)
        
        # Check remission
        remission = total_score <= self.REMISSION_THRESHOLD
        
        # Calculate response and percent change if baseline provided
        response = None
        percent_change = None
        if baseline_score is not None:
            if baseline_score > 0:
                percent_change = round(((baseline_score - total_score) / baseline_score) * 100, 1)
                response = percent_change >= self.RESPONSE_REDUCTION_PERCENT
            else:
                percent_change = 0.0
                response = False
        
        # Collect item scores with names
        item_scores = {}
        item_names = [
            "Tristesse apparente",
            "Tristesse exprimée",
            "Tension intérieure",
            "Réduction du sommeil",
            "Réduction de l'appétit",
            "Difficultés de concentration",
            "Lassitude",
            "Incapacité à ressentir",
            "Pensées pessimistes",
            "Idées de suicide"
        ]
        
        for i, name in enumerate(item_names, start=1):
            item_scores[f"q{i}"] = {
                "score": answers.get(f"q{i}", 0),
                "name": name
            }
        
        # Generate interpretation
        interpretation = self._generate_interpretation(
            total_score,
            severity,
            item_scores,
            remission,
            response,
            percent_change,
            baseline_score
        )
        
        return {
            "total_score": total_score,
            "severity": severity,
            "item_scores": item_scores,
            "remission": remission,
            "response": response,
            "percent_change": percent_change,
            "baseline_score": baseline_score,
            "interpretation": interpretation,
            "warnings": validation["warnings"],
            "calculation_date": datetime.utcnow().isoformat() + "Z"
        }
    
    def _generate_interpretation(
        self,
        total_score: int,
        severity: str,
        item_scores: Dict[str, Dict[str, Any]],
        remission: bool,
        response: Optional[bool],
        percent_change: Optional[float],
        baseline_score: Optional[int]
    ) -> str:
        """Generate comprehensive clinical interpretation."""
        interpretation = "=== MADRS – ÉCHELLE DE DÉPRESSION DE MONTGOMERY-ÅSBERG ===\n\n"
        
        # Summary
        interpretation += "=== RÉSUMÉ ===\n"
        interpretation += f"Score total: {total_score}/60\n"
        interpretation += f"Sévérité: {severity.upper()}\n"
        
        if baseline_score is not None:
            interpretation += f"Score initial (baseline): {baseline_score}/60\n"
            interpretation += f"Variation: {percent_change:+.1f}%\n"
            if response is not None:
                interpretation += f"Réponse thérapeutique (≥50% réduction): {'OUI' if response else 'NON'}\n"
        
        interpretation += f"Rémission (score ≤ 10): {'OUI' if remission else 'NON'}\n\n"
        
        # Severity interpretation
        interpretation += "=== INTERPRÉTATION CLINIQUE ===\n"
        
        if total_score <= 6:
            interpretation += (
                "✅ EUTHYMIE (Score 0-6)\n\n"
                "Le patient ne présente pas de symptomatologie dépressive cliniquement significative. "
                "Le score se situe dans la fourchette normale, indiquant une rémission symptomatique "
                "ou l'absence de dépression.\n\n"
                "Recommandations:\n"
                "• Si traitement en cours: Maintenir le traitement actuel\n"
                "• Poursuivre le suivi de prévention de rechute\n"
                "• Surveillance régulière recommandée (mensuelle à trimestrielle)\n"
                "• Renforcer les stratégies de prévention (hygiène de vie, stress, observance)\n"
                "• Psychoéducation sur les signes précoces de rechute\n"
            )
        elif total_score <= 19:
            interpretation += (
                "🟡 DÉPRESSION LÉGÈRE (Score 7-19)\n\n"
                "Le patient présente une symptomatologie dépressive légère. Les symptômes sont "
                "présents mais d'intensité limitée et n'entravent pas massivement le fonctionnement.\n\n"
                "Recommandations:\n"
                "• Évaluation diagnostique complète (premier épisode vs. récurrence)\n"
                "• Psychothérapie (TCC, TIP recommandées)\n"
                "• Considérer traitement antidépresseur si:\n"
                "  - Symptômes persistants > 2 semaines\n"
                "  - Antécédents d'épisodes dépressifs majeurs\n"
                "  - Retentissement fonctionnel significatif\n"
                "  - Préférence du patient\n"
                "• Interventions psychosociales (activation comportementale, hygiène de vie)\n"
                "• Suivi bihebdomadaire à hebdomadaire initialement\n"
                "• Réévaluation dans 2-4 semaines\n"
            )
        elif total_score <= 34:
            interpretation += (
                "🟠 DÉPRESSION MODÉRÉE (Score 20-34)\n\n"
                "Le patient présente un épisode dépressif d'intensité modérée. La symptomatologie "
                "est clairement établie avec impact fonctionnel significatif.\n\n"
                "Recommandations:\n"
                "• Traitement antidépresseur RECOMMANDÉ\n"
                "• Psychothérapie structurée (TCC ou TIP) en combinaison\n"
                "• Évaluation du risque suicidaire\n"
                "• Arrêt de travail si retentissement professionnel important\n"
                "• Suivi rapproché (hebdomadaire initialement)\n"
                "• Réévaluation à 2-4 semaines pour ajuster si nécessaire\n"
                "• Considérer causes organiques (hypothyroïdie, anémie, etc.)\n"
                "• Support familial et psychoéducation\n"
                "• Si pas de réponse à 4-6 semaines: optimisation posologique ou changement\n"
            )
        else:  # 35-60
            interpretation += (
                "🔴 DÉPRESSION SÉVÈRE (Score 35-60)\n\n"
                "Le patient présente un épisode dépressif majeur sévère. Impact majeur sur le "
                "fonctionnement. Souffrance intense. Risque suicidaire à évaluer impérativement.\n\n"
                "Recommandations URGENTES:\n"
                "• 🚨 ÉVALUATION DU RISQUE SUICIDAIRE IMPÉRATIVE\n"
                "• Considérer HOSPITALISATION si:\n"
                "  - Risque suicidaire élevé\n"
                "  - Incapacité à s'alimenter/s'hydrater\n"
                "  - Absence de support familial/social\n"
                "  - Symptômes psychotiques\n"
                "  - Échec des traitements ambulatoires\n"
                "• Traitement antidépresseur À DOSES OPTIMALES\n"
                "• Considérer association/augmentation:\n"
                "  - Antipsychotique atypique si caractéristiques psychotiques\n"
                "  - Lithium ou antipsychotique en augmentation\n"
                "• Considérer électroconvulsivothérapie (ECT) si:\n"
                "  - Résistance aux traitements\n"
                "  - Urgence vitale (risque suicidaire majeur, refus alimentaire)\n"
                "  - Dépression mélancolique ou psychotique\n"
                "• Suivi TRÈS rapproché (2-3 fois/semaine minimum)\n"
                "• Arrêt de travail prolongé\n"
                "• Implication de la famille/proches\n"
                "• Retrait des moyens létaux\n"
                "• Plan de sécurité détaillé\n"
            )
        
        # Change analysis if baseline provided
        if baseline_score is not None and percent_change is not None:
            interpretation += "\n=== ÉVOLUTION DEPUIS BASELINE ===\n"
            interpretation += f"Score initial: {baseline_score}/60\n"
            interpretation += f"Score actuel: {total_score}/60\n"
            interpretation += f"Changement: {total_score - baseline_score:+d} points ({percent_change:+.1f}%)\n\n"
            
            if response:
                interpretation += (
                    "✅ RÉPONSE THÉRAPEUTIQUE OBTENUE\n"
                    f"Réduction ≥ 50% du score initial ({percent_change:.1f}% de réduction). "
                    "Le traitement est efficace. Poursuivre et viser la rémission complète.\n\n"
                    "Actions:\n"
                    "• Maintenir le traitement actuel\n"
                    "• Poursuivre jusqu'à rémission complète (MADRS ≤ 10)\n"
                    "• Ne pas arrêter prématurément même si amélioration\n"
                    "• Phase de continuation: 4-9 mois après rémission\n"
                    "• Phase d'entretien si ≥ 3 épisodes ou facteurs de risque\n"
                )
            elif percent_change >= 25:
                interpretation += (
                    "⚠️ RÉPONSE PARTIELLE\n"
                    f"Amélioration de {percent_change:.1f}% (insuffisant pour réponse complète).\n\n"
                    "Actions:\n"
                    "• Si < 4 semaines de traitement: Poursuivre et réévaluer\n"
                    "• Si ≥ 4 semaines:\n"
                    "  - Vérifier l'observance\n"
                    "  - Optimiser la posologie si dose sous-optimale\n"
                    "  - Considérer augmentation (lithium, T3, antipsychotique atypique)\n"
                    "  - Considérer changement d'antidépresseur si plateau\n"
                    "• Renforcer la psychothérapie\n"
                )
            elif percent_change > -10:
                interpretation += (
                    "❌ ABSENCE DE RÉPONSE\n"
                    f"Pas d'amélioration significative ({percent_change:+.1f}%).\n\n"
                    "Actions:\n"
                    "• Réévaluer le diagnostic\n"
                    "• Vérifier l'observance thérapeutique strictement\n"
                    "• Rechercher facteurs de résistance:\n"
                    "  - Comorbidités (anxiété, abus de substances)\n"
                    "  - Troubles de personnalité\n"
                    "  - Facteurs psychosociaux non résolus\n"
                    "  - Causes organiques (hypothyroïdie, etc.)\n"
                    "• Si dose optimale et observance OK:\n"
                    "  - CHANGER d'antidépresseur (classe différente)\n"
                    "  - Ou considérer augmentation\n"
                    "  - Ou ECT si sévérité/urgence\n"
                )
            else:
                interpretation += (
                    "🚨 AGGRAVATION\n"
                    f"Le score a augmenté de {abs(percent_change):.1f}%.\n\n"
                    "Actions URGENTES:\n"
                    "• Réévaluation complète immédiate\n"
                    "• Évaluer le risque suicidaire\n"
                    "• Vérifier observance et interactions médicamenteuses\n"
                    "• Rechercher événements de vie stressants\n"
                    "• Considérer hospitalisation si aggravation sévère\n"
                    "• Changement thérapeutique urgent\n"
                )
        
        # Remission status
        interpretation += "\n=== STATUT DE RÉMISSION ===\n"
        if remission:
            interpretation += (
                f"✅ RÉMISSION ATTEINTE (Score {total_score} ≤ 10)\n\n"
                "Le patient répond aux critères de rémission symptomatique. "
                "La grande majorité des symptômes dépressifs sont absents.\n\n"
                "Plan de traitement:\n"
                "• MAINTENIR le traitement actuel (NE PAS arrêter)\n"
                "• Phase de continuation: 4-9 mois minimum après rémission\n"
                "• Phase d'entretien (maintenance) si:\n"
                "  - ≥ 3 épisodes dépressifs\n"
                "  - ≥ 2 épisodes avec facteurs de risque\n"
                "  - Épisode très sévère\n"
                "  - Début tardif (> 50 ans)\n"
                "• Suivi mensuel puis espacé progressivement\n"
                "• Psychothérapie de prévention de rechute\n"
                "• Psychoéducation sur signes précoces de rechute\n"
            )
        else:
            interpretation += (
                f"❌ RÉMISSION NON ATTEINTE (Score {total_score} > 10)\n\n"
                "Des symptômes dépressifs résiduels persistent. La rémission complète "
                "n'est pas encore obtenue.\n\n"
                "Importance:\n"
                "• Les symptômes résiduels sont un facteur de risque majeur de rechute\n"
                "• Viser toujours la rémission complète (MADRS ≤ 10), pas seulement la réponse\n"
                "• Un score > 10 justifie la poursuite de l'optimisation thérapeutique\n\n"
                "Actions:\n"
                "• Identifier les symptômes résiduels dominants\n"
                "• Optimiser le traitement pour viser rémission\n"
                "• Traiter spécifiquement les symptômes résiduels\n"
                "• Renforcer les interventions non pharmacologiques\n"
            )
        
        # Item-by-item analysis
        interpretation += "\n=== ANALYSE PAR ITEM ===\n\n"
        
        # Group items by severity
        severe_items = []
        moderate_items = []
        mild_items = []
        absent_items = []
        
        for item_id, item_data in item_scores.items():
            score = item_data["score"]
            name = item_data["name"]
            
            if score >= 5:
                severe_items.append(f"{name} ({score}/6)")
            elif score >= 3:
                moderate_items.append(f"{name} ({score}/6)")
            elif score >= 1:
                mild_items.append(f"{name} ({score}/6)")
            else:
                absent_items.append(name)
        
        if severe_items:
            interpretation += "**Symptômes sévères (score 5-6):**\n"
            for item in severe_items:
                interpretation += f"  🔴 {item}\n"
            interpretation += "\n"
        
        if moderate_items:
            interpretation += "**Symptômes modérés (score 3-4):**\n"
            for item in moderate_items:
                interpretation += f"  🟡 {item}\n"
            interpretation += "\n"
        
        if mild_items:
            interpretation += "**Symptômes légers (score 1-2):**\n"
            for item in mild_items:
                interpretation += f"  🟢 {item}\n"
            interpretation += "\n"
        
        if absent_items and len(absent_items) < 10:
            interpretation += "**Symptômes absents:**\n"
            for item in absent_items[:5]:  # Limit to avoid too long list
                interpretation += f"  ✓ {item}\n"
            if len(absent_items) > 5:
                interpretation += f"  ✓ ... et {len(absent_items) - 5} autres\n"
            interpretation += "\n"
        
        # Specific symptom alerts
        interpretation += "=== POINTS D'ATTENTION SPÉCIFIQUES ===\n\n"
        
        # Suicidal ideation
        suicide_score = item_scores["q10"]["score"]
        if suicide_score >= 4:
            interpretation += (
                "🚨 **ALERTE CRITIQUE: Idées suicidaires sévères**\n"
                f"Score item 10: {suicide_score}/6\n"
                "Actions immédiates:\n"
                "• Évaluation approfondie du risque suicidaire (échelle Columbia, plan, accès aux moyens)\n"
                "• Hospitalisation à considérer fortement\n"
                "• Surveillance constante si maintien ambulatoire\n"
                "• Implication de la famille/proches\n"
                "• Retrait des moyens létaux\n"
                "• Contrat de non-suicide et plan de crise\n"
                "• Contact direct si aggravation\n\n"
            )
        elif suicide_score >= 2:
            interpretation += (
                f"⚠️ **Présence d'idées suicidaires** (Score item 10: {suicide_score}/6)\n"
                "Actions:\n"
                "• Évaluation du risque suicidaire\n"
                "• Questionner sur plan, intention, moyens\n"
                "• Surveillance régulière\n"
                "• Plan de sécurité\n\n"
            )
        
        # Core depressive symptoms
        sadness_apparent = item_scores["q1"]["score"]
        sadness_reported = item_scores["q2"]["score"]
        if sadness_apparent >= 5 or sadness_reported >= 5:
            interpretation += (
                "**Tristesse dépressive majeure présente**\n"
                f"Tristesse apparente: {sadness_apparent}/6, Tristesse exprimée: {sadness_reported}/6\n"
                "Symptôme cardinal de la dépression au maximum. Cible prioritaire du traitement.\n\n"
            )
        
        # Anhedonia/inability to feel
        anhedonia = item_scores["q8"]["score"]
        if anhedonia >= 5:
            interpretation += (
                "**Anhédonie/Incapacité à ressentir sévère**\n"
                f"Score item 8: {anhedonia}/6\n"
                "Anesthésie affective majeure. Symptôme souvent résistant, peut nécessiter:\n"
                "• Optimisation posologique\n"
                "• Changement d'antidépresseur (ISRS→ IRSN ou bupropion)\n"
                "• Activation comportementale intensive\n\n"
            )
        
        # Anxiety/inner tension
        tension = item_scores["q3"]["score"]
        if tension >= 5:
            interpretation += (
                "**Tension intérieure/Angoisse sévère**\n"
                f"Score item 3: {tension}/6\n"
                "Anxiété/angoisse majeure. Considérer:\n"
                "• Benzodiazépine temporaire (2-4 semaines maximum)\n"
                "• Antidépresseur avec effet anxiolytique (paroxétine, escitalopram)\n"
                "• Prégabaline ou buspirone si anxiété persistante\n"
                "• TCC spécifique pour l'anxiété\n\n"
            )
        
        # Cognitive symptoms
        concentration = item_scores["q6"]["score"]
        if concentration >= 5:
            interpretation += (
                "**Difficultés de concentration sévères**\n"
                f"Score item 6: {concentration}/6\n"
                "Impact cognitif majeur. Éliminer causes organiques. "
                "Les déficits cognitifs peuvent persister après rémission thymique.\n\n"
            )
        
        # Vegetative symptoms
        sleep = item_scores["q4"]["score"]
        appetite = item_scores["q5"]["score"]
        if sleep >= 4 or appetite >= 4:
            interpretation += (
                f"**Symptômes végétatifs marqués** (Sommeil: {sleep}/6, Appétit: {appetite}/6)\n"
                "Perturbations neurobiologiques importantes. Considérer:\n"
                "• Mirtazapine si insomnie et perte d'appétit\n"
                "• Traitement hypnotique temporaire si insomnie sévère\n"
                "• Suppléments nutritionnels si anorexie marquée\n\n"
            )
        
        # General notes
        interpretation += (
            "=== NOTES SUR L'UTILISATION DU MADRS ===\n"
            "• Le MADRS est un outil de mesure de la sévérité, pas un outil diagnostique\n"
            "• Sensible au changement, idéal pour le suivi thérapeutique\n"
            "• Cotation basée sur entretien clinique (20-30 minutes)\n"
            "• Les ancrages 0, 2, 4, 6 sont clairement définis; 1, 3, 5 sont intermédiaires\n"
            "• Réévaluation recommandée toutes les 1-2 semaines en phase aiguë\n"
            "• Mensuelle en phase de continuation/maintenance\n"
            "• La rémission (≤ 10) doit être l'objectif thérapeutique\n"
            "• Scores > 10 = risque accru de rechute même si amélioration\n"
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
                        "id": "response_range",
                        "level": "error",
                        "message": "Chaque item doit être coté de 0 à 6."
                    },
                    {
                        "id": "completeness",
                        "level": "error",
                        "message": "Les 10 items doivent être complétés."
                    },
                    {
                        "id": "anchor_note",
                        "level": "info",
                        "message": "0, 2, 4, 6 sont des ancrages définis. 1, 3, 5 sont intermédiaires."
                    }
                ]
            },
            "scoring": {
                "scales": [
                    {
                        "id": "madrs_total",
                        "label": "MADRS – Total (0–60)",
                        "items": [f"q{i}" for i in range(1, 11)],
                        "formula": {"+": [{"var": f"q{i}"} for i in range(1, 11)]},
                        "range": [0, 60],
                        "cutoffs": [
                            {
                                "label": "Euthymie (0–6)",
                                "rule": {"<=": [{"var": "madrs_total"}, 6]}
                            },
                            {
                                "label": "Dépression légère (7–19)",
                                "rule": {
                                    "and": [
                                        {">=": [{"var": "madrs_total"}, 7]},
                                        {"<=": [{"var": "madrs_total"}, 19]}
                                    ]
                                }
                            },
                            {
                                "label": "Dépression modérée (20–34)",
                                "rule": {
                                    "and": [
                                        {">=": [{"var": "madrs_total"}, 20]},
                                        {"<=": [{"var": "madrs_total"}, 34]}
                                    ]
                                }
                            },
                            {
                                "label": "Dépression sévère (35–60)",
                                "rule": {">=": [{"var": "madrs_total"}, 35]}
                            }
                        ]
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

