"""
Pydantic models for FastAPI request/response validation
"""

from typing import Dict, List, Any, Optional, Union
from pydantic import BaseModel, Field, field_validator


class QuestionOption(BaseModel):
    """A single option for a question"""
    value: Union[int, str, float] = Field(..., description="Option value (numeric or string)")
    text: str = Field(..., description="Option text/label")


class Question(BaseModel):
    """A single question in a questionnaire"""
    id: str = Field(..., description="Question identifier (e.g., 'MADRS1')")
    number: int = Field(..., description="Question number")
    text: str = Field(..., description="Question text")
    type: str = Field(..., description="Input type (radio, select, textbox, etc.)")
    options: Dict[str, Any] = Field(..., description="Available options as dict mapping values to text")
    required: bool = Field(..., description="Whether this question is required")
    mutually_exclusive_with: Optional[str] = Field(None, description="ID of mutually exclusive question if any")
    subscale: Optional[str] = Field(None, description="Subscale this question belongs to")
    
    @field_validator('options', mode='before')
    @classmethod
    def convert_options_keys(cls, v):
        """Convert option keys to strings for JSON serialization"""
        if isinstance(v, dict):
            return {str(k): val for k, val in v.items()}
        return v


class QuestionnaireSummary(BaseModel):
    """Basic questionnaire information"""
    id: str = Field(..., description="Questionnaire identifier")
    name: str = Field(..., description="Questionnaire name")
    description: str = Field(..., description="Questionnaire description")
    num_items: int = Field(..., description="Number of questions")
    used_in_applications: List[str] = Field(default_factory=list, description="Applications using this questionnaire")


class QuestionnaireDetail(QuestionnaireSummary):
    """Complete questionnaire with all questions"""
    questions: List[Question] = Field(..., description="List of all questions")


class QuestionnaireResponse(BaseModel):
    """Response submission format - accepts both text and numeric values"""
    responses: Dict[str, Union[str, int, float]] = Field(
        ..., 
        description="Question ID mapped to response value (text or numeric)"
    )


class ScoreResult(BaseModel):
    """Standardized score calculation result"""
    score: Optional[Union[int, float]] = Field(None, description="Total score")
    valid: bool = Field(..., description="Whether calculation was successful")
    errors: List[str] = Field(default_factory=list, description="List of validation errors")
    interpretation: Optional[str] = Field(None, description="Score interpretation")
    subscales: Optional[Dict[str, Any]] = Field(None, description="Subscale scores if available")
    item_scores: Optional[Dict[str, Any]] = Field(None, description="Individual item scores if available")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional questionnaire-specific details")

