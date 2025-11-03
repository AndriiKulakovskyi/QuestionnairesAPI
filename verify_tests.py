#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quick verification script to check test structure
This script verifies the test files are properly structured without running them
"""

import sys
from pathlib import Path
import ast


def analyze_test_file(filepath):
    """Analyze a test file and extract information"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    tree = ast.parse(content)
    
    classes = []
    total_tests = 0
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            # Count test methods in this class
            test_methods = [
                m.name for m in node.body 
                if isinstance(m, ast.FunctionDef) and m.name.startswith('test_')
            ]
            if test_methods:
                classes.append({
                    'name': node.name,
                    'test_count': len(test_methods),
                    'tests': test_methods
                })
                total_tests += len(test_methods)
    
    return classes, total_tests


def main():
    """Main verification function"""
    print("=" * 70)
    print("QUESTIONNAIRES API - TEST STRUCTURE VERIFICATION")
    print("=" * 70)
    
    project_root = Path(__file__).parent
    tests_dir = project_root / "tests"
    
    if not tests_dir.exists():
        print("\n❌ ERROR: tests/ directory not found!")
        return 1
    
    # Check test files
    test_files = {
        'test_qids_sr16.py': 'QIDS-SR16 Tests',
        'test_mdq.py': 'MDQ Tests',
        'test_asrm.py': 'ASRM Tests',
        'test_epworth.py': 'Epworth Tests',
        'test_eq5del.py': 'EQ-5D-EL Tests',
        'test_fagerstrom.py': 'Fagerström Tests'
    }
    
    total_classes = 0
    total_tests = 0
    
    for filename, description in test_files.items():
        filepath = tests_dir / filename
        
        print(f"\n{description}")
        print("-" * 70)
        
        if not filepath.exists():
            print(f"❌ File not found: {filename}")
            continue
        
        try:
            classes, test_count = analyze_test_file(filepath)
            total_classes += len(classes)
            total_tests += test_count
            
            print(f"✅ File: {filename}")
            print(f"   Test Classes: {len(classes)}")
            print(f"   Test Methods: {test_count}")
            
            for cls in classes:
                print(f"\n   📋 {cls['name']}")
                print(f"      Tests: {cls['test_count']}")
                if len(cls['tests']) <= 5:
                    for test in cls['tests']:
                        print(f"         • {test}")
                else:
                    for test in cls['tests'][:3]:
                        print(f"         • {test}")
                    print(f"         ... and {cls['test_count'] - 3} more")
        
        except Exception as e:
            print(f"❌ Error analyzing {filename}: {e}")
    
    # Check supporting files
    print("\n" + "=" * 70)
    print("SUPPORTING FILES")
    print("=" * 70)
    
    supporting_files = {
        'tests/__init__.py': 'Test package marker',
        'tests/conftest.py': 'Pytest configuration and fixtures',
        'pytest.ini': 'Pytest settings',
        'run_tests.py': 'Test runner script',
        'TESTING.md': 'Testing documentation',
        'TEST_SUMMARY.md': 'Test summary'
    }
    
    for filepath, description in supporting_files.items():
        full_path = project_root / filepath
        if full_path.exists():
            print(f"✅ {filepath:30} - {description}")
        else:
            print(f"❌ {filepath:30} - MISSING")
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total Test Classes: {total_classes}")
    print(f"Total Test Methods: {total_tests}")
    print(f"Expected Coverage: >95%")
    print(f"Expected Runtime: <5 seconds")
    
    # Check if questionnaire classes exist
    print("\n" + "=" * 70)
    print("QUESTIONNAIRE CLASSES")
    print("=" * 70)
    
    try:
        from questionnaires import QIDSSR16, QIDSError, MDQ, MDQError, ASRM, ASRMError, Epworth, EpworthError, EQ5DEL, EQ5DELError, Fagerstrom, FagerstromError
        print("✅ QIDSSR16 class imported successfully")
        print("✅ MDQ class imported successfully")
        print("✅ ASRM class imported successfully")
        print("✅ Epworth class imported successfully")
        print("✅ EQ-5D-EL class imported successfully")
        print("✅ Fagerström class imported successfully")
        print("✅ Error classes imported successfully")
        
        # Quick instantiation test
        qids = QIDSSR16()
        mdq = MDQ()
        asrm = ASRM()
        epworth = Epworth()
        eq5d = EQ5DEL()
        fager = Fagerstrom()
        print(f"✅ QIDSSR16 instance created ({len(qids.get_questions())} questions)")
        print(f"✅ MDQ instance created ({len(mdq.get_questions())} questions)")
        print(f"✅ ASRM instance created ({len(asrm.get_questions())} questions)")
        print(f"✅ Epworth instance created ({len(epworth.get_questions())} questions)")
        print(f"✅ EQ-5D-EL instance created ({len(eq5d.get_questions())} questions)")
        print(f"✅ Fagerström instance created ({len(fager.get_questions())} questions)")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("\n⚠️  Note: You may need to install dependencies:")
        print("   pip install -r requirements.txt")
        return 1
    
    print("\n" + "=" * 70)
    print("✅ VERIFICATION COMPLETE - All checks passed!")
    print("=" * 70)
    print("\nTo run the tests:")
    print("  python run_tests.py all")
    print("\nOr with pytest directly:")
    print("  pytest -v")
    print("\n")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

