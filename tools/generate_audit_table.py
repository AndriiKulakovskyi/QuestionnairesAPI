"""Generate a TODO audit table for all registered questionnaires."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = ROOT.parent

if str(PACKAGE_ROOT) not in sys.path:
    sys.path.insert(0, str(PACKAGE_ROOT))

from QuestionnairesAPI.core.registry import QuestionnaireRegistry
import QuestionnairesAPI.questionnaires  # noqa: F401  # auto-registers all questionnaires

DEFAULT_STATUS = "NOT_AUDITED"
DEFAULT_NOTES = "Audit clinique requis (questions et barème)."

STATUS_OVERRIDES: Dict[str, Dict[str, str]] = {
    "EQ_5D_5L": {
        "status": "SCORING_PENDING",
        "notes": "Index EQ-5D-5L requiert la table de valeurs française et le score EVA.",
    },
    "ALTMAN": {
        "status": "DATA_MISSING",
        "notes": "Implémentation actuelle partielle (questions 1-2 manquantes).",
    },
    "YMRS": {
        "status": "REVIEW_REQUIRED",
        "notes": "Nouvelle version pondérée : vérifier la traduction clinique.",
    },
}


def normalise_override_key(code: str) -> str:
    return code.upper()


def get_status(code: str) -> Dict[str, str]:
    return STATUS_OVERRIDES.get(normalise_override_key(code), {})


def build_table() -> str:
    registry = QuestionnaireRegistry()
    headers = ["Code", "Nom", "Items", "Stratégie", "Statut", "Notes"]
    rows = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]

    for code in registry.list_all():
        questionnaire_class = registry.get(code)
        if not questionnaire_class:
            continue

        instance = questionnaire_class()
        scoring = instance.scoring_strategy
        scoring_name = type(scoring).__name__ if scoring else "None"

        override = get_status(code)
        status = override.get("status", DEFAULT_STATUS)
        notes = override.get("notes", DEFAULT_NOTES)

        rows.append(
            "| {code} | {name} | {items} | {strategy} | {status} | {notes} |".format(
                code=instance.code,
                name=instance.name,
                items=len(instance.questions),
                strategy=scoring_name,
                status=status,
                notes=notes,
            )
        )

    return "\n".join(rows)


def main() -> None:
    table = build_table()
    output_path = Path("TODO.md")
    header = [
        "# Questionnaire Audit Backlog",
        "",
        "Ce tableau dresse la liste complète des questionnaires enregistrés,",
        "leur nombre d’items, la stratégie de scoring utilisée et l’état actuel",
        "de la vérification clinique.",
        "",
    ]
    output_path.write_text("\n".join(header + [table]) + "\n", encoding="utf-8")
    print(f"Wrote audit table to {output_path.resolve()}")


if __name__ == "__main__":
    main()

