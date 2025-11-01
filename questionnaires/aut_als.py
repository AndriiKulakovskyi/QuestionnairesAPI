"""
AUT_ALS - AUT_ALS Questionnaire
===============================

34 items questionnaire

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


@register_questionnaire("AUT_ALS")
@dataclass
class AutAls(BaseQuestionnaire):
    """AUT_ALS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_ALS questionnaire with all 34 items."""
        
        questions_list = [
            Question(
                id='als_1',
                text="1.Mon cycle de sommeil passe de périodes où je dors parfaitement bien à des périodes où j'ai des insomnies et je ne peux pas dormir bien du tout.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_10',
                text="10.La seule chose à laquelle je pense est à quel point je ne vaux rien et très rapidement après je ne pense qu’aux choses qui m’inquiètent.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_11',
                text="11.Mes habitudes de sommeil passent fréquemment de périodes où je pourrais dormir toute la journée à des périodes où je n'ai plus beaucoup besoin de dormir.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_13',
                text="13.Quelques fois je me sens très coupable à propos de choses et ensuite, tout d'un coup, elles arrêtent de me tracasser.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_14',
                text="14.J'oscille souvent entre des moments où je contrôle très bien mon humeur à des moments où je ne la contrôle plus du tout.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_15',
                text="15.C'est très courant pour moi d'être très en colère à propos de quelque chose et ensuite, soudainement de me sentir comme je suis habituellement.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_17',
                text="17.Quelques fois je passe de sentiments très anxieux au sujet de quelque chose à des sentiments très tristes à leur propos.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_19',
                text="19.Il y a des moments où je me sens modérément optimiste au sujet du futur et tout de suite après très pessimiste au sujet du futur et de ce qu'il va apporter.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_23',
                text="23.Fréquemment, je me sens OK mais ensuite tout d'un coup, je deviens si fou que je pourrais frapper quelque chose.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_25',
                text="25.Souvent, je peux penser clairement et bien me concentrer pendant une minute et la minute suivante, j'ai beaucoup de difficultés à me concentrer et à penser clairement.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_26',
                text="26.J'oscille entre des périodes où je dors parfaitement bien et des périodes où je suis si nerveux que je peux à peine dormir.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_27',
                text="27.J'oscille entre des périodes où j'ai très envie d'être avec beaucoup de monde à des périodes où je n'ai pas plus envie d'activités sociales que la plupart des autres personnes.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_30',
                text="30.Il y a des moments où j'ai l'impression que je ne vaux rien et ensuite soudainement je vais commencer à trouver admirable ce que je suis et ce que j'ai fait.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_31',
                text="31.Quelques fois, je me sens parfaitement bien pendant une minute et la minute suivant, je vais être en train de pleurer.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_32',
                text="32.Mon optimisme passe souvent de périodes où je suis très optimiste à des périodes où j'ai le même niveau d'optimisme que n'importe qui d'autre.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_34',
                text="34.J'oscille entre des périodes où je me sens plein d'énergie et d'autres où j'ai si peu d'énergie que c'est un énorme effort juste d'ailler là où je dois aller.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_36',
                text="36.Il y a des moments où je me sens absolument admirable et à d'autres juste après où je me sens exactement comme n'importe qui d'autre.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_37',
                text="37.J'oscille entre m'inquiéter à propos de beaucoup de choses et des moments où je ne m'intéresse pratiquement à rien.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_39',
                text="39.Mon niveau de productivité passe fréquemment de moments où je ne suis pas plus productif que n'importe qui d'autre à des moments où je me sens très productif.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_4',
                text="4.J'oscille fréquemment de périodes où je m'inquiète plus que d'autres personnes à des périodes où je ne me fais pas plus de souci que les autres.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_40',
                text="40.Mon niveau d’appétit change souvent de plus élevé ou plus bas que normal à un niveau parfaitement normal.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_43',
                text="43.Quelques fois j’ai beaucoup d’énergie une minute et la minute suivante j’ai tellement peu d’énergie que je peux presque rien faire.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_44',
                text="44.J'oscille entre me sentir parfaitement calme et ressentir soit que mon cœur bat fort ou va très vite, et/ou que j'ai la nausée et/ou que j'ai du mal à respirer.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_45',
                text="45.Il y a des moments où j'ai plus d'énergie que d'habitude et plus que la plupart des gens et rapidement après j'ai à peu près le même niveau d'énergie que n'importe qui d'autre.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_46',
                text="46.A certains moments, j'ai l'impression de tout faire très lentement et très rapidement après, j'ai l'impression de ne pas être plus lent que quelqu'un d'autre.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_47',
                text="47.J'oscille entre penser de manière inhabituellement claire et avec créativité à des périodes où je ne pense pas avec plus de créativité ou de clarté que quelqu'un d'autre.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_48',
                text="48.Mon cycle de sommeil passe de périodes où j'ai du mal à m'endormir à des périodes où j’ai très peu envie de dormir.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_49',
                text="49.A certains moments, j'ai du mal à me concentrer où à penser et peu de temps après je pense beaucoup à toutes les choses qui m'inquiètent.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_53',
                text="53.J'oscille entre des moments où je n'ai presque pas besoin de sommeil et des moments où j'ai besoin de la même quantité de sommeil que la plupart des gens.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_54',
                text="54.Ma préférence pour les activités sociales oscille entre des moments où j'apprécie les autres et d'autres où je préfère être moi-même et ne vois personne d'autre",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_6',
                text="6.Il y a des moments où je m'implique très rapidement dans des activités, ce que je regretterai plus tard, et pour lesquelles je perdrai tout intérêt.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_7',
                text="7.J'oscille entre des moments où je parle beaucoup plus que d'habitude et des moments où j'ai seulement une envie normale de parler.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_8',
                text="8.Il y a des moments où j'ai très peu d'énergie et en peu de temps après j'ai autant d'énergie que la plupart des gens.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='als_9',
                text="9.Le plaisir que je prends à effectuer mes activités quotidiennes oscille entre des moments où j’apprécie de les effectuer à d’autres moments où je n’y trouve aucun plaisir.",
                options=[
                    AnswerOption(value='a', label="Très caractéristique", score=0),
                    AnswerOption(value='b', label="Assez caractéristique", score=1),
                    AnswerOption(value='c', label="Assez peu caractéristique", score=2),
                    AnswerOption(value='d', label="Absolument pas caractéristique", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_ALS",
            name="AUT_ALS Questionnaire",
            description="34 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=17,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_ALS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
