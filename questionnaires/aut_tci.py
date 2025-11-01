"""
AUT_TCI - AUT_TCI Questionnaire
===============================

100 items questionnaire

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


@register_questionnaire("AUT_TCI")
@dataclass
class AutTci(BaseQuestionnaire):
    """AUT_TCI Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_TCI questionnaire with all 100 items."""
        
        questions_list = [
            Question(
                id='tci1',
                text="1.J’essaie souvent des choses nouvelles uniquement pour le plaisir ou pour avoir des sensations fortes, même si les autres estiment que c’est une perte de temps",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci10',
                text="10.Je fais souvent les choses selon mon impression du moment sans tenir compte des méthodes habituelles",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci100',
                text="100.J'ai encore de bonnes habitudes à acquérir pour réussir à résister aux tentations",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci101',
                text="101.Je souhaiterais que les autres parlent moins qu'ils ne le font",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci102',
                text="102.Chacun devrait être traité avec respect et dignité, même les gens qui semblent sans importance ou mauvais",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci103',
                text="103.J'aime prendre des décisions rapidement afin de poursuivre mes activités",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci105',
                text="105.J'aime explorer de nouvelles méthodes pour faire les choses",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci106',
                text="106.J'aime mettre de l'argent de côté plutôt que le dépenser pour des divertissements ou des sensations fortes",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci108',
                text="108.J'ai eu des moments de grand bonheur au cours desquels j'ai eu soudainement la sensation claire et profonde d'une communauté avec tout ce qui existe",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci109',
                text="109.La plupart des gens semblent être plus efficaces que moi",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci11',
                text="11.Je fais habituellement les choses à ma façon plutôt qu'en fonction des souhaits des autres",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci110',
                text="110.J'ai souvent la sensation de faire partie de la force spirituelle dont toute la vie dépend",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci111',
                text="111.Même avec des amis, je préfère ne pas trop me confier",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci112',
                text="112.Je pense que mon comportement naturel est en général en accord avec mes principes et mes objectifs de vie",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci113',
                text="113.Je crois que toute vie dépend d'un certain ordre ou pouvoir spirituel qui ne peut pas être complètement expliqué",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci114',
                text="114.Souvent quand je regarde certaines choses de la vie courante, j'ai une sensation d’émerveillement comme si je les voyais d’un œil nouveau pour la première fois",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci116',
                text="116.Je me pousse souvent jusqu'à l'épuisement ou j'essaie de faire plus que je ne le peux réellement",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci117',
                text="117.Ma volonté est trop faible pour résister aux tentations très fortes, même si je sais que je souffrirai de leurs conséquences",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci118',
                text="118.Je déteste voir n'importe qui souffrir",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci12',
                text="12.Généralement, je n'aime pas les gens qui ont des idées différentes des miennes",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci120',
                text="120.Je souhaiterais être la personne la plus belle",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci121',
                text="121.J'aime l'éclosion des fleurs au printemps autant que de revoir un vieil ami",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci122',
                text="122.Habituellement, je considère une situation difficile comme un défi ou une bonne occasion",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci123',
                text="123.Les gens qui travaillent avec moi doivent apprendre à faire les choses selon mes méthodes",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci125',
                text="125.Lorsque rien de nouveau ne se passe, je recherche en général quelque chose de passionnant ou d'excitant à faire",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci15',
                text="15.J'aime discuter de mes expériences et de mes sentiments ouvertement avec des amis plutôt que de les garder pour moi-même.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci16',
                text="16.J'ai moins d'énergie et je me fatigue plus vite que la plupart des gens",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci17',
                text="17.Je me sens rarement libre de mes choix",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci18',
                text="18.Je prends souvent en compte les sentiments des autres autant que mes propres sentiments",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci19',
                text="19.J'évite souvent de rencontrer des inconnus parce que je manque de confiance face aux gens que je ne connais pas",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci2',
                text="2.J’ai habituellement confiance dans le fait que tout ira bien, même dans des situations qui inquiètent la plupart des gens",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci20',
                text="20.J'aime faire plaisir aux autres autant que je le peux",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci21',
                text="21.J'ai souvent le désire d'être la personne la plus intelligente",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci22',
                text="22.Ma détermination me permet habituellement de poursuivre une tâche longtemps après que les autres ont abandonné",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci23',
                text="23.J'attends souvent des autres qu'ils trouvent une solution à mes problèmes",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci24',
                text="24.Je dépense souvent de l'argent au point de ne plus en avoir ou de m'endetter à force de vivre à crédit",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci25',
                text="25.J'ai souvent des éclairs inattendus d'intuition ou de compréhension quand je me détends",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci26',
                text="26.Je ne me soucie pas tellement du fait que les autres m'aiment ou qu'ils approuvent ma manière de faire",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci27',
                text="27.Habituellement je pense d'abord à mon propre intérêt car de toute façon il n'est pas possible de satisfaire tout le monde",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci28',
                text="28.Je n'ai pas de patience avec les gens qui n'acceptent pas mes points de vue",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci29',
                text="29.Parfois je me sens tellement en accord avec la nature que tout me semble faire partie d'un même organisme vivant",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci3',
                text="3.J'ai souvent l'impression d'être victime des circonstances",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci30',
                text="30.Quand je dois rencontrer un groupe d'inconnus, je suis plus timide que la plupart des gens",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci32',
                text="32.On dirait que j'ai un 'sixième sens' qui me permet parfois de savoir ce qu’il va se passer",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci33',
                text="33.Quand quelqu'un m'a fait du mal, j'essaie en général de me venger",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci34',
                text="34.Mes opinions sont en grande partie influencées par des éléments que je ne contrôle pas",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci36',
                text="36.Je préfère réfléchir longtemps avant de prendre une décision",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci39',
                text="39.Je ne pense pas que ce soit une bonne idée d'aider les gens faibles qui ne peuvent pas s'aider eux-mêmes",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci4',
                text="4.Habituellement j'accepte les autres tels qu'ils sont, même s'ils sont très différents de moi",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci40',
                text="40.Je n'ai pas la conscience tranquille si je traite d'autres gens de manière injuste, même s'ils n'ont pas été justes avec moi",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci41',
                text="41.Les gens me confient habituellement leurs sentiments",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci42',
                text="42.J'ai parfois eu l'impression d'appartenir à quelque chose sans limite sans le temps et dans l'espace",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci43',
                text="43.Je ressens parfois un contact spirituel avec d'autres personnes que je ne peux pas exprimer avec des mots",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci44',
                text="44.J'apprécie que les gens puissent faire ce qu'ils veulent sans règles ni contraintes strictes",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci47',
                text="47.D’habitude, j'examine tous les détails d’un problème avant de prendre une décision",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci48',
                text="48.Il m'arrive souvent de souhaiter avoir des pouvoirs spéciaux comme Superman",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci49',
                text="49.Les autres me contrôlent trop",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci5',
                text="5.Je prends plaisir à me venger des gens qui m'ont fait du mal",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci50',
                text="50.J'aime partager ce que j'ai appris avec les autres",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci51',
                text="51.Je suis souvent capable de convaincre les autres, même de choses que je sais exagérées ou fausses",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci52',
                text="52.Parfois, j'ai eu l'impression que ma vie était dirigée par une force spirituelle supérieure à tout être humain",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci53',
                text="53.J'ai la réputation d'être quelqu'un de très réaliste qui n'agit pas sous le coup des émotions",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci55',
                text="55.Je me pousse habituellement plus durement que la plupart des gens parce que je veux faire du mieux possible",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci56',
                text="56.J'ai tellement de défauts que je ne m'aime pas beaucoup",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci57',
                text="57.Je manque de temps pour rechercher des solutions durables à mes problèmes",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci58',
                text="58.Souvent je n'arrive pas à affronter certains problèmes car je n'ai aucune idée sur la manière de m'y prendre",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci59',
                text="59.Je préfère dépenser de l'argent plutôt que de le mettre de côté",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci6',
                text="6.J'ai souvent l'impression que ma vie n'a pas de but ou manque de sens",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci60',
                text="60.Je parviens souvent à déformer la réalité afin de raconter une histoire plus drôle ou de faire une farce à quelqu'un",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci63',
                text="63.En général, il me faut de très bonnes raisons pratiques pour accepter de modifier mes habitudes",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci65',
                text="65.Je trouve les chansons et les films tristes plutôt ennuyeux",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci66',
                text="66.Les circonstances m'obligent souvent à faire des choses malgré moi",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci67',
                text="67.Lorsque quelqu'un me blesse, je préfère rester aimable plutôt que me venger",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci69',
                text="69.Je ne pense pas avoir réellement un but dans la vie",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci7',
                text="7.J'aime aider les autres à résoudre leurs problèmes",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci71',
                text="71.J'obéis souvent à mon instinct ou à mon intuition, sans réfléchir à tous les détails de la situation",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci73',
                text="73.Je me sens souvent en forte communion spirituelle ou émotionnelle avec les gens qui m'entourent",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci74',
                text="74J'essaie souvent de m'imaginer à la place des autres afin de vraiment les comprendre",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci75',
                text="75.Les principes tels que la justice et l'honnêteté jouent peu de rôle dans ma vie",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci76',
                text="76.Je suis plus efficace que la plupart des gens pour mettre de l'argent de côté",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci77',
                text="77.Même si les autres pensent que ce n'est pas important, j'insiste souvent pour que les choses soient faites de manière précise et ordonnée",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci79',
                text="79.Mes amis trouvent qu'il est difficile de connaître mes sentiments car je leur confie rarement mes pensées intimes",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci8',
                text="8.J'en aurais probablement les capacités, mais je ne vois pas l'intérêt de faire plus que le strict minimum",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci80',
                text="80.J'aime imaginer que mes ennemis souffrent",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci81',
                text="81.J'ai plus d'énergie et me fatigue moins vite que la plupart des gens",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci82',
                text="82.L'inquiétude me pousse souvent à interrompre mes activités, même si mes amis me disent que tout ira bien",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci84',
                text="84.Les membres d'une équipe sont rarement récompensés de manière équitable",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci85',
                text="85.Je ne sors pas de ma route pour faire plaisir aux autres",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci86',
                text="86.Je ne suis pas du tout timide avec des inconnus",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci87',
                text="87.Je passe la plupart de mon temps à faire des choses qui semblent nécessaires mais qui ne sont pas en fait réellement importantes pour moi",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci88',
                text="88.Je ne pense pas que les principes religieux ou moraux concernant le bien et le mal doivent avoir beaucoup d'influence sur les décisions d'affaires",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci89',
                text="89.J'essaie souvent de mettre mes propres jugements de côté afin de mieux comprendre ce que les autres vivent",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci90',
                text="90.Beaucoup de mes habitudes m'empêchent d'obtenir de bons résultats",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci92',
                text="92.Je préfère attendre que quelqu'un d'autre décide de ce qui doit être fait",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci93',
                text="93.En général, je respecte les opinions des autres",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci94',
                text="94.Mon comportement m'est dicté par certains objectifs que je me suis fixés dans la vie",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci95',
                text="95.En général, il est absurde de contribuer au succès des autres",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci97',
                text="97.J'ai plus tendance à pleurer devant un film triste que la plupart des gens",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci98',
                text="98.Je me rétablis plus rapidement que la plupart des gens de légers problèmes de santé ou de situations stressantes",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tci99',
                text="99.J'enfreins souvent les lois et les règlements lorsque je pense ne pas risquer de sanction",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_TCI",
            name="AUT_TCI Questionnaire",
            description="100 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=50,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_TCI score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
