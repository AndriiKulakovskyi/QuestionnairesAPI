"""
INF_BILAN_BIOLOGIQUE - INF_BILAN_BIOLOGIQUE Questionnaire
=========================================================

1 item questionnaire

Source: Extracted from easperger application
Applications: easperger
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


@register_questionnaire("INF_BILAN_BIOLOGIQUE")
@dataclass
class InfBilanBiologique(BaseQuestionnaire):
    """INF_BILAN_BIOLOGIQUE Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize INF_BILAN_BIOLOGIQUE questionnaire with all 1 items."""
        
        questions_list = [
            Question(
                id='lateral',
                text="Latéralisation",
                options=[
                    AnswerOption(value='a', label="gaucher", score=0),
                    AnswerOption(value='b', label="droitier", score=1),
                    AnswerOption(value='c', label="ambidextre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="INF_BILAN_BIOLOGIQUE",
            name="INF_BILAN_BIOLOGIQUE Questionnaire",
            description="1 item questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute INF_BILAN_BIOLOGIQUE score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
