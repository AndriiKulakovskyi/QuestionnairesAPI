import random
from typing import Any, Dict, List

class COMMQuestionnaire:
    """COMM - Communication Assessment Scale for Adults
    
    Self-report questionnaire assessing communication difficulties in adults with autism.
    
    Structure:
    - 48 items assessing multiple communication domains:
      • Pragmatics (social use of language)
      • Phonology (speech sounds/pronunciation)
      • Syntax (grammar/sentence structure)
      • Semantics (word meanings)
      • Nonverbal communication
    
    Scoring:
    - Each item: 0-3 scale based on frequency
      0 = Less than once a week (or never)
      1 = About once a week
      2 = Once or twice a day
      3 = Several times a day (or continuously)
    - Total score: 0-144
    - Higher scores = more communication difficulties
    
    Clinical Use:
    - Autism communication profile
    - Speech-language therapy planning
    - Social communication intervention
    - Treatment monitoring
    """

    def __init__(self):
        self.name = "COMM - Communication Assessment Scale"
        self.description = "Échelle d'évaluation de la communication chez l'adulte autiste."
        self.num_items = 48
        self.used_in_applications = ['asperger']
        self.questions = self._init_questions()

    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all 48 COMM items."""
        
        options = {
            "moins d'une fois par semaine (ou jamais)": 0,
            "à peu près une fois par semaine": 1,
            "une ou deux fois par jour": 2,
            "plusieurs fois par jour (ou continuellement)": 3
        }
        
        # All 48 communication items (abbreviated for efficiency)
        items = [
            ("pragmatic", "Je fais un mélange des pronoms personnels 'il' et 'elle'"),
            ("phonology", "Je simplifie les mots en enlevant des sons"),
            ("pragmatic", "Je me sens anxieux quand je suis avec d'autres personnes"),
            ("pragmatic", "J'ai des difficultés pour commencer mes phrases et pour trouver le bon mot"),
            ("pragmatic", "On me dit que je parle souvent de choses qui n'intéressent personne"),
            ("semantic", "J'oublie des mots que je connais"),
            ("pragmatic", "Les gens me disent que je n'écoute pas ce qu'ils racontent"),
            ("nonverbal", "Les gens me disent que mon visage est inexpressif"),
            ("pragmatic", "Lorsque j'ai du temps libre je choisis toujours la même activité"),
            ("pragmatic", "Les gens trouvent qu'il est difficile de comprendre lorsque je parle"),
            ("pragmatic", "Je répète comme en écho ce que les autres gens disent"),
            ("semantic", "Je confonds des mots de significations proches"),
            ("pragmatic", "Les gens se moquent de moi ou me harcèlent"),
            ("nonverbal", "Je ne regarde pas les gens lorsque je leur parle"),
            ("pragmatic", "Je ne saisis pas les blagues des autres"),
            ("pragmatic", "Les gens ne m'incluent pas dans leurs activités"),
            ("syntax", "Je mélange 'il' et 'lui'"),
            ("pragmatic", "Je commence mes phrases par les mêmes mots"),
            ("semantic", "Je suis désorienté lorsqu'un mot est utilisé avec une signification différente"),
            ("pragmatic", "Je me tiens trop près des autres personnes lorsque je leur parle"),
            ("pragmatic", "J'engage facilement la conversation avec un étranger"),
            ("pragmatic", "J'aime parler de listes de choses que j'ai mémorisées"),
            ("phonology", "Les gens me disent que je parle avec un accent inhabituel"),
            ("phonology", "Les gens me disent que je ne prononce pas les mots correctement"),
            ("pragmatic", "Les gens disent qu'il est difficile de savoir si je parle de quelque chose de réel ou d'imaginaire"),
            ("pragmatic", "Les gens disent que je détourne la conversation vers mon sujet favori"),
            ("syntax", "Je fais des phrases courtes"),
            ("pragmatic", "Je trouve difficile de m'exprimer devant un groupe de gens"),
            ("phonology", "J'omets le début ou la fin des mots"),
            ("pragmatic", "Les gens me disent que je répète ce qu'ils viennent juste de me dire"),
            ("pragmatic", "Les gens me disent que je les ignore lorsqu'ils m'adressent la parole"),
            ("phonology", "Je confonds les mots ayant la même sonorité"),
            ("pragmatic", "Je blesse ou énerve les gens sans m'en rendre compte"),
            ("semantic", "Je comprends mal ce que les gens disent"),
            ("pragmatic", "Les gens disent que je parle trop"),
            ("syntax", "J'omets la fin des mots"),
            ("pragmatic", "Les gens me disent que je leur répète des choses qu'ils savent déjà"),
            ("phonology", "Je fais des erreurs dans la prononciation des mots longs"),
            ("pragmatic", "J'ai du mal à savoir si les gens sont agacés ou fâchés"),
            ("pragmatic", "Je trouve que c'est difficile de parler d'évènements passés"),
            ("pragmatic", "Les gens rient de choses que je dis, alors même que je n'ai pas eu la sensation d'avoir été drôle"),
            ("pragmatic", "Je donne aux gens des informations détaillées alors qu'un commentaire plus général serait mieux"),
            ("syntax", "Les gens me disent que je ne fais pas des phrases correctes"),
            ("phonology", "Je prononce mal les mots"),
            ("pragmatic", "Les gens me disent que je pose sans cesse les mêmes questions"),
            ("semantic", "J'utilise souvent des mots comme 'cela' ou 'cette chose' et les gens ne comprennent pas"),
            ("pragmatic", "Je suis intéressé par des choses que la plupart des gens trouvent inhabituelles"),
            ("pragmatic", "Lorsque je décris quelque chose, les gens me demandent de ré expliquer depuis le début")
        ]
        
        questions = []
        for i, (domain, text) in enumerate(items, start=1):
            questions.append({
                "id": f"COMM{i}",
                "number": i,
                "domain": domain,
                "text": text,
                "options": options
            })
        
        return questions

    def calculate_score(self, responses: Dict[str, str]) -> Dict[str, Any]:
        """Calculate COMM total and domain scores."""
        if len(responses) != self.num_items:
            raise ValueError(f"Expected {self.num_items} responses, but got {len(responses)}")

        total_score = 0
        item_scores = {}
        domain_scores = {
            "pragmatic": 0,
            "phonology": 0,
            "syntax": 0,
            "semantic": 0,
            "nonverbal": 0
        }
        domain_counts = {
            "pragmatic": 0,
            "phonology": 0,
            "syntax": 0,
            "semantic": 0,
            "nonverbal": 0
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
            domain_scores[question["domain"]] += score
            domain_counts[question["domain"]] += 1

        interpretation = self._interpret_score(total_score)

        return {
            "total_score": total_score,
            "max_score": 144,
            "interpretation": interpretation,
            "severity": self._get_severity(total_score),
            "domain_scores": domain_scores,
            "domain_counts": domain_counts,
            "domain_interpretations": {
                "pragmatic": f"{domain_scores['pragmatic']} - Pragmatique/Usage social du langage ({domain_counts['pragmatic']} items)",
                "phonology": f"{domain_scores['phonology']} - Phonologie/Prononciation ({domain_counts['phonology']} items)",
                "syntax": f"{domain_scores['syntax']} - Syntaxe/Grammaire ({domain_counts['syntax']} items)",
                "semantic": f"{domain_scores['semantic']} - Sémantique/Sens des mots ({domain_counts['semantic']} items)",
                "nonverbal": f"{domain_scores['nonverbal']} - Communication non-verbale ({domain_counts['nonverbal']} items)"
            },
            "item_scores": item_scores
        }

    def _interpret_score(self, score: int) -> str:
        """Interpret COMM total score."""
        if score >= 90:
            return "Difficultés de communication très sévères"
        elif score >= 60:
            return "Difficultés de communication sévères"
        elif score >= 30:
            return "Difficultés de communication modérées"
        elif score >= 15:
            return "Difficultés de communication légères"
        else:
            return "Difficultés de communication minimes"

    def _get_severity(self, score: int) -> str:
        """Get severity level."""
        if score >= 90:
            return "very_severe"
        elif score >= 60:
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
            "Ce questionnaire évalue les difficultés de communication dans l'autisme.\n"
            "Pour chaque affirmation, indiquez à quelle fréquence cela vous arrive:\n"
            "- Moins d'une fois par semaine (ou jamais)\n"
            "- À peu près une fois par semaine\n"
            "- Une ou deux fois par jour\n"
            "- Plusieurs fois par jour (ou continuellement)"
        )


if __name__ == '__main__':
    comm = COMMQuestionnaire()
    print(f"Questionnaire: {comm.name}")
    print(f"Number of items: {comm.num_items}")
    print()
    
    # Test: Moderate communication difficulties
    test_responses = {}
    for i in range(1, 49):
        q_id = f"COMM{i}"
        # Alternate between moderate frequencies
        if i % 3 == 0:
            test_responses[q_id] = "une ou deux fois par jour"
        elif i % 3 == 1:
            test_responses[q_id] = "à peu près une fois par semaine"
        else:
            test_responses[q_id] = "moins d'une fois par semaine (ou jamais)"
    
    result = comm.calculate_score(test_responses)
    print(f"Total Score: {result['total_score']}/{result['max_score']}")
    print(f"Severity: {result['severity']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    print("Domain Scores:")
    for domain, interp in result['domain_interpretations'].items():
        print(f"  {domain}: {interp}")
    print()
    print("✓ COMM implementation complete - 48 items, communication assessment in autism")

