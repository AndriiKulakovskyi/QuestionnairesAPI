"""
TOCS - Troubles Obsessionnels Compulsifs Scale
A comprehensive checklist assessing OCD symptoms and behaviors.
"""

class TOCSQuestionnaire:
    def __init__(self):
        """Initialize the TOCS questionnaire."""
        self.name = "TOCS"
        self.full_name = "Troubles Obsessionnels Compulsifs - OCD Symptoms Checklist"
        self.description = "Questionnaire d'évaluation des symptômes obsessionnels-compulsifs (TOC)"
        self.num_items = 31
        self.questions = []
        
        # Define OCD symptom categories
        self.categories = {
            "washing_cleaning": [1, 2, 3, 4, 5],
            "checking": [6, 7, 8, 9, 10, 11],
            "repeating": [12, 13],
            "slowness": [14],
            "counting": [15],
            "ordering": [16, 17, 18],
            "hoarding": [19],
            "mental_rituals": [20],
            "other_rituals": [21, 22, 23, 24],
            "avoidance": [25, 26],
            "eating_rituals": [27],
            "superstitions": [28, 29],
            "self_harm": [30, 31]
        }
        
        self._init_questions()
    
    def _init_questions(self):
        """Initialize all 31 TOCS items."""
        
        questions_text = [
            "Je me douche, me baigne, me lave les dents de manière excessive ou ritualisée",
            "Je dois suivre un emploi du temps ou une routine stricte",
            "Je dois faire des choses de la même manière à chaque fois",
            "J'ai des compulsions concernant le nettoyage d'objets",
            "Je fais des choses pour prévenir ou supprimer tout contact avec des contaminants",
            "Je vérifie que je ne vais pas blesser les autres",
            "Je vérifie que je ne me blesse pas",
            "Je vérifie que rien de terrible n'est arrivé ou ne va arriver",
            "Je vérifie que je n'ai pas fait d'erreurs",
            "Je vérifie des appareils ménagers, des verrous de porte",
            "Je vérifie des choses liées à mon corps",
            "Je re-lis ou réécris des choses",
            "Je dois répéter des activités de routine",
            "Quelquefois mes actions deviennent exceptionnellement lentes",
            "J'ai des compulsions de comptage",
            "J'ai des compulsions d'ordre ou de rangements",
            "J'ai besoin que certaines choses soient symétriques",
            "J'ai besoin d'égaliser certaines choses",
            "J'ai des compulsions d'amasser ou de collecter des choses",
            "J'ai des rituels mentaux",
            "J'ai des rituels impliquant le fait de cligner ou de regarder fixement",
            "J'ai un besoin de dire, de demander ou de confesser des choses",
            "J'ai un grand besoin d'explorer mon environnement",
            "J'ai besoin de toucher, taper ou frotter les choses",
            "Je prends des mesures pour éviter que moi-même ou les autres se fassent du mal",
            "Je vais vers des extrêmes pour éviter certaines situations",
            "J'ai des conduites alimentaires ritualisées",
            "J'ai des comportements superstitieux",
            "J'ai des pensées sottes sur l'influence de certains événements",
            "J'ai fait des choses choquantes",
            "Autres compulsions"
        ]
        
        response_options = ["Jamais", "Déjà", "ACTUELLEMENT (pendant la semaine dernière)"]
        
        for idx, text in enumerate(questions_text, 1):
            self.questions.append({
                "id": f"TOC{idx}",
                "text": text,
                "responses": response_options,
                "scoring": {"Jamais": 1, "Déjà": 2, "ACTUELLEMENT (pendant la semaine dernière)": 3}
            })
    
    def calculate_score(self, responses: dict) -> dict:
        """
        Calculate TOCS assessment summary.
        
        Args:
            responses: Dictionary mapping question IDs to response values (1-3)
                      (e.g., {"TOC1": 3, "TOC2": 1, ...})
        
        Returns:
            Dictionary containing:
            - category_counts: Number of current symptoms per category
            - current_symptoms: List of current symptoms
            - past_symptoms: List of past symptoms
            - total_current: Total number of current symptoms
            - interpretation: Clinical interpretation
        """
        if not responses:
            return {
                "category_counts": {},
                "current_symptoms": [],
                "past_symptoms": [],
                "total_current": 0,
                "interpretation": "No responses provided"
            }
        
        category_counts = {name: 0 for name in self.categories.keys()}
        current_symptoms = []
        past_symptoms = []
        
        for q in self.questions:
            q_id = q["id"]
            if q_id in responses:
                value = responses[q_id]
                
                # Find category for this question
                item_num = int(q_id[3:])
                category_name = None
                for cat_name, items in self.categories.items():
                    if item_num in items:
                        category_name = cat_name
                        break
                
                if value == 3:  # Currently present
                    current_symptoms.append(q["text"])
                    if category_name:
                        category_counts[category_name] += 1
                elif value == 2:  # Past but not current
                    past_symptoms.append(q["text"])
        
        total_current = len(current_symptoms)
        
        # Count categories with at least one symptom
        affected_categories = sum(1 for count in category_counts.values() if count > 0)
        
        # Interpret results
        if total_current >= 5:
            if affected_categories >= 3:
                interpretation = f"Symptômes TOC actuels significatifs - {total_current} symptômes dans {affected_categories} catégories - Évaluation clinique recommandée"
            else:
                interpretation = f"Symptômes TOC actuels modérés - {total_current} symptômes présents"
        elif total_current > 0:
            interpretation = f"Quelques symptômes TOC actuels - {total_current} symptômes"
        else:
            interpretation = "Pas de symptômes TOC actuels rapportés"
        
        category_labels = {
            "washing_cleaning": "Lavage/Nettoyage",
            "checking": "Vérifications",
            "repeating": "Répétitions",
            "slowness": "Lenteur",
            "counting": "Comptage",
            "ordering": "Ordre/Symétrie",
            "hoarding": "Accumulation",
            "mental_rituals": "Rituels mentaux",
            "other_rituals": "Autres rituels",
            "avoidance": "Évitement",
            "eating_rituals": "Rituels alimentaires",
            "superstitions": "Superstitions",
            "self_harm": "Auto-agression"
        }
        
        return {
            "category_counts": category_counts,
            "category_labels": category_labels,
            "current_symptoms": current_symptoms,
            "past_symptoms": past_symptoms,
            "total_current": total_current,
            "affected_categories": affected_categories,
            "interpretation": interpretation
        }


if __name__ == '__main__':
    # Example usage
    tocs = TOCSQuestionnaire()
    
    print(f"Questionnaire: {tocs.full_name}")
    print(f"Number of items: {tocs.num_items}\n")
    
    # Example 1: Significant OCD symptoms
    print("Example 1: Significant current OCD symptoms")
    responses1 = {
        "TOC1": 3, "TOC2": 3, "TOC3": 3,  # Washing/cleaning
        "TOC6": 3, "TOC7": 2, "TOC10": 3,  # Checking
        "TOC15": 3,  # Counting
        "TOC16": 3, "TOC17": 3,  # Ordering
        "TOC20": 3,  # Mental rituals
    }
    result1 = tocs.calculate_score(responses1)
    print(f"Total current symptoms: {result1['total_current']}")
    print(f"Affected categories: {result1['affected_categories']}")
    print("Category breakdown:")
    for category, count in result1['category_counts'].items():
        if count > 0:
            label = result1['category_labels'][category]
            print(f"  {label}: {count}")
    print(f"Interpretation: {result1['interpretation']}\n")
    
    # Example 2: Past symptoms only
    print("Example 2: Past OCD symptoms (in remission)")
    responses2 = {f"TOC{i}": 2 for i in range(1, 10)}
    result2 = tocs.calculate_score(responses2)
    print(f"Total current symptoms: {result2['total_current']}")
    print(f"Past symptoms: {len(result2['past_symptoms'])}")
    print(f"Interpretation: {result2['interpretation']}\n")
    
    # Example 3: No symptoms
    print("Example 3: No OCD symptoms")
    responses3 = {f"TOC{i}": 1 for i in range(1, 15)}
    result3 = tocs.calculate_score(responses3)
    print(f"Interpretation: {result3['interpretation']}\n")

