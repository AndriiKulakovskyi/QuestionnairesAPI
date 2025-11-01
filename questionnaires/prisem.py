import random
from typing import Any, Dict, List, Optional

class PRISEMQuestionnaire:
    """PRISEM - Patient-Rated Inventory of Side Effects for Mood Stabilizers
    
    Self-report questionnaire assessing medication side effects over the past week.
    Evaluates whether symptoms are perceived as side effects of current medication.
    
    Structure:
    - 32 items across 9 categories
    - 3-point scale: "Absent" (0), "Tolérable" (1), "Pénible" (2)
    - 2 gender-specific items:
      * Item 6d (Irregular periods) - for women only
      * Item 8c (Erectile dysfunction) - for men only
    
    Categories:
    1. Gastrointestinal (4 items)
    2. Cardiac (3 items)
    3. Skin problems (3 items)
    4. Neurological (4 items)
    5. Vision/Hearing (2 items)
    6. Urogenital (4 items, 1 gender-specific)
    7. Sleep problems (2 items)
    8. Sexual function (3 items, 1 gender-specific)
    9. Other issues (7 items)
    
    Scoring:
    - Sum of all applicable items
    - Range: 0-64 (or 0-62 when accounting for gender-specific items)
    - Higher scores indicate more severe side effects
    """

    def __init__(self):
        self.name = "PRISEM - Patient-Rated Inventory of Side Effects"
        self.description = "Inventaire des effets secondaires des médicaments évalués par le patient."
        self.num_items = 32
        self.used_in_applications = ['ebipolar']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 32 PRISEM items."""
        
        # Response options (same for all items)
        options = {
            "Absent": 0,
            "Tolérable": 1,
            "Pénible": 2
        }

        items_data = [
            # Category 1: Gastrointestinal
            ("m1a", "Diarrhée", "gastrointestinal", None),
            ("m1b", "Constipation", "gastrointestinal", None),
            ("m1c", "Bouche sèche", "gastrointestinal", None),
            ("m1d", "Nausée, vomissement", "gastrointestinal", None),
            
            # Category 2: Cardiac
            ("m2a", "Palpitations", "cardiac", None),
            ("m2b", "Vertiges", "cardiac", None),
            ("m2c", "Douleurs dans la poitrine", "cardiac", None),
            
            # Category 3: Skin
            ("m3a", "Augmentation de la transpiration", "skin", None),
            ("m3b", "Démangeaisons", "skin", None),
            ("m3c", "Sécheresse de la peau", "skin", None),
            
            # Category 4: Neurological
            ("m4a", "Mal à la tête", "neurological", None),
            ("m4b", "Tremblements", "neurological", None),
            ("m4c", "Mauvais contrôle moteur", "neurological", None),
            ("m4d", "Etourdissements", "neurological", None),
            
            # Category 5: Vision/Hearing
            ("m5a", "Vision floue", "vision_hearing", None),
            ("m5b", "Acouphènes (bourdonnements dans les oreilles)", "vision_hearing", None),
            
            # Category 6: Urogenital
            ("m6a", "Difficultés pour uriner", "urogenital", None),
            ("m6b", "Mictions douloureuses", "urogenital", None),
            ("m6c", "Mictions fréquentes", "urogenital", None),
            ("m6d", "Règles irrégulières (pour les femmes)", "urogenital", "female"),
            
            # Category 7: Sleep
            ("m7a", "Difficultés d'endormissement", "sleep", None),
            ("m7b", "Augmentation du temps de sommeil", "sleep", None),
            
            # Category 8: Sexual function
            ("m8a", "Perte du désir sexuel", "sexual", None),
            ("m8b", "Difficultés à atteindre un orgasme", "sexual", None),
            ("m8c", "Troubles de l'érection (pour les hommes)", "sexual", "male"),
            
            # Category 9: Other
            ("m9a", "Anxiété", "other", None),
            ("m9b", "Difficultés de concentration", "other", None),
            ("m9c", "Malaise général", "other", None),
            ("m9d", "Agitation", "other", None),
            ("m9e", "Fatigue", "other", None),
            ("m9f", "Diminution de l'énergie", "other", None),
            ("m9g", "Poids", "other", None),
        ]

        questions = []
        for item_id, text, category, gender in items_data:
            questions.append({
                "id": f"PRISEM_{item_id}",
                "item_code": item_id,
                "text": text,
                "options": options,
                "category": category,
                "gender_specific": gender
            })
        
        return questions

    def calculate_score(self, responses: Dict[str, str], gender: Optional[str] = None) -> Dict[str, Any]:
        """
        Calculate PRISEM total score.

        Args:
            responses (Dict[str, str]): A dictionary of responses, where the key is the question ID
                                       (e.g., "PRISEM_m1a") and the value is the response option text.
            gender (Optional[str]): "male", "female", or None. Required if gender-specific items are included.

        Returns:
            Dict[str, Any]: A dictionary containing the total score and interpretation.
        """
        total_score = 0
        item_scores = {}
        category_scores = {}
        
        # Initialize category scores
        categories = ["gastrointestinal", "cardiac", "skin", "neurological", 
                     "vision_hearing", "urogenital", "sleep", "sexual", "other"]
        for cat in categories:
            category_scores[cat] = 0
        
        # Validate and calculate scores
        for question in self.questions:
            q_id = question["id"]
            
            # Skip gender-specific items if not applicable
            if question["gender_specific"]:
                if gender is None:
                    continue  # Skip if gender not provided
                if question["gender_specific"] != gender:
                    continue  # Skip if doesn't match gender
            
            if q_id not in responses:
                # Gender-specific items are optional
                if question["gender_specific"]:
                    continue
                raise ValueError(f"Missing response for question {q_id}")
            
            response_text = responses[q_id]
            if response_text not in question["options"]:
                raise ValueError(
                    f"Invalid response '{response_text}' for question {q_id}. "
                    f"Valid options are: {list(question['options'].keys())}"
                )
            
            score = question["options"][response_text]
            item_scores[q_id] = score
            total_score += score
            category_scores[question["category"]] += score

        # Calculate maximum possible score based on gender
        if gender:
            max_score = 62  # 30 general items + 1 gender-specific = 31 items * 2
        else:
            max_score = 60  # 30 general items only * 2 (excluding both gender-specific)

        # Interpret score
        if total_score >= 45:
            severity = "Effets secondaires très sévères"
        elif total_score >= 30:
            severity = "Effets secondaires sévères"
        elif total_score >= 15:
            severity = "Effets secondaires modérés"
        elif total_score >= 5:
            severity = "Effets secondaires légers"
        else:
            severity = "Effets secondaires minimes ou absents"

        return {
            "total_score": total_score,
            "max_score": max_score,
            "severity": severity,
            "category_scores": category_scores,
            "item_scores": item_scores,
            "items_evaluated": len(item_scores)
        }

    def get_random_responses(self, gender: Optional[str] = None) -> Dict[str, str]:
        """Generates random valid responses for testing purposes."""
        responses = {}
        for question in self.questions:
            # Skip gender-specific items if not applicable
            if question["gender_specific"]:
                if gender and question["gender_specific"] != gender:
                    continue
            
            q_id = question["id"]
            responses[q_id] = random.choice(list(question["options"].keys()))
        return responses

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "Pour tous les symptômes ci-dessous, cochez la case qui correspond à ce que vous "
            "avez ressenti au cours de la semaine écoulée, si, et seulement si, vous pensez que "
            "ce sont des effets secondaires dus à votre traitement médicamenteux actuel.\n\n"
            "Options:\n"
            "- Absent: Le symptôme n'est pas présent\n"
            "- Tolérable: Le symptôme est présent mais supportable\n"
            "- Pénible: Le symptôme est présent et difficile à supporter"
        )


if __name__ == '__main__':
    prisem = PRISEMQuestionnaire()
    print(f"Questionnaire: {prisem.name}")
    print(f"Description: {prisem.description}")
    print(f"Number of items: {prisem.num_items}")
    print(f"Used in applications: {prisem.used_in_applications}")
    print()
    print("="*80)
    print("INSTRUCTION:")
    print(prisem.get_instruction())
    print("="*80)
    print()
    
    print("Items by category:")
    categories = {}
    for q in prisem.questions:
        cat = q["category"]
        if cat not in categories:
            categories[cat] = []
        gender_note = f" [{q['gender_specific']}]" if q['gender_specific'] else ""
        categories[cat].append(f"{q['text']}{gender_note}")
    
    for cat, items in categories.items():
        print(f"\n{cat.upper().replace('_', ' ')} ({len(items)} items):")
        for item in items:
            print(f"  • {item}")
    print()
    print("="*80)
    
    # Test with female, high side effects
    print("\nExample 1: Female with severe side effects")
    severe_responses = {}
    for q in prisem.questions:
        if q['gender_specific'] == 'male':
            continue
        severe_responses[q['id']] = "Pénible"
    
    result = prisem.calculate_score(severe_responses, gender="female")
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Severity: {result['severity']}")
    print(f"Items evaluated: {result['items_evaluated']}")
    print("\nCategory scores:")
    for cat, score in result['category_scores'].items():
        if score > 0:
            print(f"  {cat}: {score}")
    print()
    
    # Test with male, minimal side effects
    print("Example 2: Male with minimal side effects")
    minimal_responses = {}
    for q in prisem.questions:
        if q['gender_specific'] == 'female':
            continue
        minimal_responses[q['id']] = "Absent"
    
    result = prisem.calculate_score(minimal_responses, gender="male")
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Severity: {result['severity']}")
    print()
    
    # Test with random responses (no gender specified)
    print("Example 3: Random responses (gender-neutral)")
    random_responses = prisem.get_random_responses(gender=None)
    result = prisem.calculate_score(random_responses, gender=None)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Severity: {result['severity']}")
    print(f"Items evaluated: {result['items_evaluated']}")
    print()
    
    print("="*80)
    print("✓ PRISEM implementation complete")
    print("  - 32 items across 9 categories")
    print("  - 3-point scale (Absent/Tolérable/Pénible)")
    print("  - Gender-specific items handled correctly")
    print("  - Medication side effects assessment")

