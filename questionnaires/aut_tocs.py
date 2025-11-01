"""
AUT_TOCS - AUT_TOCS Questionnaire
=================================

69 items questionnaire

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


@register_questionnaire("AUT_TOCS")
@dataclass
class AutTocs(BaseQuestionnaire):
    """AUT_TOCS Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_TOCS questionnaire with all 69 items."""
        
        questions_list = [
            Question(
                id='toc1',
                text="1. Je me douche, me baigne, me lave les dents, me prépare, je fais ma toilette de manière excessive ou ritualisée. Par exemple, les douches, les bains, et autres routines faites dans la salle de bains peuvent durer plusieurs heures. Si la séquence de lavage est interrompue, l’ensemble du processus peut avoir à être recommencé.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc11',
                text="11. Je vérifie des choses liées à des obsessions ou au sujet de mon corps. Par exemple, vous cherchez à être rassuré par vos amis ou vos médecins sur le fait que vous n’avez pas de crise cardiaque ou de cancer. Vous vérifiez régulièrement votre pouls, votre tension, ou votre température. Vous recherchez si vous avez une odeur corporelle particulière, des bleus, vous vous examinez dans la glace à la recherche de particularités laides.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc12',
                text="12. Je re-lis ou réécris des choses. Par exemple, il vous faut des heures pour lire quelques pages d’un livre ou pour écrire une courte lettre parce que vous êtes pris dans un cycle de lecture ou de relecture. Vous pouvez chercher un mot ou une phrase parfaite, ou vous vous inquiétez de ne pas avoir compris quelque chose que vous devez lire, ou avoir des obsessions sur la forme de certaines lettres. Des textes peuvent être écrits, effacés et réécrits jusqu’à ce que le papier en soit usé.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc14',
                text="14. Quelquefois mes actions deviennent exceptionnellement lentes et exagérées.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc15',
                text="15. J’ai des compulsions de comptage. Par exemple, vous pouvez compter les objets comme les jouets, les fenêtres, les tuiles, les livres, les clous d’un mur, ou même les grains de sable d’une plage. Vous pouvez aussi compter quand vous répétez certaines activités comme se laver.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc16',
                text="16. J’ai des compulsions d’ordre ou de rangements. Par exemple, vous pouvez aligner des objets sur un bureau, ou des jouets sur une étagère, ou des livres dans une bibliothèque. Vous pouvez passer des heures à mettre des choses ‘en ordre’, et être très bouleversé si cet ordre est perturbé.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc18',
                text="18. J’ai besoin d’égaliser certaines choses. (Par exemple, en touchant de la même manière les deux côtés du corps, en se laçant ou relaçant les lacets de souliers de chaque pied jusqu’à ce que vous sentiez que la pression est la même.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc19',
                text="19. J’ai des compulsions d’amasser ou de collecter des choses. Par exemple, vous pouvez remplir des pièces de vieux journaux, de billets, de bouteilles, de serviettes de papier, de sacs d’emballage, de bouteilles vides. Vous ne jetez pas ces choses parce que vous en aurez besoin un jour. Vous pouvez aussi ramasser des objets inutilisables dans la rue ou dans les poubelles.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc2',
                text="2. Je dois suivre un emploi du temps ou une routine stricte pour accomplir les activités ordinaires.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc21',
                text="21. J’ai des rituels impliquant le fait de cligner ou de regarder fixement.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc22',
                text="22. J’ai un besoin de dire, de demander ou de confesser des choses. Par exemple, vous pouvez demander aux autres de vous rassurer. Vous pouvez confesser des mauvaises actions que vous n’avez jamais faites. Vous pouvez penser que vous devez dire certaines choses aux autres pour vous sentir mieux.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc23',
                text="23. J’ai un grand besoin d’explorer mon environnement. Peut-être en prenant des risques non nécessaires, ou en faisant des choses inappropriées qui dérangent les autres.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc24',
                text="24. J’ai besoin de toucher, taper ou frotter les choses. Par exemple, vous pouvez vous sentir obligé de toucher des surfaces rugueuses comme le bois, ou des surfaces chaudes comme le four. Vous pouvez aussi vous sentir obligé de toucher légèrement les autres. Vous pouvez aussi vous sentir obligé de toucher un objet comme le téléphone pour qu’un membre de la famille ne tombe pas malade.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc26',
                text="26. Je vais vers des extrêmes pour éviter certaines situations ou choses.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc27',
                text="27. J’ai des conduites alimentaires ritualisées. Par exemple, je dois arranger ma nourriture, mon couteau et ma fourchette d’une certaine manière avant de manger. Je peux avoir à manger selon un strict rituel, ou peux être incapable de manger jusqu’à ce que les aiguilles d’une horloge indiquent une certaine heure.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc28',
                text="28. J’ai des comportements superstitieux. Par exemple, vous ne pouvez pas prendre un bus ou un train si son numéro porte malchance comme le ‘13’. Vous ne pouvez pas quitter la maison le treizième jour du mois. Vous pouvez jeter des vêtements que vous avez portés un jour où quelque chose de désagréable est arrivé.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc29',
                text="29. J’ai des pensées sottes comme par exemple que je pourrais influencer la survenue de certains évènements si je faisais certaines choses. Même si je sais que ces pensées ne sont pas réellement vraies, je ne peux leur résister. Merci d’écrire un exemple ",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc3',
                text="3. Je dois faire des choses de la même manière à chaque fois. Par exemple, suivre un rituel au moment du coucher ou des rituels pour se laver ou s’habiller.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc30',
                text="30. J’ai fait des choses choquantes, même si je ne voulais pas les faire.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc31',
                text="31. J’ai soudainement fait des choses risquées, même si je ne le voulais pas.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc32',
                text="32. J’ai détruit des choses, même si je ne voulais pas.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc33',
                text="33. J’ai blessé quelqu’un même si je ne le voulais pas.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc34',
                text="34. Je suis excessivement conscient des sensations provenant des différentes parties de mon corps et même quand je pense à autre chose.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc35',
                text="35. J’ai sciemment fait des choses pour me blesser.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc36',
                text="36. Je m’arrache les cheveux. Par exemple, je peux m’arracher les cheveux de mon cuir chevelu, de mes sourcils, de mes cils ou de l’aire pubienne. Vous pouvez utiliser vos doigts ou une pince à épiler pour vous arracher les cheveux. Vous pouvez avoir en conséquence des endroits sans cheveux qui peuvent justifier le port de perruque, ou vous arracher totalement les sourcils ou les cils.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc37',
                text="37. J’ai peur de me faire du mal. Par exemple, peur de manger avec un couteau ou une fourchette, peur de poser des objets pointus, peur de marcher près des fenêtres en verre.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc38',
                text="38. J’ai peur de faire du mal aux autres. Par exemple, peur d’empoisonner la nourriture d’autrui, peur de faire du mal à des bébés, peur de pousser quelqu’un en face d’un train, peur de blesser les sentiments de quelqu’un, peur d’être responsable en ne portant pas assistance lors des catastrophes imaginées, peur de faire du mal en donnant des mauvais conseils.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc39',
                text="39. J’ai des images violentes ou horribles à l’esprit. Par exemple, des images de corps disloqués, de feux, d’accidents de voiture, d’images dégoûtantes.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc40',
                text="40. J’ai peur de laisser échapper des obscénités. Par exemple, peur de crier des obscénités dans des lieux publics comme une église, peur d’écrire des obscénités.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc41',
                text="41. J’ai peur de faire des choses embarrassantes. Par exemple, peur d’avoir l’air idiot dans une situation sociale.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc43',
                text="43. J’ai peur de voler des objets. Par exemple peur de voler à l’étalage.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc44',
                text="44. J’ai peur de blesser les autres en n’étant pas assez prudent. Par exemple, peur de causer un accident sans s’en rendre compte.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc46',
                text="46. J’ai de fortes envies de faire des choses soudaines et dangereuses, comme courir dans la rue, sauter dans un bus ou tourner la roue de sa bicyclette de manière dangereuse.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc47',
                text="47. J’ai eu de fortes envies de faire des choses destructrices de manière déraisonnable, comme de déchirer des vêtements ou de casser un verre.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc48',
                text="48. J’ai eu de fortes envies de me faire du mal. Par exemple, toucher des choses chaudes, ou se mettre un tournevis entre les dents et tourner.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc49',
                text="49. J’ai eu de fortes envies de me blesser ou de blesser les autres, comme pincer ou frapper les autres.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc5',
                text="5. Je fais des choses pour prévenir ou supprimer tout contact avec des contaminants. Par exemple, je peux avoir à demander aux membres de ma famille d’enlever les insecticides, le vernis, les médicaments du cabinet de toilette, ou la litière du chat. Si vous ne pouvez éviter ces choses, vous pouvez avoir à porter des gants.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc50',
                text="50. J’ai eu de fortes envies déraisonnables d’offenser les autres. Par exemple, crier dans une église, ou insulter les autres.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc52',
                text="52. Je m’inquiète de la saleté et des microbes. Par exemple, attraper des microbes en s’asseyant sur certaines chaises, en se serrant la main, en touchant les poignées de portes.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc54',
                text="54. Je suis excessivement préoccupé par les animaux ou les insectes. Par exemple peur d’être contaminé en touchant un chien, un chat ou d’autres animaux.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc55',
                text="55. Je suis excessivement préoccupé par les substances collantes ou les résidus. Par exemple, peur des rubans adhésifs et d’autres substances collantes qui peuvent coincer des substances contaminantes.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc57',
                text="57. J’ai des pensées, images ou impulsions sexuelles interdites ou bouleversantes. Par exemple, des pensées non désirées concernant les étrangers, la famille ou les amis.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc58',
                text="58. J’ai des obsessions concernant le fait d’amasser ou d’économiser des choses. Par exemple, je m’inquiétude de jeter des choses importantes car je pourrais en avoir besoin plus tard ou forte envie de collecter des choses inutiles.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc59',
                text="59. Je suis préoccupé par des pensées inquiétantes concernant Dieu, les enseignements religieux ou les croyances. Par exemple, je m’inquiète d’avoir des pensées blasphématoires, d’avoir dit des choses sacrilèges ou d’être puni pour ces choses. Un autre exemple serait d’avoir pensé que Dieu est un idiot.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc6',
                text="6. Je vérifie que je ne vais pas blesser les autres. Par exemple, en vérifiant que je n’ai pas blessé quelqu’un sans le savoir. Je peux demander aux autres de me rassurer sur le fait que je ne les ai pas blessés.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc61',
                text="61. J’ai des obsessions au sujet de l’exactitude. Par exemple, je m’inquiète à propos de l’alignement exact des journaux ou des livres, au sujet des calculs qui doivent être parfaits ou de l’écriture manuelle qui doit être parfaite.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc62',
                text="62. J’ai des obsessions sur la symétrie. Par exemple, des animaux en peluche, des petites voitures, des camions, blocs, etc. doivent être précisément symétriques.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc63',
                text="63. Je dois réfléchir et re-réfléchir sur la plus insignifiante des décisions.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc64',
                text="64. Je pense souvent à aligner des choses. Par exemple, je pense que tous les objets comme des outils, ou des ustensiles ou des choses sur une étagère doivent être en ligne, tous les vêtements en série coordonnés par couleurs, ou arrangés dans un ordre spécifique.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc65',
                text="65. J’ai des pensées déraisonnables, sottes sur le fait que je peux influencer le dénouement d’un événement donné si j’agis d’une certaine manière.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc66',
                text="66. Je passe mon temps à avoir des images ou des pensées agréables sur le dénouement d’un événement donné si j’agis d’une certaine manière.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc67',
                text="67. Je pense que je dois égaliser les choses. Par exemple, je pense que chaque chose doit être identique de chaque côté de son corps, comme le fait d’effleurer l’encadrement de la porte avec l’épaule gauche et le besoin d’égaliser les choses en revenant et en effleurant encore l’encadrement de la porte avec l’épaule droite.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc68',
                text="68. J’ai l’impression que je dois connaître ou me souvenir de certaines choses. Par exemple, je dois me rappeler de choses insignifiantes comme les numéros de plaque d’immatriculation, les slogans de tee-shirts ou les autocollants des pare-chocs.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc69',
                text="69. J’ai peur de dire certaines choses. Par exemple, peur de dire certains mots à cause de peurs superstitieuses, peur de dire ‘treize’, peur de dire quelque chose qui peut manquer de respect à l’égard de quelqu’un de décédé.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc7',
                text="7. Je vérifie que je ne me blesse pas ou que je ne vais pas me blesser. Par exemple, en recherchant des blessures ou une trace de saignement après avoir porté des objets pointus ou cassables. Vous pouvez fréquemment demander aux autres de vous rassurer sur le fait que vous ne vous êtes pas blessé",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc70',
                text="70. J’ai peur de ne pas dire la chose exacte. Par exemple, peur d’avoir dit une chose fausse, peur de ne pas utiliser le mot parfait.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc71',
                text="71. Je n’arrive pas à expliquer quelque chose correctement alors que j’avais planifié auparavant exactement ce que vous vouliez dire.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc72',
                text="72. J’ai peur de perdre des choses. Par exemple, peur de perdre un colifichet, ou des objets de peu d’importance comme un bout de papier.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc74',
                text="74. Des sons intrusifs, sans aucun sens, des mots ou de la musique viennent à l’esprit. Par exemple, entendre des mots, des chants ou de la musique dans votre tête que l’on ne peut arrêter.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc75',
                text="75. Je suis ennuyé par certains bruits ou sons. Par exemple, être préoccupé par des sons forts de cloches ou des voix d’une autre pièce qui empêchent de dormir.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc76',
                text="76. J’ai des chiffres qui portent chance ou malheur. Par exemple, inquiétude au sujet de chiffres communs comme treize, ou avoir à faire centaines actions un certain nombre de fois qui porte chance, ou encore avoir à commencer une activité seulement à certaine heure de la journée qui porte chance.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc77',
                text="77. J’ai des couleurs qui ont une certaine signification. Par exemple, le noir peut être associé à la mort, le rouge peut être associé au sang et aux blessures. Vous pouvez éviter d’utiliser des objets ayant certaines couleurs.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc78',
                text="78. J’ai des peurs superstitieuses. Par exemple, peur de passer à côté d’un cimetière, d’un corbillard, d’un chat noir, passer en dessous d’un échelle, peur des présages associés à la mort.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc79',
                text="79. Je suis préoccupé par la mort ou la maladie. Par exemple, peur d’avoir une maladie comme un cancer, une maladie cardiaque, le SIDA, malgré toute tentative de réassurance.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc8',
                text="8. Je vérifie que rien de terrible n’est arrivé ou ne va arriver. Par exemple, vous pouvez écouter la radio ou la télévision à la recherche de nouvelles au sujet de catastrophes que vous avez causées. Vous pouvez demander aux autres de vous rassurer.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc80',
                text="80. Je suis excessivement préoccupé par une partie de mon corps ou par son aspect extérieur. Par exemple, vous craignez que votre visage, vos oreilles, votre nez, vos yeux, ou d’autres parties de votre corps soient hideusement laides malgré les tentatives de réassurances.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toc9',
                text="9. Je vérifie que je n’ai pas fait d’erreurs. Par exemple, vérifications répétées alors que vous lisez, écrivez, ou faites des calculs simples pour s’assurer que vous n’avez pas fait d’erreurs. Vous ne pouvez pas être sûr que vous n’avez pas fait d’erreurs.",
                options=[
                    AnswerOption(value='a', label="Jamais", score=0),
                    AnswerOption(value='b', label="Déjà", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tocdiag',
                text="Est-ce que vous concernant, on a évoqué le diagnostic de Trouble Obsessionnel Compulsif ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toctt',
                text="Est-ce que vous avez déjà reçu un traitement médicamenteux pour le Trouble Obsessionnel Compulsif ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_TOCS",
            name="AUT_TOCS Questionnaire",
            description="69 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=34,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_TOCS score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
