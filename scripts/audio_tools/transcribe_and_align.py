import os
import sys
import glob
import re
import json
from difflib import SequenceMatcher

def extract_slides_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract SLIDES_SESSION_1 block
    match = re.search(r'export const SLIDES_SESSION_1 = \[(.*?)\n\];', content, re.DOTALL)
    if not match:
        print("Could not find SLIDES_SESSION_1")
        return []
    
    # Simple regex extraction for slide num, title, script
    slide_blocks = re.findall(r'\{\s*num:\s*(\d+),.*?"title":\s*"(.*?)",.*?script:\s*`(.*?)`', content, re.DOTALL)
    
    slides = []
    for num, title, script in slide_blocks:
        slides.append({
            "num": int(num),
            "title": title.strip(),
            "script": script.strip()
        })
    return slides

print("Script template ready.")
