"""
WURS-25 (Wender Utah Rating Scale - 25 item version)

This module implements the WURS-25, a 25-item retrospective self-report questionnaire
for assessing childhood ADHD symptoms. Items are rated on a 5-point scale (0-4).
"""

from typing import Dict, List, Optional, Any
from datetime import datetime


class WURS25Error(Exception):
    """Custom exception for WURS-25 questionnaire errors."""
    pass


class WURS25:
    """
    WURS-25 (Wender Utah Rating Scale - 25 item version)
    
    A 25-item retrospective self-report questionnaire assessing childhood
    ADHD symptoms. Respondents rate how well each statement described them
    as a child/adolescent on a 0-4 scale.
    
    Attributes:
        id: Unique identifier for the questionnaire
        name: Full name in French
        abbreviation: Short form (WURS-25)
        language: Language code
        version: Version number
        reference_period: Time frame for responses (retrospective childhood)
        description: Brief description of the questionnaire
    """
    
    # Item IDs from the full WURS that are included in WURS-25
    ITEM_IDS = [3, 4, 5, 6, 7, 9, 10, 11, 12, 15, 16, 17, 20, 21, 24, 
                25, 26, 27, 28, 29, 40, 41, 51, 56, 59]
    
    # Item texts in French (keyed by original item numbers)
    ITEM_TEXTS = {
        3: "Des problèmes de concentration, facilement distrait(e)",
        4: "Anxieux(se), se faisant du souci",
        5: "Nerveux, ne tenant pas en place",
        6: "Inattentif(ve), rêveur(se)",
        7: "Facilement en colère, « soupe au lait »",
        9: "Des éclats d'humeur, des accès de colère",
        10: "Des difficultés à me tenir aux choses, à mener mes projets jusqu'à la fin, à finir les choses commencées",
        11: "Têtu(e), obstiné(e)",
        12: "Triste ou cafardeux(se), déprimé(e), malheureux(se)",
        15: "Désobéissant(e) à mes parents, rebelle, effronté(e)",
        16: "Une mauvaise opinion de moi-même",
        17: "Irritable",
        20: "D'humeur changeante, avec des hauts et des bas",
        21: "En colère",
        24: "Impulsif(ve), agissant sans réfléchir",
        25: "Tendance à être immature",
        26: "Culpabilisé(e), plein(e) de regrets",
        27: "Je pouvais perdre le contrôle de moi-même",
        28: "Tendance à être ou à agir de façon irrationnelle",
        29: "Impopulaire auprès des autres enfants ; je ne gardais pas longtemps mes amis ou je ne m'entendais pas avec les autres enfants",
        40: "Du mal à voir les choses du point de vue de quelqu'un d'autre",
        41: "Des ennuis avec les autorités, des ennuis à l'école ; convoqué(e) par le directeur",
        51: "Dans l'ensemble un élève peu doué, apprenant lentement",
        56: "Des difficultés en mathématiques ou avec les chiffres",
        59: "En dessous de son potentiel"
    }
    
    # Response options (0-4)
    RESPONSE_OPTIONS = [
        {"code": 0, "label": "0 – Pas du tout ou très légèrement", "score": 0},
        {"code": 1, "label": "1 – Légèrement", "score": 1},
        {"code": 2, "label": "2 – Modérément", "score": 2},
        {"code": 3, "label": "3 – Assez", "score": 3},
        {"code": 4, "label": "4 – Beaucoup", "score": 4}
    ]
    
    # Clinical cut-off (typically 46 for adults, but can vary by study)
    CLINICAL_CUTOFF = 46
    
    def __init__(self):
        """Initialize the WURS-25 questionnaire."""
        self.id = "WURS-25.fr"
        self.name = "Wender Utah Rating Scale – Version courte 25 items (FR)"
        self.abbreviation = "WURS-25"
        self.language = "fr-FR"
        self.version = "1.0"
        self.reference_period = "Enfance et/ou adolescence (rétrospectif)"
        self.description = (
            "Auto-questionnaire rétrospectif de 25 items (Likert 0–4) pour la "
            "symptomatologie du TDAH dans l'enfance. Score total 0–100."
        )
    
    def get_metadata(self) -> Dict[str, Any]:
        """
        Get questionnaire metadata.
        
        Returns:
            Dictionary containing questionnaire metadata
        """
        return {
            "id": self.id,
            "name": self.name,
            "abbreviation": self.abbreviation,
            "language": self.language,
            "version": self.version,
            "reference_period": self.reference_period,
            "description": self.description,
            "num_items": 25,
            "response_scale": "5-point scale (0=Pas du tout ou très légèrement to 4=Beaucoup)",
            "score_range": [0, 100],
            "score_type": "sum",
            "clinical_cutoff": self.CLINICAL_CUTOFF,
            "item_ids": self.ITEM_IDS
        }
    
    def get_questions(self) -> List[Dict[str, Any]]:
        """
        Get all questionnaire items.
        
        Returns:
            List of question dictionaries
        """
        questions = []
        for item_id in self.ITEM_IDS:
            question = {
                "id": f"q{item_id}",
                "number": item_id,
                "section_id": "sec1",
                "text": f"{item_id}. {self.ITEM_TEXTS[item_id]}",
                "type": "single_choice",
                "required": True,
                "options": self.RESPONSE_OPTIONS.copy()
            }
            questions.append(question)
        return questions
    
    def get_sections(self) -> List[Dict[str, Any]]:
        """
        Get questionnaire sections.
        
        Returns:
            List of section dictionaries
        """
        return [
            {
                "id": "sec1",
                "label": "WURS-25 – 25 items (0..4)",
                "description": (
                    "Évaluez à quel point chaque énoncé vous décrivait dans l'enfance/adolescence "
                    "(0=Pas du tout ou très légèrement … 4=Beaucoup)"
                ),
                "question_ids": [f"q{i}" for i in self.ITEM_IDS]
            }
        ]
    
    def validate_answers(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Validate questionnaire responses.
        
        Args:
            answers: Dictionary mapping question IDs to response values (0-4)
        
        Returns:
            Dictionary containing validation results with 'valid', 'errors', and 'warnings' keys
        
        Raises:
            WURS25Error: If validation fails critically
        """
        errors = []
        warnings = []
        
        # Check all 25 items are present
        expected_items = [f"q{i}" for i in self.ITEM_IDS]
        missing = [qid for qid in expected_items if qid not in answers]
        
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Validate each response value
        for qid in expected_items:
            if qid in answers:
                value = answers[qid]
                if not isinstance(value, int):
                    errors.append(f"{qid}: la valeur doit être un entier (reçu: {type(value).__name__})")
                elif value < 0 or value > 4:
                    errors.append(f"{qid}: la valeur doit être entre 0 et 4 (reçu: {value})")
        
        # Check for unusual patterns
        if not errors:
            # All zeros (unlikely childhood ADHD)
            if all(answers.get(f"q{i}", -1) == 0 for i in self.ITEM_IDS):
                warnings.append(
                    "Toutes les réponses sont à 0. Cela suggère une absence totale de symptômes "
                    "TDAH dans l'enfance, ce qui est inhabituel pour un dépistage."
                )
            
            # All maximum (possible exaggeration or severe symptoms)
            elif all(answers.get(f"q{i}", -1) == 4 for i in self.ITEM_IDS):
                warnings.append(
                    "Toutes les réponses sont à 4 (maximum). Vérifier la compréhension des "
                    "instructions ou la possibilité d'exagération des symptômes."
                )
            
            # Very low variance (same answer for most items)
            elif len(set(answers.values())) <= 2:
                warnings.append(
                    "Variance très faible dans les réponses. Vérifier que le patient a bien "
                    "différencié les items."
                )
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def calculate_score(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Calculate WURS-25 score.
        
        Args:
            answers: Dictionary mapping question IDs (q3-q59) to response values (0-4)
        
        Returns:
            Dictionary containing:
                - total_score: Total sum score (0-100)
                - clinical_significance: Whether score exceeds clinical cutoff
                - severity_level: Severity classification
                - item_scores: Individual item scores
                - interpretation: Clinical interpretation
        
        Raises:
            WURS25Error: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation["valid"]:
            raise WURS25Error(
                f"Validation échouée: {'; '.join(validation['errors'])}"
            )
        
        # Calculate total score (simple sum, no reverse coding)
        total_score = sum(answers[f"q{i}"] for i in self.ITEM_IDS)
        
        # Determine clinical significance
        clinical_significance = total_score >= self.CLINICAL_CUTOFF
        
        # Determine severity level
        severity_level = self._get_severity(total_score)
        
        # Collect item scores with symptom domains
        item_scores = {}
        for item_id in self.ITEM_IDS:
            qid = f"q{item_id}"
            item_scores[qid] = {
                "score": answers[qid],
                "text": self.ITEM_TEXTS[item_id],
                "domain": self._get_symptom_domain(item_id)
            }
        
        # Calculate domain scores (informal grouping)
        domain_scores = self._calculate_domain_scores(answers)
        
        # Generate interpretation
        interpretation = self._generate_interpretation(
            total_score,
            clinical_significance,
            severity_level,
            domain_scores
        )
        
        return {
            "total_score": total_score,
            "score_range": [0, 100],
            "clinical_cutoff": self.CLINICAL_CUTOFF,
            "clinical_significance": clinical_significance,
            "severity_level": severity_level,
            "domain_scores": domain_scores,
            "item_scores": item_scores,
            "interpretation": interpretation,
            "warnings": validation["warnings"],
            "calculation_date": datetime.utcnow().isoformat() + "Z"
        }
    
    def _get_severity(self, score: int) -> str:
        """
        Get severity level based on total score.
        
        Args:
            score: Total score (0-100)
        
        Returns:
            Severity level label
        """
        if score < 25:
            return "Minimal ou absent"
        elif score < 36:
            return "Léger"
        elif score < 46:
            return "Modéré"
        elif score < 60:
            return "Significatif"
        else:
            return "Sévère"
    
    def _get_symptom_domain(self, item_id: int) -> str:
        """
        Classify item into informal symptom domain.
        
        Args:
            item_id: Item number
        
        Returns:
            Domain label
        """
        # Inattention/concentration
        if item_id in [3, 6, 10, 51, 56]:
            return "Inattention"
        # Hyperactivity/impulsivity
        elif item_id in [5, 24, 27, 28]:
            return "Hyperactivité/Impulsivité"
        # Emotional dysregulation
        elif item_id in [7, 9, 17, 20, 21]:
            return "Dysrégulation émotionnelle"
        # Mood/anxiety
        elif item_id in [4, 12, 26]:
            return "Humeur/Anxiété"
        # Social difficulties
        elif item_id in [29, 40]:
            return "Difficultés sociales"
        # Behavioral problems
        elif item_id in [11, 15, 41]:
            return "Problèmes comportementaux"
        # Self-esteem
        elif item_id in [16, 25, 59]:
            return "Estime de soi"
        else:
            return "Autre"
    
    def _calculate_domain_scores(self, answers: Dict[str, int]) -> Dict[str, Dict[str, Any]]:
        """
        Calculate informal domain scores for interpretation.
        
        Args:
            answers: Dictionary of answers
        
        Returns:
            Dictionary of domain scores
        """
        domains = {
            "Inattention": [3, 6, 10, 51, 56],
            "Hyperactivité/Impulsivité": [5, 24, 27, 28],
            "Dysrégulation émotionnelle": [7, 9, 17, 20, 21],
            "Humeur/Anxiété": [4, 12, 26],
            "Difficultés sociales": [29, 40],
            "Problèmes comportementaux": [11, 15, 41],
            "Estime de soi": [16, 25, 59]
        }
        
        domain_scores = {}
        for domain, items in domains.items():
            score = sum(answers[f"q{i}"] for i in items)
            max_score = len(items) * 4
            mean = score / len(items)
            domain_scores[domain] = {
                "score": score,
                "max_score": max_score,
                "mean": round(mean, 2),
                "items": items
            }
        
        return domain_scores
    
    def _generate_interpretation(
        self,
        total_score: int,
        clinical_significance: bool,
        severity: str,
        domain_scores: Dict[str, Dict[str, Any]]
    ) -> str:
        """
        Generate clinical interpretation based on scores.
        
        Args:
            total_score: Total WURS-25 score
            clinical_significance: Whether score exceeds cutoff
            severity: Severity level
            domain_scores: Scores by symptom domain
        
        Returns:
            Clinical interpretation text in French
        """
        interpretation = f"Score total WURS-25: {total_score}/100\n"
        interpretation += f"Sévérité: {severity}\n\n"
        
        # Clinical significance
        if clinical_significance:
            interpretation += (
                f"⚠️ CLINIQUEMENT SIGNIFICATIF (score ≥ {self.CLINICAL_CUTOFF})\n"
                "Le score suggère une symptomatologie TDAH significative dans l'enfance/adolescence.\n\n"
            )
        else:
            interpretation += (
                f"Score sous le seuil clinique (< {self.CLINICAL_CUTOFF})\n"
                "Le score ne suggère pas de TDAH significatif dans l'enfance, ou les symptômes "
                "étaient minimes.\n\n"
            )
        
        # Overall interpretation by severity
        interpretation += "=== INTERPRÉTATION GLOBALE ===\n"
        if total_score < 25:
            interpretation += (
                "Symptômes TDAH de l'enfance MINIMAUX ou ABSENTS.\n"
                "Le patient ne rapporte pas ou très peu de symptômes typiques du TDAH durant "
                "l'enfance/adolescence. Cela ne supporte pas un diagnostic de TDAH à début infantile.\n"
            )
        elif total_score < 36:
            interpretation += (
                "Symptômes TDAH de l'enfance LÉGERS.\n"
                "Le patient rapporte quelques symptômes compatibles avec le TDAH mais d'intensité "
                "faible. Ces symptômes peuvent avoir été présents sans entraîner de déficience significative.\n"
            )
        elif total_score < 46:
            interpretation += (
                "Symptômes TDAH de l'enfance MODÉRÉS.\n"
                "Le patient rapporte des symptômes notables mais sous le seuil clinique habituel. "
                "Une évaluation clinique approfondie est recommandée pour déterminer si les critères "
                "diagnostiques du TDAH sont remplis.\n"
            )
        elif total_score < 60:
            interpretation += (
                "Symptômes TDAH de l'enfance SIGNIFICATIFS.\n"
                "⚠️ Le patient rapporte des symptômes importants compatibles avec un TDAH dans l'enfance. "
                "Ce score supporte fortement un diagnostic de TDAH à début infantile persistant à l'âge adulte.\n"
            )
        else:
            interpretation += (
                "Symptômes TDAH de l'enfance SÉVÈRES.\n"
                "⚠️ Le patient rapporte des symptômes très importants et pervasifs du TDAH dans l'enfance. "
                "Ce score suggère un TDAH sévère avec impact majeur durant l'enfance/adolescence.\n"
            )
        
        # Domain analysis
        interpretation += "\n=== ANALYSE PAR DOMAINE SYMPTOMATIQUE ===\n"
        
        # Sort domains by mean score
        sorted_domains = sorted(
            domain_scores.items(),
            key=lambda x: x[1]["mean"],
            reverse=True
        )
        
        for domain, scores in sorted_domains:
            mean = scores["mean"]
            interpretation += f"\n• {domain}: {scores['score']}/{scores['max_score']} (moyenne: {mean:.2f}/4)\n"
            
            if mean >= 3.0:
                interpretation += "  ➜ Symptômes TRÈS MARQUÉS dans ce domaine\n"
            elif mean >= 2.0:
                interpretation += "  ➜ Symptômes MARQUÉS dans ce domaine\n"
            elif mean >= 1.0:
                interpretation += "  ➜ Symptômes MODÉRÉS dans ce domaine\n"
            else:
                interpretation += "  ➜ Symptômes LÉGERS ou absents dans ce domaine\n"
        
        # Clinical recommendations
        interpretation += "\n=== RECOMMANDATIONS CLINIQUES ===\n"
        
        if clinical_significance:
            interpretation += (
                "• Évaluation diagnostique complète du TDAH adulte recommandée\n"
                "• Entretien clinique structuré (DIVA, CAADID)\n"
                "• Évaluation des symptômes TDAH actuels (ASRS, échelles adultes)\n"
                "• Bilan neuropsychologique (fonctions exécutives, attention)\n"
                "• Recherche de comorbidités (anxiété, dépression, troubles bipolaires)\n"
                "• Évaluation du retentissement fonctionnel (travail, relations, vie quotidienne)\n"
            )
            
            # Domain-specific recommendations
            if domain_scores["Dysrégulation émotionnelle"]["mean"] >= 2.5:
                interpretation += "• ⚠️ Dysrégulation émotionnelle marquée - évaluer troubles de l'humeur\n"
            
            if domain_scores["Difficultés sociales"]["mean"] >= 2.5:
                interpretation += "• ⚠️ Difficultés sociales importantes - considérer trouble du spectre autistique\n"
            
            if domain_scores["Humeur/Anxiété"]["mean"] >= 2.5:
                interpretation += "• ⚠️ Symptômes anxio-dépressifs - dépistage comorbidités affectives\n"
        else:
            if total_score >= 36:
                interpretation += (
                    "• Bien que sous le seuil, une évaluation clinique peut être justifiée si "
                    "des symptômes TDAH actuels sont présents\n"
                    "• Compléter avec échelles TDAH adulte actuelles (ASRS)\n"
                )
            else:
                interpretation += (
                    "• Score faible - TDAH infantile peu probable\n"
                    "• Si symptômes attentionnels actuels, rechercher autres causes "
                    "(anxiété, dépression, troubles du sommeil, etc.)\n"
                )
        
        # Important notes
        interpretation += (
            "\n=== NOTES IMPORTANTES ===\n"
            "• Le WURS-25 est un outil de DÉPISTAGE rétrospectif, pas un outil diagnostique\n"
            "• Les souvenirs d'enfance peuvent être biaisés (minimisation ou exagération)\n"
            "• Un score élevé n'est pas suffisant pour diagnostiquer un TDAH adulte\n"
            "• Le diagnostic de TDAH adulte nécessite:\n"
            "  - Symptômes dans l'enfance (avant 12 ans) documentés par WURS ou autre\n"
            "  - Symptômes actuels à l'âge adulte (ASRS, échelles cliniques)\n"
            "  - Retentissement fonctionnel significatif\n"
            "  - Exclusion d'autres diagnostics\n"
        )
        
        if clinical_significance:
            interpretation += (
                "\n⚠️ CONCLUSION: Les résultats du WURS-25 suggèrent une symptomatologie TDAH "
                "significative dans l'enfance, ce qui remplit le critère rétrospectif pour un "
                "éventuel TDAH adulte. Une évaluation diagnostique complète est fortement recommandée."
            )
        
        return interpretation
    
    def get_schema(self) -> Dict[str, Any]:
        """
        Get complete questionnaire schema in JSON format.
        
        Returns:
            Complete questionnaire schema
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
                        "message": "Les 25 items doivent être renseignés (0..4)."
                    },
                    {
                        "id": "range_0_4",
                        "level": "error",
                        "message": "Chaque item WURS doit être un entier entre 0 et 4."
                    }
                ]
            },
            "scoring": {
                "scales": [
                    {
                        "id": "wurs_total",
                        "label": "WURS-25 – Score total (0–100)",
                        "description": "Somme des 25 items (0–100). Aucun recodage.",
                        "items": [f"q{i}" for i in self.ITEM_IDS],
                        "range": [0, 100]
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

