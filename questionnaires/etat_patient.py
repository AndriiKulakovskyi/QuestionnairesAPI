import random
from typing import Any, Dict, List, Optional

class EtatPatientQuestionnaire:
    """État Patient - DSM-IV Symptom Checklist
    
    Clinician-rated assessment of current mood state based on DSM-IV criteria.
    To be completed regardless of the patient's mood state (euthymic, depressive,
    manic, hypomanic, or mixed).
    
    Structure:
    - 9 depressive symptoms (DSM-IV major depressive episode)
    - 8 manic symptoms (DSM-IV manic episode)
    - Yes/No/Don't know response format
    - Some symptoms have qualifiers for direction/type
    
    Scoring:
    - Two separate scores: depressive and manic
    - Each "Yes" = 1 point, "No" = 0 points
    - Depressive score range: 0-9
    - Manic score range: 0-8
    - "Don't know" responses render score invalid
    
    Clinical Use:
    - Rapid DSM-IV symptom screening
    - Monitoring symptom evolution
    - Supporting diagnostic assessment
    """

    def __init__(self):
        self.name = "État Patient - DSM-IV Symptom Checklist"
        self.description = "Inventaire des symptômes DSM-IV pour le dépistage rapide de l'état thymique."
        self.num_depressive_items = 9
        self.num_manic_items = 8
        self.used_in_applications = ['ebipolar']
        self.depressive_symptoms, self.manic_symptoms = self._init_questions()

    def _init_questions(self):
        """Initialize DSM-IV symptom lists."""
        
        # Response options (same for all items)
        options = ["Oui", "Non", "Ne sais pas"]
        
        depressive_symptoms = [
            {
                "id": "EP_humeur",
                "text": "Humeur dépressive la majeure partie de la journée",
                "dsm_criterion": "A1",
                "qualifiers": {
                    "text": "Précisez:",
                    "options": [
                        "Hyper-réactivité émotionnelle",
                        "Hypo-réactivité ou d'anesthésie"
                    ]
                }
            },
            {
                "id": "EP_interet_plaisir",
                "text": "Diminution marquée d'intérêt ou de plaisir dans toutes ou presque les activités habituelles, presque toute la journée",
                "dsm_criterion": "A2",
                "qualifiers": None
            },
            {
                "id": "EP_poids",
                "text": "Perte ou gain de poids significatif, ou, diminution ou augmentation de l'appétit",
                "dsm_criterion": "A3",
                "qualifiers": {
                    "text": "Précisez:",
                    "options": ["Perte", "Gain"]
                }
            },
            {
                "id": "EP_sommeil",
                "text": "Insomnie ou hypersomnie",
                "dsm_criterion": "A4",
                "qualifiers": {
                    "text": "Précisez:",
                    "options": ["Insomnie", "Hypersomnie"]
                }
            },
            {
                "id": "EP_psychomoteur",
                "text": "Agitation ou ralentissement psychomoteur",
                "dsm_criterion": "A5",
                "qualifiers": {
                    "text": "Précisez:",
                    "options": ["Agitation", "Ralentissement"]
                }
            },
            {
                "id": "EP_fatigue",
                "text": "Fatigue ou perte d'énergie",
                "dsm_criterion": "A6",
                "qualifiers": None
            },
            {
                "id": "EP_sentiment",
                "text": "Sentiment d'indignité, d'auto-accusation ou de culpabilité excessive ou inappropriée",
                "dsm_criterion": "A7",
                "qualifiers": None
            },
            {
                "id": "EP_idee",
                "text": "Diminution de l'aptitude à penser ou se concentrer ou indécision chaque jour",
                "dsm_criterion": "A8",
                "qualifiers": {
                    "text": "Précisez:",
                    "options": ["Accélération idéïque", "Ralentissement idéïque"]
                }
            },
            {
                "id": "EP_pensee_mort",
                "text": "Pensées récurrentes de mort, idéation suicidaire récurrente sans plan spécifique, ou tentative de suicide",
                "dsm_criterion": "A9",
                "qualifiers": None
            }
        ]
        
        manic_symptoms = [
            {
                "id": "EP_humeur_elevee",
                "text": "Humeur élevée, expansive",
                "dsm_criterion": "A (elevated mood)",
                "qualifiers": None
            },
            {
                "id": "EP_humeur_irritable",
                "text": "Humeur irritable",
                "dsm_criterion": "A (irritable mood)",
                "qualifiers": None
            },
            {
                "id": "EP_estime",
                "text": "Augmentation de l'estime de soi ou idées de grandeur",
                "dsm_criterion": "B1",
                "qualifiers": None
            },
            {
                "id": "EP_besoin_sommeil",
                "text": "Réduction du besoin de sommeil",
                "dsm_criterion": "B2",
                "qualifiers": None
            },
            {
                "id": "EP_besoin_parole",
                "text": "Plus grande communicabilité que d'habitude ou désir de parler constamment",
                "dsm_criterion": "B3",
                "qualifiers": None
            },
            {
                "id": "EP_fuite_idees",
                "text": "Fuite des idées ou sensation subjective que les pensées défilent",
                "dsm_criterion": "B4",
                "qualifiers": None
            },
            {
                "id": "EP_distractibilite",
                "text": "Distractibilité : l'attention du sujet étant trop facilement attirée par des stimuli extérieurs sans pertinence",
                "dsm_criterion": "B5",
                "qualifiers": None
            },
            {
                "id": "EP_impatience_motrice",
                "text": "Activité dirigée vers un but ou impatience motrice : augmentation de l'activité ou agitation psychomotrice",
                "dsm_criterion": "B6",
                "qualifiers": None
            },
            {
                "id": "EP_implication_excessive",
                "text": "Implication excessive dans des activités qui ont un potentiel élevé de conséquences dommageables quoique non reconnues par le patient",
                "dsm_criterion": "B7",
                "qualifiers": None
            }
        ]
        
        # Add options to all items
        for symptom in depressive_symptoms:
            symptom["options"] = options
        for symptom in manic_symptoms:
            symptom["options"] = options
        
        return depressive_symptoms, manic_symptoms

    def calculate_score(self, responses: Dict[str, str], 
                       qualifiers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Calculate depressive and manic symptom scores.

        Args:
            responses (Dict[str, str]): A dictionary of responses, where the key is the question ID
                                       (e.g., "EP_humeur") and the value is "Oui", "Non", or "Ne sais pas".
            qualifiers (Optional[Dict[str, str]]): Optional qualifiers for symptoms (e.g., direction).

        Returns:
            Dict[str, Any]: A dictionary containing depressive and manic scores with interpretations.
        """
        depressive_score = 0
        manic_score = 0
        depressive_symptoms_present = []
        manic_symptoms_present = []
        errors = []
        
        # Calculate depressive score
        for symptom in self.depressive_symptoms:
            q_id = symptom["id"]
            
            if q_id not in responses:
                errors.append(f"Missing response for {symptom['text'][:50]}...")
                continue
            
            response = responses[q_id]
            
            if response not in symptom["options"]:
                errors.append(f"Invalid response for {q_id}: {response}")
                continue
            
            if response == "Ne sais pas":
                errors.append(f"'Don't know' response for {q_id} - score invalid")
                continue
            
            if response == "Oui":
                depressive_score += 1
                depressive_symptoms_present.append({
                    "criterion": symptom["dsm_criterion"],
                    "text": symptom["text"],
                    "qualifier": qualifiers.get(q_id) if qualifiers else None
                })
        
        # Calculate manic score
        for symptom in self.manic_symptoms:
            q_id = symptom["id"]
            
            if q_id not in responses:
                errors.append(f"Missing response for {symptom['text'][:50]}...")
                continue
            
            response = responses[q_id]
            
            if response not in symptom["options"]:
                errors.append(f"Invalid response for {q_id}: {response}")
                continue
            
            if response == "Ne sais pas":
                errors.append(f"'Don't know' response for {q_id} - score invalid")
                continue
            
            if response == "Oui":
                manic_score += 1
                manic_symptoms_present.append({
                    "criterion": symptom["dsm_criterion"],
                    "text": symptom["text"]
                })
        
        # Interpret scores
        depressive_interp = self._interpret_depressive(depressive_score)
        manic_interp = self._interpret_manic(manic_score)
        
        return {
            "depressive_score": depressive_score,
            "depressive_max": self.num_depressive_items,
            "depressive_interpretation": depressive_interp,
            "depressive_symptoms_present": depressive_symptoms_present,
            "manic_score": manic_score,
            "manic_max": self.num_manic_items,
            "manic_interpretation": manic_interp,
            "manic_symptoms_present": manic_symptoms_present,
            "valid": len(errors) == 0,
            "errors": errors
        }

    def _interpret_depressive(self, score: int) -> str:
        """Interpret depressive symptom score."""
        if score >= 5:
            return "Critère DSM-IV pour épisode dépressif majeur potentiellement rempli (≥5 symptômes)"
        elif score >= 3:
            return "Symptomatologie dépressive modérée (3-4 symptômes)"
        elif score >= 1:
            return "Symptomatologie dépressive légère (1-2 symptômes)"
        else:
            return "Pas de symptômes dépressifs"

    def _interpret_manic(self, score: int) -> str:
        """Interpret manic symptom score."""
        if score >= 3:
            return "Critère DSM-IV pour épisode maniaque potentiellement rempli (≥3 symptômes si humeur élevée, ≥4 si humeur irritable)"
        elif score >= 2:
            return "Symptomatologie maniaque modérée (2 symptômes)"
        elif score >= 1:
            return "Symptomatologie maniaque légère (1 symptôme)"
        else:
            return "Pas de symptômes maniaques"

    def get_random_responses(self) -> Dict[str, str]:
        """Generates random valid responses for testing purposes."""
        responses = {}
        all_symptoms = self.depressive_symptoms + self.manic_symptoms
        for symptom in all_symptoms:
            # Mostly "Non" with some "Oui" to avoid invalid "Ne sais pas"
            responses[symptom["id"]] = random.choice(["Oui", "Non", "Non", "Non"])
        return responses

    def get_instruction(self) -> str:
        """Returns the instruction text for the questionnaire."""
        return (
            "CONSIGNES:\n\n"
            "À remplir quel que soit l'état thymique du patient (normothymique, dépressif, "
            "maniaque, hypomane ou mixte). Cochez les symptômes du DSM-IV actuellement présents.\n\n"
            "Pour chaque symptôme, répondez:\n"
            "- Oui: Le symptôme est présent\n"
            "- Non: Le symptôme n'est pas présent\n"
            "- Ne sais pas: Incertain (rend le score invalide)"
        )


if __name__ == '__main__':
    ep = EtatPatientQuestionnaire()
    print(f"Questionnaire: {ep.name}")
    print(f"Description: {ep.description}")
    print(f"Depressive symptoms: {ep.num_depressive_items}")
    print(f"Manic symptoms: {ep.num_manic_items}")
    print(f"Used in applications: {ep.used_in_applications}")
    print()
    print("="*80)
    print("INSTRUCTION:")
    print(ep.get_instruction())
    print("="*80)
    print()
    
    print("Depressive Symptoms (DSM-IV):")
    for i, symptom in enumerate(ep.depressive_symptoms, 1):
        qualifier_note = f" [+qualifier]" if symptom["qualifiers"] else ""
        print(f"{i}. {symptom['text'][:70]}...{qualifier_note}")
        print(f"   DSM Criterion: {symptom['dsm_criterion']}")
    print()
    
    print("Manic Symptoms (DSM-IV):")
    for i, symptom in enumerate(ep.manic_symptoms, 1):
        print(f"{i}. {symptom['text'][:70]}...")
        print(f"   DSM Criterion: {symptom['dsm_criterion']}")
    print()
    print("="*80)
    
    # Test case 1: Major depressive episode
    print("\nExample 1: Major Depressive Episode")
    depressive_responses = {}
    for symptom in ep.depressive_symptoms[:6]:  # 6 symptoms
        depressive_responses[symptom["id"]] = "Oui"
    for symptom in ep.depressive_symptoms[6:]:
        depressive_responses[symptom["id"]] = "Non"
    for symptom in ep.manic_symptoms:
        depressive_responses[symptom["id"]] = "Non"
    
    result = ep.calculate_score(depressive_responses)
    print(f"Depressive Score: {result['depressive_score']}/{result['depressive_max']}")
    print(f"  {result['depressive_interpretation']}")
    print(f"Manic Score: {result['manic_score']}/{result['manic_max']}")
    print(f"  {result['manic_interpretation']}")
    print()
    
    # Test case 2: Manic episode
    print("Example 2: Manic Episode")
    manic_responses = {}
    for symptom in ep.depressive_symptoms:
        manic_responses[symptom["id"]] = "Non"
    for symptom in ep.manic_symptoms[:4]:  # 4 symptoms
        manic_responses[symptom["id"]] = "Oui"
    for symptom in ep.manic_symptoms[4:]:
        manic_responses[symptom["id"]] = "Non"
    
    result = ep.calculate_score(manic_responses)
    print(f"Depressive Score: {result['depressive_score']}/{result['depressive_max']}")
    print(f"  {result['depressive_interpretation']}")
    print(f"Manic Score: {result['manic_score']}/{result['manic_max']}")
    print(f"  {result['manic_interpretation']}")
    print()
    
    # Test case 3: Euthymic (no symptoms)
    print("Example 3: Euthymic State")
    euthymic_responses = {}
    all_symptoms = ep.depressive_symptoms + ep.manic_symptoms
    for symptom in all_symptoms:
        euthymic_responses[symptom["id"]] = "Non"
    
    result = ep.calculate_score(euthymic_responses)
    print(f"Depressive Score: {result['depressive_score']}/{result['depressive_max']}")
    print(f"  {result['depressive_interpretation']}")
    print(f"Manic Score: {result['manic_score']}/{result['manic_max']}")
    print(f"  {result['manic_interpretation']}")
    print()
    
    print("="*80)
    print("✓ État Patient implementation complete")
    print("  - 9 DSM-IV depressive symptoms")
    print("  - 8 DSM-IV manic symptoms")
    print("  - Yes/No/Don't know format")
    print("  - Rapid symptom screening")
    print("  - Clinician-rated assessment")

