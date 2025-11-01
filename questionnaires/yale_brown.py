"""
Yale-Brown Obsessive Compulsive Scale (Y-BOCS)
A comprehensive scale for assessing OCD symptoms including a symptom checklist and severity ratings.
"""

class YaleBrownQuestionnaire:
    def __init__(self):
        """Initialize the Yale-Brown OCD questionnaire."""
        self.name = "Yale-Brown"
        self.full_name = "Yale-Brown Obsessive Compulsive Scale (Y-BOCS)"
        self.description = "Échelle d'évaluation des obsessions-compulsions avec liste de symptômes et cotation d'intensité"
        
        # The questionnaire has two parts:
        # Part 1: Symptom Checklist (73 items: Past/Present for obsessions and compulsions)
        # Part 2: Severity Rating (10 items: 5 for obsessions + 5 for compulsions, scale 0-4)
        
        self.checklist_items = 73
        self.severity_items = 10
        self.questions = []
        
        self._init_questions()
    
    def _init_questions(self):
        """Initialize all questions for the Yale-Brown questionnaire."""
        
        # Part 1: Symptom Checklist (items 1-73)
        # Each item has two ratings: Past and Present (Oui/Non/NS)
        
        checklist_categories = [
            {
                "category": "OBSESSIONS À THÈME AGRESSIF",
                "items": [
                    "Peur de faire du mal aux autres",
                    "Peur de se faire du mal",
                    "Images de violence ou d'horreur",
                    "Peur de laisser échapper des obscénités ou des insultes",
                    "Peur de faire quelque chose qui met dans l'embarras",
                    "Peur d'agir sous d'autres impulsions (par exemple, poignarder un ami)",
                    "Peur de voler des choses",
                    "Peur de blesser d'autres personnes par négligence (par exemple, provoquer ou subir un accident de la voie publique)",
                    "Peur que quelque chose de terrible puisse arriver (par exemple, le feu, un cambriolage)",
                    "Autres"
                ]
            },
            {
                "category": "OBSESSIONS DE CONTAMINATION",
                "items": [
                    "Angoisse ou dégoût lié aux déchets ou aux secrétions corporelles (par exemple l'urine, les selles, la salive)",
                    "Angoisses liées à la saleté ou aux microbes",
                    "Angoisse excessive liée aux éléments contaminants dans l'environnement (par exemple l'amiante, les radiations, les déchets toxiques)",
                    "Préoccupation excessive à l'égard des animaux (par exemple, les insectes)",
                    "Préoccupation liée aux substances ou aux résidus collants",
                    "Angoisse à l'idée d'être malade à cause d'un agent contaminant",
                    "Angoisse à l'idée de provoquer une maladie chez les autres (agressivité)",
                    "Préoccupé simplement par le malaise qu'il ressentirait à la suite d'une contamination",
                    "Autres"
                ]
            },
            {
                "category": "OBSESSIONS SEXUELLES",
                "items": [
                    "Impulsions, images ou pensées perverses ou interdites à propos de la sexualité",
                    "Le contenu a trait à des enfants ou à l'inceste",
                    "Le contenu a trait à l'homosexualité",
                    "Comportement sexuel envers les autres (agressivité)",
                    "Autres"
                ]
            },
            {
                "category": "OBSESSIONS DE COLLECTIONS, D'ACCUMULATION",
                "items": [
                    "A distinguer des collections et attrait pour les objets ayant une valeur sentimentale ou monétaire"
                ]
            },
            {
                "category": "OBSESSIONS RELIGIEUSES (scrupulosité)",
                "items": [
                    "Préoccupation liée aux sacrilèges ou aux blasphèmes",
                    "Préoccupation excessive liée au bien/mal, ou à la moralité"
                ]
            },
            {
                "category": "OBSESSIONS DE SYMÉTRIE, D'EXACTITUDE, D'ORDRE",
                "items": [
                    "Accompagnées d'une pensée magique (par exemple, préoccupé à l'idée que sa mère puisse avoir un accident s'il ne fait pas quelque chose de symétrique)",
                    "Non accompagnées d'une pensée magique"
                ]
            },
            {
                "category": "OBSESSIONS DIVERSES",
                "items": [
                    "Besoin de savoir ou de se souvenir",
                    "Peur de dire certaines choses",
                    "Peur de ne pas dire exactement ce qu'il faut",
                    "Images parasites (non violentes)",
                    "Sons, mots, ou musiques parasites et dénués de sens",
                    "Nombres qui portent bonheur ou non",
                    "Attribution de significations spéciales aux couleurs",
                    "Peur de perdre des choses",
                    "Gêné par certains sons / bruits",
                    "Peurs superstitieuses",
                    "Autres"
                ]
            },
            {
                "category": "OBSESSIONS COMPULSIVES SOMATIQUES",
                "items": [
                    "Préoccupation liée aux maladies",
                    "Préoccupation excessive liée à une partie du corps ou son apparence (par exemple, dysmorphophobie)",
                    "Autres"
                ]
            },
            {
                "category": "COMPULSIONS DE LAVAGE/NETTOYAGE",
                "items": [
                    "Lavage des mains ritualisé ou excessif",
                    "Soins corporels ritualisés ou excessifs (douche, bain, brossage des dents...)",
                    "Nettoyage d'objets appartenant à la maison ou d'autres objets inanimés",
                    "Autres mesures pour éviter ou supprimer le contact avec des éléments contaminants",
                    "Autres"
                ]
            },
            {
                "category": "COMPULSIONS AYANT POUR THÈME LE FAIT DE COMPTER",
                "items": [
                    "Compulsions de comptage"
                ]
            },
            {
                "category": "COMPULSIONS DE VÉRIFICATION",
                "items": [
                    "Vérifier les portes, les serrures, la cuisinière, les appareils ménagers, le frein à main dans la voiture, etc.",
                    "Vérifier que rien ne risque de faire du tort aux autres",
                    "Vérifier que rien ne risque de faire du tort à soi même",
                    "Vérifier que rien de catastrophique n'est/ne va arriver",
                    "Vérifier l'absence d'erreur",
                    "Vérification en rapport avec les obsessions somatiques",
                    "Autres vérifications"
                ]
            },
            {
                "category": "RITUELS DE RÉPÉTITION",
                "items": [
                    "Relecture ou réécriture",
                    "Répétition d'activités routinières (par exemple, sortir/entrer – se lever/s'asseoir, etc.…)",
                    "Autres"
                ]
            },
            {
                "category": "COMPULSIONS D'ORDRE/RANGEMENT",
                "items": [
                    "Compulsion d'ordre / de rangement"
                ]
            },
            {
                "category": "COMPULSIONS DE COLLECTION",
                "items": [
                    "A distinguer des collections et de l'intérêt pour les objets de valeur sentimentale ou monétaire (par exemple, lire soigneusement du courrier sans valeur, empiler les vieux journaux, trier les ordures, collectionner les objets inutiles)"
                ]
            },
            {
                "category": "COMPULSIONS DIVERSES",
                "items": [
                    "Rituels mentaux (autres que vérifier ou compter)",
                    "Besoin de dire, de demander, de contester…",
                    "Besoins de toucher, taper ou frotter",
                    "Mesure (non des vérifications) pour s'empêcher de se faire du mal ou de faire du mal aux autres",
                    "Mesures (non des vérifications) pour éviter qu'il y ait des conséquences catastrophiques",
                    "Besoin excessif de faire des listes",
                    "Rituels impliquant un clignement des yeux ou un regard fixe",
                    "Comportements alimentaires ritualisés",
                    "Comportements superstitieux",
                    "Trichotillomanie",
                    "Autres comportements d'auto-agression ou d'automutilation",
                    "Autres"
                ]
            }
        ]
        
        checklist_options = {
            "1": "Oui",
            "0": "Non",
            "9": "Ne sais pas"
        }
        
        # Build checklist questions
        item_num = 1
        for category in checklist_categories:
            for item_text in category["items"]:
                # Past
                self.questions.append({
                    "id": f"YALBPA{item_num}",
                    "text": f"{item_num}. {item_text} - Passé",
                    "category": category["category"],
                    "type": "single_choice",
                    "required": False,
                    "options": checklist_options
                })
                
                # Present
                self.questions.append({
                    "id": f"YALBPR{item_num}",
                    "text": f"{item_num}. {item_text} - Présent",
                    "category": category["category"],
                    "type": "single_choice",
                    "required": False,
                    "options": checklist_options
                })
                
                item_num += 1
        
        # Part 2: Severity Rating Scale (10 items)
        severity_questions = [
            {
                "id": "INTESY1",
                "text": "1. DURÉE DES PENSÉES OBSÉDANTES - Combien de temps durent les pensées obsédantes ?",
                "subscale": "obsessions"
            },
            {
                "id": "INTESY2",
                "text": "2. GÊNE LIÉE AUX PENSÉES OBSÉDANTES - Dans quelle mesure vos pensées obsédantes vous gênent-elles dans votre vie sociale ou professionnelle ?",
                "subscale": "obsessions"
            },
            {
                "id": "INTESY3",
                "text": "3. ANGOISSE ASSOCIÉE AUX PENSÉES OBSÉDANTES - Quel niveau d'angoisse ces pensées obsédantes créent-elles en vous ?",
                "subscale": "obsessions"
            },
            {
                "id": "INTESY4",
                "text": "4. RÉSISTANCE AUX PENSÉES OBSÉDANTES - Quel effort fournissez-vous pour résister aux pensées obsédantes ?",
                "subscale": "obsessions"
            },
            {
                "id": "INTESY5",
                "text": "5. DEGRÉ DE CONTRÔLE SUR LES PENSÉES OBSÉDANTES - Quel contrôle exercez-vous sur vos pensées obsédantes ?",
                "subscale": "obsessions"
            },
            {
                "id": "INTESY6",
                "text": "6. DURÉE DES RITUELS - Combien de temps passez-vous à faire des rituels ?",
                "subscale": "compulsions"
            },
            {
                "id": "INTESY7",
                "text": "7. GÊNE LIÉE AUX RITUELS - Dans quelle mesure les rituels vous gênent-ils dans votre vie sociale ou professionnelle ?",
                "subscale": "compulsions"
            },
            {
                "id": "INTESY8",
                "text": "8. ANGOISSE ASSOCIÉE AUX RITUELS - Comment vous sentiriez-vous si l'on vous empêchait de faire votre (vos) rituel(s) ?",
                "subscale": "compulsions"
            },
            {
                "id": "INTESY9",
                "text": "9. RÉSISTANCE AUX COMPULSIONS - Quel effort fournissez-vous pour résister aux compulsions ?",
                "subscale": "compulsions"
            },
            {
                "id": "INTESY10",
                "text": "10. DEGRÉ DE CONTRÔLE SUR LES RITUELS - Quelle est l'intensité de la pulsion qui vous oblige à ritualiser ?",
                "subscale": "compulsions"
            }
        ]
        
        severity_options = {
            "0": "Nulle",
            "1": "Légère",
            "2": "Moyenne",
            "3": "Importante",
            "4": "Extrêmement importante"
        }
        
        for sq in severity_questions:
            self.questions.append({
                "id": sq["id"],
                "text": sq["text"],
                "subscale": sq["subscale"],
                "type": "single_choice",
                "required": True,
                "options": severity_options
            })
    
    def calculate_score(self, responses):
        """
        Calculate Yale-Brown scores from the severity rating items only.
        The checklist is informational and not scored.
        
        Args:
            responses: Dictionary with question IDs as keys and response values (0-4) as values
            
        Returns:
            Dictionary containing:
                - obsessions_score: Obsessions severity score (0-20)
                - compulsions_score: Compulsions severity score (0-20)
                - total_score: Total Y-BOCS score (0-40)
                - interpretation: Clinical interpretation
        """
        
        # Only the 10 severity items (INTESY1-10) are scored
        obsessions_score = sum(
            responses.get(f"INTESY{i}", 0) for i in range(1, 6)
        )
        
        compulsions_score = sum(
            responses.get(f"INTESY{i}", 0) for i in range(6, 11)
        )
        
        total_score = obsessions_score + compulsions_score
        
        # Interpretation based on total score
        if total_score < 8:
            severity = "Subclinique"
        elif total_score < 16:
            severity = "Léger"
        elif total_score < 24:
            severity = "Modéré"
        elif total_score < 32:
            severity = "Sévère"
        else:
            severity = "Extrême"
        
        return {
            "obsessions_score": obsessions_score,
            "compulsions_score": compulsions_score,
            "total_score": total_score,
            "interpretation": severity
        }


# Example usage and testing
if __name__ == "__main__":
    yb = YaleBrownQuestionnaire()
    
    print(f"Questionnaire: {yb.full_name}")
    print(f"Checklist items: {yb.checklist_items} (each with Past/Present)")
    print(f"Severity rating items: {yb.severity_items}")
    print(f"Total questions: {len(yb.questions)}")
    
    print(f"\nFirst checklist question:")
    print(f"  {yb.questions[0]['id']}: {yb.questions[0]['text']}")
    
    print(f"\nFirst severity question:")
    severity_q = [q for q in yb.questions if 'INTESY' in q['id']][0]
    print(f"  {severity_q['id']}: {severity_q['text'][:80]}...")
    
    # Test scoring with moderate OCD
    test_responses = {
        "INTESY1": 2,  # Moderate duration of obsessions
        "INTESY2": 2,  # Moderate interference from obsessions
        "INTESY3": 2,  # Moderate distress from obsessions
        "INTESY4": 2,  # Moderate resistance to obsessions
        "INTESY5": 2,  # Moderate control over obsessions
        "INTESY6": 2,  # Moderate duration of compulsions
        "INTESY7": 2,  # Moderate interference from compulsions
        "INTESY8": 2,  # Moderate distress from compulsions
        "INTESY9": 2,  # Moderate resistance to compulsions
        "INTESY10": 2  # Moderate control over compulsions
    }
    
    result = yb.calculate_score(test_responses)
    
    print(f"\n--- Test Scoring (moderate severity) ---")
    print(f"Obsessions Score: {result['obsessions_score']}/20")
    print(f"Compulsions Score: {result['compulsions_score']}/20")
    print(f"Total Score: {result['total_score']}/40")
    print(f"Interpretation: {result['interpretation']}")

