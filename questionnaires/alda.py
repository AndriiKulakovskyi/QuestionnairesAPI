import random
from typing import Any, Dict, List

class AldaScaleQuestionnaire:
    """Alda Scale - Retrospective assessment of lithium response
    
    The Alda Scale assesses the quality of prophylactic response to lithium treatment
    in patients with bipolar disorder. It consists of an initial screening question and
    two criteria:
    
    **Question 0**: "Le patient est-il actuellement traité par lithium ?" (Oui/Non)
    - If "Non", the questionnaire is not applicable and no score is computed.
    
    **Criterion A**: Degree of improvement (0-10 scale)
    - Assesses clinical improvement while on lithium
    - Higher scores indicate better response
    
    **Criterion B**: Five confounding factors (each scored 0-2)
    - B1: Number of episodes before treatment
    - B2: Frequency of episodes before treatment  
    - B3: Duration of treatment
    - B4: Compliance during stability periods
    - B5: Use of additional medication during stability
    - Lower scores indicate fewer confounding factors
    
    **Final Score**: A - B (minimum 0, maximum 10)
    - Score ≥ 7: Répondeur au lithium
    - Score 4-6: Réponse partielle
    - Score < 4: Réponse insuffisante
    """

    def __init__(self):
        self.name = "Alda Scale - Lithium Response Assessment"
        self.description = "Évaluation rétrospective de la réponse au lithium dans le trouble bipolaire."
        self.used_in_applications = ['ebipolar']
        self.screening_question = self._init_screening_question()
        self.criterion_a = self._init_criterion_a()
        self.criterion_b = self._init_criterion_b()

    def _init_screening_question(self) -> Dict[str, Any]:
        """Initialise the prerequisite lithium treatment question."""
        return {
            "id": "ALDA_ON_LITHIUM",
            "text": "Le patient est-il actuellement traité par lithium ?",
            "type": "yes_no",
            "options": {"Oui": True, "Non": False}
        }

    def _init_criterion_a(self) -> Dict[str, Any]:
        """Initialize Criterion A - degree of improvement."""
        
        descriptions = {
            10: "Réponse complète, aucune récurrence mais le patient peut encore avoir des symptômes résiduels et récupération fonctionnelle totale",
            9: "Très bonne réponse, aucune récurrence mais le patient peut encore avoir des symptômes résiduels minimes (anxiété passagère, perturbation du sommeil, dysphorie, irritabilité) n'exigeant aucune intervention",
            8: "Très bonne réponse. L'activité de la maladie réduite de plus de 90%",
            7: "Bonne réponse. Réduction de l'activité de maladie de 80-90%",
            6: "Bonne réponse. Réduction de l'activité de maladie de 65-80%",
            5: "Bonne modérée. Réduction de l'activité de maladie de 50-65%",
            4: "Amélioration modérée. Réduction de l'activité de maladie de 35-50%",
            3: "Amélioration légère. Réduction de l'activité de maladie de 20-35%",
            2: "Amélioration légère. Réduction de l'activité de maladie de 10-20%",
            1: "Amélioration minime. Réduction de l'activité de maladie de 0-10%",
            0: "Aucun changement, ni péjoration"
        }
        
        return {
            "id": "ALDA_A",
            "text": "Critère A - Degré d'amélioration clinique sous lithium",
            "instruction": (
                "Le critère A est utilisé pour déterminer une association entre amélioration "
                "clinique et le traitement. La cotation devrait porter sur la période pendant "
                "laquelle le traitement était considéré adéquat quant à la durée et au dosage. "
                "L'activité de la maladie devrait être jugée selon la fréquence, la sévérité "
                "et la durée des épisodes."
            ),
            "options": descriptions,
            "score_range": (0, 10)
        }

    def _init_criterion_b(self) -> List[Dict[str, Any]]:
        """Initialize Criterion B - confounding factors."""
        
        items = [
            {
                "id": "ALDA_B1",
                "text": "B1: Nombre d'épisodes avant le traitement",
                "options": {
                    0: "4 épisodes ou plus",
                    1: "2 ou 3 épisodes",
                    2: "1 épisode"
                }
            },
            {
                "id": "ALDA_B2",
                "text": "B2: Fréquence des épisodes avant le traitement",
                "options": {
                    0: "Moyenne à élevée, incluant les cycles rapides",
                    1: "Faible, rémissions spontanées de 3 ans ou plus en moyenne",
                    2: "1 seul épisode, risque de récurrence ne peut être établi"
                }
            },
            {
                "id": "ALDA_B3",
                "text": "B3: Durée du traitement",
                "options": {
                    0: "2 ans ou plus",
                    1: "1-2 ans",
                    2: "Moins d'un an"
                }
            },
            {
                "id": "ALDA_B4",
                "text": "B4: Compliance durant la/les période(s) de stabilité",
                "options": {
                    0: "Excellente, documentée par des taux dans les limites thérapeutiques",
                    1: "Bonne, plus de 80% des taux dans les limites thérapeutiques",
                    2: "Pauvre, répétitivement hors traitements, moins de 80% des taux dans les limites thérapeutiques"
                }
            },
            {
                "id": "ALDA_B5",
                "text": "B5: Usage de médication additionnelle durant la phase de stabilité",
                "options": {
                    0: "Aucun hormis de rares somnifères (1 par semaine ou moins); pas d'autres stabilisateurs pour contrôler les symptômes thymiques",
                    1: "Antidépresseurs ou antipsychotiques à faible dose comme une sécurité, ou recours prolongé à des somnifères",
                    2: "Usage prolongé ou systématique d'un antidépresseur ou antipsychotique"
                }
            }
        ]
        
        return items

    def calculate_score(self, responses: Dict[str, int]) -> Dict[str, Any]:
        """
        Calculate Alda Scale score.

        Args:
            responses (Dict[str, int]): A dictionary of responses containing:
                - "ALDA_ON_LITHIUM": "Oui" or "Non"
                - "ALDA_A": Score for Criterion A (0-10)
                - "ALDA_B1" through "ALDA_B5": Scores for Criterion B items (0-2 each)

        Returns:
            Dict[str, Any]: A dictionary containing scores and interpretation.
        """
        errors: List[str] = []
        screening = responses.get("ALDA_ON_LITHIUM")
        if screening is None:
            errors.append("Question préalable manquante: traitement actuel par lithium")
        elif screening not in ("Oui", "Non"):
            errors.append("La réponse à 'ALDA_ON_LITHIUM' doit être 'Oui' ou 'Non'")
        elif screening == "Non":
            return {
                "valid": False,
                "errors": [
                    "Questionnaire non applicable: le patient n'est pas actuellement traité par lithium"
                ],
                "score_a": None,
                "score_b": None,
                "total_score": None,
                "max_score": 10,
                "b_scores": {},
                "response_category": None,
                "interpretation": "Le calcul du score Alda requiert un traitement en cours par lithium"
            }

        # Validate Criterion A
        score_a = responses.get("ALDA_A")
        if score_a is None:
            errors.append("Critère A manquant (ALDA_A)")
        elif not isinstance(score_a, int) or score_a < 0 or score_a > 10:
            errors.append("Le score du critère A doit être un entier entre 0 et 10")
        
        # Validate and sum Criterion B
        score_b = 0
        b_scores = {}
        for item in self.criterion_b:
            item_id = item["id"]
            item_score = responses.get(item_id)
            if item_score is None:
                errors.append(f"Réponse manquante pour {item_id}")
                continue
            if not isinstance(item_score, int) or item_score < 0 or item_score > 2:
                errors.append(f"{item_id} doit être un entier entre 0 et 2")
                continue

            b_scores[item_id] = item_score
            score_b += item_score

        if errors:
            return {
                "valid": False,
                "errors": errors,
                "score_a": score_a if isinstance(score_a, int) and 0 <= score_a <= 10 else None,
                "score_b": None,
                "total_score": None,
                "max_score": 10,
                "b_scores": b_scores,
                "response_category": None,
                "interpretation": "Validation échouée"
            }
        
        # Calculate final score (A - B, minimum 0)
        assert isinstance(score_a, int)
        total_score = max(0, score_a - score_b)
        
        # Interpret response
        if total_score >= 7:
            response_category = "Répondeur au lithium"
            interpretation = "Réponse excellente au lithium (score ≥ 7)"
        elif total_score >= 4:
            response_category = "Réponse partielle"
            interpretation = "Réponse partielle au lithium (score 4-6)"
        else:
            response_category = "Réponse insuffisante"
            interpretation = "Réponse faible ou absente au lithium (score < 4)"
        
        return {
            "valid": True,
            "errors": [],
            "score_a": score_a,
            "score_b": score_b,
            "total_score": total_score,
            "max_score": 10,
            "b_scores": b_scores,
            "response_category": response_category,
            "interpretation": interpretation
        }

    def get_random_responses(self) -> Dict[str, int]:
        """Generates random valid responses for testing purposes."""
        responses = {
            "ALDA_ON_LITHIUM": "Oui",
            "ALDA_A": random.randint(0, 10)
        }
        for item in self.criterion_b:
            responses[item["id"]] = random.randint(0, 2)
        return responses

    def get_instructions(self) -> str:
        """Returns the full instruction text for the questionnaire."""
        return (
            "CONSIGNES\n\n"
            "Le patient est-il actuellement traité par lithium ? Répondre « Oui » ou « Non ».\n"
            "Si la réponse est « Non », le questionnaire s'arrête ici.\n\n"
            f"{self.criterion_a['instruction']}\n\n"
            "CONSIGNES\n"
            "Le critère B est utilisé pour établir s'il y a une relation causale entre l'amélioration "
            "clinique et le traitement. Coter 0, 1 ou 2 points pour chacun des items suivants, où des "
            "scores plus élevés indiquent des facteurs confondants plus importants."
        )


if __name__ == '__main__':
    alda = AldaScaleQuestionnaire()
    print(f"Questionnaire: {alda.name}")
    print(f"Description: {alda.description}")
    print(f"Used in applications: {alda.used_in_applications}")
    print()
    print("="*80)
    print("INSTRUCTION:")
    print(alda.get_instructions())
    print("="*80)
    print()
    
    print("Criterion A Options:")
    for score, desc in alda.criterion_a["options"].items():
        print(f"  {score}: {desc[:80]}...")
    print()
    
    print("Criterion B Items:")
    for item in alda.criterion_b:
        print(f"\n{item['text']}:")
        for score, desc in item["options"].items():
            print(f"  {score}: {desc}")
    print()
    print("="*80)
    
    # Test with excellent responder profile
    print("\nExample 1: Excellent responder")
    excellent_response = {
        "ALDA_A": 10,  # Complete response
        "ALDA_B1": 0,  # 4+ episodes before (no confounding)
        "ALDA_B2": 0,  # High frequency before (no confounding)
        "ALDA_B3": 0,  # 2+ years treatment (no confounding)
        "ALDA_B4": 0,  # Excellent compliance (no confounding)
        "ALDA_B5": 0   # No additional meds (no confounding)
    }
    result = alda.calculate_score(excellent_response)
    print(f"Score A: {result['score_a']}")
    print(f"Score B: {result['score_b']}")
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Category: {result['response_category']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    
    # Test with partial responder profile
    print("Example 2: Partial responder")
    partial_response = {
        "ALDA_A": 7,   # Good response
        "ALDA_B1": 1,  # 2-3 episodes before
        "ALDA_B2": 1,  # Low frequency
        "ALDA_B3": 1,  # 1-2 years treatment
        "ALDA_B4": 0,  # Excellent compliance
        "ALDA_B5": 1   # Some additional meds
    }
    result = alda.calculate_score(partial_response)
    print(f"Score A: {result['score_a']}")
    print(f"Score B: {result['score_b']}")
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Category: {result['response_category']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    
    # Test with non-responder profile
    print("Example 3: Non-responder")
    non_response = {
        "ALDA_A": 2,   # Minimal improvement
        "ALDA_B1": 2,  # Only 1 episode (high confounding)
        "ALDA_B2": 2,  # Can't establish recurrence risk
        "ALDA_B3": 2,  # Short treatment duration
        "ALDA_B4": 2,  # Poor compliance
        "ALDA_B5": 2   # Prolonged additional meds
    }
    result = alda.calculate_score(non_response)
    print(f"Score A: {result['score_a']}")
    print(f"Score B: {result['score_b']}")
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Category: {result['response_category']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    
    # Test with random responses
    print("Example 4: Random responses")
    random_responses = alda.get_random_responses()
    result = alda.calculate_score(random_responses)
    print(f"Score A: {result['score_a']}")
    print(f"Score B: {result['score_b']}")
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Category: {result['response_category']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    
    print("="*80)
    print("✓ Alda Scale implementation complete")
    print("  - Criterion A: Clinical improvement (0-10)")
    print("  - Criterion B: Confounding factors (5 items, 0-2 each)")
    print("  - Final score: A - B (minimum 0)")
    print("  - Clinical interpretation thresholds")

