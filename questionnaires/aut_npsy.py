"""
AUT_NPSY - AUT_NPSY Questionnaire
=================================

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


@register_questionnaire("AUT_NPSY")
@dataclass
class AutNpsy(BaseQuestionnaire):
    """AUT_NPSY Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_NPSY questionnaire with all 25 items."""
        
        questions_list = [
            Question(
                id='atcd_npsy1',
                text="\n                      Avez-vous effectué un bilan neuropsychologique avant l'évaluation dans notre Centre\n                      Expert?\n                    ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcd_npsy2',
                text="Le cadre",
                options=[
                    AnswerOption(value='a', label="Autre CE Asperger", score=0),
                    AnswerOption(value='b', label="Libéral", score=1),
                    AnswerOption(value='c', label="CMP", score=2),
                    AnswerOption(value='d', label="Autre", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcd_npsy8',
                text="Avez-vous ces résultats?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcd_w1',
                text="Avez-vous effectué un test cognitif WAIS IV moins de 6 mois avant l'évaluation dans notre\n Centre Expert?\n                    ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcd_w2',
                text="Le cadre",
                options=[
                    AnswerOption(value='a', label="Autre CE Asperger", score=0),
                    AnswerOption(value='b', label="Libéral", score=1),
                    AnswerOption(value='c', label="CMP", score=2),
                    AnswerOption(value='d', label="Autre", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcd_w8',
                text="Avez-vous ces résultats?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_begai',
                text="Bégaiement",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_conv',
                text="Convulsions fébriles dans la petite enfance",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_dyscal',
                text="Dyscalculie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_dyslex',
                text="Dyslexie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_dysor',
                text="Dysorthographie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_dysph',
                text="Dysphasie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_dyspra',
                text="Dyspraxie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_lateral',
                text="Latéralité",
                options=[
                    AnswerOption(value='a', label="Gaucher", score=0),
                    AnswerOption(value='b', label="Droitier", score=1),
                    AnswerOption(value='c', label="Ambidextre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_march',
                text="Retard à l'acquisition de la marche",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_parol',
                text="Retard à l'acquisition de la parole",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_precoc',
                text="Précocité",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='npsy_1',
                text="Maîtrise suffisante de la langue française",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='npsy_2',
                text="Etat clinique compatible avec la passation des tests cognitifs",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='npsy_3',
                text="Absence de daltonisme ou de trouble visuel invalidant",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='npsy_4',
                text="Absence de troubles auditifs non appareillés",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='npsy_6',
                text="Traitement psychotrope",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NSP", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='npsy_7',
                text="Patient compatible avec une évaluation neuropsychologique",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='w4_nivetude',
                text="Niveau d'étude",
                options=[
                    AnswerOption(value='a', label="Sans diplôme", score=0),
                    AnswerOption(value='b', label="CEP", score=1),
                    AnswerOption(value='c', label="CAP BEP", score=2),
                    AnswerOption(value='d', label="BAC technologique, pro et brevet professionnel", score=3),
                    AnswerOption(value='e', label="BAC général", score=4),
                    AnswerOption(value='f', label="Diplôme universitaire 1er cycle, BTS, DUT, diplômes des professions sociales et de la santé", score=5),
                    AnswerOption(value='g', label="Diplôme universitaire 2e et 3e cycle, ingenieur grande école", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='w4_profession',
                text="Profession et catégorie sociale",
                options=[
                    AnswerOption(value='a', label="Ouvriers", score=0),
                    AnswerOption(value='b', label="Employés", score=1),
                    AnswerOption(value='c', label="Agriculteurs", score=2),
                    AnswerOption(value='d', label="Artisans, commerçants", score=3),
                    AnswerOption(value='e', label="Retraités", score=4),
                    AnswerOption(value='f', label="Professions intermédiaires", score=5),
                    AnswerOption(value='g', label="Professions intellectuelles supérieures", score=6),
                    AnswerOption(value='h', label="sans profession", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_NPSY",
            name="AUT_NPSY Questionnaire",
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
        """Compute AUT_NPSY score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
