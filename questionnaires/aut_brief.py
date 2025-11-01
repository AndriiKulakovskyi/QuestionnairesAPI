"""
AUT_BRIEF - AUT_BRIEF Questionnaire
===================================

87 items questionnaire

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


@register_questionnaire("AUT_BRIEF")
@dataclass
class AutBrief(BaseQuestionnaire):
    """AUT_BRIEF Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_BRIEF questionnaire with all 87 items."""
        
        questions_list = [
            Question(
                id='brief1',
                text="1.J'ai des accès de colère",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief10',
                text="10.J'oublie mon nom",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief11',
                text="11.J'ai des difficultés pour faire un travail ou des activités qui nécessitent plus d'une étape",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief12',
                text="12.J'ai des réactions émotionnelles excessives",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief13',
                text="13.Je m'aperçois trop tard que mon comportement fait de la peine ou énerve les autres",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief14',
                text="14.J'ai des difficultés à me préparer pour la journée",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief15',
                text="15.J'ai des difficultés pour organiser mes activités selon leur priorité",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief16',
                text="16.J'ai des difficultés pour rester tranquillement assis(e)",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief17',
                text="17.J'oublie ce que j'étais en train de faire en plein milieu d'une activité",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief18',
                text="18.Je ne vérifie pas mon travail pour voir s'il y a des erreurs",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief19',
                text="19.Je me laisse envahir par mes émotions pour des raisons anodines",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief2',
                text="2.Je fais des erreurs d'inattention lorsque je réalise des tâches",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief20',
                text="20.Je traîne beaucoup à la maison",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief21',
                text="21.Je commence les tâches (comme la cuisine ou des travaux manuels) sans avoir préparé le bon matériel",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief22',
                text="22.J'ai des difficultés à accepter des points de vue différents du mien pour résoudre les problèmes dans le cadre du travail, avec les amis ou dans les tâches quotidiennes",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief23',
                text="23.Je parle au mauvais moment",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief24',
                text="24.J'évalue mal le niveau de difficulté des tâches que je dois réaliser",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief25',
                text="25.J'ai des difficultés à commencer quelque chose par moi-même",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief26',
                text="26.J'ai du mal à rester sur un seul sujet lorsque je parle",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief27',
                text="27.Je me fatigue rapidement",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief28',
                text="28.Je réagis de manière plus émotive que mes amis",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief29',
                text="29.J'ai du mal à attendre mon tour",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief3',
                text="3.Je suis désorganisé(e)",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief30',
                text="30.Les gens disent que je suis désorganisé(e)",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief31',
                text="31.Je perds mes affaires (comme mes clés, mon argent, mon portefeuille, mes documents, etc.)",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief32',
                text="32.J'ai des difficultés à envisager une nouvelle approche pour résoudre un problème quand je suis bloqué(e)",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief33',
                text="33.J'ai des réactions excessives face à des problèmes peu importants",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief34',
                text="34.Je ne m'y prends pas à l'avance pour organiser les choses que j'ai à faire",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief35',
                text="35.J'ai une capacité d'attention limitée",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief36',
                text="36.Je fais des commentaires inappropriés à connotation sexuelle",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief37',
                text="37.Je ne comprends pas quand les autres semblent fâchés avec moi",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief38',
                text="38.J'ai des difficultés pour compter jusqu'à 3",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief39',
                text="39.Je formule des objectifs irréalistes",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief4',
                text="4.J'ai des difficultés pour me concentrer sur les tâches (comme les tâches ménagères, la lecture ou le travail)",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief40',
                text="40.Je laisse la salle de bain en désordre",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief41',
                text="41.Je fais des fautes d'inattention",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief42',
                text="42.Je suis facilement affecté(e) par mes émotions",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief43',
                text="43.Je .prends des décisions qui me mettent dans une situation difficile (légalement, financièrement, socialement)",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief44',
                text="44.Je suis gêné(e) quand je dois faire face à des changements",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief45',
                text="45.J'ai des difficultés à m'enthousiasmer pour les choses",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief46',
                text="46.J'oublie facilement les instructions",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief47',
                text="47.J'ai de bonnes idées mais ne peux pas les mettre par écrit",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief48',
                text="48.Je fais des erreurs",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief49',
                text="49.J'ai des difficultés pour me mettre à faire quelque chose",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief5',
                text="5.Je tapote avec mes doigts ou remue mes jambes",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief50',
                text="50.Je dis les choses sans réfléchir",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief51',
                text="51.Mes accès de colère sont intenses mais se terminent rapidement",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief52',
                text="52.J'ai du mal à terminer ce que je commence (tâches quotidiennes, travail)",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief53',
                text="53.Je commence les choses à la dernière minute (comme les travaux, les tâches de la vie quotidienne)",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief54',
                text="54.J'ai des difficultés à finir de moi-même ce que j'entreprends",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief55',
                text="55.Les gens disent que je suis facilement distrait(e)",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief56',
                text="56.J'ai des difficultés à me souvenir des choses, même pendant quelques minutes (comme les trajets,les numéros de téléphone)",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief57',
                text="57.Les gens disent que je suis trop émotif(ve)",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief58',
                text="58.Je fais les choses de manière précipitée",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief59',
                text="59.Je m'énerve facilement",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief6',
                text="6.J'ai besoin qu'on me rappelle de commencer une tâche même lorsque je suis d'accord pour le faire",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief60',
                text="60.Je laisse la pièce ou mon domicile en désordre",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief61',
                text="61.Je suis perturbé(e) par des changements imprévus dans ma vie quotidienne",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief62',
                text="62.J'ai du mal à occuper mon temps libre",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief63',
                text="63.Je ne planifie/organise pas mes activités à l'avance",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief64',
                text="64.Les gens disent que je ne réfléchis pas avant d'agir",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief65',
                text="65.J'ai des difficultés à trouver mes affaires dans ma chambre, mon placard ou mon bureau",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief66',
                text="66.J'ai des difficultés pour organiser mes activités",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief67',
                text="67.J'ai du mal à surmonter les difficultés/problèmes que je rencontre",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief68',
                text="68.J'ai des difficultés pour faire plus d'une chose à la fois",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief69',
                text="69.Mon humeur change souvent",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief70',
                text="70.Je ne réfléchis pas aux conséquences avant de faire quelque chose",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief71',
                text="71.J'ai des difficultés pour l'organisation de mon travail",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief72',
                text="72.Je m'énerve rapidement ou facilement pour des choses sans importance",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief73',
                text="73.Je suis impulsif(ve)",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief74',
                text="74.Je laisse traîner mes affaires partout",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief75',
                text="75.J'ai du mal à terminer complètement mon travail",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief76',
                text="76.Obtient des résultats très moyens aux contrôles, même lorsqu’il/elle connaît les bonnes réponses",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief77',
                text="77.Ne finit pas de projets à long terme",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief78',
                text="78.Doit être surveillé(e) de près",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief79',
                text="79.Ne réfléchit pas avant d’agir",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief8',
                text="8.J'ai des difficultés pour passer d'une activité ou d'une tâche à l'autre",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief80',
                text="80.A des difficultés pour passer d'une occupation à l autre",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief81',
                text="81.Est agité(e), remuant(e)",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief82',
                text="82.Est impulsif",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief83',
                text="83.A du mal à poursuivre sur un seul sujet lorsqu’il/elle parle",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief84',
                text="84.Son intérêt se bloque sur un sujet ou une activité unique",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief85',
                text="85.Répète les mêmes choses, encore et encore ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief86',
                text="86.A des difficultés pour se préparer le matin pour l'école",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief9',
                text="9.Je suis dépassé(e) quand il y a beaucoup de choses à faire",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Parfois", score=1),
                    AnswerOption(value='c', label="Souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief_cone',
                text="<b>A quel point la/le connaissez-vous ?</b>",
                options=[
                    AnswerOption(value='a', label="Pas très bien", score=0),
                    AnswerOption(value='b', label="Bien", score=1),
                    AnswerOption(value='c', label="Très bien", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brief_rel',
                text="<b>Votre relation avec elle/lui</b>",
                options=[
                    AnswerOption(value='a', label="Parent", score=0),
                    AnswerOption(value='b', label="Epoux", score=1),
                    AnswerOption(value='c', label="Frère/Soeur", score=2),
                    AnswerOption(value='d', label="Ami", score=3),
                    AnswerOption(value='e', label="Autre", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_BRIEF",
            name="AUT_BRIEF Questionnaire",
            description="87 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=43,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_BRIEF score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
