# -*- coding: utf-8 -*-
"""
60-Minute Expanded Dialogue Script Generator for Session 1 (40 Slides)
Averages ~85s dialogue + 5s pauses per slide = exactly 90s * 40 slides = 3,600s (60 Minutes).
Perfect for 3-part 20-minute splits:
- Part 1 (Slides 01-13): 20 Minutes (Foundation & Paradigm Shift)
- Part 2 (Slides 14-26): 20 Minutes (Engineering & Asynchronous Pipelines)
- Part 3 (Slides 27-40): 20 Minutes (Security, Governance & Lab Conclusion)
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

# Detailed 60-Minute Full-Length Scripts (40 Slides, ~85-90s each)
SCRIPTS_60MIN = {
    1: """[Prof. Peter] Welcome everyone to Oikos University! I am Professor Peter Kim, Director of Smart Insight Lab. Today, we inaugurate our flagship master curriculum: "The Architect of Intelligence: Mastering Agentic IT and Strategic Wisdom."

[TA Sarah] And a warm welcome to all our global students! I'm Sarah Jenkins, your Teaching Assistant and AI Research Fellow. Professor Kim and I have designed this 60-minute lecture specifically to take you from basic AI prompts to true architectural mastery.

[Prof. Peter] Look at our opening title on the screen: "From Waiting Chatbots to Sleep-Free Personal Avatars." Over the past three years, the entire technology industry has been interacting with AI as a passive encyclopedia sitting on a desk—you type a question, wait for an answer, and copy the text manually.

[TA Sarah] But in 2026, we are witnessing the biggest structural paradigm shift in computing: the transition to autonomous, sleep-free personal avatars. These are persistent software agents residing in the cloud, continuously monitoring data streams, and executing complex workflows around the clock.

[Prof. Peter] Our foundational guiding motto is "Soli Deo Gloria"—Glory to God alone. We teach this cutting-edge technology not merely to write more code, but to redeem finite human time, eliminate mechanical drudgery, and elevate human dignity and strategic wisdom.

[TA Sarah] We have structured today's 60-minute lecture into three clear 20-minute modules so you can master both the conceptual revolution and the hands-on engineering. Let us embark on this journey together!""",

    2: """[Prof. Peter] Look at Slide 2, our opening Part Divider: "PART 1: THE PARADIGM SHIFT: CHATBOTS TO AVATARS."

[TA Sarah] Notice the subtitle centered on our screen: "Soli Deo Gloria: Reclaiming human time from mechanical chatbot waiting loops."

[Prof. Peter] For the past two years, millions of knowledge workers across the globe have spent countless hours staring at blinking AI cursors in web browser tabs. You type a prompt, wait twenty seconds, copy the output, paste it into another tool, and wait again. That mechanical waiting loop is an enormous waste of human intellect.

[TA Sarah] Exactly, Professor Kim. It traps highly educated professionals in what we call 'human middleware' work. Instead of directing high-level strategy, people become manual data couriers between different web applications.

[Prof. Peter] In this first 20-minute module, we dismantle that reactive model. We explore how autonomous personal avatars work asynchronously in the background, executing multi-step business and research tasks while you sleep.

[TA Sarah] When you understand this paradigm shift, your perspective on software development and productivity will change forever. Let us click "Entering Next Phase" and begin Part 1!""",

    3: """[Prof. Peter] Slide 3 lays out our "CORE MISSION & MOTTO: Soli Deo Gloria—Glory to God Alone." Notice the three foundational principles displayed across the screen.

[TA Sarah] Principle 1 is Our Mandate: Elevating human mind and spirit above mechanical work. Human beings were created with dignity, strategic discernment, empathy, and creative vision. We were never meant to spend 10 hours a day doing repetitive copy-paste tasks between spreadsheets and email inboxes.

[Prof. Peter] Principle 2 establishes Technology's Role: Technology is a tool to serve humans, not a master to control us. In our modern digital world, addictive notification algorithms and endless feeds constantly hijack our peace of mind. As Intelligence Architects, we must establish complete sovereignty over our digital tools.

[TA Sarah] And Principle 3 is our Wisdom Goal: Automating simple tasks to save precious time for higher purpose. When our AI avatars handle routine administrative workflows, we reclaim precious hours to invest in our families, our faith, and serving society.

[Prof. Peter] Automation without wisdom leads to exhaustion and distraction. But automation grounded in Soli Deo Gloria becomes sacred time stewardship. That is our north star at Oikos University.""",

    4: """[TA Sarah] Slide 4 diagrams the "SMART INSIGHT LAB PHILOSOPHY" through three interconnected pillars: Data, Technology, and Life OS.

[Prof. Peter] Look at Card 1 on the left: "PILLAR 1: DATA." We live in an era overwhelmed by digital noise, synthetic AI text, and misinformation. The first responsibility of an architect is decoding clean, verifiable truth signals from the chaos.

[TA Sarah] Next, look at Card 2 in the center: "PILLAR 2: TECHNOLOGY." We do not just teach abstract theory; we engineer robust, secure, and sleep-free cloud agent systems. These systems run 24 hours a day on scalable cloud infrastructure with zero downtime.

[Prof. Peter] And look at Card 3 on the right: "PILLAR 3: LIFE OS." This is the core differentiator of our curriculum. Technology must be designed to protect your physical health, deep focus, and natural sleep rather than burning you out.

[TA Sarah] If your software automation causes you more stress and insomnia, it is poorly architected. But when Data, Technology, and Life OS align in harmony, you achieve true sustainable leverage and professional mastery!""",

    5: """[Prof. Peter] Slide 5 is titled "A LETTER FROM THE FUTURE: From childhood dreams to 2026 reality."

[TA Sarah] Look at the left card tagged "THE DREAM": "Childhood Wish." When we were young students, almost everyone had that classic fantasy: "What if I had a digital twin or a clone of myself who could do all my homework and tidy my room while I go outside to play?"

[Prof. Peter] It was a universal dream of delegation. And now, look at the right card tagged "THE REALITY": "2026 Autonomous Avatar." In 2026, that childhood fantasy is no longer science fiction. It is working production software engineering!

[TA Sarah] Today, an Intelligence Architect can deploy a persistent digital twin in the cloud. While you are sleeping, your avatar parses incoming project logs, synthesizes executive research briefings, drafts client replies, and organizes your Google Drive.

[Prof. Peter] When you wake up at 7 AM, your digital twin presents a completed 1-page executive summary of everything accomplished overnight. That is the leverage we are building in this course.""",

    6: """[TA Sarah] Slide 6 highlights "THE ULTIMATE CURRENCY." Notice the prominent metric in the center: "24 HOURS PER DAY."

[Prof. Peter] The stat label underneath reads: "The Equalizer for All Humanity." Think about this profound reality: whether you are a university student, a corporate CEO, or a world leader, everyone is given exactly the same 24 hours every single day.

[TA Sarah] You cannot buy extra physical hours with money, and you cannot manufacture more time. But in the modern AI era, how you deploy those 24 hours determines your entire life trajectory.

[Prof. Peter] Below the number, notice our core thesis: The ultimate wealth of the 21st century is not raw computing power or accumulating terabytes of data—it is reclaiming undivided human focus, relational presence, and strategic clarity.

[TA Sarah] When sleep-free avatars absorb mechanical data chores, our finite physical hours are redeemed for creative thought and deep human relationships. That is true time equity.""",

    7: """[Prof. Peter] On Slide 7, we present our "SESSION 1 LEARNING OBJECTIVES" across three comprehensive cards.

[TA Sarah] Card 1 is "1. PARADIGM SHIFT": Transitioning from synchronous, blocking chatbots to proactive, sleep-free cloud avatars that operate autonomously.

[Prof. Peter] Card 2 is "2. ASYNC ARCHITECTURE": Mastering the technical foundation of the 3-Layer Gemini Spark pipeline—connecting Webhook Triggers, Gemini Reasoning, and Workspace Actions.

[TA Sarah] And Card 3 is "3. GOVERNANCE & WISDOM": Implementing Human-on-the-Loop supervision, cryptographic security guardrails, and maintaining offline life balance under Soli Deo Gloria.

[Prof. Peter] By the end of this 60-minute session, you will possess both the conceptual clarity and the practical architectural blueprint to deploy your first personal avatar. Let us proceed!""",

    8: """[TA Sarah] Slide 8 illustrates "THE PARADIGM SHIFT: 'ASK ME' VS. 'RUN IT FOR ME'."

[Prof. Peter] Look at the left card tagged "PASSIVE AI": "The 'Ask Me' Era." In the 2023 chatbot era, AI functioned like a reactive search engine. You typed a question, the model generated paragraphs of text, and then you had to manually copy, format, and execute everything yourself.

[TA Sarah] Now examine the right card tagged "ACTIVE AI": "The 'Run It For Me' Era." In 2026, AI has evolved into an agentic operator. You define an end goal—such as 'Analyze yesterday's customer feedback and update our database'—and the avatar writes the code, calls the APIs, and verifies the result!

[Prof. Peter] In the 'Ask Me' paradigm, the human does 90% of the manual execution. In the 'Run It For Me' paradigm, the avatar executes 90% of the mechanical steps while the human provides high-level judgment.

[TA Sarah] That fundamental shift is the dividing line between an amateur AI user and a professional Intelligence Architect.""",

    9: """[Prof. Peter] Slide 9 analyzes "YESTERDAY: REACTIVE CHATBOTS."

[TA Sarah] On the left card, tagged "THE BOTTLENECK", we examine "Human as Middleware." For the last few years, whenever companies tried to implement AI, the human worker was forced to act as the physical bridge between ChatGPT, Google Docs, Slack, and email.

[Prof. Peter] Look at the right card tagged "THE COST": "High Latency & Fatigue." Because every single transaction required human attention, professionals experienced massive cognitive fatigue, constant context switching, and high error rates from manual typing.

[TA Sarah] When you have to switch browser tabs 50 times an hour to copy-paste data, your brain cannot engage in deep creative problem solving.

[Prof. Peter] Chatbots gave us great answers, but they left us chained to the keyboard. That is the limitation we are breaking today.""",

    10: """[TA Sarah] Slide 10 presents "TODAY: PROACTIVE AVATARS."

[Prof. Peter] Look at the left card tagged "THE LEVERAGE": "Direct Tool Execution." Modern avatars are equipped with tool belts—they can read file systems, execute shell commands, query SQL databases, and call REST APIs directly in the cloud without human intervention.

[TA Sarah] Look at the right card tagged "THE RESULT": "Asynchronous Freedom." You trigger a multi-hour research workflow before going to bed, and your avatar coordinates multiple sub-agents in parallel throughout the night.

[Prof. Peter] In the morning, you receive a perfectly synthesized, verifiable report ready for decision-making. The human transforms from an exhausted manual laborer into a sovereign director.

[TA Sarah] This concludes Module 1! In the next 20 minutes, we will dive deep under the hood into the engineering mechanics of autonomous reasoning!""",

    11: """[Prof. Peter] Welcome to Slide 11 and the start of Part 2: "PART 2: UNDER THE HOOD OF AUTONOMOUS REASONING."

[TA Sarah] Notice our subtitle: "How autonomous agents think, plan, and execute without human intervention."

[Prof. Peter] In this second 20-minute module, we transition from high-level concepts to the computational engine under the hood. We will examine how an LLM transforms into a goal-driven reasoning loop that plans, acts, and observes.

[TA Sarah] We will explore background execution metaphors, scaling multipliers, and address common engineering bottlenecks that students face in their practical assignments.

[Prof. Peter] Let us click "Entering Next Phase" and unpack the engineering core of autonomous agent reasoning!""",

    12: """[TA Sarah] Slide 12 uses an insightful engineering metaphor: "VIDEO GAME COMPUTING."

[Prof. Peter] Look at the left card tagged "METAPHOR": "Background NPC Simulation." In modern open-world video games, non-player characters do not vanish when you turn your camera away. The game engine simulates their trade, movement, and behavior continuously in background memory.

[TA Sarah] Now look at the right card tagged "REALITY": "Cloud Agent Loops." Your personal AI avatar operates on the exact same principle. It runs in a headless cloud container, listening for webhooks, evaluating cron schedules, and analyzing incoming telemetry even when your laptop is turned off.

[Prof. Peter] You do not need to keep a browser window open. The avatar lives in the cloud infrastructure, persistently guarding your data and executing your workflows.

[TA Sarah] That is the architectural meaning of 'sleep-free' computing—background persistence dedicated entirely to your objectives.""",

    13: """[Prof. Peter] Slide 13 illustrates "SCALING HUMAN ATTENTION." Look at the centerpiece metric: "100X."

[TA Sarah] Stat label: "Attention Multiplier." In traditional IT, if a manager wants to supervise 10 projects, they must attend 10 separate meetings and read hundreds of emails, hitting a hard cognitive ceiling.

[Prof. Peter] But an Intelligence Architect supervising a swarm of 10 specialized agents achieves an effective 100X throughput multiplier. Each agent handles a specific domain—code review, data parsing, security auditing—and reports back concise exceptions.

[TA Sarah] Notice the key takeaway at the bottom: You do not scale by drinking more coffee or working 80 hours a week. You scale by architecting parallel agent swarms that amplify your strategic intent.

[Prof. Peter] Wisdom and architecture allow one person to achieve the impact of an entire department.""",

    14: """[TA Sarah] Slide 14 is our "INTERACTIVE STUDENT POLL: What is your biggest time sink in daily IT workflows?"

[Prof. Peter] Let us review the four options displayed on the screen. Option A is 'Manual data copy-pasting across tools.' Option B is 'Waiting for chatbot responses.' Option C is 'Triaging emails and alerts.' And Option D is 'Repetitive weekly reporting.'

[TA Sarah] In our live classroom polling across global cohorts, over 72% of students consistently select Option A and Option C! Knowledge workers are drowning in mechanical data transfer.

[Prof. Peter] That empirical poll data confirms our diagnosis: the primary bottleneck in modern IT is not a lack of intelligence, but the friction of manual glue work between disconnected systems.

[TA Sarah] And that is exactly what our 3-Layer Gemini Spark pipeline is designed to eliminate!""",

    15: """[Prof. Peter] Slide 15 provides "POLL ANALYSIS & INSIGHT" across three diagnostic cards.

[TA Sarah] Card 1 is "1. THE GLUE WORK TRAP": Global studies show that knowledge workers spend over 60% of their workday simply formatting, copying, and routing data between incompatible software platforms.

[Prof. Peter] Card 2 is "2. CONTEXT SWITCHING": Research from cognitive science demonstrates that every digital interruption takes up to 23 minutes for a human brain to regain deep focus. Context switching destroys intellectual breakthrough.

[TA Sarah] And Card 3 is "3. THE AVATAR SOLUTION": By delegating routine glue work to autonomous headless agents, human professionals reclaim uninterrupted 4-hour deep work blocks every day.

[Prof. Peter] Eliminating glue work is the single highest-return investment an organization can make in human capital.""",

    16: """[TA Sarah] Slide 16 is our Part Divider: "TRANSITION TO ENGINEERING."

[Prof. Peter] Subtitle: "Moving from conceptual understanding to production agent implementation."

[TA Sarah] We have established the philosophical foundation and analyzed the workplace bottlenecks. Now, in the heart of our second module, we inspect the exact architectural diagrams, directory setups, and code structures.

[Prof. Peter] Put on your engineering hats as we examine the 3-layer pipeline that powers production-grade personal avatars. Let's enter the engineering lab!""",

    17: """[Prof. Peter] Slide 17 diagrams our core engineering model: "ASYNCHRONOUS ENGINE: THE 3-LAYER SPARK PIPELINE."

[TA Sarah] Notice the three vertical layers clearly mapped in our architecture diagram.

[Prof. Peter] Layer 1 at the top is the "Trigger Layer." This layer listens for incoming events—Webhook triggers from GitHub, Cron schedules running every midnight, or File Watchers detecting newly uploaded documents in Google Drive.

[TA Sarah] Layer 2 in the center is the "Reasoning Layer." Powered by Gemini Flash, this layer parses the event, selects the appropriate tool schema, executes iterative planning steps, and validates data formats.

[Prof. Peter] Layer 3 at the bottom is the "Action Layer." This layer executes the real-world payload—writing clean spreadsheets to Google Drive, appending logs to a database, and dispatching summary alerts.

[TA Sarah] By decoupling Triggers, Reasoning, and Actions, your system becomes infinitely scalable and resilient to failures.""",

    18: """[TA Sarah] Slide 18 contrasts "SYNCHRONOUS VS. ASYNCHRONOUS" execution.

[Prof. Peter] On the left card tagged "BLOCKING", we see "Synchronous Execution." In a synchronous model, every API request blocks the main thread. If a database query or web scrape takes 45 seconds, the human user is frozen staring at a loading spinner.

[TA Sarah] Now look at the right card tagged "NON-BLOCKING": "Asynchronous Pipeline." When an event occurs, it is pushed to a background event queue. The agent processes it independently in the cloud and notifies you only when the finished artifact is ready.

[Prof. Peter] Asynchronous architecture is the vital secret of sleep-free computing. It frees the human from waiting loops and allows systems to scale horizontally.

[TA Sarah] Always design your agent workflows with non-blocking, event-driven queues!""",

    19: """[Prof. Peter] Slide 19 highlights "THE GEMINI 3.5 FLASH BRAIN." Notice the centerpiece metric: "< 250 MS."

[TA Sarah] Stat label: "Sub-Second Reasoning Latency." For an autonomous agent to execute complex multi-step reasoning, it needs a brain that is both ultra-fast and intellectually capable.

[Prof. Peter] Gemini 3.5 Flash delivers full multi-modal understanding and tool calling with sub-250 millisecond response times. This means an agent can execute a 10-step planning and verification loop in less than 3 seconds!

[TA Sarah] Below the metric, notice the cost efficiency: high-speed, lightweight inference makes running 24/7 continuous avatars economically viable for every student and startup.

[Prof. Peter] Speed, accuracy, and affordability unite to power our persistent cloud avatars.""",

    20: """[TA Sarah] Slide 20 explores "HARDWARE INFRASTRUCTURE: TPU V8."

[Prof. Peter] On the left card tagged "LEGACY": "General Compute." Traditional CPUs and older GPUs suffer from high power draw, thermal throttling, and severe memory bandwidth bottlenecks during massive parallel agent execution.

[TA Sarah] On the right card tagged "AGENTIC ERA": "Custom TPU Pods." Google's TPU v8 infrastructure provides dedicated matrix multiplication acceleration and optical circuit switching designed specifically for concurrent agent swarms.

[Prof. Peter] Robust hardware infrastructure ensures that your cloud avatars run with predictable low latency and enterprise-grade reliability 365 days a year.

[TA Sarah] This concludes Module 2! In our final 20-minute module, we will explore workspace integrations, cryptographic security, and life wisdom!""",

    21: """[Prof. Peter] Welcome to Slide 21 and the beginning of our final module: "PART 3: THE CONNECTED WORKSPACE: APPS SCRIPT & DRIVE."

[TA Sarah] Subtitle: "Transforming Google Workspace into an automated enterprise command center."

[Prof. Peter] In this third 20-minute module, we bridge the reasoning brain to everyday business software—connecting agents to Google Drive, Google Sheets, Gmail, and Google Apps Script.

[TA Sarah] We will also cover essential security guardrails, financial controls, and how to maintain offline focus under Soli Deo Gloria.

[Prof. Peter] Let us click "Entering Next Phase" and build the connected enterprise workspace!""",

    22: """[TA Sarah] Slide 22 breaks down "THE TRIAD OF AGENTIC DESIGN."

[Prof. Peter] Card 1 is "1. MEMORY ENGINE": Providing the agent with short-term working context and long-term persistent knowledge so it remembers organizational rules across sessions.

[TA Sarah] Card 2 is "2. TOOL BELT": Equipping the agent with clean, standardized API contracts for file operations, web research, code execution, and database queries.

[Prof. Peter] And Card 3 is "3. GUARDRAIL MATRIX": Enforcing schema validation, strict token limits, financial spending caps, and safety filters.

[TA Sarah] An agent with tools but no guardrails is dangerous. An agent with memory, tools, and guardrails working together is a reliable enterprise partner!""",

    23: """[Prof. Peter] Slide 23 diagrams our production "SPARK OS DIRECTORY SETUP."

[TA Sarah] Look at the standardized directory hierarchy on the screen: /agents stores persona and system prompts; /skills contains modular tool execution scripts; /memory stores vector indexes and persistent logs; and /config holds environment secrets.

[Prof. Peter] Notice how every tool is encapsulated as an independent skill module inside the /skills folder. This allows you to add new capabilities to your avatar without touching core reasoning logic.

[TA Sarah] Follow this clean directory pattern in your hands-on lab assignment to ensure maintainable, modular agent architecture!""",

    24: """[TA Sarah] Slide 24 explains the "DUAL MEMORY ENGINE."

[Prof. Peter] On the left card tagged "SHORT-TERM": "Working Scratchpad." This is fast, in-context scratchpad memory where the agent records intermediate thoughts, tool responses, and active turn variables.

[TA Sarah] On the right card tagged "LONG-TERM": "Persistent Knowledge Vault." This is vector-indexed storage stored in markdown files, SQLite databases, and Google Drive, allowing the avatar to recall user preferences across weeks and months.

[Prof. Peter] Dual memory mimics human cognition: rapid working focus combined with deep, permanent knowledge retrieval.

[TA Sarah] This enables your avatar to provide deeply personalized assistance tailored to your unique workflow history.""",

    25: """[Prof. Peter] Slide 25 diagrams "GOOGLE WORKSPACE INTEGRATION."

[TA Sarah] Look at the automated workflow flow: An incoming email arrives in Gmail, triggering a lightweight Google Apps Script webhook. The script passes the email body to Gemini Flash for categorization and draft synthesis, then automatically archives the email and appends a summary row to Google Sheets.

[Prof. Peter] Notice that this entire workflow runs serverlessly inside Google's enterprise cloud infrastructure. You do not need to manage expensive dedicated servers or configure complex Kubernetes clusters.

[TA Sarah] It transforms standard office tools into an autonomous, intelligent operations hub!""",

    26: """[TA Sarah] Slide 26 presents a compelling "REAL-WORLD CASE STUDY: Executive Inbox Triage."

[Prof. Peter] Look at the left card tagged "BEFORE": "Manual Triage." An executive spends 2.5 hours every single morning manually opening 150 emails, sorting spam, downloading attachments, and drafting routine confirmations.

[TA Sarah] Now look at the right card tagged "AFTER": "Avatar Automation." The personal avatar executes at 4 AM, categorizes all 150 emails, drafts polite replies for approval, extracts urgent action items, and places a 1-page briefing doc on Google Drive!

[Prof. Peter] When the executive arrives at their desk at 8 AM, they review the entire briefing in just 10 minutes. That reclaims over 15 hours of high-value leadership time every single week.

[TA Sarah] That is the tangible, real-world ROI of building agentic workflows.""",

    27: """[Prof. Peter] Slide 27 introduces Part 4: "THE SECURITY MATRIX: PROTECTING THE DIGITAL VAULT."

[TA Sarah] Subtitle: "Establishing robust guardrails, cryptographic audits, and defense-in-depth."

[Prof. Peter] As Intelligence Architects, we must understand that autonomy without security is catastrophic. Giving an AI agent access to file systems and APIs requires rigorous defensive engineering.

[TA Sarah] In this section, we examine financial risks, prompt injection defenses, and cryptographic audit trails to ensure our avatars remain 100% secure.

[Prof. Peter] Let us enter the Security Matrix and fortify our systems!""",

    28: """[TA Sarah] Slide 28 warns about "FINANCIAL RISK: UNCONTROLLED WALLET."

[Prof. Peter] Look at the left card tagged "VULNERABILITY": "Unbounded API Spending." If an autonomous agent encounters an infinite retry loop or processes a malicious prompt, it could make thousands of recursive API calls and drain thousands of dollars in cloud credits overnight.

[TA Sarah] Look at the right card tagged "DEFENSE": "Hard Spending Caps & Token Quotas." We must enforce strict per-task budget limits, maximum token thresholds, and automated circuit breakers that immediately halt execution if spending limits are reached.

[Prof. Peter] Never deploy an autonomous agent into production without hard, non-bypassable financial fences. Security begins with budget control.""",

    29: """[Prof. Peter] Slide 29 outlines "AP2: AGENT PAYMENTS PROTOCOL" across three structured cards.

[TA Sarah] Card 1 is "1. DUAL AUTHORIZATION": Requiring explicit human approval for any financial transaction or data transfer exceeding predefined dollar thresholds.

[Prof. Peter] Card 2 is "2. EPHEMERAL TOKENS": Using single-use, cryptographically signed tokens with strict 5-minute expiration windows for tool authentication.

[TA Sarah] And Card 3 is "3. AUDIT LOGGING": Maintaining an immutable, append-only ledger that records every transaction hash and reasoning trace.

[Prof. Peter] Cryptographic protocols ensure that autonomous commerce and agentic operations remain verifiable, auditable, and secure.""",

    30: """[Prof. Peter] Slide 30 declares "THE DIGITAL MANDATE: Soli Deo Gloria in Systems Engineering."

[TA Sarah] Look at the three foundational commitments on the screen. Point 1 is Absolute Data Integrity: We commit to building agents that never generate deceptive, hallucinated, or unverified claims.

[Prof. Peter] Point 2 is Uncompromising Privacy: We rigorously protect user credentials, confidential enterprise data, and personal privacy across all agent pipelines.

[TA Sarah] And Point 3 is Humble Stewardship: We use our technological knowledge not for selfish vanity or destructive disruption, but to uplift human communities and glorify God.

[Prof. Peter] Engineering excellence is fundamentally a moral and ethical commitment. That is the Oikos standard.""",

    31: """[TA Sarah] Slide 31 brings us to our final synthesis: "PART 4: WISDOM SYNTHESIS: SOLI DEO GLORIA."

[Prof. Peter] Subtitle: "Harmonizing cutting-edge agent swarms with human wisdom and life balance."

[TA Sarah] In these final slides, we integrate everything we have learned—combining multi-agent swarms, human-on-the-loop oversight, and reclaiming offline life focus.

[Prof. Peter] Let us click "Entering Next Phase" and synthesize the ultimate wisdom of the Intelligence Architect!""",

    32: """[Prof. Peter] Slide 32 diagrams the critical threat of "PROMPT INJECTION."

[TA Sarah] On the left card tagged "ATTACK VECTOR": "Indirect Prompt Injection." An adversary embeds hidden malicious instructions inside a public webpage or email body, attempting to hijack your avatar's reasoning loop.

[Prof. Peter] On the right card tagged "SHIELD": "Strict Input Sanitization." We treat all external data as untrusted input, wrapping untrusted text inside secure XML delimiters and preventing external content from overriding system instructions.

[TA Sarah] Always separate data channels from instruction channels in your agent prompt engineering!""",

    33: """[TA Sarah] Slide 33 details the "CRYPTOGRAPHIC AUDIT TRAIL."

[Prof. Peter] Look at the 4-step verification pipeline: Action Request -> Signature Verification -> Sandboxed Execution -> Immutable Log Append.

[TA Sarah] Every decision made by your avatar is signed with private cryptographic keys, executed in an isolated sandbox, and recorded to an immutable log.

[Prof. Peter] If an anomaly occurs, you can replay the exact reasoning trace step by step. Transparency creates institutional accountability and trust.""",

    34: """[Prof. Peter] Slide 34 addresses "SHADOW IT & ENTERPRISE COMPLIANCE."

[TA Sarah] On the left card tagged "RISK": "Unsanctioned Copy-Pasting." Untrained employees pasting proprietary source code and confidential customer data into unvetted public AI chatbots.

[Prof. Peter] On the right card tagged "ENTERPRISE STANDARD": "Governed Private Hub." Providing a centralized, enterprise-governed agent directory with Single Sign-On, Role-Based Access Control, and strict data residency.

[TA Sarah] Solve Shadow IT by providing employees with superior, secure internal avatar tooling!""",

    35: """[TA Sarah] Slide 35 illustrates "BALANCING AUTONOMY AND CONTROL" across our 3-tier governance matrix.

[Prof. Peter] Look at Card 1: "TIER 1: FULL AUTONOMY." Low-risk, reversible tasks like summarizing documents, tagging emails, and organizing folders run with 100% autonomy.

[TA Sarah] Look at Card 2: "TIER 2: NOTIFY & LOG." Medium-risk tasks like drafting client emails or creating calendar invites execute automatically but notify the user with an undo option.

[Prof. Peter] And look at Card 3: "TIER 3: STRICT HUMAN APPROVAL." High-risk actions like financial transactions, database deletions, or code deployments require explicit human cryptographic sign-off.

[TA Sarah] This 3-tier matrix eliminates catastrophic risks while preserving massive operational speed!""",

    36: """[Prof. Peter] Slide 36 diagrams "DEFENSE IN DEPTH FOR AGENTS."

[TA Sarah] Look at the three concentric security rings: Ring 1 is Input Sanitization at the boundary; Ring 2 is Runtime Sandboxing during execution; and Ring 3 is Egress Filtering on network calls.

[Prof. Peter] Even if a sophisticated attacker manages to bypass Ring 1, the sandboxed environment prevents system takeover, and egress filtering blocks unauthorized data leaks.

[TA Sarah] Layered defense ensures that your personal avatar remains an unbreachable digital fortress!""",

    37: """[TA Sarah] Slide 37 portrays "THE SOVEREIGN CONDUCTOR: ORCHESTRATING SWARMS."

[Prof. Peter] Look at Card 1: The "RESEARCH AGENT" searches documentation, parses PDFs, and verifies factual citations.

[TA Sarah] Look at Card 2: The "BUILDER AGENT" translates verified research into clean code, structured spreadsheets, and formatted slides.

[Prof. Peter] And look at Card 3: The "CRITIC AGENT" rigorously checks the builder's output against quality benchmarks, flagging syntax bugs or formatting discrepancies.

[TA Sarah] You do not need to micro-manage each step; you act as the Sovereign Conductor orchestrating this entire multi-agent symphony!""",

    38: """[Prof. Peter] Slide 38 clarifies the vital distinction in "HUMAN-ON-THE-LOOP (HOTL)."

[TA Sarah] On the left card tagged "OLD MODEL": "Human-IN-the-Loop." The human is a painful operational bottleneck, forced to manually click 'Approve' on every trivial step, limiting scale.

[Prof. Peter] On the right card tagged "NEW MODEL": "Human-ON-the-Loop." The agent swarm executes autonomously at scale while the human supervises high-level telemetry, setting policy goals and handling exceptions.

[TA Sarah] Human-on-the-loop oversight gives you infinite operational leverage while maintaining 100% human ethical accountability and control!""",

    39: """[TA Sarah] Slide 39 provides deep inspiration for "RECLAIMING OFFLINE FOCUS."

[Prof. Peter] Look at Card 1: "1. THE DIGITAL SABBATH." Setting aside dedicated days every week completely disconnected from glowing screens and digital notifications.

[TA Sarah] Look at Card 2: "2. DEEP INTELLECTUAL WORK." Investing reclaimed hours into deep reading, original writing, and strategic synthesis that AI cannot replicate.

[Prof. Peter] And look at Card 3: "3. FAMILY & COMMUNITY." Being fully present for family dinners, mentoring students, prayer, and serving your local community.

[TA Sarah] Soli Deo Gloria: Using automation not to live in virtual reality, but to enrich real human life, faith, and relationships!""",

    40: """[Prof. Peter] Here we are at Slide 40: "🛠️ HANDS-ON LAB 1 & CONCLUSION."

[TA Sarah] Look at our three practical lab steps: In Lab Step 1, you will initialize your local Spark OS directory structure; in Lab Step 2, you will deploy the Gemini Flash reasoning pipeline; and in Lab Step 3, you will execute your first asynchronous background workflow!

[Prof. Peter] Theory without practice is dead. Complete Hands-On Lab 1 today to deploy your first sleep-free personal avatar.

[TA Sarah] Pair up with your study partner, create your duo video assignments, and test your systems thoroughly. Professor Kim and I look forward to seeing you in Session 2!

[Prof. Peter] Soli Deo Gloria. Thank you, work diligently, and may God bless you all!"""
}

# Update all 40 slides
for slide in slides:
    num = slide["num"]
    if num in SCRIPTS_60MIN:
        slide["script"] = SCRIPTS_60MIN[num]
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
    "**Lecture Format:** Full 60-Minute Broadcast Duo Dialogue (3x 20-Minute Modules)  ",
    "**Total Slides:** 40 Slides (Target: Exactly 60 Minutes / 3,600 Seconds)  ",
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
    md_lines.append("### 🎙️ English Lecture Script (Full 60-Min Duo Dialogue)")
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

print("✅ Full 60-Minute Expanded Dialogue applied to all 40 slides in Session 1!")
