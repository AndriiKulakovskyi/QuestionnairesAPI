"""
SCREENING - SCREENING Questionnaire
===================================

50 items questionnaire

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


@register_questionnaire("SCREENING")
@dataclass
class Screening(BaseQuestionnaire):
    """SCREENING Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize SCREENING questionnaire with all 50 items."""
        
        questions_list = [
            Question(
                id='diag1s_1',
                text="1-Si OUI, Diagnostic probable suite à la consultation de «screening» ",
                options=[
                    AnswerOption(value='a', label="Syndrome d'Asperger", score=0),
                    AnswerOption(value='b', label="Autisme de haut niveau", score=1),
                    AnswerOption(value='c', label="Autisme avec retard mental", score=2),
                    AnswerOption(value='d', label="TSA NOS sans retard mental", score=3),
                    AnswerOption(value='e', label="TSA NOS avec retard mental", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag1s_3',
                text="Si bilan non programmé, préciser ",
                options=[
                    AnswerOption(value='a', label="Consultation spécialisée de screening suffisante pour donner un avis ", score=0),
                    AnswerOption(value='b', label="Etat clinique non compatible lors de la visite de screening ", score=1),
                    AnswerOption(value='c', label="Patient non disponible ", score=2),
                    AnswerOption(value='d', label="Refus du patient", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag1s_4',
                text="Si l'état clinique actuel du patient ne permet pas l'évaluation au Centre Expert, le patient accepte-t-il  d'être évalué lorsque son état le permettra ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag2s_1_1',
                text="type paranoïaque",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag2s_1_10',
                text="type obsessionnel-compulsif",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag2s_1_11',
                text="type non spécifié",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag2s_1_2',
                text="type schizoïde",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag2s_1_3',
                text="type schizotypique",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag2s_1_4',
                text="type antisociale",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag2s_1_5',
                text="type borderline",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag2s_1_6',
                text="type histrionique",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag2s_1_7',
                text="type narcissique",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag2s_1_8',
                text="type évitant",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag2s_1_9',
                text="type dépendant",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag3s_1',
                text="Diagnostic de trouble évoqué au terme du bilan ?",
                options=[
                    AnswerOption(value='0', label="Syndrome d'Asperger", score=0),
                    AnswerOption(value='1', label="Autisme de haut niveau", score=1),
                    AnswerOption(value='2', label="Autisme sans retard mental", score=2),
                    AnswerOption(value='3', label="Autisme avec retard mental", score=3),
                    AnswerOption(value='4', label="TSA NOS sans retard mental", score=4),
                    AnswerOption(value='5', label="TSA NOS avec retard mental", score=5),
                    AnswerOption(value='6', label="Schizophrénie", score=6),
                    AnswerOption(value='7', label="Autre trouble psychotique", score=7),
                    AnswerOption(value='8', label="Retard mental", score=8),
                    AnswerOption(value='9', label="Précocité", score=9),
                    AnswerOption(value='10', label="TDAH", score=10),
                    AnswerOption(value='11', label="Dépression/ Trouble de l'humeur", score=11),
                    AnswerOption(value='12', label="Phobie sociale", score=12),
                    AnswerOption(value='13', label="TOC", score=13),
                    AnswerOption(value='14', label="Trouble de la personnalité", score=14),
                    AnswerOption(value='15', label="Trouble des apprentissages ", score=15),
                    AnswerOption(value='16', label="Trouble spécifique du langage", score=16),
                    AnswerOption(value='17', label="Dyspraxie", score=17),
                    AnswerOption(value='18', label="Autre", score=18)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag3s_1_1',
                text="type paranoïaque",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag3s_1_10',
                text="type obsessionnel-compulsif",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag3s_1_11',
                text="type non spécifié",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag3s_1_2',
                text="type schizoïde",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag3s_1_3',
                text="type schizotypique",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag3s_1_4',
                text="type antisociale",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag3s_1_5',
                text="type borderline",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag3s_1_6',
                text="type histrionique",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag3s_1_7',
                text="type narcissique",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag3s_1_8',
                text="type évitant",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag3s_1_9',
                text="type dépendant",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag_autr',
                text="Autre Diagnostic posé avant la consultation",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas ", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diag_autr_kel',
                text="Si oui, préciser lequel ",
                options=[
                    AnswerOption(value='0', label="1", score=0),
                    AnswerOption(value='1', label="2", score=1),
                    AnswerOption(value='2', label="3", score=2),
                    AnswerOption(value='3', label="4", score=3),
                    AnswerOption(value='4', label="5", score=4),
                    AnswerOption(value='5', label="6", score=5),
                    AnswerOption(value='6', label="7", score=6),
                    AnswerOption(value='7', label="8", score=7),
                    AnswerOption(value='8', label="9", score=8),
                    AnswerOption(value='9', label="10", score=9),
                    AnswerOption(value='10', label="11", score=10),
                    AnswerOption(value='11', label="12", score=11),
                    AnswerOption(value='12', label="13", score=12),
                    AnswerOption(value='13', label="14", score=13),
                    AnswerOption(value='14', label="15", score=14),
                    AnswerOption(value='15', label="16", score=15),
                    AnswerOption(value='16', label="17", score=16)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='diags',
                text="Diagnostique TSA évoqué au terme du screening ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='iaaa_1',
                text="1. Altération marquée dans l'utilisation, pour régler les interactions sociales, de comportements non-verbaux multiples, tels que le contact oculaire, la mimique faciale, les postures corporelles, les gestes",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='iaaa_2',
                text="2. Incapacité à établir des relations avec les pairs correspondant au niveau du développement.",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='iaab_2',
                text="2. Chez les sujets maîtrisant suffisamment le langage, incapacité marquée à engager ou à soutenir une conversation avec autrui",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='iaab_3',
                text="3. Usage stéréotypé et répétitif du langage, ou langage idiosyncrasique",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='iaab_4',
                text="4. Absence d'un jeu de « faire semblant » varié et spontané, ou d'un jeu d'imitation sociale correspondant au niveau du développement",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='iaac_1',
                text="1. Préoccupation circonscrite à un ou plusieurs centres d'intérêt stéréotypés et restreints, anormale soit dans son intensité, soit dans son orientation",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='iaac_2',
                text="2. Adhésion apparemment inflexible à des habitudes ou à des rituels spécifiques et non fonctionnels",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='iaac_4',
                text="4. Préoccupations persistantes pour certaines parties des objets ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='iaae_1',
                text="Les problèmes notés ci-dessus ont tous été présents pendant toute la vie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='note_info',
                text="La note d'information a-t-elle été remise au patient?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='oce_1',
                text="Patient probablement souffrant d'un trouble du spectre autistique sans déficience intellectuelle",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='oce_2',
                text="Etat mental compatible avec l'évaluation",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='oce_3',
                text="Langage fonctionnel pour effectuer le bilan au Centre Expert",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='oce_4',
                text="Adressé par un médecin qui recevra le compte-rendu du bilan",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='oce_5',
                text="Prise en charge à 100%, mutuelle, CMU ou accord du patient pour assumer les frais",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='oce_6',
                text="Accord du patient/de son responsable legal pour une évaluation dans le cadre du Centre Expert ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='oldiag',
                text="Diagnostic de trouble du spectre autistique posé avant la consultation",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas ", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='oldiag_kel',
                text="Diagnostic posé",
                options=[
                    AnswerOption(value='a', label="Syndrome d'Asperger", score=0),
                    AnswerOption(value='b', label="Autisme de haut niveau", score=1),
                    AnswerOption(value='c', label="Autisme", score=2),
                    AnswerOption(value='d', label="TSA NOS", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='oldiag_ki',
                text="Par qui",
                options=[
                    AnswerOption(value='a', label="Psychiatre/ Pédopsychiatre", score=0),
                    AnswerOption(value='b', label="Pédiatre", score=1),
                    AnswerOption(value='c', label="Généraliste", score=2),
                    AnswerOption(value='d', label="Autre", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='progress_trt',
                text="Traitement en cours",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='trt_non_parmaco',
                text="Prise en charge non pharmacologique",
                options=[
                    AnswerOption(value='0', label="1", score=0),
                    AnswerOption(value='1', label="2", score=1),
                    AnswerOption(value='2', label="3", score=2),
                    AnswerOption(value='3', label="4", score=3),
                    AnswerOption(value='4', label="5", score=4),
                    AnswerOption(value='5', label="6", score=5),
                    AnswerOption(value='6', label="7", score=6),
                    AnswerOption(value='7', label="8", score=7),
                    AnswerOption(value='8', label="9", score=8),
                    AnswerOption(value='9', label="10", score=9),
                    AnswerOption(value='10', label="11", score=10),
                    AnswerOption(value='11', label="12", score=11)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="SCREENING",
            name="SCREENING Questionnaire",
            description="50 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=25,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute SCREENING score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
