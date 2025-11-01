"""
AUT_MEDECO2P - AUT_MEDECO2P Questionnaire
=========================================

51 items questionnaire

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


@register_questionnaire("AUT_MEDECO2P")
@dataclass
class AutMedeco2p(BaseQuestionnaire):
    """AUT_MEDECO2P Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_MEDECO2P questionnaire with all 51 items."""
        
        questions_list = [
            Question(
                id='abse1',
                text="Avez-vous du vous absenter au cours de ces contrats de travail pour vous occuper de votre enfant ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abse2',
                text="Avez-vous du vous absenter au cours de ces contrats de travail pour vous occuper de votre enfant ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ant1',
                text="Si oui, indiquez",
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
            ),
            Question(
                id='ant2',
                text="Si oui, indiquez",
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
            ),
            Question(
                id='apid1',
                text="Parent/représentant légal 1",
                options=[
                    AnswerOption(value='a', label="Mère", score=0),
                    AnswerOption(value='b', label="Père", score=1),
                    AnswerOption(value='c', label="Autre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='apid2',
                text="Parent/représentant légal 2",
                options=[
                    AnswerOption(value='a', label="Mère", score=0),
                    AnswerOption(value='b', label="Père", score=1),
                    AnswerOption(value='c', label="Autre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='contra1',
                text="Travail",
                options=[
                    AnswerOption(value='a', label="en CDD", score=0),
                    AnswerOption(value='b', label="en CDI", score=1),
                    AnswerOption(value='c', label="en libéral", score=2),
                    AnswerOption(value='d', label="en auto-entrepreneur", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='contra2',
                text="Travail",
                options=[
                    AnswerOption(value='a', label="en CDD", score=0),
                    AnswerOption(value='b', label="en CDI", score=1),
                    AnswerOption(value='c', label="en libéral", score=2),
                    AnswerOption(value='d', label="en auto-entrepreneur", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dsmv1',
                text="Si oui, indiquez",
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
                    AnswerOption(value='14', label="15", score=14)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dsmv2',
                text="Si oui, indiquez",
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
                    AnswerOption(value='14', label="15", score=14)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='edulevel1',
                text="Niveau maximal atteint",
                options=[
                    AnswerOption(value='a', label="Ecole primaire", score=0),
                    AnswerOption(value='b', label="Collège", score=1),
                    AnswerOption(value='c', label="CAP / BEP", score=2),
                    AnswerOption(value='d', label="BAC", score=3),
                    AnswerOption(value='e', label="BAC +", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='edulevel2',
                text="Niveau maximal atteint",
                options=[
                    AnswerOption(value='a', label="Ecole primaire", score=0),
                    AnswerOption(value='b', label="Collège", score=1),
                    AnswerOption(value='c', label="CAP / BEP", score=2),
                    AnswerOption(value='d', label="BAC", score=3),
                    AnswerOption(value='e', label="BAC +", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empjob1',
                text="Quelle est votre catégorie socio-professionnelle ?",
                options=[
                    AnswerOption(value='a', label="Cadres dirigeants", score=0),
                    AnswerOption(value='b', label="Professions intellectuelles et scientifiques", score=1),
                    AnswerOption(value='c', label="Professions intermédiaires salariées", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empjob2',
                text="Quelle est votre catégorie socio-professionnelle ?",
                options=[
                    AnswerOption(value='a', label="Cadres dirigeants", score=0),
                    AnswerOption(value='b', label="Professions intellectuelles et scientifiques", score=1),
                    AnswerOption(value='c', label="Professions intermédiaires salariées", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='garde1',
                text="Mode de garde de l'enfant concerné",
                options=[
                    AnswerOption(value='a', label="Garde totale", score=0),
                    AnswerOption(value='b', label="Garde Alternée avec une semaine sur deux et moitié des vacances scolaires", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='garde2',
                text="Mode de garde de l'enfant concerné",
                options=[
                    AnswerOption(value='a', label="Garde totale", score=0),
                    AnswerOption(value='b', label="Garde Alternée avec une semaine sur deux et moitié des vacances scolaires", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='grpar1',
                text="Durant les 12 derniers mois avez-vous participé à un Groupe parent ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='grpar2',
                text="Durant les 12 derniers mois avez-vous participé à un Groupe parent ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='jobclas1',
                text="Travail",
                options=[
                    AnswerOption(value='a', label="à temps plein", score=0),
                    AnswerOption(value='b', label="à temps partiel", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='jobclas2',
                text="Travail",
                options=[
                    AnswerOption(value='a', label="à temps plein", score=0),
                    AnswerOption(value='b', label="à temps partiel", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lang1',
                text="Langue maternelle",
                options=[
                    AnswerOption(value='a', label="Français", score=0),
                    AnswerOption(value='b', label="Bilingue français ", score=1),
                    AnswerOption(value='c', label="Autre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lang2',
                text="Langue maternelle",
                options=[
                    AnswerOption(value='a', label="Français", score=0),
                    AnswerOption(value='b', label="Bilingue français ", score=1),
                    AnswerOption(value='c', label="Autre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='levlang1',
                text="Niveau de français",
                options=[
                    AnswerOption(value='a', label="Très bon/bon en compréhension et en expression", score=0),
                    AnswerOption(value='b', label="Difficultés d'expression orale uniquement", score=1),
                    AnswerOption(value='c', label="Difficultés en compréhension orale uniquement", score=2),
                    AnswerOption(value='d', label="Difficultés d'expression et de compréhension orale", score=3),
                    AnswerOption(value='e', label="Difficultés de lecture et d'écriture", score=4),
                    AnswerOption(value='f', label="Aucune notion de français, besoin d'un interprète", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='levlang2',
                text="Niveau de français",
                options=[
                    AnswerOption(value='a', label="Très bon/bon en compréhension et en expression", score=0),
                    AnswerOption(value='b', label="Difficultés d'expression orale uniquement", score=1),
                    AnswerOption(value='c', label="Difficultés en compréhension orale uniquement", score=2),
                    AnswerOption(value='d', label="Difficultés d'expression et de compréhension orale", score=3),
                    AnswerOption(value='e', label="Difficultés de lecture et d'écriture", score=4),
                    AnswerOption(value='f', label="Aucune notion de français, besoin d'un interprète", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lieu_medp1',
                text="Le clinicien exerce",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lieu_medp2',
                text="Le clinicien exerce",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lieu_psyg1',
                text="Le clinicien exerce",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lieu_psyg2',
                text="Le clinicien exerce",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='marist',
                text="Situation du couple parental ",
                options=[
                    AnswerOption(value='a', label="En union libre/pacsés/mariés", score=0),
                    AnswerOption(value='b', label="Séparés", score=1),
                    AnswerOption(value='c', label="Divorcés", score=2),
                    AnswerOption(value='d', label="Veuf/veuve", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='marista1',
                text="Si couple séparé/divorcé, le parent 1 est-il dans une nouvelle relation ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='marista2',
                text="Si couple séparé/divorcé, le parent 1 est-il dans une nouvelle relation ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='medg1',
                text="Avez-vous consulté durant les 12 derniers mois chez un médecin généraliste ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='medg2',
                text="Avez-vous consulté durant les 12 derniers mois chez un médecin généraliste ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='medp1',
                text="Avez-vous consulté durant les 12 derniers mois chez un médecin psychiatre ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='medp2',
                text="Avez-vous consulté durant les 12 derniers mois chez un médecin psychiatre ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='modalw1',
                text="Est-ce que les particularités développementales de votre enfant ont entraînées un changement dans vos modalités de travail pour vous ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='modalw2',
                text="Est-ce que les particularités développementales de votre enfant ont entraînées un changement dans vos modalités de travail pour vous ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='modalwa1',
                text="Si oui, précisez",
                options=[
                    AnswerOption(value='a', label="Passage à de l'auto-entreprenariat", score=0),
                    AnswerOption(value='b', label="Arrêt de travail", score=1),
                    AnswerOption(value='c', label="Réduction du temps de travail", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='modalwa2',
                text="Si oui, précisez",
                options=[
                    AnswerOption(value='a', label="Passage à de l'auto-entreprenariat", score=0),
                    AnswerOption(value='b', label="Arrêt de travail", score=1),
                    AnswerOption(value='c', label="Réduction du temps de travail", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='partic1',
                text="Si non, est-ce que l'absence de contrat de travail ou d'exercice de votre travail est liée aux particularités développementales de votre enfant ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='partic2',
                text="Si non, est-ce que l'absence de contrat de travail ou d'exercice de votre travail est liée aux particularités développementales de votre enfant ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pec021',
                text="Votre mutuelle couvre-t-elle certaines prises en charges de votre enfant ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pec041',
                text="Y a-t-il l'aide d'un taxi conventionné ou d'un VSL ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pec061',
                text="Avez-vous recourt à une personne que vous rémunérez pour garder votre enfant ou l'accompagner lors de diverses activités ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pec071',
                text="Avez-vous recours à une personne que vous ne rémunérez pas pour garder votre enfant ou l'accompagner lors de diverses activités?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psyg1',
                text="Avez-vous consulté durant les 12 derniers mois chez un psychologue ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psyg2',
                text="Avez-vous consulté durant les 12 derniers mois chez un psychologue ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='stpro1',
                text="Avez-vous eu un (des) contrat(s) de travail ou avez-vous exercé (auto-entrepreneur ou profession libérale) sur ces 12 derniers mois ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='stpro2',
                text="Avez-vous eu un (des) contrat(s) de travail ou avez-vous exercé (auto-entrepreneur ou profession libérale) sur ces 12 derniers mois ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='trtpsy1',
                text="Avez-vous un traitement psychoactifs ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='trtpsy2',
                text="Avez-vous un traitement psychoactifs ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_MEDECO2P",
            name="AUT_MEDECO2P Questionnaire",
            description="51 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=25,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_MEDECO2P score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
