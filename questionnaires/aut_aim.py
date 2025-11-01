"""
AUT_AIM - AUT_AIM Questionnaire
===============================

23 items questionnaire

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


@register_questionnaire("AUT_AIM")
@dataclass
class AutAim(BaseQuestionnaire):
    """AUT_AIM Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_AIM questionnaire with all 23 items."""
        
        questions_list = [
            Question(
                id='aim_10',
                text="10.Mon cœur bat vite en attendant un événement excitant",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_11',
                text="11.Les films tristes me touchent profondément",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_13',
                text="13.Quand je parle devant un groupe pour la première fois, ma voix devient tremblante et mon coeur bat vite",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_14',
                text="14.Quand quelque chose de bien m'arrive, je jubile habituellement plus que les autres",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_17',
                text="17.La vue de quelqu'un qui est blessé gravement m'affecte profondément",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_19',
                text="19.Calme et imperturbable pourraient facilement me décrire",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_21',
                text="21.Regarder les images d'un accident de voiture violent dans un journal me donne la nausée",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_24',
                text="24.Quand je réussis quelque chose, ma réaction est une satisfaction calme",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_25',
                text="25.Quand je fais quelque chose de mal, j'ai un sentiment très fort de culpabilité et de honte",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_26',
                text="26.Je peux rester calme, même les jours les plus pénibles",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_27',
                text="27.Quand les choses vont bien, je me sens comme si j'étais au sommet du monde",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_28',
                text="28.Quand je suis en colère, c'est facile pour moi de rester rationnel et de ne pas réagir trop fort",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_3',
                text="3.J'aime énormément être avec les autres",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_31',
                text="31.Mes humeurs négatives sont habituellement d'intensité légère",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_34',
                text="34.Mes amis diraient probablement que je suis quelqu'un de tendu ou très énervé",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_36',
                text="36.Quand je me sens coupable, cette émotion est forte",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_37',
                text="37.Je décrirais mes émotions heureuses comme étant plus proches de la satisfaction que de la joie.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_4',
                text="4.Je me sens très mal quand je fais un mensonge",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_5',
                text="5.Quand je résous un petit problème personnel, je me sens euphorique",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_6',
                text="6.Mes émotions ont tendance à être plus intenses que celles de la plupart des autres personnes",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_7',
                text="7.Mes périodes d'humeur joyeuse sont si fortes que j'ai l'impression d'être au paradis",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_8',
                text="8.Je deviens exagérément enthousiaste",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aim_9',
                text="9.Si je termine une tâche je jugeais impossible à faire, je me sens en extase",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Presque jamais", score=1),
                    AnswerOption(value='c', label="Occasionnellement", score=2),
                    AnswerOption(value='d', label="Habituellement", score=3),
                    AnswerOption(value='e', label="Presque toujours", score=4),
                    AnswerOption(value='f', label="Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_AIM",
            name="AUT_AIM Questionnaire",
            description="23 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=11,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_AIM score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
