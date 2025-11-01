"""
CGI_I - CGI_I Questionnaire
===========================

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


@register_questionnaire("CGI_I")
@dataclass
class CgiI(BaseQuestionnaire):
    """CGI_I Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize CGI_I questionnaire with all 1 items."""
        
        questions_list = [
            Question(
                id='cgii1',
                text="Comparé à son état au début du traitement, de quelle façon le patient a-t-il changé ?",
                options=[
                    AnswerOption(value='a', label="Très fortement amélioré.", score=0),
                    AnswerOption(value='b', label="Fortement amélioré.", score=1),
                    AnswerOption(value='c', label="Légèrement amélioré.", score=2),
                    AnswerOption(value='d', label="Pas de changement.", score=3),
                    AnswerOption(value='e', label="Légèrement aggravé.", score=4),
                    AnswerOption(value='f', label="Fortement aggravé.", score=5),
                    AnswerOption(value='g', label="Très fortement aggravé.", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="CGI_I",
            name="CGI_I Questionnaire",
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
        """Compute CGI_I score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
