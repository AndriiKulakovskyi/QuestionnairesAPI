"""
ASQ - Attachment Style Questionnaire
A 40-item self-report questionnaire assessing adult attachment styles.
"""

class ASQQuestionnaire:
    def __init__(self):
        """Initialize the ASQ questionnaire."""
        self.name = "ASQ"
        self.full_name = "Attachment Style Questionnaire"
        self.description = "Questionnaire d'évaluation du style d'attachement chez l'adulte"
        self.num_items = 40
        self.questions = []
        
        # Define which items belong to which subscale (Feeney et al., 1994)
        # Confidence: 1, 3, 5, 6, 8, 19, 28, 37
        # Discomfort with Closeness: 10, 14, 17, 18, 23, 25, 26, 32, 34, 35
        # Need for Approval: 7, 9, 11, 12, 13
        # Preoccupation with Relationships: 22, 24, 27, 29, 30, 39, 40
        # Relationships as Secondary: 2, 4, 36
        
        self.subscales = {
            "confidence": [1, 3, 5, 6, 8, 19, 28, 37],
            "discomfort_closeness": [10, 14, 17, 18, 23, 25, 26, 32, 34, 35],
            "need_approval": [7, 9, 11, 12, 13],
            "preoccupation_relationships": [22, 24, 27, 29, 30, 39, 40],
            "relationships_secondary": [2, 4, 36]
        }
        
        # Items to reverse-score
        self.reverse_items = [1, 5, 8, 15, 18, 19, 20, 21, 31, 37, 38]
        
        self._init_questions()
    
    def _init_questions(self):
        """Initialize all questions for the ASQ questionnaire."""
        
        items_text = [
            "Globalement, je suis une personne qui a de la valeur",
            "Je suis plus facile à connaître que la plupart des gens",
            "Je suis confiant(e) d'avoir des gens auprès de moi quand j'en aurai besoin",
            "Je préfère dépendre de moi seul(e) que de dépendre des autres",
            "Je préfère m'occuper de mes affaires et ne pas me mêler des relations entre les autres personnes de mon entourage",
            "Demander de l'aide c'est admettre que je suis un(e) incapable",
            "La valeur des gens devrait être jugée par leurs réussites",
            "Réussir des choses est plus important que de bâtir des relations",
            "Exceller dans ce qu'on a à faire est plus important que de bien s'entendre avec les autres",
            "Si vous aviez une tâche à faire, vous la feriez sans vous préoccuper de savoir si cela pourrait blesser quelqu'un",
            "Il est important pour moi que les autres m'aiment",
            "Il est important pour moi d'éviter de faire des choses que les autres n'aimeraient pas",
            "Je trouve difficile de prendre une décision sans savoir ce que pensent les autres",
            "Mes relations avec les autres sont généralement peu profondes",
            "Parfois je pense que je ne vaux rien",
            "Je trouve difficile de faire confiance aux autres",
            "Je trouve cela difficile de dépendre des autres",
            "Je trouve que les autres ne se rapprochent pas de moi autant que je le voudrais",
            "Je trouve qu'il est relativement facile de se rapprocher des autres",
            "C'est facile pour moi d'avoir confiance aux autres",
            "Je me sens à l'aise avec l'idée de dépendre des autres",
            "Je m'inquiète que les autres ne s'occupent pas autant de moi que je m'occupe d'eux",
            "Je m'inquiète à l'idée que des gens veuillent trop se rapprocher de moi",
            "Je m'inquiète de ne pas être à la hauteur des autres",
            "Je ne suis pas sûr de vouloir être proche des autres",
            "Bien que je veux être proche des autres, cela me rend mal à l'aise",
            "Je me demande pourquoi les gens veulent être en relation avec moi",
            "Il est très important pour moi d'avoir une relation intime",
            "Je m'inquiète beaucoup à propos de mes relations interpersonnelles",
            "Je me demande comment je me débrouillerais sans avoir quelqu'un qui m'aime",
            "Je me sens confiant(e) à m'ouvrir aux autres",
            "Je me sens souvent délaissé(e) ou seul(e)",
            "Je m'inquiète souvent du fait que je suis différent(e) des autres",
            "Tout le monde a ses propres problèmes, donc je ne tracasse pas les gens avec les miens",
            "Lorsque je parle de mes problèmes aux autres, je me sens généralement honteux(se) ou ridicule",
            "Je suis trop occupé(e) avec mes activités pour mettre du temps dans les relations interpersonnelles",
            "Lorsque quelque chose me tracasse, les autres en sont généralement conscients et intéressés",
            "J'ai confiance que les autres m'aiment et me respectent",
            "Je suis frustré(e) lorsque les autres ne sont pas disponibles quand j'ai besoin d'eux",
            "Les autres me déçoivent souvent"
        ]
        
        options = {
            "1": "Totalement en désaccord",
            "2": "Fortement en désaccord",
            "3": "Faiblement en désaccord",
            "4": "Faiblement en accord",
            "5": "Fortement en accord",
            "6": "Totalement en accord"
        }
        
        for i, text in enumerate(items_text, 1):
            self.questions.append({
                "id": f"ASQ{i}",
                "text": f"{i}. {text}",
                "type": "single_choice",
                "required": True,
                "options": options,
                "reverse_scored": i in self.reverse_items
            })
    
    def calculate_score(self, responses):
        """
        Calculate ASQ scores.
        
        Args:
            responses: Dictionary with question IDs as keys and response values (1-6) as values
            
        Returns:
            Dictionary containing:
                - subscale scores for each of the 5 dimensions
                - subscale_means: Mean scores for each dimension
                - interpretation: Clinical interpretation
        """
        
        if len(responses) != 40:
            raise ValueError(f"Expected 40 responses, but got {len(responses)}")
        
        # Reverse score appropriate items
        adjusted_responses = {}
        for i in range(1, 41):
            item_id = f"ASQ{i}"
            value = responses.get(item_id, 0)
            if i in self.reverse_items:
                # Reverse: 1->6, 2->5, 3->4, 4->3, 5->2, 6->1
                adjusted_responses[item_id] = 7 - value
            else:
                adjusted_responses[item_id] = value
        
        # Calculate subscale scores and means
        subscale_scores = {}
        subscale_means = {}
        
        for subscale_name, item_nums in self.subscales.items():
            score = sum(adjusted_responses.get(f"ASQ{i}", 0) for i in item_nums)
            subscale_scores[subscale_name] = score
            subscale_means[subscale_name] = score / len(item_nums)
        
        # Interpretation
        # High Confidence & Low Discomfort = Secure
        # High Discomfort & Low Preoccupation = Avoidant
        # Low Confidence & High Preoccupation = Anxious
        # High Discomfort & High Preoccupation = Fearful
        
        confidence = subscale_means["confidence"]
        discomfort = subscale_means["discomfort_closeness"]
        preoccupation = subscale_means["preoccupation_relationships"]
        
        if confidence >= 4.5 and discomfort <= 3.0:
            attachment_style = "Attachement sécure"
        elif discomfort >= 4.0 and preoccupation <= 3.0:
            attachment_style = "Attachement évitant"
        elif confidence <= 3.5 and preoccupation >= 4.0:
            attachment_style = "Attachement anxieux"
        elif discomfort >= 4.0 and preoccupation >= 4.0:
            attachment_style = "Attachement craintif"
        else:
            attachment_style = "Style d'attachement mixte ou indéterminé"
        
        # Subscale labels
        subscale_labels = {
            "confidence": "Confiance (sécurité)",
            "discomfort_closeness": "Inconfort avec la proximité",
            "need_approval": "Besoin d'approbation",
            "preoccupation_relationships": "Préoccupation relationnelle",
            "relationships_secondary": "Relations secondaires"
        }
        
        return {
            "subscale_scores": {
                subscale_labels[key]: score 
                for key, score in subscale_scores.items()
            },
            "subscale_means": {
                subscale_labels[key]: round(mean, 2)
                for key, mean in subscale_means.items()
            },
            "attachment_style": attachment_style
        }


# Example usage and testing
if __name__ == "__main__":
    asq = ASQQuestionnaire()
    
    print(f"Questionnaire: {asq.full_name}")
    print(f"Number of items: {asq.num_items}")
    print(f"\nSubscales:")
    for subscale_name, items in asq.subscales.items():
        print(f"  {subscale_name}: {len(items)} items")
    print(f"\nReverse-scored items: {asq.reverse_items}")
    
    print(f"\nFirst 3 questions:")
    for q in asq.questions[:3]:
        print(f"  {q['id']}: {q['text'][:80]}...")
        print(f"    Reverse scored: {q['reverse_scored']}")
    
    # Test scoring with secure attachment pattern
    test_responses = {}
    # Simulate secure attachment: high confidence, low discomfort, moderate others
    for i in range(1, 41):
        if i in asq.subscales["confidence"]:
            test_responses[f"ASQ{i}"] = 5  # High confidence (will be adjusted if reverse)
        elif i in asq.subscales["discomfort_closeness"]:
            test_responses[f"ASQ{i}"] = 2  # Low discomfort
        elif i in asq.subscales["preoccupation_relationships"]:
            test_responses[f"ASQ{i}"] = 3  # Moderate preoccupation
        else:
            test_responses[f"ASQ{i}"] = 3  # Neutral
    
    result = asq.calculate_score(test_responses)
    
    print(f"\n--- Test Scoring (secure attachment pattern) ---")
    print(f"Subscale Scores:")
    for subscale, score in result['subscale_scores'].items():
        print(f"  {subscale}: {score}")
    print(f"\nSubscale Means:")
    for subscale, mean in result['subscale_means'].items():
        print(f"  {subscale}: {mean}")
    print(f"\nAttachment Style: {result['attachment_style']}")

