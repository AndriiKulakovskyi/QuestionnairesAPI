"""
API routes for auto (self-report) questionnaires
"""

from typing import List, Optional
from fastapi import APIRouter, HTTPException, Depends, status
from ..dependencies import QuestionnaireRegistry, get_registry
from ..schemas import (
    QuestionnaireListItem,
    QuestionnaireMetadata,
    QuestionnaireDetail,
    AnswersRequest,
    ValidationResponse,
    ScoreResponse,
    ErrorResponse
)

router = APIRouter()


@router.get(
    "/questionnaires",
    response_model=List[QuestionnaireListItem],
    summary="List all auto questionnaires",
    description="Returns a list of all available self-report questionnaires with summary information."
)
def list_auto_questionnaires(
    registry: QuestionnaireRegistry = Depends(get_registry)
):
    """List all auto (self-report) questionnaires."""
    questionnaires = registry.list_questionnaires("auto")
    
    result = []
    for q_id, q_instance in questionnaires.items():
        metadata = q_instance.get_metadata()
        result.append(QuestionnaireListItem(
            id=q_id,
            name=metadata.get("name", ""),
            abbreviation=metadata.get("abbreviation", ""),
            language=metadata.get("language", ""),
            category="auto",
            description=metadata.get("description")
        ))
    
    return result


@router.get(
    "/questionnaires/{questionnaire_id}/metadata",
    response_model=QuestionnaireMetadata,
    responses={
        404: {"model": ErrorResponse, "description": "Questionnaire not found"}
    },
    summary="Get questionnaire metadata",
    description="Returns metadata for a specific questionnaire without including questions."
)
def get_auto_questionnaire_metadata(
    questionnaire_id: str,
    registry: QuestionnaireRegistry = Depends(get_registry)
):
    """Get metadata for a specific auto questionnaire."""
    questionnaire = registry.get_questionnaire("auto", questionnaire_id)
    
    if not questionnaire:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Questionnaire '{questionnaire_id}' not found in auto category"
        )
    
    metadata = questionnaire.get_metadata()
    return QuestionnaireMetadata(**metadata)


@router.get(
    "/questionnaires/{questionnaire_id}",
    response_model=QuestionnaireDetail,
    responses={
        404: {"model": ErrorResponse, "description": "Questionnaire not found"}
    },
    summary="Get complete questionnaire",
    description="Returns the complete questionnaire structure including metadata, sections, and all questions with options and constraints. For questionnaires with branching logic, optional gender parameter filters questions."
)
def get_auto_questionnaire(
    questionnaire_id: str,
    gender: Optional[str] = None,
    registry: QuestionnaireRegistry = Depends(get_registry)
):
    """Get complete questionnaire structure for a specific auto questionnaire."""
    questionnaire = registry.get_questionnaire("auto", questionnaire_id)
    
    if not questionnaire:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Questionnaire '{questionnaire_id}' not found in auto category"
        )
    
    # Get full questionnaire structure
    # For questionnaires with branching logic (like PRISE-M), pass gender parameter
    if hasattr(questionnaire, 'get_full_questionnaire'):
        # Try to pass gender parameter if the method accepts it
        import inspect
        sig = inspect.signature(questionnaire.get_full_questionnaire)
        if 'gender' in sig.parameters:
            full_structure = questionnaire.get_full_questionnaire(gender=gender)
        else:
            full_structure = questionnaire.get_full_questionnaire()
    else:
        # Fallback for questionnaires without this method
        full_structure = {
            "metadata": questionnaire.get_metadata(),
            "sections": questionnaire.get_sections(),
            "questions": questionnaire.get_questions()
        }
    
    return QuestionnaireDetail(**full_structure)


@router.post(
    "/questionnaires/{questionnaire_id}/validate",
    response_model=ValidationResponse,
    responses={
        404: {"model": ErrorResponse, "description": "Questionnaire not found"},
        400: {"model": ErrorResponse, "description": "Validation failed"}
    },
    summary="Validate answers",
    description="Validates submitted answers without calculating scores. Returns validation errors and warnings."
)
def validate_auto_questionnaire_answers(
    questionnaire_id: str,
    answers_request: AnswersRequest,
    registry: QuestionnaireRegistry = Depends(get_registry)
):
    """Validate answers for a specific auto questionnaire without calculating scores."""
    questionnaire = registry.get_questionnaire("auto", questionnaire_id)
    
    if not questionnaire:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Questionnaire '{questionnaire_id}' not found in auto category"
        )
    
    # Validate answers
    validation_result = questionnaire.validate_answers(answers_request.answers)
    
    return ValidationResponse(
        valid=validation_result.valid,
        errors=validation_result.errors,
        warnings=validation_result.warnings
    )


@router.post(
    "/questionnaires/{questionnaire_id}/submit",
    response_model=ScoreResponse,
    responses={
        404: {"model": ErrorResponse, "description": "Questionnaire not found"},
        400: {"model": ErrorResponse, "description": "Invalid answers"}
    },
    summary="Submit answers and calculate score",
    description="Validates and calculates scores/results for submitted answers. The structure of score_data varies by questionnaire type. For questionnaires with branching logic, demographics (e.g., gender) should be included."
)
def submit_auto_questionnaire_answers(
    questionnaire_id: str,
    answers_request: AnswersRequest,
    registry: QuestionnaireRegistry = Depends(get_registry)
):
    """Submit answers and calculate scores for a specific auto questionnaire."""
    questionnaire = registry.get_questionnaire("auto", questionnaire_id)
    
    if not questionnaire:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Questionnaire '{questionnaire_id}' not found in auto category"
        )
    
    try:
        # Extract demographics if provided
        demographics = answers_request.demographics or {}
        gender = demographics.get('gender')
        
        # Some questionnaires use calculate_score(), others use calculate_screening()
        if hasattr(questionnaire, 'calculate_score'):
            # Check if calculate_score accepts gender parameter (for branching logic)
            import inspect
            sig = inspect.signature(questionnaire.calculate_score)
            if 'gender' in sig.parameters and gender:
                result = questionnaire.calculate_score(answers_request.answers, gender=gender)
            else:
                result = questionnaire.calculate_score(answers_request.answers)
        elif hasattr(questionnaire, 'calculate_screening'):
            result = questionnaire.calculate_screening(answers_request.answers)
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Questionnaire '{questionnaire_id}' does not support scoring"
            )
        
        # Convert result to dict
        score_data = result.dict() if hasattr(result, 'dict') else result
        
        return ScoreResponse(
            questionnaire_id=questionnaire_id,
            score_data=score_data
        )
        
    except (ValueError, Exception) as e:
        # Handle validation errors and other exceptions
        error_message = str(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error_message
        )

