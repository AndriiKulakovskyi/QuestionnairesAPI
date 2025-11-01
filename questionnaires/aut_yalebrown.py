"""
AUT_YALEBROWN - AUT_YALEBROWN Questionnaire
===========================================

157 items questionnaire

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


@register_questionnaire("AUT_YALEBROWN")
@dataclass
class AutYalebrown(BaseQuestionnaire):
    """AUT_YALEBROWN Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_YALEBROWN questionnaire with all 157 items."""
        
        questions_list = [
            Question(
                id='intesy1',
                text="Combien de temps durent les pensées obsédantes ?",
                options=[
                    AnswerOption(value='a', label="Nulle", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='intesy10',
                text="Quelle  est  l'intensité  de  la  pulsion  qui  vous  oblige  à ritualiser ? Quel contrôle pouvez-vous exercer sur les rituels ? ",
                options=[
                    AnswerOption(value='a', label="Contrôle total", score=0),
                    AnswerOption(value='b', label="Beaucoup  de  contrôle.  Ressent  une  certaine  obligation  à accomplir   les   rituels,   mais   peut   généralement   exercer   un contrôle volontaire sur cette pression", score=1),
                    AnswerOption(value='c', label="Contrôle  moyen,  forte obligation  à accomplir des  rituels. Peut la contrôler, mais avec difficulté", score=2),
                    AnswerOption(value='d', label="Peu  de  contrôle.  Très  forte  obligation  à  accomplir  des rituels. Doit aller jusqu'au bout de  l'activité ritualisée, ne peut différer qu'avec difficulté", score=3),
                    AnswerOption(value='e', label="Aucun  contrôle,  l'obligation  à  accomplir  les   rituels  est vécue comme complètement involontaire et irrésistible, ne peut que rarement différer même momentanément l'activité", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='intesy2',
                text="Dans quelle mesure vos pensées obsédantes vous gênent-elles dans votre vie sociale ou professionnelle ? Y a t il des choses qu'il vous est impossible de faire à cause de ces pensées obsédantes ",
                options=[
                    AnswerOption(value='a', label="Nulle", score=0),
                    AnswerOption(value='b', label="Légère, 	faible 	gêne 	dans 	les 	activités 	sociales 	ou professionnelles  mais   l'efficacité  globale  du  patient   n'est  pas altérée", score=1),
                    AnswerOption(value='c', label="Moyenne, 	nette 	gêne 	dans 	les 	activités 	sociales 	et professionnelles mais le patient peut encore faire face", score=2),
                    AnswerOption(value='d', label="Importante, cause une altération réelle des activités  sociales et professionnelles du patient", score=3),
                    AnswerOption(value='e', label="Extrêmement importante : gêne invalidante", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='intesy3',
                text="Quel niveau d'angoisse ces pensées obsédantes  créent-elles en vous ?",
                options=[
                    AnswerOption(value='a', label="Nulle", score=0),
                    AnswerOption(value='b', label="Légère, rare et très peu gênante", score=1),
                    AnswerOption(value='c', label="Moyenne, fréquente et gênante, mais que le patient gère encore assez bien", score=2),
                    AnswerOption(value='d', label="Importante, très fréquente et très gênante", score=3),
                    AnswerOption(value='e', label="Extrêmement importante, pratiquement constante et  d'une gêne invalidante", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='intesy4',
                text="Quel  effort  fournissez-vous  pour  résister  aux   pensées obsédantes ? Essayez-vous souvent de détourner votre attention de ces pensées quand elles vous viennent à l'esprit ?",
                options=[
                    AnswerOption(value='a', label="Fait  l'effort  de  toujours  résister,  ou  symptômes  si  minimes qu'ils ne nécessitent pas qu'on leur résiste", score=0),
                    AnswerOption(value='b', label="Essaie de résister la plupart du temps", score=1),
                    AnswerOption(value='c', label="Fait quelque effort pour résister", score=2),
                    AnswerOption(value='d', label=". ède à toutes les obsessions, sans essayer de les contrôler, mais est quelque peu contrarié de ne pouvoir mieux faire", score=3),
                    AnswerOption(value='e', label="Cède volontiers et totalement à toutes les obsessions", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='intesy5',
                text="Quel contrôle exercez-vous sur vos pensées  obsédantes ? Dans quelle mesure arrivez-vous à stopper ou à détourner vos pensées obsédantes ",
                options=[
                    AnswerOption(value='a', label="Contrôle total", score=0),
                    AnswerOption(value='b', label="Beaucoup de contrôle ; généralement capable de  stopper ou de  détourner  les  obsessions  avec   quelques   efforts  et  de  la concentration", score=1),
                    AnswerOption(value='c', label="Contrôle moyen, peut de temps en temps arriver à stopper ou à détourner ses obsessions", score=2),
                    AnswerOption(value='d', label="Peu de contrôle, arrive rarement à stopper ses obsessions, peut seulement détourner son attention avec difficulté", score=3),
                    AnswerOption(value='e', label="Pas  de  contrôle,  semble  totalement  dépourvu  de  volonté, rarement capable de détourner son attention de  ses obsessions, même momentanément", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='intesy6',
                text="Combien  de  temps  passez-vous  à  faire  des   rituels  ? Lorsque ce sont des rituels incluant des activités concernant la vie   de   tous   les   jours   qui   sont   principalement   présents, demandez  :  Combien  de  temps  vous  faut-il  de  plus  qu'à  la majorité des gens pour accomplir les activités quotidiennes, du fait de vos rituels ?",
                options=[
                    AnswerOption(value='a', label="Nulle", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='intesy7',
                text="Dans quelle mesure les rituels vous gênent-ils dans votre vie sociale ou professionnelle ? Y a t il des  choses qu'il vous est impossible de faire à cause de vos rituels ?",
                options=[
                    AnswerOption(value='a', label="Nulle", score=0),
                    AnswerOption(value='b', label="Légère, faible gêne dans les activités sociales ou professionnelles,  mais  l'efficacité  globale  du  patient  n'est  pas altérée", score=1),
                    AnswerOption(value='c', label="Moyenne,    nette    gêne    dans    les    activités    sociales    ou professionnelles, mais le patient peut faire face", score=2),
                    AnswerOption(value='d', label="Importante, cause une altération réelle des activités sociales ou professionnelles du patient", score=3),
                    AnswerOption(value='e', label="Extrêmement importante, gêne invalidante", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='intesy9',
                text="Quel 	effort 	fournissez-vous    pour    résister     aux compulsions ?",
                options=[
                    AnswerOption(value='a', label="Fait  l'effort  de  toujours  résister,  ou  symptômes  si  minimes qu'ils ne nécessitent pas qu'on leur résiste", score=0),
                    AnswerOption(value='b', label="Essaie de résister la plupart du temps", score=1),
                    AnswerOption(value='c', label="Fait quelque effort pour résister", score=2),
                    AnswerOption(value='d', label=". ède à toutes les obsessions, sans essayer de les contrôler, mais est quelque peu contrarié de ne pouvoir mieux faire", score=3),
                    AnswerOption(value='e', label="Cède volontiers et totalement à toutes les obsessions", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbnf',
                text="ECHELLE LE D'OBSESSION-COMPULSION DE YALE-BROWN",
                options=[
                    AnswerOption(value='a', label="Fait", score=0),
                    AnswerOption(value='b', label="Non fait", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa1',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa10',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa11',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa12',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa13',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa14',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa15',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa16',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa17',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa18',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa19',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa2',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa20',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa21',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa22',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa23',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa24',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa25',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa26',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa27',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa28',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa29',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa3',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa30',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa31',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa32',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa33',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa34',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa35',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa36',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa37',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa38',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa39',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa4',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa40',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa41',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa42',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa43',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa44',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa45',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa46',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa47',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa48',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa49',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa5',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa50',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa51',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa52',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa53',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa54',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa55',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa56',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa57',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa58',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa59',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa6',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa60',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa61',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa62',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa63',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa64',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa65',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa66',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa67',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa68',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa69',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa7',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa70',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa71',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa72',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa73',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa8',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpa9',
                text="Passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr1',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr10',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr11',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr12',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr13',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr14',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr15',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr16',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr17',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr18',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr19',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr2',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr20',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr21',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr22',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr23',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr24',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr25',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr26',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr27',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr28',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr29',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr3',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr30',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr31',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr32',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr33',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr34',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr35',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr36',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr37',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr38',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr39',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr4',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr40',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr41',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr42',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr43',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr44',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr45',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr46',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr47',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr48',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr49',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr5',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr50',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr51',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr52',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr53',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr54',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr55',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr56',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr57',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr58',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr59',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr6',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr60',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr61',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr62',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr63',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr64',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr65',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr66',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr67',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr68',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr69',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr7',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr70',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr71',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr72',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr73',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr8',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalbpr9',
                text="Présent",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NS", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='yalchang',
                text="Changement depuis la dernière visite",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_YALEBROWN",
            name="AUT_YALEBROWN Questionnaire",
            description="157 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=78,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_YALEBROWN score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
