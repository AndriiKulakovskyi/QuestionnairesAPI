# Testing Guide

This document describes the testing infrastructure for the Questionnaires API.

## Test Structure

```
tests/
├── __init__.py
├── conftest.py              # Shared fixtures and configuration
├── test_qids_sr16.py        # QIDS-SR16 tests (70+ test cases)
└── test_mdq.py              # MDQ tests (60+ test cases)
```

## Running Tests

### Prerequisites

Install test dependencies:

```bash
pip install -r requirements.txt
```

Or in a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Using the Test Runner Script

The easiest way to run tests is using the `run_tests.py` script:

```bash
# Run all tests with coverage
python run_tests.py all

# Run only QIDS-SR16 tests
python run_tests.py qids

# Run only MDQ tests
python run_tests.py mdq

# Run tests quickly without coverage
python run_tests.py quick

# Run with detailed output
python run_tests.py verbose

# Generate HTML coverage report
python run_tests.py coverage

# Run specific tests by name
python run_tests.py test validation
python run_tests.py test scoring
```

### Using Pytest Directly

You can also use pytest commands directly:

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_qids_sr16.py

# Run specific test class
pytest tests/test_qids_sr16.py::TestQIDSSR16Scoring

# Run specific test method
pytest tests/test_qids_sr16.py::TestQIDSSR16Scoring::test_score_no_depression

# Run tests matching a keyword
pytest -k "validation"

# Run with coverage
pytest --cov=questionnaires --cov-report=term-missing

# Generate HTML coverage report
pytest --cov=questionnaires --cov-report=html
```

## Test Coverage

### QIDS-SR16 Tests (`test_qids_sr16.py`)

**Test Classes:**

1. **TestQIDSSR16Metadata** (7 tests)
   - Metadata retrieval
   - Section structure
   - Question retrieval (all, by section, by ID)
   - Full questionnaire structure

2. **TestQIDSSR16Validation** (12 tests)
   - Valid answer patterns (zeros, threes, mixed)
   - Missing items detection
   - Invalid value detection (too high, negative, non-integer)
   - Clinical consistency warnings (appetite, weight conflicts)
   - Multiple warnings

3. **TestQIDSSR16Scoring** (17 tests)
   - All severity levels (no, mild, moderate, severe, very severe depression)
   - Domain score calculations (sleep, appetite/weight, psychomotor)
   - Max logic for composite domains
   - Suicidal ideation alerts
   - Boundary conditions (score cutoff edges)
   - Error handling for invalid answers

4. **TestQIDSSR16EdgeCases** (8 tests)
   - Sleep domain edge cases
   - Insomnia vs hypersomnia
   - Weight loss vs gain
   - Retardation vs agitation
   - Suicidal ideation thresholds
   - Scoring consistency

**Total: 44 test cases for QIDS-SR16**

### MDQ Tests (`test_mdq.py`)

**Test Classes:**

1. **TestMDQMetadata** (7 tests)
   - Metadata retrieval
   - Section structure
   - Question retrieval (all, by section, by ID)
   - Q1 texts validation
   - Full questionnaire structure

2. **TestMDQValidation** (13 tests)
   - Valid answer patterns (all no, all yes, mixed)
   - Missing items detection (all, Q2, Q3 specifically)
   - Invalid value detection (Q1, Q2, Q3)
   - Clinical consistency warnings
   - No warnings for consistent data

3. **TestMDQScreening** (15 tests)
   - Negative screening scenarios (no symptoms, insufficient, no concurrence, low impact)
   - Positive screening scenarios (minimum criteria, serious impact, all symptoms)
   - Q1 total calculation
   - Interpretation text generation
   - Error handling

4. **TestMDQBoundaryConditions** (10 tests)
   - Exact symptom count boundaries (6 vs 7)
   - Q3 impact level boundaries (1 vs 2)
   - All three criteria required
   - Impact label verification
   - Screening consistency

5. **TestMDQSpecialCases** (6 tests)
   - Classic manic symptom pattern
   - Irritable manic pattern
   - Subclinical symptoms
   - Non-concurrent episodes
   - Symptoms without impairment

6. **TestMDQIntegration** (2 tests)
   - Complete workflow positive case
   - Complete workflow negative case

**Total: 53 test cases for MDQ**

## Test Fixtures

Shared fixtures in `conftest.py`:

- `qids_instance`: QIDS-SR16 questionnaire instance
- `mdq_instance`: MDQ questionnaire instance
- `qids_valid_answers_no_depression`: Sample QIDS answers (score 0)
- `qids_valid_answers_moderate`: Sample QIDS answers (moderate depression)
- `mdq_valid_answers_negative`: Sample MDQ answers (negative screening)
- `mdq_valid_answers_positive`: Sample MDQ answers (positive screening)

## Coverage Reports

After running tests with coverage, view the HTML report:

```bash
python run_tests.py coverage
# Then open: htmlcov/index.html
```

Expected coverage: >95% for both questionnaire classes

## Test Categories

Tests are organized into categories:

- **Metadata tests**: Verify questionnaire structure and metadata
- **Validation tests**: Test answer validation and error detection
- **Scoring/Screening tests**: Test calculation algorithms
- **Boundary tests**: Test edge cases and cutoff points
- **Edge case tests**: Test special clinical scenarios
- **Integration tests**: Test complete workflows

## Writing New Tests

### Test Naming Convention

```python
def test_<feature>_<scenario>():
    """Test description"""
    # Arrange
    # Act
    # Assert
```

### Example Test

```python
def test_score_moderate_depression(self):
    """Test scoring with moderate depression (score 11-15)"""
    # Arrange
    qids = QIDSSR16()
    answers = {
        "q1": 2, "q2": 1, "q3": 0, "q4": 0,
        # ... more answers
    }
    
    # Act
    result = qids.calculate_score(answers)
    
    # Assert
    assert result.total_score == 14
    assert result.severity == "Dépression modérée"
```

## Continuous Integration

These tests are designed to be run in CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
- name: Run tests
  run: |
    pip install -r requirements.txt
    pytest --cov=questionnaires --cov-report=xml
    
- name: Upload coverage
  uses: codecov/codecov-action@v3
```

## Troubleshooting

### Import Errors

If you get import errors:

```bash
# Make sure you're in the project root
cd /path/to/QuestionnairesAPI

# Install in development mode
pip install -e .
```

### Pydantic Not Found

```bash
pip install pydantic>=2.5.0
```

### Pytest Not Found

```bash
pip install pytest pytest-cov
```

## Performance

Test execution time (approximate):

- QIDS-SR16 tests: ~2 seconds
- MDQ tests: ~1.5 seconds
- **Total: ~3.5 seconds**

## Test Statistics

- **Total test files**: 2
- **Total test classes**: 10
- **Total test cases**: 97+
- **Expected coverage**: >95%
- **Expected execution time**: <5 seconds

## Best Practices

1. **Test Isolation**: Each test should be independent
2. **Clear Assertions**: Use descriptive assertion messages
3. **Fixtures**: Use shared fixtures for common setup
4. **Coverage**: Aim for >95% code coverage
5. **Speed**: Keep tests fast (<5 seconds total)
6. **Documentation**: Write clear test docstrings

## Reporting Issues

If you find a bug or test failure:

1. Run the specific test with verbose output:
   ```bash
   pytest tests/test_qids_sr16.py::TestClass::test_method -vv
   ```

2. Check the error message and traceback

3. Verify your environment:
   ```bash
   pip list | grep -E "pydantic|fastapi|pytest"
   ```

4. Report with:
   - Python version
   - Package versions
   - Complete error traceback
   - Steps to reproduce

