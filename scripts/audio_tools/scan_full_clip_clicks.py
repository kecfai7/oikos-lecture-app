import os
import sys
import numpy as np
import scipy.io.wavfile as wavfile
import subprocess
import imageio_ffmpeg
import json

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
from build_final_video import selected_mapping, files_dir

output_dir = r"c:\Oikos Univ\files_analysis"

print(f"{'Slide':<6} | {'Filename':<25} | {'Head Clicks':<12} | {'Mid Clicks':<12} | {'Tail Clicks':<12}")
print("-" * 75)

full_click_data = []

for s_num, fname in selected_mapping:
    fpath = os.path.join(files_dir, fname)
    temp_wav = os.path.join(output_dir, f"slide_{s_num:02d}.wav")
    
    sr, audio = wavfile.read(temp_wav)
    audio_float = audio.astype(np.float32) / 32768.0
    tot_len = len(audio_float)
    tot_dur = tot_len / sr
    
    diff = np.abs(np.diff(audio_float))
    thresh = 0.05
    
    head_len = min(int(2.0 * sr), tot_len)
    tail_len = min(int(2.0 * sr), tot_len)
    
    head_clicks = np.where(diff[:head_len] > thresh)[0]
    tail_clicks = np.where(diff[tot_len - tail_len:] > thresh)[0]
    mid_clicks = np.where(diff[head_len:tot_len - tail_len] > thresh)[0]
    
    print(f"Slide {s_num:02d} | {fname:<25} | {len(head_clicks):>12} | {len(mid_clicks):>12} | {len(tail_clicks):>12}")
    
    full_click_data.append({
        "slide": s_num,
        "filename": fname,
        "tot_dur": tot_dur,
        "head_count": len(head_clicks),
        "mid_count": len(mid_clicks),
        "tail_count": len(tail_clicks)
    })

with open(os.path.join(output_dir, "full_clicks.json"), "w", encoding="utf-8") as f:
    json.dump(full_click_data, f, indent=2, ensure_ascii=False)
