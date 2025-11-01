"""
ALS - ALS Questionnaire
=======================

1 item questionnaire

Source: Extracted from ebipolar application
Applications: ebipolar
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


@register_questionnaire("ALS")
@dataclass
class Als(BaseQuestionnaire):
    """ALS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize ALS questionnaire with all 1 items."""
        
        questions_list = [
            Question(
                id='radhtml_social_stprof_revenus',
                text="Source principale de revenus",
                options=[
                    AnswerOption(value='a', label="Salaire", score=0),
                    AnswerOption(value='b', label="RMI/RSA", score=1),
                    AnswerOption(value='c', label="AAH", score=2),
                    AnswerOption(value='d', label="Pension d''invalidité", score=3),
                    AnswerOption(value='e', label="Allocations de chômage", score=4),
                    AnswerOption(value='f', label="APL", score=5),
                    AnswerOption(value='g', label="Autres", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="ALS",
            name="ALS Questionnaire",
            description="1 item questionnaire",
            pathology_domain=PathologyDomain.BIPOLAR,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute ALS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
