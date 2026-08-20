# -*- coding: utf-8 -*-
"""
Precise 1-to-1 UI-Synced Script Generator for Session 1 (Slides 1 to 40)
Tailored specifically to what each React Component actually renders on the screen.
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

# Clean up dirty attributes for section slides
for s in slides:
    if s.get("type") == "section":
        s.pop("leftCard", None)
        s.pop("rightCard", None)
        s.pop("cards", None)
        s.pop("steps", None)

# Custom crafted scripts that 100% match screen elements for all 40 slides
SCRIPTS_PER_SLIDE = {
    1: """[Prof. Peter] Welcome everyone to Oikos University! I am Professor Peter Kim, Director of Smart Insight Lab. Today, we begin our master course: "The Architect of Intelligence: Mastering Agentic IT and Strategic Wisdom."

[TA Sarah] And hello everyone! I'm Sarah Jenkins, your Teaching Assistant and AI Research Fellow. Professor Kim and I are so excited to explore this course with you!

[Prof. Peter] Look at our main title on the screen: "From Waiting Chatbots to Sleep-Free Personal Avatars." For the past three years, the world interacted with AI like a textbook sitting on a desk—asking a question and waiting for an answer.

[TA Sarah] But in 2026, we step into the true agentic revolution: building autonomous, sleep-free personal avatars that execute complex digital workflows in the cloud 24 hours a day, 7 days a week!

[Prof. Peter] Our foundational motto is "Soli Deo Gloria"—Glory to God alone. We build this technology to redeem human time, eliminate mechanical drudgery, and elevate human wisdom. Let us begin!""",

    2: """[Prof. Peter] Look at Slide 2, our first Part Divider: "PART 1: THE PARADIGM SHIFT: CHATBOTS TO AVATARS."

[TA Sarah] Notice our subtitle on the screen: "Soli Deo Gloria: Reclaiming human time from mechanical chatbot waiting loops."

[Prof. Peter] For two years, humanity has been trapped staring at blinking AI cursors, typing prompts and waiting. That waiting loop wastes immense human potential.

[TA Sarah] In Part 1, we deconstruct how we transition from passive waiting to commanding proactive avatars that work while you sleep.

[Prof. Peter] Let us click "Entering Next Phase" and dive straight into Part 1!""",

    3: """[Prof. Peter] Slide 3 presents our "CORE MISSION & MOTTO: Soli Deo Gloria—Glory to God Alone." Notice the three core principles on the screen.

[TA Sarah] Principle 1 is Our Mandate: Elevating human mind and spirit above mechanical work. We were created with creativity and strategic wisdom, not to do repetitive data copying.

[Prof. Peter] Principle 2 defines Technology's Role: Technology is a tool to serve humans, not a master to control us. We must never let addictive notifications dictate our lives.

[TA Sarah] And Principle 3 is our Wisdom Goal: Automating simple tasks to save precious time for higher purpose—our families, our faith, and serving society.

[Prof. Peter] True automation is about the sacred stewardship of time.""",

    4: """[TA Sarah] Slide 4 introduces the "SMART INSIGHT LAB PHILOSOPHY" with three foundational pillars.

[Prof. Peter] Look at Card 1 on the left: "PILLAR 1: DATA." In an era of AI hallucinations and information overload, our job is decoding clear truth signals from surrounding noise.

[TA Sarah] Look at Card 2 in the center: "PILLAR 2: TECHNOLOGY." We engineer clean, robust, and scalable 24/7 cloud agent systems that never crash.

[Prof. Peter] And look at Card 3 on the right: "PILLAR 3: LIFE OS." We structure daily habits so technology protects your mental focus, physical health, and sleep rather than draining you.

[TA Sarah] When Data, Technology, and Life OS align, you become a truly wise Intelligence Architect!""",

    5: """[Prof. Peter] Slide 5 is titled "A LETTER FROM THE FUTURE: From childhood dreams to 2026 reality."

[TA Sarah] On the left card, look at the childhood wish tagged "THE DREAM": "What if a double of myself could do my homework and clean my room while I play?"

[Prof. Peter] And on the right card, look at our 2026 reality tagged "THE REALITY": "2026 Autonomous Avatar." Today, digital twins execute complex daily workflows on your behalf while you sleep!

[TA Sarah] What was once childhood science fiction has now become production software engineering.

[Prof. Peter] That is the transformative power of the avatar architecture we are building in this course.""",

    6: """[TA Sarah] Slide 6 highlights "THE ULTIMATE CURRENCY." Notice the prominent metric in the center: "24 HOURS PER DAY."

[Prof. Peter] The stat label says it clearly: "The Equalizer for All Humanity." Money, hardware, and algorithms can be multiplied, but physical human time remains strictly finite.

[TA Sarah] Below the metric, notice the key insight: In the age of AI, the ultimate wealth is not raw computation—it is reclaiming undivided human focus and presence.

[Prof. Peter] When our sleep-free avatars handle routine work, our finite 24 hours are redeemed for what matters most.""",

    7: """[Prof. Peter] On Slide 7, we lay out our "SESSION 1 LEARNING OBJECTIVES" across three structured cards.

[TA Sarah] Card 1 is "1. PARADIGM SHIFT": Moving from synchronous waiting chatbots to proactive, sleep-free cloud avatars.

[Prof. Peter] Card 2 is "2. ASYNC ARCHITECTURE": Mastering the 3-Layer Gemini Spark pipeline combining Triggers, Reasoning, and Actions.

[TA Sarah] And Card 3 is "3. GOVERNANCE & WISDOM": Implementing Human-on-the-Loop oversight, security guardrails, and offline life balance.

[Prof. Peter] By the end of this 60-minute session, you will possess both the technical blueprint and the philosophical wisdom to build autonomous avatars.""",

    8: """[TA Sarah] Slide 8 presents "THE PARADIGM SHIFT: 'ASK ME' VS. 'RUN IT FOR ME'."

[Prof. Peter] Look at the left card tagged "PASSIVE AI": "The 'Ask Me' Era." In this 2023 model, AI acts like a reactive encyclopedia. You type a prompt, wait for text, copy it, and do all the actual execution yourself.

[TA Sarah] Now look at the right card tagged "ACTIVE AI": "The 'Run It For Me' Era." In 2026, AI acts as an autonomous agent. You define a goal, and the agent executes tools, navigates APIs, and delivers finished outcomes!

[Prof. Peter] Shifting from 'Ask Me' to 'Run It For Me' is the fundamental leap from chatbot to agentic avatar.""",

    9: """[Prof. Peter] Slide 9 illustrates "YESTERDAY: REACTIVE CHATBOTS."

[TA Sarah] On the left card, tagged "THE BOTTLENECK": "Human as Middleware." The human had to sit at the desk, copy text from ChatGPT, paste it into an email, check a spreadsheet, and click send.

[Prof. Peter] On the right card, tagged "THE COST": "High Latency & Fatigue." Every single step required active human presence, causing cognitive exhaustion and severe context switching.

[TA Sarah] It turned high-level thinkers into mechanical copy-paste operators.

[Prof. Peter] That is the bottleneck we are dismantling today.""",

    10: """[TA Sarah] Slide 10 showcases "TODAY: PROACTIVE AVATARS."

[Prof. Peter] Look at the left card tagged "THE LEVERAGE": "Direct Tool Execution." Modern agents do not just generate text; they connect to your Google Drive, trigger APIs, run shell scripts, and manage databases directly.

[TA Sarah] Look at the right card tagged "THE RESULT": "Asynchronous Freedom." You set the objective in the evening, sleep peacefully, and wake up to completed reports and triaged data.

[Prof. Peter] The human shifts from being an exhausted laborer to a sovereign director.""",

    11: """[Prof. Peter] We arrive at Slide 11, our second Part Divider: "PART 2: UNDER THE HOOD OF AUTONOMOUS REASONING."

[TA Sarah] Subtitle: "How autonomous agents think, plan, and execute without human intervention."

[Prof. Peter] In this section, we move behind the scenes to understand the reasoning loops, memory systems, and computational engines that power sleep-free agents.

[TA Sarah] Let's click "Entering Next Phase" and examine the engineering foundation of agentic reasoning!""",

    12: """[TA Sarah] Slide 12 uses a brilliant metaphor: "VIDEO GAME COMPUTING."

[Prof. Peter] Look at the left card tagged "METAPHOR": "Background NPC Simulation." In modern open-world games, non-player characters continue living, trading, and working in the background even when you are not looking at them.

[TA Sarah] And look at the right card tagged "REALITY": "Cloud Agent Loops." Similarly, your personal AI avatar runs continuously in cloud memory, checking triggers and analyzing signals while you focus elsewhere.

[Prof. Peter] It is persistent background computing dedicated entirely to your mission.""",

    13: """[Prof. Peter] Slide 13 demonstrates "SCALING HUMAN ATTENTION." Look at the dramatic metric in the center: "100X."

[TA Sarah] The label states: "Attention Multiplier." A single architect supervising a swarm of 10 specialized agents achieves the throughput of an entire traditional department.

[Prof. Peter] Below the stat, notice the crucial insight: You do not scale by working 100 times harder; you scale by architecting systems that execute in parallel.

[TA Sarah] Wisdom multiplies leverage without multiplying stress!""",

    14: """[TA Sarah] Slide 14 is our "INTERACTIVE STUDENT POLL: What is your biggest time sink in daily IT workflows?"

[Prof. Peter] Look at the options on screen: Option A is Manual data copy-pasting across tools. Option B is Waiting for chatbot responses. Option C is Triaging emails and alerts. And Option D is Repetitive reporting.

[TA Sarah] Over 70% of students choose Option A and C! That proves our biggest drain is mechanical glue work.

[Prof. Peter] And that is exactly what our Gemini Spark pipeline will automate!""",

    15: """[Prof. Peter] Slide 15 provides "POLL ANALYSIS & INSIGHT" across three diagnostic cards.

[TA Sarah] Card 1 is "1. THE GLUE WORK TRAP": Over 60% of knowledge worker hours are consumed by transferring data between disconnected applications.

[Prof. Peter] Card 2 is "2. CONTEXT SWITCHING": Switching tasks every 3 minutes fragments deep focus and degrades cognitive clarity.

[TA Sarah] And Card 3 is "3. THE AVATAR SOLUTION": Delegating glue work to headless cloud agents restores uninterrupted deep work.

[Prof. Peter] Removing glue work is the highest leverage investment in modern enterprise.""",

    16: """[TA Sarah] Slide 16 is our Part Divider: "TRANSITION TO ENGINEERING."

[Prof. Peter] Subtitle: "Moving from conceptual understanding to production agent implementation."

[TA Sarah] Now that we understand the philosophy, we will inspect the exact 3-layer architecture, memory engines, and directory structures.

[Prof. Peter] Let's step into the engineering workshop!""",

    17: """[Prof. Peter] Slide 17 diagrams our core engineering model: "ASYNCHRONOUS ENGINE: THE 3-LAYER SPARK PIPELINE."

[TA Sarah] Notice the three vertical layers displayed in our architecture diagram.

[Prof. Peter] Layer 1 at the top is the "Trigger Layer": handling Webhooks, Cron Schedules, and File Watchers.

[TA Sarah] Layer 2 in the middle is the "Reasoning Layer": powered by Gemini Flash for rapid planning, schema validation, and tool selection.

[Prof. Peter] Layer 3 at the bottom is the "Action Layer": executing Drive API writes, database commits, and alert dispatches.

[TA Sarah] This 3-layer separation ensures rock-solid stability and zero execution bottlenecks.""",

    18: """[TA Sarah] Slide 18 contrasts "SYNCHRONOUS VS. ASYNCHRONOUS" execution.

[Prof. Peter] On the left card tagged "BLOCKING": "Synchronous Execution." Every request blocks the user thread. If an API takes 30 seconds, the human is frozen waiting.

[TA Sarah] On the right card tagged "NON-BLOCKING": "Asynchronous Pipeline." The request is placed in an event queue. The agent processes it in the background and notifies you upon completion!

[Prof. Peter] Asynchronous design is what makes sleep-free avatars possible.""",

    19: """[Prof. Peter] Slide 19 highlights "THE GEMINI 3.5 FLASH BRAIN." Notice the centerpiece metric: "< 250 MS."

[TA Sarah] Stat label: "Sub-Second Reasoning Latency." With Gemini 3.5 Flash, the agent plans multi-step tool calls in milliseconds with high efficiency.

[Prof. Peter] Below the number, notice the key advantage: Instant reasoning enables agents to loop through 10 iterations in just 3 seconds, making autonomous problem-solving feel seamless.

[TA Sarah] Speed and precision combined in one compact cloud brain!""",

    20: """[TA Sarah] Slide 20 explores "HARDWARE INFRASTRUCTURE: TPU V8."

[Prof. Peter] On the left card tagged "LEGACY": "General Compute." High power consumption, memory bottlenecks, and slow batch inference.

[TA Sarah] On the right card tagged "AGENTIC ERA": "Custom TPU Pods." Optimized for matrix multiplication and massive parallel agent swarms.

[Prof. Peter] High-efficiency hardware provides the backbone for affordable, continuous 24/7 avatar operations.""",

    21: """[Prof. Peter] Slide 21 is our Part Divider: "PART 3: THE CONNECTED WORKSPACE: APPS SCRIPT & DRIVE."

[TA Sarah] Subtitle: "Transforming Google Workspace into an automated enterprise command center."

[Prof. Peter] In Part 3, we connect our reasoning brain to real workspace tools—Docs, Sheets, Drive, and Gmail.

[TA Sarah] Let's click "Entering Next Phase" and build the connected workspace!""",

    22: """[TA Sarah] Slide 22 breaks down "THE TRIAD OF AGENTIC DESIGN."

[Prof. Peter] Card 1 is "1. MEMORY ENGINE": Maintaining working context and persistent long-term knowledge.

[TA Sarah] Card 2 is "2. TOOL BELT": Clean API contracts for reading files, executing SQL, and calling external webhooks.

[Prof. Peter] And Card 3 is "3. GUARDRAIL MATRIX": Enforcing schema constraints, spending caps, and safety filters.

[TA Sarah] When Memory, Tools, and Guardrails unite, your avatar operates with enterprise-grade reliability.""",

    23: """[Prof. Peter] Slide 23 diagrams the "SPARK OS DIRECTORY SETUP."

[TA Sarah] Notice the clean folder hierarchy on screen: /agents for persona configs, /skills for modular tool scripts, /memory for persistent logs, and /config for API keys.

[Prof. Peter] A clean directory structure is the foundation of modular, maintainable agent development.

[TA Sarah] Never hardcode keys; always isolate modular skills!""",

    24: """[TA Sarah] Slide 24 explains the "DUAL MEMORY ENGINE."

[Prof. Peter] On the left card tagged "SHORT-TERM": "Working Scratchpad." Fast, in-context scratchpad used during active execution turns.

[TA Sarah] On the right card tagged "LONG-TERM": "Persistent Knowledge Vault." Vector-indexed storage in markdown files and databases for cross-session recall.

[Prof. Peter] Dual memory allows agents to remember user preferences across weeks while executing swift current tasks.""",

    25: """[Prof. Peter] Slide 25 diagrams "GOOGLE WORKSPACE INTEGRATION."

[TA Sarah] Look at the integration pipeline: Webhook triggers from Gmail activate Google Apps Script, which delegates reasoning to Gemini and writes summary reports to Google Drive.

[Prof. Peter] This turns standard cloud storage into an active, intelligent workspace.

[TA Sarah] Zero server maintenance required!""",

    26: """[TA Sarah] Slide 26 presents a "REAL-WORLD CASE STUDY: Executive Inbox Triage."

[Prof. Peter] On the left card tagged "BEFORE": "Manual Triage." 2.5 hours every morning sorting 150 emails, creating task lists, and chasing attachments.

[TA Sarah] On the right card tagged "AFTER": "Avatar Automation." The agent categorizes emails at 4 AM, drafts responses, and prepares an executive 1-page briefing before breakfast!

[Prof. Peter] That is 15 reclaimed hours every single week for strategic leadership.""",

    27: """[Prof. Peter] Slide 27 marks our fourth Part Divider: "THE SECURITY MATRIX: PROTECTING THE DIGITAL VAULT."

[TA Sarah] Subtitle: "Establishing robust guardrails, cryptographic audits, and defense-in-depth."

[Prof. Peter] Autonomy without security is catastrophic. We must ensure our agents operate inside a fortified sandbox.

[TA Sarah] Let's enter the Security Matrix!""",

    28: """[TA Sarah] Slide 28 warns about "FINANCIAL RISK: UNCONTROLLED WALLET."

[Prof. Peter] On the left card tagged "VULNERABILITY": "Unbounded API Spending." An infinite retry loop or malicious prompt draining API credits overnight.

[TA Sarah] On the right card tagged "DEFENSE": "Hard Spending Caps & Token Quotas." Enforcing per-task dollar limits and strict timeout thresholds.

[Prof. Peter] Never deploy an agent without hard financial fences.""",

    29: """[Prof. Peter] Slide 29 outlines "AP2: AGENT PAYMENTS PROTOCOL" across three cards.

[TA Sarah] Card 1 is "1. DUAL AUTHORIZATION": Requiring human confirmation for transactions exceeding safety limits.

[Prof. Peter] Card 2 is "2. EPHEMERAL TOKENS": Single-use cryptographic tokens with precise expiration windows.

[TA Sarah] And Card 3 is "3. AUDIT LOGGING": Immutable ledger recording every single transaction hash.

[Prof. Peter] Secure commerce is the backbone of trusted agentic IT.""",

    30: """[Prof. Peter] Slide 30 declares "THE DIGITAL MANDATE: Soli Deo Gloria in Systems Engineering."

[TA Sarah] Point 1: Absolute Data Integrity—never generating deceptive or unverified claims.

[Prof. Peter] Point 2: Uncompromising Privacy—protecting user credentials and sensitive enterprise data.

[TA Sarah] Point 3: Humble Stewardship—using technological leverage to uplift human communities.

[Prof. Peter] Engineering excellence is a moral commitment.""",

    31: """[TA Sarah] Slide 31 is our final Part Divider: "PART 4: WISDOM SYNTHESIS: SOLI DEO GLORIA."

[Prof. Peter] Subtitle: "Harmonizing cutting-edge agent swarms with human wisdom and life balance."

[TA Sarah] In this concluding section, we review swarm orchestration, human-on-the-loop oversight, and reclaiming offline focus.

[Prof. Peter] Let's step into Wisdom Synthesis!""",

    32: """[Prof. Peter] Slide 32 diagrams the critical threat: "THREAT: PROMPT INJECTION."

[TA Sarah] On the left card tagged "ATTACK VECTOR": "Indirect Prompt Injection." Hidden instructions inside untrusted web pages or emails attempting to hijack the agent.

[Prof. Peter] On the right card tagged "SHIELD": "Strict Input Sanitization." Treating all external content as untrusted data, isolating system prompts in secure delimiters.

[TA Sarah] Always sanitize external inputs before passing them to the reasoning brain!""",

    33: """[TA Sarah] Slide 33 details the "CRYPTOGRAPHIC AUDIT TRAIL."

[Prof. Peter] Look at the step-by-step verification flow: Action Request -> Signature Verification -> Sandboxed Execution -> Immutable Log Append.

[TA Sarah] Every decision made by your avatar is traceable, reproducible, and verifiable.

[Prof. Peter] Transparency builds institutional trust.""",

    34: """[Prof. Peter] Slide 34 tackles "SHADOW IT & ENTERPRISE COMPLIANCE."

[TA Sarah] On the left card tagged "RISK": "Unsanctioned Copy-Pasting." Employees pasting proprietary code into unvetted public chatbots.

[Prof. Peter] On the right card tagged "ENTERPRISE STANDARD": "Governed Private Hub." Centralized agent directory with Single Sign-On and Role-Based Access Control.

[TA Sarah] Enterprise agents must comply with strict governance standards.""",

    35: """[TA Sarah] Slide 35 illustrates "BALANCING AUTONOMY AND CONTROL" across three distinct tiers.

[Prof. Peter] Look at Card 1: "TIER 1: FULL AUTONOMY." Low-risk tasks like summarizing documents and sorting inbox folders.

[TA Sarah] Look at Card 2: "TIER 2: NOTIFY & LOG." Medium-risk tasks like drafting client emails and updating internal records.

[Prof. Peter] And look at Card 3: "TIER 3: STRICT HUMAN APPROVAL." High-risk actions like financial payments, database migrations, and public announcements.

[TA Sarah] This 3-tier matrix prevents catastrophic runaway errors!""",

    36: """[Prof. Peter] Slide 36 diagrams "DEFENSE IN DEPTH FOR AGENTS."

[TA Sarah] Look at the three security concentric layers: Layer 1 Input Sanitization, Layer 2 Runtime Sandboxing, and Layer 3 Egress Filtering.

[Prof. Peter] Even if an adversary bypasses Layer 1, the sandbox and egress filters prevent data exfiltration.

[TA Sarah] Multi-layered defense guarantees enterprise safety.""",

    37: """[TA Sarah] Slide 37 portrays "THE SOVEREIGN CONDUCTOR: ORCHESTRATING SWARMS."

[Prof. Peter] Card 1 is the "RESEARCH AGENT": Gathers facts, parses PDFs, and verifies citations.

[TA Sarah] Card 2 is the "BUILDER AGENT": Writes clean code, formats slides, and builds datasets.

[Prof. Peter] Card 3 is the "CRITIC AGENT": Reviews output against standards and flags errors.

[TA Sarah] You act as the Sovereign Conductor orchestrating this entire symphony!""",

    38: """[Prof. Peter] Slide 38 clarifies "HUMAN-ON-THE-LOOP (HOTL)."

[TA Sarah] On the left card tagged "OLD MODEL": "Human-IN-the-Loop." The human is a bottleneck, manually approving every single trivial step.

[Prof. Peter] On the right card tagged "NEW MODEL": "Human-ON-the-Loop." The agent executes autonomously while the human monitors high-level telemetry and handles exceptions.

[TA Sarah] This achieves infinite scalability while preserving human accountability!""",

    39: """[TA Sarah] Slide 39 inspires us with "RECLAIMING OFFLINE FOCUS."

[Prof. Peter] Card 1 is "1. THE DIGITAL SABBATH": Setting dedicated days completely unplugged from digital devices.

[TA Sarah] Card 2 is "2. DEEP INTELLECTUAL WORK": Channeling saved hours into deep writing, research, and creative synthesis.

[Prof. Peter] Card 3 is "3. FAMILY & FAITH": Investing presence in family meals, prayer, and community fellowship.

[TA Sarah] Soli Deo Gloria: Using technology to enrich real human life!""",

    40: """[Prof. Peter] Here we are at Slide 40: "🛠️ HANDS-ON LAB 1 & CONCLUSION."

[TA Sarah] Look at the three practical lab steps on the screen: Step 1 Setup Spark OS Directory, Step 2 Deploy Gemini Flash Reasoning Pipeline, Step 3 Execute your First Asynchronous Workflow!

[Prof. Peter] Theory without practice is dead. Complete Lab 1 today to launch your first sleep-free avatar!

[TA Sarah] Congratulations on completing Session 1! Professor Kim and I look forward to seeing you in Session 2!

[Prof. Peter] Soli Deo Gloria. Thank you, and God bless you all!"""
}

# Apply to slides
for slide in slides:
    num = slide["num"]
    if num in SCRIPTS_PER_SLIDE:
        slide["script"] = SCRIPTS_PER_SLIDE[num]
    slide["instructor"] = "Prof. Peter Kim (54) & TA Sarah Jenkins (31) • Smart Insight Lab"

# Save updated slidesData.js
new_json = json.dumps(slides, indent=2, ensure_ascii=False)
js_text = js_text[:m.start(1)] + new_json + js_text[m.end(1):]

with open(SLIDES_DATA_JS, "w", encoding="utf-8") as f:
    f.write(js_text)

# Save updated session1.md
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
    md_lines.append("### 🎙️ English Lecture Script (100% UI-Synced Duo Dialogue)")
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

print("✅ Perfect 1-to-1 UI-Synced Scripts written for all 40 slides in Session 1!")
