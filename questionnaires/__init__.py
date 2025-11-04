# Import all auto questionnaires (self-report)
from .auto import (
    QIDSSR16, QIDSError,
    MDQ, MDQError,
    ASRM, ASRMError,
    Epworth, EpworthError,
    EQ5DEL, EQ5DELError,
    Fagerstrom, FagerstromError,
    MARS, MARSError,
    MAThyS, MAThySError,
    PRISEM, PRISEMError,
    PSQI, PSQIError,
    STAIYA, STAIYAError,
    AIMShort, AIMShortError,
    ALSShort, ALSShortError,
    AQ12, AQ12Error,
    ASRS, ASRSError,
    BIS10, BIS10Error,
    CSM, CSMError,
    CTQ, CTQError,
    CTI, CTIError,
    WURS25, WURS25Error
)

# Import hetero questionnaires (clinician-rated/heterogeneous)
from .hetero import (
    ALDA, ALDAError,
    CGI, CGIError
)

__all__ = [
    # Auto questionnaires
    "QIDSSR16", "QIDSError",
    "MDQ", "MDQError",
    "ASRM", "ASRMError",
    "Epworth", "EpworthError",
    "EQ5DEL", "EQ5DELError",
    "Fagerstrom", "FagerstromError",
    "MARS", "MARSError",
    "MAThyS", "MAThySError",
    "PRISEM", "PRISEMError",
    "PSQI", "PSQIError",
    "STAIYA", "STAIYAError",
    "AIMShort", "AIMShortError",
    "ALSShort", "ALSShortError",
    "AQ12", "AQ12Error",
    "ASRS", "ASRSError",
    "BIS10", "BIS10Error",
    "CSM", "CSMError",
    "CTQ", "CTQError",
    "CTI", "CTIError",
    "WURS25", "WURS25Error",
    # Hetero questionnaires
    "ALDA", "ALDAError",
    "CGI", "CGIError"
]

