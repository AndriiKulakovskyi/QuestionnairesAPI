"""
AUT_TAS - AUT_TAS Questionnaire
===============================

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


@register_questionnaire("AUT_TAS")
@dataclass
class AutTas(BaseQuestionnaire):
    """AUT_TAS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_TAS questionnaire with all 18 items."""
        
        questions_list = [
            Question(
                id='tas1',
                text="1.Souvent. je ne vois pas très clair dans mes sentiments",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tas10',
                text="10.Être conscient de ses émotions est essentiel",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tas11',
                text="11.Je trouve difficile de décrire mes sentiments sur les gens",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tas12',
                text="12.On me dit de décrire davantage ce que je ressens",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tas13',
                text="13.Je ne sais pas ce qui se passe à l'intérieur de moi",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tas14',
                text="14.Bien souvent, je ne sais pas pourquoi je suis en colère.",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tas15',
                text="15.Je préfère parler aux gens de leurs activités quotidiennes plutôt que de leurs sentiments",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tas16',
                text="16.Je préfère regarder des émissions de variété plutôt que des films dramatiques",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tas17',
                text="17.Il m’est difficile de révéler mes sentiments intimes même à mes amis très proches",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tas18',
                text="18.Je peux me sentir proche de quelqu'un même pendant les moments de silence",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tas19',
                text="19.Je trouve utile d’analyser mes sentiments pour résoudre mes problèmes personnels",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tas2',
                text="2.J’ai du mal à trouver les mots qui correspondent bien à mes sentiments",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tas20',
                text="20.Rechercher le sens caché des films ou des pièces de théâtre perturbe le plaisir qu'ils procurent",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tas3',
                text="3.J'éprouve des sensations physiques que les médecins eux-mêmes ne comprennent pas",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tas4',
                text="4.J'arrive facilement à décrire mes sentiments",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tas5',
                text="5.Je préfère analyser les problèmes plutôt que de me contenter de les décrire",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tas8',
                text="8.Je préfère simplement laisser les choses se produire plutôt que de comprendre pourquoi e1les ont pris ce tour",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tas9',
                text="9.J'ai des sentiments que je ne suis guère capable d'identifier",
                options=[
                    AnswerOption(value='a', label="désaccord complet", score=0),
                    AnswerOption(value='b', label="désaccord relatif", score=1),
                    AnswerOption(value='c', label="ni accord ni désaccord", score=2),
                    AnswerOption(value='d', label="accord relatif", score=3),
                    AnswerOption(value='e', label="accord complet", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_TAS",
            name="AUT_TAS Questionnaire",
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
        """Compute AUT_TAS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
