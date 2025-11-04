"""
API routes for hetero (clinician-rated) questionnaires
Currently placeholder - to be implemented in the future
"""

from typing import List
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
    summary="List all hetero questionnaires",
    description="Returns a list of all available clinician-rated questionnaires. Currently empty - to be implemented."
)
def list_hetero_questionnaires(
    registry: QuestionnaireRegistry = Depends(get_registry)
):
    """List all hetero (clinician-rated) questionnaires."""
    # Return empty list for now - hetero questionnaires not yet implemented
    return []


@router.get(
    "/questionnaires/{questionnaire_id}/metadata",
    response_model=QuestionnaireMetadata,
    responses={
        501: {"model": ErrorResponse, "description": "Not implemented"}
    },
    summary="Get questionnaire metadata",
    description="Returns metadata for a specific hetero questionnaire. Not yet implemented."
)
def get_hetero_questionnaire_metadata(
    questionnaire_id: str,
    registry: QuestionnaireRegistry = Depends(get_registry)
):
    """Get metadata for a specific hetero questionnaire."""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Hetero questionnaires are not yet implemented. Check back in future releases."
    )


@router.get(
    "/questionnaires/{questionnaire_id}",
    response_model=QuestionnaireDetail,
    responses={
        501: {"model": ErrorResponse, "description": "Not implemented"}
    },
    summary="Get complete questionnaire",
    description="Returns the complete questionnaire structure. Not yet implemented."
)
def get_hetero_questionnaire(
    questionnaire_id: str,
    registry: QuestionnaireRegistry = Depends(get_registry)
):
    """Get complete questionnaire structure for a specific hetero questionnaire."""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Hetero questionnaires are not yet implemented. Check back in future releases."
    )


@router.post(
    "/questionnaires/{questionnaire_id}/validate",
    response_model=ValidationResponse,
    responses={
        501: {"model": ErrorResponse, "description": "Not implemented"}
    },
    summary="Validate answers",
    description="Validates submitted answers. Not yet implemented."
)
def validate_hetero_questionnaire_answers(
    questionnaire_id: str,
    answers_request: AnswersRequest,
    registry: QuestionnaireRegistry = Depends(get_registry)
):
    """Validate answers for a specific hetero questionnaire."""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Hetero questionnaires are not yet implemented. Check back in future releases."
    )


@router.post(
    "/questionnaires/{questionnaire_id}/submit",
    response_model=ScoreResponse,
    responses={
        501: {"model": ErrorResponse, "description": "Not implemented"}
    },
    summary="Submit answers and calculate score",
    description="Validates and calculates scores for submitted answers. Not yet implemented."
)
def submit_hetero_questionnaire_answers(
    questionnaire_id: str,
    answers_request: AnswersRequest,
    registry: QuestionnaireRegistry = Depends(get_registry)
):
    """Submit answers and calculate scores for a specific hetero questionnaire."""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Hetero questionnaires are not yet implemented. Check back in future releases."
    )

