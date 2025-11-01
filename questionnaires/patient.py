"""
PATIENT - PATIENT Questionnaire
===============================

23 items questionnaire

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


@register_questionnaire("PATIENT")
@dataclass
class Patient(BaseQuestionnaire):
    """PATIENT Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize PATIENT questionnaire with all 23 items."""
        
        questions_list = [
            Question(
                id='adrsdif',
                text="Adresse des parents différente du patient",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ald',
                text="100% ALD",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='autorit_parent',
                text="Autorité parentale",
                options=[
                    AnswerOption(value='a', label="Conjointe", score=0),
                    AnswerOption(value='b', label="Père", score=1),
                    AnswerOption(value='c', label="Mère", score=2),
                    AnswerOption(value='d', label="Institution", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='causdc',
                text="Cause du décès",
                options=[
                    AnswerOption(value='a', label="Suicide", score=0),
                    AnswerOption(value='b', label="Décès lié aux comorbidités", score=1),
                    AnswerOption(value='c', label="Pathologie somatique", score=2),
                    AnswerOption(value='d', label="Mort violente", score=3),
                    AnswerOption(value='e', label="Autre", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cmu',
                text="Prise en charge des soins médicaux par la CMU",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='conais_ce',
                text="Comment avez vous eu connaissance du centre expert?",
                options=[
                    AnswerOption(value='a', label="par son médecin généraliste", score=0),
                    AnswerOption(value='b', label="par une association", score=1),
                    AnswerOption(value='c', label="par son médecin psychiatre", score=2),
                    AnswerOption(value='d', label="par internet", score=3),
                    AnswerOption(value='e', label="autre", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fam_consult',
                text="Est-ce qu'un membre de votre famille a déjà consulté dans un Centre Expert Asperger?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fin_suivi',
                text="Le patient n'est plus suivi dans le Centre Expert, spécifier le motif\n                ",
                options=[
                    AnswerOption(value='a', label="Patient non autiste", score=0),
                    AnswerOption(value='b', label="Autre crière non compatible au niveau du screening", score=1),
                    AnswerOption(value='c', label="Patient ne désirant pas être revu", score=2),
                    AnswerOption(value='d', label="Patient décédé", score=3),
                    AnswerOption(value='e', label="Patient a déménagé", score=4),
                    AnswerOption(value='f', label="Perdu de vue", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='genident',
                text="Genre exprimé",
                options=[
                    AnswerOption(value='a', label="Masculin", score=0),
                    AnswerOption(value='b', label="Féminin", score=1),
                    AnswerOption(value='c', label="Neutre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hav_child',
                text="Avez-vous des enfants",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mdph',
                text="Reconnaissance par la MDPH",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mutuel',
                text="Prise en charge des soins médicaux par une mutuelle",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='parsep',
                text="Situation parentale",
                options=[
                    AnswerOption(value='a', label="Parents séparés", score=0),
                    AnswerOption(value='b', label="Parents non séparés", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pec_100',
                text="Prise en charge des soins médicaux 100%",
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
                id='prov_bilan_aut',
                text="Voulez-vous que nous transmettions le Compte-rendu de cette évaluation à un autre professionnel de santé ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prov_bilan_gen',
                text="Voulez-vous que nous transmettions le Compte-rendu de cette évaluation à votre médecin généraliste ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prov_bilan_npsy',
                text="Voulez-vous que nous transmettions le Compte-rendu de l'évaluation neuropsy à un professionnel ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prov_bilan_psy',
                text="Voulez-vous que nous transmettions le Compte-rendu de cette évaluation à votre médecin psychiatre ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rad_secteur',
                text="Le patient réside dans la zone géographique du secteur psychiatrique",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rdv_manque',
                text="Le patient ne s'est pas rendu à la consultation prévue, spécifier le motif",
                options=[
                    AnswerOption(value='a', label="Patient indisponible", score=0),
                    AnswerOption(value='b', label="Etat clinique du patient non compatible avec l'évaluation", score=1),
                    AnswerOption(value='c', label="Annulation de la part du Centre Expert", score=2),
                    AnswerOption(value='d', label="Autre", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rel_propos',
                text="Préciser le lien de parenté",
                options=[
                    AnswerOption(value='a', label="Père", score=0),
                    AnswerOption(value='b', label="Mère", score=1),
                    AnswerOption(value='c', label="Frères/soeurs", score=2),
                    AnswerOption(value='d', label="Oncles/tantes", score=3),
                    AnswerOption(value='e', label="Fils/fille", score=4),
                    AnswerOption(value='f', label="Grands-parents", score=5),
                    AnswerOption(value='g', label="Epoux", score=6),
                    AnswerOption(value='h', label="Cousins", score=7),
                    AnswerOption(value='i', label="Autre", score=8)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='sexe',
                text="Sexe de naissance",
                options=[
                    AnswerOption(value='a', label="Masculin", score=0),
                    AnswerOption(value='b', label="Féminin", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="PATIENT",
            name="PATIENT Questionnaire",
            description="23 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=11,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute PATIENT score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
