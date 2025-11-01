"""
LB - LB Questionnaire
=====================

2 items questionnaire

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


@register_questionnaire("LB")
@dataclass
class Lb(BaseQuestionnaire):
    """LB Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize LB questionnaire with all 2 items."""
        
        questions_list = [
            Question(
                id='cmyn',
                text="Prise du traitement par le patient le matin du prélèvement",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psychotrop',
                text="Cocher le psychotrope utilisé et compléter le taux de psychotrope dosé",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6", score=5),
                    AnswerOption(value='g', label="7", score=6),
                    AnswerOption(value='h', label="8", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="LB",
            name="LB Questionnaire",
            description="2 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute LB score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
