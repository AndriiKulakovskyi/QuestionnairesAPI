import random
from typing import Any, Dict, List

class PTSDQuestionnaire:
    """PTSD Checklist (PCL)
    
    Self-report questionnaire measuring PTSD symptoms based on DSM criteria.
    
    Structure:
    - 17 items assessing 3 symptom clusters:
      • Re-experiencing (items 1-5)
      • Avoidance (items 6-12)
      • Hyperarousal (items 13-17)
    
    Scoring:
    - Each item: 1-5 scale
      1 = "Pas du tout" (Not at all)
      2 = "Un peu" (A little bit)
      3 = "Parfois" (Moderately)
      4 = "Souvent" (Quite a bit)
      5 = "Très souvent" (Extremely)
    - Total score: 17-85
    
    Interpretation:
    - Clinical cutoff: ≥ 44 suggests PTSD
    - Symptom severity:
      • Minimal: 17-29
      • Mild: 30-44
      • Moderate: 45-59
      • Severe: 60-85
    
    Clinical Use:
    - PTSD screening and assessment
    - Symptom severity monitoring
    - Treatment outcome evaluation
    """

    def __init__(self):
        self.name = "PTSD Checklist (PCL)"
        self.description = "Liste de vérification du syndrome de stress post-traumatique."
        self.num_items = 17
        self.used_in_applications = ['cedr']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 17 PTSD items."""
        
        questions = [
            {
                "id": "PTSD1",
                "number": 1,
                "text": "Etre perturbé(e) par des souvenirs, des pensées ou des images en relation avec cet épisode stressant.",
                "cluster": "re-experiencing",
                "options": {
                    "Pas du tout": 1,
                    "Un peu": 2,
                    "Parfois": 3,
                    "Souvent": 4,
                    "Très souvent": 5
                }
            },
            {
                "id": "PTSD2",
                "number": 2,
                "text": "Etre perturbé(e) par des rêves répétés en relation avec cet événement",
                "cluster": "re-experiencing",
                "options": {
                    "Pas du tout": 1,
                    "Un peu": 2,
                    "Parfois": 3,
                    "Souvent": 4,
                    "Très souvent": 5
                }
            },
            {
                "id": "PTSD3",
                "number": 3,
                "text": "Brusquement agir ou sentir comme si l'épisode stressant se reproduisait (comme si vous étiez en train de le revivre)",
                "cluster": "re-experiencing",
                "options": {
                    "Pas du tout": 1,
                    "Un peu": 2,
                    "Parfois": 3,
                    "Souvent": 4,
                    "Très souvent": 5
                }
            },
            {
                "id": "PTSD4",
                "number": 4,
                "text": "Se sentir très bouleversé(e) lorsque quelque chose vous rappelle l'épisode stressant",
                "cluster": "re-experiencing",
                "options": {
                    "Pas du tout": 1,
                    "Un peu": 2,
                    "Parfois": 3,
                    "Souvent": 4,
                    "Très souvent": 5
                }
            },
            {
                "id": "PTSD5",
                "number": 5,
                "text": "Avoir des réactions physiques, par exemple, battements de coeur, difficultés à respirer, sueurs lorsque quelque chose vous a rappelé l'épisode stressant",
                "cluster": "re-experiencing",
                "options": {
                    "Pas du tout": 1,
                    "Un peu": 2,
                    "Parfois": 3,
                    "Souvent": 4,
                    "Très souvent": 5
                }
            },
            {
                "id": "PTSD6",
                "number": 6,
                "text": "Eviter de penser ou de parler de votre épisode stressant ou éviter des sentiments qui sont en relation avec lui",
                "cluster": "avoidance",
                "options": {
                    "Pas du tout": 1,
                    "Un peu": 2,
                    "Parfois": 3,
                    "Souvent": 4,
                    "Très souvent": 5
                }
            },
            {
                "id": "PTSD7",
                "number": 7,
                "text": "Eviter des activités ou des situations parce qu'elles vous rappellent votre épisode stressant",
                "cluster": "avoidance",
                "options": {
                    "Pas du tout": 1,
                    "Un peu": 2,
                    "Parfois": 3,
                    "Souvent": 4,
                    "Très souvent": 5
                }
            },
            {
                "id": "PTSD8",
                "number": 8,
                "text": "Avoir des difficultés à se souvenir de parties importantes de l'expérience stressante",
                "cluster": "avoidance",
                "options": {
                    "Pas du tout": 1,
                    "Un peu": 2,
                    "Parfois": 3,
                    "Souvent": 4,
                    "Très souvent": 5
                }
            },
            {
                "id": "PTSD9",
                "number": 9,
                "text": "Perte d'intérêt dans des activités qui habituellement vous faisaient plaisir.",
                "cluster": "avoidance",
                "options": {
                    "Pas du tout": 1,
                    "Un peu": 2,
                    "Parfois": 3,
                    "Souvent": 4,
                    "Très souvent": 5
                }
            },
            {
                "id": "PTSD10",
                "number": 10,
                "text": "Se sentir distant ou coupé(e) des autres personnes",
                "cluster": "avoidance",
                "options": {
                    "Pas du tout": 1,
                    "Un peu": 2,
                    "Parfois": 3,
                    "Souvent": 4,
                    "Très souvent": 5
                }
            },
            {
                "id": "PTSD11",
                "number": 11,
                "text": "Se sentir émotionnellement engourdi(e) ou incapable d'avoir des sentiments d'amour pour ceux qui sont proches de vous",
                "cluster": "avoidance",
                "options": {
                    "Pas du tout": 1,
                    "Un peu": 2,
                    "Parfois": 3,
                    "Souvent": 4,
                    "Très souvent": 5
                }
            },
            {
                "id": "PTSD12",
                "number": 12,
                "text": "Se sentir comme si votre avenir était en quelque sorte raccourci",
                "cluster": "avoidance",
                "options": {
                    "Pas du tout": 1,
                    "Un peu": 2,
                    "Parfois": 3,
                    "Souvent": 4,
                    "Très souvent": 5
                }
            },
            {
                "id": "PTSD13",
                "number": 13,
                "text": "Avoir des difficultés pour vous endormir ou rester endormi(e)",
                "cluster": "hyperarousal",
                "options": {
                    "Pas du tout": 1,
                    "Un peu": 2,
                    "Parfois": 3,
                    "Souvent": 4,
                    "Très souvent": 5
                }
            },
            {
                "id": "PTSD14",
                "number": 14,
                "text": "Se sentir irritable ou avoir des bouffées de colère",
                "cluster": "hyperarousal",
                "options": {
                    "Pas du tout": 1,
                    "Un peu": 2,
                    "Parfois": 3,
                    "Souvent": 4,
                    "Très souvent": 5
                }
            },
            {
                "id": "PTSD15",
                "number": 15,
                "text": "Avoir des difficultés à vous concentrer",
                "cluster": "hyperarousal",
                "options": {
                    "Pas du tout": 1,
                    "Un peu": 2,
                    "Parfois": 3,
                    "Souvent": 4,
                    "Très souvent": 5
                }
            },
            {
                "id": "PTSD16",
                "number": 16,
                "text": "Etre en état de super-alarme, sur la défensive, ou sur vos gardes",
                "cluster": "hyperarousal",
                "options": {
                    "Pas du tout": 1,
                    "Un peu": 2,
                    "Parfois": 3,
                    "Souvent": 4,
                    "Très souvent": 5
                }
            },
            {
                "id": "PTSD17",
                "number": 17,
                "text": "Se sentir énervé(e) ou sursauter facilement",
                "cluster": "hyperarousal",
                "options": {
                    "Pas du tout": 1,
                    "Un peu": 2,
                    "Parfois": 3,
                    "Souvent": 4,
                    "Très souvent": 5
                }
            }
        ]
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        Calculate PTSD total score and cluster scores.

        Args:
            responses (Dict[str, str]): A dictionary of responses, where the key is the question ID
                                       and the value is the response option text.

        Returns:
            Dict[str, Any]: A dictionary containing total score, cluster scores, and interpretations.
        """
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")

        total_score = 0
        item_scores = {}
        
        # Cluster scores
        clusters = {
            "re-experiencing": 0,
            "avoidance": 0,
            "hyperarousal": 0
        }
        
        for question in self.questions:
            q_id = question["id"]
            if q_id not in responses:
                raise ValueError(f"Missing response for question {q_id}")
            
            response_text = responses[q_id]
            if response_text not in question["options"]:
                raise ValueError(
                    f"Invalid response for question {q_id}. "
                    f"Expected one of: {list(question['options'].keys())}"
                )
            
            score = question["options"][response_text]
            item_scores[q_id] = score
            total_score += score
            clusters[question["cluster"]] += score

        interpretation = self._interpret_score(total_score)
        severity = self._get_severity(total_score)
        ptsd_positive = total_score >= 44

        return {
            "total_score": total_score,
            "max_score": 85,
            "interpretation": interpretation,
            "severity": severity,
            "ptsd_positive": ptsd_positive,
            "clusters": clusters,
            "cluster_interpretations": {
                "re-experiencing": f"{clusters['re-experiencing']}/25",
                "avoidance": f"{clusters['avoidance']}/35",
                "hyperarousal": f"{clusters['hyperarousal']}/25"
            },
            "item_scores": item_scores
        }

    def _interpret_score(self, score: int) -> str:
        """Interpret PTSD total score."""
        if score >= 60:
            return "Symptomatologie PTSD sévère"
        elif score >= 45:
            return "Symptomatologie PTSD modérée - Probable PTSD"
        elif score >= 30:
            return "Symptomatologie PTSD légère - Suivi recommandé"
        else:
            return "Symptomatologie PTSD minimale"

    def _get_severity(self, score: int) -> str:
        """Get severity level."""
        if score >= 60:
            return "severe"
        elif score >= 45:
            return "moderate"
        elif score >= 30:
            return "mild"
        else:
            return "minimal"

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "Voici une liste de problèmes et de plaintes que les gens ont parfois suite à des "
            "événements de vie stressants. Veuillez lire chaque question attentivement et "
            "indiquer à quel point vous avez été perturbé(e) par ce problème AU COURS DU DERNIER MOIS.\n\n"
            "Échelle de réponse:\n"
            "1 = Pas du tout\n"
            "2 = Un peu\n"
            "3 = Parfois\n"
            "4 = Souvent\n"
            "5 = Très souvent"
        )


if __name__ == '__main__':
    ptsd = PTSDQuestionnaire()
    print(f"Questionnaire: {ptsd.name}")
    print(f"Number of items: {ptsd.num_items}")
    print()
    
    # Test: Severe PTSD
    test_responses = {f"PTSD{i}": "Très souvent" for i in range(1, 18)}
    
    result = ptsd.calculate_score(test_responses)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Severity: {result['severity']}")
    print(f"PTSD Positive: {result['ptsd_positive']}")
    print(f"Interpretation: {result['interpretation']}")
    print(f"Clusters: Re-experiencing={result['clusters']['re-experiencing']}, "
          f"Avoidance={result['clusters']['avoidance']}, "
          f"Hyperarousal={result['clusters']['hyperarousal']}")
    print()
    print("✓ PTSD implementation complete - 17 items, 3 clusters")

