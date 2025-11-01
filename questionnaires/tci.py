"""
TCI - Temperament and Character Inventory (Cloninger, 1992)
A comprehensive personality assessment measuring 4 temperament and 3 character dimensions.
"""

class TCIQuestionnaire:
    def __init__(self):
        """Initialize the TCI questionnaire."""
        self.name = "TCI"
        self.full_name = "Temperament and Character Inventory"
        self.description = "Inventaire de Tempérament et de Caractère (Cloninger) - 125 items évaluant 7 dimensions de personnalité"
        self.num_items = 125
        self.questions = []
        
        # Define subscales with their items (based on JS scoring logic)
        # Each subscale item list contains items that score 1 when "Vrai" (True)
        # Reverse-scored items are those that score 1 when "Faux" (False)
        
        self.subscales = {
            "novelty_seeking": {
                "true_items": [1, 105, 125, 10, 71, 103, 24, 59, 44, 51, 60, 99],
                "false_items": [53, 63, 36, 47, 14, 76, 106, 77],
                "total_items": 20
            },
            "reward_dependence": {
                "true_items": [20, 31, 54, 97, 15, 119],
                "false_items": [65, 79, 96, 111, 11, 26, 39, 72, 85],
                "total_items": 15
            },
            "persistence": {
                "true_items": [22, 37, 55, 116],
                "false_items": [8],
                "total_items": 5
            },
            "harm_avoidance": {
                "true_items": [46, 82, 9, 70, 115, 19, 30, 16, 62],
                "false_items": [2, 61, 64, 38, 104, 45, 78, 86, 81, 98, 124],
                "total_items": 20
            },
            "self_directedness": {
                "true_items": [94, 122, 112],
                "false_items": [3, 17, 34, 49, 66, 6, 57, 69, 87, 23, 58, 92, 109, 21, 35, 48, 83, 120, 56, 90, 100, 117],
                "total_items": 25
            },
            "cooperativeness": {
                "true_items": [4, 93, 18, 41, 74, 89, 7, 50, 67, 118, 40, 102],
                "false_items": [12, 28, 123, 101, 27, 84, 95, 5, 33, 80, 13, 75, 88],
                "total_items": 25
            },
            "self_transcendence": {
                "true_items": [32, 43, 52, 107, 113, 25, 42, 68, 108, 114, 29, 73, 91, 110, 121],
                "false_items": [],
                "total_items": 15
            }
        }
        
        self._init_questions()
    
    def _init_questions(self):
        """Initialize all 125 TCI items (abbreviated for conciseness)."""
        questions_text = [
            "J'essaie souvent des choses nouvelles uniquement pour le plaisir ou pour avoir des sensations fortes",
            "J'ai habituellement confiance dans le fait que tout ira bien",
            "J'ai souvent l'impression d'être victime des circonstances",
            "Habituellement j'accepte les autres tels qu'ils sont",
            "Je prends plaisir à me venger des gens qui m'ont fait du mal",
            # ... (items 6-125 would be here in full implementation)
        ]
        
        for idx in range(1, self.num_items + 1):
            self.questions.append({
                "id": f"TCI{idx}",
                "text": f"Item {idx}",  # Abbreviated for conciseness
                "responses": ["Vrai", "Faux"],
                "scoring": {"Vrai": 1, "Faux": 0}
            })
    
    def calculate_score(self, responses: dict) -> dict:
        """
        Calculate TCI subscale scores.
        
        Args:
            responses: Dictionary mapping question IDs to response values (1=Vrai, 0=Faux)
                      (e.g., {"TCI1": 1, "TCI2": 0, ...})
        
        Returns:
            Dictionary containing:
            - subscale_scores: Dictionary with percentage scores for each dimension
            - total_score: Overall percentage score
            - interpretation: Brief interpretation
        """
        if not responses:
            return {
                "subscale_scores": {},
                "total_score": 0,
                "interpretation": "No responses provided"
            }
        
        subscale_scores = {}
        total_raw_score = 0
        total_possible = 125
        
        for subscale_name, subscale_data in self.subscales.items():
            raw_score = 0
            
            # Score "True" items
            for item_num in subscale_data["true_items"]:
                q_id = f"TCI{item_num}"
                if q_id in responses and responses[q_id] == 1:
                    raw_score += 1
            
            # Score "False" items (reverse scored)
            for item_num in subscale_data["false_items"]:
                q_id = f"TCI{item_num}"
                if q_id in responses and responses[q_id] == 0:
                    raw_score += 1
            
            # Convert to percentage
            total_items = subscale_data["total_items"]
            percentage_score = (raw_score * 100) / total_items if total_items > 0 else 0
            subscale_scores[subscale_name] = round(percentage_score, 1)
            
            total_raw_score += raw_score
        
        # Calculate total percentage
        total_percentage = (total_raw_score * 100) / total_possible
        
        # Interpret results (simplified)
        interpretation = f"Score total: {total_percentage:.1f}%"
        
        subscale_labels = {
            "novelty_seeking": "Recherche de Nouveauté",
            "reward_dependence": "Dépendance à la Récompense",
            "persistence": "Persistance",
            "harm_avoidance": "Évitement du Danger",
            "self_directedness": "Détermination",
            "cooperativeness": "Coopération",
            "self_transcendence": "Transcendance"
        }
        
        return {
            "subscale_scores": subscale_scores,
            "subscale_labels": subscale_labels,
            "total_score": round(total_percentage, 1),
            "total_raw_score": total_raw_score,
            "interpretation": interpretation
        }


if __name__ == '__main__':
    # Example usage
    tci = TCIQuestionnaire()
    
    print(f"Questionnaire: {tci.full_name}")
    print(f"Number of items: {tci.num_items}\n")
    
    # Example 1: All True
    print("Example 1: All True responses")
    responses1 = {f"TCI{i}": 1 for i in range(1, 126)}
    result1 = tci.calculate_score(responses1)
    print(f"Total score: {result1['total_score']}%")
    print("Subscale scores:")
    for subscale, score in result1['subscale_scores'].items():
        label = result1['subscale_labels'][subscale]
        print(f"  {label}: {score}%")
    print(f"Interpretation: {result1['interpretation']}\n")
    
    # Example 2: All False
    print("Example 2: All False responses")
    responses2 = {f"TCI{i}": 0 for i in range(1, 126)}
    result2 = tci.calculate_score(responses2)
    print(f"Total score: {result2['total_score']}%")
    print(f"Interpretation: {result2['interpretation']}\n")
    
    # Example 3: Mixed
    print("Example 3: Mixed responses (50/50)")
    import random
    random.seed(42)
    responses3 = {f"TCI{i}": random.randint(0, 1) for i in range(1, 126)}
    result3 = tci.calculate_score(responses3)
    print(f"Total score: {result3['total_score']}%")
    print("Subscale scores:")
    for subscale, score in result3['subscale_scores'].items():
        label = result3['subscale_labels'][subscale]
        print(f"  {label}: {score}%")

