"""
MADRS - Montgomery-Åsberg Depression Rating Scale

This module provides the implementation of the MADRS scale,
a gold-standard clinician-rated assessment of depressive symptom severity
with 10 items rated on a 0-6 scale.
"""

from .madrs import MADRS, MADRSError

__all__ = ["MADRS", "MADRSError"]

