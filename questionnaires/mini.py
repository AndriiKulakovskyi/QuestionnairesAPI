"""
MINI - MINI Questionnaire
=========================

137 items questionnaire

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


@register_questionnaire("MINI")
@dataclass
class Mini(BaseQuestionnaire):
    """MINI Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize MINI questionnaire with all 137 items."""
        
        questions_list = [
            Question(
                id='epi_mania_iso',
                text="Episode maniaque isolé",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia3ads',
                text="2 dernières semaines",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia3aep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia3bds',
                text="2 dernières semaines",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia3bep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia3cds',
                text="2 dernières semaines",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia3cep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia3dep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia3dsd',
                text="2 dernières semaines",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia3eeac',
                text="Episode actuel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia3eep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia3eepbis',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia3esd',
                text="2 dernières semaines",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia3fep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia3fsd',
                text="2 dernières semaines",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia3gep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia3gsd',
                text="2 dernières semaines",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia4ep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia4sd',
                text="2 dernières semaines",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minia5bis',
                text="Y A-T-IL AU MOINS 5 OUI ENTRE A1 ET A3 ET A4 EST-ELLE COTEE OUI POUR CETTE PERIODE ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minib1',
                text="B1 Avez-vous eu un accident ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minib10',
                text="B10 Avez-vous tenté de vous suicider ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minib10bis',
                text="&nbsp;",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minib11',
                text="B11 Avez-vous déjà fait une tentative de suicide ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minib2',
                text="B2 Vous est-il arrivé de vous sentir désespéré ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minib4',
                text="B4 Avez-vous eu envie de vous faire du mal ou de vous blesser ou avez-vous eu en tête des images où vous vous faisiez du mal ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minib5',
                text="B5 Avez-vous pensé à vous suicider ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minib5bis1',
                text="Fréquence",
                options=[
                    AnswerOption(value='a', label="Occasionnellement", score=0),
                    AnswerOption(value='b', label="Souvent", score=1),
                    AnswerOption(value='c', label="Très souvent", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minib5bis2',
                text="Intensité",
                options=[
                    AnswerOption(value='a', label="Légère", score=0),
                    AnswerOption(value='b', label="Modérée", score=1),
                    AnswerOption(value='c', label="Sévère", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minib5bis3',
                text="Pouvez-vous dire qu’en ce qui concerne ces impulsions,vous n’allez pas passer à l’acte durant ce programme thérapeutique ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minib7',
                text="B7 Avez-vous planifié un suicide ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minib8',
                text="B8 Avez-vous commencé à agir pour vous préparer à vous blesser ou à faire une tentative de suicide dans laquelle vous vous attendiez à mourir ou en aviez l’intention ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minib_risque_cot',
                text="RISQUE SUICIDAIRE ACTUEL",
                options=[
                    AnswerOption(value='a', label="Faible", score=0),
                    AnswerOption(value='b', label="Modéré", score=1),
                    AnswerOption(value='c', label="Élevé", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic0',
                text="Avez-vous dans votre famille des antécédents de maladie maniaco-dépressive ou de trouble bipolaire ou avez-vous un membre de votre famille qui a eu une instabilité de l’humeur traitée avec un médicament comme le lithium, le divalproate de sodium ou la lamotrigine ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic2a',
                text="C2 a Avez-vous déjà eu une période de plusieurs jours où vous étiez tellement irritable que vous en arriviez à insulter les gens, à hurler, voire à vous battre avec des personnes extérieures à votre famille? Aviez-vous vous-même remarqué ou les autres, avaient-ils remarqué que vous étiez plus irritable ou que vous réagissiez plus vivement que les autres, même dans des situations où vous trouviez cela justifié ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic2b',
                text="b Vous sentez-vous excessivement irritable en ce moment ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3aea',
                text="Episode actuel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3aeac',
                text="Episode actuel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3aep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3aepbis',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3bea',
                text="Episode actuel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3bep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3cea',
                text="Episode actuel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3cep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3dea',
                text="Episode actuel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3dep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3eea',
                text="Episode actuel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3eep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3fea',
                text="Episode actuel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3fep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3gea',
                text="Episode actuel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3gep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3recapea',
                text="Episode actuel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic3recupep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic5ea',
                text="Episode actuel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic5ep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic6ea',
                text="Episode actuel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minic6ep',
                text="Episode passé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minid2',
                text="D2 Certaines de ces crises, même il y a longtemps, ont-elles été imprévisibles, ou sont-elles survenues sans que rien ne les provoque ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minid4tropanact',
                text="TROUBLE PANIQUE ACTUEL",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minid5',
                text="D5 TROUBLE PANIQUE VIE ENTIERE",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minid6',
                text="D6 SYMPTÖMES ANXIEUX PAROXYSTIQUES LIMITES VIE ENTIERE",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minieagasatp',
                text="AGORAPHOBIE ACTUELLE sans antécédents de Trouble panique",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='miniedm',
                text="EPISODE DEPRESSIF MAJEUR",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minief5',
                text="Craignez-vous ou évitez-vous 4 situations sociales ou plus ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minietrpanagroa',
                text="TROUBLE PANIQUE avec Agoraphobie ACTUEL",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minietrpansaga',
                text="TROUBLE PANIQUE sans Agoraphobie ACTUEL",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minif2',
                text="F2 Pensez-vous que cette peur est excessive ou déraisonnable et est-elle la cause d’une anxiété quasiment permanente chez vous ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minif3',
                text="F3 Redoutez-vous tellement ces situations qu’en pratique vous les évitez ou êtes-vous extrêmement mal à l’aise lorsque vous devez les affronter ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minif4',
                text="F4 Cette peur entraîne t’elle chez vous une certaine souffrance ou vous gêne-t-elle de manière significative dans votre travail à l’école ou dans vos relations avec les autres ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minig2',
                text="G2 Avez-vous essayé, mais sans succès, de résister à certaines de ces idées, de les ignorer ou de vous en débarrasser ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minig3',
                text="G3 Pensez-vous que ces idées qui reviennent sans cesse sont le produit de votre propre pensée et qu’elles ne vous sont pas imposées de l’extérieur ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minig4',
                text="G4 Au cours du mois écoulé, avez-vous souvent éprouvé le besoin de faire certaines choses sans cesse, sans pouvoir vous en empêcher, comme vous laver les mains, compter,vérifier les choses, ranger, collectionner ou accomplir des rituels religieux ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minig5',
                text=" G5 Avez-vous, à un moment donné, réalisé que ces idées envahissantes et/ou ces comportements répétitifs étaient irrationnels ou hors de proportion ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minigtruobscomact',
                text="TROUBLE OBSESSIONNEL COMPULSIF ACTUEL",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minih1',
                text="H1 Avez-vous déjà vécu, ou été le témoin de ou eu à faire face à un évènement extrêmement traumatique, au cours duquel des personnes sont mortes ou vous-mêmes et/ou d’autres personnes physique ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minih2',
                text="H2 Avez-vous réagi avec un sentiment de peur intense, d’impuissance ou d’horreur ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minih6',
                text="H6 Au cours du mois écoulé, ces problèmes vous ont-ils causé une certaine souffrance ou vous ont-ils gênés dans votre travail/à l’école, dans vos activités quotidiennes ou dans vos relations avec les autres ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minihstress',
                text="ETAT DE STRESS POST-TRAUMATIQUE ACTUEL",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minii1',
                text="I1 Au cours des 12 derniers mois, vous est-il arrivé à au moins trois reprises de boire,en moins de trois heures, plus de trois verres d’alcool ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minii2a',
                text="a Aviez-vous besoin de plus grandes quantités d’alcool pour obtenir le même effet que quand vous avez commencé à boire ou la même quantité d’alcool vous faisait-elle moins d’effet ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minii2c',
                text="c Lorsque vous buviez, vous arrivait-il souvent de boire plus que vous n’en aviez l’intention au départ ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minii2d',
                text="d Avez-vous essayé, sans pouvoir y arriver, de réduire votre consommation ou de ne plus boire ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minii2e',
                text="e Les jours où vous buviez, passiez-vous beaucoup de temps à vous procurer de l’alcool, à boire ou à vous remettre des effets de l’alcool ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minii2g',
                text="g Avez-vous continué à boire tout en sachant que cela entraînait chez vous des problèmes de santé ou des problèmes psychologiques ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minii3a',
                text="a Avez-vous été plus d’une fois, grisé ou avec la « gueule de bois » alors que vous aviez des choses à faire au travail/à l’école ou à la maison ? Cela a t-il posé des problèmes ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minii3b',
                text="b Vous est-il arrivé d’être plus fois sous l’effet de l’alcool dans une situation où cela était physiquement risqué comme conduire, utiliser une machine ou un instrument dangereux,faire du bateau, etc.… ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minii3c',
                text="c Avez-vous eu plus d’une fois des problèmes légaux parce que vous aviez bu, par exemple une interpellation ou une condamnation ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minii3d',
                text="d Avez-vous continué à boire tout en sachant que cela entraînait des problèmes avec votre famille ou d’autres personnes ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='miniiabalcac',
                text="ABUS D’ALCOOL ACTUEL",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='miniidepalcact',
                text="DÉPENDANCE ALCOOLIQUE ACTUELLE",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minij1a',
                text="J1 a Au cours des 12 derniers mois, vous est-il arrivé à plus d’une occasion de prendre l’un de ces produits dans le but de planer, de changer votre humeur ou de vous « défoncer » ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minijmedoc',
                text="Prenez-vous des médicaments contre la toux ou d’autres substances ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minijprodcons',
                text="COCHER CHAQUE PRODUIT CONSOMMÉ :",
                options=[
                    AnswerOption(value='0', label="1", score=0),
                    AnswerOption(value='1', label="2", score=1),
                    AnswerOption(value='2', label="3", score=2),
                    AnswerOption(value='3', label="4", score=3),
                    AnswerOption(value='4', label="5", score=4),
                    AnswerOption(value='5', label="6", score=5),
                    AnswerOption(value='6', label="7", score=6),
                    AnswerOption(value='7', label="8", score=7),
                    AnswerOption(value='8', label="9", score=8),
                    AnswerOption(value='9', label="10", score=9),
                    AnswerOption(value='10', label="11", score=10),
                    AnswerOption(value='11', label="12", score=11),
                    AnswerOption(value='12', label="13", score=12),
                    AnswerOption(value='13', label="14", score=13),
                    AnswerOption(value='14', label="15", score=14),
                    AnswerOption(value='15', label="16", score=15),
                    AnswerOption(value='16', label="17", score=16),
                    AnswerOption(value='17', label="18", score=17),
                    AnswerOption(value='18', label="19", score=18),
                    AnswerOption(value='19', label="20", score=19),
                    AnswerOption(value='20', label="21", score=20),
                    AnswerOption(value='21', label="22", score=21),
                    AnswerOption(value='22', label="23", score=22),
                    AnswerOption(value='23', label="24", score=23),
                    AnswerOption(value='24', label="25", score=24),
                    AnswerOption(value='25', label="26", score=25),
                    AnswerOption(value='26', label="27", score=26),
                    AnswerOption(value='27', label="28", score=27),
                    AnswerOption(value='28', label="29", score=28),
                    AnswerOption(value='29', label="30", score=29),
                    AnswerOption(value='30', label="31", score=30),
                    AnswerOption(value='31', label="32", score=31),
                    AnswerOption(value='32', label="33", score=32),
                    AnswerOption(value='33', label="34", score=33),
                    AnswerOption(value='34', label="35", score=34),
                    AnswerOption(value='35', label="36", score=35),
                    AnswerOption(value='36', label="37", score=36),
                    AnswerOption(value='37', label="38", score=37),
                    AnswerOption(value='38', label="39", score=38)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minik11b',
                text="TROUBLE DE L’HUMEUR AVEC CARACTERISTIQUES PSYCHOTIQUES VIE ENTIERE",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minik13',
                text="SYNDROME PSYCHOTIQUE ACTUEL",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minik14',
                text="SYNDROME PSYCHOTIQUE VIE ENTIERE",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minik1a',
                text="K1 a   Avez-vous déjà eu l’impression que quelqu’un vous espionnait, ou complotait contre vous, ou bien encore que l’on essayait de vous faire du mal ? NOTE : DEMANDEZ DES EXEMPLES POUR ELIMINER UN HARCELEMENT REEL.",
                options=[
                    AnswerOption(value='a', label="Non", score=0),
                    AnswerOption(value='b', label="Oui", score=1),
                    AnswerOption(value='c', label="Oui bizarre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minik2a',
                text="K2 a      Avez-vous déjà eu l'impression que l'on pouvait lire ou entendre vos pensées ou que vous pouviez lire ou entendre les pensées des autres?",
                options=[
                    AnswerOption(value='a', label="Non", score=0),
                    AnswerOption(value='b', label="Oui", score=1),
                    AnswerOption(value='c', label="Oui bizarre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minik4a',
                text="K4 a Avez-vous déjà eu l’impression que l’on s’adressait directement à vous à travers la télévision ou la radio ou que certaines personnes que vous ne connaissiez pas personnellement s’intéressaient particulièrement à vous ?",
                options=[
                    AnswerOption(value='a', label="Non", score=0),
                    AnswerOption(value='b', label="Oui", score=1),
                    AnswerOption(value='c', label="Oui bizarre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minik5a',
                text="K5 a Vos proches ont-ils déjà jugé certaines de vos idées comme étranges ou hors de la réalité ?\nCOTATEUR : DEMANDEZ DES EXEMPLES. NE COTER OUI QUE SI LE PATIENT PRESENTE CLAIREMENT DES IDEES DELIRANTES HYPOCONDRIAQUES OU DE POSSESSION, DE CULPABILITE,DE JALOUSIE, DE RUINE, DE GRANDEUR, DE DECHEANCE OU D’AUTRES NON-EXPLOREES PAR LES QUESTIONS K1 A K4.",
                options=[
                    AnswerOption(value='a', label="Non", score=0),
                    AnswerOption(value='b', label="Oui", score=1),
                    AnswerOption(value='c', label="Oui bizarre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minik6a',
                text="K6 a     Vous est-il déjà arrivé d’entendre des choses que d’autres personnes ne pouvaient pas entendre, comme des voix ?",
                options=[
                    AnswerOption(value='a', label="Non", score=0),
                    AnswerOption(value='b', label="Oui", score=1),
                    AnswerOption(value='c', label="Oui bizarre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minik6a1',
                text="SI OUI OU HALLUCINATIONS VERBALES:  Ces voix commentaient-elles vos pensées ou vos actes ou entendiez-vous deux ou plusieurs voix parler entre elles ?",
                options=[
                    AnswerOption(value='a', label="Non", score=0),
                    AnswerOption(value='b', label="Oui", score=1),
                    AnswerOption(value='c', label="Oui bizarre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minik6b1',
                text="SI OUI A HALLUCINATIONS VERBALES : Ces voix commentaient-elles vos pensées ou vos actes ou entendiez-vous deux ou plusieurs voix parler entre elles ?",
                options=[
                    AnswerOption(value='a', label="Non", score=0),
                    AnswerOption(value='b', label="Oui", score=1),
                    AnswerOption(value='c', label="Oui bizarre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minik8b',
                text="K8 b ACTUELLEMENT, LE PATIENT PRESENTE T-IL UN DISCOURS CLAIREMENT INCOHERENT OU DESORGANISE, OU UNE PERTE NETTE DES ASSOCIATIONS ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minil2',
                text="L2 Avez-vous essayé de ne pas prendre de poids malgré le fait que vous pesiez peu ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minil4b',
                text="b L’opinion ou l’estime que vous aviez de vous-même étaient-elles largement influencés par votre poids ou vos formes corporelles ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minil4c',
                text="c Pensiez-vous que ce poids était normal, voire excessif ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minilanomenact',
                text="ANOREXIE MENTALE ACTUELLE",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minim1',
                text="M1 Au cours de ces trois derniers mois, vous est-il arrivé d’avoir des crises de boulimie durant lesquelles vous mangiez de très grandes quantités de nourriture dans une période de temps limitée, c’est à dire en moins de 2 heures ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minim2',
                text="M2 Avez-vous eu de telles crises de boulimie au moins deux fois par semaine au cours de ces 3 derniers mois ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minim3',
                text="M3 Durant ces crises de boulimie, aviez-vous l’impression de ne pas pouvoir vous arrêter de manger ou de ne pas pouvoir contrôler la quantité de nourriture que vous preniez ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minim4',
                text="M4 De façon à éviter une prise de poids après ces crises de boulimie, faisiez-vous certaines choses comme vous faire vomir, vous astreindre à des régimes draconiens,faire de l’exercice, des lavements, prendre des laxatifs, des diurétiques, des coupe-faim ou autres ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minim5',
                text="M5 L’opinion ou l’estime que vous avez de vous-même sont-elles largement influencées par votre poids ou vos formes corporelles ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minim6',
                text="M6 LE PATIENT PRÉSENTE-T-IL UNE ANOREXIE MENTALE ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minim7',
                text="M7 Ces crises de boulimie surviennent-elles toujours lorsque votre poids est en dessous de___kg ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minim8',
                text="M8 BOULIMIE ACTUELLE",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minim8bis',
                text="ANOREXIE MENTALE Boulimie/ Type avec vomissements ou prise de purgatifs ACTUELLE",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minin1b',
                text="b Avez-vous ce type de préoccupations presque tous les jours ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minin1c',
                text="EST-CE QUE L’ANXIETE ET LES INQUIETUDES DU PATIENT SONT UNIQUEMENT NON OUI RESTREINTES A, OU MIEUX EXPLIQUEES PAR, UN DES TROUBLES EXPLORES PRECEDEMMENT ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minin2',
                text="N2 Vous-est-il difficile de contrôler ces préoccupations ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minin4',
                text="N4 Cette anxiété et ces inquiétudes entraînent-elles chez vous une souffrance importante ou vous perturbent-elles au travail/ à l’école ou dans vos relations avec les autres ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mininanxgenact',
                text="ANXIÉTÉ GÉNÉRALISÉE ACTUELLE",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minio1a',
                text="O1a Preniez-vous un médicament ou des remèdes quels qu’ils soient ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Incertain", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minio1b',
                text="O1b Aviez-vous une maladie physique quelle qu’elle soit ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Incertain", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minio2',
                text="O2 FINALEMENT : UNE CAUSE ORGANIQUE A-T-ELLE ÉTÉ ÉCARTÉE ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Incertain", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='miniptroperantisoc',
                text="TROUBLE DE LA PERSONNALITÉ ANTISOCIALE VIE ENTIERE",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minitb2_depress',
                text="Dépressif",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='minitb2_hypo',
                text="Hypomaniaque",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tbi',
                text="TROUBLE BIPOLAIRE I",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tbi_caract_psy',
                text="TROUBLE BIPOLAIRE I  avec caractéristique psychotiques",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tbi_epi_rec',
                text="Episode le plus récent",
                options=[
                    AnswerOption(value='a', label="Maniaque", score=0),
                    AnswerOption(value='b', label="Dépressif", score=1),
                    AnswerOption(value='c', label="Mixte", score=2),
                    AnswerOption(value='d', label="Hypomaniaque", score=3),
                    AnswerOption(value='e', label="Non spécifié", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tbii',
                text="TROUBLE BIPOLAIRE II",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tbii_epi_rec',
                text="Episode le plus récent",
                options=[
                    AnswerOption(value='a', label="Hypomaniaque", score=0),
                    AnswerOption(value='b', label="Dépressif", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tbns',
                text="TROUBLE BIPOLAIRE NON SPECIFIE",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdm',
                text="TROUBLE DEPRESSIF MAJEUR ",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdm_caract_psy',
                text="TROUBLE DEPRESSIF MAJEUR avec caractéristique psychotiques",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="MINI",
            name="MINI Questionnaire",
            description="137 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=68,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute MINI score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
