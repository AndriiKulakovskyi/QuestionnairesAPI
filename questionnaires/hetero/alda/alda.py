"""
ALDA (Alda Scale)

This module implements the ALDA scale, a retrospective assessment tool for evaluating
treatment response in bipolar disorder. It uses a unique scoring formula: Total = A - B,
where A is clinical improvement (0-10) and B is the sum of five confounding factors (0-10).
"""

from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime


class ALDAError(Exception):
    """Custom exception for ALDA scale errors."""
    pass


class ALDA:
    """
    ALDA (Alda Scale)
    
    A retrospective assessment of treatment response in bipolar disorder.
    Consists of two criteria:
    - Criterion A: Clinical improvement (0-10)
    - Criterion B: Five confounding factors that may reduce attribution to treatment (each 0-2)
    
    Total score = A - sum(B1-B5), range: -10 to +10 (or 0-10 if clamped)
    
    Attributes:
        id: Unique identifier for the scale
        name: Full name in French
        abbreviation: Short form (ALDA)
        language: Language code
        version: Version number
        reference_period: Time frame for assessment
        description: Brief description of the scale
    """
    
    # Criterion B item IDs
    B_ITEMS = ["B1", "B2", "B3", "B4", "B5"]
    
    # Response options for B items (0-2)
    B_OPTIONS = [
        {"code": 0, "score": 0},
        {"code": 1, "score": 1},
        {"code": 2, "score": 2}
    ]
    
    # Common threshold for good response
    GOOD_RESPONSE_THRESHOLD = 7
    
    def __init__(self):
        """Initialize the ALDA scale."""
        self.id = "Alda.fr"
        self.name = "Échelle d'Alda – Critères rétrospectifs de réponse au traitement (FR)"
        self.abbreviation = "Alda"
        self.language = "fr-FR"
        self.version = "1.0"
        self.reference_period = "Évaluation rétrospective sous traitement thymorégulateur"
        self.description = (
            "Deux parties : Critère A (0–10) = amélioration clinique ; "
            "Critère B = 5 pénalités (0–2 chacune). Score total = A − (B1..B5)."
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
            "num_items": 6,
            "response_scales": {
                "criterion_A": "0-10 integer scale",
                "criterion_B": "0-2 categorical scale (5 items)"
            },
            "score_range_unclamped": [-10, 10],
            "score_range_clamped": [0, 10],
            "score_type": "subtraction (A - B)",
            "good_response_threshold": self.GOOD_RESPONSE_THRESHOLD
        }
    
    def get_questions(self) -> List[Dict[str, Any]]:
        """
        Get all scale items.
        
        Returns:
            List of question dictionaries
        """
        questions = [
            {
                "id": "A",
                "section_id": "A",
                "text": "Amélioration clinique globale attribuée au traitement au long cours",
                "type": "integer",
                "required": True,
                "constraints": {
                    "value_type": "integer",
                    "min_value": 0,
                    "max_value": 10
                },
                "description": "0 = aucun changement, 10 = réponse complète"
            },
            {
                "id": "B1",
                "section_id": "B",
                "text": "Nombre d'épisodes avant le traitement",
                "type": "single_choice",
                "required": True,
                "options": [
                    {
                        "code": 0,
                        "label": "4 épisodes ou plus",
                        "score": 0
                    },
                    {
                        "code": 1,
                        "label": "2 ou 3 épisodes",
                        "score": 1
                    },
                    {
                        "code": 2,
                        "label": "1 épisode",
                        "score": 2
                    }
                ],
                "constraints": {
                    "value_type": "integer",
                    "allowed_values": [0, 1, 2]
                }
            },
            {
                "id": "B2",
                "section_id": "B",
                "text": "Fréquence des épisodes avant le traitement",
                "type": "single_choice",
                "required": True,
                "options": [
                    {
                        "code": 0,
                        "label": "Moyenne à élevée, incluant les cycles rapides",
                        "score": 0
                    },
                    {
                        "code": 1,
                        "label": "Faible, rémissions spontanées de 3 ans ou plus en moyenne",
                        "score": 1
                    },
                    {
                        "code": 2,
                        "label": "1 seul épisode, risque de récurrence ne peut être établi",
                        "score": 2
                    }
                ],
                "constraints": {
                    "value_type": "integer",
                    "allowed_values": [0, 1, 2]
                }
            },
            {
                "id": "B3",
                "section_id": "B",
                "text": "Durée du traitement",
                "type": "single_choice",
                "required": True,
                "options": [
                    {
                        "code": 0,
                        "label": "2 ans ou plus",
                        "score": 0
                    },
                    {
                        "code": 1,
                        "label": "1-2 ans",
                        "score": 1
                    },
                    {
                        "code": 2,
                        "label": "moins d'un an",
                        "score": 2
                    }
                ],
                "constraints": {
                    "value_type": "integer",
                    "allowed_values": [0, 1, 2]
                }
            },
            {
                "id": "B4",
                "section_id": "B",
                "text": "Compliance durant la/les période(s) de stabilité",
                "type": "single_choice",
                "required": True,
                "options": [
                    {
                        "code": 0,
                        "label": "Excellente, documentée par des taux dans les limites thérapeutiques",
                        "score": 0
                    },
                    {
                        "code": 1,
                        "label": "Bonne, plus de 80% des taux dans les limites thérapeutiques",
                        "score": 1
                    },
                    {
                        "code": 2,
                        "label": "Pauvre, répétitivement hors traitements, moins de 80% des taux dans les limites thérapeutiques",
                        "score": 2
                    }
                ],
                "constraints": {
                    "value_type": "integer",
                    "allowed_values": [0, 1, 2]
                }
            },
            {
                "id": "B5",
                "section_id": "B",
                "text": "Usage de médication additionnelle durant la phase de stabilité",
                "type": "single_choice",
                "required": True,
                "options": [
                    {
                        "code": 0,
                        "label": "Aucun hormis de rares somnifères (1 par semaine ou moins); pas d'autres stabilisateurs pour contrôler les symptômes thymiques",
                        "score": 0
                    },
                    {
                        "code": 1,
                        "label": "Antidépresseurs ou antipsychotiques à faible dose comme une sécurité, ou recours prolongé à des somnifères",
                        "score": 1
                    },
                    {
                        "code": 2,
                        "label": "Usage prolongé ou systématique d'un antidépresseur ou antipsychotique",
                        "score": 2
                    }
                ],
                "constraints": {
                    "value_type": "integer",
                    "allowed_values": [0, 1, 2]
                }
            }
        ]
        return questions
    
    def get_sections(self) -> List[Dict[str, Any]]:
        """
        Get scale sections.
        
        Returns:
            List of section dictionaries
        """
        return [
            {
                "id": "A",
                "label": "Critère A – Amélioration clinique",
                "description": "0 = aucun changement … 10 = réponse complète",
                "question_ids": ["A"]
            },
            {
                "id": "B",
                "label": "Critère B – Relation causalité amélioration/traitement",
                "description": "5 items 0..2",
                "question_ids": self.B_ITEMS
            }
        ]
    
    def validate_answers(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Validate scale responses.
        
        Args:
            answers: Dictionary mapping item IDs to response values
        
        Returns:
            Dictionary containing validation results with 'valid', 'errors', and 'warnings' keys
        
        Raises:
            ALDAError: If validation fails critically
        """
        errors = []
        warnings = []
        
        # Check all items are present
        expected_items = ["A"] + self.B_ITEMS
        missing = [item for item in expected_items if item not in answers]
        
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Validate criterion A
        if "A" in answers:
            value = answers["A"]
            if not isinstance(value, int):
                errors.append(f"A: la valeur doit être un entier (reçu: {type(value).__name__})")
            elif value < 0 or value > 10:
                errors.append(f"A: la valeur doit être entre 0 et 10 (reçu: {value})")
        
        # Validate criterion B items
        for item in self.B_ITEMS:
            if item in answers:
                value = answers[item]
                if not isinstance(value, int):
                    errors.append(f"{item}: la valeur doit être un entier (reçu: {type(value).__name__})")
                elif value not in [0, 1, 2]:
                    errors.append(f"{item}: la valeur doit être 0, 1 ou 2 (reçu: {value})")
        
        # Clinical warnings
        if not errors:
            A_score = answers.get("A", 0)
            B_sum = sum(answers.get(item, 0) for item in self.B_ITEMS)
            
            # Warning if high improvement but many confounders
            if A_score >= 7 and B_sum >= 7:
                warnings.append(
                    "Score A élevé mais facteurs confondants importants (B élevé). "
                    "L'amélioration peut être due à d'autres facteurs que le traitement."
                )
            
            # Warning if low improvement
            if A_score <= 3:
                warnings.append(
                    "Score A faible suggère une réponse insuffisante au traitement. "
                    "Considérer ajustement thérapeutique ou changement de traitement."
                )
            
            # Warning if short treatment duration (B3)
            if answers.get("B3", 0) == 2:
                warnings.append(
                    "Durée de traitement < 1 an. L'évaluation de la réponse peut être prématurée."
                )
            
            # Warning if poor compliance (B4)
            if answers.get("B4", 0) == 2:
                warnings.append(
                    "Compliance faible. La non-réponse peut être liée à une prise inadéquate du traitement."
                )
            
            # Warning if single episode only (B1)
            if answers.get("B1", 0) == 2:
                warnings.append(
                    "Un seul épisode avant traitement. Difficile d'établir le pattern de récurrence."
                )
            
            # Warning if low frequency with spontaneous remissions (B2)
            if answers.get("B2", 0) >= 1:
                warnings.append(
                    "Fréquence faible d'épisodes ou rémissions spontanées possibles. "
                    "Réduit la certitude d'attribution de l'amélioration au traitement."
                )
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def calculate_score(
        self,
        answers: Dict[str, int],
        clamp_min_zero: bool = True
    ) -> Dict[str, Any]:
        """
        Calculate ALDA score.
        
        Args:
            answers: Dictionary mapping item IDs to response values
            clamp_min_zero: If True, clamp total score to minimum 0 (common usage)
        
        Returns:
            Dictionary containing:
                - score_A: Criterion A score (0-10)
                - score_B: Sum of criterion B items (0-10)
                - total_score: A - B (clamped or unclamped)
                - total_score_unclamped: Raw A - B without clamping
                - clamp_applied: Whether clamping was used
                - response_category: Good/Partial/Poor response classification
                - item_scores: Individual item scores
                - interpretation: Clinical interpretation
        
        Raises:
            ALDAError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation["valid"]:
            raise ALDAError(
                f"Validation échouée: {'; '.join(validation['errors'])}"
            )
        
        # Calculate criterion A
        score_A = answers["A"]
        
        # Calculate criterion B (sum of penalties)
        score_B = sum(answers[item] for item in self.B_ITEMS)
        
        # Calculate total score
        total_score_unclamped = score_A - score_B
        total_score = max(0, total_score_unclamped) if clamp_min_zero else total_score_unclamped
        clamp_applied = clamp_min_zero and total_score_unclamped < 0
        
        # Determine response category
        response_category = self._get_response_category(total_score)
        
        # Collect item scores
        item_scores = {
            "A": {
                "score": score_A,
                "description": "Amélioration clinique globale"
            }
        }
        
        for item in self.B_ITEMS:
            item_scores[item] = {
                "score": answers[item],
                "description": self._get_b_item_description(item)
            }
        
        # Generate interpretation
        interpretation = self._generate_interpretation(
            score_A,
            score_B,
            total_score,
            total_score_unclamped,
            response_category,
            answers
        )
        
        return {
            "score_A": score_A,
            "score_B": score_B,
            "total_score": total_score,
            "total_score_unclamped": total_score_unclamped,
            "score_range": [0, 10] if clamp_min_zero else [-10, 10],
            "clamp_applied": clamp_applied,
            "response_category": response_category,
            "good_response_threshold": self.GOOD_RESPONSE_THRESHOLD,
            "item_scores": item_scores,
            "interpretation": interpretation,
            "warnings": validation["warnings"],
            "calculation_date": datetime.utcnow().isoformat() + "Z"
        }
    
    def _get_response_category(self, total_score: int) -> str:
        """
        Classify treatment response based on total score.
        
        Args:
            total_score: Total ALDA score
        
        Returns:
            Response category label
        """
        if total_score >= self.GOOD_RESPONSE_THRESHOLD:
            return "Bonne réponse"
        elif total_score >= 4:
            return "Réponse partielle"
        else:
            return "Réponse insuffisante"
    
    def _get_b_item_description(self, item: str) -> str:
        """Get short description for criterion B item."""
        descriptions = {
            "B1": "Nombre d'épisodes avant traitement",
            "B2": "Fréquence épisodes avant traitement",
            "B3": "Durée du traitement",
            "B4": "Compliance",
            "B5": "Médications additionnelles"
        }
        return descriptions.get(item, "")
    
    def _generate_interpretation(
        self,
        score_A: int,
        score_B: int,
        total_score: int,
        total_score_unclamped: int,
        response_category: str,
        answers: Dict[str, int]
    ) -> str:
        """
        Generate clinical interpretation based on scores.
        
        Args:
            score_A: Criterion A score
            score_B: Criterion B sum
            total_score: Total score (possibly clamped)
            total_score_unclamped: Raw total score
            response_category: Response classification
            answers: Full answer dictionary
        
        Returns:
            Clinical interpretation text in French
        """
        interpretation = "=== ÉCHELLE D'ALDA - ÉVALUATION DE LA RÉPONSE AU TRAITEMENT ===\n\n"
        
        # Score summary
        interpretation += f"Critère A (amélioration clinique): {score_A}/10\n"
        interpretation += f"Critère B (facteurs confondants): {score_B}/10\n"
        interpretation += f"Score total (A - B): {total_score}/10"
        
        if total_score != total_score_unclamped:
            interpretation += f" (brut: {total_score_unclamped}, borné à 0)\n"
        else:
            interpretation += "\n"
        
        interpretation += f"\n**{response_category.upper()}**\n\n"
        
        # Overall interpretation
        interpretation += "=== INTERPRÉTATION GLOBALE ===\n"
        
        if total_score >= 7:
            interpretation += (
                "✅ BONNE RÉPONSE AU TRAITEMENT\n"
                "Le patient présente une amélioration clinique substantielle qui peut être "
                "attribuée avec confiance au traitement thymorégulateur. Les facteurs confondants "
                "sont minimes, renforçant la causalité entre le traitement et l'amélioration.\n\n"
                "Recommandations:\n"
                "• Maintenir le traitement actuel\n"
                "• Surveillance régulière de l'observance\n"
                "• Monitoring des taux thérapeutiques si applicable\n"
                "• Éducation sur l'importance de la continuité du traitement\n"
            )
        elif total_score >= 4:
            interpretation += (
                "⚠️ RÉPONSE PARTIELLE AU TRAITEMENT\n"
                "Le patient présente une amélioration modérée. Plusieurs facteurs confondants "
                "peuvent réduire la certitude de l'attribution au traitement, ou l'amélioration "
                "elle-même est modeste.\n\n"
                "Recommandations:\n"
                "• Évaluer les facteurs confondants (voir détails ci-dessous)\n"
                "• Optimiser la compliance si nécessaire\n"
                "• Considérer ajustement posologique\n"
                "• Évaluer la nécessité de traitements adjuvants\n"
                "• Poursuivre surveillance clinique rapprochée\n"
            )
        else:
            interpretation += (
                "❌ RÉPONSE INSUFFISANTE AU TRAITEMENT\n"
                "Le patient ne présente pas d'amélioration clinique significative attribuable "
                "au traitement actuel, ou les facteurs confondants sont très importants.\n\n"
                "Recommandations:\n"
                "• Réévaluation diagnostique (confirmer trouble bipolaire)\n"
                "• Vérifier l'observance thérapeutique\n"
                "• Vérifier les taux thérapeutiques si applicable\n"
                "• Considérer changement de thymorégulateur\n"
                "• Considérer association de traitements\n"
                "• Évaluer comorbidités (abus de substances, troubles anxieux)\n"
                "• Évaluation psychosociale approfondie\n"
            )
        
        # Criterion A analysis
        interpretation += "\n=== CRITÈRE A: AMÉLIORATION CLINIQUE ===\n"
        interpretation += f"Score: {score_A}/10\n\n"
        
        if score_A >= 8:
            interpretation += (
                "AMÉLIORATION EXCELLENTE\n"
                "Réponse clinique proche de la rémission complète. Le patient a retrouvé "
                "un fonctionnement proche de la normale avec absence ou quasi-absence d'épisodes.\n"
            )
        elif score_A >= 6:
            interpretation += (
                "AMÉLIORATION MARQUÉE\n"
                "Réponse clinique substantielle avec réduction importante de la fréquence "
                "et/ou de la sévérité des épisodes thymiques.\n"
            )
        elif score_A >= 4:
            interpretation += (
                "AMÉLIORATION MODÉRÉE\n"
                "Réponse clinique partielle. Le patient présente une certaine amélioration "
                "mais des symptômes résiduels ou des épisodes atténués persistent.\n"
            )
        else:
            interpretation += (
                "AMÉLIORATION FAIBLE OU ABSENTE\n"
                "Le traitement n'a pas produit d'amélioration clinique significative. "
                "Réévaluation thérapeutique nécessaire.\n"
            )
        
        # Criterion B analysis
        interpretation += "\n=== CRITÈRE B: FACTEURS CONFONDANTS ===\n"
        interpretation += f"Score total: {score_B}/10\n"
        interpretation += "(Plus le score B est élevé, moins la causalité traitement→amélioration est certaine)\n\n"
        
        if score_B <= 2:
            interpretation += (
                "FACTEURS CONFONDANTS MINIMAUX\n"
                "Les conditions d'évaluation sont optimales. L'amélioration observée peut "
                "être attribuée avec grande confiance au traitement.\n"
            )
        elif score_B <= 5:
            interpretation += (
                "FACTEURS CONFONDANTS MODÉRÉS\n"
                "Certains éléments réduisent modérément la certitude de l'attribution. "
                "L'amélioration reste probablement liée au traitement mais avec quelques réserves.\n"
            )
        else:
            interpretation += (
                "FACTEURS CONFONDANTS IMPORTANTS\n"
                "⚠️ Plusieurs éléments réduisent significativement la certitude que l'amélioration "
                "soit due au traitement. D'autres facteurs peuvent expliquer l'évolution clinique.\n"
            )
        
        # Detailed B items analysis
        interpretation += "\nDétail des facteurs confondants:\n"
        
        # B1: Number of episodes before treatment
        b1 = answers.get("B1", 0)
        interpretation += f"\n• B1 - Nombre d'épisodes avant traitement: {b1}/2\n"
        if b1 == 0:
            interpretation += "  4 épisodes ou plus → Historique robuste, récurrence bien établie\n"
        elif b1 == 1:
            interpretation += "  2 ou 3 épisodes → Historique modéré\n"
        else:
            interpretation += "  ⚠️ 1 seul épisode → Difficile d'établir le pattern de récurrence\n"
        
        # B2: Episode frequency before treatment
        b2 = answers.get("B2", 0)
        interpretation += f"\n• B2 - Fréquence des épisodes avant traitement: {b2}/2\n"
        if b2 == 0:
            interpretation += "  Moyenne à élevée (incluant cycles rapides) → Amélioration attribuable au traitement\n"
        elif b2 == 1:
            interpretation += "  ⚠️ Faible avec rémissions spontanées (≥3 ans) → Réduit certitude d'attribution\n"
        else:
            interpretation += "  ⚠️ 1 seul épisode → Risque de récurrence non établi\n"
        
        # B3: Treatment duration
        b3 = answers.get("B3", 0)
        interpretation += f"\n• B3 - Durée du traitement: {b3}/2\n"
        if b3 == 0:
            interpretation += "  2 ans ou plus → Durée optimale pour évaluer la réponse\n"
        elif b3 == 1:
            interpretation += "  1-2 ans → Durée acceptable mais limite\n"
        else:
            interpretation += "  ⚠️ Moins d'un an → Durée insuffisante; évaluation prématurée\n"
        
        # B4: Compliance
        b4 = answers.get("B4", 0)
        interpretation += f"\n• B4 - Compliance: {b4}/2\n"
        if b4 == 0:
            interpretation += "  Excellente, documentée par des taux thérapeutiques → Certitude maximale\n"
        elif b4 == 1:
            interpretation += "  Bonne (>80% des taux dans limites) → Observance acceptable\n"
        else:
            interpretation += "  ⚠️ Pauvre (<80% des taux) → Impossibilité de conclure sur l'efficacité\n"
        
        # B5: Additional medications
        b5 = answers.get("B5", 0)
        interpretation += f"\n• B5 - Médications additionnelles: {b5}/2\n"
        if b5 == 0:
            interpretation += "  Aucun (sauf rares somnifères) → Amélioration attribuable au traitement principal\n"
        elif b5 == 1:
            interpretation += "  Antidépresseurs/antipsychotiques à faible dose → Contribution mixte\n"
        else:
            interpretation += "  ⚠️ Usage prolongé/systématique d'adjuvants → Difficile d'isoler l'effet\n"
        
        # Clinical recommendations based on specific factors
        interpretation += "\n=== RECOMMANDATIONS SPÉCIFIQUES ===\n"
        
        if b4 >= 1:
            interpretation += (
                "• COMPLIANCE: Renforcer l'observance thérapeutique\n"
                "  - Éducation thérapeutique\n"
                "  - Simplification du schéma posologique si possible\n"
                "  - Évaluer les barrières à l'observance (effets secondaires, insight)\n"
            )
        
        if b3 >= 1:
            interpretation += (
                "• DURÉE DE TRAITEMENT: Poursuivre le suivi\n"
                "  - Réévaluation à distance pour confirmer la stabilité\n"
                "  - Documentation longitudinale des épisodes\n"
            )
        
        if b5 >= 1:
            interpretation += (
                "• POLYPHARMACIE: Évaluer la contribution de chaque traitement\n"
                "  - Tenter simplification si possible\n"
                "  - Identifier le(s) traitement(s) essentiel(s)\n"
            )
        
        if b2 >= 1:
            interpretation += (
                "• FRÉQUENCE DES ÉPISODES: Évaluation approfondie\n"
                "  - Documenter les rémissions spontanées antérieures\n"
                "  - Considérer l'histoire naturelle du trouble\n"
                "  - Prolonger la surveillance pour mieux établir le pattern\n"
            )
        
        # Summary and conclusion
        interpretation += "\n=== CONCLUSION ===\n"
        
        if total_score >= 7:
            interpretation += (
                f"Score ALDA de {total_score}/10 indique une BONNE RÉPONSE au traitement "
                "thymorégulateur avec attribution causale fiable. Maintenir le traitement actuel "
                "et assurer un suivi régulier pour prévenir les rechutes.\n"
            )
        elif total_score >= 4:
            interpretation += (
                f"Score ALDA de {total_score}/10 indique une RÉPONSE PARTIELLE. "
                "Optimisation thérapeutique recommandée en tenant compte des facteurs confondants "
                "identifiés. Surveillance clinique rapprochée nécessaire.\n"
            )
        else:
            interpretation += (
                f"Score ALDA de {total_score}/10 indique une RÉPONSE INSUFFISANTE. "
                "Réévaluation complète du plan thérapeutique nécessaire. Considérer changement "
                "de thymorégulateur ou stratégies thérapeutiques alternatives.\n"
            )
        
        interpretation += (
            "\nNote: L'échelle d'Alda est un outil rétrospectif d'évaluation de la réponse. "
            "Elle doit être complétée par une évaluation clinique approfondie et une documentation "
            "longitudinale des épisodes thymiques."
        )
        
        return interpretation
    
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
    
    def get_schema(self) -> Dict[str, Any]:
        """
        Get complete scale schema in JSON format.
        
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
                        "id": "A_range",
                        "level": "error",
                        "message": "A doit être un entier 0–10."
                    },
                    {
                        "id": "B_range",
                        "level": "error",
                        "message": "B1..B5 doivent être 0,1 ou 2."
                    }
                ]
            },
            "scoring": {
                "variables": [
                    {
                        "id": "B_sum",
                        "expression": {
                            "+": [
                                {"var": "B1"},
                                {"var": "B2"},
                                {"var": "B3"},
                                {"var": "B4"},
                                {"var": "B5"}
                            ]
                        }
                    }
                ],
                "scales": [
                    {
                        "id": "alda_A",
                        "label": "Score A",
                        "items": ["A"],
                        "formula": {"var": "A"},
                        "range": [0, 10]
                    },
                    {
                        "id": "alda_B",
                        "label": "Score B (somme)",
                        "items": self.B_ITEMS,
                        "formula": {"var": "B_sum"},
                        "range": [0, 10]
                    },
                    {
                        "id": "alda_total",
                        "label": "Score total (A − B)",
                        "items": ["A"] + self.B_ITEMS,
                        "formula": {"-": [{"var": "A"}, {"var": "B_sum"}]},
                        "range": [-10, 10]
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

