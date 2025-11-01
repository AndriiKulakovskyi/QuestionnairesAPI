"""
AUT_HAM_ANX - AUT_HAM_ANX Questionnaire
=======================================

5 items questionnaire

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


@register_questionnaire("AUT_HAM_ANX")
@dataclass
class AutHamAnx(BaseQuestionnaire):
    """AUT_HAM_ANX Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_HAM_ANX questionnaire with all 5 items."""
        
        questions_list = [
            Question(
                id='hamanx10',
                text="10. Symptômes respiratoires Sensations de constriction ou de contraction dans la gorge ou la poitrine et respiration soupirante\n                    ",
                options=[
                    AnswerOption(value='a', label="Absents", score=0),
                    AnswerOption(value='b', label="Présence peu claire", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamanx13',
                text="13. Autres symptômes du SNA Cet item inclut la sècheresse buccale, les rougeurs ou la pâleur, les bouffées de transpiration et les vertiges\n                    ",
                options=[
                    AnswerOption(value='a', label="Absents", score=0),
                    AnswerOption(value='b', label="Présence peu claire.", score=1),
                    AnswerOption(value='c', label="Un ou plusieurs symptômes autonomes sont présents, mais n'interfèrent pas avec la vie quotidienne et le", score=2),
                    AnswerOption(value='d', label="Occasionnellement, un ou plusieurs symptômes autonomes sont présents à un degré tel qu'ils interfèrent", score=3),
                    AnswerOption(value='e', label="Les symptômes sont présents la plupart du temps et interfèrent clairement avec la vie quotidienne et le travail", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamanx6',
                text="6. Humeur dépressive:Cet item couvre à la fois la communication non-verbale de la tristesse, de la déprime, de l'abattement, de la sensation d'impuissance, et de la perte d'espoir\n                    ",
                options=[
                    AnswerOption(value='a', label="Absente", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamanx8',
                text="8. Symptômes somatiques généraux : sensoriels\n  Cet item inclut une fatigabilité accrue ainsi que de la faiblesse ou des perturbations réelles des sens, incluant\n l'acouphène, la vision floue, des bouffées de chaleur ou de froid, et des sensations de fourmillements\n                    ",
                options=[
                    AnswerOption(value='a', label="Absent", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamanx9',
                text="9. Symptômes cardio-vasculaires: Cet item inclut la tachycardie, les palpitations, l'oppression, la douleur dans la poitrine, la sensation de pulsations,:de « cognement » dans les vaisseaux sanguins, ainsi que la sensation de devoir s'évanouir\n                    ",
                options=[
                    AnswerOption(value='a', label="Absents", score=0),
                    AnswerOption(value='b', label="Leur présence n'est pas claire", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_HAM_ANX",
            name="AUT_HAM_ANX Questionnaire",
            description="5 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_HAM_ANX score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
