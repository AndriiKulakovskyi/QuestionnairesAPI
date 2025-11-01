"""
AUT_NPSY_COMP - AUT_NPSY_COMP Questionnaire
===========================================

143 items questionnaire

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


@register_questionnaire("AUT_NPSY_COMP")
@dataclass
class AutNpsyComp(BaseQuestionnaire):
    """AUT_NPSY_COMP Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_NPSY_COMP questionnaire with all 143 items."""
        
        questions_list = [
            Question(
                id='cpt2_a4',
                text="analyse",
                options=[
                    AnswerOption(value='a', label="Markedly atypical", score=0),
                    AnswerOption(value='b', label="Midly atypical", score=1),
                    AnswerOption(value='c', label="A little slow", score=2),
                    AnswerOption(value='d', label="Within average range", score=3),
                    AnswerOption(value='e', label="Good performance", score=4),
                    AnswerOption(value='f', label="Very good perfomance", score=5),
                    AnswerOption(value='g', label="A little fast", score=6),
                    AnswerOption(value='h', label="Atypically fast", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cpt2_b4',
                text="analyse",
                options=[
                    AnswerOption(value='a', label="Markedly atypical", score=0),
                    AnswerOption(value='b', label="Midly atypical", score=1),
                    AnswerOption(value='c', label="A little slow", score=2),
                    AnswerOption(value='d', label="Within average range", score=3),
                    AnswerOption(value='e', label="Good performance", score=4),
                    AnswerOption(value='f', label="Very good perfomance", score=5),
                    AnswerOption(value='g', label="A little fast", score=6),
                    AnswerOption(value='h', label="Atypically fast", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cpt2_c4',
                text="analyse",
                options=[
                    AnswerOption(value='a', label="Markedly atypical", score=0),
                    AnswerOption(value='b', label="Midly atypical", score=1),
                    AnswerOption(value='c', label="A little slow", score=2),
                    AnswerOption(value='d', label="Within average range", score=3),
                    AnswerOption(value='e', label="Good performance", score=4),
                    AnswerOption(value='f', label="Very good perfomance", score=5),
                    AnswerOption(value='g', label="A little fast", score=6),
                    AnswerOption(value='h', label="Atypically fast", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cpt2_d4',
                text="analyse",
                options=[
                    AnswerOption(value='a', label="Markedly atypical", score=0),
                    AnswerOption(value='b', label="Midly atypical", score=1),
                    AnswerOption(value='c', label="A little slow", score=2),
                    AnswerOption(value='d', label="Within average range", score=3),
                    AnswerOption(value='e', label="Good performance", score=4),
                    AnswerOption(value='f', label="Very good perfomance", score=5),
                    AnswerOption(value='g', label="A little fast", score=6),
                    AnswerOption(value='h', label="Atypically fast", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cpt2_e4',
                text="analyse",
                options=[
                    AnswerOption(value='a', label="Markedly atypical", score=0),
                    AnswerOption(value='b', label="Midly atypical", score=1),
                    AnswerOption(value='c', label="A little slow", score=2),
                    AnswerOption(value='d', label="Within average range", score=3),
                    AnswerOption(value='e', label="Good performance", score=4),
                    AnswerOption(value='f', label="Very good perfomance", score=5),
                    AnswerOption(value='g', label="A little fast", score=6),
                    AnswerOption(value='h', label="Atypically fast", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cpt2_f4',
                text="analyse",
                options=[
                    AnswerOption(value='a', label="Markedly atypical", score=0),
                    AnswerOption(value='b', label="Midly atypical", score=1),
                    AnswerOption(value='c', label="A little slow", score=2),
                    AnswerOption(value='d', label="Within average range", score=3),
                    AnswerOption(value='e', label="Good performance", score=4),
                    AnswerOption(value='f', label="Very good perfomance", score=5),
                    AnswerOption(value='g', label="A little fast", score=6),
                    AnswerOption(value='h', label="Atypically fast", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cpt2_g4',
                text="analyse",
                options=[
                    AnswerOption(value='a', label="Markedly atypical", score=0),
                    AnswerOption(value='b', label="Midly atypical", score=1),
                    AnswerOption(value='c', label="A little slow", score=2),
                    AnswerOption(value='d', label="Within average range", score=3),
                    AnswerOption(value='e', label="Good performance", score=4),
                    AnswerOption(value='f', label="Very good perfomance", score=5),
                    AnswerOption(value='g', label="A little fast", score=6),
                    AnswerOption(value='h', label="Atypically fast", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cpt2_h4',
                text="analyse",
                options=[
                    AnswerOption(value='a', label="Markedly atypical", score=0),
                    AnswerOption(value='b', label="Midly atypical", score=1),
                    AnswerOption(value='c', label="A little slow", score=2),
                    AnswerOption(value='d', label="Within average range", score=3),
                    AnswerOption(value='e', label="Good performance", score=4),
                    AnswerOption(value='f', label="Very good perfomance", score=5),
                    AnswerOption(value='g', label="A little fast", score=6),
                    AnswerOption(value='h', label="Atypically fast", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cpt2_j4',
                text="analyse",
                options=[
                    AnswerOption(value='a', label="Markedly atypical", score=0),
                    AnswerOption(value='b', label="Midly atypical", score=1),
                    AnswerOption(value='c', label="A little slow", score=2),
                    AnswerOption(value='d', label="Within average range", score=3),
                    AnswerOption(value='e', label="Good performance", score=4),
                    AnswerOption(value='f', label="Very good perfomance", score=5),
                    AnswerOption(value='g', label="A little fast", score=6),
                    AnswerOption(value='h', label="Atypically fast", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cpt2_k4',
                text="analyse",
                options=[
                    AnswerOption(value='a', label="Markedly atypical", score=0),
                    AnswerOption(value='b', label="Midly atypical", score=1),
                    AnswerOption(value='c', label="A little slow", score=2),
                    AnswerOption(value='d', label="Within average range", score=3),
                    AnswerOption(value='e', label="Good performance", score=4),
                    AnswerOption(value='f', label="Very good perfomance", score=5),
                    AnswerOption(value='g', label="A little fast", score=6),
                    AnswerOption(value='h', label="Atypically fast", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cpt2_l4',
                text="analyse",
                options=[
                    AnswerOption(value='a', label="Markedly atypical", score=0),
                    AnswerOption(value='b', label="Midly atypical", score=1),
                    AnswerOption(value='c', label="A little slow", score=2),
                    AnswerOption(value='d', label="Within average range", score=3),
                    AnswerOption(value='e', label="Good performance", score=4),
                    AnswerOption(value='f', label="Very good perfomance", score=5),
                    AnswerOption(value='g', label="A little fast", score=6),
                    AnswerOption(value='h', label="Atypically fast", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cpt2_m4',
                text="analyse",
                options=[
                    AnswerOption(value='a', label="Markedly atypical", score=0),
                    AnswerOption(value='b', label="Midly atypical", score=1),
                    AnswerOption(value='c', label="A little slow", score=2),
                    AnswerOption(value='d', label="Within average range", score=3),
                    AnswerOption(value='e', label="Good performance", score=4),
                    AnswerOption(value='f', label="Very good perfomance", score=5),
                    AnswerOption(value='g', label="A little fast", score=6),
                    AnswerOption(value='h', label="Atypically fast", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cpt2_n4',
                text="analyse",
                options=[
                    AnswerOption(value='a', label="Markedly atypical", score=0),
                    AnswerOption(value='b', label="Midly atypical", score=1),
                    AnswerOption(value='c', label="A little slow", score=2),
                    AnswerOption(value='d', label="Within average range", score=3),
                    AnswerOption(value='e', label="Good performance", score=4),
                    AnswerOption(value='f', label="Very good perfomance", score=5),
                    AnswerOption(value='g', label="A little fast", score=6),
                    AnswerOption(value='h', label="Atypically fast", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol1_1',
                text="Erreur violation de règle type1",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol1_10',
                text="Erreur violation de règle type1",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol1_2',
                text="Erreur violation de règle type1",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol1_3',
                text="Erreur violation de règle type1",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol1_4',
                text="Erreur violation de règle type1",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol1_5',
                text="Erreur violation de règle type1",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol1_6',
                text="Erreur violation de règle type1",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol1_7',
                text="Erreur violation de règle type1",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol1_8',
                text="Erreur violation de règle type1",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol1_9',
                text="Erreur violation de règle type1",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol2_1',
                text="Erreur violation de règle type2",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol2_10',
                text="Erreur violation de règle type2",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol2_2',
                text="Erreur violation de règle type2",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol2_3',
                text="Erreur violation de règle type2",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol2_4',
                text="Erreur violation de règle type2",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol2_5',
                text="Erreur violation de règle type2",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol2_6',
                text="Erreur violation de règle type2",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol2_7',
                text="Erreur violation de règle type2",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol2_8',
                text="Erreur violation de règle type2",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_rviol2_9',
                text="Erreur violation de règle type2",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_tviol_1',
                text="Temps Sup à 1 min",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_tviol_10',
                text="Temps Sup à 1 min",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_tviol_2',
                text="Temps Sup à 1 min",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_tviol_3',
                text="Temps Sup à 1 min",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_tviol_4',
                text="Temps Sup à 1 min",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_tviol_5',
                text="Temps Sup à 1 min",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_tviol_6',
                text="Temps Sup à 1 min",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_tviol_7',
                text="Temps Sup à 1 min",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_tviol_8',
                text="Temps Sup à 1 min",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='london_tviol_9',
                text="Temps Sup à 1 min",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie1',
                text="1",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie10',
                text="10",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie11',
                text="11",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie12',
                text="12",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie13',
                text="13",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie14',
                text="14",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie15',
                text="15",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie16',
                text="16",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie17',
                text="17",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie18',
                text="18",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie19',
                text="19",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie2',
                text="2",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie20',
                text="20",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie21',
                text="21",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie22',
                text="22",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie23',
                text="23",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie24',
                text="24",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie25',
                text="25",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie26',
                text="26",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie27',
                text="27",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie28',
                text="28",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie29',
                text="29",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie3',
                text="3",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie30',
                text="30",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie31',
                text="31",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie32',
                text="32",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie33',
                text="33",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie34',
                text="34",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie35',
                text="35",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie36',
                text="36",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie4',
                text="4",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie5',
                text="5",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie6',
                text="6",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie7',
                text="7",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie8',
                text="8",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rmie9',
                text="9",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="0", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin1',
                text="1.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin10',
                text="10.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin11',
                text="11.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin12',
                text="12.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin13',
                text="13.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin14',
                text="14.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin15',
                text="15.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin16',
                text="16.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin17',
                text="17.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin18',
                text="18.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin19',
                text="19.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin2',
                text="2.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin20',
                text="20.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin21',
                text="21.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin22',
                text="22.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin23',
                text="23.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin24',
                text="24.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin25',
                text="25.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin26',
                text="26.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin27',
                text="27.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin28',
                text="28.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin29',
                text="29.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin3',
                text="3.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin30',
                text="30.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin31',
                text="31.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin32',
                text="32.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin33',
                text="33.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin34',
                text="34.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin35',
                text="35.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin36',
                text="36.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin37',
                text="37.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin38',
                text="38.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin39',
                text="39.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin4',
                text="4.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin40',
                text="40.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin41',
                text="41.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin42',
                text="42.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin43',
                text="43.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin44',
                text="44.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin45',
                text="45.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin46',
                text="46.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin47',
                text="47.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin48',
                text="48.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin49',
                text="49.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin5',
                text="5.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin50',
                text="50.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin51',
                text="51.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin52',
                text="52.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin53',
                text="53.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin54',
                text="54.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin55',
                text="55.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin56',
                text="56.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin57',
                text="57.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin58',
                text="58.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin59',
                text="59.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin6',
                text="6.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin60',
                text="60.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin61',
                text="61.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin62',
                text="62.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin63',
                text="63.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin64',
                text="64.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin7',
                text="7.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin8',
                text="8.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wisconsin9',
                text="9.",
                options=[
                    AnswerOption(value='a', label="C", score=0),
                    AnswerOption(value='b', label="F", score=1),
                    AnswerOption(value='c', label="N", score=2),
                    AnswerOption(value='d', label="A", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_NPSY_COMP",
            name="AUT_NPSY_COMP Questionnaire",
            description="143 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=71,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_NPSY_COMP score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
