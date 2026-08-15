import os
import json
import cv2

output_dir = r"c:\Oikos Univ\files_analysis"
with open(os.path.join(output_dir, "clicks_report.json"), "r", encoding="utf-8") as f:
    clicks = json.load(f)

with open(os.path.join(output_dir, "audio_bounds.json"), "r", encoding="utf-8") as f:
    bounds = json.load(f)

bounds_map = {b["filename"]: b for b in bounds}
clicks_map = {c["filename"]: c for c in clicks}

print(f"{'Slide':<6} | {'Filename':<25} | {'Orig Dur':<9} | {'Speech Start':<13} | {'Head Click':<11} | {'Trim Start':<11} | {'Speech End':<11} | {'Tail Click':<11} | {'Trim End':<9} | {'New Dur':<8}")
print("-" * 135)

trim_plan = []

for s_num, fname in [(b["slide"], b["filename"]) for b in bounds]:
    b = bounds_map[fname]
    c = clicks_map.get(fname, {})
    
    tot_dur = b["total_dur"]
    sp_start = b["speech_start"]
    sp_end = b["speech_end"]
    
    hc_time = c.get("head_click_time", 0.0)
    hc_peak = c.get("head_click_peak", 0.0)
    tc_time = c.get("tail_click_time", tot_dur)
    tc_peak = c.get("tail_click_peak", 0.0)
    
    # Determine Trim Start:
    # If head click is around hc_time < sp_start, we trim after hc_time + 0.05s
    # But leave at least 0.2s before speech start if possible
    if hc_peak > 0.04 and hc_time < sp_start:
        trim_start = min(sp_start, max(hc_time + 0.08, sp_start - 0.25))
    else:
        trim_start = max(0.0, sp_start - 0.25) if sp_start > 0.3 else 0.0
        
    # Determine Trim End:
    # If tail click is tc_time > sp_end, we trim before tc_time - 0.05s
    if tc_peak > 0.04 and tc_time > sp_end and tc_time < tot_dur:
        trim_end = max(sp_end, min(tc_time - 0.08, sp_end + 0.3))
    else:
        trim_end = min(tot_dur, sp_end + 0.3) if sp_end > 0 else tot_dur
        
    # Ensure trim_end > trim_start
    if trim_end <= trim_start:
        trim_start = 0.0
        trim_end = tot_dur
        
    new_dur = trim_end - trim_start
    
    print(f"Slide {s_num:02d} | {fname:<25} | {tot_dur:>7.2f}s | {sp_start:>11.2f}s | {hc_time:>9.2f}s | {trim_start:>9.2f}s | {sp_end:>9.2f}s | {tc_time:>9.2f}s | {trim_end:>7.2f}s | {new_dur:>6.2f}s")
    
    trim_plan.append({
        "slide": s_num,
        "filename": fname,
        "orig_dur": tot_dur,
        "trim_start": round(trim_start, 3),
        "trim_end": round(trim_end, 3),
        "new_dur": round(new_dur, 3)
    })

with open(os.path.join(output_dir, "trim_plan.json"), "w", encoding="utf-8") as f:
    json.dump(trim_plan, f, indent=2, ensure_ascii=False)
