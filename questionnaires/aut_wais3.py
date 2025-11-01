"""
AUT_WAIS3 - AUT_WAIS3 Questionnaire
===================================

227 items questionnaire

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


@register_questionnaire("AUT_WAIS3")
@dataclass
class AutWais3(BaseQuestionnaire):
    """AUT_WAIS3 Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_WAIS3 questionnaire with all 227 items."""
        
        questions_list = [
            Question(
                id='wais_arimg1',
                text="Image 1",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arimg10',
                text="Image 10",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arimg2',
                text="Image 2",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arimg3',
                text="Image 3",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arimg4',
                text="Image 4",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arimg5',
                text="Image 5",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arimg6',
                text="Image 6",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arimg7',
                text="Image 7",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arimg8',
                text="Image 8",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arimg9',
                text="Image 9",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit1',
                text="1.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit10',
                text="10.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit11',
                text="11.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit12',
                text="12.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit13',
                text="13.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit14',
                text="14.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit15',
                text="15.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit16',
                text="16.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit17',
                text="17.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit18',
                text="18.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit19',
                text="19.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit2',
                text="2.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit20',
                text="20.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit3',
                text="3.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit4',
                text="4.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit5',
                text="5.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit6',
                text="6.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit7',
                text="7.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit8',
                text="8.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit9',
                text="9.Note à l’item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_comp1',
                text="1.Pourquoi les gens portent-ils des montres?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_comp13',
                text="13.C’est en forgeant que l’on devient forgeron que l’on devient forgeron",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_comp14',
                text="14.Quel est l’intérèt du parlement dans une démocratie?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_comp15',
                text="15.Pourquoi y a-t-il des jurés dans un procès de cour d’assises?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_comp17',
                text="17.Pourquoi un parlementaire ne peut-il être en même temps juge dans un tribunal?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_comp18',
                text="18.Pourquoi l’usage de la monnaie a-t-il largement supplanté le troc?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_comp2',
                text="2.Pourquoi doit-on laver les vêtements?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_comp3',
                text="3.Que faites-vous si vous trouvez dans la rue une enveloppe fermée portant une adresse et un timbre neuf?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_comp5',
                text="5.Pourqoui avons-nous des musées? (Q:Pour exposer des peintures, pour voir des objets anciens, garder des oeuvres/le patrimoine. ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_comp7',
                text="7.L’habit ne fait pas le moine",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_comp8',
                text="8.Pourquoi les gens qui sont sourds de naissance ont-ils du mal à apprendre à parler? (Q:Les enfants apprennent à parler en écoutant, le langage suppose une audition à la base",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub1',
                text="\n                      1.Dessin\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub10',
                text="\n                      10.Dessin\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub11',
                text="\n                      11.Dessin\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub12',
                text="\n                      12.Dessin\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub13',
                text="\n                      13.Dessin\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub14',
                text="\n                      14.Dessin\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub2',
                text="\n                      2.Dessin\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub3',
                text="\n                      3.Dessin\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub4',
                text="\n                      4.Dessin\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub5',
                text="\n                      5.Dessin\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub6',
                text="\n                      6.Dessin\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub7',
                text="\n                      7.Dessin\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub8',
                text="\n                      8.Dessin\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub9',
                text="\n                      9.Dessin\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img1',
                text="1.Peigne",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img10',
                text="10.Feuille",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img11',
                text="11.Gâteau",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img12',
                text="12.Coureurs",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img13',
                text="13.Cheminée",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img14',
                text="14.Miroir",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img15',
                text="15.Chaise",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img16',
                text="16.Roses",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img17',
                text="17.Couteau",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img18',
                text="18.Barque",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img19',
                text="19.Panier",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img2',
                text="2.Table",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img20',
                text="20.Vêtements",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img21',
                text="21.Armoire",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img22',
                text="22.Vache",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img23',
                text="23.Tennis",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img24',
                text="24.Femme",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img25',
                text="25.Chalet",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img3',
                text="3.Visage",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img4',
                text="4.Mallette",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img5',
                text="5.Train",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img6',
                text="6.Porte",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img7',
                text="7.Lunettes",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img8',
                text="8.Cruche",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img9',
                text="9.Pince",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info1',
                text="1.Combien de mois dans une année?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info10',
                text="10.Qu'est-ce que le Coran? ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info11',
                text="11.Que signifient les initiales O.N.U? ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info12',
                text="12.Qui a écrit 'Hamlet'?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info13',
                text="13.Qui a écrit 'le tour du monde en 80 jours'",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info14',
                text="14.Qui était Rodin?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info15',
                text="15.Qui était Martin Luther King? ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info16',
                text="16.A quelle invention est associé le nom de Gutenberg?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info17',
                text="17.Qui a peint la chapelle Sixtine? ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info18',
                text="18.Quel est le nom habituellement associé à la théorie de la relativité?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info19',
                text="19.Qu'est ce qui a rendu célèbre Marie Curie? ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info2',
                text="2.Quel jour vient juste après samedi? ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info20',
                text="20.Comment s'appelle le plus haut sommet d'Afrique?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info21',
                text="21.Quel personnage de roman célèbre a été créé par Cervantès?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info22',
                text="22.Quelle est la capitale de la Finlande? ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info23',
                text="23.Qui est l'auteur de la théorie de l'évolution des espèces?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info24',
                text="24.Qui a écrit 'Faust'?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info25',
                text="25.Combien y a t-il d'habitants dans le monde?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info26',
                text="26.Quel est le nom du premier homme qui a traversé la manche en avion?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info27',
                text="27.Qu'est ce qu'un copte? ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info28',
                text="28.Quelle invention a permis le développement des ordinateurs personnels?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info3',
                text="3.Quelle est la forme d'une balle?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info4',
                text="4.Quel âge avez-vous? ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info5',
                text="5.Qu'est ce qu'un thermomètre? ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info6',
                text="6.Où se trouve le Brésil? ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info7',
                text="7.De quel côté le soleil se lève-t-il?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info8',
                text="8.Quel est le pays d'origine des jeux olympiques? ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info9',
                text="9.Sur quel continent se trouve l'Egypte? ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat1',
                text="Note pour l’item 1",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat10',
                text="Note pour l’item10",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat11',
                text="Note pour l’item11",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat12',
                text="Note pour l’item12",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat13',
                text="Note pour l’item13",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat14',
                text="Note pour l’item14",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat15',
                text="Note pour l’item15",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat16',
                text="Note pour l’item16",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat17',
                text="Note pour l’item17",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat18',
                text="Note pour l’item18",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat19',
                text="Note pour l’item19",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat2',
                text="Note pour l’item 2",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat20',
                text="Note pour l’item20",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat21',
                text="Note pour l’item21",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat22',
                text="Note pour l’item22",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat23',
                text="Note pour l’item23",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat24',
                text="Note pour l’item24",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat25',
                text="Note pour l’item25",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat26',
                text="Note pour l’item26",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat3',
                text="Note pour l’item 3",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat4',
                text="Note pour l’item 4",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat5',
                text="Note pour l’item 5",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat6',
                text="Note pour l’item 6",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat7',
                text="Note pour l’item 7",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat8',
                text="Note pour l’item 8",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat9',
                text="Note pour l’item 9",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_1a',
                text="1-1 Note à l'essai",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_1b',
                text="1-1 Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_2a',
                text="2-1 Note à l'essai",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_2b',
                text="2-2 Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_3a',
                text="3-1 Note à l'essai",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_3b',
                text="3-2 Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_4a',
                text="4-1 Note à l'essai",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_4b',
                text="4-2 Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_5a',
                text="5-1 Note à l'essai",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_5b',
                text="5-2 Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_6a',
                text="6-1 Note à l'essai",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_6b',
                text="6-2 Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_7a',
                text="7-1 Note à l'essai",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_7b',
                text="7-2 Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_8a',
                text="8-1 Note à l'essai",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_8b',
                text="8-2 Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_1a',
                text="1-1 Note à l'essai",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_1b',
                text="1-1 Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_2a',
                text="2-1 Note à l'essai",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_2b',
                text="2-2 Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_3a',
                text="3-1 Note à l'essai",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_3b',
                text="3-2 Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_4a',
                text="4-1 Note à l'essai",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_4b',
                text="4-2 Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_5a',
                text="5-1 Note à l'essai",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_5b',
                text="5-2 Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_6a',
                text="6-1 Note à l'essai",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_6b',
                text="6-2 Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_7a',
                text="7-1 Note à l'essai",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_7b',
                text="7-2 Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_obj1b',
                text="Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_obj2b',
                text="Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6", score=6),
                    AnswerOption(value='h', label="7", score=7),
                    AnswerOption(value='i', label="8", score=8)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_obj3b',
                text="Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6", score=6),
                    AnswerOption(value='h', label="7", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_obj4b',
                text="Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6", score=6)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_obj5b',
                text="Note à l'item",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5", score=5),
                    AnswerOption(value='g', label="6", score=6),
                    AnswerOption(value='h', label="7", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim1',
                text="1.manteau-costume",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim10',
                text="10.cube-cylindre",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim11',
                text="11.manger-dormir",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim12',
                text="12.poème-statue",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim13',
                text="13.récompense-punition ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim14',
                text="14.vapeur-brouillard",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim15',
                text="15.douanier-instituteur",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim16',
                text="16.dictionnaire-annuaire",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim17',
                text="17.caoutchouc-papier",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim18',
                text="18.vent- eau",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim19',
                text="19.sédentaire-nomade",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim2',
                text="2.jaune-vert",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim3',
                text="3.chien-lion",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim4',
                text="4.cuillère-fourchette",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim5',
                text="5.chaussettes-chaussures",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim6',
                text="6.bateau-voiture ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim7',
                text="7.œil-oreille",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim8',
                text="8.table-chaise",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim9',
                text="9.soie-laine",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc1a',
                text="L-2",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc1b',
                text="6-P",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc1c',
                text="B-5",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc2a',
                text="F-7-L ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc2b',
                text="R-4-D",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc2c',
                text="H-1-8 ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc3a',
                text="T-9-A-3 ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc3b',
                text="V-1-J-5 ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc3c',
                text="7-N-4-L ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc4a',
                text="8-D-6-G-1 ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc4b',
                text="K-2-C-7-S ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc4c',
                text="5-P-3-Y-9 ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc5a',
                text="M-4-E-7-Q-2 ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc5b',
                text="W-8-H-5-F-3 ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc5c',
                text="6-G-9-A-2-S ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc6a',
                text="R-3-B-4-Z-1-C ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc6b',
                text="5-T-9-J-2-X-7 ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc6c',
                text="E-1-H-8-R-4-D ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc7a',
                text="5-H-9-S-2-N-6-A ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc7b',
                text="D-1-R-9-B-4-K-3 ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_slc7c',
                text="7-M-2-T-6-F-1-Z ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc1',
                text="1.Bateau",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc13',
                text="13.Sauvage",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc16',
                text="16.Grandiose",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc17',
                text="17.Confier",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc18',
                text="18.Vigoureux",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc19',
                text="19.Contracter",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc2',
                text="2.Fauteuil",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc22',
                text="22.Irritable",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc25',
                text="25.Assimiler",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc26',
                text="26.Concertation",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc28',
                text="\n                      28.Pittoresque\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc3',
                text="3.Bol",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc30',
                text="\n                      30.Elaborer\n\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc31',
                text="\n                      31.Prosaïque\n\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc32',
                text="\n                      32.Apologie\n\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc33',
                text="\n                      33.Conjecture\n\n                    ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc4',
                text="4.Instruire",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc5',
                text="5.Hier",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_WAIS3",
            name="AUT_WAIS3 Questionnaire",
            description="227 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=113,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_WAIS3 score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
