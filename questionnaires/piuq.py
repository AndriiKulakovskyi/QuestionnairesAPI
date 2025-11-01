"""
PIUQ - PIUQ Questionnaire
=========================

12 items questionnaire

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


@register_questionnaire("PIUQ")
@dataclass
class Piuq(BaseQuestionnaire):
    """PIUQ Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize PIUQ questionnaire with all 12 items."""
        
        questions_list = [
            Question(
                id='radhtml_piuq1',
                text="1.Pensez-vous à Internet lorsque vous faites autre chose?",
                options=[
                    AnswerOption(value='a', label="1.Jamais", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6.Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_piuq10',
                text="10.Est-ce que votre utilisation d’Internet vous cause des ennuis?",
                options=[
                    AnswerOption(value='a', label="1.Jamais", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6.Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_piuq11',
                text="11.Vous sentez-vous déprimé ou de mauvaise humeur quand vous n’êtes pas sur Internet et ces sensations cessent dès que vous vous connectez?",
                options=[
                    AnswerOption(value='a', label="1.Jamais", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6.Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_piuq12',
                text="12.Vous dites-vous quand vous êtes sur Internet: «encore quelques minutes et j’arrête»?",
                options=[
                    AnswerOption(value='a', label="1.Jamais", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6.Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_piuq2',
                text="2.Négligez-vous des tâches quotidiennes pour passer plus de temps sur Internet?",
                options=[
                    AnswerOption(value='a', label="1.Jamais", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6.Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_piuq3',
                text="3.Devriez-vous diminuer le temps passé sur Internet?",
                options=[
                    AnswerOption(value='a', label="1.Jamais", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6.Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_piuq4',
                text="4.Songez-vous souvent à Internet?",
                options=[
                    AnswerOption(value='a', label="1.Jamais", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6.Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_piuq5',
                text="5.Passez-vous du temps sur Internet alors que vous devriez dormir?",
                options=[
                    AnswerOption(value='a', label="1.Jamais", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6.Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_piuq6',
                text="6.Essayez-vous de diminuer le temps passé sur Internet sans y parvenir?",
                options=[
                    AnswerOption(value='a', label="1.Jamais", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6.Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_piuq7',
                text="7.Êtes-vous stressé si vous ne pouvez pas utiliser Internet aussi longtemps que prévu?",
                options=[
                    AnswerOption(value='a', label="1.Jamais", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6.Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_piuq8',
                text="8.Cachez-vous le temps que vous passez sur Internet?",
                options=[
                    AnswerOption(value='a', label="1.Jamais", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6.Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_piuq9',
                text="9.Êtes-vous stressé si vous ne pouvez pas utiliser Internet pendant plusieurs jours?",
                options=[
                    AnswerOption(value='a', label="1.Jamais", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6.Toujours", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="PIUQ",
            name="PIUQ Questionnaire",
            description="12 items questionnaire",
            pathology_domain=PathologyDomain.SCHIZOPHRENIA,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=6,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute PIUQ score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
