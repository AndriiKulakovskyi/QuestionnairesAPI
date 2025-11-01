"""
BVAQ - BVAQ Questionnaire
=========================

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


@register_questionnaire("BVAQ")
@dataclass
class Bvaq(BaseQuestionnaire):
    """BVAQ Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize BVAQ questionnaire with all 20 items."""
        
        questions_list = [
            Question(
                id='bvaq01',
                text="1. On me dit souvent que je dois parler davantage de mes sentiments. ",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq02',
                text="2. Il m'arrive rarement de me laisser aller à mon imagination",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq03',
                text="3. Je ne sais pas ce qui se passe au fond de moi-même",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq04',
                text="4. Même lorsque les autres se passionnent pour quelque chose, je demeure indifférent(e). ",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq05',
                text="5. Il n'y a pas grand-chose à comprendre aux émotions",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq06',
                text="6. Quand je suis bouleversé(e) par quelque chose, je parle aux autres de ce que je ressens. ",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq07',
                text="7. J'aime imaginer des histoires folles et pleines de fantaisie",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq08',
                text="8. Quand je me sens moche, je sais si j'ai peur, ou bien si je suis sombre, ou bien si je suis triste. ",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq09',
                text="9. Il m'arrive souvent d'être bouleversé(e) par des événements inattendus",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq10',
                text="10. Je trouve que l?on doit rester en contact avec ses sentiments ",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq11',
                text="11. Je sais exprimer mes sentiments verbalement",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq12',
                text="12. Rêvasser à des affaires ou événements irréels, c'est perdre son temps. ",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq13',
                text="13. Quand j'en ai marre de moi-même, je n'arrive pas à savoir si je suis triste, ou bien si j'ai peur, ou bien si je suis malheureux(se). ",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq14',
                text="14. J'accepte les déceptions sans émotion",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq15',
                text="15. Je trouve curieux que les autres analysent si souvent leurs émotions",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq16',
                text="16. Quand je parle aux gens, c'est plutôt de mes activités quotidiennes que de mes sentiments",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq17',
                text="17. Quand j'ai peu à faire, je passe du temps à rêvasser",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq18',
                text="18. Quand je suis d'une humeur radieuse, je sais si je suis enthousiaste, ou bien gai(e), ou bien fou(folle) de joie",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq19',
                text="19. Quand je vois quelqu'un pleurer avec abondance, je sens la tristesse m'envahir",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bvaq20',
                text="20. Quand je suis tendu(e), j'ai besoin de savoir avec précision d'où me vient cette sensation.",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="BVAQ",
            name="BVAQ Questionnaire",
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
        """Compute BVAQ score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
