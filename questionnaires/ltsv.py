"""
LTSV - LTSV Questionnaire
=========================

4 items questionnaire

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


@register_questionnaire("LTSV")
@dataclass
class Ltsv(BaseQuestionnaire):
    """LTSV Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize LTSV questionnaire with all 4 items."""
        
        questions_list = [
            Question(
                id='ltsv1',
                text="Méthode de la TS la plus violente:",
                options=[
                    AnswerOption(value='a', label="Arme à feu", score=0),
                    AnswerOption(value='b', label="Immolation", score=1),
                    AnswerOption(value='c', label="Noyade", score=2),
                    AnswerOption(value='d', label="Saut", score=3),
                    AnswerOption(value='e', label="Pendaison", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ltsv1spe1haut',
                text="Hauteur",
                options=[
                    AnswerOption(value='a', label="D’un endroit élevé", score=0),
                    AnswerOption(value='b', label="Hauteur modérée", score=1),
                    AnswerOption(value='c', label="Hauteur d’homme", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ltsv1spe1let',
                text="Létalité",
                options=[
                    AnswerOption(value='a', label="Contusions mineures seulement – pas besoin de traitement", score=0),
                    AnswerOption(value='b', label="Entorse ou blessure mineure - pas de dommage aux os, ligament, tendon, des tissus ou du cerveau, pas d’hémorragie interne", score=1),
                    AnswerOption(value='c', label="Fracture des extrémités - exploration nécessaire mais pas besoin d’une réparation majeure des tendons et rétablissement complet espéré", score=2),
                    AnswerOption(value='d', label="Dégâts majeurs aux tendons ou aux os à plusieurs endroits - hémorragies internes; quelques dommages résiduels prévu mais pas dans les zones vitales", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ltsv2spe',
                text="Quel est le déclencheur externe ?",
                options=[
                    AnswerOption(value='a', label="conjugal", score=0),
                    AnswerOption(value='b', label="autre facteur interpersonnel", score=1),
                    AnswerOption(value='c', label="professionnel", score=2),
                    AnswerOption(value='d', label="événement de vie", score=3),
                    AnswerOption(value='e', label="santé", score=4),
                    AnswerOption(value='f', label="autre", score=5),
                    AnswerOption(value='g', label="ne peut pas être évalué", score=6),
                    AnswerOption(value='h', label="abus sexuel", score=7),
                    AnswerOption(value='i', label="sévices physiques", score=8)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="LTSV",
            name="LTSV Questionnaire",
            description="4 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute LTSV score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
