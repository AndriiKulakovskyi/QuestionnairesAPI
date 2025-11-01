"""
SUIVI - SUIVI Questionnaire
===========================

3 items questionnaire

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


@register_questionnaire("SUIVI")
@dataclass
class Suivi(BaseQuestionnaire):
    """SUIVI Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize SUIVI questionnaire with all 3 items."""
        
        questions_list = [
            Question(
                id='change_centre',
                text="Changement de centre?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fin_suivi',
                text="Le patient n'est plus suivi, spécifier le motif",
                options=[
                    AnswerOption(value='a', label="Changement de diagnostic", score=0),
                    AnswerOption(value='b', label="Refus du patient", score=1),
                    AnswerOption(value='c', label="Refus de son médecin", score=2),
                    AnswerOption(value='d', label="Patient décédé", score=3),
                    AnswerOption(value='e', label="Déménagement", score=4),
                    AnswerOption(value='f', label="Autre", score=5),
                    AnswerOption(value='g', label="Ne sais pas", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='suivi_deces',
                text="Spécifier la cause principal du décès",
                options=[
                    AnswerOption(value='a', label="Suicide", score=0),
                    AnswerOption(value='b', label="Somatique", score=1),
                    AnswerOption(value='c', label="Autre", score=2),
                    AnswerOption(value='d', label="Ne sais pas", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="SUIVI",
            name="SUIVI Questionnaire",
            description="3 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute SUIVI score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
