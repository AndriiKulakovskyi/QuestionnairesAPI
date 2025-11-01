"""
ALTMAN - ALTMAN Questionnaire
=============================

2 items questionnaire

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


@register_questionnaire("ALTMAN")
@dataclass
class Altman(BaseQuestionnaire):
    """ALTMAN Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize ALTMAN questionnaire with all 2 items."""
        
        questions_list = [
            Question(
                id='altman3',
                text="QUESTION 3 :",
                options=[
                    AnswerOption(value='a', label="0. Je n’ai pas besoin de moins de sommeil que d’habitude.", score=0),
                    AnswerOption(value='b', label="1. J’ai parfois besoin de moins de sommeil que d’habitude.", score=1),
                    AnswerOption(value='c', label="2. J’ai souvent besoin de moins de sommeil que d’habitude.", score=2),
                    AnswerOption(value='d', label="3. J’ai fréquemment besoin de moins de sommeil que d’habitude.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='altman4',
                text="QUESTION 4 :",
                options=[
                    AnswerOption(value='a', label="0. Je ne parle pas plus que d’habitude.", score=0),
                    AnswerOption(value='b', label="1. Je parle parfois plus que d’habitude.", score=1),
                    AnswerOption(value='c', label="2. Je parle souvent plus que d’habitude.", score=2),
                    AnswerOption(value='d', label="3. Je parle fréquemment plus que d’habitude.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="ALTMAN",
            name="ALTMAN Questionnaire",
            description="2 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute ALTMAN score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
