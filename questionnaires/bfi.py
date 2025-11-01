"""
BFI - BFI Questionnaire
=======================

45 items questionnaire

Source: Extracted from ecedr application
Applications: ecedr
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


@register_questionnaire("BFI")
@dataclass
class Bfi(BaseQuestionnaire):
    """BFI Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize BFI questionnaire with all 45 items."""
        
        questions_list = [
            Question(
                id='bfi1',
                text="1.  est bavard",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi10',
                text="10. s'intéresse à de nombreux sujets",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi11',
                text="11. est plein d’énergie",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi12',
                text="12. commence facilement à se disputer avec les autres",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi13',
                text="13. est fiable dans son travail",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi14',
                text="14. peut être angoissé",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi15',
                text="15. est ingénieux, une grosse tête",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi16',
                text="16. communique beaucoup d'enthousiasme",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi17',
                text="17. est indulgent de nature",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi18',
                text="18. a tendance à être désorganisé",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi19',
                text="19. se tourmente beaucoup",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi2',
                text="2. a tendance à critiquer les autres",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi20',
                text="20. a une grande imagination",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi21',
                text="21. a tendance à être silencieux",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi22',
                text="22. fait généralement confiance aux autres",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi23',
                text="23. a tendance à être paresseux",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi24',
                text="24. est quelqu'un de tempéré, pas facilement troublé",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi25',
                text="25. est inventif",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi26',
                text="26. a une forte personnalité, s'exprime avec assurance",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi27',
                text="27. est parfois dédaigneux, méprisant",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi28',
                text="28. persévère jusqu’à ce que sa tâche soit finie",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi29',
                text="29. peut être lunatique d'humeur changeante",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi3',
                text="3. travaille consciencieusement",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi30',
                text="30. apprécie les activités artistiques et esthétiques",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi31',
                text="31. est quelquefois timide, inhibé",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi32',
                text="32. est prévenant et gentil avec presque tout le monde",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi33',
                text="33. est efficace dans son travail",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi34',
                text="34. reste calme dans les situations angoissantes",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi35',
                text="35. préfère un travail simple et routinier",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi36',
                text="36. est sociable, extraverti",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi37',
                text="37. est parfois impoli avec les autres",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi38',
                text="38. fait des projets et les poursuit",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi39',
                text="39. est facilement anxieux",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi4',
                text="4. est déprimé, cafardeux",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi40',
                text="40. aime réfléchir et jouer avec des idées",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi41',
                text="41. est peu intéressé par tout ce qui est artistique",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi42',
                text="42. aime coopérer avec les autres",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi43',
                text="43. est facilement distrait",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi44',
                text="44. a de bonnes connaissances en art, musique ou en littérature",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi45',
                text="45. cherche des histoires aux autres",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi5',
                text="5. est créatif, plein d'idées originales",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi6',
                text="6. est réservé",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi7',
                text="7. est serviable et n'est pas égoïste avec les autres",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi8',
                text="8. peut être parfois négligent",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='bfi9',
                text="9. est \\",
                options=[
                    AnswerOption(value='a', label="désapprouve fortement", score=0),
                    AnswerOption(value='b', label="désapprouve un peu", score=1),
                    AnswerOption(value='c', label="n’approuve ni ne désapprouve", score=2),
                    AnswerOption(value='d', label="approuve un peu", score=3),
                    AnswerOption(value='e', label="approuve fortement", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="BFI",
            name="BFI Questionnaire",
            description="45 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=22,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute BFI score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
