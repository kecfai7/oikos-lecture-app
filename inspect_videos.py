import os
import sys
import glob
import cv2
import json

files_dir = r"c:\Oikos Univ\files"
output_dir = r"c:\Oikos Univ\files_analysis"
os.makedirs(output_dir, exist_ok=True)

mp4_files = sorted(glob.glob(os.path.join(files_dir, "*.mp4")))
print(f"Total MP4 files found: {len(mp4_files)}")

results = []

for idx, filepath in enumerate(mp4_files):
    fname = os.path.basename(filepath)
    stat = os.stat(filepath)
    
    cap = cv2.VideoCapture(filepath)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    duration = frame_count / fps if fps > 0 else 0
    
    # Save a middle frame
    middle_frame_idx = frame_count // 2
    cap.set(cv2.CAP_PROP_POS_FRAMES, middle_frame_idx)
    ret, frame = cap.read()
    img_path = os.path.join(output_dir, f"{idx:02d}_{os.path.splitext(fname)[0]}.jpg")
    if ret:
        cv2.imwrite(img_path, frame)
    
    cap.release()
    
    info = {
        "index": idx,
        "filename": fname,
        "size_bytes": stat.st_size,
        "mtime": stat.st_mtime,
        "duration_sec": round(duration, 2),
        "resolution": f"{width}x{height}",
        "fps": round(fps, 2),
        "frame_image": img_path
    }
    results.append(info)
    print(f"[{idx+1}/{len(mp4_files)}] {fname}: {duration:.1f}s, {width}x{height}")

with open(os.path.join(output_dir, "metadata.json"), "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("Saved initial metadata to metadata.json")
