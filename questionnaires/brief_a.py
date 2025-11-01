import random
from typing import Dict, List, Any

class BRIEFAQuestionnaire:
    """
    BRIEF-A (Behavior Rating Inventory of Executive Function - Adult Version)
    
    Description:
    75-item scale assessing executive function in adults across 9 subscales
    grouped into 2 composite indices.
    
    Behavioral Regulation Index (BRI) - 30 items:
    - Inhibit (8 items): impulse control
    - Shift (6 items): cognitive flexibility
    - Emotional Control (10 items): emotional responses
    - Self-Monitor (6 items): social self-awareness
    
    Metacognition Index (MI) - 40 items:
    - Initiate (8 items): task initiation
    - Working Memory (8 items): holding information
    - Plan/Organize (10 items): goal management
    - Task Monitor (6 items): self-monitoring work
    - Organization of Materials (8 items): orderliness
    
    Note: 5 items (10, 27, 38, 48, 59) are validity items and not scored.
    
    Responses: 1=Jamais, 2=Parfois, 3=Souvent
    Scoring: Raw score sums (higher = more executive dysfunction)
    """
    
    def __init__(self):
        self.name = "BRIEF-A"
        self.description = "Behavior Rating Inventory of Executive Function - Adult"
        self.num_items = 75
        self.scored_items = 70  # 5 validity items not scored
        
        # Subscale mappings (0-indexed for Python)
        self.subscales = {
            'Inhibit': [4, 15, 28, 35, 42, 54, 57, 72],
            'Shift': [7, 21, 31, 43, 60, 66],
            'Emotional_Control': [0, 11, 18, 27, 32, 41, 50, 56, 68, 71],
            'Self_Monitor': [12, 22, 36, 49, 63, 69],
            'Initiate': [5, 13, 19, 24, 44, 48, 52, 61],
            'Working_Memory': [3, 10, 16, 25, 34, 45, 55, 67],
            'Plan_Organize': [8, 14, 20, 33, 38, 46, 53, 62, 65, 70],
            'Task_Monitor': [1, 17, 23, 40, 51, 74],
            'Organization_Materials': [2, 6, 29, 30, 39, 59, 64, 73]
        }
        
        # Validity items (0-indexed, not scored)
        self.validity_items = [9, 26, 37, 47, 58]
        
        self.questions = []
        self._init_questions()
    
    def _init_questions(self):
        """Initialize all 75 items."""
        items = [
            "J'ai des accès de colère",  # 1
            "Je fais des erreurs d'inattention lorsque je réalise des tâches",  # 2
            "Je suis désorganisé(e)",  # 3
            "J'ai des difficultés pour me concentrer sur les tâches",  # 4
            "Je tapote avec mes doigts ou remue mes jambes",  # 5
            "J'ai besoin qu'on me rappelle de commencer une tâche",  # 6
            "Mon armoire est totalement en désordre",  # 7
            "J'ai des difficultés pour passer d'une activité à l'autre",  # 8
            "Je suis dépassé(e) quand il y a beaucoup de choses à faire",  # 9
            "J'oublie mon nom",  # 10 [VALIDITY]
            "J'ai des difficultés pour faire un travail nécessitant plusieurs étapes",  # 11
            "J'ai des réactions émotionnelles excessives",  # 12
            "Je m'aperçois trop tard que mon comportement fait de la peine aux autres",  # 13
            "J'ai des difficultés à me préparer pour la journée",  # 14
            "J'ai des difficultés pour organiser mes activités selon leur priorité",  # 15
            "J'ai des difficultés pour rester tranquillement assis(e)",  # 16
            "J'oublie ce que j'étais en train de faire",  # 17
            "Je ne vérifie pas mon travail pour voir s'il y a des erreurs",  # 18
            "Je me laisse envahir par mes émotions pour des raisons anodines",  # 19
            "Je traîne beaucoup à la maison",  # 20
            "Je commence les tâches sans avoir préparé le bon matériel",  # 21
            "J'ai des difficultés à accepter des points de vue différents",  # 22
            "Je parle au mauvais moment",  # 23
            "J'évalue mal le niveau de difficulté des tâches",  # 24
            "J'ai des difficultés à commencer quelque chose par moi-même",  # 25
            "J'ai du mal à rester sur un seul sujet lorsque je parle",  # 26
            "Je me fatigue rapidement",  # 27
            "Je réagis de manière plus émotive que mes amis",  # 28
            "J'ai du mal à attendre mon tour",  # 29
            "Les gens disent que je suis désorganisé(e)",  # 30
            "Je perds mes affaires",  # 31
            "J'ai des difficultés à envisager une nouvelle approche",  # 32
            "J'ai des réactions excessives face à des problèmes peu importants",  # 33
            "Je ne m'y prends pas à l'avance",  # 34
            "J'ai une capacité d'attention limitée",  # 35
            "Je fais des commentaires inappropriés à connotation sexuelle",  # 36
            "Je ne comprends pas quand les autres semblent fâchés avec moi",  # 37
            "J'ai des difficultés pour compter jusqu'à 3",  # 38 [VALIDITY]
            "Je formule des objectifs irréalistes",  # 39
            "Je laisse la salle de bain en désordre",  # 40
            "Je fais des fautes d'inattention",  # 41
            "Je suis facilement affecté(e) par mes émotions",  # 42
            "Je prends des décisions qui me mettent dans une situation difficile",  # 43
            "Je suis gêné(e) quand je dois faire face à des changements",  # 44
            "J'ai des difficultés à m'enthousiasmer pour les choses",  # 45
            "J'oublie facilement les instructions",  # 46
            "J'ai de bonnes idées mais ne peux pas les mettre par écrit",  # 47
            "Je fais des erreurs",  # 48 [VALIDITY]
            "J'ai des difficultés pour me mettre à faire quelque chose",  # 49
            "Je dis les choses sans réfléchir",  # 50
            "Mes accès de colère sont intenses mais se terminent rapidement",  # 51
            "J'ai du mal à terminer ce que je commence",  # 52
            "Je commence les choses à la dernière minute",  # 53
            "J'ai des difficultés à finir de moi-même ce que j'entreprends",  # 54
            "Les gens disent que je suis facilement distrait(e)",  # 55
            "J'ai des difficultés à me souvenir des choses pendant quelques minutes",  # 56
            "Les gens disent que je suis trop émotif(ve)",  # 57
            "Je fais les choses de manière précipitée",  # 58
            "Je m'énerve facilement",  # 59 [VALIDITY]
            "Je laisse la pièce ou mon domicile en désordre",  # 60
            "Je suis perturbé(e) par des changements imprévus",  # 61
            "J'ai du mal à occuper mon temps libre",  # 62
            "Je ne planifie/organise pas mes activités à l'avance",  # 63
            "Les gens disent que je ne réfléchis pas avant d'agir",  # 64
            "J'ai des difficultés à trouver mes affaires",  # 65
            "J'ai des difficultés pour organiser mes activités",  # 66
            "J'ai du mal à surmonter les difficultés/problèmes",  # 67
            "J'ai des difficultés pour faire plus d'une chose à la fois",  # 68
            "Mon humeur change souvent",  # 69
            "Je ne réfléchis pas aux conséquences",  # 70
            "J'ai des difficultés pour l'organisation de mon travail",  # 71
            "Je m'énerve rapidement pour des choses sans importance",  # 72
            "Je suis impulsif(ve)",  # 73
            "Je laisse traîner mes affaires partout",  # 74
            "J'ai du mal à terminer complètement mon travail"  # 75
        ]
        
        response_options = {1: "Jamais", 2: "Parfois", 3: "Souvent"}
        
        for i, text in enumerate(items):
            subscale = self._get_item_subscale(i)
            self.questions.append({
                'id': f'BRIEF{i+1}',
                'text': text,
                'responses': response_options,
                'subscale': subscale,
                'validity_item': i in self.validity_items
            })
    
    def _get_item_subscale(self, item_idx: int) -> str:
        """Get subscale name for item index."""
        for subscale, items in self.subscales.items():
            if item_idx in items:
                return subscale
        return "Validity"
    
    def calculate_score(self, responses: List[int]) -> Dict[str, Any]:
        """Calculate BRIEF-A scores."""
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, got {len(responses)}")
        
        if any(r < 1 or r > 3 for r in responses):
            raise ValueError("All responses must be between 1 and 3")
        
        # Calculate subscale scores
        subscale_scores = {}
        for subscale, items in self.subscales.items():
            subscale_scores[subscale] = sum(responses[i] for i in items)
        
        # Calculate composite indices
        bri_subscales = ['Inhibit', 'Shift', 'Emotional_Control', 'Self_Monitor']
        mi_subscales = ['Initiate', 'Working_Memory', 'Plan_Organize', 'Task_Monitor', 'Organization_Materials']
        
        bri_score = sum(subscale_scores[s] for s in bri_subscales)
        mi_score = sum(subscale_scores[s] for s in mi_subscales)
        gec_score = bri_score + mi_score
        
        return {
            'subscale_scores': subscale_scores,
            'BRI': bri_score,
            'MI': mi_score,
            'GEC': gec_score,
            'interpretation': self._interpret(gec_score),
            'validity_check': self._check_validity(responses)
        }
    
    def _interpret(self, gec_score: int) -> str:
        """Interpret GEC score (clinical cutoffs approximate)."""
        if gec_score < 105:
            return "Minimal executive dysfunction"
        elif gec_score < 140:
            return "Mild executive dysfunction"
        elif gec_score < 175:
            return "Moderate executive dysfunction - clinical concern"
        else:
            return "Severe executive dysfunction"
    
    def _check_validity(self, responses: List[int]) -> Dict[str, Any]:
        """Check validity items for unusual responding."""
        validity_responses = [responses[i] for i in self.validity_items]
        unusual = sum(1 for r in validity_responses if r > 1)
        return {
            'validity_items': validity_responses,
            'unusual_responses': unusual,
            'valid': unusual < 2  # Flag if 2+ validity items endorsed
        }


if __name__ == '__main__':
    brief = BRIEFAQuestionnaire()
    print(f"Questionnaire: {brief.name}")
    print(f"Items: {brief.num_items} ({brief.scored_items} scored)")
    print(f"Subscales: {len(brief.subscales)}\n")
    
    # Example 1: Minimal dysfunction
    print("=" * 70)
    print("Example 1: Minimal Executive Dysfunction")
    responses1 = [1] * 75
    result1 = brief.calculate_score(responses1)
    print(f"GEC: {result1['GEC']} - {result1['interpretation']}")
    print(f"BRI: {result1['BRI']}, MI: {result1['MI']}")
    print(f"Validity: {'Valid' if result1['validity_check']['valid'] else 'Invalid'}")
    
    # Example 2: Moderate dysfunction
    print("\n" + "=" * 70)
    print("Example 2: Moderate Executive Dysfunction")
    responses2 = [2] * 75
    result2 = brief.calculate_score(responses2)
    print(f"GEC: {result2['GEC']} - {result2['interpretation']}")
    print(f"BRI: {result2['BRI']}, MI: {result2['MI']}")
    
    # Example 3: Severe dysfunction
    print("\n" + "=" * 70)
    print("Example 3: Severe Executive Dysfunction")
    responses3 = [3] * 75
    result3 = brief.calculate_score(responses3)
    print(f"GEC: {result3['GEC']} - {result3['interpretation']}")
    print(f"BRI: {result3['BRI']}, MI: {result3['MI']}")
