"""
AUT_FAGERSTROM - AUT_FAGERSTROM Questionnaire
=============================================

8 items questionnaire

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


@register_questionnaire("AUT_FAGERSTROM")
@dataclass
class AutFagerstrom(BaseQuestionnaire):
    """AUT_FAGERSTROM Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_FAGERSTROM questionnaire with all 8 items."""
        
        questions_list = [
            Question(
                id='fag_1',
                text="1.Combien de temps après votre réveil fumez-vous votre première cigarette ?",
                options=[
                    AnswerOption(value='a', label="dans les 5 minutes", score=0),
                    AnswerOption(value='b', label="de 6 à 30 minutes", score=1),
                    AnswerOption(value='c', label="de 31 à 60 minutes", score=2),
                    AnswerOption(value='d', label="après 60 minutes", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fag_2',
                text="2.Trouvez-vous difficile de vous abstenir de fumer dans les endroits où c'est interdit ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fag_3',
                text="3.A quelle cigarette de la journée vous serait-il le plus difficile de renoncer ?",
                options=[
                    AnswerOption(value='a', label="La première", score=0),
                    AnswerOption(value='b', label="n'importe quelle autre", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fag_4',
                text="4.Combien de cigarettes fumez-vous par jour ?",
                options=[
                    AnswerOption(value='a', label="10 ou moins", score=0),
                    AnswerOption(value='b', label="11-20", score=1),
                    AnswerOption(value='c', label="21-30", score=2),
                    AnswerOption(value='d', label="31 ou plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fag_5',
                text="5.Fumez-vous à un rythme plus soutenu le matin que l'après-midi ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fag_6',
                text="6.Fumez-vous lorsque vous êtes si malade que vous devez rester au lit presque toute la journée ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='q_deja_fume',
                text="Avez-vous déjà fumé des cigarettes ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='q_fume_actu',
                text="Fumez-vous actuellement ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_FAGERSTROM",
            name="AUT_FAGERSTROM Questionnaire",
            description="8 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_FAGERSTROM score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
