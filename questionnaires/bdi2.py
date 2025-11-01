"""
BDI2 - BDI2 Questionnaire
=========================

16 items questionnaire

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


@register_questionnaire("BDI2")
@dataclass
class Bdi2(BaseQuestionnaire):
    """BDI2 Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize BDI2 questionnaire with all 16 items."""
        
        questions_list = [
            Question(
                id='bdi0201',
                text="1. Tristesse",
                options=[
                    AnswerOption(value='a', label="Je ne me sens pas triste", score=0),
                    AnswerOption(value='b', label="Je me sens très souvent triste", score=1),
                    AnswerOption(value='c', label="Je suis tout le temps triste", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bdi0204',
                text="4. Perte de plaisir",
                options=[
                    AnswerOption(value='a', label="J'éprouve toujours autant de plaisir qu'avant aux choses qui me plaisent", score=0),
                    AnswerOption(value='b', label="Je n'éprouve pas autant de plaisir aux choses qu'avant", score=1),
                    AnswerOption(value='c', label="J'éprouve très peu de plaisir aux choses qui me plaisaient habituellement", score=2),
                    AnswerOption(value='d', label="Je n'éprouve aucun plaisir aux choses qui me plaisaient habituellement", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bdi0205',
                text="5. Sentiment de culpabilité",
                options=[
                    AnswerOption(value='a', label="Je ne me sens pas particulièrement coupable", score=0),
                    AnswerOption(value='b', label="Je me sens coupable pour bien des choses que j'ai faites ou que j'aurais dû faire", score=1),
                    AnswerOption(value='c', label="Je me sens coupable la plupart du temps", score=2),
                    AnswerOption(value='d', label="Je me sens tout le temps coupable", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bdi0207',
                text="7. Sentiments négatifs envers soi-même",
                options=[
                    AnswerOption(value='a', label="Mes sentiments envers moi-même n'ont pas changé", score=0),
                    AnswerOption(value='b', label="J'ai perdu confiance en moi", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bdi0208',
                text="8. Attitude critique envers soi",
                options=[
                    AnswerOption(value='a', label="Je ne me blâme pas ou ne me critique pas plus que d'habitude", score=0),
                    AnswerOption(value='b', label="Je suis plus critique envers moi-même que d'habitude", score=1),
                    AnswerOption(value='c', label="Je me reproche tous mes défauts", score=2),
                    AnswerOption(value='d', label=" Je me reproche tous les malheurs qui arrivent", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bdi0209',
                text="9. Pensées ou désirs de suicide",
                options=[
                    AnswerOption(value='a', label=" Je ne pense pas du tout à me suicider", score=0),
                    AnswerOption(value='b', label="Il m'arrive de penser à me suicider, mais je ne le ferai pas", score=1),
                    AnswerOption(value='c', label="J'aimerais me suicider", score=2),
                    AnswerOption(value='d', label="Je me suiciderais si l'occasion se présentait", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bdi0210',
                text="10. Pleurs",
                options=[
                    AnswerOption(value='a', label="Je ne pleure pas plus qu'avant", score=0),
                    AnswerOption(value='b', label="Je pleure plus qu'avant", score=1),
                    AnswerOption(value='c', label="Je pleure pour la moindre petite chose", score=2),
                    AnswerOption(value='d', label="Je voudrais pleurer mais je n'en suis pas capable", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bdi0212',
                text="12. Perte d'intérêt",
                options=[
                    AnswerOption(value='a', label="Je n'ai pas perdu d'intérêt pour les gens ou pour les activités", score=0),
                    AnswerOption(value='b', label="Je m'intéresse moins qu'avant aux gens et aux choses", score=1),
                    AnswerOption(value='c', label="Je ne m'intéresse presque plus aux gens et aux choses", score=2),
                    AnswerOption(value='d', label="J'ai du mal à m'intéresser à quoi que ce soit", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bdi0213',
                text="13. Indécision",
                options=[
                    AnswerOption(value='a', label="Je prends des décisions toujours aussi bien qu'avant", score=0),
                    AnswerOption(value='b', label="Il m'est plus difficile que d'habitude de prendre des décisions", score=1),
                    AnswerOption(value='c', label="J'ai beaucoup plus de mal qu'avant à prendre des décisions", score=2),
                    AnswerOption(value='d', label="J'ai du mal à prendre n'importe quelle décision", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bdi0214',
                text="14. Dévalorisation",
                options=[
                    AnswerOption(value='a', label="Je pense être quelqu'un de valable", score=0),
                    AnswerOption(value='b', label="Je ne crois pas avoir autant de valeur ni être aussi utile qu'avant", score=1),
                    AnswerOption(value='c', label="Je me sens moins valable que les autres", score=2),
                    AnswerOption(value='d', label="Je sens que je ne vaux absolument rien", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bdi0215',
                text="15. Perte d'énergie",
                options=[
                    AnswerOption(value='a', label="J'ai toujours autant d'énergie qu'avant", score=0),
                    AnswerOption(value='b', label="J'ai moins d'énergie qu'avant", score=1),
                    AnswerOption(value='c', label="Je n'ai pas assez d'énergie pour pouvoir faire grand chose", score=2),
                    AnswerOption(value='d', label="J'ai trop peu d'énergie pour faire quoi que ce soit", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bdi0216',
                text="16.  Modifications dans les habitudes de sommeil",
                options=[
                    AnswerOption(value='a', label="Mes habitudes de sommeil n'ont pas changé", score=0),
                    AnswerOption(value='b', label="Je dors un peu plus que d'habitude", score=1),
                    AnswerOption(value='c', label="Je dors un peu moins que d'habitude", score=2),
                    AnswerOption(value='d', label="Je dors beaucoup plus que d'habitude", score=3),
                    AnswerOption(value='e', label="Je dors beaucoup moins que d'habitude", score=4),
                    AnswerOption(value='f', label="Je dors presque toute la journée", score=5),
                    AnswerOption(value='g', label="Je me réveille une ou deux heures plus tôt et je suis incapable de ma rendormir", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bdi0217',
                text="17. Irritabilité",
                options=[
                    AnswerOption(value='a', label="Je ne suis pas plus irritable que d'habitude", score=0),
                    AnswerOption(value='b', label="Je suis plus irritable que d'habitude", score=1),
                    AnswerOption(value='c', label="Je suis beaucoup plus irritable que d'habitude", score=2),
                    AnswerOption(value='d', label="Je suis constamment irritable", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bdi0218',
                text="18. Modifications de l'appétit",
                options=[
                    AnswerOption(value='a', label="Mon appétit n'a pas changé", score=0),
                    AnswerOption(value='b', label="J'ai un peu moins d'appétit que d'habitude", score=1),
                    AnswerOption(value='c', label="J'ai un peu plus d'appétit que d'habitude", score=2),
                    AnswerOption(value='d', label="J'ai beaucoup moins d'appétit que d'habitude", score=3),
                    AnswerOption(value='e', label="J'ai beaucoup plus d'appétit que d'habitude", score=4),
                    AnswerOption(value='f', label="Je n'ai pas d'appétit du tout", score=5),
                    AnswerOption(value='g', label="J'ai constamment envie de manger", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bdi0219',
                text="19. Difficulté à se concentrer",
                options=[
                    AnswerOption(value='a', label="Je parviens à me concentrer toujours aussi bien qu'avant", score=0),
                    AnswerOption(value='b', label="Je ne parviens à me concentrer aussi bien qu'avant", score=1),
                    AnswerOption(value='c', label="J'ai du mal à me concentrer longtemps sur quoi que ce soit", score=2),
                    AnswerOption(value='d', label="Je me trouve incapable de me contrer sur quoi que ce soit", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bdi0221',
                text="21. Perte d'intérêt pour le sexe",
                options=[
                    AnswerOption(value='a', label="Je n'ai pas noté de changement récent dans mon intérêt pour le sexe", score=0),
                    AnswerOption(value='b', label="Le sexe m'intéresse moins qu'avant", score=1),
                    AnswerOption(value='c', label="Le sexe m'intéresse beaucoup moins maintenant", score=2),
                    AnswerOption(value='d', label="J'ai perdu tout intérêt pour le sexe", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="BDI2",
            name="BDI2 Questionnaire",
            description="16 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=8,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute BDI2 score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
