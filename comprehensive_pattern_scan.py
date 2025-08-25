#!/usr/bin/env python3
"""Comprehensive scan of all grammar patterns to find missing underscore cases"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from src.data.csv_loader import CSVLoader
from src.data.question_generator import QuestionGenerator
from collections import defaultdict

csv_loader = CSVLoader()
question_gen = QuestionGenerator()

print("🔍 Comprehensive scan of ALL sentence_completion questions...")

# Get all grammar data
grammar_data = csv_loader.load_grammar('N4')

# Focus only on sentence_completion questions (fill-in-the-blank)
sentence_completion_items = [
    item for item in grammar_data 
    if item.get('question_type') == 'sentence_completion'
]

print(f"Found {len(sentence_completion_items)} sentence_completion questions to test")

# Group by pattern to see which ones are failing
pattern_results = defaultdict(list)
failed_patterns = defaultdict(list)

# Test each sentence completion question
for i, item in enumerate(sentence_completion_items):
    pattern = item.get('grammar_pattern', '')
    hiragana = item.get('hiragana_reading', '')
    sentence = item.get('japanese_sentence', '')
    
    if not pattern or not hiragana:
        continue
        
    try:
        # Generate question with hiragana display
        question = question_gen.generate_grammar_question(item, show_hiragana=True)
        display_text = question.get('display_text', '')
        
        has_underscores = '_' in display_text
        
        # Track results by pattern
        pattern_results[pattern].append({
            'has_underscores': has_underscores,
            'sentence': sentence[:50] + '...' if len(sentence) > 50 else sentence,
            'hiragana': hiragana[:50] + '...' if len(hiragana) > 50 else hiragana,
            'display': display_text
        })
        
        if not has_underscores:
            # This is a FAILED case - pattern reveals answer
            failed_patterns[pattern].append({
                'sentence': sentence,
                'hiragana': hiragana,
                'display': display_text
            })
            
    except Exception as e:
        print(f"Error with item {i}: {e}")

print(f"\n📊 RESULTS BY PATTERN:")
print(f"Total unique patterns tested: {len(pattern_results)}")

# Show patterns with failures
failing_patterns = []
for pattern, results in pattern_results.items():
    total = len(results)
    failed = len([r for r in results if not r['has_underscores']])
    success_rate = ((total - failed) / total * 100) if total > 0 else 0
    
    if failed > 0:
        failing_patterns.append((pattern, failed, total, success_rate))

# Sort by number of failures (most problematic first)
failing_patterns.sort(key=lambda x: x[1], reverse=True)

print(f"\n🚨 PATTERNS THAT REVEAL ANSWERS ({len(failing_patterns)} patterns):")
for pattern, failed, total, success_rate in failing_patterns[:15]:  # Show top 15
    print(f"  {pattern}: {failed}/{total} failed ({success_rate:.1f}% working)")

if failing_patterns:
    print(f"\n🔍 DETAILED ANALYSIS OF TOP FAILING PATTERNS:")
    for pattern, failed, total, success_rate in failing_patterns[:5]:  # Detail top 5
        print(f"\n--- Pattern: '{pattern}' ---")
        examples = failed_patterns[pattern][:2]  # Show 2 examples
        for i, example in enumerate(examples, 1):
            print(f"  Example {i}:")
            print(f"    Sentence: {example['sentence']}")
            print(f"    Hiragana: {example['hiragana']}")
            print(f"    Display: {example['display']}")
            
            # Quick analysis of why it failed
            if pattern in example['hiragana']:
                print(f"    ISSUE: Pattern '{pattern}' directly visible in hiragana!")
            else:
                print(f"    ISSUE: Pattern may appear in conjugated/modified form")

print(f"\n🎯 NEXT STEPS:")
print(f"1. Add specific handling for each failing pattern")
print(f"2. Handle conjugated forms, compound patterns, and edge cases")
print(f"3. Test until 100% of sentence_completion questions hide their answers")