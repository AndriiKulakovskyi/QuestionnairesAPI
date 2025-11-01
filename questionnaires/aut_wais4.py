"""
AUT_WAIS4 - AUT_WAIS4 Questionnaire
===================================

260 items questionnaire

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


@register_questionnaire("AUT_WAIS4")
@dataclass
class AutWais4(BaseQuestionnaire):
    """AUT_WAIS4 Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_WAIS4 questionnaire with all 260 items."""
        
        questions_list = [
            Question(
                id='wais_arit1',
                text="1. Fleurs (image) (Compte jusqu'à 3)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit10',
                text="10. Yves a 28 livres. Il en vend la moitié à un marchand de livres d'occasion et se débarrasse encore de 9 livres. Combien de livres lui reste-t-il ? (5)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit11',
                text="11. Marie a 35 ans. Luc a 18 ans. Combien d'années Marie a-t-elle de plus que Luc ? (17)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit12',
                text="12. Il y a 25 chewing-gums dans chaque paquet. Combien de chewing-gums y a-t-il dans 8 paquets ? (200)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit13',
                text="13. Si vous avez 18 biscuits et que vous mangez 7 biscuits et demi, combien vous en reste-t-il ? (10,5)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit14',
                text="14. Paul participe à une réunion avec 9 autres personnes qui parlent chacune pendant 5 minutes. Paul parle pendant 2 minutes. Combien de temps, au total, tout le groupe a-t-il parlé ? (47)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit15',
                text="15. Vous avez 7 sacs d'oranges contenant chacun 20 oranges. Vous avez besoin de 500 oranges. Combien d'oranges vous manque-t-il ? (360)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit16',
                text="16. Louis distribue à 8 personnes 4 cartes à chacune. Il lui reste 6 cartes pour demain. Combien de cartes avait-il en tout ? (38)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit17',
                text="17. Line court chaque jour, du lundi au vendredi, pendant 22 minutes. Le samedi, elle court pendant 30 minutes. Pendant combien de temps court-elle en tout ? (140mn ou 2h20)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit18',
                text="18. Pour entrer au cinéma, Claire faut la queue derrière 160 personnes. Elle laisse passer 20 personnes de plus devant elle. Chaque minute, 6 personnes passent l'entrée. Combien de temps faudra-t-il à Claire pour atteindre l'entrée ? (30 mn)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit19',
                text="19. Franck travaille 188 heures en 4 semaines. S'il travaille le même nombre d'heures par semaine, combien d'heures a-t-il travaillé chaque semaine ? (47h)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit2',
                text="2. Pommes (image) (Compte jusqu'à 10)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit20',
                text="20. Louise fait habituellement 60 tours de piste avec son cheval. Aujourd'hui, elle en fait 15% de moins. Combien de tours a-t-elle fait aujourd'hui ? (51)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit21',
                text="21. Si 8 machines peuvent accomplir une tâche en 6 jours, combien de machines faut-il pour accomplir cette tâche en une demi-journée ? (96)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit22',
                text="22. Dans un bureau de poste, 20 000 lettres ont été triées en octobre. En novembre, le nombre de lettres triées a augmenté de 10%. En décembre le nombre de lettres triées a encore augmenté de 5%. Combien de lettres ont-elles été triées en décembre, après ces deux augmentations ? (23100)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit3',
                text="3. Raquettes et balles (image) (6)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit4',
                text="4. Oiseaux et chats (image) (9)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit5',
                text="5. Laisses et chiens (image) (2)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit6',
                text="6. Brice a 4 couvertures. Il en achète 4 de plus. Combien de couvertures a-t-il en tout ? (8)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit7',
                text="7. Pierre a 9 crayons. Il en donne 4 à Jean. Combien de crayons reste-t-il à Pierre ? (5)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit8',
                text="8. Jacques a 4 enfants et 20 jouets. S'il donne le même nombre de jouets à chaque enfant, combien chaque enfant en aura-t-il ? (5)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_arit9',
                text="9. Vous ramassez 10 coquillages le vendredi, 5 coquillages le samedi et 15 coquillages le dimanche. Vous donnez le même nombre de coquillages à Hugo, Yann et Marc. Combien de coquillages donnez-vous à chacun d'eux ? (10)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub1',
                text="1.Dessin",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub10',
                text="10.Dessin",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub11',
                text="11.Dessin",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub12',
                text="12.Dessin",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub13',
                text="13.Dessin",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub14',
                text="14.Dessin",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub2',
                text="2.Dessin",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub3',
                text="3.Dessin",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub4',
                text="4.Dessin",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub5',
                text="5.Dessin",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="4", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub6',
                text="6.Dessin",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="4", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub7',
                text="7.Dessin",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="4", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub8',
                text="8.Dessin",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="4", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_cub9',
                text="9.Dessin",
                options=[
                    AnswerOption(value='a', label="0", score=0)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img1',
                text="1.Table",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img10',
                text="10.Vache",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img11',
                text="11.Barrière",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img12',
                text="12.Arbres",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img13',
                text="13.Armoires",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img14',
                text="14.Karaté",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img15',
                text="15.Chalet",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img16',
                text="16.Promenade",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img17',
                text="17.Flaques",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img18',
                text="18.Chaussures",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img19',
                text="19.Tente",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img2',
                text="2.Visage",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img20',
                text="20.Voiture",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img21',
                text="21.Bibliothèque",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img22',
                text="22.Panier",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img23',
                text="23.Avion",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img24',
                text="24.Gazinière",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img3',
                text="3.Miroir",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img4',
                text="4.Lunettes",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img5',
                text="5.Coureurs",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img6',
                text="6.Couteau",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img7',
                text="7.Cruche",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img8',
                text="8.Roses",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_img9',
                text="9.Gâteau",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info1',
                text="1. Quel jour de la semaine vient juste après lundi?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info10',
                text="10. A quelle température l'eau bout-elle?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info11',
                text="11. En combien de temps la terre fait-elle un tour complet sur elle-même?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info12',
                text="12. Qui a écrit 'Le tour du monde en 80 jours'?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info13',
                text="13. Combien de degrés un angle plat mesure-t-il?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info14',
                text="14. Qui était Marguerite Yourcenar?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info15',
                text="15. Comment appelle-t-on les animaux qui pondent des ?ufs?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info16',
                text="16. Qu'est-ce qui fait que le fer rouille?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info17',
                text="17. Quel est le nom habituellement associé à la théorie de la relativité?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info18',
                text="18. Au cours de quel siècle Molière a-t-il vécu?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info19',
                text="19. Quel canal relie l'Atlantique au Pacifique?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info2',
                text="2. Quelle est la forme d'une balle?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info20',
                text="20. Donnez le nom de trois types de vaisseaux sanguins du corps humain.",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info21',
                text="21. Quelle est l'unité de mesure d'intensité du courant électrique?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info22',
                text="22. Quelle chaîne de montagnes sépare l'Europe de l'Asie?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info23',
                text="23. A quoi sert la poche du kangourou?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info24',
                text="24. A quelle vitesse un avion vole-t-il lorsqu'il passe le mur du son?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info25',
                text="25. Quelle invention a permis le développement des ordinateurs personnels?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info26',
                text="26. Quel est le plus grand organe du corps humain?",
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
                text="3. Qu'est-ce qu'un thermomètre?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info4',
                text="4. Combien y a-t-il de secondes dans une minute?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info5',
                text="5. Quels sont les quatre points cardinaux?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info6',
                text="6. De quoi s'occupe un ophtalmologiste?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info7',
                text="7. A quoi sert l'estomac?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info8',
                text="8. Qui a créé le personnage de Tintin?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_info9',
                text="9. Sur quel continent se trouve l'Égypte?",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat1',
                text="Note pour l'item 1",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat10',
                text="Note pour l'item10",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat11',
                text="Note pour l'item11",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat12',
                text="Note pour l'item12",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat13',
                text="Note pour l'item13",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat14',
                text="Note pour l'item14",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat15',
                text="Note pour l'item15",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat16',
                text="Note pour l'item16",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat17',
                text="Note pour l'item17",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat18',
                text="Note pour l'item18",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat19',
                text="Note pour l'item19",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat2',
                text="Note pour l'item 2",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat20',
                text="Note pour l'item20",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat21',
                text="Note pour l'item21",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat22',
                text="Note pour l'item22",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat23',
                text="Note pour l'item23",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat24',
                text="Note pour l'item24",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat25',
                text="Note pour l'item25",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat26',
                text="Note pour l'item26",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat3',
                text="Note pour l'item 3",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat4',
                text="Note pour l'item 4",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat5',
                text="Note pour l'item 5",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat6',
                text="Note pour l'item 6",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat7',
                text="Note pour l'item 7",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat8',
                text="Note pour l'item 8",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mat9',
                text="Note pour l'item 9",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_1',
                text="1. Note à l'item 1",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_1a',
                text="1. Note à l'essai1(Essai:1-2, rép:1-2)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_1b',
                text="1. Note à l'essai2(Essai:4-2, rép:2-4)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_2',
                text="2. Note à l'item 2",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_2a',
                text="2. Note à l'essai1(Essai:3-1-6, rép:1-3-6)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_2b',
                text="2. Note à l'essai2(Essai:0-9-4, rép:0-4-9)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_3',
                text="3. Note à l'item 3",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_3a',
                text="3. Note à l'essai1(Essai:8-7-9-2, rép:2-7-8-9)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_3b',
                text="3. Note à l'essai2(Essai:4-8-7-1, rép:1-4-7-8)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_4',
                text="4. Note à l'item 4",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_4a',
                text="4. Note à l'essai1(Essai:2-6-9-1-7, rép:1-2-6-7-9 )",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_4b',
                text="4. Note à l'essai2(Essai:3-8-3-5-8, rép:3-3-5-8-8 )",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_5',
                text="5. Note à l'item 5",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_5a',
                text="5. Note à l'essai1(Essai:2-1-7-4-3-6, rép:1-2-3-4-6-7 )",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_5b',
                text="5. Note à l'essai2(Essai:6-2-5-2-3-4, rép:2-2-3-4-5-6 )",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_6',
                text="6. Note à l'item 6",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_6a',
                text="6. Note à l'essai1(Essai:7-5-7-6-8-6-2, rép:2-5-6-6-7-7-8 )",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_6b',
                text="6. Note à l'essai2(Essai:4-8-2-5-4-3-5, rép:2-3-4-4-5-5-8 )",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_7',
                text="7. Note à l'item 7",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_7a',
                text="7. Note à l'essai1(Essai:5-8-7-2-7-5-4-5, rép:2-4-5-5-5-7-7-8 )",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_7b',
                text="7. Note à l'essai2(Essai:9-4-9-7-3-0-8-4, rép:0-3-4-4-7-8-9-9 )",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_8',
                text="8. Note à l'item 8",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_8a',
                text="8. Note à l'essai1(Essai:5-0-1-1-3-2-1-0-5, rép:0-0-1-1-1-2-3-5-5 )",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoc_8b',
                text="8. Note à l'essai2(Essai:2-7-1-4-8-4-2-9-6, rép:1-2-2-4-4-6-7-8-9 )",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_1',
                text="1. Note à l'item 1",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_1a',
                text="1. Note à l'essai 1(9-7)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_1b',
                text="1. Note à l'essai 2(6-3)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_2',
                text="2. 1. Note à l'item 2",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_2a',
                text="2. Note à l'essai 1(5-8-2)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_2b',
                text="2. Note à l'essai 2(6-9-4)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_3',
                text="3 Note à l'item 3",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_3a',
                text="3. Note à l'essai 1(7-2-8-6)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_3b',
                text="3. Note à l'essai 2(6-4-3-9)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_4',
                text="4. Note à l'item 4",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_4a',
                text="4. Note à l'essai 1(4-2-7-3-1)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_4b',
                text="4. Note à l'essai 2(7-5-8-3-6)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_5',
                text="5. Note à l'item 5",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_5a',
                text="Note à l'essai 1(3-9-2-4-8-7)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_5b',
                text="Note à l'essai 2(6-1-9-4-7-3)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_6',
                text="6. Note à l'item 6",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_6a',
                text="6. Note à l'essai 1(4-1-7-9-3-8-6)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_6b',
                text="6. Note à l'essai 2(6-9-1-7-4-2-8)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_7',
                text="7. Note à l'item 7",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_7a',
                text="7. Note à l'essai 1(3-8-2-9-6-1-7-4)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_7b',
                text="7. Note à l'essai 2(5-8-1-3-2-6-4-7)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_8',
                text="8. Note à l'item 8",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_8a',
                text="8. Note à l''essai 1(2-7-5-8-6-3-1-9-4)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcod_8b',
                text="8. Note à l''essai 2(7-1-3-9-4-2-5-6-8)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_1',
                text="1. Note à l'item 1",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_1a',
                text="1. Note à l'essai 1(3-1)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_1b',
                text="1. Note à l'essai 2(2-4)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_2',
                text="2. Note à l'item 2",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_2a',
                text="2. Note à l'essai 1(4-6)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_2b',
                text="2. Note à l'essai 2(5-7)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_3',
                text="3. Note à l'item 3",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_3a',
                text="3. Note à l'essai 1(6-2-9)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_3b',
                text="3. Note à l'essai 2(4-7-5)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_4',
                text="4. Note à l'item 4",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_4a',
                text="4. Note à l'essai 1(8-2-7-9)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_4b',
                text="4. Note à l'essai 2(4-9-6-8)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_5',
                text="5. Note à l'item 5",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_5a',
                text="5. Note à l'essai 1(6-5-8-4-3)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_5b',
                text="5. Note à l'essai 2(1-5-4-8-6)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_6',
                text="6. Note à l'item 6",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_6a',
                text="6. Note à l'essai 1(5-3-7-4-1-8)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_6b',
                text="6. Note à l'essai 2(7-2-4-8-5-6)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_7',
                text="7. Note à l'item 7",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_7a',
                text="7. Note à l'essai 1(8-1-4-9-3-6-2)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_7b',
                text="7. Note à l'essai 2(4-7-3-9-6-2-8)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_8',
                text="8. Note à l'item 8",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_8a',
                text="8. Note à l''essai1(9-4-3-7-6-2-1-8)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_mcoi_8b',
                text="8. Note à l''essai2(7-2-8-1-5-6-4-3)",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl1',
                text="1.Note à l'item 1",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl10',
                text="10.Note à l'item 10",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl11',
                text="11.Note à l'item 11",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl12',
                text="12.Note à l'item 12",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl13',
                text="13.Note à l'item 13",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl14',
                text="14.Note à l'item 14",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl15',
                text="15.Note à l'item 15",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl16',
                text="16.Note à l'item 16",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl17',
                text="17.Note à l'item 17",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl18',
                text="18.Note à l'item 18",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl19',
                text="19.Note à l'item 19",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl2',
                text="2.Note à l'item 2",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl20',
                text="20.Note à l'item 20",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl21',
                text="21.Note à l'item 21",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl22',
                text="22.Note à l'item 22",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl23',
                text="23.Note à l'item 23",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl24',
                text="24.Note à l'item 24",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl25',
                text="25.Note à l'item 25",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl26',
                text="26.Note à l'item 26",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl3',
                text="3.Note à l'item 3",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl4',
                text="4.Note à l'item 4",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl5',
                text="5.Note à l'item 5",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl6',
                text="6.Note à l'item 6",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl7',
                text="7.Note à l'item 7",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl8',
                text="8.Note à l'item 8",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_puzl9',
                text="9.Note à l'item 9",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim1',
                text="1.Framboise - Groseille",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim10',
                text="10.cube - cylindre",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim11',
                text="11.Nez - Langue",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim12',
                text="12.Soie - Laine",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim13',
                text="13.Eolienne - Barrage",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim14',
                text="14.Ephémère - Permanent",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim15',
                text="15.Inondation - Sécheresse",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim16',
                text="16.Sédentaire - Nomade",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim17',
                text="17.Autoriser - Interdire",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim18',
                text="18.Réalité - rêve",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim19',
                text="19.sédentaire-nomade",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim2',
                text="2.Cheval --Tigre",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim3',
                text="3.Carottes - Epinards ",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim4',
                text="4.Jaune - Bleu",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim5',
                text="5.Piano - Tambour",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim6',
                text="6.Poème - Statue",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim7',
                text="7.Bourgeon - Bébé",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim8',
                text="8.Miel - Lait",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_sim9',
                text="9.Nourriture - Carburant",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc1',
                text="1.Livre",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc10',
                text="10.Miroir",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc11',
                text="11.Silence",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc12',
                text="12.Arbitre",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc13',
                text="13.Vigoureux",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc14',
                text="14.Précis",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc15',
                text="15.Evoluer",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc16',
                text="16.Courage",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc17',
                text="17.Copieux",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc18',
                text="18.Initiative",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc19',
                text="19.Compassion",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc2',
                text="2.Avion",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc20',
                text="20.Opaque",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc21',
                text="21.Connivence",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc22',
                text="22.Esquiver",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc24',
                text="24.Réticent",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc25',
                text="25.Solidaire",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc26',
                text="26.Intrépide",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc27',
                text="27.Tangible",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc28',
                text="28.Pragmatique",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc29',
                text="29.Plagier",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc3',
                text="3.Panier",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc30',
                text="30.Fustiger",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc4',
                text="4.Pomme",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc5',
                text="5.Paisible",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc6',
                text="6.Terminer",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc7',
                text="7.Gant",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc8',
                text="8.Colossal",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='wais_voc9',
                text="9.Refuge",
                options=[
                    AnswerOption(value='a', label="0", score=0),
                    AnswerOption(value='b', label="1", score=1),
                    AnswerOption(value='c', label="2", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_WAIS4",
            name="AUT_WAIS4 Questionnaire",
            description="260 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=130,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_WAIS4 score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
