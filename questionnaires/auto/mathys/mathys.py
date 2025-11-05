# -*- coding: utf-8 -*-
"""
MAThyS (Évaluation Multidimensionnelle des états thymiques)
French version - Multidimensional assessment of thymic states
"""

from typing import Dict, List, Optional, Any, Union
from datetime import datetime
from pydantic import BaseModel


class MAThySError(ValueError):
    """Custom exception for MAThyS validation errors"""
    pass


class ScaleOption(BaseModel):
    """Model for a scale question"""
    min_label: str
    max_label: str
    min_value: int
    max_value: int
    step: int
    center_hint: str


class Question(BaseModel):
    """Model for a question"""
    id: str
    section_id: str
    text: str
    type: str
    required: bool
    scale: ScaleOption
    constraints: Dict[str, Any]


class Section(BaseModel):
    """Model for a section"""
    id: str
    label: str
    description: str
    question_ids: List[str]


class SubscaleResult(BaseModel):
    """Model for subscale results"""
    name: str
    label: str
    score: float
    range: tuple
    items: List[str]


class ScoreResult(BaseModel):
    """Model for score results"""
    total_score: float
    subscales: Dict[str, SubscaleResult]
    recoded_scores: Dict[str, float]
    interpretation: str
    range: tuple = (0, 200)


class ValidationResult(BaseModel):
    """Model for validation results"""
    valid: bool
    errors: List[str] = []
    warnings: List[str] = []


class MAThyS:
    """
    MAThyS (Évaluation Multidimensionnelle des états thymiques) Questionnaire Class
    
    Provides methods to:
    - Retrieve instrument metadata
    - Get questions and sections
    - Validate answers
    - Compute scores with subscales
    """
    
    INSTRUMENT_ID = "MAThyS.fr"
    INSTRUMENT_NAME = "Évaluation Multidimensionnelle des états thymiques (MAThyS)"
    ABBREVIATION = "MAThyS"
    LANGUAGE = "fr-FR"
    VERSION = "1.0"
    REFERENCE_PERIOD = "La dernière semaine"
    
    # Items that require reverse scoring (10 - value)
    REVERSE_ITEMS = {5, 6, 7, 8, 9, 10, 17, 18}
    
    # Bipolar anchors (left_anchor, right_anchor) for each item
    ITEM_ANCHORS = [
        ("Je suis moins sensible que d'habitude aux couleurs", 
         "Je suis plus sensible que d'habitude aux couleurs"),
        ("Je manque de tonus", 
         "J'ai une tension interne importante"),
        ("J'ai l'impression d'être anesthésié(e) sur le plan des émotions", 
         "J'ai parfois le sentiment de perdre le contrôle de mes émotions"),
        ("Je suis replié(e) sur moi", 
         "Je suis désinhibé(e)"),
        ("Je suis facilement distrait(e), la moindre chose me fait perdre mon attention", 
         "Je ne suis pas attentif(ve) à mon environnement"),
        ("Je suis plus sensible que d'habitude au toucher", 
         "Je suis moins sensible que d'habitude au toucher"),
        ("J'ai l'impression que mon humeur varie beaucoup en fonction de mon environnement", 
         "Mon humeur est monotone et peu changeante"),
        ("Je suis particulièrement sensible à la musique", 
         "Je suis plus indifférent(e) que d'habitude à la musique"),
        ("Mon cerveau ne s'arrête jamais", 
         "Mon cerveau fonctionne au ralenti"),
        ("Je suis plus réactif(ve) à mon environnement", 
         "Je suis moins réactif(ve) à mon environnement"),
        ("Je me sens sans énergie", 
         "J'ai le sentiment d'avoir une grande énergie"),
        ("J'ai le sentiment que mes pensées sont ralenties", 
         "J'ai le sentiment que mes idées défilent dans ma tête"),
        ("Je trouve la nourriture sans goût", 
         "Je recherche les plaisirs gastronomiques car j'en apprécie davantage les saveurs"),
        ("J'ai moins envie de communiquer avec les autres", 
         "J'ai plus envie de communiquer avec les autres"),
        ("Je manque de motivation pour aller de l'avant", 
         "Je multiplie les projets nouveaux"),
        ("Ma perte d'intérêt pour mon environnement m'empêche de gérer le quotidien.", 
         "J'ai envie de faire plus de choses que d'habitude"),
        ("Je prends les décisions de manière plus rapide que d'habitude.", 
         "J'ai plus de difficultés que d'habitude à prendre des décisions"),
        ("Je ressens les émotions de manière très intense.", 
         "Mes émotions sont atténuées"),
        ("Je suis ralenti(e) dans mes mouvements.", 
         "Je suis physiquement agité(e)"),
        ("J'ai l'impression d'être moins sensible aux odeurs que d'habitude.", 
         "J'ai l'impression d'être plus sensible aux odeurs que d'habitude")
    ]
    
    # Subscale definitions
    SUBSCALES = {
        "emotion": {
            "label": "Émotion",
            "items": [3, 7, 10, 18],
            "range": (0, 40)
        },
        "motivation": {
            "label": "Motivation",
            "items": [2, 11, 12, 15, 16, 17, 19],
            "range": (0, 70)
        },
        "perception": {
            "label": "Perception sensorielle",
            "items": [1, 6, 8, 13, 20],
            "range": (0, 50)
        },
        "interaction": {
            "label": "Interaction personnelle",
            "items": [4, 14],
            "range": (0, 20)
        },
        "cognition": {
            "label": "Cognition",
            "items": [5, 9],
            "range": (0, 20)
        }
    }
    
    def __init__(self):
        """Initialize the MAThyS questionnaire"""
        self._sections = self._build_sections()
        self._questions = self._build_questions()
    
    def _build_sections(self) -> List[Section]:
        """Build the sections structure"""
        return [
            Section(
                id="sec_items",
                label="MAThyS – 20 items (0–10)",
                description="Indiquez votre état AU COURS DE LA DERNIÈRE SEMAINE",
                question_ids=[f"q{i}" for i in range(1, 21)]
            )
        ]
    
    def _build_questions(self) -> List[Question]:
        """Build all questions"""
        questions = []
        
        for i, (left_anchor, right_anchor) in enumerate(self.ITEM_ANCHORS, start=1):
            questions.append(Question(
                id=f"q{i}",
                section_id="sec_items",
                text=f"{i}.",
                type="scale",
                required=True,
                scale=ScaleOption(
                    min_label=left_anchor,
                    max_label=right_anchor,
                    min_value=0,
                    max_value=10,
                    step=1,
                    center_hint="Le centre (~5) = état habituel"
                ),
                constraints={
                    "value_type": "number",
                    "min_value": 0,
                    "max_value": 10
                }
            ))
        
        return questions
    
    def get_metadata(self) -> Dict[str, Any]:
        """Get instrument metadata"""
        return {
            "id": self.INSTRUMENT_ID,
            "name": self.INSTRUMENT_NAME,
            "abbreviation": self.ABBREVIATION,
            "language": self.LANGUAGE,
            "version": self.VERSION,
            "reference_period": self.REFERENCE_PERIOD,
            "description": "Échelle de 20 items (0–10 chacun) évaluant 5 dimensions thymiques; certains items sont inversés pour le calcul des scores. Score total = somme des 5 sous-scores.",
            "sources": [
                "MATHYS.pdf (version FR fournie)",
                "Mathys_CotationScore.docx (barème / sous-scores)",
                "Henry C. et al., BMC Psychiatry 2008;8:82 (développement & validation)"
            ],
            "total_questions": 20,
            "scoring_range": [0, 200],
            "reverse_items": list(self.REVERSE_ITEMS),
            "subscales": {
                name: {
                    "label": info["label"],
                    "items": info["items"],
                    "range": info["range"]
                }
                for name, info in self.SUBSCALES.items()
            }
        }
    
    def get_sections(self) -> List[Dict[str, Any]]:
        """Get all sections"""
        return [section.model_dump() for section in self._sections]
    
    def get_questions(self, section_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Get questions, optionally filtered by section
        
        Args:
            section_id: Optional section ID to filter questions
            
        Returns:
            List of questions as dictionaries
        """
        questions = self._questions
        if section_id:
            questions = [q for q in questions if q.section_id == section_id]
        return [q.model_dump() for q in questions]
    
    def get_question_by_id(self, question_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific question by ID"""
        for q in self._questions:
            if q.id == question_id:
                return q.model_dump()
        return None
    
    def validate_answers(self, answers: Dict[str, Union[int, float]]) -> ValidationResult:
        """
        Validate provided answers
        
        Args:
            answers: Dictionary of question_id -> answer mappings (0-10)
            
        Returns:
            ValidationResult with validation status and messages
        """
        errors = []
        warnings = []
        
        # Check for missing required questions
        expected_keys = [f"q{i}" for i in range(1, 21)]
        missing = [k for k in expected_keys if k not in answers]
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Check value ranges and types
        invalid = {}
        for k in expected_keys:
            if k in answers:
                try:
                    val = float(answers[k])
                    if val < 0 or val > 10:
                        invalid[k] = val
                except (ValueError, TypeError):
                    invalid[k] = answers[k]
        
        if invalid:
            errors.append(f"Valeurs invalides (doivent être des nombres entre 0 et 10): {invalid}")
        
        # Clinical warnings (only if no errors)
        if not errors:
            # Check if all values are at extremes
            try:
                values = [float(answers[k]) for k in expected_keys]
                
                # Warning if many extreme values
                extreme_count = sum(1 for v in values if v <= 1 or v >= 9)
                if extreme_count >= 15:
                    warnings.append(
                        f"{extreme_count} items sur 20 sont à des valeurs extrêmes (≤1 ou ≥9). "
                        "Vérifier la qualité des réponses."
                    )
                
                # Warning if all centered (potential non-engagement)
                centered_count = sum(1 for v in values if 4 <= v <= 6)
                if centered_count >= 18:
                    warnings.append(
                        "La plupart des réponses sont centrées (4-6). "
                        "Cela peut indiquer un état habituel ou un manque d'engagement."
                    )
            except (ValueError, TypeError):
                pass  # Already caught in validation
        
        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    def _recode_items(self, answers: Dict[str, Union[int, float]]) -> Dict[str, float]:
        """
        Recode items according to MAThyS scoring rules
        
        Args:
            answers: Raw answers (0-10)
            
        Returns:
            Recoded scores (reversed for items 5,6,7,8,9,10,17,18)
        """
        recoded = {}
        
        for i in range(1, 21):
            key = f"q{i}"
            val = float(answers[key])
            
            if i in self.REVERSE_ITEMS:
                # Reverse scoring: 10 - value
                recoded[key] = 10.0 - val
            else:
                recoded[key] = val
        
        return recoded
    
    def _calculate_subscale(
        self, 
        subscale_name: str, 
        recoded: Dict[str, float]
    ) -> SubscaleResult:
        """Calculate a single subscale score"""
        subscale_info = self.SUBSCALES[subscale_name]
        items = subscale_info["items"]
        
        # Sum the recoded values for this subscale's items
        score = sum(recoded[f"q{i}"] for i in items)
        
        return SubscaleResult(
            name=subscale_name,
            label=subscale_info["label"],
            score=score,
            range=subscale_info["range"],
            items=[f"q{i}" for i in items]
        )
    
    def calculate_score(self, answers: Dict[str, Union[int, float]]) -> ScoreResult:
        """
        Calculate MAThyS total score and subscales
        
        Args:
            answers: Dictionary with keys 'q1' through 'q20', values 0-10
            
        Returns:
            ScoreResult with total score, subscales, and interpretation
            
        Raises:
            MAThySError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation.valid:
            raise MAThySError("; ".join(validation.errors))
        
        # Recode items
        recoded = self._recode_items(answers)
        
        # Calculate subscales
        subscales = {}
        for subscale_name in self.SUBSCALES.keys():
            subscales[subscale_name] = self._calculate_subscale(subscale_name, recoded)
        
        # Calculate total score (sum of all subscales)
        total = sum(sub.score for sub in subscales.values())
        
        # Safety check
        if total < 0 or total > 200:
            raise MAThySError(f"Score hors bornes: {total}")
        
        # Build interpretation
        interpretation = self._build_interpretation(total, subscales, validation.warnings)
        
        return ScoreResult(
            total_score=total,
            subscales=subscales,
            recoded_scores=recoded,
            interpretation=interpretation
        )
    
    def _build_interpretation(
        self, 
        total: float,
        subscales: Dict[str, SubscaleResult],
        warnings: List[str]
    ) -> str:
        """Build clinical interpretation text"""
        interpretation = f"Score total MAThyS: {total:.1f}/200. "
        
        # Add subscale details
        interpretation += "Sous-scores: "
        subscale_texts = []
        for name, result in subscales.items():
            max_score = result.range[1]
            subscale_texts.append(f"{result.label}={result.score:.1f}/{max_score}")
        interpretation += ", ".join(subscale_texts) + ". "
        
        # General interpretation
        # Note: MAThyS is a dimensional tool; higher scores don't necessarily mean "worse"
        # as it measures intensity and variability of thymic states
        interpretation += (
            "Le MAThyS évalue l'intensité et la variabilité des états thymiques "
            "sur 5 dimensions (Émotion, Motivation, Perception, Interaction, Cognition). "
        )
        
        # Highlight extreme subscales
        extreme_low = []
        extreme_high = []
        for name, result in subscales.items():
            max_score = result.range[1]
            percentage = (result.score / max_score) * 100
            
            if percentage <= 20:
                extreme_low.append(result.label)
            elif percentage >= 80:
                extreme_high.append(result.label)
        
        if extreme_low:
            interpretation += f"Dimensions à score bas (≤20%): {', '.join(extreme_low)}. "
        if extreme_high:
            interpretation += f"Dimensions à score élevé (≥80%): {', '.join(extreme_high)}. "
        
        # Add warnings
        if warnings:
            interpretation += " ".join(warnings) + " "
        
        return interpretation.strip()
    
    def get_full_questionnaire(self) -> Dict[str, Any]:
        """Get complete questionnaire structure for frontend"""
        return {
            "metadata": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions()
        }

