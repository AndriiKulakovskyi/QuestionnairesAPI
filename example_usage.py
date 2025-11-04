#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example usage of QIDS-SR16 and MDQ questionnaire classes
This demonstrates how to use the classes with FastAPI
"""

from questionnaires import QIDSSR16, QIDSError, MDQ, MDQError


def example_qids_sr16():
    """Example usage of QIDS-SR16 questionnaire"""
    print("=" * 60)
    print("QIDS-SR16 Example")
    print("=" * 60)
    
    # Initialize the questionnaire
    qids = QIDSSR16()
    
    # Get metadata
    print("\n1. Metadata:")
    metadata = qids.get_metadata()
    print(f"   Name: {metadata['name']}")
    print(f"   Abbreviation: {metadata['abbreviation']}")
    print(f"   Language: {metadata['language']}")
    print(f"   Total Questions: {metadata['total_questions']}")
    
    # Get sections
    print("\n2. Sections:")
    sections = qids.get_sections()
    for section in sections:
        print(f"   - {section['label']}: {section['description']}")
    
    # Get all questions (for frontend)
    print("\n3. Sample Questions:")
    questions = qids.get_questions()
    print(f"   Total questions: {len(questions)}")
    # Show first question
    q1 = questions[0]
    print(f"\n   Question ID: {q1['id']}")
    print(f"   Text: {q1['text']}")
    print(f"   Options:")
    for opt in q1['options']:
        print(f"      {opt['code']}: {opt['label']}")
    
    # Example: Calculate score with sample answers
    print("\n4. Score Calculation:")
    
    # Example 1: No depression
    answers_no_depression = {f"q{i}": 0 for i in range(1, 17)}
    
    try:
        result = qids.calculate_score(answers_no_depression)
        print(f"\n   Example 1 - No symptoms:")
        print(f"   Total Score: {result.total_score}/27")
        print(f"   Severity: {result.severity}")
        print(f"   Domain Scores: {result.domain_scores}")
    except QIDSError as e:
        print(f"   Error: {e}")
    
    # Example 2: Moderate depression
    answers_moderate = {
        "q1": 2, "q2": 1, "q3": 1, "q4": 0,  # Sleep problems
        "q5": 2,  # Sadness
        "q6": 0, "q7": 1, "q8": 0, "q9": 0,  # Appetite/weight
        "q10": 2,  # Concentration
        "q11": 1,  # Self-view
        "q12": 1,  # Suicidal ideation
        "q13": 2,  # Interest
        "q14": 2,  # Energy
        "q15": 1, "q16": 0   # Psychomotor
    }
    
    try:
        result = qids.calculate_score(answers_moderate)
        print(f"\n   Example 2 - Moderate symptoms:")
        print(f"   Total Score: {result.total_score}/27")
        print(f"   Severity: {result.severity}")
        print(f"   Interpretation: {result.interpretation}")
    except QIDSError as e:
        print(f"   Error: {e}")
    
    # Example 3: Validation error
    print("\n5. Validation:")
    invalid_answers = {"q1": 5, "q2": 0}  # Missing items and invalid value
    validation = qids.validate_answers(invalid_answers)
    print(f"   Valid: {validation.valid}")
    if validation.errors:
        print(f"   Errors: {validation.errors}")
    
    # Get full questionnaire for frontend
    print("\n6. Full Questionnaire Structure (for API):")
    full = qids.get_full_questionnaire()
    print(f"   Keys: {list(full.keys())}")
    print(f"   Ready to be served via FastAPI endpoint")


def example_mdq():
    """Example usage of MDQ questionnaire"""
    print("\n\n" + "=" * 60)
    print("MDQ Example")
    print("=" * 60)
    
    # Initialize the questionnaire
    mdq = MDQ()
    
    # Get metadata
    print("\n1. Metadata:")
    metadata = mdq.get_metadata()
    print(f"   Name: {metadata['name']}")
    print(f"   Abbreviation: {metadata['abbreviation']}")
    print(f"   Language: {metadata['language']}")
    print(f"   Total Questions: {metadata['total_questions']}")
    print(f"   Screening Criteria: {metadata['screening_criteria']}")
    
    # Get sections
    print("\n2. Sections:")
    sections = mdq.get_sections()
    for section in sections:
        print(f"   - {section['label']}: {section['description']}")
    
    # Get all questions (for frontend)
    print("\n3. Sample Questions:")
    questions = mdq.get_questions()
    print(f"   Total questions: {len(questions)}")
    # Show first and last question
    q1 = questions[0]
    print(f"\n   Question ID: {q1['id']}")
    print(f"   Text: {q1['text']}")
    print(f"   Options: {[opt['label'] for opt in q1['options']]}")
    
    # Example: Calculate screening with sample answers
    print("\n4. Screening Calculation:")
    
    # Example 1: Negative screening
    answers_negative = {f"q1_{i}": 0 for i in range(1, 14)}
    answers_negative.update({"q2": 0, "q3": 0})
    
    try:
        result = mdq.calculate_screening(answers_negative)
        print(f"\n   Example 1 - Negative screening:")
        print(f"   Q1 Total: {result.q1_total}/13")
        print(f"   Q2 (Concurrent): {result.q2_concurrent}")
        print(f"   Q3 (Impact): {result.q3_impact_label}")
        print(f"   Result: {result.screening_result}")
    except MDQError as e:
        print(f"   Error: {e}")
    
    # Example 2: Positive screening
    answers_positive = {
        "q1_1": 1, "q1_2": 1, "q1_3": 1, "q1_4": 1,
        "q1_5": 1, "q1_6": 1, "q1_7": 1, "q1_8": 1,
        "q1_9": 0, "q1_10": 0, "q1_11": 0, "q1_12": 0, "q1_13": 0,
        "q2": 1,  # Yes, concurrent
        "q3": 3   # Serious problem
    }
    
    try:
        result = mdq.calculate_screening(answers_positive)
        print(f"\n   Example 2 - Positive screening:")
        print(f"   Q1 Total: {result.q1_total}/13")
        print(f"   Q2 (Concurrent): {result.q2_concurrent}")
        print(f"   Q3 (Impact): {result.q3_impact_label}")
        print(f"   Result: {result.screening_result}")
        print(f"   Interpretation: {result.interpretation}")
    except MDQError as e:
        print(f"   Error: {e}")
    
    # Example 3: Validation
    print("\n5. Validation:")
    invalid_answers = {"q1_1": 2, "q2": 1}  # Missing items and invalid value
    validation = mdq.validate_answers(invalid_answers)
    print(f"   Valid: {validation.valid}")
    if validation.errors:
        print(f"   Errors: {validation.errors}")
    
    # Get full questionnaire for frontend
    print("\n6. Full Questionnaire Structure (for API):")
    full = mdq.get_full_questionnaire()
    print(f"   Keys: {list(full.keys())}")
    print(f"   Ready to be served via FastAPI endpoint")


def example_fastapi_integration():
    """Example of how these classes would be used with FastAPI"""
    print("\n\n" + "=" * 60)
    print("FastAPI Integration Example")
    print("=" * 60)
    
    print("""
# Example FastAPI routes:

from fastapi import FastAPI, HTTPException
from questionnaires import QIDSSR16, QIDSError, MDQ, MDQError

app = FastAPI()

# Initialize questionnaires
qids = QIDSSR16()
mdq = MDQ()

# GET endpoints - Retrieve questionnaire structure
@app.get("/api/questionnaires/qids-sr16")
async def get_qids_questionnaire():
    '''Get complete QIDS-SR16 questionnaire structure for frontend'''
    return qids.get_full_questionnaire()

@app.get("/api/questionnaires/mdq")
async def get_mdq_questionnaire():
    '''Get complete MDQ questionnaire structure for frontend'''
    return mdq.get_full_questionnaire()

# POST endpoints - Submit answers and get scores
@app.post("/api/questionnaires/qids-sr16/score")
async def calculate_qids_score(answers: dict):
    '''Calculate QIDS-SR16 score from submitted answers'''
    try:
        result = qids.calculate_score(answers)
        return result.dict()
    except QIDSError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/questionnaires/mdq/screen")
async def calculate_mdq_screening(answers: dict):
    '''Calculate MDQ screening result from submitted answers'''
    try:
        result = mdq.calculate_screening(answers)
        return result.dict()
    except MDQError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Validation endpoint
@app.post("/api/questionnaires/qids-sr16/validate")
async def validate_qids_answers(answers: dict):
    '''Validate QIDS-SR16 answers without calculating score'''
    validation = qids.validate_answers(answers)
    return validation.dict()

@app.post("/api/questionnaires/mdq/validate")
async def validate_mdq_answers(answers: dict):
    '''Validate MDQ answers without calculating screening'''
    validation = mdq.validate_answers(answers)
    return validation.dict()
    """)


if __name__ == "__main__":
    example_qids_sr16()
    example_mdq()
    example_fastapi_integration()
    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)

