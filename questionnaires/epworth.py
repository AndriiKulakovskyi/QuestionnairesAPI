"""
EPWORTH - EPWORTH Questionnaire
===============================

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


@register_questionnaire("EPWORTH")
@dataclass
class Epworth(BaseQuestionnaire):
    """EPWORTH Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize EPWORTH questionnaire with all 9 items."""
        
        questions_list = [
            Question(
                id='ess01',
                text="1. Assis en train de lire",
                options=[
                    AnswerOption(value='a', label="Ne somnolerait jamais", score=0),
                    AnswerOption(value='b', label="faible chance de s'endormir", score=1),
                    AnswerOption(value='c', label="chance moyenne de s'endormir", score=2),
                    AnswerOption(value='d', label="forte chance de s'endormir", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ess02',
                text="2. En train de regarder la télévision",
                options=[
                    AnswerOption(value='a', label="Ne somnolerait jamais", score=0),
                    AnswerOption(value='b', label="faible chance de s'endormir", score=1),
                    AnswerOption(value='c', label="chance moyenne de s'endormir", score=2),
                    AnswerOption(value='d', label="forte chance de s'endormir", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ess03',
                text="3. Assis, inactif, dans un endroit public (au théâtre, en réunion)",
                options=[
                    AnswerOption(value='a', label="Ne somnolerait jamais", score=0),
                    AnswerOption(value='b', label="faible chance de s'endormir", score=1),
                    AnswerOption(value='c', label="chance moyenne de s'endormir", score=2),
                    AnswerOption(value='d', label="forte chance de s'endormir", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ess04',
                text="4. Comme passager dans une voiture roulant sans arrêt pendant une heure",
                options=[
                    AnswerOption(value='a', label="Ne somnolerait jamais", score=0),
                    AnswerOption(value='b', label="faible chance de s'endormir", score=1),
                    AnswerOption(value='c', label="chance moyenne de s'endormir", score=2),
                    AnswerOption(value='d', label="forte chance de s'endormir", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ess05',
                text="5. Allongé l'après-midi pour se reposer quand les circonstances le permettent",
                options=[
                    AnswerOption(value='a', label="Ne somnolerait jamais", score=0),
                    AnswerOption(value='b', label="faible chance de s'endormir", score=1),
                    AnswerOption(value='c', label="chance moyenne de s'endormir", score=2),
                    AnswerOption(value='d', label="forte chance de s'endormir", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ess06',
                text="6. Assis en train de parler à quelqu'un",
                options=[
                    AnswerOption(value='a', label="Ne somnolerait jamais", score=0),
                    AnswerOption(value='b', label="faible chance de s'endormir", score=1),
                    AnswerOption(value='c', label="chance moyenne de s'endormir", score=2),
                    AnswerOption(value='d', label="forte chance de s'endormir", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ess07',
                text="7. Assis calmement après un repas sans alcool",
                options=[
                    AnswerOption(value='a', label="Ne somnolerait jamais", score=0),
                    AnswerOption(value='b', label="faible chance de s'endormir", score=1),
                    AnswerOption(value='c', label="chance moyenne de s'endormir", score=2),
                    AnswerOption(value='d', label="forte chance de s'endormir", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ess08',
                text="8. Dans une auto immobilisée quelques minutes dans un encombrement",
                options=[
                    AnswerOption(value='a', label="Ne somnolerait jamais", score=0),
                    AnswerOption(value='b', label="faible chance de s'endormir", score=1),
                    AnswerOption(value='c', label="chance moyenne de s'endormir", score=2),
                    AnswerOption(value='d', label="forte chance de s'endormir", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ess09',
                text="Ces envies de dormir surviennent-elles ",
                options=[
                    AnswerOption(value='a', label="seulement après les repas", score=0),
                    AnswerOption(value='b', label="à certaines heures du jour, toujours les mêmes ", score=1),
                    AnswerOption(value='c', label="la nuit", score=2),
                    AnswerOption(value='d', label="à n'importe quelle heure du jour ", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="EPWORTH",
            name="EPWORTH Questionnaire",
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
        """Compute EPWORTH score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
