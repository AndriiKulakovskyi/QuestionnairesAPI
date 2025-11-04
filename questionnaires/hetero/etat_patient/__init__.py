"""
État du patient - DSM-IV Current Symptoms

This module provides the implementation of the Patient State assessment,
a DSM-IV based checklist for current depressive and manic symptoms with
conditional sub-items.
"""

from .etat_patient import EtatPatient, EtatPatientError

__all__ = ["EtatPatient", "EtatPatientError"]

