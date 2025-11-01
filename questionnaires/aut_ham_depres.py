"""
AUT_HAM_DEPRES - AUT_HAM_DEPRES Questionnaire
=============================================

18 items questionnaire

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


@register_questionnaire("AUT_HAM_DEPRES")
@dataclass
class AutHamDepres(BaseQuestionnaire):
    """AUT_HAM_DEPRES Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_HAM_DEPRES questionnaire with all 18 items."""
        
        questions_list = [
            Question(
                id='hamd1',
                text="1 Humeur dépressive",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="Ces états affectifs ne sont signalés que si l'on interroge le sujet", score=1),
                    AnswerOption(value='c', label="Ces états affectifs sont signalés verbalement spontanément", score=2),
                    AnswerOption(value='d', label="Le sujet communique ces états affectifs non verbalement ; par ex. par son expression faciale, son attitude,", score=3),
                    AnswerOption(value='e', label="Le sujet ne communique PRATIQUEMENT QUE ces états affectifs dans ses communications spontanées", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamd10',
                text="10 Anxiété psychique",
                options=[
                    AnswerOption(value='a', label="Aucun trouble", score=0),
                    AnswerOption(value='b', label="Tension subjective et irritabilité", score=1),
                    AnswerOption(value='c', label="Se fait du souci à propos de problèmes mineurs", score=2),
                    AnswerOption(value='d', label="Attitude inquiète, apparente dans l'expression faciale et le langage", score=3),
                    AnswerOption(value='e', label="Peurs exprimées sans qu'on pose de questions", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamd12',
                text="12 Symptômes somatiques gastro-intestinaux",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Perte d'appétit, mais mange sans y être poussé par les infirmières. Sentiment de lourdeur abdominale", score=1),
                    AnswerOption(value='c', label="A des difficultés à manger en l'absence d'incitations du personnel. Demande ou a besoin de laxatifs, de", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamd13',
                text="13 Symptômes somatiques généraux",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Lourdeur dans les membres, dans le dos ou la tête. Douleurs dans le dos, céphalées, douleurs", score=1),
                    AnswerOption(value='c', label="Coter 2 au cas où n'importe quel symptôme est net", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamd14',
                text="14 Symptômes génitaux : symptômes tels que : perte de libido, troubles menstruels",
                options=[
                    AnswerOption(value='a', label="Absents", score=0),
                    AnswerOption(value='b', label="Légers", score=1),
                    AnswerOption(value='c', label="Graves", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamd15',
                text="15 Hypocondrie",
                options=[
                    AnswerOption(value='a', label="Absente", score=0),
                    AnswerOption(value='b', label="Attention concentrée sur son propre corps", score=1),
                    AnswerOption(value='c', label="Préoccupations sur sa santé", score=2),
                    AnswerOption(value='d', label="Plaintes fréquentes, demandes d'aide, etc", score=3),
                    AnswerOption(value='e', label="Idées délirantes hypocondriaques", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamd17',
                text="17 Prise de conscience",
                options=[
                    AnswerOption(value='a', label="Reconnaît qu'il est déprimé et malade", score=0),
                    AnswerOption(value='b', label="Reconnaît qu'il est malade, mais l'attribue à la nourriture, au climat, au surmenage, à un virus, à un besoin", score=1),
                    AnswerOption(value='c', label="Nie qu'il est malade", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamd18a',
                text="18 Variations dans la journée : A. Noter si les symptômes sont plus marqués dans la matinée ou la soirée. S'il N'Y A PAS de variations  diurnes, indiquer : aucune.\n                    ",
                options=[
                    AnswerOption(value='a', label="Aucune", score=0),
                    AnswerOption(value='b', label="Plus marqués le matin", score=1),
                    AnswerOption(value='c', label="Plus marqués l'après-midi", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamd18b',
                text="\n                      18 Variations dans la journée\n                      B. Quand il y a variation diurne, indiquer la sévérité de la variation. Indiquer 'Aucune' s'il n'y a pas de\n                      variation\n                    ",
                options=[
                    AnswerOption(value='a', label="Aucune", score=0),
                    AnswerOption(value='b', label="Légère", score=1),
                    AnswerOption(value='c', label="Importante", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamd2',
                text="2 Sentiments de culpabilité",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="S'adresse des reproches à lui-même, a l'impression qu'il a causé un préjudice à des gens", score=1),
                    AnswerOption(value='c', label="Idées de culpabilité ou ruminations sur des erreurs passées ou sur des actions condamnables", score=2),
                    AnswerOption(value='d', label="La maladie actuelle est une punition. Idées délirantes de culpabilité", score=3),
                    AnswerOption(value='e', label="Entend des voix qui l'accusent ou le dénoncent et/ou a des hallucinations visuelles menaçantes", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamd21',
                text="21 Symptômes obsessionnels et compulsionnels",
                options=[
                    AnswerOption(value='a', label="Absents", score=0),
                    AnswerOption(value='b', label="Légers", score=1),
                    AnswerOption(value='c', label="Graves", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamd3',
                text="3 Suicide",
                options=[
                    AnswerOption(value='a', label="Absent", score=0),
                    AnswerOption(value='b', label="A l'impression que la vie ne vaut pas la peine d'être vécue", score=1),
                    AnswerOption(value='c', label="Souhaite être mort ou équivalent : toute pensée de mort possible dirigée contre lui-même", score=2),
                    AnswerOption(value='d', label="Idées ou geste de suicide", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamd4',
                text="4 Insomnie du début de la nuit",
                options=[
                    AnswerOption(value='a', label="Pas de difficulté à s'endormir", score=0),
                    AnswerOption(value='b', label="Se plaint de difficultés éventuelles à s'endormir ; par ex. de mettre plus d'une demi-heure", score=1),
                    AnswerOption(value='c', label="Se plaint d'avoir chaque soir des difficultés à s'endormir", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamd5',
                text="5 Insomnie du milieu de la nuit",
                options=[
                    AnswerOption(value='a', label="Pas de difficulté", score=0),
                    AnswerOption(value='b', label="Le malade se plaint d'être agité et troublé pendant la nuit", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamd6',
                text="6 Insomnie du matin",
                options=[
                    AnswerOption(value='a', label="Pas de difficulté", score=0),
                    AnswerOption(value='b', label="Se réveille de très bonne heure le matin mais se rendort", score=1),
                    AnswerOption(value='c', label="Incapable de se rendormir s'il se lève", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamd7',
                text="7 Travail et activités",
                options=[
                    AnswerOption(value='a', label="Pas de difficulté", score=0),
                    AnswerOption(value='b', label="Pensées et sentiments d'incapacité, fatigue ou faiblesse se rapportant à des activités professionnelles ou", score=1),
                    AnswerOption(value='c', label="Perte d'intérêt pour les activités professionnelles ou de détente - ou bien décrite directement par le", score=2),
                    AnswerOption(value='d', label="Diminution du temps d'activité ou diminution de la productivité. A l'hôpital : coter 3 si le malade ne passe", score=3),
                    AnswerOption(value='e', label="A arrêté son travail en raison de sa maladie actuelle. A l'hôpital, coter 4 si le malade n'a aucune autre", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamd8',
                text="8 Ralentissement",
                options=[
                    AnswerOption(value='a', label="Langage et pensée normaux", score=0),
                    AnswerOption(value='b', label="Léger ralentissement à l'entretien", score=1),
                    AnswerOption(value='c', label="Ralentissement manifeste à l'entretien", score=2),
                    AnswerOption(value='d', label="Entretien difficile", score=3),
                    AnswerOption(value='e', label="Stupeur", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hamd9',
                text="9 Agitation",
                options=[
                    AnswerOption(value='a', label="Aucune", score=0),
                    AnswerOption(value='b', label="Crispations, secousses musculaires", score=1),
                    AnswerOption(value='c', label="Joue avec ses mains, ses cheveux, etc", score=2),
                    AnswerOption(value='d', label="Bouge, ne peut rester assis tranquille", score=3),
                    AnswerOption(value='e', label="Se tord les mains, ronge ses ongles, arrache ses cheveux, se mord les lèvres", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_HAM_DEPRES",
            name="AUT_HAM_DEPRES Questionnaire",
            description="18 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=9,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_HAM_DEPRES score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
