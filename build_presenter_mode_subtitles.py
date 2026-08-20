import os
import sys
import json
import re
import subprocess
import time
import imageio_ffmpeg
from build_final_video import selected_mapping

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
ffmpeg_dir = os.path.dirname(ffmpeg_exe)
os.environ["PATH"] = ffmpeg_dir + os.path.pathsep + os.environ.get("PATH", "")

files_dir = r"c:\Oikos Univ\files"
cleaned_dir = r"c:\Oikos Univ\files_cleaned"
analysis_dir = r"c:\Oikos Univ\files_analysis"
presenter_scripts_file = os.path.join(analysis_dir, "presenter_mode_session1_scripts.json")
word_cache_file = os.path.join(analysis_dir, "session1_word_timestamps.json")

def load_presenter_scripts():
    with open(presenter_scripts_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    scripts = {}
    for k, v in data.items():
        s_num = int(k)
        text = v.get("script", "")
        # Clean markdown formatting
        text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
        text = re.sub(r"\*([^*]+)\*", r"\1", text)
        text = re.sub(r"`([^`]+)`", r"\1", text)
        text = re.sub(r"\s+", " ", text).strip()
        scripts[s_num] = text
    return scripts

def split_into_sentences(script):
    sentences = re.split(r'(?<=[.?!])\s+', script)
    return [s.strip() for s in sentences if s.strip()]

def format_srt_time(seconds):
    millis = int(round((seconds - int(seconds)) * 1000))
    if millis >= 1000:
        millis = 999
    secs = int(seconds) % 60
    mins = (int(seconds) // 60) % 60
    hours = int(seconds) // 3600
    return f"{hours:02d}:{mins:02d}:{secs:02d},{millis:03d}"

def format_vtt_time(seconds):
    millis = int(round((seconds - int(seconds)) * 1000))
    if millis >= 1000:
        millis = 999
    secs = int(seconds) % 60
    mins = (int(seconds) // 60) % 60
    hours = int(seconds) // 3600
    return f"{hours:02d}:{mins:02d}:{secs:02d}.{millis:03d}"

def generate_subtitles():
    scripts = load_presenter_scripts()
    with open(word_cache_file, "r", encoding="utf-8") as f:
        whisper_data = json.load(f)
        
    srt_entries = []
    vtt_entries = []
    
    current_timeline_offset = 0.0
    entry_index = 1
    
    print("="*90)
    print("Building Subtitles directly from Presenter Mode Scripts (https://oikos-lecture-app-nu.vercel.app/)...")
    print("="*90)
    
    for s_num, fname in selected_mapping:
        clean_mp4 = os.path.join(cleaned_dir, f"slide_{s_num:02d}_clean.mp4")
        
        # Get exact clip duration using FFmpeg
        cmd = [ffmpeg_exe, "-i", clean_mp4]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        dur_match = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", res.stderr)
        if not dur_match:
            raise ValueError(f"Could not read duration for {clean_mp4}")
            
        h, m, s = map(float, dur_match.groups())
        clip_dur = h * 3600 + m * 60 + s
        
        script_text = scripts.get(s_num, "")
        sentences = split_into_sentences(script_text)
        
        key = f"slide_{s_num:02d}"
        slide_info = whisper_data.get(key, {})
        words = slide_info.get("words", [])
        
        if not sentences:
            current_timeline_offset += clip_dur
            continue
            
        slide_subtitles = []
        
        if words and len(words) >= len(sentences):
            total_script_words = sum(len(s.split()) for s in sentences)
            total_spoken_words = len(words)
            
            curr_w_idx = 0
            for i, sent in enumerate(sentences):
                sent_word_count = len(sent.split())
                target_w_count = max(1, int(round((sent_word_count / total_script_words) * total_spoken_words)))
                
                start_w_idx = min(len(words) - 1, curr_w_idx)
                end_w_idx = min(len(words) - 1, curr_w_idx + target_w_count - 1)
                
                if i == len(sentences) - 1:
                    end_w_idx = len(words) - 1
                    
                t_start = words[start_w_idx]["start"]
                t_end = words[end_w_idx]["end"]
                
                # Split long sentences into 2 readable lines
                sent_words = sent.split()
                if len(sent_words) > 11:
                    mid_w = len(sent_words) // 2
                    part1 = " ".join(sent_words[:mid_w])
                    part2 = " ".join(sent_words[mid_w:])
                    mid_t = (t_start + t_end) / 2.0
                    slide_subtitles.append((t_start, mid_t - 0.05, part1))
                    slide_subtitles.append((mid_t + 0.05, t_end, part2))
                else:
                    slide_subtitles.append((t_start, t_end, sent))
                    
                curr_w_idx = end_w_idx + 1
        else:
            sp_start = 0.5
            sp_end = max(sp_start + 1.0, clip_dur - 0.5)
            unit_dur = (sp_end - sp_start) / len(sentences)
            for i, sent in enumerate(sentences):
                t_s = sp_start + (i * unit_dur)
                t_e = t_s + (unit_dur * 0.95)
                sent_words = sent.split()
                if len(sent_words) > 11:
                    mid_w = len(sent_words) // 2
                    part1 = " ".join(sent_words[:mid_w])
                    part2 = " ".join(sent_words[mid_w:])
                    mid_t = (t_s + t_e) / 2.0
                    slide_subtitles.append((t_s, mid_t - 0.05, part1))
                    slide_subtitles.append((mid_t + 0.05, t_e, part2))
                else:
                    slide_subtitles.append((t_s, t_e, sent))
                    
        for t_s, t_e, txt in slide_subtitles:
            abs_start = current_timeline_offset + max(0.1, t_s)
            abs_end = current_timeline_offset + min(clip_dur - 0.05, max(t_s + 0.8, t_e))
            
            srt_entries.append((entry_index, abs_start, abs_end, txt))
            vtt_entries.append((entry_index, abs_start, abs_end, txt))
            entry_index += 1
            
        first_txt = slide_subtitles[0][2][:35] if slide_subtitles else ""
        last_txt = slide_subtitles[-1][2][:35] if slide_subtitles else ""
        print(f"Slide {s_num:02d}: {len(slide_subtitles):2d} subtitles | Clip: {clip_dur:>6.2f}s | Offset: {current_timeline_offset:>7.2f}s -> {current_timeline_offset+clip_dur:>7.2f}s")
        print(f"   [Start: {format_srt_time(current_timeline_offset + slide_subtitles[0][0])}] {first_txt}...")
        print(f"   [End:   {format_srt_time(current_timeline_offset + slide_subtitles[-1][1])}] {last_txt}...")
        current_timeline_offset += clip_dur

    # Write SRT
    srt_path = os.path.join(files_dir, "Session1_Lecture.srt")
    with open(srt_path, "w", encoding="utf-8") as f:
        for idx, start, end, text in srt_entries:
            f.write(f"{idx}\n{format_srt_time(start)} --> {format_srt_time(end)}\n{text}\n\n")
            
    # Write VTT
    vtt_path = os.path.join(files_dir, "Session1_Lecture.vtt")
    with open(vtt_path, "w", encoding="utf-8") as f:
        f.write("WEBVTT\n\n")
        for idx, start, end, text in vtt_entries:
            f.write(f"{idx}\n{format_vtt_time(start)} --> {format_vtt_time(end)}\n{text}\n\n")
            
    print(f"\n[OK] Generated Presenter Mode SRT: {srt_path}")
    print(f"[OK] Generated Presenter Mode VTT: {vtt_path}")
    print(f"Total Subtitle Entries: {len(srt_entries)}")
    return srt_path

def burn_subtitles_to_video(srt_path):
    input_video = os.path.join(files_dir, "Session1_Full_Lecture_Optimized.mp4")
    output_video = os.path.join(files_dir, "Session1_Full_Lecture_Subtitled.mp4")
    
    escaped_srt = srt_path.replace("\\", "/").replace(":", "\\:")
    
    # Subtitle Style: High clarity 1080p, semi-transparent black box
    sub_filter = f"subtitles='{escaped_srt}':force_style='FontName=Arial,FontSize=20,PrimaryColour=&H00FFFFFF,BackColour=&H80000000,BorderStyle=4,Outline=1,MarginV=30,Alignment=2'"
    
    cmd = [
        ffmpeg_exe, "-y",
        "-i", input_video,
        "-vf", sub_filter,
        "-c:v", "libx264",
        "-crf", "26",
        "-preset", "fast",
        "-pix_fmt", "yuv420p",
        "-c:a", "copy",
        "-movflags", "+faststart",
        output_video
    ]
    
    print("\n" + "="*90)
    print("Burning Presenter Mode subtitles into final lecture video with FFmpeg...")
    print(f"Input:  {input_video}")
    print(f"Output: {output_video}")
    print("="*90)
    
    t0 = time.time()
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    elapsed = time.time() - t0
    
    if res.returncode == 0 and os.path.exists(output_video):
        stat = os.stat(output_video)
        print(f"\n[SUCCESS] Final Subtitled video created successfully in {elapsed:.1f}s!")
        print(f"File: {output_video}")
        print(f"Size: {stat.st_size / (1024*1024):.2f} MB")
    else:
        print("\n[ERROR] FFmpeg failed to burn subtitles:")
        print(res.stderr)

if __name__ == "__main__":
    srt_file = generate_subtitles()
    burn_subtitles_to_video(srt_file)
