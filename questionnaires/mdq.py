"""
MDQ - MDQ Questionnaire
=======================

11 items questionnaire

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


@register_questionnaire("MDQ")
@dataclass
class Mdq(BaseQuestionnaire):
    """MDQ Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize MDQ questionnaire with all 11 items."""
        
        questions_list = [
            Question(
                id='mdq1',
                text="vous vous sentiez si bien et si remonté que d’autres personnes pensaient que vous n’étiez pas comme\nd’habitude ou que vous étiez si remonté que vous alliez vous attirer des ennuis",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mdq12',
                text="vous faisiez des choses inhabituelles pour vous ou que d’autres gens pensaient être excessives,\nimprudentes ou risquéess",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mdq13',
                text="vous dépensiez de l’argent de manière si inadaptée que cela vous attirait des ennuis ou à votre famille",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mdq14',
                text="2.Vous avez coché « oui » à plus d’une des questions précédentes, est-ce que plusieurs d’entre elles\nsont apparues durant la même période de temps ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mdq15',
                text="v3. A quel point, une de ces questions a été pour vous un problème au point de ne plus travailler, d’avoir\ndes difficultés familiales, légales, d’argent, de vous inciter à des bagarres ou des disputes ?",
                options=[
                    AnswerOption(value='a', label="pas de problème", score=0),
                    AnswerOption(value='b', label="problème mineur", score=1),
                    AnswerOption(value='c', label="problème moyen", score=2),
                    AnswerOption(value='d', label="problème sérieux", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mdq16',
                text="MDQ",
                options=[
                    AnswerOption(value='a', label="Positif", score=0),
                    AnswerOption(value='b', label="Négatif", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mdq2',
                text="vous étiez si irritable que vous criiez après les gens ou que vous provoquiez des bagarres ou des\ndisputes",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mdq4',
                text="vous dormiez beaucoup moins que d’habitude et trouviez que cela ne vous manquait pas vraiment",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mdq6',
                text="des pensées traversaient rapidement votre tête et vous ne pouviez pas les ralentir",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mdq8',
                text="vous aviez beaucoup plus d’énergie que d’habitude",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mdq_score',
                text="BIPOLAIRE",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="MDQ",
            name="MDQ Questionnaire",
            description="11 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute MDQ score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
