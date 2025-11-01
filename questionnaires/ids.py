"""
IDS - IDS Questionnaire
=======================

16 items questionnaire

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


@register_questionnaire("IDS")
@dataclass
class Ids(BaseQuestionnaire):
    """IDS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize IDS questionnaire with all 16 items."""
        
        questions_list = [
            Question(
                id='radhtml_qids_1',
                text="1. Endormissement",
                options=[
                    AnswerOption(value='a', label="Je ne mets jamais plus de 30 minutes à m’endormir", score=0),
                    AnswerOption(value='b', label="Moins d'une fois sur deux, je mets au moins 30 minutes à m’endormir", score=1),
                    AnswerOption(value='c', label="Plus d'une fois sur deux, je mets au moins 30 minutes à m’endormir", score=2),
                    AnswerOption(value='d', label="Plus d'une fois sur deux, je mets plus d’une heure à m’endormir", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_qids_10',
                text="10. Concentration/Prise de décisions",
                options=[
                    AnswerOption(value='a', label="Il n’y a aucun changement dans ma capacité habituelle à me concentrer ou à prendre des décisions", score=0),
                    AnswerOption(value='b', label="Je me sens parfois indécis(e) ou je trouve parfois que ma concentration est limitée", score=1),
                    AnswerOption(value='c', label="La plupart du temps, j'ai du mal à me concentrer ou à prendre des décisions", score=2),
                    AnswerOption(value='d', label="Je n’arrive pas me concentrer assez pour lire ou je n’arrive pas à prendre des décisions même si elles sont insignifiantes", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_qids_11',
                text="11. Opinion de moi-même",
                options=[
                    AnswerOption(value='a', label="Je considère que j'ai autant de valeur que les autres et que je suis aussi méritant(e) que les autres", score=0),
                    AnswerOption(value='b', label="Je me critique plus que d’habitude", score=1),
                    AnswerOption(value='c', label="Je crois fortement que je cause des problèmes aux autres", score=2),
                    AnswerOption(value='d', label="Je pense presque tout le temps à mes petits et mes gros défauts", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_qids_12',
                text="12. Idées de mort ou de suicide",
                options=[
                    AnswerOption(value='a', label="Je ne pense pas au suicide ni à la mort", score=0),
                    AnswerOption(value='b', label="Je pense que la vie est sans intérêt ou je me demande si elle vaut la peine d'être vécue", score=1),
                    AnswerOption(value='c', label="Je pense au suicide ou à la mort plusieurs fois par semaine pendant plusieurs minutes", score=2),
                    AnswerOption(value='d', label="Je pense au suicide ou à la mort plusieurs fois par jours en détail, j’ai envisagé le suicide de manière précise ou j’ai réellement tenté de mettre fin à mes jours", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_qids_13',
                text="13. Enthousiasme général",
                options=[
                    AnswerOption(value='a', label="Il n’y pas de changement par rapport à d’habitude dans la manière dont je m’intéresse aux gens ou à mes activités", score=0),
                    AnswerOption(value='b', label="Je me rends compte que je m’intéresse moins aux gens et à mes activités", score=1),
                    AnswerOption(value='c', label="Je me rends compte que je n’ai d’intérêt que pour une ou deux des activités que j'avais auparavant", score=2),
                    AnswerOption(value='d', label="Je n’ai pratiquement plus d'intérêt pour les activités que j'avais auparavant", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_qids_14',
                text="14. Énergie",
                options=[
                    AnswerOption(value='a', label="J'ai autant d'énergie que d'habitude", score=0),
                    AnswerOption(value='b', label="Je me fatigue plus facilement que d’habitude", score=1),
                    AnswerOption(value='c', label="Je dois faire un gros effort pour commencer ou terminer mes activités quotidiennes (par exemple, faire les courses, les devoirs, la cuisine ou aller au travail)", score=2),
                    AnswerOption(value='d', label="Je ne peux vraiment pas faire mes activités quotidiennes parce que je n’ai simplement plus d’énergie", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_qids_15',
                text="15. Impression de ralentissement",
                options=[
                    AnswerOption(value='a', label="Je pense, je parle et je bouge aussi vite que d’habitude", score=0),
                    AnswerOption(value='b', label="Je trouve que je réfléchis plus lentement ou que ma voix est étouffée ou monocorde", score=1),
                    AnswerOption(value='c', label="Il me faut plusieurs secondes pour répondre à la plupart des questions et je suis sûr(e) que je réfléchis plus lentement", score=2),
                    AnswerOption(value='d', label="Je suis souvent incapable de répondre aux questions si je ne fais pas de gros efforts", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_qids_16',
                text="16. Impression d'agitation",
                options=[
                    AnswerOption(value='a', label="Je ne me sens pas agité(e)", score=0),
                    AnswerOption(value='b', label="Je suis souvent agité(e), je me tords les mains ou j’ai besoin de changer de position quand je suis assis(e)", score=1),
                    AnswerOption(value='c', label="J'éprouve le besoin soudain de bouger et je suis plutôt agité(e)", score=2),
                    AnswerOption(value='d', label="Par moments, je suis incapable de rester assis(e) et j’ai besoin de faire les cent pas", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_qids_2',
                text="2. Sommeil pendant la nuit",
                options=[
                    AnswerOption(value='a', label="Je ne me réveille pas la nuit", score=0),
                    AnswerOption(value='b', label="J’ai un sommeil agité, léger et quelques réveils brefs chaque nuit", score=1),
                    AnswerOption(value='c', label="Je me réveille au moins une fois par nuit, mais je me rendors facilement", score=2),
                    AnswerOption(value='d', label="Plus d'une fois sur deux, je me réveille plus d’une fois par nuit et reste éveillé(e) 20 minutes ou plus", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_qids_3',
                text="3. Réveil avant l'heure prévue",
                options=[
                    AnswerOption(value='a', label="La plupart du temps, je me réveille 30 minutes ou moins avant le moment où je dois me lever", score=0),
                    AnswerOption(value='b', label="Plus d'une fois sur deux, je me réveille plus de 30 minutes avant le moment où je dois me lever", score=1),
                    AnswerOption(value='c', label="Je me réveille presque toujours une heure ou plus avant le moment où je dois me lever, mais je finis par me rendormir", score=2),
                    AnswerOption(value='d', label="Je me réveille au moins une heure avant le moment où je dois me lever et je n’arrive pas à me rendormir", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_qids_4',
                text="4. Sommeil excessif",
                options=[
                    AnswerOption(value='a', label="Je ne dors pas plus de 7 à 8 heures par nuit, et je ne fais pas de sieste dans la journée", score=0),
                    AnswerOption(value='b', label="Je ne dors pas plus de 10 heures sur un jour entier de 24 heures, siestes comprises", score=1),
                    AnswerOption(value='c', label="Je ne dors pas plus de 12 heures sur un jour entier de 24 heures, siestes comprises", score=2),
                    AnswerOption(value='d', label="Je dors plus de 12 heures sur un jour entier de 24 heures, siestes comprises", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_qids_5',
                text="5. Tristesse",
                options=[
                    AnswerOption(value='a', label="Je ne me sens pas triste", score=0),
                    AnswerOption(value='b', label="Je me sens triste moins de la moitié du temps", score=1),
                    AnswerOption(value='c', label="Je me sens triste plus de la moitié du temps", score=2),
                    AnswerOption(value='d', label="Je me sens triste presque tout le temps", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_qids_6',
                text="6. Diminution de l’appétit",
                options=[
                    AnswerOption(value='a', label="J’ai le même appétit que d’habitude", score=0),
                    AnswerOption(value='b', label="Je mange un peu moins souvent ou en plus petite quantité que d’habitude", score=1),
                    AnswerOption(value='c', label="Je mange beaucoup moins que d’habitude et seulement en me forçant", score=2),
                    AnswerOption(value='d', label="Je mange rarement sur un jour entier de 24 heures et seulement en me forçant énormément ou quand on me persuade de manger", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_qids_7',
                text="7. Augmentation de l'appétit",
                options=[
                    AnswerOption(value='a', label="J’ai le même appétit que d’habitude", score=0),
                    AnswerOption(value='b', label="J'éprouve le besoin de manger plus souvent que d’habitude", score=1),
                    AnswerOption(value='c', label="Je mange régulièrement plus souvent et/ou en plus grosse quantité que d’habitude", score=2),
                    AnswerOption(value='d', label="J'éprouve un grand besoin de manger plus que d'habitude pendant et entre les repas", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_qids_8',
                text="8. Perte de poids (au cours des 15 derniers jours)",
                options=[
                    AnswerOption(value='a', label="Mon poids n’a pas changé", score=0),
                    AnswerOption(value='b', label="J’ai l’impression d’avoir perdu un peu de poids", score=1),
                    AnswerOption(value='c', label="J’ai perdu 1 kg ou plus", score=2),
                    AnswerOption(value='d', label="J’ai perdu plus de 2 kg", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_qids_9',
                text="9. Prise de poids (au cours des 15 derniers jours)",
                options=[
                    AnswerOption(value='a', label="Mon poids n’a pas changé", score=0),
                    AnswerOption(value='b', label="J’ai l’impression d’avoir pris un peu de poids", score=1),
                    AnswerOption(value='c', label="J’ai pris 1 kg ou plus", score=2),
                    AnswerOption(value='d', label="J’ai pris plus de 2 kg", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="IDS",
            name="IDS Questionnaire",
            description="16 items questionnaire",
            pathology_domain=PathologyDomain.SCHIZOPHRENIA,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=8,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute IDS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
