"""
A-TAC - Autism, Tics, ADHD and other Comorbidities
A comprehensive parent interview questionnaire screening for multiple neurodevelopmental conditions.
"""

class ATACQuestionnaire:
    def __init__(self):
        """Initialize the A-TAC questionnaire."""
        self.name = "A-TAC"
        self.full_name = "Autism, Tics, ADHD and other Comorbidities (A-TAC)"
        self.description = "Entretien parental structuré évaluant l'autisme, les tics, le TDAH et autres comorbidités neurodéveloppementales"
        
        # A-TAC has multiple domains (20 domains labeled A-T)
        self.domains = {
            "A": {"name": "Motricité", "num_items": 6},
            "B": {"name": "Perceptions", "num_items": 5},
            "C": {"name": "Attention", "num_items": 15},
            "D": {"name": "Impulsivité et activité", "num_items": 10},
            "E": {"name": "Apprentissage", "num_items": 8},
            "F": {"name": "Facultés de projection et d'organisation", "num_items": 9},
            "G": {"name": "Mémoire", "num_items": 12},
            "H": {"name": "Langage", "num_items": 10},
            "I": {"name": "Imagination", "num_items": 6},
            "J": {"name": "Interaction sociale", "num_items": 10},
            "K": {"name": "Flexibilité comportementale", "num_items": 8},
            "L": {"name": "Tics", "num_items": 10},
            "M": {"name": "Compulsions et routines", "num_items": 8},
            "N": {"name": "Alimentation et sommeil", "num_items": 6},
            "O": {"name": "Humeur", "num_items": 10},
            "P": {"name": "Anxiété", "num_items": 8},
            "Q": {"name": "Conduite", "num_items": 8},
            "R": {"name": "Développement précoce", "num_items": 6},
            "S": {"name": "Santé et famille", "num_items": 8},
            "T": {"name": "Autres symptômes", "num_items": 6}
        }
        
        self.response_options = {
            2: "Oui",
            1: "Oui, à un certain degré",
            0: "Non"
        }
        
        self.total_items = sum(domain["num_items"] for domain in self.domains.values())
        self.questions = []
        self._init_questions()
    
    def _init_questions(self):
        """Initialize A-TAC items (abbreviated structure)."""
        # Due to the large size (150+ items), we create a representative structure
        # In full implementation, all questions would be explicitly listed
        
        item_number = 1
        for domain_code, domain_info in self.domains.items():
            for i in range(domain_info["num_items"]):
                self.questions.append({
                    "id": f"ATAC{item_number}",
                    "domain": domain_code,
                    "domain_name": domain_info["name"],
                    "text": f"{domain_info['name']} - Item {i+1}",  # Abbreviated
                    "responses": self.response_options
                })
                item_number += 1
    
    def calculate_score(self, responses: dict) -> dict:
        """
        Calculate A-TAC scores.
        
        Args:
            responses: Dictionary mapping question IDs to response values (0, 1, or 2)
        
        Returns:
            Dictionary containing:
            - domain_scores: Dictionary with scores for each domain
            - screening_results: Screening results for specific conditions
            - total_score: Total score across all domains
            - interpretation: Clinical interpretation
        """
        if not responses:
            return {
                "domain_scores": {},
                "screening_results": {},
                "total_score": 0,
                "interpretation": "No responses provided"
            }
        
        # Calculate domain scores
        domain_scores = {}
        for domain_code, domain_info in self.domains.items():
            domain_items = [q for q in self.questions if q["domain"] == domain_code]
            domain_score = sum(responses.get(q["id"], 0) for q in domain_items)
            domain_max = domain_info["num_items"] * 2  # Max score if all items = 2
            domain_scores[domain_info["name"]] = {
                "raw_score": domain_score,
                "max_score": domain_max,
                "percentage": round((domain_score / domain_max) * 100, 1) if domain_max > 0 else 0
            }
        
        # Screen for specific conditions based on A-TAC algorithm
        screening_results = {}
        
        # ADHD screening (based on domains C + D)
        adhd_items = [q for q in self.questions if q["domain"] in ["C", "D"]]
        adhd_score = sum(responses.get(q["id"], 0) for q in adhd_items)
        adhd_threshold = 30  # Simplified threshold
        screening_results["ADHD"] = {
            "score": adhd_score,
            "screen_positive": adhd_score >= adhd_threshold
        }
        
        # Autism screening (based on domains H, I, J, K)
        autism_items = [q for q in self.questions if q["domain"] in ["H", "I", "J", "K"]]
        autism_score = sum(responses.get(q["id"], 0) for q in autism_items)
        autism_threshold = 35  # Simplified threshold
        screening_results["Autism"] = {
            "score": autism_score,
            "screen_positive": autism_score >= autism_threshold
        }
        
        # Tic disorders screening (domain L)
        tic_items = [q for q in self.questions if q["domain"] == "L"]
        tic_score = sum(responses.get(q["id"], 0) for q in tic_items)
        tic_threshold = 10  # Simplified threshold
        screening_results["Tics"] = {
            "score": tic_score,
            "screen_positive": tic_score >= tic_threshold
        }
        
        # Learning disorders screening (domain E)
        learning_items = [q for q in self.questions if q["domain"] == "E"]
        learning_score = sum(responses.get(q["id"], 0) for q in learning_items)
        learning_threshold = 8  # Simplified threshold
        screening_results["Learning_Disorders"] = {
            "score": learning_score,
            "screen_positive": learning_score >= learning_threshold
        }
        
        # Total score
        total_score = sum(responses.get(q["id"], 0) for q in self.questions)
        total_max = len(self.questions) * 2
        
        # Interpret results
        positive_screens = [condition for condition, result in screening_results.items() 
                           if result["screen_positive"]]
        
        if len(positive_screens) >= 3:
            interpretation = f"Dépistage positif pour plusieurs conditions: {', '.join(positive_screens)}"
        elif len(positive_screens) == 2:
            interpretation = f"Dépistage positif pour: {', '.join(positive_screens)}"
        elif len(positive_screens) == 1:
            interpretation = f"Dépistage positif pour: {positive_screens[0]}"
        else:
            interpretation = "Pas de dépistage positif pour les conditions principales"
        
        return {
            "domain_scores": domain_scores,
            "screening_results": screening_results,
            "total_score": total_score,
            "total_percentage": round((total_score / total_max) * 100, 1),
            "interpretation": interpretation
        }


if __name__ == '__main__':
    # Example usage
    atac = ATACQuestionnaire()
    
    print(f"Questionnaire: {atac.full_name}")
    print(f"Total items: {atac.total_items}")
    print(f"Number of domains: {len(atac.domains)}\n")
    
    # Example 1: Positive screening for ADHD and Autism
    print("Example 1: Child with ADHD and Autism symptoms")
    responses1 = {}
    for q in atac.questions:
        # High scores for ADHD (C, D) and Autism (H, I, J, K) domains
        if q["domain"] in ["C", "D", "H", "I", "J", "K"]:
            responses1[q["id"]] = 2
        else:
            responses1[q["id"]] = 0
    
    result1 = atac.calculate_score(responses1)
    print(f"Total score: {result1['total_score']} ({result1['total_percentage']}%)")
    print("\nScreening results:")
    for condition, result in result1['screening_results'].items():
        status = "POSITIF" if result["screen_positive"] else "négatif"
        print(f"  {condition}: {status} (score: {result['score']})")
    print(f"\nInterprétation: {result1['interpretation']}\n")
    
    # Example 2: Minimal symptoms
    print("Example 2: Child with minimal symptoms")
    responses2 = {q["id"]: 0 for q in atac.questions}
    result2 = atac.calculate_score(responses2)
    print(f"Total score: {result2['total_score']} ({result2['total_percentage']}%)")
    print(f"Interprétation: {result2['interpretation']}\n")
    
    # Example 3: Tic disorder screening
    print("Example 3: Child with tic symptoms")
    responses3 = {}
    for q in atac.questions:
        if q["domain"] == "L":  # Tics domain
            responses3[q["id"]] = 2
        else:
            responses3[q["id"]] = 0
    
    result3 = atac.calculate_score(responses3)
    print(f"Screening results for Tics: {result3['screening_results']['Tics']}")
    print(f"Interprétation: {result3['interpretation']}\n")

