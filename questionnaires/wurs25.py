"""
WURS25 - WURS25 Questionnaire
=============================

1 item questionnaire

Source: Extracted from eschizo application
Applications: eschizo
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


@register_questionnaire("WURS25")
@dataclass
class Wurs25(BaseQuestionnaire):
    """WURS25 Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize WURS25 questionnaire with all 1 items."""
        
        questions_list = [
            Question(
                id='radhtml_wurs25',
                text="25. Tendance à être immature",
                options=[
                    AnswerOption(value='a', label="Pas du tout ou très légèrement", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Modérément", score=2),
                    AnswerOption(value='d', label="Assez", score=3),
                    AnswerOption(value='e', label="Beaucoup", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="WURS25",
            name="WURS25 Questionnaire",
            description="1 item questionnaire",
            pathology_domain=PathologyDomain.SCHIZOPHRENIA,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute WURS25 score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
