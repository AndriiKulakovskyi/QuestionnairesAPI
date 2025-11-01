"""
NEUROPSY - NEUROPSY Questionnaire
=================================

46 items questionnaire

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


@register_questionnaire("NEUROPSY")
@dataclass
class Neuropsy(BaseQuestionnaire):
    """NEUROPSY Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize NEUROPSY questionnaire with all 46 items."""
        
        questions_list = [
            Question(
                id='begaiement',
                text="Bégaiement",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cafe_app',
                text="Avez-vous bu du café pendant la pause",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cafe_avp',
                text="Avez-vous bu du café avant de venir",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='convulsion',
                text="Convulsion",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='d2_test',
                text="D2",
                options=[
                    AnswerOption(value='a', label="1", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='doubl_tach_test',
                text="Double tâche de Baddeley",
                options=[
                    AnswerOption(value='a', label="1", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dyscalculie',
                text="Dyscalculie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dyslexie',
                text="Dyslexie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dysorthographie',
                text="dysorthographie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dysphasie',
                text="Dysphasie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dyspraxie',
                text="Dyspraxie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empan_test',
                text="Empan audio-verbal",
                options=[
                    AnswerOption(value='a', label="1", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='etat_cog',
                text="Etat clinique compatible avec la passation des tests cognitifs",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='feb_enf',
                text="fébrile dans la petite enfance",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='flue_verb_choi',
                text="Choix du questionnaire",
                options=[
                    AnswerOption(value='a', label="Animaux et lettre P", score=0),
                    AnswerOption(value='b', label="Fruits et lettre R", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fluence_test',
                text="Fluences verbales",
                options=[
                    AnswerOption(value='a', label="1", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fume_app',
                text="Avez-vous fumé pendant la pause ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fume_avp',
                text="Avez-vous fumé avant ce rendez-vous?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fumeur_avp',
                text="Etes-vous fumeur ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mem_dess_test',
                text="MEM IV : Dessin",
                options=[
                    AnswerOption(value='a', label="1", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='nb_tps_cafe_avp',
                text="Combien de temps avant ce rendez-vous",
                options=[
                    AnswerOption(value='a', label="5 à 30 min", score=0),
                    AnswerOption(value='b', label="< 1H", score=1),
                    AnswerOption(value='c', label="> 1H", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='nb_tps_fume_avp',
                text="Combien de temps avant ",
                options=[
                    AnswerOption(value='a', label="5 à 30 min", score=0),
                    AnswerOption(value='b', label="< 1H", score=1),
                    AnswerOption(value='c', label="> 1H", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='nb_tps_the_avp',
                text="Combien de temps avant ce rendez-vous",
                options=[
                    AnswerOption(value='a', label="5 à 30 min", score=0),
                    AnswerOption(value='b', label="< 1H", score=1),
                    AnswerOption(value='c', label="> 1H", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_abs',
                text="Absence illetrisme et d'alphabétisme",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_dalt',
                text="Absence de daltonisme ou de trouble visuel invalidant",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_lang',
                text="Langue maternelle française",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_lat',
                text="Latéralité",
                options=[
                    AnswerOption(value='a', label="Droite", score=0),
                    AnswerOption(value='b', label="Gauche", score=1),
                    AnswerOption(value='c', label="Ambidextre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_ret_par',
                text="Retard à l'acquisition de la parole",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_sismo',
                text="Pas de traitement par sismothérapie dans l’année écoulée",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_suspi',
                text="Suspicion des troubles des apprentissages et des acquisations",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_tro_aut',
                text="Absence de troubles auditifs non appareillés",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuro_trt_psy',
                text="Traitement psychotrope",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neuropsy_off',
                text="Partie neuropsy",
                options=[
                    AnswerOption(value='a', label="1", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='precocite',
                text="Précocité",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='retard_marche',
                text="Retard à l'acquisition de la marche",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rl_ri_test',
                text="RL-RI 16 items ",
                options=[
                    AnswerOption(value='a', label="1", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='svupdesn',
                text="Version simplifiée ?*",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdah_act',
                text="TDAH actuel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tdah_enf',
                text="TDAH dans l'enfance",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='the_app',
                text="Avez-vous bu du thé pendant la pause",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='the_avp',
                text="Avez-vous bu du thé avant de venir",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tmt_test',
                text="TMT",
                options=[
                    AnswerOption(value='a', label="1", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tps_etat',
                text="Temps écoulé depuis la dernière évaluation de l'état du patient",
                options=[
                    AnswerOption(value='a', label="Moins d'une semaine", score=0),
                    AnswerOption(value='b', label="plus d'une semaine", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='trou_app',
                text="Avez-vous eu des troubles de l'apprentissage?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='vit_trt_test',
                text="Vitesse traitement",
                options=[
                    AnswerOption(value='a', label="1", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais4_test',
                text="WAIS 4",
                options=[
                    AnswerOption(value='a', label="1", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="NEUROPSY",
            name="NEUROPSY Questionnaire",
            description="46 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=23,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute NEUROPSY score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
