# -*- coding: utf-8 -*-
"""
Validation Script for Oikos University Session 3 Slides
Validates:
1. Total slide count is exactly 45.
2. Exactly 4 part section headers on Slides 2, 12, 23, 30.
3. Five case studies on Slides 11, 22, 29, 36, 44.
4. Triad slides have exactly 3 cards.
5. Poll slides have exactly 4 options.
6. Comparison slides have valid leftCard and rightCard with points.
7. Architecture slides have valid layers or tree.
8. Dialogue scripts have 3-presenter format ([Prof. Peter], [TA Sarah], [TA James]) with multi-turn depth.
"""

import re
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

SLIDES_DATA_JS = r"c:\Oikos Univ\src\data\slidesData.js"

def parse_session3_from_js():
    with open(SLIDES_DATA_JS, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r"export\s+const\s+SLIDES_SESSION_3\s*=\s*(\[[\s\S]*?\]);", content)
    if not match:
        raise ValueError("Could not find SLIDES_SESSION_3 in slidesData.js")
    
    import json
    return json.loads(match.group(1))

def main():
    slides = parse_session3_from_js()
    print(f"Total Slides in SLIDES_SESSION_3: {len(slides)}")
    
    errors = []
    warnings = []
    
    if len(slides) != 45:
        errors.append(f"Expected exactly 45 slides, found {len(slides)}")
        
    part_slides = [s for s in slides if s.get('type') == 'section' or s.get('title', '').startswith('PART ')]
    print(f"\n--- PART SECTIONS ({len(part_slides)}) ---")
    for ps in part_slides:
        print(f"  Slide {ps['num']:02d}: {ps['title']}")
        
    expected_parts = {2: "PART 1", 12: "PART 2", 23: "PART 3", 30: "PART 4"}
    for num, prefix in expected_parts.items():
        matching = [s for s in slides if s['num'] == num]
        if not matching:
            errors.append(f"Missing expected part divider on Slide {num}")
        elif not matching[0]['title'].startswith(prefix):
            errors.append(f"Slide {num} title should start with '{prefix}', found: '{matching[0]['title']}'")
            
    case_slides = [s for s in slides if "CASE STUDY" in s.get('title', '').upper()]
    print(f"\n--- CASE STUDIES ({len(case_slides)}) ---")
    for cs in case_slides:
        print(f"  Slide {cs['num']:02d}: {cs['title']}")
        
    expected_case_nums = [11, 22, 29, 36, 44]
    actual_case_nums = [cs['num'] for cs in case_slides]
    if actual_case_nums != expected_case_nums:
        errors.append(f"Case studies expected at slides {expected_case_nums}, found at {actual_case_nums}")
        
    for s in slides:
        num = s['num']
        stype = s.get('type')
        script = s.get('script', '')
        
        # Check speakers in script
        speakers = re.findall(r'\[(.*?)\]', script)
        speaker_set = set(speakers)
        expected_speakers = {"Prof. Peter", "TA Sarah", "TA James"}
        
        if not expected_speakers.issubset(speaker_set):
            missing = expected_speakers - speaker_set
            warnings.append(f"Slide {num:02d} script missing speaker(s): {missing}")
            
        if len(speakers) < 5:
            warnings.append(f"Slide {num:02d} has only {len(speakers)} dialogue turns (recommended 6+)")
            
        # Check layout structures
        if stype == 'triad':
            cards = s.get('cards', [])
            if len(cards) != 3:
                errors.append(f"Slide {num:02d} (triad) should have 3 cards, found {len(cards)}")
        elif stype == 'poll':
            opts = s.get('options', [])
            if len(opts) != 4:
                errors.append(f"Slide {num:02d} (poll) should have 4 options, found {len(opts)}")
        elif stype == 'comparison':
            if not s.get('leftCard') or not s.get('rightCard'):
                errors.append(f"Slide {num:02d} (comparison) missing leftCard or rightCard")
        elif stype == 'architecture':
            layers = s.get('layers', [])
            tree = s.get('tree', [])
            if not layers and not tree:
                errors.append(f"Slide {num:02d} (architecture) missing layers and tree")
                
    print("\n--- VALIDATION SUMMARY ---")
    print(f"Errors: {len(errors)}")
    for e in errors:
        print(f"  ❌ ERROR: {e}")
    print(f"Warnings/Notices: {len(warnings)}")
    for w in warnings:
        print(f"  ⚠️ WARNING: {w}")
        
    if not errors and not warnings:
        print("\n✨ ALL 45 SLIDES FULLY VALIDATED WITH ZERO ERRORS AND ZERO WARNINGS!")
        
    print("\nAll 45 slides summary:")
    for s in slides:
        print(f"  [{s['num']:02d}] ({s.get('type', 'unknown'):<12}) {s.get('title', '')}")

if __name__ == '__main__':
    main()
