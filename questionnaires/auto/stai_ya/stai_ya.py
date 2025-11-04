"""
STAI-YA (Inventaire d'Anxiété État - STAI Forme Y-A)
State-Trait Anxiety Inventory - Form Y-A (State Anxiety)

This module implements the STAI Form Y-A, which measures state anxiety 
(i.e., anxiety "right now, at this moment").
"""

from typing import Dict, List, Optional, Any
from datetime import datetime


class STAIYAError(Exception):
    """Custom exception for STAI-YA questionnaire errors."""
    pass


class STAIYA:
    """
    STAI-YA (State-Trait Anxiety Inventory - Form Y-A)
    
    A 20-item self-report questionnaire measuring state anxiety
    (how the person feels "right now, at this moment").
    
    Attributes:
        id: Unique identifier for the questionnaire
        name: Full name in French
        abbreviation: Short form
        language: Language code
        version: Version number
        reference_period: Time frame for responses
        description: Brief description of the questionnaire
    """
    
    # Reverse-scored items (calmer, more positive states)
    REVERSE_ITEMS = {1, 2, 5, 8, 10, 11, 15, 16, 19, 20}
    
    # Item texts in French
    ITEM_TEXTS = [
        "Je me sens calme.",
        "Je me sens en sécurité, sans inquiétude, en sûreté.",
        "Je suis tendu(e), crispé(e).",
        "Je me sens surmené(e).",
        "Je me sens tranquille, bien dans ma peau.",
        "Je me sens ému(e), bouleversé(e), contrarié(e).",
        "L'idée de malheurs éventuels me tracasse en ce moment.",
        "Je me sens content(e).",
        "Je me sens effrayé(e).",
        "Je me sens à mon aise.",
        "Je sens que j'ai confiance en moi.",
        "Je me sens nerveux (nerveuse), irritable.",
        "J'ai la frousse, la trouille (j'ai peur).",
        "Je me sens indécis(e).",
        "Je suis décontracté(e), détendu(e).",
        "Je suis satisfait(e).",
        "Je suis inquiet, soucieux (inquiète, soucieuse).",
        "Je ne sais plus où j'en suis, je me sens déconcerté(e), dérouté(e).",
        "Je me sens solide, posé(e), pondéré(e), réfléchi(e).",
        "Je me sens de bonne humeur, aimable."
    ]
    
    # Response options
    RESPONSE_OPTIONS = [
        {"code": 1, "label": "non", "score": 1},
        {"code": 2, "label": "plutôt non", "score": 2},
        {"code": 3, "label": "plutôt oui", "score": 3},
        {"code": 4, "label": "oui", "score": 4}
    ]
    
    def __init__(self):
        """Initialize the STAI-YA questionnaire."""
        self.id = "STAI-YA.fr"
        self.name = "Inventaire d'Anxiété État (STAI – Forme Y-A)"
        self.abbreviation = "STAI-YA"
        self.language = "fr-FR"
        self.version = "1.0"
        self.reference_period = "À l'instant, juste en ce moment"
        self.description = (
            "Échelle d'anxiété-état à 20 items (non / plutôt non / plutôt oui / oui). "
            "Cotation 1–4, avec inversion pour 10 items. Score total 20–80."
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
            "num_items": 20,
            "response_scale": "4-point scale (non/plutôt non/plutôt oui/oui)",
            "score_range": [20, 80],
            "reverse_items": sorted(list(self.REVERSE_ITEMS))
        }
    
    def get_questions(self) -> List[Dict[str, Any]]:
        """
        Get all questionnaire items.
        
        Returns:
            List of question dictionaries
        """
        questions = []
        for i, text in enumerate(self.ITEM_TEXTS, start=1):
            question = {
                "id": f"q{i}",
                "number": i,
                "section_id": "sec1",
                "text": f"{i}. {text}",
                "type": "single_choice",
                "required": True,
                "options": self.RESPONSE_OPTIONS.copy(),
                "reverse_scored": i in self.REVERSE_ITEMS
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
                "label": "STAI-YA – 20 items (État)",
                "description": "Cochez une réponse par ligne : non / plutôt non / plutôt oui / oui",
                "question_ids": [f"q{i}" for i in range(1, 21)]
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
            STAIYAError: If validation fails critically
        """
        errors = []
        warnings = []
        
        # Check all 20 items are present
        expected_items = [f"q{i}" for i in range(1, 21)]
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
        
        # Check for unusual patterns (all same response)
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
        Calculate STAI-YA score.
        
        Args:
            answers: Dictionary mapping question IDs (q1-q20) to response values (1-4)
        
        Returns:
            Dictionary containing:
                - total_score: Sum of all items after reverse scoring (20-80)
                - category: Anxiety level category (French norms)
                - item_scores: Individual item scores after reverse coding
                - interpretation: Clinical interpretation
        
        Raises:
            STAIYAError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation["valid"]:
            raise STAIYAError(
                f"Validation échouée: {'; '.join(validation['errors'])}"
            )
        
        # Calculate scores with reverse coding
        item_scores = {}
        total = 0
        
        for i in range(1, 21):
            qid = f"q{i}"
            value = answers[qid]
            
            # Apply reverse scoring if needed
            if i in self.REVERSE_ITEMS:
                scored_value = 5 - value
            else:
                scored_value = value
            
            item_scores[qid] = {
                "raw": value,
                "scored": scored_value,
                "reversed": i in self.REVERSE_ITEMS
            }
            total += scored_value
        
        # Determine anxiety category based on French norms
        if total <= 35:
            category = "Anxiété état très faible"
            severity = "very_low"
        elif 36 <= total <= 45:
            category = "Anxiété état faible"
            severity = "low"
        elif 46 <= total <= 55:
            category = "Anxiété état moyenne"
            severity = "average"
        elif 56 <= total <= 65:
            category = "Anxiété état élevée"
            severity = "high"
        else:  # >= 66
            category = "Anxiété état très élevée"
            severity = "very_high"
        
        # Generate interpretation
        interpretation = self._generate_interpretation(total, severity)
        
        return {
            "total_score": total,
            "score_range": [20, 80],
            "category": category,
            "severity": severity,
            "item_scores": item_scores,
            "interpretation": interpretation,
            "warnings": validation["warnings"],
            "calculation_date": datetime.utcnow().isoformat() + "Z"
        }
    
    def _generate_interpretation(self, score: int, severity: str) -> str:
        """
        Generate clinical interpretation based on score.
        
        Args:
            score: Total STAI-YA score
            severity: Severity level
        
        Returns:
            Clinical interpretation text in French
        """
        interpretations = {
            "very_low": (
                f"Score de {score}/80 indique un niveau d'anxiété état très faible. "
                "Le patient rapporte se sentir très calme et détendu en ce moment."
            ),
            "low": (
                f"Score de {score}/80 indique un niveau d'anxiété état faible. "
                "Le patient rapporte un niveau d'anxiété légèrement en dessous de la moyenne."
            ),
            "average": (
                f"Score de {score}/80 indique un niveau d'anxiété état moyen. "
                "Le patient rapporte un niveau d'anxiété dans la norme."
            ),
            "high": (
                f"Score de {score}/80 indique un niveau d'anxiété état élevée. "
                "Le patient rapporte un niveau d'anxiété cliniquement significatif nécessitant "
                "une attention clinique."
            ),
            "very_high": (
                f"Score de {score}/80 indique un niveau d'anxiété état très élevée. "
                "Le patient rapporte un niveau d'anxiété très élevé en ce moment, suggérant "
                "une détresse aiguë nécessitant une évaluation et une intervention immédiates."
            )
        }
        return interpretations[severity]
    
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
            "scoring": {
                "scales": [
                    {
                        "id": "stai_ya_total",
                        "label": "STAI-YA – Score total (20–80)",
                        "description": (
                            "Somme des 20 items après recodage "
                            "(items 1,2,5,8,10,11,15,16,19,20 inversés selon le manuel)."
                        ),
                        "items": [f"q{i}" for i in range(1, 21)],
                        "range": [20, 80]
                    }
                ],
                "categories": [
                    {"range": [20, 35], "label": "Anxiété état très faible", "severity": "very_low"},
                    {"range": [36, 45], "label": "Anxiété état faible", "severity": "low"},
                    {"range": [46, 55], "label": "Anxiété état moyenne", "severity": "average"},
                    {"range": [56, 65], "label": "Anxiété état élevée", "severity": "high"},
                    {"range": [66, 80], "label": "Anxiété état très élevée", "severity": "very_high"}
                ]
            },
            "logic": {            },
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

