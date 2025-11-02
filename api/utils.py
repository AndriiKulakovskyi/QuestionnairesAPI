"""
Utility functions for response format conversion and validation
"""

import inspect
from typing import Dict, List, Any, Union


def detect_expected_format(questionnaire_class: type) -> str:
    """
    Detect the expected response format for a questionnaire by inspecting calculate_score signature.
    
    Returns:
        'dict_str' for Dict[str, str]
        'dict_int' for Dict[str, int]
        'dict_float' for Dict[str, float]
        'list_int' for List[int]
        'dict_any' for Dict[str, Any]
        'single_int' for single int
        'single_float' for single float
    """
    if not hasattr(questionnaire_class, 'calculate_score'):
        return 'unknown'
    
    sig = inspect.signature(questionnaire_class.calculate_score)
    params = list(sig.parameters.values())
    
    if len(params) == 0:
        return 'unknown'
    
    first_param = params[0]
    param_type = first_param.annotation
    
    if param_type == inspect.Signature.empty:
        # Try to infer from docstring or default to dict
        return 'dict_any'
    
    # Handle typing hints
    origin = getattr(param_type, '__origin__', None)
    args = getattr(param_type, '__args__', None)
    
    if origin is list:
        if args and args[0] == int:
            return 'list_int'
        return 'list_unknown'
    
    if origin is dict:
        if not args or len(args) < 2:
            return 'dict_any'
        key_type, value_type = args[0], args[1]
        
        if value_type == str:
            return 'dict_str'
        elif value_type == int:
            return 'dict_int'
        elif value_type == float:
            return 'dict_float'
        else:
            return 'dict_any'
    
    if param_type == int:
        return 'single_int'
    elif param_type == float:
        return 'single_float'
    
    return 'dict_any'


def build_text_to_value_map(questions: List[Dict[str, Any]]) -> Dict[str, Dict[str, Union[int, float, str]]]:
    """
    Build a reverse lookup map: question_id -> {text: value}
    
    Returns:
        Dictionary mapping question IDs to dictionaries mapping option text to values
    """
    text_map = {}
    
    for question in questions:
        q_id = question.get('id')
        options = question.get('options', {})
        
        if not q_id or not options:
            continue
        
        text_map[q_id] = {}
        
        # Options can be Dict[int, str] or Dict[str, str]
        for key, value in options.items():
            if isinstance(value, str):
                # Map text to key (which might be int or str)
                text_map[q_id][value] = key
            else:
                # If value is not a string, use it as is
                text_map[q_id][str(value)] = key
    
    return text_map


def normalize_responses(
    responses: Dict[str, Union[str, int, float]],
    questionnaire_instance: Any,
    questions: List[Dict[str, Any]]
) -> Union[Dict[str, Any], List[int]]:
    """
    Normalize API responses to the format expected by the questionnaire's calculate_score method.
    
    Handles:
    - Text responses -> Convert to numeric values using option mapping
    - Numeric responses -> Pass through if valid
    - List[int] questionnaires -> Convert dict to ordered list
    
    Args:
        responses: API responses as Dict[str, Union[str, int, float]]
        questionnaire_instance: Instantiated questionnaire object
        questions: List of question dictionaries
        
    Returns:
        Normalized responses in the format expected by calculate_score
    """
    questionnaire_class = type(questionnaire_instance)
    expected_format = detect_expected_format(questionnaire_class)
    
    # Build text-to-value mapping
    text_to_value = build_text_to_value_map(questions)
    
    # Handle List[int] format (e.g., ADHD-RS)
    if expected_format == 'list_int':
        # Sort questions by number to maintain order
        sorted_questions = sorted(questions, key=lambda q: q.get('number', 0))
        normalized_list = []
        
        for question in sorted_questions:
            q_id = question.get('id')
            if not q_id:
                continue
                
            if q_id not in responses:
                # Default to 0 for missing responses
                normalized_list.append(0)
            else:
                response_value = responses[q_id]
                # Convert if text, otherwise use as-is
                if isinstance(response_value, str):
                    if q_id in text_to_value and response_value in text_to_value[q_id]:
                        normalized_list.append(int(text_to_value[q_id][response_value]))
                    else:
                        # Try to parse as int
                        try:
                            normalized_list.append(int(response_value))
                        except ValueError:
                            raise ValueError(f"Invalid response format for {q_id}: {response_value}")
                else:
                    normalized_list.append(int(response_value))
        
        return normalized_list
    
    # Handle Dict formats
    normalized_dict = {}
    
    for question in questions:
        q_id = question.get('id')
        if not q_id:
            continue
        
        if q_id not in responses:
            continue
        
        response_value = responses[q_id]
        options = question.get('options', {})
        
        # If response is a string, try to convert to value
        if isinstance(response_value, str):
            if q_id in text_to_value and response_value in text_to_value[q_id]:
                normalized_dict[q_id] = text_to_value[q_id][response_value]
            else:
                # Check if it's a direct match in options (value -> text)
                # Try to find matching option text
                found = False
                for opt_key, opt_text in options.items():
                    if opt_text == response_value:
                        normalized_dict[q_id] = opt_key
                        found = True
                        break
                
                if not found:
                    # Try parsing as number
                    try:
                        if expected_format == 'dict_int':
                            normalized_dict[q_id] = int(response_value)
                        elif expected_format == 'dict_float':
                            normalized_dict[q_id] = float(response_value)
                        else:
                            normalized_dict[q_id] = response_value
                    except ValueError:
                        normalized_dict[q_id] = response_value
        else:
            # Numeric response - use as-is but validate
            if expected_format == 'dict_int':
                normalized_dict[q_id] = int(response_value)
            elif expected_format == 'dict_float':
                normalized_dict[q_id] = float(response_value)
            else:
                normalized_dict[q_id] = response_value
    
    return normalized_dict


def validate_response_format(
    responses: Dict[str, Union[str, int, float]],
    questions: List[Dict[str, Any]]
) -> List[str]:
    """
    Validate that responses match expected question formats.
    
    Returns:
        List of error messages (empty if valid)
    """
    errors = []
    
    for question in questions:
        q_id = question.get('id')
        if not q_id:
            continue
            
        options = question.get('options', {})
        
        if q_id not in responses:
            if question.get('required', False):
                errors.append(f"Missing required question: {q_id} (Item {question.get('number', '?')})")
            continue
        
        response_value = responses[q_id]
        
        # Skip None values (will be handled by required check)
        if response_value is None:
            if question.get('required', False):
                errors.append(f"Missing required question: {q_id} (Item {question.get('number', '?')})")
            continue
        
        # Check if response matches any option value or text
        valid = False
        
        # Check if it's a valid option key (value)
        if response_value in options:
            valid = True
        
        # Check if it's a valid option text
        if not valid:
            for opt_text in options.values():
                if isinstance(opt_text, str) and opt_text == response_value:
                    valid = True
                    break
        
        # For numeric responses, check if it's in the valid range
        if not valid and isinstance(response_value, (int, float)):
            option_keys = [k for k in options.keys() if isinstance(k, (int, float))]
            if option_keys:
                min_val = min(option_keys)
                max_val = max(option_keys)
                if min_val <= response_value <= max_val:
                    valid = True
        
        # If still not valid and options exist, show error
        if not valid and options:
            option_preview = list(options.keys())[:3]
            errors.append(
                f"Invalid response for {q_id} (Item {question.get('number', '?')}): "
                f"'{response_value}'. Valid options: {option_preview}..."
            )
        elif not valid and not options:
            # Question with no options (textbox) - accept any value
            valid = True
    
    return errors


def check_mutually_exclusive_questions(
    responses: Dict[str, Union[str, int, float]],
    questions: List[Dict[str, Any]]
) -> List[str]:
    """
    Check mutually exclusive questions (e.g., QIDS6/QIDS7).
    
    Returns:
        List of error messages for violations
    """
    errors = []
    
    for question in questions:
        q_id = question['id']
        mutual_excl_id = question.get('mutually_exclusive_with')
        
        if not mutual_excl_id:
            continue
        
        # Check if both questions are answered
        if q_id in responses and mutual_excl_id in responses:
            # Both answered - check if they're valid together
            # Typically, mutually exclusive means only one should have a non-zero/non-default answer
            q1_value = responses[q_id]
            q2_value = responses[mutual_excl_id]
            
            # Get default/zero values for comparison
            q1_options = question.get('options', {})
            q1_default = 0 if 0 in q1_options else list(q1_options.keys())[0]
            
            # Find the other question
            other_question = next(
                (q for q in questions if q['id'] == mutual_excl_id),
                None
            )
            if other_question:
                q2_options = other_question.get('options', {})
                q2_default = 0 if 0 in q2_options else list(q2_options.keys())[0]
                
                # Both have non-default values - this is an error
                if q1_value != q1_default and q2_value != q2_default:
                    errors.append(
                        f"Questions {q_id} and {mutual_excl_id} are mutually exclusive. "
                        f"Only one should be answered."
                    )
    
    return errors

