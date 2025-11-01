"""
AUT_C1CRIDSM - AUT_C1CRIDSM Questionnaire
=========================================

38 items questionnaire

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


@register_questionnaire("AUT_C1CRIDSM")
@dataclass
class AutC1cridsm(BaseQuestionnaire):
    """AUT_C1CRIDSM Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_C1CRIDSM questionnaire with all 38 items."""
        
        questions_list = [
            Question(
                id='asdi1',
                text="1. Présente-t-il / elle des difficultés importantes d'interaction avec ses pairs ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, un peu", score=1),
                    AnswerOption(value='c', label="Non", score=2),
                    AnswerOption(value='d', label="Non connu", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asdi10',
                text="10. Le développement de son langage a-t-il été retardé ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, un peu", score=1),
                    AnswerOption(value='c', label="Non", score=2),
                    AnswerOption(value='d', label="Non connu", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asdi11',
                text="11. Son  langage est-il « superficiellement parfait » qu'il y ait ou non  des  troubles de compréhension ou d'autres troubles de la parole et du langage ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, un peu", score=1),
                    AnswerOption(value='c', label="Non", score=2),
                    AnswerOption(value='d', label="Non connu", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asdi12',
                text="12. Son langage est-il soigné, pédant ou « trop adulte » ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, un peu", score=1),
                    AnswerOption(value='c', label="Non", score=2),
                    AnswerOption(value='d', label="Non connu", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asdi15',
                text="15. Fait-il / elle un usage limité des gestes ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, un peu", score=1),
                    AnswerOption(value='c', label="Non", score=2),
                    AnswerOption(value='d', label="Non connu", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asdi16',
                text="16. Ses gestes sont-ils embarrassés, gauches, maladroits, étranges ou inhabituels ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, un peu", score=1),
                    AnswerOption(value='c', label="Non", score=2),
                    AnswerOption(value='d', label="Non connu", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asdi17',
                text="17. Ses expressions faciales sont-elles plutôt limitées à un petit répertoire ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, un peu", score=1),
                    AnswerOption(value='c', label="Non", score=2),
                    AnswerOption(value='d', label="Non connu", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asdi19',
                text="19. Son regard est-il distant, étrange, particulier, anormal ou bizarre ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, un peu", score=1),
                    AnswerOption(value='c', label="Non", score=2),
                    AnswerOption(value='d', label="Non connu", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asdi2',
                text="2. Présente-t-il / elle peu d'intérêt ou un manque d'intérêt à se faire des  amis ou à interagir avec ses pairs ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, un peu", score=1),
                    AnswerOption(value='c', label="Non", score=2),
                    AnswerOption(value='d', label="Non connu", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asdi3',
                text="3. A-t-il / elle des difficultés à se rendre compte des signaux sociaux, c'est-à-dire qu'il / elle ne remarque pas les changements de conversation ou d'interaction sociale ou ne prend pas en compte de tels changements dans son interaction avec les autres ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, un peu", score=1),
                    AnswerOption(value='c', label="Non", score=2),
                    AnswerOption(value='d', label="Non connu", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asdi4',
                text="4. Présente-t-il / elle des conduites inappropriées sur le plan social ou émotionnel ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, un peu", score=1),
                    AnswerOption(value='c', label="Non", score=2),
                    AnswerOption(value='d', label="Non connu", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asdi5',
                text="5. Existe-t-il  un  centre d'intérêt ou  un  intérêt spécifique qui lui prend  beaucoup  de temps à tel point que le temps pour d'autres activités s'en trouve très réduit ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, un peu", score=1),
                    AnswerOption(value='c', label="Non", score=2),
                    AnswerOption(value='d', label="Non connu", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asdi6',
                text="6. Ses centres d'intérêt ou son intérêt spécifique présentent-ils un caractère restreint ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, un peu", score=1),
                    AnswerOption(value='c', label="Non", score=2),
                    AnswerOption(value='d', label="Non connu", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asdi7',
                text="7. Ses centres d'intérêt sont-ils basés sur la mémoire de ce qui est appris par cœur plutôt que sur leur sens réel ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, un peu", score=1),
                    AnswerOption(value='c', label="Non", score=2),
                    AnswerOption(value='d', label="Non connu", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asdi8',
                text="8. Essaie-t-il / elle d'introduire et de s'imposer des routines, rituels ou  intérêts à tel point que cela pose des problèmes pour lui-même / elle-même ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, un peu", score=1),
                    AnswerOption(value='c', label="Non", score=2),
                    AnswerOption(value='d', label="Non connu", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asdi9',
                text="9. Essaie-t-il / elle d'introduire et de s'imposer des routines, rituels ou  intérêts à tel point que cela pose des problèmes pour les autres ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Oui, un peu", score=1),
                    AnswerOption(value='c', label="Non", score=2),
                    AnswerOption(value='d', label="Non connu", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asdicrit',
                text="Critères diagnostiques Asperger selon ASDI ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asdinf',
                text="ASDI réalisé ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cridsm17',
                text="1. Manque de réciprocité sociale et émotionnelle; allant de l'approche sociale anormale et du défaut d'alternance dans la prise de parole, avec  un partage d'intérêts, d'émotions, et d'affects, ainsi qu'une   réponse,   réduits,   jusqu'à   l'absence totale d'initiation de l'interaction sociale.\n                    ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Inconnu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cridsm18',
                text="2. Défaut d'utilisation des comportements communicatifs non   verbaux utilisés pour l'interaction sociale; allant d'une intégration pauvre de la communication verbale et non verbale, jsuqu'à une absence totale d'expression faciale et de gestes, en passant par des anomalies de contact visuel et de langage corporel ou un défaut de compréhension et d'utilisation de la communication non verbale\n                    ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Inconnu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cridsm19',
                text="3. Défaut de développement et de maintien de relations sociales correspondant au niveau de développement, en dehors des relations avec les aidants, allant de difficultés à ajuster son comportement  pour  s'adapter  à  différents  contextes  sociaux,  jusqu'à  une   absence apparente  d'intérêt  pour  les  gens,  en  passant  par  des  difficultés  à  partager  des  jeux imaginatifs et à se faire des amis.\n                    ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Inconnu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cridsm20',
                text="1. Caractère stéréotypé ou répétitif du langage, des mouvements moteurs, ou de l'utilisation des objets, (comme  des  stéréotypies  motrices  simples, une écholalie, une utilisation répétitive des objets, ou utilisation idiosyncratique de phrases).\n                    ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Inconnu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cridsm21',
                text="2. Adhésion excessive à des routines, des modèles de comportement verbal ou non verbal ritualisés, ou une résistance excessive au changement (comme des rituels moteurs, une\n insistance à prendre le même chemin ou consommer la même nourriture, des  questions\n répétitives, ou une détresse extrême lors de petites changements).\n                    ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Inconnu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cridsm24',
                text="C.  Les symptômes doivent être présents dans la petite enfance mais peuvent ne devenir manifestes que lorsque les exigences sociales dépassent les capacités limitées",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Inconnu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cridsm25',
                text="D. Les symptomes limitent et gênent le fonctionnement quotidien",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Inconnu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cridsm26',
                text="Critères diagnostiques DSM-V Trouble du spectre Autistique ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dsmaut01',
                text="Déficience intellectuelle",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dsmaut02',
                text="Trouble du langage",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dsmaut03',
                text="Condition médicale ou génétique connue ou un facteur environnemental",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dsmaut04',
                text="Trouble neurodéveloppemental, mental ou du comportement",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dsmaut05',
                text="Catatonie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dsmaut06',
                text="Niveau 1 : nécessite un soutien très important",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dsmaut07',
                text="Niveau 2 : nécessite un soutien important",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dsmaut08',
                text="Niveau 3 : nécessite un soutien",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dsmaut09',
                text="Niveau 1 : nécessite un soutien très important",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dsmaut10',
                text="Niveau 2 : nécessite un soutien important",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dsmaut11',
                text="Niveau 3 : nécessite un soutien",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dsmchang',
                text="Changement depuis la dernière visite",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_C1CRIDSM",
            name="AUT_C1CRIDSM Questionnaire",
            description="38 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=19,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_C1CRIDSM score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
