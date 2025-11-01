"""
AUT_ATCDLT - AUT_ATCDLT Questionnaire
=====================================

33 items questionnaire

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


@register_questionnaire("AUT_ATCDLT")
@dataclass
class AutAtcdlt(BaseQuestionnaire):
    """AUT_ATCDLT Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_ATCDLT questionnaire with all 33 items."""
        
        questions_list = [
            Question(
                id='antalrgi',
                text="Allergie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antcanc',
                text="Cancérologie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antcancrem',
                text="Rémission  actuelle ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antcancs',
                text="Cancérologie",
                options=[
                    AnswerOption(value='a', label="Poumon", score=0),
                    AnswerOption(value='b', label="Col utérus ", score=1),
                    AnswerOption(value='c', label="Prostate", score=2),
                    AnswerOption(value='d', label="Hématologique", score=3),
                    AnswerOption(value='e', label="Mélanome", score=4),
                    AnswerOption(value='f', label="Colorectal", score=5),
                    AnswerOption(value='g', label="Sein", score=6),
                    AnswerOption(value='h', label="ORL", score=7),
                    AnswerOption(value='i', label="Autres ", score=8)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antcardi',
                text="Cardio-vasculaire",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antcardirem',
                text="Rémission  actuelle ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antcardis',
                text="Cardio-vasculaire",
                options=[
                    AnswerOption(value='a', label="Infarctus myocarde", score=0),
                    AnswerOption(value='b', label="AVC", score=1),
                    AnswerOption(value='c', label="Mal. Thromboembol.", score=2),
                    AnswerOption(value='d', label="Cardiopathie congénitale", score=3),
                    AnswerOption(value='e', label="Insuffisance Cardiaque", score=4),
                    AnswerOption(value='f', label="Tb rythme ", score=5),
                    AnswerOption(value='g', label="HTA", score=6),
                    AnswerOption(value='h', label="Valvulopathie", score=7),
                    AnswerOption(value='i', label="Autres", score=8)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antendo',
                text="Endocrinologie ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antendorem',
                text="Rémission  actuelle ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antendos',
                text="Endocrinologie",
                options=[
                    AnswerOption(value='a', label="Hypothyroïdie ", score=0),
                    AnswerOption(value='b', label="DNID", score=1),
                    AnswerOption(value='c', label="Hyperthyroïdie", score=2),
                    AnswerOption(value='d', label="Déficit en GH ", score=3),
                    AnswerOption(value='e', label="Dyslipidémie ", score=4),
                    AnswerOption(value='f', label="Insuffisance surrénalienne ", score=5),
                    AnswerOption(value='g', label="DID", score=6),
                    AnswerOption(value='h', label="Insuffisance gonadotropique ", score=7),
                    AnswerOption(value='i', label="Autres", score=8)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anthepa',
                text="Hepato-Gastrologie ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antheparem',
                text="Rémission  actuelle ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anthepas',
                text="Pathologie",
                options=[
                    AnswerOption(value='a', label="Maladie Cœliaque ", score=0),
                    AnswerOption(value='b', label="Ulcère", score=1),
                    AnswerOption(value='c', label="Maladie Crohn ", score=2),
                    AnswerOption(value='d', label="Reflux gastro oesophagien ", score=3),
                    AnswerOption(value='e', label="Diarrhée chronique ", score=4),
                    AnswerOption(value='f', label="Hépatite B/C chronique ", score=5),
                    AnswerOption(value='g', label="Constipation chronique ", score=6),
                    AnswerOption(value='h', label="Pancréatite", score=7),
                    AnswerOption(value='i', label="Autres", score=8)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antipulmrem',
                text="Rémission  actuelle ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antipulms',
                text="Pulmonaire",
                options=[
                    AnswerOption(value='a', label="Asthme", score=0),
                    AnswerOption(value='b', label="BPCO", score=1),
                    AnswerOption(value='c', label="Tuberculose", score=2),
                    AnswerOption(value='d', label="Autres", score=3),
                    AnswerOption(value='e', label="Allergie", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antneuro',
                text="Neurologie ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antneurorem',
                text="Rémission  actuelle ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antneuros',
                text="Neurologie",
                options=[
                    AnswerOption(value='a', label="Neuropathie distale ", score=0),
                    AnswerOption(value='b', label="SEP", score=1),
                    AnswerOption(value='c', label="Parkinson", score=2),
                    AnswerOption(value='d', label="Méningite viral/bact ", score=3),
                    AnswerOption(value='e', label="Myasthenie", score=4),
                    AnswerOption(value='f', label="Myopathie", score=5),
                    AnswerOption(value='g', label="Neurofibromatose", score=6),
                    AnswerOption(value='h', label="Migraine", score=7),
                    AnswerOption(value='i', label="Traumatisme crânien avec PC ", score=8),
                    AnswerOption(value='j', label="Autres", score=9)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antorl',
                text="ORL/Ophtalmologie  ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antorls',
                text="spécifier ",
                options=[
                    AnswerOption(value='a', label="Glaucome ouvert ", score=0),
                    AnswerOption(value='b', label="Glaucome fermé ", score=1),
                    AnswerOption(value='c', label="Cataracte", score=2),
                    AnswerOption(value='d', label="Hypermétropie", score=3),
                    AnswerOption(value='e', label="Astigmatisme", score=4),
                    AnswerOption(value='f', label="Myopie", score=5),
                    AnswerOption(value='g', label="Surdité/Hypoacousie", score=6),
                    AnswerOption(value='h', label="Sd vestibulaire ", score=7),
                    AnswerOption(value='i', label="Strabisme", score=8)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antpulm',
                text="Pulmonaire",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antrhum',
                text="Rhumatologie/Dermatologie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antrhumrem',
                text="Rémission  actuelle ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antrhums',
                text="Rhumatologie/Dermatologie",
                options=[
                    AnswerOption(value='a', label="Lupus", score=0),
                    AnswerOption(value='b', label="Psoriasis", score=1),
                    AnswerOption(value='c', label="P. Rhumatoïde ", score=2),
                    AnswerOption(value='d', label="Eczéma", score=3),
                    AnswerOption(value='e', label="Spondylarthrite", score=4),
                    AnswerOption(value='f', label="Angiome", score=5),
                    AnswerOption(value='g', label="Hyperuricémie/goutte", score=6),
                    AnswerOption(value='h', label="Hamartome", score=7),
                    AnswerOption(value='i', label="Autres,", score=8)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdchang',
                text="Changement depuis la dernière visite pour l'ensemble des antécédents médicaux",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdltn',
                text="Tous les critères",
                options=[
                    AnswerOption(value='a', label="Non pour tous les critères", score=0),
                    AnswerOption(value='b', label="Non connu pour tous les critères", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='autrmal',
                text="Autres maladies significatives",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='autrmrem',
                text="Rémission  actuelle ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='crisact',
                text="Crises actuelles",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gynco',
                text="Spécifier",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='malgen',
                text="Maladies génétiques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='malgerem',
                text="Rémission  actuelle ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='orlrem',
                text="Rémission  actuelle ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_ATCDLT",
            name="AUT_ATCDLT Questionnaire",
            description="33 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=16,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_ATCDLT score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
