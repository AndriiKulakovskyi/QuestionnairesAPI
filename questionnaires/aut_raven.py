"""
AUT_RAVEN - AUT_RAVEN Questionnaire
===================================

60 items questionnaire

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


@register_questionnaire("AUT_RAVEN")
@dataclass
class AutRaven(BaseQuestionnaire):
    """AUT_RAVEN Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_RAVEN questionnaire with all 60 items."""
        
        questions_list = [
            Question(
                id='spma1',
                text="1.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spma10',
                text="10.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spma11',
                text="11.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spma12',
                text="12.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spma2',
                text="2.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spma3',
                text="3.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spma4',
                text="4.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spma5',
                text="5.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spma6',
                text="6.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spma7',
                text="7.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spma8',
                text="8.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spma9',
                text="9.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmb1',
                text="1.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmb10',
                text="10.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmb11',
                text="11.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmb12',
                text="12.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmb2',
                text="2.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmb3',
                text="3.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmb4',
                text="4.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmb5',
                text="5.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmb6',
                text="6.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmb7',
                text="7.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmb8',
                text="8.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmb9',
                text="9.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmc1',
                text="1.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmc10',
                text="10.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmc11',
                text="11.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmc12',
                text="12.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmc2',
                text="2.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmc3',
                text="3.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmc4',
                text="4.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmc5',
                text="5.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmc6',
                text="6.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmc7',
                text="7.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmc8',
                text="8.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmc9',
                text="9.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmd1',
                text="1.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmd10',
                text="10.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmd11',
                text="11.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmd12',
                text="12.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmd2',
                text="2.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmd3',
                text="3.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmd4',
                text="4.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmd5',
                text="5.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmd6',
                text="6.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmd7',
                text="7.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmd8',
                text="8.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spmd9',
                text="9.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spme1',
                text="1.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spme10',
                text="10.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spme11',
                text="11.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spme12',
                text="12.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spme2',
                text="2.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spme3',
                text="3.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spme4',
                text="4.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spme5',
                text="5.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spme6',
                text="6.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spme7',
                text="7.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spme8',
                text="8.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spme9',
                text="9.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_RAVEN",
            name="AUT_RAVEN Questionnaire",
            description="60 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=30,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_RAVEN score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
