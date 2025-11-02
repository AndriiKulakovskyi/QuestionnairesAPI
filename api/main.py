"""
FastAPI application for Questionnaires API
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List, Dict, Any
import sys

from questionnaires import QUESTIONNAIRE_REGISTRY, get_questionnaire, list_available_questionnaires
from api.models import (
    QuestionnaireSummary,
    QuestionnaireDetail,
    QuestionnaireResponse,
    ScoreResult,
    Question
)
from api.utils import (
    normalize_responses,
    validate_response_format,
    check_mutually_exclusive_questions
)

app = FastAPI(
    title="Questionnaires API",
    description="API for accessing clinical questionnaires and computing scores",
    version="1.0.0"
)


@app.get("/")
async def root():
    """API information and version"""
    return {
        "name": "Questionnaires API",
        "version": "1.0.0",
        "description": "API for accessing clinical questionnaires and computing scores",
        "endpoints": {
            "list_questionnaires": "/questionnaires",
            "get_questionnaire": "/questionnaires/{questionnaire_id}",
            "calculate_score": "/questionnaires/{questionnaire_id}/score"
        }
    }


@app.get("/questionnaires", response_model=List[QuestionnaireSummary])
async def list_questionnaires():
    """List all available questionnaires"""
    summaries = []
    
    for q_id, q_class in QUESTIONNAIRE_REGISTRY.items():
        try:
            # Get the first alias for each questionnaire (the primary one)
            # Create instance to get metadata
            instance = q_class()
            
            summary = QuestionnaireSummary(
                id=q_id,
                name=getattr(instance, 'name', 'Unknown'),
                description=getattr(instance, 'description', ''),
                num_items=len(getattr(instance, 'questions', [])),
                used_in_applications=getattr(instance, 'used_in_applications', [])
            )
            summaries.append(summary)
        except Exception as e:
            # Skip questionnaires that fail to instantiate
            continue
    
    # Deduplicate by name (since multiple aliases exist)
    seen_names = set()
    unique_summaries = []
    for summary in summaries:
        if summary.name not in seen_names:
            seen_names.add(summary.name)
            unique_summaries.append(summary)
    
    return unique_summaries


@app.get("/questionnaires/{questionnaire_id}", response_model=QuestionnaireDetail)
async def get_questionnaire_details(questionnaire_id: str):
    """Get detailed information about a specific questionnaire including all questions"""
    try:
        q_class = get_questionnaire(questionnaire_id)
        instance = q_class()
        
        # Convert questions to Pydantic models
        questions = []
        for q in instance.questions:
            question = Question(
                id=q.get('id', ''),
                number=q.get('number', 0),
                text=q.get('text', ''),
                type=q.get('type', 'radio'),
                options=q.get('options', {}),
                required=q.get('required', True),
                mutually_exclusive_with=q.get('mutually_exclusive_with'),
                subscale=q.get('subscale')
            )
            questions.append(question)
        
        detail = QuestionnaireDetail(
            id=questionnaire_id,
            name=getattr(instance, 'name', 'Unknown'),
            description=getattr(instance, 'description', ''),
            num_items=len(questions),
            used_in_applications=getattr(instance, 'used_in_applications', []),
            questions=questions
        )
        
        return detail
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Questionnaire '{questionnaire_id}' not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error loading questionnaire: {str(e)}"
        )


@app.post("/questionnaires/{questionnaire_id}/score", response_model=ScoreResult)
async def calculate_score(questionnaire_id: str, response_data: QuestionnaireResponse):
    """Submit responses and calculate questionnaire score"""
    try:
        # Get questionnaire class and instance
        q_class = get_questionnaire(questionnaire_id)
        instance = q_class()
        
        questions = instance.questions
        
        # Validate response format
        format_errors = validate_response_format(response_data.responses, questions)
        
        # Check mutually exclusive questions
        mutual_excl_errors = check_mutually_exclusive_questions(response_data.responses, questions)
        
        # Combine all validation errors
        validation_errors = format_errors + mutual_excl_errors
        
        if validation_errors:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "errors": validation_errors,
                    "valid": False
                }
            )
        
        # Normalize responses to expected format
        normalized_responses = normalize_responses(
            response_data.responses,
            instance,
            questions
        )
        
        # Call calculate_score
        try:
            result = instance.calculate_score(normalized_responses)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "errors": [str(e)],
                    "valid": False
                }
            )
        
        # Standardize result format
        score_result = ScoreResult(
            score=result.get('score') or result.get('total_score'),
            valid=result.get('valid', True),
            errors=result.get('errors', []),
            interpretation=result.get('interpretation'),
            subscales=result.get('subscales') or result.get('subscale_scores'),
            item_scores=result.get('item_scores'),
            details={
                k: v for k, v in result.items()
                if k not in ['score', 'total_score', 'valid', 'errors', 'interpretation', 'subscales', 'subscale_scores', 'item_scores']
            }
        )
        
        # If there are errors in the result, return 400
        if score_result.errors:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "errors": score_result.errors,
                    "valid": False
                }
            )
        
        return score_result
        
    except HTTPException:
        raise
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Questionnaire '{questionnaire_id}' not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error calculating score: {str(e)}"
        )


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": f"Internal server error: {str(exc)}"}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

