import random
from typing import Any, Dict, List

class AlimentationQuestionnaire:
    """Questionnaire Alimentaire - Dietary Habits Assessment
    
    Self-report questionnaire assessing usual dietary intake.
    
    Structure:
    - 23 items covering food consumption frequency/quantity:
      • Daily items (1-8): bread, milk, coffee, cheese, fruits, oil, butter
      • Weekly items (9-21): vegetables, protein sources, wine, yogurt, chocolate
      • Monthly items (22-23): cereals, nuts
    
    Scoring:
    - Descriptive assessment (not scored)
    - Each item quantifies consumption in specific units
    - Provides dietary pattern overview
    
    Clinical Use:
    - Nutritional assessment
    - Dietary counseling
    - Health promotion
    - Metabolic health evaluation
    """

    def __init__(self):
        self.name = "Questionnaire Alimentaire"
        self.description = "Évaluation des habitudes alimentaires."
        self.num_items = 24  # 8 daily + 13 weekly (including 9a/9b) + 2 monthly + 1 monthly nuts
        self.used_in_applications = ['cedr']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 23 dietary items."""
        
        questions = [
            # Daily consumption
            {
                "id": "ALIMENT1",
                "number": 1,
                "text": "Quelles quantité de pain blanc ou baguette consommez-vous par jour ?",
                "frequency": "daily",
                "category": "carbohydrates",
                "options": ["0 gr", "30 gr", "45 gr", "60 gr", "75 gr", "90 gr", "120 gr", "150 gr et plus"],
                "reference": "1 baguette = 250 gr ; 1 ficelle = 120 gr ; 1 pain = 400 gr"
            },
            {
                "id": "ALIMENT2",
                "number": 2,
                "text": "Quelle quantité de pains spéciaux consommez-vous par jour ?",
                "frequency": "daily",
                "category": "carbohydrates",
                "options": ["0 gr", "30 gr", "45 gr", "60 gr", "75 gr", "90 gr", "120 gr", "150 gr et plus"]
            },
            {
                "id": "ALIMENT3",
                "number": 3,
                "text": "Combien de tasses de lait consommez-vous par jour ?",
                "frequency": "daily",
                "category": "dairy",
                "options": ["0", "1/2", "1", "2", "3", "4", "5 et +"],
                "reference": "1 petite tasse = 70 mL ; 1 bol = 4 tasses"
            },
            {
                "id": "ALIMENT4",
                "number": 4,
                "text": "Combien de tasses de café consommez-vous par jour ?",
                "frequency": "daily",
                "category": "beverages",
                "options": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9 et +"]
            },
            {
                "id": "ALIMENT5",
                "number": 5,
                "text": "Combien de portions de fromage consommez-vous par jour ?",
                "frequency": "daily",
                "category": "dairy",
                "options": ["0", "1/4", "1/2", "1", "2", "3", "4", "5 et +"],
                "reference": "1 portion = 30 gr"
            },
            {
                "id": "ALIMENT6",
                "number": 6,
                "text": "Quelle quantité de fruits consommez-vous par jour ?",
                "frequency": "daily",
                "category": "fruits",
                "options": ["0 gr", "50 gr", "100 gr", "150 gr", "200 gr", "250 gr", "300 gr", "350 gr", "400 gr", "500 gr", "600 gr et +"],
                "reference": "1 pomme = 1 poire = 1 banane = 200 gr"
            },
            {
                "id": "ALIMENT7",
                "number": 7,
                "text": "Combien de cuillerées à soupe d'huile consommez-vous par jour ?",
                "frequency": "daily",
                "category": "fats",
                "options": ["0", "1/4", "1/2", "1", "2", "3", "4", "5 et +"],
                "reference": "pour la cuisson, l'assaisonnement"
            },
            {
                "id": "ALIMENT8",
                "number": 8,
                "text": "Combien de portions de beurre consommez-vous par jour ?",
                "frequency": "daily",
                "category": "fats",
                "options": ["0", "1/4", "1/2", "1", "1.5", "2", "3", "4", "5 et +"],
                "reference": "pour vos tartines, la cuisson, après la cuisson… 1 portion individuelle = 10 gr"
            },
            # Weekly consumption
            {
                "id": "ALIMENT9A",
                "number": "9a",
                "text": "Combien de fois consommez-vous de la salade verte par semaine ?",
                "frequency": "weekly",
                "category": "vegetables",
                "options": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9 et +"]
            },
            {
                "id": "ALIMENT9B",
                "number": "9b",
                "text": "Combien de portions à chaque fois ?",
                "frequency": "weekly",
                "category": "vegetables",
                "options": ["0", "1/2", "1", "1.5", "2"],
                "reference": "1 portion = 60 gr"
            },
            {
                "id": "ALIMENT10",
                "number": 10,
                "text": "Combien de portions de haricots verts consommez-vous par semaine ?",
                "frequency": "weekly",
                "category": "vegetables",
                "options": ["0", "1/2", "1", "1.5", "2", "2.5", "3 et +"],
                "reference": "1 portion = 100 gr"
            },
            {
                "id": "ALIMENT11",
                "number": 11,
                "text": "Combien de portions de carottes cuites consommez-vous par semaine ?",
                "frequency": "weekly",
                "category": "vegetables",
                "options": ["0", "1/2", "1", "1.5", "2", "2.5", "3 et +"],
                "reference": "1 portion = 100 gr"
            },
            {
                "id": "ALIMENT12",
                "number": 12,
                "text": "Combien de portions de légumes secs (lentilles, haricots secs,…) consommez-vous par semaine ?",
                "frequency": "weekly",
                "category": "vegetables",
                "options": ["0", "1/2", "1", "1.5", "2", "2.5", "3", "3.5 et +"],
                "reference": "1 portion = 100 gr"
            },
            {
                "id": "ALIMENT13",
                "number": 13,
                "text": "Combien de portions de frites (ou pommes de terre rissolées) consommez-vous par semaine ?",
                "frequency": "weekly",
                "category": "carbohydrates",
                "options": ["0", "1/4", "1/2", "1", "2", "3", "4", "5 et +"],
                "reference": "1 portion = 100 gr"
            },
            {
                "id": "ALIMENT14",
                "number": 14,
                "text": "Combien d'oeufs consommez-vous par semaine ?",
                "frequency": "weekly",
                "category": "protein",
                "options": ["0", "1", "2", "3", "4", "5", "6 et +"]
            },
            {
                "id": "ALIMENT15",
                "number": 15,
                "text": "Quelle quantité de poisson consommez-vous par semaine ?",
                "frequency": "weekly",
                "category": "protein",
                "options": ["0 gr", "50 gr", "100 gr", "150 gr", "200 gr", "300 gr", "400 gr", "500 gr et +"]
            },
            {
                "id": "ALIMENT16",
                "number": 16,
                "text": "Quelle quantité de volaille (poulet, dinde, lapin,…) consommez-vous par semaine ?",
                "frequency": "weekly",
                "category": "protein",
                "options": ["0 gr", "50 gr", "100 gr", "150 gr", "200 gr", "300 gr", "400 gr", "500 gr et +"],
                "reference": "1 cuisse = 100 gr"
            },
            {
                "id": "ALIMENT17",
                "number": 17,
                "text": "Quelle quantité de porc (côtelettes, jambon, saucisses,…) consommez-vous par semaine ?",
                "frequency": "weekly",
                "category": "protein",
                "options": ["0 gr", "50 gr", "100 gr", "150 gr", "200 gr", "300 gr", "400 gr", "500 gr et +"],
                "reference": "1 côtelette = 2 tranches de jambon = 2 saucisses = 100 gr"
            },
            {
                "id": "ALIMENT18",
                "number": 18,
                "text": "Quelle quantité de boeuf consommez-vous par semaine ?",
                "frequency": "weekly",
                "category": "protein",
                "options": ["0 gr", "50 gr", "100 gr", "150 gr", "200 gr", "300 gr", "400 gr", "500 gr et +"],
                "reference": "1 steak moyen = 100 gr"
            },
            {
                "id": "ALIMENT19",
                "number": 19,
                "text": "Quelle quantité de vin consommez-vous par semaine ?",
                "frequency": "weekly",
                "category": "beverages",
                "options": ["0 verre", "1 verre", "2 verres", "3 verres", "1 bouteille", "2 bouteilles", "3 bouteilles", "4 bouteilles et +"]
            },
            {
                "id": "ALIMENT20",
                "number": 20,
                "text": "Combien de yaourts consommez-vous par semaine ?",
                "frequency": "weekly",
                "category": "dairy",
                "options": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11 et +"]
            },
            {
                "id": "ALIMENT21",
                "number": 21,
                "text": "Quelle quantité de chocolat et/ou barres chocolatées consommez-vous par semaine ?",
                "frequency": "weekly",
                "category": "sweets",
                "options": ["0", "2 carrés", "1 barre", "2 barres", "3 barres", "1 tablette", "2 tablettes et +"]
            },
            # Monthly consumption
            {
                "id": "ALIMENT22",
                "number": 22,
                "text": "Combien de paquets de céréales (du petit déjeuner) consommez-vous par mois ?",
                "frequency": "monthly",
                "category": "carbohydrates",
                "options": ["0", "1", "2", "3", "4", "5 et +"],
                "reference": "1 paquet = 350 gr"
            },
            {
                "id": "ALIMENT23",
                "number": 23,
                "text": "Combien de portions de fruits oléagineux (noix, cacahuètes, amandes,…) consommez-vous par mois ?",
                "frequency": "monthly",
                "category": "snacks",
                "options": ["0", "1/2", "1", "2", "3", "4", "5", "6 et +"]
            }
        ]
        
        return questions

    def collect_responses(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        Collect dietary responses (descriptive assessment, no scoring).

        Args:
            responses (Dict[str, str]): A dictionary of responses with item IDs as keys.

        Returns:
            Dict[str, Any]: A dictionary containing categorized dietary data.
        """
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")

        # Categorize responses
        categories = {
            "carbohydrates": {},
            "dairy": {},
            "fruits": {},
            "vegetables": {},
            "protein": {},
            "fats": {},
            "beverages": {},
            "sweets": {},
            "snacks": {}
        }
        
        frequency_groups = {
            "daily": {},
            "weekly": {},
            "monthly": {}
        }
        
        for question in self.questions:
            q_id = question["id"]
            if q_id not in responses:
                raise ValueError(f"Missing response for question {q_id}")
            
            response = responses[q_id]
            category = question.get("category", "other")
            frequency = question.get("frequency", "unknown")
            
            categories[category][q_id] = {
                "question": question["text"],
                "response": response,
                "number": question["number"]
            }
            
            frequency_groups[frequency][q_id] = {
                "question": question["text"],
                "response": response,
                "category": category
            }

        return {
            "by_category": categories,
            "by_frequency": frequency_groups,
            "all_responses": responses,
            "summary": self._generate_summary(responses)
        }

    def _generate_summary(self, responses: Dict[str, str]) -> str:
        """Generate a brief dietary summary."""
        summary_points = []
        
        # Check bread consumption
        bread_total = responses.get("ALIMENT1", "0 gr")
        if "120" in bread_total or "150" in bread_total:
            summary_points.append("Consommation élevée de pain")
        
        # Check coffee
        coffee = responses.get("ALIMENT4", "0")
        if coffee.startswith(("5", "6", "7", "8", "9")):
            summary_points.append("Consommation élevée de café")
        
        # Check fruits
        fruits = responses.get("ALIMENT6", "0 gr")
        if "0 gr" in fruits or "50 gr" in fruits:
            summary_points.append("Consommation faible de fruits")
        elif "400" in fruits or "500" in fruits or "600" in fruits:
            summary_points.append("Consommation élevée de fruits")
        
        # Check protein variety
        fish = responses.get("ALIMENT15", "0 gr")
        poultry = responses.get("ALIMENT16", "0 gr")
        if "0 gr" in fish and "0 gr" in poultry:
            summary_points.append("Consommation limitée de protéines variées")
        
        return "; ".join(summary_points) if summary_points else "Alimentation variée"

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "Merci de cocher la case correspondant à votre alimentation habituelle "
            "(alimentation « en moyenne »).\n\n"
            "Certaines questions concernent votre consommation par jour, d'autres "
            "par semaine, et d'autres par mois."
        )


if __name__ == '__main__':
    alim = AlimentationQuestionnaire()
    print(f"Questionnaire: {alim.name}")
    print(f"Number of items: {alim.num_items}")
    print()
    
    # Test responses (all 23 items)
    test_responses = {
        "ALIMENT1": "60 gr", "ALIMENT2": "0 gr", "ALIMENT3": "1",
        "ALIMENT4": "2", "ALIMENT5": "1", "ALIMENT6": "200 gr",
        "ALIMENT7": "1", "ALIMENT8": "1/2",
        "ALIMENT9A": "3", "ALIMENT9B": "1", "ALIMENT10": "2",
        "ALIMENT11": "1", "ALIMENT12": "1", "ALIMENT13": "1",
        "ALIMENT14": "2", "ALIMENT15": "100 gr", "ALIMENT16": "100 gr",
        "ALIMENT17": "50 gr", "ALIMENT18": "100 gr", "ALIMENT19": "2 verres",
        "ALIMENT20": "3", "ALIMENT21": "1 barre", "ALIMENT22": "1", "ALIMENT23": "1"
    }
    
    result = alim.collect_responses(test_responses)
    print(f"Summary: {result['summary']}")
    print(f"Daily items: {len(result['by_frequency']['daily'])}")
    print(f"Weekly items: {len(result['by_frequency']['weekly'])}")
    print(f"Monthly items: {len(result['by_frequency']['monthly'])}")
    print()
    print("✓ Alimentation implementation complete - 23 items, comprehensive dietary assessment")

