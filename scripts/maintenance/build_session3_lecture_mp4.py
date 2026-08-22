# -*- coding: utf-8 -*-
"""
Oikos University - Session 3 MP4 Video Generator
Adheres to design_oikos.md:
- 3-Presenter Dialogue: Prof. Peter Kim (Voice Morphing), TA Sarah Jenkins, TA James Wilson
- Output Directory: c:\\Oikos Univ\\session3_videos
- High-Resolution Playwright 1080p slide captures
- 4x Module Part Split MP4s + 1x Full Master Lecture MP4
"""

import os
import sys
import asyncio
import subprocess
import re
import json
import imageio_ffmpeg
import edge_tts
from playwright.async_api import async_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Oikos Univ"
OUTPUT_DIR = os.path.join(BASE_DIR, "session3_videos")
SLIDES_IMG_DIR = os.path.join(OUTPUT_DIR, "slide_images")
AUDIO_DIR = os.path.join(OUTPUT_DIR, "audio_segments")
SLIDES_DATA_FILE = os.path.join(BASE_DIR, "src", "data", "slidesData.js")
VOICE_ENGINE_SCRIPT = os.path.join(BASE_DIR, "voice_morphing_engine.py")
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

VOICE_PETER = "en-US-ChristopherNeural"
VOICE_SARAH = "en-US-JennyNeural"
VOICE_JAMES = "en-US-GuyNeural"

VOICE_PETER_RATE = "-2%"
VOICE_PETER_PITCH = "-2Hz"
VOICE_SARAH_RATE = "+2%"
VOICE_SARAH_PITCH = "+1Hz"
VOICE_JAMES_RATE = "+3%"
VOICE_JAMES_PITCH = "+0Hz"

def parse_session_slides(session_id=3):
    with open(SLIDES_DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    pattern = rf"export\s+const\s+SLIDES_SESSION_{session_id}\s*=\s*(\[[\s\S]*?\]);"
    match = re.search(pattern, content)
    if not match:
        raise ValueError(f"Could not find SLIDES_SESSION_{session_id} in {SLIDES_DATA_FILE}")
    return json.loads(match.group(1))

def morph_to_professor_voice(input_path, output_path):
    if not os.path.exists(VOICE_ENGINE_SCRIPT):
        if os.path.exists(input_path):
            import shutil
            shutil.copy(input_path, output_path)
        return
    cmd = [
        "python", VOICE_ENGINE_SCRIPT,
        "--input", input_path,
        "--output", output_path,
        "--preset", "peter_prof"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    if res.returncode != 0 or not os.path.exists(output_path):
        import shutil
        shutil.copy(input_path, output_path)

def format_srt_time(millis):
    hours = millis // 3600000
    mins = (millis % 3600000) // 60000
    secs = (millis % 60000) // 1000
    ms = millis % 1000
    return f"{hours:02d}:{mins:02d}:{secs:02d},{ms:03d}"

def parse_dialogue_turns(script_text):
    paragraphs = [p.strip() for p in script_text.split("\n\n") if p.strip()]
    turns = []
    
    for p in paragraphs:
        if p.startswith("[Prof. Peter") or p.startswith("[Peter"):
            speaker = "Prof. Peter Kim"
            voice = VOICE_PETER
            rate = VOICE_PETER_RATE
            pitch = VOICE_PETER_PITCH
            clean_text = re.sub(r'^\[(Prof\.\s*Peter|Prof\.\s*Peter\s*Kim|Peter)\]\s*', '', p)
        elif p.startswith("[TA Sarah") or p.startswith("[Sarah"):
            speaker = "TA Sarah Jenkins"
            voice = VOICE_SARAH
            rate = VOICE_SARAH_RATE
            pitch = VOICE_SARAH_PITCH
            clean_text = re.sub(r'^\[(TA\s*Sarah|Sarah\s*\(TA\)|Sarah)\]\s*', '', p)
        elif p.startswith("[TA James") or p.startswith("[James"):
            speaker = "TA James Wilson"
            voice = VOICE_JAMES
            rate = VOICE_JAMES_RATE
            pitch = VOICE_JAMES_PITCH
            clean_text = re.sub(r'^\[(TA\s*James|James\s*\(TA\)|James)\]\s*', '', p)
        else:
            speaker = "Prof. Peter Kim"
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
    final_audio_path = os.path.join(AUDIO_DIR, f"s3_slide_{slide_num:02d}_turn_{turn_idx:02d}.mp3")
    
    if "Peter" in turn_data["speaker"]:
        raw_audio_path = os.path.join(AUDIO_DIR, f"s3_slide_{slide_num:02d}_turn_{turn_idx:02d}_raw.mp3")
        communicate = edge_tts.Communicate(
            text=turn_data["text"],
            voice=turn_data["voice"],
            rate=turn_data["rate"],
            pitch=turn_data["pitch"]
        )
        await communicate.save(raw_audio_path)
        await asyncio.sleep(0.05)
        morph_to_professor_voice(raw_audio_path, final_audio_path)
    else:
        communicate = edge_tts.Communicate(
            text=turn_data["text"],
            voice=turn_data["voice"],
            rate=turn_data["rate"],
            pitch=turn_data["pitch"]
        )
        await communicate.save(final_audio_path)
        await asyncio.sleep(0.05)
        
    return final_audio_path

def get_audio_duration_ms(audio_path):
    cmd = [FFMPEG_EXE, "-i", audio_path]
    res = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, errors="replace")
    match = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", res.stderr)
    if match:
        hours = int(match.group(1))
        mins = int(match.group(2))
        secs = float(match.group(3))
        return int((hours * 3600 + mins * 60 + secs) * 1000)
    return 3000

async def capture_slide_image(slide_num, page, session_id=3):
    img_path = os.path.join(SLIDES_IMG_DIR, f"session_{session_id}_slide_{slide_num:02d}.png")
    if os.path.exists(img_path) and os.path.getsize(img_path) > 50000:
        return img_path
    
    url = f"https://oikos-lecture-app.vercel.app/?session={session_id}&slide={slide_num}"
    await page.goto(url, wait_until="networkidle")
    await asyncio.sleep(0.4)
    
    await page.evaluate("""() => {
        const header = document.querySelector('header');
        if (header) header.style.display = 'none';
        return true;
    }""")
    
    await page.screenshot(path=img_path, full_page=False)
    print(f"  📸 Captured 1080p slide image for Session {session_id} Slide {slide_num:02d}: {img_path}")
    return img_path

async def build_slide_video(slide_data, page=None, session_id=3):
    slide_num = slide_data["num"]
    print(f"\n=======================================================")
    print(f"🎬 Processing Session {session_id} • Slide {slide_num:02d}: {slide_data['title']}")
    print(f"=======================================================")
    
    turns = parse_dialogue_turns(slide_data["script"])
    print(f"  👥 Dialogue Turns: {len(turns)} between Prof. Peter Kim, TA Sarah & TA James")
    
    turn_audio_files = []
    srt_entries = []
    
    def chunk_turn_into_subtitles(turn_text, start_ms, total_dur_ms, base_idx):
        sentences = re.split(r'(?<=[.!?])\s+', turn_text.strip())
        valid_sentences = [s.strip() for s in sentences if s.strip()]
        if not valid_sentences:
            valid_sentences = [turn_text]
        
        total_chars = sum(len(s) for s in valid_sentences)
        entries = []
        cur_st = start_ms
        
        for i, s in enumerate(valid_sentences):
            s_dur = int((len(s) / max(total_chars, 1)) * total_dur_ms)
            s_dur = max(s_dur, 1200)
            cur_et = cur_st + s_dur
            if i == len(valid_sentences) - 1:
                cur_et = start_ms + total_dur_ms
            
            entries.append({
                "idx": base_idx + len(entries),
                "start": format_srt_time(cur_st),
                "end": format_srt_time(cur_et),
                "text": s
            })
            cur_st = cur_et
        return entries

    # Generate silence break
    pause_audio = os.path.join(AUDIO_DIR, "breath_pause.mp3")
    if not os.path.exists(pause_audio):
        cmd = [
            FFMPEG_EXE, "-y", "-f", "lavfi",
            "-i", "anullsrc=r=24000:cl=mono",
            "-t", "0.4", "-q:a", "9",
            pause_audio
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    current_time_ms = 400
    for idx, turn in enumerate(turns):
        audio_path = await generate_turn_audio(idx, turn, slide_num)
        dur_ms = get_audio_duration_ms(audio_path)
        
        sub_chunks = chunk_turn_into_subtitles(turn["text"], current_time_ms, dur_ms, len(srt_entries) + 1)
        srt_entries.extend(sub_chunks)
        
        print(f"    [Turn {idx+1}] {turn['speaker']} ({dur_ms/1000:.1f}s, {len(sub_chunks)} subtitle lines): \"{turn['text'][:35]}...\"")
        
        turn_audio_files.append(audio_path)
        turn_audio_files.append(pause_audio)
        current_time_ms += dur_ms + 400

    print(f"  🎙️ Merged Audio Track (with breaks): {current_time_ms/1000:.1f} seconds")
    
    # Save Subtitle SRT
    srt_path = os.path.join(OUTPUT_DIR, f"Slide_{slide_num:02d}_Subtitles.srt")
    with open(srt_path, "w", encoding="utf-8") as f:
        for entry in srt_entries:
            clean_line = entry["text"].replace('"', '').replace('“', '').replace('”', '')
            f.write(f"{entry['idx']}\n{entry['start']} --> {entry['end']}\n{clean_line}\n\n")
    print(f"  📝 Clean Subtitle SRT saved: {srt_path}")
    
    # Concat Audio Files
    concat_list_path = os.path.join(AUDIO_DIR, f"s3_slide_{slide_num:02d}_concat.txt")
    with open(concat_list_path, "w", encoding="utf-8") as f:
        for a_file in turn_audio_files:
            f.write(f"file '{a_file.replace('\\', '/')}'\n")
            
    final_merged_audio = os.path.join(AUDIO_DIR, f"s3_slide_{slide_num:02d}_merged.mp3")
    concat_cmd = [
        FFMPEG_EXE, "-y", "-f", "concat", "-safe", "0",
        "-i", concat_list_path, "-c", "copy", final_merged_audio
    ]
    subprocess.run(concat_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Screenshot Slide
    if page:
        img_path = await capture_slide_image(slide_num, page, session_id=session_id)
    else:
        img_path = os.path.join(SLIDES_IMG_DIR, f"session_{session_id}_slide_{slide_num:02d}.png")
        
    out_mp4 = os.path.join(OUTPUT_DIR, f"Session{session_id}_Slide_{slide_num:02d}_DuoLecture.mp4")
    srt_clean_path = srt_path.replace("\\", "/").replace(":", "\\:")
    
    sub_filter = (
        f"subtitles='{srt_clean_path}':force_style='"
        f"FontName=Paperlogy,FontSize=16,PrimaryColour=&H00FFFFFF,"
        f"SecondaryColour=&H00000000,OutlineColour=&H00000000,BackColour=&H80000000,"
        f"Bold=1,Italic=0,Alignment=2,MarginV=32,BorderStyle=4,Shadow=0'"
    )
    
    cmd_render = [
        FFMPEG_EXE, "-y",
        "-loop", "1", "-i", img_path,
        "-i", final_merged_audio,
        "-vf", sub_filter,
        "-c:v", "libx264", "-tune", "stillimage",
        "-c:a", "aac", "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        out_mp4
    ]
    
    print(f"  ⚡ Encoding 1080p MP4 with Burned-In Subtitles...")
    res = subprocess.run(cmd_render, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode == 0 and os.path.exists(out_mp4):
        size_mb = os.path.getsize(out_mp4) / (1024 * 1024)
        print(f"  🎉 SUCCESS! Video Created: {out_mp4} ({size_mb:.2f} MB)")
        return out_mp4
    else:
        print(f"  ❌ FAILED encoding video for slide {slide_num}: {res.stderr.decode('utf-8', errors='replace')}")
        return None

def build_part_modules_and_master(session_id=3):
    print("\n=======================================================")
    print(f"🎞️ Generating 4x Module Split Videos (Session {session_id})...")
    print("=======================================================")
    
    parts = [
        {"name": f"Session{session_id}_Part1_Local_First_Shell", "start": 1, "end": 11, "title": "Local-First Paradigm & OS Shell Control"},
        {"name": f"Session{session_id}_Part2_WebView2_Deconstruction", "start": 12, "end": 22, "title": "Deconstructing 1.2GB Heavy Armor"},
        {"name": f"Session{session_id}_Part3_Omniscient_Eye_Vision", "start": 23, "end": 29, "title": "The Omniscient Eye: Lens & Vision"},
        {"name": f"Session{session_id}_Part4_Governance_and_Lab", "start": 30, "end": 45, "title": "Governance, Safety & Lab 3"}
    ]
    
    for p in parts:
        concat_txt = os.path.join(OUTPUT_DIR, f"concat_{p['name']}.txt")
        with open(concat_txt, "w", encoding="utf-8") as f:
            for s_num in range(p["start"], p["end"] + 1):
                v_path = os.path.join(OUTPUT_DIR, f"Session{session_id}_Slide_{s_num:02d}_DuoLecture.mp4").replace("\\", "/")
                if os.path.exists(v_path):
                    f.write(f"file '{v_path}'\n")
                    
        part_out = os.path.join(OUTPUT_DIR, f"{p['name']}.mp4")
        concat_cmd = [
            FFMPEG_EXE, "-y",
            "-f", "concat", "-safe", "0",
            "-i", concat_txt,
            "-c", "copy",
            part_out
        ]
        subprocess.run(concat_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if os.path.exists(part_out):
            sz = os.path.getsize(part_out) / (1024 * 1024)
            print(f"  🎬 Created Module: {p['name']}.mp4 (Slides {p['start']:02d}~{p['end']:02d}: {p['title']} | {sz:.2f} MB)")
            
    # Full Master Video
    master_concat_txt = os.path.join(OUTPUT_DIR, f"master_video_concat_session{session_id}.txt")
    with open(master_concat_txt, "w", encoding="utf-8") as f:
        for s_num in range(1, 46):
            v_path = os.path.join(OUTPUT_DIR, f"Session{session_id}_Slide_{s_num:02d}_DuoLecture.mp4").replace("\\", "/")
            if os.path.exists(v_path):
                f.write(f"file '{v_path}'\n")
                
    master_out = os.path.join(OUTPUT_DIR, f"Session{session_id}_Full_Master_Lecture.mp4")
    master_cmd = [
        FFMPEG_EXE, "-y",
        "-f", "concat", "-safe", "0",
        "-i", master_concat_txt,
        "-c", "copy",
        master_out
    ]
    subprocess.run(master_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(master_out):
        sz = os.path.getsize(master_out) / (1024 * 1024)
        print(f"\n🏆 FULL MASTER DUO LECTURE VIDEO COMPLETED!")
        print(f"📍 Location: {master_out} ({sz:.2f} MB)")

async def main_async():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(SLIDES_IMG_DIR, exist_ok=True)
    os.makedirs(AUDIO_DIR, exist_ok=True)
    
    slides = parse_session_slides(session_id=3)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        
        for slide in slides:
            await build_slide_video(slide, page=page, session_id=3)
            
        await browser.close()
        
    build_part_modules_and_master(session_id=3)
    print(f"\n✨ All completed! Files saved in: {OUTPUT_DIR}")

def main():
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
