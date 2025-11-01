"""
YMRS - YMRS Questionnaire
=========================

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
from ..core.scoring import WeightedSumStrategy
from ..core.registry import register_questionnaire


@register_questionnaire("YMRS")
@dataclass
class Ymrs(BaseQuestionnaire):
    """YMRS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize YMRS questionnaire with all 10 items."""
        
        questions_list = [
            Question(
                id='ymrs1',
                text="1. Élévation de l’humeur",
                options=[
                    AnswerOption(value='0', label="0. Absente", score=0),
                    AnswerOption(value='1', label="1. Légèrement ou possiblement élevée lorsqu’on l’interroge", score=1),
                    AnswerOption(value='2', label="2. Élévation subjective nette ; optimiste, confiant, enjoué", score=2),
                    AnswerOption(value='3', label="3. Humeur élevée ; plaisanteries excessives", score=3),
                    AnswerOption(value='4', label="4. Euphorique ; rires ou chants inappropriés", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs2',
                text="2. Activité motrice / énergie",
                options=[
                    AnswerOption(value='0', label="0. Activité normale", score=0),
                    AnswerOption(value='1', label="1. Activité ou énergie légèrement augmentée", score=1),
                    AnswerOption(value='2', label="2. Agitation modérée ; gestuelle accrue", score=2),
                    AnswerOption(value='3', label="3. Agitation marquée ; difficultés à rester assis", score=3),
                    AnswerOption(value='4', label="4. Agitation extrême nécessitant une surveillance", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs3',
                text="3. Intérêt sexuel",
                options=[
                    AnswerOption(value='0', label="0. Normal", score=0),
                    AnswerOption(value='1', label="1. Légère augmentation ou possible", score=1),
                    AnswerOption(value='2', label="2. Augmentation nette lorsqu’on l’interroge", score=2),
                    AnswerOption(value='3', label="3. Aborde spontanément des thèmes sexuels ; se décrit comme hypersexuel", score=3),
                    AnswerOption(value='4', label="4. Comportement sexuel inapproprié", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs4',
                text="4. Sommeil",
                options=[
                    AnswerOption(value='0', label="0. Sommeil habituel", score=0),
                    AnswerOption(value='1', label="1. Perte inférieure ou égale à une heure", score=1),
                    AnswerOption(value='2', label="2. Réduction supérieure à une heure", score=2),
                    AnswerOption(value='3', label="3. Dormir trois heures ou moins", score=3),
                    AnswerOption(value='4', label="4. Nie le besoin de dormir", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs5',
                text="5. Irritabilité",
                options=[
                    AnswerOption(value='0', label="0. Absente", score=0),
                    AnswerOption(value='1', label="1. Légère ; subjectivement augmentée", score=1),
                    AnswerOption(value='2', label="2. Irritable par moments durant l’entretien", score=2),
                    AnswerOption(value='3', label="3. Fréquemment irritable ; brusque", score=3),
                    AnswerOption(value='4', label="4. Hostile ; évaluation difficile ou impossible", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs6',
                text="6. Débit et quantité du langage",
                options=[
                    AnswerOption(value='0', label="0. Normal", score=0),
                    AnswerOption(value='1', label="1. Pression légère ou possible", score=1),
                    AnswerOption(value='2', label="2. Pression modérée ; interrompre devient difficile", score=2),
                    AnswerOption(value='3', label="3. Doit être interrompu ; conversation difficile", score=3),
                    AnswerOption(value='4', label="4. Logorrhée incoercible ou incohérente", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs7',
                text="7. Troubles de la pensée / langage",
                options=[
                    AnswerOption(value='0', label="0. Aucun", score=0),
                    AnswerOption(value='1', label="1. Circonstanciel ; légère distractibilité", score=1),
                    AnswerOption(value='2', label="2. Perd le fil ; changements fréquents de sujet", score=2),
                    AnswerOption(value='3', label="3. Fuite des idées ; réponses hors sujet", score=3),
                    AnswerOption(value='4', label="4. Incohérence ; communication impossible", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs8',
                text="8. Contenu de la pensée",
                options=[
                    AnswerOption(value='0', label="0. Normal", score=0),
                    AnswerOption(value='1', label="1. Projets discutables ; nouveaux centres d’intérêt", score=1),
                    AnswerOption(value='2', label="2. Idées grandioses modérées", score=2),
                    AnswerOption(value='3', label="3. Délires expansifs marqués", score=3),
                    AnswerOption(value='4', label="4. Délires grandioses extrêmes ou dangereux", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs9',
                text="9. Comportement perturbateur / agressivité",
                options=[
                    AnswerOption(value='0', label="0. Coopératif", score=0),
                    AnswerOption(value='1', label="1. Sarcastique ou bruyant par moments", score=1),
                    AnswerOption(value='2', label="2. Exigeant ; menaces verbales", score=2),
                    AnswerOption(value='3', label="3. Menace l’évaluateur ; criant", score=3),
                    AnswerOption(value='4', label="4. Agressivité physique ou destructrice", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs10',
                text="10. Apparence",
                options=[
                    AnswerOption(value='0', label="0. Soigné ; habillement approprié", score=0),
                    AnswerOption(value='1', label="1. Légèrement négligé ou flamboyant", score=1),
                    AnswerOption(value='2', label="2. Modérément négligé ou extravagant", score=2),
                    AnswerOption(value='3', label="3. Très négligé ; accoutrement bizarre", score=3),
                    AnswerOption(value='4', label="4. Complètement négligé ou choquant", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs11',
                text="11. Introspection",
                options=[
                    AnswerOption(value='0', label="0. Reconnaît être malade ; accepte le traitement", score=0),
                    AnswerOption(value='1', label="1. Possible maladie", score=1),
                    AnswerOption(value='2', label="2. Admet des changements de comportement mais nie la maladie", score=2),
                    AnswerOption(value='3', label="3. Admet de possibles changements mais nie la maladie", score=3),
                    AnswerOption(value='4', label="4. Nie tout changement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="YMRS",
            name="YMRS Questionnaire",
            description="10 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.CLINICIAN_RATED,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = WeightedSumStrategy({
            'ymrs5': 2.0,
            'ymrs6': 2.0,
            'ymrs8': 2.0,
            'ymrs9': 2.0
        })
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute YMRS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
