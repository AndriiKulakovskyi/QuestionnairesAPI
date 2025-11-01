"""
CALGARY - CALGARY Questionnaire
===============================

9 items questionnaire

Source: Extracted from eschizo application
Applications: eschizo
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


@register_questionnaire("CALGARY")
@dataclass
class Calgary(BaseQuestionnaire):
    """CALGARY Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize CALGARY questionnaire with all 9 items."""
        
        questions_list = [
            Question(
                id='radhtml_calgary_autodepreciation',
                text="3. AUTO-DÉPRÉCIATION : Quelle est votre opinion de vous-même, en comparaison avec d'autres personnes? Est ce que vous vous sentez meilleur ou moins bon, ou à peu près comparable aux autres personnes en général ? Vous sentez-vous inférieur ou même sans aucune valeur?",
                options=[
                    AnswerOption(value='a', label="ABSENTE", score=0),
                    AnswerOption(value='b', label="LÉGÈRE : légère infériorité; n'atteint pas le degré de se sentir sans valeur.", score=1),
                    AnswerOption(value='c', label="MODÉRÉE : le sujet se sent sans valeur mais moins de 50 % du temps.", score=2),
                    AnswerOption(value='d', label="SÉVÈRE : le sujet se sent sans valeur plus de 50 % du temps. Il peut être mis au défi de reconnaître un autre point de vue.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_calgary_culpabpatho',
                text="5. CULPABILITÉ PATHOLOGIQUE : Avez-vous tendance à vous blâmer vous-même pour des petites choses que vous pourriez avoir faites dans le passé? Pensez-vous que vous méritez d'être aussi préoccupé de cela?",
                options=[
                    AnswerOption(value='a', label="ABSENTE", score=0),
                    AnswerOption(value='b', label="LÉGÈRE : le sujet se sent coupable de certaines peccadilles mais moins de 50 % du temps.", score=1),
                    AnswerOption(value='c', label="MODÉRÉE : le sujet se sent coupable habituellement (plus de 50 % du temps) à propos d'actes dont il exagère la signification.", score=2),
                    AnswerOption(value='d', label="SÉVÈRE : le sujet se sent habituellement qu'il est à blâmer pour tout ce qui va mal même lorsque ce n'est pas de sa faute.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_calgary_depobservee',
                text="9. DÉPRESSION OBSERVÉE : Basée sur les observations de l'interviewer durant l'entretien complet. La question \\\"est-ce que vous ressentez une envie de pleurer?\\\" utilisée à des moments appropriés durant l'entretien peut susciter l'émergence d'informations utiles à cette observation.",
                options=[
                    AnswerOption(value='a', label="ABSENTE", score=0),
                    AnswerOption(value='b', label="LÉGÈRE : le sujet apparaît triste et sur le point de pleurer même durant des parties de l'entretien touchant des sujets effectivement neutres.", score=1),
                    AnswerOption(value='c', label="MODÉRÉE : le sujet apparaît triste, près des larmes durant tout l'entretien avec une voix monotone et mélancolique, extériorise des larmes ou est près des larmes à certains moments", score=2),
                    AnswerOption(value='d', label="SÉVÈRE : le patient s'étrangle lorsqu'il évoque des sujets générant de la détresse, soupire profondément, fréquemment et pleure ouvertement, ou est de façon persistante dans un état de souffrance figée.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_calgary_depresmatin',
                text="6. DÉPRESSION MATINALE : Lorsque vous vous êtes senti déprimé au cours des deux dernières semaines, avez-vous remarqué que la dépression était pire à certains moments de la journée?",
                options=[
                    AnswerOption(value='a', label="ABSENTE", score=0),
                    AnswerOption(value='b', label="LÉGÈRE : dépression présente mais sans variation diurne", score=1),
                    AnswerOption(value='c', label="MODÉRÉE : le sujet mentionne spontanément que la dépression est pire le matin.", score=2),
                    AnswerOption(value='d', label="SÉVÈRE : la dépression est, de façon marquée, pure le matin, avec un fonctionnement perturbé qui s'améliore l'après midi.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_calgary_desespoir',
                text="2. DÉSESPOIR : Comment entrevoyez-vous le futur pour vous-même? Est ce que vous pouvez envisager un avenir pour vous? Ou est-ce que la vie vous paraît plutôt sans espoir? Est ce que vous avez tout laissé tomber ou est ce qu'il vous paraît y avoir encore des raisons d'essayer?",
                options=[
                    AnswerOption(value='a', label="ABSENT", score=0),
                    AnswerOption(value='b', label="LÉGER : à certains moments, le sujet s'est senti sans espoir au cours de la dernière semaine mais il a encore un certain degré d'espoir pour l'avenir.", score=1),
                    AnswerOption(value='c', label="MODÉRÉ : perception persistante mais modérée de désespoir au cours de la dernière semaine. On peut cependant persuader le sujet d'acquiescer à la possibilité que les choses peuvent s'améliorer", score=2),
                    AnswerOption(value='d', label="SÉVÈRE : sentiment persistant et éprouvant de désespoir.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_calgary_eveilhatif',
                text="7. ÉVEIL PRÉCOCE : Vous réveillez-vous plus tôt le matin qu'à l'accoutumée? Combien de fois par semaine cela vous arrive-t-il?",
                options=[
                    AnswerOption(value='a', label="ABSENT : pas de réveil précoce.", score=0),
                    AnswerOption(value='b', label="LÉGER : à l'occasion s'éveille (jusqu'à 2 fois par semaine) une heure ou plus avant le moment normal de s'éveiller ou l'heure fixée à son réveille-matin.", score=1),
                    AnswerOption(value='c', label="MODÉRÉ : s'éveille fréquemment de façon hâtive (jusqu'à 5 fois par semaine) une heure ou plus avant son heure habituelle d'éveil ou l'heure fixée par son réveille-matin", score=2),
                    AnswerOption(value='d', label="SÉVÈRE : s'éveille tous les jours une heure ou plus avant l'heure normale d'éveil", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_calgary_humdep',
                text="1. DÉPRESSION : Comment pourriez-vous décrire votre humeur durant les deux dernières semaines : avez-vous pu demeurer raisonnablement gai ou est ce que vous avez été très déprimé ou plutôt triste ces derniers temps ? Durant les deux dernières semaines, combien de fois vous êtes-vous senti ainsi, tous les jours? Toute la journée?",
                options=[
                    AnswerOption(value='a', label="ABSENTE", score=0),
                    AnswerOption(value='b', label="LÉGÈRE : le sujet exprime une certaine tristesse ou un certain découragement lorsqu'il est questionné", score=1),
                    AnswerOption(value='c', label="MODÉRÉE : humeur dépressive distinctive est présente tous les jours", score=2),
                    AnswerOption(value='d', label="SÉVÈRE : humeur dépressive marquée persistant tous les jours, plus de la moitié du temps, affectant le fonctionnement normal, psychomoteur et social", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_calgary_idrefculpabilite',
                text="4. IDÉES DE RÉFÉRENCE ASSOCIÉES A LA CULPABILITÉ : Avez-vous l'impression que l'on vous blâme pour certaines choses ou même qu'on vous accuse sans raison? A propos de quoi? (ne pas inclure ici des blâmes ou des accusations justifiés. Exclure les délires de culpabilité)",
                options=[
                    AnswerOption(value='a', label="ABSENTE", score=0),
                    AnswerOption(value='b', label="LÉGÈRE : le sujet se sent blâmé mais non accusé, moins de 50 % du temps.", score=1),
                    AnswerOption(value='c', label="MODÉRÉE : sentiment persistant d'être blâmé et/ou sentiment occasionnel d'être accusé.", score=2),
                    AnswerOption(value='d', label="SÉVÈRE : sentiment persistant d'être accusé. Lorsqu'on le contredit, le sujet reconnaît que cela n'est pas vrai.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_calgary_suicide',
                text="8. SUICIDE : Avez-vous déjà eu l'impression que la vie ne valait pas la peine d'être vécue? Avez-vous déjà pensé mettre fin à tout cela? Qu'est ce que vous pensez que vous auriez pu faire? Avez-vous effectivement essayé?",
                options=[
                    AnswerOption(value='a', label="ABSENT", score=0),
                    AnswerOption(value='b', label="LÉGER : le sujet a l'idée qu'il serait mieux mort ou des idées occupationnelles de suicide", score=1),
                    AnswerOption(value='c', label="MODÉRÉ : il a envisagé délibérément le suicide avec un projet mais sans faire de tentative", score=2),
                    AnswerOption(value='d', label="SÉVÈRE : tentative de suicide apparemment conçue pour se terminer par la mort (c'est-à-dire de découverte accidentelle ou par un moyen qui s'est avéré inefficace)", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="CALGARY",
            name="CALGARY Questionnaire",
            description="9 items questionnaire",
            pathology_domain=PathologyDomain.SCHIZOPHRENIA,
            respondent_type=RespondentType.CLINICIAN_RATED,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=5,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute CALGARY score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
