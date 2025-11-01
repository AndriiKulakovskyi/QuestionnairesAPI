"""
AUT_MEDECO - AUT_MEDECO Questionnaire
=====================================

25 items questionnaire

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


@register_questionnaire("AUT_MEDECO")
@dataclass
class AutMedeco(BaseQuestionnaire):
    """AUT_MEDECO Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_MEDECO questionnaire with all 25 items."""
        
        questions_list = [
            Question(
                id='ald',
                text="ALD",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='arrtrav',
                text="Arrêt travail au cours de l'année passée",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non applicable", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='chang_prof',
                text="Changement statut professionnel durant les 6 derniers mois",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='chang_prof1',
                text="Préciser",
                options=[
                    AnswerOption(value='a', label="Sans emploi", score=0),
                    AnswerOption(value='b', label="Actif", score=1),
                    AnswerOption(value='c', label="Retraité", score=2),
                    AnswerOption(value='d', label="Etudiant", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='chang_prof2',
                text="Préciser sans emploi",
                options=[
                    AnswerOption(value='a', label="Au chômage", score=0),
                    AnswerOption(value='b', label="En recherche d’emploi", score=1),
                    AnswerOption(value='c', label="En invalidité", score=2),
                    AnswerOption(value='d', label="Au foyer", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='chang_prof4',
                text="Avez-vous changé de catégorie socioprofessionnelle ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='chang_prof7',
                text="Temps plein",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cmuc',
                text="CMU-C",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cons_nb2p',
                text="Précisez",
                options=[
                    AnswerOption(value='a', label="En ville", score=0),
                    AnswerOption(value='b', label="Secteur", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cons_nb3p',
                text="Précisez",
                options=[
                    AnswerOption(value='a', label="En ville", score=0),
                    AnswerOption(value='b', label="Secteur", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cpam',
                text="CPAM",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='endett',
                text="Niveau d'endettement",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Endettement facile à gérer", score=1),
                    AnswerOption(value='c', label="Endettement difficile à gérer", score=2),
                    AnswerOption(value='d', label="Endettement très difficile à gérer", score=3),
                    AnswerOption(value='e', label="Non renseigné", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hosp_hdt',
                text="HDT",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hosp_ho',
                text="HO",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hosp_tpl',
                text="Hospitalisation en hôpital psychiatrique temps partiel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hosp_tpn',
                text="Hospitalisation en hôpital psychiatrique temps plein",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='medg',
                text="Médecin Généraliste",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='medp',
                text="Médecin Psychiatrique",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mutuel',
                text="Mutuelle",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='protect',
                text="Mesures de protection",
                options=[
                    AnswerOption(value='a', label="Aucune", score=0),
                    AnswerOption(value='b', label="Curatelle", score=1),
                    AnswerOption(value='c', label="Curatelle renforcée", score=2),
                    AnswerOption(value='d', label="Tutelle", score=3),
                    AnswerOption(value='e', label="Sauvegarde de justice", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psyg',
                text="Psychologue",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='srevenu',
                text="A.3.5 Sources de revenu",
                options=[
                    AnswerOption(value='a', label="Salaire", score=0),
                    AnswerOption(value='b', label="Bourse", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='urg',
                text="Passage aux urgences",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='work_stop1',
                text="Arrêt de travail en lien avec le trouble psychiatrique depuis la dernière visite",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non applicable", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='work_stop6',
                text="Arrêt de travail en lien avec un trouble somatique depuis la dernière visite",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non applicable", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_MEDECO",
            name="AUT_MEDECO Questionnaire",
            description="25 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=12,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_MEDECO score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
