"""
ASRS v1.1 (Adult ADHD Self-Report Scale)

This module provides the implementation of the ASRS v1.1 questionnaire,
an 18-item screening tool for adult ADHD developed by the World Health Organization.
"""

from .asrs import ASRS, ASRSError

__all__ = ["ASRS", "ASRSError"]

