import os
import sys
import glob
import json
import cv2
from parse_slides import load_slides

output_dir = r"c:\Oikos Univ\files_analysis"
transcripts_path = os.path.join(output_dir, "transcripts.json")

with open(transcripts_path, "r", encoding="utf-8") as f:
    transcripts = json.load(f)

from build_final_video import selected_mapping, files_dir

print(f"{'Slide':<6} | {'Filename':<25} | {'Dur':<6} | {'Speech Start':<12} | {'Speech End':<12} | {'Leading (s)':<11} | {'Trailing (s)':<11}")
print("-" * 105)

summary_data = []

for s_num, fname in selected_mapping:
    fpath = os.path.join(files_dir, fname)
    t_data = transcripts.get(fname, {})
    segments = t_data.get("segments", [])
    
    if segments:
        speech_start = segments[0]["start"]
        speech_end = segments[-1]["end"]
    else:
        speech_start = 0.0
        speech_end = 0.0
        
    cap = cv2.VideoCapture(fpath)
    fps = cap.get(cv2.CAP_PROP_FPS)
    fc = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    tot_dur = fc / fps if fps > 0 else 0.0
    cap.release()
        
    leading_pad = speech_start
    trailing_pad = max(0.0, tot_dur - speech_end)
    
    print(f"Slide {s_num:02d} | {fname:<25} | {tot_dur:>6.2f}s | {speech_start:>10.2f}s | {speech_end:>10.2f}s | {leading_pad:>10.2f}s | {trailing_pad:>10.2f}s")
    
    summary_data.append({
        "slide": s_num,
        "filename": fname,
        "total_dur": round(tot_dur, 3),
        "speech_start": round(speech_start, 3),
        "speech_end": round(speech_end, 3),
        "leading_pad": round(leading_pad, 3),
        "trailing_pad": round(trailing_pad, 3)
    })

with open(os.path.join(output_dir, "audio_bounds.json"), "w", encoding="utf-8") as f:
    json.dump(summary_data, f, indent=2, ensure_ascii=False)
