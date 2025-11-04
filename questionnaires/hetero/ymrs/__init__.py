"""
YMRS - Young Mania Rating Scale

This module provides the implementation of the YMRS,
a gold-standard clinician-rated assessment of manic symptom severity
with 11 items (7 items rated 0-4, and 4 items rated 0-8).
"""

from .ymrs import YMRS, YMRSError

__all__ = ["YMRS", "YMRSError"]

