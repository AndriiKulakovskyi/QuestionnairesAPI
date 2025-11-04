"""
CTQ (Childhood Trauma Questionnaire)

This module implements the CTQ, a 28-item retrospective self-report questionnaire
measuring childhood maltreatment across five dimensions: Emotional Abuse, Physical Abuse,
Sexual Abuse, Emotional Neglect, and Physical Neglect.
"""

from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime


class CTQError(Exception):
    """Custom exception for CTQ questionnaire errors."""
    pass


class CTQ:
    """
    CTQ (Childhood Trauma Questionnaire)
    
    A 28-item retrospective self-report questionnaire assessing childhood
    maltreatment across five dimensions plus a denial/minimization scale.
    
    Dimensions:
    - Emotional Abuse (5 items)
    - Physical Abuse (5 items)  
    - Sexual Abuse (5 items)
    - Emotional Neglect (5 items)
    - Physical Neglect (5 items)
    - Denial/Minimization (3 items)
    
    Attributes:
        id: Unique identifier for the questionnaire
        name: Full name in French
        abbreviation: Short form (CTQ)
        language: Language code
        version: Version number
        reference_period: Time frame for responses (retrospective childhood)
        description: Brief description of the questionnaire
    """
    
    # Reverse-scored items (recoding: 6 - value)
    REVERSE_ITEMS = {2, 5, 7, 13, 19, 26, 28}
    
    # Subscale item mappings (1-indexed)
    EMOTIONAL_ABUSE_ITEMS = [3, 8, 14, 18, 25]
    PHYSICAL_ABUSE_ITEMS = [9, 11, 12, 15, 17]
    SEXUAL_ABUSE_ITEMS = [20, 21, 23, 24, 27]
    EMOTIONAL_NEGLECT_ITEMS = [5, 7, 13, 19, 28]  # All reversed
    PHYSICAL_NEGLECT_ITEMS = [1, 2, 4, 6, 26]     # 2 and 26 reversed
    
    # Denial/minimization items
    DENIAL_ITEMS = [10, 16, 22]
    
    # Cut-offs for severity levels by subscale
    CUTOFFS = {
        "emotional_abuse": [
            (5, 8, "Aucun/minime"),
            (9, 12, "Faible/modéré"),
            (13, 15, "Moyen/sévère"),
            (16, 25, "Sévère/extrême")
        ],
        "physical_abuse": [
            (5, 7, "Aucun/minime"),
            (8, 9, "Faible/modéré"),
            (10, 12, "Moyen/sévère"),
            (13, 25, "Sévère/extrême")
        ],
        "sexual_abuse": [
            (5, 5, "Aucun/minime"),
            (6, 7, "Faible/modéré"),
            (8, 12, "Moyen/sévère"),
            (13, 25, "Sévère/extrême")
        ],
        "emotional_neglect": [
            (5, 9, "Aucun/minime"),
            (10, 14, "Faible/modéré"),
            (15, 17, "Moyen/sévère"),
            (18, 25, "Sévère/extrême")
        ],
        "physical_neglect": [
            (5, 7, "Aucun/minime"),
            (8, 9, "Faible/modéré"),
            (10, 12, "Moyen/sévère"),
            (13, 25, "Sévère/extrême")
        ]
    }
    
    # Item texts in French
    ITEM_TEXTS = {
        1: "Il m'est arrivé de ne pas avoir assez à manger.",
        2: "Je savais qu'il y avait quelqu'un pour prendre soin de moi et me protéger.",
        3: "Des membres de ma famille me disaient que j'étais « stupide » ou « paresseux » ou « laid ».",
        4: "Mes parents étaient trop saouls ou « pétés » pour s'occuper de la famille.",
        5: "Il y avait quelqu'un dans ma famille qui m'aidait à sentir que j'étais important ou particulier.",
        6: "Je devais porter des vêtements sales.",
        7: "Je me sentais aimé(e).",
        8: "Je pensais que mes parents n'avaient pas souhaité ma naissance.",
        9: "J'ai été frappé(e) si fort par un membre de ma famille que j'ai dû consulter un docteur ou aller à l'hôpital.",
        10: "Je n'aurais rien voulu changer à ma famille.",
        11: "Un membre de ma famille m'a frappé(e) si fort que j'ai eu des bleus ou des marques.",
        12: "J'étais puni(e) au moyen d'une ceinture, d'un bâton, d'une corde ou de quelque autre objet dur.",
        13: "Les membres de ma famille étaient attentifs les uns aux autres.",
        14: "Les membres de ma famille me disaient des choses blessantes ou insultantes.",
        15: "Je pense que j'ai été physiquement maltraité(e).",
        16: "J'ai eu une enfance parfaite.",
        17: "J'ai été frappé(e) ou battu(e) si fort que quelqu'un l'a remarqué (par ex. un professeur, un voisin ou un docteur).",
        18: "J'avais le sentiment que quelqu'un dans ma famille me détestait.",
        19: "Les membres de ma famille se sentaient proches les uns des autres.",
        20: "Quelqu'un a essayé de me faire des attouchements sexuels ou de m'en faire faire.",
        21: "Quelqu'un a menacé de me blesser ou de raconter des mensonges à mon sujet si je ne faisais pas quelque chose de nature sexuelle avec lui.",
        22: "J'avais la meilleure famille du monde.",
        23: "Quelqu'un a essayé de me faire faire des actes sexuels ou de me faire regarder de tels actes.",
        24: "J'ai été victime d'abus sexuels.",
        25: "Je pense que j'ai été maltraité affectivement.",
        26: "Il y avait quelqu'un pour m'emmener chez le docteur si j'en avais besoin.",
        27: "Je pense qu'on a abusé de moi sexuellement.",
        28: "Ma famille était une source de force et de soutien."
    }
    
    # Response options (1-5)
    RESPONSE_OPTIONS = [
        {"code": 1, "label": "Jamais", "score": 1},
        {"code": 2, "label": "Rarement", "score": 2},
        {"code": 3, "label": "Quelquefois", "score": 3},
        {"code": 4, "label": "Souvent", "score": 4},
        {"code": 5, "label": "Très souvent", "score": 5}
    ]
    
    def __init__(self):
        """Initialize the CTQ questionnaire."""
        self.id = "CTQ.fr"
        self.name = "Childhood Trauma Questionnaire (CTQ) – Version française"
        self.abbreviation = "CTQ"
        self.language = "fr-FR"
        self.version = "1.0"
        self.reference_period = "Enfance et/ou adolescence (rétrospectif)"
        self.description = (
            "Questionnaire auto-rapporté en 28 items (Likert 1–5 : 1=Jamais, 5=Très souvent). "
            "5 sous-dimensions (abus émotionnel/physique/sexuel, négligence émotionnelle/physique) "
            "+ échelle de déni/minimisation (3 items). Certains items sont inversés."
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
            "num_items": 28,
            "response_scale": "5-point scale (1=Jamais to 5=Très souvent)",
            "score_range": [25, 125],
            "score_type": "sum",
            "reverse_items": sorted(list(self.REVERSE_ITEMS)),
            "subscales": {
                "emotional_abuse": {"items": self.EMOTIONAL_ABUSE_ITEMS, "range": [5, 25]},
                "physical_abuse": {"items": self.PHYSICAL_ABUSE_ITEMS, "range": [5, 25]},
                "sexual_abuse": {"items": self.SEXUAL_ABUSE_ITEMS, "range": [5, 25]},
                "emotional_neglect": {"items": self.EMOTIONAL_NEGLECT_ITEMS, "range": [5, 25]},
                "physical_neglect": {"items": self.PHYSICAL_NEGLECT_ITEMS, "range": [5, 25]}
            },
            "denial_scale": {"items": self.DENIAL_ITEMS, "range": [0, 3]}
        }
    
    def get_questions(self) -> List[Dict[str, Any]]:
        """
        Get all questionnaire items.
        
        Returns:
            List of question dictionaries
        """
        questions = []
        for i in range(1, 29):
            # Determine subscale
            subscale = None
            if i in self.EMOTIONAL_ABUSE_ITEMS:
                subscale = "emotional_abuse"
            elif i in self.PHYSICAL_ABUSE_ITEMS:
                subscale = "physical_abuse"
            elif i in self.SEXUAL_ABUSE_ITEMS:
                subscale = "sexual_abuse"
            elif i in self.EMOTIONAL_NEGLECT_ITEMS:
                subscale = "emotional_neglect"
            elif i in self.PHYSICAL_NEGLECT_ITEMS:
                subscale = "physical_neglect"
            elif i in self.DENIAL_ITEMS:
                subscale = "denial"
            
            question = {
                "id": f"q{i}",
                "number": i,
                "section_id": "sec_all",
                "text": f"{i}. {self.ITEM_TEXTS[i]}",
                "type": "single_choice",
                "required": True,
                "options": self.RESPONSE_OPTIONS.copy(),
                "reverse_scored": i in self.REVERSE_ITEMS,
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
                "label": "CTQ – 28 items (1..5)",
                "description": "Au cours de mon enfance et/ou de mon adolescence…",
                "question_ids": [f"q{i}" for i in range(1, 29)]
            }
        ]
    
    def validate_answers(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Validate questionnaire responses.
        
        Args:
            answers: Dictionary mapping question IDs to response values (1-5)
        
        Returns:
            Dictionary containing validation results with 'valid', 'errors', and 'warnings' keys
        
        Raises:
            CTQError: If validation fails critically
        """
        errors = []
        warnings = []
        
        # Check all 28 items are present
        expected_items = [f"q{i}" for i in range(1, 29)]
        missing = [qid for qid in expected_items if qid not in answers]
        
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Validate each response value
        for qid in expected_items:
            if qid in answers:
                value = answers[qid]
                if not isinstance(value, int):
                    errors.append(f"{qid}: la valeur doit être un entier (reçu: {type(value).__name__})")
                elif value < 1 or value > 5:
                    errors.append(f"{qid}: la valeur doit être entre 1 et 5 (reçu: {value})")
        
        # Check for high denial/minimization
        if not errors:
            denial_count = sum(1 for i in self.DENIAL_ITEMS if answers.get(f"q{i}", 0) == 5)
            if denial_count >= 2:
                warnings.append(
                    f"Score de déni/minimisation élevé ({denial_count}/3). "
                    "Les réponses peuvent sous-estimer les traumatismes réellement vécus."
                )
        
        # Check for all minimum responses (possible denial)
        if not errors:
            non_denial_items = [i for i in range(1, 29) if i not in self.DENIAL_ITEMS]
            if all(answers.get(f"q{i}", 0) == 1 for i in non_denial_items):
                warnings.append(
                    "Toutes les réponses (hors déni) sont à 1 (Jamais). "
                    "Vérifier la possibilité de minimisation ou déni."
                )
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def calculate_score(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Calculate CTQ scores.
        
        Args:
            answers: Dictionary mapping question IDs (q1-q28) to response values (1-5)
        
        Returns:
            Dictionary containing:
                - subscale_scores: Scores for each of 5 subscales with severity levels
                - total_score: Total sum score (25-125)
                - denial_score: Denial/minimization score (0-3)
                - item_scores: Individual item scores with details
                - interpretation: Clinical interpretation
        
        Raises:
            CTQError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation["valid"]:
            raise CTQError(
                f"Validation échouée: {'; '.join(validation['errors'])}"
            )
        
        # Apply reverse coding where needed
        recoded = {}
        for i in range(1, 29):
            qid = f"q{i}"
            value = answers[qid]
            
            if i in self.REVERSE_ITEMS:
                recoded[i] = 6 - value
            else:
                recoded[i] = value
        
        # Calculate subscale scores
        emotional_abuse = sum(recoded[i] for i in self.EMOTIONAL_ABUSE_ITEMS)
        physical_abuse = sum(recoded[i] for i in self.PHYSICAL_ABUSE_ITEMS)
        sexual_abuse = sum(recoded[i] for i in self.SEXUAL_ABUSE_ITEMS)
        emotional_neglect = sum(recoded[i] for i in self.EMOTIONAL_NEGLECT_ITEMS)
        physical_neglect = sum(recoded[i] for i in self.PHYSICAL_NEGLECT_ITEMS)
        
        # Calculate total score (sum of 5 subscales)
        total_score = (emotional_abuse + physical_abuse + sexual_abuse +
                      emotional_neglect + physical_neglect)
        
        # Calculate denial/minimization score
        denial_score = sum(1 for i in self.DENIAL_ITEMS if answers[f"q{i}"] == 5)
        
        # Get severity levels
        subscale_scores = {
            "emotional_abuse": {
                "score": emotional_abuse,
                "severity": self._get_severity("emotional_abuse", emotional_abuse)
            },
            "physical_abuse": {
                "score": physical_abuse,
                "severity": self._get_severity("physical_abuse", physical_abuse)
            },
            "sexual_abuse": {
                "score": sexual_abuse,
                "severity": self._get_severity("sexual_abuse", sexual_abuse)
            },
            "emotional_neglect": {
                "score": emotional_neglect,
                "severity": self._get_severity("emotional_neglect", emotional_neglect)
            },
            "physical_neglect": {
                "score": physical_neglect,
                "severity": self._get_severity("physical_neglect", physical_neglect)
            }
        }
        
        # Collect item scores
        item_scores = {}
        for i in range(1, 29):
            qid = f"q{i}"
            item_scores[qid] = {
                "raw": answers[qid],
                "scored": recoded[i],
                "reversed": i in self.REVERSE_ITEMS,
                "subscale": None
            }
            
            if i in self.EMOTIONAL_ABUSE_ITEMS:
                item_scores[qid]["subscale"] = "emotional_abuse"
            elif i in self.PHYSICAL_ABUSE_ITEMS:
                item_scores[qid]["subscale"] = "physical_abuse"
            elif i in self.SEXUAL_ABUSE_ITEMS:
                item_scores[qid]["subscale"] = "sexual_abuse"
            elif i in self.EMOTIONAL_NEGLECT_ITEMS:
                item_scores[qid]["subscale"] = "emotional_neglect"
            elif i in self.PHYSICAL_NEGLECT_ITEMS:
                item_scores[qid]["subscale"] = "physical_neglect"
            elif i in self.DENIAL_ITEMS:
                item_scores[qid]["subscale"] = "denial"
        
        # Generate interpretation
        interpretation = self._generate_interpretation(
            subscale_scores,
            total_score,
            denial_score
        )
        
        return {
            "subscale_scores": subscale_scores,
            "total_score": total_score,
            "score_range": [25, 125],
            "denial_score": denial_score,
            "item_scores": item_scores,
            "interpretation": interpretation,
            "warnings": validation["warnings"],
            "calculation_date": datetime.utcnow().isoformat() + "Z"
        }
    
    def _get_severity(self, subscale: str, score: int) -> str:
        """
        Get severity level for a subscale score.
        
        Args:
            subscale: Subscale name
            score: Subscale score (5-25)
        
        Returns:
            Severity level label
        """
        for min_val, max_val, label in self.CUTOFFS[subscale]:
            if min_val <= score <= max_val:
                return label
        return "Hors bornes"
    
    def _generate_interpretation(
        self,
        subscale_scores: Dict[str, Dict[str, Any]],
        total_score: int,
        denial_score: int
    ) -> str:
        """
        Generate clinical interpretation based on scores.
        
        Args:
            subscale_scores: Scores for all subscales with severity
            total_score: Total CTQ score
            denial_score: Denial/minimization score
        
        Returns:
            Clinical interpretation text in French
        """
        interpretation = f"Score total CTQ de {total_score}/125\n\n"
        
        # Overall assessment
        severe_count = sum(1 for s in subscale_scores.values() 
                          if "Sévère" in s["severity"])
        moderate_count = sum(1 for s in subscale_scores.values() 
                            if "Moyen" in s["severity"] or "Faible" in s["severity"])
        
        if severe_count >= 3:
            interpretation += (
                "⚠️ TRAUMATISME COMPLEXE SÉVÈRE - Le patient rapporte des maltraitances "
                "multiples et sévères durant l'enfance/adolescence.\n\n"
            )
        elif severe_count >= 1:
            interpretation += (
                "⚠️ TRAUMATISME SIGNIFICATIF - Le patient rapporte au moins un type de "
                "maltraitance sévère durant l'enfance/adolescence.\n\n"
            )
        elif moderate_count >= 3:
            interpretation += (
                "Traumatisme modéré - Le patient rapporte plusieurs types de maltraitances "
                "d'intensité faible à modérée.\n\n"
            )
        else:
            interpretation += (
                "Pas de traumatisme significatif rapporté ou traumatisme minimal.\n\n"
            )
        
        # Detailed subscale analysis
        interpretation += "=== ANALYSE PAR DIMENSION ===\n\n"
        
        for subscale_key, subscale_data in subscale_scores.items():
            score = subscale_data["score"]
            severity = subscale_data["severity"]
            
            if subscale_key == "emotional_abuse":
                interpretation += f"• Abus émotionnel ({score}/25): {severity}\n"
                if "Sévère" in severity:
                    interpretation += "  Humiliations, insultes, critiques répétées et destructrices.\n"
            elif subscale_key == "physical_abuse":
                interpretation += f"• Abus physique ({score}/25): {severity}\n"
                if "Sévère" in severity:
                    interpretation += "  Violence physique avec blessures, coups répétés.\n"
            elif subscale_key == "sexual_abuse":
                interpretation += f"• Abus sexuel ({score}/25): {severity}\n"
                if "Sévère" in severity:
                    interpretation += "  ⚠️ Abus sexuel significatif nécessitant attention spécialisée.\n"
            elif subscale_key == "emotional_neglect":
                interpretation += f"• Négligence émotionnelle ({score}/25): {severity}\n"
                if "Sévère" in severity:
                    interpretation += "  Absence de soutien, d'amour, d'attention émotionnelle.\n"
            elif subscale_key == "physical_neglect":
                interpretation += f"• Négligence physique ({score}/25): {severity}\n"
                if "Sévère" in severity:
                    interpretation += "  Besoins de base non satisfaits (nourriture, vêtements, soins).\n"
        
        # Denial/minimization
        interpretation += f"\n• Déni/minimisation: {denial_score}/3"
        if denial_score >= 2:
            interpretation += (
                " (ÉLEVÉ)\n  ⚠️ Score de déni élevé suggère possible minimisation des traumatismes. "
                "Les scores peuvent sous-estimer la maltraitance réelle.\n"
            )
        elif denial_score == 1:
            interpretation += " (MODÉRÉ)\n  Légère tendance à minimiser ou idéaliser l'enfance.\n"
        else:
            interpretation += " (FAIBLE)\n  Pas de déni apparent.\n"
        
        # Clinical recommendations
        if severe_count >= 1 or total_score >= 60:
            interpretation += (
                "\n=== RECOMMANDATIONS CLINIQUES ===\n"
                "• Évaluation psychiatrique approfondie\n"
                "• Dépistage SSPT (syndrome de stress post-traumatique)\n"
                "• Évaluation des troubles dissociatifs\n"
                "• Thérapie trauma-focalisée (EMDR, thérapie cognitive du trauma)\n"
                "• Évaluation des comorbidités (dépression, anxiété, addictions)\n"
                "• Soutien psychologique spécialisé en trauma complexe\n"
            )
            
            if subscale_scores["sexual_abuse"]["score"] >= 8:
                interpretation += "• ⚠️ Prise en charge spécialisée pour trauma sexuel\n"
            
            if denial_score >= 2:
                interpretation += (
                    "• ⚠️ Aborder avec précaution le déni/minimisation en thérapie\n"
                    "• Travailler progressivement sur la reconnaissance du trauma\n"
                )
        elif moderate_count >= 2:
            interpretation += (
                "\n=== RECOMMANDATIONS ===\n"
                "• Psychothérapie de soutien\n"
                "• Évaluation de l'impact actuel sur le fonctionnement\n"
                "• Surveillance des symptômes anxio-dépressifs\n"
            )
        
        # Impact statement
        if severe_count >= 1:
            interpretation += (
                "\n=== IMPACT POTENTIEL ===\n"
                "Les traumatismes infantiles sévères sont associés à:\n"
                "• Risque accru de troubles psychiatriques (dépression, anxiété, SSPT)\n"
                "• Difficultés relationnelles et d'attachement\n"
                "• Risque de revictimisation\n"
                "• Troubles de la régulation émotionnelle\n"
                "• Risque accru de troubles somatiques\n"
                "• Impact sur l'estime de soi et l'identité\n"
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
                        "message": "Les 28 items doivent être renseignés (1=Jamais … 5=Très souvent)."
                    },
                    {
                        "id": "range_1_5",
                        "level": "error",
                        "message": "Chaque item doit être un entier entre 1 et 5."
                    }
                ]
            },
            "scoring": {
                "variables": [
                    {
                        "id": f"r{i}",
                        "description": f"Recodage inversé de q{i} (6 - q{i})",
                        "expression": {"-": [6, {"var": f"q{i}"}]}
                    } for i in self.REVERSE_ITEMS
                ],
                "scales": [
                    {
                        "id": "ctq_abus_emotionnel",
                        "label": "Abus émotionnel (5–25)",
                        "description": "Somme des items 3, 8, 14, 18, 25.",
                        "items": [f"q{i}" for i in self.EMOTIONAL_ABUSE_ITEMS],
                        "range": [5, 25]
                    },
                    {
                        "id": "ctq_abus_physique",
                        "label": "Abus physique (5–25)",
                        "description": "Somme des items 9, 11, 12, 15, 17.",
                        "items": [f"q{i}" for i in self.PHYSICAL_ABUSE_ITEMS],
                        "range": [5, 25]
                    },
                    {
                        "id": "ctq_abus_sexuel",
                        "label": "Abus sexuel (5–25)",
                        "description": "Somme des items 20, 21, 23, 24, 27.",
                        "items": [f"q{i}" for i in self.SEXUAL_ABUSE_ITEMS],
                        "range": [5, 25]
                    },
                    {
                        "id": "ctq_negligence_emotionnelle",
                        "label": "Négligence émotionnelle (5–25)",
                        "description": "Somme des items inversés 5, 7, 13, 19, 28.",
                        "items": [f"q{i}" for i in self.EMOTIONAL_NEGLECT_ITEMS],
                        "range": [5, 25]
                    },
                    {
                        "id": "ctq_negligence_physique",
                        "label": "Négligence physique (5–25)",
                        "description": "Somme des items 1, 2(inv), 4, 6, 26(inv).",
                        "items": [f"q{i}" for i in self.PHYSICAL_NEGLECT_ITEMS],
                        "range": [5, 25]
                    },
                    {
                        "id": "ctq_total",
                        "label": "CTQ – Score total (25–125)",
                        "description": "Somme des 5 sous-scores (les items de déni/minimisation n'entrent pas dans le total).",
                        "range": [25, 125]
                    },
                    {
                        "id": "ctq_deni_minimisation",
                        "label": "Déni / minimisation (0–3)",
                        "description": "Items 10, 16, 22 – 1 point pour chaque item coté 5 (Très souvent), sinon 0.",
                        "items": [f"q{i}" for i in self.DENIAL_ITEMS],
                        "range": [0, 3]
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

