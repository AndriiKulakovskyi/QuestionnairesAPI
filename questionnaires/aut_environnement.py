"""
AUT_ENVIRONNEMENT - AUT_ENVIRONNEMENT Questionnaire
===================================================

14 items questionnaire

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


@register_questionnaire("AUT_ENVIRONNEMENT")
@dataclass
class AutEnvironnement(BaseQuestionnaire):
    """AUT_ENVIRONNEMENT Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_ENVIRONNEMENT questionnaire with all 14 items."""
        
        questions_list = [
            Question(
                id='env_wkm',
                text="Statut professionnel de la mère",
                options=[
                    AnswerOption(value='a', label="Sans emploi", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='env_wkm1',
                text="Préciser sans emploi",
                options=[
                    AnswerOption(value='a', label="Au chômage", score=0),
                    AnswerOption(value='b', label="En invalidité", score=1),
                    AnswerOption(value='c', label="Au foyer", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='env_wkp',
                text="Statut professionnel du père",
                options=[
                    AnswerOption(value='a', label="Sans emploi", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='env_wkp1',
                text="Préciser sans emploi",
                options=[
                    AnswerOption(value='a', label="Au chômage", score=0),
                    AnswerOption(value='b', label="En invalidité", score=1),
                    AnswerOption(value='c', label="Au foyer", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='etud_maxm',
                text="Niveau d'étude maximum atteint de la mère",
                options=[
                    AnswerOption(value='0', label="CP", score=0),
                    AnswerOption(value='1', label="CE1", score=1),
                    AnswerOption(value='2', label="CE2", score=2),
                    AnswerOption(value='3', label="CM1", score=3),
                    AnswerOption(value='4', label="CM2", score=4),
                    AnswerOption(value='5', label="6ème", score=5),
                    AnswerOption(value='6', label="5ème", score=6),
                    AnswerOption(value='7', label="4ème", score=7),
                    AnswerOption(value='8', label="3ème", score=8),
                    AnswerOption(value='9', label="2nde", score=9),
                    AnswerOption(value='10', label="1ère", score=10),
                    AnswerOption(value='11', label="BAC", score=11),
                    AnswerOption(value='12', label="CAP", score=12),
                    AnswerOption(value='13', label="BEP", score=13),
                    AnswerOption(value='14', label=">BAC", score=14)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='etud_maxp',
                text="Niveau d'étude maximum atteint du père",
                options=[
                    AnswerOption(value='0', label="CP", score=0),
                    AnswerOption(value='1', label="CE1", score=1),
                    AnswerOption(value='2', label="CE2", score=2),
                    AnswerOption(value='3', label="CM1", score=3),
                    AnswerOption(value='4', label="CM2", score=4),
                    AnswerOption(value='5', label="6ème", score=5),
                    AnswerOption(value='6', label="5ème", score=6),
                    AnswerOption(value='7', label="4ème", score=7),
                    AnswerOption(value='8', label="3ème", score=8),
                    AnswerOption(value='9', label="2nde", score=9),
                    AnswerOption(value='10', label="1ère", score=10),
                    AnswerOption(value='11', label="BAC", score=11),
                    AnswerOption(value='12', label="CAP", score=12),
                    AnswerOption(value='13', label="BEP", score=13),
                    AnswerOption(value='14', label=">BAC", score=14)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gro_streso',
                text="Votre mère a-t-elle vécu un de ces évènements au cours de sa grossesse?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mari_parent',
                text="Statut marital des parents",
                options=[
                    AnswerOption(value='a', label="Marié", score=0),
                    AnswerOption(value='b', label="Séparé", score=1),
                    AnswerOption(value='c', label="Divorcé", score=2),
                    AnswerOption(value='d', label="Célibataire", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='migr_pkoi',
                text="Motif de la migration ",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='migr_pkoip',
                text="Motif de la migration",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pnce_fr',
                text="France métropolitaine",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pnce_m',
                text="France métropolitaine",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pnce_p',
                text="France métropolitaine",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pnce_pfr',
                text="France métropolitaine",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_ENVIRONNEMENT",
            name="AUT_ENVIRONNEMENT Questionnaire",
            description="14 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=7,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_ENVIRONNEMENT score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
