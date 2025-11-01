"""
STAYA - STAYA Questionnaire
===========================

20 items questionnaire

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


@register_questionnaire("STAYA")
@dataclass
class Staya(BaseQuestionnaire):
    """STAYA Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize STAYA questionnaire with all 20 items."""
        
        questions_list = [
            Question(
                id='staya01',
                text="1. Je me sens calme.",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya02',
                text="2. Je me sens en sécurité, sans inquiétude, en sûreté",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya03',
                text="3. Je suis tendu(e), crispé(e)",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya04',
                text="4. Je me sens surmené(e). ",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya05',
                text="5. Je me sens tranquille, bien dans ma peau. ",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya06',
                text="6. Je me sens ému(e), bouleversé(e), contrarié(e). ",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya07',
                text="7. L'idée de malheurs éventuels me tracasse en ce moment. ",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya08',
                text="8. Je me sens content(e). ",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya09',
                text="9. Je me sens effrayé(e) ",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya10',
                text="10. Je me sens à mon aise",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya11',
                text="11. Je sens que j'ai confiance en moi",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya12',
                text="12. Je me sens nerveux (nerveuse), irritable",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya13',
                text="13. J'ai la frousse, la trouille (j'ai peur).",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya14',
                text="14. Je me sens indécis(e). ",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya15',
                text="15. Je suis décontracté(e), détendu(e).",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya16',
                text="16. Je suis satisfait(e).",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya17',
                text="17. Je suis inquiet, soucieux (inquiète, soucieuse) ",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya18',
                text="18. Je ne sais plus où j'en suis, je me sens déconcerté(e), dérouté(e). ",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya19',
                text="19. Je me sens solide, posé(e), pondéré(e), réfléchi(e).",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='staya20',
                text="20. Je me sens de bonne humeur, aimable",
                options=[
                    AnswerOption(value='a', label="non", score=0),
                    AnswerOption(value='b', label="plutôt non", score=1),
                    AnswerOption(value='c', label="plutôt oui", score=2),
                    AnswerOption(value='d', label="oui", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="STAYA",
            name="STAYA Questionnaire",
            description="20 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=10,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute STAYA score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
