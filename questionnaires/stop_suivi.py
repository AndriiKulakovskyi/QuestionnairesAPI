"""
STOP_SUIVI - STOP_SUIVI Questionnaire
=====================================

3 items questionnaire

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


@register_questionnaire("STOP_SUIVI")
@dataclass
class StopSuivi(BaseQuestionnaire):
    """STOP_SUIVI Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize STOP_SUIVI questionnaire with all 3 items."""
        
        questions_list = [
            Question(
                id='causdc',
                text="Cause du décès",
                options=[
                    AnswerOption(value='a', label="Suicide", score=0),
                    AnswerOption(value='b', label="Décès lié aux comorbidités", score=1),
                    AnswerOption(value='c', label="Pathologie somatique", score=2),
                    AnswerOption(value='d', label="Mort violente", score=3),
                    AnswerOption(value='e', label="Autre", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fin_suivi',
                text="Le patient n'est plus suivi dans le Centre Expert, spécifier le motif\n        ",
                options=[
                    AnswerOption(value='a', label="Patient non autiste", score=0),
                    AnswerOption(value='b', label="Autre crière non compatible au niveau du screening", score=1),
                    AnswerOption(value='c', label="Patient ne désirant pas être revu", score=2),
                    AnswerOption(value='d', label="Patient décédé", score=3),
                    AnswerOption(value='e', label="Patient a déménagé", score=4),
                    AnswerOption(value='f', label="Perdu de vue", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rdv_manque',
                text="Le patient ne s'est pas rendu à la consultation prévue, spécifier le motif",
                options=[
                    AnswerOption(value='a', label="Patient indisponible", score=0),
                    AnswerOption(value='b', label="Etat clinique du patient non compatible avec l'évaluation", score=1),
                    AnswerOption(value='c', label="Annulation de la part du Centre Expert", score=2),
                    AnswerOption(value='d', label="Autre", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="STOP_SUIVI",
            name="STOP_SUIVI Questionnaire",
            description="3 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute STOP_SUIVI score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
