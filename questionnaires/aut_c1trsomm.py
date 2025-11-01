"""
AUT_C1TRSOMM - AUT_C1TRSOMM Questionnaire
=========================================

39 items questionnaire

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


@register_questionnaire("AUT_C1TRSOMM")
@dataclass
class AutC1trsomm(BaseQuestionnaire):
    """AUT_C1TRSOMM Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_C1TRSOMM questionnaire with all 39 items."""
        
        questions_list = [
            Question(
                id='auag',
                text="Comportements auto-mutilateurs",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='auagprgv',
                text="Gravité  de comportements mutilateurs en moyenne",
                options=[
                    AnswerOption(value='a', label="Légère", score=0),
                    AnswerOption(value='b', label="Modérée", score=1),
                    AnswerOption(value='c', label="Sévère", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='auagprty2',
                text="Type",
                options=[
                    AnswerOption(value='a', label="Morsure", score=0),
                    AnswerOption(value='b', label="Se frapper", score=1),
                    AnswerOption(value='c', label="Griffure", score=2),
                    AnswerOption(value='d', label="Brûlure", score=3),
                    AnswerOption(value='e', label="Scarification", score=4),
                    AnswerOption(value='f', label="Amputation", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='auagsvgv',
                text="Gravité  de comportements mutilateurs en moyenne",
                options=[
                    AnswerOption(value='a', label="Légère", score=0),
                    AnswerOption(value='b', label="Modérée", score=1),
                    AnswerOption(value='c', label="Sévère", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='auagsvty2',
                text="Type",
                options=[
                    AnswerOption(value='a', label="Morsure", score=0),
                    AnswerOption(value='b', label="Se frapper", score=1),
                    AnswerOption(value='c', label="Griffure", score=2),
                    AnswerOption(value='d', label="Brûlure", score=3),
                    AnswerOption(value='e', label="Scarification", score=4),
                    AnswerOption(value='f', label="Amputation", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cauch',
                text="Cauchemars ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cauch1',
                text="Réveils répétés au cours de la période principale de sommeil ou de la sieste avec souvenirs précis de rêves effrayants et prolongés. Ces rêves comportent habituellement un danger pour la survie, la sécurité ou l’estime de soi. Les réveils surviennent généralement au cours de la deuxième moitié de la période de sommeil.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cauch2',
                text="Lorsque le sujet se réveille après un cauchemar il est rapidement orienté et pleinement éveillé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cauch4',
                text="En rémission ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hypers1',
                text="Episodes de sommeil nocturne prolongé ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hypers2',
                text="Episodes de sommeil diurne prolongé ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hypers4',
                text="En rémission",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='insom1',
                text="Difficulté d'endormissement ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='insom2',
                text="Difficulté de maintien du sommeil ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='insom3',
                text="Sommeil non réparateur",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='insom5',
                text="En rémission",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='intsev',
                text="Intention suicidaire lors de la tentative la plus sévère ",
                options=[
                    AnswerOption(value='a', label="Pas d’intention ou intention minimale, manipulation ", score=0),
                    AnswerOption(value='b', label="Intention présente mais ambivalente", score=1),
                    AnswerOption(value='c', label="Intention claire, pensait mourir ", score=2),
                    AnswerOption(value='d', label="Non connu", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='letsev',
                text="Risque létal de la tentative la plus sévère ",
                options=[
                    AnswerOption(value='a', label="Pas de risque  ", score=0),
                    AnswerOption(value='b', label="Risque minimal ", score=1),
                    AnswerOption(value='c', label="Risque léger ", score=2),
                    AnswerOption(value='d', label="Risque modéré ", score=3),
                    AnswerOption(value='e', label="Risque sérieux ", score=4),
                    AnswerOption(value='f', label="Risque extrême", score=5),
                    AnswerOption(value='g', label="Non connu", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='narco',
                text="Narcolepsie ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='narco1',
                text="Attaques irrésistibles d’un sommeil réparateur survenant quotidiennement pendant au moins trois mois ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='narco2',
                text="Cataplexie, c-a-d épisodes brefs de perte de tonus musculaire bilatéral, le plus souvent lié à une émotion intense",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='narco3',
                text="Intrusion récurrente d’éléments du sommeil paradoxal lors des transitions veille- sommeil se manifestant par des hallucinations hypnopompiques ou hypnagogiques ou par des paralysies du sommeil en début ou en fin d’épisodes de sommeil",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='narco5',
                text="En rémission",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='otrchang',
                text="Changement depuis la dernière visite",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='retph',
                text="Retard de phase / Absence de phase  ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='retph1',
                text="Tendance à décaler le rythme diurne vers une heure plus tardive de coucher et de lever matinal",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='retph4',
                text="En rémission",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='somna',
                text="Somnambulisme ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='somna1',
                text="Au cours de ses déambulations le sujet a un visage inexpressif, le regard fixe, et ne réagit guère aux efforts de son entourage pour communiquer avec lui ; il ne peut être réveillé qu’avec beaucoup de difficultés",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='somna2',
                text="Au réveil le sujet ne garde aucun souvenir de l’épisode ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='somna5',
                text="En rémission",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tern1',
                text="Episodes récurrents de réveil brutal, habituellement lors du 1/3 de la  période principale de sommeil, et débutant par un cri de terreur.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tern2',
                text="Présence au cours de chaque épisode d’une peur intense et d’une activation neurovégétative se traduisant par des symptômes tels que tachycardie, polypnée, transpiration.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tern3',
                text="Pendant l’épisode la personne ne réagit que peu aux efforts faits par son entourage pour la réconforter.\n                    ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tern4',
                text="Absence de remémoration détaillée d’un rêve ; amnésie de l’épisode",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tern6',
                text="En rémission ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='terrnoc',
                text="Terreurs nocturnes ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ts',
                text="Conduites suicidaires  ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tsgrav',
                text="Tentative de suicide grave  ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_C1TRSOMM",
            name="AUT_C1TRSOMM Questionnaire",
            description="39 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=19,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_C1TRSOMM score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
