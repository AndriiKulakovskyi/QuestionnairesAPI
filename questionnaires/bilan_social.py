"""
BILAN_SOCIAL - BILAN_SOCIAL Questionnaire
=========================================

10 items questionnaire

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


@register_questionnaire("BILAN_SOCIAL")
@dataclass
class BilanSocial(BaseQuestionnaire):
    """BILAN_SOCIAL Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize BILAN_SOCIAL questionnaire with all 10 items."""
        
        questions_list = [
            Question(
                id='social_cl_pr',
                text="Donner la classe professionnelle ",
                options=[
                    AnswerOption(value='a', label="Agriculteurs exploitants", score=0),
                    AnswerOption(value='b', label="Artisans, commerçants et chefs d’entreprise", score=1),
                    AnswerOption(value='c', label="Cadres et professions intellectuelles supérieure", score=2),
                    AnswerOption(value='d', label="Professions intermédiaires", score=3),
                    AnswerOption(value='e', label="Employés", score=4),
                    AnswerOption(value='f', label="Ouvriers", score=5),
                    AnswerOption(value='g', label="Retraités", score=6),
                    AnswerOption(value='h', label="Autres personnes sans activité professionnelle", score=7),
                    AnswerOption(value='i', label="Autres", score=8)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='social_educ',
                text="2. Education",
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
                    AnswerOption(value='14', label="BAC+1", score=14),
                    AnswerOption(value='15', label="BAC+2", score=15),
                    AnswerOption(value='16', label="BAC+3", score=16),
                    AnswerOption(value='17', label="BAC+4", score=17),
                    AnswerOption(value='18', label="BAC+5", score=18),
                    AnswerOption(value='19', label="Doctorat", score=19)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='social_lien',
                text="6. PERSONNE AVEC LAQUELLE LE SUJET PASSE LE PLUS DE TEMPS",
                options=[
                    AnswerOption(value='a', label="Conjoint", score=0),
                    AnswerOption(value='b', label="Mère", score=1),
                    AnswerOption(value='c', label="Père", score=2),
                    AnswerOption(value='d', label="Colocataire", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='social_protec',
                text="7. MESURES DE PROTECTION ?",
                options=[
                    AnswerOption(value='a', label="Aucune", score=0),
                    AnswerOption(value='b', label="Curatelle", score=1),
                    AnswerOption(value='c', label="Tutelle", score=2),
                    AnswerOption(value='d', label="Sauvegarde de justice.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='social_stprof',
                text="3. STATUT PROFESSIONNEL ACTUEL",
                options=[
                    AnswerOption(value='a', label="Sans Emploi", score=0),
                    AnswerOption(value='b', label="Retraité", score=1),
                    AnswerOption(value='c', label="Actif", score=2),
                    AnswerOption(value='d', label="Etudiant", score=3),
                    AnswerOption(value='e', label="Pension", score=4),
                    AnswerOption(value='f', label="Au foyer", score=5),
                    AnswerOption(value='g', label="Autres", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='social_stprof_pleintps',
                text="Est-ce un emploi temps plein ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='social_trav',
                text="8. Arrêt de travail actuel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non applicable", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='social_trav_long',
                text="Longue durée?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='social_travan',
                text="9. ARRET DE TRAVAIL AU COURS DE L’ANNEE PASSEE ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non applicable", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='social_vie_mode',
                text="5. MODE DE VIE",
                options=[
                    AnswerOption(value='a', label="Seul", score=0),
                    AnswerOption(value='b', label="Chez ses parents", score=1),
                    AnswerOption(value='c', label="Dans son propre foyer familial", score=2),
                    AnswerOption(value='d', label="Chez les enfants", score=3),
                    AnswerOption(value='e', label="Chez de la famille", score=4),
                    AnswerOption(value='f', label="Colocation", score=5),
                    AnswerOption(value='g', label="Collectivité", score=6),
                    AnswerOption(value='h', label="Autres", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="BILAN_SOCIAL",
            name="BILAN_SOCIAL Questionnaire",
            description="10 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute BILAN_SOCIAL score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
