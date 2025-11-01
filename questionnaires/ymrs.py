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
from ..core.scoring import SimpleSumStrategy
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
                text="1. Elévation de l’humeur",
                options=[
                    AnswerOption(value='a', label="0. Absente", score=0),
                    AnswerOption(value='b', label="1. Légèrement ou possiblement élevée lorsqu’on l’interroge", score=1),
                    AnswerOption(value='c', label="2. Elévation subjective nette ; optimiste, plein d’assurance ; gai ; contenu approprié", score=2),
                    AnswerOption(value='d', label="3. Elevée, au contenu approprié, plaisantin", score=3),
                    AnswerOption(value='e', label="4. Euphorique ; rires inappropriés ; chante", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs10',
                text="10. Apparence",
                options=[
                    AnswerOption(value='a', label="0. Soignée et habillement adéquat", score=0),
                    AnswerOption(value='b', label="1. Légèrement ou possiblement élevée lorsqu’on l’interroge", score=1),
                    AnswerOption(value='c', label="2. Peu soigné ; modérément débraillé ; trop habillé", score=2),
                    AnswerOption(value='d', label="3. Débraillé ; à moitié nu ; maquillage criard", score=3),
                    AnswerOption(value='e', label="4. Complètement négligé ; orné ; accoutrement bizarre", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs11',
                text="11. Introspection",
                options=[
                    AnswerOption(value='a', label="0. Présente ; admet être malade ; reconnaît le besoin de traitement", score=0),
                    AnswerOption(value='b', label="1. Eventuellement malade", score=1),
                    AnswerOption(value='c', label="2. Admet des changements de comportement, mais nie la maladie", score=2),
                    AnswerOption(value='d', label="3. Admet de possibles changements de comportement, mais nie la maladie", score=3),
                    AnswerOption(value='e', label="4. Nie tout changement de comportement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs2',
                text="2. Activité motrice et énergie augmentées",
                options=[
                    AnswerOption(value='a', label="0. Absentes", score=0),
                    AnswerOption(value='b', label="1. Subjectivement élevées", score=1),
                    AnswerOption(value='c', label="2. Animé ; expression gestuelle plus élevée", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs3',
                text="3. Intérêt sexuel",
                options=[
                    AnswerOption(value='a', label="0. Normal, non augmenté", score=0),
                    AnswerOption(value='b', label="1. Augmentation légère ou possible", score=1),
                    AnswerOption(value='c', label="2. Clairement augmenté lorsqu’on l’interroge", score=2),
                    AnswerOption(value='d', label="3. Parle spontanément de la sexualité ; élabore sur des thèmes sexuels ; se décrit comme étant hyper sexuel", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs4',
                text="4. Sommeil",
                options=[
                    AnswerOption(value='a', label="0. Ne rapporte pas de diminution de sommeil", score=0),
                    AnswerOption(value='b', label="1. Dort jusqu’à une heure de moins que d’habitude", score=1),
                    AnswerOption(value='c', label="2. Sommeil réduit de plus d’une heure par rapport à d’habitude", score=2),
                    AnswerOption(value='d', label="3. Rapporte un moins grand besoin de sommeil", score=3),
                    AnswerOption(value='e', label="4. Nie le besoin de sommeil", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs5',
                text="5. Irritabilité",
                options=[
                    AnswerOption(value='a', label="0. Absente", score=0),
                    AnswerOption(value='b', label="2. Subjectivement augmentée", score=1),
                    AnswerOption(value='c', label="4. Irritable par moment durant l’entretien ; épisodes récents d’énervement ou de colère dans le service", score=2),
                    AnswerOption(value='d', label="6. Fréquemment irritable durant l’entretien ; brusque ; abrupt", score=3),
                    AnswerOption(value='e', label="8. Hostile, non coopératif ; évaluation impossible", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs7',
                text="7. Langage - troubles de la pensée",
                options=[
                    AnswerOption(value='a', label="0. Absent", score=0),
                    AnswerOption(value='b', label="1. Circonstanciel ; légère distractivité ; pensées rapides", score=1),
                    AnswerOption(value='c', label="2. Distractivité ; perd le fil de ses idées ; change fréquemment de sujet ; pensées accélérées", score=2),
                    AnswerOption(value='d', label="3. Fuite des idées ; réponses hors sujet ; difficile à suivre ; fait des rimes ; écholalie", score=3),
                    AnswerOption(value='e', label="4. Incohérent ; communication impossible", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs8',
                text="8. Contenu",
                options=[
                    AnswerOption(value='a', label="0. Normal", score=0),
                    AnswerOption(value='b', label="2. Projets discutables ; intérêts nouveaux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ymrs9',
                text="9. Comportement agressif et perturbateur",
                options=[
                    AnswerOption(value='a', label="0. Absent, coopératif", score=0),
                    AnswerOption(value='b', label="2. Sarcastique ; parle fort par moment, sur la défensive", score=1),
                    AnswerOption(value='c', label="4. Exigeant ; fait des menaces dans le service", score=2),
                    AnswerOption(value='d', label="6. Menace l’évaluateur ; crie ; évaluation difficile", score=3),
                    AnswerOption(value='e', label="8. Agressif physiquement ; destructeur ; évaluation impossible", score=4)
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
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute YMRS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
