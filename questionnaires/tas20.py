from typing import Dict, List, Any

class TAS20Questionnaire:
    """
    TAS-20 (Toronto Alexithymia Scale - 20 items)
    
    Description:
    20-item self-report measure of alexithymia (difficulty identifying and describing emotions).
    
    Three subscales:
    - Difficulty Identifying Feelings (DIF): 7 items
    - Difficulty Describing Feelings (DDF): 5 items
    - Externally Oriented Thinking (EOT): 8 items
    
    Scoring: 1-5 Likert scale
    Reverse scored items: 4, 5, 10, 18, 19
    Total range: 20-100
    
    Interpretation:
    - ≤51: Non-alexithymic
    - 52-60: Possible alexithymia
    - ≥61: Alexithymic
    """
    
    def __init__(self):
        self.name = "TAS-20"
        self.description = "Toronto Alexithymia Scale"
        self.num_items = 20
        self.reverse_items = [3, 4, 9, 17, 18]  # 0-indexed
        self.questions = []
        self._init_questions()
    
    def _init_questions(self):
        """Initialize the 20 TAS items."""
        items = [
            ("Souvent, je ne vois pas très clair dans mes sentiments", "DIF"),
            ("J'ai du mal à trouver les mots qui correspondent bien à mes sentiments", "DDF"),
            ("J'éprouve des sensations physiques que les médecins ne comprennent pas", "DIF"),
            ("J'arrive facilement à décrire mes sentiments", "DDF"),  # REVERSE
            ("Je préfère analyser les problèmes plutôt que de me contenter de les décrire", "EOT"),  # REVERSE
            ("Quand je suis bouleversé(e) je ne sais pas si je suis triste, effrayé(e) ou en colère", "DIF"),
            ("Je suis souvent intrigué(e) par des sensations au niveau de mon corps", "DIF"),
            ("Je préfère simplement laisser les choses se produire", "EOT"),
            ("J'ai des sentiments que je ne suis guère capable d'identifier", "DIF"),
            ("Être conscient de ses émotions est essentiel", "EOT"),  # REVERSE
            ("Je trouve difficile de décrire mes sentiments sur les gens", "DDF"),
            ("On me dit de décrire davantage ce que je ressens", "DDF"),
            ("Je ne sais pas ce qui se passe à l'intérieur de moi", "DIF"),
            ("Bien souvent, je ne sais pas pourquoi je suis en colère", "DIF"),
            ("Je préfère parler aux gens de leurs activités quotidiennes plutôt que de leurs sentiments", "EOT"),
            ("Je préfère regarder des émissions de variété plutôt que des films dramatiques", "EOT"),
            ("Il m'est difficile de révéler mes sentiments intimes", "DDF"),
            ("Je peux me sentir proche de quelqu'un même pendant les moments de silence", "EOT"),  # REVERSE
            ("Je trouve utile d'analyser mes sentiments pour résoudre mes problèmes personnels", "EOT"),  # REVERSE
            ("Rechercher le sens caché des films perturbe le plaisir qu'ils procurent", "EOT")
        ]
        
        response_options = {
            1: "Désaccord complet",
            2: "Désaccord relatif",
            3: "Ni accord ni désaccord",
            4: "Accord relatif",
            5: "Accord complet"
        }
        
        for i, (text, subscale) in enumerate(items):
            self.questions.append({
                'id': f'TAS{i+1}',
                'text': text,
                'responses': response_options,
                'subscale': subscale,
                'reverse': i in self.reverse_items
            })
    
    def calculate_score(self, responses: List[int]) -> Dict[str, Any]:
        """Calculate TAS-20 scores."""
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, got {len(responses)}")
        
        if any(r < 1 or r > 5 for r in responses):
            raise ValueError("All responses must be between 1 and 5")
        
        # Apply reverse scoring
        scored = []
        for i, r in enumerate(responses):
            if i in self.reverse_items:
                scored.append(6 - r)
            else:
                scored.append(r)
        
        # Subscale mapping (0-indexed)
        dif_items = [0, 2, 5, 6, 8, 12, 13]
        ddf_items = [1, 3, 10, 11, 16]
        eot_items = [4, 7, 9, 14, 15, 17, 18, 19]
        
        dif_score = sum(scored[i] for i in dif_items)
        ddf_score = sum(scored[i] for i in ddf_items)
        eot_score = sum(scored[i] for i in eot_items)
        total_score = sum(scored)
        
        return {
            'total_score': total_score,
            'DIF': dif_score,
            'DDF': ddf_score,
            'EOT': eot_score,
            'interpretation': self._interpret(total_score),
            'max_score': 100
        }
    
    def _interpret(self, score: int) -> str:
        """Interpret TAS-20 score."""
        if score <= 51:
            return "Non-alexithymic"
        elif score <= 60:
            return "Possible alexithymia"
        else:
            return "Alexithymic"

if __name__ == '__main__':
    tas = TAS20Questionnaire()
    print(f"Questionnaire: {tas.name} - {tas.num_items} items\n")
    
    # Example 1: Non-alexithymic
    print("Example 1: Non-Alexithymic")
    responses1 = [2, 2, 1, 4, 4, 2, 1, 2, 1, 4, 2, 2, 1, 2, 2, 2, 2, 4, 4, 2]
    result1 = tas.calculate_score(responses1)
    print(f"Total: {result1['total_score']}/100 - {result1['interpretation']}")
    print(f"DIF: {result1['DIF']}, DDF: {result1['DDF']}, EOT: {result1['EOT']}\n")
    
    # Example 2: Possible alexithymia
    print("Example 2: Possible Alexithymia")
    responses2 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    result2 = tas.calculate_score(responses2)
    print(f"Total: {result2['total_score']}/100 - {result2['interpretation']}")
    print(f"DIF: {result2['DIF']}, DDF: {result2['DDF']}, EOT: {result2['EOT']}\n")
    
    # Example 3: Alexithymic
    print("Example 3: Alexithymic")
    responses3 = [5, 5, 4, 2, 2, 5, 4, 5, 5, 2, 5, 5, 5, 5, 5, 5, 5, 1, 2, 5]
    result3 = tas.calculate_score(responses3)
    print(f"Total: {result3['total_score']}/100 - {result3['interpretation']}")
    print(f"DIF: {result3['DIF']}, DDF: {result3['DDF']}, EOT: {result3['EOT']}")
