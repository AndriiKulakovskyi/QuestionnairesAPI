"""
STAI-YA (Inventaire d'Anxiété État - STAI Forme Y-A)
State-Trait Anxiety Inventory - Form Y-A (State Anxiety)

This module provides the implementation of the STAI-YA questionnaire,
a 20-item self-report measure of state anxiety.
"""

from .stai_ya import STAIYA, STAIYAError

__all__ = ["STAIYA", "STAIYAError"]

