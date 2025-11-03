from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence


class CSSRSQuestionnaire:
    """Python representation of the C-SSRS form defined in apps/ecedr/www/form/150.php."""

    def __init__(self) -> None:
        self.name = "C-SSRS - Columbia Suicide Severity Rating Scale"
        self.description = (
            "Structured clinician-administered questionnaire capturing suicidal ideation "
            "and suicidal behaviour. This mirrors the implementation used in the eBipolar "
            "application (evaluation initiale / évaluation médicale)."
        )
        self.instructions_overview = (
            "Posez les questions 1 et 2. Si les deux réponses sont négatives, passez à la "
            "section « Comportement suicidaire ». Si la réponse à la question 2 est « oui », "
            "posez les questions 3, 4 et 5. Si la réponse à la question 1 et/ou 2 est « oui », "
            "complétez la section « Intensité de l'idéation ». Les réponses portent sur la "
            "période allant de la semaine précédente (évaluation initiale) ou de la dernière "
            "visite (suivi) jusqu'au moment où la personne s'est sentie la plus suicidaire."
        )
        self.warning = (
            "Avertissement : Cette échelle est destinée à être utilisée par des cliniciens "
            "qualifiés. Les questions contenues dans l'Échelle d'évaluation de Columbia sur la "
            "gravité du risque suicidaire (C-SSRS) sont des suggestions à titre indicatif. La "
            "présence de risque suicidaire dépend de l'estimation clinique finale. Les "
            "définitions des comportements suicidaires reposent sur celles du Columbia Suicide "
            "History Form (Posner, Oquendo & Mann). Pour toute question ou besoin de "
            "formation, contacter posnerk@childpsych.columbia.edu."
        )

        self.ideation_labels: Dict[int, str] = {
            1: "Désir d'être mort(e)",
            2: "Pensées suicidaires actives non spécifiques",
            3: "Idéation suicidaire active avec méthode envisagée",
            4: "Idéation suicidaire active avec intention (sans scénario)",
            5: "Idéation suicidaire active avec scénario précis et intention",
        }
        self.frequency_labels: Dict[int, str] = {
            1: "Moins d'une fois par semaine",
            2: "Une fois par semaine",
            3: "2 à 5 fois par semaine",
            4: "Tous les jours ou presque",
            5: "Plusieurs fois par jour",
        }
        self.duration_labels: Dict[int, str] = {
            1: "Quelques instants (secondes ou minutes)",
            2: "Moins d'une heure / un certain temps",
            3: "1 à 4 heures / longtemps",
            4: "4 à 8 heures / une grande partie de la journée",
            5: "Plus de 8 heures / en permanence",
        }
        self.control_labels: Dict[int, str] = {
            0: "N'essaie pas de maîtriser ses pensées",
            1: "Maîtrise facilement ses pensées",
            2: "Capable de maîtriser ses pensées avec de légères difficultés",
            3: "Capable de maîtriser ses pensées avec quelques difficultés",
            4: "Capable de maîtriser ses pensées avec de grandes difficultés",
            5: "Incapable de maîtriser ses pensées",
        }
        self.deterrent_labels: Dict[int, str] = {
            0: "Sans objet",
            1: "Des éléments dissuasifs ont véritablement empêché la tentative",
            2: "Des éléments dissuasifs ont probablement arrêté la tentative",
            3: "Incertain que des éléments dissuasifs aient arrêté la tentative",
            4: "Très probablement aucun élément dissuasif",
            5: "Aucun élément dissuasif n'a arrêté la tentative",
        }
        self.reason_labels: Dict[int, str] = {
            0: "Sans objet",
            1: "Uniquement pour attirer l'attention / se venger / faire réagir",
            2: "Principalement pour attirer l'attention / se venger / faire réagir",
            3: "Autant pour attirer l'attention que pour faire cesser la douleur",
            4: "Principalement pour faire cesser la douleur",
            5: "Uniquement pour faire cesser la douleur",
        }
        self.medical_impact_labels: Dict[int, str] = {
            0: "Aucune atteinte ou atteinte très légère",
            1: "Atteinte physique légère",
            2: "Atteinte physique modérée nécessitant une prise en charge",
            3: "Atteinte physique grave (hospitalisation et soins intensifs probable)",
            4: "Atteinte physique très grave (hospitalisation et soins intensifs nécessaire)",
            5: "Décès",
        }
        self.potential_impact_labels: Dict[int, str] = {
            0: "Comportement peu enclin à engendrer des blessures",
            1: "Comportement susceptible d'engendrer des blessures sans risque vital",
            2: "Comportement susceptible de causer la mort malgré des soins disponibles",
        }

        self.sections = self._build_sections()
        self.questions = self._flatten_questions(self.sections)

    def _build_sections(self) -> List[Dict[str, Any]]:
        yes_no_options = [
            {"value": 1, "label": "Oui"},
            {"value": 0, "label": "Non"},
        ]

        frequency_options = [
            {"value": value, "label": label}
            for value, label in self.frequency_labels.items()
        ]
        duration_options = [
            {"value": value, "label": label}
            for value, label in self.duration_labels.items()
        ]
        control_options = [
            {"value": value, "label": label}
            for value, label in sorted(self.control_labels.items())
        ]
        deterrent_options = [
            {"value": value, "label": label}
            for value, label in sorted(self.deterrent_labels.items())
        ]
        reason_options = [
            {"value": value, "label": label}
            for value, label in sorted(self.reason_labels.items())
        ]
        medical_options = [
            {"value": value, "label": label}
            for value, label in sorted(self.medical_impact_labels.items())
        ]
        potential_options = [
            {"value": value, "label": label}
            for value, label in sorted(self.potential_impact_labels.items())
        ]

        sections: List[Dict[str, Any]] = []

        def add_section(section_id: str, title: str, questions: Sequence[Dict[str, Any]]) -> None:
            section_questions: List[Dict[str, Any]] = []
            for question in questions:
                question_copy = dict(question)
                question_copy.setdefault("section", section_id)
                section_questions.append(question_copy)
            sections.append({"id": section_id, "title": title, "questions": section_questions})

        add_section(
            "ideation",
            "Idéation suicidaire",
            [
                {
                    "id": "CSSRS1",
                    "number": 1,
                    "text": "Avez-vous souhaité être mort(e) ou vous endormir et ne jamais vous réveiller ?",
                    "type": "single_choice",
                    "options": yes_no_options,
                    "notes": (
                        "Le sujet adhère à des pensées concernant le désir de mourir, de ne plus être en vie, "
                        "ou de s'endormir et ne pas se réveiller."
                    ),
                },
                {
                    "id": "CSSRS1BIS",
                    "text": "Décrire le contenu lié au désir d'être mort(e)",
                    "type": "textarea",
                    "shown_if": [{"question": "CSSRS1", "equals": 1}],
                },
                {
                    "id": "CSSRS2",
                    "number": 2,
                    "text": "Avez-vous réellement pensé à vous suicider ?",
                    "type": "single_choice",
                    "options": yes_no_options,
                    "notes": (
                        "Pensées suicidaires actives non spécifiques, sans méthode ni intention ni scénario précis."
                    ),
                },
                {
                    "id": "CSSRS2BIS",
                    "text": "Décrire les pensées suicidaires non spécifiques",
                    "type": "textarea",
                    "shown_if": [{"question": "CSSRS2", "equals": 1}],
                },
                {
                    "id": "CSSRS3",
                    "number": 3,
                    "text": "Avez-vous pensé à la manière dont vous vous y prendriez ?",
                    "type": "single_choice",
                    "options": yes_no_options,
                    "shown_if": [{"question": "CSSRS2", "equals": 1}],
                    "notes": (
                        "Le sujet envisage au moins une méthode pour se suicider mais sans scénario détaillé."
                    ),
                },
                {
                    "id": "CSSRS3BIS",
                    "text": "Décrire la ou les méthodes envisagées",
                    "type": "textarea",
                    "shown_if": [{"question": "CSSRS3", "equals": 1}],
                },
                {
                    "id": "CSSRS4",
                    "number": 4,
                    "text": "Avez-vous eu l'intention de passer à l'acte ?",
                    "type": "single_choice",
                    "options": yes_no_options,
                    "shown_if": [{"question": "CSSRS2", "equals": 1}],
                    "notes": "Idéation active avec intention de passage à l'acte mais sans scénario précis.",
                },
                {
                    "id": "CSSRS4BIS",
                    "text": "Décrire l'intention de passage à l'acte",
                    "type": "textarea",
                    "shown_if": [{"question": "CSSRS4", "equals": 1}],
                },
                {
                    "id": "CSSRS5",
                    "number": 5,
                    "text": (
                        "Avez-vous élaboré un scénario détaillé pour vous suicider et avez-vous l'intention "
                        "de le mettre à exécution ?"
                    ),
                    "type": "single_choice",
                    "options": yes_no_options,
                    "shown_if": [{"question": "CSSRS2", "equals": 1}],
                    "notes": "Idéation active avec scénario détaillé et intention de mise en œuvre.",
                },
                {
                    "id": "CSSRS5BIS",
                    "text": "Décrire le scénario suicidaire détaillé",
                    "type": "textarea",
                    "shown_if": [{"question": "CSSRS5", "equals": 1}],
                },
            ],
        )

        intensity_condition = {
            "any": [
                {"question": "CSSRS1", "equals": 1},
                {"question": "CSSRS2", "equals": 1},
            ]
        }

        add_section(
            "intensity",
            "Intensité de l'idéation",
            [
                {
                    "id": "CSSRS6",
                    "number": "6",
                    "text": "Idéation la plus grave (1 à 5)",
                    "type": "numeric",
                    "shown_if": [intensity_condition],
                    "notes": (
                        "Indiquer le numéro de l'item d'idéation le plus grave observé durant la période évaluée."
                    ),
                },
                {
                    "id": "CSSRS7",
                    "text": "Description de l'idéation la plus grave",
                    "type": "textarea",
                    "shown_if": [intensity_condition],
                },
                {
                    "id": "CSSRS8",
                    "text": "Fréquence des pensées suicidaires",
                    "type": "single_choice",
                    "options": frequency_options,
                    "shown_if": [intensity_condition],
                },
                {
                    "id": "CSSRS9",
                    "text": "Durée des pensées suicidaires",
                    "type": "single_choice",
                    "options": duration_options,
                    "shown_if": [intensity_condition],
                },
                {
                    "id": "CSSRS10",
                    "text": "Maîtrise des pensées suicidaires",
                    "type": "single_choice",
                    "options": control_options,
                    "shown_if": [intensity_condition],
                    "notes": "Capacité perçue à interrompre les pensées suicidaires si la personne le souhaite.",
                },
                {
                    "id": "CSSRS11",
                    "text": "Éléments dissuasifs",
                    "type": "single_choice",
                    "options": deterrent_options,
                    "shown_if": [intensity_condition],
                    "notes": "Présence d'éléments ou de personnes ayant empêché le passage à l'acte.",
                },
                {
                    "id": "CSSRS12",
                    "text": "Causes de l'idéation suicidaire",
                    "type": "single_choice",
                    "options": reason_options,
                    "shown_if": [intensity_condition],
                    "notes": "Motifs principaux associés à l'idéation suicidaire.",
                },
            ],
        )

        add_section(
            "behavior",
            "Comportements suicidaires",
            [
                {
                    "id": "CSSRS13",
                    "number": 13,
                    "text": (
                        "Avez-vous fait une tentative de suicide ou quelque chose de dangereux qui aurait pu "
                        "entraîner votre mort ?"
                    ),
                    "type": "single_choice",
                    "options": yes_no_options,
                    "notes": (
                        "Acte potentiellement auto-agressif avec intention, qu'il y ait ou non des lésions."
                    ),
                },
                {
                    "id": "CSSRS13BIS",
                    "text": "Décrire la tentative de suicide",
                    "type": "textarea",
                    "shown_if": [{"question": "CSSRS13", "equals": 1}],
                },
                {
                    "id": "CSSRS14",
                    "text": "Nombre total de tentatives de suicide",
                    "type": "numeric",
                    "shown_if": [{"question": "CSSRS13", "equals": 1}],
                },
                {
                    "id": "CSSRS15",
                    "number": 15,
                    "text": "Le sujet a-t-il eu un comportement auto-agressif non suicidaire ?",
                    "type": "single_choice",
                    "options": yes_no_options,
                },
                {
                    "id": "CSSRS16",
                    "number": 16,
                    "text": "Tentative interrompue par un facteur extérieur ?",
                    "type": "single_choice",
                    "options": yes_no_options,
                    "notes": (
                        "Interruption par un facteur externe d'un acte auto-agressif qui aurait été mené à terme."
                    ),
                },
                {
                    "id": "CSSRS16BIS",
                    "text": "Décrire la tentative interrompue",
                    "type": "textarea",
                    "shown_if": [{"question": "CSSRS16", "equals": 1}],
                },
                {
                    "id": "CSSRS29",
                    "text": "Nombre total de tentatives interrompues",
                    "type": "numeric",
                    "shown_if": [{"question": "CSSRS16", "equals": 1}],
                },
                {
                    "id": "CSSRS31",
                    "number": 17,
                    "text": "Tentative avortée (la personne s'est arrêtée d'elle-même avant de passer à l'acte) ?",
                    "type": "single_choice",
                    "options": yes_no_options,
                    "notes": (
                        "La personne interrompt d'elle-même la tentative avant qu'un comportement autodestructeur ne soit réalisé."
                    ),
                },
                {
                    "id": "CSSRS29BIS",
                    "text": "Décrire la tentative avortée",
                    "type": "textarea",
                    "shown_if": [{"question": "CSSRS31", "equals": 1}],
                },
                {
                    "id": "CSSRS30",
                    "text": "Nombre total de tentatives avortées",
                    "type": "numeric",
                    "shown_if": [{"question": "CSSRS31", "equals": 1}],
                },
                {
                    "id": "CSSRS20",
                    "number": 18,
                    "text": "Avez-vous pris des mesures préparatoires en vue d'une tentative de suicide ?",
                    "type": "single_choice",
                    "options": yes_no_options,
                    "notes": "Préparatifs ou actes dépassant la verbalisation (rassembler des moyens, lettre, etc.).",
                },
                {
                    "id": "CSSRS20BIS",
                    "text": "Décrire les actes préparatoires",
                    "type": "textarea",
                    "shown_if": [{"question": "CSSRS20", "equals": 1}],
                },
                {
                    "id": "CSSRS21",
                    "number": 19,
                    "text": "Un comportement suicidaire a-t-il été observé durant la période évaluée ?",
                    "type": "single_choice",
                    "options": yes_no_options,
                },
            ],
        )

        lethality_condition = [{"question": "CSSRS21", "equals": 1}]

        add_section(
            "observed_lethality",
            "Létalité / lésions médicales observées",
            [
                {
                    "id": "CSSRS22_D",
                    "text": "Date de la tentative la plus récente",
                    "type": "date",
                    "shown_if": lethality_condition,
                },
                {
                    "id": "CSSRS22_C",
                    "text": "Impact médical de la tentative la plus récente",
                    "type": "single_choice",
                    "options": medical_options,
                    "shown_if": lethality_condition,
                },
                {
                    "id": "CSSRS23_D",
                    "text": "Date de la tentative la plus létale",
                    "type": "date",
                    "shown_if": lethality_condition,
                },
                {
                    "id": "CSSRS23_C",
                    "text": "Impact médical de la tentative la plus létale",
                    "type": "single_choice",
                    "options": medical_options,
                    "shown_if": lethality_condition,
                },
                {
                    "id": "CSSRS24_D",
                    "text": "Date de la première tentative",
                    "type": "date",
                    "shown_if": lethality_condition,
                },
                {
                    "id": "CSSRS24_C",
                    "text": "Impact médical de la première tentative",
                    "type": "single_choice",
                    "options": medical_options,
                    "shown_if": lethality_condition,
                },
            ],
        )

        add_section(
            "potential_lethality",
            "Létalité potentielle",
            [
                {
                    "id": "CSSRS25_C",
                    "text": "Létalité potentielle – tentative la plus récente",
                    "type": "single_choice",
                    "options": potential_options,
                    "shown_if": lethality_condition,
                },
                {
                    "id": "CSSRS27_C",
                    "text": "Létalité potentielle – tentative la plus létale",
                    "type": "single_choice",
                    "options": potential_options,
                    "shown_if": lethality_condition,
                },
                {
                    "id": "CSSRS28_C",
                    "text": "Létalité potentielle – première tentative",
                    "type": "single_choice",
                    "options": potential_options,
                    "shown_if": lethality_condition,
                },
            ],
        )

        return sections

    @staticmethod
    def _flatten_questions(sections: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
        flat: List[Dict[str, Any]] = []
        for section in sections:
            flat.extend(section.get("questions", []))
        return flat

    def get_sections(self) -> List[Dict[str, Any]]:
        return self.sections

    def get_instructions(self) -> str:
        return f"{self.warning}\n\n{self.instructions_overview}"

    def summarize(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        errors: List[str] = []

        ideation_summary = self._compute_ideation_summary(responses, errors)
        intensity_summary = self._summarize_intensity(responses, errors)
        behavior_summary = self._summarize_behavior(responses, errors)
        observed_lethality = self._summarize_observed_lethality(responses, errors)
        potential_lethality = self._summarize_potential_lethality(responses, errors)

        result: Dict[str, Any] = {
            "ideation": {
                "highest_positive_item": ideation_summary,
                "recorded_severity": self._clean_str(responses.get("CSSRS6")),
                "description": self._clean_str(responses.get("CSSRS7")),
                "intensity": intensity_summary,
            },
            "behavior": behavior_summary,
            "observed_lethality": observed_lethality,
            "potential_lethality": potential_lethality,
            "raw_responses": responses,
            "errors": errors,
            "valid": len(errors) == 0,
        }
        return result

    # ---- helpers -----------------------------------------------------------------
    def _compute_ideation_summary(
        self, responses: Dict[str, Any], errors: List[str]
    ) -> Optional[Dict[str, Any]]:
        highest: Optional[Dict[str, Any]] = None
        for level in range(5, 0, -1):
            qid = f"CSSRS{level}"
            verdict = self._is_yes(responses.get(qid))
            if verdict is True:
                highest = {
                    "level": level,
                    "question_id": qid,
                    "label": self.ideation_labels.get(level),
                }
                break
            if verdict is None and responses.get(qid) not in (None, ""):
                errors.append(f"{qid}: valeur '{responses.get(qid)}' non reconnue")
        return highest

    def _summarize_intensity(
        self, responses: Dict[str, Any], errors: List[str]
    ) -> Dict[str, Optional[Dict[str, Any]]]:
        return {
            "frequency": self._map_choice(responses, "CSSRS8", self.frequency_labels, errors),
            "duration": self._map_choice(responses, "CSSRS9", self.duration_labels, errors),
            "controllability": self._map_choice(
                responses, "CSSRS10", self.control_labels, errors
            ),
            "deterrents": self._map_choice(
                responses, "CSSRS11", self.deterrent_labels, errors
            ),
            "reasons": self._map_choice(responses, "CSSRS12", self.reason_labels, errors),
        }

    def _summarize_behavior(
        self, responses: Dict[str, Any], errors: List[str]
    ) -> Dict[str, Any]:
        attempt = self._validate_yes_no(responses, "CSSRS13", errors)
        interrupted = self._validate_yes_no(responses, "CSSRS16", errors)
        aborted = self._validate_yes_no(responses, "CSSRS31", errors)
        preparation = self._validate_yes_no(responses, "CSSRS20", errors)
        observed = self._validate_yes_no(responses, "CSSRS21", errors)
        nssi = self._validate_yes_no(responses, "CSSRS15", errors)

        return {
            "attempt": attempt,
            "attempt_details": self._clean_str(responses.get("CSSRS13BIS")),
            "attempt_count": self._to_int(responses, "CSSRS14", errors),
            "non_suicidal_self_injury": nssi,
            "interrupted_attempt": interrupted,
            "interrupted_details": self._clean_str(responses.get("CSSRS16BIS")),
            "interrupted_count": self._to_int(responses, "CSSRS29", errors),
            "aborted_attempt": aborted,
            "aborted_details": self._clean_str(responses.get("CSSRS29BIS")),
            "aborted_count": self._to_int(responses, "CSSRS30", errors),
            "preparatory_behavior": preparation,
            "preparatory_details": self._clean_str(responses.get("CSSRS20BIS")),
            "observed_by_clinician": observed,
        }

    def _summarize_observed_lethality(
        self, responses: Dict[str, Any], errors: List[str]
    ) -> Dict[str, Optional[Dict[str, Any]]]:
        return {
            "most_recent": self._lethality_entry(
                responses, "CSSRS22_D", "CSSRS22_C", self.medical_impact_labels, errors
            ),
            "most_lethal": self._lethality_entry(
                responses, "CSSRS23_D", "CSSRS23_C", self.medical_impact_labels, errors
            ),
            "first_attempt": self._lethality_entry(
                responses, "CSSRS24_D", "CSSRS24_C", self.medical_impact_labels, errors
            ),
        }

    def _summarize_potential_lethality(
        self, responses: Dict[str, Any], errors: List[str]
    ) -> Dict[str, Optional[Dict[str, Any]]]:
        return {
            "most_recent": self._impact_entry(
                responses, "CSSRS25_C", self.potential_impact_labels, errors
            ),
            "most_lethal": self._impact_entry(
                responses, "CSSRS27_C", self.potential_impact_labels, errors
            ),
            "first_attempt": self._impact_entry(
                responses, "CSSRS28_C", self.potential_impact_labels, errors
            ),
        }

    def _impact_entry(
        self,
        responses: Dict[str, Any],
        key: str,
        labels: Dict[int, str],
        errors: List[str],
    ) -> Optional[Dict[str, Any]]:
        impact = self._map_choice(responses, key, labels, errors)
        if impact is None:
            return None
        return {"code": impact["code"], "label": impact["label"]}

    def _lethality_entry(
        self,
        responses: Dict[str, Any],
        date_key: str,
        code_key: str,
        labels: Dict[int, str],
        errors: List[str],
    ) -> Optional[Dict[str, Any]]:
        date_value = self._clean_str(responses.get(date_key))
        impact = self._map_choice(responses, code_key, labels, errors)
        if date_value is None and impact is None:
            return None
        entry: Dict[str, Any] = {}
        if date_value is not None:
            entry["date"] = date_value
        if impact is not None:
            entry["impact"] = {"code": impact["code"], "label": impact["label"]}
        return entry if entry else None

    def _map_choice(
        self,
        responses: Dict[str, Any],
        key: str,
        labels: Dict[int, str],
        errors: List[str],
    ) -> Optional[Dict[str, Any]]:
        raw = responses.get(key)
        if raw is None or str(raw).strip() == "":
            return None
        try:
            code = int(str(raw).strip())
        except ValueError:
            errors.append(f"{key}: valeur '{raw}' non numérique")
            return None
        label = labels.get(code)
        if label is None:
            errors.append(f"{key}: code {code} inconnu")
            return {"code": code, "label": None}
        return {"code": code, "label": label}

    def _validate_yes_no(
        self, responses: Dict[str, Any], key: str, errors: List[str]
    ) -> Optional[bool]:
        verdict = self._is_yes(responses.get(key))
        if verdict is None and responses.get(key) not in (None, ""):
            errors.append(f"{key}: valeur '{responses.get(key)}' non reconnue")
        return verdict

    @staticmethod
    def _clean_str(value: Any) -> Optional[str]:
        if value is None:
            return None
        if isinstance(value, str):
            cleaned = value.strip()
            return cleaned or None
        return str(value)

    @staticmethod
    def _is_yes(value: Any) -> Optional[bool]:
        if value is None:
            return None
        if isinstance(value, bool):
            return value
        if isinstance(value, (int, float)):
            if value == 1:
                return True
            if value == 0:
                return False
            return bool(value)
        if isinstance(value, str):
            normalised = value.strip().lower()
            if normalised in {"1", "oui", "yes", "true", "vrai", "o", "y"}:
                return True
            if normalised in {"0", "non", "no", "false", "faux", "n"}:
                return False
        return None

    @staticmethod
    def _to_int(
        responses: Dict[str, Any], key: str, errors: List[str]
    ) -> Optional[int]:
        raw = responses.get(key)
        if raw is None or str(raw).strip() == "":
            return None
        try:
            return int(str(raw).strip())
        except ValueError:
            errors.append(f"{key}: valeur '{raw}' non numérique")
            return None


