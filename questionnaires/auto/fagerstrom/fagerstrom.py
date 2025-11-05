# -*- coding: utf-8 -*-
"""
FTND (Fagerström Test for Nicotine Dependence)
French version - Tobacco dependence assessment scale

SCORING METHODOLOGY:
===================

The FTND is a 6-item questionnaire that assesses nicotine dependence.

CALCULATION:
-----------
Total Score = Q1 + Q2 + Q3 + Q4 + Q5 + Q6

Where:
- Q1 (Time to first cigarette): 0-3 points
  * 0 = After 60 minutes
  * 1 = 31-60 minutes
  * 2 = 6-30 minutes
  * 3 = Within 5 minutes
  
- Q2 (Difficult to refrain in forbidden places): 0-1 points
  * 0 = No
  * 1 = Yes
  
- Q3 (Which cigarette hardest to give up): 0-1 points
  * 0 = Any other
  * 1 = The first one
  
- Q4 (Cigarettes per day): 0-3 points
  * 0 = 10 or less
  * 1 = 11-20
  * 2 = 21-30
  * 3 = 31 or more
  
- Q5 (Smoke more in morning): 0-1 points
  * 0 = No
  * 1 = Yes
  
- Q6 (Smoke when ill): 0-1 points
  * 0 = No
  * 1 = Yes

SCORE RANGE: 0-10

INTERPRETATION:
--------------
- 0-2: No dependence or very weak dependence
- 3-4: Weak dependence
- 5: Medium dependence
- ≥6: Strong dependence

EXAMPLE:
--------
answers = {"q1": 2, "q2": 1, "q3": 1, "q4": 1, "q5": 0, "q6": 0}
Total = 2 + 1 + 1 + 1 + 0 + 0 = 5
Interpretation: "Dépendance moyenne" (Medium dependence)
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
from pydantic import BaseModel


class FagerstromError(ValueError):
    """Custom exception for Fagerström validation errors"""
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
    dependence_level: str
    interpretation: str
    item_scores: Dict[str, int]


class ValidationResult(BaseModel):
    """Model for validation results"""
    valid: bool
    errors: List[str] = []
    warnings: List[str] = []


class Fagerstrom:
    """
    Fagerström Test for Nicotine Dependence (FTND)
    
    A 6-item questionnaire assessing nicotine dependence.
    Provides methods to:
    - Retrieve instrument metadata
    - Get questions and sections
    - Validate answers
    - Calculate total score (0-10)
    - Determine dependence level
    """
    
    INSTRUMENT_ID = "Fagerstrom.fr"
    INSTRUMENT_NAME = "Échelle de dépendance tabagique de Fagerström (FTND) – Version française"
    ABBREVIATION = "FTND"
    LANGUAGE = "fr-FR"
    VERSION = "1.0"
    REFERENCE_PERIOD = "Habitudes actuelles de tabagisme"
    
    # Dependence level cutoffs
    CUTOFFS = [
        (0, 2, "Pas de dépendance ou dépendance très faible"),
        (3, 4, "Dépendance faible"),
        (5, 5, "Dépendance moyenne"),
        (6, 10, "Dépendance forte")
    ]
    
    def __init__(self):
        """Initialize the Fagerström questionnaire"""
        self._sections = self._build_sections()
        self._questions = self._build_questions()
    
    def _build_sections(self) -> List[Section]:
        """Build the sections structure"""
        return [
            Section(
                id="sec1",
                label="FTND – 6 items",
                description="Cochez une réponse par question",
                question_ids=[f"q{i}" for i in range(1, 7)]
            )
        ]
    
    def _build_questions(self) -> List[Question]:
        """Build all questions with their options and scoring"""
        questions = []
        
        # Q1: Time to first cigarette (0-3 points)
        questions.append(Question(
            id="q1",
            section_id="sec1",
            text="1. Combien de temps après votre réveil fumez-vous votre première cigarette ?",
            type="single_choice",
            required=True,
            options=[
                QuestionOption(code=3, label="Dans les 5 minutes", score=3),
                QuestionOption(code=2, label="De 6 à 30 minutes", score=2),
                QuestionOption(code=1, label="De 31 à 60 minutes", score=1),
                QuestionOption(code=0, label="Après 60 minutes", score=0)
            ],
            constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
        ))
        
        # Q2: Difficult to refrain (0-1 points)
        questions.append(Question(
            id="q2",
            section_id="sec1",
            text="2. Trouvez-vous difficile de vous abstenir de fumer dans les endroits où c'est interdit ?",
            type="single_choice",
            required=True,
            options=[
                QuestionOption(code=1, label="Oui", score=1),
                QuestionOption(code=0, label="Non", score=0)
            ],
            constraints={"value_type": "integer", "allowed_values": [0, 1]}
        ))
        
        # Q3: Which cigarette hardest to give up (0-1 points)
        questions.append(Question(
            id="q3",
            section_id="sec1",
            text="3. À quelle cigarette de la journée vous serait-il le plus difficile de renoncer ?",
            type="single_choice",
            required=True,
            options=[
                QuestionOption(code=1, label="La première", score=1),
                QuestionOption(code=0, label="N'importe quelle autre", score=0)
            ],
            constraints={"value_type": "integer", "allowed_values": [0, 1]}
        ))
        
        # Q4: Cigarettes per day (0-3 points)
        questions.append(Question(
            id="q4",
            section_id="sec1",
            text="4. Combien de cigarettes fumez-vous par jour ?",
            type="single_choice",
            required=True,
            options=[
                QuestionOption(code=0, label="10 ou moins", score=0),
                QuestionOption(code=1, label="11–20", score=1),
                QuestionOption(code=2, label="21–30", score=2),
                QuestionOption(code=3, label="31 ou plus", score=3)
            ],
            constraints={"value_type": "integer", "allowed_values": [0, 1, 2, 3]}
        ))
        
        # Q5: Smoke more in morning (0-1 points)
        questions.append(Question(
            id="q5",
            section_id="sec1",
            text="5. Fumez-vous à un rythme plus soutenu le matin que l'après-midi ?",
            type="single_choice",
            required=True,
            options=[
                QuestionOption(code=1, label="Oui", score=1),
                QuestionOption(code=0, label="Non", score=0)
            ],
            constraints={"value_type": "integer", "allowed_values": [0, 1]}
        ))
        
        # Q6: Smoke when ill (0-1 points)
        questions.append(Question(
            id="q6",
            section_id="sec1",
            text="6. Fumez-vous lorsque vous êtes si malade que vous devez rester au lit presque toute la journée ?",
            type="single_choice",
            required=True,
            options=[
                QuestionOption(code=1, label="Oui", score=1),
                QuestionOption(code=0, label="Non", score=0)
            ],
            constraints={"value_type": "integer", "allowed_values": [0, 1]}
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
            "description": "Questionnaire à 6 items évaluant la dépendance à la nicotine. Score total = 0–10.",
            "sources": [
                "FAGERSTROM.pdf (version FR du questionnaire)",
                "FAGERSTROM_CotationScore.docx (barème de cotation)",
                "Fagerström K.O. Br J Addict 1991: 543–547."
            ],
            "total_questions": 6,
            "score_range": [0, 10],
            "cutoffs": [
                {"range": "0-2", "label": "Pas de dépendance ou dépendance très faible"},
                {"range": "3-4", "label": "Dépendance faible"},
                {"range": "5", "label": "Dépendance moyenne"},
                {"range": "≥6", "label": "Dépendance forte"}
            ]
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
        expected_keys = [f"q{i}" for i in range(1, 7)]
        missing = [k for k in expected_keys if k not in answers]
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Validate Q1 and Q4 (0-3 range)
        for q_id in ["q1", "q4"]:
            if q_id in answers:
                if not isinstance(answers[q_id], int) or answers[q_id] not in [0, 1, 2, 3]:
                    errors.append(f"{q_id} doit être un entier 0, 1, 2 ou 3 (reçu: {answers[q_id]})")
        
        # Validate Q2, Q3, Q5, Q6 (0-1 range)
        for q_id in ["q2", "q3", "q5", "q6"]:
            if q_id in answers:
                if not isinstance(answers[q_id], int) or answers[q_id] not in [0, 1]:
                    errors.append(f"{q_id} doit être 0 ou 1 (reçu: {answers[q_id]})")
        
        # Clinical warnings
        if not errors:
            # High dependence warning
            total = sum(answers.get(f"q{i}", 0) for i in range(1, 7))
            if total >= 8:
                warnings.append(
                    "Score très élevé (≥8). Dépendance nicotinique forte. "
                    "Envisager un accompagnement au sevrage tabagique."
                )
            
            # Early morning smoking (Q1 = 3)
            if answers.get("q1") == 3:
                warnings.append(
                    "Cigarette dans les 5 minutes après réveil: indicateur fort de dépendance physique."
                )
            
            # High cigarette consumption (Q4 = 3)
            if answers.get("q4") == 3:
                warnings.append(
                    "Consommation ≥31 cigarettes/jour: risque sanitaire majeur."
                )
        
        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    def calculate_score(self, answers: Dict[str, int]) -> ScoreResult:
        """
        Calculate FTND total score and dependence level
        
        SCORING:
        -------
        1. Validate all answers (q1-q6)
        2. Sum all item responses: total = q1 + q2 + q3 + q4 + q5 + q6
        3. Determine dependence level based on total
        
        Args:
            answers: Dictionary with keys 'q1' through 'q6'
            
        Returns:
            ScoreResult with total score, dependence level, and interpretation
            
        Raises:
            FagerstromError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation.valid:
            raise FagerstromError("; ".join(validation.errors))
        
        # Calculate total score (sum of all 6 items)
        total_score = sum(answers[f"q{i}"] for i in range(1, 7))
        
        # Determine dependence level
        dependence_level = self._get_dependence_level(total_score)
        
        # Get individual item scores
        item_scores = {f"q{i}": answers[f"q{i}"] for i in range(1, 7)}
        
        # Build interpretation
        interpretation = self._build_interpretation(
            total_score, dependence_level, item_scores, validation.warnings
        )
        
        return ScoreResult(
            total_score=total_score,
            dependence_level=dependence_level,
            interpretation=interpretation,
            item_scores=item_scores
        )
    
    def _get_dependence_level(self, total_score: int) -> str:
        """Determine dependence level from total score"""
        for min_score, max_score, level in self.CUTOFFS:
            if min_score <= total_score <= max_score:
                return level
        return "Score invalide"
    
    def _build_interpretation(
        self,
        total_score: int,
        dependence_level: str,
        item_scores: Dict[str, int],
        warnings: List[str]
    ) -> str:
        """Build clinical interpretation text"""
        interpretation = f"Score FTND: {total_score}/10. "
        interpretation += f"Niveau de dépendance: {dependence_level}. "
        
        # Interpret specific items
        if item_scores.get("q1") >= 2:
            interpretation += "Cigarette matinale précoce (dépendance physique). "
        
        if item_scores.get("q4") >= 2:
            interpretation += f"Consommation importante (>20 cigarettes/jour). "
        
        if item_scores.get("q3") == 1:
            interpretation += "Première cigarette difficilement remplaçable. "
        
        # Recommendations based on level
        if total_score <= 2:
            interpretation += "Dépendance faible ou absente. Le sevrage peut être envisagé sans substitution nicotinique systématique."
        elif 3 <= total_score <= 4:
            interpretation += "Dépendance faible. Substitution nicotinique à faible dose peut faciliter le sevrage."
        elif total_score == 5:
            interpretation += "Dépendance moyenne. Substitution nicotinique recommandée pour le sevrage."
        else:
            interpretation += "Dépendance forte. Substitution nicotinique fortement recommandée, éventuellement associée à un accompagnement thérapeutique."
        
        # Add warnings
        if warnings:
            interpretation += " " + " ".join(warnings)
        
        return interpretation.strip()
    
    def get_full_questionnaire(self) -> Dict[str, Any]:
        """Get complete questionnaire structure for frontend"""
        return {
            "metadata": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions()
        }
