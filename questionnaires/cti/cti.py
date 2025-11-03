"""
CTI (Circadian Type Inventory)

This module implements the CTI, an 11-item self-report questionnaire measuring
circadian flexibility/rigidity and languid/vigorous tendencies.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime


class CTIError(Exception):
    """Custom exception for CTI questionnaire errors."""
    pass


class CTI:
    """
    CTI (Circadian Type Inventory)
    
    An 11-item self-report questionnaire assessing circadian preferences
    and adaptability across two dimensions:
    - Flexibility/Rigidity (5 items)
    - Languid/Vigorous (6 items)
    
    Attributes:
        id: Unique identifier for the questionnaire
        name: Full name in French
        abbreviation: Short form (CTI)
        language: Language code
        version: Version number
        reference_period: Time frame for responses
        description: Brief description of the questionnaire
    """
    
    # Subscale item mappings (1-indexed)
    FLEXIBILITY_ITEMS = [2, 4, 6, 8, 10]
    LANGUID_ITEMS = [1, 3, 5, 7, 9, 11]
    
    # Item texts in French
    ITEM_TEXTS = [
        "Avez-vous tendance à avoir besoin de plus de sommeil que les autres personnes ?",
        "Si vous aviez à faire un certain travail au milieu de la nuit, pensez‑vous que vous pourriez le faire presque aussi facilement qu'à une heure plus normale de la journée ?",
        "Est-ce que vous trouvez qu'il est difficile de vous réveiller correctement si vous êtes réveillé à une heure inhabituelle ?",
        "Aimez-vous travailler à des heures inhabituelles du jour ou de la nuit ?",
        "Si vous allez au lit très tard, avez-vous besoin de dormir plus tard le lendemain matin ?",
        "Si vous avez beaucoup à faire, pouvez-vous travailler tard le soir pour terminer sans être trop fatigué ?",
        "Vous sentez-vous endormi pendant un certain temps après le réveil le matin ?",
        "Trouvez‑vous aussi facile de travailler tard la nuit que tôt le matin ?",
        "Si vous devez vous lever très tôt un matin, avez-vous tendance à vous sentir fatigué toute la journée ?",
        "Seriez-vous aussi content de faire quelque chose au milieu de la nuit que pendant la journée ?",
        "Devez-vous compter sur un réveil, ou sur quelqu'un d'autre, pour vous réveiller le matin ?"
    ]
    
    # Response options (1-5)
    RESPONSE_OPTIONS = [
        {"code": 1, "label": "1 – Presque jamais", "score": 1},
        {"code": 2, "label": "2 – Rarement", "score": 2},
        {"code": 3, "label": "3 – Parfois", "score": 3},
        {"code": 4, "label": "4 – En général", "score": 4},
        {"code": 5, "label": "5 – Presque toujours", "score": 5}
    ]
    
    def __init__(self):
        """Initialize the CTI questionnaire."""
        self.id = "CTI.fr"
        self.name = "Inventaire du Type Circadien (CTI) – Version française"
        self.abbreviation = "CTI"
        self.language = "fr-FR"
        self.version = "1.0"
        self.reference_period = "Habitudes/préférences habituelles (hors contraintes professionnelles)"
        self.description = (
            "Inventaire en 11 items (Likert 1–5 : 1=Presque jamais … 5=Presque toujours). "
            "Deux sous-scores : Flexibilité/Rigidité (5–25) et Languide/Vigoureux (6–30)."
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
            "num_items": 11,
            "response_scale": "5-point scale (1=Presque jamais to 5=Presque toujours)",
            "score_type": "sum",
            "subscales": {
                "flexibility": {"items": self.FLEXIBILITY_ITEMS, "range": [5, 25]},
                "languid": {"items": self.LANGUID_ITEMS, "range": [6, 30]}
            },
            "interpretation": "Higher flexibility = more flexible; Higher languid = more languid (less vigorous)"
        }
    
    def get_questions(self) -> List[Dict[str, Any]]:
        """
        Get all questionnaire items.
        
        Returns:
            List of question dictionaries
        """
        questions = []
        for i, text in enumerate(self.ITEM_TEXTS, start=1):
            # Determine subscale
            if i in self.FLEXIBILITY_ITEMS:
                subscale = "flexibility"
            elif i in self.LANGUID_ITEMS:
                subscale = "languid"
            else:
                subscale = None
            
            question = {
                "id": f"q{i}",
                "number": i,
                "section_id": "sec_all",
                "text": f"{i}. {text}",
                "type": "single_choice",
                "required": True,
                "options": self.RESPONSE_OPTIONS.copy(),
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
                "label": "CTI – 11 items (1..5)",
                "description": "Entourez une seule réponse par question (1=Presque jamais … 5=Presque toujours)",
                "question_ids": [f"q{i}" for i in range(1, 12)]
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
            CTIError: If validation fails critically
        """
        errors = []
        warnings = []
        
        # Check all 11 items are present
        expected_items = [f"q{i}" for i in range(1, 12)]
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
        
        # Check for unusual patterns
        if not errors and len(set(answers.values())) == 1:
            warnings.append(
                "Toutes les réponses sont identiques. Veuillez vérifier que le patient "
                "a bien compris les instructions."
            )
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def calculate_score(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Calculate CTI scores.
        
        Args:
            answers: Dictionary mapping question IDs (q1-q11) to response values (1-5)
        
        Returns:
            Dictionary containing:
                - subscale_scores: Scores for flexibility and languid subscales
                - circadian_profile: Profile classification
                - item_scores: Individual item scores
                - interpretation: Clinical interpretation
        
        Raises:
            CTIError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation["valid"]:
            raise CTIError(
                f"Validation échouée: {'; '.join(validation['errors'])}"
            )
        
        # Calculate subscale scores (simple sums, no reverse coding)
        flexibility_score = sum(answers[f"q{i}"] for i in self.FLEXIBILITY_ITEMS)
        languid_score = sum(answers[f"q{i}"] for i in self.LANGUID_ITEMS)
        
        # Determine circadian profile
        circadian_profile = self._get_profile(flexibility_score, languid_score)
        
        # Collect item scores
        item_scores = {}
        for i in range(1, 12):
            qid = f"q{i}"
            item_scores[qid] = {
                "score": answers[qid],
                "subscale": "flexibility" if i in self.FLEXIBILITY_ITEMS else "languid"
            }
        
        # Generate interpretation
        interpretation = self._generate_interpretation(
            flexibility_score,
            languid_score,
            circadian_profile
        )
        
        return {
            "subscale_scores": {
                "flexibility": flexibility_score,
                "languid": languid_score
            },
            "subscale_ranges": {
                "flexibility": [5, 25],
                "languid": [6, 30]
            },
            "circadian_profile": circadian_profile,
            "item_scores": item_scores,
            "interpretation": interpretation,
            "warnings": validation["warnings"],
            "calculation_date": datetime.utcnow().isoformat() + "Z"
        }
    
    def _get_profile(self, flexibility: int, languid: int) -> str:
        """
        Determine circadian profile based on subscale scores.
        
        Args:
            flexibility: Flexibility score (5-25)
            languid: Languid score (6-30)
        
        Returns:
            Profile classification
        """
        # Determine flexibility level (higher = more flexible)
        if flexibility >= 20:
            flex_level = "Très flexible"
        elif flexibility >= 15:
            flex_level = "Flexible"
        elif flexibility >= 10:
            flex_level = "Modérément rigide"
        else:
            flex_level = "Rigide"
        
        # Determine vigor level (higher languid score = less vigorous)
        if languid >= 24:
            vigor_level = "Très languide"
        elif languid >= 18:
            vigor_level = "Languide"
        elif languid >= 12:
            vigor_level = "Modérément vigoureux"
        else:
            vigor_level = "Très vigoureux"
        
        return f"{flex_level}, {vigor_level}"
    
    def _generate_interpretation(
        self,
        flexibility: int,
        languid: int,
        profile: str
    ) -> str:
        """
        Generate clinical interpretation based on scores.
        
        Args:
            flexibility: Flexibility score
            languid: Languid score
            profile: Profile classification
        
        Returns:
            Clinical interpretation text in French
        """
        interpretation = f"Profil circadien: {profile}\n\n"
        
        # Flexibility dimension
        interpretation += f"=== FLEXIBILITÉ / RIGIDITÉ ({flexibility}/25) ===\n"
        if flexibility >= 20:
            interpretation += (
                "Score TRÈS ÉLEVÉ de flexibilité circadienne.\n"
                "Le patient peut facilement s'adapter à des horaires inhabituels, "
                "travailler à des heures atypiques, et maintenir son efficacité "
                "indépendamment du moment de la journée.\n\n"
                "Caractéristiques:\n"
                "• Grande adaptabilité horaire\n"
                "• Peut travailler efficacement de nuit\n"
                "• S'ajuste facilement aux changements d'horaires\n"
                "• Bon profil pour le travail posté\n"
            )
        elif flexibility >= 15:
            interpretation += (
                "Score ÉLEVÉ de flexibilité circadienne.\n"
                "Le patient présente une bonne capacité d'adaptation aux horaires variables "
                "et peut fonctionner à des heures inhabituelles avec une certaine efficacité.\n\n"
                "Caractéristiques:\n"
                "• Bonne adaptabilité horaire\n"
                "• Tolérance aux horaires atypiques\n"
                "• Ajustement relativement facile\n"
            )
        elif flexibility >= 10:
            interpretation += (
                "Score MODÉRÉ - Tendance à la rigidité circadienne.\n"
                "Le patient a des difficultés à s'adapter aux horaires inhabituels "
                "et fonctionne mieux avec des horaires réguliers.\n\n"
                "Caractéristiques:\n"
                "• Préférence pour horaires réguliers\n"
                "• Difficulté avec horaires atypiques\n"
                "• Besoin de routines stables\n"
            )
        else:
            interpretation += (
                "Score FAIBLE - Forte rigidité circadienne.\n"
                "Le patient présente une rigidité importante de son rythme circadien "
                "avec des difficultés majeures d'adaptation aux horaires variables.\n\n"
                "Caractéristiques:\n"
                "• Rigidité horaire marquée\n"
                "• Très mauvaise tolérance aux horaires atypiques\n"
                "• Nécessité absolue d'horaires réguliers\n"
                "• ⚠️ Contre-indication au travail posté\n"
            )
        
        # Languid dimension
        interpretation += f"\n=== LANGUIDE / VIGOUREUX ({languid}/30) ===\n"
        vigor_score = 30 - languid  # Inverse for vigor interpretation
        
        if languid >= 24:
            interpretation += (
                "Score TRÈS ÉLEVÉ de langueur (très faible vigueur).\n"
                "Le patient rapporte une léthargie importante, un besoin de sommeil élevé, "
                "et des difficultés à lutter contre la somnolence.\n\n"
                "Caractéristiques:\n"
                "• Besoin de sommeil important\n"
                "• Difficulté à se réveiller\n"
                "• Léthargie prolongée après réveil\n"
                "• Dépendance aux aides au réveil\n"
                "• ⚠️ Évaluer troubles du sommeil (PSQI, apnée du sommeil)\n"
                "• ⚠️ Évaluer somnolence diurne (Epworth)\n"
            )
        elif languid >= 18:
            interpretation += (
                "Score ÉLEVÉ de langueur (faible vigueur).\n"
                "Le patient rapporte une certaine léthargie et un besoin de sommeil "
                "supérieur à la moyenne.\n\n"
                "Caractéristiques:\n"
                "• Besoin de sommeil augmenté\n"
                "• Réveil difficile\n"
                "• Fatigue après privation de sommeil\n"
                "• Recommandation: évaluation de la qualité du sommeil\n"
            )
        elif languid >= 12:
            interpretation += (
                "Score MODÉRÉ - Vigueur modérée.\n"
                "Le patient présente un niveau de vigueur dans la moyenne, "
                "avec une capacité raisonnable à gérer les variations de sommeil.\n\n"
                "Caractéristiques:\n"
                "• Besoin de sommeil normal\n"
                "• Réveil relativement facile\n"
                "• Tolérance moyenne à la privation de sommeil\n"
            )
        else:
            interpretation += (
                "Score FAIBLE de langueur (très haute vigueur).\n"
                "Le patient présente une grande vigueur circadienne avec un faible "
                "besoin de sommeil et une grande résistance à la somnolence.\n\n"
                "Caractéristiques:\n"
                "• Besoin de sommeil réduit\n"
                "• Réveil facile et rapide\n"
                "• Bonne résistance à la privation de sommeil\n"
                "• Éveil prolongé sans fatigue excessive\n"
                "• Profil optimal pour performances soutenues\n"
            )
        
        # Overall profile interpretation
        interpretation += "\n=== PROFIL CIRCADIEN GLOBAL ===\n"
        
        if flexibility >= 15 and languid <= 15:
            interpretation += (
                "✅ PROFIL OPTIMAL: Flexible ET Vigoureux\n"
                "Le patient présente le profil le plus adaptatif avec une excellente "
                "flexibilité circadienne et une bonne vigueur. Ce profil est associé à:\n"
                "• Meilleur ajustement aux contraintes horaires\n"
                "• Tolérance au travail posté\n"
                "• Récupération rapide du jetlag\n"
                "• Performance maintenue en horaires variables\n"
            )
        elif flexibility >= 15 and languid > 18:
            interpretation += (
                "Profil FLEXIBLE mais LANGUIDE\n"
                "Bonne adaptabilité horaire mais avec léthargie et besoin de sommeil élevé.\n"
                "• Peut travailler à des heures atypiques mais avec fatigue\n"
                "• Recommandation: optimiser la qualité du sommeil\n"
                "• Évaluer troubles du sommeil sous-jacents\n"
            )
        elif flexibility < 10 and languid <= 15:
            interpretation += (
                "Profil RIGIDE mais VIGOUREUX\n"
                "Bonne vigueur mais faible adaptabilité horaire.\n"
                "• Fonctionne bien avec horaires réguliers\n"
                "• Difficulté avec horaires variables\n"
                "• Recommandation: maintenir horaires stables\n"
            )
        else:
            interpretation += (
                "⚠️ Profil RIGIDE ET LANGUIDE\n"
                "Faible flexibilité et vigueur circadienne réduites.\n"
                "• Besoin impératif d'horaires réguliers\n"
                "• Contre-indication au travail posté\n"
                "• Évaluation approfondie du sommeil recommandée\n"
                "• Considérer troubles circadiens (PSQI) et somnolence (Epworth)\n"
            )
        
        # Clinical recommendations
        interpretation += "\n=== RECOMMANDATIONS CLINIQUES ===\n"
        
        if flexibility < 10:
            interpretation += "• Éviter le travail posté ou horaires variables\n"
            interpretation += "• Maintenir horaires de sommeil réguliers\n"
            interpretation += "• Lumière vive le matin pour renforcer rythme circadien\n"
        
        if languid >= 20:
            interpretation += "• Évaluation PSQI (qualité du sommeil)\n"
            interpretation += "• Évaluation Epworth (somnolence diurne)\n"
            interpretation += "• Dépistage apnée du sommeil\n"
            interpretation += "• Hygiène du sommeil stricte\n"
            interpretation += "• Considérer polysomnographie si symptômes persistants\n"
        
        if flexibility >= 15 and languid <= 15:
            interpretation += "• Profil favorable - Pas de contre-indication horaire\n"
            interpretation += "• Peut tolérer travail posté si nécessaire\n"
            interpretation += "• Maintenir hygiène du sommeil standard\n"
        
        interpretation += (
            "\nNote: Le CTI doit être interprété en conjonction avec d'autres "
            "outils d'évaluation du sommeil (PSQI, Epworth) pour une évaluation complète "
            "des rythmes circadiens et de la qualité du sommeil."
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
                        "message": "Les 11 items doivent être renseignés (1=Presque jamais … 5=Presque toujours)."
                    },
                    {
                        "id": "range_1_5",
                        "level": "error",
                        "message": "Chaque item doit être un entier entre 1 et 5."
                    }
                ]
            },
            "scoring": {
                "scales": [
                    {
                        "id": "cti_flexibilite",
                        "label": "CTI – Flexibilité / Rigidité (5–25)",
                        "description": "Somme des items 2 + 4 + 6 + 8 + 10. Un score élevé = tendance plus flexible.",
                        "items": [f"q{i}" for i in self.FLEXIBILITY_ITEMS],
                        "range": [5, 25]
                    },
                    {
                        "id": "cti_languide",
                        "label": "CTI – Languide / Vigoureux (6–30)",
                        "description": "Somme des items 1 + 3 + 5 + 7 + 9 + 11. Un score élevé = tendance plus languide.",
                        "items": [f"q{i}" for i in self.LANGUID_ITEMS],
                        "range": [6, 30]
                    }
                ]
            },
            "provenance": {
                "created_at": datetime.utcnow().isoformat() + "Z",
                "updated_at": datetime.utcnow().isoformat() + "Z",
                "validated_by": "IngénieurQuestionnaire",
                "validation_date": datetime.utcnow().date().isoformat(),
                "references": [
                    "Di Milia L, Smith PA, Folkard S. Personality and Individual Differences. 2005;39:1293–1305."
                ],
                "notes": [
                    "Les sujets vigoureux et flexibles sont mieux ajustés dans leurs rythmes circadiens.",
                    "À articuler avec PSQI et ESS (Epworth) pour évaluer sommeil et somnolence diurne."
                ]
            }
        }

