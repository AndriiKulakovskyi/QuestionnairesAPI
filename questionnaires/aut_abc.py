"""
AUT_ABC - AUT_ABC Questionnaire
===============================

61 items questionnaire

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


@register_questionnaire("AUT_ABC")
@dataclass
class AutAbc(BaseQuestionnaire):
    """AUT_ABC Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_ABC questionnaire with all 61 items."""
        
        questions_list = [
            Question(
                id='abc1',
                text="1.Est excessivement actif à la maison, à l'école, au travail ou ailleurs",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc10',
                text="10.A des accès/crises de colère",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc11',
                text="11.A un comportement stéréotypé, des mouvements anormaux et répétitifs.",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc12',
                text="12.Est préoccupé : regarde dans le vide",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc14',
                text="14.Est irritable et pleurnicheur",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc15',
                text="15.Est agité, incapable de rester en place",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc16',
                text="16.Est renfermé : préfère les activités solitaires ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc17',
                text="17.A un comportement bizarre, étrange ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc18',
                text="18.Est désobéissant, difficile à contrôler ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc19',
                text="19.Hurle quand le moment ne s'y prête pas ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc2',
                text="2.Fait exprès de se blesser",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc20',
                text="20.A une expression figée : manque de réactions émotionnelles ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc21',
                text="21.Perturbe les autres ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc22',
                text="22.Discours répétitif ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc23',
                text="23.Ne fait rien d'autre que de rester assis à regarder les autres ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc24',
                text="24.N'est pas coopératif ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc25',
                text="25.Est d'humeur dépressive ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc26',
                text="26.Résiste à  toute forme de contact physique ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc27',
                text="27.Balance sa tête d'avant en arrière et de manière répétitive 	",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc28',
                text="28.Ne fait pas attention aux instructions qu’on lui donne 	",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc29',
                text="29.Exige que l'on fasse immédiatement ce qu'il veut 	",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc3',
                text="3.Manque d'entrain, est mou, inactif",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc30',
                text="30.S'isole des autres enfants ou adultes 	",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc31',
                text="31.Perturbe les activités de groupe ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc32',
                text="32.Reste longtemps assis ou debout dans la même position ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc33',
                text="33.Se parle à voix haute ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc34',
                text="34.Pleure pour des petites contrariétés ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc35',
                text="35.Fait des mouvements répétitifs avec la tête, le corps ou les mains ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc36',
                text="36.A de brusques sautes d'humeur ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc39',
                text="39.N'arrive pas à rester assis longtemps \n",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc40',
                text="40.Il est difficile d'entrer en relation, d'établir un contact ou un dialogue avec lui \n\n",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc41',
                text="41.Pleure et hurle quand la situation ne s'y prête pas \n\n",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc42',
                text="42.Préfère être seul \n\n",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc43',
                text="43.N'essaye pas de communiquer avec des mots ou par des gestes \n\n",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc44',
                text="44.Se laisse facilement distraire \n\n",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc45',
                text="45.Remue ou agite les mains ou les pieds de façon répétée \n\n",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc46',
                text="46.Répète sans cesse le même mot ou la même expression \n",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc47',
                text="47.Tape des pieds, donne des coups dans les objets ou claque les portes \n",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc48',
                text="48.Court ou saute constamment à travers la pièce \n",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc49',
                text="49.Balance le corps d'avant en arrière de façon répétée \n",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc5',
                text="5.Cherche à s'isoler des autres",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc50',
                text="50.Fait exprès de se faire mal \n",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc51',
                text="51.Ne fait pas attention quand on lui parle ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc52',
                text="52.S'inflige des violences physiques ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc53',
                text="53.Est inactif, ne bouge jamais spontanément ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc54',
                text="54.A tendance à être excessivement actif ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc55',
                text="55.Réagit de manière négative lorsqu'on lui montre de l'affection ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc56',
                text="56.Ignore délibérément les ordres qu'on lui donne  ",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc57',
                text="57.A des accès ou des crises de colère quand il n'obtient\n pas ce qu'il veut",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc58',
                text="58.Se montre indifférent vis-à-vis des autres \n",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc6',
                text="6.Répète, sans raison, les mêmes mouvements avec son corps",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc8',
                text="8.Crie quand la situation ne s'y prête pas",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc9',
                text="9.Parle de manière excessive",
                options=[
                    AnswerOption(value='a', label="Ce n'est pas du tout un problème", score=0),
                    AnswerOption(value='b', label="C'est un problème peu important", score=1),
                    AnswerOption(value='c', label="C'est un problème moyennement important", score=2),
                    AnswerOption(value='d', label="C'est un problème très important", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc_liensuj',
                text="Lien avec le sujet ",
                options=[
                    AnswerOption(value='a', label="Père/mère", score=0),
                    AnswerOption(value='b', label="Enseignant", score=1),
                    AnswerOption(value='c', label="Personnel d'encadrement", score=2),
                    AnswerOption(value='d', label="Autre", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc_sitmed1',
                text="a.Est-il sourd ?",
                options=[
                    AnswerOption(value='a', label="Non", score=0),
                    AnswerOption(value='b', label="Oui", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc_sitmed2',
                text="a.Est-il aveugle ?",
                options=[
                    AnswerOption(value='a', label="Non", score=0),
                    AnswerOption(value='b', label="Oui", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc_sitmed3',
                text="a.Est-il épileptique ?",
                options=[
                    AnswerOption(value='a', label="Non", score=0),
                    AnswerOption(value='b', label="Oui", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc_sitmed4',
                text="d.A-t'il une paralysie cérébrale ",
                options=[
                    AnswerOption(value='a', label="Non", score=0),
                    AnswerOption(value='b', label="Oui", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc_sitmed5',
                text="e. Autre",
                options=[
                    AnswerOption(value='a', label="Non", score=0),
                    AnswerOption(value='b', label="Oui", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc_sujclas',
                text="Si le sujet va à l'école, veuillez indiquer le type de classe",
                options=[
                    AnswerOption(value='a', label="Classe pour personnes ayant des troubles du développement", score=0),
                    AnswerOption(value='b', label="Classe pour personnes ayant des troubles importants du comportement", score=1),
                    AnswerOption(value='c', label="Classe pour polyhandicapés", score=2),
                    AnswerOption(value='d', label="Autre", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='abc_sujobs',
                text="Où le sujet a-t-il été observé ?",
                options=[
                    AnswerOption(value='a', label="Domicile", score=0),
                    AnswerOption(value='b', label="Ecole", score=1),
                    AnswerOption(value='c', label="Foyer d'accueil/Résidence", score=2),
                    AnswerOption(value='d', label="Atelier d’activités spécialisées", score=3),
                    AnswerOption(value='e', label="Autre", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_ABC",
            name="AUT_ABC Questionnaire",
            description="61 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=30,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_ABC score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
