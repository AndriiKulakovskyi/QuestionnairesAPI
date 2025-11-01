"""
EQ5D - EQ5D Questionnaire
=========================

5 items questionnaire

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


@register_questionnaire("EQ5D")
@dataclass
class Eq5d(BaseQuestionnaire):
    """EQ5D Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize EQ5D questionnaire with all 5 items."""
        
        questions_list = [
            Question(
                id='radhtml_eq5d_activite',
                text="Activités courantes (exemples : travail, études, travaux domestiques, activités familiales ou loisirs)",
                options=[
                    AnswerOption(value='a', label="Je n'ai aucun problème pour accomplir mes activités courantes", score=0),
                    AnswerOption(value='b', label="J'ai des problèmes légers pour accomplir mes activités courantes", score=1),
                    AnswerOption(value='c', label="J'ai des problèmes modérés pour accomplir mes activités courantes", score=2),
                    AnswerOption(value='d', label="J'ai des problèmes sévères pour accomplir mes activités courantes", score=3),
                    AnswerOption(value='e', label="Je suis incapable d'accomplir mes activités courantes", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_eq5d_anxiete',
                text="Anxiété, dépression",
                options=[
                    AnswerOption(value='a', label="Je ne suis ni anxieux(se), ni déprimé(e)", score=0),
                    AnswerOption(value='b', label="Je suis légèrement anxieux(se) ou déprimé(e)", score=1),
                    AnswerOption(value='c', label="Je suis modérément anxieux(se) ou déprimé(e)", score=2),
                    AnswerOption(value='d', label="Je suis sévèrement anxieux(se) ou déprimé(e)", score=3),
                    AnswerOption(value='e', label="Je suis extrêmement anxieux(se) ou déprimé(e)", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_eq5d_autonomie',
                text="Autonomie de la personne",
                options=[
                    AnswerOption(value='a', label="Je n'ai aucun problème pour me laver ou m'habiller tout seul", score=0),
                    AnswerOption(value='b', label="J'ai des problèmes légers pour me laver ou m'habiller tout seul", score=1),
                    AnswerOption(value='c', label="J'ai des problèmes modérés pour me laver ou m'habiller tout seul", score=2),
                    AnswerOption(value='d', label="J'ai des problèmes sévères pour me laver ou m'habiller tout seul", score=3),
                    AnswerOption(value='e', label="Je suis incapable de me laver ou de m'habiller tout(e) seul(e)", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_eq5d_douleur',
                text="Douleurs, gêne",
                options=[
                    AnswerOption(value='a', label="Je n'ai ni douleur, ni gêne", score=0),
                    AnswerOption(value='b', label="J'ai des douleurs ou une gêne légère(s)", score=1),
                    AnswerOption(value='c', label="J'ai des douleurs ou une gêne modérée(s)", score=2),
                    AnswerOption(value='d', label="J'ai des douleurs ou une gêne sévère(s)", score=3),
                    AnswerOption(value='e', label="J'ai des douleurs ou une gêne extrême(s)", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_eq5d_mobilite',
                text="Mobilité",
                options=[
                    AnswerOption(value='a', label="Je n'ai aucun problème pour me déplacer à pied", score=0),
                    AnswerOption(value='b', label="J'ai des problèmes légers pour me déplacer à pied", score=1),
                    AnswerOption(value='c', label="J'ai des problèmes modérés pour me déplacer à pied", score=2),
                    AnswerOption(value='d', label="J'ai des problèmes sévères pour me déplacer à pied", score=3),
                    AnswerOption(value='e', label="Je suis incapable de me déplacer à pied", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="EQ5D",
            name="EQ5D Questionnaire",
            description="5 items questionnaire",
            pathology_domain=PathologyDomain.SCHIZOPHRENIA,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute EQ5D score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
