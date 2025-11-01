"""
TTT_DEUX_ANS - TTT_DEUX_ANS Questionnaire
=========================================

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


@register_questionnaire("TTT_DEUX_ANS")
@dataclass
class TttDeuxAns(BaseQuestionnaire):
    """TTT_DEUX_ANS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize TTT_DEUX_ANS questionnaire with all 3 items."""
        
        questions_list = [
            Question(
                id='ttt_deux_ans_1',
                text="Prise de psychotropes",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ttt_deux_ans_autres',
                text="Autres médicaments prescrits régulièrement",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ttt_deux_ans_causes',
                text="CAUSES",
                options=[
                    AnswerOption(value='a', label="pour dormir", score=0),
                    AnswerOption(value='b', label="pour l’humeur", score=1),
                    AnswerOption(value='c', label="pour des angoisses", score=2),
                    AnswerOption(value='d', label="idées délirantes, hallucinations", score=3),
                    AnswerOption(value='e', label="autre", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="TTT_DEUX_ANS",
            name="TTT_DEUX_ANS Questionnaire",
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
        """Compute TTT_DEUX_ANS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
