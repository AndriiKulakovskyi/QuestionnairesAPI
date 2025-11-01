"""
CSSRS - CSSRS Questionnaire
===========================

10 items questionnaire

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


@register_questionnaire("CSSRS")
@dataclass
class Cssrs(BaseQuestionnaire):
    """CSSRS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize CSSRS questionnaire with all 10 items."""
        
        questions_list = [
            Question(
                id='cssrs13',
                text="Avez-vous fait une tentative de suicide ou quelque chose de dangereux qui aurait pu entraîner votre mort ?\n",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cssrs15',
                text="Le sujet a-t-il eu un comportement auto-agressif non suicidaire ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cssrs2',
                text="2. Avez-vous réellement pensé à vous suicider ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cssrs20',
                text="Avez-vous pris certaines mesures pour faire une tentative de suicide ou pour préparer votre suicide ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cssrs21',
                text="Un comportement suicidaire a-t-il été observé au cours de la période d'évaluation ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cssrs3',
                text="3. Avez-vous pensé à la manière dont vous vous y prendriez ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cssrs4',
                text="4. Avez-vous eu des pensées de ce genre et l'intention de passer à l'acte ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cssrs5',
                text="5. Avez-vous commencé ou fini d'élaborer un scénario détaillé sur la manière dont vous voulez vous suicider ?\nAvez-vous l'intention de mettre ce scénario à exécution ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cssrs8',
                text="Combien de fois avez-vous eu ces pensées ?",
                options=[
                    AnswerOption(value='a', label="Moins d'une fois par semaine", score=0),
                    AnswerOption(value='b', label="Une fois par semaine", score=1),
                    AnswerOption(value='c', label="2 à 5 fois par semaine", score=2),
                    AnswerOption(value='d', label="Tous les jours ou presque", score=3),
                    AnswerOption(value='e', label="Plusieurs fois par jour", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cssrs9',
                text="Lorsque vous avez ces pensées, combien de temps durent-elles ?",
                options=[
                    AnswerOption(value='a', label="Quelques instants : quelques secondes ou quelques minutes", score=0),
                    AnswerOption(value='b', label="Moins d'une heure/un certain temps", score=1),
                    AnswerOption(value='c', label="1 à 4 heures/longtemps", score=2),
                    AnswerOption(value='d', label="4 à 8 heures/une grande partie de la journée", score=3),
                    AnswerOption(value='e', label="Plus de 8 heures/en permanence ou tout le temps", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="CSSRS",
            name="CSSRS Questionnaire",
            description="10 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute CSSRS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
