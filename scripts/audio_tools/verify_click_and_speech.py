import os
import json

output_dir = r"c:\Oikos Univ\files_analysis"
with open(os.path.join(output_dir, "clicks_report.json"), "r", encoding="utf-8") as f:
    clicks = json.load(f)

with open(os.path.join(output_dir, "audio_bounds.json"), "r", encoding="utf-8") as f:
    bounds = json.load(f)

bounds_map = {b["filename"]: b for b in bounds}

print(f"{'Slide':<6} | {'Head Click (s)':<14} | {'Speech Start (s)':<16} | {'Speech End (s)':<14} | {'Tail Click (s)':<14} | {'Tot Dur (s)':<12}")
print("-" * 90)

for c in clicks:
    b = bounds_map.get(c["filename"], {})
    s_num = c["slide"]
    hc_time = c["head_click_time"]
    tc_time = c["tail_click_time"]
    sp_start = b.get("speech_start", 0.0)
    sp_end = b.get("speech_end", 0.0)
    tot_dur = c["tot_dur"]
    
    print(f"Slide {s_num:02d} | {hc_time:>12.3f}s | {sp_start:>14.3f}s | {sp_end:>12.3f}s | {tc_time:>12.3f}s | {tot_dur:>10.2f}s")
