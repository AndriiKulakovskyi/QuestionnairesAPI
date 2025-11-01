"""
ISF - ISF Questionnaire
=======================

10 items questionnaire

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


@register_questionnaire("ISF")
@dataclass
class Isf(BaseQuestionnaire):
    """ISF Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize ISF questionnaire with all 10 items."""
        
        questions_list = [
            Question(
                id='isf1',
                text="1. Avez-vous déjà eu l’impression que la vie ne vaut pas la peine d’être vécue ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='isf1bis',
                text="Spécifier : Quand cela est-il arrivé pour la dernière fois ?",
                options=[
                    AnswerOption(value='a', label="la semaine dernière", score=0),
                    AnswerOption(value='b', label="il y a entre deux semaines et douze mois", score=1),
                    AnswerOption(value='c', label="il y a plus d’un an", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='isf2',
                text="2. Avez-vous déjà souhaité mourir, par exemple, de vous coucher et de ne pas vous réveiller ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='isf2bis',
                text="Spécifier : Quand cela est-il arrivé pour la dernière fois ?",
                options=[
                    AnswerOption(value='a', label="la semaine dernière", score=0),
                    AnswerOption(value='b', label="il y a entre deux semaines et douze mois", score=1),
                    AnswerOption(value='c', label="il y a plus d’un an", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='isf3',
                text="3. Avez-vous déjà pensé à vous donner la mort, même si vous ne le feriez jamais ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='isf3bis',
                text="Spécifier : Quand cela est-il arrivé pour la dernière fois ?",
                options=[
                    AnswerOption(value='a', label="la semaine dernière", score=0),
                    AnswerOption(value='b', label="il y a entre deux semaines et douze mois", score=1),
                    AnswerOption(value='c', label="il y a plus d’un an", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='isf4',
                text="4. Avez-vous déjà sérieusement envisagé de vous donner la mort ou planifié la façon de vous y prendre ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='isf4bis',
                text="Spécifier : Quand cela est-il arrivé pour la dernière fois ?",
                options=[
                    AnswerOption(value='a', label="la semaine dernière", score=0),
                    AnswerOption(value='b', label="il y a entre deux semaines et douze mois", score=1),
                    AnswerOption(value='c', label="il y a plus d’un an", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='isf5',
                text="5. Avez-vous déjà essayé de vous donner la mort ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='isf5bis',
                text="Spécifier : Quand cela est-il arrivé pour la dernière fois ?",
                options=[
                    AnswerOption(value='a', label="la semaine dernière", score=0),
                    AnswerOption(value='b', label="il y a entre deux semaines et douze mois", score=1),
                    AnswerOption(value='c', label="il y a plus d’un an", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="ISF",
            name="ISF Questionnaire",
            description="10 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute ISF score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
