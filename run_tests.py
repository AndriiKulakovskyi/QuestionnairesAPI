#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test runner script for Questionnaires API
Provides convenient commands for running different test suites
"""

import sys
import subprocess
from pathlib import Path


def run_command(cmd, description):
    """Run a command and print results"""
    print(f"\n{'='*60}")
    print(f"{description}")
    print(f"{'='*60}\n")
    result = subprocess.run(cmd, shell=True)
    return result.returncode


def run_all_tests():
    """Run all tests with coverage"""
    return run_command(
        "pytest tests/ -v --cov=questionnaires --cov-report=term-missing",
        "Running all tests with coverage"
    )


def run_qids_tests():
    """Run only QIDS-SR16 tests"""
    return run_command(
        "pytest tests/test_qids_sr16.py -v",
        "Running QIDS-SR16 tests"
    )


def run_mdq_tests():
    """Run only MDQ tests"""
    return run_command(
        "pytest tests/test_mdq.py -v",
        "Running MDQ tests"
    )


def run_quick_tests():
    """Run tests without coverage (faster)"""
    return run_command(
        "pytest tests/ -v",
        "Running quick tests (no coverage)"
    )


def run_with_output():
    """Run tests with detailed output"""
    return run_command(
        "pytest tests/ -vv -s",
        "Running tests with detailed output"
    )


def generate_coverage_report():
    """Generate HTML coverage report"""
    run_command(
        "pytest tests/ --cov=questionnaires --cov-report=html",
        "Generating coverage report"
    )
    print("\nCoverage report generated at: htmlcov/index.html")
    return 0


def run_specific_test(test_name):
    """Run a specific test by name"""
    return run_command(
        f"pytest tests/ -k '{test_name}' -v",
        f"Running tests matching: {test_name}"
    )


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("""
Questionnaires API Test Runner

Usage: python run_tests.py [command]

Commands:
    all         - Run all tests with coverage (default)
    qids        - Run only QIDS-SR16 tests
    mdq         - Run only MDQ tests
    quick       - Run all tests without coverage (faster)
    verbose     - Run tests with detailed output
    coverage    - Generate HTML coverage report
    test <name> - Run specific test matching name

Examples:
    python run_tests.py all
    python run_tests.py qids
    python run_tests.py test validation
    python run_tests.py coverage
        """)
        return run_all_tests()
    
    command = sys.argv[1].lower()
    
    if command == "all":
        return run_all_tests()
    elif command == "qids":
        return run_qids_tests()
    elif command == "mdq":
        return run_mdq_tests()
    elif command == "quick":
        return run_quick_tests()
    elif command in ["verbose", "v"]:
        return run_with_output()
    elif command == "coverage":
        return generate_coverage_report()
    elif command == "test" and len(sys.argv) > 2:
        return run_specific_test(sys.argv[2])
    else:
        print(f"Unknown command: {command}")
        print("Run without arguments to see usage help")
        return 1


if __name__ == "__main__":
    sys.exit(main())

