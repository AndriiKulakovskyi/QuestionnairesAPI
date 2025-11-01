"""
AUT_LSAS - AUT_LSAS Questionnaire
=================================

48 items questionnaire

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


@register_questionnaire("AUT_LSAS")
@dataclass
class AutLsas(BaseQuestionnaire):
    """AUT_LSAS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_LSAS questionnaire with all 48 items."""
        
        questions_list = [
            Question(
                id='lsas10a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas10e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas11a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas11e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas12a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas12e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas13a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas13e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas14a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas14e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas15a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas15e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas16a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas16e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas17a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas17e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas18a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas18e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas19a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas19e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas1a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas1e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas20a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas20e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas21a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas21e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas22a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas22e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas23a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas23e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas24a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas24e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas2a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas2e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas3a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas3e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas4a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas4e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas5a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas5e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas6a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas6e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas7a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas7e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas8a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas8e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas9a',
                text="ANXIETE",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lsas9e',
                text="EVITEMENT",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_LSAS",
            name="AUT_LSAS Questionnaire",
            description="48 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=24,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_LSAS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
