"""
AUT_C1ADOS2 - AUT_C1ADOS2 Questionnaire
=======================================

130 items questionnaire

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


@register_questionnaire("AUT_C1ADOS2")
@dataclass
class AutC1ados2(BaseQuestionnaire):
    """AUT_C1ADOS2 Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_C1ADOS2 questionnaire with all 130 items."""
        
        questions_list = [
            Question(
                id='a21a01',
                text="A1. Niveau général de langage non écholalique",
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
                id='a21a02',
                text="A2. Fréquence des vocalisations dirigées vers les autres",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21a03',
                text="A3. Intonation des vocalisations ou verbalisations",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="8", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21a04',
                text="A4. Echolalie immediate",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="8", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21a05',
                text="A5. Utilisation stéréotypé/Idiosyncrasique de mots ou de phrases",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="8", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21a06',
                text="A6. Utilisation du corps de l'autre",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="8", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21a07',
                text="A7. Pointage",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21a08',
                text="A8. Gestes",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="8", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21b01',
                text="B1. Contact visuel inhabituel",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="2", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21b02',
                text="B2. Sourire social en réponse",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21b03',
                text="B3. Expressions faciales dirigées vers les autres",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21b04',
                text="B4. Intégration du regard et des autres comportements durant les ouvertures sociales",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21b05',
                text="B5. Plaisir partagé dans l'interaction",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21b06',
                text="B6. Réponse à l'appel de son prénom",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21b07',
                text="B7. Demande",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21b08',
                text="B8. Donner",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21b09',
                text="B9. Montrer",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21b10',
                text="B10. Initiation spontanée de l'attention conjointe",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21b11',
                text="B11. Réponse à l'attention conjointe",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21b12',
                text="B12. Qualité des ouvertures sociales",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21b13a',
                text="B13a. Quantité d'ouvertures sociales/Maintien de l'attention: EXAMINATEUR",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="7", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21b13b',
                text="B13b. Quantité d'ouvertures sociales/Maintien de l'attention: PARENT",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="7", score=4),
                    AnswerOption(value='f', label="8", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21b14',
                text="B14. Qualité de la réponse sociale",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21b15',
                text="B15. Niveau d'implication",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21b16',
                text="B16. Qualité générale de la relation",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21c01',
                text="C1. Jeu fonctionnel avec les objets",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21c02',
                text="C2. Imagination/Créativité",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21class',
                text="Classification ADOS-2",
                options=[
                    AnswerOption(value='a', label="Autisme", score=0),
                    AnswerOption(value='b', label="Spectre autistique", score=1),
                    AnswerOption(value='c', label="Hors du spectre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21d01',
                text="D1. Intérêt sensoriel inhabituel pour le matériel de jeu/la personne",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21d02',
                text="D2. Maniérismes des mains et des doigts et autres maniérismes complexes",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21d03',
                text="D3. Comportements d'auto mutilation",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21d04',
                text="D4. Intérêts inhabituellement répétitifs et comportements stéréotypés",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21e01',
                text="E1. Hyperactivité",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="7", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21e02',
                text="E2. Colères, Agression ou Comportement négatif ou perturbateur",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a21e03',
                text="E3. Anxiété",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22a01',
                text="A1. Niveau général de langage non écholalique",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22a02',
                text="A2. Anomalies du langage associées à l'autisme (intonation/volume/rythme/débit",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="7", score=3),
                    AnswerOption(value='e', label="8", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22a03',
                text="A3. Echolalie immediate",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22a04',
                text="A4. Utilisation stéréotypé/Idiosyncrasique de mots ou de phrases",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22a05',
                text="A5. Conversation",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22a06',
                text="A6. Pointage",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22a07',
                text="A7. Gestes descriptifs, conventionnels et instrumentaux ou informatifs",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="8", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22b01',
                text="B1. Contact visuel inhabituel",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="2", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22b02',
                text="B2. Expressions faciales dirigées vers les autres",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22b03',
                text="B3. Plaisir partagé dans l'interaction",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22b04',
                text="B4. Réponse à l'appel de son prénom",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22b05',
                text="B5. Montrer",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22b06',
                text="B6. Initiation spontanée de l'attention conjointe",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22b07',
                text="B7. Réponse à l'attention conjointe",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22b08',
                text="B8. Qualité des ouvertures sociales",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22b09a',
                text="B9a. Quantité d'ouvertures sociales/Maintien de l'attention: EXAMINATEUR",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="7", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22b09b',
                text="B9b. Quantité d'ouvertures sociales/Maintien de l'attention: PARENT",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="7", score=4),
                    AnswerOption(value='f', label="8", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22b10',
                text="B10. Qualité de la réponse sociale",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22b11',
                text="B11. Quantité de communication sociale réciproque",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22b12',
                text="B12. Qualité générale de la relation",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22c01',
                text="C1. Jeu fonctionnel avec des objets",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22c02',
                text="C2. Imagination/Créativité",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22class',
                text="Classification ADOS-2",
                options=[
                    AnswerOption(value='a', label="Autisme", score=0),
                    AnswerOption(value='b', label="Spectre autistique", score=1),
                    AnswerOption(value='c', label="Hors du spectre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22d01',
                text="D1. Intérêt sensoriel inhabituel pour le matériel de jeu/la personne",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22d02',
                text="D2. Maniérismes des mains et des doigts et autres maniérismes complexes",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22d03',
                text="D3. Comportements d'auto mutilation",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22d04',
                text="D4. Intérêts inhabituellement répétitifs et comportements stéréotypés",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22e01',
                text="E1. Hyperactivité",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="7", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22e02',
                text="E2. Colères, Agression ou Comportement négatif ou perturbateur",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a22e03',
                text="E3. Anxiété",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23a01',
                text="A1. Niveau général de langage non écholalique",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23a02',
                text="A2. Anomalies du langage associées à l'autisme (intonation/volume/rythme/débit",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="7", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23a03',
                text="A3. Echolalie immediate",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23a04',
                text="A4. Utilisation stéréotypé/Idiosyncrasique de mots ou de phrases",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23a05',
                text="A5. Offre d'information",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23a06',
                text="A6. Demande d'information",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23a07',
                text="A7. Compte rendu des évènements",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23a08',
                text="A8. Conversation",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23a09',
                text="A9. Gestes descriptifs, conventionnels et instrumentaux ou informatifs",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="8", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23b01',
                text="B1. Contact visuel inhabituel",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="2", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23b02',
                text="B2. Expressions faciales dirigées vers l'examinateur",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23b03',
                text="B3. Production de langage et communications non verbale associées",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="7", score=3),
                    AnswerOption(value='e', label="8", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23b04',
                text="B4. Plaisir partagé dans l'interaction",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23b05',
                text="B5. Empathie/commentaires sur les émotions d'autrui",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23b06',
                text="B6. Compréhension de situation sociales typiques et des relations",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23b07',
                text="B7. Qualité des ouvertures sociales",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23b08',
                text="B8. Quantité d'ouvertures sociales/maintien de l'attention",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="7", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23b09',
                text="B9. Qualité de la réponse sociale",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23b10',
                text="B10. Quantité de communication sociale réciproque",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23b11',
                text="B11. Qualité générale de la relation",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23c01',
                text="C1. Imagination/Créativité",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23class',
                text="Classification ADOS-2",
                options=[
                    AnswerOption(value='a', label="Autisme", score=0),
                    AnswerOption(value='b', label="Spectre autistique", score=1),
                    AnswerOption(value='c', label="Hors du spectre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23d01',
                text="D1. Intérêt sensoriel inhabituel pour le matériel de jeu/la personne",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23d02',
                text="D2. Maniérismes des mains et des doigts et autres maniérismes complexes",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23d03',
                text="D3. Comportements d'auto mutilation",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23d04',
                text="D4. Intérêts excessifs pour des sujets ou objets inhabituels ou fortement spécifiques ou comportements répétitifs",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23d05',
                text="D5. Compulsions ou rituels",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23e01',
                text="E1. Hyperactivité/Agitation",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="7", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23e02',
                text="E2. Colères, Agression ou Comportement négatif ou perturbateur",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a23e03',
                text="E3. Anxiété",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24a01',
                text="A1. Niveau général de langage non écholalique",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24a02',
                text="A2. Anomalies du langage associées à l'autisme (intonation/volume/rythme/débit",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="7", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24a03',
                text="A3. Echolalie immediate",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24a04',
                text="A4. Utilisation stéréotypé/Idiosyncrasique de mots ou de phrases",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24a05',
                text="A5. Offre d'information",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24a06',
                text="A6. Demande d'information",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24a07',
                text="A7. Compte rendu d'évènements",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24a08',
                text="A8. Conversation",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24a09',
                text="A9. Gestes descriptifs, conventionnels et instrumentaux ou informatifs",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="8", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24a10',
                text="A10. Gestes empathiques ou emotionnels",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="8", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24b01',
                text="B1. Contact visuel inhabituel",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="2", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24b02',
                text="B2. Expressions faciales dirigées vers l'examinateur",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24b03',
                text="B3. Production de langage et communications non verbale associées",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="7", score=3),
                    AnswerOption(value='e', label="8", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24b04',
                text="B4. Plaisir partagé dans l'interaction",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24b05',
                text="B5. Communication de ses propres affects",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24b06',
                text="B6. Empathie/commentaires sur les émotions d'autrui",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24b07',
                text="B7. Compréhension de situation sociales typiques et des relations",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24b08',
                text="B8. Responsabilité",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24b09',
                text="B9. Qualité des ouvertures sociales",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24b10',
                text="B10. Quantité d'ouvertures sociales/maintien de l'attention",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="7", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24b11',
                text="B11. Qualité de la réponse sociale",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24b12',
                text="B12. Quantité de communication sociale réciproque",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24b13',
                text="B13. Qualité générale de la relation",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24c01',
                text="C1. Imagination/Créativité",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24class',
                text="Classification ADOS-2",
                options=[
                    AnswerOption(value='a', label="Autisme", score=0),
                    AnswerOption(value='b', label="Spectre autistique", score=1),
                    AnswerOption(value='c', label="Hors du spectre", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24d01',
                text="D1. Intérêt sensoriel inhabituel pour le matériel de jeu/la personne",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24d02',
                text="D2. Maniérismes des mains et des doigts et autres maniérismes complexes",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24d03',
                text="D3. Comportements d'auto mutilation",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24d04',
                text="D4. Intérêts excessifs pour des sujets ou objets inhabituels ou fortement spécifiques ou comportements répétitifs",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24d05',
                text="D5. Compulsions ou rituels",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24e01',
                text="E1. Hyperactivité/Agitation",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="7", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24e02',
                text="E2. Colères, Agression ou Comportement négatif ou perturbateur",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='a24e03',
                text="E3. Anxiété",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='adosnf',
                text="Examen",
                options=[
                    AnswerOption(value='a', label="Fait", score=0),
                    AnswerOption(value='b', label="Non fait", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='modsaisi',
                text="Module ADOS2 ",
                options=[
                    AnswerOption(value='a', label="Module 1", score=0),
                    AnswerOption(value='b', label="Module 2", score=1),
                    AnswerOption(value='c', label="Module 3", score=2),
                    AnswerOption(value='d', label="Module 4", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_C1ADOS2",
            name="AUT_C1ADOS2 Questionnaire",
            description="130 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=65,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_C1ADOS2 score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
