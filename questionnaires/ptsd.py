"""
PTSD - PTSD Questionnaire
=========================

9 items questionnaire

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


@register_questionnaire("PTSD")
@dataclass
class Ptsd(BaseQuestionnaire):
    """PTSD Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize PTSD questionnaire with all 9 items."""
        
        questions_list = [
            Question(
                id='ptsd12',
                text="12- Se sentir comme si votre avenir était en quelque sorte raccourci",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ptsd14',
                text="14- Se sentir irritable ou avoir des bouffées de colère",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ptsd15',
                text="15- Avoir des difficultés à vous concentrer",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ptsd16',
                text="16- Etre en état de super-alarme, sur la défensive, ou sur vos gardes",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ptsd5',
                text="5- Avoir des réactions physiques, par exemple, battements de coeur, difficultés à respirer, sueurs lorsque quelque chose vous a rappelé l’épisode stressant",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ptsd6',
                text="6- Eviter de penser ou de parler de votre épisode stressant ou éviter des sentiments qui sont en relation avec lui",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ptsd7',
                text="7- Eviter des activités ou des situations parce qu’elles vous rappellent votre épisode stressant",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ptsd8',
                text="8- Avoir des difficultés à se souvenir de parties importantes de l’expérience stressante",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ptsd9',
                text="9- Perte d’intérêt dans des activités qui habituellement vous faisaient plaisir.",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Un peu", score=1),
                    AnswerOption(value='c', label="Parfois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="Très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="PTSD",
            name="PTSD Questionnaire",
            description="9 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute PTSD score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
