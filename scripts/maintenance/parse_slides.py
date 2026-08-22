import re
import json

def load_slides():
    with open(r"c:\Oikos Univ\src\data\slidesData.js", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Match SLIDES_SESSION_1
    start_marker = "export const SLIDES_SESSION_1 = ["
    start_pos = content.find(start_marker)
    if start_pos == -1:
        raise ValueError("Could not find SLIDES_SESSION_1")
    
    end_marker = "\n];"
    end_pos = content.find(end_marker, start_pos)
    block = content[start_pos + len(start_marker):end_pos]
    
    # Split by slide objects: { num: ... }
    slide_objs = []
    # Pattern to find each slide dictionary structure
    # We can match num, title, script
    pattern = r'num:\s*(\d+).*?title:\s*"(.*?)".*?script:\s*`(.*?)`'
    matches = re.findall(pattern, block, re.DOTALL)
    
    slides = {}
    for num, title, script in matches:
        slides[int(num)] = {
            "num": int(num),
            "title": title.strip(),
            "script": script.strip()
        }
    return slides

if __name__ == "__main__":
    s = load_slides()
    print(f"Loaded {len(s)} slides.")
    for num in sorted(s.keys()):
        print(f"Slide {num:02d}: {s[num]['title']} | Script len: {len(s[num]['script'])}")
