"""
AUT_ANH_SO - AUT_ANH_SO Questionnaire
=====================================

31 items questionnaire

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


@register_questionnaire("AUT_ANH_SO")
@dataclass
class AutAnhSo(BaseQuestionnaire):
    """AUT_ANH_SO Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_ANH_SO questionnaire with all 31 items."""
        
        questions_list = [
            Question(
                id='anh-so1',
                text="1.Avoir des amis intimes n'est pas aussi important que beaucoup de personnes le disent.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so11',
                text="11.Quand les choses vont vraiment bien pour mes amis proches, cela me fait plaisir.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so12',
                text="12.Quand quelqu’un proche de moi est déprimé, cela me déprime aussi.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so13',
                text="13.Mes réponses émotionnelles semblent très différentes de celles des autres gens.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so15',
                text="15.Le fait d’être avec des amis me fait me sentir vraiment bien.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so16',
                text="16.Lorsque des choses me préoccupent, j’aime bien en parler à d’autres gens.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so17',
                text="17.Je préfère des activités de loisirs et de détente qui n’impliquent pas d’autres gens.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so18',
                text="18.C’est amusant de chanter avec d’autres gens.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so19',
                text="19.Savoir que j’ai des amis qui s’occupent de moi me donne un sentiment de sécurité.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so2',
                text="2.J'attache très peu d'importance à avoir des amis intimes.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so20',
                text="20.Lorsque je déménage dans une autre ville, j’ai un grand besoin de me faire de nouveaux de nouveaux amis.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so21',
                text="21.Les gens se sentent généralement mieux s’ils restent à l’écart des implications émotionnelles de la majorité des gens.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so22',
                text="22.Bien que je sache que je devrais avoir de l’affection pour certains, en réalité je n’en éprouve pas.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so23',
                text="23.Les gens attendent souvent de moi que je bavarde davantage avec eux que je ne le souhaiterais.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so24',
                text="24.Je trouve agréable et enrichissant d’apprendre de plus en plus sur la vie émotionnelle de mes amis.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so25',
                text="25.J’écoute d’habitude avec attention et intérêt ce que les autres essaient de me raconter sur leurs problèmes et leurs contrariétés.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so26',
                text="26.Je n’ai jamais vraiment eu d’amis intimes au lycée.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so29',
                text="29.Il existe peu de choses plus fatigantes que d’avoir avec quelqu’un une discussion longue et personnelle.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so3',
                text="3.Je préfère regarder la télévision plutôt que de sortir avec des gens.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so31',
                text="31.J’ai souvent constaté qu’il était difficile de résister à une conversation avec un bon copain, même quand j’ai autre chose à faire.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so32',
                text="32.Se faire de nouveaux amis ne vaut pas l’énergie que cela nécessite.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so33',
                text="33.Il y a des choses plus importantes pour moi que l’intimité.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so34',
                text="34.Les gens qui essaient de mieux me connaître abandonnent généralement au bout d’un moment.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so37',
                text="37.Je trouve que trop souvent les gens supposent que leurs activités courantes et leurs opinions vont m’intéresser.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so38',
                text="38.Je ne me sens pas vraiment très proche de mes amis.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so39',
                text="39.Mes relations avec les autres personnes n’ont jamais atteints un niveau très intimes.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so4',
                text="4.Un trajet en voiture est beaucoup plus agréable si quelqu’un est avec moi.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so40',
                text="40.Pour diverses raisons, je préfère la compagnie des animaux familiers à celle des gens.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so5',
                text="5.J’aime faire des appels téléphoniques à longue distance à des amis ou à des proches.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so6',
                text="6.Jouer avec des enfants est une vraie corvée.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anh-so7',
                text="7.J’ai toujours aimé regarder des photographies d’amis.",
                options=[
                    AnswerOption(value='a', label="Vrai", score=0),
                    AnswerOption(value='b', label="Faux", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_ANH_SO",
            name="AUT_ANH_SO Questionnaire",
            description="31 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=15,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_ANH_SO score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
