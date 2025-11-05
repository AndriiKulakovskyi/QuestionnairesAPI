# -*- coding: utf-8 -*-
"""
ASRM (Altman Self-Rating Mania Scale)
French version - Self-assessment scale for manic/hypomanic symptoms
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
from pydantic import BaseModel


class ASRMError(ValueError):
    """Custom exception for ASRM validation errors"""
    pass


class QuestionOption(BaseModel):
    """Model for a question option"""
    code: int
    label: str
    score: int


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
    probability: str
    interpretation: str
    range: tuple = (0, 20)


class ValidationResult(BaseModel):
    """Model for validation results"""
    valid: bool
    errors: List[str] = []
    warnings: List[str] = []


class ASRM:
    """
    ASRM (Altman Self-Rating Mania Scale) Questionnaire Class
    
    Provides methods to:
    - Retrieve instrument metadata
    - Get questions and sections
    - Validate answers
    - Compute scores
    """
    
    INSTRUMENT_ID = "ASRM.fr"
    INSTRUMENT_NAME = "Auto-Questionnaire Altman – Échelle d'Auto-Évaluation de la Manie (ASRM)"
    ABBREVIATION = "ASRM"
    LANGUAGE = "fr-FR"
    VERSION = "1.0"
    REFERENCE_PERIOD = "7 derniers jours"
    
    # Cutoff for high probability
    CUTOFF_HIGH_PROBABILITY = 6
    
    # Item texts from French version
    ITEMS = [
        # Q1: Happiness/Cheerfulness
        (
            "Je ne me sens pas plus heureux(se) ou plus joyeux(se) que d'habitude.",
            "Je me sens parfois plus heureux(se) ou plus joyeux(se) que d'habitude.",
            "Je me sens souvent plus heureux(se) ou plus joyeux(se) que d'habitude.",
            "Je me sens plus heureux(se) ou plus joyeux(se) que d'habitude la plupart du temps.",
            "Je me sens plus heureux(se) ou plus joyeux(se) que d'habitude tout le temps."
        ),
        # Q2: Self-confidence
        (
            "Je ne me sens pas plus sûr(e) de moi que d'habitude.",
            "Je me sens parfois plus sûr(e) de moi que d'habitude.",
            "Je me sens souvent plus sûr(e) de moi que d'habitude.",
            "Je me sens plus sûr(e) de moi que d'habitude la plupart du temps.",
            "Je me sens extrêmement sûr(e) de moi tout le temps."
        ),
        # Q3: Sleep need
        (
            "Je n'ai pas besoin de moins de sommeil que d'habitude.",
            "J'ai parfois besoin de moins de sommeil que d'habitude.",
            "J'ai souvent besoin de moins de sommeil que d'habitude.",
            "J'ai fréquemment besoin de moins de sommeil que d'habitude.",
            "Je peux passer toute la journée et toute la nuit sans dormir et ne pas être fatigué(e)."
        ),
        # Q4: Talkativeness
        (
            "Je ne parle pas plus que d'habitude.",
            "Je parle parfois plus que d'habitude.",
            "Je parle souvent plus que d'habitude.",
            "Je parle fréquemment plus que d'habitude.",
            "Je parle sans arrêt et je ne peux être interrompu(e)."
        ),
        # Q5: Activity level
        (
            "Je n'ai pas été plus actif(ve) que d'habitude (socialement, sexuellement, au travail, à la maison ou à l'école).",
            "J'ai parfois été plus actif(ve) que d'habitude.",
            "J'ai souvent été plus actif(ve) que d'habitude.",
            "J'ai fréquemment été plus actif(ve) que d'habitude.",
            "Je suis constamment actif(ve), ou en mouvement tout le temps."
        )
    ]
    
    QUESTION_LABELS = [
        "Humeur (Bonheur/Joie)",
        "Confiance en soi",
        "Besoin de sommeil",
        "Discours (Loquacité)",
        "Niveau d'activité"
    ]
    
    def __init__(self):
        """Initialize the ASRM questionnaire"""
        self._sections = self._build_sections()
        self._questions = self._build_questions()
    
    def _build_sections(self) -> List[Section]:
        """Build the sections structure"""
        return [
            Section(
                id="sec1",
                label="ASRM – 5 items",
                description="Période de référence : la semaine dernière",
                question_ids=[f"q{i}" for i in range(1, 6)]
            )
        ]
    
    def _build_questions(self) -> List[Question]:
        """Build all questions"""
        questions = []
        
        for i, (options_tuple, label) in enumerate(zip(self.ITEMS, self.QUESTION_LABELS), start=1):
            questions.append(Question(
                id=f"q{i}",
                section_id="sec1",
                text=f"Question {i}: {label}",
                type="single_choice",
                required=True,
                options=[
                    QuestionOption(code=j, label=options_tuple[j], score=j)
                    for j in range(5)
                ],
                constraints={
                    "value_type": "integer",
                    "min_value": 0,
                    "max_value": 4,
                    "allowed_values": [0, 1, 2, 3, 4]
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
            "description": "Échelle auto-rapportée à 5 items, chacun coté de 0 à 4, évaluant la symptomatologie maniaque/hypomaniaque récente. Score total = somme des 5 items (0–20).",
            "sources": [
                "Altman EG, Hedeker D, Peterson JL, Davis JM. The Altman Self-Rating Mania Scale. Biol Psychiatry. 1997;42(10):948-55.",
                "altman.pdf (version FR fournie)",
                "Altman_CotationScore.docx (cotation/séquelles)"
            ],
            "total_questions": 5,
            "scoring_range": [0, 20],
            "cutoff": self.CUTOFF_HIGH_PROBABILITY
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
        
        # Check for missing required questions
        expected_keys = [f"q{i}" for i in range(1, 6)]
        missing = [k for k in expected_keys if k not in answers]
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Check value ranges
        invalid = {k: v for k, v in answers.items() 
                  if k in expected_keys and (not isinstance(v, int) or v < 0 or v > 4)}
        if invalid:
            errors.append(f"Valeurs invalides (doivent être des entiers 0–4): {invalid}")
        
        # Clinical warnings (if applicable)
        if not errors and len([k for k in expected_keys if answers.get(k, 0) == 4]) >= 3:
            warnings.append(
                "Trois items ou plus au maximum (score 4) - suggère des symptômes maniaques sévères. "
                "Évaluation clinique urgente recommandée."
            )
        
        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    def calculate_score(self, answers: Dict[str, int]) -> ScoreResult:
        """
        Calculate ASRM total score and probability
        
        Args:
            answers: Dictionary with keys 'q1' through 'q5', values 0-4
            
        Returns:
            ScoreResult with total score, probability, and interpretation
            
        Raises:
            ASRMError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation.valid:
            raise ASRMError("; ".join(validation.errors))
        
        # Calculate total score (simple sum)
        total = sum(answers[f"q{i}"] for i in range(1, 6))
        
        # Safety check
        if total < 0 or total > 20:
            raise ASRMError(f"Score hors bornes: {total}")
        
        # Determine probability
        if total >= self.CUTOFF_HIGH_PROBABILITY:
            probability = "Probabilité élevée d'épisode maniaque/hypomaniaque"
        else:
            probability = "Probabilité faible d'épisode maniaque/hypomaniaque"
        
        # Build interpretation
        interpretation = self._build_interpretation(total, probability, answers, validation.warnings)
        
        return ScoreResult(
            total_score=total,
            probability=probability,
            interpretation=interpretation
        )
    
    def _build_interpretation(
        self, 
        total: int, 
        probability: str,
        answers: Dict[str, int],
        warnings: List[str]
    ) -> str:
        """Build clinical interpretation text"""
        interpretation = f"Score total: {total}/20. {probability}. "
        
        # Add severity context
        if total >= 12:
            interpretation += "Score très élevé suggérant des symptômes maniaques marqués. "
        elif total >= 6:
            interpretation += "Score élevé suggérant des symptômes maniaques/hypomaniaques. "
        else:
            interpretation += "Score sous le seuil, pas d'indication actuelle de manie/hypomanie. "
        
        # Add warnings
        if warnings:
            interpretation += " ".join(warnings) + " "
        
        # Clinical recommendation
        if total >= self.CUTOFF_HIGH_PROBABILITY:
            interpretation += "Une évaluation clinique approfondie est recommandée."
        
        return interpretation.strip()
    
    def get_full_questionnaire(self) -> Dict[str, Any]:
        """Get complete questionnaire structure for frontend"""
        return {
            "metadata": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions()
        }

