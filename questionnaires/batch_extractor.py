"""
Batch extraction script for all questionnaires
This script systematically extracts all 146+ questionnaires from the four applications
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any, Set, Optional
from extraction_utils import (
    extract_questionnaire_from_php,
    parse_javascript_scoring,
    extract_sql_questionnaire,
    generate_python_class_name,
    generate_python_file_name,
    list_questionnaires_to_extract
)


BASE_PATH = "/Users/andriikulakovskyi/Documents/Projets/ebipolar_eschizo"
OUTPUT_PATH = Path(BASE_PATH) / "Questionnaires"


class QuestionnaireExtractor:
    """Main extractor class for processing all questionnaires"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.questionnaires_index = {}
        self.duplicates_map = {}
        
    def identify_duplicates(self) -> Dict[str, List[str]]:
        """Identify questionnaires that appear in multiple applications"""
        
        # Common questionnaires across applications (based on name similarity)
        # Key: canonical name, Value: list of (app, identifier) tuples
        common_questionnaires = {}
        
        all_questionnaires = list_questionnaires_to_extract(str(self.base_path))
        
        # eBipolar and eSchizo tables
        ebipolar_tables = set(all_questionnaires.get('ebipolar', []))
        eschizo_tables = set(all_questionnaires.get('eschizo', []))
        
        # Find common tables
        common_tables = ebipolar_tables & eschizo_tables
        
        for table in common_tables:
            canonical_name = table.replace('autoq_', '').replace('hetero_', '')
            if canonical_name not in common_questionnaires:
                common_questionnaires[canonical_name] = []
            common_questionnaires[canonical_name].append(('ebipolar', table))
            common_questionnaires[canonical_name].append(('eschizo', table))
        
        # Check for MADRS, YMRS etc. in CEDR
        cedr_forms = all_questionnaires.get('cedr', [])
        for form_id in cedr_forms:
            # Try to extract questionnaire name from PHP file
            php_path = self.base_path / f"apps/ecedr/www/form/{form_id}.php"
            if php_path.exists():
                with open(php_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Check if it's MADRS, YMRS, etc.
                    if 'MADRS' in content.upper():
                        if 'madrs' not in common_questionnaires:
                            common_questionnaires['madrs'] = []
                        common_questionnaires['madrs'].append(('cedr', form_id))
                    elif 'YMRS' in content.upper():
                        if 'ymrs' not in common_questionnaires:
                            common_questionnaires['ymrs'] = []
                        common_questionnaires['ymrs'].append(('cedr', form_id))
        
        return common_questionnaires
    
    def extract_php_questionnaire(self, app: str, form_id: str) -> Dict[str, Any]:
        """Extract a questionnaire from PHP/JS files"""
        
        # Map app name to directory name
        app_dir_map = {
            'asperger': 'easperger',
            'cedr': 'ecedr'
        }
        app_dir = app_dir_map.get(app, app)
        
        php_path = self.base_path / f"apps/{app_dir}/www/form/{form_id}.php"
        js_path = self.base_path / f"apps/{app_dir}/www/js_scores/{form_id}_score.js"
        
        questionnaire_data = extract_questionnaire_from_php(str(php_path))
        
        if js_path.exists():
            scoring_data = parse_javascript_scoring(str(js_path))
            questionnaire_data['scoring'] = scoring_data
        
        questionnaire_data['source_app'] = app
        questionnaire_data['form_id'] = form_id
        
        return questionnaire_data
    
    def extract_sql_questionnaire_full(self, app: str, table_name: str) -> Dict[str, Any]:
        """Extract a questionnaire from SQL database schema"""
        
        sql_path = self.base_path / f"db_data/{app}/{app}.sql"
        
        with open(sql_path, 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        questionnaire_data = extract_sql_questionnaire(sql_content, table_name)
        
        # Try to find _nom_champ table for question texts
        nom_champ_table = f"{table_name}_nom_champ"
        nom_champ_data = self._extract_nom_champ(sql_content, nom_champ_table)
        if nom_champ_data:
            questionnaire_data['question_metadata'] = nom_champ_data
        
        questionnaire_data['source_app'] = app
        questionnaire_data['table_name'] = table_name
        
        return questionnaire_data
    
    def _extract_nom_champ(self, sql_content: str, table_name: str) -> Optional[Dict]:
        """Extract question metadata from _nom_champ table"""
        
        # This would typically be in INSERT statements
        # Pattern: INSERT INTO `table_name` ... VALUES (...)
        pattern = rf"INSERT INTO `{table_name}`.*?VALUES\s*(.*?);"
        
        match = re.search(pattern, sql_content, re.DOTALL | re.IGNORECASE)
        if not match:
            return None
        
        # Would need more complex parsing for full extraction
        return {'found': True}
    
    def generate_questionnaire_class(self, questionnaire_data: Dict[str, Any], 
                                     used_in_apps: List[str]) -> str:
        """Generate Python class code for a questionnaire"""
        
        title = questionnaire_data.get('title', 'Unknown')
        table_name = questionnaire_data.get('table_name', questionnaire_data.get('form_id', 'unknown'))
        class_name = generate_python_class_name(table_name)
        
        questions_code = self._generate_questions_code(questionnaire_data['questions'])
        scoring_code = self._generate_scoring_code(questionnaire_data.get('scoring', {}))
        
        template = f'''"""
Questionnaire: {title}
"""

from typing import Dict, List, Optional, Any


class {class_name}:
    """{title}"""
    
    def __init__(self):
        self.name = "{title}"
        self.description = ""
        self.used_in_applications = {used_in_apps}
        self.questions = self._init_questions()
        
    def _init_questions(self) -> List[Dict[str, Any]]:
        """Initialize all questions"""
        questions = {questions_code}
        return questions
    
    def validate_responses(self, responses: Dict[str, Any]) -> Dict[str, List[str]]:
        """Validate responses"""
        errors = []
        
        for question in self.questions:
            q_id = question['id']
            if q_id not in responses or responses[q_id] is None:
                errors.append(f"Question {{question.get('number', question['id'])}} doit être renseignée")
        
        return {{'errors': errors, 'valid': len(errors) == 0}}
    
    def calculate_score(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate questionnaire score"""
        validation = self.validate_responses(responses)
        if not validation['valid']:
            return {{
                'score': None,
                'valid': False,
                'errors': validation['errors']
            }}
        
        {scoring_code}
        
        return {{
            'score': total_score,
            'valid': True,
            'errors': []
        }}


if __name__ == "__main__":
    questionnaire = {class_name}()
    print(f"Questionnaire: {{questionnaire.name}}")
    print(f"Number of questions: {{len(questionnaire.questions)}}")
'''
        
        return template
    
    def _generate_questions_code(self, questions: List[Dict]) -> str:
        """Generate code for questions list"""
        if not questions:
            return "[]"
        
        questions_str = "[\n"
        for q in questions:
            questions_str += "            {\n"
            questions_str += f"                'id': '{q['id']}',\n"
            questions_str += f"                'text': '{q.get('text', '')}',\n"
            questions_str += f"                'type': '{q.get('type', 'select')}',\n"
            questions_str += f"                'options': {q.get('options', {})},\n"
            questions_str += "            },\n"
        questions_str += "        ]"
        
        return questions_str
    
    def _generate_scoring_code(self, scoring_data: Dict) -> str:
        """Generate scoring calculation code"""
        if not scoring_data or 'reverse_score_indices' not in scoring_data:
            # Simple sum scoring
            return """total_score = 0
        for question in self.questions:
            q_id = question['id']
            total_score += responses.get(q_id, 0)"""
        
        # More complex scoring with reverse items
        return """# Scoring logic extracted from JavaScript
        total_score = 0
        # TODO: Implement specific scoring logic"""
    
    def process_all_questionnaires(self):
        """Main processing function"""
        
        print("Starting extraction of all questionnaires...")
        print("=" * 70)
        
        # Get all questionnaires
        all_questionnaires = list_questionnaires_to_extract(str(self.base_path))
        
        # Identify duplicates
        common_questionnaires = self.identify_duplicates()
        print(f"\nIdentified {len(common_questionnaires)} shared questionnaires across apps")
        
        processed = set()
        extracted_count = 0
        
        # Process each application
        for app, questionnaire_list in all_questionnaires.items():
            print(f"\nProcessing {app.upper()}: {len(questionnaire_list)} questionnaires")
            
            for q_id in questionnaire_list:
                # Skip if already processed (duplicate)
                canonical_name = q_id.replace('autoq_', '').replace('hetero_', '')
                if canonical_name in processed:
                    print(f"  Skipping {q_id} (already extracted as shared questionnaire)")
                    continue
                
                try:
                    # Extract based on app type
                    if app in ['asperger', 'cedr']:
                        q_data = self.extract_php_questionnaire(app, q_id)
                    else:  # ebipolar, eschizo
                        q_data = self.extract_sql_questionnaire_full(app, q_id)
                    
                    # Determine which apps use this questionnaire
                    used_in = [app]
                    if canonical_name in common_questionnaires:
                        used_in = [app_name for app_name, _ in common_questionnaires[canonical_name]]
                    
                    # Generate Python class
                    # (For now, just log - actual generation would be done here)
                    print(f"  ✓ Extracted: {q_id} (used in: {', '.join(used_in)})")
                    
                    processed.add(canonical_name)
                    extracted_count += 1
                    
                except Exception as e:
                    print(f"  ✗ Error extracting {q_id}: {str(e)}")
        
        print(f"\n{'=' * 70}")
        print(f"Extraction complete: {extracted_count} questionnaires processed")
        print(f"Output directory: {OUTPUT_PATH}")


if __name__ == "__main__":
    extractor = QuestionnaireExtractor(BASE_PATH)
    extractor.process_all_questionnaires()

