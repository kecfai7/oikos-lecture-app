import os
import sys
import glob
import json
import re
from difflib import SequenceMatcher
from parse_slides import load_slides

slides = load_slides()

output_dir = r"c:\Oikos Univ\files_analysis"
transcripts_path = os.path.join(output_dir, "transcripts.json")
metadata_path = os.path.join(output_dir, "metadata.json")

if not os.path.exists(transcripts_path):
    print("transcripts.json not ready yet.")
    sys.exit(0)

with open(transcripts_path, "r", encoding="utf-8") as f:
    transcripts = json.load(f)

with open(metadata_path, "r", encoding="utf-8") as f:
    meta_list = json.load(f)
    meta_map = {m["filename"]: m for m in meta_list}

def clean_text(t):
    return re.sub(r'[^a-zA-Z0-9\s]', ' ', t).lower()

analysis = []

for fname, data in transcripts.items():
    text = data["text"]
    c_text = clean_text(text)
    meta = meta_map.get(fname, {})
    duration = meta.get("duration_sec", 0)
    
    best_num = None
    best_score = -1.0
    best_slide_title = ""
    
    words_text = set(c_text.split())
    
    for num, sdata in slides.items():
        s_script = clean_text(sdata["script"])
        words_script = set(s_script.split())
        
        if not words_text or not words_script:
            overlap = 0.0
        else:
            overlap = len(words_text.intersection(words_script)) / max(len(words_script), 1)
        
        # Also check sequence matcher
        ratio = SequenceMatcher(None, c_text, s_script).ratio()
        
        score = overlap * 0.7 + ratio * 0.3
        
        # Give bonus if slide number or title keywords match
        slide_num_match = re.search(r'slide\s*(\d+)', c_text)
        if slide_num_match and int(slide_num_match.group(1)) == num:
            score += 0.2
            
        if score > best_score:
            best_score = score
            best_num = num
            best_slide_title = sdata["title"]
            
    analysis.append({
        "filename": fname,
        "mtime": meta.get("mtime", 0),
        "duration": duration,
        "best_slide": best_num,
        "slide_title": best_slide_title,
        "score": round(best_score, 3),
        "transcript": text
    })

# Sort by filename (timestamp order)
analysis.sort(key=lambda x: x["filename"])

print(f"{'Idx':<4} | {'Filename':<25} | {'Slide':<5} | {'Dur(s)':<6} | {'Score':<5} | {'Transcript Snippet'}")
print("-" * 110)
for idx, a in enumerate(analysis):
    print(f"{idx+1:<4} | {a['filename']:<25} | Slide {a['best_slide']:<2} | {a['duration']:<6.1f} | {a['score']:<5.3f} | {a['transcript'][:45]}...")

with open(os.path.join(output_dir, "analysis_results.json"), "w", encoding="utf-8") as f:
    json.dump(analysis, f, indent=2, ensure_ascii=False)
