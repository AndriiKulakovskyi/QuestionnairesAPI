"""
PTHF - PTHF Questionnaire
=========================

63 items questionnaire

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


@register_questionnaire("PTHF")
@dataclass
class Pthf(BaseQuestionnaire):
    """PTHF Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize PTHF questionnaire with all 63 items."""
        
        questions_list = [
            Question(
                id='mbct_et',
                text="EXPERTISE DU THERAPEUTE",
                options=[
                    AnswerOption(value='a', label="NON CONNU", score=0),
                    AnswerOption(value='b', label="PAS DE QUALIFICATION SPECIFIQUE", score=1),
                    AnswerOption(value='c', label="THERAPEUTE STAGIAIRE", score=2),
                    AnswerOption(value='d', label="THERAPEUTE EN SUPERVISION", score=3),
                    AnswerOption(value='e', label="THERAPEUTE SENIOR INDEPENDANT", score=4),
                    AnswerOption(value='f', label="THERAPEUTE EXPERT", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mbct_mot_fin_the',
                text="MOTIF DE FIN DE THERAPIE",
                options=[
                    AnswerOption(value='a', label="EN COURS", score=0),
                    AnswerOption(value='b', label="PATIENT A  DECIDE D’ARRETER", score=1),
                    AnswerOption(value='c', label="LE THERAPEUTE A RECOMMANDER L’ARRET", score=2),
                    AnswerOption(value='d', label="DECISION COMMUNE DU PATIENT ET DU THERAPEUTE", score=3),
                    AnswerOption(value='e', label="AUTRES", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mbct_result',
                text="RESULTAT:",
                options=[
                    AnswerOption(value='a', label="PAS D’AMELIORATION", score=0),
                    AnswerOption(value='b', label="AMELIORATION MINIME", score=1),
                    AnswerOption(value='c', label="AMELIORATION CERTAINE", score=2),
                    AnswerOption(value='d', label="AMELIORATION DEFINIE", score=3),
                    AnswerOption(value='e', label="AMELIORATION SOUTENUE", score=4),
                    AnswerOption(value='f', label="REMISSION COMPLETE", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tautre_et',
                text="EXPERTISE DU THERAPEUTE",
                options=[
                    AnswerOption(value='a', label="NON CONNU", score=0),
                    AnswerOption(value='b', label="PAS DE QUALIFICATION SPECIFIQUE", score=1),
                    AnswerOption(value='c', label="THERAPEUTE STAGIAIRE", score=2),
                    AnswerOption(value='d', label="THERAPEUTE EN SUPERVISION", score=3),
                    AnswerOption(value='e', label="THERAPEUTE SENIOR INDEPENDANT", score=4),
                    AnswerOption(value='f', label="THERAPEUTE EXPERT", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tautre_mot_fin_the',
                text="MOTIF DE FIN DE THERAPIE",
                options=[
                    AnswerOption(value='a', label="EN COURS", score=0),
                    AnswerOption(value='b', label="PATIENT A  DECIDE D’ARRETER", score=1),
                    AnswerOption(value='c', label="LE THERAPEUTE A RECOMMANDER L’ARRET", score=2),
                    AnswerOption(value='d', label="DECISION COMMUNE DU PATIENT ET DU THERAPEUTE", score=3),
                    AnswerOption(value='e', label="AUTRES", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tautre_result',
                text="RESULTAT:",
                options=[
                    AnswerOption(value='a', label="PAS D’AMELIORATION", score=0),
                    AnswerOption(value='b', label="AMELIORATION MINIME", score=1),
                    AnswerOption(value='c', label="AMELIORATION CERTAINE", score=2),
                    AnswerOption(value='d', label="AMELIORATION DEFINIE", score=3),
                    AnswerOption(value='e', label="AMELIORATION SOUTENUE", score=4),
                    AnswerOption(value='f', label="REMISSION COMPLETE", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tautres_off',
                text="Autres thérapie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcec_et',
                text="EXPERTISE DU THERAPEUTE",
                options=[
                    AnswerOption(value='a', label="NON CONNU", score=0),
                    AnswerOption(value='b', label="PAS DE QUALIFICATION SPECIFIQUE", score=1),
                    AnswerOption(value='c', label="THERAPEUTE STAGIAIRE", score=2),
                    AnswerOption(value='d', label="THERAPEUTE EN SUPERVISION", score=3),
                    AnswerOption(value='e', label="THERAPEUTE SENIOR INDEPENDANT", score=4),
                    AnswerOption(value='f', label="THERAPEUTE EXPERT", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcec_mot_fin_the',
                text="MOTIF DE FIN DE THERAPIE",
                options=[
                    AnswerOption(value='a', label="EN COURS", score=0),
                    AnswerOption(value='b', label="PATIENT A  DECIDE D’ARRETER", score=1),
                    AnswerOption(value='c', label="LE THERAPEUTE A RECOMMANDER L’ARRET", score=2),
                    AnswerOption(value='d', label="DECISION COMMUNE DU PATIENT ET DU THERAPEUTE", score=3),
                    AnswerOption(value='e', label="AUTRES", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcec_off',
                text="Thérapie comportementale et cognitive",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcec_result',
                text="RESULTAT:",
                options=[
                    AnswerOption(value='a', label="PAS D’AMELIORATION", score=0),
                    AnswerOption(value='b', label="AMELIORATION MINIME", score=1),
                    AnswerOption(value='c', label="AMELIORATION CERTAINE", score=2),
                    AnswerOption(value='d', label="AMELIORATION DEFINIE", score=3),
                    AnswerOption(value='e', label="AMELIORATION SOUTENUE", score=4),
                    AnswerOption(value='f', label="REMISSION COMPLETE", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcoana_et',
                text="EXPERTISE DU THERAPEUTE",
                options=[
                    AnswerOption(value='a', label="NON CONNU", score=0),
                    AnswerOption(value='b', label="PAS DE QUALIFICATION SPECIFIQUE", score=1),
                    AnswerOption(value='c', label="THERAPEUTE STAGIAIRE", score=2),
                    AnswerOption(value='d', label="THERAPEUTE EN SUPERVISION", score=3),
                    AnswerOption(value='e', label="THERAPEUTE SENIOR INDEPENDANT", score=4),
                    AnswerOption(value='f', label="THERAPEUTE EXPERT", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcoana_mot_fin_the',
                text="MOTIF DE FIN DE THERAPIE",
                options=[
                    AnswerOption(value='a', label="EN COURS", score=0),
                    AnswerOption(value='b', label="PATIENT A  DECIDE D’ARRETER", score=1),
                    AnswerOption(value='c', label="LE THERAPEUTE A RECOMMANDER L’ARRET", score=2),
                    AnswerOption(value='d', label="DECISION COMMUNE DU PATIENT ET DU THERAPEUTE", score=3),
                    AnswerOption(value='e', label="AUTRES", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcoana_off',
                text="Thérapie cognitive analytique",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcoana_result',
                text="RESULTAT:",
                options=[
                    AnswerOption(value='a', label="PAS D’AMELIORATION", score=0),
                    AnswerOption(value='b', label="AMELIORATION MINIME", score=1),
                    AnswerOption(value='c', label="AMELIORATION CERTAINE", score=2),
                    AnswerOption(value='d', label="AMELIORATION DEFINIE", score=3),
                    AnswerOption(value='e', label="AMELIORATION SOUTENUE", score=4),
                    AnswerOption(value='f', label="REMISSION COMPLETE", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcogn_et',
                text="EXPERTISE DU THERAPEUTE",
                options=[
                    AnswerOption(value='a', label="NON CONNU", score=0),
                    AnswerOption(value='b', label="PAS DE QUALIFICATION SPECIFIQUE", score=1),
                    AnswerOption(value='c', label="THERAPEUTE STAGIAIRE", score=2),
                    AnswerOption(value='d', label="THERAPEUTE EN SUPERVISION", score=3),
                    AnswerOption(value='e', label="THERAPEUTE SENIOR INDEPENDANT", score=4),
                    AnswerOption(value='f', label="THERAPEUTE EXPERT", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcogn_mot_fin_the',
                text="MOTIF DE FIN DE THERAPIE",
                options=[
                    AnswerOption(value='a', label="EN COURS", score=0),
                    AnswerOption(value='b', label="PATIENT A  DECIDE D’ARRETER", score=1),
                    AnswerOption(value='c', label="LE THERAPEUTE A RECOMMANDER L’ARRET", score=2),
                    AnswerOption(value='d', label="DECISION COMMUNE DU PATIENT ET DU THERAPEUTE", score=3),
                    AnswerOption(value='e', label="AUTRES", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcogn_off',
                text="Thérapie cognitive",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcogn_result',
                text="RESULTAT:",
                options=[
                    AnswerOption(value='a', label="PAS D’AMELIORATION", score=0),
                    AnswerOption(value='b', label="AMELIORATION MINIME", score=1),
                    AnswerOption(value='c', label="AMELIORATION CERTAINE", score=2),
                    AnswerOption(value='d', label="AMELIORATION DEFINIE", score=3),
                    AnswerOption(value='e', label="AMELIORATION SOUTENUE", score=4),
                    AnswerOption(value='f', label="REMISSION COMPLETE", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcom_result',
                text="RESULTAT:",
                options=[
                    AnswerOption(value='a', label="PAS D’AMELIORATION", score=0),
                    AnswerOption(value='b', label="AMELIORATION MINIME", score=1),
                    AnswerOption(value='c', label="AMELIORATION CERTAINE", score=2),
                    AnswerOption(value='d', label="AMELIORATION DEFINIE", score=3),
                    AnswerOption(value='e', label="AMELIORATION SOUTENUE", score=4),
                    AnswerOption(value='f', label="REMISSION COMPLETE", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcomp_et',
                text="EXPERTISE DU THERAPEUTE",
                options=[
                    AnswerOption(value='a', label="NON CONNU", score=0),
                    AnswerOption(value='b', label="PAS DE QUALIFICATION SPECIFIQUE", score=1),
                    AnswerOption(value='c', label="THERAPEUTE STAGIAIRE", score=2),
                    AnswerOption(value='d', label="THERAPEUTE EN SUPERVISION", score=3),
                    AnswerOption(value='e', label="THERAPEUTE SENIOR INDEPENDANT", score=4),
                    AnswerOption(value='f', label="THERAPEUTE EXPERT", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcomp_mot_fin_the',
                text="MOTIF DE FIN DE THERAPIE",
                options=[
                    AnswerOption(value='a', label="EN COURS", score=0),
                    AnswerOption(value='b', label="PATIENT A  DECIDE D’ARRETER", score=1),
                    AnswerOption(value='c', label="LE THERAPEUTE A RECOMMANDER L’ARRET", score=2),
                    AnswerOption(value='d', label="DECISION COMMUNE DU PATIENT ET DU THERAPEUTE", score=3),
                    AnswerOption(value='e', label="AUTRES", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcomp_off',
                text="Thérapie comportementale",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcouple_et',
                text="EXPERTISE DU THERAPEUTE",
                options=[
                    AnswerOption(value='a', label="NON CONNU", score=0),
                    AnswerOption(value='b', label="PAS DE QUALIFICATION SPECIFIQUE", score=1),
                    AnswerOption(value='c', label="THERAPEUTE STAGIAIRE", score=2),
                    AnswerOption(value='d', label="THERAPEUTE EN SUPERVISION", score=3),
                    AnswerOption(value='e', label="THERAPEUTE SENIOR INDEPENDANT", score=4),
                    AnswerOption(value='f', label="THERAPEUTE EXPERT", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcouple_mot_fin_the',
                text="MOTIF DE FIN DE THERAPIE",
                options=[
                    AnswerOption(value='a', label="EN COURS", score=0),
                    AnswerOption(value='b', label="PATIENT A  DECIDE D’ARRETER", score=1),
                    AnswerOption(value='c', label="LE THERAPEUTE A RECOMMANDER L’ARRET", score=2),
                    AnswerOption(value='d', label="DECISION COMMUNE DU PATIENT ET DU THERAPEUTE", score=3),
                    AnswerOption(value='e', label="AUTRES", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcouple_off',
                text="Thérapie de couple",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tcouple_result',
                text="RESULTAT:",
                options=[
                    AnswerOption(value='a', label="PAS D’AMELIORATION", score=0),
                    AnswerOption(value='b', label="AMELIORATION MINIME", score=1),
                    AnswerOption(value='c', label="AMELIORATION CERTAINE", score=2),
                    AnswerOption(value='d', label="AMELIORATION DEFINIE", score=3),
                    AnswerOption(value='e', label="AMELIORATION SOUTENUE", score=4),
                    AnswerOption(value='f', label="REMISSION COMPLETE", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdiacom_et',
                text="EXPERTISE DU THERAPEUTE",
                options=[
                    AnswerOption(value='a', label="NON CONNU", score=0),
                    AnswerOption(value='b', label="PAS DE QUALIFICATION SPECIFIQUE", score=1),
                    AnswerOption(value='c', label="THERAPEUTE STAGIAIRE", score=2),
                    AnswerOption(value='d', label="THERAPEUTE EN SUPERVISION", score=3),
                    AnswerOption(value='e', label="THERAPEUTE SENIOR INDEPENDANT", score=4),
                    AnswerOption(value='f', label="THERAPEUTE EXPERT", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdiacom_mot_fin_the',
                text="MOTIF DE FIN DE THERAPIE",
                options=[
                    AnswerOption(value='a', label="EN COURS", score=0),
                    AnswerOption(value='b', label="PATIENT A  DECIDE D’ARRETER", score=1),
                    AnswerOption(value='c', label="LE THERAPEUTE A RECOMMANDER L’ARRET", score=2),
                    AnswerOption(value='d', label="DECISION COMMUNE DU PATIENT ET DU THERAPEUTE", score=3),
                    AnswerOption(value='e', label="AUTRES", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdiacom_off',
                text="Thérapie dialectique comportementale",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdiacom_result',
                text="RESULTAT:",
                options=[
                    AnswerOption(value='a', label="PAS D’AMELIORATION", score=0),
                    AnswerOption(value='b', label="AMELIORATION MINIME", score=1),
                    AnswerOption(value='c', label="AMELIORATION CERTAINE", score=2),
                    AnswerOption(value='d', label="AMELIORATION DEFINIE", score=3),
                    AnswerOption(value='e', label="AMELIORATION SOUTENUE", score=4),
                    AnswerOption(value='f', label="REMISSION COMPLETE", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='teea_et',
                text="EXPERTISE DU THERAPEUTE",
                options=[
                    AnswerOption(value='a', label="NON CONNU", score=0),
                    AnswerOption(value='b', label="PAS DE QUALIFICATION SPECIFIQUE", score=1),
                    AnswerOption(value='c', label="THERAPEUTE STAGIAIRE", score=2),
                    AnswerOption(value='d', label="THERAPEUTE EN SUPERVISION", score=3),
                    AnswerOption(value='e', label="THERAPEUTE SENIOR INDEPENDANT", score=4),
                    AnswerOption(value='f', label="THERAPEUTE EXPERT", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='teea_mot_fin_the',
                text="MOTIF DE FIN DE THERAPIE",
                options=[
                    AnswerOption(value='a', label="EN COURS", score=0),
                    AnswerOption(value='b', label="PATIENT A  DECIDE D’ARRETER", score=1),
                    AnswerOption(value='c', label="LE THERAPEUTE A RECOMMANDER L’ARRET", score=2),
                    AnswerOption(value='d', label="DECISION COMMUNE DU PATIENT ET DU THERAPEUTE", score=3),
                    AnswerOption(value='e', label="AUTRES", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='teea_off',
                text="Thérapie d'engagement et d'acceptation",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='teea_result',
                text="RESULTAT:",
                options=[
                    AnswerOption(value='a', label="PAS D’AMELIORATION", score=0),
                    AnswerOption(value='b', label="AMELIORATION MINIME", score=1),
                    AnswerOption(value='c', label="AMELIORATION CERTAINE", score=2),
                    AnswerOption(value='d', label="AMELIORATION DEFINIE", score=3),
                    AnswerOption(value='e', label="AMELIORATION SOUTENUE", score=4),
                    AnswerOption(value='f', label="REMISSION COMPLETE", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tfami_et',
                text="EXPERTISE DU THERAPEUTE",
                options=[
                    AnswerOption(value='a', label="NON CONNU", score=0),
                    AnswerOption(value='b', label="PAS DE QUALIFICATION SPECIFIQUE", score=1),
                    AnswerOption(value='c', label="THERAPEUTE STAGIAIRE", score=2),
                    AnswerOption(value='d', label="THERAPEUTE EN SUPERVISION", score=3),
                    AnswerOption(value='e', label="THERAPEUTE SENIOR INDEPENDANT", score=4),
                    AnswerOption(value='f', label="THERAPEUTE EXPERT", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tfami_mot_fin_the',
                text="MOTIF DE FIN DE THERAPIE",
                options=[
                    AnswerOption(value='a', label="EN COURS", score=0),
                    AnswerOption(value='b', label="PATIENT A  DECIDE D’ARRETER", score=1),
                    AnswerOption(value='c', label="LE THERAPEUTE A RECOMMANDER L’ARRET", score=2),
                    AnswerOption(value='d', label="DECISION COMMUNE DU PATIENT ET DU THERAPEUTE", score=3),
                    AnswerOption(value='e', label="AUTRES", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tfami_off',
                text="Thérapie familiale",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tfami_result',
                text="RESULTAT:",
                options=[
                    AnswerOption(value='a', label="PAS D’AMELIORATION", score=0),
                    AnswerOption(value='b', label="AMELIORATION MINIME", score=1),
                    AnswerOption(value='c', label="AMELIORATION CERTAINE", score=2),
                    AnswerOption(value='d', label="AMELIORATION DEFINIE", score=3),
                    AnswerOption(value='e', label="AMELIORATION SOUTENUE", score=4),
                    AnswerOption(value='f', label="REMISSION COMPLETE", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tgroupe_et',
                text="EXPERTISE DU THERAPEUTE",
                options=[
                    AnswerOption(value='a', label="NON CONNU", score=0),
                    AnswerOption(value='b', label="PAS DE QUALIFICATION SPECIFIQUE", score=1),
                    AnswerOption(value='c', label="THERAPEUTE STAGIAIRE", score=2),
                    AnswerOption(value='d', label="THERAPEUTE EN SUPERVISION", score=3),
                    AnswerOption(value='e', label="THERAPEUTE SENIOR INDEPENDANT", score=4),
                    AnswerOption(value='f', label="THERAPEUTE EXPERT", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tgroupe_mot_fin_the',
                text="MOTIF DE FIN DE THERAPIE",
                options=[
                    AnswerOption(value='a', label="EN COURS", score=0),
                    AnswerOption(value='b', label="PATIENT A  DECIDE D’ARRETER", score=1),
                    AnswerOption(value='c', label="LE THERAPEUTE A RECOMMANDER L’ARRET", score=2),
                    AnswerOption(value='d', label="DECISION COMMUNE DU PATIENT ET DU THERAPEUTE", score=3),
                    AnswerOption(value='e', label="AUTRES", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tgroupe_off',
                text="Thérapie de groupe",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tgroupe_result',
                text="RESULTAT:",
                options=[
                    AnswerOption(value='a', label="PAS D’AMELIORATION", score=0),
                    AnswerOption(value='b', label="AMELIORATION MINIME", score=1),
                    AnswerOption(value='c', label="AMELIORATION CERTAINE", score=2),
                    AnswerOption(value='d', label="AMELIORATION DEFINIE", score=3),
                    AnswerOption(value='e', label="AMELIORATION SOUTENUE", score=4),
                    AnswerOption(value='f', label="REMISSION COMPLETE", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tinter_et',
                text="EXPERTISE DU THERAPEUTE",
                options=[
                    AnswerOption(value='a', label="NON CONNU", score=0),
                    AnswerOption(value='b', label="PAS DE QUALIFICATION SPECIFIQUE", score=1),
                    AnswerOption(value='c', label="THERAPEUTE STAGIAIRE", score=2),
                    AnswerOption(value='d', label="THERAPEUTE EN SUPERVISION", score=3),
                    AnswerOption(value='e', label="THERAPEUTE SENIOR INDEPENDANT", score=4),
                    AnswerOption(value='f', label="THERAPEUTE EXPERT", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tinter_mot_fin_the',
                text="MOTIF DE FIN DE THERAPIE",
                options=[
                    AnswerOption(value='a', label="EN COURS", score=0),
                    AnswerOption(value='b', label="PATIENT A  DECIDE D’ARRETER", score=1),
                    AnswerOption(value='c', label="LE THERAPEUTE A RECOMMANDER L’ARRET", score=2),
                    AnswerOption(value='d', label="DECISION COMMUNE DU PATIENT ET DU THERAPEUTE", score=3),
                    AnswerOption(value='e', label="AUTRES", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tinter_off',
                text="Thérapie interpersonnelle",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tinter_result',
                text="RESULTAT:",
                options=[
                    AnswerOption(value='a', label="PAS D’AMELIORATION", score=0),
                    AnswerOption(value='b', label="AMELIORATION MINIME", score=1),
                    AnswerOption(value='c', label="AMELIORATION CERTAINE", score=2),
                    AnswerOption(value='d', label="AMELIORATION DEFINIE", score=3),
                    AnswerOption(value='e', label="AMELIORATION SOUTENUE", score=4),
                    AnswerOption(value='f', label="REMISSION COMPLETE", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tpcons_et',
                text="EXPERTISE DU THERAPEUTE",
                options=[
                    AnswerOption(value='a', label="NON CONNU", score=0),
                    AnswerOption(value='b', label="PAS DE QUALIFICATION SPECIFIQUE", score=1),
                    AnswerOption(value='c', label="THERAPEUTE STAGIAIRE", score=2),
                    AnswerOption(value='d', label="THERAPEUTE EN SUPERVISION", score=3),
                    AnswerOption(value='e', label="THERAPEUTE SENIOR INDEPENDANT", score=4),
                    AnswerOption(value='f', label="THERAPEUTE EXPERT", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tpcons_mot_fin_the',
                text="MOTIF DE FIN DE THERAPIE",
                options=[
                    AnswerOption(value='a', label="EN COURS", score=0),
                    AnswerOption(value='b', label="PATIENT A  DECIDE D’ARRETER", score=1),
                    AnswerOption(value='c', label="LE THERAPEUTE A RECOMMANDER L’ARRET", score=2),
                    AnswerOption(value='d', label="DECISION COMMUNE DU PATIENT ET DU THERAPEUTE", score=3),
                    AnswerOption(value='e', label="AUTRES", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tpcons_off',
                text="Thérapie en pleine conscience",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tpcons_result',
                text="RESULTAT:",
                options=[
                    AnswerOption(value='a', label="PAS D’AMELIORATION", score=0),
                    AnswerOption(value='b', label="AMELIORATION MINIME", score=1),
                    AnswerOption(value='c', label="AMELIORATION CERTAINE", score=2),
                    AnswerOption(value='d', label="AMELIORATION DEFINIE", score=3),
                    AnswerOption(value='e', label="AMELIORATION SOUTENUE", score=4),
                    AnswerOption(value='f', label="REMISSION COMPLETE", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tpsyanal_et',
                text="EXPERTISE DU THERAPEUTE",
                options=[
                    AnswerOption(value='a', label="NON CONNU", score=0),
                    AnswerOption(value='b', label="PAS DE QUALIFICATION SPECIFIQUE", score=1),
                    AnswerOption(value='c', label="THERAPEUTE STAGIAIRE", score=2),
                    AnswerOption(value='d', label="THERAPEUTE EN SUPERVISION", score=3),
                    AnswerOption(value='e', label="THERAPEUTE SENIOR INDEPENDANT", score=4),
                    AnswerOption(value='f', label="THERAPEUTE EXPERT", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tpsyanal_mot_fin_the',
                text="MOTIF DE FIN DE THERAPIE",
                options=[
                    AnswerOption(value='a', label="EN COURS", score=0),
                    AnswerOption(value='b', label="PATIENT A  DECIDE D’ARRETER", score=1),
                    AnswerOption(value='c', label="LE THERAPEUTE A RECOMMANDER L’ARRET", score=2),
                    AnswerOption(value='d', label="DECISION COMMUNE DU PATIENT ET DU THERAPEUTE", score=3),
                    AnswerOption(value='e', label="AUTRES", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tpsyanal_off',
                text="Psychothérapie psychanalytique",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tpsyanal_result',
                text="RESULTAT:",
                options=[
                    AnswerOption(value='a', label="PAS D’AMELIORATION", score=0),
                    AnswerOption(value='b', label="AMELIORATION MINIME", score=1),
                    AnswerOption(value='c', label="AMELIORATION CERTAINE", score=2),
                    AnswerOption(value='d', label="AMELIORATION DEFINIE", score=3),
                    AnswerOption(value='e', label="AMELIORATION SOUTENUE", score=4),
                    AnswerOption(value='f', label="REMISSION COMPLETE", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tpsydyna_et',
                text="EXPERTISE DU THERAPEUTE",
                options=[
                    AnswerOption(value='a', label="NON CONNU", score=0),
                    AnswerOption(value='b', label="PAS DE QUALIFICATION SPECIFIQUE", score=1),
                    AnswerOption(value='c', label="THERAPEUTE STAGIAIRE", score=2),
                    AnswerOption(value='d', label="THERAPEUTE EN SUPERVISION", score=3),
                    AnswerOption(value='e', label="THERAPEUTE SENIOR INDEPENDANT", score=4),
                    AnswerOption(value='f', label="THERAPEUTE EXPERT", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tpsydyna_mot_fin_the',
                text="MOTIF DE FIN DE THERAPIE",
                options=[
                    AnswerOption(value='a', label="EN COURS", score=0),
                    AnswerOption(value='b', label="PATIENT A  DECIDE D’ARRETER", score=1),
                    AnswerOption(value='c', label="LE THERAPEUTE A RECOMMANDER L’ARRET", score=2),
                    AnswerOption(value='d', label="DECISION COMMUNE DU PATIENT ET DU THERAPEUTE", score=3),
                    AnswerOption(value='e', label="AUTRES", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tpsydyna_off',
                text="Psychothérapie psychodynamique",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tpsydyna_result',
                text="RESULTAT:",
                options=[
                    AnswerOption(value='a', label="PAS D’AMELIORATION", score=0),
                    AnswerOption(value='b', label="AMELIORATION MINIME", score=1),
                    AnswerOption(value='c', label="AMELIORATION CERTAINE", score=2),
                    AnswerOption(value='d', label="AMELIORATION DEFINIE", score=3),
                    AnswerOption(value='e', label="AMELIORATION SOUTENUE", score=4),
                    AnswerOption(value='f', label="REMISSION COMPLETE", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tsnd_et',
                text="EXPERTISE DU THERAPEUTE",
                options=[
                    AnswerOption(value='a', label="NON CONNU", score=0),
                    AnswerOption(value='b', label="PAS DE QUALIFICATION SPECIFIQUE", score=1),
                    AnswerOption(value='c', label="THERAPEUTE STAGIAIRE", score=2),
                    AnswerOption(value='d', label="THERAPEUTE EN SUPERVISION", score=3),
                    AnswerOption(value='e', label="THERAPEUTE SENIOR INDEPENDANT", score=4),
                    AnswerOption(value='f', label="THERAPEUTE EXPERT", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tsnd_mot_fin_the',
                text="MOTIF DE FIN DE THERAPIE",
                options=[
                    AnswerOption(value='a', label="EN COURS", score=0),
                    AnswerOption(value='b', label="PATIENT A  DECIDE D’ARRETER", score=1),
                    AnswerOption(value='c', label="LE THERAPEUTE A RECOMMANDER L’ARRET", score=2),
                    AnswerOption(value='d', label="DECISION COMMUNE DU PATIENT ET DU THERAPEUTE", score=3),
                    AnswerOption(value='e', label="AUTRES", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tsnd_off',
                text="Thérapie de soutien ou non dirigée",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tsnd_result',
                text="RESULTAT:",
                options=[
                    AnswerOption(value='a', label="PAS D’AMELIORATION", score=0),
                    AnswerOption(value='b', label="AMELIORATION MINIME", score=1),
                    AnswerOption(value='c', label="AMELIORATION CERTAINE", score=2),
                    AnswerOption(value='d', label="AMELIORATION DEFINIE", score=3),
                    AnswerOption(value='e', label="AMELIORATION SOUTENUE", score=4),
                    AnswerOption(value='f', label="REMISSION COMPLETE", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="PTHF",
            name="PTHF Questionnaire",
            description="63 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=31,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute PTHF score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
