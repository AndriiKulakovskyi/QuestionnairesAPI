"""
AUT_EMPAT - AUT_EMPAT Questionnaire
===================================

60 items questionnaire

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


@register_questionnaire("AUT_EMPAT")
@dataclass
class AutEmpat(BaseQuestionnaire):
    """AUT_EMPAT Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_EMPAT questionnaire with all 60 items."""
        
        questions_list = [
            Question(
                id='empat1',
                text="1. Je peux facilement dire si quelqu'un veut engager une conversation avec moi",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat10',
                text="10. Les gens me disent souvent que j’affirme trop mes opinions lors de discussions",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat11',
                text="11. Ca ne me tracasse pas trop si je suis en retard à un rendez-vous avec un ami",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat12',
                text="12. Parce que les amitiés et les rapports sociaux sont trop difficiles je tends à les éviter",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat13',
                text="13. Je ne violerai jamais une loi, si mineure soit elle",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat14',
                text="14. Je trouve souvent difficile de juger si quelque chose est grossier ou poli",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat15',
                text="15. Dans une conversation, je tends à me concentrer sur mes propres pensées plutôt que sur ce que mon interlocuteur pourrait penser",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat16',
                text="16. Je préfère les farces aux jeux de mots",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat17',
                text="17. Je vis la vie au jour le jour plutôt qu’en me projetant dans l’avenir",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat18',
                text="18. Quand j’étais enfant, j'aimais couper des vers de terre pour voir ce qui se passait",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat19',
                text="19. Je comprends si quelqu'un dit quelque chose mais veut en dire une autre",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat2',
                text="2. Je préfère les animaux aux humains",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat20',
                text="20. Je tends à avoir des opinions très fortes au sujet de la moralité",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat21',
                text="21. Il m’est souvent difficile de savoir pourquoi certaines choses dérangent tant les autres personnes",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat22',
                text="22. Je trouve facile de me mettre dans la peau de quelqu'un d'autre",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat23',
                text="23. Je pense que les bonnes manières sont les choses les plus importantes que les parents peuvent enseigner à leurs enfants ",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat24',
                text="24. J’aime faire des choses à l’improviste ",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat25',
                text="25. J’arrive facilement à prédire ce que les gens vont ressentir",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat26',
                text="26. Je repère rapidement dans un groupe une personne se sent mal à l’aise",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat27',
                text="27. Si je dis quelque chose qui offense quelqu’un, je me dis que c’est son problème pas le mien",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat28',
                text="28. Si quelqu’un me demande si j’aime sa coupe de cheveux, je lui réponds franchement même si c’est pour lui dire que je ne l’aime pas",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat29',
                text="29. Je ne peux pas toujours comprendre pourquoi une personne s’est sentie offensée par une remarque",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat3',
                text="3. J'essaie de suivre les tendances actuelles et la mode",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat30',
                text="30. Les gens me disent souvent que je suis très imprévisible",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat31',
                text="31. J’aime être le centre de l’attention quelque soit la situation",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat32',
                text="32. Voir les personnes pleurer ne me dérange pas vraiment",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat33',
                text="33. J’aime avoir des discussions au sujet de la politique",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat34',
                text="34. Je suis très brusque, ce que certains pourraient prendre pour de l’impolitesse, bien que ce ne soit pas intentionnel de ma part",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat35',
                text="35. Je n’ai pas tendance à trouver les situations sociales compliquées",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat36',
                text="36. On me dit souvent que je suis bon pour deviner ce que les gens ressentent ou pensent",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat37',
                text="37. Quand je parle avec les gens, j’ai tendance à parler plus de leur expérience personnelle que de la mienne",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat38',
                text="38. Ça me bouleverse de voir souffrir un animal",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat39',
                text="39. Je suis capable de prendre des décisions sans être influencé par les sentiments d’autrui",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat4',
                text="4. Je trouve difficile d'expliquer à d'autres des choses que je comprends facilement quand ils ne le comprennent pas du premier coup",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat40',
                text="40. Je ne peux pas me détendre tant que je n’ai pas fait tout ce que j’avais projeté de faire dans la journée",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat41',
                text="41. Je peux facilement dire si quelqu’un est intéressé ou ennuyé par ce que je suis en train de dire",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat42',
                text="42. Je suis bouleversé lorsque je vois des gens souffrir aux informations à la télévision",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat43',
                text="43. Habituellement mes amis se confient à moi car ils disent que je suis très compréhensif",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat44',
                text="44. Je peux sentir si je dérange même si on ne me le dit pas",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat45',
                text="45. Je commence souvent de nouveaux passe-temps, mais je m’en lasse rapidement et je passe à autre chose",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat46',
                text="46. Les gens me disent que je vais trop loin dans mes taquineries",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat47',
                text="47. Je serais trop nerveux pour aller sur de grandes montagnes russes",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat48',
                text="48. Certains disent souvent que je suis insensible bien que je ne sache pas toujours pourquoi",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat49',
                text="49. Si je vois un étranger dans un groupe, je pense que c’est au groupe de faire un effort pour qu’il se joigne à eux",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat5',
                text="5. Je rêve la plupart des nuits",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat50',
                text="50. Je reste habituellement détaché émotionnellement lorsque je regarde film",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat51',
                text="51. J’aime être très organisé au quotidien et je fais souvent une liste de choses que j’ai à faire",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat52',
                text="52. Je peux facilement et intuitivement percevoir ce que quelqu’un ressent",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat53',
                text="53. Je n’aime pas prendre de risque",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat54',
                text="54. Je peux aisément comprendre ce dont une autre personne a envie de parler",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat55',
                text="55. Je peux dire si quelqu’un masque ses réelles émotions",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat56',
                text="56. Avant de prendre une décision, je pèse toujours le pour et le contre",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat57',
                text="57. Je ne sais pas comment fonctionnent les règles des situations sociales",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat58',
                text="58. Je suis bon pour deviner ce que quelqu’un veut faire ",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat59',
                text="59. J’ai tendance me sentir concerné lorsque mes amis ont des problèmes",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat6',
                text="6. J’ai vraiment plaisir à prendre soin des autres",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat60',
                text="60. Je peux habituellement apprécier le point de vue d’autrui, si je ne suis pas d’accord",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat7',
                text="7. J’essaie de résoudre par moi-même mes problèmes plutôt que d’en discuter avec d’autres",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat8',
                text="8. J'ai du mal à savoir quoi faire dans une situation sociale",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='empat9',
                text="9. Je suis au meilleur de moi-même le matin",
                options=[
                    AnswerOption(value='a', label="Fortement d’accord", score=0),
                    AnswerOption(value='b', label="Légèrement d’accord", score=1),
                    AnswerOption(value='c', label="Légèrement en désaccord", score=2),
                    AnswerOption(value='d', label="Fortement en désaccord", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_EMPAT",
            name="AUT_EMPAT Questionnaire",
            description="60 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=30,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_EMPAT score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
