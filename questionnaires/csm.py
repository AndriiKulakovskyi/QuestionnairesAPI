"""
CSM - CSM Questionnaire
=======================

11 items questionnaire

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


@register_questionnaire("CSM")
@dataclass
class Csm(BaseQuestionnaire):
    """CSM Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize CSM questionnaire with all 11 items."""
        
        questions_list = [
            Question(
                id='csm1',
                text="1. En ne considérant que le rythme de vie qui vous convient le mieux, à quelle heure vous lèveriez-vous en étant entièrement libre d’organiser votre journée ?",
                options=[
                    AnswerOption(value='a', label="entre 5h 00 et 6h 30", score=0),
                    AnswerOption(value='b', label="entre 6h 30 et 7h 45", score=1),
                    AnswerOption(value='c', label="entre 7h 45 et 9h 45", score=2),
                    AnswerOption(value='d', label="entre 9h45 et 11h 00", score=3),
                    AnswerOption(value='e', label="entre 11h00 et midi", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csm10',
                text="10. A quelle heure vous lèveriez-vous en prévision d’une journée de travail de 8 heures que vous êtes totalement libre d’organiser ?",
                options=[
                    AnswerOption(value='a', label="avant 6h 30", score=0),
                    AnswerOption(value='b', label="entre 6h 30 et 7h 30", score=1),
                    AnswerOption(value='c', label="entre 7h 30 et 8h 30", score=2),
                    AnswerOption(value='d', label="après 8h 30", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csm11',
                text="11. Si vous deviez toujours vous lever à 6h 00, cela vous paraîtrait ?",
                options=[
                    AnswerOption(value='a', label="affreusement difficile", score=0),
                    AnswerOption(value='b', label="plutôt difficile et déplaisant", score=1),
                    AnswerOption(value='c', label="déplaisant sans plus", score=2),
                    AnswerOption(value='d', label="sans aucune difficulté", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csm12',
                text="12. Après une bonne nuit de sommeil, combien de temps vous faut-il pour être pleinement réveillé ?",
                options=[
                    AnswerOption(value='a', label="moins de 10 minutes", score=0),
                    AnswerOption(value='b', label="entre 11 et 20 minutes", score=1),
                    AnswerOption(value='c', label="entre 21 et 40 minutes", score=2),
                    AnswerOption(value='d', label="plus de 40 minutes", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csm2',
                text="2. En ne considérant que le rythme de vie qui vous convient le mieux, à quelle heure vous coucheriez-vous sachant que vous êtes entièrement libre d’organiser votre soirée ?",
                options=[
                    AnswerOption(value='a', label="entre 20h 00 et 21h 00", score=0),
                    AnswerOption(value='b', label="entre 21h 00 et 22h 15", score=1),
                    AnswerOption(value='c', label="entre 22h 15 et 0h 30", score=2),
                    AnswerOption(value='d', label="entre 0h 30 et 1h 45", score=3),
                    AnswerOption(value='e', label="entre 1h 45 et 3h 00", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csm4',
                text="4. Comment vous sentez-vous durant la demi-heure qui suit votre réveil du matin ?",
                options=[
                    AnswerOption(value='a', label="pas du tout réveillé", score=0),
                    AnswerOption(value='b', label="peu éveillé", score=1),
                    AnswerOption(value='c', label="relativement éveillé", score=2),
                    AnswerOption(value='d', label="très éveillé", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csm5',
                text="5. Comment vous sentez-vous durant la demi-heure qui suit votre réveil du matin ?",
                options=[
                    AnswerOption(value='a', label="très fatigué", score=0),
                    AnswerOption(value='b', label="plutôt fatigué", score=1),
                    AnswerOption(value='c', label="plutôt en forme", score=2),
                    AnswerOption(value='d', label="tout à fait frais et dispos", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csm6',
                text="6. Vous avez décidé de faire un sport. Un ami vous suggère de faire deux fois par semaine des séances d’une heure. Le meilleur moment pour lui est de 7 à 8 heures du matin. Ne considérant que le rythme qui vous convient le mieux, dans quelle forme pensez-vous être ?",
                options=[
                    AnswerOption(value='a', label="Bonne forme", score=0),
                    AnswerOption(value='b', label="Forme raisonnable", score=1),
                    AnswerOption(value='c', label="Vous trouvez cela difficile", score=2),
                    AnswerOption(value='d', label="Vous trouvez cela très difficile", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csm7',
                text="7. A quelle heure dans la soirée vous sentez-vous fatigué au point de devoir aller vous coucher ?",
                options=[
                    AnswerOption(value='a', label="entre 20h 00 et 21h 00", score=0),
                    AnswerOption(value='b', label="entre 21h 00 et 22h 15", score=1),
                    AnswerOption(value='c', label="entre 22h 15 et 0h 30", score=2),
                    AnswerOption(value='d', label="entre 0h 30 et 1h 45", score=3),
                    AnswerOption(value='e', label="entre 1h 45 et 3h 00", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csm8',
                text="8. Vous devez être à votre maximum de performance pour un examen écrit qui dure 2 heures. On vous laisse libre de choisir l’heure à laquelle vous pensez être le plus efficace. Ce sera:",
                options=[
                    AnswerOption(value='a', label="entre 8h 00 et 10h 00", score=0),
                    AnswerOption(value='b', label="entre 11h 00 et 13h 00", score=1),
                    AnswerOption(value='c', label="entre 15h 00 et 17h 00", score=2),
                    AnswerOption(value='d', label="entre 19h 00 et 21h 00", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csm9',
                text="9. On entend souvent dire que telle personne est “du matin” et que telle autre personne est “du soir”. En ce qui vous concerne, vous seriez:",
                options=[
                    AnswerOption(value='a', label="tout à fait “du matin”", score=0),
                    AnswerOption(value='b', label="plutôt “du matin” que “du soir”", score=1),
                    AnswerOption(value='c', label="plutôt “du soir” que “du matin”", score=2),
                    AnswerOption(value='d', label="tout à fait “du soir”", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="CSM",
            name="CSM Questionnaire",
            description="11 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute CSM score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
