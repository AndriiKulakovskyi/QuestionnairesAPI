"""
AUT_ATAC - AUT_ATAC Questionnaire
=================================

225 items questionnaire

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


@register_questionnaire("AUT_ATAC")
@dataclass
class AutAtac(BaseQuestionnaire):
    """AUT_ATAC Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_ATAC questionnaire with all 225 items."""
        
        questions_list = [
            Question(
                id='atac1',
                text="Est-ce qu'il lui est difficile de coordonner les mouvements de son corps avec souplesse ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac10',
                text="10.Est-ce qu'il lui est difficile de suivre des consignes et de terminer ses devoirs ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac11',
                text="11.Est-ce qu'il lui est difficile d'organiser des tâches et activités ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac13',
                text="13.Est-ce qu'il/elle perd facilement ses affaires ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac14',
                text="14.Est-ce qu'il/elle est facilement distrait ou perturbé ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac15',
                text="15.Est-ce qu'il est souvent oublieux dans la vie de tous les jours ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac16',
                text="16.Est-ce qu'il lui est difficile de maintenir les mains ou les pieds immobiles ou de rester assis tranquillement ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac17',
                text="17.Est-ce qu'il/elle se lève souvent et remue beaucoup en classe ou dans d'autres situations où on est supposé rester assis ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac18',
                text="18.Est-ce qu'il/elle s'agite facilement ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac19',
                text="19.Est-ce qu'il lui est difficile de jouer calmement ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac20',
                text="20.Est-ce qu'il se comporte comme s'il était poussé par un moteur et est toujours à courir ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac21',
                text="21.Est-ce qu'il est très bavard ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac22',
                text="22.Est-ce qu'il laisse échapper la réponse avant que la question soit posée ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac23',
                text="23.Est-ce qu'il lui est difficile d'attendre son tour ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac24',
                text="24.Est-ce qu'il/elle coupe souvent la parole aux autres ou fait souvent intrusion ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac25',
                text="25.Est-ce qu'il/elle s'ennuie facilement ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac26',
                text="26.Est-ce qu'il a eu plus de mal à apprendre à lire que les autres enfants ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac27',
                text="27.Est-ce qu'il apprend lentement et de façon laborieuse ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac28',
                text="28.Est-ce qu'il a des difficultés en mathématiques ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac29',
                text="29.Est-ce qu'il lui est difficile de changer ses plans ou sa stratégie pour faire les choses si c'est nécessaire ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac3',
                text="3.Est-ce qu'il lui est difficile d'apprécier les distances et les relations de taille ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac30',
                text="30.Est-ce qu'il trouve difficile d'être ordonné ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac31',
                text="31.Est-ce qu'il lui est difficile de se rappeler où il/elle a posé ses affaires ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac32',
                text="32.Est-ce qu'il lui est difficile de se rappeler des instructions longues ou enchaînées ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac33',
                text="33.Est-ce qu'il lui est difficile d'apprendre par coeur des comptines, des chansons ou les tables de multiplication ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac34',
                text="34.Est-ce qu'il/elle était en retard pour apprendre à parler ou est-ce qu'il/elle ne parle pas du tout ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac35',
                text="35.Est-ce qu'il lui est difficile de suivre une conversation ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac36',
                text="36.Est-ce qu'il lui plaît de répéter les mots et les expressions ou utilise-t-il le vocabulaire de façon étrange ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac37',
                text="37.Est-ce qu'il lui est difficile de jouer à faire semblant ou d'imiter d'autres personnes ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac38',
                text="38.Est-ce qu'il parle d'une voix trop aiguë ou trop basse ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac39',
                text="39.Est-ce qu'il lui est difficile de garder un fil conducteur quand il/elle veut raconter quelque chose ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac4',
                text="4.Est-ce qu'il/elle est hypersensible au toucher ou aux vêtements serrés ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac40',
                text="40.Est-ce qu'il lui est difficile d'exprimer ses émotions et réactions par sa mimique, ses intonations ou sa façon de se tenir ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac41',
                text="41.Est-ce qu'il/elle a des problèmes évidents pour trouver ou garder des amis ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac42',
                text="42.Est-ce qu'il/elle montre peu d'intérêt au partage avec les autres de plaisirs, d'intérêts ou d'activités ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac43',
                text="43.Est-ce qu'il/elle ne peut passer un moment avec d'autres que s'il fixe les conditions ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac44',
                text="44.Est-ce qu'il lui est difficile de se comporter comme les copains s'y attendent ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac45',
                text="45.Est-ce qu'il/elle est très influençable par les autres ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac46',
                text="46.Est-ce qu'il/elle montre un tel engouement pour certains sujets que ça en devient répétitif ou trop intense ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac47',
                text="47.Est-ce qu'il/elle parait fixé dans des routines au point que cela pose un problème aux autres ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac48',
                text="48.Est-ce qu'il/elle a eu une période où il/elle a fait certains mouvements automatiquement quand il/elle était content ou en colère ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac49',
                text="49.Est-ce qu'il/elle s'attache aux détails ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac5',
                text="5.Est-ce qu'il/elle est particulièrement sensible à certains sons/bruits ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac50',
                text="50.Est-ce qu'il/elle supporte mal les changements mineurs dans la vie quotidienne ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac51',
                text="51.Est-ce qu'il/elle a eu une période où il/elle a fait des bruit involontaires tels que se racler la gorge, renifler, déglutir, aboyer ou pousser des cris ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac52',
                text="52.Est-ce qu'il/elle a jamais présenté des mouvements involontaires, des tics, des contractions ou des grimaces ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac53',
                text="53.Est-ce qu'il/elle fait beaucoup de bruits, par exemple des sifflements, des chantonnements ou des murmures ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac54',
                text="54.Est-ce qu'il/elle a des obsessions, c'est à dire des pensées récurrentes qu'il/elle ne peut pas contrôler, par exemple concernant la saleté, la contamination ou de possibles événements dangereux ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac55',
                text="55.Est-ce qu'il/elle a des comportements compulsifs, comme par exemple de se laver les mains, toucher les choses, vérifier, répéter, ranger ou remettre les objets à une certaine place ou compter ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac56',
                text="56.Est-ce qu'il/elle est arrivé que sa prise de poids soit insuffisante pendant au moins un an?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac57',
                text="57.est-ce qu'il/elle a donné l'impression d'avoir peur de prendre du poids et grossir ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac58',
                text="58.Est-ce qu'il lui est difficile de fonctionner en dehors du foyer ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac59',
                text="59.Est-ce qu'il/elle exprime souvent une peur que quelqu'un de la famille meure ou ait un accident ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac6',
                text="6.Est-ce qu'il/elle est particulièrement sensible à certains goûts, odeurs ou consistances.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac61',
                text="61.Est-ce qu'il lui est difficile de dormir s'il n'y a pas quelqu'un de la famille présent ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac62',
                text="62.Est-ce qu'il/elle se plaint souvent de maux de tête, de maux de ventre, de nausées ou de vomissements quand il/elle doit quitter ses proches ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac64',
                text="64.Est-ce qu'il/elle est souvent en conflit avec les autres ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac65',
                text="65.Est-ce qu'il/elle agace souvent les autres en faisant des choses provocantes exprès ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac68',
                text="68.Est-ce qu'il/elle ment ou triche souvent ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac69',
                text="69.Est-ce qu'il/elle a déjà volé dans un magasin ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac7',
                text="7.Est-ce qu'il prête souvent peu d'attention aux détails ou est-ce qu'il fait souvent des erreurs d'étourderie à l'école où lors d'autres activités ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac70',
                text="70.Est-ce qu'il/elle a été physiquement cruel délibérément avec quelqu'un ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac71',
                text="71.Est-ce qu'il/elle prend souvent l'initiative des bagarres ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac72',
                text="72.Est-ce qu'il/elle prend ou vole régulièrement des affaires à la maison ou ailleurs ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac73',
                text="73.Est-ce qu'il/elle a déjà eu des attaques de panique avec une peur ou angoisse soudaine parfois accompagnée d'essoufflement et de palpitations ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac74',
                text="74.Est-ce qu'il/elle a peur de quitter la maison, d'être dans la foule, de faire la queue ou de prendre le bus ou le train ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac75',
                text="75.Est-ce qu'il/elle est particulièrement nerveux ou angoissé ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac76',
                text="76.Est-ce qu'il/elle a peu confiance en lui/elle ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac77',
                text="77.Est-ce qu'il/elle se plaint souvent de maux de ventre, de maux de tête, de troubles respiratoires ou d'autres symptômes physiques ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac78',
                text="78.Est-ce qu'il/elle a eu des périodes où il/elle a été extrêmement actif avec des pensées très rapides ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac79',
                text="79.Est-ce qu'il/elle est par périodes manifestement susceptible ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac8',
                text="8.Est-ce qu'il lui est difficile de soutenir son attention lors de tâches ou d‘activités ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac80',
                text="80.Est-ce que sa confiance en lui varie considérablement d'une situation à l'autre ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac81',
                text="81.Est-ce qu'il/elle a eu des visions ou vu ce qui n'est pas visible par d'autres ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac82',
                text="82.Est-ce qu'il/elle bégaye ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac83',
                text="83.Est-ce qu'il/elle a été brimé par ses camarades à l'école ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac84',
                text="84.Est-ce qu'il/elle a été obèse ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac85',
                text="85.Est-ce qu'il/elle a des troubles de sommeil ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac86',
                text="86.Est-ce qu'il/elle fait souvent des cauchemars ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac87',
                text="87.Est-ce qu'il/elle est somnambule ou présente des terreurs nocturnes pendant lesquelles il est difficile d'établir un contact avec lui et le/la consoler ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac88',
                text="88.Est-ce qu'il/elle a jamais essayé de se blesser ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac89',
                text="89.Est-ce qu'il/elle s'est blessé volontairement de façon répétée ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac9',
                text="9.Est-ce qu'il/elle donne souvent l'impression de ne pas écouter ce qu'on lui dit ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac90',
                text="90.Est-ce qu'il/elle a très peur d'autre chose, par exemple l'avion, le sang, les seringues, l'altitude, les endroits confinés ou certains animaux ou insectes ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac91',
                text="91.Est-ce qu'il/elle a présenté plusieurs épisodes d'énurésie nocturne après 5 ans ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac93',
                text="93.Est-ce qu'il/elle fume ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac94',
                text="94.Est-ce qu'il/elle prend du tabac sous d'autres formes ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac95',
                text="95.Est-ce qu'il/elle a déjà eu des problèmes en lien avec l'alcool ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atac96',
                text="96.Est-ce qu'il/elle a déjà eu une période après l'âge de 5 ans pendant laquelle il/elle voulait ne manger que certains types particuliers de nourriture ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataca1',
                text="A1.Est-ce qu'il/elle est gauche ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataca2',
                text="A2.Est-ce qu'il/elle est maladroit ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataca3',
                text="A3.A-t-il des troubles de l'équilibre ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataca4',
                text="A4.Est-ce qu'il/elle trébuche ou tombe facilement ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataca5',
                text="A5.Est-ce que ces problèmes/particularités ont entraîné une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataca6',
                text="A6.Est-ce qu'il/elle souffre des problèmes de coordination ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataca8',
                text="A8.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacb1',
                text="B1.Est-ce qu'il comprend difficilement les principes d'orientation et direction dans l'espace, par exemple met-il souvent ses vêtements à l'envers ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacb2',
                text="B2.Est-ce qu'il/elle heurte souvent des gens ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacb3',
                text="B3.Est-ce qu'il/elle a une mauvaise notion du temps ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacb4',
                text="B4.Est-ce qu'il lui est difficile d'imiter les mouvements des autres ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacb5',
                text="B5.Est-ce qu'il lui est difficile de reconnaître les gens ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacb6',
                text="B6.Est-ce que ces problèmes/particularités ont entraîné une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacb7',
                text="B7.Est-ce qu'il/elle souffre des problèmes/particularités de perceptions ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacb9',
                text="B9.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacc1',
                text="C1.Est-ce qu'il lui est difficile d'initier des tâches ou activités ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacc2',
                text="C2.Est-ce qu'il lui est difficile d'achever les tâches ou activités ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacc3',
                text="C3.Est-ce que ces problèmes/particularités ont causé une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacc4',
                text="C4.Est-ce qu'il/elle souffre des problèmes/particularités concernant l'attention ou les facultés de concentration ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacc6',
                text="C6.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacd1',
                text="D1.Est-ce qu'il/elle est particulièrement intrépide dans les situations de dangers physiques ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacd2',
                text="D2.Est-ce que ces problèmes/particularités lui ont entraîné une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacd3',
                text="D3.Est-ce qu'il/elle souffre des problèmes d'impulsivité et d'hyperactivité ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacd5',
                text="D5.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atace1',
                text="E1.Est-ce qu'il/elle lit lentement ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atace10',
                text="E10.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atace3',
                text="E3.Est-ce que les problèmes de maths où il faut lire un texte représentent une difficulté particulière ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atace4',
                text="E4.Est-ce qu'il lui est difficile de comprendre ou se servir des abstractions ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atace5',
                text="E5.Est-ce que l'orthographe représente une difficulté ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atace6',
                text="E6.Est-ce qu'il/elle a une éducation spéciale à l'école ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atace7',
                text="E7.Est-ce que ces problèmes/particularités ont entraîné une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atace8',
                text="E8.Est-ce qu'il/elle souffre des problèmes d'apprentissage ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacf1',
                text="F1.Est-ce qu'il est difficile pour lui de comprendre les conséquences de ses actes ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacf3',
                text="F3.Est-ce qu'il/elle est difficile pour lui de prendre soin de son hygiène personnelle et de ses vêtements, etc. ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacf4',
                text="F4.Est-ce qu'il lui est difficile de différer la récompense ou d'envisager l'intérêt de ce qui ne conduit pas à une récompense immédiate ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacf5',
                text="F5.Est-ce que les activités de la vie quotidienne sont fatigantes ou lui demandent beaucoup d'énergie ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacf6',
                text="F6.Est-ce que ces problèmes/particularités ont entraîné une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacf7',
                text="F7.Est-ce qu'il/elle souffre des problèmes concernant les facultés de projection et d'organisation ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacf9',
                text="F9.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacg1',
                text="G1.Est-ce qu'il lui est difficile de se souvenir des faits personnels comme sa date de naissance ou son adresse.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacg10',
                text="G10.Est-ce qu'il/elle souffre des problèmes de mémoire ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacg12',
                text="G12.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacg2',
                text="G2.Est-ce qu'il/elle confond souvent les noms ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacg3',
                text="G3.Est-ce qu'il lui est difficile de se souvenir des noms des jours, mois et saisons ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacg4',
                text="G4.Est-ce qu'il lui est difficile de se souvenir des faits non personnels, comme les dates historiques ou des formules chimiques apprises à l'école ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacg5',
                text="G5.Est-ce qu'il lui est difficile de se souvenir des événements qui ont eu lieu récemment, par exemple ce qui s'est passé pendant la journée ou ce qui a été servi à la cantine ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacg6',
                text="G6.Est-ce qu'il lui est difficile de se souvenir des événements un peu plus anciens, par exemple ce qui s'est passé pendant un voyage ou ce qu'il/elle a eu comme cadeaux de Noël ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacg7',
                text="G7.Est-ce qu'il lui est difficile de se souvenir des rendez-vous avec des copains ou des devoirs donnés pour le lendemain ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacg8',
                text="G8.Est-ce qu'il lui est difficile d'apprendre les règles d'un nouveau jeu ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacg9',
                text="G9.Est-ce que ces problèmes/particularités ont entraîné une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atach1',
                text="H1.Est-ce qu'il lui est difficile de s'exprimer avec des phrases complètes ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atach10',
                text="H10.Est-ce que ces problèmes/particularités ont entraîné une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atach11',
                text="H11.Est-ce qu'il/elle souffre des problèmes de langage ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atach13',
                text="H13.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atach2',
                text="H2.Est-ce qu'il/elle parle d'une voix monotone ou « étrange » ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atach3',
                text="H3.Est-ce qu'il lui est difficile de raconter ses expériences ou certaines situations de façon compréhensible pour l'interlocuteur ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atach4',
                text="H4.Est-ce qu'il lui est difficile d'exprimer ce qu'il/elle désire ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atach5',
                text="H5.Est-ce qu'il lui est difficile de parler de façon fluide, sans balbutier ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atach6',
                text="H6.Est-ce qu'il lui est difficile de prononcer les mots difficiles ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atach7',
                text="H7.Est-ce que l'expression verbale des émotions est difficile pour lui/elle ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atach8',
                text="H8.Est ce qu'il/elle utilise des phrases étranges, des mots désuets ou précieux ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atach9',
                text="H9.Est-ce qu'il/elle parle si vite qu'il/elle est difficile à comprendre ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataci1',
                text="I1.Est-ce qu'il/elle est perçu comme égocentrique ou égoïste ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataci10',
                text="I10.Est-ce qu'il/elle donne souvent l'impression de manquer de sens commun ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataci11',
                text="I11.Est-ce qu'il lui est difficile de croiser le regard des autres ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataci13',
                text="I13.Est-ce que ses gestes sont gauches, maladroits, étranges ou inhabituels ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataci14',
                text="I14.Est-ce qu'il lui est difficile d'interpréter ce que les autres expriment par le regard ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataci15',
                text="I15.Est-ce que son regard est fixe, étrange, particulier, anormal ou singulier ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataci16',
                text="I16.Est-ce que ces problèmes/particularités ont causé une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataci17',
                text="I17.Est-ce qu'il/elle souffre des problèmes d'interaction sociale ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataci19',
                text="I19.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataci3',
                text="I3.Est-ce qu'il lui est difficile de comprendre les indices sociaux comme les mimiques, intonations ou façons de se tenir ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataci4',
                text="I4.Est-ce qu'il lui est difficile de comprendre les sentiments des autres ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataci5',
                text="I5.Est-ce qu'il lui est difficile de témoigner de respect envers les autres ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataci6',
                text="I6.Est-ce qu'il/elle montre un comportement excessif quand il y a beaucoup de monde ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataci7',
                text="I7.Est-ce qu'il/elle a l'habitude de partir au milieu d'une conversation ou de changer de sujet abruptement ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataci8',
                text="I8.Est-ce qu'il lui est difficile de savoir comment on doit se comporter dans différentes situations sociales ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataci9',
                text="I9.Est-ce qu'il/elle se rend parfois ridicule involontairement ou fait-il parfois des remarques naïves ou embarrassantes ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacj1',
                text="J1.Est-ce que ces problèmes/particularités ont causé une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacj2',
                text="J2.Est-ce qu'il/elle souffre des problèmes de flexibilité ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacj4',
                text="J4.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atack2',
                text="K2.Est-ce que ces problèmes/particularités ont entraîné une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atack3',
                text="K3.Est-ce qu'il/elle souffre des problèmes de tics ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atack5',
                text="K5.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacl1',
                text="L1.Est-ce que ces problèmes/particularités ont entraîné une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacl2',
                text="L2.Est-ce qu'il/elle souffre des problèmes de compulsions ou d'obsessions ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacl4',
                text="L4.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacm1',
                text="M1.Est-ce qu'il/elle a suivi un régime tel que cela a entraîné une perte de poids ou l'absence de prise de poids ou qu'il est resté au même poids pendant un certain temps ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacm10',
                text="M10.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacm2',
                text="M2.Est-ce qu'il/elle a fait de l'exercice de manière exagérée ou est ce qu'il a porté un intérêt démesuré à son apparence physique ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacm3',
                text="M3.Pour les filles : Est-ce qu'elle a eu un arrêt de menstruations pendant au moins trois mois à la suite d'une perte de poids ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacm4',
                text="M4.Est-ce qu'il/elle a déjà eu des périodes où il/elle était pris de fringales et/ou vomissait régulièrement ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacm5',
                text="M5.Est-ce qu'il/elle a essayé de perdre du poids même s'il/elle était déjà mince ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacm6',
                text="M6.Est-ce qu'il/elle a présenté une anorexie mentale ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacm7',
                text="M7.Est-ce que ces problèmes/particularités ont causé une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacm8',
                text="M8.Est-ce qu'il/elle souffre des problèmes d'alimentation ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacn1',
                text="N1.Est-ce qu'il lui est difficile d'aller à l'école en raison de la crainte d'être séparé de la famille ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacn3',
                text="N3.Est-ce qu'il/elle a des réactions plus fortes que l'ordinaire quand des amitiés ou autres relations proches prennent fin ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacn4',
                text="N4.Est-ce que ces problèmes/particularités ont causé une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacn5',
                text="N5.Est-ce qu'il/elle souffre des problèmes de séparation ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacn7',
                text="N7.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataco1',
                text="O1.Est-ce qu'il/elle perd facilement son sang froid ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataco2',
                text="O2.Est-ce qu'il/elle refuse souvent de suivre les consignes des adultes ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataco4',
                text="O4.Est-ce qu'il/elle traite mal ses proches délibérément ou leur manque de respect ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ataco5',
                text="O5.Est-ce qu'il/elle rejette souvent la faute sur les autres lorsqu'il/elle fait des erreurs ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacop14',
                text="OP14.Est-ce que ces problèmes/particularités ont entraîné une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacop15',
                text="OP15.Est-ce qu'il/elle souffre des problèmes d'opposition ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacop17',
                text="OP17.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacp1',
                text="P1.Est-ce qu'il/elle menace, tracasse ou humilie souvent les autres ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacp10',
                text="P10.Est-ce qu'il/elle a cambriolé la maison, le local ou le véhicule de quelqu'un ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacp2',
                text="P2.Est-ce qu'il/elle est cruel avec les insectes ou les petites bêtes ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacp4',
                text="P4.Est-ce qu'il/elle a déjà déclenché un incendie ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacp5',
                text="P5.Est-ce qu'il/elle a déjà abusé sexuellement de quelqu'un ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacp6',
                text="P6.Est-ce qu'il/elle a déjà été arrêté par la police ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacp7',
                text="P7.Est-ce qu'il s'est servi d'une arme qui peut causer des dégâts physiques sérieux ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacp8',
                text="P8.Est-ce qu'il/elle a jamais volé quelqu'un",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacp9',
                text="P9.Est-ce qu'il/elle a essayé de détruire la propriété de quelqu'un délibérément ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacper',
                text="Personne interrogée ",
                options=[
                    AnswerOption(value='a', label="Mère", score=0),
                    AnswerOption(value='b', label="Père", score=1),
                    AnswerOption(value='c', label="Tuteur", score=2),
                    AnswerOption(value='d', label="Apparenté", score=3),
                    AnswerOption(value='e', label="Autre", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacq1',
                text="Q1.Est-ce qu'il/elle est extrêmement timide ou silencieux ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacq2',
                text="Q2.Est-ce qu'il totalement silencieux ou presque dans des situations où on n'est pas supposé l'être ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacq4',
                text="Q4.Est-ce que ces problèmes/particularités ont causé une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacq5',
                text="Q5.Est-ce qu'il/elle souffre des problèmes d'anxiété ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacq7',
                text="Q7.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacr10',
                text="R10.Est-ce qu'il/elle souffre des problèmes d'humeur ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacr12',
                text="R12.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacr2',
                text="R2.Est-ce qu'il/elle se plaint souvent de solitude ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacr3',
                text="R3.Est-ce qu'il/elle exprime souvent un sentiment d'infériorité ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacr5',
                text="R5.Est-ce qu'il/elle a eu des idées ou parlé de se suicider ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacr6',
                text="R6.Est-ce qu'il/elle a déjà tenté de se suicider ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacr7',
                text="R7.Est-ce qu'il/elle a souvent une impression de vide ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacr8',
                text="R8.Est ce qu'il/elle a l'idée que ses talents ne sont pas reconnus à leur juste valeur ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacr9',
                text="R9.Est-ce que ces problèmes/particularités ont entraîné une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacs2',
                text="S2.Est-ce qu'il/elle a déjà entendu des voix ou des sons que personne d'autre ne pouvait entendre ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacs3',
                text="S3.Est-ce que ces problèmes/particularités ont entraîné une altération significative de son fonctionnement à l'école, avec ses copains ou à la maison ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacs4',
                text="S4.Est-ce qu'il/elle souffre des problèmes de notion de réalité ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, à un certain degré", score=1),
                    AnswerOption(value='c', label="Non", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atacs6',
                text="S6.Est-ce qu'ils sont toujours présents ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_ATAC",
            name="AUT_ATAC Questionnaire",
            description="225 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=112,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_ATAC score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
