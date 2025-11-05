# -*- coding: utf-8 -*-
"""
ESS (Epworth Sleepiness Scale)
French version - Self-assessment scale for daytime sleepiness
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
from pydantic import BaseModel


class EpworthError(ValueError):
    """Custom exception for Epworth validation errors"""
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
    severity: str
    interpretation: str
    clinical_context: Optional[str] = None
    range: tuple = (0, 24)


class ValidationResult(BaseModel):
    """Model for validation results"""
    valid: bool
    errors: List[str] = []
    warnings: List[str] = []


class Epworth:
    """
    Epworth Sleepiness Scale (ESS) Questionnaire Class
    
    Provides methods to:
    - Retrieve instrument metadata
    - Get questions and sections
    - Validate answers
    - Compute scores
    """
    
    INSTRUMENT_ID = "Epworth.fr"
    INSTRUMENT_NAME = "Échelle de Somnolence d'Epworth (ESS) – Version française"
    ABBREVIATION = "ESS"
    LANGUAGE = "fr-FR"
    VERSION = "1.0"
    REFERENCE_PERIOD = "Mois récents"
    
    # Cutoff for excessive daytime sleepiness
    CUTOFF_EXCESSIVE_SLEEPINESS = 11
    
    # 8 situation items for scoring
    SITUATION_ITEMS = [
        "Assis en train de lire",
        "En train de regarder la télévision",
        "Assis, inactif, dans un endroit public (au théâtre, en réunion)",
        "Comme passager dans une voiture roulant sans arrêt pendant une heure",
        "Allongé l'après-midi pour se reposer quand les circonstances le permettent",
        "Assis en train de parler à quelqu'un",
        "Assis calmement après un repas sans alcool",
        "Dans une auto immobilisée quelques minutes dans un encombrement"
    ]
    
    # Response options (0-3 scale)
    RESPONSE_OPTIONS = [
        {"code": 0, "label": "0 – ne somnolerait jamais", "score": 0},
        {"code": 1, "label": "1 – faible chance de s'endormir", "score": 1},
        {"code": 2, "label": "2 – chance moyenne de s'endormir", "score": 2},
        {"code": 3, "label": "3 – forte chance de s'endormir", "score": 3}
    ]
    
    # Q9 options (timing of sleepiness - not scored)
    TIMING_OPTIONS = [
        {"code": 0, "label": "seulement après les repas"},
        {"code": 1, "label": "à certaines heures du jour, toujours les mêmes"},
        {"code": 2, "label": "la nuit"},
        {"code": 3, "label": "à n'importe quelle heure du jour"}
    ]
    
    def __init__(self):
        """Initialize the Epworth questionnaire"""
        self._sections = self._build_sections()
        self._questions = self._build_questions()
    
    def _build_sections(self) -> List[Section]:
        """Build the sections structure"""
        return [
            Section(
                id="sec_items",
                label="Situations",
                description="8 situations – coter la probabilité de somnoler/s'endormir",
                question_ids=[f"q{i}" for i in range(1, 9)]
            ),
            Section(
                id="sec_extra",
                label="Complément clinique",
                description="Moment d'apparition des envies de dormir (hors score)",
                question_ids=["q9"]
            )
        ]
    
    def _build_questions(self) -> List[Question]:
        """Build all questions"""
        questions = []
        
        # Q1-Q8: Situation items (scored)
        for i, situation in enumerate(self.SITUATION_ITEMS, start=1):
            questions.append(Question(
                id=f"q{i}",
                section_id="sec_items",
                text=f"{i}/ {situation}",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(**opt) for opt in self.RESPONSE_OPTIONS
                ],
                constraints={
                    "value_type": "integer",
                    "allowed_values": [0, 1, 2, 3]
                }
            ))
        
        # Q9: Timing question (not scored)
        questions.append(Question(
            id="q9",
            section_id="sec_extra",
            text="Ces envies de dormir surviennent-elles ? (cocher une seule réponse)",
            type="single_choice",
            required=False,
            options=[
                QuestionOption(**opt, score=None) for opt in self.TIMING_OPTIONS
            ],
            constraints={
                "value_type": "integer",
                "allowed_values": [0, 1, 2, 3]
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
            "description": "Auto-questionnaire de somnolence diurne en 8 items (0–3 chacun). Score total 0–24.",
            "sources": [
                "Epworth.pdf (version FR fournie)",
                "Epworth_CotationScore.docx (règles de cotation)",
                "Johns MW. Sleep 1991;14:540–545."
            ],
            "total_questions": 9,
            "scored_questions": 8,
            "scoring_range": [0, 24],
            "cutoff": self.CUTOFF_EXCESSIVE_SLEEPINESS
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
        
        # Check for missing required questions (Q1-Q8)
        expected_keys = [f"q{i}" for i in range(1, 9)]
        missing = [k for k in expected_keys if k not in answers]
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Check value ranges for Q1-Q8
        invalid = {k: v for k, v in answers.items() 
                  if k in expected_keys and (not isinstance(v, int) or v < 0 or v > 3)}
        if invalid:
            errors.append(f"Valeurs invalides (doivent être des entiers 0–3): {invalid}")
        
        # Q9 is optional, but validate if present
        if "q9" in answers:
            if not isinstance(answers["q9"], int) or answers["q9"] < 0 or answers["q9"] > 3:
                errors.append("Q9 doit être un entier 0–3 si fourni.")
        
        # Clinical warnings
        if not errors:
            # Check if all situations have high probability (score 3)
            high_scores = [k for k in expected_keys if answers.get(k, 0) == 3]
            if len(high_scores) >= 6:
                warnings.append(
                    "Six situations ou plus avec forte chance de s'endormir - "
                    "suggère une somnolence diurne très sévère. Évaluation urgente recommandée."
                )
            
            # Check for dangerous situations with high sleepiness
            dangerous_situations = ["q4", "q8"]  # Car passenger, car in traffic
            dangerous_high = [k for k in dangerous_situations if answers.get(k, 0) >= 2]
            if dangerous_high:
                warnings.append(
                    "Probabilité moyenne ou forte de s'endormir dans des situations de conduite - "
                    "risque de sécurité routière. Conseil d'éviter la conduite recommandé."
                )
        
        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    def calculate_score(self, answers: Dict[str, int]) -> ScoreResult:
        """
        Calculate Epworth total score and severity
        
        Args:
            answers: Dictionary with keys 'q1' through 'q8' (required), 'q9' (optional)
            
        Returns:
            ScoreResult with total score, severity, and interpretation
            
        Raises:
            EpworthError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation.valid:
            raise EpworthError("; ".join(validation.errors))
        
        # Calculate total score (sum of Q1-Q8 only, Q9 not included)
        total = sum(answers[f"q{i}"] for i in range(1, 9))
        
        # Safety check
        if total < 0 or total > 24:
            raise EpworthError(f"Score hors bornes: {total}")
        
        # Determine severity
        if total >= self.CUTOFF_EXCESSIVE_SLEEPINESS:
            severity = "Somnolence diurne excessive (SDE) probable"
        else:
            severity = "Somnolence dans les limites normales"
        
        # Get clinical context from Q9 if available
        clinical_context = None
        if "q9" in answers:
            timing_labels = {
                0: "seulement après les repas",
                1: "à certaines heures du jour, toujours les mêmes",
                2: "la nuit",
                3: "à n'importe quelle heure du jour"
            }
            clinical_context = f"Timing: {timing_labels.get(answers['q9'], 'non spécifié')}"
        
        # Build interpretation
        interpretation = self._build_interpretation(
            total, severity, answers, validation.warnings, clinical_context
        )
        
        return ScoreResult(
            total_score=total,
            severity=severity,
            interpretation=interpretation,
            clinical_context=clinical_context
        )
    
    def _build_interpretation(
        self,
        total: int,
        severity: str,
        answers: Dict[str, int],
        warnings: List[str],
        clinical_context: Optional[str]
    ) -> str:
        """Build clinical interpretation text"""
        interpretation = f"Score total: {total}/24. {severity}. "
        
        # Add severity context
        if total >= 16:
            interpretation += "Score très élevé - somnolence diurne sévère nécessitant une évaluation médicale urgente. "
        elif total >= self.CUTOFF_EXCESSIVE_SLEEPINESS:
            interpretation += "Score élevé indiquant une somnolence diurne excessive. Consultation médicale recommandée. "
        else:
            interpretation += "Score dans les limites normales. "
        
        # Add clinical context
        if clinical_context:
            interpretation += clinical_context + ". "
        
        # Add warnings
        if warnings:
            interpretation += " ".join(warnings) + " "
        
        # Clinical recommendations
        if total >= self.CUTOFF_EXCESSIVE_SLEEPINESS:
            interpretation += (
                "Une évaluation médicale est recommandée pour rechercher d'éventuels troubles du sommeil "
                "(apnée du sommeil, narcolepsie, etc.)."
            )
        
        return interpretation.strip()
    
    def get_full_questionnaire(self) -> Dict[str, Any]:
        """Get complete questionnaire structure for frontend"""
        return {
            "metadata": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions()
        }

