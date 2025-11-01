"""
LSAS - Liebowitz Social Anxiety Scale
A questionnaire assessing social anxiety across 24 situations.
Each situation is rated on two dimensions: Anxiety (0-3) and Avoidance (0-3).
"""

class LSASQuestionnaire:
    def __init__(self):
        """Initialize the LSAS questionnaire."""
        self.name = "LSAS"
        self.full_name = "Liebowitz Social Anxiety Scale - Échelle de Phobie Sociale de Liebowitz"
        self.description = "Questionnaire évaluant l'anxiété sociale et les comportements d'évitement dans 24 situations sociales"
        self.num_items = 24
        self.questions = []
        
        # Items that are social interaction situations (vs. performance situations)
        self.social_interaction_items = [5, 7, 10, 11, 12, 15, 18, 19, 21, 22, 23, 24]
        
        # Items that are performance situations
        self.performance_items = [1, 2, 3, 4, 6, 8, 9, 13, 14, 16, 17, 20]
        
        self._init_questions()
    
    def _init_questions(self):
        """Initialize all questions for the LSAS questionnaire."""
        
        # Each situation has two ratings: Anxiety (A) and Avoidance (E)
        situations = [
            {"num": 1, "text": "Téléphoner en public", "type": "P"},
            {"num": 2, "text": "Participer au sein d'un petit groupe", "type": "P"},
            {"num": 3, "text": "Manger dans un lieu public", "type": "P"},
            {"num": 4, "text": "Boire en compagnie dans un lieu public", "type": "P"},
            {"num": 5, "text": "Parler à des gens qui détiennent une autorité", "type": "S"},
            {"num": 6, "text": "Jouer, donner une représentation ou une conférence", "type": "P"},
            {"num": 7, "text": "Aller à une soirée", "type": "S"},
            {"num": 8, "text": "Travailler en étant observé", "type": "P"},
            {"num": 9, "text": "Écrire en étant observé", "type": "P"},
            {"num": 10, "text": "Contacter par téléphone quelqu'un que vous ne connaissez pas très bien", "type": "S"},
            {"num": 11, "text": "Parler à des gens que vous ne connaissez pas très bien", "type": "S"},
            {"num": 12, "text": "Rencontrer des inconnus", "type": "S"},
            {"num": 13, "text": "Uriner dans les toilettes publiques", "type": "P"},
            {"num": 14, "text": "Entrer dans une pièce alors que tout le monde est déjà assis", "type": "P"},
            {"num": 15, "text": "Être le centre d'attention", "type": "S"},
            {"num": 16, "text": "Prendre la parole à une réunion", "type": "P"},
            {"num": 17, "text": "Passer un examen", "type": "P"},
            {"num": 18, "text": "Exprimer son désaccord ou sa désapprobation à des gens que vous ne connaissez pas très bien", "type": "S"},
            {"num": 19, "text": "Regarder dans les yeux des gens que vous ne connaissez pas très bien", "type": "S"},
            {"num": 20, "text": "Faire un compte-rendu à un groupe", "type": "P"},
            {"num": 21, "text": "Essayer de draguer quelqu'un", "type": "S"},
            {"num": 22, "text": "Rapporter des marchandises dans un magasin", "type": "S"},
            {"num": 23, "text": "Donner une soirée", "type": "S"},
            {"num": 24, "text": "Résister aux pressions d'un vendeur insistant", "type": "S"}
        ]
        
        anxiety_options = {
            "0": "Aucun",
            "1": "Légère",
            "2": "Moyenne",
            "3": "Sévère"
        }
        
        avoidance_options = {
            "0": "Jamais",
            "1": "Occasionnel (0-33%)",
            "2": "Fréquent (33-66%)",
            "3": "Habituel (67-100%)"
        }
        
        for situation in situations:
            # Anxiety rating
            self.questions.append({
                "id": f"LSAS{situation['num']}A",
                "text": f"{situation['num']}. {situation['text']} ({situation['type']}) - ANXIETE",
                "type": "single_choice",
                "required": True,
                "options": anxiety_options
            })
            
            # Avoidance rating
            self.questions.append({
                "id": f"LSAS{situation['num']}E",
                "text": f"{situation['num']}. {situation['text']} ({situation['type']}) - EVITEMENT",
                "type": "single_choice",
                "required": True,
                "options": avoidance_options
            })
    
    def calculate_score(self, responses):
        """
        Calculate LSAS scores.
        
        Args:
            responses: Dictionary with question IDs as keys and response values (0-3) as values
            
        Returns:
            Dictionary containing:
                - total_anxiety: Total anxiety score (0-72)
                - total_avoidance: Total avoidance score (0-72)
                - social_interaction_anxiety: Social interaction anxiety score (0-36)
                - social_interaction_avoidance: Social interaction avoidance score (0-36)
                - performance_anxiety: Performance anxiety score (0-36)
                - performance_avoidance: Performance avoidance score (0-36)
                - total_score: Combined total (0-144)
                - interpretation: Clinical interpretation
        """
        
        if len(responses) != 48:  # 24 situations x 2 ratings
            raise ValueError(f"Expected 48 responses (24 anxiety + 24 avoidance), but got {len(responses)}")
        
        # Calculate total scores
        total_anxiety = sum(responses.get(f"LSAS{i}A", 0) for i in range(1, 25))
        total_avoidance = sum(responses.get(f"LSAS{i}E", 0) for i in range(1, 25))
        
        # Calculate social interaction scores
        social_interaction_anxiety = sum(responses.get(f"LSAS{i}A", 0) for i in self.social_interaction_items)
        social_interaction_avoidance = sum(responses.get(f"LSAS{i}E", 0) for i in self.social_interaction_items)
        
        # Calculate performance scores
        performance_anxiety = sum(responses.get(f"LSAS{i}A", 0) for i in self.performance_items)
        performance_avoidance = sum(responses.get(f"LSAS{i}E", 0) for i in self.performance_items)
        
        # Total combined score
        total_score = total_anxiety + total_avoidance
        
        # Interpretation based on total score
        if total_score < 30:
            severity = "Anxiété sociale absente ou très légère"
        elif total_score < 50:
            severity = "Anxiété sociale légère"
        elif total_score < 65:
            severity = "Anxiété sociale modérée"
        elif total_score < 80:
            severity = "Anxiété sociale marquée"
        elif total_score < 95:
            severity = "Anxiété sociale sévère"
        else:
            severity = "Anxiété sociale très sévère"
        
        return {
            "total_anxiety": total_anxiety,
            "total_avoidance": total_avoidance,
            "social_interaction_anxiety": social_interaction_anxiety,
            "social_interaction_avoidance": social_interaction_avoidance,
            "performance_anxiety": performance_anxiety,
            "performance_avoidance": performance_avoidance,
            "total_score": total_score,
            "interpretation": severity
        }


# Example usage and testing
if __name__ == "__main__":
    lsas = LSASQuestionnaire()
    
    print(f"Questionnaire: {lsas.full_name}")
    print(f"Number of situations: {lsas.num_items}")
    print(f"Total questions (with A and E ratings): {len(lsas.questions)}")
    print(f"\nSocial interaction items: {lsas.social_interaction_items}")
    print(f"Performance items: {lsas.performance_items}")
    
    print(f"\nFirst 4 questions:")
    for q in lsas.questions[:4]:
        print(f"  {q['id']}: {q['text'][:60]}...")
    
    # Test scoring with moderate social anxiety
    test_responses = {}
    # Simulate moderate anxiety (1-2) and occasional avoidance (1) for all situations
    for i in range(1, 25):
        test_responses[f"LSAS{i}A"] = 2  # Moderate anxiety
        test_responses[f"LSAS{i}E"] = 1  # Occasional avoidance
    
    result = lsas.calculate_score(test_responses)
    
    print(f"\n--- Test Scoring (moderate anxiety, occasional avoidance) ---")
    print(f"Total Anxiety: {result['total_anxiety']}/72")
    print(f"Total Avoidance: {result['total_avoidance']}/72")
    print(f"Social Interaction Anxiety: {result['social_interaction_anxiety']}/36")
    print(f"Social Interaction Avoidance: {result['social_interaction_avoidance']}/36")
    print(f"Performance Anxiety: {result['performance_anxiety']}/36")
    print(f"Performance Avoidance: {result['performance_avoidance']}/36")
    print(f"Total Score: {result['total_score']}/144")
    print(f"Interpretation: {result['interpretation']}")

