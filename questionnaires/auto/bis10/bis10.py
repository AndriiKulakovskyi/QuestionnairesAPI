"""
BIS-10 (Barratt Impulsiveness Scale)

This module implements the BIS-10, a 34-item self-report questionnaire measuring
impulsivity across three dimensions: Motor, Attentional, and Non-planning (Planning Difficulty).
"""

from typing import Dict, List, Optional, Any
from datetime import datetime


class BIS10Error(Exception):
    """Custom exception for BIS-10 questionnaire errors."""
    pass


class BIS10:
    """
    BIS-10 (Barratt Impulsiveness Scale)
    
    A 34-item self-report questionnaire measuring impulsivity across three dimensions:
    - Motor Impulsivity (11 items)
    - Attentional Impulsivity (8 items)
    - Non-planning/Planning Difficulty (11 items)
    
    Note: Items 19, 26, 27, 29 are excluded from scoring (30 items scored).
    
    Attributes:
        id: Unique identifier for the questionnaire
        name: Full name in French
        abbreviation: Short form (BIS-10)
        language: Language code
        version: Version number
        reference_period: Time frame for responses
        description: Brief description of the questionnaire
    """
    
    # Items excluded from scoring (per original publication)
    EXCLUDED_ITEMS = {19, 26, 27, 29}
    
    # Reverse-scored items (recoding: 5 - value)
    REVERSE_ITEMS = {1, 7, 8, 9, 10, 12, 13, 15, 21, 33, 34}
    
    # Subscale item mappings (1-indexed)
    MOTOR_ITEMS = [2, 3, 4, 16, 17, 20, 22, 23, 24, 28, 34]
    ATTENTIONAL_ITEMS = [5, 6, 9, 11, 21, 25, 30, 32]
    PLANNING_ITEMS = [1, 7, 8, 10, 12, 13, 14, 15, 18, 31, 33]
    
    # Available French item texts (from provided PDF)
    ITEM_TEXTS = {
        1: "Je prépare soigneusement les tâches à accomplir",
        2: "Énoncé 2 (voir formulaire BIS10.pdf)",
        3: "Énoncé 3 (voir formulaire BIS10.pdf)",
        4: "Énoncé 4 (voir formulaire BIS10.pdf)",
        5: "Énoncé 5 (voir formulaire BIS10.pdf)",
        6: "J'ai des idées qui fusent",
        7: "Énoncé 7 (voir formulaire BIS10.pdf)",
        8: "Je suis maître de moi",
        9: "Je me concentre facilement",
        10: "Énoncé 10 (voir formulaire BIS10.pdf)",
        11: "Énoncé 11 (voir formulaire BIS10.pdf)",
        12: "Je réfléchis soigneusement",
        13: "Énoncé 13 (voir formulaire BIS10.pdf)",
        14: "Je dis les choses sans y penser",
        15: "Énoncé 15 (voir formulaire BIS10.pdf)",
        16: "Énoncé 16 (voir formulaire BIS10.pdf)",
        17: "J'agis sur un « coup de tête »",
        18: "Énoncé 18 (voir formulaire BIS10.pdf)",
        19: "Énoncé 19 (voir formulaire BIS10.pdf) [EXCLU du score]",
        20: "J'agis selon l'inspiration du moment",
        21: "Je suis quelqu'un de réfléchi",
        22: "Énoncé 22 (voir formulaire BIS10.pdf)",
        23: "J'achète les choses sur un « coup de tête »",
        24: "Énoncé 24 (voir formulaire BIS10.pdf)",
        25: "Je change de passe-temps",
        26: "Énoncé 26 (voir formulaire BIS10.pdf) [EXCLU du score]",
        27: "Énoncé 27 (voir formulaire BIS10.pdf) [EXCLU du score]",
        28: "Je dépense ou paye à crédit plus que je ne gagne",
        29: "Énoncé 29 (voir formulaire BIS10.pdf) [EXCLU du score]",
        30: "Énoncé 30 (voir formulaire BIS10.pdf)",
        31: "Énoncé 31 (voir formulaire BIS10.pdf)",
        32: "Énoncé 32 (voir formulaire BIS10.pdf)",
        33: "Énoncé 33 (voir formulaire BIS10.pdf)",
        34: "Énoncé 34 (voir formulaire BIS10.pdf)"
    }
    
    # Response options (1-4)
    RESPONSE_OPTIONS = [
        {"code": 1, "label": "Rarement ou jamais", "score": 1},
        {"code": 2, "label": "Occasionnellement", "score": 2},
        {"code": 3, "label": "Souvent", "score": 3},
        {"code": 4, "label": "Toujours ou presque toujours", "score": 4}
    ]
    
    def __init__(self):
        """Initialize the BIS-10 questionnaire."""
        self.id = "BIS-10.fr"
        self.name = "Barratt Impulsiveness Scale – BIS-10 (Version française)"
        self.abbreviation = "BIS-10"
        self.language = "fr-FR"
        self.version = "1.0"
        self.reference_period = "Mode de fonctionnement habituel (hors épisodes thymiques anormalement dépressifs/euphoriques)"
        self.description = (
            "Échelle d'impulsivité en 34 items (Likert 1–4). "
            "La cotation officielle utilise 30 items (exclusion: 19, 26, 27, 29). "
            "Trois sous-scores (Motrice, Attentionnelle, Difficulté de planification) et un total (30–120)."
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
            "num_items": 34,
            "num_scored_items": 30,
            "response_scale": "4-point scale (1=Rarement/jamais to 4=Toujours ou presque toujours)",
            "score_range": [30, 120],
            "score_type": "sum",
            "excluded_items": sorted(list(self.EXCLUDED_ITEMS)),
            "reverse_items": sorted(list(self.REVERSE_ITEMS)),
            "subscales": {
                "motor": {"items": self.MOTOR_ITEMS, "range": [11, 44]},
                "attentional": {"items": self.ATTENTIONAL_ITEMS, "range": [8, 32]},
                "planning": {"items": self.PLANNING_ITEMS, "range": [11, 44]}
            }
        }
    
    def get_questions(self) -> List[Dict[str, Any]]:
        """
        Get all questionnaire items.
        
        Returns:
            List of question dictionaries
        """
        questions = []
        for i in range(1, 35):
            # Determine subscale
            subscale = None
            if i in self.MOTOR_ITEMS:
                subscale = "motor"
            elif i in self.ATTENTIONAL_ITEMS:
                subscale = "attentional"
            elif i in self.PLANNING_ITEMS:
                subscale = "planning"
            
            question = {
                "id": f"q{i}",
                "number": i,
                "section_id": "sec_all",
                "text": f"{i}. {self.ITEM_TEXTS[i]}",
                "type": "single_choice",
                "required": True,
                "options": self.RESPONSE_OPTIONS.copy(),
                "reverse_scored": i in self.REVERSE_ITEMS,
                "excluded_from_total": i in self.EXCLUDED_ITEMS,
                "subscale": subscale
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
                "id": "sec_all",
                "label": "BIS-10 – 34 items (1..4)",
                "description": "Rarement/jamais=1 · Occasionnellement=2 · Souvent=3 · Toujours ou presque toujours=4",
                "question_ids": [f"q{i}" for i in range(1, 35)]
            }
        ]
    
    def validate_answers(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Validate questionnaire responses.
        
        Args:
            answers: Dictionary mapping question IDs to response values (1-4)
        
        Returns:
            Dictionary containing validation results with 'valid', 'errors', and 'warnings' keys
        
        Raises:
            BIS10Error: If validation fails critically
        """
        errors = []
        warnings = []
        
        # Check all 34 items are present
        expected_items = [f"q{i}" for i in range(1, 35)]
        missing = [qid for qid in expected_items if qid not in answers]
        
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Validate each response value
        for qid in expected_items:
            if qid in answers:
                value = answers[qid]
                if not isinstance(value, int):
                    errors.append(f"{qid}: la valeur doit être un entier (reçu: {type(value).__name__})")
                elif value < 1 or value > 4:
                    errors.append(f"{qid}: la valeur doit être entre 1 et 4 (reçu: {value})")
        
        # Check for unusual patterns
        if not errors and len(set(answers.values())) == 1:
            warnings.append(
                "Toutes les réponses sont identiques. Veuillez vérifier que le patient "
                "a bien compris les instructions."
            )
        
        # Check if all scored items are minimum (low impulsivity - possible underreporting)
        if not errors:
            scored_values = [answers.get(f"q{i}", 0) for i in range(1, 35) if i not in self.EXCLUDED_ITEMS]
            if all(v == 1 for v in scored_values):
                warnings.append(
                    "Toutes les réponses des items scorés sont à 1 (Rarement/jamais). "
                    "Cela peut indiquer une sous-évaluation de l'impulsivité."
                )
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def calculate_score(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Calculate BIS-10 scores.
        
        Args:
            answers: Dictionary mapping question IDs (q1-q34) to response values (1-4)
        
        Returns:
            Dictionary containing:
                - subscale_scores: Scores for each subscale
                - total_score: Total sum score (30-120)
                - item_scores: Individual item scores with details
                - interpretation: Clinical interpretation
        
        Raises:
            BIS10Error: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation["valid"]:
            raise BIS10Error(
                f"Validation échouée: {'; '.join(validation['errors'])}"
            )
        
        # Apply reverse coding where needed
        recoded = {}
        for i in range(1, 35):
            qid = f"q{i}"
            value = answers[qid]
            
            if i in self.REVERSE_ITEMS:
                recoded[i] = 5 - value
            else:
                recoded[i] = value
        
        # Calculate subscale scores
        motor_score = sum(recoded[i] for i in self.MOTOR_ITEMS)
        attentional_score = sum(recoded[i] for i in self.ATTENTIONAL_ITEMS)
        planning_score = sum(recoded[i] for i in self.PLANNING_ITEMS)
        
        # Calculate total score (sum of subscales)
        total_score = motor_score + attentional_score + planning_score
        
        # Collect item scores with details
        item_scores = {}
        for i in range(1, 35):
            qid = f"q{i}"
            item_scores[qid] = {
                "raw": answers[qid],
                "scored": recoded[i],
                "reversed": i in self.REVERSE_ITEMS,
                "excluded": i in self.EXCLUDED_ITEMS,
                "subscale": None
            }
            
            if i in self.MOTOR_ITEMS:
                item_scores[qid]["subscale"] = "motor"
            elif i in self.ATTENTIONAL_ITEMS:
                item_scores[qid]["subscale"] = "attentional"
            elif i in self.PLANNING_ITEMS:
                item_scores[qid]["subscale"] = "planning"
        
        # Generate interpretation
        interpretation = self._generate_interpretation(
            total_score,
            motor_score,
            attentional_score,
            planning_score
        )
        
        return {
            "subscale_scores": {
                "motor": motor_score,
                "attentional": attentional_score,
                "planning": planning_score
            },
            "total_score": total_score,
            "score_range": [30, 120],
            "subscale_ranges": {
                "motor": [11, 44],
                "attentional": [8, 32],
                "planning": [11, 44]
            },
            "item_scores": item_scores,
            "interpretation": interpretation,
            "warnings": validation["warnings"],
            "calculation_date": datetime.utcnow().isoformat() + "Z"
        }
    
    def _generate_interpretation(
        self,
        total_score: int,
        motor: int,
        attentional: int,
        planning: int
    ) -> str:
        """
        Generate clinical interpretation based on scores.
        
        Args:
            total_score: Total BIS-10 score (30-120)
            motor: Motor impulsivity subscale (11-44)
            attentional: Attentional impulsivity subscale (8-32)
            planning: Planning difficulty subscale (11-44)
        
        Returns:
            Clinical interpretation text in French
        """
        interpretation = f"Score total BIS-10 de {total_score}/120 indique "
        
        if total_score < 52:
            interpretation += (
                "un niveau d'impulsivité très faible. Le patient rapporte un bon "
                "contrôle impulsif dans son fonctionnement habituel."
            )
        elif total_score < 72:
            interpretation += (
                "un niveau d'impulsivité faible à modéré. Le patient rapporte "
                "un contrôle impulsif globalement satisfaisant."
            )
        elif total_score < 90:
            interpretation += (
                "un niveau d'impulsivité modéré à élevé. Le patient rapporte "
                "des difficultés de contrôle impulsif qui peuvent nécessiter "
                "une attention clinique."
            )
        else:
            interpretation += (
                "un niveau d'impulsivité élevé à très élevé. Le patient rapporte "
                "des difficultés importantes de contrôle impulsif nécessitant "
                "une évaluation et un suivi clinique."
            )
        
        # Add subscale details
        interpretation += "\n\nDétails par dimension:"
        
        interpretation += f"\n• Impulsivité motrice ({motor}/44): "
        if motor >= 35:
            interpretation += "Niveau très élevé - Agit sans réfléchir, impulsivité comportementale marquée."
        elif motor >= 28:
            interpretation += "Niveau élevé - Tendance à agir sur un coup de tête."
        elif motor >= 22:
            interpretation += "Niveau modéré - Quelques actions impulsives occasionnelles."
        else:
            interpretation += "Niveau faible - Bon contrôle moteur, peu d'actions impulsives."
        
        interpretation += f"\n• Impulsivité attentionnelle ({attentional}/32): "
        if attentional >= 26:
            interpretation += "Niveau très élevé - Difficultés majeures de concentration et d'attention."
        elif attentional >= 21:
            interpretation += "Niveau élevé - Distractibilité importante, instabilité cognitive."
        elif attentional >= 16:
            interpretation += "Niveau modéré - Quelques difficultés attentionnelles."
        else:
            interpretation += "Niveau faible - Bonne capacité de concentration."
        
        interpretation += f"\n• Difficulté de planification ({planning}/44): "
        if planning >= 35:
            interpretation += "Niveau très élevé - Difficultés majeures à planifier et anticiper."
        elif planning >= 28:
            interpretation += "Niveau élevé - Manque de prévoyance, vie \"au jour le jour\"."
        elif planning >= 22:
            interpretation += "Niveau modéré - Quelques difficultés organisationnelles."
        else:
            interpretation += "Niveau faible - Bonne capacité de planification."
        
        # Clinical recommendations
        if total_score >= 90:
            interpretation += (
                "\n\n⚠️ RECOMMANDATIONS CLINIQUES:\n"
                "• Évaluation des troubles du contrôle des impulsions\n"
                "• Dépistage TDAH si impulsivité attentionnelle élevée\n"
                "• Recherche de troubles addictifs ou comportements à risque\n"
                "• Évaluation de comorbidités (trouble bipolaire, personnalité borderline)\n"
                "• Thérapie cognitivo-comportementale ciblant l'impulsivité"
            )
        elif total_score >= 72:
            interpretation += (
                "\n\nRecommandations:\n"
                "• Surveillance clinique si retentissement fonctionnel\n"
                "• Psychoéducation sur le contrôle des impulsions\n"
                "• Stratégies de gestion de l'impulsivité"
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
                        "message": "Les 34 items doivent être renseignés (1..4)."
                    },
                    {
                        "id": "range_1_4",
                        "level": "error",
                        "message": "Chaque item doit être un entier 1..4 (1=Rarement/jamais … 4=Toujours ou presque toujours)."
                    }
                ]
            },
            "scoring": {
                "variables": [
                    {
                        "id": f"r{i}",
                        "description": f"Recodage inversé de q{i} (5 - q{i})",
                        "expression": {"-": [5, {"var": f"q{i}"}]}
                    } for i in self.REVERSE_ITEMS
                ],
                "scales": [
                    {
                        "id": "bis10_motrice",
                        "label": "Impulsivité motrice (11–44)",
                        "description": "Somme des items: 2, 3, 4, 16, 17, 20, 22, 23, 24, 28, 34 (avec inversion de 34)",
                        "items": [f"q{i}" for i in self.MOTOR_ITEMS],
                        "range": [11, 44]
                    },
                    {
                        "id": "bis10_attentionnelle",
                        "label": "Impulsivité attentionnelle (8–32)",
                        "description": "Somme des items: 5, 6, 9, 11, 21, 25, 30, 32 (avec inversion de 9 et 21)",
                        "items": [f"q{i}" for i in self.ATTENTIONAL_ITEMS],
                        "range": [8, 32]
                    },
                    {
                        "id": "bis10_planification",
                        "label": "Difficulté de planification (11–44)",
                        "description": "Somme des items: 1, 7, 8, 10, 12, 13, 14, 15, 18, 31, 33 (avec inversion des items inversés)",
                        "items": [f"q{i}" for i in self.PLANNING_ITEMS],
                        "range": [11, 44]
                    },
                    {
                        "id": "bis10_total",
                        "label": "BIS-10 – Score total (30–120)",
                        "description": "Somme des trois sous-scores. Items exclus: 19, 26, 27, 29.",
                        "items": [f"q{i}" for i in range(1, 35) if i not in self.EXCLUDED_ITEMS],
                        "range": [30, 120]
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

