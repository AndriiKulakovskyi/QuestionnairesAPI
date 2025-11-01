"""
Questionnaire API Service Layer
================================

This module provides a service layer for questionnaire operations,
designed to be used by FastAPI, Flask, or other web frameworks.

The service layer handles:
- Questionnaire retrieval and listing
- Response validation
- Score computation
- Response storage (interface for database)
- Error handling and formatting

Author: Fondation FondaMental
Version: 2.0.0
"""

from typing import List, Dict, Any, Optional
from dataclasses import asdict
from datetime import datetime

from ..core.models import (
    PathologyDomain,
    QuestionnaireResponse,
    ScoreResult,
    BaseQuestionnaire
)
from ..core.registry import questionnaire_factory


class QuestionnaireService:
    """
    Service layer for questionnaire operations.
    
    This class provides high-level operations that can be exposed via API endpoints.
    """
    
    def __init__(self):
        """Initialize service with questionnaire factory."""
        self.factory = questionnaire_factory
    
    # ========================================================================
    # Questionnaire Discovery and Retrieval
    # ========================================================================
    
    def list_all_questionnaires(self) -> List[Dict[str, Any]]:
        """
        List all available questionnaires with basic metadata.
        
        Returns:
            List of questionnaire metadata dictionaries
        
        API Endpoint:
            GET /api/questionnaires
        """
        result = []
        
        for code in self.factory.get_all_codes():
            metadata = self.factory.registry.get_metadata(code)
            if metadata:
                result.append(metadata)
        
        return result
    
    def list_questionnaires_by_pathology(
        self,
        pathology: str
    ) -> List[Dict[str, Any]]:
        """
        List questionnaires for a specific pathology domain.
        
        Args:
            pathology: Pathology domain name (e.g., "bipolar", "schizophrenia")
        
        Returns:
            List of questionnaire metadata
        
        API Endpoint:
            GET /api/questionnaires?pathology={pathology}
        """
        try:
            pathology_enum = PathologyDomain[pathology.upper()]
        except KeyError:
            return []
        
        codes = self.factory.get_codes_by_pathology(pathology_enum)
        
        result = []
        for code in codes:
            metadata = self.factory.registry.get_metadata(code)
            if metadata:
                result.append(metadata)
        
        return result
    
    def get_questionnaire_details(self, code: str) -> Optional[Dict[str, Any]]:
        """
        Get full details of a questionnaire including all questions and options.
        
        Args:
            code: Questionnaire code
        
        Returns:
            Complete questionnaire schema or None if not found
        
        API Endpoint:
            GET /api/questionnaires/{code}
        """
        try:
            questionnaire = self.factory.create(code)
            return questionnaire.to_api_schema()
        except ValueError:
            return None
    
    def get_questionnaire_questions(self, code: str) -> Optional[List[Dict[str, Any]]]:
        """
        Get just the questions for a questionnaire (for rendering a form).
        
        Args:
            code: Questionnaire code
        
        Returns:
            List of questions or None if questionnaire not found
        
        API Endpoint:
            GET /api/questionnaires/{code}/questions
        """
        try:
            questionnaire = self.factory.create(code)
            schema = questionnaire.to_api_schema()
            return schema.get('questions', [])
        except ValueError:
            return None
    
    # ========================================================================
    # Response Validation
    # ========================================================================
    
    def validate_response(
        self,
        code: str,
        responses: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Validate a questionnaire response.
        
        Args:
            code: Questionnaire code
            responses: Dictionary of question_id -> answer mappings
        
        Returns:
            Dictionary with validation result:
            {
                'valid': bool,
                'errors': List[str],
                'missing_questions': List[str]
            }
        
        API Endpoint:
            POST /api/questionnaires/{code}/validate
        """
        try:
            questionnaire = self.factory.create(code)
        except ValueError:
            return {
                'valid': False,
                'errors': [f"Questionnaire '{code}' not found"],
                'missing_questions': []
            }
        
        # Create response object
        response_obj = QuestionnaireResponse(
            questionnaire_id=code,
            responses=responses
        )
        
        # Validate
        errors = questionnaire.validate_responses(response_obj)
        
        # Find missing required questions
        required_ids = {q.id for q in questionnaire.questions if q.required}
        answered_ids = set(responses.keys())
        missing = list(required_ids - answered_ids)
        
        return {
            'valid': len(errors) == 0,
            'errors': errors,
            'missing_questions': missing
        }
    
    # ========================================================================
    # Score Computation
    # ========================================================================
    
    def compute_scores(
        self,
        code: str,
        responses: Dict[str, Any],
        respondent_id: Optional[str] = None,
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Compute scores for a completed questionnaire.
        
        Args:
            code: Questionnaire code
            responses: Dictionary of question_id -> answer mappings
            respondent_id: Optional ID of the respondent
            session_id: Optional session/visit ID
        
        Returns:
            Dictionary with score results:
            {
                'success': bool,
                'questionnaire_code': str,
                'scores': ScoreResult as dict,
                'errors': List[str]
            }
        
        API Endpoint:
            POST /api/questionnaires/{code}/score
        """
        try:
            questionnaire = self.factory.create(code)
        except ValueError:
            return {
                'success': False,
                'questionnaire_code': code,
                'scores': None,
                'errors': [f"Questionnaire '{code}' not found"]
            }
        
        # Create response object
        response_obj = QuestionnaireResponse(
            questionnaire_id=code,
            responses=responses,
            respondent_id=respondent_id,
            session_id=session_id,
            is_complete=True
        )
        
        # Validate first
        validation_errors = questionnaire.validate_responses(response_obj)
        if validation_errors:
            return {
                'success': False,
                'questionnaire_code': code,
                'scores': None,
                'errors': validation_errors
            }
        
        # Compute scores
        try:
            score_result = questionnaire.compute_score(response_obj)
            
            return {
                'success': True,
                'questionnaire_code': code,
                'scores': score_result.to_dict(),
                'errors': []
            }
        
        except Exception as e:
            return {
                'success': False,
                'questionnaire_code': code,
                'scores': None,
                'errors': [f"Scoring error: {str(e)}"]
            }
    
    # ========================================================================
    # Batch Operations
    # ========================================================================
    
    def score_multiple_questionnaires(
        self,
        questionnaire_responses: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Score multiple questionnaires in one request.
        
        Args:
            questionnaire_responses: List of dicts with format:
                {
                    'code': str,
                    'responses': Dict[str, Any],
                    'respondent_id': Optional[str],
                    'session_id': Optional[str]
                }
        
        Returns:
            List of score results for each questionnaire
        
        API Endpoint:
            POST /api/questionnaires/batch-score
        """
        results = []
        
        for item in questionnaire_responses:
            code = item.get('code')
            responses = item.get('responses', {})
            respondent_id = item.get('respondent_id')
            session_id = item.get('session_id')
            
            result = self.compute_scores(
                code=code,
                responses=responses,
                respondent_id=respondent_id,
                session_id=session_id
            )
            
            results.append(result)
        
        return results
    
    def get_visit_questionnaires(
        self,
        visit_type: str,
        pathology: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get all questionnaires applicable for a specific visit type.
        
        Args:
            visit_type: Type of visit (e.g., "Initial", "Follow-up")
            pathology: Optional pathology filter
        
        Returns:
            List of questionnaire schemas for the visit
        
        API Endpoint:
            GET /api/visits/{visit_type}/questionnaires?pathology={pathology}
        """
        pathology_enum = None
        if pathology:
            try:
                pathology_enum = PathologyDomain[pathology.upper()]
            except KeyError:
                pass
        
        questionnaires = self.factory.create_for_visit(
            visit_type=visit_type,
            pathology=pathology_enum
        )
        
        return [q.to_api_schema() for q in questionnaires]


# ============================================================================
# Global Service Instance
# ============================================================================

# Singleton service instance
questionnaire_service = QuestionnaireService()
