"""
EGF (GAF) - Global Assessment of Functioning

This module provides the implementation of the Global Assessment of Functioning scale,
a single-item clinician-rated measure of overall psychological, social, and occupational
functioning on a 0-100 scale.
"""

from .egf import EGF, EGFError

__all__ = ["EGF", "EGFError"]

