"""
CSRI - CSRI Questionnaire
=========================

12 items questionnaire

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


@register_questionnaire("CSRI")
@dataclass
class Csri(BaseQuestionnaire):
    """CSRI Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize CSRI questionnaire with all 12 items."""
        
        questions_list = [
            Question(
                id='csri_aide_autres_qui',
                text="Par qui?",
                options=[
                    AnswerOption(value='a', label="Mère", score=0),
                    AnswerOption(value='b', label="Père", score=1),
                    AnswerOption(value='c', label="frère/soeur", score=2),
                    AnswerOption(value='d', label="enfant", score=3),
                    AnswerOption(value='e', label="autre parent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csri_aide_ext_qui',
                text="Par qui?",
                options=[
                    AnswerOption(value='a', label="Mère", score=0),
                    AnswerOption(value='b', label="Père", score=1),
                    AnswerOption(value='c', label="frère/soeur", score=2),
                    AnswerOption(value='d', label="enfant", score=3),
                    AnswerOption(value='e', label="autre parent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csri_aide_garde_enf_qui',
                text="Par qui?",
                options=[
                    AnswerOption(value='a', label="Mère", score=0),
                    AnswerOption(value='b', label="Père", score=1),
                    AnswerOption(value='c', label="frère/soeur", score=2),
                    AnswerOption(value='d', label="enfant", score=3),
                    AnswerOption(value='e', label="autre parent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csri_aide_maison_qui',
                text="Par qui?",
                options=[
                    AnswerOption(value='a', label="Mère", score=0),
                    AnswerOption(value='b', label="Père", score=1),
                    AnswerOption(value='c', label="frère/soeur", score=2),
                    AnswerOption(value='d', label="enfant", score=3),
                    AnswerOption(value='e', label="autre parent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csri_aide_pers_char_qui',
                text="Par qui?",
                options=[
                    AnswerOption(value='a', label="Mère", score=0),
                    AnswerOption(value='b', label="Père", score=1),
                    AnswerOption(value='c', label="frère/soeur", score=2),
                    AnswerOption(value='d', label="enfant", score=3),
                    AnswerOption(value='e', label="autre parent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csri_aide_soin_perso_qui',
                text="Par qui?",
                options=[
                    AnswerOption(value='a', label="Mère", score=0),
                    AnswerOption(value='b', label="Père", score=1),
                    AnswerOption(value='c', label="frère/soeur", score=2),
                    AnswerOption(value='d', label="enfant", score=3),
                    AnswerOption(value='e', label="autre parent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csri_aide_tenir_qui',
                text="Par qui?",
                options=[
                    AnswerOption(value='a', label="Mère", score=0),
                    AnswerOption(value='b', label="Père", score=1),
                    AnswerOption(value='c', label="frère/soeur", score=2),
                    AnswerOption(value='d', label="enfant", score=3),
                    AnswerOption(value='e', label="autre parent", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csri_hospit_lieu',
                text="Lieu",
                options=[
                    AnswerOption(value='a', label="Clinique privée", score=0),
                    AnswerOption(value='b', label="Hôpital", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csri_hospitj_lieu',
                text="Lieu",
                options=[
                    AnswerOption(value='a', label="Clinique privée", score=0),
                    AnswerOption(value='b', label="Hôpital", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csri_med_spe_lieu',
                text="Lieu",
                options=[
                    AnswerOption(value='a', label="Clinique privée", score=0),
                    AnswerOption(value='b', label="Hôpital", score=1),
                    AnswerOption(value='c', label="Cabinet en ville", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csri_urg',
                text="Au cours de l’année, avez-vous eu recours, pour vous-même, à un service d’urgences ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='csri_urg_amb',
                text="Avez-vous été transporté en ambulance ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="CSRI",
            name="CSRI Questionnaire",
            description="12 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=6,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute CSRI score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
