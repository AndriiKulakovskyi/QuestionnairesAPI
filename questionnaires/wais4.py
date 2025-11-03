"""Utilities for handling WAIS-IV (Wechsler Adult Intelligence Scale - 4e édition).

This module centralises the recurring calculations used in the neuropsychological
assessment workflow (subtests WAIS-IV, questionnaires complémentaires ainsi que
quelques tests associés). Les normes complètes et tables de conversion restent
couverts par le manuel officiel ; ici nous gérons uniquement les calculs
arithmétiques issus des données brutes collectées dans l'application."""

from dataclasses import dataclass
from typing import Dict, Any, List, Optional, Sequence, Tuple


DigitTrials = Sequence[Tuple[Optional[int], Optional[int]]]


@dataclass(frozen=True)
class ClinicalOption:
    label: str
    help_text: Optional[str] = None


class WAIS4Test:
    """Helper for WAIS-IV subtests and associated cognitive batteries."""

    LATERALITY_CHOICES = ["Gaucher", "Droitier", "Ambidextre"]
    BOOLEAN_CHOICES = ["Oui", "Non"]
    BOOLEAN_WITH_UNKNOWN = ["Oui", "Non", "Ne sais pas"]

    DIGIT_FORWARD_START = 2
    DIGIT_BACKWARD_START = 2
    DIGIT_SEQUENCING_START = 3

    def __init__(self):
        self.name = "WAIS-IV"
        self.full_name = "Wechsler Adult Intelligence Scale - Fourth Edition (WAIS-IV)"
        self.description = (
            "Batterie d'évaluation cognitive de l'adulte (4e édition)."
            " Cette implémentation fournit des outils de calcul pour les sous-tests"
            " collectés dans l'application clinique, sans se substituer aux tables"
            " officielles de conversion standardisée."
        )

    # ------------------------------------------------------------------
    # Clinical metadata utilities
    # ------------------------------------------------------------------
    def get_clinical_fields(self) -> Dict[str, List[str]]:
        """Return enumerations used for the clinical criteria dropdowns."""
        return {
            "laterality": self.LATERALITY_CHOICES,
            "language_french": self.BOOLEAN_CHOICES,
            "normothymic": self.BOOLEAN_CHOICES,
            "recent_episode_absent": self.BOOLEAN_CHOICES,
            "socio_professional_data": self.BOOLEAN_CHOICES,
            "daltonism_absent": self.BOOLEAN_CHOICES,
            "hearing_issue_absent": self.BOOLEAN_CHOICES,
            "no_ect_last_year": self.BOOLEAN_CHOICES,
            "accepted_for_assessment": self.BOOLEAN_CHOICES,
        }

    def get_learning_trouble_fields(self) -> Dict[str, List[str]]:
        """Return choices for developmental/learning disorders checklist."""
        keys = [
            "dyslexie",
            "dysorthographie",
            "dyscalculie",
            "dysphasie",
            "dyspraxie",
            "retard_parole",
            "begaiement",
            "retard_marche",
            "convulsions_febriles",
            "precocite",
        ]
        return {key: self.BOOLEAN_WITH_UNKNOWN for key in keys}

    # ------------------------------------------------------------------
    # WAIS-IV Matrices
    # ------------------------------------------------------------------
    def calculate_matrices(self, item_scores: Sequence[int], standard_score: Optional[int] = None) -> Dict[str, Any]:
        """Compute WAIS-IV Matrix Reasoning raw total and optional standard score.

        Args:
            item_scores: iterable of 26 binary scores (0/1)
            standard_score: optional scaled score (mean 10, SD 3) provided by clinician

        Returns:
            Dictionary with raw total, completion ratio and (optionally) z-score.
        """

        if len(item_scores) != 26:
            raise ValueError("WAIS Matrices requires 26 item scores")

        if any(score not in (0, 1) for score in item_scores):
            raise ValueError("Matrices scores must be 0 or 1")

        raw_total = sum(item_scores)
        result: Dict[str, Any] = {
            "raw_total": raw_total,
            "max_score": 26,
            "completion_rate": raw_total / 26.0,
        }

        if standard_score is not None:
            result["standard_score"] = standard_score
            result["z_score"] = round((standard_score - 10) / 3, 2)

        return result

    # ------------------------------------------------------------------
    # Processing speed (Code & Symboles)
    # ------------------------------------------------------------------
    def calculate_processing_speed(
        self,
        code_correct: int,
        code_incorrect: int,
        symbol_correct: int,
        symbol_incorrect: int,
        code_standard: Optional[int] = None,
        symbol_standard: Optional[int] = None,
        index_standard: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Aggregate information for Coding & Symbol Search subtests."""

        if min(code_correct, code_incorrect, symbol_correct, symbol_incorrect) < 0:
            raise ValueError("Counts cannot be negative")

        code_raw = code_correct
        symbols_raw = symbol_correct

        result = {
            "code": {
                "raw_correct": code_correct,
                "raw_incorrect": code_incorrect,
                "raw_total": code_raw,
                "standard_score": code_standard,
            },
            "symboles": {
                "raw_correct": symbol_correct,
                "raw_incorrect": symbol_incorrect,
                "raw_total": symbols_raw,
                "standard_score": symbol_standard,
            },
        }

        if code_standard is not None and symbol_standard is not None:
            result["composite"] = {
                "standard_sum": code_standard + symbol_standard,
                "index_standard": index_standard,
            }
        else:
            result["composite"] = {
                "standard_sum": None,
                "index_standard": index_standard,
            }

        return result

    # ------------------------------------------------------------------
    # Digit span (Mémoire des chiffres)
    # ------------------------------------------------------------------
    def calculate_digit_span(
        self,
        forward_trials: DigitTrials,
        backward_trials: DigitTrials,
        sequencing_trials: DigitTrials,
        standard_scores: Optional[Dict[str, Optional[int]]] = None,
    ) -> Dict[str, Any]:
        """Compute raw results for the Digit Span subtest (forward/backward/sequencing)."""

        def _compute(trials: DigitTrials, start_length: int) -> Dict[str, Any]:
            lengths = [start_length + i for i in range(len(trials))]
            item_scores: List[int] = []
            total = 0
            max_span: Optional[float] = None

            for idx, (trial1, trial2) in enumerate(trials):
                for value in (trial1, trial2):
                    if value not in (0, 1, None):
                        raise ValueError("Digit span trials must be 0, 1 or None")
                score = (trial1 or 0) + (trial2 or 0)
                item_scores.append(score)
                total += score

                length = lengths[idx]
                if score == 2:
                    max_span = length
                elif score == 1 and (max_span is None or length - 0.5 > max_span):
                    max_span = length - 0.5

            return {
                "item_scores": item_scores,
                "raw_total": total,
                "max_span": max_span,
            }

        forward = _compute(forward_trials, self.DIGIT_FORWARD_START)
        backward = _compute(backward_trials, self.DIGIT_BACKWARD_START)
        sequencing = _compute(sequencing_trials, self.DIGIT_SEQUENCING_START)

        total_raw = forward["raw_total"] + backward["raw_total"] + sequencing["raw_total"]

        result = {
            "forward": forward,
            "backward": backward,
            "sequencing": sequencing,
            "total_raw": total_raw,
            "span_difference": None,
        }

        if forward["max_span"] is not None and backward["max_span"] is not None:
            result["span_difference"] = round(forward["max_span"] - backward["max_span"], 2)

        if standard_scores:
            result["standard_scores"] = standard_scores

        return result

    # ------------------------------------------------------------------
    # CVLT (California Verbal Learning Test) helper
    # ------------------------------------------------------------------
    def calculate_cvlt(self, raw_scores: Dict[str, Optional[float]]) -> Dict[str, Any]:
        """Summarise CVLT outcomes from the raw entries."""

        learning_trials = [raw_scores.get(f"rappel{i}") for i in range(1, 6)]
        learning_values = [int(value) for value in learning_trials if value is not None]
        total_learning = sum(learning_values)

        result: Dict[str, Any] = {
            "total_learning": total_learning,
            "mean_learning": total_learning / len(learning_values) if learning_values else None,
            "short_delay_free": raw_scores.get("rappel_libre_court"),
            "short_delay_cued": raw_scores.get("rappel_indice_court"),
            "long_delay_free": raw_scores.get("rappel_libre_long"),
            "long_delay_cued": raw_scores.get("rappel_indice_long"),
            "recognition": {
                "correct": raw_scores.get("reconnaissances_correctes"),
                "false_positives": raw_scores.get("fausses_reconnaissances"),
                "discriminability": raw_scores.get("discriminabilite"),
            },
            "perseverations": raw_scores.get("total_perseverations"),
            "intrusions": raw_scores.get("total_intrusions"),
            "semantic_clustering": raw_scores.get("indice_regroupement_semantique"),
            "serial_clustering": raw_scores.get("indice_regroupement_seriel"),
            "primacy": raw_scores.get("primacy"),
            "recency": raw_scores.get("recency"),
            "bias": raw_scores.get("biais"),
            "delay_minutes": raw_scores.get("delai_minutes"),
        }

        if learning_values:
            result["learning_slope"] = learning_values[-1] - learning_values[0]
        else:
            result["learning_slope"] = None

        return result

    # ------------------------------------------------------------------
    # COBRA questionnaire
    # ------------------------------------------------------------------
    def calculate_cobra(self, responses: Sequence[int]) -> Dict[str, Any]:
        """Compute total COBRA score (16 items, 0-3 chacune)."""

        if len(responses) != 16:
            raise ValueError("COBRA requires 16 responses")
        if any(response not in (0, 1, 2, 3) for response in responses):
            raise ValueError("COBRA responses must be between 0 and 3")

        total = sum(responses)

        if total <= 15:
            interpretation = "Plaintes cognitives faibles"
        elif total <= 31:
            interpretation = "Plaintes cognitives modérées"
        else:
            interpretation = "Plaintes cognitives sévères"

        return {
            "total": total,
            "max_score": 48,
            "interpretation": interpretation,
        }

    # ------------------------------------------------------------------
    # Trail Making Test (TMT)
    # ------------------------------------------------------------------
    def calculate_trail_making(self, data: Dict[str, Optional[float]]) -> Dict[str, Any]:
        """Aggregate Trail Making A/B metrics."""

        time_a = data.get("time_a")
        time_b = data.get("time_b")
        errors_a_total = self._safe_sum(data.get("errors_a_corrected"), data.get("errors_a_uncorrected"))
        errors_b_total = self._safe_sum(data.get("errors_b_corrected"), data.get("errors_b_uncorrected"))

        diff_time = None
        if time_a is not None and time_b is not None:
            diff_time = time_b - time_a

        diff_errors = None
        if errors_a_total is not None and errors_b_total is not None:
            diff_errors = errors_b_total - errors_a_total

        return {
            "part_a": {
                "time": time_a,
                "errors_total": errors_a_total,
            },
            "part_b": {
                "time": time_b,
                "errors_total": errors_b_total,
                "perseverative_errors": data.get("perseverative_errors"),
            },
            "difference": {
                "time_b_minus_a": diff_time,
                "errors_b_minus_a": diff_errors,
            },
        }

    # ------------------------------------------------------------------
    # Stroop (Golden version)
    # ------------------------------------------------------------------
    def calculate_stroop(self, plates: Dict[str, Dict[str, Optional[int]]]) -> Dict[str, Any]:
        """Summarise Stroop plate performances."""

        result: Dict[str, Any] = {}
        for plate_name in ("A", "B", "C"):
            plate_key = f"plate_{plate_name.lower()}"
            data = plates.get(plate_key, {})
            result[plate_key] = {
                "raw_total": data.get("raw"),
                "age_corrected": data.get("age_corrected"),
                "errors_corrected": data.get("errors_corrected"),
                "errors_uncorrected": data.get("errors_uncorrected"),
                "t_score": data.get("t_score"),
                "z_score": data.get("z_score"),
            }

        interference = plates.get("interference", {})
        result["interference"] = {
            "t_score": interference.get("t_score"),
            "z_score": interference.get("z_score"),
        }
        return result

    # ------------------------------------------------------------------
    # Fluences verbales (Cardebat)
    # ------------------------------------------------------------------
    def calculate_fluences(
        self,
        letter_data: Dict[str, Optional[int]],
        category_data: Dict[str, Optional[int]],
    ) -> Dict[str, Any]:
        """Return summary for phonemic and semantic fluency."""

        def _summary(data: Dict[str, Optional[int]]) -> Dict[str, Any]:
            total = data.get("total_correct")
            return {
                "total_correct": total,
                "percentile": data.get("percentile"),
                "z_score": data.get("z_score"),
                "perseverations": data.get("perseverations"),
                "derived_words": data.get("derived_words"),
                "intrusions": data.get("intrusions"),
                "proper_nouns": data.get("proper_nouns"),
                "rule_breaks": data.get("rule_breaks"),
                "clusters_count": data.get("clusters_count"),
                "cluster_size_mean": data.get("cluster_size_mean"),
                "switch_count": data.get("switch_count"),
            }

        return {
            "letter": _summary(letter_data),
            "category": _summary(category_data),
        }

    # ------------------------------------------------------------------
    # SCIP summary
    # ------------------------------------------------------------------
    def calculate_scip(self, subtests: Dict[str, Dict[str, Optional[float]]]) -> Dict[str, Any]:
        """Compile SCIP module scores (Version 1/2/3)."""

        return {
            name: {
                "raw_total": values.get("raw"),
                "z_score": values.get("z"),
            }
            for name, values in subtests.items()
        }

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _safe_sum(*values: Optional[float]) -> Optional[float]:
        filtered = [value for value in values if value is not None]
        if not filtered:
            return None
        return sum(filtered)


if __name__ == '__main__':
    wais4 = WAIS4Test()
    print(f"Test: {wais4.full_name}")
    print(f"Core subtests: {len(wais4.core_subtests)}")
    print(f"Supplemental subtests: {len(wais4.supplemental_subtests)}")
    print("\nIndices:")
    for idx, subtests in wais4.indices.items():
        print(f"  {idx}: {', '.join(subtests)}")

