# -*- coding: utf-8 -*-
"""
MARS (Medication Adherence Rating Scale)
French version - Self-assessment scale for medication adherence in psychiatry
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
from pydantic import BaseModel


class MARSError(ValueError):
    """Custom exception for MARS validation errors"""
    pass


class QuestionOption(BaseModel):
    """Model for a question option"""
    code: int
    label: str
    score: Optional[int] = None


class Question(BaseModel):
    """Model for a question"""
    id: str
    section_id: str
    text: str
    type: str
    required: bool
    options: List[QuestionOption]
    constraints: Dict[str, Any]


class Section(BaseModel):
    """Model for a section"""
    id: str
    label: str
    description: str
    question_ids: List[str]


class ScoreResult(BaseModel):
    """Model for score results"""
    total_score: int
    recoded_scores: Dict[str, int]
    interpretation: str
    range: tuple = (0, 10)


class ValidationResult(BaseModel):
    """Model for validation results"""
    valid: bool
    errors: List[str] = []
    warnings: List[str] = []


class MARS:
    """
    MARS (Medication Adherence Rating Scale) Questionnaire Class
    
    Provides methods to:
    - Retrieve instrument metadata
    - Get questions and sections
    - Validate answers
    - Compute scores
    """
    
    INSTRUMENT_ID = "MARS.fr"
    INSTRUMENT_NAME = "Medication Adherence Rating Scale (MARS) – Version française"
    ABBREVIATION = "MARS-10"
    LANGUAGE = "fr-FR"
    VERSION = "1.0"
    REFERENCE_PERIOD = "Semaine écoulée"
    
    # Items with positive scoring (YES=1, NO=0)
    POSITIVE_ITEMS = {7, 8}
    # Items with negative scoring (NO=1, YES=0)
    NEGATIVE_ITEMS = {1, 2, 3, 4, 5, 6, 9, 10}
    
    # Item texts from French version
    ITEMS = [
        "Vous est-il parfois arrivé d'oublier de prendre vos médicaments ?",
        "Négligez-vous parfois l'heure de prise d'un de vos médicaments ?",
        "Lorsque vous vous sentez mieux, interrompez-vous parfois votre traitement ?",
        "Vous est-il arrivé d'arrêter le traitement parce que vous vous sentiez moins bien en le prenant ?",
        "Je ne prends les médicaments que lorsque je me sens malade.",
        "Ce n'est pas naturel pour mon corps et mon esprit d'être équilibré par des médicaments.",
        "Mes idées sont plus claires avec les médicaments.",
        "En continuant à prendre les médicaments, je peux éviter de tomber à nouveau malade.",
        "Avec les médicaments, je me sens bizarre, comme un « zombie ».",
        "Les médicaments me rendent lourd(e) et fatigué(e)."
    ]
    
    def __init__(self):
        """Initialize the MARS questionnaire"""
        self._sections = self._build_sections()
        self._questions = self._build_questions()
    
    def _build_sections(self) -> List[Section]:
        """Build the sections structure"""
        return [
            Section(
                id="sec1",
                label="MARS – 10 items",
                description="Cochez une réponse par ligne (Semaine écoulée)",
                question_ids=[f"q{i}" for i in range(1, 11)]
            )
        ]
    
    def _build_questions(self) -> List[Question]:
        """Build all questions"""
        questions = []
        
        for i, text in enumerate(self.ITEMS, start=1):
            questions.append(Question(
                id=f"q{i}",
                section_id="sec1",
                text=f"{i}. {text}",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=1, label="OUI", score=None),
                    QuestionOption(code=0, label="NON", score=None)
                ],
                constraints={
                    "value_type": "integer",
                    "allowed_values": [0, 1]
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
            "description": "Échelle en 10 items (OUI/NON) évaluant l'adhérence médicamenteuse en psychiatrie. Score total 0–10, score élevé = meilleure adhérence.",
            "sources": [
                "MARS.pdf (version FR fournie)",
                "MARS_CotationScore.docx (règles de cotation)",
                "Thompson K, Kulkarni J, Sergejew AA. Schizophr Res. 2000;42(3):241–247."
            ],
            "total_questions": 10,
            "scoring_range": [0, 10],
            "scoring_notes": [
                "Items 1, 2, 3, 4, 5, 6, 9, 10: NON = 1, OUI = 0",
                "Items 7, 8: OUI = 1, NON = 0",
                "Distribution rapportée: médiane ≈6; IQR ≈4–8 (0–10)",
                "Interprétation: continuum (plus élevé = meilleure adhérence)"
            ]
        }
    
    def get_sections(self) -> List[Dict[str, Any]]:
        """Get all sections"""
        return [section.dict() for section in self._sections]
    
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
        return [q.dict() for q in questions]
    
    def get_question_by_id(self, question_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific question by ID"""
        for q in self._questions:
            if q.id == question_id:
                return q.dict()
        return None
    
    def validate_answers(self, answers: Dict[str, int]) -> ValidationResult:
        """
        Validate provided answers
        
        Args:
            answers: Dictionary of question_id -> answer mappings
            
        Returns:
            ValidationResult with validation status and messages
        """
        errors = []
        warnings = []
        
        # Check for missing required questions
        expected_keys = [f"q{i}" for i in range(1, 11)]
        missing = [k for k in expected_keys if k not in answers]
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Check value validity (must be 0 or 1)
        invalid = {k: v for k, v in answers.items() 
                  if k in expected_keys and (not isinstance(v, int) or v not in (0, 1))}
        if invalid:
            errors.append(f"Valeurs invalides (doivent être 0 (NON) ou 1 (OUI)): {invalid}")
        
        # Clinical warnings
        if not errors:
            # Calculate preliminary score to check for very low adherence
            recoded = self._recode_items(answers)
            total = sum(recoded.values())
            
            if total <= 3:
                warnings.append(
                    "Score très bas (≤3/10) suggérant une adhérence médicamenteuse très faible. "
                    "Intervention clinique recommandée."
                )
            elif total >= 9:
                warnings.append(
                    "Score très élevé (≥9/10) suggérant une excellente adhérence médicamenteuse."
                )
        
        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    def _recode_items(self, answers: Dict[str, int]) -> Dict[str, int]:
        """
        Recode items according to MARS scoring rules
        
        Args:
            answers: Raw answers (1=OUI, 0=NON)
            
        Returns:
            Recoded scores where higher values indicate better adherence
        """
        recoded = {}
        
        for i in range(1, 11):
            key = f"q{i}"
            raw = answers[key]
            
            if i in self.POSITIVE_ITEMS:
                # Items 7, 8: OUI (1) = 1 point, NON (0) = 0 points
                recoded[key] = 1 if raw == 1 else 0
            else:
                # Items 1, 2, 3, 4, 5, 6, 9, 10: NON (0) = 1 point, OUI (1) = 0 points
                recoded[key] = 1 if raw == 0 else 0
        
        return recoded
    
    def calculate_score(self, answers: Dict[str, int]) -> ScoreResult:
        """
        Calculate MARS total score
        
        Args:
            answers: Dictionary with keys 'q1' through 'q10', values 0 (NON) or 1 (OUI)
            
        Returns:
            ScoreResult with total score, recoded items, and interpretation
            
        Raises:
            MARSError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation.valid:
            raise MARSError("; ".join(validation.errors))
        
        # Recode items
        recoded = self._recode_items(answers)
        
        # Calculate total score (sum of recoded items)
        total = sum(recoded.values())
        
        # Safety check
        if total < 0 or total > 10:
            raise MARSError(f"Score hors bornes: {total}")
        
        # Build interpretation
        interpretation = self._build_interpretation(total, validation.warnings)
        
        return ScoreResult(
            total_score=total,
            recoded_scores=recoded,
            interpretation=interpretation
        )
    
    def _build_interpretation(self, total: int, warnings: List[str]) -> str:
        """Build clinical interpretation text"""
        interpretation = f"Score total MARS: {total}/10. "
        
        # Add severity context based on distribution (median ≈6, IQR ≈4–8)
        if total >= 8:
            interpretation += "Adhérence médicamenteuse excellente (au-dessus de l'IQR supérieur). "
        elif total >= 6:
            interpretation += "Adhérence médicamenteuse bonne (dans la plage médiane typique). "
        elif total >= 4:
            interpretation += "Adhérence médicamenteuse modérée (dans la plage IQR inférieure). "
        else:
            interpretation += "Adhérence médicamenteuse faible (en-dessous de l'IQR). "
        
        # Add interpretation guidance
        interpretation += (
            "Le score MARS est un continuum : plus le score est élevé, "
            "meilleure est l'adhérence médicamenteuse. "
        )
        
        # Add warnings
        if warnings:
            interpretation += " ".join(warnings) + " "
        
        # Clinical recommendation for low scores
        if total <= 5:
            interpretation += (
                "Une évaluation clinique des barrières à l'adhérence médicamenteuse est recommandée."
            )
        
        return interpretation.strip()
    
    def get_full_questionnaire(self) -> Dict[str, Any]:
        """Get complete questionnaire structure for frontend"""
        return {
            "metadata": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions()
        }

