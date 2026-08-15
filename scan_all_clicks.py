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
os.makedirs(output_dir, exist_ok=True)

click_report = []

print(f"{'Slide':<6} | {'Filename':<25} | {'Head Click Peak':<16} | {'Head Click Time':<16} | {'Tail Click Peak':<16} | {'Tail Click Time':<16}")
print("-" * 110)

for s_num, fname in selected_mapping:
    fpath = os.path.join(files_dir, fname)
    temp_wav = os.path.join(output_dir, f"slide_{s_num:02d}.wav")
    
    # Extract mono WAV 48kHz
    cmd = [
        ffmpeg_exe, "-y",
        "-i", fpath,
        "-vn",
        "-ac", "1",
        "-ar", "48000",
        "-acodec", "pcm_s16le",
        temp_wav
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    sr, audio = wavfile.read(temp_wav)
    audio_float = audio.astype(np.float32) / 32768.0
    tot_len = len(audio_float)
    tot_dur = tot_len / sr
    
    # Head window (first 1.5s)
    head_samples = min(int(1.5 * sr), tot_len)
    head = audio_float[:head_samples]
    head_diff = np.abs(np.diff(head))
    head_max_diff_idx = np.argmax(head_diff) if len(head_diff) > 0 else 0
    head_click_peak = head_diff[head_max_diff_idx] if len(head_diff) > 0 else 0.0
    head_click_time = head_max_diff_idx / sr
    
    # Tail window (last 2.0s)
    tail_samples = min(int(2.0 * sr), tot_len)
    tail = audio_float[tot_len - tail_samples:]
    tail_diff = np.abs(np.diff(tail))
    tail_max_diff_idx = np.argmax(tail_diff) if len(tail_diff) > 0 else 0
    tail_click_peak = tail_diff[tail_max_diff_idx] if len(tail_diff) > 0 else 0.0
    tail_click_time = tot_dur - 2.0 + (tail_max_diff_idx / sr)
    
    print(f"Slide {s_num:02d} | {fname:<25} | {head_click_peak:>16.4f} | {head_click_time:>14.3f}s | {tail_click_peak:>16.4f} | {tail_click_time:>14.3f}s")
    
    click_report.append({
        "slide": s_num,
        "filename": fname,
        "tot_dur": tot_dur,
        "head_click_peak": float(head_click_peak),
        "head_click_time": float(head_click_time),
        "tail_click_peak": float(tail_click_peak),
        "tail_click_time": float(tail_click_time)
    })

with open(os.path.join(output_dir, "clicks_report.json"), "w", encoding="utf-8") as f:
    json.dump(click_report, f, indent=2, ensure_ascii=False)
