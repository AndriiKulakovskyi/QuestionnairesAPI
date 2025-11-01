"""
BAS - BAS Questionnaire
=======================

9 items questionnaire

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


@register_questionnaire("BAS")
@dataclass
class Bas(BaseQuestionnaire):
    """BAS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize BAS questionnaire with all 9 items."""
        
        questions_list = [
            Question(
                id='bas1',
                text="Tension intérieure. Correspond aux sentiments de malaise mal défini, d'irritabilité, d'agitation intérieure,\nde tension nerveuse allant jusqu'à la panique, l'effroi ou l'angoisse. Coter selon l’intensité, la fréquence, la\ndurée, le degré de réassurance nécessaire.\nA distinguer de la tristesse, de l'inquiétude pour des \\",
                options=[
                    AnswerOption(value='a', label="0 Calme. Tension intérieure seulement passagère.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Sentiments occasionnels d'irritabilité et de malaise mal défini", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4 Sentiments continuels de tension intérieure ou panique intermittente que le malade ne peut maitriser qu'avec difficultés", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6 Effroi ou angoisse sans relâche. Panique envahissante.", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bas10',
                text="Troubles neuro-végétatifs. Correspond à des symptômes tels que : palpitations, difficultés respiratoires,vertiges, sueurs abondantes, froideur des extrémités, sécheresse de la bouche, troubles digestifs, diarrhées,mictions fréquentes.A distinguer de la tension intérieure, des douleurs et des troubles sensori-moteurs.",
                options=[
                    AnswerOption(value='a', label="0 Calme. Tension intérieure seulement passagère.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Symptômes neuro-végétatifs à l'occasion d'une émotion", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4 Troubles neuro-végétatifs fréquents ou intenses,vécus comme gênants ou affectant la vie sociale", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6 Troubles neuro-végétatifs très fréquents, interrompant les activités ou invalidants.", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bas2',
                text="Sentiments hostiles. Correspond à la colère, à l’hostilité, à des sentiments agressifs avec ou sans\nmanifestations actives.\nCoter selon l’intensité, la fréquence et le niveau de provocation toléré.\nCoter zéro l'incapacité à ressentir de la colère.",
                options=[
                    AnswerOption(value='a', label="0 Ne se met pas facilement en colère", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Se met facilement en colère. Exprime des sentiments hostiles qui sont aisément dissipés", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4 Répond aux provocations par une hostilité ou une colère disproportionnée", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6 Etat persistant de colère, de fureur, ou de haine intense, difficile ou impossible à contrôler", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bas3',
                text="Hypocondrie. Correspond à une préoccupation exagérée ou une inquiétude injustifiée concernant la sante\nou les maladies.\nA distinguer de l’inquiétude pour des \\",
                options=[
                    AnswerOption(value='a', label="0 Absence de préoccupation particulière concernant la sante", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Réagit avec appréhension au moindre signe de désordre physique. Peur exagérée de la maladie", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4 Convaincu qu'il est atteint d'une maladie, mais peut être rassuré au moins temporairement", score=4),
                    AnswerOption(value='f', label="5", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bas5',
                text="Inquiétude pour des \\",
                options=[
                    AnswerOption(value='a', label="0 Pas d'inquiétude particulière ", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Inquiétude injustifiée pouvant être dissipée ", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4 Inquiet et tracassé par des vétilles et les menus faits de la vie quotidienne", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6 Inquiétude envahissante et souvent douloureuse. Les tentatives pour rassurer le sujet sont sans\neffet .", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bas6',
                text="Douleurs. Correspond à l'expression d'une gêne ou d'une douleur physique.\nCoter selon l'intensité, la fréquence, la durée et aussi la demande de soulagement. Ne tenir compte d'aucune opinion\nquant à une organicité éventuelle.\nA distinguer de l'hypocondrie, des troubles neuro-végétatifs et de la tension musculaire.",
                options=[
                    AnswerOption(value='a', label="0 Absence de douleurs ou douleurs passagères", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Douleurs précises mais occasionnelles", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4 Douleurs prolongées et pénibles. Demandes d'un traitement antalgique efficace", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6 Douleurs intenses ou invalidantes", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bas7',
                text="Troubles neuro-végétatifs. Correspond aux signes de dysfonctionnement neuro-végétatif :\nhyperventilation, bouffées vasomotrices, sueurs, mains froides, dilatation pupillaire, bouche sèche,\névanouissements.",
                options=[
                    AnswerOption(value='a', label="0 Pas de troubles neuro-végétatifs observés.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Troubles neuro-végétatifs discrets : rougit, blêmit ou se couvre de sueurs à l'occasion d'une émotion.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4 Signes neuro-végétatifs évidents même en dehors des situations de stress", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6 Troubles neuro-végétatifs obligeant à interrompre l'entretien", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bas8',
                text="Tension musculaire. Correspond à une tension musculaire telle qu'on peut l'observer dans la mimique, la\nposture et les mouvements",
                options=[
                    AnswerOption(value='a', label="0 Parait détendu", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Légère tension dans le visage et la posture", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4  Tension modérée dans la posture et la face, que l'on remarque facilement au niveau des mâchoires et des muscles du cou. Ne semble pas trouver une position détendue quand il est assis. Mouvements raides et maladroits", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6 Tendu d'une manière frappante. Assis, se tient souvent vouté et recroquevillé, ou bien est tendu et se tient droit et raide sur le bord du siège", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bas9',
                text="Réduction du sommeil. Correspond à une réduction de la durée ou de la profondeur du sommeil par comparaison avec le sommeil du patient lorsqu'il n'est pas malade",
                options=[
                    AnswerOption(value='a', label="0 Dort comme d'habitude", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Légère difficulté à s'endormir ou sommeil légèrement réduit, léger ou agité", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4 Sommeil réduit ou interrompu au moins deux heures", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6 Moins de deux ou trois heures de sommeil", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="BAS",
            name="BAS Questionnaire",
            description="9 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute BAS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
