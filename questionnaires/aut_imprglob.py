"""
AUT_IMPRGLOB - AUT_IMPRGLOB Questionnaire
=========================================

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


@register_questionnaire("AUT_IMPRGLOB")
@dataclass
class AutImprglob(BaseQuestionnaire):
    """AUT_IMPRGLOB Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_IMPRGLOB questionnaire with all 2 items."""
        
        questions_list = [
            Question(
                id='cgichang',
                text="Changement depuis la dernière visite",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gravmdi',
                text="En fonction de votre expérience clinique totale avec ce type de patient, quel est le niveau de gravité des troubles mentaux actuels du patient  ?",
                options=[
                    AnswerOption(value='a', label="non évalué", score=0),
                    AnswerOption(value='b', label="normal, pas du tout malade", score=1),
                    AnswerOption(value='c', label="à la limite", score=2),
                    AnswerOption(value='d', label="légèrement malade", score=3),
                    AnswerOption(value='e', label="modérément malade", score=4),
                    AnswerOption(value='f', label="manifestement malade", score=5),
                    AnswerOption(value='g', label="gravement malade", score=6),
                    AnswerOption(value='h', label="parmi les patients les plus malades", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_IMPRGLOB",
            name="AUT_IMPRGLOB Questionnaire",
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
        """Compute AUT_IMPRGLOB score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
