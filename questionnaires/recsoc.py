"""
RECSOC - RECSOC Questionnaire
=============================

60 items questionnaire

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


@register_questionnaire("RECSOC")
@dataclass
class Recsoc(BaseQuestionnaire):
    """RECSOC Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize RECSOC questionnaire with all 60 items."""
        
        questions_list = [
            Question(
                id='srsa1',
                text="\n                      1.Je suis beaucoup plus mal à l'aise dans les situations sociales que quand je suis seul(e).\n                    ",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa10',
                text="10.J'interprète les choses de manière trop littérale et, de ce fait, j'interprète mal le sens réel de certaines conversations.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa11',
                text="11.J'ai confiance en moi.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa12',
                text="12.Je suis capable de communiquer mes sentiments aux autres.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa15',
                text="15.Quand les gens changent de ton ou d'expression faciale, généralement je le remarque et le comprends.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa16',
                text="16.J'évite le contact visuel ou on me dit que j'ai un contact visuel étrange. ",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa17',
                text="17.Je reconnais lorsque quelque chose est injuste.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa18',
                text="18.J'ai des difficultés à me faire des amis, même quand j'essaie de faire de mon mieux pour y parvenir.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa19',
                text="19.Je ressens de la frustration quand je tente de transmettre mes idées au cours d'une conversation.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa2',
                text="2. Mes expressions faciales ne correspondent pas à ce que je ressens vraiment. \n                    ",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa20',
                text="20.J'ai des intérêts sensoriels que les autres trouvent inhabituels (par exemple, sentir ou regarder les choses d'une façon particulière). ",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa21',
                text="21.Je suis capable d'imiter les actions et attitudes des autres quand il est socialement approprié de le faire.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa22',
                text="22.J'interagis de manière appropriée avec d'autres adultes. ",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa23',
                text="23.Je ne me joins pas aux activités de groupe ou aux évènements sociaux sauf si je suis fortement incité(e) à le faire. ",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa24',
                text="24.J'ai plus de difficultés que les autres lorsque des changements affectent ma routine.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa25',
                text="25.Cela m'est égal de ne pas être « en phase » ou « sur la même longueur d'onde » que les autres.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa26',
                text="26.J'apporte du réconfort aux autres quand ils sont tristes.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa27',
                text="27.J'évite d'initier des interactions sociales avec d'autres adultes.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa28',
                text="28.Je pense à la même chose ou parle de la même chose de manière répétitive.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa29',
                text="29.Je suis considéré(e) par les autres comme étrange ou bizarre.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa3',
                text="\n                      3.J'ai confiance en moi quand j'interagis avec les autres.\n                    ",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa30',
                text="30.Je suis troublé(e) dans les situations où il se passe beaucoup de choses en même temps.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa31',
                text="31.Je ne peux pas m'arrêter de penser à quelque chose une fois que j'ai commencé à y penser.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa32',
                text="32.J'ai une bonne hygiène personnelle.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa33',
                text="33.Je suis maladroit(e) dans mes interactions sociales, même quand j'essaie d'être poli(e).",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa34',
                text="34.J'évite les gens qui veulent se rapprocher de moi sur le plan affectif.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa35',
                text="35.J'ai du mal à suivre le rythme d'une conversation normale.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa36',
                text="36.J'ai des difficultés à nouer des relations avec les membres de ma famille.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa37',
                text="37.J'''ai des difficultés à nouer des relations avec d'autres adultes en dehors de ma famille.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa38',
                text="38.Je réponds de manière appropriée aux changements d'humeur des autres (par exemple, quand l'humeur d'un ami passe de la gaieté à la tristesse).",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa39',
                text="39.Les gens pensent que je m'intéresse à un nombre limité de sujets ou que je suis trop investi (e) dans ces sujets.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa4',
                text="\n                      4.Quand je suis stressé(e), je présente des formes de comportements rigides qui paraissent étranges aux autres. \n                    ",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa40',
                text="40.J'ai de l'imagination.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa41',
                text="41.Je passe parfois d'une activité à une autre sans but précis.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa42',
                text="42.Je suis extrêmement sensible à certains sons, textures ou odeurs.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa43',
                text="43.J'aime bavarder (ou avoir des conversations informelles avec les autres).",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa44',
                text="44.J'ai plus de difficultés que la plupart des personnes à comprendre les liens de cause à effet (autrement dit, à comprendre comment les évènements sont liés les uns aux autres). ",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa45',
                text="45.Je m'intéresse généralement à ce que les personnes autour de moi sont en train de regarder ou d'écouter. ",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa46',
                text="46.Les autres ont l'impression que j'ai des expressions du visage trop sérieuses.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa47',
                text="47.Je ris parfois de manière inappropriée.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa48',
                text="48.J'ai le sens de l'humour et comprends les plaisanteries. ",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa49',
                text="49.Je réalise extrêmement bien certains types de tâches intellectuelles ou informatiques mais je ne réussis pas aussi bien la plupart des autres tâches. ",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa5',
                text="\n                      5.Je ne détecte pas quand les autres essayent de se servir de moi. \n                    ",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa50',
                text="50.J'ai des comportements répétitifs que les autres trouvent étranges.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa51',
                text="51.J'ai des difficultés à répondre aux questions directement, et je finis par tourner autour du sujet",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa52',
                text="52.Il m'arrive de faire beaucoup de bruit sans m'en rendre compte.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa53',
                text="53.J'ai tendance à parler avec une voix monocorde (c'est-à-dire avec moins de modulation dans ma voix que la plupart des gens). ",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa54',
                text="54.J'ai tendance à considérer les personnes de la même façon que je considère les objets.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa55',
                text="55.Je suis trop proche physiquement des gens ou envahis leur espace personnel sans m'en rendre compte.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa56',
                text="56.Il m'arrive de faire l'erreur de marcher entre deux personnes qui sont en train de se parler.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa57',
                text="57.J'ai tendance à m'isoler.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa58',
                text="58.Je me concentre trop sur certaines parties des objets ou d'un sujet au lieu de les percevoir dans leur globalité.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa59',
                text="59.Je suis plus méfiant(e) que la plupart des gens.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa60',
                text="60.Les autres pensent que je suis émotionnellement distant(e) et que je ne montre pas mes émotions.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa61',
                text="61.J'ai tendance à manquer de souplesse. ",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa62',
                text="62.Quand j'explique aux autres les raisons de mes actions, ils les jugent étranges ou illogiques.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa63',
                text="63.J'ai une manière inhabituelle de saluer les autres personnes",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa64',
                text="64.Je suis bien plus tendu(e) dans les situations sociales que quand je suis seul(e).",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa65',
                text="65.Il m'arrive de regarder fixement ou d'avoir le regard dans le vide.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srsa8',
                text="8.Je me comporte d'une façon pouvant paraître étrange ou bizarre pour les autres.",
                options=[
                    AnswerOption(value='a', label="Faux", score=0),
                    AnswerOption(value='b', label="Parfois VRAI", score=1),
                    AnswerOption(value='c', label="Souvent VRAI", score=2),
                    AnswerOption(value='d', label="Presque toujours VRAI", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="RECSOC",
            name="RECSOC Questionnaire",
            description="60 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=30,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute RECSOC score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
