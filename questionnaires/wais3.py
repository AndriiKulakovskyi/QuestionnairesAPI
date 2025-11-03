"""WAIS-III helper utilities used in the neuropsychological assessment flow."""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence, Tuple


DigitTrials = Sequence[Tuple[Optional[int], Optional[int]]]


@dataclass(frozen=True)
class ClinicalOption:
    label: str
    help_text: Optional[str] = None


class WAIS3Test:
    """Provide raw-score computations for WAIS-III and allied cognitive tests."""

    LATERALITY_CHOICES = ["Gaucher", "Droitier", "Ambidextre"]
    BOOLEAN_CHOICES = ["Oui", "Non"]
    BOOLEAN_WITH_UNKNOWN = ["Oui", "Non", "Ne sais pas"]

    VOCABULARY_ITEMS = 33
    MATRICES_ITEMS = 26
    COBRA_ITEMS = 16

    DIGIT_FORWARD_START = 2
    DIGIT_BACKWARD_START = 2

    def __init__(self):
        self.name = "WAIS-III"
        self.full_name = "Wechsler Adult Intelligence Scale - Third Edition (WAIS-III)"
        self.description = (
            "Calculs auxiliaires pour le bilan neuropsychologique WAIS-III/WAIS."
            " Les conversions normatives (notes standard / QI) restent soumises"
            " au manuel officiel ; cette classe se limite aux totaux bruts et"
            " agrégations logiques nécessaires dans l'application."
        )

    # ------------------------------------------------------------------
    # Clinical metadata helpers
    # ------------------------------------------------------------------
    def get_clinical_fields(self) -> Dict[str, List[str]]:
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

    def get_instructions(self) -> str:
        return (
            "Consignes : administrer les sous-tests WAIS-III selon les règles du manuel."
            " Saisir les notes brutes (0-1 ou 0-2 selon l'item). Les conversions vers les"
            " notes standard (moyenne 10, écart-type 3) nécessitent les tables normatives"
            " spécifiques à l'âge du patient. Cette implémentation calcule uniquement les"
            " totaux bruts, les agrégats et certains dérivés (empans, indices complémentaires)."
        )

    # ------------------------------------------------------------------
    # Vocabulaire (33 items, 0-2)
    # ------------------------------------------------------------------
    def calculate_vocabulary(self, item_scores: Sequence[int], standard_score: Optional[int] = None) -> Dict[str, Any]:
        if len(item_scores) != self.VOCABULARY_ITEMS:
            raise ValueError("WAIS-III Vocabulaire nécessite 33 items")
        if any(score not in (0, 1, 2) for score in item_scores):
            raise ValueError("Chaque item vocabulaire doit valoir 0, 1 ou 2")

        raw_total = sum(item_scores)
        result: Dict[str, Any] = {
            "raw_total": raw_total,
            "max_score": self.VOCABULARY_ITEMS * 2,
        }
        if standard_score is not None:
            result["standard_score"] = standard_score
            result["z_score"] = round((standard_score - 10) / 3, 2)
        return result

    # ------------------------------------------------------------------
    # Matrices (26 items 0/1)
    # ------------------------------------------------------------------
    def calculate_matrices(self, item_scores: Sequence[int], standard_score: Optional[int] = None) -> Dict[str, Any]:
        if len(item_scores) != self.MATRICES_ITEMS:
            raise ValueError("WAIS-III Matrices nécessite 26 items")
        if any(score not in (0, 1) for score in item_scores):
            raise ValueError("Matrices : réponses 0 ou 1")

        raw_total = sum(item_scores)
        result: Dict[str, Any] = {
            "raw_total": raw_total,
            "max_score": self.MATRICES_ITEMS,
            "completion_rate": raw_total / self.MATRICES_ITEMS,
        }
        if standard_score is not None:
            result["standard_score"] = standard_score
            result["z_score"] = round((standard_score - 10) / 3, 2)
        return result

    # ------------------------------------------------------------------
    # Code & Symboles
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

        if min(code_correct, code_incorrect, symbol_correct, symbol_incorrect) < 0:
            raise ValueError("Les comptes ne peuvent pas être négatifs")

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
    # Digit Span WAIS-III (forward/backward)
    # ------------------------------------------------------------------
    def calculate_digit_span(
        self,
        forward_trials: DigitTrials,
        backward_trials: DigitTrials,
        standard_scores: Optional[Dict[str, Optional[int]]] = None,
    ) -> Dict[str, Any]:

        def _compute(trials: DigitTrials, start_length: int) -> Dict[str, Any]:
            lengths = [start_length + i for i in range(len(trials))]
            item_scores: List[int] = []
            total = 0
            max_span: Optional[float] = None

            for idx, (trial1, trial2) in enumerate(trials):
                for value in (trial1, trial2):
                    if value not in (0, 1, None):
                        raise ValueError("Les essais doivent valoir 0, 1 ou None")
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

        total_raw = forward["raw_total"] + backward["raw_total"]

        result = {
            "forward": forward,
            "backward": backward,
            "total_raw": total_raw,
            "span_difference": None,
        }

        if forward["max_span"] is not None and backward["max_span"] is not None:
            result["span_difference"] = round(forward["max_span"] - backward["max_span"], 2)

        if standard_scores:
            result["standard_scores"] = standard_scores

        return result

    # ------------------------------------------------------------------
    # CVLT, COBRA, TMT, Stroop, Fluences, SCIP – same helpers as WAIS-IV
    # ------------------------------------------------------------------
    def calculate_cvlt(self, raw_scores: Dict[str, Optional[float]]) -> Dict[str, Any]:
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

    def calculate_cobra(self, responses: Sequence[int]) -> Dict[str, Any]:
        if len(responses) != self.COBRA_ITEMS:
            raise ValueError("COBRA nécessite 16 items")
        if any(response not in (0, 1, 2, 3) for response in responses):
            raise ValueError("COBRA : valeurs de 0 à 3")

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

    def calculate_trail_making(self, data: Dict[str, Optional[float]]) -> Dict[str, Any]:
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

    def calculate_stroop(self, plates: Dict[str, Dict[str, Optional[int]]]) -> Dict[str, Any]:
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

    def calculate_fluences(
        self,
        letter_data: Dict[str, Optional[int]],
        category_data: Dict[str, Optional[int]],
    ) -> Dict[str, Any]:
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

    def calculate_scip(self, subtests: Dict[str, Dict[str, Optional[float]]]) -> Dict[str, Any]:
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
    # Example usage
    wais3 = WAIS3Test()
    
    print(f"Test: {wais3.full_name}")
    print(f"Number of subtests: {len(wais3.subtests)}\n")
    
    print("Subtests by Index:")
    for index_name, subtests in wais3.indices.items():
        print(f"\n{index_name}:")
        for subtest in subtests:
            print(f"  - {wais3.subtests[subtest]['name']}")
    
    # Example: Calculate raw scores for Picture Completion subtest
    print("\n" + "="*80)
    print("EXAMPLE: Picture Completion Subtest")
    print("="*80)
    
    # Simulate responses (25 items, each scored 0 or 1)
    pic_comp_responses = {f"picture_completion_{i}": 1 if i <= 20 else 0 for i in range(1, 26)}
    
    raw_score = wais3.calculate_subtest_raw_score("picture_completion", pic_comp_responses)
    print(f"Raw score: {raw_score}/25")
    print(f"Scaled score: {wais3.raw_to_scaled_score('picture_completion', raw_score, 30)}")
    print("Note: Scaled score requires normative tables from WAIS-III manual")
    
    # Example: Calculate all scores
    print("\n" + "="*80)
    print("EXAMPLE: Full Battery Scoring Structure")
    print("="*80)
    
    # Simulate complete battery responses  
    all_responses = {}
    # Picture Completion (25 items)
    for i in range(1, 26):
        all_responses[f"picture_completion_{i}"] = 1 if i <= 18 else 0
    # Vocabulary (33 items, 0-2 points each)
    for i in range(1, 34):
        all_responses[f"vocabulary_{i}"] = 2 if i <= 10 else (1 if i <= 25 else 0)
    # Add more subtests as needed...
    
    results = wais3.calculate_scores(all_responses, age=30)
    
    print("\nRaw Scores:")
    for subtest, score in results["raw_scores"].items():
        if score is not None:
            print(f"  {wais3.subtests[subtest]['name']}: {score}")
    
    print("\nIndex Scores:")
    for index, score in results["index_scores"].items():
        print(f"  {index}: {score if score else 'Requires normative tables'}")
    
    print(f"\nNote: {results['note']}")

