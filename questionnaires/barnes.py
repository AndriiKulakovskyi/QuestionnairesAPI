"""
BARNES - BARNES Questionnaire
=============================

4 items questionnaire

Source: Extracted from eschizo application
Applications: eschizo
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


@register_questionnaire("BARNES")
@dataclass
class Barnes(BaseQuestionnaire):
    """BARNES Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize BARNES questionnaire with all 4 items."""
        
        questions_list = [
            Question(
                id='radhtml_barnes_agitation',
                text="Conscience de l'agitation",
                options=[
                    AnswerOption(value='a', label="Absence d'impatience subjective.", score=0),
                    AnswerOption(value='b', label="Impression non spécifique d'agitation intérieure.", score=1),
                    AnswerOption(value='c', label="Le patient a conscience d'une incapacité à garder ses jambes au repos ou ressent le besoin de bouger ses jambes et/ou se plaint d'une agitation intérieure aggravée spécifiquement lorsqu'on lui demande de rester  tranquille.", score=2),
                    AnswerOption(value='d', label="Conscience d'un besoin compulsif intense de bouger la plupart du temps et/ou rapporte une forte envie de marcher ou piétiner la plupart du temps.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_barnes_akathisie',
                text="Evaluation globale de l'akathisie",
                options=[
                    AnswerOption(value='a', label="Absence ; Pas de sensation d'agitation ou d'impatience. La présence de mouvements caractéristiques d'akathisie en l'absence d'impression subjective d'agitation intérieure ou de besoin compulsif de bouger les jambes doit être considérée comme une pseudo-akathisie.", score=0),
                    AnswerOption(value='b', label="Douteux. Tension intérieure et agitation non spécifiques.", score=1),
                    AnswerOption(value='c', label="Légère. Conscience d'impatiences dans les jambes et/ou sensation d'agitation intérieure aggravée lors de la station debout au repos. L'agitation est présente mais les mouvements caractéristiques peuvent manquer. Occasionne peu ou pas de gêne.", score=2),
                    AnswerOption(value='d', label="Moyenne. Conscience d'une agitation associée à des mouvements caractéristiques comme le balancement d'un pied sur l'autre en station debout. Responsable d'une gêne chez le patient.", score=3),
                    AnswerOption(value='e', label="Akathisie marquée. Impression subjective d'agitation avec le désir compulsif de marcher ou piétiner. Le patient peut néanmoins rester assis au moins 5 minutes. Manifestement éprouvante pour le patient.", score=4),
                    AnswerOption(value='f', label="Akathisie sévère. Le patient rapporte un besoin compulsif de faire les cents pas la plupart du temps; Incapable de rester assis ou allongé plus de quelques minutes. Agitation permanente associée à une détresse intense et une insomnie.", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_barnes_detresse',
                text="Détresse relative aux impatiences",
                options=[
                    AnswerOption(value='a', label="Pas de détresse", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Moyenne", score=2),
                    AnswerOption(value='d', label="Grave\\r\\n", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_barnes_objective',
                text="Cotation objective",
                options=[
                    AnswerOption(value='a', label="Normal. Impatiences des membres occasionnelles.", score=0),
                    AnswerOption(value='b', label="Présence de mouvements caractéristiques d'impatience : frottement, piétinement, balancement d'une jambe lorsqu'il est assis et/ou balancement d'un pied sur l'autre ou piétinement sur place lorsqu'il est debout mais les mouvements sont présents moins de la moitié du temps d'observation.", score=1),
                    AnswerOption(value='c', label="Phénomènes décrits ci-dessus présents au moins la moitié du temps d'observation.", score=2),
                    AnswerOption(value='d', label="Le patient a constamment des mouvements d'agitation caractéristique et/ou est dans l'incapacité de rester assis ou debout sans marcher ou sans piétiner.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="BARNES",
            name="BARNES Questionnaire",
            description="4 items questionnaire",
            pathology_domain=PathologyDomain.SCHIZOPHRENIA,
            respondent_type=RespondentType.CLINICIAN_RATED,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute BARNES score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
