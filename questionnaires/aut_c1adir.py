"""
AUT_C1ADIR - AUT_C1ADIR Questionnaire
=====================================

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


@register_questionnaire("AUT_C1ADIR")
@dataclass
class AutC1adir(BaseQuestionnaire):
    """AUT_C1ADIR Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_C1ADIR questionnaire with all 2 items."""
        
        questions_list = [
            Question(
                id='adinf',
                text="ADI-R",
                options=[
                    AnswerOption(value='a', label="Fait", score=0),
                    AnswerOption(value='b', label="Non fait", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='adirelp',
                text="Parenté de la personne interrogée",
                options=[
                    AnswerOption(value='a', label="Mère", score=0),
                    AnswerOption(value='b', label="Père", score=1),
                    AnswerOption(value='c', label="autre tuteur", score=2),
                    AnswerOption(value='d', label="combinaison de plusieurs entretiens", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_C1ADIR",
            name="AUT_C1ADIR Questionnaire",
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
        """Compute AUT_C1ADIR score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
