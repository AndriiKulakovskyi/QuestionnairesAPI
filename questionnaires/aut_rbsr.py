"""
AUT_RBSR - AUT_RBSR Questionnaire
=================================

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


@register_questionnaire("AUT_RBSR")
@dataclass
class AutRbsr(BaseQuestionnaire):
    """AUT_RBSR Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_RBSR questionnaire with all 9 items."""
        
        questions_list = [
            Question(
                id='rbsr30',
                text="30.Refuse de visiter de nouveaux lieux",
                options=[
                    AnswerOption(value='a', label="le comportement n’est pas présent", score=0),
                    AnswerOption(value='b', label="le comportement est présent et est un problème léger", score=1),
                    AnswerOption(value='c', label="le comportement est présent et est un problème modéré", score=2),
                    AnswerOption(value='d', label="le comportement est présent et est un problème sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rbsr31',
                text="31.S’énerve lorsqu’on l’interrompt dans ce qu’il / elle fait",
                options=[
                    AnswerOption(value='a', label="le comportement n’est pas présent", score=0),
                    AnswerOption(value='b', label="le comportement est présent et est un problème léger", score=1),
                    AnswerOption(value='c', label="le comportement est présent et est un problème modéré", score=2),
                    AnswerOption(value='d', label="le comportement est présent et est un problème sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rbsr33',
                text="33.Insiste pour s’asseoir à la même place",
                options=[
                    AnswerOption(value='a', label="le comportement n’est pas présent", score=0),
                    AnswerOption(value='b', label="le comportement est présent et est un problème léger", score=1),
                    AnswerOption(value='c', label="le comportement est présent et est un problème modéré", score=2),
                    AnswerOption(value='d', label="le comportement est présent et est un problème sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rbsr34',
                text="34.N’aime pas les changements dans le comportement ou l’apparence des gens autour de lui / elle",
                options=[
                    AnswerOption(value='a', label="le comportement n’est pas présent", score=0),
                    AnswerOption(value='b', label="le comportement est présent et est un problème léger", score=1),
                    AnswerOption(value='c', label="le comportement est présent et est un problème modéré", score=2),
                    AnswerOption(value='d', label="le comportement est présent et est un problème sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rbsr35',
                text="35.Insiste pour utiliser une porte en particulier",
                options=[
                    AnswerOption(value='a', label="le comportement n’est pas présent", score=0),
                    AnswerOption(value='b', label="le comportement est présent et est un problème léger", score=1),
                    AnswerOption(value='c', label="le comportement est présent et est un problème modéré", score=2),
                    AnswerOption(value='d', label="le comportement est présent et est un problème sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rbsr36',
                text="36.Aime entendre continuellement les mêmes CD, cassettes, enregistrements ou morceaux musicaux. Aime regarder les mêmes films / vidéos ou morceaux de films / vidéos",
                options=[
                    AnswerOption(value='a', label="le comportement n’est pas présent", score=0),
                    AnswerOption(value='b', label="le comportement est présent et est un problème léger", score=1),
                    AnswerOption(value='c', label="le comportement est présent et est un problème modéré", score=2),
                    AnswerOption(value='d', label="le comportement est présent et est un problème sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rbsr37',
                text="37.Résiste aux changements d’activité. Difficultés avec les transitions",
                options=[
                    AnswerOption(value='a', label="le comportement n’est pas présent", score=0),
                    AnswerOption(value='b', label="le comportement est présent et est un problème léger", score=1),
                    AnswerOption(value='c', label="le comportement est présent et est un problème modéré", score=2),
                    AnswerOption(value='d', label="le comportement est présent et est un problème sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rbsr38',
                text="38.Insiste pour avoir chaque jour un même programme de ménage, d’école ou de travail ",
                options=[
                    AnswerOption(value='a', label="le comportement n’est pas présent", score=0),
                    AnswerOption(value='b', label="le comportement est présent et est un problème léger", score=1),
                    AnswerOption(value='c', label="le comportement est présent et est un problème modéré", score=2),
                    AnswerOption(value='d', label="le comportement est présent et est un problème sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rbsr39',
                text="39.Insiste pour que chaque chose soit réalisée à une heure précise",
                options=[
                    AnswerOption(value='a', label="le comportement n’est pas présent", score=0),
                    AnswerOption(value='b', label="le comportement est présent et est un problème léger", score=1),
                    AnswerOption(value='c', label="le comportement est présent et est un problème modéré", score=2),
                    AnswerOption(value='d', label="le comportement est présent et est un problème sévère", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_RBSR",
            name="AUT_RBSR Questionnaire",
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
        """Compute AUT_RBSR score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
