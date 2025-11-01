"""
AUT_EQ5D - AUT_EQ5D Questionnaire
=================================

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


@register_questionnaire("AUT_EQ5D")
@dataclass
class AutEq5d(BaseQuestionnaire):
    """AUT_EQ5D Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_EQ5D questionnaire with all 3 items."""
        
        questions_list = [
            Question(
                id='mobility',
                text="MOBILITÉ",
                options=[
                    AnswerOption(value='a', label="Je n’ai aucun problème pour me déplacer à pied", score=0),
                    AnswerOption(value='b', label="J’ai des problèmes légers pour me déplacer à pied", score=1),
                    AnswerOption(value='c', label="J’ai des problèmes modérés pour me déplacer à pied", score=2),
                    AnswerOption(value='d', label="J’ai des problèmes sévères pour me déplacer à pied", score=3),
                    AnswerOption(value='e', label="Je suis incapable de me déplacer à pied", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pain',
                text="DOULEURS / GÊNE",
                options=[
                    AnswerOption(value='a', label="Je n’ai ni douleur, ni gêne", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='selfcare',
                text="AUTONOMIE DE LA PERSONNE",
                options=[
                    AnswerOption(value='a', label="Je n’ai aucun problème pour me laver ou m’habiller tout seul", score=0),
                    AnswerOption(value='b', label="J’ai des problèmes légers pour me laver ou m’habiller tout seul", score=1),
                    AnswerOption(value='c', label="J’ai des problèmes modérés pour me laver ou m’habiller tout seul", score=2),
                    AnswerOption(value='d', label="J’ai des problèmes sévères pour me laver ou m’habiller tout seul", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_EQ5D",
            name="AUT_EQ5D Questionnaire",
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
        """Compute AUT_EQ5D score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
