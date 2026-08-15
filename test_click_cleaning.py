import os
import sys
import numpy as np
import scipy.io.wavfile as wavfile
import subprocess
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
files_dir = r"c:\Oikos Univ\files"
output_dir = r"c:\Oikos Univ\files_analysis"

sample_file = os.path.join(files_dir, "2026-08-10 17-11-58.mp4") # Slide 36
orig_wav = os.path.join(output_dir, "orig_slide36.wav")
clean_wav = os.path.join(output_dir, "clean_slide36.wav")

# Extract mono WAV 48kHz
cmd = [
    ffmpeg_exe, "-y",
    "-i", sample_file,
    "-vn",
    "-ac", "1",
    "-ar", "48000",
    "-acodec", "pcm_s16le",
    orig_wav
]
subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

sr, audio = wavfile.read(orig_wav)
audio_float = audio.astype(np.float32) / 32768.0
tot_len = len(audio_float)

clean_audio = audio_float.copy()

# De-click algorithm:
# 1. Detect transient click spikes using derivative threshold
diff = np.abs(np.diff(clean_audio))
# Threshold for click impulse derivative
thresh = 0.05

# In head (0 to 1.8s) and tail (last 2.0s), replace spikes with silence or smooth interpolation
head_samples = int(1.8 * sr)
tail_samples = int(2.0 * sr)

head_indices = np.where(diff[:head_samples] > thresh)[0]
tail_indices = np.where(diff[tot_len - tail_samples:] > thresh)[0] + (tot_len - tail_samples)

click_indices = np.concatenate([head_indices, tail_indices])

print(f"Detected {len(click_indices)} click spike samples in head/tail regions.")

# Mute 30ms around click spikes in head/tail regions
for idx in click_indices:
    win_start = max(0, idx - int(0.015 * sr))
    win_end = min(tot_len, idx + int(0.015 * sr))
    # Apply fade out/in over the 30ms window
    window_len = win_end - win_start
    if window_len > 0:
        clean_audio[win_start:win_end] *= 0.0

# Apply 50ms fade-in at very start and 50ms fade-out at very end
fade_len = int(0.05 * sr)
clean_audio[:fade_len] *= np.linspace(0.0, 1.0, fade_len)
clean_audio[-fade_len:] *= np.linspace(1.0, 0.0, fade_len)

# Save cleaned wav
clean_pcm = np.clip(clean_audio * 32767.0, -32768, 32767).astype(np.int16)
wavfile.write(clean_wav, sr, clean_pcm)

# Check peak diff after cleaning
clean_diff = np.abs(np.diff(clean_audio[:head_samples]))
print(f"Original head click peak diff: {np.max(diff[:head_samples]):.4f}")
print(f"Cleaned head click peak diff:  {np.max(clean_diff):.4f}")
