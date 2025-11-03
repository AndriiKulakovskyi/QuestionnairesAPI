"""DSM-5 questionnaire structure and DIVA scoring utilities."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


YES_NO: Tuple[str, ...] = ("Oui", "Non")
YES_NO_NSP: Tuple[str, ...] = ("Oui", "Non", "Ne sais pas")
YES_NO_NA: Tuple[str, ...] = ("Oui", "Non", "Non applicable")


def _age_options() -> Tuple[str, ...]:
    values = ["", "Ne sais pas", "<5"]
    values.extend(str(year) for year in range(5, 90))
    values.append(">89")
    return tuple(values)


def _count_options(include_na: bool = False) -> Tuple[str, ...]:
    values: List[str] = ["", "Ne sais pas"]
    if include_na:
        values.append("NA")
    values.extend(str(number) for number in range(0, 21))
    values.append(">20")
    return tuple(values)


def _count_active_values(include_na: bool = False) -> Tuple[str, ...]:
    values = ["NA"] if include_na else []
    values.extend(str(number) for number in range(0, 21))
    values.append(">20")
    return tuple(values)


def _hospital_duration_month_options() -> Tuple[str, ...]:
    values = ["", "Ne sais pas", "0", "1/4", "1/2", "3/4"]
    values.extend(str(number) for number in range(1, 21))
    values.append(">20")
    return tuple(values)


MOOD_DISORDER_TYPES: Tuple[str, ...] = (
    "",
    "Bipolaire de type 1",
    "Bipolaire de type 2",
    "Bipolaire non spécifié",
    "Trouble Dépressif Majeur",
    "Trouble dysthymique",
    "Trouble de l'humeur dû à une affection médicale générale",
    "Trouble de l'humeur induit par l'utilisation d'une substance",
    "Trouble dépressif non spécifié",
    "Trouble Cyclothymique",
    "Autre",
)


FIRST_EPISODE_TYPES: Tuple[str, ...] = (
    "",
    "Episode Dépressif Majeur sans caractéristiques psychotiques",
    "Episode Dépressif Majeur avec caractéristiques psychotiques",
    "Hypomanie",
    "Manie sans caractéristiques psychotiques",
    "Manie avec caractéristiques psychotiques",
    "Ne sais pas",
)


RECENT_EPISODE_TYPES: Tuple[str, ...] = (
    "",
    "Episode Dépressif Majeur",
    "Hypomanie",
    "Manie",
    "Episode non spécifié",
    "Ne sais pas",
)


PSYCHOTIC_DISORDER_TYPES: Tuple[str, ...] = (
    "",
    "Schizophrénie",
    "Trouble schizophréniforme",
    "Trouble schizo-affectif",
    "Troubles délirants",
    "Trouble psychotique bref",
    "Trouble psychotique partagé",
    "Trouble psychotique induit par une affection médicale générale",
    "Trouble psychotique induit par une substance",
    "Trouble psychotique non spécifié",
)


ANXIETY_CHOICES: Tuple[str, ...] = (
    "Trouble panique",
    "Agoraphobie sans trouble panique",
    "Phobie sociale",
    "Phobie spécifique",
    "Trouble obsessionnel compulsif",
    "Stress post-traumatique",
    "Anxiété généralisée (épisode actuel seulement)",
    "Trouble anxieux dû à une affection médicale générale",
    "Trouble anxieux induit par une substance",
    "Trouble anxieux non specifié",
)


SUBSTANCE_CHOICES: Tuple[str, ...] = (
    "Alcool",
    "Sédatif-Hypnotique-Anxiolytique (Benzodiazépines et apparentés)",
    "Cannabis",
    "Stimulants (Amphétamines - Ritaline - coupe-faim )",
    "Opiacés (Héroïne - Opium - Méthadone)",
    "Cocaïne (cocaïne + feuille de coca - Crack)",
    "Hallucinogène / PCP (Poudre d'ange - LSD - champignons - Mescaline - MDMA (Ectasy) - Psylocibine)",
    "Autres (Solvants colle - gaz - peinture - nitrite d'oxyde - Amylnitrite (Poppers))",
)


SUBSTANCE_INDUCED_TYPES: Tuple[str, ...] = (
    "Delirium",
    "Démence persistante",
    "Trouble amnésique",
    "Trouble psychotique",
    "Trouble de l’humeur",
    "Trouble anxieux",
    "Trouble du sommeil",
    "Trouble persistant des perceptions liés aux hallucinogènes",
)


EATING_DISORDER_TYPES: Tuple[str, ...] = (
    "",
    "Anorexie type restrictive",
    "Anorexie type boulimie",
    "Hyperphagie boulimique",
    "Boulimie seule",
    "Trouble des conduites alimentaires non spécifié",
    "Night eating syndrome",
)


SOMATOFORM_TYPES: Tuple[str, ...] = (
    "Trouble de somatisation",
    "Trouble douloureux",
    "Trouble somatoforme indifférencié",
    "Hypocondrie",
    "Peur d'une dysmorphie corporelle",
)


DIVA_INATTENTION_ITEMS: Tuple[Tuple[str, str], ...] = (
    ("a1", "A1. Souvent, ne parvient pas à prêter attention aux détails, ou fait des fautes d'étourderie"),
    ("a2", "A2. A souvent du mal à soutenir son attention au travail ou dans les jeux"),
    ("a3", "A3. Semble souvent ne pas écouter quand on lui parle personnellement"),
    ("a4", "A4. Souvent, ne se conforme pas aux consignes et ne parvient pas à mener à terme ses obligations"),
    ("a5", "A5. A souvent du mal à organiser ses travaux ou ses activités"),
    ("a6", "A6. Souvent, évite ou fait à contrecoeur les tâches nécessitant un effort mental soutenu"),
    ("a7", "A7. Perd souvent les objets nécessaires à son travail ou à ses activités"),
    ("a8", "A8. Se laisse facilement distraire par des stimuli externes"),
    ("a9", "A9. A des oublis fréquents dans la vie quotidienne"),
)


DIVA_HYPERACTIVITY_ITEMS: Tuple[Tuple[str, str], ...] = (
    ("hi1", "H/I 1. Remue souvent les mains ou les pieds, ou se tortille sur son siège"),
    ("hi2", "H/I 2. Se lève souvent dans des situations où il est supposé rester assis"),
    ("hi3", "H/I 3. Souvent, court ou grimpe partout dans des situations inappropriées"),
    ("hi4", "H/I 4. A souvent du mal à se tenir tranquille dans les jeux ou activités de loisir"),
    ("hi5", "H/I 5. Est souvent « sur la brèche » ou agit comme s'il était « monté sur ressorts »"),
    ("hi6", "H/I 6. Parle souvent trop"),
    ("hi7", "H/I 7. Laisse souvent échapper la réponse à une question qui n'est pas encore entièrement posée"),
    ("hi8", "H/I 8. A souvent du mal à attendre son tour"),
    ("hi9", "H/I 9. Interrompt souvent les autres ou impose sa présence"),
)


DSM_IV_THRESHOLD: int = 6


@dataclass(frozen=True)
class DSMField:
    field: str
    label: str
    type: str
    options: Optional[Tuple[str, ...]] = None
    multiple: bool = False
    help_text: Optional[str] = None
    depends_on: Optional[str] = None
    depends_on_values: Optional[Tuple[str, ...]] = None
    required: bool = False
    style: Tuple[str, ...] = ()

    def as_dict(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {
            "field": self.field,
            "label": self.label,
            "type": self.type,
        }
        if self.options is not None:
            data["options"] = list(self.options)
        if self.multiple:
            data["multiple"] = True
        if self.help_text:
            data["help_text"] = self.help_text
        if self.depends_on:
            data["depends_on"] = self.depends_on
        if self.depends_on_values:
            data["depends_on_values"] = list(self.depends_on_values)
        if self.required:
            data["required"] = True
        if self.style:
            data["style"] = list(self.style)
        return data


@dataclass(frozen=True)
class DSMSection:
    id: str
    name: str
    fields: Tuple[DSMField, ...]

    def as_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "fields": [field.as_dict() for field in self.fields],
        }


def _build_mood_section() -> DSMSection:
    active_values = _count_active_values()
    fields: List[DSMField] = [
        DSMField("rad_tbhum_existe", "Le patient a-t-il un trouble de l'humeur?", "enum", options=YES_NO_NSP),
        DSMField(
            "rad_tb_hum",
            "Type de trouble",
            "enum",
            options=MOOD_DISORDER_TYPES,
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "titre_tb_hum_1er_ep",
            "CARACTERISTIQUES DU PREMIER EPISODE",
            "display",
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
            style=("gras",),
        ),
        DSMField(
            "rad_tb_hum_type1er",
            "Type du premier épisode",
            "enum",
            options=FIRST_EPISODE_TYPES,
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_tb_hum_1erpostpartum",
            "Survenue en post-partum (dans les 6 premiers mois)",
            "enum",
            options=YES_NO_NSP,
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_tb_hum_1ercyclo",
            "Le patient a t'il présenté une période initiale cyclothymique (période >2ans)",
            "enum",
            options=YES_NO_NSP,
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "titre_tb_hum_vie_entiere",
            "CARACTERISTIQUES DU TROUBLE VIE ENTIERE",
            "display",
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
            style=("gras",),
        ),
        DSMField(
            "rad_tb_hum_nbepdep",
            "Nombre d'épisodes dépressifs majeurs",
            "enum",
            options=_count_options(),
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_tb_hum_nbepdeppsy",
            "Indiquer le nombre",
            "enum",
            options=_count_options(),
            depends_on="rad_tb_hum_nbepdep",
            depends_on_values=active_values,
        ),
        DSMField(
            "rad_tb_hum_nbephypoman",
            "Nombre d'épisodes hypomaniaques",
            "enum",
            options=_count_options(),
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_tb_hum_nbepman",
            "Nombre d'épisodes maniaques",
            "enum",
            options=_count_options(),
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_tb_hum_ind",
            "Présence d’au moins un épisode induit (virage sous Antidépresseurs ou ECT)",
            "enum",
            options=YES_NO_NSP,
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_rapidcycling",
            "Présence de cycles rapides actuels ou passés",
            "enum",
            options=YES_NO_NSP,
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_remisintercycl",
            "Rémission complète entre les épisodes",
            "enum",
            options=YES_NO_NSP,
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_saisonalite",
            "Caractère saisonnier",
            "enum",
            options=YES_NO_NSP,
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_tb_hum_aao_tt",
            "Age du premier traitement psychotrope",
            "enum",
            options=_age_options(),
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_AGETHYM",
            "Age du premier traitement thymorégulateur",
            "enum",
            options=_age_options(),
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_tb_hum_aao_1hospi",
            "Age de la première hospitalisation",
            "enum",
            options=_age_options(),
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_tb_hum_nb_hospi",
            "Nombre d'hospitalisations",
            "enum",
            options=_count_options(),
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_tb_hum_duree_hospi",
            "Durée totale des hospitalisations (en mois)",
            "enum",
            options=_hospital_duration_month_options(),
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "titre_tb_hum_12mois",
            "CARACTERISTIQUE DU TROUBLE AU COURS DES 12 DERNIERS MOIS",
            "display",
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
            style=("gras",),
        ),
        DSMField(
            "rad_tb_hum_epthyman",
            "Présence d’au moins un épisode thymique au cours de l’année écoulée",
            "enum",
            options=YES_NO_NSP,
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_tb_hum_nb_hospian",
            "Nombre d'hospitalisations",
            "enum",
            options=_count_options(),
            depends_on="rad_tb_hum_epthyman",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "tb_hum_duree_hospian",
            "Durée totale des hospitalisations (en semaine) au cours de l’année écoulée",
            "text",
            depends_on="rad_tb_hum_epthyman",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_social_travan",
            "9. Arrêt de travail au cours de l'année passée",
            "enum",
            options=YES_NO_NA,
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_tb_hum_nb_arretan",
            "Nombre d’arrêts de travail sur l’année écoulée",
            "enum",
            options=_count_options(include_na=True),
            depends_on="rad_social_travan",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "tb_hum_duree_arretan",
            "Durée totale des arrêts de travail sur l'année écoulée (en semaines)",
            "text",
            depends_on="rad_social_travan",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "titre_eprecent",
            "CARACTERISTIQUES DE L'EPISODE LE PLUS RECENT",
            "display",
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
            style=("gras",),
        ),
        DSMField(
            "date_eprecent_datedeb",
            "Date de début de l’épisode le plus récent",
            "date",
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "date_eprecent_datefin",
            "Date de fin de l’épisode le plus récent",
            "date",
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_eprecent_type",
            "Type d'épisode le plus récent",
            "enum",
            options=RECENT_EPISODE_TYPES,
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "titre_epactuel",
            "CARACTERISTIQUES DU TROUBLE DE L'HUMEUR ACTUEL",
            "display",
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
            style=("gras",),
        ),
        DSMField(
            "rad_epactuel",
            "Présence d'un épisode actuel",
            "enum",
            options=YES_NO_NSP,
            depends_on="rad_tbhum_existe",
            depends_on_values=("Oui",),
        ),
    ]
    return DSMSection("mood_disorders", "Troubles de l'humeur", tuple(fields))


def _build_psychotic_section() -> DSMSection:
    fields = (
        DSMField("rad_tb_psychos", "Le patient a t'il un trouble psychotique", "enum", options=YES_NO_NSP),
        DSMField(
            "date_tb_psychos_date",
            "Date de survenue du trouble psychotique",
            "date",
            depends_on="rad_tb_psychos",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_tb_psychos_type",
            "Type de trouble",
            "enum",
            options=PSYCHOTIC_DISORDER_TYPES,
            depends_on="rad_tb_psychos",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_tb_psychos_lastmonth",
            "Présence de symptômes le mois écoulé",
            "enum",
            options=YES_NO_NSP,
            depends_on="rad_tb_psychos",
            depends_on_values=("Oui",),
        ),
    )
    return DSMSection("psychotic_disorders", "Troubles psychotiques", fields)


def _build_comorbid_section() -> DSMSection:
    fields: List[DSMField] = [
        DSMField("rad_tb_anx", "Le patient a t'il un trouble anxieux", "enum", options=YES_NO_NSP),
        DSMField(
            "chk_troubles_anxieux_choix",
            "Troubles anxieux",
            "set",
            options=ANXIETY_CHOICES,
            multiple=True,
            help_text="Maintenez la touche Ctrl lors du click de sélection",
            depends_on="rad_tb_anx",
            depends_on_values=("Oui",),
            style=("gras",),
        ),
        DSMField(
            "rad_anxieux_phobie_sociale_age_debut",
            "Age de début",
            "enum",
            options=_age_options(),
            depends_on="chk_troubles_anxieux_choix",
            depends_on_values=("Phobie sociale",),
        ),
        DSMField(
            "rad_anxieux_phobie_sociale_symptome_mois_ecoule",
            "Présence de symptômes le mois écoulé",
            "enum",
            options=YES_NO_NSP,
            depends_on="chk_troubles_anxieux_choix",
            depends_on_values=("Phobie sociale",),
        ),
        DSMField("rad_tb_subst", "Le patient a-t-il ou a-t-il eu un trouble lié à l'utilisation de substance", "enum", options=YES_NO_NSP),
        DSMField(
            "chk_substances_type",
            "Trouble dû à l'utilisation d'une substance",
            "set",
            options=SUBSTANCE_CHOICES,
            multiple=True,
            help_text="Maintenez la touche Ctrl lors du click de sélection",
            depends_on="rad_tb_subst",
            depends_on_values=("Oui",),
            style=("gras",),
        ),
        DSMField(
            "rad_stimulants_type",
            "Type du trouble",
            "enum",
            options=("Abus", "Dépendance"),
            depends_on="chk_substances_type",
            depends_on_values=("Stimulants (Amphétamines - Ritaline - coupe-faim )",),
        ),
        DSMField(
            "rad_stimulants_mois",
            "Présence de symptômes le mois écoulé",
            "enum",
            options=YES_NO_NSP,
            depends_on="chk_substances_type",
            depends_on_values=("Stimulants (Amphétamines - Ritaline - coupe-faim )",),
        ),
        DSMField(
            "rad_stimulants_age",
            "Age de début",
            "enum",
            options=_age_options(),
            depends_on="chk_substances_type",
            depends_on_values=("Stimulants (Amphétamines - Ritaline - coupe-faim )",),
        ),
        DSMField(
            "stimulants_dur",
            "Durée cumulée du trouble sur la vie entière en mois",
            "text",
            depends_on="chk_substances_type",
            depends_on_values=("Stimulants (Amphétamines - Ritaline - coupe-faim )",),
        ),
        DSMField("rad_tb_substind", "En absence d’abus ou de dépendance, existe-t-il un trouble induit par une substance", "enum", options=YES_NO_NSP),
        DSMField(
            "chk_tb_substind_sub",
            "Type de substance",
            "set",
            options=(
                "Alcool",
                "Sédatif - Hypnotique - Anxiolytique",
                "Cannabis",
                "Stimulants",
                "Opiacés",
                "Cocaïne",
                "Hallucinogène / PCP",
                "Autres substance",
            ),
            multiple=True,
            help_text="Maintenez la touche Ctrl lors du click de sélection",
            depends_on="rad_tb_substind",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "chk_tb_substind_typ",
            "Type de trouble",
            "set",
            options=SUBSTANCE_INDUCED_TYPES,
            multiple=True,
            help_text="Maintenez la touche Ctrl lors du click de sélection",
            depends_on="rad_tb_substind",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_tb_substindpres",
            "Présence de symptômes dans le mois écoulé",
            "enum",
            options=YES_NO_NSP,
            depends_on="rad_tb_substind",
            depends_on_values=("Oui",),
        ),
        DSMField("rad_tb_alim", "Le patient a t'il un trouble du comportement alimentaire", "enum", options=YES_NO_NSP),
        DSMField(
            "rad_conduites_alimentaires_type",
            "Type du trouble du comportement alimentaire",
            "enum",
            options=EATING_DISORDER_TYPES,
            depends_on="rad_tb_alim",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_AMENO_TCAa",
            "Aménorrhée:",
            "enum",
            options=YES_NO,
            depends_on="rad_conduites_alimentaires_type",
            depends_on_values=tuple(option for option in EATING_DISORDER_TYPES if option),
        ),
        DSMField(
            "rad_AGEDEBUT_TCAa",
            "Age de début",
            "enum",
            options=_age_options(),
            depends_on="rad_conduites_alimentaires_type",
            depends_on_values=tuple(option for option in EATING_DISORDER_TYPES if option),
        ),
        DSMField(
            "rad_AGEFIN_TCAa",
            "Age de fin",
            "enum",
            options=_age_options(),
            depends_on="rad_conduites_alimentaires_type",
            depends_on_values=tuple(option for option in EATING_DISORDER_TYPES if option),
        ),
        DSMField(
            "rad_conduites_alimentaires_symptomes_mois_ecoule",
            "Présence de symptômes le mois écoulé",
            "enum",
            options=YES_NO_NSP,
            depends_on="rad_tb_alim",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_OCCUR_TCAa",
            "Trouble actuel:",
            "enum",
            options=YES_NO,
            depends_on="rad_conduites_alimentaires_type",
            depends_on_values=tuple(option for option in EATING_DISORDER_TYPES if option),
        ),
        DSMField("rad_tb_somat", "Le patient a t'il un trouble somatoforme actuel", "enum", options=YES_NO_NSP),
        DSMField(
            "rad_somatoforme_type",
            "Trouble somatoforme",
            "enum",
            options=SOMATOFORM_TYPES,
            depends_on="rad_tb_somat",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_somatoforme_age_debut",
            "Age de début",
            "enum",
            options=_age_options(),
            depends_on="rad_tb_somat",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_somatoforme_presence_symptomes_mois_ecoule",
            "Présence de symptômes le mois écoulé",
            "enum",
            options=YES_NO_NSP,
            depends_on="rad_tb_somat",
            depends_on_values=("Oui",),
        ),
        DSMField(
            "rad_diva",
            "Le patient a t il été évalué avec la DIVA pour le THADA ?",
            "enum",
            options=YES_NO_NSP,
        ),
    ]
    return DSMSection("comorbid_disorders", "Troubles comorbides", tuple(fields))


def _build_diva_fields() -> Tuple[DSMField, ...]:
    depends = ("Oui",)
    fields: List[DSMField] = [
        DSMField(
            "titre_dsmiv_tr",
            "Critère DSM-IV TR",
            "display",
            depends_on="rad_diva",
            depends_on_values=depends,
            style=("gras",),
        )
    ]
    for code, label in DIVA_INATTENTION_ITEMS:
        fields.append(
            DSMField(
                f"titre_{code}",
                label,
                "display",
                depends_on="rad_diva",
                depends_on_values=depends,
                style=("gras",),
            )
        )
        fields.append(
            DSMField(
                f"rad_divadul_{code}",
                "Présent à l’âge adulte",
                "enum",
                options=YES_NO,
                depends_on="rad_diva",
                depends_on_values=depends,
            )
        )
        fields.append(
            DSMField(
                f"rad_divaenf_{code}",
                "Présent dans l’enfance",
                "enum",
                options=YES_NO,
                depends_on="rad_diva",
                depends_on_values=depends,
            )
        )
    fields.append(
        DSMField(
            "titre_cda",
            "Nombre total de critères de Déficit Attentionnel",
            "display",
            depends_on="rad_diva",
            depends_on_values=depends,
            style=("gras",),
        )
    )
    fields.append(
        DSMField(
            "total_adul_a",
            "Age adulte",
            "text",
            depends_on="rad_diva",
            depends_on_values=depends,
        )
    )
    fields.append(
        DSMField(
            "total_enf_a",
            "Enfance",
            "text",
            depends_on="rad_diva",
            depends_on_values=depends,
        )
    )
    for code, label in DIVA_HYPERACTIVITY_ITEMS:
        fields.append(
            DSMField(
                f"titre_{code}",
                label,
                "display",
                depends_on="rad_diva",
                depends_on_values=depends,
                style=("gras",),
            )
        )
        fields.append(
            DSMField(
                f"rad_divadul_{code}",
                "Présent à l’âge adulte",
                "enum",
                options=YES_NO,
                depends_on="rad_diva",
                depends_on_values=depends,
            )
        )
        fields.append(
            DSMField(
                f"rad_divaenf_{code}",
                "Présent dans l’enfance",
                "enum",
                options=YES_NO,
                depends_on="rad_diva",
                depends_on_values=depends,
            )
        )
    fields.append(
        DSMField(
            "titre_chi",
            "Nombre total de critères d’Hyperactivité et d’Impulsivité",
            "display",
            depends_on="rad_diva",
            depends_on_values=depends,
            style=("gras",),
        )
    )
    fields.append(
        DSMField(
            "total_adul_hi",
            "Age adulte",
            "text",
            depends_on="rad_diva",
            depends_on_values=depends,
        )
    )
    fields.append(
        DSMField(
            "total_enf_hi",
            "Enfance",
            "text",
            depends_on="rad_diva",
            depends_on_values=depends,
        )
    )
    return tuple(fields)


def _build_diva_section() -> DSMSection:
    return DSMSection("diva", "DIVA", _build_diva_fields())

INATTENTION_CODES: Tuple[str, ...] = tuple(code for code, _ in DIVA_INATTENTION_ITEMS)
HYPERACTIVITY_CODES: Tuple[str, ...] = tuple(code for code, _ in DIVA_HYPERACTIVITY_ITEMS)


class DSM5Questionnaire:
    """Structured DSM-5 questionnaire helper."""

    def __init__(self) -> None:
        self.sections: List[Dict[str, Any]] = self._build_sections()
        self.diva_fields: Dict[str, Dict[str, Tuple[str, ...]]] = self._build_diva_field_map()

    @staticmethod
    def _build_sections() -> List[Dict[str, Any]]:
        section_objects = (
            _build_mood_section(),
            _build_psychotic_section(),
            _build_comorbid_section(),
            _build_diva_section(),
        )
        return [section.as_dict() for section in section_objects]

    @staticmethod
    def _build_diva_field_map() -> Dict[str, Dict[str, Tuple[str, ...]]]:
        return {
            "inattention": {
                "adult": tuple(f"rad_divadul_{code}" for code in INATTENTION_CODES),
                "child": tuple(f"rad_divaenf_{code}" for code in INATTENTION_CODES),
            },
            "hyperactivity_impulsivity": {
                "adult": tuple(f"rad_divadul_{code}" for code in HYPERACTIVITY_CODES),
                "child": tuple(f"rad_divaenf_{code}" for code in HYPERACTIVITY_CODES),
            },
        }

    def get_sections(self) -> List[Dict[str, Any]]:
        """Return questionnaire sections."""
        return self.sections

    def get_diva_fields(self) -> Mapping[str, Mapping[str, Tuple[str, ...]]]:
        """Return field identifiers used in the DIVA scoring block."""
        return self.diva_fields

    def get_instructions(self) -> str:
        return (
            "Collecter les informations DSM-5 en suivant l'ordre des sections (troubles de l'humeur,"
            " troubles psychotiques, comorbidités). Les items DIVA reprennent les critères DSM-IV TR"
            " de l'adulte : répondre « Oui » ou « Non » pour chaque item en enfance et à l'âge adulte."
            " Un score est considéré comme positif lorsqu'au moins six critères sont présents dans"
            " chaque période (enfance et âge adulte) pour le domaine concerné."
        )

    @staticmethod
    def _normalise_diva_value(value: Any) -> Optional[bool]:
        if value is None:
            return None
        if isinstance(value, bool):
            return value
        if isinstance(value, (int, float)):
            if int(value) == 1:
                return True
            if int(value) == 0:
                return False
            return None
        if isinstance(value, (list, tuple)) and value:
            value = value[0]
        if isinstance(value, str):
            token = value.strip().lower()
            if token == "":
                return None
            if token in {"oui", "true", "vrai", "yes", "1"}:
                return True
            if token in {"non", "false", "faux", "no", "0"}:
                return False
        return None

    def calculate_diva_scores(self, responses: Mapping[str, Any]) -> Dict[str, Any]:
        domain_results: Dict[str, Any] = {}
        errors: List[str] = []

        for domain, contexts in self.diva_fields.items():
            context_results: Dict[str, Any] = {}
            domain_total = 0
            domain_max = 0
            for context, field_ids in contexts.items():
                context_total = 0
                missing: List[str] = []
                invalid: List[str] = []
                for field_id in field_ids:
                    raw_value = responses.get(field_id)
                    normalised = self._normalise_diva_value(raw_value)
                    if normalised is None:
                        if raw_value in (None, ""):
                            missing.append(field_id)
                        else:
                            invalid.append(field_id)
                        continue
                    if normalised:
                        context_total += 1
                context_max = len(field_ids)
                domain_total += context_total
                domain_max += context_max
                meets_threshold = context_total >= DSM_IV_THRESHOLD
                context_results[context] = {
                    "score": context_total,
                    "max": context_max,
                    "threshold": DSM_IV_THRESHOLD,
                    "meets_threshold": meets_threshold,
                    "missing": missing,
                    "invalid": invalid,
                }
                if missing:
                    errors.append(f"{domain}.{context}: missing values for {', '.join(missing)}")
                if invalid:
                    errors.append(f"{domain}.{context}: invalid values for {', '.join(invalid)}")
            meets_domain = all(result["meets_threshold"] for result in context_results.values())
            domain_results[domain] = {
                "total": domain_total,
                "max": domain_max,
                "contexts": context_results,
                "meets_domain_threshold": meets_domain,
            }

        summary = {
            domain: result["meets_domain_threshold"]
            for domain, result in domain_results.items()
        }
        summary["meets_combined"] = all(summary.values())

        return {
            "domains": domain_results,
            "summary": summary,
            "threshold": DSM_IV_THRESHOLD,
            "errors": errors,
            "valid": not errors,
        }

    def calculate_score(self, responses: Mapping[str, Any]) -> Dict[str, Any]:
        """Wrapper exposing DIVA scores."""
        diva_scores = self.calculate_diva_scores(responses)
        return {
            "diva": diva_scores,
            "valid": diva_scores["valid"],
            "errors": diva_scores["errors"],
        }


__all__ = ["DSM5Questionnaire"]

