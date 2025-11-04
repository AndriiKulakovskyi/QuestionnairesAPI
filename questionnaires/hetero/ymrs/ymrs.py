"""
YMRS - Young Mania Rating Scale

This module implements the YMRS, the most widely used clinician-rated scale for assessing
the severity of manic symptoms in bipolar disorder. Developed by Young et al. in 1978,
it consists of 11 items with heterogeneous scoring:
- 7 items rated 0-4 (items 1,2,3,4,7,10,11)
- 4 items rated 0-8 (items 5,6,8,9) - doubled weight for these core symptoms

The YMRS is the gold standard for measuring mania severity in clinical trials and
treatment monitoring. Rating is based on a clinical interview and observation of the
patient's behavior during the past 48 hours (or longer depending on clinical context).
"""

from typing import Dict, List, Optional, Any, Tuple, Set
from datetime import datetime


class YMRSError(Exception):
    """Custom exception for YMRS scale errors."""
    pass


class YMRS:
    """
    YMRS - Young Mania Rating Scale
    
    An 11-item clinician-rated scale for assessing manic symptom severity.
    
    Item scoring structure (heterogeneous):
    - Items 1,2,3,4,7,10,11: rated 0-4
    - Items 5,6,8,9: rated 0-8 (double weighted)
    
    Total score range: 0-60
    
    Clinical cutoffs:
    - 0-11: No significant manic symptoms (euthymia/remission)
    - 12-20: Hypomania (mild to moderate manic symptoms)
    - ≥21: Mania (moderate to severe manic episode)
    
    The YMRS is sensitive to change and widely used in clinical trials for
    bipolar disorder. The double-weighted items (5,6,8,9) represent core
    manic symptoms: irritability, speech pressure, thought content, and
    disruptive behavior.
    
    Attributes:
        id: Unique identifier for the scale
        name: Full name in French
        abbreviation: Short form (YMRS)
        language: Language code
        version: Version number
        reference_period: Time frame for assessment
        description: Brief description of the scale
    """
    
    # Items rated 0-4
    ITEMS_0_TO_4: Set[int] = {1, 2, 3, 4, 7, 10, 11}
    
    # Items rated 0-8 (double weighted)
    ITEMS_0_TO_8: Set[int] = {5, 6, 8, 9}
    
    # Clinical cutoffs
    CUTOFF_NO_HYPOMANIA = 11
    CUTOFF_HYPOMANIA = 12
    CUTOFF_MANIA = 21
    
    # Remission threshold (commonly used in clinical practice)
    REMISSION_THRESHOLD = 12
    
    def __init__(self):
        """Initialize the YMRS scale."""
        self.id = "YMRS.fr"
        self.name = "Échelle de Manie de Young (YMRS) – Version française"
        self.abbreviation = "YMRS"
        self.language = "fr-FR"
        self.version = "1.0"
        self.reference_period = "Semaine écoulée / état actuel (selon guide)"
        self.description = (
            "11 items; certains cotés 0–4, d'autres 0–8. "
            "Score total 0–60 (plus élevé = manie plus sévère)."
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
            "num_items": 11,
            "rating_scale": "Heterogeneous: 7 items (0-4) + 4 items (0-8)",
            "items_0_to_4": list(self.ITEMS_0_TO_4),
            "items_0_to_8": list(self.ITEMS_0_TO_8),
            "score_range": [0, 60],
            "administration": "Clinician-rated based on clinical interview and observation",
            "duration": "15-30 minutes",
            "cutoffs": {
                "no_hypomania": "0-11",
                "hypomania": "12-20",
                "mania": "≥21"
            },
            "remission_threshold": self.REMISSION_THRESHOLD,
            "key_features": [
                "Gold standard for mania assessment",
                "Sensitive to change",
                "Widely used in clinical trials",
                "Double-weighted items for core symptoms",
                "Good inter-rater reliability"
            ],
            "reference": "Young RC et al. Br J Psychiatry. 1978;133:429-435"
        }
    
    def get_questions(self) -> List[Dict[str, Any]]:
        """
        Get all 11 YMRS items with their specific scoring ranges.
        
        Returns:
            List of 11 question dictionaries
        """
        # Item definitions with max scores
        items_meta = {
            1: ("Élévation de l'humeur", 4),
            2: ("Activité motrice et énergie augmentées", 4),
            3: ("Intérêt sexuel", 4),
            4: ("Sommeil", 4),
            5: ("Irritabilité", 8),
            6: ("Discours (débit et quantité)", 8),
            7: ("Langage – troubles de la pensée", 4),
            8: ("Contenu (idées, thèmes)", 8),
            9: ("Comportement agressif et perturbateur", 8),
            10: ("Apparence", 4),
            11: ("Introspection (insight)", 4)
        }
        
        # Detailed clinical descriptions for each item
        item_descriptions = {
            1: "Évaluer l'humeur euphorique, optimiste, ou expansive. 0=Absence; 2=Légèrement ou possiblement augmentée; 4=Manifestement élevée, euphorique.",
            2: "Évaluer l'augmentation de l'activité motrice, l'agitation, et le niveau d'énergie. 0=Absent; 2=Augmentation subjective; 4=Énergie excessive, hyperactivité motrice presque constante.",
            3: "Évaluer les pensées sexuelles, préoccupations, ou comportements. 0=Normal; 2=Légèrement augmenté; 4=Contenu sexuel manifeste ou comportement sexuel manifeste.",
            4: "Évaluer la réduction du besoin de sommeil. 0=Ne rapporte pas de diminution; 2=Dort 1 heure de moins que d'habitude; 4=Nie le besoin de dormir.",
            5: "Évaluer l'irritabilité et la tendance à la colère (item 0-8). 0=Absent; 2=Subjectivement augmentée; 4=Irritable à certains moments durant l'entretien; 6=Fréquemment irritable; 8=Hostile, non coopératif.",
            6: "Évaluer le débit et la quantité de parole (item 0-8). 0=Pas d'augmentation; 2=Sent qu'il parle plus; 4=Augmentation notée; 6=Difficile à interrompre, logorrhée; 8=Parle sans interruption, impossible à interrompre.",
            7: "Évaluer les troubles formels de la pensée (fuite des idées, coq-à-l'âne). 0=Absent; 2=Circonstancialité; 4=Perte des associations, coq-à-l'âne fréquent, désorganisation.",
            8: "Évaluer le contenu de la pensée: projets grandioses, idées de grandeur, délires (item 0-8). 0=Normal; 2=Nouveaux intérêts, projets compatibles; 4=Projets spéciaux, hyperreligieux; 6=Idées de grandeur ou persécution, idées de référence; 8=Délires, hallucinations.",
            9: "Évaluer le comportement agressif, perturbateur ou destructeur (item 0-8). 0=Absent, coopératif; 2=Sarcastique, bruyant par moments; 4=Exigeant, menaces; 6=Menace l'examinateur, cris; 8=Agressif physiquement, destructeur.",
            10: "Évaluer la tenue vestimentaire et le soin corporel. 0=Habillé et soigné de façon appropriée; 2=Minime inattention; 4=Négligé, en partie habillé, maquillage criard.",
            11: "Évaluer la conscience de la maladie et le besoin de traitement. 0=Conscience; 2=Reconnaît possible trouble; 4=Nie totalement la maladie."
        }
        
        questions = []
        
        for i in range(1, 12):
            label, max_value = items_meta[i]
            description = item_descriptions.get(i, "")
            
            # Generate options based on max_value
            options = [{"code": j, "label": str(j), "score": j} for j in range(max_value + 1)]
            
            questions.append({
                "id": f"q{i}",
                "section_id": "sec_items",
                "text": f"{i}. {label}",
                "description": description,
                "type": "integer",
                "required": True,
                "options": options,
                "constraints": {
                    "value_type": "integer",
                    "min_value": 0,
                    "max_value": max_value,
                    "allowed_values": list(range(max_value + 1))
                },
                "rating_note": f"Coté de 0 à {max_value}" + (" (item à double poids)" if max_value == 8 else "")
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
                "label": "Items 1–11",
                "description": "Cotation guidée par entretien clinique",
                "question_ids": [f"q{i}" for i in range(1, 12)],
                "instructions": (
                    "Chaque item doit être coté en se basant sur un entretien clinique et "
                    "l'observation du patient. Items 1,2,3,4,7,10,11 sont cotés de 0 à 4. "
                    "Items 5,6,8,9 sont cotés de 0 à 8 (double poids pour ces symptômes centraux)."
                )
            }
        ]
    
    def validate_answers(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Validate YMRS responses.
        
        Args:
            answers: Dictionary mapping item IDs to response values
        
        Returns:
            Dictionary containing validation results with 'valid', 'errors', and 'warnings' keys
        """
        errors = []
        warnings = []
        
        # Check all 11 items are present
        expected_items = [f"q{i}" for i in range(1, 12)]
        missing = [item for item in expected_items if item not in answers]
        
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Validate response values with correct ranges
        for i in range(1, 12):
            item_id = f"q{i}"
            if item_id not in answers:
                continue
            
            value = answers[item_id]
            
            # Check if it's an integer
            if not isinstance(value, int):
                errors.append(f"{item_id}: la valeur doit être un entier (reçu: {type(value).__name__})")
                continue
            
            # Check range based on item type
            if i in self.ITEMS_0_TO_4:
                if not (0 <= value <= 4):
                    errors.append(f"{item_id}: la valeur doit être entre 0 et 4 (reçu: {value})")
            elif i in self.ITEMS_0_TO_8:
                if not (0 <= value <= 8):
                    errors.append(f"{item_id}: la valeur doit être entre 0 et 8 (reçu: {value})")
        
        # Clinical warnings (only if validation passes)
        if not errors:
            # Calculate total for warning thresholds
            total = sum(answers.get(f"q{i}", 0) for i in range(1, 12))
            
            # Severe mania
            if total >= 35:
                warnings.append(
                    "⚠️ Manie sévère (score ≥ 35). État maniaque majeur nécessitant "
                    "intervention urgente. Risque d'hospitalisation."
                )
            elif total >= self.CUTOFF_MANIA:
                warnings.append(
                    "⚠️ Manie (score ≥ 21). Épisode maniaque caractérisé nécessitant "
                    "traitement actif et surveillance rapprochée."
                )
            elif total >= self.CUTOFF_HYPOMANIA:
                warnings.append(
                    "⚠️ Hypomanie (score 12-20). Symptômes hypomaniaques présents. "
                    "Surveillance et ajustement thérapeutique à considérer."
                )
            
            # Specific high-risk symptoms
            # Aggressive behavior (item 9)
            if answers.get("q9", 0) >= 6:
                warnings.append(
                    "🚨 ALERTE SÉCURITÉ: Comportement agressif important (item 9 ≥ 6). "
                    "Risque de violence. Sécurité du patient et de l'entourage à évaluer. "
                    "Hospitalisation à considérer."
                )
            
            # Severe irritability (item 5)
            if answers.get("q5", 0) >= 6:
                warnings.append(
                    "⚠️ Irritabilité sévère (item 5 ≥ 6). Risque de conflits et "
                    "comportements impulsifs. Surveillance nécessaire."
                )
            
            # Psychotic features (item 8)
            if answers.get("q8", 0) >= 6:
                warnings.append(
                    "⚠️ Caractéristiques psychotiques (item 8 ≥ 6). Idées de grandeur, "
                    "délires ou hallucinations. Considérer ajout d'antipsychotique."
                )
            
            # Severe sleep disturbance (item 4)
            if answers.get("q4", 0) >= 3:
                warnings.append(
                    "⚠️ Réduction majeure du sommeil (item 4 ≥ 3). "
                    "Intervention pour le sommeil nécessaire (risque d'aggravation)."
                )
            
            # Speech pressure (item 6)
            if answers.get("q6", 0) >= 6:
                warnings.append(
                    "⚠️ Pression du discours sévère (item 6 ≥ 6). "
                    "Logorrhée majeure, symptôme de manie sévère."
                )
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def get_severity_category(self, total_score: int) -> str:
        """
        Get severity category based on clinical cutoffs.
        
        Args:
            total_score: Total YMRS score (0-60)
        
        Returns:
            Severity category label
        """
        if total_score <= self.CUTOFF_NO_HYPOMANIA:
            return "Pas d'hypomanie"
        elif total_score <= 20:
            return "Hypomanie"
        else:
            return "Manie"
    
    def calculate_score(
        self,
        answers: Dict[str, int],
        baseline_score: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Calculate YMRS score and interpretation.
        
        Args:
            answers: Dictionary mapping item IDs (q1-q11) to response values
            baseline_score: Optional baseline score for calculating change
        
        Returns:
            Dictionary containing:
                - total_score: Total YMRS score (0-60)
                - severity: Severity category
                - item_scores: Individual item scores
                - remission: Whether score meets remission criteria
                - percent_change: Percent change from baseline (if baseline provided)
                - interpretation: Detailed clinical interpretation
                - warnings: Clinical warnings
        
        Raises:
            YMRSError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation["valid"]:
            raise YMRSError(
                f"Validation échouée: {'; '.join(validation['errors'])}"
            )
        
        # Calculate total score
        total_score = sum(answers.get(f"q{i}", 0) for i in range(1, 12))
        
        # Get severity category
        severity = self.get_severity_category(total_score)
        
        # Check remission
        remission = total_score < self.REMISSION_THRESHOLD
        
        # Calculate percent change if baseline provided
        percent_change = None
        if baseline_score is not None and baseline_score > 0:
            percent_change = round(((baseline_score - total_score) / baseline_score) * 100, 1)
        
        # Collect item scores with names
        item_names = {
            "q1": "Élévation de l'humeur",
            "q2": "Activité motrice et énergie",
            "q3": "Intérêt sexuel",
            "q4": "Sommeil",
            "q5": "Irritabilité",
            "q6": "Discours",
            "q7": "Langage/Pensée",
            "q8": "Contenu",
            "q9": "Comportement agressif",
            "q10": "Apparence",
            "q11": "Introspection"
        }
        
        item_scores = {}
        for i in range(1, 12):
            item_id = f"q{i}"
            max_val = 8 if i in self.ITEMS_0_TO_8 else 4
            item_scores[item_id] = {
                "score": answers.get(item_id, 0),
                "max": max_val,
                "name": item_names[item_id]
            }
        
        # Generate interpretation
        interpretation = self._generate_interpretation(
            total_score,
            severity,
            item_scores,
            remission,
            percent_change,
            baseline_score
        )
        
        return {
            "total_score": total_score,
            "severity": severity,
            "item_scores": item_scores,
            "remission": remission,
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
        percent_change: Optional[float],
        baseline_score: Optional[int]
    ) -> str:
        """Generate comprehensive clinical interpretation."""
        interpretation = "=== YMRS – ÉCHELLE DE MANIE DE YOUNG ===\n\n"
        
        # Summary
        interpretation += "=== RÉSUMÉ ===\n"
        interpretation += f"Score total: {total_score}/60\n"
        interpretation += f"Sévérité: {severity.upper()}\n"
        
        if baseline_score is not None:
            interpretation += f"Score initial (baseline): {baseline_score}/60\n"
            if percent_change is not None:
                interpretation += f"Variation: {percent_change:+.1f}%\n"
        
        interpretation += f"Rémission (score < 12): {'OUI' if remission else 'NON'}\n\n"
        
        # Severity interpretation
        interpretation += "=== INTERPRÉTATION CLINIQUE ===\n"
        
        if total_score <= self.CUTOFF_NO_HYPOMANIA:
            interpretation += (
                "✅ PAS D'HYPOMANIE (Score 0-11)\n\n"
                "Le patient ne présente pas de symptomatologie maniaque ou hypomaniaque "
                "cliniquement significative. Le score se situe dans la fourchette de rémission.\n\n"
                "Recommandations:\n"
                "• Si traitement en cours: Maintenir le traitement thymorégulateur\n"
                "• Surveillance régulière (mensuelle à trimestrielle)\n"
                "• Psychoéducation sur les signes précoces d'hypomanie/manie\n"
                "• Hygiène de sommeil stricte (facteur déclencheur majeur)\n"
                "• Éviter alcool et substances\n"
                "• Plan de prévention de rechute\n"
            )
        elif total_score <= 20:
            interpretation += (
                "🟡 HYPOMANIE (Score 12-20)\n\n"
                "Le patient présente des symptômes hypomaniaques. Élévation légère à modérée "
                "de l'humeur et/ou augmentation de l'activité/énergie, sans altération majeure "
                "du fonctionnement.\n\n"
                "Recommandations:\n"
                "• Évaluation complète du statut thymique\n"
                "• Vérifier l'observance du traitement thymorégulateur\n"
                "• Si sous antidépresseur: ARRÊT ou réduction progressive\n"
                "• Optimiser le thymorégulateur:\n"
                "  - Vérifier lithémie/valproémie si applicable\n"
                "  - Augmenter la dose si sous-optimale\n"
                "  - Considérer ajout d'antipsychotique atypique (quetiapine, olanzapine, aripiprazole)\n"
                "• Renforcer l'hygiène du sommeil (CRUCIAL)\n"
                "• Benzodiazépine temporaire si insomnie/agitation\n"
                "• Suivi rapproché (2-3 fois/semaine)\n"
                "• Réduction des stimulations (travail, activités sociales)\n"
                "• Implication de la famille pour surveillance\n"
                "• Réévaluation dans 3-7 jours\n"
                "• Hospitalisation si aggravation rapide ou insight limité\n"
            )
        else:  # ≥21
            interpretation += (
                "🔴 MANIE (Score ≥ 21)\n\n"
                "Le patient présente un épisode maniaque caractérisé. Altération significative "
                "du fonctionnement social/professionnel. Risque d'actes à conséquences graves.\n\n"
                "Recommandations URGENTES:\n"
                "• 🚨 ÉVALUATION URGENTE DE LA SÉCURITÉ:\n"
                "  - Risque de comportements impulsifs dangereux\n"
                "  - Capacité de jugement altérée\n"
                "  - Risque financier, sexuel, légal\n"
                "  - Risque d'épuisement physique\n"
                "• CONSIDÉRER HOSPITALISATION si:\n"
                "  - Score ≥ 30 (manie sévère)\n"
                "  - Caractéristiques psychotiques\n"
                "  - Comportement agressif/perturbateur\n"
                "  - Insight absent\n"
                "  - Absence de support familial\n"
                "  - Risque pour soi ou autrui\n"
                "• TRAITEMENT MÉDICAMENTEUX INTENSIF:\n"
                "  - ARRÊT IMMÉDIAT de tout antidépresseur\n"
                "  - Thymorégulateur à dose optimale (lithium ou valproate)\n"
                "  - AJOUT D'ANTIPSYCHOTIQUE ATYPIQUE IMPÉRATIF:\n"
                "    · Olanzapine 10-20 mg/j\n"
                "    · Quetiapine 400-800 mg/j\n"
                "    · Rispéridone 2-6 mg/j\n"
                "    · Aripiprazole 15-30 mg/j\n"
                "  - Benzodiazépine (lorazépam, clonazépam) pour agitation/insomnie\n"
                "• MESURES DE SÉCURITÉ:\n"
                "  - Retrait carte bancaire, chéquiers\n"
                "  - Supervision de la conduite automobile\n"
                "  - Protection juridique si nécessaire\n"
                "  - Implication famille/proches (surveillance H24)\n"
                "• SUIVI TRÈS RAPPROCHÉ:\n"
                "  - Quotidien si ambulatoire (avec équipe mobile si disponible)\n"
                "  - Réévaluation tous les 1-2 jours\n"
                "• ARRÊT DE TRAVAIL IMMÉDIAT\n"
                "• Réduction maximale des stimulations\n"
            )
            
            if total_score >= 35:
                interpretation += (
                    "\n⚠️ MANIE SÉVÈRE (Score ≥ 35):\n"
                    "État maniaque très sévère. Hospitalisation fortement recommandée.\n"
                    "Risque majeur d'épuisement, de déshydratation, d'actes à conséquences graves.\n"
                    "Surveillance constante indispensable.\n"
                )
        
        # Change analysis if baseline provided
        if baseline_score is not None and percent_change is not None:
            interpretation += "\n=== ÉVOLUTION DEPUIS BASELINE ===\n"
            interpretation += f"Score initial: {baseline_score}/60\n"
            interpretation += f"Score actuel: {total_score}/60\n"
            interpretation += f"Changement: {total_score - baseline_score:+d} points ({percent_change:+.1f}%)\n\n"
            
            if percent_change <= -50:
                interpretation += (
                    "✅ AMÉLIORATION MAJEURE\n"
                    f"Réduction ≥ 50% du score initial ({abs(percent_change):.1f}% de réduction). "
                    "Excellente réponse thérapeutique.\n\n"
                    "Actions:\n"
                    "• Maintenir le traitement actuel\n"
                    "• Ne pas réduire prématurément (risque de rechute élevé)\n"
                    "• Poursuivre jusqu'à rémission complète (score < 12)\n"
                    "• Traitement d'entretien prolongé (≥ 12 mois minimum)\n"
                )
            elif percent_change <= -25:
                interpretation += (
                    "⚠️ AMÉLIORATION PARTIELLE\n"
                    f"Réduction de {abs(percent_change):.1f}% (insuffisant pour réponse complète).\n\n"
                    "Actions:\n"
                    "• Si < 2 semaines de traitement: Poursuivre et réévaluer\n"
                    "• Si ≥ 2 semaines:\n"
                    "  - Vérifier observance\n"
                    "  - Optimiser posologie si sous-optimale\n"
                    "  - Si monothérapie: Ajouter 2e thymorégulateur ou antipsychotique\n"
                    "  - Si déjà combinaison: Ajuster doses ou changer molécule\n"
                )
            elif percent_change > -10:
                interpretation += (
                    "❌ PAS D'AMÉLIORATION\n"
                    f"Changement minimal ({percent_change:+.1f}%).\n\n"
                    "Actions:\n"
                    "• Vérifier observance strictement\n"
                    "• Vérifier dosages sanguins (lithémie, valproémie)\n"
                    "• Intensifier le traitement:\n"
                    "  - Augmenter doses si sous-optimales\n"
                    "  - Ajouter/changer antipsychotique\n"
                    "  - Considérer clozapine si résistance\n"
                    "• Considérer électroconvulsivothérapie (ECT) si résistance sévère\n"
                    "• Hospitalisation si pas déjà fait\n"
                )
            else:
                interpretation += (
                    "🚨 AGGRAVATION\n"
                    f"Le score a augmenté de {abs(percent_change):.1f}%.\n\n"
                    "Actions URGENTES:\n"
                    "• Réévaluation complète immédiate\n"
                    "• Vérifier observance et interactions\n"
                    "• Hospitalisation à considérer fortement\n"
                    "• Changement thérapeutique urgent\n"
                    "• Évaluer facteurs déclenchants (stress, substances, privation de sommeil)\n"
                )
        
        # Item-by-item analysis
        interpretation += "\n=== ANALYSE PAR ITEM ===\n\n"
        
        # Group items by severity (accounting for different max scores)
        severe_items = []
        moderate_items = []
        mild_items = []
        absent_items = []
        
        for item_id, item_data in item_scores.items():
            score = item_data["score"]
            max_score = item_data["max"]
            name = item_data["name"]
            
            # Calculate percentage of maximum
            pct = (score / max_score * 100) if max_score > 0 else 0
            
            if pct >= 75:  # ≥75% of max
                severe_items.append(f"{name} ({score}/{max_score})")
            elif pct >= 50:  # 50-74% of max
                moderate_items.append(f"{name} ({score}/{max_score})")
            elif pct > 0:  # 1-49% of max
                mild_items.append(f"{name} ({score}/{max_score})")
            else:
                absent_items.append(name)
        
        if severe_items:
            interpretation += "**Symptômes sévères (≥75% du maximum):**\n"
            for item in severe_items:
                interpretation += f"  🔴 {item}\n"
            interpretation += "\n"
        
        if moderate_items:
            interpretation += "**Symptômes modérés (50-74% du maximum):**\n"
            for item in moderate_items:
                interpretation += f"  🟡 {item}\n"
            interpretation += "\n"
        
        if mild_items:
            interpretation += "**Symptômes légers (1-49% du maximum):**\n"
            for item in mild_items:
                interpretation += f"  🟢 {item}\n"
            interpretation += "\n"
        
        # Core symptoms analysis (double-weighted items)
        interpretation += "=== SYMPTÔMES CENTRAUX (Items à double poids 0-8) ===\n\n"
        core_symptoms = {
            "q5": "Irritabilité",
            "q6": "Discours (pression)",
            "q8": "Contenu (idées de grandeur, délires)",
            "q9": "Comportement agressif/perturbateur"
        }
        
        core_total = sum(item_scores[item_id]["score"] for item_id in core_symptoms.keys())
        core_max = 32  # 4 items × 8 points
        core_pct = (core_total / core_max * 100)
        
        interpretation += f"Score des symptômes centraux: {core_total}/{core_max} ({core_pct:.0f}%)\n\n"
        
        for item_id, name in core_symptoms.items():
            score = item_scores[item_id]["score"]
            interpretation += f"  • {name}: {score}/8"
            if score >= 6:
                interpretation += " ⚠️ SÉVÈRE"
            elif score >= 4:
                interpretation += " (modéré)"
            interpretation += "\n"
        
        interpretation += "\n"
        
        if core_pct >= 60:
            interpretation += (
                "⚠️ Les symptômes centraux sont très marqués. Ces symptômes (irritabilité, "
                "pression du discours, contenu psychotique, agressivité) sont les plus "
                "perturbateurs et nécessitent traitement antipsychotique.\n\n"
            )
        
        # Specific clinical points
        interpretation += "=== POINTS CLINIQUES SPÉCIFIQUES ===\n\n"
        
        # Sleep
        sleep_score = item_scores["q4"]["score"]
        if sleep_score >= 3:
            interpretation += (
                f"**Sommeil critique** (Score: {sleep_score}/4)\n"
                "Réduction majeure du besoin de sommeil. Facteur d'aggravation de la manie.\n"
                "Actions: Benzodiazépine, antipsychotique sédatif (quetiapine), hygiène stricte.\n\n"
            )
        
        # Insight
        insight_score = item_scores["q11"]["score"]
        if insight_score >= 3:
            interpretation += (
                f"**Absence d'insight** (Score: {insight_score}/4)\n"
                "Le patient ne reconnaît pas sa maladie. Risque majeur de non-observance.\n"
                "Considérer: Hospitalisation, implication famille, protection juridique.\n\n"
            )
        
        # Psychotic features
        content_score = item_scores["q8"]["score"]
        if content_score >= 6:
            interpretation += (
                f"**Caractéristiques psychotiques** (Score: {content_score}/8)\n"
                "Idées de grandeur ou délires présents. Manie avec caractéristiques psychotiques.\n"
                "Antipsychotique IMPÉRATIF. Doses plus élevées souvent nécessaires.\n\n"
            )
        
        # Aggression
        aggression_score = item_scores["q9"]["score"]
        if aggression_score >= 6:
            interpretation += (
                f"**Comportement agressif majeur** (Score: {aggression_score}/8)\n"
                "Risque immédiat pour le patient et l'entourage.\n"
                "HOSPITALISATION URGENTE recommandée. Sécurité prioritaire.\n\n"
            )
        
        # General notes
        interpretation += (
            "=== NOTES SUR L'UTILISATION DU YMRS ===\n"
            "• Le YMRS est un outil de mesure de sévérité, pas un outil diagnostique\n"
            "• Cotation basée sur entretien clinique et observation (15-30 minutes)\n"
            "• Items 5,6,8,9 sont à double poids (0-8) car symptômes centraux\n"
            "• Items 1,2,3,4,7,10,11 sont cotés 0-4\n"
            "• Réévaluation fréquente en phase aiguë (tous les 1-3 jours)\n"
            "• La rémission (< 12) doit être l'objectif\n"
            "• Traitement d'entretien prolongé essentiel (≥ 12 mois, souvent à vie)\n"
            "• Facteurs déclenchants: privation de sommeil, stress, substances, arrêt traitement\n"
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
                        "id": "presence_all",
                        "level": "error",
                        "message": "Les 11 items doivent être renseignés."
                    },
                    {
                        "id": "ranges_ok",
                        "level": "error",
                        "message": "Respecter les bornes : items {1,2,3,4,7,10,11} ∈ [0..4] ; items {5,6,8,9} ∈ [0..8]."
                    }
                ]
            },
            "scoring": {
                "scales": [
                    {
                        "id": "ymrs_total",
                        "label": "YMRS – Score total (0–60)",
                        "description": "Somme des 11 items (0–60).",
                        "items": [f"q{i}" for i in range(1, 12)],
                        "formula": {"+": [{"var": f"q{i}"} for i in range(1, 12)]},
                        "range": [0, 60],
                        "cutoffs": [
                            {
                                "label": "0–11 : pas d'hypomanie",
                                "rule": {"<=": [{"var": "ymrs_total"}, 11]}
                            },
                            {
                                "label": "12–20 : hypomanie",
                                "rule": {
                                    "and": [
                                        {">=": [{"var": "ymrs_total"}, 12]},
                                        {"<=": [{"var": "ymrs_total"}, 20]}
                                    ]
                                }
                            },
                            {
                                "label": "≥21 : manie",
                                "rule": {">=": [{"var": "ymrs_total"}, 21]}
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

