"""
SHAPS - SHAPS Questionnaire
===========================

13 items questionnaire

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


@register_questionnaire("SHAPS")
@dataclass
class Shaps(BaseQuestionnaire):
    """SHAPS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize SHAPS questionnaire with all 13 items."""
        
        questions_list = [
            Question(
                id='shaps1',
                text="1 - Mon émission de télévision ou de radio me procure beaucoup de plaisir",
                options=[
                    AnswerOption(value='a', label="Fortement en désaccord", score=0),
                    AnswerOption(value='b', label="En désaccord", score=1),
                    AnswerOption(value='c', label="D’accord", score=2),
                    AnswerOption(value='d', label="Fortement d’accord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='shaps10',
                text="10 - J’apprécie beaucoup une tasse de thé ou de café ou un verre de ma boisson favorite",
                options=[
                    AnswerOption(value='a', label="Fortement en désaccord", score=0),
                    AnswerOption(value='b', label="En désaccord", score=1),
                    AnswerOption(value='c', label="D’accord", score=2),
                    AnswerOption(value='d', label="Fortement d’accord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='shaps11',
                text="11 - Je trouve du plaisir,dans de petits riens tels que par exemple, une journée fortement ensoleillée ou un coup de téléphone d’un ami",
                options=[
                    AnswerOption(value='a', label="Tout à fait d'accord", score=0),
                    AnswerOption(value='b', label="D'accord", score=1),
                    AnswerOption(value='c', label="En désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en desaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='shaps12',
                text="12 - Je suis capable d’apprécier un très beau paysage ou une très belle vue",
                options=[
                    AnswerOption(value='a', label="Tout à fait d'accord", score=0),
                    AnswerOption(value='b', label="D'accord", score=1),
                    AnswerOption(value='c', label="En désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en desaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='shaps13',
                text="13 - Je prends plaisir à aider les autres",
                options=[
                    AnswerOption(value='a', label="Tout à fait d'accord", score=0),
                    AnswerOption(value='b', label="D'accord", score=1),
                    AnswerOption(value='c', label="En désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en desaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='shaps14',
                text="14 - Je ressens du plaisir à recevoir des éloges d’autres personnes",
                options=[
                    AnswerOption(value='a', label="Tout à fait d'accord", score=0),
                    AnswerOption(value='b', label="D'accord", score=1),
                    AnswerOption(value='c', label="En désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en desaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='shaps2',
                text="2 - J’apprécie beaucoup d’être avec ma famille ou avec des amis intimes",
                options=[
                    AnswerOption(value='a', label="Tout à fait d'accord", score=0),
                    AnswerOption(value='b', label="D'accord", score=1),
                    AnswerOption(value='c', label="En désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en desaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='shaps3',
                text="3 - Je trouve du plaisir dans mes hobbies ou passe-temps",
                options=[
                    AnswerOption(value='a', label="Fortement en désaccord", score=0),
                    AnswerOption(value='b', label="En désaccord", score=1),
                    AnswerOption(value='c', label="D’accord", score=2),
                    AnswerOption(value='d', label="Fortement d’accord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='shaps4',
                text="4 - Je suis capable d’apprécier mon plat favori",
                options=[
                    AnswerOption(value='a', label="Tout à fait d'accord", score=0),
                    AnswerOption(value='b', label="D'accord", score=1),
                    AnswerOption(value='c', label="En désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en desaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='shaps5',
                text="5 - J’aime beaucoup prendre un bain chaud ou une douche rafraîchissante",
                options=[
                    AnswerOption(value='a', label="Tout à fait d'accord", score=0),
                    AnswerOption(value='b', label="D'accord", score=1),
                    AnswerOption(value='c', label="En désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en desaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='shaps6',
                text="6 - Je trouve du plaisir dans le parfum des fleurs ou dans l’odeur d’une fraîche brise de mer ou du pain fraîchement cuit",
                options=[
                    AnswerOption(value='a', label="Tout à fait d'accord", score=0),
                    AnswerOption(value='b', label="D'accord", score=1),
                    AnswerOption(value='c', label="En désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en desaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='shaps7',
                text="7 - J’aime beaucoup voir des visages souriants autour de moi",
                options=[
                    AnswerOption(value='a', label="Tout à fait d'accord", score=0),
                    AnswerOption(value='b', label="D'accord", score=1),
                    AnswerOption(value='c', label="En désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en desaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='shaps9',
                text="9 - J’aime beaucoup lire un livre, un magazine ou un journal",
                options=[
                    AnswerOption(value='a', label="Tout à fait d'accord", score=0),
                    AnswerOption(value='b', label="D'accord", score=1),
                    AnswerOption(value='c', label="En désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en desaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="SHAPS",
            name="SHAPS Questionnaire",
            description="13 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=6,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute SHAPS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
