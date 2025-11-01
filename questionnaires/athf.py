"""
ATHF - ATHF Questionnaire
=========================

7 items questionnaire

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


@register_questionnaire("ATHF")
@dataclass
class Athf(BaseQuestionnaire):
    """ATHF Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize ATHF questionnaire with all 7 items."""
        
        questions_list = [
            Question(
                id='athfa1',
                text="A. Selon la posologie :",
                options=[
                    AnswerOption(value='a', label="A1 l’une des molécules < 4 semaines OU <100 mg/jour", score=0),
                    AnswerOption(value='b', label="A2 >= 4 semaines ET 100-199 mg/jour", score=1),
                    AnswerOption(value='c', label="A3 >= 4 semaines ET 200-299 mg/jour", score=2),
                    AnswerOption(value='d', label="A4 >= 4 semaines ET 300 mg/jour ou supérieur", score=3),
                    AnswerOption(value='e', label="Pas de prescription ou condition inexistante", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='athfa8',
                text="A. Lithium seul pour un EDM unipolaire (pour les patients bipolaires : les concentrations plasmatiques ont la priorité sur la posologie) : Par concentrations plasmatiques:",
                options=[
                    AnswerOption(value='a', label="A1 prescription < 4 semaines OU >= 4 semaines et concentration < 0.4 mEq/L", score=0),
                    AnswerOption(value='b', label="A2 >= 4 semaines ET concentration 0.41-0.6 mEq/L", score=1),
                    AnswerOption(value='c', label="A3 >= 4 semaines ET concentration > 0.6 mEq/L", score=2),
                    AnswerOption(value='d', label="A1 traitement < 4 semaines OU >= 4 semaines et posologie < 600 mg/jour", score=3),
                    AnswerOption(value='e', label="A2 >= 4 semaines et posologie 600-899 mg/jour", score=4),
                    AnswerOption(value='f', label="A3 >= 4 semaines et posologie 900 mg/jour", score=5),
                    AnswerOption(value='g', label="Pas de prescription ou condition inexistante", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='athfb6',
                text="B. ECT Bilateral",
                options=[
                    AnswerOption(value='a', label="B1 1-3 séances d’ECT Bilatéral", score=0),
                    AnswerOption(value='b', label="B2 4-6 séances d’ECT Bilatéral", score=1),
                    AnswerOption(value='c', label="B4 7-9 séances d’ECT Bilatéral", score=2),
                    AnswerOption(value='d', label="B5 >= 10 séances d’ECT Bilatéral", score=3),
                    AnswerOption(value='e', label="Pas de prescription ou condition inexistante", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='athfb8',
                text="B. Lithium comme agent de potentialisation",
                options=[
                    AnswerOption(value='a', label="B4 antidepresseur I - IX noté niveau 3 et Li au moins 2 semaines ou CBZ noté niveau 3 et Li au moins 2 semaines", score=0),
                    AnswerOption(value='b', label="B5 antidepresseur I - IX noté niveau 4 et Li au moins 2 semaines", score=1),
                    AnswerOption(value='c', label="Pas de prescription ou condition inexistante", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='athfc10',
                text="C. Antipsychotiques",
                options=[
                    AnswerOption(value='a', label="C1 Si utilisé chez des patients non psychotiques, les traitements par antipsychotiques devront être cotés globalement comme un essai continu, quelque soit le nombre de neuroleptiques prescrit.", score=0),
                    AnswerOption(value='b', label="Pas de prescription", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='athfe8',
                text="E. hormones thyroïdiennes",
                options=[
                    AnswerOption(value='a', label="E1 prescription < 4 semaines ", score=0),
                    AnswerOption(value='b', label="E2 >=4 semaines ET posologie < 25 mcg/jour", score=1),
                    AnswerOption(value='c', label="E3 >= 4 semaines ET posologie 25-49 mcg/jour", score=2),
                    AnswerOption(value='d', label="E4 >= 4 semaines ET posologie >= 50 mcg/jour", score=3),
                    AnswerOption(value='e', label="Pas de prescription ou condition inexistante", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='athff10',
                text="F. Photothérapie",
                options=[
                    AnswerOption(value='a', label="F1 quelle que soit la forme", score=0),
                    AnswerOption(value='b', label="Pas de prescription", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="ATHF",
            name="ATHF Questionnaire",
            description="7 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute ATHF score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
