"""
OPPOSITION - OPPOSITION Questionnaire
=====================================

2 items questionnaire

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


@register_questionnaire("OPPOSITION")
@dataclass
class Opposition(BaseQuestionnaire):
    """OPPOSITION Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize OPPOSITION questionnaire with all 2 items."""
        
        questions_list = [
            Question(
                id='forms_opp',
                text="Formulaires de non opposition",
                options=[
                    AnswerOption(value='a', label="Patient majeur", score=0),
                    AnswerOption(value='b', label="Patient sous curatelle", score=1),
                    AnswerOption(value='c', label="Patient sous tutelle", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='opposition',
                text="Opposition/Non opposition",
                options=[
                    AnswerOption(value='a', label="Ne s'oppose pas au recueil et à l'utilisation d'informations réalisés à partir de son dossier médical", score=0),
                    AnswerOption(value='b', label="S'oppose au recueil et à l'utilisation d'informations réalisés à partir de son dossier médical", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="OPPOSITION",
            name="OPPOSITION Questionnaire",
            description="2 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute OPPOSITION score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
