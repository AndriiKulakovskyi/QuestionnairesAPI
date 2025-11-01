"""
QAE - QAE Questionnaire
=======================

20 items questionnaire

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


@register_questionnaire("QAE")
@dataclass
class Qae(BaseQuestionnaire):
    """QAE Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize QAE questionnaire with all 20 items."""
        
        questions_list = [
            Question(
                id='qae01',
                text="1- Souvent, je ne sais pas très bien ce que je ressens en moi ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae02',
                text="2- Je trouve que c'est difficile de dire ce que je ressens en moi ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae03',
                text="3- Je sens des choses dans mon corps que mêmes les médecins ne comprennent pas ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae04',
                text="4- J'arrive facilement à dire ce que je ressens en moi ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae05',
                text="5- Quand j'ai un problème, je veux savoir d'où il vient et pas seulement juste en parler",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae06',
                text="6- Quand je suis bouleversé(e), je ne sais pas si je suis triste, effrayé(e) ou en colère",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae07',
                text="7- Je suis souvent intrigué(e) par des choses que je ressens dans mon corps ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae08',
                text="8- Je préfère attendre et voir ce qui se passe, plutôt que de penser à pourquoi les choses arrivent",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae09',
                text="9- Quelque fois, je n'arrive pas à trouver les mots pour dire ce que je ressens en moi",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae10',
                text="10- C'est important de comprendre ce qu'on ressent en soi ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae11',
                text="11- Je trouve que c'est difficile de dire ce que je ressens pour les autres personnes ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae12',
                text="12- Les autres personnes me disent que je devrais plus parler de ce que je ressens en moi",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae13',
                text="13- Je ne sais pas ce qui se passe à l'intérieur de moi ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae14',
                text="14- Bien souvent, je ne sais pas pourquoi je suis en colère ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae15',
                text="15- Je préfère parler aux gens de leurs activités de tous les jours plutôt que de leurs sentiments ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae16',
                text="16- Je préfère regarder des émissions de télé amusantes plutôt que des films racontant les problèmes des gens ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae17',
                text="17- C'est dur pour moi de dire ce que je ressens vraiment en moi, même à mon/ma meilleur(e) ami(e) ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae18',
                text="18- Je peux me sentir proche de quelqu'un, même si on est assis sans bouger et sans rien dire ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae19',
                text="19- Quand je veux résoudre mes problèmes, ça m'aide de penser à ce que je ressens ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='qae20',
                text="20- J'aime moins un film si je dois me concentrer pour comprendre son histoire ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas vrai", score=0),
                    AnswerOption(value='b', label="C'est un peu vrai", score=1),
                    AnswerOption(value='c', label="C'est tout à fait vrai", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="QAE",
            name="QAE Questionnaire",
            description="20 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=10,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute QAE score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
