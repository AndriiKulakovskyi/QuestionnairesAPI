"""
AUT_C1QDCA - AUT_C1QDCA Questionnaire
=====================================

9 items questionnaire

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


@register_questionnaire("AUT_C1QDCA")
@dataclass
class AutC1qdca(BaseQuestionnaire):
    """AUT_C1QDCA Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_C1QDCA questionnaire with all 9 items."""
        
        questions_list = [
            Question(
                id='cogsoc',
                text="Un bilan des cognitions sociales a-t-il été réalisé ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lis',
                text="La Lecture Intentionnelle des Situations  (LIS) a-t-elle été réalisée ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='nivcotot',
                text="AU TOTAL, le niveau cognitif du sujet est jugé comme ",
                options=[
                    AnswerOption(value='a', label="Normal Le meilleur score QIV, QIP ou QIT >= 85", score=0),
                    AnswerOption(value='b', label="Limite Le meilleur score QIV, QIP ou QIT 85<>=70", score=1),
                    AnswerOption(value='c', label="Retard mental Le meilleur score QIV, QIP ou QIT < 70", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qirea',
                text="Un QI a-t-il déjà été réalisé ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qit',
                text="QIT",
                options=[
                    AnswerOption(value='a', label="homogène", score=0),
                    AnswerOption(value='b', label="hétérogène", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='vine',
                text="Une Vineland a-t-elle été réalisée ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wai4',
                text="WAIS IV",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wis4',
                text="WISC IV",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wis5',
                text="WISC V",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_C1QDCA",
            name="AUT_C1QDCA Questionnaire",
            description="9 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_C1QDCA score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
