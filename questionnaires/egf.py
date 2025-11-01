import random
from typing import Any, Dict, List

class EGFQuestionnaire:
    """EGF - Global Functioning Scale (Échelle de Fonctionnement Global)
    
    Clinician-rated single-item scale assessing overall functioning.
    Based on DSM-IV Global Assessment of Functioning (GAF).
    
    Structure:
    - 1 item: Global functioning score (0-100)
    
    Scoring:
    - 0-100 continuous scale
    - Divided into 10-point ranges with descriptive anchors:
      • 100-91: Superior functioning
      • 90-81: Absent or minimal symptoms
      • 80-71: Transient symptoms
      • 70-61: Mild symptoms
      • 60-51: Moderate symptoms
      • 50-41: Serious symptoms
      • 40-31: Major impairment
      • 30-21: Inability to function
      • 20-11: Danger of harm
      • 10-1: Persistent danger
      • 0: Inadequate information
    
    Interpretation:
    - Higher scores indicate better functioning
    - Scores ≥71: Good functioning
    - Scores 51-70: Moderate impairment
    - Scores ≤50: Severe impairment
    
    Clinical Use:
    - Overall functioning assessment
    - Treatment planning
    - Outcome measurement
    - Disability evaluation
    """

    def __init__(self):
        self.name = "EGF - Échelle de Fonctionnement Global"
        self.description = "Évaluation globale du fonctionnement (clinicien)."
        self.num_items = 1
        self.used_in_applications = ['cedr']
        self.score_ranges = self._init_score_ranges()

    def _init_score_ranges(self) -> List[Dict[str, Any]]:
        """Initialize EGF score range descriptions."""
        
        ranges = [
            {
                "range": "100-91",
                "description": "Niveau supérieur de fonctionnement dans une grande variété d'activités. N'est jamais débordé par les problèmes rencontrés. Est recherché par autrui en raison de ses nombreuses qualités. Absence de symptômes.",
                "level": "superior"
            },
            {
                "range": "90-81",
                "description": "Symptômes absents ou minimes (p. ex. anxiété légère avant un examen), fonctionnement satisfaisant dans tous les domaines, intéressé et impliqué dans une grande variété d'activités, socialement efficace, en général satisfait de la vie, pas plus de problèmes ou de préoccupations que les soucis de tous les jours.",
                "level": "excellent"
            },
            {
                "range": "80-71",
                "description": "Si des symptômes sont présents, ils sont transitoires et il s'agit de réactions prévisibles à des facteurs de stress (p. ex. difficultés de concentration après une dispute familiale). Handicap léger dans le fonctionnement social, professionnel ou scolaire.",
                "level": "good"
            },
            {
                "range": "70-61",
                "description": "Quelques symptômes légers (p. ex. humeur dépressive et insomnie légère) ou une certaine difficulté dans le fonctionnement social, professionnel ou scolaire, mais fonctionne assez bien de façon générale, entretient plusieurs relations interpersonnelles positives.",
                "level": "mild_impairment"
            },
            {
                "range": "60-51",
                "description": "Symptômes d'intensité moyenne (p. ex. émoussement affectif, prolixité circonlocutoire, attaques de panique occasionnelles) ou difficultés d'intensité moyenne dans le fonctionnement social, professionnel ou scolaire (p. ex. peu d'amis, conflits avec les pairs ou collègues de travail).",
                "level": "moderate_impairment"
            },
            {
                "range": "50-41",
                "description": "Symptômes importants (p. ex. idéation suicidaire, rituels obsessionnels envahissants, vol à l'étalage) ou altération importante du fonctionnement social, professionnel ou scolaire (p. ex. absence d'amis, incapacité à garder un emploi).",
                "level": "serious_impairment"
            },
            {
                "range": "40-31",
                "description": "Déficit important dans plusieurs domaines : travail ou école, relations familiales, jugement, pensée ou humeur (p. ex. homme dépressif évite ses amis, néglige sa famille et est incapable de travailler ; enfant bat fréquemment des enfants plus jeunes, est provocant à la maison et échoue à l'école).",
                "level": "major_impairment"
            },
            {
                "range": "30-21",
                "description": "Le comportement est notablement influencé par des idées délirantes ou des hallucinations ou trouble grave de la communication ou de jugement (par ex. parfois incohérent, actes grossièrement inadaptés, préoccupation suicidaire) ou incapable de fonctionner dans presque tous les domaines (par ex. reste au lit toute la journée, absence de travail, de foyer ou d'amis).",
                "level": "severe_impairment"
            },
            {
                "range": "20-11",
                "description": "Existence d'un certain danger d'auto ou d'hétéro-agression (p. ex. tentative de suicide sans attente précise de la mort, violence fréquente, excitation maniaque) ou incapacité temporaire à maintenir une hygiène corporelle minimum (p. ex. se barbouille d'excréments) ou altération massive de la communication (p. ex. incohérence indiscutable ou mutisme).",
                "level": "danger"
            },
            {
                "range": "10-1",
                "description": "Danger persistant d'auto ou d'hétéro-agression grave (p. ex. accès répétés de violence) ou incapacité durable à maintenir une hygiène corporelle minimum ou geste suicidaire avec attente précise de la mort.",
                "level": "persistent_danger"
            },
            {
                "range": "0",
                "description": "Information inadéquate",
                "level": "no_info"
            }
        ]
        
        return ranges

    def calculate_score(self, score: int) -> Dict[str, Any]:
        """
        Interpret EGF score.

        Args:
            score (int): Global functioning score (0-100).

        Returns:
            Dict[str, Any]: A dictionary containing score and interpretation.
        """
        if not isinstance(score, int) or not (0 <= score <= 100):
            raise ValueError("Score must be an integer between 0 and 100")

        interpretation = self._interpret_score(score)
        functioning_level = self._get_functioning_level(score)
        severity = self._get_severity(score)

        return {
            "score": score,
            "max_score": 100,
            "interpretation": interpretation,
            "functioning_level": functioning_level,
            "severity": severity,
            "requires_intervention": score <= 70
        }

    def _interpret_score(self, score: int) -> str:
        """Interpret EGF score."""
        if score == 0:
            return "Information inadéquate"
        elif score <= 10:
            return "Danger persistant - Hospitalisation requise"
        elif score <= 20:
            return "Danger présent - Surveillance étroite nécessaire"
        elif score <= 30:
            return "Altération sévère du fonctionnement - Soins intensifs"
        elif score <= 40:
            return "Altération majeure - Intervention urgente"
        elif score <= 50:
            return "Symptômes importants - Traitement actif requis"
        elif score <= 60:
            return "Altération modérée - Suivi régulier recommandé"
        elif score <= 70:
            return "Symptômes légers - Suivi ambulatoire"
        elif score <= 80:
            return "Fonctionnement globalement bon - Symptômes transitoires"
        elif score <= 90:
            return "Fonctionnement excellent - Symptômes absents ou minimes"
        else:  # score <= 100
            return "Fonctionnement supérieur - Pleine santé mentale"

    def _get_functioning_level(self, score: int) -> str:
        """Get functioning level category."""
        if score == 0:
            return "no_info"
        elif score <= 20:
            return "danger"
        elif score <= 40:
            return "severe_impairment"
        elif score <= 60:
            return "moderate_impairment"
        elif score <= 80:
            return "mild_impairment"
        else:
            return "good_functioning"

    def _get_severity(self, score: int) -> str:
        """Get severity level."""
        if score == 0:
            return "unknown"
        elif score <= 40:
            return "severe"
        elif score <= 60:
            return "moderate"
        elif score <= 70:
            return "mild"
        else:
            return "minimal"

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "Evaluer le fonctionnement psychologique, social et professionnel sur un continuum "
            "hypothétique allant de la santé mentale à la maladie.\n\n"
            "Ne pas tenir compte d'un handicap du fonctionnement dû à des facteurs limitant "
            "d'ordre physique ou environnemental.\n\n"
            "Attribuer un score unique de 0 à 100."
        )


if __name__ == '__main__':
    egf = EGFQuestionnaire()
    print(f"Questionnaire: {egf.name}")
    print(f"Number of items: {egf.num_items}")
    print()
    
    # Test different score levels
    test_scores = [85, 65, 45, 25, 5]
    
    for test_score in test_scores:
        result = egf.calculate_score(test_score)
        print(f"Score: {result['score']}/100")
        print(f"Level: {result['functioning_level']}")
        print(f"Severity: {result['severity']}")
        print(f"Interpretation: {result['interpretation']}")
        print()
    
    print("✓ EGF implementation complete - 0-100 global functioning scale")

