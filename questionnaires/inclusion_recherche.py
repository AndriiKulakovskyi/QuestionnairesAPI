"""
INCLUSION_RECHERCHE - INCLUSION_RECHERCHE Questionnaire
=======================================================

1 item questionnaire

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


@register_questionnaire("INCLUSION_RECHERCHE")
@dataclass
class InclusionRecherche(BaseQuestionnaire):
    """INCLUSION_RECHERCHE Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize INCLUSION_RECHERCHE questionnaire with all 1 items."""
        
        questions_list = [
            Question(
                id='inclusion',
                text="Liste des projets de recherche",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="INCLUSION_RECHERCHE",
            name="INCLUSION_RECHERCHE Questionnaire",
            description="1 item questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute INCLUSION_RECHERCHE score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
