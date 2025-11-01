"""
SPIN - SPIN Questionnaire
=========================

17 items questionnaire

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


@register_questionnaire("SPIN")
@dataclass
class Spin(BaseQuestionnaire):
    """SPIN Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize SPIN questionnaire with all 17 items."""
        
        questions_list = [
            Question(
                id='spin1',
                text="1. J’ai peur des gens en position d’autorité.",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Extrêmement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spin10',
                text="10. Parler à des inconnus me fait peur.",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Extrêmement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spin11',
                text="11. J’évite d’avoir à parler en public.",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Extrêmement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spin12',
                text="12. Je ferais n’importe quoi pour éviter d’être critiqué.",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Extrêmement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spin13',
                text="13. Avoir des palpitations cardiaques me dérange quand il y a des gens près de moi.",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Extrêmement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spin14',
                text="14. Cela me gêne de faire certaines choses quand des\ngens pourraient être en train de regarder.",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Extrêmement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spin15',
                text="15. Être embarrassé en public ou avoir l’air stupide fait partie de mes pires craintes.",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Extrêmement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spin16',
                text="16. J’évite de parler à toute personne en situation d’autorité.",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Extrêmement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spin17',
                text="17. Trembler devant les autres me dérange.",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Extrêmement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spin2',
                text="2. Je suis mal à l’aise de rougir en public",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Extrêmement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spin3',
                text="3. Les soirées et les autres événements en groupe me font peur.",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Extrêmement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spin4',
                text="4. J’évite de parler aux gens que je ne connais pas.",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Extrêmement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spin5',
                text="5. Me faire critiquer m’effraie beaucoup.",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Extrêmement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spin6',
                text="6. La peur d’être dans l’embarras me pousse à éviter de faire des choses ou de parler aux gens.",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Extrêmement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spin7',
                text="7. Transpirer devant les gens me perturbe.",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Extrêmement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spin8',
                text="8. J’évite d’aller dans les soirées.",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Extrêmement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='spin9',
                text="9. J’évite les activités où je suis le centre d’attention.",
                options=[
                    AnswerOption(value='a', label="Pas du tout", score=0),
                    AnswerOption(value='b', label="Légèrement", score=1),
                    AnswerOption(value='c', label="Moyennement", score=2),
                    AnswerOption(value='d', label="Beaucoup", score=3),
                    AnswerOption(value='e', label="Extrêmement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="SPIN",
            name="SPIN Questionnaire",
            description="17 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=8,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute SPIN score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
