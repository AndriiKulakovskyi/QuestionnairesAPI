"""
CDI - CDI Questionnaire
=======================

27 items questionnaire

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


@register_questionnaire("CDI")
@dataclass
class Cdi(BaseQuestionnaire):
    """CDI Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize CDI questionnaire with all 27 items."""
        
        questions_list = [
            Question(
                id='cdi01',
                text="1.",
                options=[
                    AnswerOption(value='a', label=" Je suis triste de temps en temps", score=0),
                    AnswerOption(value='b', label="Je suis triste très souvent", score=1),
                    AnswerOption(value='c', label="Je suis triste tout le temps", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi02',
                text="2.",
                options=[
                    AnswerOption(value='a', label="Rien ne marchera jamais bien pour moi", score=0),
                    AnswerOption(value='b', label="Je ne suis pas sûr que tout marchera bien pour moi ", score=1),
                    AnswerOption(value='c', label="Tout marchera bien pour moi", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi03',
                text="3.",
                options=[
                    AnswerOption(value='a', label="Je réussis presque tout ce que je fais", score=0),
                    AnswerOption(value='b', label="Je rate beaucoup de choses ", score=1),
                    AnswerOption(value='c', label="Je rate tout ", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi04',
                text="4.",
                options=[
                    AnswerOption(value='a', label="Des tas de choses m'amusent", score=0),
                    AnswerOption(value='b', label="Peu de choses m'amusent", score=1),
                    AnswerOption(value='c', label="Rien ne m'amuse", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi05',
                text="5.",
                options=[
                    AnswerOption(value='a', label="Je suis désagréable tout le temps", score=0),
                    AnswerOption(value='b', label="Je suis souvent désagréable", score=1),
                    AnswerOption(value='c', label="Je suis désagréable de temps en temps", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi06',
                text="6.",
                options=[
                    AnswerOption(value='a', label="De temps en temps, je pense que des choses désagréables vont m'arriver", score=0),
                    AnswerOption(value='b', label="J'ai peur que des choses désagréables m'arrivent", score=1),
                    AnswerOption(value='c', label="Je suis sûr que des choses horribles vont m'arriver", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi07',
                text="7.",
                options=[
                    AnswerOption(value='a', label="Je me déteste", score=0),
                    AnswerOption(value='b', label="Je ne m'aime pas", score=1),
                    AnswerOption(value='c', label="Je m'aime bien", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi08',
                text="8.",
                options=[
                    AnswerOption(value='a', label="Tout ce qui ne va pas est de ma faute", score=0),
                    AnswerOption(value='b', label="Bien souvent, ce qui ne va pas est de ma faute", score=1),
                    AnswerOption(value='c', label="Ce qui ne va pas n'est généralement pas de ma faute", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi09',
                text="9.",
                options=[
                    AnswerOption(value='a', label="Je ne pense pas à me tuer", score=0),
                    AnswerOption(value='b', label="Je pense à me tuer mais je ne le ferai pas", score=1),
                    AnswerOption(value='c', label="Je veux me tuer", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi10',
                text="10.",
                options=[
                    AnswerOption(value='a', label="J'ai envie de pleurer tous les jours", score=0),
                    AnswerOption(value='b', label="J'ai souvent envie de pleurer", score=1),
                    AnswerOption(value='c', label="J'ai envie de pleurer de temps en temps", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi11',
                text="11.",
                options=[
                    AnswerOption(value='a', label="Il y a tout le temps quelque chose qui me tracasse / travaille", score=0),
                    AnswerOption(value='b', label="Il y a souvent quelque chose qui me tracasse / travaille", score=1),
                    AnswerOption(value='c', label="Il y a de temps en temps quelque chose qui me tracasse / travaille", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi12',
                text="12.",
                options=[
                    AnswerOption(value='a', label="J'aime bien être avec les autres", score=0),
                    AnswerOption(value='b', label="Souvent, je n'aime pas être avec les autres", score=1),
                    AnswerOption(value='c', label="Je ne veux jamais être avec les autres", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi13',
                text="13.",
                options=[
                    AnswerOption(value='a', label="Je n'arrive pas à me décider entre plusieurs choses", score=0),
                    AnswerOption(value='b', label="J'ai du mal à me décider entre plusieurs choses", score=1),
                    AnswerOption(value='c', label="Je me décide facilement entre plusieurs choses", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi14',
                text="14.",
                options=[
                    AnswerOption(value='a', label="Je me trouve bien physiquement", score=0),
                    AnswerOption(value='b', label="Il y a des choses que je n'aime pas dans mon physique", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi15',
                text="15.",
                options=[
                    AnswerOption(value='a', label="Je dois me forcer tout le temps pour faire mes devoirs", score=0),
                    AnswerOption(value='b', label="Je dois me forcer souvent pour faire mes devoirs", score=1),
                    AnswerOption(value='c', label="Ça ne me pose pas de problème de faire mes devoirs", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi16',
                text="16.",
                options=[
                    AnswerOption(value='a', label="J'ai toujours du mal à dormir la nuit", score=0),
                    AnswerOption(value='b', label="J'ai souvent du mal à dormir la nuit", score=1),
                    AnswerOption(value='c', label="Je dors plutôt bien", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi17',
                text="17.",
                options=[
                    AnswerOption(value='a', label="Je suis fatigué de temps en temps", score=0),
                    AnswerOption(value='b', label="Je suis souvent fatigué", score=1),
                    AnswerOption(value='c', label="Je suis tout le temps fatigué", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi18',
                text="18.",
                options=[
                    AnswerOption(value='a', label="La plupart du temps je n'ai pas envie de manger", score=0),
                    AnswerOption(value='b', label="Souvent je n'ai pas envie de manger", score=1),
                    AnswerOption(value='c', label="J'ai plutôt bon appétit", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi19',
                text="19.",
                options=[
                    AnswerOption(value='a', label="Je ne m'inquiète pas quand j'ai mal quelque part", score=0),
                    AnswerOption(value='b', label="Je m'inquiète souvent quand j'ai mal quelque part", score=1),
                    AnswerOption(value='c', label="Je m'inquiète toujours quand j'ai mal quelque part", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi20',
                text="20.",
                options=[
                    AnswerOption(value='a', label="Je ne me sens pas seul", score=0),
                    AnswerOption(value='b', label="Je me sens souvent seul", score=1),
                    AnswerOption(value='c', label="Je me sens toujours seul", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi21',
                text="21.",
                options=[
                    AnswerOption(value='a', label="Je ne m'amuse jamais à l'école", score=0),
                    AnswerOption(value='b', label="Je m'amuse rarement à l'école", score=1),
                    AnswerOption(value='c', label="Je m'amuse souvent à l'école", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi22',
                text="22.",
                options=[
                    AnswerOption(value='a', label="J'ai beaucoup d'amis", score=0),
                    AnswerOption(value='b', label="J'ai quelques amis mais je voudrais en avoir plus", score=1),
                    AnswerOption(value='c', label="Je n'ai aucun ami", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi23',
                text="23.",
                options=[
                    AnswerOption(value='a', label="Mes résultats scolaires sont bons", score=0),
                    AnswerOption(value='b', label="Mes résultats scolaires ne sont pas aussi bons qu'avant", score=1),
                    AnswerOption(value='c', label="J'ai de mauvais résultats dans des matières où j'avais l'habitude de bien réussir", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi24',
                text="24.",
                options=[
                    AnswerOption(value='a', label="Je ne fais jamais aussi bien que les autres", score=0),
                    AnswerOption(value='b', label="Je peux faire aussi bien que les autres si je le veux", score=1),
                    AnswerOption(value='c', label="Je ne fais ni mieux ni plus mal que les autres", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi25',
                text="25.",
                options=[
                    AnswerOption(value='a', label="Personne ne m'aime vraiment", score=0),
                    AnswerOption(value='b', label="Je me demande si quelqu'un m'aime", score=1),
                    AnswerOption(value='c', label="Je suis sûr que quelqu'un m'aime", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi26',
                text="26.",
                options=[
                    AnswerOption(value='a', label="Je fais généralement ce qu'on me dit", score=0),
                    AnswerOption(value='b', label="La plupart du temps je ne fais pas ce qu'on me dit", score=1),
                    AnswerOption(value='c', label="Je ne fais jamais ce qu'on me dit", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cdi27',
                text="27.",
                options=[
                    AnswerOption(value='a', label="Je m'entends bien avec les autres", score=0),
                    AnswerOption(value='b', label="Je me bagarre souvent", score=1),
                    AnswerOption(value='c', label="Je me bagarre tout le temps", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="CDI",
            name="CDI Questionnaire",
            description="27 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=13,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute CDI score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
