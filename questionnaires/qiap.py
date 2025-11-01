import random
from typing import Any, Dict, List

class QIAPQuestionnaire:
    """QIAP - International Physical Activity Questionnaire (Short Form)
    
    Self-report questionnaire assessing physical activity over the last 7 days.
    
    Structure:
    - 3 activity categories, each with 2 sub-questions:
      1. Vigorous physical activity (days + duration)
      2. Moderate physical activity (days + duration)
      3. Walking (days + duration + intensity)
    - 1 sitting time question (duration on weekday)
    
    Scoring:
    - Days per week: 0-7
    - Duration: hours and minutes
    - MET calculation:
      • Vigorous activity: 8.0 METs
      • Moderate activity: 4.0 METs
      • Walking: 3.3 METs
    - Total MET-minutes/week = sum of (MET × minutes × days)
    
    Interpretation:
    - Low: <600 MET-minutes/week
    - Moderate: 600-3000 MET-minutes/week
    - High: >3000 MET-minutes/week
    
    Clinical Use:
    - Physical activity assessment
    - Lifestyle evaluation
    - Health promotion monitoring
    """

    def __init__(self):
        self.name = "QIAP - International Physical Activity Questionnaire"
        self.description = "Questionnaire international d'activité physique (7 derniers jours)."
        self.num_items = 4  # 3 activity categories + sitting time
        self.used_in_applications = ['cedr']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize QIAP items."""
        
        questions = [
            {
                "id": "QIAP1",
                "category": "vigorous",
                "text": "1. Activité physique intense",
                "sub_items": {
                    "QIAP1A": {
                        "text": "Durant ces 7 derniers jours, combien de jours avez-vous fait de l'activité physique intense comme lever des poids lourds, pelleter ou bêcher, faire de l'aérobic, faire du vélo à un rythme élevé?",
                        "type": "days",
                        "unit": "Jour(s) par semaine",
                        "range": [0, 7]
                    },
                    "QIAP1BH": {
                        "text": "Combien de temps par jour au total avez-vous passé à faire de l'activité physique intense?",
                        "type": "hours",
                        "unit": "Heure(s)"
                    },
                    "QIAP1BM": {
                        "text": "Combien de temps par jour au total avez-vous passé à faire de l'activité physique intense?",
                        "type": "minutes",
                        "unit": "Minute(s)"
                    }
                },
                "met_value": 8.0
            },
            {
                "id": "QIAP2",
                "category": "moderate",
                "text": "2. Activité physique modérée",
                "sub_items": {
                    "QIAP2A": {
                        "text": "Durant ces 7 derniers jours, combien de jours avez-vous fait de l'activité physique modérée comme lever des poids légers, faire du vélo à un rythme modéré ou faire une séance de tennis à intensité légère (ne pas inclure la marche)?",
                        "type": "days",
                        "unit": "Jour(s) par semaine",
                        "range": [0, 7]
                    },
                    "QIAP2BH": {
                        "text": "Combien de temps par jour au total avez-vous passé à faire de l'activité physique modérée?",
                        "type": "hours",
                        "unit": "Heure(s)"
                    },
                    "QIAP2BM": {
                        "text": "Combien de temps par jour au total avez-vous passé à faire de l'activité physique modérée?",
                        "type": "minutes",
                        "unit": "Minute(s)"
                    }
                },
                "met_value": 4.0
            },
            {
                "id": "QIAP3",
                "category": "walking",
                "text": "3. Marche",
                "sub_items": {
                    "QIAP3A": {
                        "text": "Durant ces 7 derniers jours, combien de jours avez-vous marché pendant au moins 10 minutes consécutives?",
                        "type": "days",
                        "unit": "Jour(s) par semaine",
                        "range": [0, 7]
                    },
                    "QIAP3BH": {
                        "text": "Combien de temps par jour au total avez-vous passé à marcher?",
                        "type": "hours",
                        "unit": "Heure(s)"
                    },
                    "QIAP3BM": {
                        "text": "Combien de temps par jour au total avez-vous passé à marcher?",
                        "type": "minutes",
                        "unit": "Minute(s)"
                    },
                    "QIAP3C": {
                        "text": "À quelle vitesse marchez-vous habituellement?",
                        "type": "intensity",
                        "options": {
                            "Lente": 2.5,
                            "Normale": 3.3,
                            "Rapide": 4.0
                        }
                    }
                },
                "met_value": 3.3  # Default, can be adjusted by QIAP3C
            },
            {
                "id": "QIAP4",
                "category": "sitting",
                "text": "4. Temps assis",
                "sub_items": {
                    "QIAP4AH": {
                        "text": "Durant les 7 derniers jours, combien de temps avez-vous passé assis(e) lors d'un jour de semaine?",
                        "type": "hours",
                        "unit": "Heure(s)"
                    },
                    "QIAP4AM": {
                        "text": "Durant les 7 derniers jours, combien de temps avez-vous passé assis(e) lors d'un jour de semaine?",
                        "type": "minutes",
                        "unit": "Minute(s)"
                    },
                    "QIAP4BH": {
                        "text": "Durant les 7 derniers jours, combien de temps avez-vous passé assis(e) lors d'un jour de week-end?",
                        "type": "hours",
                        "unit": "Heure(s)"
                    },
                    "QIAP4BM": {
                        "text": "Durant les 7 derniers jours, combien de temps avez-vous passé assis(e) lors d'un jour de week-end?",
                        "type": "minutes",
                        "unit": "Minute(s)"
                    }
                }
            }
        ]
        
        return questions

    def calculate_score(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate QIAP physical activity score in MET-minutes/week.

        Args:
            responses (Dict[str, Any]): A dictionary of responses with numeric values for
                                       days, hours, and minutes.

        Returns:
            Dict[str, Any]: A dictionary containing MET scores, activity levels, and interpretation.
        """
        met_scores = {}
        total_met_minutes = 0
        
        # Calculate vigorous activity
        vigorous_days = int(responses.get("QIAP1A", 0))
        vigorous_hours = int(responses.get("QIAP1BH", 0))
        vigorous_minutes = int(responses.get("QIAP1BM", 0))
        vigorous_total_minutes = (vigorous_hours * 60) + vigorous_minutes
        vigorous_met = 8.0 * vigorous_total_minutes * vigorous_days
        met_scores["vigorous"] = vigorous_met
        total_met_minutes += vigorous_met
        
        # Calculate moderate activity
        moderate_days = int(responses.get("QIAP2A", 0))
        moderate_hours = int(responses.get("QIAP2BH", 0))
        moderate_minutes = int(responses.get("QIAP2BM", 0))
        moderate_total_minutes = (moderate_hours * 60) + moderate_minutes
        moderate_met = 4.0 * moderate_total_minutes * moderate_days
        met_scores["moderate"] = moderate_met
        total_met_minutes += moderate_met
        
        # Calculate walking
        walking_days = int(responses.get("QIAP3A", 0))
        walking_hours = int(responses.get("QIAP3BH", 0))
        walking_minutes = int(responses.get("QIAP3BM", 0))
        walking_total_minutes = (walking_hours * 60) + walking_minutes
        
        # Adjust MET value based on walking intensity if provided
        walking_met_value = 3.3
        if "QIAP3C" in responses:
            intensity_map = {"Lente": 2.5, "Normale": 3.3, "Rapide": 4.0}
            walking_met_value = intensity_map.get(responses["QIAP3C"], 3.3)
        
        walking_met = walking_met_value * walking_total_minutes * walking_days
        met_scores["walking"] = walking_met
        total_met_minutes += walking_met
        
        # Calculate sitting time
        sitting_weekday_hours = int(responses.get("QIAP4AH", 0))
        sitting_weekday_minutes = int(responses.get("QIAP4AM", 0))
        sitting_weekend_hours = int(responses.get("QIAP4BH", 0))
        sitting_weekend_minutes = int(responses.get("QIAP4BM", 0))
        
        avg_sitting_minutes = ((sitting_weekday_hours * 60 + sitting_weekday_minutes) * 5 + 
                              (sitting_weekend_hours * 60 + sitting_weekend_minutes) * 2) / 7

        interpretation = self._interpret_score(total_met_minutes)
        activity_level = self._get_activity_level(total_met_minutes)

        return {
            "total_met_minutes_per_week": round(total_met_minutes, 1),
            "interpretation": interpretation,
            "activity_level": activity_level,
            "met_breakdown": met_scores,
            "avg_sitting_minutes_per_day": round(avg_sitting_minutes, 1),
            "meets_who_recommendations": total_met_minutes >= 600
        }

    def _interpret_score(self, met_minutes: float) -> str:
        """Interpret QIAP MET score."""
        if met_minutes >= 3000:
            return "Activité physique élevée - Excellente santé métabolique"
        elif met_minutes >= 1500:
            return "Activité physique élevée - Bons bénéfices pour la santé"
        elif met_minutes >= 600:
            return "Activité physique modérée - Atteint les recommandations OMS"
        elif met_minutes >= 1:
            return "Activité physique faible - En dessous des recommandations"
        else:
            return "Aucune activité physique déclarée"

    def _get_activity_level(self, met_minutes: float) -> str:
        """Get activity level category."""
        if met_minutes >= 3000:
            return "high"
        elif met_minutes >= 600:
            return "moderate"
        else:
            return "low"

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "Ce questionnaire a été conçu pour évaluer votre activité physique au quotidien "
            "lors des 7 derniers jours.\n\n"
            "\"Activité physique intense\" se réfère à une activité qui demande un effort "
            "plus qu'en temps normal.\n\n"
            "\"Activité physique modérée\" se réfère à une activité qui demande un effort "
            "physique modéré et qui vous fait respirer un peu plus qu'en temps normal.\n\n"
            "Les questions font référence aux 7 derniers jours."
        )


if __name__ == '__main__':
    qiap = QIAPQuestionnaire()
    print(f"Questionnaire: {qiap.name}")
    print(f"Number of categories: {qiap.num_items}")
    print()
    
    # Test: Moderate activity level
    test_responses = {
        "QIAP1A": "2",
        "QIAP1BH": "0",
        "QIAP1BM": "30",
        "QIAP2A": "3",
        "QIAP2BH": "0",
        "QIAP2BM": "40",
        "QIAP3A": "5",
        "QIAP3BH": "0",
        "QIAP3BM": "30",
        "QIAP3C": "Normale",
        "QIAP4AH": "8",
        "QIAP4AM": "0",
        "QIAP4BH": "6",
        "QIAP4BM": "0"
    }
    
    result = qiap.calculate_score(test_responses)
    print(f"Total MET-minutes/week: {result['total_met_minutes_per_week']}")
    print(f"Activity Level: {result['activity_level']}")
    print(f"Meets WHO recommendations: {result['meets_who_recommendations']}")
    print(f"Interpretation: {result['interpretation']}")
    print(f"Avg sitting time: {result['avg_sitting_minutes_per_day']} min/day")
    print()
    print("✓ QIAP implementation complete - Physical activity assessment with MET calculation")

