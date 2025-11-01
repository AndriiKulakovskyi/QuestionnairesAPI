"""
CSHQ - Children's Sleep Habits Questionnaire
A parent-report questionnaire assessing sleep behaviors and problems in children.
"""

class CSHQQuestionnaire:
    def __init__(self):
        """Initialize the CSHQ questionnaire."""
        self.name = "CSHQ"
        self.full_name = "Children's Sleep Habits Questionnaire - Habitudes de Sommeil de l'Enfant"
        self.description = "Questionnaire parental évaluant les habitudes de sommeil et les difficultés de sommeil chez l'enfant"
        self.num_items = 47  # 47 scored items
        self.questions = []
        
        # Define reverse-scored items (items where lower frequency = higher score)
        self.reverse_items = [1, 2, 3, 15, 16, 21, 34]
        
        # Define subscales
        self.subscales = {
            "bedtime_resistance": [1, 3, 4, 7, 10, 12],
            "sleep_onset_delay": [2],
            "sleep_duration": [13, 15, 16],
            "sleep_anxiety": [7, 11, 12, 27],
            "night_wakings": [21, 31, 32],
            "parasomnias": [17, 18, 19, 20, 23, 29, 30],
            "sleep_disordered_breathing": [24, 25, 26],
            "daytime_sleepiness": [34, 36, 37, 38, 39, 44, 46, 47]
        }
        
        self._init_questions()
    
    def _init_questions(self):
        """Initialize all 47 CSHQ items."""
        
        # Standard response options for most items
        standard_responses = ["régulièrement (5-7 fois/semaine)", "quelquefois (2-4 fois/semaine)", "rarement (0-1 fois/semaine)"]
        
        questions_data = [
            # Bedtime routine
            ("Votre enfant va au lit à la même heure", "bedtime_resistance", standard_responses, False),
            ("Votre enfant s'endort en 20 min après être allé au lit", "sleep_onset_delay", standard_responses, False),
            ("Votre enfant s'endort seul dans son propre lit", "bedtime_resistance", standard_responses, False),
            ("Votre enfant s'endort dans le lit de ses parents ou de ses frères/soeurs", "bedtime_resistance", standard_responses, True),
            ("Votre enfant s'endort avec des mouvements rythmiques ou de balancements", None, standard_responses, True),
            ("Votre enfant a besoin d'objet spéciaux pour s'endormir (poupée, couverture spéciale, etc.)", None, standard_responses, True),
            ("Votre enfant a besoin de ses parents dans la pièce pour s'endormir", "bedtime_resistance,sleep_anxiety", standard_responses, True),
            ("Votre enfant est prêt pour aller au lit à l'heure du coucher", None, standard_responses, False),
            ("Votre enfant résiste pour aller au lit à l'heure du coucher", None, standard_responses, True),
            ("Votre enfant s'oppose à l'heure du coucher (cries, refuse de rester au lit, etc.)", "bedtime_resistance", standard_responses, True),
            ("Votre enfant est effrayé de dormir dans le noir", "sleep_anxiety", standard_responses, True),
            ("Votre enfant est effrayé de dormir seul", "bedtime_resistance,sleep_anxiety", standard_responses, True),
            ("Votre enfant dort trop peu", "sleep_duration", standard_responses, True),
            ("Votre enfant dort trop", None, standard_responses, True),
            ("Votre enfant dort la durée qu'il faut", "sleep_duration", standard_responses, False),
            ("Votre enfant dort le même nombre d'heures chaque jour", "sleep_duration", standard_responses, False),
            ("Votre enfant mouille son lit la nuit", "parasomnias", standard_responses, True),
            ("Votre enfant parle durant la nuit", "parasomnias", standard_responses, True),
            ("Votre enfant bouge sans cesse durant la nuit", "parasomnias", standard_responses, True),
            ("Votre enfant a des soubresauts ou secoue des parties du corps la nuit", "parasomnias", standard_responses, True),
            ("Votre enfant se réveille une fois la nuit", "night_wakings", standard_responses, True),
            ("Votre enfant se réveille plus d'une fois la nuit", None, standard_responses, True),
            ("Votre enfant fait des cauchemars", "parasomnias", standard_responses, True),
            ("Votre enfant ronfle bruyamment", "sleep_disordered_breathing", standard_responses, True),
            ("Votre enfant semble arrêter de respirer durant la nuit", "sleep_disordered_breathing", standard_responses, True),
            ("Votre enfant a des difficultés respiratoires la nuit", "sleep_disordered_breathing", standard_responses, True),
            ("Votre enfant a du mal à s'endormir loin de la maison", "sleep_anxiety", standard_responses, True),
            ("Votre enfant se plaint d'avoir mal aux jambes la nuit", None, standard_responses, True),
            ("Votre enfant a des soubresauts ou secoue les jambes la nuit", "parasomnias", standard_responses, True),
            ("Votre enfant a des terreurs nocturnes", "parasomnias", standard_responses, True),
            ("Votre enfant se réveille une fois puis a du mal à se rendormir", "night_wakings", standard_responses, True),
            ("Votre enfant  grince des dents la nuit", "night_wakings", standard_responses, True),
            ("Votre enfant se réveille en hurlant, en transpirant et sans pouvoir se calmer", None, standard_responses, True),
            ("Votre enfant se réveille tout seul", "daytime_sleepiness", standard_responses, False),
            ("Votre enfant se réveille de mauvaise humeur", None, standard_responses, True),
            ("Votre enfant doit être réveillé par quelqu'un d'autre", "daytime_sleepiness", standard_responses, True),
            ("Votre enfant a du mal à sortir du lit le matin", "daytime_sleepiness", standard_responses, True),
            ("Votre enfant met longtemps à devenir alerte le matin", "daytime_sleepiness", standard_responses, True),
            ("Votre enfant semble fatigué", "daytime_sleepiness", standard_responses, True),
            ("Votre enfant ne mange pas beaucoup au petit déjeuner", None, standard_responses, True),
            ("Votre enfant est de mauvaise humeur et irritable pendant la journée", None, standard_responses, True),
            ("Votre enfant semble hyperactif, fatigué ou agressif", None, standard_responses, True),
            ("Votre enfant a des accidents durant la journée", None, standard_responses, True),
            ("Votre enfant se sent somnolent ou s'endort en regardant la télévision", "daytime_sleepiness", standard_responses, True),
            ("Votre enfant se sent somnolent ou s'endort en voiture", None, standard_responses, True),
            ("Votre enfant a du mal à rester éveillé à l'école ou pendant les devoirs", "daytime_sleepiness", standard_responses, True),
            ("Votre enfant a du mal à rester éveillé quand il joue", "daytime_sleepiness", standard_responses, True),
        ]
        
        for idx, (text, subscale_str, responses, is_problem) in enumerate(questions_data, 1):
            subscales_list = subscale_str.split(",") if subscale_str else []
            self.questions.append({
                "id": f"CSHQ{idx}",
                "text": text,
                "subscales": subscales_list,
                "responses": responses,
                "is_problem": is_problem  # Whether this behavior is problematic
            })
    
    def _reverse_score(self, value):
        """Apply reverse scoring transformation."""
        # 3 -> 1, 2 -> 2, 1 -> 3
        return 4 - value
    
    def calculate_score(self, responses: dict) -> dict:
        """
        Calculate CSHQ scores.
        
        Args:
            responses: Dictionary mapping question IDs to response values (1-3)
                      (e.g., {"CSHQ1": 3, "CSHQ2": 2, ...})
        
        Returns:
            Dictionary containing:
            - subscale_scores: Dictionary with scores for each subscale
            - total_score: Total score across all items
            - interpretation: Clinical interpretation
        """
        if not responses:
            return {
                "subscale_scores": {},
                "total_score": 0,
                "interpretation": "No responses provided"
            }
        
        subscale_scores = {name: 0 for name in self.subscales.keys()}
        subscale_counts = {name: 0 for name in self.subscales.keys()}
        
        # Calculate subscale scores
        for subscale_name, item_indices in self.subscales.items():
            for idx in item_indices:
                q_id = f"CSHQ{idx}"
                if q_id in responses:
                    value = responses[q_id]
                    # Apply reverse scoring if needed
                    if idx in self.reverse_items:
                        value = self._reverse_score(value)
                    subscale_scores[subscale_name] += value
                    subscale_counts[subscale_name] += 1
        
        # Calculate total score (with adjustment for items 7 and 12 counted twice)
        total_score = 0
        items_to_subtract = []  # Items 7 and 12 are in multiple subscales, subtract once
        
        for idx in range(1, self.num_items + 1):
            q_id = f"CSHQ{idx}"
            if q_id in responses:
                value = responses[q_id]
                # Apply reverse scoring if needed
                if idx in self.reverse_items:
                    value = self._reverse_score(value)
                
                # Items 7 and 12 are counted in multiple subscales, subtract once for total
                if idx in [7, 12]:
                    items_to_subtract.append(value)
                else:
                    total_score += value
        
        # Add items 7 and 12 only once
        for value in items_to_subtract:
            total_score += value
        
        # Interpret results
        # Clinical cutoff: Total score > 41 indicates sleep problems
        if total_score > 41:
            severity = "Problèmes de sommeil cliniquement significatifs"
        elif total_score > 35:
            severity = "Problèmes de sommeil modérés"
        else:
            severity = "Habitudes de sommeil normales"
        
        interpretation = f"{severity} (Score total: {total_score})"
        
        return {
            "subscale_scores": subscale_scores,
            "subscale_counts": subscale_counts,
            "total_score": total_score,
            "interpretation": interpretation
        }


if __name__ == '__main__':
    # Example usage
    cshq = CSHQQuestionnaire()
    
    print(f"Questionnaire: {cshq.full_name}")
    print(f"Number of items: {cshq.num_items}\n")
    
    # Example 1: Significant sleep problems
    print("Example 1: Significant sleep problems")
    responses1 = {f"CSHQ{i}": 3 for i in range(1, 48)}
    result1 = cshq.calculate_score(responses1)
    print(f"Total score: {result1['total_score']}")
    print("Subscale scores:")
    for subscale, score in result1['subscale_scores'].items():
        count = result1['subscale_counts'][subscale]
        print(f"  {subscale}: {score} ({count} items)")
    print(f"Interpretation: {result1['interpretation']}\n")
    
    # Example 2: Normal sleep habits
    print("Example 2: Normal sleep habits")
    responses2 = {f"CSHQ{i}": 1 for i in range(1, 48)}
    result2 = cshq.calculate_score(responses2)
    print(f"Total score: {result2['total_score']}")
    print(f"Interpretation: {result2['interpretation']}\n")
    
    # Example 3: Moderate sleep problems
    print("Example 3: Moderate sleep problems (mixed responses)")
    import random
    random.seed(42)
    responses3 = {f"CSHQ{i}": random.randint(1, 3) for i in range(1, 48)}
    result3 = cshq.calculate_score(responses3)
    print(f"Total score: {result3['total_score']}")
    print("Subscale scores:")
    for subscale, score in result3['subscale_scores'].items():
        count = result3['subscale_counts'][subscale]
        print(f"  {subscale}: {score} ({count} items)")
    print(f"Interpretation: {result3['interpretation']}\n")

