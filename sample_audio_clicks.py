import os
import sys
import numpy as np
import scipy.io.wavfile as wavfile
import subprocess
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
files_dir = r"c:\Oikos Univ\files"
temp_wav = r"c:\Oikos Univ\files_analysis\sample_clip.wav"

# Let's inspect slide 1, slide 36, slide 40 audio
sample_file = os.path.join(files_dir, "2026-08-10 17-11-58.mp4") # Slide 36

# Extract audio as WAV 48kHz 16-bit mono
cmd = [
    ffmpeg_exe, "-y",
    "-i", sample_file,
    "-vn",
    "-ac", "1",
    "-ar", "48000",
    "-acodec", "pcm_s16le",
    temp_wav
]
subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

sr, audio = wavfile.read(temp_wav)
audio_float = audio.astype(np.float32) / 32768.0

print(f"Sample rate: {sr}, total samples: {len(audio)}, duration: {len(audio)/sr:.2f}s")

# Inspect first 1.5 seconds and last 2.5 seconds
head = audio_float[:int(1.5*sr)]
tail = audio_float[-int(2.5*sr):]

print(f"Head max peak: {np.max(np.abs(head)):.4f}")
print(f"Tail max peak: {np.max(np.abs(tail)):.4f}")

# Find sharp spikes (diff of audio)
head_diff = np.abs(np.diff(head))
tail_diff = np.abs(np.diff(tail))

print(f"Head max diff: {np.max(head_diff):.4f}")
print(f"Tail max diff: {np.max(tail_diff):.4f}")
