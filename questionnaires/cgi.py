"""
CGI - CGI Questionnaire
=======================

2 items questionnaire

Source: Extracted from ebipolar application
Applications: ebipolar
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


@register_questionnaire("CGI")
@dataclass
class Cgi(BaseQuestionnaire):
    """CGI Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize CGI questionnaire with all 2 items."""
        
        questions_list = [
            Question(
                id='radhtml_cgi_1',
                text="Gravité de la maladie : En fonction de votre expérience clinique totale avec ce type de patient, quel est le niveau de gravité des troubles mentaux actuels du patient",
                options=[
                    AnswerOption(value='a', label="Non évalué", score=0),
                    AnswerOption(value='b', label="Normal, pas du tout malade", score=1),
                    AnswerOption(value='c', label="A la limite", score=2),
                    AnswerOption(value='d', label="Légèrement malade", score=3),
                    AnswerOption(value='e', label="Modérément malade", score=4),
                    AnswerOption(value='f', label="Manifestement malade", score=5),
                    AnswerOption(value='g', label="Gravement malade", score=6),
                    AnswerOption(value='h', label="Parmi les patients les plus malades", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_cgi_2',
                text="Amélioration globale : Évaluer l'amélioration totale qu'elle soi ou non, selon votre opinion, due entièrement au traitement médicamenteux. Comparé à son état au début du traitement, de quelle façon le patient a-t-il changé",
                options=[
                    AnswerOption(value='a', label="Non évalué", score=0),
                    AnswerOption(value='b', label="Très fortement amélioré", score=1),
                    AnswerOption(value='c', label="Fortement amélioré", score=2),
                    AnswerOption(value='d', label="Légèrement amélioré", score=3),
                    AnswerOption(value='e', label="Pas de changement", score=4),
                    AnswerOption(value='f', label="Légèrement aggravé", score=5),
                    AnswerOption(value='g', label="Fortement aggravé", score=6),
                    AnswerOption(value='h', label="Très fortement aggravé", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="CGI",
            name="CGI Questionnaire",
            description="2 items questionnaire",
            pathology_domain=PathologyDomain.BIPOLAR,
            respondent_type=RespondentType.CLINICIAN_RATED,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute CGI score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
