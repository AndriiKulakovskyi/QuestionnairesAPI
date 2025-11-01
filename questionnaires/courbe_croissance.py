"""
COURBE_CROISSANCE - COURBE_CROISSANCE Questionnaire
===================================================

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


@register_questionnaire("COURBE_CROISSANCE")
@dataclass
class CourbeCroissance(BaseQuestionnaire):
    """COURBE_CROISSANCE Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize COURBE_CROISSANCE questionnaire with all 1 items."""
        
        questions_list = [
            Question(
                id='croia1',
                text="Age",
                options=[
                    AnswerOption(value='0', label="1 mois", score=0),
                    AnswerOption(value='1', label="2 mois", score=1),
                    AnswerOption(value='2', label="3 mois", score=2),
                    AnswerOption(value='3', label="4 mois", score=3),
                    AnswerOption(value='4', label="5 mois", score=4),
                    AnswerOption(value='5', label="6 mois", score=5),
                    AnswerOption(value='6', label="7 mois", score=6),
                    AnswerOption(value='7', label="8 mois", score=7),
                    AnswerOption(value='8', label="9 mois", score=8),
                    AnswerOption(value='9', label="10 mois", score=9),
                    AnswerOption(value='10', label="11 mois", score=10)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="COURBE_CROISSANCE",
            name="COURBE_CROISSANCE Questionnaire",
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
        """Compute COURBE_CROISSANCE score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
