"""
PRISEM - PRISEM Questionnaire
=============================

32 items questionnaire

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


@register_questionnaire("PRISEM")
@dataclass
class Prisem(BaseQuestionnaire):
    """PRISEM Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize PRISEM questionnaire with all 32 items."""
        
        questions_list = [
            Question(
                id='prism01a',
                text="Diarrhée",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism01b',
                text="Constipation",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism01c',
                text="Bouche sèche",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism01d',
                text="Nausée, vomissement",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism02a',
                text="Palpitations",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism02b',
                text="Vertiges",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism02c',
                text="Douleurs dans la poitrine",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism03a',
                text="Augmentation de la transpiration",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism03b',
                text="Démangeaisons",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism03c',
                text="Sécheresse de la peau",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism04a',
                text="Mal à la tête",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism04b',
                text="Tremblements",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism04c',
                text="Mauvais contrôle moteur",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism04d',
                text="Etourdissements",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism05a',
                text="Vision floue",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism05b',
                text="Acouphènes (bourdonnements dans les oreilles)",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism06a',
                text="Difficultés pour uriner",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism06b',
                text="Mictions douloureuses",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism06c',
                text="Mictions fréquentes",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism06d',
                text="Règles irrégulières (pour les femmes)",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism07a',
                text="Difficultés d'endormissement",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism07b',
                text="Augmentation du temps de sommeil",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism08a',
                text="Perte du désir sexuel",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism08b',
                text="Difficultés à atteindre un orgasme",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism08c',
                text="Troubles de l'érection (pour les hommes)",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism09a',
                text="Anxiété",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism09b',
                text="Difficultés de concentration",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism09c',
                text="Malaise général",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism09d',
                text="Agitation",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism09e',
                text="Fatigue",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism09f',
                text="Diminution de l'énergie",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prism09g',
                text="Prise de poids",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Tolérable", score=1),
                    AnswerOption(value='c', label="Pénible", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="PRISEM",
            name="PRISEM Questionnaire",
            description="32 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=16,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute PRISEM score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
