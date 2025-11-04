"""
CGI (Clinical Global Impressions)

This module provides the implementation of the Clinical Global Impressions scale,
a widely used clinician-rated measure of symptom severity, treatment response,
and therapeutic efficacy in psychiatry.
"""

from .cgi import CGI, CGIError

__all__ = ["CGI", "CGIError"]

