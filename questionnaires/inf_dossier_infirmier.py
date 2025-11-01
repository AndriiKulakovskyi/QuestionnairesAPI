"""
INF_DOSSIER_INFIRMIER - INF_DOSSIER_INFIRMIER Questionnaire
===========================================================

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


@register_questionnaire("INF_DOSSIER_INFIRMIER")
@dataclass
class InfDossierInfirmier(BaseQuestionnaire):
    """INF_DOSSIER_INFIRMIER Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize INF_DOSSIER_INFIRMIER questionnaire with all 5 items."""
        
        questions_list = [
            Question(
                id='ecg',
                text="Electrocardiogramme effectué",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ecg_envoi',
                text="ECG envoyé à un cardiologue ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ecg_valide',
                text="Demande de consultation ou d'avis auprès d'un cardiologue",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lateral',
                text="Latéralisation",
                options=[
                    AnswerOption(value='a', label="gaucher", score=0),
                    AnswerOption(value='b', label="droitier", score=1),
                    AnswerOption(value='c', label="ambidextre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tabac',
                text="Statut du patient vis-à-vis du Tabac :",
                options=[
                    AnswerOption(value='a', label="Non-fumeur", score=0),
                    AnswerOption(value='b', label="Ex fumeur", score=1),
                    AnswerOption(value='c', label="Fumeur actuel", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="INF_DOSSIER_INFIRMIER",
            name="INF_DOSSIER_INFIRMIER Questionnaire",
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
        """Compute INF_DOSSIER_INFIRMIER score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
