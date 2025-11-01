"""
AUT_RECSOC - AUT_RECSOC Questionnaire
=====================================

47 items questionnaire

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


@register_questionnaire("AUT_RECSOC")
@dataclass
class AutRecsoc(BaseQuestionnaire):
    """AUT_RECSOC Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_RECSOC questionnaire with all 47 items."""
        
        questions_list = [
            Question(
                id='recscocremp',
                text="Ce questionnaire est rempli par",
                options=[
                    AnswerOption(value='a', label="Père", score=0),
                    AnswerOption(value='b', label="Mère", score=1),
                    AnswerOption(value='c', label="Autre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc10',
                text="10.Interprète les choses de manière trop littérale et ne comprend pas le sens réel des conversations.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc11',
                text="11.A confiance en lui/elle.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc12',
                text="12.Est capable de communiquer des sentiments aux autres.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc15',
                text="15.Est capable de comprendre la signification du ton de la voix et de l'expression faciale des autres personnes.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc16',
                text="16.Evite le contact visuel ou a un contact visuel inhabituel.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc17',
                text="17.Reconnaît lorsque quelque chose est injuste.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc18',
                text="18.L'enfant a du mal à se faire des amis, même quand il/elle fait de son mieux pour essayer.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc19',
                text="19.A des difficultés à transmettre ses idées au cours d'une conversation.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc2',
                text="\n                      2.Son expression faciale n'est pas en harmonie avec ce qu'il/elle dit.\n\n                    ",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc21',
                text="21.Est capable d'imiter les actions des autres.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc22',
                text="22.Joue de manière appropriée avec les enfants de son âge.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc23',
                text="23.Ne se joint pas aux activités des autres sauf si on le lui demande.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc24',
                text="24.A plus de difficulté que les autres enfants à modifier ses routines.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc25',
                text="25.Ne se soucie pas d'être “en phase” ou sur la même “longueur d'onde” que les autres.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc26',
                text="26.Offre du réconfort aux autres quand ils sont tristes.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc27',
                text="27.Evite d'initier des interactions sociales avec les autres.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc28',
                text="28.Obsessionnel, pense ou parle de la même chose de manière répétitive.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc3',
                text="\n                      3.Semble avoir confiance en lui/elle quand il/elle interagit avec les autres.\n\n                    ",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc31',
                text="31.Ne peut pas s'arrêter de penser à quelque chose une fois qu'il/elle a commencé.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc32',
                text="32.A une bonne hygiène personnelle.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc34',
                text="34.Evite les gens qui veulent être émotionnellement proches de lui/elle.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc35',
                text="35.A du mal à suivre le rythme d'une conversation normale.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc36',
                text="36.A des difficultés à entrer en relation avec les adultes.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc37',
                text="37.A des difficultés à entrer en relation avec les personnes de son âge.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc39',
                text="39.A une variété d'intérêts restreinte.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc41',
                text="41.Sans but ; passe d'une activité à l'autre passivement.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc42',
                text="42.Semble extrêmement sensible aux sons, aux textures ou aux odeurs.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc43',
                text="43.Se sépare facilement des personnes qui s'occupent de lui/elle.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc46',
                text="46.A une expression faciale trop sérieuse.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc47',
                text="47.Rit de manière inappropriée.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc48',
                text="48.A le sens de l'humour ; comprend les plaisanteries.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc49',
                text="49.A des aptitudes dans certains domaines précis largement supérieures à la moyenne, mais le niveau de fonctionnement dans la plupart des tâches n'est pas bon.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc5',
                text="\n                      5.Ne réalise pas que les autres essayent de se servir de lui/elle.\n                    ",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc50',
                text="50.A des comportements étranges répétitifs comme agiter les mains ou se balancer.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc51',
                text="51.A des difficultés à répondre aux questions directement et finit par tourner autour du sujet.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc52',
                text="52.Sait quand il/elle parle trop fort ou fait trop de bruit.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc54',
                text="54.Semble utiliser les gens comme s'ils étaient des objets.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc55',
                text="55.Se rend compte quand il/elle est trop proche ou quand il/elle envahit l'espace d'autrui.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc56',
                text="56.Marche entre deux personnes qui sont en train de parler.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc57',
                text="57.On se moque beaucoup de lui/elle.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc58',
                text="58.Se concentre trop sur des parties d'objets au lieu de voir la totalité de l'objet.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc61',
                text="61.Est inflexible, a du mal à changer d'opinion.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc62',
                text="62.Donne des raisons inhabituelles ou illogiques pour faire des choses.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc63',
                text="63.Touche ou accueille les autres de manière inadaptée.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc65',
                text="65.Regarde ou fixe les autres de manière inappropriée.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='recsoc8',
                text="8.Se comporte de façon étrange ou bizarre.",
                options=[
                    AnswerOption(value='a', label="Pas VRAI", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_RECSOC",
            name="AUT_RECSOC Questionnaire",
            description="47 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=23,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_RECSOC score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
