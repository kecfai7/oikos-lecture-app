import os
import sys
import glob
import json
import time
import imageio_ffmpeg
import whisper

# Add imageio_ffmpeg path to PATH so whisper can invoke ffmpeg subprocess
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
ffmpeg_dir = os.path.dirname(ffmpeg_exe)
# Also create ffmpeg.exe alias if needed
target_ffmpeg = os.path.join(ffmpeg_dir, "ffmpeg.exe")
if not os.path.exists(target_ffmpeg):
    import shutil
    shutil.copyfile(ffmpeg_exe, target_ffmpeg)

os.environ["PATH"] = ffmpeg_dir + os.path.pathsep + os.environ.get("PATH", "")

files_dir = r"c:\Oikos Univ\files"
output_dir = r"c:\Oikos Univ\files_analysis"
os.makedirs(output_dir, exist_ok=True)

mp4_files = sorted(glob.glob(os.path.join(files_dir, "*.mp4")))
print(f"Loading Whisper model ('tiny.en')...")
model = whisper.load_model("tiny.en")

transcripts = {}
json_path = os.path.join(output_dir, "transcripts.json")

if os.path.exists(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        transcripts = json.load(f)

for idx, filepath in enumerate(mp4_files):
    fname = os.path.basename(filepath)
    if fname in transcripts:
        print(f"[{idx+1}/{len(mp4_files)}] Skipping (already transcribed): {fname}")
        continue
    
    t0 = time.time()
    print(f"[{idx+1}/{len(mp4_files)}] Transcribing {fname}...", end="", flush=True)
    res = model.transcribe(filepath, fp16=False)
    text = res.get("text", "").strip()
    elapsed = time.time() - t0
    print(f" done ({elapsed:.1f}s): {text[:60]}...")
    
    transcripts[fname] = {
        "text": text,
        "segments": res.get("segments", [])
    }
    
    # Save incrementally
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(transcripts, f, indent=2, ensure_ascii=False)

print("Transcription complete!")
