"""
Questionnaire: PSQI (Pittsburgh Sleep Quality Index)
Indice de Qualité du Sommeil de Pittsburgh
"""

from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import re


class PSQIQuestionnaire:
    """PSQI - Pittsburgh Sleep Quality Index
    
    Auto-questionnaire d'évaluation de la qualité du sommeil sur les 30 derniers jours.
    Comprend 7 composantes : durée, latence, efficience, troubles, qualité, médication, dysfonctionnement diurne.
    """
    
    def __init__(self):
        self.name = "PSQI - Pittsburgh Sleep Quality Index"
        self.description = ("Indice de qualité du sommeil évaluant les habitudes de sommeil "
                           "au cours des 30 derniers jours. Score total de 0-21, avec 7 composantes.")
        self.used_in_applications = ["ebipolar", "eschizo"]
        
        # Standard frequency options for most questions
        self.frequency_options = {
            "Jamais au cours des 30 derniers jours": 0,
            "Moins d'une fois par semaine": 1,
            "Une ou deux fois par semaine": 2,
            "Trois fois par semaine ou plus": 3
        }
        
    def validate_time_format(self, time_str: str) -> bool:
        """Validate HH:MM format"""
        pattern = r'^[0-2][0-9]:[0-5][0-9]$'
        return bool(re.match(pattern, time_str))
    
    def parse_time(self, time_str: str) -> tuple:
        """Parse time string to hours and minutes"""
        if not self.validate_time_format(time_str):
            raise ValueError(f"Format de temps invalide: {time_str}. Attendu: HH:MM")
        hours, minutes = time_str.split(':')
        return int(hours), int(minutes)
    
    def calculate_time_in_bed(self, bedtime: str, waketime: str) -> float:
        """Calculate time in bed in hours
        
        Args:
            bedtime: Bedtime in HH:MM format (24h)
            waketime: Wake time in HH:MM format (24h)
            
        Returns:
            Time in bed in hours (float)
        """
        bed_h, bed_m = self.parse_time(bedtime)
        wake_h, wake_m = self.parse_time(waketime)
        
        # Calculate difference in hours
        if bed_h > 12:  # Evening bedtime
            diff_hours = 24 - bed_h + wake_h
        else:  # Morning bedtime (unusual but handled)
            diff_hours = wake_h - bed_h
        
        # Handle case where difference is negative (crossing midnight differently)
        if diff_hours < 0:
            diff_hours += 24
        
        # Add minutes
        if bed_m > wake_m:
            diff_hours = (diff_hours - 1) + ((60 + wake_m - bed_m) / 60)
        else:
            diff_hours = diff_hours + ((wake_m - bed_m) / 60)
        
        # Handle case where total > 24 (shouldn't happen but be safe)
        if diff_hours > 24:
            diff_hours -= 24
            
        return diff_hours
    
    def calculate_sleep_efficiency(self, bedtime: str, waketime: str, sleep_duration: str) -> int:
        """Calculate sleep efficiency component score
        
        Sleep efficiency = (hours actually slept / time in bed) * 100
        
        Args:
            bedtime: Time went to bed (HH:MM)
            waketime: Time woke up (HH:MM)
            sleep_duration: Hours actually slept (HH:MM)
            
        Returns:
            Component score (0-3)
        """
        time_in_bed = self.calculate_time_in_bed(bedtime, waketime)
        sleep_h, sleep_m = self.parse_time(sleep_duration)
        sleep_hours = sleep_h + (sleep_m / 60)
        
        # Calculate efficiency percentage
        efficiency_pct = (sleep_hours / time_in_bed) * 100
        
        # Score based on efficiency
        if efficiency_pct >= 85:
            return 0
        elif efficiency_pct >= 75:
            return 1
        elif efficiency_pct >= 65:
            return 2
        else:
            return 3
    
    def calculate_score(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate PSQI component scores and total score
        
        The PSQI has 7 components, each scored 0-3:
        1. Sleep Duration (C1) - from question 4
        2. Sleep Disturbance (C2) - from questions 5b-5j
        3. Sleep Latency (C3) - from question 2 + question 5a
        4. Sleep Efficiency (C5) - calculated from questions 1, 3, 4
        5. Sleep Quality (C6) - from question 6
        6. Medication Use (C7) - from question 7
        7. Daytime Dysfunction (C4) - from questions 8 + 9
        
        Total score = sum of 7 components (range 0-21)
        Score > 5 indicates poor sleep quality
        
        Args:
            responses: Dictionary with:
                - psqi_1: Bedtime (HH:MM)
                - psqi_2: Sleep latency in minutes (numeric)
                - psqi_3: Wake time (HH:MM)
                - psqi_4: Hours slept (HH:MM)
                - rad_psqi_5a through rad_psqi_5j: Frequency responses
                - rad_psqi_6: Quality rating
                - rad_psqi_7: Medication frequency
                - rad_psqi_8: Staying awake difficulty frequency
                - rad_psqi_9: Motivation difficulty rating
                
        Returns:
            Dictionary with component scores, total score, and interpretation
        """
        errors = []
        components = {}
        
        try:
            # Component 1: Sleep Duration (Question 4)
            if 'psqi_4' not in responses:
                errors.append("Question 4 (durée de sommeil) manquante")
            else:
                sleep_h, _ = self.parse_time(responses['psqi_4'])
                if sleep_h >= 7:
                    components['sleep_duration'] = 0
                elif sleep_h >= 6:
                    components['sleep_duration'] = 1
                elif sleep_h >= 5:
                    components['sleep_duration'] = 2
                else:
                    components['sleep_duration'] = 3
        except Exception as e:
            errors.append(f"Erreur calcul durée de sommeil: {str(e)}")
        
        try:
            # Component 2: Sleep Disturbance (Questions 5b-5j)
            disturbance_questions = ['rad_psqi_5b', 'rad_psqi_5c', 'rad_psqi_5d', 'rad_psqi_5e',
                                    'rad_psqi_5f', 'rad_psqi_5g', 'rad_psqi_5h', 'rad_psqi_5i', 'rad_psqi_5j']
            disturbance_sum = 0
            for q in disturbance_questions:
                if q not in responses or responses[q] not in self.frequency_options:
                    errors.append(f"Question {q} manquante ou invalide")
                else:
                    disturbance_sum += self.frequency_options[responses[q]]
            
            if not errors or 'disturbance_sum' not in locals():
                if disturbance_sum == 0:
                    components['sleep_disturbance'] = 0
                elif disturbance_sum <= 9:
                    components['sleep_disturbance'] = 1
                elif disturbance_sum <= 18:
                    components['sleep_disturbance'] = 2
                else:
                    components['sleep_disturbance'] = 3
        except Exception as e:
            errors.append(f"Erreur calcul troubles du sommeil: {str(e)}")
        
        try:
            # Component 3: Sleep Latency (Question 2 + Question 5a)
            if 'psqi_2' not in responses:
                errors.append("Question 2 (latence d'endormissement) manquante")
            elif 'rad_psqi_5a' not in responses:
                errors.append("Question 5a manquante")
            else:
                # Score for question 2 (minutes to fall asleep)
                latency_mins = float(responses['psqi_2'])
                if latency_mins <= 15:
                    latency_q2_score = 0
                elif latency_mins <= 30:
                    latency_q2_score = 1
                elif latency_mins <= 60:
                    latency_q2_score = 2
                else:
                    latency_q2_score = 3
                
                # Score for question 5a
                latency_q5a_score = self.frequency_options.get(responses['rad_psqi_5a'], 0)
                
                # Combined latency score
                latency_sum = latency_q2_score + latency_q5a_score
                if latency_sum == 0:
                    components['sleep_latency'] = 0
                elif latency_sum <= 2:
                    components['sleep_latency'] = 1
                elif latency_sum <= 4:
                    components['sleep_latency'] = 2
                else:
                    components['sleep_latency'] = 3
        except Exception as e:
            errors.append(f"Erreur calcul latence: {str(e)}")
        
        try:
            # Component 4: Sleep Efficiency (Questions 1, 3, 4)
            if 'psqi_1' not in responses or 'psqi_3' not in responses or 'psqi_4' not in responses:
                errors.append("Questions 1, 3, ou 4 manquantes pour calcul efficience")
            else:
                components['sleep_efficiency'] = self.calculate_sleep_efficiency(
                    responses['psqi_1'],
                    responses['psqi_3'],
                    responses['psqi_4']
                )
        except Exception as e:
            errors.append(f"Erreur calcul efficience: {str(e)}")
        
        try:
            # Component 5: Sleep Quality (Question 6)
            quality_options = {
                "Très bonne": 0,
                "Assez bonne": 1,
                "Assez mauvaise": 2,
                "Très mauvaise": 3
            }
            if 'rad_psqi_6' not in responses or responses['rad_psqi_6'] not in quality_options:
                errors.append("Question 6 (qualité du sommeil) manquante ou invalide")
            else:
                components['sleep_quality'] = quality_options[responses['rad_psqi_6']]
        except Exception as e:
            errors.append(f"Erreur calcul qualité: {str(e)}")
        
        try:
            # Component 6: Medication Use (Question 7)
            if 'rad_psqi_7' not in responses or responses['rad_psqi_7'] not in self.frequency_options:
                errors.append("Question 7 (médication) manquante ou invalide")
            else:
                components['medication_use'] = self.frequency_options[responses['rad_psqi_7']]
        except Exception as e:
            errors.append(f"Erreur calcul médication: {str(e)}")
        
        try:
            # Component 7: Daytime Dysfunction (Questions 8 + 9)
            dysfunction_options = {
                "Pas difficile du tout": 0,
                "Légèrement difficile": 1,
                "Assez difficile": 2,
                "Très difficile": 3
            }
            if 'rad_psqi_8' not in responses or responses['rad_psqi_8'] not in self.frequency_options:
                errors.append("Question 8 manquante ou invalide")
            elif 'rad_psqi_9' not in responses or responses['rad_psqi_9'] not in dysfunction_options:
                errors.append("Question 9 manquante ou invalide")
            else:
                dysfunction_sum = (self.frequency_options[responses['rad_psqi_8']] +
                                 dysfunction_options[responses['rad_psqi_9']])
                if dysfunction_sum == 0:
                    components['daytime_dysfunction'] = 0
                elif dysfunction_sum <= 2:
                    components['daytime_dysfunction'] = 1
                elif dysfunction_sum <= 4:
                    components['daytime_dysfunction'] = 2
                else:
                    components['daytime_dysfunction'] = 3
        except Exception as e:
            errors.append(f"Erreur calcul dysfonctionnement diurne: {str(e)}")
        
        # Calculate total score
        if len(components) == 7:
            total_score = sum(components.values())
            valid = True
        else:
            total_score = None
            valid = False
        
        return {
            'score': total_score,
            'components': components,
            'valid': valid,
            'errors': errors,
            'interpretation': self._interpret_score(total_score) if valid else None
        }
    
    def _interpret_score(self, score: int) -> str:
        """Interpret PSQI total score
        
        Standard PSQI cutoff: > 5 indicates poor sleep quality
        
        Args:
            score: Total PSQI score (0-21)
            
        Returns:
            Interpretation text
        """
        if score <= 5:
            return "Bonne qualité de sommeil"
        elif score <= 10:
            return "Qualité de sommeil moyenne (troubles légers)"
        elif score <= 15:
            return "Mauvaise qualité de sommeil (troubles modérés)"
        else:
            return "Très mauvaise qualité de sommeil (troubles sévères)"


# Example usage
if __name__ == "__main__":
    questionnaire = PSQIQuestionnaire()
    
    # Example responses (moderate sleep problems)
    example_responses = {
        'psqi_1': "23:30",  # Bedtime
        'psqi_2': "45",  # 45 minutes to fall asleep
        'psqi_3': "07:00",  # Wake time
        'psqi_4': "06:00",  # Hours actually slept
        'rad_psqi_5a': "Une ou deux fois par semaine",  # Can't fall asleep in 30min
        'rad_psqi_5b': "Une ou deux fois par semaine",  # Wake up at night
        'rad_psqi_5c': "Trois fois par semaine ou plus",  # Bathroom visits
        'rad_psqi_5d': "Jamais au cours des 30 derniers jours",  # Breathing problems
        'rad_psqi_5e': "Jamais au cours des 30 derniers jours",  # Cough/snore
        'rad_psqi_5f': "Moins d'une fois par semaine",  # Too cold
        'rad_psqi_5g': "Moins d'une fois par semaine",  # Too hot
        'rad_psqi_5h': "Moins d'une fois par semaine",  # Nightmares
        'rad_psqi_5i': "Une ou deux fois par semaine",  # Pain
        'rad_psqi_5j': "Moins d'une fois par semaine",  # Other reasons
        'rad_psqi_6': "Assez mauvaise",  # Sleep quality
        'rad_psqi_7': "Moins d'une fois par semaine",  # Medication
        'rad_psqi_8': "Une ou deux fois par semaine",  # Staying awake
        'rad_psqi_9': "Légèrement difficile"  # Motivation
    }
    
    result = questionnaire.calculate_score(example_responses)
    print(f"Score total PSQI: {result['score']}/21")
    print(f"Interprétation: {result['interpretation']}")
    print(f"\nComposantes:")
    for component, score in result['components'].items():
        print(f"  {component}: {score}/3")

