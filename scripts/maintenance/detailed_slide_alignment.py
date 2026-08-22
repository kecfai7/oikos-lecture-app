import os
import json
import re
from parse_slides import load_slides

slides = load_slides()

output_dir = r"c:\Oikos Univ\files_analysis"
with open(os.path.join(output_dir, "analysis_results.json"), "r", encoding="utf-8") as f:
    analysis = json.load(f)

# Map analysis by filename
analysis_map = {a["filename"]: a for a in analysis}

# Let's inspect slide numbers in scripts and transcripts
print(f"Total slides in Session 1: {len(slides)}")
print("=" * 120)

for s_num in sorted(slides.keys()):
    s_info = slides[s_num]
    s_title = s_info["title"]
    s_script = s_info["script"]
    
    # Find all candidate videos matching this slide
    candidates = []
    for a in analysis:
        # Check transcript
        txt = a["transcript"]
        score = a["score"]
        if a["best_slide"] == s_num:
            candidates.append(a)
        elif f"slide {s_num}" in txt.lower() or f"slide {s_num:02d}" in txt.lower():
            candidates.append(a)
    
    print(f"Slide {s_num:02d}: {s_title}")
    if not candidates:
        print("  ❌ NO CANDIDATE FOUND!")
    else:
        for c in candidates:
            print(f"  - [{c['filename']}] Dur: {c['duration']:>4.1f}s | Score: {c['score']:.3f} | Snippet: {c['transcript'][:60]}...")
    print("-" * 120)
