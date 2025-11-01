from typing import Any, Dict

try:
    from .madrs import MADRSQuestionnaire
except ImportError:
    # For direct execution
    from madrs import MADRSQuestionnaire

class MADRSN1Questionnaire(MADRSQuestionnaire):
    """MADRS N+1 - Montgomery-Åsberg Depression Rating Scale (Follow-up)
    
    This is identical to the MADRS questionnaire but used for follow-up assessments.
    The "N+1" designation indicates this is a subsequent assessment after baseline (N).
    
    Inherits all functionality from MADRSQuestionnaire:
    - Same 10 items
    - Same scoring (0-6 per item, total 0-60)
    - Same interpretation thresholds
    
    Context:
    - Used to track changes in depressive symptoms over time
    - Allows comparison with baseline MADRS assessment
    - Helpful for monitoring treatment response
    """

    def __init__(self):
        # Call parent constructor to inherit all MADRS functionality
        super().__init__()
        
        # Update name to indicate follow-up version
        self.name = "MADRS N+1 - Montgomery-Åsberg Depression Rating Scale (Follow-up)"
        self.description = (
            "Échelle de dépression de Montgomery-Åsberg (évaluation de suivi). "
            "Identique au MADRS standard, utilisée pour les évaluations de suivi."
        )
        
        # Note: used_in_applications inherited from parent
        # Note: questions inherited from parent


if __name__ == '__main__':
    madrs_n1 = MADRSN1Questionnaire()
    print(f"Questionnaire: {madrs_n1.name}")
    print(f"Description: {madrs_n1.description}")
    print(f"Number of items: {len(madrs_n1.questions)}")
    print(f"Used in applications: {madrs_n1.used_in_applications}")
    print()
    print("="*80)
    print("NOTE: MADRS N+1 is functionally identical to MADRS")
    print("="*80)
    print()
    
    print("First 3 items (inherited from MADRS):")
    for i, q in enumerate(madrs_n1.questions[:3]):
        print(f"\n{q['number']}. {q['text'][:80]}...")
        print(f"   Scoring: 0-6 (even scores with anchor points)")
    print()
    print("="*80)
    
    # Test scoring (inherited functionality)
    print("\nExample: Moderate depression")
    test_responses = {
        "MADRS1": 3,
        "MADRS2": 3,
        "MADRS3": 2,
        "MADRS4": 2,
        "MADRS5": 2,
        "MADRS6": 2,
        "MADRS7": 3,
        "MADRS8": 3,
        "MADRS9": 2,
        "MADRS10": 2
    }
    
    result = madrs_n1.calculate_score(test_responses)
    print(f"Total Score: {result['score']}/60")
    print(f"Interpretation: {result['interpretation']}")
    print()
    
    print("="*80)
    print("✓ MADRS N+1 (Follow-up) implementation complete")
    print("  - Inherits all MADRS functionality")
    print("  - 10 items, clinician-rated, 0-6 per item")
    print("  - Used for tracking changes over time")
    print("  - Enables treatment response monitoring")

