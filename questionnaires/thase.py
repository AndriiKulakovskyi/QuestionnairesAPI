"""
THASE - THASE Questionnaire
===========================

1 item questionnaire

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


@register_questionnaire("THASE")
@dataclass
class Thase(BaseQuestionnaire):
    """THASE Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize THASE questionnaire with all 1 items."""
        
        questions_list = [
            Question(
                id='thase1',
                text="Criteres de resistance de Thase et Rush",
                options=[
                    AnswerOption(value='a', label="Niveau 1 : Résistance à un premier antidépresseur utilisé à doses suffisantes et pendant une durée adéquate.", score=0),
                    AnswerOption(value='b', label="Niveau 2 : Niveau 1 + échec à un autre antidépresseur d’une autre classe.", score=1),
                    AnswerOption(value='c', label="Niveau 3 : Niveau 2 + échec à un antidépresseur tricyclique.", score=2),
                    AnswerOption(value='d', label="Niveau 4 : Niveau 3 + échec à un inhibiteur de la monoamine oxydase.", score=3),
                    AnswerOption(value='e', label="Niveau 5 : Niveau 4 + échec de l’électroconvulsivothérapie bilatérale", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="THASE",
            name="THASE Questionnaire",
            description="1 item questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute THASE score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
