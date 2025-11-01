"""
QIAP - QIAP Questionnaire
=========================

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


@register_questionnaire("QIAP")
@dataclass
class Qiap(BaseQuestionnaire):
    """QIAP Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize QIAP questionnaire with all 1 items."""
        
        questions_list = [
            Question(
                id='qiap3c',
                text="3c. À quelle allure marchez-vous habituellement ?",
                options=[
                    AnswerOption(value='a', label="A vive allure, qui vous a fait respirer à un rythme plus élevé qu'en temps normal? ", score=0),
                    AnswerOption(value='b', label="A une allure modérée, qui vous a fait respirer à un rythme un peu plus élevé qu'en temps normal?", score=1),
                    AnswerOption(value='c', label="A une allure lente, qui n’a pas changé le rythme de votre respiration?", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="QIAP",
            name="QIAP Questionnaire",
            description="1 item questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute QIAP score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
