import random
from typing import Any, Dict, List

class BDHIQuestionnaire:
    """BDHI - Buss-Durkee Hostility Inventory
    
    Self-report questionnaire assessing various aspects of hostility and aggression.
    
    Structure:
    - 75 true/false items
    - 8 subscales:
      1. Assault (Physical aggression) - 10 items
      2. Indirect Hostility - 9 items
      3. Irritability - 11 items
      4. Negativism - 5 items
      5. Resentment - 8 items
      6. Suspicion - 10 items
      7. Verbal Hostility - 13 items
      8. Guilt - 9 items
    - 2 composite scores:
      * Attitudinal Component = Resentment + Suspicion
      * Motor Component = Assault + Indirect Hostility + Irritability + Verbal Hostility
    
    Scoring:
    - Items are scored 0 or 1
    - Some items use standard scoring (True=1, False=0)
    - Some items use reverse scoring (True=0, False=1)
    - Higher scores indicate greater hostility/aggression
    """

    def __init__(self):
        self.name = "BDHI - Buss-Durkee Hostility Inventory"
        self.description = "Inventaire d'hostilité de Buss-Durkee."
        self.num_items = 75
        self.used_in_applications = ['ebipolar']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 75 BDHI items with their subscales and scoring."""
        
        # Items with reverse scoring (True=0, False=1)
        reverse_items = {1, 10, 17, 21, 27, 34, 39, 50, 55, 63, 66, 67, 71, 72, 74}
        
        # Subscale assignments
        subscales = {
            'assault': [1, 9, 17, 25, 33, 41, 49, 57, 65, 70],
            'indirect_hostility': [2, 10, 18, 26, 34, 42, 50, 58, 75],
            'irritability': [4, 11, 20, 27, 35, 44, 52, 60, 66, 71, 73],
            'negativism': [3, 12, 19, 28, 36],
            'resentment': [5, 13, 21, 29, 37, 45, 53, 61],
            'suspicion': [6, 14, 22, 30, 38, 46, 54, 62, 67, 72],
            'verbal_hostility': [7, 15, 23, 31, 39, 43, 47, 51, 55, 59, 63, 68, 74],
            'guilt': [8, 16, 24, 32, 40, 48, 56, 64, 69]
        }
        
        # Item texts
        items_text = {
            1: "Il est rare que je lève la main sur quelqu'un, même si j'ai été frappé le premier",
            2: "Il m'arrive parfois de faire circuler des ragots sur des personnes que je n'aime pas",
            3: "Si on ne me demande pas quelque chose gentiment, je ne le fais pas",
            4: "Je m'emporte facilement, mais ça ne dure pas",
            5: "Je n'ai pas l'impression d'obtenir ce qui m'est dû",
            6: "J'ai souvent l'impression qu'on parle de moi derrière mon dos",
            7: "Lorsque je n'approuve pas le comportement de mes amis, je le leur dis",
            8: "Les rares fois où j'ai triché, j'en ai éprouvé des remords intolérables",
            9: "J'ai parfois une envie incontrôlable de faire mal aux autres",
            10: "Je ne perds jamais mon sang froid au point de lancer des objets par terre",
            11: "Parfois, les gens m'agacent, rien que par leur présence",
            12: "Lorsqu'on veut m'imposer une règle qui ne me plaît pas, je suis tenté de passer outre",
            13: "J'ai l'impression que la chance sourit surtout aux autres",
            14: "J'ai tendance à rester sur mes gardes, avec les gens qui se montrent un peu trop gentils avec moi",
            15: "Dans une conversation, je suis rarement de l'avis des autres",
            16: "J'ai parfois des pensées qui me font honte",
            17: "Je ne vois pas ce qui pourrait me pousser à frapper quelqu'un",
            18: "Lorsque je suis en colère, il m'arrive de faire la tête",
            19: "Lorsque quelqu'un me parle sur un ton autoritaire, je fais tout le contraire de ce qu'il me demande",
            20: "Dans bien des cas, je ne montre pas à quel point je peux être irrité",
            21: "Il n'y a pas une seule personne pour laquelle j'éprouve une véritable haine",
            22: "J'ai l'impression d'être détesté par un certain nombre de personnes",
            23: "Je ne peux pas m'empêcher de contredire les gens qui ne sont pas de mon avis",
            24: "Quand on n'assume pas ses responsabilités professionnelles, on ne peut pas avoir la conscience tranquille",
            25: "Si on me frappe, je réponds coup par coup",
            26: "Quand je suis furieux, il m'arrive de claquer les portes",
            27: "Je suis toujours patient avec les autres",
            28: "Lorsqu'on m'a mis en colère, il m'arrive de m'enfermer dans un mutisme profond",
            29: "Lorsque je pense à tout ce qui m'est arrivé dans la vie, j'éprouve une certaine rancoeur",
            30: "J'ai l'impression d'être jalousé par un certain nombre de personnes",
            31: "J'exige que les gens respectent mes droits",
            32: "La pensée de ne pas avoir fait plus pour mes parents me donne des remords",
            33: "Quiconque m'insulte, moi ou ma famille, cherche vraiment la bagarre",
            34: "Je ne fais jamais de mauvaises plaisanteries aux autres",
            35: "Lorsqu'on se moque de moi, je vois rouge",
            36: "Il suffit qu'on me donne un ordre, pour que je mette trois heures à l'exécuter",
            37: "Je rencontre souvent des gens qui me déplaisent",
            38: "J'ai parfois le sentiment que les gens se moquent de moi",
            39: "Je ne me montre jamais désagréable dans mes propos, même lorsqu'on m'a mis en colère",
            40: "Je pense sans arrêt à me faire pardonner pour les fautes que j'ai commises",
            41: "Les gens qui n'arrêtent pas de vous chercher des histoires méritent qu'on leur casse la figure",
            42: "Lorsque je n'obtiens pas ce que je veux, il m'arrive de bouder",
            43: "Lorsque quelqu'un m'agace, je suis capable de le lui faire savoir",
            44: "Je me sens souvent prêt à exploser",
            45: "Même si je ne le montre pas, je suis parfois dévoré de jalousie",
            46: "J'ai pour principe de ne jamais faire confiance à un inconnu",
            47: "Si on crie après moi, je réponds sur le même ton",
            48: "J'éprouve souvent des remords",
            49: "Quand je perds mon sang froid, je suis capable de gifler quelqu'un",
            50: "Sorti de l'enfance, je n'ai plus eu de véritables crises de nerfs",
            51: "Il m'arrive de dire des choses méchantes lorsque je suis en colère",
            52: "Il m'arrive de me sentir aigri",
            53: "Si les gens pouvaient deviner ce que je pense, ils ne me trouveraient vraiment pas commode à vivre",
            54: "Je me demande souvent quelles peuvent bien être les motivations profondes des gens qui se montrent gentils avec moi",
            55: "Je suis incapable de « remettre quelqu'un à sa place », même s'il le mérite",
            56: "Devant un échec, je me sens coupable et j'ai des remords",
            57: "Il m'arrive de me bagarrer physiquement, mais pas plus qu'un autre",
            58: "Il m'est arrivé d'être en colère au point de casser ce que j'avais sous la main",
            59: "Il m'arrive souvent de proférer des menaces que je n'ai pas vraiment l'intention d'exécuter",
            60: "Je ne peux pas m'empêcher d'être un peu « cassant » avec les gens que je n'aime pas",
            61: "J'ai parfois le sentiment que la vie ne me fait vraiment pas de cadeaux",
            62: "J'ai trop cru à la sincérité des gens et j'en suis revenu",
            63: "Je n'exprime généralement pas la mauvaise opinion que j'ai des autres",
            64: "Quand je fais quelque chose de mal, ma conscience me le fait payer cher",
            65: "Si je dois recourir à la violence physique pour défendre mes droits, je le fais",
            66: "Si quelqu'un se montre incorrect avec moi, cela ne m'affecte pas outre mesure",
            67: "Je n'ai pas de véritables ennemis",
            68: "Quand je défends mon point de vue, j'ai tendance à hausser le ton",
            69: "J'ai souvent le sentiment que je n'ai pas fait ce que j'aurais dû faire dans la vie",
            70: "Il est arrivé que des gens me provoquent à un tel point que nous en sommes venus aux mains",
            71: "Je ne me laisse pas atteindre par des choses sans importance",
            72: "J'ai rarement l'impression que les gens essayent de m'agresser ou de s'en prendre à moi",
            73: "Ces derniers temps, j'ai été plutôt « de mauvais poil »",
            74: "Je préfère faire des concessions plutôt que de me laisser entraîner dans une dispute",
            75: "Il m'arrive de montrer ma colère en tapant sur la table"
        }
        
        questions = []
        for item_num in range(1, 76):
            # Determine subscale
            item_subscale = None
            for subscale, items in subscales.items():
                if item_num in items:
                    item_subscale = subscale
                    break
            
            questions.append({
                "id": f"BDHI{item_num}",
                "number": item_num,
                "text": items_text[item_num],
                "options": ["Vrai", "Faux"],
                "subscale": item_subscale,
                "reverse_scored": item_num in reverse_items
            })
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        Calculate BDHI subscale and composite scores.

        Args:
            responses (Dict[str, str]): A dictionary of responses, where the key is the question ID
                                       (e.g., "BDHI1") and the value is "Vrai" or "Faux".

        Returns:
            Dict[str, Any]: A dictionary containing subscale and composite scores.
        """
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")

        # Initialize subscale scores
        subscale_scores = {
            'assault': 0,
            'indirect_hostility': 0,
            'irritability': 0,
            'negativism': 0,
            'resentment': 0,
            'suspicion': 0,
            'verbal_hostility': 0,
            'guilt': 0
        }
        
        # Calculate scores
        for question in self.questions:
            q_id = question["id"]
            if q_id not in responses:
                raise ValueError(f"Missing response for question {q_id}")
            
            response = responses[q_id]
            if response not in question["options"]:
                raise ValueError(f"Invalid response '{response}' for question {q_id}")
            
            # Score the item
            if question["reverse_scored"]:
                # Reverse scoring: True=0, False=1
                score = 0 if response == "Vrai" else 1
            else:
                # Standard scoring: True=1, False=0
                score = 1 if response == "Vrai" else 0
            
            # Add to subscale
            subscale_scores[question["subscale"]] += score

        # Calculate composite scores
        attitudinal_component = subscale_scores['resentment'] + subscale_scores['suspicion']
        motor_component = (subscale_scores['assault'] + subscale_scores['indirect_hostility'] + 
                          subscale_scores['irritability'] + subscale_scores['verbal_hostility'])

        return {
            "subscales": subscale_scores,
            "composites": {
                "attitudinal_component": attitudinal_component,
                "motor_component": motor_component
            },
            "subscale_max_scores": {
                'assault': 10,
                'indirect_hostility': 9,
                'irritability': 11,
                'negativism': 5,
                'resentment': 8,
                'suspicion': 10,
                'verbal_hostility': 13,
                'guilt': 9
            }
        }

    def get_random_responses(self) -> Dict[str, str]:
        """Generates random valid responses for testing purposes."""
        responses = {}
        for question in self.questions:
            responses[question["id"]] = random.choice(question["options"])
        return responses

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "Ce questionnaire explore un certain nombre de comportements et de réactions émotionnelles "
            "que l'on peut rencontrer chez tout individu. Certaines des formulations décrivent des réactions "
            "d'énervement, d'agacement ou d'agressivité, observables dans la vie courante. L'agressivité est "
            "une réaction émotionnelle naturelle et normale qui permet à l'individu de se défendre et de faire "
            "face à de nombreuses situations difficiles ou menaçantes.\n\n"
            "Ce questionnaire ne comporte donc pas de « bonnes » ou de « mauvaises » réponses. Il n'a d'intérêt "
            "que si vous répondez sincèrement à toutes les questions, en cochant la case « vrai » si une "
            "description s'applique plutôt bien à vous, ou la case « faux », dans le cas contraire.\n\n"
            "Pour chacun des items, répondez VRAI ou FAUX."
        )


if __name__ == '__main__':
    bdhi = BDHIQuestionnaire()
    print(f"Questionnaire: {bdhi.name}")
    print(f"Description: {bdhi.description}")
    print(f"Number of items: {bdhi.num_items}")
    print(f"Used in applications: {bdhi.used_in_applications}")
    print()
    print("="*80)
    print("Sample items (first 5):")
    for q in bdhi.questions[:5]:
        reverse_note = " [REVERSE]" if q['reverse_scored'] else ""
        print(f"{q['number']}. {q['text']}{reverse_note}")
        print(f"   Subscale: {q['subscale']}")
    print()
    print("="*80)
    
    # Test with high aggression profile
    print("\nExample 1: High Aggression Profile")
    high_agg = {}
    for q in bdhi.questions:
        # Answer True for aggressive items, False for reverse items
        if q['subscale'] in ['assault', 'irritability', 'verbal_hostility']:
            high_agg[q['id']] = "Faux" if q['reverse_scored'] else "Vrai"
        else:
            high_agg[q['id']] = "Vrai" if q['reverse_scored'] else "Faux"
    
    result = bdhi.calculate_score(high_agg)
    print("Subscale Scores:")
    for subscale, score in result['subscales'].items():
        max_score = result['subscale_max_scores'][subscale]
        print(f"  {subscale}: {score}/{max_score}")
    print(f"\nComposite Scores:")
    print(f"  Attitudinal Component: {result['composites']['attitudinal_component']}")
    print(f"  Motor Component: {result['composites']['motor_component']}")
    print()
    
    # Test with low aggression profile
    print("Example 2: Low Aggression Profile")
    low_agg = {}
    for q in bdhi.questions:
        # Answer False for aggressive items, True for reverse items
        low_agg[q['id']] = "Vrai" if q['reverse_scored'] else "Faux"
    
    result = bdhi.calculate_score(low_agg)
    print("Subscale Scores:")
    for subscale, score in result['subscales'].items():
        max_score = result['subscale_max_scores'][subscale]
        print(f"  {subscale}: {score}/{max_score}")
    print(f"\nComposite Scores:")
    print(f"  Attitudinal Component: {result['composites']['attitudinal_component']}")
    print(f"  Motor Component: {result['composites']['motor_component']}")
    print()
    
    print("="*80)
    print("✓ BDHI implementation complete")
    print("  - 75 items with True/False format")
    print("  - 8 subscales with reverse scoring")
    print("  - 2 composite scores")
    print("  - Comprehensive hostility assessment")

