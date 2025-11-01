"""
Automatic Questionnaire Class Generator
========================================

This script automatically generates questionnaire classes from extracted JSON data.

Usage:
    python generate_questionnaires.py --source ../extracted_questions_*.json --output ../questionnaires/

Features:
- Reads extracted question data from JSON
- Generates complete Python questionnaire class
- Includes real French question text and answer options
- Applies default scoring strategy (can be customized later)
- Registers questionnaire automatically

Author: Fondation FondaMental
Version: 2.0.0
"""

import json
import argparse
from pathlib import Path
from typing import Dict, List


# Template for questionnaire class
QUESTIONNAIRE_TEMPLATE = '''"""
{name} - {full_name}
{underline}

{description}

Source: {source_info}
Applications: {applications}
Author: Fondation FondaMental
Version: 2.0.0
"""

from dataclasses import dataclass
from ..core.models import (
    BaseQuestionnaire,
    Question,
    AnswerOption,
    QuestionType,
    PathologyDomain,
    RespondentType,
    QuestionnaireResponse,
    ScoreResult
)
from ..core.scoring import {scoring_strategy_import}
from ..core.registry import register_questionnaire


@register_questionnaire("{code}")
@dataclass
class {class_name}(BaseQuestionnaire):
    """{full_name} - reusable across applications."""
    
    def __init__(self):
        """Initialize {code} questionnaire with all {item_count} items."""
        
        questions_list = [
{questions_code}
        ]
        
        super().__init__(
            code="{code}",
            name="{full_name}",
            description="{description}",
            pathology_domain=PathologyDomain.{pathology},
            respondent_type=RespondentType.{respondent_type},
            questions=questions_list,
            visit_types={visit_types},
            estimated_duration_minutes={duration},
            version="1.0"
        )
        
        self.scoring_strategy = {scoring_strategy_init}
    
    def compute_score(self, responses: QuestionnaireResponse) -> ScoreResult:
        """Compute {code} score."""
        validation_errors = self.validate_responses(responses)
        if validation_errors:
            raise ValueError(f"Invalid responses: {{'; '.join(validation_errors)}}")
        
        result = self.scoring_strategy.calculate(responses, self.questions)
        return result
'''


QUESTION_TEMPLATE = '''            Question(
                id='{qid}',
                text="{text}",
                options=[
{options}
                ],
                question_type=QuestionType.SINGLE_CHOICE
            )'''


OPTION_TEMPLATE = '''                    AnswerOption(value='{value}', label="{label}", score={score})'''


def escape_string(s: str) -> str:
    """Escape strings for Python code."""
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')


def determine_pathology(app_name: str) -> str:
    """Map application name to pathology domain."""
    mapping = {
        'ebipolar': 'BIPOLAR',
        'eschizo': 'SCHIZOPHRENIA',
        'ecedr': 'DEPRESSION',
        'easperger': 'AUTISM_SPECTRUM',
    }
    return mapping.get(app_name.lower(), 'GENERAL')


def determine_respondent_type(quest_code: str) -> str:
    """Guess respondent type from questionnaire code."""
    code_upper = quest_code.upper()
    
    # Known clinician-rated scales
    clinician = ['YMRS', 'MADRS', 'PANSS', 'CALGARY', 'BARNES', 'CGI', 'FAST']
    if any(c in code_upper for c in clinician):
        return 'CLINICIAN_RATED'
    
    # Known self-report
    self_report = ['ALTMAN', 'MDQ', 'BIS', 'ASRS', 'SHAPS', 'QIDS', 'BFI']
    if any(c in code_upper for c in self_report):
        return 'SELF_REPORT'
    
    # Default
    return 'SELF_REPORT'


def generate_question_code(qid: str, question_data: Dict) -> str:
    """Generate Python code for a single Question object."""
    
    text = escape_string(question_data['text'])
    options_list = question_data.get('options', [])
    
    # Generate options code
    options_code = []
    for idx, option_text in enumerate(options_list):
        # Determine value (a, b, c... or 0, 1, 2...)
        if len(options_list) <= 10:
            value = chr(ord('a') + idx)
        else:
            value = str(idx)
        
        option_label = escape_string(option_text)
        option_code = OPTION_TEMPLATE.format(
            value=value,
            label=option_label,
            score=idx
        )
        options_code.append(option_code)
    
    options_str = ',\n'.join(options_code)
    
    return QUESTION_TEMPLATE.format(
        qid=qid,
        text=text,
        options=options_str
    )


def generate_questionnaire_class(
    quest_code: str,
    questions_dict: Dict,
    app_name: str,
    output_dir: Path
) -> Path:
    """
    Generate a complete questionnaire class file.
    
    Args:
        quest_code: Questionnaire code (e.g., "YMRS")
        questions_dict: Dictionary of question data
        app_name: Application name (ebipolar, eschizo, etc.)
        output_dir: Output directory for generated file
    
    Returns:
        Path to generated file
    """
    
    # Generate questions code
    questions_code_list = []
    for qid in sorted(questions_dict.keys()):
        q_data = questions_dict[qid]
        q_code = generate_question_code(qid, q_data)
        questions_code_list.append(q_code)
    
    questions_code = ',\n'.join(questions_code_list)
    
    # Determine metadata
    item_count = len(questions_dict)
    pathology = determine_pathology(app_name)
    respondent_type = determine_respondent_type(quest_code)
    
    # Class name: convert CODE to TitleCase
    class_name = ''.join(word.capitalize() for word in quest_code.split('_'))
    
    # Full name (can be customized later)
    full_name = f"{quest_code} Questionnaire"
    
    # Description (placeholder)
    description = f"{item_count} item{'s' if item_count > 1 else ''} questionnaire"
    
    # Estimated duration (rough estimate: 30 seconds per question)
    duration = max(5, (item_count * 30) // 60)
    
    # Determine scoring strategy
    if item_count < 5:
        scoring_strategy_import = "SimpleSumStrategy"
        scoring_strategy_init = "SimpleSumStrategy()"
    else:
        scoring_strategy_import = "SimpleSumStrategy"
        scoring_strategy_init = "SimpleSumStrategy()"
    
    # Generate underline
    header_text = f"{quest_code} - {full_name}"
    underline = '=' * len(header_text)
    
    # Generate file content
    file_content = QUESTIONNAIRE_TEMPLATE.format(
        name=quest_code,
        full_name=full_name,
        underline=underline,
        description=description,
        source_info=f"Extracted from {app_name} application",
        applications=app_name,
        code=quest_code,
        class_name=class_name,
        item_count=item_count,
        questions_code=questions_code,
        pathology=pathology,
        respondent_type=respondent_type,
        visit_types='["Initial", "Follow-up"]',
        duration=duration,
        scoring_strategy_import=scoring_strategy_import,
        scoring_strategy_init=scoring_strategy_init
    )
    
    # Write to file
    filename = f"{quest_code.lower()}.py"
    output_path = output_dir / filename
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(file_content)
    
    return output_path


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Generate questionnaire classes from JSON')
    parser.add_argument('--source', nargs='+', required=True, help='Path to extracted JSON file(s)')
    parser.add_argument('--output', default='../questionnaires/', help='Output directory')
    parser.add_argument('--app', help='Application name (ebipolar, eschizo, etc.)')
    
    args = parser.parse_args()
    
    # Setup paths
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Get JSON files from arguments
    json_files = [Path(f) for f in args.source]
    
    print(f"Found {len(json_files)} JSON file(s)")
    
    total_generated = 0
    
    for json_file in json_files:
        print(f"\nProcessing: {json_file.name}")
        
        # Determine app name from filename if not provided
        if args.app:
            app_name = args.app
        else:
            # Extract from filename: extracted_questions_APP.json
            parts = json_file.stem.split('_')
            if 'ebipolar' in json_file.stem:
                app_name = 'ebipolar'
            elif 'eschizo' in json_file.stem:
                app_name = 'eschizo'
            elif 'ecedr' in json_file.stem:
                app_name = 'ecedr'
            elif 'easperger' in json_file.stem:
                app_name = 'easperger'
            else:
                app_name = 'general'
        
        # Load JSON
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Generate class for each questionnaire
        for quest_code, questions_dict in data.items():
            if not questions_dict:
                print(f"  ⚠️  Skipping {quest_code} (no questions)")
                continue
            
            try:
                output_path = generate_questionnaire_class(
                    quest_code=quest_code,
                    questions_dict=questions_dict,
                    app_name=app_name,
                    output_dir=output_dir
                )
                print(f"  ✅ Generated {quest_code} → {output_path.name}")
                total_generated += 1
            
            except Exception as e:
                print(f"  ❌ Error generating {quest_code}: {e}")
    
    print(f"\n{'='*60}")
    print(f"✅ Generated {total_generated} questionnaire classes")
    print(f"📁 Output directory: {output_dir.absolute()}")
    print(f"{'='*60}")
    
    print("\n📝 Next steps:")
    print("1. Review generated files and customize as needed")
    print("2. Update scoring strategies for complex questionnaires")
    print("3. Add interpretation thresholds")
    print("4. Import all classes in questionnaires/__init__.py")


if __name__ == "__main__":
    main()
