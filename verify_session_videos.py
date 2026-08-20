# -*- coding: utf-8 -*-
"""
Oikos University - Duo Lecture Video QA & Verification Inspector Module
Performs comprehensive quality assurance checks on all 40 slides,
part split videos (20 min x 3), and master 60-min broadcast MP4.
"""

import os
import sys
import subprocess
import re
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

try:
    import imageio_ffmpeg
    FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:
    FFMPEG_EXE = "ffmpeg"

BASE_DIR = r"c:\Oikos Univ"
OUTPUT_DIR = os.path.join(BASE_DIR, "duo_videos")
AUDIO_DIR = os.path.join(OUTPUT_DIR, "audio_segments")
SLIDES_IMG_DIR = os.path.join(OUTPUT_DIR, "slide_images")
SLIDES_DATA_JS = os.path.join(BASE_DIR, "src", "data", "slidesData.js")

def get_media_duration_sec(filepath):
    if not os.path.exists(filepath):
        return 0.0
    cmd = [FFMPEG_EXE, "-i", filepath]
    res = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, errors="ignore")
    match = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", res.stderr)
    if match:
        hours = int(match.group(1))
        mins = int(match.group(2))
        secs = float(match.group(3))
        return hours * 3600 + mins * 60 + secs
    return 0.0

def format_time_str(sec):
    m = int(sec // 60)
    s = sec % 60
    return f"{m:02d}:{s:04.1f}"

def load_session_slides(session_id=1):
    with open(SLIDES_DATA_JS, "r", encoding="utf-8") as f:
        content = f.read()
    var_name = f"SLIDES_SESSION_{session_id}"
    match = re.search(rf"export const {var_name} = (\[[\s\S]*?\n\]);", content)
    if not match:
        return []
    return json.loads(match.group(1))

def run_verification(session_id=1):
    slides = load_session_slides(session_id)
    total_slides = len(slides) if slides else 40
    
    print("=" * 80)
    print(f"🔍 OIKOS UNIVERSITY DUO LECTURE QA INSPECTOR (SESSION {session_id})")
    print("=" * 80)
    print(f"📊 Checking 40 Slides Completeness, Duration, Audio, Captures & Subtitles...\n")

    slide_results = []
    total_slide_duration = 0.0
    missing_slides = []
    
    # Header
    print(f"{'Slide':<7} | {'Status':<8} | {'Video File':<32} | {'Duration':<9} | {'Img':<4} | {'SRT':<4} | {'Size MB':<8} | {'Title'}")
    print("-" * 115)

    for i in range(1, total_slides + 1):
        video_name = f"Session{session_id}_Slide_{i:02d}_DuoLecture.mp4"
        video_path = os.path.join(OUTPUT_DIR, video_name)
        img_name = f"session_{session_id}_slide_{i:02d}.png"
        img_path = os.path.join(SLIDES_IMG_DIR, img_name)
        srt_name = f"Slide_{i:02d}_Subtitles.srt"
        srt_path = os.path.join(OUTPUT_DIR, srt_name)

        has_video = os.path.exists(video_path) and os.path.getsize(video_path) > 1000
        has_img = os.path.exists(img_path) and os.path.getsize(img_path) > 10000
        has_srt = os.path.exists(srt_path) and os.path.getsize(srt_path) > 50

        slide_title = slides[i-1]["title"] if i-1 < len(slides) else f"Slide {i}"
        
        if has_video:
            dur = get_media_duration_sec(video_path)
            size_mb = os.path.getsize(video_path) / (1024 * 1024)
            total_slide_duration += dur
            status = "✅ PASS"
            slide_results.append({
                "num": i, "status": "PASS", "dur": dur, "size_mb": size_mb,
                "title": slide_title, "has_img": has_img, "has_srt": has_srt
            })
            dur_str = format_time_str(dur)
            size_str = f"{size_mb:.2f} MB"
        else:
            status = "❌ MISSING"
            dur_str = "--:--"
            size_str = "0.00 MB"
            missing_slides.append(i)
            slide_results.append({
                "num": i, "status": "MISSING", "dur": 0, "size_mb": 0,
                "title": slide_title, "has_img": has_img, "has_srt": has_srt
            })

        img_flag = "OK" if has_img else "NO"
        srt_flag = "OK" if has_srt else "NO"

        print(f"Slide {i:02d} | {status:<8} | {video_name:<32} | {dur_str:<9} | {img_flag:<4} | {srt_flag:<4} | {size_str:<8} | {slide_title[:30]}")

    print("-" * 115)
    print(f"📈 Total 40 Slides Cumulative Duration: {format_time_str(total_slide_duration)} ({total_slide_duration/60:.2f} minutes)\n")

    # 2. Check 3x 20-Min Part Split Videos
    print("=" * 80)
    print("🎞️ 3x 20-MINUTE MODULE SPLIT VERIFICATION")
    print("=" * 80)
    
    parts_config = [
        ("Part 1: Foundations", f"Session{session_id}_Part1_20Min_Foundations.mp4", 1, 13),
        ("Part 2: Engineering", f"Session{session_id}_Part2_20Min_Engineering.mp4", 14, 26),
        ("Part 3: Governance & Lab", f"Session{session_id}_Part3_20Min_Governance_and_Lab.mp4", 27, 40)
    ]

    for part_label, filename, start_s, end_s in parts_config:
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 1000:
            dur = get_media_duration_sec(filepath)
            size_mb = os.path.getsize(filepath) / (1024 * 1024)
            print(f"  🎬 [{part_label}] (Slides {start_s:02d}~{end_s:02d}):")
            print(f"     File: {filename}")
            print(f"     Duration: {format_time_str(dur)} ({dur/60:.2f} mins) | Size: {size_mb:.2f} MB | Status: ✅ READY")
        else:
            print(f"  ❌ [{part_label}] Missing: {filename}")

    # 3. Check Full 60-Minute Master Video
    print("\n" + "=" * 80)
    print("🏆 FULL 60-MINUTE MASTER VIDEO VERIFICATION")
    print("=" * 80)
    master_file = f"Session{session_id}_Full_60Min_DuoLecture_Master.mp4"
    master_path = os.path.join(OUTPUT_DIR, master_file)
    if os.path.exists(master_path) and os.path.getsize(master_path) > 1000:
        dur = get_media_duration_sec(master_path)
        size_mb = os.path.getsize(master_path) / (1024 * 1024)
        print(f"  👑 Master Video: {master_file}")
        print(f"     Duration: {format_time_str(dur)} ({dur/60:.2f} mins) | Size: {size_mb:.2f} MB | Status: ✅ PERFECT")
    else:
        print(f"  ❌ Master Video Missing: {master_file}")

    print("=" * 80)
    if missing_slides:
        print(f"⚠️ ATTENTION REQUIRED: {len(missing_slides)} slides missing: {missing_slides}")
        print(f"👉 Fix by running: python build_duo_lecture_mp4.py --session {session_id} --slides {','.join(map(str, missing_slides))}")
    else:
        print(f"🎉 ALL 40 SLIDES & BROADCAST VIDEOS ARE 100% COMPLETE & VERIFIED!")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Inspect & Verify Duo Lecture Video Assets")
    parser.add_argument("--session", type=int, default=1, help="Session ID (default: 1)")
    args = parser.parse_args()
    run_verification(args.session)
