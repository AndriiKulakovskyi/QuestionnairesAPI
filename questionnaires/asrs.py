"""
ASRS - ASRS Questionnaire
=========================

19 items questionnaire

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


@register_questionnaire("ASRS")
@dataclass
class Asrs(BaseQuestionnaire):
    """ASRS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize ASRS questionnaire with all 19 items."""
        
        questions_list = [
            Question(
                id='asrs1',
                text="1. A quelle fréquence vous arrive-t-il d'avoir des difficultés à finaliser les derniers détails d'un projet une fois que les parties les plus stimulantes ont été faites ?",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs10',
                text="10. À la maison ou au travail, à quelle fréquence vous arrive-t-il d'égarer des choses ou d'avoir des difficultés à les retrouver?",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs11',
                text="11. À quelle fréquence vous arrive-t-il d'être distrait par l?activité ou par le bruit autour de vous?",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs12',
                text="12. À quelle fréquence vous arrive-t-il de quitter votre siège pendant des réunions ou d'autres situations où vous devriez rester assis?",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs13',
                text="13. À quelle fréquence vous arrive-t-il d'avoir des difficultés à vous tenir tranquille?",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs14',
                text="14. À quelle fréquence vous arrive-t-il d'avoir des difficultés à vous détendre et à vous reposer dans vos temps libres?",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs15',
                text="15. À quelle fréquence vous arrive-t-il de parler de façon excessive à l?occasion de rencontres sociales?",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs16',
                text="16. Pendant une conversation, à quelle fréquence vous arrive-t-il de terminer les phrases de vos interlocuteurs avant que ces derniers aient le temps de les finir?\n	",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs17',
                text="17. À quelle fréquence vous arrive-t-il d'avoir des difficultés à attendre votre tour lorsque vous devriez le faire?\n	",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs18',
                text="18. À quelle fréquence vous arrive-t-il d'interrompre les gens lorsqu'ils sont occupés?\n	",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs19',
                text="Certains de ces comportements étaient-ils présents avant l’âge de 7 ans ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs2',
                text="2. A quelle fréquence vous arrive-t-il d'avoir des difficultés à mettre les choses en ordre lorsque vous devez faire quelque chose qui demande de l'organisation ?",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs3',
                text="3. A quelle fréquence vous arrive-t-il d'avoir des difficultés à vous rappeler vos rendez-vous ou vos obligations ?",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs4',
                text="4. Quand vous devez faire quelque chose qui demande beaucoup de réflexion, à quelle fréquence vous arrive-t-il d'éviter de le faire ou de le remettre à plus tard'",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs5',
                text="5. À quelle fréquence vous arrive-t-il de remuer ou de tortiller les mains ou les pieds lorsque vous devez rester assis pendant une période prolongée?",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs6',
                text="6. À quelle fréquence vous arrive-t-il de vous sentir excessivement actif et contraint de faire quelque chose, comme si vous étiez entraîné malgré vous par un moteur?",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs7',
                text="7. À quelle fréquence vous arrive-t-il de faire des fautes d'étourderie lorsque vous travaillez à un projet ennuyeux ou difficile?",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs8',
                text="8. À quelle fréquence vous arrive-t-il d'avoir des difficultés à vous concentrer lorsque vous faites un travail ennuyeux ou répétitif?",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='asrs9',
                text="9. À quelle fréquence vous arrive-t-il d'avoir des difficultés à vous concentrer sur les propos de votre interlocuteur, même s?il s?adresse directement à vous?",
                options=[
                    AnswerOption(value='a', label="jamais", score=0),
                    AnswerOption(value='b', label="Rarement", score=1),
                    AnswerOption(value='c', label="Quelquefois", score=2),
                    AnswerOption(value='d', label="Souvent", score=3),
                    AnswerOption(value='e', label="très souvent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="ASRS",
            name="ASRS Questionnaire",
            description="19 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=9,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute ASRS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
