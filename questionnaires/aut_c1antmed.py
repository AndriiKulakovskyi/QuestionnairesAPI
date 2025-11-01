"""
AUT_C1ANTMED - AUT_C1ANTMED Questionnaire
=========================================

100 items questionnaire

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


@register_questionnaire("AUT_C1ANTMED")
@dataclass
class AutC1antmed(BaseQuestionnaire):
    """AUT_C1ANTMED Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_C1ANTMED questionnaire with all 100 items."""
        
        questions_list = [
            Question(
                id='accnat',
                text="Accouchement naturel",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='acqchang',
                text="Changement depuis la dernière visite",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='affecbb',
                text="Affection médicale sérieuse du bébé",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='alc',
                text="Alcool",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='alcdeb',
                text="début d'alcool pendant la grossesse",
                options=[
                    AnswerOption(value='a', label="T1 ", score=0),
                    AnswerOption(value='b', label="T2", score=1),
                    AnswerOption(value='c', label="T3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='anoeeg',
                text="Anomalies EEG sans convulsions ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='antfct',
                text="Trimestre",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='autre',
                text="Autre",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='autredeb',
                text="début de toxique pendant la grossesse",
                options=[
                    AnswerOption(value='a', label="T1 ", score=0),
                    AnswerOption(value='b', label="T2", score=1),
                    AnswerOption(value='c', label="T3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cana',
                text="Cannabis",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='canadeb',
                text="début du cannabis pendant la grossesse",
                options=[
                    AnswerOption(value='a', label="T1 ", score=0),
                    AnswerOption(value='b', label="T2", score=1),
                    AnswerOption(value='c', label="T3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cesa',
                text="Césarienne",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cesapla',
                text="spécifier : cesarienne planifiée",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cesaurg',
                text="En urgence",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cmv',
                text="CMV",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cmvt',
                text="spécifier trimestre",
                options=[
                    AnswerOption(value='a', label="T1 ", score=0),
                    AnswerOption(value='b', label="T2", score=1),
                    AnswerOption(value='c', label="T3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='coca',
                text="Cocaïne",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cocadeb',
                text="début de cocaïne pendant la grossesse",
                options=[
                    AnswerOption(value='a', label="T1 ", score=0),
                    AnswerOption(value='b', label="T2", score=1),
                    AnswerOption(value='c', label="T3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='convfeb',
                text="Convulsions fébriles ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cosang',
                text="Consanguinité des parents du patient",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='crisabs',
                text="Absences",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='crisact',
                text="Crises actuelles",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='crisaton',
                text="Crises atoniques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='crisnc',
                text="Crises non classifiées ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='crispart',
                text="Crises partielles complexes",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='crisstat',
                text="Status epilepticus ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cristoni',
                text="Crises tonico-cloniques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='croia1',
                text="Age",
                options=[
                    AnswerOption(value='0', label="1 mois", score=0),
                    AnswerOption(value='1', label="2 mois", score=1),
                    AnswerOption(value='2', label="3 mois", score=2),
                    AnswerOption(value='3', label="4 mois", score=3),
                    AnswerOption(value='4', label="5 mois", score=4),
                    AnswerOption(value='5', label="6 mois", score=5),
                    AnswerOption(value='6', label="7 mois", score=6),
                    AnswerOption(value='7', label="8 mois", score=7),
                    AnswerOption(value='8', label="9 mois", score=8),
                    AnswerOption(value='9', label="10 mois", score=9),
                    AnswerOption(value='10', label="11 mois", score=10)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='derytmaj',
                text="Décalage du rythme majeur",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='difmotr',
                text="Motricité actuelle / Difficulté actuelle de la motricité",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='esichang',
                text="Changement depuis la dernière visite",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fiv',
                text="Fécondation in vitro",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='forc',
                text="Forceps",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gemel',
                text="Gémellarité",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gemels',
                text="spécifier gemellarité",
                options=[
                    AnswerOption(value='a', label="Monozygote", score=0),
                    AnswerOption(value='b', label="Dizygote", score=1),
                    AnswerOption(value='c', label="Zygotie non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gripa',
                text="Grippe A",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gripat',
                text="spécifier trimestre",
                options=[
                    AnswerOption(value='a', label="T1 ", score=0),
                    AnswerOption(value='b', label="T2", score=1),
                    AnswerOption(value='c', label="T3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gripsais',
                text="Grippe saisonnière",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gripsaist',
                text="spécifier trimestre",
                options=[
                    AnswerOption(value='a', label="T1 ", score=0),
                    AnswerOption(value='b', label="T2", score=1),
                    AnswerOption(value='c', label="T3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gros_cafe',
                text="Prise de café pendant la grossesse?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gros_fol',
                text="Avez vous pris un supplément en acide folique avant et/ou au début de votre grossesse?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gros_fola',
                text="Etait-ce",
                options=[
                    AnswerOption(value='a', label="3 mois précédant la conception", score=0),
                    AnswerOption(value='b', label="Trimestre1", score=1),
                    AnswerOption(value='c', label="Trimestre 2", score=2),
                    AnswerOption(value='d', label="Trimestre 3", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='groschang',
                text="Changement depuis la dernière visite",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hero',
                text="Héroïne",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='herodeb',
                text="début d'héroïne pendant la grossesse",
                options=[
                    AnswerOption(value='a', label="T1 ", score=0),
                    AnswerOption(value='b', label="T2", score=1),
                    AnswerOption(value='c', label="T3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='herp',
                text="Herpès",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='herpt',
                text="spécifier trimestre",
                options=[
                    AnswerOption(value='a', label="T1 ", score=0),
                    AnswerOption(value='b', label="T2", score=1),
                    AnswerOption(value='c', label="T3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hiv',
                text="HIV",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hivt',
                text="spécifier trimestre",
                options=[
                    AnswerOption(value='a', label="T1 ", score=0),
                    AnswerOption(value='b', label="T2", score=1),
                    AnswerOption(value='c', label="T3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hypoton',
                text="Hypotonie",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hypsmaj',
                text="Hypersomnie majeure",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='infaut',
                text="Autres",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='infautt',
                text="spécifier trimestre",
                options=[
                    AnswerOption(value='a', label="T1 ", score=0),
                    AnswerOption(value='b', label="T2", score=1),
                    AnswerOption(value='c', label="T3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='infersco',
                text="Interfèrent-elles avec la réussite scolaire ou la vie courante ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='infevir',
                text="Infection pendant la grossesse",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='injsperm',
                text="Micro-injection intracytoplasmique de spermatozoïde",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='insmaj',
                text="Insomnie majeure",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='langact',
                text="Langage actuel",
                options=[
                    AnswerOption(value='a', label="Pas de langage ou moins de 5 mots", score=0),
                    AnswerOption(value='b', label="Quelques mots ou quelques phrases", score=1),
                    AnswerOption(value='c', label="Langage fonctionnel ", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='langx',
                text="Apparition soudaine d’un langage complexe",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='liste',
                text="Listériose",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='listet',
                text="spécifier trimestre",
                options=[
                    AnswerOption(value='a', label="T1 ", score=0),
                    AnswerOption(value='b', label="T2", score=1),
                    AnswerOption(value='c', label="T3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mednpsy',
                text="spécifier médicaments neuro-psy",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='morute',
                text="Trimestre",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='motrfin',
                text="Trouble de motricité fine",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='motrglob',
                text="Trouble de motricité global ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='neonat',
                text="Hospitalisation en néonatologie ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pathfeta',
                text="Pathologie fœtale pendant la grossesse",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pathfetas',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="Retard de croissance intra-utérin", score=0),
                    AnswerOption(value='b', label="Hypoxie fœtale ", score=1),
                    AnswerOption(value='c', label="Macrosomie fœtale", score=2),
                    AnswerOption(value='d', label="Hypotrophie fœtale", score=3),
                    AnswerOption(value='e', label="Syndrome alcoolique fœtal", score=4),
                    AnswerOption(value='f', label="autre", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pathgro',
                text="Pathologie maternelle liée à la grossesse",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pathgros',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="Diabète gestationnel ", score=0),
                    AnswerOption(value='b', label="Hypertension artérielle gravidique ", score=1),
                    AnswerOption(value='c', label="Rupture prématurée des membranes ", score=2),
                    AnswerOption(value='d', label="MAP", score=3),
                    AnswerOption(value='e', label="Placenta praevia", score=4),
                    AnswerOption(value='f', label="autre", score=5)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pathngro',
                text="Pathologie maternelle non liée à la grossesse et hors",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pointes',
                text="Marche sur la pointe des pieds",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='procmas',
                text="Procréation médicale assistée",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='prov',
                text="Provoqué",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='provpla',
                text="spécifier : Planifié",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='provurg',
                text="En urgence",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='reanim',
                text="Réanimation",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='reeduc',
                text="Y a-t-il eu une évaluation / rééducation par un spécialiste ? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='repponde',
                text="y a t-il eu une répercussion pondérale ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='retlang',
                text="Retard de langage",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='retpsy',
                text="Retard acquisition psychomotrice",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='revnmaj',
                text="Réveils nocturnes majeurs",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rube',
                text="Rubéole",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='rubet',
                text="spécifier trimestre",
                options=[
                    AnswerOption(value='a', label="T1 ", score=0),
                    AnswerOption(value='b', label="T2", score=1),
                    AnswerOption(value='c', label="T3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='saign',
                text="Saignements durant la grossesse ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='saignret',
                text="Retentissement",
                options=[
                    AnswerOption(value='a', label="Léger", score=0),
                    AnswerOption(value='b', label="Modéré ", score=1),
                    AnswerOption(value='c', label="Sévère", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='saigntri',
                text="spécifier trimestre ",
                options=[
                    AnswerOption(value='a', label="T1 ", score=0),
                    AnswerOption(value='b', label="T2", score=1),
                    AnswerOption(value='c', label="T3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='souffet',
                text="Souffrance fœtale",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='souffets',
                text="spécifier souffrance foetale",
                options=[
                    AnswerOption(value='a', label="Anoxie", score=0),
                    AnswerOption(value='b', label="Ictère sévère", score=1),
                    AnswerOption(value='c', label="Hémorragie cérébrale", score=2),
                    AnswerOption(value='d', label="Infection", score=3),
                    AnswerOption(value='e', label="Autre", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tabac',
                text="Tabac",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tabacdeb',
                text="début du tabac pendant la grossesse",
                options=[
                    AnswerOption(value='a', label="T1 ", score=0),
                    AnswerOption(value='b', label="T2", score=1),
                    AnswerOption(value='c', label="T3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tox',
                text="Exposition à des toxiques pendant la grossesse ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toxo',
                text="Toxoplasmose",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='toxot',
                text="spécifier trimestre",
                options=[
                    AnswerOption(value='a', label="T1 ", score=0),
                    AnswerOption(value='b', label="T2", score=1),
                    AnswerOption(value='c', label="T3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tralim',
                text="Trouble de l'alimentation avant l'âge de 1 an",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='trsomm',
                text="Trouble du sommeil avant l'âge de 1 an",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='trtmed',
                text="Exposition à des traitements médicamenteux ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='vaccin',
                text="Vaccin",
                options=[
                    AnswerOption(value='a', label="Vaccin antidiphtérique", score=0),
                    AnswerOption(value='b', label="Vaccin antitétanique", score=1),
                    AnswerOption(value='c', label="Vaccin antipoliomyelitique", score=2),
                    AnswerOption(value='d', label="Vaccin anticoquelucheux", score=3),
                    AnswerOption(value='e', label="Vaccin antituberculeux B.C.G", score=4),
                    AnswerOption(value='f', label="Vaccin antirougeoleux", score=5),
                    AnswerOption(value='g', label="Vaccin antirubéolique", score=6),
                    AnswerOption(value='h', label="Vaccin antivarioliques", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='vacgrip',
                text="Vaccination antigrippale pendant la grossesse ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Non connu", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='vent',
                text="Ventouse",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_C1ANTMED",
            name="AUT_C1ANTMED Questionnaire",
            description="100 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=50,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_C1ANTMED score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
