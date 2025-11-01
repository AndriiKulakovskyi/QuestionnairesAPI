"""
EPHP - EPHP Questionnaire
=========================

13 items questionnaire

Source: Extracted from eschizo application
Applications: eschizo
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


@register_questionnaire("EPHP")
@dataclass
class Ephp(BaseQuestionnaire):
    """EPHP Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize EPHP questionnaire with all 13 items."""
        
        questions_list = [
            Question(
                id='radhtml_ephpa1',
                text="<b>1 Capacité à s'organiser dans une <u>activité habituelle</u> c'est-à-dire qui s'inscrit dans une certaine routine de la vie de la personne</b> (par exemple, faire une course habituelle, préparer un repas, etc.)",
                options=[
                    AnswerOption(value='a', label="0-La difficulté à s'organiser concerne toutes les actions simples de la vie quotidienne.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2-La personne est capable de réaliser des actes quotidiens très simples (faire une course, faire cuire un steak) mais ne s'adapte pas aux changements contextuels banaux (les horaires d'ouverture du magasin, remplacer la poêle habituelle qui n'est pas disponible par une autre) et/ou ne parvient pas à faire deux choses en même temps (faire une autre course en même temps que la première, préparer de la purée servie en même temps que le steak?).", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4-Le sujet est capable de réaliser des activités quotidiennes plus complexes et qui impliquent la possibilité de faire deux choses en même temps, dans la mesure où rien ne vient perturber leur déroulement (par exemple, préparer un repas de telle sorte que chaque plat soit prêt à servir au bon moment et comportant un plat avec son accompagnement et un dessert ou une entrée).", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6-Le sujet est capable de réaliser tous les actes routiniers de la vie quotidienne, y compris lorsqu'ils impliquent de nombreuses séquences successives, même si ce n'est possible qu'au prix d'une stimulation régulière et importante par l'entourage.", score=6),
                    AnswerOption(value='h', label="Non évaluable.", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_ephpa2',
                text="2 Capacité à s'organiser dans une activité inhabituelle c'est-à-dire qui correspond à une situation nouvelle pour la personne. Cet item doit porter sur les capacités que la personne parvient à mettre en oeuvre dans le meilleur des cas dans une situation nouvelle ou inhabituelle, (par exemple, faire un trajet nouveau en voiture ou en transport en commun , réparer ou faire réparer un objet, préparer un repas si elle ne le fait pas habituellement, etc.). Il ne s'agit pas de la capacité à acquérir des compétences nouvelles qui est abordée dans l'item suivant.",
                options=[
                    AnswerOption(value='a', label="0-Aucune situation nouvelle, même simple, ne peut être correctement réalisée.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2-La personne est capable de réaliser des actes non routiniers très simples comme planifier un trajet simple mais inhabituel, changer une pile ou charger la batterie d'un objet nouveau, etc.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4-Le sujet est capable de réaliser des activités non routinières plus complexes.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6-Le sujet est capable d'un très bon niveau de réalisation dans des situations non routinières complexes comme entreprendre un travail de bricolage impliquant l'utilisation de plusieurs outils et de divers matériaux, réaliser un site internet ou organiser un évènement comme une exposition ou un voyage.", score=6),
                    AnswerOption(value='h', label="Non évaluable", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_ephpa3',
                text="<b>3 Capacités d'apprentissage.</b> Globalement, on considère qu'il existe deux grands types d'apprentissage : ceux qui concernent les connaissances générales (acquérir de nouvelles connaissances sur tel ou tel domaine, histoire, art, vie de animaux, code de la route, etc.) et les apprentissages de savoir faire (changer un pneu crevé, savoir faire la cuisine, etc.). Cependant quel que soit le type de capacité d'apprentissage, ces compétences sont importantes pour anticiper le potentiel d'évolution ou d'adaptation à un nouvel environnement. Les deux types d'apprentissage sont ici pris en compte simultanément.",
                options=[
                    AnswerOption(value='a', label="0-La personne ne parvient jamais à acquérir une nouvelle connaissance ou une nouvelle habileté même aussi simple que mettre en route une machine à laver ou savoir faire marcher un micro-onde.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2-La personne est capable d'acquérir de nouvelles connaissances ou capacités mais de manière très lente et limitée et/ou au prix d'une aide intense et durable", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4-Le sujet est capable de capacités d'apprentissage réelles dans certains domaines mais les progrès sont facilement remis en cause et/ou sont plus lents qu'on l'attendrait.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6-Le sujet est capable d'excellentes capacités d'apprentissage ? même si il ne les met pas au service d'une meilleure insertion sociale - comme apprendre une langue étrangère, devenir un bon joueur d'échec ou acquérir un bon niveau en informatique.", score=6),
                    AnswerOption(value='h', label="Non évaluable", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_ephpa4',
                text="<b>4 Capacité à fixer son attention et à mémoriser.</b> Cet item porte sur les capacités cognitives de base que sont le fait de pouvoir fixer son attention, ne pas perdre le fil d'une discussion, d'une émission de télévision, d'une lecture, etc., et être capable d'en faire un résumé adapté. Ces difficultés sont souvent très importantes chez les personnes souffrant d'un handicap d'origine psychique et largement sous-estimées par leur entourage. L'intérêt que la personne porte à une situation influe bien sûr sur son niveau d'attention , cependant, ce facteur (la motivation) est évalué dans la rubrique suivante et ne doit pas être pris en compte. Il faut donc coter en fonction du meilleur niveau de la personne.",
                options=[
                    AnswerOption(value='a', label="0-la personne ne peut fixer son attention plus de quelques secondes de telle sorte que toute consigne même simple doit lui être répétée car elle les oublie aussitôt.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2-la personne parvient à fixer son attention quelques minutes sur une activité (lire un article de journal même court, regarder une émission de télévision, etc.) mais a tendance à perdre le fil et/ ne parvient pas à en faire un résumé même sommaire ou incomplet.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4-La personne est capable de fixer son attention correctement le temps de voir un film ou une émission, de lire un texte mais est à l'évidence fatigable et ne retient pas toujours les informations principales.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6-La personne n'a pas de difficulté notable pour fixer son attention et mémoriser, du moins dans les situations dans lesquelles elle est motivée pour utiliser ses capacités.", score=6),
                    AnswerOption(value='h', label="Non évaluable", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_ephpb5',
                text="<b>5 Difficulté à initier une action de base</b>, c'est-à-dire les gestes élémentaires de la vie quotidienne comme se lever, faire son lit, descendre la poubelle, faire une course, etc. Il convient de tenir compte du mode de vie de la personne et de ce qu'il serait logique qu'elle fasse spontanément et de prendre en compte l'importance des stimulations nécessaires pour que ces actions soient réalisées.",
                options=[
                    AnswerOption(value='a', label="0-La difficulté à initier une action retentit de manière considérable sur la vie quotidienne et/ou une stimulation ou une aide constante est nécessaire pour que les besoins fondamentaux soient globalement satisfaits.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2-Le sujet est globalement capable de faire face aux besoins fondamentaux de la vie quotidienne, mais sa difficulté à se mettre en route retentit très fortement sur son niveau d'activité.Il a besoin d'un niveau de stimulation très élevé et/ou donne l'impression d'une extrême fatigabilité.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4-Le sujet est suffisamment entreprenant pour faire face aux besoins courants de la vie quotidienne. Ses difficultés se manifestent par un manque d'initiative et de persévérance et/ou parle fait qu'il a tendance à se débarrasser au plus vite de ce qu'il a à faire et/ou par un besoin destimulation ou d'encouragement important. L'impression générale reste celle d'une importante fatigabilité.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6-Le sujet ne semble pas avoir de difficulté particulière pour s'engager dans une activité et persévérer jusqu'à ce que son but soit atteint. Globalement son niveau d'énergie semble correct", score=6),
                    AnswerOption(value='h', label="Non évaluable", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_ephpb6',
                text="<b>6 Difficulté à anticiper et à s'impliquer dans un projet</b>, à entreprendre ou à persévérer, du fait d'un manque de motivation, de dynamisme, d'enthousiasme ou d'une excessive sensibilité au stress. Cela peut correspondre au fait que la personne ne met rien en oeuvre pour des objectifs qu'elle semble souhaiter ou au fait que toute situation nouvelle ou imprévue est ressentie comme extrêmement difficile ou épuisante. Cet item évalue également dans quelle mesure certaines réalisations ne sont possibles que grâce au soutien et aux encouragements de l'entourage. Le fait que les projets de la personne s'inscrivent ou non dans une meilleure adaptation à la vie sociale n'est pas à prendre en compte dans cet item.",
                options=[
                    AnswerOption(value='a', label="0-La difficulté est telle que tout engagement dans un projet même simple (comme faire quelques achats avec un proche ou participer ponctuellement à une activité dans un environnement protégé) est impossible.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2-Le sujet est capable de faire quelques projets mais ne met en oeuvre que de rares actions isolées pour y parvenir et manque gravement de dynamisme. Il peut avoir tendance à anticiper toute action nouvelle comme extrêmement difficile de telle sorte qu'il parait épuisé d'avance et/ou ne tient pas ses engagements, le cas échéant malgré le soutien de son entourage.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4-Le sujet est capable de faire preuve d'initiatives pour atteindre ses objectifs mais manque de persévérance ce qui compromet souvent ses projets, même lorsqu'il est soutenu et encouragé. Sa sensibilité aux évènements imprévus ou difficiles met souvent en cause sa capacité à entreprendre.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6-Le sujet ne semble pas manquer notablement de motivation et se montre capable d'initier des actions de manière suivie et cohérente avec ses projets et de persévérer même lorsque des difficultés surviennent.", score=6),
                    AnswerOption(value='h', label="Non évaluable", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_ephpb7',
                text="<b>7 Utilisation du temps.</b> Cet item a pour but de coter le temps passé sans but précis, à ne rien faire (comme dormir dans la journée, rester au lit ou assis sans rien faire, rester devant la télévision ou écouter de la musique sans y faire attention, etc.).",
                options=[
                    AnswerOption(value='a', label="0-Le sujet passe toute sa journée ou presque à ne rien faire.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2-Le sujet passe à peu près la moitié de ses journées à ne rien faire.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4-Le sujet passe trop de temps, mais moins de la moitié de ses journées, à ne rien faire.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6-Absence d'inactivité excessive (l'inactivité ne dépasse pas le temps normal nécessaire au repos).", score=6),
                    AnswerOption(value='h', label="Non évaluable", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_ephpb8',
                text="<b>8 Curiosité.</b> Cet item a pour but de coter dans quelle mesure le sujet fait attention à son environnement, s'intéresse au monde dans lequel il vit et se pose des questions à ce propos. Sa curiosité peut s'exprimer par la lecture de la presse, par le suivi de certaines questions d'actualité, par une tendance à s'informer sur des faits de société, de culture générale ou sur des faits concernant son entourage ou son environnement. Il convient d'exclure les idées fixes obsessionnelles, délirantes ou bizarres et les hallucinations.",
                options=[
                    AnswerOption(value='a', label="0-Aucune ou quasi aucune curiosité pour son environnement.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2-Une certaine curiosité sporadique mais non suivie en pensée ou en actes.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4-Quelques sujets de curiosité, sur lesquels le sujet passe du temps à réfléchir et fait un certain effort pour mieux les connaître.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6-Curiosité pour de nombreux sujets avec un effort évident pour mieux connaître quelques-uns d'entre eux (par exemple par la lecture, le fait de poser des questions, se renseigner, observer de façon méthodique, etc.)", score=6),
                    AnswerOption(value='h', label="Non évaluable", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_ephpc10',
                text="<b>10 Capacités d'empathie émotionnelle.</b> Cet item a pour but d'évaluer la capacité de la personne à se montrer sensible aux émotions d'autrui, à les percevoir et à en tenir compte, à comprendre qu'autrui peut avoir des émotions qui lui sont propres, à se montrer compréhensif et capable de tact et de respect.",
                options=[
                    AnswerOption(value='a', label="0-Le sujet est incapable de percevoir les émotions d'autrui et d'y réagir émotionnellement.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2-Le sujet perçoit parfois l'émotion d'autrui mais se montre globalement peu chaleureux ou indifférent dans la plupart des situations.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4-Le sujet manifeste plus régulièrement sa sensibilité aux émotions d'autrui. Il peut se montrer parfois chaleureux ou sembler se soucier de ce que l'autre ressent.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6-Le sujet peut ressentir intuitivement ce que l'autre ressent, prend spontanément en considération les émotions d'autrui et en tient compte dans son attitude, son comportement ou sa communication. Il est capable de se montrer chaleureux, tolérant et compréhensif, de percevoir lorsque l'autre est ému ou gêné et/ou de faire preuve de tact.", score=6),
                    AnswerOption(value='h', label="Non évaluable", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_ephpc11',
                text="<b>11 Capacités à identifier les rôles sociaux, la signification des situations sociales.</b> Cet item concerne la capacité à identifier dans une situation donnée les principaux rôles sociaux et la manière dont ces rôles sociaux influencent le comportement de ceux qui les occupent (comme reconnaître une position d'autorité et sur quoi se fonde cette position d'autorité, identifier l'attitude aimable de quelqu'un qui exerce un métier de service, comprendre à qui demander telle ou telle information ou aide du fait de son métier ou de son accès à certaines connaissances, etc.)",
                options=[
                    AnswerOption(value='a', label="0-Le sujet est incapable d'identifier et de comprendre les situations sociales.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2-Le sujet est capable d'identifier certaines situations sociales simples et stéréotypées sans pour autant bien comprendre le rôle joué par l'autre dans ces situations sociales.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4-Le sujet est capable d'identifier les situations sociales les plus courantes et d'avoir un certain degré de compréhension des différents rôles sociaux", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6-Le sujet n'a aucune difficulté pour se repérer dans les interactions sociales et pour comprendre les motifs de chacun dans les situations les plus diverses.", score=6),
                    AnswerOption(value='h', label="Non évaluable", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_ephpc9',
                text="<b>9 Capacités d'empathie cognitive. </b>Cet item a pour but d'évaluer la capacité de la personne à comprendre que les autres sont différents d'elle-même - qu'ils ont des croyances, des désirs, des intentions qui leur sont propres ? et à tenir compte de ces différences. Il s'agit donc d'évaluer la capacité de la personne à adopter le point de vue de l'autre, à se mettre à sa place et à tenir compte de cette compréhension dans sa relation et sa communication avec autrui.",
                options=[
                    AnswerOption(value='a', label="0-Le sujet est incapable de se mettre à la place des autres.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2-Le sujet est très peu capable de se mettre à la place des autres. Il peut parfois comprendre la position d'autrui mais de manière sporadique ou lorsque des « codes » ont préalablement été solidement établis (par exemple, savoir qu'un proche plaisante sans pour autant comprendre le fond de la plaisanterie).", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4-Le sujet parvient plus régulièrement à se mettre à la place des autres. Cependant il commet souvent des erreurs et/ou ne parvient que modérément à tenir compte de cette compréhension dans sa relation ou sa communication avec autrui.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6-Le sujet prend spontanément en considération la situation d'autrui dans la plupart des cas. Il peut prendre en compte le fait qu'autrui n'a pas les mêmes informations ou les mêmes croyances et en tenir compte pour l'aider ou au contraire en tirer des bénéfices pour lui-même.", score=6),
                    AnswerOption(value='h', label="Non évaluable", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_ephpd12',
                text="<b>12 Capacité à savoir évaluer ses capacités et à reconnaître ses limites</b>",
                options=[
                    AnswerOption(value='a', label="0-Le sujet n'a aucune conscience de ses difficultés et de ses incapacités dans la vie quotidienne, sociale, etc. L'écart entre ce que la personne dit faire ou savoir faire et la réalité est considérable.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2-Le sujet n'a qu'une conscience limitée de ses difficultés. Il est convaincu d'avoir un degré d'autonomie supérieur à celui qui est le sien en réalité et/ou d'avoir des capacités importantes et/ou méconnait certains comportements très inadaptés.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4-Le sujet est capable dans un certain nombre de domaines de percevoir ses difficultés ou ses limites mais a tendance à les minimiser ou au contraire à les amplifier, voire les deux à la fois.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6-Le sujet a une réelle connaissance de ses difficultés ou de la qualité de ses réalisations et se montre capable de décrire avec précision ce qu'il sait faire et les domaines, actions, et situationsdans lesquels il se trouve en difficulté.", score=6),
                    AnswerOption(value='h', label="Non évaluable", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_ephpd13',
                text="<b>13 Capacité à savoir demander de l'aide en cas de besoin et à coopérer aux soins</b>",
                options=[
                    AnswerOption(value='a', label="0-Le sujet se montre incapable de demander de l'aide, que ce soit dans le domaine de la vie quotidienne ou de sa santé. Typiquement, il se montre réticent ou manifeste une totale incompréhension par rapport à toute proposition d'aide ou de soin.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2-Le sujet ne demande à peu près rien spontanément mais peut accepter passivement ou de manière intermittente quelques aides dans la vie quotidienne et/ou certains soins. Dans d'autres cas, le sujet est capable de formuler quelques demandes d'aides mais pas de les maintenir de manière stable.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4-Le sujet est capable de demander de l'aide, d'exprimer des attentes (comme être accompagné dans des situations stressantes, ou être stimulé pour parvenir à se mettre en route)et/ou se montre coopérant de manière stable pour certains soins.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6-Le sujet est capable de demander de l'aide de manière adaptée, utilise régulièrement des stratégies ou a mis en place des organisations pour pallier ses principales difficultés (comme financer une aide pour le ménage de son domicile ou s'appuyer sur l'aide de son entourage pour démarrer la journée) et collabore de manière active aux soins qui lui sont nécessaires.", score=6),
                    AnswerOption(value='h', label="Non évaluable", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="EPHP",
            name="EPHP Questionnaire",
            description="13 items questionnaire",
            pathology_domain=PathologyDomain.SCHIZOPHRENIA,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=6,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute EPHP score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
