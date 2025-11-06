"""
CGI (Clinical Global Impressions)

This module implements the Clinical Global Impressions scale, a brief and widely used
clinician-rated assessment of symptom severity, treatment response, and therapeutic efficacy.

The CGI consists of three subscales:
- CGI-S: Severity of illness (0-7)
- CGI-I: Global improvement (0-7)
- Therapeutic Index: Ratio of therapeutic effect to side effects (0-16)
"""

from typing import Dict, List, Optional, Any, Literal
from datetime import datetime


class CGIError(Exception):
    """Custom exception for CGI scale errors."""
    pass


class CGI:
    """
    CGI (Clinical Global Impressions)
    
    A clinician-rated assessment tool for evaluating:
    1. Severity of illness (CGI-S)
    2. Global improvement/change (CGI-I)
    3. Therapeutic efficacy vs. side effects (Therapeutic Index)
    
    Notes:
    - CGI-I and Therapeutic Index are NOT assessed at baseline
    - All scales use 0 = "Not assessed" option
    - Therapeutic Index uses a complex formula based on effect × side effects
    
    Attributes:
        id: Unique identifier for the scale
        name: Full name in French
        abbreviation: Short form (CGI)
        language: Language code
        version: Version number
        reference_period: Time frame for assessment
        description: Brief description of the scale
    """
    
    # Item IDs
    ITEM_CGI_S = "cgi01"
    ITEM_CGI_I = "cgi02"
    ITEM_THERAPEUTIC_EFFECT = "cgi03a"
    ITEM_SIDE_EFFECTS = "cgi03b"
    
    # Visit types
    VISIT_BASELINE = "baseline"
    VISIT_FOLLOWUP = "followup"
    
    def __init__(self):
        """Initialize the CGI scale."""
        self.id = "CGI.fr"
        self.name = "Impressions Cliniques Globales (CGI) – Version française"
        self.abbreviation = "CGI"
        self.language = "fr-FR"
        self.version = "1.0"
        self.reference_period = "Évaluation clinique courante (visite index ou suivi)"
        self.description = (
            "Echelle en 3 items : Gravité (CGI-S), Amélioration globale (CGI-I), "
            "Index thérapeutique (effet thérapeutique × effets secondaires)."
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
            "num_items": 4,
            "subscales": ["CGI-S", "CGI-I", "Therapeutic Index"],
            "response_scales": {
                "cgi_s": "0-7 ordinal scale (severity)",
                "cgi_i": "0-7 ordinal scale (improvement)",
                "therapeutic_effect": "0-4 ordinal scale",
                "side_effects": "0-4 ordinal scale"
            },
            "visit_type_dependent": True,
            "baseline_items": ["cgi01"],
            "followup_items": ["cgi01", "cgi02", "cgi03a", "cgi03b"],
            "score_ranges": {
                "cgi_s": [0, 7],
                "cgi_i": [0, 7],
                "therapeutic_index": [0, 16]
            }
        }
    
    def get_questions(self) -> List[Dict[str, Any]]:
        """
        Get all scale items.
        
        Returns:
            List of question dictionaries with visibility rules
        """
        questions = [
            {
                "id": "cgi01",
                "section_id": "sec1",
                "text": "Gravité de la maladie",
                "description": "En fonction de votre expérience clinique totale avec ce type de patient, quel est le niveau de gravité des troubles mentaux actuels du patient",
                "type": "single_choice",
                "required": True,
                "options": [
                    {
                        "code": 0,
                        "label": "Non évalué",
                        "score": 0
                    },
                    {
                        "code": 1,
                        "label": "Normal, pas du tout malade",
                        "score": 1
                    },
                    {
                        "code": 2,
                        "label": "A la limite",
                        "score": 2
                    },
                    {
                        "code": 3,
                        "label": "Légèrement malade",
                        "score": 3
                    },
                    {
                        "code": 4,
                        "label": "Modérément malade",
                        "score": 4
                    },
                    {
                        "code": 5,
                        "label": "Manifestement malade",
                        "score": 5
                    },
                    {
                        "code": 6,
                        "label": "Gravement malade",
                        "score": 6
                    },
                    {
                        "code": 7,
                        "label": "Parmi les patients les plus malades",
                        "score": 7
                    }
                ],
                "constraints": {
                    "value_type": "integer",
                    "allowed_values": [0, 1, 2, 3, 4, 5, 6, 7]
                },
                "visibility": {
                    "rule": "always",
                    "description": "Always visible (baseline and follow-up)"
                }
            },
            {
                "id": "cgi02",
                "section_id": "sec1",
                "text": "Amélioration globale",
                "description": "Évaluer l'amélioration totale qu'elle soit ou non, selon votre opinion, due entièrement au traitement médicamenteux. Comparé à son état au début du traitement, de quelle façon le patient a-t-il changé",
                "type": "single_choice",
                "required": True,
                "options": [
                    {
                        "code": 0,
                        "label": "Non évalué",
                        "score": 0
                    },
                    {
                        "code": 1,
                        "label": "Très fortement amélioré",
                        "score": 1
                    },
                    {
                        "code": 2,
                        "label": "Fortement amélioré",
                        "score": 2
                    },
                    {
                        "code": 3,
                        "label": "Légèrement amélioré",
                        "score": 3
                    },
                    {
                        "code": 4,
                        "label": "Pas de changement",
                        "score": 4
                    },
                    {
                        "code": 5,
                        "label": "Légèrement aggravé",
                        "score": 5
                    },
                    {
                        "code": 6,
                        "label": "Fortement aggravé",
                        "score": 6
                    },
                    {
                        "code": 7,
                        "label": "Très fortement aggravé",
                        "score": 7
                    }
                ],
                "constraints": {
                    "value_type": "integer",
                    "allowed_values": [0, 1, 2, 3, 4, 5, 6, 7]
                },
                "visibility": {
                    "rule": "visit_type != 'baseline'",
                    "description": "Only visible at follow-up visits (not at baseline)"
                }
            },
            {
                "id": "cgi03a",
                "section_id": "sec1",
                "text": "Index thérapeutique – Effet thérapeutique",
                "description": "Évaluer l'efficacité du traitement actuel",
                "type": "single_choice",
                "required": True,
                "options": [
                    {
                        "code": 0,
                        "label": "Non évalué",
                        "score": 0
                    },
                    {
                        "code": 1,
                        "label": "Important",
                        "score": 1
                    },
                    {
                        "code": 2,
                        "label": "Modéré",
                        "score": 2
                    },
                    {
                        "code": 3,
                        "label": "Minime",
                        "score": 3
                    },
                    {
                        "code": 4,
                        "label": "Nul ou aggravation",
                        "score": 4
                    }
                ],
                "constraints": {
                    "value_type": "integer",
                    "allowed_values": [0, 1, 2, 3, 4]
                },
                "visibility": {
                    "rule": "visit_type != 'baseline'",
                    "description": "Only visible at follow-up visits (not at baseline)"
                }
            },
            {
                "id": "cgi03b",
                "section_id": "sec1",
                "text": "Index thérapeutique – Effets secondaires",
                "description": "Évaluer l'impact des effets secondaires du traitement",
                "type": "single_choice",
                "required": True,
                "options": [
                    {
                        "code": 0,
                        "label": "Non évalué",
                        "score": 0
                    },
                    {
                        "code": 1,
                        "label": "Aucun",
                        "score": 1
                    },
                    {
                        "code": 2,
                        "label": "N'interfèrent pas significativement avec le fonctionnement du patient",
                        "score": 2
                    },
                    {
                        "code": 3,
                        "label": "Interfèrent significativement avec le fonctionnement du patient",
                        "score": 3
                    },
                    {
                        "code": 4,
                        "label": "Dépassent l'effet thérapeutique",
                        "score": 4
                    }
                ],
                "constraints": {
                    "value_type": "integer",
                    "allowed_values": [0, 1, 2, 3, 4]
                },
                "visibility": {
                    "rule": "visit_type != 'baseline'",
                    "description": "Only visible at follow-up visits (not at baseline)"
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
                "id": "sec1",
                "label": "CGI – Items",
                "description": "Saisir les 3 items (items 2 et 3 non évalués à l'inclusion)",
                "question_ids": ["cgi01", "cgi02", "cgi03a", "cgi03b"]
            }
        ]
    
    def validate_answers(
        self,
        answers: Dict[str, int],
        visit_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Validate scale responses.
        
        Args:
            answers: Dictionary mapping item IDs to response values
            visit_type: Type of visit ("baseline" or "followup"), affects which items are required
        
        Returns:
            Dictionary containing validation results with 'valid', 'errors', and 'warnings' keys
        
        Raises:
            CGIError: If validation fails critically
        """
        errors = []
        warnings = []
        
        # Determine required items based on visit type
        if visit_type == self.VISIT_BASELINE:
            required_items = [self.ITEM_CGI_S]
            optional_items = [self.ITEM_CGI_I, self.ITEM_THERAPEUTIC_EFFECT, self.ITEM_SIDE_EFFECTS]
        else:
            # Follow-up or unspecified
            required_items = [
                self.ITEM_CGI_S,
                self.ITEM_CGI_I,
                self.ITEM_THERAPEUTIC_EFFECT,
                self.ITEM_SIDE_EFFECTS
            ]
            optional_items = []
        
        # Check required items are present
        missing = [item for item in required_items if item not in answers]
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Validate CGI-S (cgi01)
        if self.ITEM_CGI_S in answers:
            value = answers[self.ITEM_CGI_S]
            if not isinstance(value, int):
                errors.append(f"cgi01: la valeur doit être un entier (reçu: {type(value).__name__})")
            elif value not in range(0, 8):
                errors.append(f"cgi01: la valeur doit être entre 0 et 7 (reçu: {value})")
            elif value == 0 and visit_type != self.VISIT_BASELINE:
                warnings.append(
                    "CGI-S (cgi01) marqué comme 'Non évalué'. "
                    "La gravité devrait généralement être évaluée à chaque visite."
                )
        
        # Validate CGI-I (cgi02)
        if self.ITEM_CGI_I in answers:
            value = answers[self.ITEM_CGI_I]
            if not isinstance(value, int):
                errors.append(f"cgi02: la valeur doit être un entier (reçu: {type(value).__name__})")
            elif value not in range(0, 8):
                errors.append(f"cgi02: la valeur doit être entre 0 et 7 (reçu: {value})")
            elif visit_type == self.VISIT_BASELINE and value != 0:
                errors.append(
                    "CGI-I (cgi02) ne doit pas être évalué à la visite initiale. "
                    "Utiliser 0 = 'Non évalué'."
                )
        
        # Validate therapeutic effect (cgi03a)
        if self.ITEM_THERAPEUTIC_EFFECT in answers:
            value = answers[self.ITEM_THERAPEUTIC_EFFECT]
            if not isinstance(value, int):
                errors.append(f"cgi03a: la valeur doit être un entier (reçu: {type(value).__name__})")
            elif value not in range(0, 5):
                errors.append(f"cgi03a: la valeur doit être entre 0 et 4 (reçu: {value})")
            elif visit_type == self.VISIT_BASELINE and value != 0:
                errors.append(
                    "L'effet thérapeutique (cgi03a) ne doit pas être évalué à la visite initiale. "
                    "Utiliser 0 = 'Non évalué'."
                )
        
        # Validate side effects (cgi03b)
        if self.ITEM_SIDE_EFFECTS in answers:
            value = answers[self.ITEM_SIDE_EFFECTS]
            if not isinstance(value, int):
                errors.append(f"cgi03b: la valeur doit être un entier (reçu: {type(value).__name__})")
            elif value not in range(0, 5):
                errors.append(f"cgi03b: la valeur doit être entre 0 et 4 (reçu: {value})")
            elif visit_type == self.VISIT_BASELINE and value != 0:
                errors.append(
                    "Les effets secondaires (cgi03b) ne doivent pas être évalués à la visite initiale. "
                    "Utiliser 0 = 'Non évalué'."
                )
        
        # Clinical warnings for follow-up visits
        if not errors and visit_type != self.VISIT_BASELINE:
            cgi_s = answers.get(self.ITEM_CGI_S, 0)
            cgi_i = answers.get(self.ITEM_CGI_I, 0)
            effect = answers.get(self.ITEM_THERAPEUTIC_EFFECT, 0)
            side_effects = answers.get(self.ITEM_SIDE_EFFECTS, 0)
            
            # Severity warnings
            if cgi_s >= 6:
                warnings.append(
                    "Gravité élevée (CGI-S ≥ 6). Patient gravement malade. "
                    "Considérer intensification du traitement ou hospitalisation."
                )
            
            # Improvement warnings
            if cgi_i >= 5:
                warnings.append(
                    "Aggravation clinique (CGI-I ≥ 5). "
                    "Réévaluation urgente du plan thérapeutique nécessaire."
                )
            elif cgi_i == 4 and cgi_s >= 4:
                warnings.append(
                    "Pas de changement (CGI-I = 4) avec sévérité modérée à élevée. "
                    "Considérer ajustement thérapeutique."
                )
            
            # Therapeutic effect warnings
            if effect >= 3:
                warnings.append(
                    "Effet thérapeutique minime ou nul (cgi03a ≥ 3). "
                    "Réévaluer l'adéquation du traitement actuel."
                )
            
            # Side effects warnings
            if side_effects >= 3:
                warnings.append(
                    "Effets secondaires significatifs (cgi03b ≥ 3). "
                    "Les effets indésirables interfèrent avec le fonctionnement. "
                    "Considérer ajustement posologique ou changement de traitement."
                )
            
            # Therapeutic index warnings
            if effect != 0 and side_effects == 4:
                warnings.append(
                    "⚠️ ALERTE: Effets secondaires dépassent l'effet thérapeutique. "
                    "Changement de traitement fortement recommandé."
                )
            
            # Discrepancy warnings
            if cgi_i <= 2 and cgi_s >= 5:
                warnings.append(
                    "Incohérence: Amélioration forte (CGI-I) mais gravité toujours élevée (CGI-S). "
                    "Vérifier l'évaluation."
                )
            elif cgi_i >= 5 and cgi_s <= 2:
                warnings.append(
                    "Incohérence: Aggravation (CGI-I) mais gravité faible (CGI-S). "
                    "Vérifier l'évaluation."
                )
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def calculate_therapeutic_index(self, effect: int, side_effects: int) -> int:
        """
        Calculate the therapeutic index based on the CGI formula.
        
        Formula:
        - If effect = 0 (not assessed): return 0
        - If effect = 1 (major): return side_effects
        - If effect = 2 (moderate): return side_effects + 4
        - If effect = 3 (minimal): return side_effects + 8
        - If effect = 4 (none/worse): return side_effects + 12
        
        Args:
            effect: Therapeutic effect score (0-4)
            side_effects: Side effects score (0-4)
        
        Returns:
            Therapeutic index (0-16)
        """
        if effect == 0:
            return 0
        elif effect == 1:
            return side_effects
        elif effect == 2:
            return side_effects + 4
        elif effect == 3:
            return side_effects + 8
        else:  # effect == 4
            return side_effects + 12
    
    def calculate_score(
        self,
        answers: Dict[str, int],
        visit_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Calculate CGI scores.
        
        Args:
            answers: Dictionary mapping item IDs to response values
            visit_type: Type of visit ("baseline" or "followup")
        
        Returns:
            Dictionary containing:
                - cgi_s: CGI-S severity score (0-7)
                - cgi_i: CGI-I improvement score (0-7, or None if not assessed)
                - therapeutic_effect: Therapeutic effect score (0-4, or None if not assessed)
                - side_effects: Side effects score (0-4, or None if not assessed)
                - therapeutic_index: Calculated therapeutic index (0-16, or None)
                - visit_type: Visit type used for calculation
                - interpretation: Clinical interpretation
        
        Raises:
            CGIError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers, visit_type)
        if not validation["valid"]:
            raise CGIError(
                f"Validation échouée: {'; '.join(validation['errors'])}"
            )
        
        # Extract scores
        cgi_s = answers.get(self.ITEM_CGI_S, 0)
        cgi_i = answers.get(self.ITEM_CGI_I, 0) if visit_type != self.VISIT_BASELINE else None
        effect = answers.get(self.ITEM_THERAPEUTIC_EFFECT, 0) if visit_type != self.VISIT_BASELINE else None
        side_effects = answers.get(self.ITEM_SIDE_EFFECTS, 0) if visit_type != self.VISIT_BASELINE else None
        
        # Calculate therapeutic index
        therapeutic_index = None
        if effect is not None and side_effects is not None and effect != 0:
            therapeutic_index = self.calculate_therapeutic_index(effect, side_effects)
        
        # Generate interpretation
        interpretation = self._generate_interpretation(
            cgi_s, cgi_i, effect, side_effects, therapeutic_index, visit_type
        )
        
        return {
            "cgi_s": cgi_s,
            "cgi_i": cgi_i,
            "therapeutic_effect": effect,
            "side_effects": side_effects,
            "therapeutic_index": therapeutic_index,
            "visit_type": visit_type or "unspecified",
            "interpretation": interpretation,
            "warnings": validation["warnings"],
            "calculation_date": datetime.utcnow().isoformat() + "Z"
        }
    
    def _get_severity_label(self, score: int) -> str:
        """Get severity category label."""
        labels = {
            0: "Non évalué",
            1: "Normal, pas malade",
            2: "À la limite",
            3: "Légèrement malade",
            4: "Modérément malade",
            5: "Manifestement malade",
            6: "Gravement malade",
            7: "Extrêmement malade"
        }
        return labels.get(score, "Invalide")
    
    def _get_improvement_label(self, score: int) -> str:
        """Get improvement category label."""
        labels = {
            0: "Non évalué",
            1: "Très fortement amélioré",
            2: "Fortement amélioré",
            3: "Légèrement amélioré",
            4: "Pas de changement",
            5: "Légèrement aggravé",
            6: "Fortement aggravé",
            7: "Très fortement aggravé"
        }
        return labels.get(score, "Invalide")
    
    def _get_therapeutic_effect_label(self, score: int) -> str:
        """Get therapeutic effect label."""
        labels = {
            0: "Non évalué",
            1: "Important",
            2: "Modéré",
            3: "Minime",
            4: "Nul ou aggravation"
        }
        return labels.get(score, "Invalide")
    
    def _get_side_effects_label(self, score: int) -> str:
        """Get side effects label."""
        labels = {
            0: "Non évalué",
            1: "Aucun",
            2: "Effets mineurs",
            3: "Effets significatifs",
            4: "Effets dépassant le bénéfice"
        }
        return labels.get(score, "Invalide")
    
    def _generate_interpretation(
        self,
        cgi_s: int,
        cgi_i: Optional[int],
        effect: Optional[int],
        side_effects: Optional[int],
        therapeutic_index: Optional[int],
        visit_type: Optional[str]
    ) -> str:
        """Generate clinical interpretation."""
        interpretation = "=== IMPRESSIONS CLINIQUES GLOBALES (CGI) ===\n\n"
        
        # Visit type
        if visit_type == self.VISIT_BASELINE:
            interpretation += "Type de visite: VISITE INITIALE (baseline)\n\n"
        elif visit_type == self.VISIT_FOLLOWUP:
            interpretation += "Type de visite: VISITE DE SUIVI (follow-up)\n\n"
        else:
            interpretation += "Type de visite: Non spécifié\n\n"
        
        # CGI-S (Severity)
        interpretation += "=== CGI-S: GRAVITÉ DE LA MALADIE ===\n"
        interpretation += f"Score: {cgi_s}/7 – {self._get_severity_label(cgi_s)}\n\n"
        
        if cgi_s == 0:
            interpretation += "La gravité n'a pas été évaluée.\n"
        elif cgi_s == 1:
            interpretation += (
                "Normal – PAS MALADE\n"
                "Le patient ne présente pas de symptômes de la maladie. "
                "Fonctionnement normal dans tous les domaines.\n"
            )
        elif cgi_s == 2:
            interpretation += (
                "À LA LIMITE\n"
                "Le patient présente des symptômes minimes qui peuvent être à la limite "
                "de la normalité ou du trouble psychiatrique. Surveillance recommandée.\n"
            )
        elif cgi_s == 3:
            interpretation += (
                "LÉGÈREMENT MALADE\n"
                "Le patient présente des symptômes légers mais définitivement présents. "
                "Impact fonctionnel minimal. Traitement ambulatoire approprié.\n"
            )
        elif cgi_s == 4:
            interpretation += (
                "MODÉRÉMENT MALADE\n"
                "Le patient présente des symptômes d'intensité modérée avec impact "
                "fonctionnel notable. Traitement actif recommandé.\n"
            )
        elif cgi_s == 5:
            interpretation += (
                "MANIFESTEMENT MALADE\n"
                "Le patient présente des symptômes importants avec altération significative "
                "du fonctionnement. Traitement intensif nécessaire.\n"
            )
        elif cgi_s == 6:
            interpretation += (
                "GRAVEMENT MALADE\n"
                "Le patient présente des symptômes sévères avec altération majeure du "
                "fonctionnement. Considérer intensification du traitement ou hospitalisation.\n"
            )
        elif cgi_s == 7:
            interpretation += (
                "EXTRÊMEMENT MALADE\n"
                "Le patient fait partie des plus gravement atteints. Symptômes extrêmes "
                "avec dysfonctionnement majeur. Hospitalisation et traitement intensif "
                "généralement nécessaires.\n"
            )
        
        # CGI-I (Improvement) - only at follow-up
        if cgi_i is not None:
            interpretation += "\n=== CGI-I: AMÉLIORATION GLOBALE ===\n"
            interpretation += f"Score: {cgi_i}/7 – {self._get_improvement_label(cgi_i)}\n\n"
            
            if cgi_i == 0:
                interpretation += "L'amélioration n'a pas été évaluée.\n"
            elif cgi_i <= 2:
                interpretation += (
                    "AMÉLIORATION SIGNIFICATIVE\n"
                    "Le patient présente une amélioration cliniquement significative par "
                    "rapport à la visite initiale. Le traitement actuel est efficace.\n\n"
                    "Recommandations:\n"
                    "• Maintenir le traitement actuel\n"
                    "• Renforcer l'observance\n"
                    "• Poursuivre le suivi régulier\n"
                )
            elif cgi_i == 3:
                interpretation += (
                    "AMÉLIORATION LÉGÈRE\n"
                    "Le patient présente une certaine amélioration mais celle-ci reste "
                    "légère. Le traitement a un effet partiel.\n\n"
                    "Recommandations:\n"
                    "• Évaluer si l'amélioration est suffisante\n"
                    "• Considérer optimisation posologique\n"
                    "• Envisager traitements adjuvants si nécessaire\n"
                )
            elif cgi_i == 4:
                interpretation += (
                    "PAS DE CHANGEMENT\n"
                    "Le patient ne présente pas d'amélioration ni d'aggravation par "
                    "rapport à la visite initiale. Le traitement actuel est inefficace.\n\n"
                    "Recommandations:\n"
                    "• Réévaluer le diagnostic\n"
                    "• Vérifier l'observance thérapeutique\n"
                    "• Considérer changement de traitement\n"
                    "• Envisager augmentation posologique\n"
                )
            else:  # cgi_i >= 5
                interpretation += (
                    "AGGRAVATION CLINIQUE\n"
                    "Le patient présente une aggravation par rapport à la visite initiale. "
                    "Le traitement actuel est inefficace ou délétère.\n\n"
                    "Recommandations URGENTES:\n"
                    "• Arrêt ou modification immédiate du traitement\n"
                    "• Réévaluation diagnostique complète\n"
                    "• Évaluation des risques (suicide, agressivité)\n"
                    "• Considérer hospitalisation si aggravation sévère\n"
                )
        else:
            interpretation += "\n=== CGI-I: AMÉLIORATION GLOBALE ===\n"
            interpretation += "Non applicable (visite initiale)\n"
        
        # Therapeutic Index
        if effect is not None and side_effects is not None:
            interpretation += "\n=== INDEX THÉRAPEUTIQUE ===\n"
            interpretation += f"Effet thérapeutique: {effect}/4 – {self._get_therapeutic_effect_label(effect)}\n"
            interpretation += f"Effets secondaires: {side_effects}/4 – {self._get_side_effects_label(side_effects)}\n"
            
            if therapeutic_index is not None:
                interpretation += f"Index thérapeutique: {therapeutic_index}/16\n\n"
                
                # Interpret therapeutic index
                if effect == 0 or side_effects == 0:
                    interpretation += "Index non évalué (effet ou effets secondaires non renseignés).\n"
                elif therapeutic_index <= 3:
                    # Effect = 1 (major), side effects 1-3
                    interpretation += (
                        "EXCELLENT RAPPORT BÉNÉFICE/RISQUE\n"
                        "Effet thérapeutique important avec effets secondaires minimes à modérés. "
                        "Le traitement est optimal.\n"
                    )
                elif therapeutic_index == 4:
                    # Effect = 1, side effects = 4 OR effect = 2, side effects = 0
                    if effect == 1:
                        interpretation += (
                            "ATTENTION: Effet important mais effets secondaires majeurs\n"
                            "Les effets secondaires dépassent le bénéfice. Ajustement nécessaire.\n"
                        )
                    else:
                        interpretation += (
                            "BON RAPPORT BÉNÉFICE/RISQUE\n"
                            "Effet modéré sans effets secondaires.\n"
                        )
                elif therapeutic_index <= 7:
                    # Effect = 2, side effects 1-3
                    interpretation += (
                        "RAPPORT BÉNÉFICE/RISQUE ACCEPTABLE\n"
                        "Effet thérapeutique modéré avec effets secondaires variables. "
                        "Optimisation possible.\n"
                    )
                elif therapeutic_index == 8:
                    # Effect = 2, side effects = 4 OR effect = 3, side effects = 0
                    if effect == 2:
                        interpretation += (
                            "EFFETS SECONDAIRES PROBLÉMATIQUES\n"
                            "Effet modéré mais effets secondaires dépassant le bénéfice. "
                            "Changement de traitement recommandé.\n"
                        )
                    else:
                        interpretation += (
                            "EFFET THÉRAPEUTIQUE LIMITÉ\n"
                            "Effet minimal sans effets secondaires. Efficacité insuffisante.\n"
                        )
                elif therapeutic_index <= 11:
                    # Effect = 3, side effects 1-3
                    interpretation += (
                        "RAPPORT BÉNÉFICE/RISQUE DÉFAVORABLE\n"
                        "Effet thérapeutique minime avec effets secondaires. "
                        "Changement de traitement fortement recommandé.\n"
                    )
                elif therapeutic_index == 12:
                    # Effect = 3, side effects = 4 OR effect = 4, side effects = 0
                    if effect == 3:
                        interpretation += (
                            "TRAITEMENT INADAPTÉ\n"
                            "Effet minimal et effets secondaires dépassant le bénéfice. "
                            "Arrêt ou changement immédiat nécessaire.\n"
                        )
                    else:
                        interpretation += (
                            "ABSENCE D'EFFET THÉRAPEUTIQUE\n"
                            "Aucun effet thérapeutique ou aggravation sans effets secondaires. "
                            "Changement de traitement nécessaire.\n"
                        )
                else:  # therapeutic_index >= 13
                    # Effect = 4, side effects 1-4
                    interpretation += (
                        "TRAITEMENT DÉLÉTÈRE\n"
                        "Absence d'effet thérapeutique (ou aggravation) avec effets secondaires. "
                        "ARRÊT IMMÉDIAT du traitement recommandé.\n"
                    )
                
                # Detailed recommendations based on therapeutic index
                interpretation += "\n"
                if therapeutic_index <= 4 and effect >= 2:
                    interpretation += (
                        "Recommandations:\n"
                        "• Maintenir le traitement si bien toléré\n"
                        "• Surveillance régulière des effets secondaires\n"
                    )
                elif therapeutic_index >= 8 or effect >= 3:
                    interpretation += (
                        "Recommandations:\n"
                        "• Réévaluer l'indication du traitement\n"
                        "• Considérer changement de molécule\n"
                        "• Ajustement posologique si effets secondaires importants\n"
                        "• Discussion bénéfice/risque avec le patient\n"
                    )
            else:
                interpretation += "\nIndex thérapeutique: Non calculé (effet non évalué)\n"
        else:
            interpretation += "\n=== INDEX THÉRAPEUTIQUE ===\n"
            interpretation += "Non applicable (visite initiale)\n"
        
        # Summary
        interpretation += "\n=== SYNTHÈSE CLINIQUE ===\n"
        
        if visit_type == self.VISIT_BASELINE:
            if cgi_s <= 2:
                interpretation += "Patient en bon état clinique à l'inclusion. Surveillance recommandée.\n"
            elif cgi_s <= 4:
                interpretation += "Patient avec symptomatologie légère à modérée. Traitement ambulatoire approprié.\n"
            else:
                interpretation += "Patient avec symptomatologie importante. Traitement actif nécessaire.\n"
        else:
            # Follow-up summary
            if cgi_i is not None and cgi_i <= 2 and cgi_s <= 3:
                interpretation += (
                    "ÉVOLUTION FAVORABLE\n"
                    "Amélioration significative avec gravité faible. Poursuivre le traitement actuel.\n"
                )
            elif cgi_i is not None and cgi_i >= 5:
                interpretation += (
                    "ÉVOLUTION DÉFAVORABLE\n"
                    "Aggravation clinique nécessitant modification thérapeutique urgente.\n"
                )
            elif cgi_s >= 5:
                interpretation += (
                    "GRAVITÉ PERSISTANTE\n"
                    "Patient toujours gravement atteint. Intensification du traitement à considérer.\n"
                )
            elif therapeutic_index is not None and therapeutic_index >= 8:
                interpretation += (
                    "RAPPORT BÉNÉFICE/RISQUE DÉFAVORABLE\n"
                    "Effet thérapeutique insuffisant et/ou effets secondaires importants. "
                    "Modification thérapeutique recommandée.\n"
                )
            else:
                interpretation += (
                    "État clinique stable ou en amélioration modérée. "
                    "Poursuite du suivi et optimisation si nécessaire.\n"
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
                        "id": "range_cgi01",
                        "level": "error",
                        "message": "CGI01 doit être un entier 0–7."
                    },
                    {
                        "id": "range_cgi02",
                        "level": "error",
                        "message": "CGI02 doit être un entier 0–7 (ou 0 si non évalué)."
                    },
                    {
                        "id": "range_cgi03",
                        "level": "error",
                        "message": "CGI03A et CGI03B doivent être des entiers 0–4 (ou 0 si non évalué)."
                    },
                    {
                        "id": "baseline_rule",
                        "level": "warning",
                        "message": (
                            "En visite initiale, poser uniquement l'item 1 "
                            "(mettre 0=Non évalué pour items 2 et 3)."
                        )
                    }
                ]
            },
            "scoring": {
                "variables": [
                    {
                        "id": "cgi03_index_therapeutique",
                        "description": (
                            "Calcul de l'index thérapeutique à partir de CGI03A (effet) "
                            "et CGI03B (effets secondaires)."
                        ),
                        "expression": {
                            "if": [
                                {"==": [{"var": "cgi03a"}, 0]}, 0,
                                {"if": [
                                    {"==": [{"var": "cgi03a"}, 1]}, {"var": "cgi03b"},
                                    {"if": [
                                        {"==": [{"var": "cgi03a"}, 2]}, {"+": [{"var": "cgi03b"}, 4]},
                                        {"if": [
                                            {"==": [{"var": "cgi03a"}, 3]}, {"+": [{"var": "cgi03b"}, 8]},
                                            {"+": [{"var": "cgi03b"}, 12]}
                                        ]}
                                    ]}
                                ]}
                            ]
                        }
                    }
                ],
                "scales": [
                    {
                        "id": "cgi_s",
                        "label": "CGI – Gravité (CGI-S)",
                        "description": "0=Non évalué ; 1=Normal … 7=Parmi les patients les plus malades.",
                        "items": ["cgi01"],
                        "formula": {"var": "cgi01"},
                        "range": [0, 7]
                    },
                    {
                        "id": "cgi_i",
                        "label": "CGI – Amélioration (CGI-I)",
                        "description": "0=Non évalué ; 1=Très fortement amélioré … 7=Très fortement aggravé.",
                        "items": ["cgi02"],
                        "formula": {"var": "cgi02"},
                        "range": [0, 7]
                    },
                    {
                        "id": "cgi_ti",
                        "label": "CGI – Index thérapeutique",
                        "description": (
                            "Algorithme: si Effet=0 → 0; Effet=1 → B; Effet=2 → B+4; "
                            "Effet=3 → B+8; Effet=4 → B+12 (B = CGI03B)."
                        ),
                        "items": ["cgi03a", "cgi03b"],
                        "formula": {"var": "cgi03_index_therapeutique"},
                        "range": [0, 16]
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

