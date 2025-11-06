"""
État du patient - DSM-IV Current Symptoms Assessment

This module implements a DSM-IV based checklist for assessing current depressive and
manic symptoms. It features a binary/tri-state response format (yes/no/don't know)
with conditional sub-items that appear based on parent item responses.

The questionnaire is designed for rapid clinical assessment of mood state and includes
automatic safety flagging for suicidal ideation.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime


class EtatPatientError(Exception):
    """Custom exception for État du patient errors."""
    pass


class EtatPatient:
    """
    État du patient - DSM-IV Current Symptoms Assessment
    
    A clinician-rated checklist for current depressive and manic symptoms based on
    DSM-IV criteria. Features:
    - 9 main depressive symptom items with conditional sub-items
    - 9 manic symptom items
    - Tri-state responses: Yes (1), No (0), Don't know (9)
    - Conditional visibility for sub-items
    - Automatic safety flagging for suicidal ideation
    
    Scoring:
    - Depressive count: 0-9 (number of positive depressive symptoms)
    - Manic count: 0-9 (number of positive manic symptoms)
    - Safety flag: 0 or 1 (suicidal ideation present)
    
    Attributes:
        id: Unique identifier for the scale
        name: Full name in French
        abbreviation: Short form
        language: Language code
        version: Version number
        reference_period: Time frame for assessment
        description: Brief description of the scale
    """
    
    # Main depressive items
    DEPRESSIVE_ITEMS = [
        "dep_mood",
        "dep_anhedonia",
        "dep_weight_appetite",
        "dep_sleep",
        "dep_psychomotor",
        "dep_fatigue",
        "dep_guilt",
        "dep_concentration",
        "dep_suicide"
    ]
    
    # Manic items
    MANIC_ITEMS = [
        "man_elevated",
        "man_irritable",
        "man_grandeur",
        "man_sleep_need",
        "man_talkative",
        "man_flight",
        "man_distract",
        "man_goal_activity",
        "man_risky"
    ]
    
    # Conditional sub-items (not counted in totals, descriptive only)
    CONDITIONAL_ITEMS = [
        "dep_hyperreact",
        "dep_hyporeact",
        "dep_weight_loss",
        "dep_weight_gain",
        "dep_insomnia",
        "dep_hypersomnia",
        "dep_agitation",
        "dep_retard",
        "dep_idee_accel",
        "dep_idee_ralent"
    ]
    
    # Response codes
    RESPONSE_YES = 1
    RESPONSE_NO = 0
    RESPONSE_DONT_KNOW = 9
    
    def __init__(self):
        """Initialize the État du patient scale."""
        self.id = "EtatPatient.fr"
        self.name = "État du patient – Symptômes actuels (DSM-IV)"
        self.abbreviation = "EtatPatient"
        self.language = "fr-FR"
        self.version = "1.0"
        self.reference_period = "État actuel (au moment de l'évaluation)"
        self.description = (
            "Checklist binaire (oui / non / ne sais pas) des symptômes dépressifs "
            "et maniaques actuels (DSM-IV) avec sous-items conditionnels."
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
            "num_main_items": len(self.DEPRESSIVE_ITEMS) + len(self.MANIC_ITEMS),
            "num_conditional_items": len(self.CONDITIONAL_ITEMS),
            "response_format": "Tri-state: 1=Yes, 0=No, 9=Don't know",
            "sections": ["Depressive symptoms", "Manic symptoms"],
            "features": [
                "Conditional sub-items",
                "Safety flagging (suicidal ideation)",
                "DSM-IV based criteria",
                "Rapid clinical assessment"
            ],
            "scoring": {
                "depressive_count": "0-9 (number of positive depressive symptoms)",
                "manic_count": "0-9 (number of positive manic symptoms)",
                "safety_flag": "0 or 1 (suicidal ideation present)"
            }
        }
    
    def get_questions(self) -> List[Dict[str, Any]]:
        """
        Get all scale items with conditional visibility rules.
        
        Returns:
            List of question dictionaries
        """
        questions = []
        
        # Helper function to create tri-state question
        def create_question(qid: str, section: str, text: str, display_if: Optional[Dict[str, Any]] = None, description: Optional[str] = None) -> Dict[str, Any]:
            # Main questions (without display_if) are always required
            # Conditional sub-questions (with display_if) are required only when visible
            is_conditional = display_if is not None
            
            q = {
                "id": qid,
                "section_id": section,
                "text": text,
                "type": "single_choice",
                "required": not is_conditional,  # Main questions = required, sub-questions = not required by default
                "options": [
                    {"code": 1, "label": "oui", "score": 1},
                    {"code": 0, "label": "non", "score": 0},
                    {"code": 9, "label": "ne sais pas", "score": 0}
                ],
                "constraints": {
                    "value_type": "integer",
                    "allowed_values": [0, 1, 9]
                }
            }
            if description:
                q["description"] = description
            if display_if:
                q["display_if"] = display_if
                # Conditional questions are required only when visible (when display_if evaluates to true)
                q["required_if"] = display_if
            return q
        
        # Depressive symptoms - Main items with descriptions for those with conditional sub-items
        questions.append(create_question("dep_mood", "depression", "Humeur dépressive la majeure partie de la journée", description="Si OUI alors compléter :"))
        questions.append(create_question("dep_anhedonia", "depression", "Diminution marquée d'intérêt ou de plaisir dans toutes ou presque les activités habituelles, presque toute la journée"))
        questions.append(create_question("dep_weight_appetite", "depression", "Perte ou gain de poids significatif, ou diminution ou augmentation de l'appétit", description="Si OUI alors compléter :"))
        questions.append(create_question("dep_sleep", "depression", "Insomnie ou hypersomnie", description="Si OUI alors compléter :"))
        questions.append(create_question("dep_psychomotor", "depression", "Agitation ou ralentissement psychomoteur", description="Si OUI alors compléter :"))
        questions.append(create_question("dep_fatigue", "depression", "Fatigue ou perte d'énergie"))
        questions.append(create_question("dep_guilt", "depression", "Sentiment de dévalorisation ou de culpabilité excessive ou inappropriée"))
        questions.append(create_question("dep_concentration", "depression", "Diminution de l'aptitude à penser ou se concentrer ou indécision chaque jour", description="Si OUI alors compléter :"))
        questions.append(create_question("dep_suicide", "depression", "Pensées récurrentes de mort, idéation suicidaire récurrente sans plan spécifique, ou tentative de suicide ou plan précis pour se suicider"))
        
        # Depressive symptoms - Conditional sub-items (using JSONLogic display_if)
        questions.append(create_question("dep_hyperreact", "depression", "Impression subjective d'hyper-réactivité émotionnelle", 
            display_if={"==": [{"var": "answers.dep_mood"}, 1]}))
        questions.append(create_question("dep_hyporeact", "depression", "Impression subjective d'hypo-réactivité ou d'anesthésie", 
            display_if={"==": [{"var": "answers.dep_mood"}, 1]}))
        questions.append(create_question("dep_weight_loss", "depression", "Perte de poids", 
            display_if={"==": [{"var": "answers.dep_weight_appetite"}, 1]}))
        questions.append(create_question("dep_weight_gain", "depression", "Gain de poids", 
            display_if={"==": [{"var": "answers.dep_weight_appetite"}, 1]}))
        questions.append(create_question("dep_insomnia", "depression", "Insomnie", 
            display_if={"==": [{"var": "answers.dep_sleep"}, 1]}))
        questions.append(create_question("dep_hypersomnia", "depression", "Hypersomnie", 
            display_if={"==": [{"var": "answers.dep_sleep"}, 1]}))
        questions.append(create_question("dep_agitation", "depression", "Agitation", 
            display_if={"==": [{"var": "answers.dep_psychomotor"}, 1]}))
        questions.append(create_question("dep_retard", "depression", "Ralentissement", 
            display_if={"==": [{"var": "answers.dep_psychomotor"}, 1]}))
        questions.append(create_question("dep_idee_accel", "depression", "Impression d'accélération idéïque", 
            display_if={"==": [{"var": "answers.dep_concentration"}, 1]}))
        questions.append(create_question("dep_idee_ralent", "depression", "Impression de ralentissement idéïque", 
            display_if={"==": [{"var": "answers.dep_concentration"}, 1]}))
        
        # Manic symptoms
        manic_main = [
            ("man_elevated", "Humeur élevée, expansive"),
            ("man_irritable", "Humeur irritable"),
            ("man_grandeur", "Augmentation de l'estime de soi ou idées de grandeur"),
            ("man_sleep_need", "Réduction du besoin de sommeil"),
            ("man_talkative", "Plus grande communicabilité que d'habitude ou désir de parler constamment"),
            ("man_flight", "Fuite des idées ou sensation subjective que les pensées défilent"),
            ("man_distract", "Distractibilité : l'attention du sujet étant trop facilement attirée par des stimuli extérieurs sans pertinence"),
            ("man_goal_activity", "Activité dirigée vers un but : augmentation de l'activité ou agitation psychomotrice"),
            ("man_risky", "Engagement excessif dans des activités agréables mais à potentiel élevé de conséquences dommageables")
        ]
        
        for qid, text in manic_main:
            questions.append(create_question(qid, "mania", text))
        
        return questions
    
    def get_sections(self) -> List[Dict[str, Any]]:
        """
        Get scale sections.
        
        Returns:
            List of section dictionaries
        """
        # Build question IDs for each section
        depression_ids = [q["id"] for q in self.get_questions() if q["section_id"] == "depression"]
        mania_ids = [q["id"] for q in self.get_questions() if q["section_id"] == "mania"]
        
        return [
            {
                "id": "depression",
                "label": "Symptômes dépressifs actuels",
                "description": "Évaluation des symptômes dépressifs selon critères DSM-IV",
                "question_ids": depression_ids
            },
            {
                "id": "mania",
                "label": "Symptômes maniaques actuels",
                "description": "Évaluation des symptômes maniaques/hypomaniaques selon critères DSM-IV",
                "question_ids": mania_ids
            }
        ]
    
    def validate_answers(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Validate scale responses.
        
        Args:
            answers: Dictionary mapping item IDs to response values
        
        Returns:
            Dictionary containing validation results with 'valid', 'errors', and 'warnings' keys
        """
        errors = []
        warnings = []
        
        # Check main items are present
        all_main_items = self.DEPRESSIVE_ITEMS + self.MANIC_ITEMS
        missing = [item for item in all_main_items if item not in answers]
        
        if missing:
            errors.append(f"Items principaux manquants: {', '.join(missing)}")
        
        # Validate response values
        for item_id, value in answers.items():
            if not isinstance(value, int):
                errors.append(f"{item_id}: la valeur doit être un entier (reçu: {type(value).__name__})")
            elif value not in [0, 1, 9]:
                errors.append(f"{item_id}: la valeur doit être 0, 1 ou 9 (reçu: {value})")
        
        # Clinical warnings (only if validation passes)
        if not errors:
            # Safety: Suicidal ideation
            if answers.get("dep_suicide") == 1:
                warnings.append(
                    "ALERTE SÉCURITÉ: Idéation suicidaire présente (dep_suicide = oui). "
                    "Évaluation du risque suicidaire immédiate requise. Considérer hospitalisation."
                )
            
            # Count depressive symptoms
            dep_count = sum(1 for item in self.DEPRESSIVE_ITEMS if answers.get(item) == 1)
            if dep_count >= 5:
                warnings.append(
                    f"Critère quantitatif d'épisode dépressif majeur atteint ({dep_count}/9 symptômes). "
                    "Vérifier durée (≥2 semaines), retentissement et exclusion organique."
                )
            elif dep_count >= 2:
                warnings.append(
                    f"Symptomatologie dépressive significative ({dep_count}/9 symptômes). "
                    "Surveillance et évaluation approfondie recommandées."
                )
            
            # Count manic symptoms
            man_count = sum(1 for item in self.MANIC_ITEMS if answers.get(item) == 1)
            if man_count >= 3:
                # Check if elevated/expansive mood or irritable mood is present
                has_mood_change = (answers.get("man_elevated") == 1 or answers.get("man_irritable") == 1)
                if has_mood_change:
                    warnings.append(
                        f"Critère quantitatif d'épisode maniaque/hypomaniaque ({man_count}/9 symptômes "
                        "avec humeur élevée/irritable). Vérifier durée, sévérité et retentissement."
                    )
                else:
                    warnings.append(
                        f"Plusieurs symptômes maniaques ({man_count}/9) sans changement d'humeur caractéristique. "
                        "Évaluation diagnostique approfondie recommandée."
                    )
            
            # Mixed features
            if dep_count >= 3 and man_count >= 3:
                warnings.append(
                    "⚠️ CARACTÉRISTIQUES MIXTES: Présence simultanée de symptômes dépressifs "
                    "et maniaques significatifs. Évaluer pour épisode mixte ou trouble bipolaire."
                )
            
            # Check for "don't know" responses
            dont_know_items = [item for item in all_main_items if answers.get(item) == 9]
            if dont_know_items:
                warnings.append(
                    f"Réponses 'ne sais pas' pour {len(dont_know_items)} item(s): {', '.join(dont_know_items)}. "
                    "Information incomplète - considérer sources collatérales ou réévaluation."
                )
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def calculate_score(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Calculate État du patient scores.
        
        Args:
            answers: Dictionary mapping item IDs to response values
        
        Returns:
            Dictionary containing:
                - depressive_count: Number of positive depressive symptoms (0-9)
                - manic_count: Number of positive manic symptoms (0-9)
                - safety_flag: 1 if suicidal ideation present, 0 otherwise
                - depressive_symptoms: List of positive depressive symptoms
                - manic_symptoms: List of positive manic symptoms
                - interpretation: Clinical interpretation
                - warnings: Clinical warnings
        
        Raises:
            EtatPatientError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation["valid"]:
            raise EtatPatientError(
                f"Validation échouée: {'; '.join(validation['errors'])}"
            )
        
        # Calculate depressive count (only "yes" responses, "don't know" = 0)
        depressive_count = sum(1 for item in self.DEPRESSIVE_ITEMS if answers.get(item) == 1)
        depressive_symptoms = [item for item in self.DEPRESSIVE_ITEMS if answers.get(item) == 1]
        
        # Calculate manic count
        manic_count = sum(1 for item in self.MANIC_ITEMS if answers.get(item) == 1)
        manic_symptoms = [item for item in self.MANIC_ITEMS if answers.get(item) == 1]
        
        # Safety flag
        safety_flag = 1 if answers.get("dep_suicide") == 1 else 0
        
        # Generate interpretation
        interpretation = self._generate_interpretation(
            depressive_count,
            manic_count,
            safety_flag,
            depressive_symptoms,
            manic_symptoms,
            answers
        )
        
        return {
            "depressive_count": depressive_count,
            "manic_count": manic_count,
            "safety_flag": safety_flag,
            "depressive_symptoms": depressive_symptoms,
            "manic_symptoms": manic_symptoms,
            "conditional_items": {
                item: answers.get(item) for item in self.CONDITIONAL_ITEMS if item in answers
            },
            "interpretation": interpretation,
            "warnings": validation["warnings"],
            "calculation_date": datetime.utcnow().isoformat() + "Z"
        }
    
    def _generate_interpretation(
        self,
        depressive_count: int,
        manic_count: int,
        safety_flag: int,
        depressive_symptoms: List[str],
        manic_symptoms: List[str],
        answers: Dict[str, int]
    ) -> str:
        """Generate clinical interpretation."""
        interpretation = "=== ÉTAT DU PATIENT – SYMPTÔMES ACTUELS (DSM-IV) ===\n\n"
        
        # Summary
        interpretation += "=== RÉSUMÉ ===\n"
        interpretation += f"Symptômes dépressifs: {depressive_count}/9\n"
        interpretation += f"Symptômes maniaques: {manic_count}/9\n"
        interpretation += f"Alerte sécurité (idéation suicidaire): {'OUI' if safety_flag == 1 else 'NON'}\n\n"
        
        # Safety alert
        if safety_flag == 1:
            interpretation += (
                "ALERTE SÉCURITÉ - IDÉATION SUICIDAIRE PRÉSENTE\n"
                "================================================================================\n"
                "Le patient présente des pensées de mort, idéation suicidaire, tentative ou plan.\n\n"
                "ACTIONS IMMÉDIATES REQUISES:\n"
                "• Évaluation approfondie du risque suicidaire (méthode, plan, accès aux moyens)\n"
                "• Évaluation de la létalité et intentionnalité\n"
                "• Identifier facteurs de risque et facteurs protecteurs\n"
                "• Considérer FORTEMENT l'hospitalisation si risque élevé\n"
                "• Retrait des moyens létaux de l'environnement\n"
                "• Mise en place surveillance rapprochée\n"
                "• Contact avec proches/réseau de soutien\n"
                "• Plan de sécurité détaillé si maintien ambulatoire\n"
                "• Documentation médico-légale complète\n"
                "• NE PAS laisser le patient seul si risque imminent\n\n"
                "================================================================================\n\n"
            )
        
        # Depressive symptoms analysis
        interpretation += "=== SYMPTÔMES DÉPRESSIFS ===\n"
        interpretation += f"Nombre de symptômes présents: {depressive_count}/9\n\n"
        
        if depressive_count == 0:
            interpretation += "Aucun symptôme dépressif actuel rapporté.\n"
        elif depressive_count >= 5:
            has_core_symptom = (
                answers.get("dep_mood") == 1 or
                answers.get("dep_anhedonia") == 1
            )
            interpretation += (
                "ÉPISODE DÉPRESSIF MAJEUR (Critère quantitatif DSM-IV atteint)\n\n"
                f"Le patient présente {depressive_count} symptômes dépressifs, "
                "dépassant le seuil de 5 symptômes requis pour un épisode dépressif majeur.\n\n"
            )
            if has_core_symptom:
                interpretation += "✓ Au moins un symptôme cardinal présent (humeur dépressive ou anhédonie)\n"
            else:
                interpretation += "⚠️ Aucun symptôme cardinal (humeur dépressive ou anhédonie) présent. Vérifier l'évaluation.\n"
            interpretation += (
                "\nPOUR DIAGNOSTIC D'ÉPISODE DÉPRESSIF MAJEUR, vérifier également:\n"
                "• Durée: symptômes présents presque toute la journée, presque tous les jours, ≥ 2 semaines\n"
                "• Retentissement: souffrance cliniquement significative ou altération fonctionnement\n"
                "• Exclusions: non dû à substances, condition médicale, ou deuil normal\n"
                "• Au moins 1 symptôme cardinal (humeur dépressive OU anhédonie) doit être présent\n"
            )
        elif depressive_count >= 2:
            interpretation += (
                "SYMPTOMATOLOGIE DÉPRESSIVE SIGNIFICATIVE\n\n"
                f"Le patient présente {depressive_count} symptômes dépressifs. "
                "Bien que le seuil d'épisode dépressif majeur (5 symptômes) ne soit pas atteint, "
                "cette symptomatologie nécessite surveillance et évaluation.\n\n"
                "Considérations:\n"
                "• Épisode dépressif mineur (2-4 symptômes, incluant humeur ou anhédonie)\n"
                "• Symptômes résiduels d'épisode antérieur\n"
                "• Dysthymie / trouble dépressif persistant\n"
                "• Phase prodromique d'épisode dépressif majeur\n"
            )
        else:
            interpretation += (
                f"Symptomatologie dépressive légère ({depressive_count} symptôme{'s' if depressive_count > 1 else ''}).\n"
                "Surveillance recommandée.\n"
            )
        
        # List positive depressive symptoms
        if depressive_symptoms:
            interpretation += "\nSymptômes dépressifs présents:\n"
            symptom_labels = {
                "dep_mood": "Humeur dépressive",
                "dep_anhedonia": "Anhédonie (diminution marquée d'intérêt/plaisir)",
                "dep_weight_appetite": "Changement poids/appétit",
                "dep_sleep": "Trouble du sommeil",
                "dep_psychomotor": "Trouble psychomoteur",
                "dep_fatigue": "Fatigue/perte d'énergie",
                "dep_guilt": "Sentiment de dévalorisation/culpabilité",
                "dep_concentration": "Trouble concentration/indécision",
                "dep_suicide": "Pensées récurrentes de mort / idéation suicidaire"
            }
            for symptom in depressive_symptoms:
                interpretation += f"  • {symptom_labels.get(symptom, symptom)}\n"
            
            # Add conditional details if available
            interpretation += "\nDétails conditionnels:\n"
            if answers.get("dep_mood") == 1:
                if answers.get("dep_hyperreact") == 1:
                    interpretation += "  - Hyper-réactivité émotionnelle\n"
                if answers.get("dep_hyporeact") == 1:
                    interpretation += "  - Hypo-réactivité / anesthésie émotionnelle\n"
            if answers.get("dep_weight_appetite") == 1:
                if answers.get("dep_weight_loss") == 1:
                    interpretation += "  - Perte de poids\n"
                if answers.get("dep_weight_gain") == 1:
                    interpretation += "  - Gain de poids\n"
            if answers.get("dep_sleep") == 1:
                if answers.get("dep_insomnia") == 1:
                    interpretation += "  - Insomnie\n"
                if answers.get("dep_hypersomnia") == 1:
                    interpretation += "  - Hypersomnie\n"
            if answers.get("dep_psychomotor") == 1:
                if answers.get("dep_agitation") == 1:
                    interpretation += "  - Agitation psychomotrice\n"
                if answers.get("dep_retard") == 1:
                    interpretation += "  - Ralentissement psychomoteur\n"
            if answers.get("dep_concentration") == 1:
                if answers.get("dep_idee_accel") == 1:
                    interpretation += "  - Accélération idéique\n"
                if answers.get("dep_idee_ralent") == 1:
                    interpretation += "  - Ralentissement idéique\n"
        
        # Manic symptoms analysis
        interpretation += "\n\n=== SYMPTÔMES MANIAQUES/HYPOMANIAQUES ===\n"
        interpretation += f"Nombre de symptômes présents: {manic_count}/9\n\n"
        
        if manic_count == 0:
            interpretation += "Aucun symptôme maniaque actuel rapporté.\n"
        elif manic_count >= 3:
            has_mood_change = (
                answers.get("man_elevated") == 1 or
                answers.get("man_irritable") == 1
            )
            interpretation += (
                "SYMPTOMATOLOGIE MANIAQUE/HYPOMANIAQUE SIGNIFICATIVE\n\n"
                f"Le patient présente {manic_count} symptômes maniaques, "
                "dépassant le seuil de 3 symptômes (en plus du changement d'humeur) "
                "requis pour un épisode maniaque/hypomaniaque.\n\n"
            )
            if has_mood_change:
                mood_type = []
                if answers.get("man_elevated") == 1:
                    mood_type.append("humeur élevée/expansive")
                if answers.get("man_irritable") == 1:
                    mood_type.append("humeur irritable")
                interpretation += f"✓ Changement d'humeur présent: {' et '.join(mood_type)}\n"
            else:
                interpretation += (
                    "⚠️ ATTENTION: Aucun changement d'humeur caractéristique (élevée/expansive ou irritable) rapporté.\n"
                    "Le changement d'humeur est REQUIS pour le diagnostic d'épisode maniaque/hypomaniaque.\n"
                )
            interpretation += (
                "\nPOUR DIAGNOSTIC D'ÉPISODE MANIAQUE/HYPOMANIAQUE, vérifier:\n"
                "• Humeur: élevée, expansive OU irritable de manière anormale et persistante\n"
                "• Durée: ≥ 1 semaine (manie) ou ≥ 4 jours (hypomanie)\n"
                "• Sévérité: hospitalisation nécessaire OU altération marquée = MANIE\n"
                "           observable mais sans hospitalisation/psychose = HYPOMANIE\n"
                "• Retentissement: altération marquée du fonctionnement (manie)\n"
                "• Exclusions: non dû à substances ou condition médicale\n"
                "• Nombre: ≥ 3 symptômes (≥ 4 si humeur uniquement irritable)\n"
            )
        elif manic_count >= 1:
            interpretation += (
                f"Symptomatologie maniaque légère ({manic_count} symptôme{'s' if manic_count > 1 else ''}).\n"
                "Insuffisant pour épisode maniaque/hypomaniaque. Surveillance recommandée.\n"
            )
        else:
            interpretation += "Aucun symptôme maniaque.\n"
        
        # List positive manic symptoms
        if manic_symptoms:
            interpretation += "\nSymptômes maniaques présents:\n"
            symptom_labels = {
                "man_elevated": "Humeur élevée, expansive",
                "man_irritable": "Humeur irritable",
                "man_grandeur": "Augmentation de l'estime de soi ou idées de grandeur",
                "man_sleep_need": "Réduction besoin de sommeil",
                "man_talkative": "Plus grande communicabilité que d'habitude",
                "man_flight": "Fuite des idées ou sensation que les pensées défilent",
                "man_distract": "Distractibilité",
                "man_goal_activity": "Activité dirigée vers un but : augmentation activité",
                "man_risky": "Engagement excessif activités à potentiel de conséquences dommageables"
            }
            for symptom in manic_symptoms:
                interpretation += f"  • {symptom_labels.get(symptom, symptom)}\n"
        
        # Mixed features
        if depressive_count >= 3 and manic_count >= 3:
            interpretation += (
                "\n\nCARACTÉRISTIQUES MIXTES\n"
                "================================================================================\n"
                "Le patient présente simultanément des symptômes dépressifs ET maniaques significatifs.\n\n"
                "Considérations diagnostiques:\n"
                "• Épisode dépressif majeur avec caractéristiques mixtes\n"
                "• Épisode maniaque avec caractéristiques mixtes\n"
                "• Trouble bipolaire type I ou II\n"
                "• États mixtes (dysphorie maniaque)\n\n"
                "Implications cliniques:\n"
                "• Risque suicidaire accru (énergie + désespoir)\n"
                "• Réponse différente aux traitements (éviter antidépresseurs seuls)\n"
                "• Nécessité thymorégulateurs\n"
                "• Pronostic et prise en charge spécifiques\n"
                "================================================================================\n"
            )
        
        # Clinical recommendations
        interpretation += "\n\n=== RECOMMANDATIONS CLINIQUES ===\n"
        
        if safety_flag == 1:
            interpretation += "1. PRIORITÉ: Évaluation risque suicidaire et mesures de sécurité immédiates\n"
        
        if depressive_count >= 5:
            interpretation += "2. Évaluation diagnostique complète pour épisode dépressif majeur\n"
            interpretation += "3. Traitement antidépresseur (sauf si caractéristiques mixtes/bipolaires)\n"
            interpretation += "4. Psychothérapie (TCC, TIP recommandées)\n"
        elif depressive_count >= 2:
            interpretation += "2. Surveillance de l'évolution symptomatique\n"
            interpretation += "3. Considérer interventions précoces (psychothérapie, psychoéducation)\n"
        
        if manic_count >= 3:
            interpretation += "• Évaluation pour trouble bipolaire\n"
            interpretation += "• Considérer thymorégulateurs (éviter antidépresseurs seuls)\n"
            interpretation += "• Évaluation du retentissement fonctionnel et nécessité hospitalisation\n"
        
        if depressive_count >= 3 and manic_count >= 3:
            interpretation += "• Consultation psychiatrique spécialisée recommandée (états mixtes)\n"
            interpretation += "• Thymorégulateurs en première intention\n"
            interpretation += "• Surveillance rapprochée du risque suicidaire\n"
        
        interpretation += (
            "\n=== NOTES IMPORTANTES ===\n"
            "• Ces critères quantitatifs sont NÉCESSAIRES mais NON SUFFISANTS pour le diagnostic\n"
            "• Vérifier TOUJOURS: durée, retentissement, exclusion causes organiques/substances\n"
            "• Le diagnostic DSM-IV/5 nécessite une évaluation clinique complète\n"
            "• Cette évaluation représente un POINT DANS LE TEMPS, documenter l'évolution\n"
            "• Les sous-items conditionnels sont descriptifs et enrichissent l'évaluation clinique\n"
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
                        "id": "response_values",
                        "level": "error",
                        "message": "Les réponses doivent être 0 (non), 1 (oui) ou 9 (ne sais pas)."
                    },
                    {
                        "id": "safety_alert",
                        "level": "critical",
                        "message": "Idéation suicidaire détectée - évaluation risque immédiate requise."
                    }
                ]
            },
            "scoring": {
                "variables": [],
                "scales": [
                    {
                        "id": "depressive_count",
                        "label": "Nombre de symptômes dépressifs (principaux)",
                        "items": self.DEPRESSIVE_ITEMS,
                        "formula": {"+": [{"var": item} for item in self.DEPRESSIVE_ITEMS]},
                        "range": [0, len(self.DEPRESSIVE_ITEMS)]
                    },
                    {
                        "id": "manic_count",
                        "label": "Nombre de symptômes maniaques",
                        "items": self.MANIC_ITEMS,
                        "formula": {"+": [{"var": item} for item in self.MANIC_ITEMS]},
                        "range": [0, len(self.MANIC_ITEMS)]
                    },
                    {
                        "id": "safety_flag",
                        "label": "Drapeau sécurité (idéation suicidaire)",
                        "items": ["dep_suicide"],
                        "formula": {"if": [{"==": [{"var": "dep_suicide"}, 1]}, 1, 0]},
                        "range": [0, 1]
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

