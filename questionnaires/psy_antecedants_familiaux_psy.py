"""
PSY_ANTECEDANTS_FAMILIAUX_PSY - PSY_ANTECEDANTS_FAMILIAUX_PSY Questionnaire
===========================================================================

99 items questionnaire

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


@register_questionnaire("PSY_ANTECEDANTS_FAMILIAUX_PSY")
@dataclass
class PsyAntecedantsFamiliauxPsy(BaseQuestionnaire):
    """PSY_ANTECEDANTS_FAMILIAUX_PSY Questionnaire - reusable across applications."""
    
    def __init__(self):
        """Initialize PSY_ANTECEDANTS_FAMILIAUX_PSY questionnaire with all 99 items."""
        
        questions_list = [
            Question(
                id='atcdfamcv_enfant',
                text="a-t-il des facteurs de risques cardio-vasculaires ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_enfant_typdiab',
                text="spécifier le type :",
                options=[
                    AnswerOption(value='a', label="Type I", score=0),
                    AnswerOption(value='b', label="Type II", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_enfant_type',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_fratrie',
                text="a-t-il des facteurs de risques cardio-vasculaires ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_fratrie_type',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_gdmeremat',
                text="Votre grand-mère maternelle a-t-elle des facteurs de risques cardio-vasculaires ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_gdmeremat_typdiab',
                text="spécifier le type :",
                options=[
                    AnswerOption(value='a', label="Type I", score=0),
                    AnswerOption(value='b', label="Type II", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_gdmeremat_type',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_gdmerepat',
                text="Votre grand-mère paternelle a-t-elle des facteurs de risques cardio-vasculaires ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_gdmerepat_typdiab',
                text="spécifier le type :",
                options=[
                    AnswerOption(value='a', label="Type I", score=0),
                    AnswerOption(value='b', label="Type II", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_gdmerepat_type',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_gdperemat',
                text="Votre grand-Père maternel a-t-il des facteurs de risques cardio-vasculaires ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_gdperemat_typdiab',
                text="spécifier le type :",
                options=[
                    AnswerOption(value='a', label="Type I", score=0),
                    AnswerOption(value='b', label="Type II", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_gdperemat_type',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_gdperepat',
                text="Votre grand-père paternel a-t-il des facteurs de risques cardio-vasculaires ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_gdperepat_typdiab',
                text="spécifier le type :",
                options=[
                    AnswerOption(value='a', label="Type I", score=0),
                    AnswerOption(value='b', label="Type II", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_gdperepat_type',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_mere',
                text="Votre mère a-t-elle des facteurs de risques cardio-vasculaires ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_mere_typdiab',
                text="spécifier le type :",
                options=[
                    AnswerOption(value='a', label="Type I", score=0),
                    AnswerOption(value='b', label="Type II", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_mere_type',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_pere',
                text="Votre père a-t-il des facteurs de risques cardio-vasculaires ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_pere_typdiab',
                text="spécifier le type :",
                options=[
                    AnswerOption(value='a', label="Type I", score=0),
                    AnswerOption(value='b', label="Type II", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfamcv_pere_type',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2),
                    AnswerOption(value='d', label="4", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfampsy_enfant_anx',
                text="Troubles anxieux",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfampsy_enfant_dem',
                text="Démence",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfampsy_fratrie_anx',
                text="Troubles anxieux",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfampsy_fratrie_dem',
                text="Démence",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfampsy_gdmeremat_anx',
                text="Troubles anxieux",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfampsy_gdmeremat_dem',
                text="Démence",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfampsy_gdmerepat_anx',
                text="Troubles anxieux",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfampsy_gdmerepat_dem',
                text="Démence",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfampsy_gdperemat_anx',
                text="Troubles anxieux",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfampsy_gdperemat_dem',
                text="Démence",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfampsy_gdperepat_anx',
                text="Troubles anxieux",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfampsy_gdperepat_dem',
                text="Démence",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfampsy_mere_anx',
                text="Troubles anxieux",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfampsy_mere_dem',
                text="Démence",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfampsy_pere_anx',
                text="Troubles anxieux",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='atcdfampsy_pere_dem',
                text="Démence",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='enfant_substance',
                text="Dépendance ou abus de substances",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='enfant_substance_type',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='enfant_suicide',
                text="Suicide",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Tentative de suicide", score=1),
                    AnswerOption(value='c', label="Suicide abouti", score=2),
                    AnswerOption(value='d', label="Ne sais pas", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='enfant_trouble_schi',
                text="Troubles Schizophréniques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='enfant_trouble_thy',
                text="Troubles Thymiques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='enfant_trouble_thy_typ',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="EDM ou Unipolaire", score=0),
                    AnswerOption(value='b', label="Bipolaire", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fratrie_substance',
                text="Dépendance ou abus de substances",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fratrie_substance_type',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fratrie_suicide',
                text="Suicide",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Tentative de suicide", score=1),
                    AnswerOption(value='c', label="Suicide abouti", score=2),
                    AnswerOption(value='d', label="Ne sais pas", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fratrie_trouble_schi',
                text="Troubles Schizophréniques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fratrie_trouble_thy',
                text="Troubles Thymiques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='fratrie_trouble_thy_typ',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="EDM ou Unipolaire", score=0),
                    AnswerOption(value='b', label="Bipolaire", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdmeremat_substance',
                text="Dépendance ou abus de substances",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdmeremat_substance_type',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdmeremat_suicide',
                text="Suicide",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Tentative de suicide", score=1),
                    AnswerOption(value='c', label="Suicide abouti", score=2),
                    AnswerOption(value='d', label="Ne sais pas", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdmeremat_trouble_schi',
                text="Troubles Schizophréniques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdmeremat_trouble_thy',
                text="Troubles Thymiques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdmeremat_trouble_thy_typ',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="EDM ou Unipolaire", score=0),
                    AnswerOption(value='b', label="Bipolaire", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdmerepat_substance',
                text="Dépendance ou abus de substances",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdmerepat_substance_type',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdmerepat_suicide',
                text="Suicide",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Tentative de suicide", score=1),
                    AnswerOption(value='c', label="Suicide abouti", score=2),
                    AnswerOption(value='d', label="Ne sais pas", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdmerepat_trouble_schi',
                text="Troubles Schizophréniques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdmerepat_trouble_thy',
                text="Troubles Thymiques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdmerepat_trouble_thy_typ',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="EDM ou Unipolaire", score=0),
                    AnswerOption(value='b', label="Bipolaire", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdperemat_substance',
                text="Dépendance ou abus de substances",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdperemat_substance_type',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdperemat_suicide',
                text="Suicide",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Tentative de suicide", score=1),
                    AnswerOption(value='c', label="Suicide abouti", score=2),
                    AnswerOption(value='d', label="Ne sais pas", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdperemat_trouble_schi',
                text="Troubles Schizophréniques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdperemat_trouble_thy',
                text="Troubles Thymiques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdperemat_trouble_thy_typ',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="EDM ou Unipolaire", score=0),
                    AnswerOption(value='b', label="Bipolaire", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdperepat_substance',
                text="Dépendance ou abus de substances",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdperepat_substance_type',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdperepat_suicide',
                text="Suicide",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Tentative de suicide", score=1),
                    AnswerOption(value='c', label="Suicide abouti", score=2),
                    AnswerOption(value='d', label="Ne sais pas", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdperepat_trouble_schi',
                text="Troubles Schizophréniques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdperepat_trouble_thy',
                text="Troubles Thymiques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='gdperepat_trouble_thy_typ',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="EDM ou Unipolaire", score=0),
                    AnswerOption(value='b', label="Bipolaire", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mere_substance',
                text="Dépendance ou abus de substances",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mere_substance_type',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mere_suicide',
                text="Suicide",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Tentative de suicide", score=1),
                    AnswerOption(value='c', label="Suicide abouti", score=2),
                    AnswerOption(value='d', label="Ne sais pas", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mere_trouble_schi',
                text="Troubles Schizophréniques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mere_trouble_thy',
                text="Troubles Thymiques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='mere_trouble_thy_typ',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="EDM ou Unipolaire", score=0),
                    AnswerOption(value='b', label="Bipolaire", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pere_substance',
                text="Dépendance ou abus de substances",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pere_substance_type',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="1", score=0),
                    AnswerOption(value='b', label="2", score=1),
                    AnswerOption(value='c', label="3", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pere_suicide',
                text="Suicide",
                options=[
                    AnswerOption(value='a', label="Aucun", score=0),
                    AnswerOption(value='b', label="Tentative de suicide", score=1),
                    AnswerOption(value='c', label="Suicide abouti", score=2),
                    AnswerOption(value='d', label="Ne sais pas", score=3)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pere_trouble_schi',
                text="Troubles Schizophréniques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pere_trouble_thy',
                text="Troubles Thymiques",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='pere_trouble_thy_typ',
                text="spécifier",
                options=[
                    AnswerOption(value='a', label="EDM ou Unipolaire", score=0),
                    AnswerOption(value='b', label="Bipolaire", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='structure_enfant',
                text="Avez-vous des enfants ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='structure_enfant_atteint_psy',
                text="a-t-il des antécédents de maladie psychiatrique ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='structure_enfant_atteint_sex',
                text="Enfant  Atteint",
                options=[
                    AnswerOption(value='a', label="Fils", score=0),
                    AnswerOption(value='b', label="Fille", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='structure_fratrie',
                text="Avez-vous des frères/soeurs ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='structure_fratrie_atteint_psy',
                text="a-t-il des antécédents de maladie psychiatrique ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='structure_fratrie_atteint_sex',
                text="Germain Atteint",
                options=[
                    AnswerOption(value='a', label="Frère", score=0),
                    AnswerOption(value='b', label="Soeur", score=1)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='structure_gdmeremat',
                text="Votre  grand-mère maternelle a-t-elle des antécédents de maladie psychiatrique ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='structure_gdmerepat',
                text="Votre  grand-mère paternelle a-t-elle des antécédents de maladie psychiatrique ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='structure_gdperemat',
                text="Votre  grand-père maternel a-t-elle des antécédents de maladie psychiatrique ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='structure_gdperepat',
                text="Votre  grand-père paternel a-t-il des antécédents de maladie psychiatrique ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='structure_mere',
                text="Votre mère a-t-elle des antécédents de maladie psychiatrique ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            ),
            Question(
                id='structure_pere',
                text="Votre père a-t-il des antécédents de maladie psychiatrique ?",
                options=[
                    AnswerOption(value='a', label="Oui", score=0),
                    AnswerOption(value='b', label="Non", score=1),
                    AnswerOption(value='c', label="Ne sais pas", score=2)
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )
        ]
        
        super().__init__(
            code="PSY_ANTECEDANTS_FAMILIAUX_PSY",
            name="PSY_ANTECEDANTS_FAMILIAUX_PSY Questionnaire",
            description="99 items questionnaire",
            pathology_domain=PathologyDomain.DEPRESSION,
            respondent_type=RespondentType.SELF_REPORT,
            questions=questions_list,
            visit_types=["Initial", "Follow-up"],
            estimated_duration_minutes=49,
            version="1.0"
        )
        
        self.scoring_strategy = SimpleSumStrategy()
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute PSY_ANTECEDANTS_FAMILIAUX_PSY score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {'; '.join(validation_errors)}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
