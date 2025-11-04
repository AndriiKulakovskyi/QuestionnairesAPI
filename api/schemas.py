"""
Pydantic models for API request and response schemas
"""

from typing import Dict, List, Any, Optional, Union
from pydantic import BaseModel, Field


class QuestionnaireListItem(BaseModel):
    """Summary information for listing questionnaires."""
    id: str = Field(..., description="Unique questionnaire identifier")
    name: str = Field(..., description="Full name of the questionnaire")
    abbreviation: str = Field(..., description="Short abbreviation")
    language: str = Field(..., description="Language code (e.g., 'fr-FR')")
    category: str = Field(..., description="Category: 'auto' or 'hetero'")
    description: Optional[str] = Field(None, description="Brief description")


class QuestionnaireMetadata(BaseModel):
    """Metadata for a questionnaire without questions."""
    id: str
    name: str
    abbreviation: str
    language: str
    version: str
    reference_period: Optional[str] = None
    description: Optional[str] = None
    total_questions: Optional[int] = None
    scoring_range: Optional[List[int]] = None
    sources: Optional[List[str]] = None
    
    class Config:
        extra = "allow"  # Allow additional fields from different questionnaires


class QuestionOption(BaseModel):
    """A single option for a question."""
    code: Union[int, str]
    label: str
    score: Optional[Union[int, float]] = None
    
    class Config:
        extra = "allow"


class Question(BaseModel):
    """A single question in a questionnaire."""
    id: str
    section_id: Optional[str] = None
    text: str
    type: str
    required: bool
    options: List[QuestionOption]
    constraints: Dict[str, Any]
    help: Optional[str] = None
    
    class Config:
        extra = "allow"


class Section(BaseModel):
    """A section grouping questions."""
    id: str
    label: str
    description: str
    question_ids: List[str]
    
    class Config:
        extra = "allow"


class QuestionnaireDetail(BaseModel):
    """Complete questionnaire structure including all questions."""
    metadata: Dict[str, Any]
    sections: List[Dict[str, Any]]
    questions: List[Dict[str, Any]]
    respondent: Optional[Dict[str, Any]] = Field(
        None,
        description="Optional demographic requirements schema for branching logic questionnaires"
    )
    logic: Optional[Dict[str, Any]] = Field(
        None,
        description="Optional branching logic rules for conditional question display"
    )


class AnswersRequest(BaseModel):
    """Request body for submitting answers."""
    answers: Dict[str, Union[int, str, float]] = Field(
        ..., 
        description="Dictionary mapping question IDs to answer values"
    )
    demographics: Optional[Dict[str, str]] = Field(
        None,
        description="Optional demographic information (e.g., gender) for branching logic questionnaires"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "answers": {
                    "q1": 0,
                    "q2": 1,
                    "q3": 2
                },
                "demographics": {
                    "gender": "F"
                }
            }
        }


class ValidationResponse(BaseModel):
    """Response for answer validation."""
    valid: bool = Field(..., description="Whether the answers are valid")
    errors: List[str] = Field(default_factory=list, description="Validation error messages")
    warnings: List[str] = Field(default_factory=list, description="Validation warnings")


class ScoreResponse(BaseModel):
    """Generic response for score calculation."""
    questionnaire_id: str
    score_data: Dict[str, Any] = Field(
        ..., 
        description="Score data (structure varies by questionnaire type)"
    )
    validation: Optional[ValidationResponse] = Field(
        None, 
        description="Validation result if included"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "questionnaire_id": "QIDS-SR16.fr",
                "score_data": {
                    "total_score": 12,
                    "severity": "Dépression modérée",
                    "domain_scores": {
                        "sleep": 2,
                        "sadness": 2
                    },
                    "interpretation": "Score total: 12/27 - Dépression modérée."
                }
            }
        }


class ErrorResponse(BaseModel):
    """Standard error response."""
    detail: str = Field(..., description="Error message")
    questionnaire_id: Optional[str] = Field(None, description="Questionnaire ID if applicable")
    
    class Config:
        json_schema_extra = {
            "example": {
                "detail": "Questionnaire not found",
                "questionnaire_id": "INVALID-ID"
            }
        }


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    questionnaires: Dict[str, int] = Field(
        ..., 
        description="Count of questionnaires by category"
    )


class APIInfoResponse(BaseModel):
    """Root endpoint information."""
    title: str
    description: str
    version: str
    endpoints: Dict[str, str] = Field(
        ..., 
        description="Available endpoint groups"
    )

