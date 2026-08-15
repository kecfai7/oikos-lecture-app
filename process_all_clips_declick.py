import os
import sys
import numpy as np
import scipy.io.wavfile as wavfile
import subprocess
import imageio_ffmpeg
import json
from build_final_video import selected_mapping, files_dir

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

output_dir = r"c:\Oikos Univ\files_cleaned"
os.makedirs(output_dir, exist_ok=True)

cleaned_clips = []
concat_lines = []

print("Processing all 40 clips to eliminate mouse click noises...")
print("=" * 110)

total_clicks_removed = 0

for s_num, fname in selected_mapping:
    src_mp4 = os.path.join(files_dir, fname)
    temp_wav = os.path.join(output_dir, f"temp_{s_num:02d}.wav")
    clean_wav = os.path.join(output_dir, f"clean_{s_num:02d}.wav")
    out_mp4 = os.path.join(output_dir, f"slide_{s_num:02d}_clean.mp4")
    
    # 1. Extract audio to 48kHz WAV
    cmd_extract = [
        ffmpeg_exe, "-y",
        "-i", src_mp4,
        "-vn",
        "-ac", "1",
        "-ar", "48000",
        "-acodec", "pcm_s16le",
        temp_wav
    ]
    subprocess.run(cmd_extract, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # 2. Load audio and detect click spikes
    sr, audio = wavfile.read(temp_wav)
    audio_float = audio.astype(np.float32) / 32768.0
    tot_len = len(audio_float)
    tot_dur = tot_len / sr
    
    clean_audio = audio_float.copy()
    diff = np.abs(np.diff(clean_audio))
    thresh = 0.04
    
    head_len = min(int(2.0 * sr), tot_len)
    tail_len = min(int(2.5 * sr), tot_len)
    
    head_indices = np.where(diff[:head_len] > thresh)[0]
    tail_indices = np.where(diff[tot_len - tail_len:] > thresh)[0] + (tot_len - tail_len)
    
    click_indices = np.concatenate([head_indices, tail_indices])
    
    # Group click indices into windows to mute
    muted_count = 0
    if len(click_indices) > 0:
        # Cluster indices into ranges
        click_times = click_indices / sr
        # Mute 25ms around click spikes
        for idx in click_indices:
            w_start = max(0, idx - int(0.012 * sr))
            w_end = min(tot_len, idx + int(0.012 * sr))
            clean_audio[w_start:w_end] = 0.0
            muted_count += 1
            
    # Apply 40ms head fade-in & 40ms tail fade-out
    fade_samples = int(0.04 * sr)
    if tot_len > 2 * fade_samples:
        clean_audio[:fade_samples] *= np.linspace(0.0, 1.0, fade_samples)
        clean_audio[-fade_samples:] *= np.linspace(1.0, 0.0, fade_samples)
        
    # 3. Write clean WAV
    clean_pcm = np.clip(clean_audio * 32767.0, -32768, 32767).astype(np.int16)
    wavfile.write(clean_wav, sr, clean_pcm)
    
    # 4. Mux video from src_mp4 with clean_wav audio into out_mp4
    cmd_mux = [
        ffmpeg_exe, "-y",
        "-i", src_mp4,
        "-i", clean_wav,
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k",
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-shortest",
        out_mp4
    ]
    subprocess.run(cmd_mux, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    total_clicks_removed += muted_count
    print(f"Slide {s_num:02d} | {fname:<25} | Dur: {tot_dur:>6.2f}s | Click spikes muted: {muted_count:>4} | Cleaned -> {os.path.basename(out_mp4)}")
    
    cleaned_clips.append(out_mp4)
    clean_path_fmt = out_mp4.replace("\\", "/")
    concat_lines.append(f"file '{clean_path_fmt}'")

# Write concat list for cleaned files
concat_list_clean = os.path.join(output_dir, "concat_list_clean.txt")
with open(concat_list_clean, "w", encoding="utf-8") as f:
    f.write("\n".join(concat_lines))

print("=" * 110)
print(f"All 40 clips processed! Total click spikes removed: {total_clicks_removed}")
print(f"Clean concat list saved: {concat_list_clean}")

# 5. Merge all cleaned clips into final master video
final_master_path = r"c:\Oikos Univ\files\Session1_Full_Lecture.mp4"

cmd_concat = [
    ffmpeg_exe, "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", concat_list_clean,
    "-c", "copy",
    final_master_path
]

print(f"Merging cleaned clips into master video: {final_master_path}...")
res = subprocess.run(cmd_concat, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

if res.returncode == 0 and os.path.exists(final_master_path):
    stat = os.stat(final_master_path)
    print(f"SUCCESS! Clean master video generated successfully!")
    print(f"File size: {stat.st_size / (1024*1024):.2f} MB")
else:
    print("FAILED to concat cleaned clips!")
    print(res.stderr)
