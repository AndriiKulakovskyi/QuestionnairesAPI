"""
MADRS - MADRS Questionnaire
===========================

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


@register_questionnaire("MADRS")
@dataclass
class Madrs(BaseQuestionnaire):
    """MADRS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize MADRS questionnaire with all 9 items."""
        
        questions_list = [
            Question(
                id='madrs10',
                text="10 - Idées de suicide Correspond au sentiment que la vie ne vaut pas le peine d'être vécue, qu'une mort naturelle serait la bienvenue, idées de suicide et préparatifs au suicide. Les tentatives de suicide ne doivent pas, en elles-mêmes, influencer la cotation.",
                options=[
                    AnswerOption(value='a', label="0 Jouit de la vie ou la prend comme elle vient.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Fatigué de la vie, idées de suicide seulement passagères.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4 Il vaudrait mieux être mort. Les idées de suicide sont courantes et le suicide est considéré comme une solution possible mais sans projet ou intention précis.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6 Projets explicites de suicide si l'occasion se présente. Préparatifs de suicide.", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='madrs2',
                text="2- Tristesse exprimée Correspond à l'expression d'une humeur dépressive, que celle-ci soit apparente ou non. Inclut le cafard, le découragement ou le sentiment de détresse sans espoir. Coter selon l'intensité, la durée à laquelle l'humeur est dite être influencée par les événements.",
                options=[
                    AnswerOption(value='a', label="0 Tristesse occasionnelle en rapport avec les circonstances.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Triste ou cafardeux, mais se déride sans difficulté.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4 Sentiment envahissant de tristesse ou de dépression ; l'humeur est encore influencée par les circonstances extérieures.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6 Tristesse, désespoir ou découragement permanents ou sans fluctuations.", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='madrs3',
                text="3- Tension intérieure Correspond aux sentiments de malaise mal défini, d'irritabilité, d'agitation intérieure, de tension nerveuse allant jusqu'à la panique, l'effroi ou l'angoisse. Coter selon l'intensité, la fréquence, la durée, le degré de réassurance nécessaire.",
                options=[
                    AnswerOption(value='a', label="0 Calme. Tension intérieure seulement passagère.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Sentiments occasionnels d'irritabilité et de malaise mal défini.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4 Sentiments continuels de tension intérieure ou panique intermittente que le malade ne peut maîtriser qu'avec difficulté.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6 Effroi ou angoisse sans relâche. Panique envahissante.", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='madrs4',
                text="4- Réduction de sommeil Correspond à une réduction de la durée ou de la profondeur du sommeil par comparaison avec le sommeil du patient lorsqu'il n'est pas malade.",
                options=[
                    AnswerOption(value='a', label="0 Dort comme d'habitude.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Légère difficulté à s'endormir ou sommeil légèrement réduit, léger ou agité.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4 Sommeil réduit ou interrompu au moins deux heures.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6 Moins de deux ou trois heures de sommeil.", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='madrs5',
                text="5- Réduction de l'appétit Correspond au sentiment d'une perte de l'appétit comparé à l'appétit habituel. Coter l'absence de désir de nourriture ou le besoin de se forcer pour manger.",
                options=[
                    AnswerOption(value='a', label="0 Appétit normal ou augmenté.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Appétit légèrement réduit.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4 Pas d'appétit. Nourriture sans goût.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6 Ne mange que si on le persuade.", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='madrs6',
                text="6 - Difficultés de concentration Correspond aux difficultés à rassembler ses pensées allant jusqu'à l'incapacité à se concentrer. Coter l'intensité, la fréquence et le degré d'incapacité.",
                options=[
                    AnswerOption(value='a', label="0 Pas de difficultés de concentration.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Difficultés occasionnelles à rassembler ses pensées", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4 Difficultés à se concentrer et à maintenir sonattention, cequi réduit la capacité à lire ou à soutenir une conversation", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6 Incapable de lire ou de converser sans grande diffuculté.", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='madrs7',
                text="7- Lassitude Correspond à une difficulté à se mettre en train ou une lenteur à commencer et à accomplir les activités quotidiennes.",
                options=[
                    AnswerOption(value='a', label="0 Guère de difficultés à se mettre en route. Pas de lenteur.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Difficultés à commencer des activités.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4 Difficultés à commencer des activités routinières qui sont poursuivies avec effort.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6 Grande lassitude. Incapable de faire quoi que ce soit sans aide.", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='madrs8',
                text="8- Incapacité à ressentir Correspond à l'expérience subjective d'une réduction d'intérêt pour le monde environnant, ou les activités qui donnent normalement du plaisir. La capacité à réagir avec une émotion appropriée aux circonstances ou aux gens est réduite.",
                options=[
                    AnswerOption(value='a', label="0 Intérêt normal pour le monde environnant et pour les gens.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Capacité réduite à prendre du plaisir à ses intérêts habituels.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4 Perte d'intérêt pour le monde environnant. Perte de sentiment pour les amis et les connaissances.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6 Sentiment d'être paralysé émotionnellement, incapacité à ressentir de la colère, du chagrin ou du plaisir et impossibilité complète ou même douloureuse de ressentir quelque chose pour les proches parents et amis.", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='madrs9',
                text="9- Pensées pessimistes Correspond aux idées de culpabilité, d'infériorité, d'auto-accusation, de pêché, de remords ou de ruine.",
                options=[
                    AnswerOption(value='a', label="0 Pas de pensée pessimiste.", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2 Idées intermittentes d'échec, d'auto-accusation ou d'autodépréciation.", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4 Auto-accusations persistantes ou idées de culpabilité ou péché précises mais encore rationnelles. Pessimisme croissant à propos du futur.", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6 Idées délirantes de ruine, de remords ou péché inexpiable. Auto-accusations absurdes ou inébranlables.", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="MADRS",
            name="MADRS Questionnaire",
            description="9 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.CLINICIAN_RATED,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute MADRS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
