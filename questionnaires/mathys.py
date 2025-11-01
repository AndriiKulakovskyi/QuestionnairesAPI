"""
MATHYS - MATHYS Questionnaire
=============================

7 items questionnaire

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


@register_questionnaire("MATHYS")
@dataclass
class Mathys(BaseQuestionnaire):
    """MATHYS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize MATHYS questionnaire with all 7 items."""
        
        questions_list = [
            Question(
                id='mathys21',
                text="Tristesse",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Occasionnellement.", score=1),
                    AnswerOption(value='c', label="Souvent.", score=2),
                    AnswerOption(value='d', label="Très souvent", score=3),
                    AnswerOption(value='e', label="Constamment", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mathys22',
                text="Joie",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Occasionnellement.", score=1),
                    AnswerOption(value='c', label="Souvent.", score=2),
                    AnswerOption(value='d', label="Très souvent", score=3),
                    AnswerOption(value='e', label="Constamment", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mathys23',
                text="Irritabilité",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Occasionnellement.", score=1),
                    AnswerOption(value='c', label="Souvent.", score=2),
                    AnswerOption(value='d', label="Très souvent", score=3),
                    AnswerOption(value='e', label="Constamment", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mathys24',
                text="Panique",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Occasionnellement.", score=1),
                    AnswerOption(value='c', label="Souvent.", score=2),
                    AnswerOption(value='d', label="Très souvent", score=3),
                    AnswerOption(value='e', label="Constamment", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mathys25',
                text="Anxiété",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Occasionnellement.", score=1),
                    AnswerOption(value='c', label="Souvent.", score=2),
                    AnswerOption(value='d', label="Très souvent", score=3),
                    AnswerOption(value='e', label="Constamment", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mathys26',
                text="Colère",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Occasionnellement.", score=1),
                    AnswerOption(value='c', label="Souvent.", score=2),
                    AnswerOption(value='d', label="Très souvent", score=3),
                    AnswerOption(value='e', label="Constamment", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mathys27',
                text="Exaltation",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Occasionnellement.", score=1),
                    AnswerOption(value='c', label="Souvent.", score=2),
                    AnswerOption(value='d', label="Très souvent", score=3),
                    AnswerOption(value='e', label="Constamment", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="MATHYS",
            name="MATHYS Questionnaire",
            description="7 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute MATHYS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
