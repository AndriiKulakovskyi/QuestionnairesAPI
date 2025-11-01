"""
STORI - STORI Questionnaire
===========================

50 items questionnaire

Source: Extracted from eschizo application
Applications: eschizo
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


@register_questionnaire("STORI")
@dataclass
class Stori(BaseQuestionnaire):
    """STORI Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize STORI questionnaire with all 50 items."""
        
        questions_list = [
            Question(
                id='radhtml_stori1',
                text="1. Je ne pense pas que les gens qui ont une maladie psychique puissent aller mieux.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori10',
                text="10. Ma vie est vraiment bonne maintenant et le futur s'annonce lumineux",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori11',
                text="11. Je me sens actuellement comme si je n'étais qu'une personne malade.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori12',
                text="12. Parce que les autres ont confiance en moi, je commence tout juste à penser que peut-être je peux aller mieux",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori13',
                text="13. Je commence seulement à réaliser que la maladie ne change pas qui je suis en tant que personne",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori14',
                text="14. Je commence actuellement à accepter la maladie comme une partie du tout qui fait ma personne",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori15',
                text="15. Je suis heureux d'être la personne que je suis",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori16',
                text="16. J'ai l'impression de ne plus savoir qui je suis",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori17',
                text="17. J'ai récemment commencé à reconnaître qu'une partie de moi n'est pas affectée par la maladie",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori18',
                text="18. Je commence juste à réaliser que je peux toujours être une personne de valeur",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori19',
                text="19. J'apprend de nouvelles choses sur moi-même alors que je travaille à mon rétablissement",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori2',
                text="2. J'ai seulement récemment découvert que les gens avec une maladie psychique peuvent aller mieux.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori20',
                text="20. Je pense que le fait d'avoir travaillé pour dépasser la maladie a fait de moi une personne meilleure",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori21',
                text="21. Je ne serai jamais la personne que je pensais que je serais.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori22',
                text="22. J'ai tout juste commencé à accepter la maladie comme une partie de ma vie avec laquelle je vais devoir apprendre à vivre",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori23',
                text="23. Je commence à reconnaître où sont mes forces et mes faiblesses",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori24',
                text="24. Je commence à sentir que j'apporte une contribution de valeur à la vie",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori25',
                text="25. J'accomplis des choses qui valent la peine et qui sont satisfaisantes dans ma vie",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori26',
                text="26. Je suis en colère que cela me soit arrivé à moi.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori27',
                text="27. Je commence tout juste à me demander si des choses positives pourraient ressortir de ce qui m'arrive.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori28',
                text="28. Je commence à réfléchir à quelles sont mes qualités particulières.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori29',
                text="29. En devant faire face à la maladie, j'apprends beaucoup au sujet de la vie.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori3',
                text="3. Je commence à apprendre comment je peux faire des choses pour moi afin d'aller mieux.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori30',
                text="30. En surmontant la maladie, j'ai acquis de nouvelles valeurs dans la vie.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori31',
                text="31. Ma vie me semble totalement inutile actuellement.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori32',
                text="32. Je commence tout juste à penser que je peux peut être faire quelque chose de ma vie.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori33',
                text="33. J'essaie de penser à des moyens d'apporter une contribution dans la vie.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori34',
                text="34. Je travaille ces jours sur des choses de la vie qui sont personnellement importantes pour moi.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori35',
                text="35. J'ai des projets importants qui me donnent une raison d'être.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori36',
                text="36. Je ne peux rien faire à propos de ma situation.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori37',
                text="37. Je commence à penser que je pourrais faire quelque chose pour m'aider.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori38',
                text="38. Je commence à me sentir plus confiant au sujet d'apprendre à vivre avec la maladie.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori39',
                text="39. Il y a parfois des revers mais je ne laisse pas tomber.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori4',
                text="4. Je travaille dur pour rester bien et cela en vaudra la peine sur le long terme.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori40',
                text="40. Je me réjouis de relever de nouveaux défis dans la vie.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori41',
                text="41. Les autres savent mieux que moi ce qui est bon pour moi.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori42',
                text="42. J'aimerais commencer à apprendre à m'occuper de moi correctement.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori43',
                text="43. Je commence à en apprendre davantage sur la maladie psychique et sur comment je peux m'aider moi-même.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori44',
                text="44. Je me sens maintenant raisonnablement confiant en ce qui concerne la gestion de la maladie.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori45',
                text="45. Maintenant, je peux bien gérer la maladie.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori46',
                text="46. Il ne me semble pas que j'aie actuellement un quelconque contrôle sur ma vie.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori47',
                text="47. J'aimerais commencer à apprendre à gérer la maladie.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori48',
                text="48. Je commence seulement à travailler pour remettre ma vie sur les rails.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori49',
                text="49. Je commence à me sentir responsable de ma propre vie.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori5',
                text="5. J'ai maintenant un sentiment de « paix intérieure » au sujet de la vie avec la maladie",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori50',
                text="50. Je suis aux commandes de ma propre vie.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori6',
                text="6. Je sens que ma vie à été ruinée par cette maladie.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori7',
                text="7. Je commence seulement à réaliser que ma vie n'a pas à être affreuse pour toujours.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori8',
                text="8. J'ai récemment commencé à apprendre des gens qui vivent bien malgré une sérieuse maladie.",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='radhtml_stori9',
                text="9. Je commence à être raisonnablement confiant à propos de remettre ma vie sur les rails",
                options=[
                    AnswerOption(value='a', label="0.pas du tout vrai actuellement", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2),
                    AnswerOption(value='d', label="3", score=3),
                    AnswerOption(value='e', label="4", score=4),
                    AnswerOption(value='f', label="5.complètement vrai actuellement", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="STORI",
            name="STORI Questionnaire",
            description="50 items questionnaire",
            pathology_domain=PathologyDomain.SCHIZOPHRENIA,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=25,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute STORI score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
