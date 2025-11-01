import random
from typing import Any, Dict, List

class RBSRQuestionnaire:
    """RBS-R - Repetitive Behavior Scale-Revised
    
    Informant-report questionnaire assessing repetitive behaviors in autism spectrum disorders.
    
    Structure:
    - 43 items across 6 subscales:
      I. Stereotypic Behavior (6 items)
      II. Self-Injurious Behavior (8 items)
      III. Compulsive Behavior (8 items)
      IV. Ritualistic Behavior (6 items)
      V. Sameness/Immutable Behavior (11 items)
      VI. Restricted Interests (4 items)
    
    Scoring:
    - Each item: 0-3 scale
      0 = Behavior not present
      1 = Behavior present and is a mild problem
      2 = Behavior present and is a moderate problem
      3 = Behavior present and is a severe problem
    - Scoring considers: (a) frequency, (b) difficulty interrupting, (c) interference with daily activities
    - Total score: 0-129 (sum of all items)
    - Subscale scores: sum of items within each subscale
    
    Clinical Use:
    - Autism spectrum disorder assessment
    - Treatment planning and monitoring
    - Research on repetitive behaviors
    - Intervention outcome measurement
    """

    def __init__(self):
        self.name = "RBS-R - Repetitive Behavior Scale-Revised"
        self.description = "Échelle des comportements répétitifs (version révisée)."
        self.num_items = 43
        self.used_in_applications = ['asperger']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 43 RBS-R items."""
        
        options = {
            "le comportement n'est pas présent": 0,
            "le comportement est présent et est un problème léger": 1,
            "le comportement est présent et est un problème modéré": 2,
            "le comportement est présent et est un problème sévère": 3
        }
        
        questions = [
            # I. STEREOTYPIC BEHAVIOR
            {"id": "RBSR1", "number": 1, "subscale": "stereotypic",
             "text": "ENSEMBLE DU CORPS (balancement du corps, mouvement de va et vient)", "options": options},
            {"id": "RBSR2", "number": 2, "subscale": "stereotypic",
             "text": "TETE (enroule sa tête, hoche de la tête, tourne sa tête)", "options": options},
            {"id": "RBSR3", "number": 3, "subscale": "stereotypic",
             "text": "MAINS / DOIGTS (agite ses mains, agite ou tord ses doigts, tape des mains, agite ou secoue ses bras ou ses mains)", "options": options},
            {"id": "RBSR4", "number": 4, "subscale": "stereotypic",
             "text": "LOCOMOTION (tourne en rond, tourne sur lui-même saute, bondit)", "options": options},
            {"id": "RBSR5", "number": 5, "subscale": "stereotypic",
             "text": "USAGE D'OBJETS (fait tourner ou pivoter des objets, tourne, frappe ou jette les objets, fait tomber les objets de ses mains)", "options": options},
            {"id": "RBSR6", "number": 6, "subscale": "stereotypic",
             "text": "SENSORIELS (se couvre les yeux, regarde de près ou fixement ses mains ou des objets, se couvre les oreilles, sent ou renifle les choses, frotte des surfaces)", "options": options},
            
            # II. SELF-INJURIOUS BEHAVIOR
            {"id": "RBSR7", "number": 7, "subscale": "self_injurious",
             "text": "SE FRAPPE AVEC UNE PARTIE DE SON CORPS (se frappe ou gifle sa tête, son visage ou une autre partie de son corps)", "options": options},
            {"id": "RBSR8", "number": 8, "subscale": "self_injurious",
             "text": "SE FRAPPE CONTRE UN OBJET OU UNE SURFACE (se frappe ou se donne des coups à la tête ou une autre partie de son corps contre la table, le sol ou une autre surface)", "options": options},
            {"id": "RBSR9", "number": 9, "subscale": "self_injurious",
             "text": "SE FRAPPE AVEC UN OBJET (se frappe ou se donne des coups à la tête ou une autre partie de son corps avec un objet)", "options": options},
            {"id": "RBSR10", "number": 10, "subscale": "self_injurious",
             "text": "SE MORD (se mord la main, le poignet, le bras, les lèvres ou la langue)", "options": options},
            {"id": "RBSR11", "number": 11, "subscale": "self_injurious",
             "text": "SE TIRE (se tire les cheveux ou la peau)", "options": options},
            {"id": "RBSR12", "number": 12, "subscale": "self_injurious",
             "text": "SE GRATTE OU SE FROTTTE (se gratte ou se frotte en laissant des marques sur les bras, les jambes, le visage ou le torse)", "options": options},
            {"id": "RBSR13", "number": 13, "subscale": "self_injurious",
             "text": "INSERT SES DOIGTS OU DES OBJETS (insert ses doigts ou des objets dans ses yeux ou dans ses oreilles)", "options": options},
            {"id": "RBSR14", "number": 14, "subscale": "self_injurious",
             "text": "S'ARRACHE LA PEAU (s'arrache/gratte la peau du visage, des mains, des bras, ou du torse)", "options": options},
            
            # III. COMPULSIVE BEHAVIOR
            {"id": "RBSR15", "number": 15, "subscale": "compulsive",
             "text": "ORDRE/RANGEMENT (Range certains objets dans un ordre précis ou à une place précise. Besoin que les choses soient symétriques ou identiques)", "options": options},
            {"id": "RBSR16", "number": 16, "subscale": "compulsive",
             "text": "COMPLETUDE (Doit avoir les portes fermées ou ouvertes. Sort au complet tous les objets d'une boite ou d'un lieu)", "options": options},
            {"id": "RBSR17", "number": 17, "subscale": "compulsive",
             "text": "LAVAGE / NETTOYAGE (Nettoie excessivement certaines parties de son corps. Ramasse les peluches des vêtements et les fils)", "options": options},
            {"id": "RBSR18", "number": 18, "subscale": "compulsive",
             "text": "VERIFICATION (Vérifie de manière répétée les portes, les fenêtres, les tiroirs, les appareils ménagers, les horloges, les serrures, etc.)", "options": options},
            {"id": "RBSR19", "number": 19, "subscale": "compulsive",
             "text": "COMPTAGE (Compte des objets ou des choses ; compte d'une certaine manière ou jusqu'à un certain nombre)", "options": options},
            {"id": "RBSR20", "number": 20, "subscale": "compulsive",
             "text": "ACCUMULATION / COLLECTIONNISME (Collectionne, accumule ou cache certaines choses)", "options": options},
            {"id": "RBSR21", "number": 21, "subscale": "compulsive",
             "text": "REPETITION (Besoin de répéter des comportements routiniers ; s'assoie et se lève de sa chaise, entre et sort par la porte, s'habille et se déshabille)", "options": options},
            {"id": "RBSR22", "number": 22, "subscale": "compulsive",
             "text": "TOUCHER / TAPER (Besoin de toucher, de taper ou de frotter des objets, des surfaces, des gens)", "options": options},
            
            # IV. RITUALISTIC BEHAVIOR
            {"id": "RBSR23", "number": 23, "subscale": "ritualistic",
             "text": "MANGER / TEMPS DU REPAS (Préfère ou insiste fortement pour manger / boire seulement certaines choses. Mange ou boit des choses dans un certain ordre. Insiste pour que les aliments soient cuisinés d'une certaine manière)", "options": options},
            {"id": "RBSR24", "number": 24, "subscale": "ritualistic",
             "text": "DORMIR / TEMPS DU COUCHER (Insiste sur certaines routines avant de se coucher. Range certaines choses dans la chambre 'juste comme il faut' avant de se mettre au lit. Insiste pour que certaines choses soit avec lui / elle durant le sommeil)", "options": options},
            {"id": "RBSR25", "number": 25, "subscale": "ritualistic",
             "text": "SOIN POUR SE LAVER ET S'HABILLER (Insiste pour respecter un certain ordre dans la réalisation de certaines taches ou activités lors de l'utilisation de la salle de bains, lors de la toilette, de la douche, du bain, ou de l'habillage)", "options": options},
            {"id": "RBSR26", "number": 26, "subscale": "ritualistic",
             "text": "VOYAGE / TRANSPORT (Insiste pour prendre certaines routes / chemins. Doit s'asseoir à une certaine place dans la voiture. Insiste pour que certains objets soient présents durant le trajet)", "options": options},
            {"id": "RBSR27", "number": 27, "subscale": "ritualistic",
             "text": "JEU / LOISIR (Insiste pour jouer à certaines choses. Suit une routine rigide durant les jeux / loisirs. Insiste pour que certaines choses soient présentes / disponibles durant les jeux / loisirs)", "options": options},
            {"id": "RBSR28", "number": 28, "subscale": "ritualistic",
             "text": "COMMUNICATION / INTERACTION SOCIALE (Répète les mêmes sujets de conversation durant les interaction sociales. Pose des questions répétées. Insiste pour parler de certaines choses durant les conversations)", "options": options},
            
            # V. SAMENESS/IMMUTABLE BEHAVIOR
            {"id": "RBSR29", "number": 29, "subscale": "sameness",
             "text": "Insiste pour que les choses restent à la même place (par exemple les jouets, meubles, photos, etc.)", "options": options},
            {"id": "RBSR30", "number": 30, "subscale": "sameness",
             "text": "Refuse de visiter de nouveaux lieux", "options": options},
            {"id": "RBSR31", "number": 31, "subscale": "sameness",
             "text": "S'énerve lorsqu'on l'interrompt dans ce qu'il / elle fait", "options": options},
            {"id": "RBSR32", "number": 32, "subscale": "sameness",
             "text": "Insiste pour marcher d'une certaine manière (par exemple en ligne droite)", "options": options},
            {"id": "RBSR33", "number": 33, "subscale": "sameness",
             "text": "Insiste pour s'asseoir à la même place", "options": options},
            {"id": "RBSR34", "number": 34, "subscale": "sameness",
             "text": "N'aime pas les changements dans le comportement ou l'apparence des gens autour de lui / elle", "options": options},
            {"id": "RBSR35", "number": 35, "subscale": "sameness",
             "text": "Insiste pour utiliser une porte en particulier", "options": options},
            {"id": "RBSR36", "number": 36, "subscale": "sameness",
             "text": "Aime entendre continuellement les mêmes CD, cassettes, enregistrements ou morceaux musicaux. Aime regarder les mêmes films / vidéos ou morceaux de films / vidéos", "options": options},
            {"id": "RBSR37", "number": 37, "subscale": "sameness",
             "text": "Résiste aux changements d'activité. Difficultés avec les transitions", "options": options},
            {"id": "RBSR38", "number": 38, "subscale": "sameness",
             "text": "Insiste pour avoir chaque jour un même programme de ménage, d'école ou de travail", "options": options},
            {"id": "RBSR39", "number": 39, "subscale": "sameness",
             "text": "Insiste pour que chaque chose soit réalisée à une heure précise", "options": options},
            
            # VI. RESTRICTED INTERESTS
            {"id": "RBSR40", "number": 40, "subscale": "restricted",
             "text": "Fascination, préoccupation pour un objet ou une activité (par exemple les trains, les ordinateurs, la météo, les dinosaures)", "options": options},
            {"id": "RBSR41", "number": 41, "subscale": "restricted",
             "text": "Très attaché(e) à un objet en particulier", "options": options},
            {"id": "RBSR42", "number": 42, "subscale": "restricted",
             "text": "Plus préoccupé(e) par une partie d'un objet que par l'objet en totalité (par exemple bouton d'un habit, roues d'une voiture en jouet)", "options": options},
            {"id": "RBSR43", "number": 43, "subscale": "restricted",
             "text": "Fasciné(e), préoccupé(e) par les mouvements ou les choses qui bougent (par exemple ventilateurs, horloges)", "options": options},
        ]
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """Calculate RBS-R total and subscale scores."""
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")

        total_score = 0
        item_scores = {}
        subscale_scores = {
            "stereotypic": 0,
            "self_injurious": 0,
            "compulsive": 0,
            "ritualistic": 0,
            "sameness": 0,
            "restricted": 0
        }
        
        for question in self.questions:
            q_id = question["id"]
            if q_id not in responses:
                raise ValueError(f"Missing response for question {q_id}")
            
            response_text = responses[q_id]
            if response_text not in question["options"]:
                raise ValueError(f"Invalid response for question {q_id}")
            
            score = question["options"][response_text]
            item_scores[q_id] = score
            total_score += score
            subscale_scores[question["subscale"]] += score

        interpretation = self._interpret_score(total_score)
        severity = self._get_severity(total_score)

        return {
            "total_score": total_score,
            "max_score": 129,
            "interpretation": interpretation,
            "severity": severity,
            "subscale_scores": subscale_scores,
            "subscale_interpretations": {
                "stereotypic": f"{subscale_scores['stereotypic']}/18 - Comportements stéréotypés",
                "self_injurious": f"{subscale_scores['self_injurious']}/24 - Comportements automutilatoires",
                "compulsive": f"{subscale_scores['compulsive']}/24 - Comportements compulsifs",
                "ritualistic": f"{subscale_scores['ritualistic']}/18 - Comportements ritualisés",
                "sameness": f"{subscale_scores['sameness']}/33 - Comportements immuables",
                "restricted": f"{subscale_scores['restricted']}/12 - Intérêts restreints"
            },
            "item_scores": item_scores
        }

    def _interpret_score(self, score: int) -> str:
        """Interpret RBS-R total score."""
        if score >= 80:
            return "Comportements répétitifs très sévères"
        elif score >= 50:
            return "Comportements répétitifs sévères"
        elif score >= 30:
            return "Comportements répétitifs modérés"
        elif score >= 15:
            return "Comportements répétitifs légers"
        else:
            return "Comportements répétitifs minimes"

    def _get_severity(self, score: int) -> str:
        """Get severity level."""
        if score >= 80:
            return "very_severe"
        elif score >= 50:
            return "severe"
        elif score >= 30:
            return "moderate"
        elif score >= 15:
            return "mild"
        else:
            return "minimal"

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "Pour chaque item, merci de lire chacun des items listés ci-dessous et de choisir "
            "le score qui convient le mieux pour décrire le comportement du sujet au cours du dernier mois.\n\n"
            "Lorsque vous décidez d'un score pour un item, considérez:\n"
            "(a) la fréquence avec laquelle ce comportement est présent\n"
            "(b) la difficulté qu'a le sujet pour interrompre ce comportement\n"
            "(c) combien le comportement interfère avec les activités quotidiennes du sujet"
        )


if __name__ == '__main__':
    rbsr = RBSRQuestionnaire()
    print(f"Questionnaire: {rbsr.name}")
    print(f"Number of items: {rbsr.num_items}")
    print()
    
    # Test: Moderate severity
    test_responses = {}
    for i in range(1, 44):
        q_id = f"RBSR{i}"
        # Alternate between mild and moderate problems
        if i % 2 == 0:
            test_responses[q_id] = "le comportement est présent et est un problème modéré"
        else:
            test_responses[q_id] = "le comportement est présent et est un problème léger"
    
    result = rbsr.calculate_score(test_responses)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Severity: {result['severity']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    print("Subscale Scores:")
    for subscale, interp in result['subscale_interpretations'].items():
        print(f"  {subscale}: {interp}")
    print()
    print("✓ RBS-R implementation complete - 43 items, 6 subscales, autism repetitive behaviors")

