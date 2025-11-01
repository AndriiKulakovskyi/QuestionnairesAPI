"""
AUT_BIS10 - AUT_BIS10 Questionnaire
===================================

34 items questionnaire

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


@register_questionnaire("AUT_BIS10")
@dataclass
class AutBis10(BaseQuestionnaire):
    """AUT_BIS10 Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_BIS10 questionnaire with all 34 items."""
        
        questions_list = [
            Question(
                id='bis10_1',
                text="1.Je prépare soigneusement les tâches à accomplir",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasionnellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_10',
                text="10.Je mets de l'argent de côté régulièrement",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_11',
                text="11.J'ai « la bougeotte » aux spectacles ou aux conférences",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_12',
                text="12.Je réfléchis soigneusement",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_13',
                text="13.Je veille à ma sécurité d'emploi",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_14',
                text="14.Je dis les choses sans y penser",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_15',
                text="15.J'aime réfléchir à des problèmes complexes",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_16',
                text="16.Je change de travail",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_17',
                text="17.J'agis sur un coup de tête",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_18',
                text="18.Réfléchir à un problème m'ennuie vite",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_19',
                text="19.Je me fais faire régulièrement des bilans de santé",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_2',
                text="2.Je fais les choses sans y penser",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_20',
                text="20.J'agis selon l'inspiration du moment",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_21',
                text="21.Je suis quelqu'un de réfléchi",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_22',
                text="22.Je change de domicile",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_23',
                text="23.J'achète les choses sur un 'coup de tête'",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_24',
                text="24.Je ne peux penser qu’à un problème à la fois",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_25',
                text="25.Je change de passe-temps",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_26',
                text="26.Je marche et bouge vite",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_27',
                text="27.Je résous les problèmes par tâtonnements",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_28',
                text="28.Je dépense ou paye à crédit plus que je ne gagne",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_29',
                text="29.Je parle vite",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_3',
                text="3.Je me décide rapidement",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_30',
                text="30.Quand je réfléchis, mes pensées s'égarent souvent",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_31',
                text="31.Je m'intéresse plus au présent qu'à l'avenir",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_32',
                text="32.Je me sens agité aux spectacles ou lors de conférences",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_33',
                text="33.J’aime les 'casses têtes'",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_34',
                text="34.Je pense à l'avenir",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_4',
                text="4.J'ai tendance à ne pas m'en faire",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_5',
                text="5.Je ne fais pas attention",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_6',
                text="6.J'ai des idées qui fusent",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_7',
                text="7.Je projette mes voyages longtemps à l'avance",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_8',
                text="8.Je suis maître de moi",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bis10_9',
                text="9.Je me concentre facilement",
                options=[
                    AnswerOption(value='a', label="Rarement/ jamais", score=0),
                    AnswerOption(value='b', label="Occasion-nellement", score=1),
                    AnswerOption(value='c', label="Souvent", score=2),
                    AnswerOption(value='d', label="Presque toujours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_BIS10",
            name="AUT_BIS10 Questionnaire",
            description="34 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=17,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_BIS10 score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
