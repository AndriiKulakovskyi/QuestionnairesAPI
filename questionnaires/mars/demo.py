# -*- coding: utf-8 -*-
"""
MARS Questionnaire Demo
Demonstrates the MARS implementation with various test cases
"""

from mars import MARS, MARSError


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def test_case(name, answers, mars):
    """Test a specific case and print results"""
    print(f"\n--- {name} ---")
    print(f"Raw answers: {answers}")
    
    # Validate
    validation = mars.validate_answers(answers)
    print(f"Valid: {validation.valid}")
    if validation.errors:
        print(f"Errors: {validation.errors}")
        return
    if validation.warnings:
        print(f"Warnings: {validation.warnings}")
    
    # Calculate score
    try:
        result = mars.calculate_score(answers)
        print(f"Total score: {result.total_score}/10")
        print(f"Recoded scores: {result.recoded_scores}")
        print(f"Interpretation: {result.interpretation}")
    except MARSError as e:
        print(f"Error calculating score: {e}")


def main():
    """Main demo function"""
    print_section("MARS (Medication Adherence Rating Scale) - Demo")
    
    # Initialize MARS
    mars = MARS()
    
    # Display metadata
    print_section("Metadata")
    metadata = mars.get_metadata()
    print(f"ID: {metadata['id']}")
    print(f"Name: {metadata['name']}")
    print(f"Abbreviation: {metadata['abbreviation']}")
    print(f"Language: {metadata['language']}")
    print(f"Version: {metadata['version']}")
    print(f"Reference Period: {metadata['reference_period']}")
    print(f"Total Questions: {metadata['total_questions']}")
    print(f"Scoring Range: {metadata['scoring_range']}")
    print(f"\nScoring Notes:")
    for note in metadata['scoring_notes']:
        print(f"  - {note}")
    
    # Display questions
    print_section("Questions")
    questions = mars.get_questions()
    for i, q in enumerate(questions, 1):
        print(f"\n{i}. {q['text']}")
        print(f"   Options: {q['options'][0]['label']} ({q['options'][0]['code']}) / "
              f"{q['options'][1]['label']} ({q['options'][1]['code']})")
    
    # Test cases
    print_section("Test Cases")
    
    # Test 1: Perfect adherence (score = 10)
    test_case(
        "Test 1: Perfect Adherence",
        {
            "q1": 0, "q2": 0, "q3": 0, "q4": 0, "q5": 0,
            "q6": 0, "q7": 1, "q8": 1, "q9": 0, "q10": 0
        },
        mars
    )
    
    # Test 2: Poorest adherence (score = 0)
    test_case(
        "Test 2: Poorest Adherence",
        {
            "q1": 1, "q2": 1, "q3": 1, "q4": 1, "q5": 1,
            "q6": 1, "q7": 0, "q8": 0, "q9": 1, "q10": 1
        },
        mars
    )
    
    # Test 3: Moderate adherence (score ≈ 6)
    test_case(
        "Test 3: Moderate Adherence",
        {
            "q1": 0, "q2": 0, "q3": 1, "q4": 0, "q5": 0,
            "q6": 1, "q7": 1, "q8": 1, "q9": 0, "q10": 1
        },
        mars
    )
    
    # Test 4: Good adherence with occasional forgetfulness (score ≈ 8)
    test_case(
        "Test 4: Good Adherence with Occasional Forgetfulness",
        {
            "q1": 1, "q2": 0, "q3": 0, "q4": 0, "q5": 0,
            "q6": 0, "q7": 1, "q8": 1, "q9": 0, "q10": 0
        },
        mars
    )
    
    # Test 5: Poor adherence due to side effects (score ≈ 2)
    test_case(
        "Test 5: Poor Adherence Due to Side Effects",
        {
            "q1": 1, "q2": 1, "q3": 0, "q4": 1, "q5": 0,
            "q6": 0, "q7": 0, "q8": 0, "q9": 1, "q10": 1
        },
        mars
    )
    
    # Test 6: Missing data (validation error)
    test_case(
        "Test 6: Missing Data (Should Fail Validation)",
        {
            "q1": 0, "q2": 1, "q3": 0
        },
        mars
    )
    
    # Test 7: Invalid value (validation error)
    test_case(
        "Test 7: Invalid Value (Should Fail Validation)",
        {
            "q1": 0, "q2": 0, "q3": 0, "q4": 0, "q5": 0,
            "q6": 0, "q7": 2, "q8": 1, "q9": 0, "q10": 0  # q7=2 is invalid
        },
        mars
    )
    
    print_section("Demo Complete")
    print("\nThe MARS questionnaire has been successfully implemented!")
    print("It includes:")
    print("  ✓ 10 binary items (OUI/NON)")
    print("  ✓ Reverse scoring for items 1-6, 9-10 (NO=1)")
    print("  ✓ Positive scoring for items 7-8 (YES=1)")
    print("  ✓ Total score range: 0-10")
    print("  ✓ Clinical interpretation")
    print("  ✓ Validation with warnings for very low/high adherence")
    print()


if __name__ == "__main__":
    main()

