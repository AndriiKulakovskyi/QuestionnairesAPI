"""
AUT_C1PARTPER - AUT_C1PARTPER Questionnaire
===========================================

12 items questionnaire

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


@register_questionnaire("AUT_C1PARTPER")
@dataclass
class AutC1partper(BaseQuestionnaire):
    """AUT_C1PARTPER Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_C1PARTPER questionnaire with all 12 items."""
        
        questions_list = [
            Question(
                id='bruit',
                text="Bruit",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='chal',
                text="Chaleur",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='doul',
                text="Douleur",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='froid',
                text="Froid",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gout',
                text="Goût",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='odeur',
                text="Odeur",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='perschang',
                text="Changement depuis la dernière visite",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='synest',
                text="Synesthésies",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='synest_e',
                text="Entrée",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='synest_s',
                text="Sortie",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='touch',
                text="Toucher",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='visio',
                text="Vision",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_C1PARTPER",
            name="AUT_C1PARTPER Questionnaire",
            description="12 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=6,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_C1PARTPER score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
