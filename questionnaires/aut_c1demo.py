"""
AUT_C1DEMO - AUT_C1DEMO Questionnaire
=====================================

35 items questionnaire

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


@register_questionnaire("AUT_C1DEMO")
@dataclass
class AutC1demo(BaseQuestionnaire):
    """AUT_C1DEMO Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_C1DEMO questionnaire with all 35 items."""
        
        questions_list = [
            Question(
                id='acspec',
                text="\n                      Accompagnant spécialisé\n                    ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='activite',
                text="A.3.2 Type d'activité",
                options=[
                    AnswerOption(value='a', label="Contrat à durée indéterminée", score=0),
                    AnswerOption(value='b', label="Contrat à durée déterminée", score=1),
                    AnswerOption(value='c', label="Chomage", score=2),
                    AnswerOption(value='d', label="Non applicable", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='adopton',
                text="Sujet adopté",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='auxviesc_2',
                text="Si Oui, l'AESH ou l'AVS est",
                options=[
                    AnswerOption(value='a', label="Publique", score=0),
                    AnswerOption(value='b', label="Privée", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bac',
                text="Baccalauréat",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='brevcol',
                text="Brevet des collèges",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='capbep',
                text="CAP/BEP",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='clissupi',
                text="CLISS ou UPI autisme",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='descola',
                text="Votre enfant a-t-il déjà été déscolarisé?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dmochang',
                text="Changement depuis la dernière visite",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ethorgmm',
                text="Ethnie de la grand-mère maternelle",
                options=[
                    AnswerOption(value='a', label="Asiatique", score=0),
                    AnswerOption(value='b', label="Noir", score=1),
                    AnswerOption(value='c', label="Caucasien", score=2),
                    AnswerOption(value='d', label="Autre", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ethorgmp',
                text="Ethnie de la grand-mère paternelle",
                options=[
                    AnswerOption(value='a', label="Asiatique", score=0),
                    AnswerOption(value='b', label="Noir", score=1),
                    AnswerOption(value='c', label="Caucasien", score=2),
                    AnswerOption(value='d', label="Autre", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ethorgpm',
                text="Ethnie du grand-père maternelle",
                options=[
                    AnswerOption(value='a', label="Asiatique", score=0),
                    AnswerOption(value='b', label="Noir", score=1),
                    AnswerOption(value='c', label="Caucasien", score=2),
                    AnswerOption(value='d', label="Autre", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ethorgpp',
                text="Ethniedu grand-père paternel",
                options=[
                    AnswerOption(value='a', label="Asiatique", score=0),
                    AnswerOption(value='b', label="Noir", score=1),
                    AnswerOption(value='c', label="Caucasien", score=2),
                    AnswerOption(value='d', label="Autre", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ethori',
                text="Ethnie du sujet",
                options=[
                    AnswerOption(value='a', label="Asiatique", score=0),
                    AnswerOption(value='b', label="Noir", score=1),
                    AnswerOption(value='c', label="Caucasien", score=2),
                    AnswerOption(value='d', label="Autre", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='etusup',
                text="Etudes supérieures",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hopjour',
                text="Hôpital de jour ou autre structure sanitaire",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ime',
                text="IME ou autre structure medico-sociale",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mfr',
                text="\n                      MFR\n                    ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='milieu',
                text="Sujet né dans un milieu",
                options=[
                    AnswerOption(value='a', label="Rural", score=0),
                    AnswerOption(value='b', label="Urbain", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='passcola',
                text="Jamais de scolarisation",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='paysact',
                text="Sujet né dans le pays actuel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prochang',
                text="Changement depuis la dernière visite",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='profes',
                text="A.3.1 Catégorie socioprofessionnelle",
                options=[
                    AnswerOption(value='a', label="Agriculteurs/exploitants ", score=0),
                    AnswerOption(value='b', label="Artisans, commerçants et chefs d’entreprise", score=1),
                    AnswerOption(value='c', label="Cadres / professions intellectuelles supérieures", score=2),
                    AnswerOption(value='d', label="Professions intermédiaires", score=3),
                    AnswerOption(value='e', label="Employés ", score=4),
                    AnswerOption(value='f', label="Ouvriers", score=5),
                    AnswerOption(value='g', label="Retraités", score=6),
                    AnswerOption(value='h', label="Autres personnes sans activités professionnels", score=7),
                    AnswerOption(value='i', label="Etudiant", score=8),
                    AnswerOption(value='j', label="Non applicable", score=9)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rased',
                text="\n                      RASED\n                    ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='scolass',
                text="Scolarité assistée ou spécialisée ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='scolassc',
                text="Autre",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='sconorm',
                text="Scolarité normale",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='scprim',
                text="Scolarité primaire achevée",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='scseco',
                text="Scolarité secondaire achevée",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='segpa',
                text="\n                      SEGPA, SES, EREA\n                    ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='sessad',
                text="\n                      SESSAD\n                    ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tempscola',
                text="Si votre enfant est scolarisé autre qu'à la maison, précisez le temps",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tpscomp',
                text="Temps complet",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ulis',
                text="ULIS ou ULIS Collège",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_C1DEMO",
            name="AUT_C1DEMO Questionnaire",
            description="35 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=17,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_C1DEMO score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
