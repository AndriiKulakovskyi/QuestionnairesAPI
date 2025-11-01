"""
AUT_CSHQ - AUT_CSHQ Questionnaire
=================================

87 items questionnaire

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


@register_questionnaire("AUT_CSHQ")
@dataclass
class AutCshq(BaseQuestionnaire):
    """AUT_CSHQ Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_CSHQ questionnaire with all 87 items."""
        
        questions_list = [
            Question(
                id='cshq1',
                text="1.Votre enfant va au lit à la même heure",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq11',
                text="11. Votre enfant est effrayé de dormir dans le noir",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq12',
                text="12. Votre enfant est effrayé de dormir seul",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq13',
                text="13. Votre enfant dort trop peu",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq14',
                text="14. Votre enfant dort trop",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq15',
                text="15. Votre enfant dort la durée qu’il faut",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq16',
                text="16. Votre enfant dort le même nombre d’heures chaque jour",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq17',
                text="17. Votre enfant mouille son lit la nuit",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq18',
                text="18. Votre enfant parle durant la nuit",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq19',
                text="19. Votre enfant bouge sans cesse durant la nuit",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq2',
                text="2. Votre enfant s’endort en 20 min après être allé au lit",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq20',
                text="20. Votre enfant est somnambule durant la nuit",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq22',
                text="22. Votre enfant se plaint de douleurs corporelles durant la nuit. Si oui, lesquelles ?",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq24',
                text="24. Votre enfant ronfle fortement",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq25',
                text="25. Votre enfant semble s’arrêter de respirer durant la nuit",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq26',
                text="26. Votre enfant ronfle et sursaute durant la nuit",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq28',
                text="28. Votre enfant se plaint de problème de sommeil",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq29',
                text="29. Votre enfant se réveille durant la nuit criant, transpirant, inconsolable",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq3',
                text="3. Votre enfant s’endort seul dans son propre lit",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq30',
                text="30. Votre enfant se réveille la nuit, alarmé par un cauchemar",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq31',
                text="31. Votre enfant se réveille une fois durant la nuit",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq32',
                text="32. Votre enfant se réveille plus d’une fois durant la nuit",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq33',
                text="33. Votre enfant retourne se coucher sans aide après un réveil",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq34',
                text="34. Votre enfant se réveille de lui-même",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq35',
                text="35. Votre enfant se réveille avec un réveil matin",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq36',
                text="36. Votre enfant se réveille de mauvaise humeur",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq37',
                text="37. Un adulte ou ses frères/sœurs réveillent votre enfant",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq38',
                text="38. Votre enfant a des difficultés pour sortir du lit le matin",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq39',
                text="39. Votre enfant prend beaucoup de temps pour devenir alerte le matin",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq4',
                text="4. Votre enfant s’endort dans le lit de ses parents ou de ses frères/soeurs",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq40',
                text="40. Votre enfant se lève très tôt le matin",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq41',
                text="41. Votre enfant a un bon appétit le matin",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq42',
                text="42. Votre enfant fait des siestes durant la journée",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq43',
                text="43. Votre enfant s’endort brutalement au milieu d’une activité",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq44',
                text="44. Votre enfant semble fatigué",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq45',
                text="45. Jouait seul",
                options=[
                    AnswerOption(value='a', label="pas endormi", score=0),
                    AnswerOption(value='b', label="très fatigué", score=1),
                    AnswerOption(value='c', label="s’est endormi", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq46',
                text="46. Regardait la TV",
                options=[
                    AnswerOption(value='a', label="pas endormi", score=0),
                    AnswerOption(value='b', label="très fatigué", score=1),
                    AnswerOption(value='c', label="s’est endormi", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq47',
                text="47. Un voyage en voiture",
                options=[
                    AnswerOption(value='a', label="pas endormi", score=0),
                    AnswerOption(value='b', label="très fatigué", score=1),
                    AnswerOption(value='c', label="s’est endormi", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq48',
                text="48. Un repas",
                options=[
                    AnswerOption(value='a', label="pas endormi", score=0),
                    AnswerOption(value='b', label="très fatigué", score=1),
                    AnswerOption(value='c', label="s’est endormi", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq5',
                text="5. Votre enfant s’endort avec des mouvements rythmiques ou de balancements",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq7',
                text="7. Votre enfant a besoin de ses parents dans la pièce pour s’endormir",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq8',
                text="8. Votre enfant est prêt pour aller au lit à l’heure du coucher",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshq9',
                text="9. Votre enfant résiste pour aller au lit à l’heure du coucher",
                options=[
                    AnswerOption(value='a', label="régulièrement", score=0),
                    AnswerOption(value='b', label="quelquefois", score=1),
                    AnswerOption(value='c', label="rarement", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb1',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb10',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb11',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb12',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb13',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb14',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb15',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb16',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb17',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb18',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb19',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb2',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb20',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb21',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb22',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb23',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb24',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb25',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb26',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb27',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb28',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb29',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb3',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb30',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb31',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb32',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb33',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb34',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb35',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb36',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb37',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb38',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb39',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb4',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb40',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb41',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb42',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb43',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb44',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb5',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb6',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb7',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb8',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cshqpb9',
                text="Problème ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="NA", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_CSHQ",
            name="AUT_CSHQ Questionnaire",
            description="87 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=43,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_CSHQ score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
