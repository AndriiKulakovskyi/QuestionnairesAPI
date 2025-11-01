"""
EQ5D5L - EQ5D5L Questionnaire
=============================

4 items questionnaire

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


@register_questionnaire("EQ5D5L")
@dataclass
class Eq5d5l(BaseQuestionnaire):
    """EQ5D5L Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize EQ5D5L questionnaire with all 4 items."""
        
        questions_list = [
            Question(
                id='eq5d5l_activite',
                text="ACTIVITES COURANTES",
                options=[
                    AnswerOption(value='a', label="Je n’ai aucun problème pour accomplir mes activités courantes", score=0),
                    AnswerOption(value='b', label="J’ai des problèmes légers pour accomplir mes activités courantes", score=1),
                    AnswerOption(value='c', label="J’ai des problèmes modérés pour accomplir mes activités courantes", score=2),
                    AnswerOption(value='d', label="J’ai des problèmes sévères pour accomplir mes activités courantes", score=3),
                    AnswerOption(value='e', label="Je suis incapable d’accomplir mes activités courantes", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='eq5d5l_autonomie',
                text="AUTONOMIE DE LA PERSONNE",
                options=[
                    AnswerOption(value='a', label="Je n’ai aucun problème pour me laver ou m’habiller tout seul", score=0),
                    AnswerOption(value='b', label="J’ai des problèmes légers pour me laver ou m’habiller tout seul", score=1),
                    AnswerOption(value='c', label="J’ai des problèmes modérés pour me laver ou m’habiller tout seul", score=2),
                    AnswerOption(value='d', label="J’ai des problèmes sévères pour me laver ou m’habiller tout seul", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='eq5d5l_dou_gene',
                text="DOULEURS / GENE",
                options=[
                    AnswerOption(value='a', label="Je n’ai ni douleur, ni gêne", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='eq5d5l_mobilite',
                text="MOBILITE",
                options=[
                    AnswerOption(value='a', label="Je n’ai aucun problème pour me déplacer à pied", score=0),
                    AnswerOption(value='b', label="J’ai des problèmes légers pour me déplacer à pied", score=1),
                    AnswerOption(value='c', label="J’ai des problèmes modérés pour me déplacer à pied", score=2),
                    AnswerOption(value='d', label="J’ai des problèmes sévères pour me déplacer à pied", score=3),
                    AnswerOption(value='e', label="Je suis incapable de me déplacer à pied", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="EQ5D5L",
            name="EQ5D5L Questionnaire",
            description="4 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute EQ5D5L score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
