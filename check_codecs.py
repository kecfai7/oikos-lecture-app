import os
import sys
import glob
import re
import subprocess
import json
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

files_dir = r"c:\Oikos Univ\files"
mp4_files = sorted(glob.glob(os.path.join(files_dir, "*.mp4")))

print("Checking video formats for concatenation...")
sample_meta = []

for idx, f in enumerate(mp4_files):
    cmd = [ffmpeg_exe, "-i", f]
    res = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    err = res.stderr
    
    res_match = re.search(r'Video:.*?, (\d+x\d+)', err)
    fps_match = re.search(r'(\d+(?:\.\d+)?) fps', err)
    audio_match = re.search(r'Audio:.*?, (\d+) Hz', err)
    
    sample_meta.append({
        "file": os.path.basename(f),
        "video": res_match.group(1) if res_match else "unknown",
        "fps": fps_match.group(1) if fps_match else "unknown",
        "audio": audio_match.group(1) if audio_match else "unknown"
    })

# Check if all formats match
videos = set(m["video"] for m in sample_meta)
fpss = set(m["fps"] for m in sample_meta)
audios = set(m["audio"] for m in sample_meta)

print(f"Unique Video Resolutions: {videos}")
print(f"Unique Frame Rates: {fpss}")
print(f"Unique Audio Rates: {audios}")
