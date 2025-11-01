"""
Core Domain Models for Questionnaire System
============================================

This module defines the fundamental domain models for the psychiatric questionnaire system.
These models are designed to be:
- Immutable where appropriate (using frozen dataclasses)
- Type-safe with comprehensive type hints
- Validated at construction time
- Serializable for API responses

Author: Fondation FondaMental
Version: 2.0.0 (Refactored)
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union, Literal
from enum import Enum
from abc import ABC, abstractmethod
import json


# ============================================================================
# Enums and Type Definitions
# ============================================================================

class QuestionType(Enum):
    """Type of question determining how it should be presented and scored."""
    SINGLE_CHOICE = "single_choice"      # Radio buttons - one answer
    MULTIPLE_CHOICE = "multiple_choice"  # Checkboxes - multiple answers
    LIKERT_SCALE = "likert_scale"        # Ordered scale (e.g., 1-5)
    TEXT_INPUT = "text_input"            # Free text
    NUMERIC_INPUT = "numeric_input"      # Numeric value
    DATE_INPUT = "date_input"            # Date picker


class PathologyDomain(Enum):
    """Clinical pathology domain for organizing questionnaires."""
    BIPOLAR = "bipolar"
    SCHIZOPHRENIA = "schizophrenia"
    DEPRESSION = "depression"
    AUTISM_SPECTRUM = "autism_spectrum"
    ANXIETY = "anxiety"
    ADHD = "adhd"
    GENERAL = "general"


class RespondentType(Enum):
    """Who completes the questionnaire."""
    SELF_REPORT = "self_report"          # Patient fills out
    CLINICIAN_RATED = "clinician_rated"  # Clinician completes based on assessment
    CAREGIVER = "caregiver"              # Family member or caregiver
    MIXED = "mixed"                      # Combination


# ============================================================================
# Answer and Question Models
# ============================================================================

@dataclass(frozen=True)
class AnswerOption:
    """
    Represents a single answer option for a question.
    
    Attributes:
        value: The value stored in the database (e.g., 'a', '0', '1')
        label: The text displayed to the user (French)
        score: Numeric score assigned to this option (for scoring)
        conditional_trigger: If set, selecting this option triggers conditional logic
    
    Examples:
        >>> option = AnswerOption(value='a', label="Jamais", score=0)
        >>> option = AnswerOption(value='1', label="Oui", score=1, conditional_trigger="show_q10")
    """
    value: Union[str, int]
    label: str
    score: Optional[Union[int, float]] = None
    conditional_trigger: Optional[str] = None
    
    def __post_init__(self):
        """Validate the answer option."""
        if not self.label or not str(self.label).strip():
            raise ValueError("Answer option label cannot be empty")


@dataclass(frozen=True)
class Question:
    """
    Represents a single question in a questionnaire.
    
    Attributes:
        id: Unique identifier (matches database field name)
        text: Question text in French
        options: List of possible answer options
        question_type: Type of question (determines presentation)
        required: Whether an answer is mandatory
        reverse_scored: If True, scoring is reversed (max becomes min)
        conditional_on: Question ID that must be answered for this to appear
        conditional_value: Required value of conditional question
        group: Logical grouping of questions (for subscales)
    
    Examples:
        >>> q = Question(
        ...     id="ymrs1",
        ...     text="1. Elevation de l'humeur",
        ...     options=[AnswerOption('a', "Absente", 0), ...],
        ...     question_type=QuestionType.SINGLE_CHOICE
        ... )
    """
    id: str
    text: str
    options: List[AnswerOption]
    question_type: QuestionType = QuestionType.SINGLE_CHOICE
    required: bool = True
    reverse_scored: bool = False
    conditional_on: Optional[str] = None
    conditional_value: Optional[Union[str, int]] = None
    group: Optional[str] = None
    help_text: Optional[str] = None
    
    def __post_init__(self):
        """Validate the question."""
        if not self.id or not str(self.id).strip():
            raise ValueError("Question ID cannot be empty")
        if not self.text or not str(self.text).strip():
            raise ValueError("Question text cannot be empty")
        if not self.options:
            raise ValueError(f"Question {self.id} must have at least one answer option")
    
    def get_option_by_value(self, value: Union[str, int]) -> Optional[AnswerOption]:
        """Retrieve an answer option by its value."""
        for option in self.options:
            if option.value == value:
                return option
        return None
    
    def is_valid_response(self, response: Union[str, int, List]) -> bool:
        """Check if a response is valid for this question."""
        if self.question_type == QuestionType.MULTIPLE_CHOICE:
            if not isinstance(response, list):
                return False
            return all(self.get_option_by_value(v) is not None for v in response)
        else:
            return self.get_option_by_value(response) is not None


# ============================================================================
# Response Models
# ============================================================================

@dataclass
class QuestionnaireResponse:
    """
    Represents a complete response to a questionnaire.
    
    Attributes:
        questionnaire_id: ID of the questionnaire being answered
        responses: Mapping of question IDs to answers
        respondent_id: ID of the person responding (for tracking)
        session_id: Session or visit ID
        completion_time_seconds: How long it took to complete
        is_complete: Whether all required questions were answered
    """
    questionnaire_id: str
    responses: Dict[str, Union[str, int, List]]
    respondent_id: Optional[str] = None
    session_id: Optional[str] = None
    completion_time_seconds: Optional[int] = None
    is_complete: bool = False
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def get_response(self, question_id: str, default: Any = None) -> Any:
        """Get response for a specific question."""
        return self.responses.get(question_id, default)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            'questionnaire_id': self.questionnaire_id,
            'responses': self.responses,
            'respondent_id': self.respondent_id,
            'session_id': self.session_id,
            'completion_time_seconds': self.completion_time_seconds,
            'is_complete': self.is_complete,
            'metadata': self.metadata
        }


@dataclass
class ScoreResult:
    """
    Represents the computed scores from a questionnaire.
    
    Attributes:
        total_score: Overall total score
        subscale_scores: Scores for individual subscales/domains
        interpretation: Clinical interpretation (e.g., "Mild depression")
        severity_level: Standardized severity (normal, mild, moderate, severe)
        percentile: Percentile rank if normative data available
        raw_values: Raw computed values before interpretation
        warnings: Any warnings about scoring (e.g., missing data)
    """
    total_score: Union[int, float]
    subscale_scores: Dict[str, Union[int, float]] = field(default_factory=dict)
    interpretation: Optional[str] = None
    severity_level: Optional[Literal["normal", "mild", "moderate", "severe", "very_severe"]] = None
    percentile: Optional[float] = None
    raw_values: Dict[str, Any] = field(default_factory=dict)
    warnings: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API responses."""
        return {
            'total_score': self.total_score,
            'subscale_scores': self.subscale_scores,
            'interpretation': self.interpretation,
            'severity_level': self.severity_level,
            'percentile': self.percentile,
            'raw_values': self.raw_values,
            'warnings': self.warnings
        }


# ============================================================================
# Base Questionnaire (Abstract)
# ============================================================================

@dataclass
class BaseQuestionnaire(ABC):
    """
    Abstract base class for all questionnaires.
    
    This class defines the interface that all concrete questionnaires must implement.
    It provides common functionality for validation, scoring, and serialization.
    
    Attributes:
        code: Short code identifier (e.g., "YMRS", "MADRS")
        name: Full name in French
        description: Brief description of what the questionnaire measures
        pathology_domain: Clinical domain this questionnaire belongs to
        respondent_type: Who completes this questionnaire
        questions: List of all questions in order
        visit_types: When this questionnaire is administered
        estimated_duration_minutes: Estimated time to complete
        version: Version of the questionnaire
    """
    code: str
    name: str
    description: str
    pathology_domain: PathologyDomain
    respondent_type: RespondentType
    questions: List[Question]
    visit_types: List[str] = field(default_factory=list)
    estimated_duration_minutes: Optional[int] = None
    version: str = "1.0"
    
    def __post_init__(self):
        """Validate questionnaire configuration."""
        if not self.code or not self.code.strip():
            raise ValueError("Questionnaire code cannot be empty")
        if not self.questions:
            raise ValueError(f"Questionnaire {self.code} must have at least one question")
    
    def validate_responses(self, responses: QuestionnaireResponse) -> List[str]:
        """
        Validate that responses are complete and valid.
        
        Args:
            responses: The questionnaire response to validate
        
        Returns:
            List of validation error messages (empty if valid)
        """
        errors = []
        
        # Check questionnaire ID matches
        if responses.questionnaire_id != self.code:
            errors.append(
                f"Response is for questionnaire '{responses.questionnaire_id}' "
                f"but validating against '{self.code}'"
            )
        
        # Check all required questions are answered
        for question in self.questions:
            if question.required and question.id not in responses.responses:
                # Check if conditional - may not be required
                if question.conditional_on:
                    conditional_answer = responses.get_response(question.conditional_on)
                    if conditional_answer != question.conditional_value:
                        continue  # Not required due to conditional logic
                
                errors.append(f"Missing response for required question: {question.id}")
                continue
            
            # Validate response value
            if question.id in responses.responses:
                response_value = responses.get_response(question.id)
                if not question.is_valid_response(response_value):
                    errors.append(
                        f"Invalid response '{response_value}' for question {question.id}"
                    )
        
        return errors
    
    @abstractmethod
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """
        Compute scores from responses.
        
        This method must be implemented by each concrete questionnaire class
        with the specific scoring logic for that instrument.
        
        Args:
            responses: Complete questionnaire responses
        
        Returns:
            ScoreResult object containing computed scores and interpretation
        
        Raises:
            ValueError: If responses are invalid or incomplete
        """
        pass
    
    def get_question_by_id(self, question_id: str) -> Optional[Question]:
        """Retrieve a question by its ID."""
        for question in self.questions:
            if question.id == question_id:
                return question
        return None
    
    def get_questions_by_group(self, group: str) -> List[Question]:
        """Get all questions in a specific group/subscale."""
        return [q for q in self.questions if q.group == group]
    
    def to_api_schema(self) -> Dict[str, Any]:
        """
        Convert questionnaire to API schema format.
        
        Returns a JSON-serializable dictionary suitable for API responses.
        """
        return {
            'code': self.code,
            'name': self.name,
            'description': self.description,
            'pathology_domain': self.pathology_domain.value,
            'respondent_type': self.respondent_type.value,
            'estimated_duration_minutes': self.estimated_duration_minutes,
            'version': self.version,
            'total_questions': len(self.questions),
            'questions': [
                {
                    'id': q.id,
                    'text': q.text,
                    'type': q.question_type.value,
                    'required': q.required,
                    'options': [
                        {
                            'value': opt.value,
                            'label': opt.label,
                            'score': opt.score
                        }
                        for opt in q.options
                    ],
                    'group': q.group,
                    'help_text': q.help_text
                }
                for q in self.questions
            ]
        }
