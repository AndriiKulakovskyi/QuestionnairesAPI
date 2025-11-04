"""
AQ-12 (Aggression Questionnaire - 12 items)

This module implements the short version of the Aggression Questionnaire (AQ-12),
which assesses four dimensions of aggression: Physical, Verbal, Anger, and Hostility.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime


class AQ12Error(Exception):
    """Custom exception for AQ-12 questionnaire errors."""
    pass


class AQ12:
    """
    AQ-12 (Aggression Questionnaire - 12 items)
    
    A 12-item self-report questionnaire measuring aggression across
    four dimensions: Physical Aggression, Verbal Aggression, Anger, and Hostility.
    
    Attributes:
        id: Unique identifier for the questionnaire
        name: Full name in French
        abbreviation: Short form (AQ-12)
        language: Language code
        version: Version number
        reference_period: Time frame for responses (typical functioning)
        description: Brief description of the questionnaire
    """
    
    # Subscale item mappings (1-indexed)
    PHYSICAL_AGGRESSION_ITEMS = [1, 5, 9]
    VERBAL_AGGRESSION_ITEMS = [2, 6, 10]
    ANGER_ITEMS = [3, 7, 11]
    HOSTILITY_ITEMS = [4, 8, 12]
    
    # Item texts in French
    ITEM_TEXTS = [
        "Si on me provoque, je peux cogner.",
        "J'exprime souvent mon désaccord avec les autres.",
        "Je m'emporte rapidement.",
        "Parfois, j'ai l'impression que je n'ai pas été gâté par la vie comme les autres.",
        "Il y a des personnes qui me gonflent tellement qu'on peut en arriver aux mains.",
        "Je ne peux pas m'empêcher d'entrer en conflit quand les autres ne sont pas d'accord avec moi.",
        "Parfois, je pète un câble sans raison.",
        "Je me demande parfois pourquoi je ressens tant d'amertume.",
        "J'ai déjà menacé quelqu'un.",
        "Mes amis disent que j'ai l'esprit de contradiction.",
        "J'ai du mal à contrôler mon humeur.",
        "Les autres semblent toujours avoir plus de chances que moi."
    ]
    
    # Response options (1-6)
    RESPONSE_OPTIONS = [
        {"code": 1, "label": "1 – Pas du tout moi", "score": 1},
        {"code": 2, "label": "2", "score": 2},
        {"code": 3, "label": "3", "score": 3},
        {"code": 4, "label": "4", "score": 4},
        {"code": 5, "label": "5", "score": 5},
        {"code": 6, "label": "6 – Tout à fait moi", "score": 6}
    ]
    
    def __init__(self):
        """Initialize the AQ-12 questionnaire."""
        self.id = "AQ-12.fr"
        self.name = "Questionnaire d'Agression – 12 items (AQ-12) – Version française"
        self.abbreviation = "AQ-12"
        self.language = "fr-FR"
        self.version = "1.0"
        self.reference_period = "Mode de fonctionnement habituel"
        self.description = (
            "Mesure l'agression auto-rapportée sur 4 dimensions. 12 items, "
            "réponses 1..6 (1=Pas du tout moi, 6=Tout à fait moi). "
            "Sous-scores: Agression physique, Agression verbale, Colère, Hostilité."
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
            "num_items": 12,
            "response_scale": "6-point scale (1=Pas du tout moi, 6=Tout à fait moi)",
            "score_range": [12, 72],
            "score_type": "sum",
            "subscales": {
                "physical_aggression": {"items": self.PHYSICAL_AGGRESSION_ITEMS, "range": [3, 18]},
                "verbal_aggression": {"items": self.VERBAL_AGGRESSION_ITEMS, "range": [3, 18]},
                "anger": {"items": self.ANGER_ITEMS, "range": [3, 18]},
                "hostility": {"items": self.HOSTILITY_ITEMS, "range": [3, 18]}
            }
        }
    
    def get_questions(self) -> List[Dict[str, Any]]:
        """
        Get all questionnaire items.
        
        Returns:
            List of question dictionaries
        """
        questions = []
        for i, text in enumerate(self.ITEM_TEXTS, start=1):
            # Determine which subscale this item belongs to
            subscale = None
            if i in self.PHYSICAL_AGGRESSION_ITEMS:
                subscale = "physical_aggression"
            elif i in self.VERBAL_AGGRESSION_ITEMS:
                subscale = "verbal_aggression"
            elif i in self.ANGER_ITEMS:
                subscale = "anger"
            elif i in self.HOSTILITY_ITEMS:
                subscale = "hostility"
            
            question = {
                "id": f"q{i}",
                "number": i,
                "section_id": "sec1",
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
                "id": "sec1",
                "label": "AQ-12 – 12 items (1..6)",
                "description": "1 = Pas du tout moi … 6 = Tout à fait moi",
                "question_ids": [f"q{i}" for i in range(1, 13)]
            }
        ]
    
    def validate_answers(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Validate questionnaire responses.
        
        Args:
            answers: Dictionary mapping question IDs to response values (1-6)
        
        Returns:
            Dictionary containing validation results with 'valid', 'errors', and 'warnings' keys
        
        Raises:
            AQ12Error: If validation fails critically
        """
        errors = []
        warnings = []
        
        # Check all 12 items are present
        expected_items = [f"q{i}" for i in range(1, 13)]
        missing = [qid for qid in expected_items if qid not in answers]
        
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Validate each response value
        for qid in expected_items:
            if qid in answers:
                value = answers[qid]
                if not isinstance(value, int):
                    errors.append(f"{qid}: la valeur doit être un entier (reçu: {type(value).__name__})")
                elif value < 1 or value > 6:
                    errors.append(f"{qid}: la valeur doit être entre 1 et 6 (reçu: {value})")
        
        # Check for unusual patterns
        if not errors and len(set(answers.values())) == 1:
            warnings.append(
                "Toutes les réponses sont identiques. Veuillez vérifier que le patient "
                "a bien compris les instructions."
            )
        
        # Check for all minimum (no aggression reported)
        if not errors and all(answers.get(f"q{i}", 0) == 1 for i in range(1, 13)):
            warnings.append(
                "Toutes les réponses sont à 1 (Pas du tout moi). "
                "Cela peut indiquer une sous-évaluation ou une désirabilité sociale."
            )
        
        # Check for all maximum (extreme aggression)
        if not errors and all(answers.get(f"q{i}", 0) == 6 for i in range(1, 13)):
            warnings.append(
                "Toutes les réponses sont à 6 (Tout à fait moi). "
                "Cela suggère un niveau d'agression extrême nécessitant une évaluation clinique urgente."
            )
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def calculate_score(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Calculate AQ-12 scores.
        
        Args:
            answers: Dictionary mapping question IDs (q1-q12) to response values (1-6)
        
        Returns:
            Dictionary containing:
                - subscale_scores: Scores for each subscale (3-18)
                - total_score: Total sum score (12-72)
                - item_scores: Individual item scores with subscale info
                - interpretation: Clinical interpretation
        
        Raises:
            AQ12Error: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation["valid"]:
            raise AQ12Error(
                f"Validation échouée: {'; '.join(validation['errors'])}"
            )
        
        # Calculate subscale scores (sums)
        physical_score = sum(answers[f"q{i}"] for i in self.PHYSICAL_AGGRESSION_ITEMS)
        verbal_score = sum(answers[f"q{i}"] for i in self.VERBAL_AGGRESSION_ITEMS)
        anger_score = sum(answers[f"q{i}"] for i in self.ANGER_ITEMS)
        hostility_score = sum(answers[f"q{i}"] for i in self.HOSTILITY_ITEMS)
        
        # Calculate total score (sum of all 12 items)
        total_score = sum(answers[f"q{i}"] for i in range(1, 13))
        
        # Collect item scores
        item_scores = {}
        for i in range(1, 13):
            qid = f"q{i}"
            subscale = None
            if i in self.PHYSICAL_AGGRESSION_ITEMS:
                subscale = "physical_aggression"
            elif i in self.VERBAL_AGGRESSION_ITEMS:
                subscale = "verbal_aggression"
            elif i in self.ANGER_ITEMS:
                subscale = "anger"
            elif i in self.HOSTILITY_ITEMS:
                subscale = "hostility"
            
            item_scores[qid] = {
                "score": answers[qid],
                "subscale": subscale
            }
        
        # Generate interpretation
        interpretation = self._generate_interpretation(
            total_score,
            physical_score,
            verbal_score,
            anger_score,
            hostility_score
        )
        
        return {
            "subscale_scores": {
                "physical_aggression": physical_score,
                "verbal_aggression": verbal_score,
                "anger": anger_score,
                "hostility": hostility_score
            },
            "total_score": total_score,
            "score_range": [12, 72],
            "subscale_ranges": {
                "physical_aggression": [3, 18],
                "verbal_aggression": [3, 18],
                "anger": [3, 18],
                "hostility": [3, 18]
            },
            "item_scores": item_scores,
            "interpretation": interpretation,
            "warnings": validation["warnings"],
            "calculation_date": datetime.utcnow().isoformat() + "Z"
        }
    
    def _generate_interpretation(
        self,
        total_score: int,
        physical: int,
        verbal: int,
        anger: int,
        hostility: int
    ) -> str:
        """
        Generate clinical interpretation based on scores.
        
        Args:
            total_score: Total score (12-72)
            physical: Physical aggression subscale (3-18)
            verbal: Verbal aggression subscale (3-18)
            anger: Anger subscale (3-18)
            hostility: Hostility subscale (3-18)
        
        Returns:
            Clinical interpretation text in French
        """
        interpretation = f"Score total de {total_score}/72 indique "
        
        if total_score < 24:
            interpretation += (
                "un niveau d'agression très faible. Le patient rapporte peu ou pas "
                "de tendances agressives dans son fonctionnement habituel."
            )
        elif total_score < 36:
            interpretation += (
                "un niveau d'agression faible à modéré. Le patient rapporte des "
                "tendances agressives occasionnelles dans les limites de la normale."
            )
        elif total_score < 48:
            interpretation += (
                "un niveau d'agression modéré. Le patient rapporte des tendances "
                "agressives qui peuvent nécessiter une attention clinique."
            )
        elif total_score < 60:
            interpretation += (
                "un niveau d'agression élevé. Le patient rapporte des tendances "
                "agressives significatives nécessitant une évaluation et un suivi clinique."
            )
        else:
            interpretation += (
                "un niveau d'agression très élevé. Le patient rapporte des tendances "
                "agressives sévères nécessitant une intervention clinique immédiate. "
                "Évaluation du risque hétéro-agressif recommandée."
            )
        
        # Add subscale details
        interpretation += "\n\nDétails par dimension:"
        
        interpretation += f"\n• Agression physique ({physical}/18): "
        if physical >= 15:
            interpretation += "Niveau très élevé - Risque de violence physique."
        elif physical >= 12:
            interpretation += "Niveau élevé - Tendances à l'agression physique."
        elif physical >= 9:
            interpretation += "Niveau modéré - Quelques réactions physiques agressives."
        else:
            interpretation += "Niveau faible - Peu ou pas d'agression physique."
        
        interpretation += f"\n• Agression verbale ({verbal}/18): "
        if verbal >= 15:
            interpretation += "Niveau très élevé - Comportements verbalement agressifs fréquents."
        elif verbal >= 12:
            interpretation += "Niveau élevé - Conflits verbaux fréquents."
        elif verbal >= 9:
            interpretation += "Niveau modéré - Désaccords verbaux occasionnels."
        else:
            interpretation += "Niveau faible - Communication généralement non-agressive."
        
        interpretation += f"\n• Colère ({anger}/18): "
        if anger >= 15:
            interpretation += "Niveau très élevé - Problèmes sévères de contrôle de la colère."
        elif anger >= 12:
            interpretation += "Niveau élevé - Difficultés notables de gestion de la colère."
        elif anger >= 9:
            interpretation += "Niveau modéré - Contrôle de la colère parfois difficile."
        else:
            interpretation += "Niveau faible - Bon contrôle émotionnel."
        
        interpretation += f"\n• Hostilité ({hostility}/18): "
        if hostility >= 15:
            interpretation += "Niveau très élevé - Attitudes hostiles marquées et amertume."
        elif hostility >= 12:
            interpretation += "Niveau élevé - Méfiance et ressentiment fréquents."
        elif hostility >= 9:
            interpretation += "Niveau modéré - Quelques attitudes négatives envers autrui."
        else:
            interpretation += "Niveau faible - Attitudes généralement positives."
        
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
                        "message": "Les 12 items doivent être renseignés (entiers 1..6)."
                    },
                    {
                        "id": "range_1_6",
                        "level": "error",
                        "message": "Chaque item AQ-12 doit être un entier entre 1 et 6."
                    }
                ]
            },
            "scoring": {
                "variables": [],
                "scales": [
                    {
                        "id": "aq12_total",
                        "label": "AQ-12 – Total (12–72)",
                        "description": "Somme des 12 items (aucun item inversé).",
                        "items": [f"q{i}" for i in range(1, 13)],
                        "range": [12, 72]
                    },
                    {
                        "id": "aq12_physique",
                        "label": "Agression physique (3–18)",
                        "description": "Somme des items 1, 5, 9.",
                        "items": [f"q{i}" for i in self.PHYSICAL_AGGRESSION_ITEMS],
                        "range": [3, 18]
                    },
                    {
                        "id": "aq12_verbale",
                        "label": "Agression verbale (3–18)",
                        "description": "Somme des items 2, 6, 10.",
                        "items": [f"q{i}" for i in self.VERBAL_AGGRESSION_ITEMS],
                        "range": [3, 18]
                    },
                    {
                        "id": "aq12_colere",
                        "label": "Colère (3–18)",
                        "description": "Somme des items 3, 7, 11.",
                        "items": [f"q{i}" for i in self.ANGER_ITEMS],
                        "range": [3, 18]
                    },
                    {
                        "id": "aq12_hostilite",
                        "label": "Hostilité (3–18)",
                        "description": "Somme des items 4, 8, 12.",
                        "items": [f"q{i}" for i in self.HOSTILITY_ITEMS],
                        "range": [3, 18]
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

