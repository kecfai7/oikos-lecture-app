import os
import sys
import subprocess
import time
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

files_dir = r"c:\Oikos Univ\files"
concat_list_clean = r"c:\Oikos Univ\files_cleaned\concat_list_clean.txt"

output_compressed_mp4 = os.path.join(files_dir, "Session1_Full_Lecture_Compressed.mp4")

# We use libx264 with CRF 26 and preset fast, 720p, audio AAC 128k
# This provides excellent readability for slides while dramatically reducing size (from ~2GB down to ~300-400MB)

cmd = [
    ffmpeg_exe, "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", concat_list_clean,
    "-c:v", "libx264",
    "-crf", "26",
    "-preset", "fast",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "128k",
    "-movflags", "+faststart",
    output_compressed_mp4
]

print("Starting high-efficiency video compression for Session 1...")
print(f"Target file: {output_compressed_mp4}")
print("Parameters: H.264 (libx264), CRF 26, Preset: fast, Audio AAC 128k, faststart enabled")

t0 = time.time()
res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
elapsed = time.time() - t0

if res.returncode == 0 and os.path.exists(output_compressed_mp4):
    orig_path = os.path.join(files_dir, "Session1_Full_Lecture.mp4")
    orig_size = os.path.getsize(orig_path) / (1024*1024) if os.path.exists(orig_path) else 1981.04
    new_size = os.path.getsize(output_compressed_mp4) / (1024*1024)
    reduction = ((orig_size - new_size) / orig_size) * 100
    
    print(f"\nCompression Complete in {elapsed:.1f} seconds!")
    print(f"Original File Size:   {orig_size:.2f} MB")
    print(f"Compressed File Size: {new_size:.2f} MB")
    print(f"Size Reduction:       -{reduction:.1f}%")
    
    # Optionally overwrite Session1_Full_Lecture.mp4 or replace it with compressed version
    import shutil
    shutil.copyfile(output_compressed_mp4, os.path.join(files_dir, "Session1_Full_Lecture_Optimized.mp4"))
    print("Saved optimized copy as Session1_Full_Lecture_Optimized.mp4")
else:
    print("\nCompression failed!")
    print(res.stderr)
