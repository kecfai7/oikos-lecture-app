# -*- coding: utf-8 -*-
"""
60-Minute Master Duo Script Generator for Session 1 (40 Slides)
Target Total Audio Duration: Exactly 58-60 Minutes (~3500-3600 Seconds)
Features:
- Prof. Peter Kim (Authentic Voice) & TA Sarah Jenkins (31, AI Fellow)
- Deep, engaging, conversational dialogue designed for global students.
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

# 40 Slides - Expanded 60-Minute Full Dialogue Dataset
SESSION_1_60MIN_SLIDES = [
    {
        "num": 1,
        "type": "title",
        "title": "OIKOS UNIVERSITY • SOLI DEO GLORIA",
        "subtitle": "THE ARCHITECT OF INTELLIGENCE: Mastering Agentic IT & Strategic Wisdom",
        "detail": "Session 1: From Waiting Chatbots to Sleep-Free Personal Avatars",
        "instructor": "Prof. Peter Kim (Lead) & TA Sarah Jenkins (Fellow) • Smart Insight Lab",
        "script": """[Prof. Peter] Welcome everyone to Oikos University! I am Professor Peter Kim, Director of the Smart Insight Lab. It is my immense joy and honor to open Session 1 of our landmark master course: "The Architect of Intelligence: Mastering Agentic IT and Strategic Wisdom."

[TA Sarah] And a warm welcome to all of our incredible students joining us from across the globe! I am Sarah Jenkins, your Teaching Assistant and AI Research Fellow at the Smart Insight Lab. Professor Kim and I will be your co-pilots throughout this entire semester.

[Prof. Peter] Look at the central theme on our screen: "From Waiting Chatbots to Sleep-Free Personal Avatars." For the past three years, the entire world interacted with AI like a digital encyclopedia sitting on a desk. You had to sit down, type a prompt, wait for an answer, and manually copy-paste the output.

[TA Sarah] Exactly, Professor Kim! But in 2026, we are witnessing the single greatest architectural revolution in computer science history. AI has transformed from a passive chatbot into an active, autonomous avatar—a digital co-worker that runs persistently in the cloud 24 hours a day, 7 days a week, even while you sleep!

[Prof. Peter] That is why our course motto is "Soli Deo Gloria"—Glory to God alone. We do not build technology merely to be consumed by screens. We architect intelligent systems to redeem our time, eliminate mechanical drudgery, and elevate human dignity and creativity. Let us embark on this transformative 60-minute journey together!""",
        "koreanGuide": {
            "summary": "Session 1 강의 오프닝: 챗봇에서 슬립프리 자율 아바타로의 패러다임 대전환 및 60분 오리엔테이션",
            "points": [
                "2인 교수진 소개: 피터 킴 교수(54세, 총괄 디렉터) & 사라 젠킨스 조교(31세, AI 연구 펠로우)",
                "수동적 챗봇(Passive Chatbot)에서 24/7 클라우드 상주형 자율 아바타(Personal Avatar)로의 진화",
                "Soli Deo Gloria 정신: 기계적 반복 노동 해방 및 인간 고유의 창조적 시간 회복"
            ],
            "tips": "피터 교수와 사라 조교가 활기찬 핑퐁 대화로 전세계 학생들을 따뜻하게 맞이하며 60분 강의의 비전을 제시합니다."
        },
        "keyTerms": [
            {"term": "Architect of Intelligence", "def": "A strategist who designs, governs, and orchestrates autonomous AI agent systems.", "defKo": "지능 건축가 (에이전트 시스템 설계자)"},
            {"term": "Sleep-Free Personal Avatar", "def": "A persistent cloud-resident agent that executes complex workflows autonomously 24/7.", "defKo": "슬립프리 개인 아바타 (24시간 지속 자율 에이전트)"}
        ]
    },
    {
        "num": 2,
        "type": "split",
        "title": "TRADITIONAL CODER VS. INTELLIGENCE ARCHITECT",
        "subtitle": "Moving from manual code writing to strategic agent orchestration and systems design",
        "leftCard": {
            "tag": "PAST MODEL",
            "title": "The Traditional Coder",
            "points": [
                "Writes syntax line by line inside local IDEs.",
                "High mental fatigue from debugging syntax errors.",
                "Stuck in the reactive feedback loop of prompts."
            ]
        },
        "rightCard": {
            "tag": "2026 PARADIGM",
            "title": "The Intelligence Architect",
            "points": [
                "Designs multi-agent workflows and high-level logic.",
                "Directs specialized agent swarms with governance.",
                "Focuses on strategic decision-making and business value."
            ]
        },
        "script": """[Prof. Peter] Slide 2 defines the fundamental identity shift you will undergo in this course. Look at the stark contrast on our screen: The Traditional Coder on the left versus The Intelligence Architect on the right.

[TA Sarah] Professor Kim, when I was in graduate school, we spent eighty percent of our waking hours hunting down missing semicolons, debugging package conflicts, and writing boilerplate code line by line. It was exhausting!

[Prof. Peter] Indeed, Sarah. The traditional coder is bound to the syntax layer. But as an Intelligence Architect in 2026, you operate at the conceptual and architectural layer. You do not spend hours typing repetitive syntax; you direct specialized AI agent swarms to write, test, and verify the code for you.

[TA Sarah] Look at the right card: The Intelligence Architect defines the data flow, establishes strict security guardrails, and evaluates the final business outcome. You are no longer just a typist; you are the master engineer orchestrating a team of digital workers.

[Prof. Peter] This shift elevates your productivity by more than a hundredfold. But more importantly, it shifts your mind from low-level mechanical labor to high-level strategic wisdom.""",
        "koreanGuide": {
            "summary": "전통적 코더에서 지능 건축가로의 진화: 문법 타이핑에서 멀티 에이전트 오케스트레이션으로",
            "points": [
                "전통적 코더: 구문 디버깅과 보일러플레이트 작성에 80% 이상의 인지 자원 소모",
                "지능 건축가: 시스템 아키텍처 설계, 보안 가드레일 설정, 비즈니스 가치 평가에 집중",
                "100배 이상의 생산성 혁신과 전략적 사고로의 도약"
            ],
            "tips": "사라 조교가 대학원 시절의 코딩 피로 경험을 나누고, 피터 교수가 건축가로서의 시각 전환을 격려합니다."
        },
        "keyTerms": [
            {"term": "Traditional Coder", "def": "A software developer who manually writes and debugs source code line by line.", "defKo": "전통적 코더 (수동 구문 작성자)"},
            {"term": "Intelligence Architect", "def": "An engineer who orchestrates autonomous agents and designs overarching AI systems.", "defKo": "지능 건축가 (에이전트 시스템 아키텍트)"}
        ]
    }
]

print("Master 60-Minute Slide Dataset module ready.")
