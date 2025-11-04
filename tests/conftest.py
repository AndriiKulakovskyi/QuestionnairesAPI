# -*- coding: utf-8 -*-
"""
Pytest configuration and shared fixtures
"""

import pytest
from questionnaires import QIDSSR16, MDQ, ASRM, Epworth, EQ5D5L, Fagerstrom


@pytest.fixture
def qids_instance():
    """Fixture providing a QIDS-SR16 instance"""
    return QIDSSR16()


@pytest.fixture
def mdq_instance():
    """Fixture providing an MDQ instance"""
    return MDQ()


@pytest.fixture
def qids_valid_answers_no_depression():
    """Fixture providing valid QIDS answers with no depression"""
    return {f"q{i}": 0 for i in range(1, 17)}


@pytest.fixture
def qids_valid_answers_moderate():
    """Fixture providing valid QIDS answers with moderate depression"""
    return {
        "q1": 2, "q2": 1, "q3": 1, "q4": 0,
        "q5": 2, "q6": 0, "q7": 1, "q8": 0,
        "q9": 0, "q10": 2, "q11": 1, "q12": 1,
        "q13": 2, "q14": 2, "q15": 1, "q16": 0
    }


@pytest.fixture
def mdq_valid_answers_negative():
    """Fixture providing valid MDQ answers for negative screening"""
    answers = {f"q1_{i}": 0 for i in range(1, 14)}
    answers.update({"q2": 0, "q3": 0})
    return answers


@pytest.fixture
def mdq_valid_answers_positive():
    """Fixture providing valid MDQ answers for positive screening"""
    answers = {f"q1_{i}": 1 for i in range(1, 11)}  # 10 symptoms
    answers.update({f"q1_{i}": 0 for i in range(11, 14)})
    answers.update({"q2": 1, "q3": 3})
    return answers


@pytest.fixture
def asrm_instance():
    """Fixture providing an ASRM instance"""
    return ASRM()


@pytest.fixture
def asrm_valid_answers_low():
    """Fixture providing valid ASRM answers for low probability"""
    return {f"q{i}": 0 for i in range(1, 6)}


@pytest.fixture
def asrm_valid_answers_high():
    """Fixture providing valid ASRM answers for high probability"""
    return {"q1": 3, "q2": 2, "q3": 2, "q4": 2, "q5": 2}


@pytest.fixture
def epworth_instance():
    """Fixture providing an Epworth instance"""
    return Epworth()


@pytest.fixture
def epworth_valid_answers_normal():
    """Fixture providing valid Epworth answers for normal sleepiness"""
    return {f"q{i}": 0 for i in range(1, 9)}


@pytest.fixture
def epworth_valid_answers_excessive():
    """Fixture providing valid Epworth answers for excessive sleepiness"""
    return {"q1": 3, "q2": 2, "q3": 2, "q4": 2, "q5": 2, "q6": 1, "q7": 2, "q8": 1}


@pytest.fixture
def eq5del_instance():
    """Fixture providing an EQ-5D-5L instance"""
    return EQ5D5L()


@pytest.fixture
def eq5del_valid_answers_perfect():
    """Fixture providing valid EQ-5D-5L answers for perfect health"""
    answers = {f"q{i}": 1 for i in range(1, 6)}
    answers['vas'] = 100
    return answers


@pytest.fixture
def eq5del_valid_answers_moderate():
    """Fixture providing valid EQ-5D-5L answers for moderate problems"""
    return {"q1": 2, "q2": 2, "q3": 3, "q4": 2, "q5": 3, "vas": 60}


@pytest.fixture
def eq5d_instance():
    """Fixture providing an EQ-5D-5L instance"""
    return EQ5D5L()


@pytest.fixture
def eq5d_valid_answers_perfect():
    """Fixture providing valid EQ-5D-5L answers for perfect health"""
    answers = {f"q{i}": 1 for i in range(1, 6)}
    answers['vas'] = 100
    return answers


@pytest.fixture
def eq5d_valid_answers_mixed():
    """Fixture providing valid EQ-5D-5L answers for mixed health state"""
    return {"q1": 2, "q2": 1, "q3": 3, "q4": 2, "q5": 2, "vas": 70}


# Pytest hooks for custom behavior
def pytest_configure(config):
    """Configure pytest with custom markers"""
    config.addinivalue_line(
        "markers", "unit: mark test as a unit test"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers automatically"""
    for item in items:
        # Add unit marker to all tests by default
        if "unit" not in item.keywords and "integration" not in item.keywords:
            item.add_marker(pytest.mark.unit)



@pytest.fixture
def fagerstrom_instance():
    """Fixture providing a Fagerström instance"""
    return Fagerstrom()


@pytest.fixture
def fagerstrom_valid_answers_no_dependence():
    """Fixture providing valid Fagerström answers for no dependence"""
    return {f"q{i}": 0 for i in range(1, 7)}


@pytest.fixture
def fagerstrom_valid_answers_medium():
    """Fixture providing valid Fagerström answers for medium dependence"""
    return {"q1": 2, "q2": 1, "q3": 1, "q4": 1, "q5": 0, "q6": 0}
