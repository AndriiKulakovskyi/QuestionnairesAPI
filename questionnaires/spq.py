"""
SPQ - Schizotypal Personality Questionnaire
A 74-item self-report questionnaire assessing schizotypal personality traits.
"""

class SPQQuestionnaire:
    def __init__(self):
        """Initialize the SPQ questionnaire."""
        self.name = "SPQ"
        self.full_name = "Schizotypal Personality Questionnaire"
        self.description = "Questionnaire d'auto-évaluation des traits de personnalité schizotypique"
        self.num_items = 74
        self.questions = []
        
        # Define which items belong to which subscale
        self.subscales = {
            "idees_reference": [1, 10, 19, 28, 37, 45, 53, 60, 63],
            "anxiete_sociale": [2, 11, 20, 29, 38, 46, 54, 71],
            "pensee_magique": [3, 12, 21, 30, 39, 47, 55],
            "perceptions_inhabituelles": [4, 13, 22, 31, 40, 48, 56, 61, 64],
            "comportements_bizarres": [5, 14, 23, 32, 67, 70, 74],
            "absence_amis_proches": [6, 15, 24, 33, 41, 49, 57, 62, 66],
            "discours_bizarre": [7, 16, 25, 34, 42, 50, 58, 69, 72],
            "pauvrete_affects": [8, 17, 26, 35, 43, 51, 68, 73],
            "ideation_persecutoire": [9, 18, 27, 36, 44, 52, 59, 65]
        }
        
        self._init_questions()
    
    def _init_questions(self):
        """Initialize all questions for the SPQ questionnaire."""
        
        items_text = [
            "Il m'arrive d'avoir l'impression que ce que je vois à la télévision ou ce que je lis dans les journaux m'est personnellement destiné",
            "Il m'arrive d'éviter les lieux où il y a de la foule, car j'y deviens facilement anxieux",
            "J'ai déjà eu des expériences en rapport avec des choses surnaturelles",
            "Il peut m'arriver de prendre des ombres ou certains objets pour des personnes ou bien certains bruits pour des voix",
            "Je pense que beaucoup de gens me considèrent comme quelqu'un d'un peu bizarre ou un peu curieux",
            "Je trouve peu d'intérêt à faire la connaissance d'autres personnes",
            "Les gens ont parfois du mal à comprendre ce que je dis quand je me lance dans une explication",
            "Les gens me trouvent parfois lointain ou distant",
            "J'ai le sentiment qu'on parle de moi dans mon dos",
            "Je me rends compte que les gens me remarquent quand je sors pour aller au restaurant ou au cinéma",
            "Je deviens facilement très nerveux quand je suis obligé de tenir des conversations de courtoisie avec les gens",
            "Je pense que certaines personnes ont le don de télépathie (lecture de la pensée des autres)",
            "Il m'est déjà arrivé d'avoir la sensation de sentir une force ou une présence auprès de moi, alors même que j'étais tout seul à ce moment-là",
            "Les gens font parfois des commentaires sur mes comportements ou certaines de mes manières qu'ils trouvent inhabituelles",
            "En général, j'aime mieux garder pour moi ce que je pense",
            "Je saute parfois du coq-à-l'âne quand je discute",
            "J'ai du mal à exprimer mes véritables sentiments, que ce soit au moyen de la parole ou avec le regard",
            "J'ai souvent le sentiment qu'il y a quelque chose en moi qui ne revient pas aux gens",
            "Il m'arrive que les gens me fassent des allusions voilées ou disent des choses à double sens",
            "Ca me rend nerveux de sentir quelqu'un marcher derrière moi",
            "Je suis parfois convaincu que d'autres personnes seraient capables de dire ce que je suis en train de penser",
            "Quand je me regarde dans un miroir ou quand je regarde quelqu'un dans un miroir, il m'arrive d'avoir l'impression de voir le visage se modifier légèrement",
            "Il arrive parfois que les gens pensent que je suis un peu étrange",
            "La plupart du temps je reste silencieux quand je suis avec d'autres personnes",
            "Il m'arrive quelquefois de perdre le fil de ce que je suis en train de dire",
            "Je ris et je souris rarement",
            "J'ai parfois le sentiment que mes amis ou mes collègues de travail ne sont pas vraiment loyaux ou dignes de foi",
            "J'ai déjà remarqué que certains objets ou certaines situations apparemment sans importance peuvent être des sortes de messages si l'on arrive à les décrypter",
            "J'ai souvent peur d'être en compagnie de gens que je ne connais pas bien",
            "Je pense que j'ai parfois le pouvoir d'exercer une influence sur les autres par le pouvoir de la pensée",
            "Il arrive souvent que les gens qui font quelque chose devant moi ou non loin de moi le fassent exprès pour me donner des signes au sujet de quelque chose",
            "On peut se sentir parfois trop proche d'une autre personne, même si on la connaît bien",
            "Je trouve que les gens que je connais ne peuvent pas rester silencieux quand ils sont avec moi",
            "Je me fais souvent des films dans ma tête à propos de choses qui pourraient m'arriver",
            "Je me sens souvent tendu(e) quand je suis avec quelqu'un que je ne connais pas bien",
            "Je pense qu'il arrive parfois que les choses se passent ou non selon la force de la pensée",
            "En général, je me sens submergé par les émotions des autres",
            "Je trouve que je suis souvent le dernier(e) à comprendre le sens d'une blague",
            "Il m'arrive d'avoir l'impression que je peux lire les pensées des gens",
            "Il m'est arrivé d'avoir un « sixième sens » qui m'a permis de savoir des choses dont les autres n'avaient pas connaissance",
            "Je préfère rester chez moi plutôt que de sortir pour rencontrer de nouveaux amis",
            "Les gens me font parfois des remarques pour me dire que je m'exprime de façon trop bizarre",
            "Je n'ai pas tellement envie d'avoir des amis proches",
            "Je trouve que j'observe souvent les effets de mon action sur les gens de façon très détaillée",
            "Je pense qu'il y a quelque chose de mystérieux dans certaines coïncidences qu'on ne peut pas expliquer",
            "Il m'arrive de me demander si le fait d'être observé(e) ou le sujet de conversations n'est pas une simple idée que je me fais",
            "J'ai parfois des sensations sur mon propre corps (par exemple, des picotements, des brûlures) dont la cause n'est pas claire",
            "Je pense que je pourrais me sentir aussi proche d'un étranger que d'un ami",
            "Je préfère ne pas me lier avec des groupes de gens",
            "Il y a des moments où mes propos ne sont pas toujours bien clairs",
            "Les émotions que j'ai ressenties n'ont pas toujours été aussi fortes que celles ressenties par d'autres personnes dans la même situation",
            "Je trouve qu'il est difficile de me sentir proche de quelqu'un",
            "Il m'arrive d'avoir l'impression que les gens parlent de moi",
            "Il m'arrive de me sentir très mal à l'aise dans des situations sociales, même quand j'ai l'impression de faire des choses correctement",
            "Il m'est arrivé d'avoir des expériences très inhabituelles qui sont difficiles à expliquer",
            "Il m'arrive de penser que je peux communiquer par télépathie avec quelqu'un d'autre",
            "Il m'est arrivé de sentir que j'étais séparé(e) de mon propre corps",
            "J'ai tendance à me tenir en retrait dans les situations sociales",
            "Les gens font parfois des commentaires en disant que je suis difficile à connaître",
            "Il m'arrive d'avoir l'impression qu'il se passe quelque chose de bizarre que je ne peux pas expliquer, même si rien de particulier ne se passe",
            "J'ai parfois l'impression que les autres me dévisagent",
            "Il m'arrive d'être subitement distrait par des sons lointains auxquels je n'accorde normalement aucune attention",
            "J'attache peu d'importance au fait d'avoir des amis proches",
            "J'ai parfois le sentiment que les gens parlent de moi",
            "Mes pensées sont parfois si intenses que je peux presque les entendre",
            "Je dois souvent rester vigilant pour que les gens n'abusent pas de ma confiance ou de ma bonne volonté",
            "J'ai le sentiment qu'il ne m'est pas possible d'être proche des gens",
            "Je suis quelqu'un d'original ou d'assez spécial, en tout cas assez différent des autres",
            "Ma manière de m'exprimer n'est pas très expressive et vivante",
            "Je trouve qu'il est difficile de communiquer clairement aux autres ce que j'ai envie de leur dire",
            "J'ai quelques habitudes excentriques",
            "Je me sens très mal à l'aise quand je parle à des gens que je ne connais pas bien",
            "On me fait parfois la remarque que mes propos sont embrouillés",
            "J'ai tendance à garder mes sentiments pour moi",
            "Les gens m'évitent parfois à cause de mon apparence excentrique"
        ]
        
        options = {
            "1": "Oui",
            "0": "Non"
        }
        
        for i, text in enumerate(items_text, 1):
            self.questions.append({
                "id": f"SPQ_{i}",
                "text": f"{i}. {text}",
                "type": "single_choice",
                "required": True,
                "options": options
            })
    
    def calculate_score(self, responses):
        """
        Calculate SPQ scores.
        
        Args:
            responses: Dictionary with question IDs as keys and response values (0 or 1) as values
            
        Returns:
            Dictionary containing:
                - subscale scores for each of the 9 dimensions
                - total_score: Total SPQ score (0-74)
                - interpretation: Clinical interpretation
        """
        
        if len(responses) != 74:
            raise ValueError(f"Expected 74 responses, but got {len(responses)}")
        
        # Calculate subscale scores
        subscale_scores = {}
        for subscale_name, item_nums in self.subscales.items():
            subscale_scores[subscale_name] = sum(
                responses.get(f"SPQ_{i}", 0) for i in item_nums
            )
        
        # Calculate total score
        total_score = sum(subscale_scores.values())
        
        # Interpretation based on total score
        # Cutoff scores from literature (Raine et al., 1991)
        if total_score >= 41:
            severity = "Score élevé - Traits schizotypiques marqués"
        elif total_score >= 32:
            severity = "Score modérément élevé - Traits schizotypiques modérés"
        else:
            severity = "Score dans la norme - Traits schizotypiques légers ou absents"
        
        # Subscale interpretations
        subscale_labels = {
            "idees_reference": "Idées de référence",
            "anxiete_sociale": "Anxiété sociale excessive",
            "pensee_magique": "Pensée magique",
            "perceptions_inhabituelles": "Perceptions inhabituelles",
            "comportements_bizarres": "Comportements bizarres",
            "absence_amis_proches": "Absence d'amis proches",
            "discours_bizarre": "Discours bizarre",
            "pauvrete_affects": "Pauvreté des affects",
            "ideation_persecutoire": "Idéation persécutoire"
        }
        
        return {
            "subscales": {
                subscale_labels[key]: score 
                for key, score in subscale_scores.items()
            },
            "total_score": total_score,
            "interpretation": severity
        }


# Example usage and testing
if __name__ == "__main__":
    spq = SPQQuestionnaire()
    
    print(f"Questionnaire: {spq.full_name}")
    print(f"Number of items: {spq.num_items}")
    print(f"\nSubscales:")
    for subscale_name, items in spq.subscales.items():
        print(f"  {subscale_name}: {len(items)} items")
    
    print(f"\nFirst 3 questions:")
    for q in spq.questions[:3]:
        print(f"  {q['id']}: {q['text'][:80]}...")
    
    # Test scoring with moderate schizotypy
    test_responses = {}
    # Simulate moderate schizotypy (approximately 50% endorsement)
    import random
    random.seed(42)
    for i in range(1, 75):
        test_responses[f"SPQ_{i}"] = random.choice([0, 1])
    
    result = spq.calculate_score(test_responses)
    
    print(f"\n--- Test Scoring (random 50% endorsement) ---")
    print(f"Subscale Scores:")
    for subscale, score in result['subscales'].items():
        print(f"  {subscale}: {score}")
    print(f"\nTotal Score: {result['total_score']}/74")
    print(f"Interpretation: {result['interpretation']}")

