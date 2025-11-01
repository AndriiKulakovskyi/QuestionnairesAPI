"""
AUT_MEDECO2 - AUT_MEDECO2 Questionnaire
=======================================

71 items questionnaire

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


@register_questionnaire("AUT_MEDECO2")
@dataclass
class AutMedeco2(BaseQuestionnaire):
    """AUT_MEDECO2 Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize AUT_MEDECO2 questionnaire with all 71 items."""
        
        questions_list = [
            Question(
                id='??',
                text="Indiquez votre type de logement principal",
                options=[
                    AnswerOption(value='a', label="Personnel", score=0),
                    AnswerOption(value='b', label="Familial", score=1),
                    AnswerOption(value='c', label="Chez un tiers", score=2),
                    AnswerOption(value='d', label="Chez un tiers", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='aidemep',
                text="Aides mises en place (PMI, TISF?)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ce',
                text="Cap Emploi",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='chambre',
                text="L'enfant a-t-il une chambre individuelle",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cons_aut_lieu1',
                text="Autre",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cons_aut_lieu2',
                text="Autre",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='cpo',
                text="Centre de Pré-Orientation (CPO)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='crpro',
                text="Centre de Rééducation Professionnelle (CRP)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='demenag',
                text="Avez-vous déménagé pour vous rapprocher des lieux de prise en charge de votre enfant ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='dsm4s',
                text="Est-ce que d'autre(s) enfant(s) de la fratrie a/ont reçu un diagnostic DSM IV / V ou une autre pathologie médicale neurologique ou génétique? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ea',
                text="Entreprises Adaptées",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ergo_lieu1',
                text="un.e ergothérapeute (suivi individuel)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ergo_lieu2',
                text="un.e ergothérapeute (suivi individuel)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='esat',
                text="Etablissements et Services d'Aide par le Travail (ESAT)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='exam',
                text="Avez-vous réalisé pour votre enfant des examens complémentaires/biologiques (IRM, EEG, audiogramme, prise de sang?)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fratgr',
                text="Est-ce qu'un ou des frère(s)/soeur(s) participe(nt) à un Groupe fratrie ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='garde',
                text="Mode de garde ",
                options=[
                    AnswerOption(value='a', label="Garde totale", score=0),
                    AnswerOption(value='b', label="Garde Alternée", score=1),
                    AnswerOption(value='c', label="Droits de visite", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='habitat',
                text="Type d'habitation",
                options=[
                    AnswerOption(value='a', label="appartement", score=0),
                    AnswerOption(value='b', label="maison", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hav_child',
                text="Avez-vous des enfants ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hooccur_avq1',
                text="Etes-vous aidés par un proche pour la réalisation des AVQ (tâches ménagères, tâches administratives, déplacement, repas, hygiène et gestion des ressources?.) ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hooccur_avq2',
                text="Etes-vous aidé par un service à la personne pour la réalisation des AVQ ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hooccur_groupe',
                text="Est-ce que vos proches participent à un groupe ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hoocur_arret_travail',
                text="A-t-il/elle été arrêté(e) au cours de ces contrats de travail (hors semaines d'hospitalisations)? ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hoterm_pec',
                text="pour quel type de prise en charge",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hsoc_lieu1',
                text="des professionnel.le.s animant un groupe d'habiletés sociales",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='hsoc_lieu2',
                text="des professionnel.le.s animant un groupe d'habiletés sociales",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='interv_lieu1',
                text="un.e intervenant.e à domicile (méthode ABA,TEACCH...)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='interv_lieu2',
                text="un.e intervenant.e à domicile (méthode ABA, TEACCH...)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='jardin',
                text="Présence d'un jardin",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='jobclas',
                text="Le type de contrat",
                options=[
                    AnswerOption(value='a', label="à temps plein", score=0),
                    AnswerOption(value='b', label="à temps partiel", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lieu_exam',
                text="Réalisé",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lieu_fratgr',
                text="et groupe réalisé",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='lieu_groupe',
                text="Groupe réalisé",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='loisi01',
                text="Votre enfant a-t-il accès à des activités extra-scolaires ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='loisi01b',
                text="Activité(s) pratiquée(s)",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='loisi01c',
                text="Si oui, est-ce via des associations promouvant l'inclusion sociale des enfants avec TSA ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='loisi02',
                text="Votre enfant participe-t-il à des camps/colonies de vacances ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='loisi02a',
                text="Si oui, est-ce via des associations promouvant l'inclusion sociale des enfants avec TSA ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='medg',
                text="Avez-vous consulté durant les 12 derniers mois chez un.e médecin généraliste/pédiatre",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='medp_lieu1',
                text="un.e médecin pédopsychiatre / neuropédiatre",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='medp_lieu2',
                text="un.e médecin pédopsychiatre / neuropédiatre",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='ml',
                text="Mission Locale",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='orthoph_lieu1',
                text="un.e orthophoniste (suivi individuel)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='orthoph_lieu2',
                text="un.e orthophoniste (suivi individuel)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='orthopt_lieu1',
                text="un.e orthoptiste",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='orthopt_lieu2',
                text="un.e orthoptiste",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pe',
                text="Pôle Emploi",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pec',
                text="Avez-vous eu des difficultés pour trouver une prise en charge disponible ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pec5y',
                text="Est-ce que il y a eu une prise en charge comportementale intensive avant l'âge de 5 ans?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pecs',
                text="L'enfant utilise-t-il le PECS / MAKATON ou un système de communication adapté ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psychom_lieu1',
                text="un.e psychomotricien.ne (suivi individuel)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psychom_lieu2',
                text="un.e psychomotricien.ne (suivi individuel)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psyg_lieu1',
                text="un.e psychologue (suivi individuel)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psyg_lieu2',
                text="un.e psychologue (suivi individuel)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psyg_type_lieu1',
                text="Réalisé",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6", score=5),
                    AnswerOption(value='g', label="7", score=6),
                    AnswerOption(value='h', label="8", score=7),
                    AnswerOption(value='i', label="9", score=8)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psyg_type_lieu2',
                text="Précisez, si vous connaissez le type d'approche",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6", score=5),
                    AnswerOption(value='g', label="7", score=6),
                    AnswerOption(value='h', label="8", score=7),
                    AnswerOption(value='i', label="9", score=8)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='psysco',
                text="Avez-vous consulté pour votre enfant durant les 12 derniers mois auprès d'un.e psychologue scolaire",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='saltyp',
                text="Indiquez les sources de revenus et ressources que vous avez",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3),
                    AnswerOption(value='e', label="5", score=4),
                    AnswerOption(value='f', label="6", score=5),
                    AnswerOption(value='g', label="7", score=6),
                    AnswerOption(value='h', label="8", score=7)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='saltypa',
                text="Précisez les prestations",
                options=[
                    AnswerOption(value='0', label="1", score=0),
                    AnswerOption(value='1', label="2", score=1),
                    AnswerOption(value='2', label="3", score=2),
                    AnswerOption(value='3', label="4", score=3),
                    AnswerOption(value='4', label="5", score=4),
                    AnswerOption(value='5', label="6", score=5),
                    AnswerOption(value='6', label="7", score=6),
                    AnswerOption(value='7', label="8", score=7),
                    AnswerOption(value='8', label="9", score=8),
                    AnswerOption(value='9', label="10", score=9),
                    AnswerOption(value='10', label="11", score=10),
                    AnswerOption(value='11', label="12", score=11)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='scolar01',
                text="Votre enfant a t-il déjà fait l'objet de harcèlement à l'école ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sait pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='scolar03',
                text="Y a-t-il eu une ou des interventions pour expliquer les TSA aux camarades de l'école de votre enfant ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='sdasa',
                text="Services à domicile et ambulatoires, services d'accompagnement (optionnel) ",
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
                id='servsoc',
                text="Implication des services sociaux ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='sme',
                text="Service de maintien dans l'emploi",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='stpro1',
                text="A-t-il/elle eu un (des) contrat(s) de travail sur ces 12 derniers mois ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tpl_nb1',
                text="Des hospitalisations de jour (HDJ) pour motif psychiatrique",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tpl_nb3',
                text="Prise en charge au Centre d'Accueil Thérapeutique à Temps Partiel (CATTP)",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tpn_nb1',
                text="Des hospitalisations à temps-plein pour motif psychiatrique ",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='tpn_nb2',
                text="Prise en charge aux appartements thérapeutiques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='urg',
                text="Consultation aux urgences psychiatriques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='voyage',
                text="Avez-vous effectué des voyages (en France ou à l'étranger) pour votre diagnostic/ prise en charge ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="AUT_MEDECO2",
            name="AUT_MEDECO2 Questionnaire",
            description="71 items questionnaire",
            pathology_domain=PathologyDomain.AUTISM_SPECTRUM,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=35,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute AUT_MEDECO2 score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
