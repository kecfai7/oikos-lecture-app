import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Oikos Univ\src\data\slidesData.js', 'r', encoding='utf-8') as f:
    js_text = f.read()

m = re.search(r'export const SLIDES_SESSION_1 = (\[[\s\S]*?\n\]);', js_text)
slides = json.loads(m.group(1))

for s in slides:
    num = s.get('num')
    stype = s.get('type')
    title = s.get('title')
    has_cards = 'cards' in s
    has_left = 'leftCard' in s
    has_steps = 'steps' in s
    has_points = 'points' in s
    has_stat = 'stat' in s
    has_poll = 'poll' in s or stype == 'poll'
    print(f"Slide {num:02d} | Type: {stype:<12} | Title: {title[:40]:<40} | cards:{has_cards} left/right:{has_left} steps:{has_steps} points:{has_points} stat:{has_stat}")
