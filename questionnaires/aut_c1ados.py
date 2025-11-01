"""
AUT_C1ADOS - AUT_C1ADOS Questionnaire
=====================================

10 items questionnaire

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


@register_questionnaire("AUT_C1ADOS")
@dataclass
class AutC1ados(BaseQuestionnaire):
    """AUT_C1ADOS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_C1ADOS questionnaire with all 10 items."""
        
        questions_list = [
            Question(
                id='adosnf',
                text="Examen",
                options=[
                    AnswerOption(value='a', label="Fait", score=0),
                    AnswerOption(value='b', label="Non fait", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag_cs_m1',
                text="Diagnostic Autisme selon ADOS",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag_cs_m2',
                text="Diagnostic Autisme selon ADOS",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag_cs_m3',
                text="Diagnostic Autisme selon ADOS",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag_cs_m4',
                text="Diagnostic Autisme selon ADOS",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag_tsa_m1',
                text="Diagnostic TSA selon ADOS",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag_tsa_m2',
                text="Diagnostic TSA selon ADOS",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag_tsa_m3',
                text="Diagnostic TSA selon ADOS",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag_tsa_m4',
                text="Diagnostic TSA selon ADOS",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='modsaisi',
                text="Module ADOS ",
                options=[
                    AnswerOption(value='a', label="Module 1", score=0),
                    AnswerOption(value='b', label="Module 2", score=1),
                    AnswerOption(value='c', label="Module 3", score=2),
                    AnswerOption(value='d', label="Module 4", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_C1ADOS",
            name="AUT_C1ADOS Questionnaire",
            description="10 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_C1ADOS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
