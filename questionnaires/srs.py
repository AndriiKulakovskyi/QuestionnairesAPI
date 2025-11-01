"""
SRS - Social Reciprocity Scale (Échelle de Réciprocité Sociale)
A parent/clinician-rated questionnaire assessing social communication impairments.
Available in adult and child versions.
"""

class SRSQuestionnaire:
    def __init__(self):
        """Initialize the SRS questionnaire."""
        self.name = "SRS"
        self.full_name = "Social Reciprocity Scale - Échelle de Réciprocité Sociale"
        self.description = "Échelle d'évaluation de la réciprocité sociale et des compétences sociales (version adulte et enfant)"
        self.num_items = 65
        self.questions = []
        
        # Define subscales (as per SRS standard scoring)
        self.subscales = {
            "social_awareness": list(range(1, 9)),  # 8 items
            "social_cognition": list(range(9, 21)),  # 12 items
            "social_communication": list(range(21, 43)),  # 22 items
            "social_motivation": list(range(43, 54)),  # 11 items
            "autistic_mannerisms": list(range(54, 66))  # 12 items
        }
        
        self._init_questions()
    
    def _init_questions(self):
        """Initialize all 65 SRS items (abbreviated for implementation)."""
        
        # Sample questions (full 65-item list would be extracted from forms 211, 212, 256, 257)
        questions_text = [
            "Semble beaucoup plus nerveux dans des situations sociales",
            "Son expression faciale n'est pas en harmonie avec son discours",
            "Semble avoir confiance en lui/elle quand il/elle interagit",
            # ... (items 4-65 would be here in full implementation)
        ]
        
        response_options = ["Pas VRAI", "Parfois VRAI", "Souvent VRAI", "Presque toujours VRAI"]
        
        for idx in range(1, self.num_items + 1):
            self.questions.append({
                "id": f"RECSOC{idx}",
                "text": f"Item {idx}",  # Abbreviated
                "responses": response_options,
                "scoring": {
                    "Pas VRAI": 1,
                    "Parfois VRAI": 2,
                    "Souvent VRAI": 3,
                    "Presque toujours VRAI": 4
                }
            })
    
    def calculate_score(self, responses: dict) -> dict:
        """
        Calculate SRS scores.
        
        Args:
            responses: Dictionary mapping question IDs to response values (1-4)
                      (e.g., {"RECSOC1": 1, "RECSOC2": 3, ...})
        
        Returns:
            Dictionary containing:
            - subscale_scores: Dictionary with raw scores for each subscale
            - total_score: Total raw score (range: 0-195 after adjustment)
            - t_score: T-score (standardized)
            - interpretation: Clinical interpretation
        """
        if not responses:
            return {
                "subscale_scores": {},
                "total_score": 0,
                "t_score": None,
                "interpretation": "No responses provided"
            }
        
        subscale_scores = {}
        total_raw_score = 0
        
        for subscale_name, item_indices in self.subscales.items():
            subscale_score = 0
            for idx in item_indices:
                q_id = f"RECSOC{idx}"
                if q_id in responses:
                    # Subtract 1 to get 0-3 scale
                    subscale_score += responses[q_id] - 1
            subscale_scores[subscale_name] = subscale_score
            total_raw_score += subscale_score
        
        # Interpret results (using standard SRS cutoffs for total raw score)
        if total_raw_score >= 76:
            severity = "Sévère - Déficits marqués en réciprocité sociale"
        elif total_raw_score >= 60:
            severity = "Modéré - Déficits modérés en réciprocité sociale"
        elif total_raw_score >= 40:
            severity = "Léger - Quelques difficultés en réciprocité sociale"
        else:
            severity = "Normal - Pas de déficits significatifs"
        
        subscale_labels = {
            "social_awareness": "Conscience sociale",
            "social_cognition": "Cognition sociale",
            "social_communication": "Communication sociale",
            "social_motivation": "Motivation sociale",
            "autistic_mannerisms": "Comportements autistiques"
        }
        
        return {
            "subscale_scores": subscale_scores,
            "subscale_labels": subscale_labels,
            "total_score": total_raw_score,
            "t_score": None,  # Would require normative tables
            "interpretation": f"{severity} (Score total: {total_raw_score}/195)"
        }


if __name__ == '__main__':
    # Example usage
    srs = SRSQuestionnaire()
    
    print(f"Questionnaire: {srs.full_name}")
    print(f"Number of items: {srs.num_items}\n")
    
    # Example 1: Severe social deficits
    print("Example 1: Severe social communication deficits")
    responses1 = {f"RECSOC{i}": 4 for i in range(1, 66)}
    result1 = srs.calculate_score(responses1)
    print(f"Total score: {result1['total_score']}/195")
    print("Subscale scores:")
    for subscale, score in result1['subscale_scores'].items():
        label = result1['subscale_labels'][subscale]
        print(f"  {label}: {score}")
    print(f"Interpretation: {result1['interpretation']}\n")
    
    # Example 2: Mild difficulties
    print("Example 2: Mild social difficulties")
    responses2 = {f"RECSOC{i}": 2 for i in range(1, 66)}
    result2 = srs.calculate_score(responses2)
    print(f"Total score: {result2['total_score']}/195")
    print(f"Interpretation: {result2['interpretation']}\n")
    
    # Example 3: Normal range
    print("Example 3: Normal social functioning")
    responses3 = {f"RECSOC{i}": 1 for i in range(1, 66)}
    result3 = srs.calculate_score(responses3)
    print(f"Total score: {result3['total_score']}/195")
    print(f"Interpretation: {result3['interpretation']}\n")

