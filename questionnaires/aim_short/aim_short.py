"""
AIM-short (Affect Intensity Measure - Version courte)

This module implements the short version of the Affect Intensity Measure (AIM),
which assesses emotional reactivity - the intensity with which individuals experience emotions.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime


class AIMShortError(Exception):
    """Custom exception for AIM-short questionnaire errors."""
    pass


class AIMShort:
    """
    AIM-short (Affect Intensity Measure - Short Version)
    
    A 20-item self-report questionnaire measuring the intensity of emotional experiences
    across various affective states (happiness, sadness, anxiety, guilt).
    
    Attributes:
        id: Unique identifier for the questionnaire
        name: Full name in French
        abbreviation: Short form (AIM-20)
        language: Language code
        version: Version number
        reference_period: Time frame for responses (typical functioning)
        description: Brief description of the questionnaire
    """
    
    # Reverse-scored items (items expressing less intense emotions)
    REVERSE_ITEMS = {5, 10, 13, 15, 18, 20}
    
    # Item texts in French
    ITEM_TEXTS = [
        "Quand je suis heureux(se), c'est avec une forte exubérance.",
        "Mes périodes d'humeur joyeuse sont si fortes que j'ai l'impression d'être au paradis.",
        "Si je termine une tâche que je jugeais impossible à faire, je me sens en extase.",
        "Les films tristes me touchent profondément.",
        "Quand je suis heureux(se), c'est un sentiment d'être sans inquiétude et content(e) plutôt qu'excité et plein d'enthousiasme.",
        "Quand je parle devant un groupe pour la première fois, ma voix devient tremblante et mon cœur bat vite.",
        "Quand je me sens bien, c'est facile pour moi d'osciller entre des périodes de bonne humeur et des moments où je suis très joyeux(se).",
        "Quand je suis heureux(se), je me sens comme si j'éclatais de joie.",
        "Quand je suis heureux(se), je me sens plein d'énergie.",
        "Quand je réussis quelque chose, ma réaction est une satisfaction calme.",
        "Quand je fais quelque chose de mal, j'ai un sentiment très fort de culpabilité et de honte.",
        "Quand les choses vont bien, je me sens comme si j'étais \"au sommet du monde\".",
        "Quand je sais que j'ai fait quelque chose très bien, je me sens détendu(e) et content(e) plutôt qu'excité(e) et exalté(e).",
        "Quand je suis anxieux(se), c'est habituellement très fort.",
        "Quand je me sens heureux(se), c'est un sentiment de bonheur calme.",
        "Quand je suis heureux(se), je déborde d'énergie.",
        "Quand je me sens coupable, cette émotion est forte.",
        "Je décrirai mes émotions heureuses comme étant plus proches de la satisfaction que de la joie.",
        "Quand je suis heureux(se), je tremble.",
        "Quand je suis heureux(se), mes sentiments sont plus proches de la satisfaction et du calme interne que de l'excitation et de la joie de vivre."
    ]
    
    # Response options (6-point scale)
    RESPONSE_OPTIONS = [
        {"code": 1, "label": "1 – Jamais", "score": 1},
        {"code": 2, "label": "2 – Presque jamais", "score": 2},
        {"code": 3, "label": "3 – Occasionnellement", "score": 3},
        {"code": 4, "label": "4 – Habituellement", "score": 4},
        {"code": 5, "label": "5 – Presque toujours", "score": 5},
        {"code": 6, "label": "6 – Toujours", "score": 6}
    ]
    
    def __init__(self):
        """Initialize the AIM-short questionnaire."""
        self.id = "AIM-short.fr"
        self.name = "Affect Intensity Measure (AIM) – Version courte (FR)"
        self.abbreviation = "AIM-20"
        self.language = "fr-FR"
        self.version = "1.0"
        self.reference_period = "Mode de fonctionnement habituel (hors périodes d'humeur anormalement basse ou élevée)"
        self.description = (
            "Mesure la réactivité émotionnelle (intensité des émotions) – 20 items, "
            "réponses 1..6. Certains items sont inversés. "
            "Score = moyenne des 20 items recodés (1..6)."
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
            "response_scale": "6-point scale (Jamais to Toujours)",
            "score_range": [1.0, 6.0],
            "score_type": "mean",
            "reverse_items": sorted(list(self.REVERSE_ITEMS)),
            "notes": [
                "Consigne : se baser sur son fonctionnement habituel, hors épisodes thymiques anormaux."
            ]
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
                "label": "AIM – 20 items (1..6)",
                "description": "Jamais (1) … Toujours (6)",
                "question_ids": [f"q{i}" for i in range(1, 21)]
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
            AIMShortError: If validation fails critically
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
                elif value < 1 or value > 6:
                    errors.append(f"{qid}: la valeur doit être entre 1 et 6 (reçu: {value})")
        
        # Check for unusual patterns (all same response)
        if not errors and len(set(answers.values())) == 1:
            warnings.append(
                "Toutes les réponses sont identiques. Veuillez vérifier que le patient "
                "a bien compris les instructions."
            )
        
        # Check for all minimum or all maximum
        if not errors:
            if all(answers.get(f"q{i}", 0) == 1 for i in range(1, 21)):
                warnings.append(
                    "Toutes les réponses sont à 1 (Jamais). Cela suggère une très faible "
                    "réactivité émotionnelle ou une possible sous-évaluation."
                )
            elif all(answers.get(f"q{i}", 0) == 6 for i in range(1, 21)):
                warnings.append(
                    "Toutes les réponses sont à 6 (Toujours). Cela suggère une réactivité "
                    "émotionnelle extrême ou une possible sur-évaluation."
                )
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def calculate_score(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Calculate AIM-short score.
        
        Args:
            answers: Dictionary mapping question IDs (q1-q20) to response values (1-6)
        
        Returns:
            Dictionary containing:
                - mean_score: Mean of all items after reverse coding (1.0-6.0)
                - sum_score: Sum of all items after reverse coding (20-120)
                - category: Qualitative interpretation
                - item_scores: Individual item scores after reverse coding
                - interpretation: Clinical interpretation
        
        Raises:
            AIMShortError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation["valid"]:
            raise AIMShortError(
                f"Validation échouée: {'; '.join(validation['errors'])}"
            )
        
        # Calculate scores with reverse coding
        item_scores = {}
        total = 0
        
        for i in range(1, 21):
            qid = f"q{i}"
            value = answers[qid]
            
            # Apply reverse scoring if needed (7 - value)
            if i in self.REVERSE_ITEMS:
                scored_value = 7 - value
            else:
                scored_value = value
            
            item_scores[qid] = {
                "raw": value,
                "scored": scored_value,
                "reversed": i in self.REVERSE_ITEMS
            }
            total += scored_value
        
        # Calculate mean score
        mean_score = total / 20.0
        
        # Determine category based on mean score
        category = self._get_category(mean_score)
        severity = self._get_severity(mean_score)
        
        # Generate interpretation
        interpretation = self._generate_interpretation(mean_score, category)
        
        return {
            "mean_score": round(mean_score, 2),
            "sum_score": total,
            "score_range": [1.0, 6.0],
            "sum_range": [20, 120],
            "category": category,
            "severity": severity,
            "item_scores": item_scores,
            "interpretation": interpretation,
            "warnings": validation["warnings"],
            "calculation_date": datetime.utcnow().isoformat() + "Z"
        }
    
    def _get_category(self, mean_score: float) -> str:
        """
        Map mean score to qualitative category.
        
        Args:
            mean_score: Mean score (1.0-6.0)
        
        Returns:
            Qualitative category label
        """
        # Round to nearest integer (clamped to 1-6)
        rounded = int(round(min(6.0, max(1.0, mean_score))))
        
        mapping = {
            1: "Très faible (proche de « jamais »)",
            2: "Presque jamais intense",
            3: "Occasionnellement intense",
            4: "Habituellement intense",
            5: "Presque toujours intense",
            6: "Toujours intense"
        }
        
        return mapping.get(rounded, "Interprétation continue")
    
    def _get_severity(self, mean_score: float) -> str:
        """
        Get severity level based on mean score.
        
        Args:
            mean_score: Mean score (1.0-6.0)
        
        Returns:
            Severity level code
        """
        if mean_score < 2.0:
            return "very_low"
        elif mean_score < 3.0:
            return "low"
        elif mean_score < 4.0:
            return "moderate"
        elif mean_score < 5.0:
            return "high"
        else:
            return "very_high"
    
    def _generate_interpretation(self, mean_score: float, category: str) -> str:
        """
        Generate clinical interpretation based on score.
        
        Args:
            mean_score: Mean score
            category: Category label
        
        Returns:
            Clinical interpretation text in French
        """
        interpretation = (
            f"Score moyen de {mean_score:.2f}/6.00 indique une intensité émotionnelle "
            f"« {category} ». "
        )
        
        if mean_score < 2.5:
            interpretation += (
                "Le patient rapporte vivre ses émotions avec une intensité très faible. "
                "Cela peut refléter un style émotionnel modéré, un détachement émotionnel, "
                "ou une tendance à minimiser les expériences affectives."
            )
        elif mean_score < 3.5:
            interpretation += (
                "Le patient rapporte vivre ses émotions avec une intensité faible à modérée. "
                "Les réactions émotionnelles sont généralement mesurées et contrôlées."
            )
        elif mean_score < 4.5:
            interpretation += (
                "Le patient rapporte une intensité émotionnelle dans la moyenne. "
                "Les émotions sont vécues de manière habituelle, avec une réactivité "
                "émotionnelle typique."
            )
        elif mean_score < 5.5:
            interpretation += (
                "Le patient rapporte vivre ses émotions avec une intensité élevée. "
                "Les expériences émotionnelles sont fortes et marquées, ce qui peut "
                "être associé à une sensibilité émotionnelle accrue."
            )
        else:
            interpretation += (
                "Le patient rapporte vivre ses émotions avec une intensité très élevée. "
                "Les réactions émotionnelles sont extrêmement fortes et intenses, "
                "ce qui peut être associé à une hypersensibilité émotionnelle ou "
                "à des troubles de la régulation émotionnelle."
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
                        "message": "Les 20 items doivent être renseignés (valeurs entières 1..6)."
                    },
                    {
                        "id": "range_1_6",
                        "level": "error",
                        "message": "Chaque item AIM doit être un entier entre 1 et 6."
                    }
                ]
            },
            "scoring": {
                "variables": [
                    {
                        "id": f"r{i}",
                        "description": f"Recodage inversé de q{i} (7 - q{i})",
                        "expression": {"-": [7, {"var": f"q{i}"}]}
                    } for i in self.REVERSE_ITEMS
                ],
                "scales": [
                    {
                        "id": "aim_total_mean",
                        "label": "AIM – Score moyen (1..6)",
                        "description": (
                            "Moyenne des 20 items après recodage "
                            "(items inversés : 5, 10, 13, 15, 18, 20)."
                        ),
                        "items": [f"q{i}" for i in range(1, 21)],
                        "range": [1, 6],
                        "notes": [
                            "Interprétation continue : plus proche de 6 = émotions vécues plus intensément.",
                            "Repères : 2=presque jamais, 3=occasionnellement, 4=habituellement, "
                            "5=presque toujours, 6=toujours (intenses)."
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

