import os
import sys
import subprocess
import json
import imageio_ffmpeg
from parse_slides import load_slides

slides = load_slides()

files_dir = r"c:\Oikos Univ\files"
output_dir = r"c:\Oikos Univ\files_analysis"

selected_mapping = [
    (1, "2026-08-10 15-54-42.mp4"),
    (2, "2026-08-10 15-56-10.mp4"),
    (3, "2026-08-10 15-58-00.mp4"),
    (4, "2026-08-10 15-59-44.mp4"),
    (5, "2026-08-10 16-01-07.mp4"),
    (6, "2026-08-10 16-02-44.mp4"),
    (7, "2026-08-10 16-04-23.mp4"),
    (8, "2026-08-10 16-05-47.mp4"),
    (9, "2026-08-10 16-07-51.mp4"),
    (10, "2026-08-10 16-10-19.mp4"),
    (11, "2026-08-10 16-12-43.mp4"),
    (12, "2026-08-10 16-15-04.mp4"),
    (13, "2026-08-10 16-17-28.mp4"),
    (14, "2026-08-10 16-19-52.mp4"),
    (15, "2026-08-10 16-21-46.mp4"),
    (16, "2026-08-10 16-24-02.mp4"), # discarded 16-23-30
    (17, "2026-08-10 16-25-23.mp4"),
    (18, "2026-08-10 16-30-13.mp4"),
    (19, "2026-08-10 16-32-27.mp4"),
    (20, "2026-08-10 16-34-20.mp4"),
    (21, "2026-08-10 16-36-53.mp4"), # discarded 16-36-04
    (22, "2026-08-10 16-38-49.mp4"),
    (23, "2026-08-10 16-41-40.mp4"), # discarded 16-40-59
    (24, "2026-08-10 16-43-52.mp4"),
    (25, "2026-08-10 16-45-47.mp4"),
    (26, "2026-08-10 16-47-42.mp4"),
    (27, "2026-08-10 16-49-26.mp4"),
    (28, "2026-08-10 16-51-06.mp4"),
    (29, "2026-08-10 16-54-29.mp4"), # discarded 16-53-26
    (30, "2026-08-10 16-56-32.mp4"),
    (31, "2026-08-10 16-58-27.mp4"),
    (32, "2026-08-10 17-00-35.mp4"),
    (33, "2026-08-10 17-03-34.mp4"),
    (34, "2026-08-10 17-05-39.mp4"),
    (35, "2026-08-10 17-07-58.mp4"),
    (36, "2026-08-10 17-11-58.mp4"), # discarded 17-10-20
    (37, "2026-08-10 17-13-33.mp4"),
    (38, "2026-08-10 17-15-00.mp4"),
    (39, "2026-08-10 17-19-19.mp4"), # discarded 17-17-55
    (40, "2026-08-10 17-21-28.mp4"),
]

if __name__ == "__main__":
    print("Verifying selected files...")
    concat_file_content = []
    for s_num, fname in selected_mapping:
        fpath = os.path.join(files_dir, fname)
        if not os.path.exists(fpath):
            raise FileNotFoundError(f"File missing for Slide {s_num}: {fpath}")
        print(f"Slide {s_num:02d}: {fname} OK ({slides[s_num]['title'][:30]})")
        clean_path = fpath.replace("\\", "/")
        concat_file_content.append(f"file '{clean_path}'")

    concat_list_path = os.path.join(files_dir, "concat_list.txt")
    with open(concat_list_path, "w", encoding="utf-8") as f:
        f.write("\n".join(concat_file_content))

    print(f"\nWrote concat list to {concat_list_path}")

    output_video_path = os.path.join(files_dir, "Session1_Full_Lecture.mp4")
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

    cmd = [
        ffmpeg_exe,
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list_path,
        "-c", "copy",
        output_video_path
    ]

    print(f"Merging 40 video clips into {output_video_path}...")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if res.returncode == 0 and os.path.exists(output_video_path):
        stat = os.stat(output_video_path)
        print(f"SUCCESS! Master video created: {output_video_path}")
        print(f"Size: {stat.st_size / (1024*1024):.2f} MB")
    else:
        print("FAILED to merge videos!")
        print(res.stderr)
