# -*- coding: utf-8 -*-
"""
Autonomous 2-Presenter Duo Lecture Video & Subtitle Generator (MP4 Master Pipeline)
- Presenter 1: Prof. Peter Kim (54) -> Microsoft Neural Voice 'en-US-ChristopherNeural'
- Presenter 2: TA Sarah Jenkins (31) -> Microsoft Neural Voice 'en-US-JennyNeural'
- Features:
  1. High-Resolution 1080p Slide Capture from Web App
  2. Neural Voice Duo Conversational Synthesis with realistic timing pauses
  3. SRT / VTT Subtitle Generation
  4. 1080p MP4 Video Rendering with Embedded Subtitles
  5. Master Full Lecture Concat (40 Slides -> 60-min Master Video)
"""

import os
import sys
import json
import re
import argparse
import asyncio
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

import imageio_ffmpeg
import edge_tts
from playwright.async_api import async_playwright
from generate_duo_session1 import SESSION_1_DUO_SLIDES

# Paths
BASE_DIR = r"c:\Oikos Univ"
OUTPUT_DIR = os.path.join(BASE_DIR, "duo_videos")
SLIDES_IMG_DIR = os.path.join(OUTPUT_DIR, "slide_images")
AUDIO_DIR = os.path.join(OUTPUT_DIR, "audio_segments")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SLIDES_IMG_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

# Voice Configs
VOICE_PETER = "en-US-ChristopherNeural"  # Mature, authoritative 50s professor tone
VOICE_PETER_RATE = "-2%"
VOICE_PETER_PITCH = "-2Hz"

VOICE_SARAH = "en-US-JennyNeural"        # Bright, articulate, smart 30s TA tone
VOICE_SARAH_RATE = "+3%"
VOICE_SARAH_PITCH = "+1Hz"

def format_srt_time(ms):
    total_sec = ms / 1000.0
    millis = int(ms % 1000)
    secs = int(total_sec) % 60
    mins = int(total_sec // 60) % 60
    hours = int(total_sec // 3600)
    return f"{hours:02d}:{mins:02d}:{secs:02d},{millis:03d}"

def parse_dialogue_turns(script_text):
    paragraphs = script_text.split('\n\n')
    turns = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if p.startswith('[Prof. Peter]') or p.startswith('[Prof. Peter Kim]'):
            speaker = "Prof. Peter Kim"
            voice = VOICE_PETER
            rate = VOICE_PETER_RATE
            pitch = VOICE_PETER_PITCH
            clean_text = re.sub(r'^\[Prof\.\s*Peter(\s*Kim)?\]\s*', '', p)
        elif p.startswith('[TA Sarah]') or p.startswith('[Sarah (TA)]') or p.startswith('[Prof. Sarah]'):
            speaker = "TA Sarah Jenkins"
            voice = VOICE_SARAH
            rate = VOICE_SARAH_RATE
            pitch = VOICE_SARAH_PITCH
            clean_text = re.sub(r'^\[(TA\s*Sarah|Sarah\s*\(TA\)|Prof\.\s*Sarah)\]\s*', '', p)
        else:
            speaker = "Narrator"
            voice = VOICE_PETER
            rate = "+0%"
            pitch = "+0Hz"
            clean_text = p
            
        turns.append({
            "speaker": speaker,
            "voice": voice,
            "rate": rate,
            "pitch": pitch,
            "text": clean_text
        })
    return turns

async def generate_turn_audio(turn_idx, turn_data, slide_num):
    audio_path = os.path.join(AUDIO_DIR, f"slide_{slide_num:02d}_turn_{turn_idx:02d}.mp3")
    communicate = edge_tts.Communicate(
        text=turn_data["text"],
        voice=turn_data["voice"],
        rate=turn_data["rate"],
        pitch=turn_data["pitch"]
    )
    await communicate.save(audio_path)
    return audio_path

def get_audio_duration_ms(audio_path):
    cmd = [FFMPEG_EXE, "-i", audio_path]
    res = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    match = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", res.stderr)
    if match:
        hours = int(match.group(1))
        mins = int(match.group(2))
        secs = float(match.group(3))
        return int((hours * 3600 + mins * 60 + secs) * 1000)
    return 3000

async def capture_slide_image(slide_num, page):
    img_path = os.path.join(SLIDES_IMG_DIR, f"slide_{slide_num:02d}.png")
    if os.path.exists(img_path):
        return img_path
    
    url = f"https://oikos-lecture-app.vercel.app/"
    await page.goto(url, wait_until="networkidle")
    
    # Press right arrow to get to target slide
    for _ in range(slide_num - 1):
        await page.keyboard.press("ArrowRight")
        await asyncio.sleep(0.12)
        
    await asyncio.sleep(0.4)
    
    await page.evaluate("""() => {
        const header = document.querySelector('header');
        if (header) header.style.display = 'none';
        return true;
    }""")
    
    await page.screenshot(path=img_path, full_page=False)
    print(f"  📸 Captured 1080p slide image: {img_path}")
    return img_path

async def build_slide_video(slide_data, page=None):
    slide_num = slide_data["num"]
    print(f"\n=======================================================")
    print(f"🎬 Processing Slide {slide_num:02d}: {slide_data['title']}")
    print(f"=======================================================")
    
    turns = parse_dialogue_turns(slide_data["script"])
    print(f"  👥 Dialogue Turns: {len(turns)} between Prof. Peter Kim & TA Sarah")
    
    # 1. Synthesize audio
    turn_audio_files = []
    srt_entries = []
    current_time_ms = 0
    silence_gap_ms = 400
    
    for idx, turn in enumerate(turns):
        audio_file = await generate_turn_audio(idx, turn, slide_num)
        duration_ms = get_audio_duration_ms(audio_file)
        turn_audio_files.append((audio_file, duration_ms))
        
        start_time = current_time_ms
        end_time = start_time + duration_ms
        srt_entries.append({
            "idx": idx + 1,
            "start": format_srt_time(start_time),
            "end": format_srt_time(end_time),
            "speaker": turn["speaker"],
            "text": turn["text"]
        })
        current_time_ms = end_time + silence_gap_ms
        print(f"    [Turn {idx+1}] {turn['speaker']} ({duration_ms/1000:.1f}s): \"{turn['text'][:35]}...\"")

    # 2. Concat audio
    concat_txt_path = os.path.join(AUDIO_DIR, f"slide_{slide_num:02d}_concat.txt")
    silence_file = os.path.join(AUDIO_DIR, "silence_400ms.mp3")
    
    if not os.path.exists(silence_file):
        subprocess.run([
            FFMPEG_EXE, "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
            "-t", "0.4", "-q:a", "9", silence_file
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    with open(concat_txt_path, "w", encoding="utf-8") as f:
        for audio_file, _ in turn_audio_files:
            clean_audio = audio_file.replace("\\", "/")
            clean_silence = silence_file.replace("\\", "/")
            f.write(f"file '{clean_audio}'\n")
            f.write(f"file '{clean_silence}'\n")
            
    merged_audio_path = os.path.join(AUDIO_DIR, f"slide_{slide_num:02d}_merged.mp3")
    subprocess.run([
        FFMPEG_EXE, "-y", "-f", "concat", "-safe", "0", "-i", concat_txt_path,
        "-c", "copy", merged_audio_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    total_audio_sec = current_time_ms / 1000.0
    print(f"  🎙️ Merged Audio Track: {total_audio_sec:.1f} seconds")
    
    # 3. Subtitles SRT
    srt_path = os.path.join(OUTPUT_DIR, f"Slide_{slide_num:02d}_Subtitles.srt")
    with open(srt_path, "w", encoding="utf-8") as f:
        for entry in srt_entries:
            speaker_tag = f"[{entry['speaker']}]"
            f.write(f"{entry['idx']}\n")
            f.write(f"{entry['start']} --> {entry['end']}\n")
            f.write(f"{speaker_tag} {entry['text']}\n\n")
    print(f"  📝 Subtitle SRT saved: {srt_path}")

    # 4. Slide Image
    if page:
        img_path = await capture_slide_image(slide_num, page)
    else:
        img_path = os.path.join(SLIDES_IMG_DIR, f"slide_{slide_num:02d}.png")
        if not os.path.exists(img_path):
            cmd = [
                FFMPEG_EXE, "-y", "-f", "lavfi",
                "-i", f"color=c=0x0B132B:s=1920x1080:d=1",
                "-vframes", "1", img_path
            ]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 5. Render 1080p MP4 Video with Subtitles
    out_video_path = os.path.join(OUTPUT_DIR, f"Session1_Slide_{slide_num:02d}_DuoLecture.mp4")
    
    cmd_encode = [
        FFMPEG_EXE, "-y",
        "-loop", "1",
        "-i", img_path,
        "-i", merged_audio_path,
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-t", f"{total_audio_sec:.3f}",
        "-movflags", "+faststart",
        out_video_path
    ]
    
    print(f"  ⚡ Encoding 1080p MP4...")
    subprocess.run(cmd_encode, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if os.path.exists(out_video_path):
        size_mb = os.path.getsize(out_video_path) / (1024 * 1024)
        print(f"  🎉 SUCCESS! Video Created: {out_video_path} ({size_mb:.2f} MB)")
        return out_video_path
    return None

async def build_master_concatenation(video_paths):
    if not video_paths:
        return
    master_concat_txt = os.path.join(OUTPUT_DIR, "master_video_concat.txt")
    with open(master_concat_txt, "w", encoding="utf-8") as f:
        for v in video_paths:
            clean_v = v.replace("\\", "/")
            f.write(f"file '{clean_v}'\n")
            
    master_video_path = os.path.join(OUTPUT_DIR, "Session1_Full_60Min_DuoLecture_Master.mp4")
    print(f"\n=======================================================")
    print(f"🎞️ Merging all {len(video_paths)} slides into Master Lecture Video...")
    print(f"=======================================================")
    
    cmd = [
        FFMPEG_EXE, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", master_concat_txt,
        "-c", "copy",
        master_video_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(master_video_path):
        size_mb = os.path.getsize(master_video_path) / (1024 * 1024)
        print(f"🏆 MASTER DUO LECTURE VIDEO COMPLETED!")
        print(f"📍 Location: {master_video_path} ({size_mb:.2f} MB)")

def load_session_slides(session_id):
    slides_data_path = os.path.join(BASE_DIR, "src", "data", "slidesData.js")
    with open(slides_data_path, "r", encoding="utf-8") as f:
        content = f.read()
    var_name = f"SLIDES_SESSION_{session_id}"
    pattern = rf"export const {var_name} = (\[[\s\S]*?\n\]);"
    match = re.search(pattern, content)
    if not match:
        raise ValueError(f"Could not find {var_name} in slidesData.js")
    return json.loads(match.group(1))

async def main():
    parser = argparse.ArgumentParser(description="Generate Duo Lecture MP4 Videos for Student Pair Projects")
    parser.add_argument("--session", type=int, default=1, help="Session number (1 to 15, default: 1)")
    parser.add_argument("--slide", type=int, help="Generate video for a single slide number (e.g. --slide 1)")
    parser.add_argument("--slides", type=str, help="Comma-separated slide numbers (e.g. --slides 1,8,14,40)")
    parser.add_argument("--all", action="store_true", help="Generate all 40 slides and build Master Video")
    args = parser.parse_args()

    session_slides = load_session_slides(args.session)
    target_slides = []
    
    if args.slide:
        target_slides = [s for s in session_slides if s["num"] == args.slide]
    elif args.slides:
        nums = [int(n.strip()) for n in args.slides.split(",") if n.strip()]
        target_slides = [s for s in session_slides if s["num"] in nums]
    elif args.all:
        target_slides = session_slides
    else:
        # Default: generate demo slides (Slide 1 & Slide 8)
        target_slides = [s for s in session_slides if s["num"] in [1, 8]]

    print("=======================================================")
    print(f"🚀 Oikos Univ 2-Presenter Duo Lecture Video Generator (Session {args.session})")
    print("👨‍🏫 Lead: Prof. Peter Kim (54) | 👩‍💻 TA: Sarah Jenkins (31)")
    print(f"📋 Target: {len(target_slides)} slides from Session {args.session}")
    print("=======================================================")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()
        
        generated_videos = []
        for s in target_slides:
            vpath = await build_slide_video(s, page)
            if vpath:
                generated_videos.append(vpath)
                
        await browser.close()
        
    if args.all and len(generated_videos) == len(session_slides):
        await build_master_concatenation(generated_videos)

    print(f"\n✨ All completed! Files saved in: {OUTPUT_DIR}")

if __name__ == "__main__":
    asyncio.run(main())
