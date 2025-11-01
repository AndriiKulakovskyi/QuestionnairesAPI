"""
Social Anhedonia Scale - Échelle d'Anhédonie Sociale
A questionnaire assessing social interest and pleasure in social interactions.
"""

class SocialAnhedoniaQuestionnaire:
    def __init__(self):
        """Initialize the Social Anhedonia questionnaire."""
        self.name = "Social Anhedonia"
        self.full_name = "Social Anhedonia Scale - Échelle d'Anhédonie Sociale"
        self.description = "Échelle d'évaluation de l'intérêt social et du plaisir dans les interactions sociales"
        self.num_items = 40
        self.questions = []
        
        # Items that are reverse-scored (higher scores on these = lower anhedonia)
        self.reverse_items = [4, 5, 7, 8, 9, 11, 12, 15, 16, 17, 18, 19, 21, 22, 24, 25, 
                              27, 28, 29, 31, 33, 34, 35, 37, 38, 39, 40]
        
        self._init_questions()
    
    def _init_questions(self):
        """Initialize all 40 Social Anhedonia items."""
        
        questions_text = [
            "Avoir des amis intimes n'est pas aussi important que beaucoup de personnes le disent",
            "J'attache très peu d'importance à avoir des amis intimes",
            "Je préfère regarder la télévision plutôt que de sortir avec des gens",
            "Un trajet en voiture est beaucoup plus agréable si quelqu'un est avec moi",
            "J'aime faire des appels téléphoniques à longue distance à des amis ou à des proches",
            "Jouer avec des enfants est une vraie corvée",
            "J'ai toujours aimé regarder des photographies d'amis",
            "Bien qu'il y ait des choses que j'aime faire seul(e), je m'amuse plus en les faisant avec d'autres",
            "Je deviens parfois profondément attaché(e) aux gens avec qui je passe beaucoup de temps",
            "Parfois les gens pensent que je suis timide quand je veux simplement qu'on me laisse seul(e)",
            "Quand les choses vont vraiment bien pour mes amis proches, cela me fait plaisir",
            "Quand quelqu'un proche de moi est déprimé, cela me déprime aussi",
            "Mes réponses émotionnelles semblent très différentes de celles des autres gens",
            "Quand je suis seul(e) à la maison, je n'aime pas que quelqu'un me téléphone",
            "Le fait d'être avec des amis me fait me sentir vraiment bien",
            "Juste être avec des amis peut me remonter le moral",
            "Quand je suis avec d'autres gens, je suis souvent perdu(e) dans mes pensées",
            "Il est important pour moi de rester en contact avec mes amis",
            "Recevoir une lettre d'un ami peut être vraiment excitant",
            "Etre avec d'autres gens est un bon moyen de passer le temps",
            "J'apprécierais vraiment de faire un voyage de vacances avec un groupe d'amis",
            "J'ai très peu besoin d'une vie sociale en dehors de ma famille",
            "Je préférerais lire un livre ou regarder la télévision plutôt que d'aller à une réception",
            "J'aime vraiment parler avec d'autres gens",
            "L'idée d'organiser une réception pour des amis me donne de l'entrain",
            "Traîner avec des amis est souvent une perte de temps pour moi",
            "J'ai en général beaucoup de plaisir à converser avec les gens",
            "Je préférerais qu'on me laisse seul(e) plutôt que d'être avec un grand groupe de gens",
            "Je tire vraiment satisfaction à parler avec d'autres gens",
            "Je préfère habituellement faire les choses seul(e)",
            "Même lorsque je suis avec d'autres gens, je finis en général par être seul(e)",
            "Je préfère être seul(e) plutôt que d'avoir un(e) colocataire",
            "Etre autour d'amis est souvent beaucoup d'amusement",
            "Aller à des réunions sociales est souvent ennuyeux",
            "Un de mes grands plaisirs dans la vie est d'être avec un groupe d'amis",
            "La solitude me rend mal à l'aise",
            "S'engager dans des activités avec d'autres gens me donne en général plus de plaisir que de les faire seul(e)",
            "Des projets de groupe me donnent de l'enthousiasme",
            "Aller à des réceptions ou à d'autres fonctions sociales semble généralement être une perte de temps",
            "Si j'avais le choix, je passerais tout mon temps avec d'autres gens"
        ]
        
        response_options = ["Vrai", "Faux"]
        
        for idx, text in enumerate(questions_text, 1):
            self.questions.append({
                "id": f"ANH-SO{idx}",
                "text": text,
                "responses": response_options,
                "scoring": {"Vrai": 1, "Faux": 0},
                "reverse_scored": idx in self.reverse_items
            })
    
    def calculate_score(self, responses: dict) -> dict:
        """
        Calculate Social Anhedonia score.
        
        Args:
            responses: Dictionary mapping question IDs to response values (1=Vrai, 0=Faux)
                      (e.g., {"ANH-SO1": 1, "ANH-SO2": 0, ...})
        
        Returns:
            Dictionary containing:
            - total_score: Total score (0-40, higher = more social anhedonia)
            - interpretation: Clinical interpretation
        """
        if not responses:
            return {
                "total_score": 0,
                "interpretation": "No responses provided"
            }
        
        total_score = 0
        
        for q in self.questions:
            q_id = q["id"]
            if q_id in responses:
                value = responses[q_id]
                
                # Apply reverse scoring for appropriate items
                if q["reverse_scored"]:
                    # For reverse items, "Faux" (0) indicates anhedonia
                    total_score += (1 - value)
                else:
                    # For regular items, "Vrai" (1) indicates anhedonia
                    total_score += value
        
        # Interpret results
        if total_score >= 24:
            severity = "Anhédonie sociale sévère - Désintérêt social marqué"
        elif total_score >= 16:
            severity = "Anhédonie sociale modérée - Plaisir social réduit"
        elif total_score >= 8:
            severity = "Anhédonie sociale légère - Quelques difficultés"
        else:
            severity = "Normal - Intérêt et plaisir social préservés"
        
        return {
            "total_score": total_score,
            "interpretation": f"{severity} (Score: {total_score}/40)"
        }


if __name__ == '__main__':
    # Example usage
    sa = SocialAnhedoniaQuestionnaire()
    
    print(f"Questionnaire: {sa.full_name}")
    print(f"Number of items: {sa.num_items}\n")
    
    # Example 1: High social anhedonia
    print("Example 1: High social anhedonia")
    responses1 = {}
    for i in range(1, 41):
        q_id = f"ANH-SO{i}"
        # Answer in direction of anhedonia
        if i in sa.reverse_items:
            responses1[q_id] = 0  # False for reverse items = anhedonia
        else:
            responses1[q_id] = 1  # True for regular items = anhedonia
    result1 = sa.calculate_score(responses1)
    print(f"Total score: {result1['total_score']}/40")
    print(f"Interpretation: {result1['interpretation']}\n")
    
    # Example 2: Normal social interest
    print("Example 2: Normal social interest")
    responses2 = {}
    for i in range(1, 41):
        q_id = f"ANH-SO{i}"
        # Answer opposite to anhedonia
        if i in sa.reverse_items:
            responses2[q_id] = 1  # True for reverse items = normal
        else:
            responses2[q_id] = 0  # False for regular items = normal
    result2 = sa.calculate_score(responses2)
    print(f"Total score: {result2['total_score']}/40")
    print(f"Interpretation: {result2['interpretation']}\n")
    
    # Example 3: Moderate
    print("Example 3: Moderate social anhedonia (mixed responses)")
    import random
    random.seed(42)
    responses3 = {f"ANH-SO{i}": random.randint(0, 1) for i in range(1, 41)}
    result3 = sa.calculate_score(responses3)
    print(f"Total score: {result3['total_score']}/40")
    print(f"Interpretation: {result3['interpretation']}\n")

