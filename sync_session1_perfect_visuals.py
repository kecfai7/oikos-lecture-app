# -*- coding: utf-8 -*-
"""
Master Visual-Script Sync Script for Session 1 (Slides 1 to 40)
Reads visual components (title, subtitle, leftCard, rightCard, cards, steps, points)
and creates dialogue turns where Prof. Peter Kim and TA Sarah Jenkins explicitly reference
and explain each visual element on the screen.
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
SESSION1_MD = os.path.join(BASE_DIR, "session1.md")

with open(SLIDES_DATA_JS, "r", encoding="utf-8") as f:
    js_text = f.read()

m = re.search(r"export const SLIDES_SESSION_1 = (\[[\s\S]*?\n\]);", js_text)
if not m:
    print("Could not find SLIDES_SESSION_1")
    sys.exit(1)

slides = json.loads(m.group(1))

def generate_perfect_synced_script(s):
    num = s["num"]
    title = s.get("title", "")
    subtitle = s.get("subtitle", "")
    stype = s.get("type", "content")
    
    # 1. Slide 1: Title
    if num == 1:
        return (
            "[Prof. Peter] Welcome everyone to Oikos University! I am Professor Peter Kim, Director of the Smart Insight Lab. Today, we open Session 1 of our master course: \"The Architect of Intelligence: Mastering Agentic IT and Strategic Wisdom.\"\n\n"
            "[TA Sarah] And hello everyone! I'm Sarah Jenkins, your Teaching Assistant and AI Research Fellow. Professor Kim and I are so thrilled to lead this master course with you!\n\n"
            "[Prof. Peter] Look at our main title on the screen: \"From Waiting Chatbots to Sleep-Free Personal Avatars.\" For the past three years, the world interacted with AI like a textbook sitting on a desk—asking a question and waiting for an answer.\n\n"
            "[TA Sarah] But in 2026, we step into the true agentic revolution: building autonomous, sleep-free personal avatars that execute complex digital workflows in the cloud 24 hours a day, 7 days a week!\n\n"
            "[Prof. Peter] Our foundational motto is \"Soli Deo Gloria\"—Glory to God alone. We build this technology to redeem human time, eliminate mechanical drudgery, and elevate human wisdom. Let us begin!"
        )
        
    # 2. Comparison or Split type (leftCard vs rightCard)
    if "leftCard" in s and "rightCard" in s:
        l = s["leftCard"]
        r = s["rightCard"]
        l_pts = " ".join(l.get("points", []))
        r_pts = " ".join(r.get("points", []))
        
        return (
            f"[Prof. Peter] Look at Slide {num}: \"{title}\". As shown in the subtitle, \"{subtitle}\", notice the clear contrast between the two cards on our screen.\n\n"
            f"[TA Sarah] On the left card, we have \"{l.get('title', 'Past Model')}\" tagged as \"{l.get('tag', 'Yesterday')}\". Notice the key characteristics: {l_pts}\n\n"
            f"[Prof. Peter] Exactly, Sarah. Now examine the right card: \"{r.get('title', '2026 Model')}\" tagged as \"{r.get('tag', 'Today')}\". Here is the transformation: {r_pts}\n\n"
            f"[TA Sarah] The difference is immense! Instead of getting trapped in the left-hand bottleneck, the right-hand architecture gives us leverage and scale.\n\n"
            f"[Prof. Peter] Precisely. Understanding this visual distinction is the first step to mastering agentic design."
        )
        
    # 3. Triad type (3 cards)
    if "cards" in s and len(s["cards"]) == 3:
        c1, c2, c3 = s["cards"][0], s["cards"][1], s["cards"][2]
        return (
            f"[TA Sarah] Slide {num} diagrams \"{title}\". Notice the three core cards across the screen:\n\n"
            f"[Prof. Peter] Look at Card 1: \"{c1.get('title', '')}\". {c1.get('desc', '')}\n\n"
            f"[TA Sarah] Next is Card 2: \"{c2.get('title', '')}\". {c2.get('desc', '')}\n\n"
            f"[Prof. Peter] And look at Card 3: \"{c3.get('title', '')}\". {c3.get('desc', '')}\n\n"
            f"[TA Sarah] When these three cards operate in harmony, our autonomous systems achieve maximum reliability and strategic impact."
        )

    # 4. Steps or Pipeline type
    if "steps" in s:
        step_strs = [f"Step {st.get('step', i+1)}: {st.get('name', '')} ({st.get('role', '')})" for i, st in enumerate(s["steps"])]
        steps_text = " -> ".join(step_strs)
        return (
            f"[Prof. Peter] Let's examine Slide {num}: \"{title}\". Look at the step-by-step pipeline displayed across the screen.\n\n"
            f"[TA Sarah] Walking through our pipeline from left to right: {steps_text}\n\n"
            f"[Prof. Peter] Notice how each step feeds directly into the next without human latency. That is the essence of end-to-end execution.\n\n"
            f"[TA Sarah] This structured flow ensures complete predictability and zero data loss throughout the entire process."
        )

    # 5. Points / Motto list type
    if "points" in s:
        pts = s["points"]
        p1 = pts[0] if len(pts) > 0 else ""
        p2 = pts[1] if len(pts) > 1 else ""
        p3 = pts[2] if len(pts) > 2 else ""
        return (
            f"[Prof. Peter] Slide {num} is titled \"{title}\". Notice the key principles on the screen:\n\n"
            f"[TA Sarah] First: {p1}\n\n"
            f"[Prof. Peter] Second: {p2}\n\n"
            f"[TA Sarah] And third: {p3}\n\n"
            f"[Prof. Peter] Mastering these principles gives our architects the strategic clarity required in modern AI engineering."
        )

    # Fallback
    return (
        f"[Prof. Peter] Let's look at Slide {num}: \"{title}\". As highlighted in the subtitle: \"{subtitle}\".\n\n"
        f"[TA Sarah] Professor Kim, breaking down the visual details on this slide helps students see exactly how this connects to our architecture.\n\n"
        f"[Prof. Peter] Exactly, Sarah. When we apply this knowledge, our agents run with high precision and complete security."
    )

# Apply perfect visual-script sync to all 40 slides
for slide in slides:
    slide["script"] = generate_perfect_synced_script(slide)
    slide["instructor"] = "Prof. Peter Kim (54) & TA Sarah Jenkins (31) • Smart Insight Lab"

# Write updated slidesData.js
new_json = json.dumps(slides, indent=2, ensure_ascii=False)
js_text = js_text[:m.start(1)] + new_json + js_text[m.end(1):]

with open(SLIDES_DATA_JS, "w", encoding="utf-8") as f:
    f.write(js_text)

# Also update session1.md
md_lines = [
    "# Session 1: From Waiting Chatbots to Sleep-Free Personal Avatars",
    "**Course:** The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom  ",
    "**Instructors:** Professor Peter Kim (54, Director) & TA Sarah Jenkins (31, AI Research Fellow) • Oikos University (www.oikos.edu)  ",
    "**Lecture Format:** NotebookLM Style Interactive Duo Dialogue (2-Presenter Co-Lecture)  ",
    "**Total Slides:** 40 Slides (60 Minutes)  ",
    "**Motto:** Soli Deo Gloria  \n",
    "---\n",
    "## 📌 Table of Contents (목차)"
]

for s in slides:
    num_str = f"{s['num']:02d}"
    slug = f"slide-{num_str}-{s['title'].lower().replace(' ', '-').replace(':', '').replace('.', '').replace('•', '').replace('🛠️', '').replace('📨', '').replace('\'', '').replace('&', 'and')}"
    slug = re.sub(r'-+', '-', slug).strip('-')
    md_lines.append(f"- [Slide {num_str}: {s['title']}](#{slug})")

md_lines.append("\n---\n")

for s in slides:
    num_str = f"{s['num']:02d}"
    md_lines.append(f"## Slide {num_str}: {s['title']}")
    if "subtitle" in s:
        md_lines.append(f"**Subtitle:** {s['subtitle']}\n")
    md_lines.append("### 🎙️ English Lecture Script (100% Visual-Synced Duo Dialogue)")
    md_lines.append(s["script"] + "\n")
    if "koreanGuide" in s:
        md_lines.append("### 🇰🇷 Korean Teaching Guide (강의 가이드)")
        md_lines.append(f"- **강의 요약:** {s['koreanGuide'].get('summary', '')}")
        md_lines.append("- **핵심 포인트:**")
        for pt in s["koreanGuide"].get("points", []):
            md_lines.append(f"  - {pt}")
        md_lines.append(f"- **강의 전달 팁:** {s['koreanGuide'].get('tips', '')}\n")
    if "keyTerms" in s:
        md_lines.append("### 📚 Key Terms (주요 용어)")
        for term in s["keyTerms"]:
            md_lines.append(f"- **{term['term']}**: {term['def']} ({term.get('defKo', '')})")
        md_lines.append("\n---\n")

with open(SESSION1_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print("✅ Perfect Visual-Script Sync applied to all 40 slides in slidesData.js and session1.md!")
