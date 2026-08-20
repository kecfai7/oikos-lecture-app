# -*- coding: utf-8 -*-
"""
Master Duo Conversion Engine for Sessions 2 through 15 (560 Slides)
Converts solo lectures into engaging NotebookLM-style Duo Dialogues
between Prof. Peter Kim (54) and TA Sarah Jenkins (31).
Updates both src/data/slidesData.js and session2.md ~ session15.md.
"""

import os
import sys
import json
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Oikos Univ"
SLIDES_DATA_JS = os.path.join(BASE_DIR, "src", "data", "slidesData.js")

# Read slidesData.js
with open(SLIDES_DATA_JS, "r", encoding="utf-8") as f:
    js_content = f.read()

# Helper to split paragraphs into dialogue turns
def convert_script_to_duo(session_id, slide_num, title, orig_script, points, slide_type):
    # If already converted
    if "[Prof. Peter]" in orig_script and "[TA Sarah]" in orig_script:
        return orig_script

    clean_orig = orig_script.strip()
    paras = [p.strip() for p in clean_orig.split('\n\n') if p.strip()]

    # Slide 1: Opening Title Slide
    if slide_num == 1:
        script = (
            f"[Prof. Peter] Welcome back, everyone, to Oikos University! I am Professor Peter Kim, Director of Smart Insight Lab. Today, we begin our exciting Session {session_id}: \"{title}\".\n\n"
            f"[TA Sarah] And hello everyone! I'm Sarah Jenkins, your Teaching Assistant and AI Research Fellow. Professor Kim and I are so excited to explore today's architecture with you all!\n\n"
            f"[Prof. Peter] Exactly, Sarah. In this session, we go beyond surface-level theory into real-world agentic mastery. We are learning how to architect systems that work reliably and elevate human potential.\n\n"
            f"[TA Sarah] For all our global students, we will guide you step by step in clear, accessible English. Let's dive straight into Session {session_id}!"
        )
        return script

    # Slide 40: Hands-on Lab & Conclusion
    if slide_num == 40 or "LAB" in title.upper() or "CONCLUSION" in title.upper():
        script = (
            f"[TA Sarah] Here we are at Slide 40: Our Hands-on Lab and Session Conclusion!\n\n"
            f"[Prof. Peter] That is right, Sarah. As we always emphasize at Oikos University, theory without hands-on engineering is incomplete. Tonight, every student will implement today's blueprint!\n\n"
            f"[TA Sarah] In this lab, follow the step-by-step instructions in your workbook: configure your environment, deploy the required connectors, and verify the live outputs.\n\n"
            f"[Prof. Peter] Congratulations on mastering Session {session_id}! On behalf of TA Sarah Jenkins and myself, Soli Deo Gloria, and we look forward to seeing you in our next session!"
        )
        return script

    # Regular slides (2 to 39): Construct rich 4-turn to 5-turn dialogue based on slide title, content, and existing script
    if len(paras) >= 4:
        # We alternate speakers across paragraphs
        new_paras = []
        for i, p in enumerate(paras):
            speaker = "[Prof. Peter]" if i % 2 == 0 else "[TA Sarah]"
            # Add natural dialogue cues
            p_text = p
            if i == 0 and speaker == "[Prof. Peter]":
                p_text = f"Let's look at Slide {slide_num}: \"{title}\". " + p_text
            elif i == 1 and speaker == "[TA Sarah]":
                p_text = f"Professor Kim, looking at this slide, " + p_text[0].lower() + p_text[1:]
            elif speaker == "[TA Sarah]" and not p_text.startswith("Professor Kim"):
                if not re.match(r'^(And|Also|Notice|Here|Looking|Exactly)', p_text):
                    p_text = "Notice also that " + p_text[0].lower() + p_text[1:]
            new_paras.append(f"{speaker} {p_text}")
        return "\n\n".join(new_paras)
    
    elif len(paras) == 2 or len(paras) == 3:
        p1 = paras[0]
        p2 = paras[1]
        p3 = paras[2] if len(paras) == 3 else ""
        
        script = (
            f"[Prof. Peter] Let's examine Slide {slide_num}: \"{title}\". {p1}\n\n"
            f"[TA Sarah] Professor Kim, this is such a critical concept for our students! {p2}\n\n"
        )
        if p3:
            script += f"[Prof. Peter] Exactly, Sarah. {p3}\n\n[TA Sarah] That is why understanding this balance gives us true strategic leverage."
        else:
            script += f"[Prof. Peter] Precisely, Sarah. When we apply this principle, our autonomous systems run with speed, safety, and purpose."
        return script.strip()
    
    else:
        # Single paragraph or short content
        sentences = re.split(r'(?<=[.?!])\s+', clean_orig)
        if len(sentences) >= 4:
            s1 = " ".join(sentences[:2])
            s2 = " ".join(sentences[2:4])
            s3 = " ".join(sentences[4:])
            script = (
                f"[Prof. Peter] On Slide {slide_num}, we explore \"{title}\". {s1}\n\n"
                f"[TA Sarah] Professor Kim, breaking this down for our students: {s2}\n\n"
                f"[Prof. Peter] Exactly, Sarah. {s3}\n\n"
                f"[TA Sarah] This allows our architecture to scale seamlessly without manual bottlenecks."
            )
            return script
        else:
            script = (
                f"[Prof. Peter] Welcome to Slide {slide_num}: \"{title}\". {clean_orig}\n\n"
                f"[TA Sarah] Professor Kim, this connects directly to our architectural goals. By mastering this component, students can build robust, sleep-free agentic workflows with complete confidence!"
            )
            return script

def update_korean_guide(guide, slide_num):
    if not guide:
        return guide
    tips = guide.get("tips", "")
    if "사라" not in tips:
        guide["tips"] = "피터 교수(54세, 거시적 비전/전략)와 사라 조교(31세, 실무 엔지니어링/질문자)의 활기찬 핑퐁 대화 톤으로 강의를 전달하세요."
    return guide

# Process sessions 2 to 15
print("=======================================================")
print("🚀 Transforming Sessions 2 to 15 to 2-Presenter Duo...")
print("=======================================================")

for session_id in range(2, 16):
    var_name = f"SLIDES_SESSION_{session_id}"
    pattern = rf"export const {var_name} = (\[[\s\S]*?\n\]);"
    match = re.search(pattern, js_content)
    if not match:
        print(f"⚠️ Could not find {var_name}")
        continue
    
    slides_json_str = match.group(1)
    try:
        slides = json.loads(slides_json_str)
    except Exception as e:
        print(f"❌ Error parsing JSON for {var_name}: {e}")
        continue
    
    # Transform slides
    for slide in slides:
        s_num = slide.get("num", 1)
        title = slide.get("title", "")
        orig_script = slide.get("script", "")
        points = slide.get("points", [])
        stype = slide.get("type", "content")
        
        slide["script"] = convert_script_to_duo(session_id, s_num, title, orig_script, points, stype)
        slide["instructor"] = "Prof. Peter Kim & TA Sarah Jenkins • Smart Insight Lab"
        if "koreanGuide" in slide:
            slide["koreanGuide"] = update_korean_guide(slide["koreanGuide"], s_num)
            
    # Replace back in js_content
    new_json_str = json.dumps(slides, indent=2, ensure_ascii=False)
    js_content = js_content[:match.start(1)] + new_json_str + js_content[match.end(1):]
    print(f"✅ Converted {var_name} (40 Slides)")

    # Update session markdown file (session2.md ~ session15.md)
    md_path = os.path.join(BASE_DIR, f"session{session_id}.md")
    md_lines = []
    sess_title = slides[0].get("detail", f"Session {session_id}: Advanced Agentic IT")
    md_lines.append(f"# {sess_title}")
    md_lines.append(f"**Course:** The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom  ")
    md_lines.append(f"**Instructors:** Professor Peter Kim (54, Director) & TA Sarah Jenkins (31, AI Research Fellow) • Oikos University (www.oikos.edu)  ")
    md_lines.append(f"**Lecture Format:** NotebookLM Style Interactive Duo Dialogue (2-Presenter Co-Lecture)  ")
    md_lines.append(f"**Total Slides:** 40 Slides (60 Minutes)  ")
    md_lines.append(f"**Motto:** Soli Deo Gloria  \n")
    md_lines.append("---\n")
    md_lines.append("## 📌 Table of Contents (목차)")
    
    for slide in slides:
        num_str = f"{slide['num']:02d}"
        slug = f"slide-{num_str}-{slide['title'].lower().replace(' ', '-').replace(':', '').replace('.', '').replace('•', '').replace('🛠️', '').replace('📨', '').replace('\'', '').replace('&', 'and')}"
        slug = re.sub(r'-+', '-', slug).strip('-')
        md_lines.append(f"- [Slide {num_str}: {slide['title']}](#{slug})")
    
    md_lines.append("\n---\n")

    for slide in slides:
        num_str = f"{slide['num']:02d}"
        md_lines.append(f"## Slide {num_str}: {slide['title']}")
        if "subtitle" in slide:
            md_lines.append(f"**Subtitle:** {slide['subtitle']}\n")
        
        md_lines.append("### 🎙️ English Lecture Script (Duo Dialogue)")
        md_lines.append(slide["script"] + "\n")
        
        if "koreanGuide" in slide:
            md_lines.append("### 🇰🇷 Korean Teaching Guide (강의 가이드)")
            md_lines.append(f"- **강의 요약:** {slide['koreanGuide'].get('summary', '')}")
            md_lines.append("- **핵심 포인트:**")
            for pt in slide["koreanGuide"].get("points", []):
                md_lines.append(f"  - {pt}")
            md_lines.append(f"- **강의 전달 팁:** {slide['koreanGuide'].get('tips', '')}\n")

        if "keyTerms" in slide:
            md_lines.append("### 📚 Key Terms (주요 용어)")
            for term in slide["keyTerms"]:
                md_lines.append(f"- **{term['term']}**: {term['def']} ({term.get('defKo', '')})")
            md_lines.append("\n---\n")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"   📝 Updated session{session_id}.md")

# Write updated slidesData.js
with open(SLIDES_DATA_JS, "w", encoding="utf-8") as f:
    f.write(js_content)

print("\n=======================================================")
print("🎉 All 15 Sessions (600 Slides total) Successfully Converted!")
print("=======================================================")
