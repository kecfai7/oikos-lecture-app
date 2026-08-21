import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

with open(r'c:\Oikos Univ\src\data\slidesData.js', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'export const SLIDES_SESSION_2 = (\[[\s\S]*?\n\]);', content)
if not m:
    print('ERROR: SLIDES_SESSION_2 not found!')
    exit(1)

slides = json.loads(m.group(1))
print(f'Total Slides in SLIDES_SESSION_2: {len(slides)}')

errors = []
warnings = []

part_section_slides = []
case_study_slides = []

for idx, s in enumerate(slides):
    num = s.get('num')
    expected_num = idx + 1
    if num != expected_num:
        errors.append(f'Slide index {idx} has num={num}, expected {expected_num}')
    
    stype = s.get('type')
    title = s.get('title', '')
    script = s.get('script', '')
    kg = s.get('koreanGuide', {})
    kt = s.get('keyTerms', [])
    
    # Check sections
    if stype == 'section':
        part_section_slides.append((num, title))
    if 'CASE STUDY' in title:
        case_study_slides.append((num, title))
        
    # Check structure types
    if stype == 'triad':
        cards = s.get('cards', [])
        if len(cards) != 3:
            errors.append(f'Slide {num} (triad) has {len(cards)} cards, expected 3')
    elif stype == 'architecture':
        layers = s.get('layers', [])
        if len(layers) not in [3, 4] and not s.get('tree'):
            errors.append(f'Slide {num} (architecture) has {len(layers)} layers, expected 3 or 4')
    elif stype == 'comparison':
        if 'leftCard' not in s or 'rightCard' not in s:
            errors.append(f'Slide {num} (comparison) missing leftCard or rightCard')
    elif stype == 'metric':
        metrics = s.get('metrics', [])
        if len(metrics) != 3:
            errors.append(f'Slide {num} (metric) has {len(metrics)} metrics, expected 3')
    elif stype == 'poll':
        options = s.get('options', [])
        if len(options) != 4:
            errors.append(f'Slide {num} (poll) has {len(options)} options, expected 4')
            
    # Check speakers in script
    has_peter = '[Prof. Peter]' in script or '[Prof. Peter Kim]' in script
    has_sarah = '[TA Sarah]' in script or '[Sarah]' in script
    has_james = '[TA James]' in script or '[James]' in script
    
    if not (has_peter and has_sarah and has_james):
        speakers = []
        if has_peter: speakers.append('Peter')
        if has_sarah: speakers.append('Sarah')
        if has_james: speakers.append('James')
        warnings.append(f'Slide {num:02d} speakers present: {speakers}')
        
    # Check slide number reference in script
    num_str = f'Slide {num}'
    if num_str not in script and f'Slide {num:02d}' not in script:
        warnings.append(f'Slide {num:02d} script does not explicitly mention "Slide {num}"')
        
    # Check Korean Guide
    if not kg.get('summary'):
        errors.append(f'Slide {num} missing koreanGuide.summary')
    if not kg.get('points') or len(kg.get('points', [])) < 2:
        errors.append(f'Slide {num} missing koreanGuide.points')
    if not kg.get('tips'):
        errors.append(f'Slide {num} missing koreanGuide.tips')
        
    # Check Key Terms
    if not kt or len(kt) < 2:
        errors.append(f'Slide {num} has {len(kt)} keyTerms, expected at least 2')

print(f'\n--- PART SECTIONS ({len(part_section_slides)}) ---')
for p in part_section_slides:
    print(f'  Slide {p[0]:02d}: {p[1]}')

print(f'\n--- CASE STUDIES ({len(case_study_slides)}) ---')
for c in case_study_slides:
    print(f'  Slide {c[0]:02d}: {c[1]}')

print(f'\n--- VALIDATION SUMMARY ---')
print(f'Errors: {len(errors)}')
for e in errors:
    print(f'  ❌ ERROR: {e}')

print(f'Warnings/Notices: {len(warnings)}')
for w in warnings:
    print(f'  ⚠️ NOTICE: {w}')

print('\nAll 45 slides summary:')
for idx, s in enumerate(slides):
    num = s['num']
    stype = s['type']
    title = s['title']
    print(f'  [{num:02d}] ({stype:<12}) {title}')
