"""
AMIEL_LEBIGRE - AMIEL_LEBIGRE Questionnaire
===========================================

53 items questionnaire

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


@register_questionnaire("AMIEL_LEBIGRE")
@dataclass
class AmielLebigre(BaseQuestionnaire):
    """AMIEL_LEBIGRE Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AMIEL_LEBIGRE questionnaire with all 53 items."""
        
        questions_list = [
            Question(
                id='amiel10_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel11_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel12_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel13_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel14_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel15_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel16_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel17_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel18_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel19_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel1_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel20_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel21_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel22_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel23_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel24_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel25_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel26_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel27_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel28_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel29_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel2_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel30_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel31_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel32_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel33_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel34_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel35_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel36_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel37_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel38_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel39_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel3_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel40_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel41_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel42_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel43_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel44_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel45_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel46_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel47_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel48_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel49_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel4_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel50_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel51_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel52_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel53_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel5_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel6_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel7_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel8_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='amiel9_date',
                text="Date : ",
                options=[
                    AnswerOption(value='a', label="SIX MOIS", score=0),
                    AnswerOption(value='b', label="UN AN", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AMIEL_LEBIGRE",
            name="AMIEL_LEBIGRE Questionnaire",
            description="53 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=26,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AMIEL_LEBIGRE score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
