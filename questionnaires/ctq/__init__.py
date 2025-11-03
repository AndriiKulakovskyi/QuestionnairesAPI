"""
CTQ (Childhood Trauma Questionnaire)

This module provides the implementation of the CTQ questionnaire,
a 28-item retrospective self-report measure of childhood maltreatment
across five dimensions.
"""

from .ctq import CTQ, CTQError

__all__ = ["CTQ", "CTQError"]

