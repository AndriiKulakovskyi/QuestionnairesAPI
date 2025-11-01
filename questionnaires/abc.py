import random
from typing import Any, Dict, List

class ABCQuestionnaire:
    """ABC - Aberrant Behavior Checklist
    
    Informant-report questionnaire assessing problem behaviors in autism and developmental disabilities.
    
    Structure:
    - 58 items across 5 subscales:
      I. Irritability/Agitation (15 items)
      II. Lethargy/Social Withdrawal (16 items)
      III. Stereotypic Behavior (7 items)
      IV. Hyperactivity/Noncompliance (16 items)
      V. Inappropriate Speech (4 items)
    
    Scoring:
    - Each item: 0-3 scale
      0 = Not a problem at all
      1 = Slight problem
      2 = Moderate problem
      3 = Severe problem
    - Subscale scores: sum of items within each subscale
    - Total score: 0-174 (sum of all items)
    
    Clinical Use:
    - Treatment monitoring in autism
    - Behavioral intervention planning
    - Medication trials
    - Research on problem behaviors
    """

    def __init__(self):
        self.name = "ABC - Aberrant Behavior Checklist"
        self.description = "Liste des comportements anormaux dans l'autisme et les troubles du développement."
        self.num_items = 58
        self.used_in_applications = ['asperger']
        
        # Subscale item mappings
        self.subscale_items = {
            "irritability": [2, 4, 8, 10, 14, 19, 25, 29, 34, 36, 41, 47, 50, 52, 57],
            "lethargy": [3, 5, 12, 16, 20, 23, 26, 30, 32, 37, 40, 42, 43, 53, 55, 58],
            "stereotypy": [6, 11, 17, 27, 35, 45, 49],
            "hyperactivity": [1, 7, 13, 15, 18, 21, 24, 28, 31, 38, 39, 44, 48, 51, 54, 56],
            "inappropriate_speech": [9, 22, 33, 46]
        }
        
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 58 ABC items."""
        
        options = {
            "Ce n'est pas du tout un problème": 0,
            "C'est un problème peu important": 1,
            "C'est un problème moyennement important": 2,
            "C'est un problème très important": 3
        }
        
        items_text = [
            "Est excessivement actif à la maison, à l'école, au travail ou ailleurs",
            "Fait exprès de se blesser",
            "Manque d'entrain, est mou, inactif",
            "Est agressif envers les autres enfants ou adultes (verbalement ou physiquement)",
            "Cherche à s'isoler des autres",
            "Répète, sans raison, les mêmes mouvements avec son corps",
            "Est turbulent (brutal et bruyant quand la situation ne s'y prête pas)",
            "Crie quand la situation ne s'y prête pas",
            "Parle de manière excessive",
            "A des accès/crises de colère",
            "A un comportement stéréotypé, des mouvements anormaux et répétitifs",
            "Est préoccupé : regarde dans le vide",
            "Est impulsif (agit sans réfléchir)",
            "Est irritable et pleurnicheur",
            "Est agité, incapable de rester en place",
            "Est renfermé : préfère les activités solitaires",
            "A un comportement bizarre, étrange",
            "Est désobéissant, difficile à contrôler",
            "Hurle quand le moment ne s'y prête pas",
            "A une expression figée : manque de réactions émotionnelles",
            "Perturbe les autres",
            "Discours répétitif",
            "Ne fait rien d'autre que de rester assis à regarder les autres",
            "N'est pas coopératif",
            "Est d'humeur dépressive",
            "Résiste à toute forme de contact physique",
            "Balance sa tête d'avant en arrière et de manière répétitive",
            "Ne fait pas attention aux instructions qu'on lui donne",
            "Exige que l'on fasse immédiatement ce qu'il veut",
            "S'isole des autres enfants ou adultes",
            "Perturbe les activités de groupe",
            "Reste longtemps assis ou debout dans la même position",
            "Se parle à voix haute",
            "Pleure pour des petites contrariétés",
            "Fait des mouvements répétitifs avec la tête, le corps ou les mains",
            "A de brusques sautes d'humeur",
            "Reste indifférent aux activités organisées (ne réagit pas)",
            "Ne reste pas tranquillement assis (par exemple durant les cours, les repas, etc.)",
            "N'arrive pas à rester assis longtemps",
            "Il est difficile d'entrer en relation, d'établir un contact ou un dialogue avec lui",
            "Pleure et hurle quand la situation ne s'y prête pas",
            "Préfère être seul",
            "N'essaye pas de communiquer avec des mots ou par des gestes",
            "Se laisse facilement distraire",
            "Remue ou agite les mains ou les pieds de façon répétée",
            "Répète sans cesse le même mot ou la même expression",
            "Tape des pieds, donne des coups dans les objets ou claque les portes",
            "Court ou saute constamment à travers la pièce",
            "Balance le corps d'avant en arrière de façon répétée",
            "Fait exprès de se faire mal",
            "Ne fait pas attention quand on lui parle",
            "S'inflige des violences physiques",
            "Est inactif, ne bouge jamais spontanément",
            "A tendance à être excessivement actif",
            "Réagit de manière négative lorsqu'on lui montre de l'affection",
            "Ignore délibérément les ordres qu'on lui donne",
            "A des accès ou des crises de colère quand il n'obtient pas ce qu'il veut",
            "Se montre indifférent vis-à-vis des autres"
        ]
        
        questions = []
        for i in range(1, 59):
            # Determine subscale
            subscale = None
            for sub_name, items in self.subscale_items.items():
                if i in items:
                    subscale = sub_name
                    break
            
            questions.append({
                "id": f"ABC{i}",
                "number": i,
                "text": items_text[i-1],
                "subscale": subscale,
                "options": options
            })
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """Calculate ABC total and subscale scores."""
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")

        total_score = 0
        item_scores = {}
        subscale_scores = {
            "irritability": 0,
            "lethargy": 0,
            "stereotypy": 0,
            "hyperactivity": 0,
            "inappropriate_speech": 0
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

        return {
            "total_score": total_score,
            "max_score": 174,
            "interpretation": interpretation,
            "subscale_scores": subscale_scores,
            "subscale_interpretations": {
                "irritability": f"{subscale_scores['irritability']}/45 - Irritabilité/Agitation",
                "lethargy": f"{subscale_scores['lethargy']}/48 - Léthargie/Retrait social",
                "stereotypy": f"{subscale_scores['stereotypy']}/21 - Comportements stéréotypés",
                "hyperactivity": f"{subscale_scores['hyperactivity']}/48 - Hyperactivité/Non-compliance",
                "inappropriate_speech": f"{subscale_scores['inappropriate_speech']}/12 - Discours inapproprié"
            },
            "item_scores": item_scores
        }

    def _interpret_score(self, score: int) -> str:
        """Interpret ABC total score."""
        if score >= 100:
            return "Comportements problématiques très sévères"
        elif score >= 60:
            return "Comportements problématiques sévères"
        elif score >= 30:
            return "Comportements problématiques modérés"
        elif score >= 15:
            return "Comportements problématiques légers"
        else:
            return "Comportements problématiques minimes"

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "Ce questionnaire évalue les comportements problématiques chez les personnes "
            "avec autisme ou troubles du développement.\n\n"
            "Pour chaque comportement, indiquez s'il représente:\n"
            "- Pas du tout un problème\n"
            "- Un problème peu important\n"
            "- Un problème moyennement important\n"
            "- Un problème très important"
        )


if __name__ == '__main__':
    abc = ABCQuestionnaire()
    print(f"Questionnaire: {abc.name}")
    print(f"Number of items: {abc.num_items}")
    print()
    
    # Test: Moderate severity across subscales
    test_responses = {}
    for i in range(1, 59):
        q_id = f"ABC{i}"
        # Alternate between slight and moderate problems
        if i % 2 == 0:
            test_responses[q_id] = "C'est un problème moyennement important"
        else:
            test_responses[q_id] = "C'est un problème peu important"
    
    result = abc.calculate_score(test_responses)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    print("Subscale Scores:")
    for subscale, interp in result['subscale_interpretations'].items():
        print(f"  {subscale}: {interp}")
    print()
    print("✓ ABC implementation complete - 58 items, 5 subscales, autism aberrant behaviors")

