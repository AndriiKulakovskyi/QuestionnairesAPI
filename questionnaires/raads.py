import random
from typing import Any, Dict, List

class RAADSQuestionnaire:
    """RAADS-R - Ritvo Autism Asperger Diagnostic Scale-Revised
    
    Adult self-report questionnaire for autism spectrum disorder screening.
    
    Structure:
    - 80 items across 4 subscales:
      1. Social Relatedness (39 items)
      2. Circumscribed Interests (14 items)
      3. Language (7 items)
      4. Sensory Motor (20 items)
    
    Scoring:
    - Each item: 0-3 scale reflecting developmental trajectory
      0 = Never true (Jamais vrai)
      1 = True only when I was younger than 16 (Vrai seulement quand j'avais moins de 16 ans)
      2 = True only now (Vrai seulement maintenant)
      3 = True now and when I was younger than 16 (Vrai maintenant et quand j'avais moins de 16 ans)
    - Some items are reverse-scored (neurotypical responses get points)
    - Total score: 0-240
    - Clinical cutoff: ≥65 suggests autism spectrum
    
    Clinical Use:
    - Adult autism screening
    - Differential diagnosis
    - Research tool
    """

    def __init__(self):
        self.name = "RAADS-R - Ritvo Autism Asperger Diagnostic Scale-Revised"
        self.description = "Échelle diagnostique de l'autisme et du syndrome d'Asperger chez l'adulte."
        self.num_items = 80
        self.used_in_applications = ['asperger']
        
        # Items that are reverse-scored (neurotypical answers get points)
        self.reverse_items = [1, 6, 11, 18, 23, 26, 37, 43, 47, 48, 53, 58, 62, 68, 72, 77]
        
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 80 RAADS-R items with subscale mappings."""
        
        options = {
            "Jamais vrai": 0,
            "Vrai seulement quand j'avais moins de 16 ans": 1,
            "Vrai seulement maintenant": 2,
            "Vrai maintenant et quand j'avais moins de 16 ans": 3
        }
        
        # Subscale mapping based on RAADS-R structure
        # SR = Social Relatedness, CI = Circumscribed Interests, L = Language, SM = Sensory Motor
        subscale_map = {
            1: "social", 2: "language", 3: "social", 4: "language", 5: "social", 
            6: "social", 7: "language", 8: "circumscribed", 9: "circumscribed", 10: "sensory",
            11: "social", 12: "social", 13: "circumscribed", 14: "social", 15: "social",
            16: "sensory", 17: "social", 18: "social", 19: "sensory", 20: "social",
            21: "social", 22: "social", 23: "social", 24: "circumscribed", 25: "social",
            26: "social", 27: "social", 28: "social", 29: "sensory", 30: "circumscribed",
            31: "social", 32: "social", 33: "language", 34: "sensory", 35: "language",
            36: "sensory", 37: "social", 38: "social", 39: "social", 40: "circumscribed",
            41: "circumscribed", 42: "sensory", 43: "social", 44: "social", 45: "social",
            46: "sensory", 47: "social", 48: "social", 49: "language", 50: "circumscribed",
            51: "sensory", 52: "circumscribed", 53: "social", 54: "social", 55: "social",
            56: "social", 57: "sensory", 58: "social", 59: "sensory", 60: "social",
            61: "social", 62: "language", 63: "circumscribed", 64: "social", 65: "sensory",
            66: "language", 67: "sensory", 68: "social", 69: "social", 70: "circumscribed",
            71: "sensory", 72: "social", 73: "sensory", 74: "sensory", 75: "circumscribed",
            76: "social", 77: "social", 78: "circumscribed", 79: "social", 80: "circumscribed"
        }
        
        items_text = [
            "Je suis une personne compatissante",
            "J'utilise souvent des mots et des phrases entendus dans des films ou à la télévision dans les conversations",
            "Je suis souvent surpris lorsque les autres me disent que j'ai été impoli",
            "Parfois je parle trop fort ou trop doucement, et je ne m'en aperçois pas",
            "J'ai souvent des difficultés à savoir comment me comporter en société",
            "Je peux « me mettre dans la peau de quelqu'un d'autre »",
            "J'ai du mal à comprendre le sens de certaines phrases comme « je tiens à toi comme à la prunelle de mes yeux »",
            "J'aime seulement parler aux gens qui partagent mes centres d'intérêts",
            "Je fais plus attention aux détails qu'à l'idée générale",
            "Je suis sensible à l'effet produit par un aliment dans ma bouche. Ceci est plus important que son goût",
            "Mes meilleurs amis ou ma famille me manquent quand nous sommes séparés depuis longtemps",
            "Quelquefois je vexe les autres en disant ce que je pense, sans le faire exprès",
            "J'aime seulement penser et parler des choses qui m'intéressent",
            "Je préfère aller manger dans un restaurant tout seul plutôt qu'avec quelqu'un que je connais",
            "Je n'arrive pas à imaginer comment ce serait d'être quelqu'un d'autre",
            "On m'a déjà dit que j'étais maladroit ou que je manquais de coordination",
            "Les autres me trouvent étrange ou différent",
            "Je comprends lorsque des amis ont besoin d'être réconfortés",
            "Je suis très sensible au contact de mes vêtements lorsqu je les touche. Leur texture est plus importante pour moi que leur look",
            "J'aime copier la manière dont certaines personnes parlent et agissent. Cela m'aide à me sentir plus « normal »",
            "Cela peut être très intimidant pour moi de parler à plus d'une personne en même temps",
            "Je dois adopter un comportement « normal » pour plaire aux autres et pour qu'ils m'apprécient",
            "Rencontrer de nouvelles personnes est habituellement facile pour moi",
            "Je suis déstabilisé lorsque quelqu'un m'interrompt alors que je parle de quelque chose qui m'intéresse beaucoup",
            "Il m'est difficile de percevoir les sentiments des autres lors d'une conversation",
            "J'aime avoir une conversation avec plusieurs personnes, par exemple lors d'un dîner, à l'école, ou au travail",
            "Je prends les choses trop au premier degré, ainsi je passe à côté de ce que les gens essaient de dire",
            "C'est très difficile pour moi de comprendre lorsque quelqu'un est gêné ou jaloux",
            "Certaines textures ordinaires qui ne posent aucun problème aux autres sont pour moi insupportables lorsqu'elles sont au contact de ma peau",
            "Je suis très contrarié lorsqu'on m'empêche de faire les choses à ma façon",
            "Je n'ai jamais désiré ou eu besoin de ce que les autres personnes appellent une « relation intime »",
            "C'est difficile pour moi de commencer et d'arrêter une conversation. J'ai besoin d'aller jusqu'au bout de mon propos",
            "Je parle avec un rythme de voix normal",
            "Je peux sans transition être très sensible ou pas du tout sensible au même son, à la même couleur ou à la même texture",
            "La phrase « je t'ai dans la peau » me met mal à l'aise",
            "Quelquefois la sonorité d'un mot ou un bruit aigu peut me faire mal aux oreilles",
            "On me considère comme une personne très compréhensive",
            "Je ne peux pas m'identifier à un personnage dans un film, et je ne peux pas ressentir ce qu'il ressent",
            "Je ne peux pas dire si quelqu'un est en train de me draguer",
            "Je peux me représenter avec précision les détails qui m'intéressent",
            "Je fais des listes de choses qui m'intéressent, même si elles n'ont pas d'utilité pratique",
            "Quand je me sens dépassé par des stimulations sensorielles, je dois m'isoler pour y échapper",
            "J'aime parler de choses et d'autres avec mes amis",
            "Je ne peux pas dire si quelqu'un est intéressé ou ennuyé par ce que je dis",
            "Lorsque quelqu'un est en train de parler, il peut m'être très difficile de lire sur son visage, de comprendre les mouvements de ses mains ou de son corps",
            "Je peux ressentir à différents moments la même chose très différemment (comme des vêtements ou la température)",
            "Je me sens très à l'aise lors d'un rendez vous amoureux ou lorsque je me trouve en société",
            "J'essaie d'être aussi aidant que possible lorsque les autres me parlent de leurs problèmes personnels",
            "On m'a dit que j'avais une voix particulière (par exemple, plate, monotone, enfantine ou aigue)",
            "Quelquefois une idée ou un sujet reste bloqué dans mon esprit et je dois en parler, même si cela n'intéresse personne",
            "Je fais certaines choses avec mes mains de façon répétée (comme un battement d'ailes, faire tournoyer un bâton ou une ficelle, agiter des choses devant mes yeux)",
            "Je n'ai jamais été intéressé par ce que la plupart des gens que je connais considèrent comme intéressant",
            "On me considère comme une personne compatissante",
            "Pour m'entendre avec les autres, je suis un ensemble de règles spécifiques qui m'aide à paraître normale",
            "C'est très difficile pour moi de travailler et d'évoluer dans un groupe",
            "Lorsque je parle à quelqu'un, il m'est difficile de changer de sujet. Si l'autre personne le fait, je peux être bouleversé et confus",
            "Quelquefois je dois couvrir mes oreilles pour arrêter des bruits douloureux",
            "Je peux discuter et avoir des conversations superficielles",
            "Quelquefois des choses qui devraient être douloureuses ne me font pas mal",
            "Quand je parle à quelqu'un, j'ai des difficultés à savoir si c'est à mon tour de parler ou d'écouter",
            "Je suis considéré comme un solitaire par ceux qui me connaissent le mieux",
            "Je parle habituellement avec un ton de voix normal",
            "J'aime que les choses se déroulent toujours de la même manière jour après jour, et même les petits changements dans mes routines me perturbent",
            "Comment se faire des amis et s'intégrer socialement est un mystère pour moi",
            "Cela me calme de tourner en rond ou de me balancer sur une chaise lorsque je me sens stressé",
            "La phrase « il a le coeur sur la main » n'a pas de sens pour moi",
            "Si je suis dans un endroit où il y a beaucoup d'odeurs, de matières à toucher, de bruits ou de lumières intenses, je me sens anxieux ou effrayé",
            "Je sais faire la différence lorsque quelqu'un dit une chose mais veut en dire une autre",
            "J'aime être seul autant que possible",
            "Je garde mes pensées empilées dans ma mémoire comme dans un classeur, et je prends celles dont j'ai besoin en sélectionnant dans la pile",
            "Le même son peut paraître quelquefois très loud ou très doux alors que je sais qu'il n'a pas changé",
            "J'aime passer du temps à manger et parler avec ma famille et mes amis",
            "Je ne supporte pas les choses que je n'aime pas (comme des odeurs, des matières, des sons ou des couleurs)",
            "Je n'aime pas être tenu ou étreint",
            "Lorsque je vais quelque part, je dois suivre un parcours familier sinon je peux devenir très confus et perturbé",
            "C'est difficile de comprendre ce que les autres personnes attendent de moi",
            "J'aime avoir des amis proches",
            "On me dit que je donne trop de détails",
            "On me dit souvent que je pose des questions embarrassantes",
            "J'ai tendance à souligner les erreurs des autres"
        ]
        
        questions = []
        for i in range(1, 81):
            questions.append({
                "id": f"RAADS{i:02d}",
                "number": i,
                "text": items_text[i-1],
                "subscale": subscale_map[i],
                "options": options,
                "reverse_scored": i in self.reverse_items
            })
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """Calculate RAADS-R total and subscale scores."""
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")

        total_score = 0
        item_scores = {}
        subscale_scores = {
            "social": 0,
            "circumscribed": 0,
            "language": 0,
            "sensory": 0
        }
        
        for question in self.questions:
            q_id = question["id"]
            if q_id not in responses:
                raise ValueError(f"Missing response for question {q_id}")
            
            response_text = responses[q_id]
            if response_text not in question["options"]:
                raise ValueError(f"Invalid response for question {q_id}")
            
            raw_score = question["options"][response_text]
            
            # Apply reverse scoring if needed
            if question["reverse_scored"]:
                score = 3 - raw_score  # Reverse: 0->3, 1->2, 2->1, 3->0
            else:
                score = raw_score
            
            item_scores[q_id] = score
            total_score += score
            subscale_scores[question["subscale"]] += score

        interpretation = self._interpret_score(total_score)
        autism_suggested = total_score >= 65

        return {
            "total_score": total_score,
            "max_score": 240,
            "interpretation": interpretation,
            "autism_suggested": autism_suggested,
            "subscale_scores": subscale_scores,
            "subscale_interpretations": {
                "social": f"{subscale_scores['social']}/117 - Social Relatedness",
                "circumscribed": f"{subscale_scores['circumscribed']}/42 - Circumscribed Interests",
                "language": f"{subscale_scores['language']}/21 - Language",
                "sensory": f"{subscale_scores['sensory']}/60 - Sensory Motor"
            },
            "item_scores": item_scores
        }

    def _interpret_score(self, score: int) -> str:
        """Interpret RAADS-R total score."""
        if score >= 65:
            return "Score suggestif d'un trouble du spectre autistique"
        else:
            return "Score en dessous du seuil clinique"

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "Ce questionnaire évalue les traits autistiques chez l'adulte.\n"
            "Pour chaque affirmation, indiquez si elle était vraie:\n"
            "- Maintenant et pendant votre enfance (avant 16 ans)\n"
            "- Seulement maintenant\n"
            "- Seulement pendant votre enfance\n"
            "- Jamais vraie"
        )


if __name__ == '__main__':
    raads = RAADSQuestionnaire()
    print(f"Questionnaire: {raads.name}")
    print(f"Number of items: {raads.num_items}")
    print(f"Reverse-scored items: {len(raads.reverse_items)}")
    print()
    
    # Test: High autism score
    test_responses = {}
    for i in range(1, 81):
        q_id = f"RAADS{i:02d}"
        # Give autism-indicative responses (considering reverse scoring)
        if i in raads.reverse_items:
            test_responses[q_id] = "Jamais vrai"  # Reverse items: no empathy = 3 points
        else:
            test_responses[q_id] = "Vrai maintenant et quand j'avais moins de 16 ans"  # Regular: persistent trait = 3 points
    
    result = raads.calculate_score(test_responses)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Autism Suggested: {result['autism_suggested']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    print("Subscale Scores:")
    for subscale, interp in result['subscale_interpretations'].items():
        print(f"  {subscale}: {interp}")
    print()
    print("✓ RAADS-R implementation complete - 80 items, 4 subscales, adult autism screening")

