"""
Utility functions for extracting questionnaires from the PHP/JS/SQL codebase
"""

import re
import os
from typing import Dict, List, Tuple, Optional, Any
import json


def parse_php_qcm_question(php_line: str) -> Optional[Dict[str, Any]]:
    """
    Parse a PHP QCM (Multiple Choice Question) line
    
    Example input:
    $C2821 = new QCM(array("fr"=>"Question text","en"=>"..."),
                     "SYSTE1",
                     array(-1=>"",1=>"Option 1",2=>"Option 2"),
                     ...);
    
    Returns:
        Dictionary with question_id, text (fr), and options
    """
    # Pattern to match QCM definition
    qcm_pattern = r'new QCM\(array\("fr"=>"([^"]*)".*?\),"([^"]+)",array\((.*?)\),'
    
    match = re.search(qcm_pattern, php_line, re.DOTALL)
    if not match:
        return None
    
    question_text = match.group(1)
    question_id = match.group(2)
    options_str = match.group(3)
    
    # Parse options
    options = {}
    option_pattern = r'(-?\d+)=>"([^"]*)"'
    for opt_match in re.finditer(option_pattern, options_str):
        opt_value = int(opt_match.group(1))
        opt_text = opt_match.group(2)
        options[opt_value] = opt_text
    
    return {
        'id': question_id,
        'text': question_text,
        'options': options,
        'type': 'select'
    }


def extract_questionnaire_from_php(php_file_path: str) -> Dict[str, Any]:
    """
    Extract questionnaire structure from a PHP form file
    
    Args:
        php_file_path: Path to PHP file
        
    Returns:
        Dictionary with questionnaire metadata and questions
    """
    with open(php_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract table name/form name
    form_pattern = r'new formulaire\("([^"]+)"'
    form_match = re.search(form_pattern, content)
    table_name = form_match.group(1) if form_match else "unknown"
    
    # Extract title
    title_pattern = r'new formulaire\([^,]+,[^,]+,"([^"]+)"'
    title_match = re.search(title_pattern, content)
    title = title_match.group(1) if title_match else "Unknown Questionnaire"
    
    questions = []
    
    # Find all QCM questions
    for line in content.split('\n'):
        if 'new QCM' in line:
            question = parse_php_qcm_question(line)
            if question:
                questions.append(question)
        elif 'new Textbox' in line:
            # Handle text input questions
            textbox_pattern = r'new Textbox\(array\("fr"=>"([^"]*)".*?\),"([^"]+)"'
            match = re.search(textbox_pattern, line)
            if match:
                questions.append({
                    'id': match.group(2),
                    'text': match.group(1),
                    'type': 'textbox',
                    'options': {}
                })
    
    return {
        'table_name': table_name,
        'title': title,
        'questions': questions
    }


def parse_javascript_scoring(js_file_path: str) -> Dict[str, Any]:
    """
    Extract scoring logic from JavaScript file
    
    Args:
        js_file_path: Path to JavaScript scoring file
        
    Returns:
        Dictionary with scoring information
    """
    try:
        with open(js_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return {'error': 'File not found', 'scoring_logic': None}
    
    # Extract function name
    function_pattern = r'function\s+(\w+)\s*\('
    function_match = re.search(function_pattern, content)
    function_name = function_match.group(1) if function_match else "unknown"
    
    # Extract reverse scoring indices (common pattern)
    reverse_indices = []
    
    # Pattern: if(i==0 || i== 3 || i== 4|| ...)
    indices_pattern = r'if\(i==(\d+(?:\s*\|\|\s*i==\s*\d+)*)\)'
    for match in re.finditer(indices_pattern, content):
        indices_str = match.group(1)
        # Extract all numbers
        numbers = re.findall(r'\d+', indices_str)
        reverse_indices.extend([int(n) for n in numbers])
    
    return {
        'function_name': function_name,
        'reverse_score_indices': list(set(reverse_indices)),
        'raw_content': content
    }


def extract_sql_questionnaire(sql_content: str, table_name: str) -> Dict[str, Any]:
    """
    Extract questionnaire from SQL CREATE TABLE statement
    
    Args:
        sql_content: SQL file content
        table_name: Name of the table (e.g., 'autoq_aim')
        
    Returns:
        Dictionary with questionnaire data
    """
    # Find the CREATE TABLE statement
    pattern = rf'CREATE TABLE.*?`{table_name}`\s*\((.*?)\)\s*ENGINE'
    match = re.search(pattern, sql_content, re.DOTALL | re.IGNORECASE)
    
    if not match:
        return {'error': 'Table not found'}
    
    table_def = match.group(1)
    
    questions = []
    
    # Parse columns with ENUM type (these are questions with fixed options)
    enum_pattern = r"`(\w+)`\s+enum\((.*?)\)"
    
    for enum_match in re.finditer(enum_pattern, table_def, re.IGNORECASE):
        column_name = enum_match.group(1)
        enum_values_str = enum_match.group(2)
        
        # Skip non-question columns
        if column_name.startswith('ID_') or column_name == 'date_saisie':
            continue
        
        # Parse enum values
        enum_values = re.findall(r"'([^']*)'", enum_values_str)
        
        questions.append({
            'id': column_name,
            'type': 'enum',
            'options': {i: val for i, val in enumerate(enum_values)}
        })
    
    return {
        'table_name': table_name,
        'questions': questions
    }


def list_questionnaires_to_extract(base_path: str) -> Dict[str, List[str]]:
    """
    List all questionnaires that need to be extracted
    
    Returns:
        Dictionary with lists of files per application
    """
    questionnaires = {
        'asperger': [],
        'cedr': [],
        'ebipolar': [],
        'eschizo': []
    }
    
    # Asperger app (easperger directory) - find all PHP files with corresponding JS score files
    asperger_form_path = os.path.join(base_path, 'apps/easperger/www/form')
    asperger_js_path = os.path.join(base_path, 'apps/easperger/www/js_scores')
    
    if os.path.exists(asperger_js_path):
        for js_file in os.listdir(asperger_js_path):
            if js_file.endswith('_score.js'):
                form_id = js_file.replace('_score.js', '')
                php_file = f"{form_id}.php"
                php_path = os.path.join(asperger_form_path, php_file)
                if os.path.exists(php_path):
                    questionnaires['asperger'].append(form_id)
    
    # CEDR app - same structure
    cedr_form_path = os.path.join(base_path, 'apps/ecedr/www/form')
    cedr_js_path = os.path.join(base_path, 'apps/ecedr/www/js_scores')
    
    if os.path.exists(cedr_js_path):
        for js_file in os.listdir(cedr_js_path):
            if js_file.endswith('_score.js'):
                form_id = js_file.replace('_score.js', '')
                php_file = f"{form_id}.php"
                php_path = os.path.join(cedr_form_path, php_file)
                if os.path.exists(php_path):
                    questionnaires['cedr'].append(form_id)
    
    # eBipolar - extract from SQL
    ebipolar_sql = os.path.join(base_path, 'db_data/ebipolar/ebipolar.sql')
    if os.path.exists(ebipolar_sql):
        with open(ebipolar_sql, 'r', encoding='utf-8') as f:
            content = f.read()
            # Find all autoq_ and hetero_ tables
            table_pattern = r'CREATE TABLE `((?:autoq_|hetero_)\w+)`'
            tables = re.findall(table_pattern, content)
            # Remove _nom_champ and _groupe tables
            tables = [t for t in tables if not (t.endswith('_nom_champ') or t.endswith('_groupe'))]
            questionnaires['ebipolar'] = tables
    
    # eSchizo - same as eBipolar
    eschizo_sql = os.path.join(base_path, 'db_data/eschizo/eschizo.sql')
    if os.path.exists(eschizo_sql):
        with open(eschizo_sql, 'r', encoding='utf-8') as f:
            content = f.read()
            table_pattern = r'CREATE TABLE.*?`((?:autoq_|hetero_)\w+)`'
            tables = re.findall(table_pattern, content, re.IGNORECASE)
            tables = [t for t in tables if not (t.endswith('_nom_champ') or t.endswith('_groupe'))]
            questionnaires['eschizo'] = tables
    
    return questionnaires


def generate_python_class_name(questionnaire_name: str) -> str:
    """
    Generate a Python class name from questionnaire identifier
    
    Examples:
        'autoq_aim' -> 'AIMQuestionnaire'
        'hetero_madrs' -> 'MADRSQuestionnaire'
        '209' -> 'Systematisation209Questionnaire'
    """
    # Remove prefixes
    name = questionnaire_name.replace('autoq_', '').replace('hetero_', '')
    
    # Convert to title case and remove underscores
    words = name.split('_')
    class_name = ''.join(word.capitalize() for word in words)
    
    return f"{class_name}Questionnaire"


def generate_python_file_name(questionnaire_name: str) -> str:
    """
    Generate a Python file name from questionnaire identifier
    
    Examples:
        'autoq_aim' -> 'aim.py'
        'hetero_madrs' -> 'madrs.py'
    """
    # Remove prefixes
    name = questionnaire_name.replace('autoq_', '').replace('hetero_', '')
    
    return f"{name}.py"


if __name__ == "__main__":
    # Test extraction
    base_path = "/Users/andriikulakovskyi/Documents/Projets/ebipolar_eschizo"
    
    questionnaires = list_questionnaires_to_extract(base_path)
    
    print("Questionnaires to extract:")
    for app, q_list in questionnaires.items():
        print(f"\n{app.upper()}: {len(q_list)} questionnaires")
        print(f"  {', '.join(q_list[:5])}..." if len(q_list) > 5 else f"  {', '.join(q_list)}")

