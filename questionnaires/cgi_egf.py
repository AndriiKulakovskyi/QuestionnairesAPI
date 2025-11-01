"""
CGI_EGF - CGI_EGF Questionnaire
===============================

1 item questionnaire

Source: Extracted from ecedr application
Applications: ecedr
Author: Fondation FondaMental
Version: 2.0.0
"""

from dataclasses import dataclass
from ..core.models import (
    BaseQuestionnaire,
    Question,
    AnswerOption,
    QuestionType,
    PathologyDomain,
    RespondentType,
    QuestionnaireResponse,
    ScoreResult
)
from ..core.scoring import SimpleSumStrategy
from ..core.registry import register_questionnaire


@register_questionnaire("CGI_EGF")
@dataclass
class CgiEgf(BaseQuestionnaire):
    """CGI_EGF Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize CGI_EGF questionnaire with all 1 items."""
        
        questions_list = [
            Question(
                id='cgi1',
                text="1. Gravité de la maladie",
                options=[
                    AnswerOption(value='a', label="0. non évalué", score=0),
                    AnswerOption(value='b', label="1. normal, pas du tout malade", score=1),
                    AnswerOption(value='c', label="2. à la limite", score=2),
                    AnswerOption(value='d', label="3. légèrement malade", score=3),
                    AnswerOption(value='e', label="4. modérément malade", score=4),
                    AnswerOption(value='f', label="5. manifestement malade", score=5),
                    AnswerOption(value='g', label="6. gravement malade", score=6),
                    AnswerOption(value='h', label="7. parmi les patients les plus malades", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="CGI_EGF",
            name="CGI_EGF Questionnaire",
            description="1 item questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.CLINICIAN_RATED,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute CGI_EGF score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
