"""
AUT_SPQ - AUT_SPQ Questionnaire
===============================

72 items questionnaire

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


@register_questionnaire("AUT_SPQ")
@dataclass
class AutSpq(BaseQuestionnaire):
    """AUT_SPQ Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_SPQ questionnaire with all 72 items."""
        
        questions_list = [
            Question(
                id='spq_1',
                text="1.Il m'arrive d'avoir l'impression que ce que je vois à la télévision ou ce que je lis dans les journaux m'est personnellement destiné.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_10',
                text="10.Je me rends compte que les gens me remarquent quand je sors pour aller au restaurant ou au cinéma.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_11',
                text="11.Je deviens facilement très nerveux quand je suis obligé de tenir des conversations de courtoisie avec les gens.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_13',
                text="13.Il m'est déjà arrivé d'avoir la sensation de sentir une force ou une présence auprès de moi, alors même que j'étais tout seul à ce moment-là.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_14',
                text="14.Les gens font parfois des commentaires sur mes comportements ou certaines de mes manières qu'ils trouvent inhabituelles.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_15',
                text="15.En général, j'aime mieux garder pour moi ce que je pense.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_16',
                text="16.Je saute parfois du coq-à-l'âne quand je discute.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_17',
                text="17.J'ai du mal à exprimer mes véritables sentiments, que ce soit au moyen de la parole ou avec le regard.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_18',
                text="18.J'ai souvent le sentiment qu'il y a quelque chose en moi qui ne revient pas aux gens.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_19',
                text="19.Il m'arrive que les gens me fassent des allusions voilées ou disent des choses à double sens.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_2',
                text="2.Il m'arrive d'éviter les lieux où il y a de la foule, car j'y deviens facilement anxieux.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_20',
                text="20.Ca me rend nerveux de sentir quelqu'un marcher derrière moi.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_21',
                text="21.Je suis parfois convaincu que d'autres personnes seraient capables de dire ce que je suis en train de penser.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_22',
                text="22.Quand je me regarde dans un miroir ou quand je regarde quelqu'un dans un miroir, il m'arrive d'avoir l'impression de voir le visage se modifier légèrement.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_23',
                text="23.Il arrive parfois que les gens pensent que je suis un peu étrange.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_24',
                text="24.La plupart du temps je reste silencieux quand je suis avec d'autres personnes.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_25',
                text="25.Il m'arrive quelquefois de perdre le fil de ce que je suis en train de dire.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_26',
                text="26.Je ris et je souris rarement.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_27',
                text="27.J'ai parfois le sentiment que mes amis ou mes collègues de travail ne sont pas vraiment loyaux ou dignes de foi.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_28',
                text="28.J'ai déjà remarqué que certains objets ou certaines situations apparemment sans importance peuvent être des sortes de messages si l'on arrive à les décrypter.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_29',
                text="29.Je suis facilement anxieux quand je rencontre des gens pour la première fois.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_3',
                text="3.J'ai déjà eu des expériences en rapport avec des choses surnaturelles.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_31',
                text="31.Il m'est parfois arrivé d'entendre une voix intérieure qui disait ou commentait mes pensées tout haut.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_32',
                text="32.Certaines personnes pensent que je suis quelqu'un de très bizarre.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_33',
                text="33.Ca m'est souvent difficile de me sentir proche des gens sur le plan émotionnel.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_34',
                text="34.Il m'arrive souvent de partir dans tous les sens quand je parle de quelque chose.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_35',
                text="35.J'ai du mal à utiliser les expressions du visage ou les gestes des mains pour communiquer avec les gens.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_36',
                text="36.Je sens que je dois rester sur mes gardes même avec mes amis.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_37',
                text="37.Il m'arrive parfois de voir des signes précis dans les publicités, les enseignes ou les vitrines de la rue, ou dans la façon dont les objets sont agencées autour de moi.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_38',
                text="38.Je me sens souvent nerveux quand je me trouve dans un groupe de gens que je ne connais pas",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_39',
                text="39.J'ai parfois le sentiment que d'autres personnes peuvent ressentir mes sentiments tout en étant loin de moi.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_4',
                text="4.Il peut m'arriver de prendre des ombres ou certains objets pour des personnes ou bien certains bruits pour des voix.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_40',
                text="40.Il me semble avoir déjà vu certaines choses que les autres ne pouvaient pas voir.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_41',
                text="41.J'ai le sentiment de n'être vraiment proche de personne en dehors de ma famille ou de mon conjoint ou qu'il n'y a pas vraiment quelqu'un à qui je puisse me confier ou parler de mes problèmes personnels.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_42',
                text="42.Certains me trouvent parfois vague ou peu clair lors des conversations.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_43',
                text="43.J'ai du mal à répondre aux invitations ou à rendre les politesses aux gens.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_44',
                text="44.Je relève souvent des remarques dépréciatives ou des menaces cachées dans ce que les gens disent ou font.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_45',
                text="45.Lorsque je fais mes courses, j'ai le sentiment que les gens me remarquent.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_46',
                text="46.Je me sens très mal à l'aise dans les situations où je suis en présence de gens que je ne connais pas",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_47',
                text="47.J'ai déjà eu des expériences particulières en rapport avec l'astrologie, la divination, le contact avec d'autres êtres, les perceptions extrasensorielles, ou tout simplement, j'ai le sentiment d'avoir un sixième sens.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_48',
                text="48.Il arrive que les objets qui m'entourent paraissent parfois inhabituellement trop grands ou trop petits, comme si leurs proportions avaient changé.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_49',
                text="49.Ecrire une lettre à un ami est si compliqué que cela n'en vaut souvent pas la peine.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_5',
                text="5.Je pense que beaucoup de gens me considèrent comme quelqu'un d'un peu bizarre ou un peu curieux.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_50',
                text="50.Il m'arrive d'utiliser les mots de travers.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_51',
                text="51.J'ai tendance à éviter de regarder les gens dans les yeux quand je leur parle.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_52',
                text="52.Je pense qu'il vaut mieux que les gens n'en sachent pas trop sur moi.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_53',
                text="53.Lorsque je vois des gens parler entre eux, je me demande souvent s'ils ne parlent pas de moi.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_54',
                text="54.Je serais très angoissé si je devais faire un discours devant un grand groupe de gens.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_55',
                text="55.J'ai déjà eu l'impression de parvenir à communiquer avec d'autres personnes rien que par la pensée.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_56',
                text="56.Il arrive que mon odorat devienne parfois inhabituellement développé.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_57',
                text="57.J'ai tendance à me tenir en retrait dans les situations sociales.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_58',
                text="58.J'ai tendance à m'écarter du sujet pendant une conversation.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_59',
                text="59.J'ai souvent l'impression que les autres ont quelque chose contre moi.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_6',
                text="6.Je trouve peu d'intérêt à faire la connaissance d'autres personnes.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_60',
                text="60.J'ai parfois l'impression que les autres me dévisagent.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_61',
                text="61.Il m'arrive d'être subitement distrait par des sons lointains auxquels je n'accorde normalement aucune attention.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_62',
                text="62.J'attache peu d'importance au fait d'avoir des amis proches.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_63',
                text="63.J'ai parfois le sentiment que les gens parlent de moi.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_64',
                text="64.Mes pensées sont parfois si intenses que je peux presque les entendre.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_65',
                text="65.Je dois souvent rester vigilant pour que les gens n'abusent pas de ma confiance ou de ma bonne volonté.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_66',
                text="66.J'ai le sentiment qu'il ne m'est pas possible d'être proche des gens.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_67',
                text="67.Je suis quelqu'un d'original ou d'assez spécial, en tout cas assez différent des autres.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_68',
                text="68.Ma manière de m'exprimer n'est pas très expressive et vivante.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_69',
                text="69.Je trouve qu'il est difficile de communiquer clairement aux autres ce que j'ai envie de leur dire.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_7',
                text="7.Les gens ont parfois du mal à comprendre ce que je dis quand je me lance dans une explication.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_70',
                text="70.J'ai quelques habitudes excentriques.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_71',
                text="71.Je me sens très mal à l'aise quand je parle à des gens que je ne connais pas bien",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_72',
                text="72.On me fait parfois la remarque que mes propos sont embrouillés.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_73',
                text="73.J'ai tendance à garder mes sentiments pour moi.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_74',
                text="74.Les gens m'évitent parfois à cause de mon apparence excentrique.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_8',
                text="8.Les gens me trouvent parfois lointain ou distant.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spq_9',
                text="9.J'ai le sentiment qu'on parle de moi dans mon dos.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_SPQ",
            name="AUT_SPQ Questionnaire",
            description="72 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=36,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_SPQ score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
