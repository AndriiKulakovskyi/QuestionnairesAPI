import random
from typing import Any, Dict, List

class MathysQuestionnaire:
    """Mathys Scale - Multidimensional Assessment of Thymic States
    
    Visual Analog Scale (VAS) questionnaire assessing mixed affective states.
    Measures symptoms on a continuum between opposite poles (e.g., hypomania vs depression).
    
    Structure:
    - 20 items, each with bipolar extremes
    - Scored from 0 to 10 (continuous scale, allows 0.5 increments)
    - Items 5, 6, 7, 8, 9, 10, 17, 18 are reverse scored
    
    Subscales (5 dimensions):
    - Emotion (4 items: 3, 7, 10, 18)
    - Motivation/Psychomotor (7 items: 2, 11, 12, 15, 16, 17, 19)
    - Sensory Perception (5 items: 1, 6, 8, 13, 20)
    - Interpersonal Communication (2 items: 4, 14)
    - Cognition (2 items: 5, 9)
    
    Scoring:
    - Each item: 0-10 continuous scale
    - Reverse scored items: score = 10 - raw_score
    - Subscale scores: sum of relevant items
    - Total score: sum of all subscales (0-200)
    
    Interpretation:
    - Higher scores indicate more severe/intense symptoms
    - Can detect mixed states (both manic and depressive features)
    """

    def __init__(self):
        self.name = "Mathys Scale - Multidimensional Assessment of Thymic States"
        self.description = "Échelle d'évaluation dimensionnelle des états thymiques mixtes (VAS)."
        self.num_items = 20
        self.used_in_applications = ['ebipolar']
        self.reverse_items = [5, 6, 7, 8, 9, 10, 17, 18]
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 20 Mathys items with their bipolar poles."""
        
        items_data = [
            (1, "Je suis moins sensible que d'habitude aux couleurs", 
                "Je suis plus sensible que d'habitude aux couleurs", "sensory"),
            (2, "Je manque de tonus", 
                "J'ai une tension interne importante", "motivation"),
            (3, "J'ai l'impression d'être anesthésié(e) sur le plan des émotions", 
                "J'ai parfois le sentiment de perdre le contrôle de mes émotions", "emotion"),
            (4, "Je suis replié(e) sur moi", 
                "Je suis désinhibé(e)", "interpersonal"),
            (5, "Je suis facilement distrait(e), la moindre chose me fait perdre mon attention", 
                "Je ne suis pas attentif(ve) à mon environnement", "cognition"),  # reverse
            (6, "Je suis plus sensible que d'habitude au toucher", 
                "Je suis moins sensible que d'habitude au toucher", "sensory"),  # reverse
            (7, "J'ai l'impression que mon humeur varie beaucoup en fonction de mon environnement", 
                "Mon humeur est monotone et peu changeante", "emotion"),  # reverse
            (8, "Je suis particulièrement sensible à la musique", 
                "Je suis plus indifférent que d'habitude à la musique", "sensory"),  # reverse
            (9, "Mon cerveau ne s'arrête jamais", 
                "Mon cerveau fonctionne au ralenti", "cognition"),  # reverse
            (10, "Je suis plus réactif(ve) à mon environnement", 
                "Je suis moins réactif(ve) à mon environnement", "emotion"),  # reverse
            (11, "Je me sens sans énergie", 
                 "J'ai le sentiment d'avoir une grande énergie", "motivation"),
            (12, "J'ai le sentiment que mes pensées sont ralenties", 
                 "J'ai le sentiment que mes idées défilent dans ma tête", "motivation"),
            (13, "Je trouve la nourriture sans goût", 
                 "Je recherche les plaisirs gastronomiques car j'en apprécie davantage les saveurs", "sensory"),
            (14, "J'ai moins envie de communiquer avec les autres", 
                 "J'ai plus envie de communiquer avec les autres", "interpersonal"),
            (15, "Je manque de motivation pour aller de l'avant", 
                 "Je multiplie les projets nouveaux", "motivation"),
            (16, "Ma perte d'intérêt pour mon environnement m'empêche de gérer le quotidien", 
                 "J'ai envie de faire plus de choses que d'habitude", "motivation"),
            (17, "Je prends les décisions de manière plus rapide que d'habitude", 
                 "J'ai plus de difficultés que d'habitude à prendre des décisions", "motivation"),  # reverse
            (18, "Je ressens les émotions de manière très intense", 
                 "Mes émotions sont atténuées", "emotion"),  # reverse
            (19, "Je suis ralenti(e) dans mes mouvements", 
                 "Je suis physiquement agité(e)", "motivation"),
            (20, "J'ai l'impression d'être moins sensible aux odeurs que d'habitude", 
                 "J'ai l'impression d'être plus sensible aux odeurs que d'habitude", "sensory")
        ]

        questions = []
        for num, left_pole, right_pole, subscale in items_data:
            questions.append({
                "id": f"MATHYS{num}",
                "number": num,
                "text": f"{num}. {left_pole} | {right_pole}",
                "left_pole": left_pole,
                "right_pole": right_pole,
                "subscale": subscale,
                "reverse_scored": num in self.reverse_items,
                "min": 0.0,
                "max": 10.0
            })
        
        return questions

    def calculate_score(self, responses: Dict[str, float]) -> Dict[str, Any]:
        """
        Calculate Mathys subscale and total scores.

        Args:
            responses (Dict[str, float]): A dictionary of responses, where the key is the question ID
                                         (e.g., "MATHYS1") and the value is the score (0.0-10.0).

        Returns:
            Dict[str, Any]: A dictionary containing subscale scores, total score, and interpretations.
        """
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")

        # Initialize subscale scores
        subscales = {
            "emotion": [],
            "motivation": [],
            "sensory": [],
            "interpersonal": [],
            "cognition": []
        }
        
        item_scores = {}
        
        # Process each response
        for question in self.questions:
            q_id = question["id"]
            if q_id not in responses:
                raise ValueError(f"Missing response for question {q_id}")
            
            raw_score = responses[q_id]
            
            # Validate score range
            if not (0.0 <= raw_score <= 10.0):
                raise ValueError(
                    f"Score for {q_id} must be between 0.0 and 10.0, got {raw_score}"
                )
            
            # Apply reverse scoring if needed
            if question["reverse_scored"]:
                final_score = 10.0 - raw_score
            else:
                final_score = raw_score
            
            # Round to 1 decimal place
            final_score = round(final_score, 1)
            item_scores[q_id] = final_score
            
            # Add to appropriate subscale
            subscales[question["subscale"]].append(final_score)

        # Calculate subscale sums
        subscale_scores = {}
        for subscale_name, scores in subscales.items():
            subscale_scores[subscale_name] = round(sum(scores), 1)

        # Calculate total score
        total_score = round(sum(subscale_scores.values()), 1)

        # Interpretation
        if total_score >= 150:
            severity = "Symptômes très sévères (états mixtes prononcés)"
        elif total_score >= 100:
            severity = "Symptômes sévères"
        elif total_score >= 50:
            severity = "Symptômes modérés"
        elif total_score >= 25:
            severity = "Symptômes légers"
        else:
            severity = "Symptômes minimes ou absents"

        return {
            "subscales": {
                "emotion": subscale_scores["emotion"],
                "motivation_psychomotor": subscale_scores["motivation"],
                "sensory_perception": subscale_scores["sensory"],
                "interpersonal_communication": subscale_scores["interpersonal"],
                "cognition": subscale_scores["cognition"]
            },
            "subscale_items": {
                "emotion": [3, 7, 10, 18],
                "motivation": [2, 11, 12, 15, 16, 17, 19],
                "sensory": [1, 6, 8, 13, 20],
                "interpersonal": [4, 14],
                "cognition": [5, 9]
            },
            "total_score": total_score,
            "min_score": 0.0,
            "max_score": 200.0,
            "interpretation": severity,
            "item_scores": item_scores
        }

    def get_random_responses(self) -> Dict[str, float]:
        """Generates random valid responses for testing purposes."""
        responses = {}
        for question in self.questions:
            q_id = question["id"]
            # Random score between 0 and 10, with 0.5 increments
            responses[q_id] = round(random.uniform(0.0, 10.0) * 2) / 2
        return responses

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNE:\n\n"
            "Consigne de cotation : coter toujours le score le plus extrême (0 au lieu de 1 par exemple ; 10 au lieu de 9).\n\n"
            "Chaque item est coté entre 0 et 10, avec possibilité de demi points (Ex.: 2.5).\n\n"
            "Pour chaque item, deux affirmations opposées sont présentées. "
            "Placez un curseur sur l'échelle entre ces deux extrêmes selon votre état actuel :\n"
            "- 0 = correspond totalement à l'affirmation de gauche\n"
            "- 10 = correspond totalement à l'affirmation de droite\n"
            "- 5 = position intermédiaire"
        )


if __name__ == '__main__':
    mathys = MathysQuestionnaire()
    print(f"Questionnaire: {mathys.name}")
    print(f"Description: {mathys.description}")
    print(f"Number of items: {mathys.num_items}")
    print(f"Used in applications: {mathys.used_in_applications}")
    print()
    print("="*80)
    print("INSTRUCTION:")
    print(mathys.get_instruction())
    print("="*80)
    print()
    
    print("Sample items (first 5):")
    for q in mathys.questions[:5]:
        reverse_flag = " [REVERSE]" if q["reverse_scored"] else ""
        print(f"\n{q['number']}. [{q['subscale'].upper()}]{reverse_flag}")
        print(f"  Left (0):  {q['left_pole']}")
        print(f"  Right (10): {q['right_pole']}")
    print()
    print("="*80)
    
    # Test with high severity profile
    print("\nExample 1: High severity (mixed state)")
    high_responses = {f"MATHYS{i}": 9.0 for i in range(1, 21)}
    
    result = mathys.calculate_score(high_responses)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Interpretation: {result['interpretation']}")
    print("\nSubscale scores:")
    for subscale, score in result['subscales'].items():
        print(f"  {subscale}: {score}")
    print()
    
    # Test with low severity
    print("Example 2: Low severity (minimal symptoms)")
    low_responses = {f"MATHYS{i}": 1.0 for i in range(1, 21)}
    
    result = mathys.calculate_score(low_responses)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Interpretation: {result['interpretation']}")
    print("\nSubscale scores:")
    for subscale, score in result['subscales'].items():
        print(f"  {subscale}: {score}")
    print()
    
    # Test with random responses
    print("Example 3: Random responses (moderate mixed symptoms)")
    random_responses = mathys.get_random_responses()
    result = mathys.calculate_score(random_responses)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Interpretation: {result['interpretation']}")
    print("\nSubscale scores:")
    for subscale, score in result['subscales'].items():
        print(f"  {subscale}: {score}")
    print()
    
    # Test reverse scoring
    print("Example 4: Testing reverse scoring")
    test_responses = {f"MATHYS{i}": 5.0 for i in range(1, 21)}
    result = mathys.calculate_score(test_responses)
    print("All items rated at 5.0 (midpoint)")
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Note: With reverse scoring, midpoint (5) stays at 5 after inversion")
    print()
    
    print("="*80)
    print("✓ Mathys Scale implementation complete")
    print("  - 20 items with Visual Analog Scale (VAS)")
    print("  - Bipolar poles for each item")
    print("  - 8 reverse-scored items")
    print("  - 5 subscales (emotion, motivation, sensory, interpersonal, cognition)")
    print("  - Continuous scoring 0-10 (with 0.5 increments)")
    print("  - Detects mixed affective states")

