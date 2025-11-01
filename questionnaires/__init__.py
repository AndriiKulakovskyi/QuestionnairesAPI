"""
Questionnaires Module

Clinical questionnaires extracted from eBipolar, eSchizo, Asperger, and CEDR applications.
All questionnaires are in French with accurate scoring algorithms.
"""

from .systematisation_quotient_sq import SystematisationQuotientQuestionnaire
from .madrs import MADRSQuestionnaire
from .qids_sr16 import QIDSSR16Questionnaire
from .ymrs import YMRSQuestionnaire
from .ctq import CTQQuestionnaire
from .psqi import PSQIQuestionnaire
from .mars import MARSQuestionnaire
from .wurs import WURSQuestionnaire
from .cgi_egf import CGIEGFQuestionnaire
from .eq5d import EQ5DQuestionnaire
from .ymrs_n1 import YMRSN1Questionnaire
from .panss import PANSSQuestionnaire
from .mdq import MDQQuestionnaire
from .aq import AQQuestionnaire
from .altman import AltmanQuestionnaire
from .asrs import ASRSQuestionnaire
from .epworth import EpworthQuestionnaire
from .fast import FASTQuestionnaire
from .stai_a import STAIAQuestionnaire
from .alda import AldaScaleQuestionnaire
from .aim import AIMQuestionnaire
from .aq12 import AQ12Questionnaire
from .csm import CSMQuestionnaire
from .mathys import MathysQuestionnaire
from .madrs_n1 import MADRSN1Questionnaire
from .type_circadien import TypeCircadienQuestionnaire
from .prisem import PRISEMQuestionnaire
from .etat_patient import EtatPatientQuestionnaire
from .bdhi import BDHIQuestionnaire
from .als import ALSQuestionnaire
from .shaps import SHAPSQuestionnaire
from .bis11 import BIS11Questionnaire
from .spin import SPINQuestionnaire
from .bfi import BFIQuestionnaire
from .bas import BASQuestionnaire
from .rosenberg import RosenbergQuestionnaire
from .sachs import SachsQuestionnaire
from .ptsd import PTSDQuestionnaire
from .cgi_i import CGIIQuestionnaire
from .leaps import LEAPSQuestionnaire
from .qiap import QIAPQuestionnaire
from .alimentation import AlimentationQuestionnaire
from .egf import EGFQuestionnaire
from .erd import ERDQuestionnaire
from .rbsr import RBSRQuestionnaire
from .raads import RAADSQuestionnaire
from .abc import ABCQuestionnaire
from .eq import EQQuestionnaire
from .comm import COMMQuestionnaire
from .adhd_rs import ADHDRSQuestionnaire
from .brief_a import BRIEFAQuestionnaire
from .thada import THADAQuestionnaire
from .hamilton_anxiety import HamiltonAnxietyQuestionnaire
from .hamilton_depression import HamiltonDepressionQuestionnaire
from .tas20 import TAS20Questionnaire
from .fagerstrom import FagerstromQuestionnaire
from .lsas import LSASQuestionnaire
from .yale_brown import YaleBrownQuestionnaire
from .spq import SPQQuestionnaire
from .asq import ASQQuestionnaire
from .mcdd import MCDDQuestionnaire
from .cshq import CSHQQuestionnaire
from .tci import TCIQuestionnaire
from .tics import TicsQuestionnaire
from .tocs import TOCSQuestionnaire
from .srs import SRSQuestionnaire
from .social_anhedonia import SocialAnhedoniaQuestionnaire
from .cgi_severity import CGISeverityQuestionnaire
from .gipsy import GIPSYQuestionnaire
from .comprep import COMPREPQuestionnaire
from .atac import ATACQuestionnaire

# Neuropsychological Tests
from .wais3 import WAIS3Test
from .wais4 import WAIS4Test
from .raven import RavenProgressiveMatricesTest
from .dunn import DunnSensoryProfileTest
from .npsy import NPSYTest, NPSYComplementaryBattery

__all__ = [
    'SystematisationQuotientQuestionnaire',
    'MADRSQuestionnaire',
    'QIDSSR16Questionnaire',
    'YMRSQuestionnaire',
    'CTQQuestionnaire',
    'PSQIQuestionnaire',
    'MARSQuestionnaire',
    'WURSQuestionnaire',
    'CGIEGFQuestionnaire',
    'EQ5DQuestionnaire',
    'YMRSN1Questionnaire',
    'PANSSQuestionnaire',
    'MDQQuestionnaire',
    'AQQuestionnaire',
    'AltmanQuestionnaire',
    'ASRSQuestionnaire',
    'EpworthQuestionnaire',
    'FASTQuestionnaire',
    'STAIAQuestionnaire',
    'AldaScaleQuestionnaire',
    'AIMQuestionnaire',
    'AQ12Questionnaire',
    'CSMQuestionnaire',
    'MathysQuestionnaire',
    'MADRSN1Questionnaire',
    'TypeCircadienQuestionnaire',
    'PRISEMQuestionnaire',
    'EtatPatientQuestionnaire',
    'BDHIQuestionnaire',
    'ALSQuestionnaire',
    'SHAPSQuestionnaire',
    'BIS11Questionnaire',
    'SPINQuestionnaire',
    'BFIQuestionnaire',
    'BASQuestionnaire',
    'RosenbergQuestionnaire',
    'SachsQuestionnaire',
    'PTSDQuestionnaire',
    'CGIIQuestionnaire',
    'LEAPSQuestionnaire',
    'QIAPQuestionnaire',
    'AlimentationQuestionnaire',
    'EGFQuestionnaire',
    'ERDQuestionnaire',
    'RBSRQuestionnaire',
    'RAADSQuestionnaire',
    'ABCQuestionnaire',
    'EQQuestionnaire',
    'COMMQuestionnaire',
    'ADHDRSQuestionnaire',
    'BRIEFAQuestionnaire',
    'THADAQuestionnaire',
    'HamiltonAnxietyQuestionnaire',
    'HamiltonDepressionQuestionnaire',
    'TAS20Questionnaire',
    'FagerstromQuestionnaire',
    'LSASQuestionnaire',
    'YaleBrownQuestionnaire',
    'SPQQuestionnaire',
    'ASQQuestionnaire',
    'MCDDQuestionnaire',
    'CSHQQuestionnaire',
    'TCIQuestionnaire',
    'TicsQuestionnaire',
    'TOCSQuestionnaire',
    'SRSQuestionnaire',
    'SocialAnhedoniaQuestionnaire',
    'CGISeverityQuestionnaire',
    'GIPSYQuestionnaire',
    'COMPREPQuestionnaire',
    'ATACQuestionnaire',
    # Neuropsych Tests
    'WAIS3Test',
    'WAIS4Test',
    'RavenProgressiveMatricesTest',
    'DunnSensoryProfileTest',
    'NPSYTest',
    'NPSYComplementaryBattery',
]

__version__ = '0.1.0'
__author__ = 'Extracted from EMR codebase'

# Questionnaire registry for easy lookup
QUESTIONNAIRE_REGISTRY = {
    'sq': SystematisationQuotientQuestionnaire,
    'systematisation': SystematisationQuotientQuestionnaire,
    'madrs': MADRSQuestionnaire,
    'montgomery': MADRSQuestionnaire,
    'qids': QIDSSR16Questionnaire,
    'qids-sr16': QIDSSR16Questionnaire,
    'ymrs': YMRSQuestionnaire,
    'young': YMRSQuestionnaire,
    'ctq': CTQQuestionnaire,
    'childhood-trauma': CTQQuestionnaire,
    'psqi': PSQIQuestionnaire,
    'pittsburgh': PSQIQuestionnaire,
    'mars': MARSQuestionnaire,
    'medication-adherence': MARSQuestionnaire,
    'wurs': WURSQuestionnaire,
    'wurs-25': WURSQuestionnaire,
    'wender': WURSQuestionnaire,
    'cgi-egf': CGIEGFQuestionnaire,
    'cgi': CGIEGFQuestionnaire,
    'egf': CGIEGFQuestionnaire,
    'eq5d': EQ5DQuestionnaire,
    'eq-5d': EQ5DQuestionnaire,
    'euroqol': EQ5DQuestionnaire,
    'ymrs-n1': YMRSN1Questionnaire,
    'ymrs-n+1': YMRSN1Questionnaire,
    'ymrs-followup': YMRSN1Questionnaire,
    'panss': PANSSQuestionnaire,
    'positive-negative-syndrome': PANSSQuestionnaire,
    'mdq': MDQQuestionnaire,
    'mood-disorder': MDQQuestionnaire,
    'aq': AQQuestionnaire,
    'autism-quotient': AQQuestionnaire,
    'altman': AltmanQuestionnaire,
    'asrm': AltmanQuestionnaire,
    'altman-mania': AltmanQuestionnaire,
    'asrs': ASRSQuestionnaire,
    'adhd-adult': ASRSQuestionnaire,
    'epworth': EpworthQuestionnaire,
    'ess': EpworthQuestionnaire,
    'sleepiness': EpworthQuestionnaire,
    'fast': FASTQuestionnaire,
    'functioning': FASTQuestionnaire,
    'stai-a': STAIAQuestionnaire,
    'staia': STAIAQuestionnaire,
    'staya': STAIAQuestionnaire,
    'state-anxiety': STAIAQuestionnaire,
    'alda': AldaScaleQuestionnaire,
    'alda-scale': AldaScaleQuestionnaire,
    'lithium-response': AldaScaleQuestionnaire,
    'aim': AIMQuestionnaire,
    'affective-intensity': AIMQuestionnaire,
    'aq12': AQ12Questionnaire,
    'aggression-12': AQ12Questionnaire,
    'csm': CSMQuestionnaire,
    'chronotype': CSMQuestionnaire,
    'morningness': CSMQuestionnaire,
    'mathys': MathysQuestionnaire,
    'mixed-states': MathysQuestionnaire,
    'thymic-states': MathysQuestionnaire,
    'madrs-n1': MADRSN1Questionnaire,
    'madrs-followup': MADRSN1Questionnaire,
    'type-circadien': TypeCircadienQuestionnaire,
    'itc': TypeCircadienQuestionnaire,
    'circadian-type': TypeCircadienQuestionnaire,
    'prisem': PRISEMQuestionnaire,
    'side-effects': PRISEMQuestionnaire,
    'etat-patient': EtatPatientQuestionnaire,
    'dsm-symptoms': EtatPatientQuestionnaire,
    'patient-state': EtatPatientQuestionnaire,
    'bdhi': BDHIQuestionnaire,
    'buss-durkee': BDHIQuestionnaire,
    'hostility': BDHIQuestionnaire,
    'als': ALSQuestionnaire,
    'affective-lability': ALSQuestionnaire,
    'mood-shifts': ALSQuestionnaire,
    'shaps': SHAPSQuestionnaire,
    'anhedonia': SHAPSQuestionnaire,
    'pleasure': SHAPSQuestionnaire,
    'bis-11': BIS11Questionnaire,
    'bis': BIS11Questionnaire,
    'barratt': BIS11Questionnaire,
    'impulsiveness': BIS11Questionnaire,
    'spin': SPINQuestionnaire,
    'social-phobia': SPINQuestionnaire,
    'social-anxiety': SPINQuestionnaire,
    'bfi': BFIQuestionnaire,
    'big-five': BFIQuestionnaire,
    'personality': BFIQuestionnaire,
    'bas': BASQuestionnaire,
    'bech-anxiety': BASQuestionnaire,
    'anxiety-scale': BASQuestionnaire,
    'rosenberg': RosenbergQuestionnaire,
    'self-esteem': RosenbergQuestionnaire,
    'rses': RosenbergQuestionnaire,
    'sachs': SachsQuestionnaire,
    'bipolar-inventory': SachsQuestionnaire,
    'bipolarity': SachsQuestionnaire,
    'ptsd': PTSDQuestionnaire,
    'ptsd-checklist': PTSDQuestionnaire,
    'pcl': PTSDQuestionnaire,
    'cgi-i': CGIIQuestionnaire,
    'cgi-improvement': CGIIQuestionnaire,
    'leaps': LEAPSQuestionnaire,
    'work-productivity': LEAPSQuestionnaire,
    'qiap': QIAPQuestionnaire,
    'ipaq': QIAPQuestionnaire,
    'physical-activity': QIAPQuestionnaire,
    'alimentation': AlimentationQuestionnaire,
    'dietary': AlimentationQuestionnaire,
    'nutrition': AlimentationQuestionnaire,
    'egf': EGFQuestionnaire,
    'global-functioning': EGFQuestionnaire,
    'gaf': EGFQuestionnaire,
    'erd': ERDQuestionnaire,
    'widlocher': ERDQuestionnaire,
    'psychomotor-retardation': ERDQuestionnaire,
    'rbsr': RBSRQuestionnaire,
    'rbs-r': RBSRQuestionnaire,
    'repetitive-behavior': RBSRQuestionnaire,
    'raads': RAADSQuestionnaire,
    'raads-r': RAADSQuestionnaire,
    'ritvo': RAADSQuestionnaire,
    'abc': ABCQuestionnaire,
    'aberrant-behavior': ABCQuestionnaire,
    'eq': EQQuestionnaire,
    'empathy': EQQuestionnaire,
    'empathy-quotient': EQQuestionnaire,
    'comm': COMMQuestionnaire,
    'communication': COMMQuestionnaire,
    'adhd-rs': ADHDRSQuestionnaire,
    'adhdrs': ADHDRSQuestionnaire,
    'brief': BRIEFAQuestionnaire,
    'brief-a': BRIEFAQuestionnaire,
    'thada': THADAQuestionnaire,
    'ham-a': HamiltonAnxietyQuestionnaire,
    'hamilton-anxiety': HamiltonAnxietyQuestionnaire,
    'ham-d': HamiltonDepressionQuestionnaire,
    'hamd': HamiltonDepressionQuestionnaire,
    'hamilton-depression': HamiltonDepressionQuestionnaire,
    'tas': TAS20Questionnaire,
    'tas-20': TAS20Questionnaire,
    'alexithymia': TAS20Questionnaire,
    'fagerstrom': FagerstromQuestionnaire,
    'ftnd': FagerstromQuestionnaire,
    'nicotine': FagerstromQuestionnaire,
    'lsas': LSASQuestionnaire,
    'liebowitz': LSASQuestionnaire,
    'social-anxiety-scale': LSASQuestionnaire,
    'yale-brown': YaleBrownQuestionnaire,
    'ybocs': YaleBrownQuestionnaire,
    'y-bocs': YaleBrownQuestionnaire,
    'ocd': YaleBrownQuestionnaire,
    'spq': SPQQuestionnaire,
    'schizotypal': SPQQuestionnaire,
    'schizotypy': SPQQuestionnaire,
    'asq': ASQQuestionnaire,
    'attachment': ASQQuestionnaire,
    'attachment-style': ASQQuestionnaire,
    'mcdd': MCDDQuestionnaire,
    'multiple-complex-developmental': MCDDQuestionnaire,
    'developmental-disorder': MCDDQuestionnaire,
    'cshq': CSHQQuestionnaire,
    'sleep-habits': CSHQQuestionnaire,
    'children-sleep': CSHQQuestionnaire,
    'tci': TCIQuestionnaire,
    'temperament-character': TCIQuestionnaire,
    'cloninger': TCIQuestionnaire,
    'tics': TicsQuestionnaire,
    'tourette': TicsQuestionnaire,
    'motor-vocal-tics': TicsQuestionnaire,
    'tocs': TOCSQuestionnaire,
    'ocd-symptoms': TOCSQuestionnaire,
    'obsessive-compulsive': TOCSQuestionnaire,
    'bis10': BIS11Questionnaire,  # BIS10 is the same as BIS-11
    'srs': SRSQuestionnaire,
    'social-reciprocity': SRSQuestionnaire,
    'reciprocity': SRSQuestionnaire,
    'social-anhedonia': SocialAnhedoniaQuestionnaire,
    'anhedonie-sociale': SocialAnhedoniaQuestionnaire,
    'cgi-s': CGISeverityQuestionnaire,
    'cgi-severity': CGISeverityQuestionnaire,
    'clinical-severity': CGISeverityQuestionnaire,
    'gipsy': GIPSYQuestionnaire,
    'gi-psy': GIPSYQuestionnaire,
    'gastrointestinal': GIPSYQuestionnaire,
    'comprep': COMPREPQuestionnaire,
    'repetitive-behaviors': COMPREPQuestionnaire,
    'sensory-phenomena': COMPREPQuestionnaire,
    'atac': ATACQuestionnaire,
    'a-tac': ATACQuestionnaire,
    'autism-tics-adhd': ATACQuestionnaire,
    # Neuropsychological Tests
    'wais-3': WAIS3Test,
    'wais-iii': WAIS3Test,
    'wais3': WAIS3Test,
    'wais-4': WAIS4Test,
    'wais-iv': WAIS4Test,
    'wais4': WAIS4Test,
    'raven': RavenProgressiveMatricesTest,
    'raven-pm38': RavenProgressiveMatricesTest,
    'progressive-matrices': RavenProgressiveMatricesTest,
    'dunn': DunnSensoryProfileTest,
    'dunn-sensory': DunnSensoryProfileTest,
    'sensory-profile': DunnSensoryProfileTest,
    'npsy': NPSYTest,
    'neuropsych-eval': NPSYTest,
    'npsy-comp': NPSYComplementaryBattery,
    'npsy-complementary': NPSYComplementaryBattery,
    'executive-battery': NPSYComplementaryBattery,
}

def get_questionnaire(name: str):
    """Get questionnaire class by name (case-insensitive)
    
    Args:
        name: Questionnaire name or alias
        
    Returns:
        Questionnaire class
        
    Example:
        >>> madrs_class = get_questionnaire('madrs')
        >>> questionnaire = madrs_class()
    """
    name_lower = name.lower().replace('_', '-')
    if name_lower in QUESTIONNAIRE_REGISTRY:
        return QUESTIONNAIRE_REGISTRY[name_lower]
    raise KeyError(f"Questionnaire '{name}' not found. Available: {list(QUESTIONNAIRE_REGISTRY.keys())}")


def list_available_questionnaires():
    """List all available questionnaire names
    
    Returns:
        List of questionnaire identifiers
    """
    return sorted(set(QUESTIONNAIRE_REGISTRY.keys()))


# Application mapping - which questionnaires are used in which apps
APPLICATION_QUESTIONNAIRES = {
    'asperger': ['sq', 'aq', 'eq5d', 'rbsr', 'raads', 'abc', 'eq', 'comm', 'adhd-rs', 'brief-a', 'thada', 'ham-a', 'ham-d', 'tas-20', 'fagerstrom', 'lsas', 'yale-brown', 'spq', 'asq', 'mcdd', 'cshq', 'tci', 'tics', 'tocs', 'bis10', 'aim', 'als', 'psqi', 'srs', 'social-anhedonia', 'cgi-s', 'gipsy', 'comprep', 'atac', 'wais-3', 'wais-4', 'raven', 'dunn', 'npsy', 'npsy-comp'],
    'cedr': ['madrs', 'qids', 'ymrs', 'altman', 'epworth', 'fast', 'stai-a', 'shaps', 'bis-11', 'spin', 'bfi', 'bas', 'rosenberg', 'sachs', 'ptsd', 'cgi-i', 'leaps', 'qiap', 'alimentation', 'egf', 'erd'],
    'ebipolar': ['madrs', 'ymrs', 'ymrs-n1', 'ctq', 'psqi', 'mars', 'wurs', 'cgi-egf', 'eq5d', 'mdq', 'altman', 'asrs', 'epworth', 'fast', 'stai-a', 'alda', 'aim', 'aq12', 'csm', 'mathys', 'madrs-n1', 'type-circadien', 'prisem', 'etat-patient', 'bdhi', 'als'],
    'eschizo': ['madrs', 'ymrs', 'ymrs-n1', 'ctq', 'psqi', 'mars', 'wurs', 'cgi-egf', 'eq5d', 'panss', 'altman', 'asrs', 'epworth', 'fast', 'stai-a'],
}


def get_questionnaires_for_app(app_name: str):
    """Get all questionnaires used in a specific application
    
    Args:
        app_name: Application name (asperger, cedr, ebipolar, eschizo)
        
    Returns:
        List of questionnaire classes
    """
    app_lower = app_name.lower()
    if app_lower not in APPLICATION_QUESTIONNAIRES:
        raise KeyError(f"Application '{app_name}' not found. Available: {list(APPLICATION_QUESTIONNAIRES.keys())}")
    
    questionnaire_names = APPLICATION_QUESTIONNAIRES[app_lower]
    return [get_questionnaire(name) for name in questionnaire_names]

