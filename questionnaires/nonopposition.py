"""
NONOPPOSITION - NONOPPOSITION Questionnaire
===========================================

5 items questionnaire

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


@register_questionnaire("NONOPPOSITION")
@dataclass
class Nonopposition(BaseQuestionnaire):
    """NONOPPOSITION Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize NONOPPOSITION questionnaire with all 5 items."""
        
        questions_list = [
            Question(
                id='atteste',
                text="J'atteste (cocher les cases correspondantes) :",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atteste_curatelle',
                text="J'atteste (cocher les cases correspondantes) : CURATELLE",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atteste_mineur',
                text="J'atteste (cocher les cases correspondantes) : MINEUR",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atteste_tutelle',
                text="J'atteste (cocher les cases correspondantes) : TUTELLE",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='opposition',
                text="Opposition/Non opposition",
                options=[
                    AnswerOption(value='a', label="Ne s'oppose pas au recueil et à l'utilisation d'informations réalisées à partir de son dossier médical", score=0),
                    AnswerOption(value='b', label="S'oppose au recueil et à l'utilisation d'informations réalisées à partir de son dossier médical", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="NONOPPOSITION",
            name="NONOPPOSITION Questionnaire",
            description="5 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute NONOPPOSITION score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
