"""
QIDS - QIDS Questionnaire
=========================

13 items questionnaire

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


@register_questionnaire("QIDS")
@dataclass
class Qids(BaseQuestionnaire):
    """QIDS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize QIDS questionnaire with all 13 items."""
        
        questions_list = [
            Question(
                id='qids1',
                text="1. Endormissement :",
                options=[
                    AnswerOption(value='a', label="0 Je ne mets jamais plus de 30 minutes à m’endormir.", score=0),
                    AnswerOption(value='b', label="1 Moins d'une fois sur deux, je mets au moins 30 minutes à m’endormir.", score=1),
                    AnswerOption(value='c', label="2 Plus d'une fois sur deux, je mets au moins 30 minutes à m’endormir.", score=2),
                    AnswerOption(value='d', label="3 Plus d'une fois sur deux, je mets plus d’une heure à m’endormir.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qids10',
                text="10. Concentration/Prise de décisions :",
                options=[
                    AnswerOption(value='a', label="0 Il n’y a aucun changement dans ma capacité habituelle à me concentrer ou à prendre des décisions.", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qids12',
                text="12. Idées de mort ou de suicide :",
                options=[
                    AnswerOption(value='a', label="0 Je ne pense pas au suicide ni à la mort.", score=0),
                    AnswerOption(value='b', label="1 Je pense que la vie est sans intérêt ou je me demande si elle vaut la peine d'être vécue.", score=1),
                    AnswerOption(value='c', label="2 Je pense au suicide ou à la mort plusieurs fois par semaine pendant plusieurs minutes.", score=2),
                    AnswerOption(value='d', label="3 Je pense au suicide ou à la mort plusieurs fois par jours en détail, j’ai envisagé le suicide de manière précise ou j’ai réellement tenté de mettre fin à mes jours.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qids13',
                text="13. Enthousiasme général :",
                options=[
                    AnswerOption(value='a', label="0 Il n’y pas de changement par rapport à d’habitude dans la manière dont je m’intéresse aux gens ou à mes activités.", score=0),
                    AnswerOption(value='b', label="1 Je me rends compte que je m’intéresse moins aux gens et à mes activités.", score=1),
                    AnswerOption(value='c', label="2 Je me rends compte que je n’ai d’intérêt que pour une ou deux des activités que j'avais auparavant.", score=2),
                    AnswerOption(value='d', label="3 Je n’ai pratiquement plus d'intérêt pour les activités que j'avais auparavant.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qids14',
                text="14. Énergie :",
                options=[
                    AnswerOption(value='a', label="0 J'ai autant d'énergie que d'habitude.", score=0),
                    AnswerOption(value='b', label="1 Je me fatigue plus facilement que d’habitude.", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qids15',
                text="15. Impression de ralentissement :",
                options=[
                    AnswerOption(value='a', label="0 Je pense, je parle et je bouge aussi vite que d’habitude.", score=0),
                    AnswerOption(value='b', label="1 Je trouve que je réfléchis plus lentement ou que ma voix est étouffée ou monocorde.", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qids2',
                text="2. Sommeil pendant la nuit :",
                options=[
                    AnswerOption(value='a', label="0 Je ne me réveille pas la nuit.", score=0),
                    AnswerOption(value='b', label="1 J’ai un sommeil agité, léger et quelques réveils brefs chaque nuit.", score=1),
                    AnswerOption(value='c', label="2 Je me réveille au moins une fois par nuit, mais je me rendors facilement.", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qids3',
                text="3. Réveil avant l'heure prévue :",
                options=[
                    AnswerOption(value='a', label="0 La plupart du temps, je me réveille 30 minutes ou moins avant le moment où je dois me lever.", score=0),
                    AnswerOption(value='b', label="1 Plus d'une fois sur deux, je me réveille plus de 30 minutes avant le moment où je dois me lever.", score=1),
                    AnswerOption(value='c', label="2 Je me réveille presque toujours une heure ou plus avant le moment où je dois me lever, mais je finis par me rendormir.", score=2),
                    AnswerOption(value='d', label="3 Je me réveille au moins une heure avant le moment où je dois me lever et je n’arrive pas à me rendormir.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qids4',
                text="4. Sommeil excessif :",
                options=[
                    AnswerOption(value='a', label="0 Je ne dors pas plus de 7 à 8 heures par nuit, et je ne fais pas de sieste dans la journée.", score=0),
                    AnswerOption(value='b', label="1 Je ne dors pas plus de 10 heures sur un jour entier de 24 heures, siestes comprises.", score=1),
                    AnswerOption(value='c', label="2 Je ne dors pas plus de 12 heures sur un jour entier de 24 heures, siestes comprises.", score=2),
                    AnswerOption(value='d', label="3 Je dors plus de 12 heures sur un jour entier de 24 heures, siestes comprises.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qids5',
                text="5. Tristesse :",
                options=[
                    AnswerOption(value='a', label="0 Je ne me sens pas triste.", score=0),
                    AnswerOption(value='b', label="1 Je me sens triste moins de la moitié du temps.", score=1),
                    AnswerOption(value='c', label="2 Je me sens triste plus de la moitié du temps.", score=2),
                    AnswerOption(value='d', label="3 Je me sens triste presque tout le temps.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qids6',
                text="6. Diminution de l’appétit :",
                options=[
                    AnswerOption(value='a', label="0 J’ai le même appétit que d’habitude.", score=0),
                    AnswerOption(value='b', label="1 Je mange un peu moins souvent ou en plus petite quantité que d’habitude.", score=1),
                    AnswerOption(value='c', label="2 Je mange beaucoup moins que d’habitude et seulement en me forçant.", score=2),
                    AnswerOption(value='d', label="3 Je mange rarement sur un jour entier de 24 heures et seulement en me forçant énormément ou quand on me persuade de manger.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qids6a',
                text="6a. Appétit :",
                options=[
                    AnswerOption(value='a', label="Même appétit que d’habitude.", score=0),
                    AnswerOption(value='b', label="Plus d'appétit que d’habitude.", score=1),
                    AnswerOption(value='c', label="Moins d'appétit que d’habitude", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qids7',
                text="7. Augmentation de l'appétit :",
                options=[
                    AnswerOption(value='a', label="0 J’ai le même appétit que d’habitude.", score=0),
                    AnswerOption(value='b', label="1 J'éprouve le besoin de manger plus souvent que d’habitude.", score=1),
                    AnswerOption(value='c', label="2 Je mange régulièrement plus souvent et/ou en plus grosse quantité que d’habitude.", score=2),
                    AnswerOption(value='d', label="3 J'éprouve un grand besoin de manger plus que d'habitude pendant et entre les repas.", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="QIDS",
            name="QIDS Questionnaire",
            description="13 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=6,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute QIDS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
