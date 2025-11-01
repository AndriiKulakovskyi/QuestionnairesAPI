"""
PSY_DIAG_PSYCHIATRIQUE - PSY_DIAG_PSYCHIATRIQUE Questionnaire
=============================================================

21 items questionnaire

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


@register_questionnaire("PSY_DIAG_PSYCHIATRIQUE")
@dataclass
class PsyDiagPsychiatrique(BaseQuestionnaire):
    """PSY_DIAG_PSYCHIATRIQUE Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize PSY_DIAG_PSYCHIATRIQUE questionnaire with all 21 items."""
        
        questions_list = [
            Question(
                id='caract_saison',
                text="Caractère saisonnier ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='epi_car_psycho',
                text="Caractéristiques psychotiques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="DM", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='epi_car_sai',
                text="Caractère saisonnier",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="DM", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='epi_hospi',
                text="Hospitalisation",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="DM", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='epi_mixt',
                text="Mixité",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="DM", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='epi_recur_depress',
                text="Récurrence dépressive sous traitement",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="DM", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='epi_remi_comp',
                text="Rémission complète",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="DM", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='epi_resist',
                text="Résistant",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="DM", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='epi_traite',
                text="Traité",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="DM", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='epi_vir_antid',
                text="Virage sous antidépresseur",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="DM", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='remi_comp_epi',
                text="Y a-t-il eu rémission complète entre les épisodes ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='remi_incomp_epi',
                text="Y a-t-il eu rémission incomplète entre les épisodes ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='sev_epi_act',
                text="Préciser la sévérité de l'épisode actuel selon les critères DSM IV",
                options=[
                    AnswerOption(value='a', label="Léger", score=0),
                    AnswerOption(value='b', label="Modéré", score=1),
                    AnswerOption(value='c', label="Sévère sans caractéristiques psychotiques", score=2),
                    AnswerOption(value='d', label="Sévère avec caractéristiques psychotiques congruentes", score=3),
                    AnswerOption(value='e', label="Sévère avec caractéristiques psychotiques non congruentes", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='trou_depress_maj',
                text="Trouble Dépressif Majeur",
                options=[
                    AnswerOption(value='a', label="Isolé", score=0),
                    AnswerOption(value='b', label="Récurrent", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='type_affect',
                text="Préciser le type d’affection",
                options=[
                    AnswerOption(value='a', label="Endocrinienne", score=0),
                    AnswerOption(value='b', label="Neurologique", score=1),
                    AnswerOption(value='c', label="Cardio-vasculaire", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='type_epi_depress_maj_act',
                text="Préciser le type d’épisode dépressif majeur actuel",
                options=[
                    AnswerOption(value='a', label="Sans caractéristique mélancolique atypique ou catatonique", score=0),
                    AnswerOption(value='b', label="Mélancolique", score=1),
                    AnswerOption(value='c', label="Atypique", score=2),
                    AnswerOption(value='d', label="Catatonique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='type_prem_epi',
                text="Type du premier épisode :",
                options=[
                    AnswerOption(value='a', label="Episode Dépressif Majeur sans caractéristiques psychotiques", score=0),
                    AnswerOption(value='b', label="Episode Dépressif Majeur avec caractéristiques psychotiques", score=1),
                    AnswerOption(value='c', label="Hypomanie", score=2),
                    AnswerOption(value='d', label="Manie sans caractéristiques psychotiques", score=3),
                    AnswerOption(value='e', label="Manie avec caractéristiques psychotiques", score=4),
                    AnswerOption(value='f', label="Mixte sans caractéristiques psychotiques", score=5),
                    AnswerOption(value='g', label="Mixte avec caractéristiques psychotiques", score=6),
                    AnswerOption(value='h', label="Ne sais pas", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='type_prem_epir',
                text="Résistance",
                options=[
                    AnswerOption(value='a', label="Résistant : échec à deux traitements antidépresseur de même classe", score=0),
                    AnswerOption(value='b', label="Non Résistant", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='type_trou_dysth',
                text="Type trouble dysthymique",
                options=[
                    AnswerOption(value='a', label="Précoce", score=0),
                    AnswerOption(value='b', label="Tardif", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='type_trouble',
                text="Type de trouble :",
                options=[
                    AnswerOption(value='a', label="Trouble Dépressif Majeur", score=0),
                    AnswerOption(value='b', label="Bipolaire de Type I", score=1),
                    AnswerOption(value='c', label="Bipolaire de Type II", score=2),
                    AnswerOption(value='d', label="Bipolaire non spécifié", score=3),
                    AnswerOption(value='e', label="Trouble dysthymique", score=4),
                    AnswerOption(value='f', label="Trouble de l'humeur dû à une affection médicale générale instable", score=5),
                    AnswerOption(value='g', label="Trouble de l'humeur associé à une affection médicale générale", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='type_trouble_spe',
                text="Préciser le type de trouble",
                options=[
                    AnswerOption(value='a', label="Episode d’allure de dépression majeure", score=0),
                    AnswerOption(value='b', label="Episode avec caractéristiques dépressives", score=1),
                    AnswerOption(value='c', label="Episode avec caractéristiques maniaques", score=2),
                    AnswerOption(value='d', label="Episode avec caractéristiques mixtes", score=3),
                    AnswerOption(value='e', label="Trouble de l'humeur induit par l'utilisation d'une substance", score=4),
                    AnswerOption(value='f', label="Ne sais pas", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="PSY_DIAG_PSYCHIATRIQUE",
            name="PSY_DIAG_PSYCHIATRIQUE Questionnaire",
            description="21 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=10,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute PSY_DIAG_PSYCHIATRIQUE score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
