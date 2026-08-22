# -*- coding: utf-8 -*-
"""
Oikos University - Session 10 Clean 45-Slide Master Generator
Course: The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom
Session 10: Escaping Developer Gravity: Antigravity 2.0 & Multi-Agent Orchestration Blueprint
Features:
- Full 45 Slides with 3-Presenter Trio (Prof. Peter Kim, TA Sarah Jenkins, TA James Wilson)
- Clean 4-Part Structure (Part 1: Slide 2, Part 2: Slide 12, Part 3: Slide 23, Part 4: Slide 30)
- 5 Practical Enterprise Case Studies:
    1. Slide 11: Legacy 500,000-Line Monolith Modernization via 93-Agent Swarm
    2. Slide 22: Autonomous Full-Stack SaaS Generation in 12 Hours
    3. Slide 29: Stopping a Malicious Dependency Injection via RDD Diff Gate
    4. Slide 36: 24/7 Self-Healing CI/CD Swarm Resolves 120 Broken Builds
    5. Slide 44: 35X Enterprise Engineering Velocity ROI Blueprint
- Full sync with session10.md and slidesData.js (SLIDES_SESSION_10)
"""

import json
import re
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Oikos Univ"
SLIDES_DATA_JS = os.path.join(BASE_DIR, "src", "data", "slidesData.js")
SESSION10_MD = os.path.join(BASE_DIR, "session10.md")

SLIDES_45_SESSION_10 = [
    # Slide 1: Course Title
    {
        "num": 1,
        "type": "title",
        "title": "OIKOS UNIVERSITY • SOLI DEO GLORIA",
        "subtitle": "THE ARCHITECT OF INTELLIGENCE: Mastering Agentic IT & Strategic Wisdom",
        "detail": "Session 10: Escaping Developer Gravity: Antigravity 2.0 & Multi-Agent Orchestration Blueprint",
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab",
        "script": (
            "[Prof. Peter] Welcome back, global scholars and architects, to Oikos University! I am Professor Peter Kim, Director of Smart Insight Lab. Today on Slide 1, we enter the pinnacle of autonomous software engineering: \"Session 10: Escaping Developer Gravity: Antigravity 2.0 & Multi-Agent Orchestration Blueprint.\"\n\n"
            "[TA Sarah] Hello everyone! I am Sarah Jenkins, Senior AI Fellow. For decades, software developers have been crushed by 'Developer Gravity'—the heavy friction of boilerplate syntax, dependency conflicts, unit test debugging, and manual code refactoring.\n\n"
            "[TA James] And I am James Wilson, your DevOps TA! Google Antigravity 2.0 shatters developer gravity forever: powered by a 150MB native Go CLI (`agy`), a high-concurrency multi-agent swarm architecture that spawns 93 specialized subagents in parallel, and Review-Driven Development (RDD) with structured Artifacts!\n\n"
            "[Prof. Peter] Under our founding motto, \"SOLI DEO GLORIA—To God Alone Be the Glory,\" let us transition from mechanical code typists into sovereign conductors of autonomous intelligence fleets.\n\n"
            "[TA Sarah] Let us open Part 1 and explore the Rise of 93-Agent Swarms on Slide 2!"
        ),
        "koreanGuide": {
            "summary": "Session 10 개요 및 Oikos University 3인 강사진(피터 교수, 사라 수석조교, 제임스 개발조교) 환영 인사",
            "points": [
                "강의 주제: 개발자 중력 탈출: Antigravity 2.0과 93개 자율 에이전트 스웜 오케스트레이션",
                "수작업 코딩의 중력(보일러플레이트, 의존성 지옥, 테스트 작성)에서 벗어나 시스템 총괄 지휘관으로 도약",
                "Go 언어 기반 150MB 초경량 agy CLI 및 Review-Driven Development(RDD) 아티팩트 거버넌스"
            ],
            "tips": "피터 교수의 지휘관 패러다임과 사라 조교의 스웜 협업 구조, 제임스 조교의 고동시성 엔지니어링 에너지를 결합하세요."
        },
        "keyTerms": [
            {
                "term": "Developer Gravity",
                "def": "The cumulative friction of routine boilerplate, debugging, syntax errors, and administrative drag that slows software development.",
                "defKo": "개발자 중력 (코딩 마찰력)"
            },
            {
                "term": "Google Antigravity 2.0",
                "def": "Google's flagship multi-agent software engineering environment executing autonomous planning, coding, and verification swarms.",
                "defKo": "구글 안티그래비티 2.0 (Antigravity 2.0)"
            }
        ]
    },
    # Slide 2: Part 1 Section Divider
    {
        "num": 2,
        "type": "section",
        "title": "PART 1: THE RISE OF 93-AGENT SWARMS",
        "subtitle": "Transcending single-threaded coding to orchestrate massive parallel AI specialist fleets under Soli Deo Gloria",
        "script": (
            "[TA Sarah] Look at Slide 2: \"PART 1: THE RISE OF 93-AGENT SWARMS.\" Professor, why is single-assistant coding obsolete in 2026?\n\n"
            "[Prof. Peter] Because asking a single AI chatbot to rewrite a 100,000-line codebase is like asking one lone carpenter to build a 50-story skyscraper! It gets confused, runs out of memory, and drops requirements.\n\n"
            "[TA James] In Antigravity 2.0, we spawn a coordinated swarm: 1 Lead Architect, 30 Feature Coders, 20 Unit Testers, 15 Security Auditors, 10 UI Browser Testers, and 5 Documentation Writers—all working concurrently across isolated git worktrees!\n\n"
            "[TA Sarah] In Part 1, we deconstruct the transition from typing lines of code to conducting system swarms.\n\n"
            "[Prof. Peter] Let us examine the heavy shackle of traditional coding gravity on Slide 3."
        ),
        "koreanGuide": {
            "summary": "Part 1 섹션 전환: 93개 자율 에이전트 스웜의 부상과 단일 챗봇의 종말",
            "points": [
                "단일 챗봇의 한계: 10만 줄 코드베이스를 혼자 리팩토링하다 기억상실과 환각에 빠지는 목수 1명의 한계",
                "93개 분산 에이전트 스웜: 아키텍트, 피처 코더, 테스터, 보안 감사관, 브라우저 테스터가 병렬 동시 작업",
                "격리된 깃 워크트리(Git Worktree)에서 동시 협업을 수행하는 자율 엔지니어링 군단"
            ],
            "tips": "사라 조교가 1인 목수 대 50층 빌딩 비유를 짚고 제임스가 93개 역할 분담의 위력을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Agent Swarm Concurrency",
                "def": "The simultaneous execution of specialized subagents working on decoupled sub-tasks across isolated workspaces.",
                "defKo": "에이전트 스웜 동시성"
            },
            {
                "term": "Git Worktree Isolation",
                "def": "Allocating separate filesystem working trees for each active agent to prevent git merge collisions during parallel development.",
                "defKo": "깃 워크트리 작업 격리"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 3: The Heavy Shackle of Traditional Coding Gravity
    {
        "num": 3,
        "type": "content",
        "title": "THE HEAVY SHACKLE OF TRADITIONAL CODING GRAVITY",
        "subtitle": "How senior engineers waste 75% of their careers on mechanical boilerplate and debugging",
        "points": [
            "Boilerplate Drain: Writing repetitive CRUD routers, DTO schemas, and SQL migrations by hand.",
            "Dependency Hell: Spending entire afternoons debugging version conflicts between npm and pip packages.",
            "Testing Drag: Writing 500 unit tests manually rather than focusing on novel algorithmic breakthroughs."
        ],
        "script": (
            "[Prof. Peter] Slide 3 exposes \"THE HEAVY SHACKLE OF TRADITIONAL CODING GRAVITY.\"\n\n"
            "[TA Sarah] Look at where senior software engineers spend their actual working hours: only 20% is creative architecture! The remaining 80% is spent wrestling with import errors, writing repetitive JSON serializers, and fixing broken unit tests!\n\n"
            "[TA James] That is computational servitude! Antigravity 2.0 delegates 100% of the mechanical boilerplate to autonomous subagent swarms, freeing human architects to operate at the level of pure systems design!\n\n"
            "[Prof. Peter] Let us examine the great transition from writer to system director on Slide 4."
        ),
        "koreanGuide": {
            "summary": "전통적 코딩 중력의 족쇄: 시니어 엔지니어의 80% 시간 낭비 실태",
            "points": [
                "보일러플레이트 노역: 반복적인 CRUD 라우터, DTO 스키마, SQL 마이그레이션 수작업 타이핑",
                "의존성 지옥: 패키지 버전 충돌과 라이브러리 비호환성 디버깅에 오후 전체를 낭비",
                "지능 해방: 기계적 잡무를 100% 에이전트 스웜에 위임하고 인간은 순수 시스템 설계에만 집중"
            ],
            "tips": "사라 조교와 제임스 조교가 80%의 기계적 노역에서 해방되는 통쾌함을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Computational Servitude",
                "def": "The squandering of high-level human intellectual capacity on routine, repetitive syntactic implementation tasks.",
                "defKo": "컴퓨팅 노역 (반복 코딩 낭비)"
            },
            {
                "term": "Pure Systems Design",
                "def": "Focusing engineering intellect strictly on architectural topology, security boundaries, and core business invariants.",
                "defKo": "순수 시스템 아키텍처 설계"
            }
        ]
    },
    # Slide 4: The Great Transition: Writer to System Director
    {
        "num": 4,
        "type": "comparison",
        "title": "THE GREAT TRANSITION: WRITER TO DIRECTOR",
        "subtitle": "Evolving from a syntax typist into the Sovereign Conductor of an AI engineering orchestra",
        "leftCard": {
            "tag": "CODE WRITER (LEGACY)",
            "title": "Syntax Typist",
            "points": [
                "Types code line-by-line in IDE.",
                "Memorizes language syntax & library quirks.",
                "Spends 4 hours debugging missing semicolons.",
                "Max throughput: 200 lines of code per day."
            ]
        },
        "rightCard": {
            "tag": "SYSTEM DIRECTOR (2026)",
            "title": "Sovereign Conductor",
            "points": [
                "Authorizes architecture via `implementation_plan.md`.",
                "Spawns 93 subagents to execute in parallel.",
                "Audits code diffs & verified test runs.",
                "Max throughput: 50,000 lines of verified code per day."
            ]
        },
        "script": (
            "[TA Sarah] Slide 4 details \"THE GREAT TRANSITION: WRITER TO SYSTEM DIRECTOR.\"\n\n"
            "[TA James] In the old world, an elite engineer typed 200 lines of clean code a day. In Antigravity 2.0, you act like a Movie Director or an Orchestra Conductor! You write the vision, approve the `implementation_plan.md`, and direct 93 subagents that produce 50,000 lines of verified, audited code in a single day!\n\n"
            "[Prof. Peter] The baton in your hand is the power of intentional direction. You are no longer typing the notes; you are conducting the symphony!\n\n"
            "[TA Sarah] Let us inspect the democratization of creation on Slide 5."
        ),
        "koreanGuide": {
            "summary": "위대한 대전환: 코드 타이피스트에서 시스템 총괄 지휘관(Director)으로",
            "points": [
                "과거: 하루 200줄의 코드를 타이핑하며 세미콜론과 문법 오류에 4시간을 허비하던 시절",
                "현재: implementation_plan.md로 비전을 제시하고 93개 서브에이전트를 지휘해 하루 5만 줄의 검증된 코드 생산",
                "오케스트라 지휘자 비유: 악보의 음표를 하나씩 연주하는 연주자에서 전체 교향악단을 이끄는 지휘자로 도약"
            ],
            "tips": "제임스 조교의 지휘자 비유와 피터 교수의 교향악단 은유를 살려 생동감 있게 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Sovereign Conductor Paradigm",
                "def": "The engineering discipline where human architects direct, audit, and approve autonomous multi-agent software swarms.",
                "defKo": "주권적 총괄 지휘관 패러다임"
            },
            {
                "term": "Implementation Plan Artifact",
                "def": "A formal technical design document specifying task scope, modified files, and verification steps before execution.",
                "defKo": "구현 계획 아티팩트 (implementation_plan.md)"
            }
        ]
    },
    # Slide 5: Reclaiming 30% Cognitive Space from Boilerplate
    {
        "num": 5,
        "type": "content",
        "title": "RECLAIMING COGNITIVE CAPACITY",
        "subtitle": "Eliminating cognitive fatigue to focus on novel algorithms, domain wisdom, and business strategy",
        "points": [
            "Cognitive Offloading: Delegating unit test generation, typing annotations, and Dockerfiles to agents.",
            "Deep Work Expansion: Sustaining 4-hour uninterrupted blocks of pure architectural problem-solving.",
            "Higher-Order Value: Shifting from 'How do I write this loop?' to 'What is the highest ethical value of this system?'"
        ],
        "script": (
            "[Prof. Peter] Slide 5 explores \"RECLAIMING COGNITIVE CAPACITY.\"\n\n"
            "[TA Sarah] When you no longer have to spend your mental energy worrying about Python syntax errors or CSS flexbox alignments, your brain enters a state of profound flow!\n\n"
            "[TA James] You can spend 4 unbroken hours thinking about distributed consensus algorithms, zero-knowledge security proofs, and user experience psychology!\n\n"
            "[Prof. Peter] That is how we cultivate true wisdom in technological leadership.\n\n"
            "[TA Sarah] Let us inspect Assistants vs. Agents on Slide 6."
        ),
        "koreanGuide": {
            "summary": "인지 용량의 회수: 기계적 보일러플레이트 제거와 깊은 몰입(Deep Work)",
            "points": [
                "인지적 위임: 단위 테스트, 타입 주석, 도커파일 작성을 서브에이전트에 100% 위임",
                "딥워크 확장: 문법 오류의 방해 없이 4시간 연속으로 고차원 분산 합의 알고리즘에 몰입",
                "고차원 가치 질문: '이 루프를 어떻게 짜지?'에서 '이 시스템이 사람들을 어떻게 이롭게 할까?'로 전환"
            ],
            "tips": "사라 조교와 피터 교수가 인지 용량 회수가 가져오는 깊은 몰입의 기쁨을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Cognitive Offloading",
                "def": "Delegating routine mechanical tasks to automated agents to preserve human focus for high-order reasoning.",
                "defKo": "인지적 작업 위임 (Cognitive Offloading)"
            },
            {
                "term": "High-Order Systems Thinking",
                "def": "Evaluating holistic architecture, ethical implications, and security invariants rather than low-level code mechanics.",
                "defKo": "고차원 시스템 사고"
            }
        ]
    },
    # Slide 6: Defining the Boundary: Assistants vs. Agents
    {
        "num": 6,
        "type": "comparison",
        "title": "DEFINING THE BOUNDARY: ASSISTANTS VS. AGENTS",
        "subtitle": "Why autocomplete code completion (Copilot) is fundamentally inferior to autonomous swarms (Antigravity)",
        "leftCard": {
            "tag": "CODE ASSISTANT (COPILOT)",
            "title": "Passive Autocomplete",
            "points": [
                "Suggests next 3 lines of code as you type.",
                "Zero execution capability (cannot run tests).",
                "Blind to external files & terminal errors.",
                "Human remains the mechanical typist."
            ]
        },
        "rightCard": {
            "tag": "AUTONOMOUS SWARM (ANTIGRAVITY)",
            "title": "Active Execution Fleet",
            "points": [
                "Reads whole repository & plans multi-file diffs.",
                "Executes shell commands & runs unit tests.",
                "Diagnoses runtime errors & self-heals bugs.",
                "Human acts as the reviewing Director."
            ]
        },
        "script": (
            "[TA Sarah] Slide 6 clarifies \"THE BOUNDARY: CODE ASSISTANTS VS. AUTONOMOUS AGENTS.\"\n\n"
            "[TA James] Do not confuse code autocomplete with Antigravity! Autocomplete assistants like legacy Copilot just guess the next 5 words as you type. They cannot run tests, they cannot edit 10 files at once, and they cannot read terminal errors!\n\n"
            "[Prof. Peter] Antigravity 2.0 is an Autonomous Agent Fleet! It plans the task, creates new files, runs compilers, captures browser screenshots, fixes its own compilation errors in a self-healing loop, and presents a completed walkthrough!\n\n"
            "[TA Sarah] Let us launch an interactive poll on Slide 7!"
        ),
        "koreanGuide": {
            "summary": "경계의 정의: 단순 코드 어시스턴트(Copilot) vs 자율 에이전트 스웜(Antigravity)",
            "points": [
                "어시스턴트(Copilot): 타이핑 시 다음 3줄을 추천하는 수동적 자동완성 (테스트 실행 불가, 전체 파악 불가)",
                "자율 스웜(Antigravity): 전체 리포지토리 분석, 터미널 컴파일러 실행, 브라우저 스크린샷 캡처, 자가 치유(Self-healing) 완결",
                "보조 도구에서 자율 동료로의 질적 도약"
            ],
            "tips": "제임스 조교가 자동완성과 자율 에이전트의 질적 차이를 명쾌하게 선을 그어줍니다."
        },
        "keyTerms": [
            {
                "term": "Passive Autocomplete",
                "def": "Inline text completion models predicting tokens without environmental execution or self-verification capabilities.",
                "defKo": "수동적 코드 자동완성"
            },
            {
                "term": "Autonomous Self-Healing Loop",
                "def": "The continuous cycle of writing code, running compilers/tests, diagnosing failures, and automatically fixing errors.",
                "defKo": "자율 자가 치유 루프"
            }
        ]
    },
    # Slide 7: Interactive Poll: Your Biggest Software Bottleneck
    {
        "num": 7,
        "type": "poll",
        "title": "📨 INTERACTIVE POLL: SOFTWARE BOTTLENECKS",
        "subtitle": "Which stage of enterprise software engineering slows down your team the most?",
        "pollOptions": [
            "Option A: Upgrading legacy frameworks & migrating deprecated dependencies",
            "Option B: Writing comprehensive end-to-end integration and browser tests",
            "Option C: Reviewing massive 2,000-line pull requests for subtle security bugs",
            "Option D: Setting up cloud infrastructure, CI/CD pipelines, and Docker containers"
        ],
        "script": (
            "[Prof. Peter] Slide 7 is our \"INTERACTIVE POLL: SOFTWARE BOTTLENECKS.\" Grab your phones and vote right now!\n\n"
            "[TA Sarah] The question is: \"Which phase of enterprise software engineering creates the most exhausting bottleneck for your engineering team?\"\n\n"
            "[TA James] Option A: Upgrading legacy codebases. Option B: Writing end-to-end browser tests. Option C: Reviewing 2,000-line pull requests. Or Option D: Debugging CI/CD pipelines!\n\n"
            "[TA Sarah] Option A (Legacy Upgrades) and Option B (Testing) are surging across our live audience!\n\n"
            "[Prof. Peter] Let us examine how Antigravity swarms solve every one of these bottlenecks on Slide 8."
        ),
        "koreanGuide": {
            "summary": "실시간 수강생 설문: 엔터프라이즈 소프트웨어 엔지니어링의 최대 병목은?",
            "points": [
                "수강생 실시간 참여를 통한 소프트웨어 개발 수명주기(SDLC)의 주요 병목 진단",
                "레거시 프레임워크 업그레이드, E2E 브라우저 테스트, 거대 PR 코드 리뷰, CI/CD 파이프라인 중 최대 병목 식별",
                "Antigravity 2.0 스웜이 해결할 실제 엔터프라이즈 과제 확인"
            ],
            "tips": "3인의 강사진이 수강생들의 공감대를 형성하며 Part 2 내부 메커니즘으로 이끕니다."
        },
        "keyTerms": [
            {
                "term": "SDLC Bottleneck",
                "def": "A stage in the software development lifecycle that constrains overall engineering delivery velocity.",
                "defKo": "SDLC 개발 수명주기 병목"
            },
            {
                "term": "Legacy Modernization Drag",
                "def": "The heavy technical debt and risk associated with updating aging enterprise software architectures.",
                "defKo": "레거시 현대화 기술 부채"
            }
        ]
    },
    # Slide 8: Analyzing the Poll: Elevating to Architecture
    {
        "num": 8,
        "type": "content",
        "title": "ANALYZING THE POLL: ELEVATING TO ARCHITECTURE",
        "subtitle": "How multi-agent parallel swarms turn multi-month bottlenecks into multi-minute victories",
        "points": [
            "Legacy Migrations: Spawning 40 subagents to refactor 500 decoupled modules simultaneously.",
            "Testing Automation: Browser subagents automatically navigating web pages and recording WebP failure videos.",
            "Continuous Verification: Automated linters and security auditors reviewing every line before human inspection."
        ],
        "script": (
            "[TA Sarah] Slide 8 analyzes our poll results: \"ELEVATING TO ARCHITECTURE.\"\n\n"
            "[TA James] Look at how swarming crushes these bottlenecks: Instead of 1 engineer spending 6 months migrating 500 microservices, Antigravity spawns 40 subagents to refactor all 500 services in parallel in 25 minutes!\n\n"
            "[Prof. Peter] Browser subagents launch real Chrome instances, click buttons, take screenshots, and record WebP videos of bugs automatically! You spend your time reviewing high-level results rather than manually clicking buttons.\n\n"
            "[TA Sarah] Let us inspect Part 1 takeaways on Slide 10."
        ),
        "koreanGuide": {
            "summary": "설문 분석: 다중 에이전트 병렬 스웜을 통한 수개월 병목의 수분 내 해결",
            "points": [
                "레거시 마이그레이션: 40개 서브에이전트가 500개 모듈을 동시 병렬 리팩토링 (6개월 ➔ 25분)",
                "브라우저 테스트 자동화: 브라우저 서브에이전트가 크롬을 띄워 버튼을 클릭하고 WebP 버그 비디오 자동 녹화",
                "지속적 사전 검증: 린터와 보안 감사 에이전트가 인간 검토 전 모든 코드를 1차 전수 검증"
            ],
            "tips": "사라 조교와 제임스 조교가 6개월 걸리던 대규모 마이그레이션이 25분 만에 끝나는 스웜의 위력을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Parallel Module Refactoring",
                "def": "Deconstructing monolithic codebases and updating independent packages simultaneously via concurrent AI agents.",
                "defKo": "병렬 모듈 동시 리팩토링"
            },
            {
                "term": "Automated WebP Session Recording",
                "def": "Capturing lightweight animated video proof of browser interactions to verify UI functionality deterministically.",
                "defKo": "WebP 브라우저 세션 자동 녹화"
            }
        ]
    },
    # Slide 9: Mastering the Conductor's Baton: 4 Rules
    {
        "num": 9,
        "type": "content",
        "title": "MASTERING THE CONDUCTOR'S BATON: 4 RULES",
        "subtitle": "The 4 golden rules of directing autonomous AI agent swarms",
        "points": [
            "Rule 1: Clear Boundaries (Define explicit task scopes and file boundaries in the implementation plan).",
            "Rule 2: Verification Invariants (Require automated compilers, linters, and unit tests to pass before review).",
            "Rule 3: Artifact Inspection (Read the diffs, check screenshots, and audit walkthrough summaries).",
            "Rule 4: Sovereign Veto (Reject any plan or code mutation that violates enterprise architectural standards)."
        ],
        "script": (
            "[Prof. Peter] Slide 9 presents \"MASTERING THE CONDUCTOR'S BATON: 4 GOLDEN RULES.\"\n\n"
            "[TA Sarah] Rule 1: Set clear boundaries—never tell an agent 'Fix everything'; give explicit file scopes! Rule 2: Require verification invariants—compilers and unit tests must pass 100%.\n\n"
            "[TA James] Rule 3: Inspect the Artifacts—read the `walkthrough.md` and check the git diff! Rule 4: Exercise your Sovereign Veto—if an agent proposes an ugly hack, reject the plan and direct it to build an elegant architecture!\n\n"
            "[Prof. Peter] Let us examine our first enterprise case study on Slide 11!"
        ),
        "koreanGuide": {
            "summary": "지휘관의 지휘봉 마스터하기: 자율 에이전트 스웜 지휘 4대 황금률",
            "points": [
                "규칙 1 (명확한 경계): '알아서 다 고쳐'가 아닌 명확한 대상 파일과 작업 범위 한정",
                "규칙 2 (검증 불변 원칙): 컴파일러, 린터, 단위 테스트 100% 통과를 사전 필수 조건화",
                "규칙 3 (아티팩트 감사): walkthrough.md 요약과 git diff 코드를 꼼꼼히 확인",
                "규칙 4 (주권적 거부권): 우아하지 못한 임시변통(Hack) 코드는 단호히 거부하고 재작성 지시"
            ],
            "tips": "3인의 강사진이 지휘관의 4대 수칙을 단호하고 권위 있게 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Sovereign Veto",
                "def": "The human director's ultimate authority to reject, modify, or abort agent execution plans at any stage.",
                "defKo": "주권적 거부권 (Sovereign Veto)"
            },
            {
                "term": "Verification Invariant",
                "def": "A strict non-negotiable quality condition (zero lint errors, 100% test pass) required before code merges.",
                "defKo": "검증 불변 원칙"
            }
        ]
    },
    # Slide 10: Part 1 Transition: Under the Hood of Antigravity 2.0
    {
        "num": 10,
        "type": "content",
        "title": "PART 1 TRANSITION: ENTERING THE ENGINE ROOM",
        "subtitle": "Connecting swarm philosophy to Go binary internals, subagent roles, and the Self-Evolving Loop",
        "points": [
            "From Vision to Mechanics: How does a single CLI coordinate 93 agents without crashing system memory?",
            "The Self-Evolving Loop: Agents compiling new tools and plugins to expand their own capabilities.",
            "The Roadmap Ahead: Master Go internals in Part 2, CLI commands in Part 3, and RDD governance in Part 4."
        ],
        "script": (
            "[Prof. Peter] Slide 10 bridges our roadmap: \"PART 1 TRANSITION: ENTERING THE ENGINE ROOM.\"\n\n"
            "[TA Sarah] We have seen the power of the Conductor. But how does Antigravity 2.0 actually coordinate 93 subagents under the hood without crashing your laptop?\n\n"
            "[TA James] The secret is a 150MB native Go binary, lightweight subagent message buses, and the miraculous 'Self-Evolving Loop'—where agents write and compile their own subagent tools!\n\n"
            "[Prof. Peter] Let us examine our first enterprise case study on Slide 11!"
        ),
        "koreanGuide": {
            "summary": "Part 1 전환: 안티그래비티 2.0 엔진룸 진입 (Go 바이너리와 자가 진화 루프)",
            "points": [
                "비전에서 메커니즘으로: 단일 CLI가 메모리 폭발 없이 어떻게 93개 에이전트를 조율하는가?",
                "자가 진화 루프(Self-Evolving Loop): 에이전트가 스스로 새로운 도구와 플러그인을 컴파일해 역량 확장",
                "Part 2~4 로드맵 제시: Go 엔진 내부 ➔ agy CLI 마스터 ➔ RDD 거버넌스"
            ],
            "tips": "제임스 조교가 150MB Go 바이너리와 자가 진화 루프의 마법을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Self-Evolving Loop",
                "def": "The capability of AI agent systems to generate, compile, test, and register new tools dynamically during runtime.",
                "defKo": "자가 진화 루프 (Fairy Making Fairy)"
            },
            {
                "term": "Native Binary Orchestrator",
                "def": "A high-performance compiled executable (Go) managing agent concurrency with minimal runtime overhead.",
                "defKo": "네이티브 바이너리 오케스트레이터"
            }
        ]
    },
    # Slide 11: Case Study 1: Legacy 500K-Line Monolith Modernization
    {
        "num": 11,
        "type": "casestudy",
        "title": "CASE STUDY 1: 500K-LINE MONOLITH MODERNIZATION",
        "subtitle": "Fintech Enterprise modernizes 15-year-old 500,000-line legacy Java monolith in 72 hours using 93-Agent Swarm",
        "company": "Top-10 Global Financial Clearing House",
        "problem": "Company ran a 500,000-line Java 8 monolithic codebase with 2,400 deprecated APIs and zero integration tests; manual modernization was estimated at 18 months and $6.5M.",
        "solution": "Deployed Antigravity 2.0: Lead Architect spawned 60 subagents to refactor modules, 20 subagents to write JUnit tests, and 13 browser subagents to verify admin UIs.",
        "impact": "Completed 100% Java 21 migration in 72 hours; achieved 94% automated test coverage; saved $6.2M in engineering fees; zero production incidents.",
        "script": (
            "[Prof. Peter] Slide 11 presents \"CASE STUDY 1: 500,000-LINE MONOLITH MODERNIZATION.\" Look at this staggering enterprise victory!\n\n"
            "[TA Sarah] A global financial clearing house was trapped on an ancient 500,000-line Java 8 monolith with 2,400 deprecated API calls and almost zero automated tests. External consulting firms estimated 18 months and 6.5 million dollars to modernize it!\n\n"
            "[TA James] They launched Antigravity 2.0: The Lead Architect agent created an AST dependency map and spawned 60 subagents to refactor modules to modern Java 21, 20 subagents to generate JUnit tests, and 13 browser subagents to verify the admin web dashboards in parallel!\n\n"
            "[Prof. Peter] In just 72 hours over a single weekend, the entire 500,000-line codebase was modernized, tested with 94% code coverage, and deployed to production with zero regressions—saving 6.2 million dollars!\n\n"
            "[TA Sarah] That proves the reality of escaping developer gravity.\n\n"
            "[TA James] Now let us open Part 2 and look Under the Hood of Antigravity 2.0 on Slide 12!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 1: 50만 줄 금융 청산소 자바 8 레거시를 72시간 만에 자바 21로 전면 현대화",
            "points": [
                "문제 상황: 2,400개 폐기 API가 얽힌 50만 줄 레거시, 컨설팅 견적 18개월 및 650만 달러",
                "솔루션: 안티그래비티 2.0 스웜 가동(모듈 리팩토링 60명, JUnit 테스트 20명, UI 검증 13명 동시 투입)",
                "성과: 주말 72시간 만에 자바 21 전환 완료, 테스트 커버리지 94% 달성, 620만 달러 절감, 배포 장애 0건"
            ],
            "tips": "사라 조교와 제임스 조교가 18개월 걸릴 프로젝트가 주말 72시간 만에 끝난 스웜 혁신을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Monolithic Modernization",
                "def": "The systematic architectural refactoring of legacy enterprise codebases to modern frameworks and language versions.",
                "defKo": "모놀리식 레거시 전면 현대화"
            },
            {
                "term": "High-Concurrency Refactoring",
                "def": "Decomposing large codebases to allow dozens of AI agents to update independent packages in parallel.",
                "defKo": "고동시성 병렬 리팩토링"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 12: Part 2 Section Divider
    {
        "num": 12,
        "type": "section",
        "title": "PART 2: UNDER THE HOOD OF ANTIGRAVITY 2.0",
        "subtitle": "Go-based 150MB engine, split-view workspaces, subagent roles, and the Self-Evolving Loop",
        "script": (
            "[TA Sarah] Look at Slide 12: \"PART 2: UNDER THE HOOD OF ANTIGRAVITY 2.0.\" Now we deconstruct the mechanical engine room!\n\n"
            "[Prof. Peter] Antigravity 2.0 is built with profound engineering discipline. It eschews bloated electron shells in favor of a lean, ultra-fast Go binary that orchestrates subagents with microsecond precision.\n\n"
            "[TA James] In Part 2, we explore the Self-Evolving Loop (요정이 요정을 만드는 기적), the 150MB native engine, the Mission Control split-view workspace, and the specialized subagent roles (Coder, Reviewer, Browser)!\n\n"
            "[TA Sarah] Let us inspect the Self-Evolving Loop on Slide 13!"
        ),
        "koreanGuide": {
            "summary": "Part 2 섹션 전환: 안티그래비티 2.0의 내부 아키텍처 해부",
            "points": [
                "Go 언어 기반 150MB 초경량 네이티브 엔진의 극단적 성능과 마이크로초 단위 스케줄링",
                "자가 진화 루프: 요정이 요정을 만드는 기적(에이전트가 새로운 에이전트 도구를 동적 생성)",
                "미션 컨트롤 분할 뷰(Split-View)와 전문 서브에이전트 역할 분담(Coder, Reviewer, Browser)"
            ],
            "tips": "피터 교수가 군더더기 없는 Go 바이너리 철학을 선언하고 제임스가 3대 서브에이전트 역할을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Go-Based Engine",
                "def": "A compiled 150MB executable delivering high-concurrency goroutine scheduling and zero-runtime dependency.",
                "defKo": "Go 기반 네이티브 엔진"
            },
            {
                "term": "Split-View Mission Control",
                "def": "The unified IDE interface displaying conversational planning, live terminal execution, and rendered artifacts simultaneously.",
                "defKo": "분할 뷰 미션 컨트롤"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 13: The Self-Evolving Loop: 요정이 요정을 만드는 기적
    {
        "num": 13,
        "type": "content",
        "title": "THE SELF-EVOLVING LOOP: 요정이 요정을 만드는 기적",
        "subtitle": "How AI agents dynamically author, compile, and register custom subagent skills at runtime",
        "points": [
            "The Meta-Agent Principle: An agent discovers it lacks a specific tool (e.g., parsing binary protobuf files).",
            "Autonomous Tool Generation: The agent writes a new Python/Go utility, compiles it, and registers it in `skills/`.",
            "Instant Capability Expansion: The subagent fleet immediately inherits the new skill in the next execution turn."
        ],
        "script": (
            "[Prof. Peter] Slide 13 reveals \"THE SELF-EVOLVING LOOP: 요정이 요정을 만드는 기적 (The Miracle of Fairies Creating Fairies).\"\n\n"
            "[TA Sarah] This is one of the most astonishing breakthroughs in Antigravity 2.0: When an agent encounters a problem it has no tool for—like parsing an obscure binary satellite telemetry format—it does not give up!\n\n"
            "[TA James] It writes a new Python or Go parser script, creates a `SKILL.md` specification with YAML frontmatter, compiles it, and registers it in the `.agents/skills/` directory! In the very next turn, the entire 93-agent swarm inherits that new capability!\n\n"
            "[Prof. Peter] Software that extends its own capabilities under human architectural direction is true agentic evolution.\n\n"
            "[TA Sarah] Let us inspect the ultra-lightweight Go engine on Slide 14."
        ),
        "koreanGuide": {
            "summary": "자가 진화 루프: 요정이 요정을 만드는 기적 (런타임 스킬 동적 생성)",
            "points": [
                "메타 에이전트 원리: 특수 바이너리나 새로운 포맷 처리 도구가 없음을 감지해도 멈추지 않음",
                "자율 도구 생성: 파이썬/Go 스크립트와 YAML 명세가 담긴 SKILL.md를 즉석 작성하고 등록",
                "스웜 전체 역량 즉시 확장: 93개 에이전트 군단 전체가 새로 생성된 스킬을 즉시 공유받아 활용"
            ],
            "tips": "사라 조교와 피터 교수가 '요정이 요정을 만드는 기적'의 감동적 공학 메커니즘을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Skill Dynamic Synthesis",
                "def": "The automated authoring and registration of structured skill packages (SKILL.md) during active problem-solving.",
                "defKo": "스킬 동적 합성 및 등록"
            },
            {
                "term": "Swarm Capability Inheritance",
                "def": "The instantaneous propagation of newly authored tools across all concurrent subagents in an execution session.",
                "defKo": "스웜 역량 즉시 상속"
            }
        ]
    },
    # Slide 14: Ultra-Lightweight CLI: Go-Based 150MB Engine
    {
        "num": 14,
        "type": "content",
        "title": "ULTRA-LIGHTWEIGHT CLI: GO-BASED 150MB ENGINE",
        "subtitle": "Zero-dependency single binary executing subagents in microseconds via lightweight goroutines",
        "points": [
            "Zero Electron Overhead: Replaced 2GB Node/Electron memory footprint with a compiled 150MB native Go binary.",
            "Goroutine Concurrency: Spawning 100 subagent communication channels using less than 50MB of system RAM.",
            "Sub-Millisecond IPC: Direct memory and Unix socket message buses delivering microsecond agent synchronization."
        ],
        "script": (
            "[TA Sarah] Slide 14 details \"ULTRA-LIGHTWEIGHT CLI: GO-BASED 150MB ENGINE.\"\n\n"
            "[TA James] Why is Antigravity 2.0 so fast? Because Google ditched heavy Electron wrappers! The `agy` CLI is written in pure Go, compiled to a single 150MB standalone binary with zero external dependencies!\n\n"
            "[Prof. Peter] It leverages Go's ultra-lightweight Goroutines: spawning 100 subagent communication channels takes only 50 megabytes of RAM and synchronizes across subagents in microseconds!\n\n"
            "[TA Sarah] Let us inspect the Mission Control Split-View Workspace on Slide 15."
        ),
        "koreanGuide": {
            "summary": "초경량 CLI: Go 언어 기반 150MB 네이티브 엔진과 고루틴 동시성",
            "points": [
                "일렉트론 거품 제거: 2GB를 먹던 무거운 런타임을 150MB 단일 정적 바이너리로 완전 대체",
                "고루틴(Goroutine) 초경량 동시성: 100개 서브에이전트 통신 채널을 띄워도 RAM 점유율 50MB 미만",
                "마이크로초 초고속 IPC: 유닉스 소켓과 직접 메모리 버스를 통한 초고속 서브에이전트 동기화"
            ],
            "tips": "제임스 조교가 Go 바이너리와 고루틴의 가벼움이 주는 극단적 성능을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Goroutine Scheduling",
                "def": "Go runtime multiplexing thousands of lightweight concurrent threads over a small pool of OS threads.",
                "defKo": "고루틴 동시성 스케줄링"
            },
            {
                "term": "Static Native Binary",
                "def": "A self-contained executable containing all compiled dependencies, eliminating runtime installation friction.",
                "defKo": "정적 네이티브 바이너리"
            }
        ]
    },
    # Slide 15: The Mission Control: Split-View Workspace
    {
        "num": 15,
        "type": "content",
        "title": "THE MISSION CONTROL: SPLIT-VIEW WORKSPACE",
        "subtitle": "Harmonizing Strategic Planning, Terminal Execution, Code Diffs, and Live Browser Previews",
        "points": [
            "Left Pane: Architectural Planning & Conversational Stream (Reviewing `implementation_plan.md`).",
            "Center Pane: Live Git Code Diffs & Multi-File Mutation Viewer.",
            "Right Top Pane: Sandboxed Shell Execution & Live Compiler Telemetry.",
            "Right Bottom Pane: Headless Browser Preview & Live WebP Video Recording Stream."
        ],
        "script": (
            "[Prof. Peter] Slide 15 diagrams \"THE MISSION CONTROL: SPLIT-VIEW WORKSPACE.\"\n\n"
            "[TA Sarah] In Antigravity IDE, look at your 4-quadrant cockpit: Left pane is your Architectural Plan. Center pane shows live git diffs across all mutated files in real time. Top right shows live compiler terminal logs. And bottom right displays the live browser preview where agents test your web UI!\n\n"
            "[TA James] You have complete, transparent visibility over all 93 subagents simultaneously. Zero blind spots!\n\n"
            "[TA Sarah] Let us inspect the 3 primary subagent roles on Slides 16, 17, and 18!"
        ),
        "koreanGuide": {
            "summary": "미션 컨트롤 분할 뷰: 4개 패널로 구성된 지휘관 콕핏",
            "points": [
                "좌측 패널: 아키텍처 기획 및 대화형 스트림 (implementation_plan.md 검토)",
                "중앙 패널: 실시간 git diff 및 다중 파일 변경 내역 시각화",
                "우측 상단: 샌드박스 터미널 쉘 실행 및 실시간 컴파일러 로그",
                "우측 하단: 헤드리스 브라우저 실시간 렌더링 및 WebP 비디오 녹화 스트림"
            ],
            "tips": "사라 조교와 제임스 조교가 4개 패널의 유기적 배치와 사각지대 없는 관제력을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "4-Quadrant Mission Control",
                "def": "The unified developer cockpit integrating plan review, code diffs, terminal execution, and browser previews.",
                "defKo": "4분할 미션 컨트롤 콕핏"
            },
            {
                "term": "Unified Telemetry Stream",
                "def": "The synchronized visual presentation of multi-agent state mutations in a single responsive interface.",
                "defKo": "통합 텔레메트리 스트림"
            }
        ]
    },
    # Slide 16: Agent Role 1: Coder – The Algorithmic Powerhouse
    {
        "num": 16,
        "type": "content",
        "title": "AGENT ROLE 1: CODER – THE ALGORITHMIC POWERHOUSE",
        "subtitle": "Specialized subagent generating high-performance, strictly-typed implementation code",
        "points": [
            "File-Scoped Precision: Modifies only assigned files without touching unauthorized modules.",
            "AST-Aware Mutations: Uses semantic code replacement tools (`replace_file_content`) to prevent syntax errors.",
            "Strict Type Rigor: Enforces TypeScript, Rust, Go, and Python type hints across all created functions."
        ],
        "script": (
            "[TA Sarah] Slide 16 highlights \"AGENT ROLE 1: CODER – THE ALGORITHMIC POWERHOUSE.\"\n\n"
            "[TA James] The Coder subagent is your pure implementation engine. It receives strict file scopes, parses AST trees, and writes robust, strongly-typed code in TypeScript, Go, or Python. It never touches files outside its assigned boundary!\n\n"
            "[Prof. Peter] Let us inspect Agent Role 2: The Reviewer on Slide 17."
        ),
        "koreanGuide": {
            "summary": "에이전트 역할 1: 코더(Coder) - 알고리즘 구현의 핵심 엔진",
            "points": [
                "파일 범위 한정: 자신에게 할당된 모듈만 수정하고 미인가 파일은 절대 건드리지 않음",
                "AST 기반 정밀 수정: replace_file_content 도구를 사용해 구문 오류 없는 정밀 코드 대체",
                "엄격한 타입 시스템: TypeScript, Rust, Go, Python의 타입 힌트와 불변성을 완벽히 준수"
            ],
            "tips": "제임스 조교가 코더 에이전트의 정밀성과 범위 준수 원칙을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Coder Subagent",
                "def": "A specialized AI agent focused exclusively on authoring and refactoring implementation source code.",
                "defKo": "코더 서브에이전트 (구현 전담)"
            },
            {
                "term": "AST-Aware Code Replacement",
                "def": "Precise string and block replacements that preserve abstract syntax tree validity and indentation.",
                "defKo": "AST 기반 코드 정밀 치환"
            }
        ]
    },
    # Slide 17: Agent Role 2: Reviewer – The Quality Sentinel
    {
        "num": 17,
        "type": "content",
        "title": "AGENT ROLE 2: REVIEWER – THE QUALITY SENTINEL",
        "subtitle": "Independent adversarial subagent auditing code diffs, security flaws, and performance regressions",
        "points": [
            "Adversarial Review: Actively searches for race conditions, SQL injections, and memory leaks in Coder's output.",
            "Automated Veto Power: If a unit test fails or a lint rule triggers, Reviewer sends the code back to Coder with diff notes.",
            "Zero Human Fatigue: Conducts 50 thorough code review iterations before the human director ever looks at the PR."
        ],
        "script": (
            "[Prof. Peter] Slide 17 introduces \"AGENT ROLE 2: REVIEWER – THE QUALITY SENTINEL.\"\n\n"
            "[TA Sarah] The Reviewer is an independent, adversarial subagent! It does NOT trust the Coder! It scans the code diff for race conditions, SQL injection risks, and Big-O performance regressions!\n\n"
            "[TA James] If Reviewer spots a bug, it rejects the code and forces Coder into an internal self-healing loop! It runs 50 adversarial audit cycles in 30 seconds before presenting the clean code to you!\n\n"
            "[Prof. Peter] Let us inspect Agent Role 3: The Browser Tester on Slide 18."
        ),
        "koreanGuide": {
            "summary": "에이전트 역할 2: 리뷰어(Reviewer) - 품질과 보안의 무자비한 보초",
            "points": [
                "적대적 코드 감사: 코더의 결과물을 절대 맹신하지 않고 레이스 컨디션, SQL 인젝션, 메모리 누수 전수 검사",
                "자동 거부권 행사: 린트 에러나 테스트 실패 시 즉각 코더에게 수정 지시를 보내 자가 치유 루프 가동",
                "인간 피로도 제로: 인간 지휘관이 PR을 보기 전에 이미 50번의 엄격한 상호 검증을 30초 만에 완결"
            ],
            "tips": "사라 조교와 피터 교수가 코더와 리뷰어 간의 생산적인 적대적 상호 검증 구조를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Reviewer Subagent",
                "def": "An adversarial auditing agent verifying code quality, security invariants, and test pass rates.",
                "defKo": "리뷰어 서브에이전트 (품질 감사 전담)"
            },
            {
                "term": "Adversarial Code Audit",
                "def": "Rigorous critical inspection assuming implementation code contains hidden defects and actively attempting to trigger failures.",
                "defKo": "적대적 코드 감사"
            }
        ]
    },
    # Slide 18: Agent Role 3: Browser – The Interactive Tester
    {
        "num": 18,
        "type": "content",
        "title": "AGENT ROLE 3: BROWSER – THE INTERACTIVE TESTER",
        "subtitle": "Autonomous Chromium subagent validating UI interactions, responsive layouts, and WebP recordings",
        "points": [
            "Headless Navigation: Spawns real Chrome instances, types forms, clicks buttons, and tests edge-case flows.",
            "Visual Artifact Capture: Takes full-page screenshots and records WebP session videos as proof of functionality.",
            "End-to-End Verification: Verifies that full-stack changes actually work in live web browsers before merging."
        ],
        "script": (
            "[TA Sarah] Slide 18 presents \"AGENT ROLE 3: BROWSER – THE INTERACTIVE TESTER.\"\n\n"
            "[TA James] The Browser subagent controls live headless Chrome instances! It opens your web app, resizes the viewport to test mobile responsiveness, types into search boxes, clicks checkout buttons, and records animated WebP video recordings!\n\n"
            "[Prof. Peter] You don't just see code; you see visual video proof that the feature actually works in a real browser!\n\n"
            "[TA Sarah] Let us inspect our second enterprise case study on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "에이전트 역할 3: 브라우저 테스터(Browser) - E2E 시각적 검증",
            "points": [
                "헤드리스 크롬 실시간 제어: 폼 입력, 버튼 클릭, 뷰포트 조절을 통한 모바일 반응형 완벽 테스트",
                "시각적 아티팩트 증거: 전체 스크린샷과 WebP 세션 비디오를 자동 녹화하여 기능 동작 실증",
                "E2E 최종 검증: 코드가 실제 브라우저에서 문제없이 작동함을 완벽히 확인한 후 머지 승인 요청"
            ],
            "tips": "제임스 조교가 WebP 비디오 녹화를 통한 시각적 무결성 검증의 편리함을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Browser Subagent",
                "def": "An autonomous agent controlling web browser runtimes to execute end-to-end user interface testing.",
                "defKo": "브라우저 서브에이전트 (E2E 테스트 전담)"
            },
            {
                "term": "Visual Proof Artifact",
                "def": "Screenshots and video recordings generated by agents confirming successful feature execution in live runtimes.",
                "defKo": "시각적 검증 증거물"
            }
        ]
    },
    # Slide 19: The 12-Hour Software Breakthrough
    {
        "num": 19,
        "type": "content",
        "title": "THE 12-HOUR SOFTWARE BREAKTHROUGH",
        "subtitle": "Compressing a 6-month full-stack enterprise SaaS sprint into a single 12-hour overnight swarm run",
        "points": [
            "Overnight Swarm Autonomy: Directing a swarm at 8:00 PM; waking up to a complete full-stack SaaS platform at 8:00 AM.",
            "Continuous Verification: Swarm executes 1,200 automated builds, runs 4,000 unit tests, and records 50 browser demos.",
            "The Human Morning Role: Reviewing `walkthrough.md`, auditing diffs, and deploying to cloud production."
        ],
        "script": (
            "[Prof. Peter] Slide 19 diagrams \"THE 12-HOUR SOFTWARE BREAKTHROUGH: Overnight Swarm Velocity.\"\n\n"
            "[TA Sarah] Think about how revolutionary this is: At 8:00 PM, you write your architectural plan. You type `/goal` and launch the Antigravity swarm. While you sleep peacefully, 93 agents execute in parallel!\n\n"
            "[TA James] They run 1,200 builds, generate 4,000 unit tests, fix 80 compilation bugs in self-healing loops, and record 50 browser UI test videos! When you wake up at 8:00 AM with your morning coffee, you read the completed `walkthrough.md` and deploy to Google Cloud in 5 minutes!\n\n"
            "[Prof. Peter] Let us examine our second enterprise case study on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "12시간 소프트웨어 돌파구: 6개월 스프린트를 밤샘 12시간 자율 스웜으로 압축",
            "points": [
                "밤샘 자율 스웜: 저녁 8시에 아키텍처 계획 승인 후 /goal 실행 ➔ 수면 중 93개 에이전트 병렬 작업",
                "지속적 자율 검증: 1,200번 빌드, 4,000개 단위 테스트, 80개 버그 자가 치유, 50개 브라우저 영상 녹화",
                "아침 5분 배포: 모닝커피를 마시며 walkthrough.md와 diff를 최종 승인하고 클라우드 즉시 배포"
            ],
            "tips": "사라 조교와 제임스 조교가 밤샘 자율 개발(Overnight Swarm)이 주는 생산성의 기적을 생생히 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Overnight Swarm Run",
                "def": "The continuous autonomous execution of multi-agent software swarms completing complex feature sets unattended.",
                "defKo": "밤샘 자율 스웜 실행"
            },
            {
                "term": "Walkthrough Artifact",
                "def": "A comprehensive summary document detailing all completed modifications, test results, and visual verification media.",
                "defKo": "결과 보고 워크스루 아티팩트 (walkthrough.md)"
            }
        ]
    },
    # Slide 20: Part 2 Transition: Command Line Mastery
    {
        "num": 20,
        "type": "content",
        "title": "PART 2 TRANSITION: ENTERING COMMAND LINE MASTERY",
        "subtitle": "Connecting swarm architecture to `agy` CLI flags, `/grill-me`, and June 18, 2026 legacy cutoff",
        "points": [
            "Mastering the Tool: Transitioning from GUI buttons to high-speed terminal command orchestration.",
            "Interactive Alignment: Using `/grill-me` to resolve design ambiguities before code execution starts.",
            "The Roadmap Ahead: Master `agy` CLI in Part 3, and Review-Driven Development (RDD) in Part 4."
        ],
        "script": (
            "[Prof. Peter] Slide 20 transitions to our command line control: \"PART 2 TRANSITION: ENTERING COMMAND LINE MASTERY.\"\n\n"
            "[TA Sarah] We understand the architecture. Now, how do we command the swarm from our terminal? Through the official `agy` CLI!\n\n"
            "[TA James] In Part 3, we master essential slash commands like `/grill-me` for interview-driven plan hardening, learn the June 18, 2026 legacy Gemini CLI cutoff, and build custom SDK swarms!\n\n"
            "[Prof. Peter] Let us examine our second enterprise case study on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "Part 2 전환: 커맨드 라인 마스터리로의 진입 (agy CLI 및 /grill-me)",
            "points": [
                "도구의 통달: GUI 클릭을 넘어 고속 터미널 agy 커맨드로 스웜을 전격 지휘",
                "인터뷰 기반 계획 경질화: /grill-me 명령을 통해 코딩 전 설계 불확실성을 완벽 해소",
                "2026년 6월 18일 레거시 Gemini CLI 공식 종료 및 agy 전환 로드맵 예고"
            ],
            "tips": "제임스 조교가 agy CLI 명령어 체계와 /grill-me의 중요성을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "agy CLI Command Suite",
                "def": "The unified terminal interface governing Google Antigravity 2.0 swarms, planning modes, and subagents.",
                "defKo": "agy CLI 명령어 스위트"
            },
            {
                "term": "/grill-me Interview",
                "def": "An interactive slash command where AI rigorously interviews the developer to resolve design decisions before planning.",
                "defKo": "/grill-me 심층 인터뷰 명령어"
            }
        ]
    },
    # Slide 21: Case Study 2: Autonomous Full-Stack SaaS Generation
    {
        "num": 21,
        "type": "casestudy",
        "title": "CASE STUDY 2: AUTONOMOUS FULL-STACK SAAS",
        "subtitle": "Solo Founder builds and launches multi-tenant AI analytics SaaS in 12 hours via Antigravity 2.0 Swarm",
        "company": "Silicon Valley AI Analytics Startup",
        "problem": "Solo founder needed to build a multi-tenant Next.js / FastAPI web app with Stripe billing, PostgreSQL database, and OAuth authentication; traditional MVP cycle was 4 months.",
        "solution": "Launched Antigravity 2.0 swarm with 40 subagents executing planning, backend APIs, frontend React components, and Playwright tests.",
        "impact": "Production SaaS platform deployed in 12 hours; acquired first 100 paying customers on day 2; saved $80,000 in early contractor hiring fees.",
        "script": (
            "[Prof. Peter] Slide 21 presents \"CASE STUDY 2: AUTONOMOUS FULL-STACK SAAS GENERATION.\"\n\n"
            "[TA Sarah] A solo startup founder in San Francisco had a brilliant concept for an AI marketing analytics platform. But building multi-tenant Next.js, Stripe billing, PostgreSQL schemas, and Google OAuth traditionally takes 4 months of contractor development!\n\n"
            "[TA James] On a Friday evening, the founder launched Antigravity 2.0. The 40-agent swarm wrote the FastAPI backend, assembled the React Tailwind frontend, wired Stripe webhooks, and generated 200 Playwright integration tests!\n\n"
            "[Prof. Peter] By Saturday morning at 8:00 AM, the full-stack platform was live on Google Cloud Run! The founder launched on Product Hunt on Sunday and acquired their first 100 paying customers on Day 2, saving 80,000 dollars in contractor fees!\n\n"
            "[TA Sarah] That is the exponential velocity of Antigravity 2.0.\n\n"
            "[TA James] Now let us open Part 3 and master Command Line Execution on Slide 23!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 2: 1인 창업자가 12시간 만에 구축한 멀티테넌트 풀스택 SaaS",
            "points": [
                "문제 상황: Next.js, FastAPI, Stripe 결제, OAuth가 포함된 SaaS MVP 구축에 외주 4개월 및 8만 달러 소요",
                "솔루션: 안티그래비티 2.0 40개 에이전트 스웜 가동으로 백엔드, 프론트엔드, 결제 연동, 테스트 일괄 작성",
                "성과: 12시간 만에 상용 배포 완료, 2일 차에 유료 고객 100명 확보, 80,000달러 외주 개발비 전액 절감"
            ],
            "tips": "사라 조교와 제임스 조교가 1인 창업자가 유니콘급 개발 속도를 내는 실전 스토리를 전합니다."
        },
        "keyTerms": [
            {
                "term": "Solo Founder Velocity",
                "def": "The exponential individual engineering productivity attained through multi-agent orchestration.",
                "defKo": "1인 창업가 초격차 생산성"
            },
            {
                "term": "Multi-Tenant SaaS Generation",
                "def": "The automated authoring of complete enterprise web applications including auth, billing, and database isolation.",
                "defKo": "멀티테넌트 SaaS 자동 구축"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 22: Part 3 Section Divider
    {
        "num": 22,
        "type": "section",
        "title": "PART 3: COMMAND LINE MASTERY & STATE CONTROL",
        "subtitle": "The `agy` CLI ecosystem, `/grill-me`, planning modes, terminal sandboxes, and the June 18, 2026 cutoff",
        "script": (
            "[TA Sarah] Look at Slide 22: \"PART 3: COMMAND LINE MASTERY & STATE CONTROL.\" Now we master the exact commands that drive the engine!\n\n"
            "[Prof. Peter] The command line is the native language of power. In Part 3, we explore the `agy` CLI command suite, interactive planning modes, safe terminal sandboxing, and the June 18, 2026 legacy cutoff.\n\n"
            "[TA James] Let us inspect deploying the `agy` CLI command architecture on Slide 23!"
        ),
        "koreanGuide": {
            "summary": "Part 3 섹션 전환: 커맨드 라인 마스터리와 상태 제어 (agy CLI)",
            "points": [
                "터미널의 위력: 고속 터미널 CLI를 통한 에이전트 상태 제어와 작업 오케스트레이션",
                "agy CLI 명령어 체계, /grill-me, Planning Mode vs Fast Mode",
                "안전한 터미널 샌드박싱 및 2026년 6월 18일 레거시 Gemini CLI 공식 종료 전환"
            ],
            "tips": "피터 교수가 터미널의 힘을 선언하고 제임스가 핵심 명령어 해설을 시작합니다."
        },
        "keyTerms": [
            {
                "term": "Terminal State Control",
                "def": "Managing background agent execution states, task queues, and process lifecycles via CLI utilities.",
                "defKo": "터미널 에이전트 상태 제어"
            },
            {
                "term": "Legacy CLI Cutoff",
                "def": "Google's official June 18, 2026 deprecation deadline terminating legacy Gemini CLI in favor of agy 2.0.",
                "defKo": "레거시 CLI 공식 종료 전환"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 23: Deploying the `agy` CLI Command Architecture
    {
        "num": 23,
        "type": "content",
        "title": "DEPLOYING THE `AGY` CLI COMMAND ARCHITECTURE",
        "subtitle": "Core CLI verbs: `agy plan`, `agy run`, `agy swarm`, and `agy audit`",
        "points": [
            "`agy plan 'goal'`: Analyzes repository and writes structured `implementation_plan.md` without modifying code.",
            "`agy run`: Executes approved plan chunks, spawning Coder and Reviewer subagents.",
            "`agy swarm --concurrency=50`: Spawns high-concurrency subagent fleets across git worktrees.",
            "`agy audit`: Performs static analysis, secret scanning, and dependency CVE checks."
        ],
        "script": (
            "[Prof. Peter] Slide 23 diagrams \"THE `AGY` CLI COMMAND ARCHITECTURE.\"\n\n"
            "[TA Sarah] Memorize these four core verbs: `agy plan` creates the design document. `agy run` executes the approved changes. `agy swarm` scales concurrency to 50 or 100 subagents! And `agy audit` performs security and CVE dependency scans!\n\n"
            "[TA James] Notice `agy plan`: It NEVER touches your source code! It only inspects files and creates the plan artifact for your review. Safe, predictable, disciplined.\n\n"
            "[TA Sarah] Let us inspect the `/grill-me` command on Slide 24!"
        ),
        "koreanGuide": {
            "summary": "agy CLI 핵심 명령어 아키텍처: plan, run, swarm, audit 4대 동사",
            "points": [
                "agy plan: 소스코드를 건드리지 않고 리포지토리를 분석하여 implementation_plan.md 생성",
                "agy run: 인간이 승인한 계획 청크를 실행하며 코더와 리뷰어 서브에이전트 가동",
                "agy swarm --concurrency=50: 50개 서브에이전트 고동시성 병렬 실행",
                "agy audit: 정적 분석, 시크릿 유출 검사, 의존성 보안 취약점(CVE) 전수 스캔"
            ],
            "tips": "사라 조교와 제임스 조교가 4대 핵심 동사의 역할과 안전성을 명쾌하게 해설합니다."
        },
        "keyTerms": [
            {
                "term": "agy CLI Verbs",
                "def": "The standardized command-line syntax (plan, run, swarm, audit) governing agent lifecycle execution.",
                "defKo": "agy CLI 4대 핵심 동사"
            },
            {
                "term": "Non-Mutating Plan Mode",
                "def": "The execution constraint ensuring planning commands only read files and generate design proposals without editing code.",
                "defKo": "무변형 계획 모드"
            }
        ]
    },
    # Slide 24: The `/grill-me` Command: Hardening Specs
    {
        "num": 24,
        "type": "content",
        "title": "THE `/GRILL-ME` COMMAND: HARDENING SPECIFICATIONS",
        "subtitle": "Interactive interview-driven plan hardening: Resolving architectural edge cases before typing code",
        "points": [
            "The Problem: Vague user prompts ('Add authentication') cause agents to make bad assumptions.",
            "The `/grill-me` Interview: AI asks 5 sharp architectural questions (JWT vs Session, OAuth providers, MFA).",
            "Rock-Solid Plan: Outputting a deterministic, unambiguous specification with zero design loopholes."
        ],
        "script": (
            "[TA Sarah] Slide 24 highlights our favorite slash command: \"THE `/GRILL-ME` INTERVIEW COMMAND.\"\n\n"
            "[TA James] Why do junior developers get bad results from AI? Because they type vague prompts like 'Build auth'! Then the AI guesses wrong, and everyone wastes 3 hours!\n\n"
            "[Prof. Peter] When you type `/grill-me`, the AI flips the script and interviews YOU! It asks: 'Do you want JWT tokens or Redis sessions? Which OAuth providers? What is your password hashing algorithm?' You answer in 2 minutes, and the agent generates a rock-solid, loophole-free plan!\n\n"
            "[TA Sarah] Let us compare Planning Mode vs. Fast Mode on Slide 25."
        ),
        "koreanGuide": {
            "summary": "/grill-me 심층 인터뷰: 코딩 전 설계 불확실성을 날카롭게 해소하는 기법",
            "points": [
                "모호한 프롬프트의 재앙: '인증 기능 추가해 줘' 같은 모호한 지시는 3시간의 헛바퀴 코딩 유발",
                "/grill-me 인터뷰: AI가 사용자에게 JWT vs 세션, OAuth 제공자, 암호 해싱 알고리즘 등 5가지 핵심 질문 역질의",
                "무결점 명세서: 2분간의 질답을 통해 맹점과 루프홀이 없는 완벽한 아키텍처 계획 확립"
            ],
            "tips": "피터 교수와 제임스 조교가 /grill-me를 통해 AI가 개발자를 심층 인터뷰하는 과정을 시연합니다."
        },
        "keyTerms": [
            {
                "term": "/grill-me Interview Mode",
                "def": "An interactive agent capability interrogating the human developer to clarify underspecified architectural requirements.",
                "defKo": "/grill-me 역질의 인터뷰 모드"
            },
            {
                "term": "Requirement Disambiguation",
                "def": "The elimination of uncertainty in software specifications through structured interactive dialogue.",
                "defKo": "요구사항 모호성 완전 해소"
            }
        ]
    },
    # Slide 25: Planning Mode vs. Fast Mode
    {
        "num": 25,
        "type": "comparison",
        "title": "PLANNING MODE VS. FAST MODE",
        "subtitle": "Choosing the right execution speed: Rigorous 2-phase architecture vs. instant one-off edits",
        "leftCard": {
            "tag": "PLANNING MODE (DEFAULT)",
            "title": "2-Phase Architecture",
            "points": [
                "Mandatory for multi-file features & refactoring.",
                "Phase 1: Researches repo & writes `implementation_plan.md`.",
                "Phase 2: Pauses for human approval, then executes.",
                "Emits verified `walkthrough.md` with tests."
            ]
        },
        "rightCard": {
            "tag": "FAST MODE (--FAST)",
            "title": "Instant 1-Shot Edits",
            "points": [
                "For trivial fixes: typos, CSS alignment, 1-line bugs.",
                "Skips formal planning artifact creation.",
                "Executes immediately in under 3 seconds.",
                "Bypasses interactive review gates."
            ]
        },
        "script": (
            "[Prof. Peter] Slide 25 contrasts \"PLANNING MODE VS. FAST MODE: Strategic Pacing.\"\n\n"
            "[TA Sarah] When building complex multi-file features, always use Planning Mode! It researches your repo, drafts the plan, waits for your explicit approval, and verifies results with a `walkthrough.md`.\n\n"
            "[TA James] But if you just need to fix a CSS color typo or update a version string, use Fast Mode (`--fast`)! It executes immediately in 2 seconds without ceremony!\n\n"
            "[Prof. Peter] Let us inspect isolated terminal execution on Slide 26."
        ),
        "koreanGuide": {
            "summary": "플래닝 모드(기본) vs 패스트 모드(--fast)의 전략적 분기",
            "points": [
                "플래닝 모드: 다중 파일 기능 구현 및 리팩토링 시 필수 (조사 ➔ 계획 승인 ➔ 실행 ➔ 워크스루)",
                "패스트 모드 (--fast): 단순 오타 수정, CSS 여백 조절, 1줄 버그 수정 시 2초 만에 즉시 실행",
                "과업의 복잡도와 위험도에 따른 유연한 모드 선택"
            ],
            "tips": "사라 조교와 제임스 조교가 프로젝트 규모에 따른 최적 모드 선택 기준을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Two-Phase Planning Protocol",
                "def": "The disciplined development workflow separating technical research and plan approval from source code modification.",
                "defKo": "2단계 플래닝 프로토콜"
            },
            {
                "term": "Fast-Mode Bypass",
                "def": "Direct execution mode skipping formal artifact drafting for trivial, non-breaking modifications.",
                "defKo": "패스트 모드 즉시 실행"
            }
        ]
    },
    # Slide 26: June 18, 2026: Legacy Gemini CLI Hard Cutoff
    {
        "num": 26,
        "type": "content",
        "title": "JUNE 18, 2026: LEGACY GEMINI CLI CUTOFF",
        "subtitle": "Google's mandatory platform migration: Deprecating legacy CLI in favor of the `agy` 2.0 architecture",
        "points": [
            "Hard Cutoff Date: June 18, 2026 — Legacy `gemini-cli` endpoints will be permanently deactivated.",
            "Architectural Upgrade: Migration to 150MB Go binary (`agy`), multi-agent swarms, and RDD artifacts.",
            "Automated Migration Tool: Run `agy migrate --from-gemini-cli` to convert skills, rules, and hooks automatically."
        ],
        "script": (
            "[TA Sarah] Slide 26 highlights a critical enterprise calendar deadline: \"JUNE 18, 2026: LEGACY GEMINI CLI HARD CUTOFF.\"\n\n"
            "[TA James] Mark your calendar: On June 18, 2026, Google will permanently shut down the legacy `gemini-cli` endpoints! All enterprise pipelines must migrate to the modern `agy` 2.0 Go architecture!\n\n"
            "[Prof. Peter] Fortunately, migration is seamless: run `agy migrate --from-gemini-cli`, and your existing rules, skills, and MCP servers are upgraded to Antigravity 2.0 in 10 seconds flat!\n\n"
            "[TA Sarah] Let us inspect custom swarms via Python SDK on Slide 27."
        ),
        "koreanGuide": {
            "summary": "2026년 6월 18일: 레거시 Gemini CLI 공식 종료 및 agy 자동 마이그레이션",
            "points": [
                "공식 종료 일정: 2026년 6월 18일 레거시 gemini-cli 엔드포인트 영구 폐쇄",
                "아키텍처 대업그레이드: 150MB Go 바이너리 agy 2.0, 멀티에이전트 스웜, RDD 아티팩트 체계로 전면 전환",
                "원클릭 마이그레이션: agy migrate --from-gemini-cli 실행 시 10초 만에 기존 스킬/룰 자동 변환"
            ],
            "tips": "제임스 조교가 2026년 6월 18일 마감일과 원클릭 마이그레이션 명령어를 명확히 안내합니다."
        },
        "keyTerms": [
            {
                "term": "Legacy CLI Deprecation",
                "def": "The scheduled decommissioning of earlier single-threaded command-line tools in favor of multi-agent runtimes.",
                "defKo": "레거시 CLI 공식 폐기 일정"
            },
            {
                "term": "Automated Migration Script",
                "def": "The CLI utility upgrading legacy configuration files, skills, and prompts to Antigravity 2.0 specifications.",
                "defKo": "자동 마이그레이션 유틸리티"
            }
        ]
    },
    # Slide 27: System Scalability: Custom Swarms via SDK
    {
        "num": 27,
        "type": "content",
        "title": "SYSTEM SCALABILITY: CUSTOM SWARMS VIA SDK",
        "subtitle": "Programmatically instantiating 100 specialized subagents using the Antigravity Python/Go SDK",
        "points": [
            "Programmatic Swarms: Writing 20 lines of Python to spawn a 50-agent automated penetration testing fleet.",
            "Dynamic Task Queues: Distributing 1,000 microservice upgrade tickets across active worker subagents.",
            "Subagent Memory Isolation: Each subagent operates with private context buffers, preventing cross-task token pollution."
        ],
        "script": (
            "[Prof. Peter] Slide 27 explores \"SYSTEM SCALABILITY: CUSTOM SWARMS VIA SDK.\"\n\n"
            "[TA Sarah] You are not limited to the command line. Using the Antigravity Python SDK, you can write automated scripts that spawn custom agent swarms on demand!\n\n"
            "[TA James] Look at the code snippet on screen: In 20 lines of Python, you spawn 50 worker subagents, connect them to a Redis task queue, and refactor 1,000 repository microservices automatically with private token buffers!\n\n"
            "[TA Sarah] Let us inspect our third enterprise case study on Slide 29!"
        ),
        "koreanGuide": {
            "summary": "시스템 확장성: 파이썬/Go SDK를 통한 커스텀 스웜의 프로그래밍 제어",
            "points": [
                "프로그래밍 방식 스웜 생성: 단 20줄의 파이썬 코드로 50개 모의 침투 테스트 에이전트 군단 동적 소환",
                "동적 태스크 큐: 1,000개 마이크로서비스 리팩토링 티켓을 활성 서브에이전트에 분산 배분",
                "서브에이전트 메모리 격리: 에이전트마다 독립된 컨텍스트 버퍼를 운용하여 토큰 오염 원천 차단"
            ],
            "tips": "사라 조교와 제임스 조교가 SDK 기반의 무한 확장 자동화 스크립트 작성법을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Antigravity SDK",
                "def": "The programmatic library (Python/Go) enabling developers to spawn, orchestrate, and monitor subagent swarms in code.",
                "defKo": "안티그래비티 SDK"
            },
            {
                "term": "Context Buffer Isolation",
                "def": "Maintaining completely separate token memory spaces for each active subagent to prevent reasoning interference.",
                "defKo": "컨텍스트 버퍼 격리"
            }
        ]
    },
    # Slide 28: Part 3 Transition: Trust, Safety & Governance
    {
        "num": 28,
        "type": "content",
        "title": "PART 3 TRANSITION: ENTERING RDD GOVERNANCE",
        "subtitle": "Connecting command execution to Review-Driven Development, Artifacts, and data protection",
        "points": [
            "Speed Demands Safety: Massive swarms running at 50,000 lines/day require ironclad governance frameworks.",
            "Review-Driven Development (RDD): The human director audits every code diff, plan, and walkthrough.",
            "The Roadmap Ahead: Master RDD in Part 4, dedicate our craft to Soli Deo Gloria, and execute Lab 10."
        ],
        "script": (
            "[Prof. Peter] Slide 28 transitions to our governance framework: \"PART 3 TRANSITION: ENTERING RDD GOVERNANCE.\"\n\n"
            "[TA Sarah] When software swarms generate 50,000 lines of code a day, human beings cannot read raw code line-by-line. How do we maintain absolute control?\n\n"
            "[TA James] Through Review-Driven Development (RDD)! RDD uses structured Artifacts (`implementation_plan.md`, `walkthrough.md`, git diff blocks, and WebP video proofs) so humans can verify complex systems in seconds!\n\n"
            "[Prof. Peter] Let us examine our third enterprise case study on Slide 29!"
        ),
        "koreanGuide": {
            "summary": "Part 3 전환: Review-Driven Development(RDD) 거버넌스 진입",
            "points": [
                "속도와 거버넌스: 하루 5만 줄의 코드가 생산될 때 인간이 통제력을 유지하는 RDD 프레임워크",
                "구조화된 아티팩트: implementation_plan, walkthrough, git diff, WebP 비디오를 통한 초고속 검증",
                "Part 4 로드맵 제시: RDD 아티팩트 체계 ➔ 데이터 유출 방지 ➔ 실습 10 완결"
            ],
            "tips": "사라 조교와 제임스 조교가 RDD 거버넌스가 왜 5만 줄 시대의 필수 안전장치인지 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Review-Driven Development (RDD)",
                "def": "A software engineering methodology centering human architectural oversight around structured plan, diff, and verification artifacts.",
                "defKo": "리뷰 중심 개발 방법론 (RDD)"
            },
            {
                "term": "Artifact Governance Architecture",
                "def": "The standardized markdown schema communicating technical intent, code mutations, and empirical test proof to human directors.",
                "defKo": "아티팩트 거버넌스 아키텍처"
            }
        ]
    },
    # Slide 29: Case Study 3: Stopping Malicious Dependency Injection via RDD
    {
        "num": 29,
        "type": "casestudy",
        "title": "CASE STUDY 3: STOPPING MALICIOUS INJECTION VIA RDD",
        "subtitle": "Antigravity RDD Code Diff Gate catches hidden crypto-miner injected into third-party npm package",
        "company": "Global Cloud Infrastructure Enterprise",
        "problem": "An open-source npm library was hijacked by a threat actor who added a hidden obfuscated Monero crypto-mining payload to a patch release.",
        "solution": "Antigravity Reviewer subagent analyzed the git diff, detected obfuscated `eval()` strings and unauthorized network outbound calls, and flagged the PR.",
        "impact": "Malicious PR blocked before merging to main branch; prevented compromise of 15,000 production Kubernetes clusters.",
        "script": (
            "[Prof. Peter] Slide 29 presents \"CASE STUDY 3: STOPPING MALICIOUS DEPENDENCY INJECTION VIA RDD.\"\n\n"
            "[TA Sarah] A popular open-source npm logging package was hijacked by cybercriminals, who inserted an obfuscated Monero crypto-miner into version 2.4.1. When an automated bot updated dependencies, it pulled the poisoned package!\n\n"
            "[TA James] But Antigravity's Reviewer subagent inspected the git diff! It caught obfuscated `eval()` strings and flagged an unauthorized outbound network call to an unverified IP address in `package.json`! The Reviewer raised a critical security alert on the `walkthrough.md`!\n\n"
            "[Prof. Peter] The human Director clicked 'Reject'! Over 15,000 production Kubernetes clusters were saved from compromise! Structured RDD diff gates protect the enterprise fortress.\n\n"
            "[TA Sarah] Now let us open Part 4 and examine Trust and Governance on Slide 30!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 3: npm 패키지 속 암호화폐 채굴 악성코드를 RDD diff 게이트로 적발",
            "points": [
                "문제 상황: 유명 npm 로깅 라이브러리가 해킹되어 난독화된 모네로 채굴 페이로드가 의존성 업데이트로 유입",
                "솔루션: 안티그래비티 리뷰어 서브에이전트가 git diff를 정밀 분석하여 난독화 eval() 및 미인가 IP 통신 적발",
                "성과: 메인 브랜치 머지 전 악성 PR 차단 완료, 15,000개 쿠버네티스 클러스터 감염 사고 원천 방어"
            ],
            "tips": "사라 조교와 제임스 조교가 RDD diff 감사 게이트가 공급망 해킹을 어떻게 막아냈는지 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Dependency Poisoning",
                "def": "The covert insertion of malicious code into legitimate third-party software libraries.",
                "defKo": "의존성 라이브러리 오염 공격"
            },
            {
                "term": "Diff Inspection Gate",
                "def": "The mandatory human and automated checkpoint verifying all exact lines added, modified, or deleted in a pull request.",
                "defKo": "코드 변경분(Diff) 검증 관문"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 30: Part 4 Section Divider
    {
        "num": 30,
        "type": "section",
        "title": "PART 4: TRUST, SAFETY & CONDUCTOR SOVEREIGNTY",
        "subtitle": "The Artifacts system, code diff tracking, enterprise exfiltration defense, and Soli Deo Gloria",
        "script": (
            "[TA Sarah] Look at Slide 30: \"PART 4: TRUST, SAFETY & CONDUCTOR SOVEREIGNTY.\" Now we master the ultimate governance discipline of the Intelligence Architect!\n\n"
            "[Prof. Peter] Supreme velocity without supreme discipline is catastrophic. In Part 4, we examine the Artifacts system, code diff tracking, visual video evidence, enterprise data protection, dedicate our work to Soli Deo Gloria, and execute Lab 10!\n\n"
            "[TA James] Let us inspect the Shield of Truth: The Artifacts System on Slide 31."
        ),
        "koreanGuide": {
            "summary": "Part 4 섹션 전환: 신뢰, 안전 및 지휘관의 주권적 거버넌스",
            "points": [
                "극단적 속도에 걸맞은 극단적 규율: 아티팩트 시스템, 코드 diff 추적, 시각적 비디오 증거",
                "기업 데이터 유출 방지와 제로 데이터 보존 원칙",
                "지능 건축가의 거룩한 소명과 Soli Deo Gloria"
            ],
            "tips": "피터 교수가 속도와 규율의 균형을 선언하고 제임스가 아티팩트 시스템 해설을 시작합니다."
        },
        "keyTerms": [
            {
                "term": "Conductor Sovereignty",
                "def": "The uncompromised authority and accountability of human directors over multi-agent software swarms.",
                "defKo": "지휘관의 주권적 권한"
            },
            {
                "term": "Artifact Governance Ecosystem",
                "def": "The standardized set of markdown files and visual media documenting agent planning, execution, and verification.",
                "defKo": "아티팩트 거버넌스 생태계"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 31: The Shield of Truth: The Artifacts System
    {
        "num": 31,
        "type": "content",
        "title": "THE SHIELD OF TRUTH: THE ARTIFACTS SYSTEM",
        "subtitle": "Structured, persistent markdown documents creating complete visibility over multi-agent workflows",
        "points": [
            "`implementation_plan.md`: The architectural blueprint specifying proposed changes, open questions, and verification steps.",
            "`walkthrough.md`: The post-execution report detailing modified files, test outputs, and embedded WebP recordings.",
            "Immutable Audit Records: Stored in `.gemini/brain/` to provide permanent forensic transparency.",
            "Zero Guesswork: The human director reviews structured markdown rather than parsing 10,000 lines of terminal logs."
        ],
        "script": (
            "[Prof. Peter] Slide 31 presents \"THE SHIELD OF TRUTH: THE ARTIFACTS SYSTEM.\"\n\n"
            "[TA Sarah] Antigravity 2.0 does not dump messy text into chat windows. It produces formal, structured Artifacts: `implementation_plan.md` before coding begins, and `walkthrough.md` after coding finishes!\n\n"
            "[TA James] These artifacts contain clickable file links, git diff snippets, and embedded WebP video recordings of browser tests! The human director reviews the entire 50-file modification in 60 seconds with total clarity!\n\n"
            "[Prof. Peter] Let us inspect code diff tracking on Slide 32."
        ),
        "koreanGuide": {
            "summary": "진리의 방패: 아티팩트(Artifacts) 시스템의 2대 핵심 문서",
            "points": [
                "implementation_plan.md: 코딩 전 제안된 변경 파일, 설계 질문, 검증 계획을 담은 아키텍처 청사진",
                "walkthrough.md: 실행 완료 후 변경된 파일, 테스트 결과, 임베디드 WebP 비디오를 담은 최종 결과 보고서",
                "60초 초고속 검증: 1만 줄의 터미널 로그를 헤맬 필요 없이 정제된 마크다운으로 50개 파일 수정을 1분 만에 파악"
            ],
            "tips": "사라 조교와 제임스 조교가 아티팩트 시스템이 제공하는 60초 검증의 명쾌함을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Structured Artifact",
                "def": "A specialized persistent markdown document presenting technical plans, changes, or verification proof to users.",
                "defKo": "구조화된 아티팩트 문서"
            },
            {
                "term": "Clickable Markdown Link",
                "def": "A standard file:// link format enabling developers to navigate directly to modified code symbols in their IDE.",
                "defKo": "클릭형 마크다운 파일 링크"
            }
        ]
    },
    # Slide 32: The Power of Code Diff: Tracking Every Mutation
    {
        "num": 32,
        "type": "content",
        "title": "THE POWER OF CODE DIFF: TRACKING MUTATIONS",
        "subtitle": "Visualizing exact additions (+), deletions (-), and invariants across 50 files simultaneously",
        "points": [
            "Color-Coded Git Diffs: Green additions (+) and red deletions (-) highlighted with syntax color clarity.",
            "Non-Destructive Editing: Ensuring existing comments, docstrings, and unrelated modules are 100% preserved.",
            "Atomic Rollback: One-click undo reverts entire multi-file changesets instantly if tests fail."
        ],
        "script": (
            "[TA Sarah] Slide 32 details \"THE POWER OF CODE DIFF: TRACKING EVERY MUTATION.\"\n\n"
            "[TA James] Look at the diff viewer: Every line added is glowing green, every line removed is red, and unchanged lines provide context. Antigravity strictly preserves your existing comments and docstrings!\n\n"
            "[Prof. Peter] And if any unexpected behavior occurs, you click 'Rollback', and all 50 modified files revert to their pristine previous git commit in 10 milliseconds!\n\n"
            "[TA Sarah] Let us inspect Review-Driven Development (RDD) on Slide 33."
        ),
        "koreanGuide": {
            "summary": "코드 Diff의 위력: 모든 변경분의 정밀 시각화와 10ms 원자적 롤백",
            "points": [
                "색상 구분된 Git Diff: 추가된 라인은 초록색(+), 삭제된 라인은 빨간색(-)으로 명확히 시각화",
                "비파괴적 수정 원칙: 기존 주석, 독스트링, 무관한 코드를 100% 보존하는 정밀 편집",
                "10ms 원자적 롤백: 이상 발견 시 클릭 한 번으로 50개 파일 변경분을 이전 커밋으로 즉시 되돌림"
            ],
            "tips": "제임스 조교가 비파괴적 수정과 10ms 즉시 롤백의 안전성을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Atomic Rollback",
                "def": "The instantaneous programmatic reversion of all file mutations across a multi-agent transaction to restore baseline integrity.",
                "defKo": "원자적 즉시 롤백"
            },
            {
                "term": "Non-Destructive Code Mutation",
                "def": "The strict policy preserving unrelated existing comments, architectural structure, and legacy logic during refactoring.",
                "defKo": "비파괴적 코드 수정 원칙"
            }
        ]
    },
    # Slide 33: Review-Driven Development (RDD): Human-in-the-Loop
    {
        "num": 33,
        "type": "content",
        "title": "REVIEW-DRIVEN DEVELOPMENT (RDD)",
        "subtitle": "The 3-phase governance protocol: Research ➔ Plan Approval ➔ Verify",
        "points": [
            "Phase 1: Research (Agents investigate repo with `view_file` and `grep_search` with ZERO file modifications).",
            "Phase 2: Plan Approval (Human director reviews `implementation_plan.md` and clicks 'Proceed').",
            "Phase 3: Verify (Agents execute, run unit tests, and present `walkthrough.md` with visual proof)."
        ],
        "script": (
            "[Prof. Peter] Slide 33 outlines \"REVIEW-DRIVEN DEVELOPMENT (RDD): THE 3-PHASE PROTOCOL.\"\n\n"
            "[TA Sarah] This is the core engineering protocol of Oikos University: Phase 1 is Research—agents read files and grep search, but cannot modify a single character! Phase 2 is Plan Approval—the human director reviews the plan and explicitly approves it!\n\n"
            "[TA James] Phase 3 is Verify—agents execute, run tests, and emit the `walkthrough.md`! Human intelligence directs the plan; artificial intelligence executes the labor!\n\n"
            "[Prof. Peter] Let us inspect enterprise security and preventing data exfiltration on Slide 34."
        ),
        "koreanGuide": {
            "summary": "Review-Driven Development (RDD) 3단계 프로토콜: 조사 ➔ 승인 ➔ 검증",
            "points": [
                "1단계 조사(Research): 파일 읽기와 grep 검색만 수행하며 코드 수정 0건 (무변형 탐색)",
                "2단계 계획 승인(Plan Approval): 인간 지휘관이 implementation_plan.md를 검토하고 '진행' 승인",
                "3단계 검증(Verify): 코드 수정, 단위 테스트 실행, walkthrough.md 시각적 증거 제출"
            ],
            "tips": "사라 조교와 피터 교수가 인간의 지휘권과 AI의 실행력이 완벽히 조화된 RDD 3단계를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Review-Driven Development (RDD)",
                "def": "A software engineering methodology centering human architectural oversight around structured plan, diff, and verification artifacts.",
                "defKo": "리뷰 중심 개발 방법론 (RDD)"
            },
            {
                "term": "Human-in-the-Loop Governance",
                "def": "The mandatory architectural requirement that automated systems cannot execute state mutations without explicit human approval.",
                "defKo": "인간 개입형 거버넌스"
            }
        ]
    },
    # Slide 34: Enterprise Security: Preventing Data Exfiltration
    {
        "num": 34,
        "type": "content",
        "title": "ENTERPRISE SECURITY: PREVENTING EXFILTRATION",
        "subtitle": "Network isolation, secrets scrubbing, local sandbox bounds, and paid tier guarantees",
        "points": [
            "Zero Data Retention: Enterprise Paid Tier guarantees your proprietary code is NEVER logged or used for model training.",
            "Secrets Scrubber: Automated regex filters redact API keys, private keys, and passwords before prompt dispatch.",
            "Network Sandbox: Subagents are blocked from sending outbound HTTP requests to unauthorized domains."
        ],
        "script": (
            "[TA Sarah] Slide 34 covers \"ENTERPRISE SECURITY: PREVENTING DATA EXFILTRATION.\"\n\n"
            "[TA James] How do we protect enterprise secrets? First, Google's Paid Tier guarantees Zero Data Retention—your code is never used to train public models! Second, Antigravity includes an automated Secrets Scrubber that redacts API keys and AWS tokens before dispatch!\n\n"
            "[Prof. Peter] Third, all subagent shell tools run in sandboxed network namespaces, blocking rogue data exfiltration to external servers!\n\n"
            "[TA Sarah] Let us inspect Soli Deo Gloria on Slide 35!"
        ),
        "koreanGuide": {
            "summary": "엔터프라이즈 보안: 데이터 유출 방지 및 시크릿 마스킹 방어선",
            "points": [
                "무보관 원칙(Zero Data Retention): 유료 엔터프라이즈 티어는 코드 학습 활용 원천 배제 보증",
                "시크릿 스크러버(Secrets Scrubber): API 키, AWS 토큰, 비밀번호를 프롬프트 전송 전 자동 마스킹",
                "네트워크 샌드박스: 서브에이전트의 미승인 외부 도메인 아웃바운드 통신을 OS 레벨에서 원천 차단"
            ],
            "tips": "제임스 조교가 기업 기밀과 개인정보를 완벽히 지키는 3단계 보안 방어선을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Secrets Scrubbing",
                "def": "The automated redaction of sensitive credentials (API keys, private tokens) from agent prompt contexts.",
                "defKo": "시크릿 자동 마스킹 (Secrets Scrubbing)"
            },
            {
                "term": "Network Namespace Sandboxing",
                "def": "Restricting process network access to designated internal endpoints to prevent data exfiltration.",
                "defKo": "네트워크 네임스페이스 격리"
            }
        ]
    },
    # Slide 35: Soli Deo Gloria: Reclaiming Time for Divine Focus
    {
        "num": 35,
        "type": "content",
        "title": "SOLI DEO GLORIA: RECLAIMING DIVINE FOCUS",
        "subtitle": "Ephesians 5:16: Channeling reclaimed engineering capacity into eternal callings, worship, and community",
        "points": [
            "Soli Deo Gloria: The supreme motto of Oikos University and Smart Insight Lab.",
            "Reclaiming 35 Hours/Week: Liberating human engineers from mechanical syntax typing to focus on high-order truth.",
            "The Conductor's Sacred Duty: Stewarding autonomous swarms to build software that reflects divine order and love."
        ],
        "script": (
            "[Prof. Peter] Slide 35 declares our supreme banner: \"SOLI DEO GLORIA: RECLAIMING DIVINE FOCUS: To God Alone Be the Glory.\"\n\n"
            "[TA Sarah] When you master Antigravity 2.0 swarms, you don't just build features faster—you reclaim 35 hours every single week from mechanical coding slavery!\n\n"
            "[TA James] You take those redeemed hours and invest them in deep contemplation, family devotion, and serving your community with excellence!\n\n"
            "[Prof. Peter] We conduct intelligent fleets not for personal vanity, but to redeem finite time for God's eternal glory.\n\n"
            "[TA Sarah] Let us inspect our fourth enterprise case study on Slide 36!"
        ),
        "koreanGuide": {
            "summary": "Soli Deo Gloria: 주당 35시간의 생애 시간 탈환과 신적 소명 헌신",
            "points": [
                "오직 하나님께 영광(Soli Deo Gloria): 단순 속도 경쟁을 넘어선 시간 구속의 거룩한 소명",
                "주당 35시간 회수: 기계적 문법 타이핑의 노역에서 벗어나 주당 35시간의 온전한 자유 획득",
                "지휘관의 거룩한 의무: 자율 지능 군단을 지휘하여 하나님의 질서와 정의, 사랑을 반영하는 소프트웨어 건축"
            ],
            "tips": "3인의 강사진이 에베소서 5장 16절 말씀과 함께 공학적 자유의 신학적 의미를 웅장하게 선언합니다."
        },
        "keyTerms": [
            {
                "term": "Soli Deo Gloria",
                "def": "The foundational theological motto dedicating all intellectual and technological mastery to the Glory of God Alone.",
                "defKo": "솔리 데오 글로리아 (오직 하나님께 영광)"
            },
            {
                "term": "Cognitive Emancipation",
                "def": "The liberation of human intellect from repetitive technical labor to pursue higher-order creative and spiritual callings.",
                "defKo": "인지적 해방 (지적 자유)"
            }
        ]
    },
    # Slide 36: Case Study 4: 24/7 Self-Healing CI/CD Swarm
    {
        "num": 36,
        "type": "casestudy",
        "title": "CASE STUDY 4: 24/7 SELF-HEALING CI/CD SWARM",
        "subtitle": "Global Telecommunications Giant deploys Antigravity Swarm resolving 120 broken nightly builds automatically",
        "company": "Global 5G Telecommunications Conglomerate",
        "problem": "Company experienced 120 broken build failures weekly across 3,000 developer repos, causing 40 hours of on-call engineer triage delay every weekend.",
        "solution": "Deployed Antigravity 2.0 CI/CD webhook daemon: Swarm spawns on build failure, diagnoses stack traces, creates fix branches, verifies unit tests, and submits PR.",
        "impact": "88% of broken builds resolved autonomously in under 4 minutes; on-call engineer weekend pages reduced by 95%; saved $2.4M in developer overtime.",
        "script": (
            "[Prof. Peter] Slide 36 presents \"CASE STUDY 4: 24/7 SELF-HEALING CI/CD SWARM.\"\n\n"
            "[TA Sarah] A global telecommunications giant with 3,000 developers had a massive weekend crisis: every Saturday morning, 120 broken CI/CD builds flooded on-call engineers with pager alerts, ruining weekends and delaying releases!\n\n"
            "[TA James] They connected Antigravity 2.0 to their GitHub Actions CI/CD webhook! Whenever a build fails, Antigravity spawns an autonomous triage swarm: it parses compiler stack traces, inspects git diffs, writes the fix, runs local tests, and submits an audited PR with a `walkthrough.md` in 3.8 minutes!\n\n"
            "[Prof. Peter] Look at the results: 88% of broken builds were fixed autonomously with zero human intervention! Weekend on-call pages plunged by 95%, saving 2.4 million dollars in overtime and restoring peace of mind to 3,000 engineers!\n\n"
            "[TA Sarah] Let us inspect our 6-step Swarm Deployment Blueprint on Slide 37!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 4: 글로벌 통신사의 주말 빌드 장애 120건을 3.8분 만에 자가 치유한 스웜",
            "points": [
                "문제 상황: 3,000명 개발자의 주말 빌드 에러 120건으로 당직 엔지니어의 주말 소멸 및 출시 지연",
                "솔루션: GitHub Actions에 안티그래비티 2.0 웹훅 연동 ➔ 빌드 실패 시 스웜이 스택 트레이스를 분석하고 자율 수정 PR 제출",
                "성과: 빌드 장애의 88%를 3.8분 만에 무인 자율 해결, 주말 호출 알람 95% 급감, 연간 240만 달러 야근 수당 절감"
            ],
            "tips": "사라 조교와 제임스 조교가 주말 당직의 고통을 없애준 자가 치유 CI/CD 스웜의 위력을 실감 나게 전합니다."
        },
        "keyTerms": [
            {
                "term": "Self-Healing CI/CD Pipeline",
                "def": "An automated build pipeline that detects compilation failures, diagnoses root causes, and submits tested bug-fix PRs autonomously.",
                "defKo": "자가 치유 CI/CD 파이프라인"
            },
            {
                "term": "Autonomous Stack Trace Triage",
                "def": "AI agents parsing compiler error logs and mapping failures to exact source code lines for immediate remediation.",
                "defKo": "스택 트레이스 자율 진단 및 수정"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 37: The 6-Step Swarm Deployment Blueprint
    {
        "num": 37,
        "type": "content",
        "title": "THE 6-STEP SWARM DEPLOYMENT BLUEPRINT",
        "subtitle": "The standardized pipeline from user goal to verified production release",
        "points": [
            "Step 1: Specification Interview (Run `/grill-me` to disambiguate architectural intent).",
            "Step 2: Non-Mutating Plan Drafting (Execute `agy plan` to generate `implementation_plan.md`).",
            "Step 3: Human Director Authorization (Review scope, click 'Proceed', and assign subagent concurrency).",
            "Step 4: Parallel Swarm Execution (Coder subagents refactor across isolated git worktrees).",
            "Step 5: Adversarial Audit & Verification (Reviewer and Browser subagents run unit tests & WebP recordings).",
            "Step 6: Walkthrough Inspection & Merge (Review `walkthrough.md`, audit diffs, and merge to main)."
        ],
        "script": (
            "[TA Sarah] Slide 37 provides our master operational blueprint: \"THE 6-STEP SWARM DEPLOYMENT BLUEPRINT.\"\n\n"
            "[TA James] Follow these exact 6 steps: Step 1: Run `/grill-me`. Step 2: Generate `implementation_plan.md` with `agy plan`. Step 3: Approve the plan. Step 4: Launch parallel Coder subagents! Step 5: Run Reviewer audits and Browser WebP tests. Step 6: Inspect `walkthrough.md` and merge!\n\n"
            "[Prof. Peter] This structured 6-step blueprint guarantees world-class velocity with zero compromise on quality.\n\n"
            "[TA Sarah] Let us inspect our Pre-Deployment Production Checklist on Slide 38."
        ),
        "koreanGuide": {
            "summary": "스웜 배포 6단계 표준 구현 청사진",
            "points": [
                "1단계: /grill-me 인터뷰를 통한 아키텍처 의도 명확화",
                "2단계: agy plan을 통한 무변형 implementation_plan.md 생성",
                "3단계: 인간 지휘관의 범위 검토 및 '진행' 승인",
                "4단계: 격리된 깃 워크트리에서 코더 서브에이전트 병렬 실행",
                "5단계: 리뷰어 적대적 감사 및 브라우저 WebP 테스트 검증",
                "6단계: walkthrough.md 최종 검토 및 메인 브랜치 머지"
            ],
            "tips": "제임스 조교가 6단계 워크플로우를 완벽한 지휘관 행동 지침으로 정리합니다."
        },
        "keyTerms": [
            {
                "term": "Swarm Deployment Blueprint",
                "def": "The formal 6-stage engineering process governing multi-agent planning, parallel execution, and verification.",
                "defKo": "스웜 배포 표준 청사진"
            },
            {
                "term": "Phased Swarm Execution",
                "def": "Orchestrating AI agents through strict sequential milestones ensuring stability before deployment.",
                "defKo": "단계별 스웜 실행 통제"
            }
        ]
    },
    # Slide 38: Production Checklist: Pre-Deployment Verification
    {
        "num": 38,
        "type": "content",
        "title": "PRODUCTION CHECKLIST: PRE-DEPLOYMENT VERIFICATION",
        "subtitle": "The 6-gate audit every Antigravity swarm pull request must pass before main branch merge",
        "points": [
            "Gate 1: `implementation_plan.md` reviewed and explicitly approved by the human Director.",
            "Gate 2: 100% of automated unit, integration, and linter tests passing with zero errors.",
            "Gate 3: All code diffs audited for secrets, AST integrity, and non-destructive preservation.",
            "Gate 4: Browser subagent WebP recording verifies UI responsiveness and zero console errors.",
            "Gate 5: Paid Tier enterprise data isolation active with zero model training telemetry.",
            "Gate 6: `walkthrough.md` published detailing all completed changes and empirical test logs."
        ],
        "script": (
            "[TA James] Slide 38 presents our \"PRODUCTION CHECKLIST: PRE-DEPLOYMENT VERIFICATION.\"\n\n"
            "[TA Sarah] Before merging any swarm PR, audit all 6 gates: Gate 1: Plan approved. Gate 2: 100% tests passing. Gate 3: Diffs audited. Gate 4: Browser WebP video verified. Gate 5: Zero-data-retention active. Gate 6: Walkthrough published!\n\n"
            "[Prof. Peter] Strict quality gates guarantee that our software remains an unbreakable fortress of truth.\n\n"
            "[TA Sarah] Let us review Session 10 Key Takeaways on Slide 39!"
        ),
        "koreanGuide": {
            "summary": "프로덕션 체크리스트: 스웜 PR 배포 전 6대 검증 관문",
            "points": [
                "1관문: implementation_plan.md에 대한 인간 지휘관의 명시적 승인",
                "2관문: 단위, 통합, 린트 테스트 100% 통과",
                "3관문: 시크릿 유출 및 비파괴적 코드 보존 diff 검증 완료",
                "4관문: 브라우저 WebP 영상 및 콘솔 에러 0건 확인",
                "5관문: 유료 티어 무보관(Zero Retention) 데이터 격리 확인",
                "6관문: walkthrough.md 결과 보고서 등재 완료"
            ],
            "tips": "제임스 조교가 6대 검증 관문을 단호하게 체크리스트로 확인합니다."
        },
        "keyTerms": [
            {
                "term": "Pre-Merge Verification Gate",
                "def": "A mandatory quality gate that multi-agent changesets must satisfy before integration into primary branches.",
                "defKo": "머지 전 사전 검증 관문"
            },
            {
                "term": "Zero Console Error Invariant",
                "def": "The strict verification rule requiring browser execution to produce zero runtime console exceptions.",
                "defKo": "콘솔 에러 제로 불변식"
            }
        ]
    },
    # Slide 39: Session 10 Summary & Key Takeaways
    {
        "num": 39,
        "type": "content",
        "title": "SESSION 10 SUMMARY & KEY TAKEAWAYS",
        "subtitle": "Synthesizing the 4 foundational pillars of Antigravity 2.0 and Swarm Orchestration",
        "points": [
            "Pillar 1: Escaped Developer Gravity (Transitioned from mechanical code typist to Sovereign Conductor).",
            "Pillar 2: Antigravity 2.0 Engine (Go-based 150MB binary, split-view cockpit, and 93 subagents).",
            "Pillar 3: Self-Evolving Loop (Agents dynamically authoring and compiling their own tools).",
            "Pillar 4: Review-Driven Development (Governing 50,000 lines/day via structured Artifacts and diffs)."
        ],
        "script": (
            "[TA Sarah] Slide 39 summarizes our \"SESSION 10 KEY TAKEAWAYS: 4 FOUNDATIONAL PILLARS.\"\n\n"
            "[TA James] Pillar 1: We escaped developer gravity and became Sovereign Conductors! Pillar 2: The 150MB Go engine coordinates 93 agents in parallel! Pillar 3: The Self-Evolving Loop creates tools on demand! And Pillar 4: RDD artifacts govern 50,000 lines a day with total safety!\n\n"
            "[Prof. Peter] When these four pillars unite, you possess the power to build complex software at the speed of thought.\n\n"
            "[TA Sarah] Let us inspect the Life OS Swarm Cockpit on Slide 40!"
        ),
        "koreanGuide": {
            "summary": "Session 10 요약 및 4대 핵심 축 총정리",
            "points": [
                "1대 축: 개발자 중력 탈출 (코드 타이피스트에서 주권적 총괄 지휘관으로 도약)",
                "2대 축: 안티그래비티 2.0 엔진 (Go 기반 150MB 바이너리와 93개 서브에이전트 스웜)",
                "3대 축: 자가 진화 루프 (에이전트가 런타임에 스스로 새로운 도구를 작성·컴파일)",
                "4대 축: RDD 아티팩트 거버넌스 (구조화된 아티팩트로 하루 5만 줄의 코드를 완벽 통제)"
            ],
            "tips": "제임스 조교가 4대 축을 리듬감 있게 요약하여 학습 효과를 극대화합니다."
        },
        "keyTerms": [
            {
                "term": "Architectural Synthesis",
                "def": "The unified integration of multi-agent concurrency, compiled native runtimes, dynamic tool synthesis, and artifact governance.",
                "defKo": "아키텍처 통합 합성"
            },
            {
                "term": "Thought-Speed Engineering",
                "def": "The capability to translate architectural concepts into live, verified production software in minutes.",
                "defKo": "생각 속도의 소프트웨어 공학"
            }
        ]
    },
    # Slide 40: Life OS Swarm Cockpit
    {
        "num": 40,
        "type": "content",
        "title": "LIFE OS SWARM COCKPIT",
        "subtitle": "Configuring your personal multi-agent development environment: VS Code + Antigravity 2.0 CLI",
        "points": [
            "Cockpit Setup: Antigravity IDE on left monitor for live diffs; terminal on right monitor for `agy` verbs.",
            "Custom Skill Vault: Creating personal `.agents/skills/` directory for bespoke domain workflows.",
            "Autonomous Daily Sprint: Launching 10-agent background swarms for continuous repository refactoring."
        ],
        "script": (
            "[Prof. Peter] Slide 40 outlines your personal setup: \"LIFE OS SWARM COCKPIT.\"\n\n"
            "[TA Sarah] How do you configure your daily Life OS workstation? Keep Antigravity IDE open on your primary monitor to review live git diffs and browser tests. Keep your terminal open on your secondary monitor for `agy` commands.\n\n"
            "[TA James] Create your private `.agents/skills/` vault for your company's custom tools, and launch background 10-agent swarms to maintain continuous codebase health while you focus on high-level strategy!\n\n"
            "[TA Sarah] Let us inspect the Conductor's Era on Slide 41."
        ),
        "koreanGuide": {
            "summary": "라이프 OS 스웜 콕핏: 듀얼 모니터 세팅과 개인 맞춤형 스킬 금고",
            "points": [
                "개발 콕핏 구성: 메인 모니터에 Antigravity IDE(실시간 diff 및 브라우저 뷰) + 서브 모니터에 agy 터미널",
                "커스텀 스킬 금고: .agents/skills/ 경로에 사내 전용 도구 및 도메인 스킬 상시 축적",
                "일일 자율 스프린트: 10개 백그라운드 스웜을 상시 가동해 지속적 코드 리팩토링 및 헬스 체크"
            ],
            "tips": "사라 조교와 제임스 조교가 프로 엔지니어가 사용하는 듀얼 모니터 스웜 배치법을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Swarm Workstation Cockpit",
                "def": "A multi-monitor operational layout harmonizing visual IDE artifact review with terminal command orchestration.",
                "defKo": "스웜 워크스테이션 콕핏"
            },
            {
                "term": "Personal Skill Vault",
                "def": "A structured repository of customized domain skill packages enhancing local subagent capabilities.",
                "defKo": "개인 맞춤형 스킬 금고"
            }
        ]
    },
    # Slide 41: The Conductor's Era: Lead the Future
    {
        "num": 41,
        "type": "content",
        "title": "THE CONDUCTOR'S ERA: LEAD THE FUTURE",
        "subtitle": "Rising above fear of automation to become the master architect who directs the symphony of AI",
        "points": [
            "The Obsolete Fear: 'AI will replace software engineers.' Reality: AI replaces typists, empowering Architects.",
            "The New Nobility: Those who master multi-agent orchestration will build the next generation of global systems.",
            "Leading with Purpose: Directing artificial intelligence to build systems of beauty, integrity, and human flourishing."
        ],
        "script": (
            "[Prof. Peter] Slide 41 proclaims \"THE CONDUCTOR'S ERA: LEAD THE FUTURE OF SOFTWARE.\"\n\n"
            "[TA Sarah] Mediocre voices say: 'AI will replace programmers.' But at Oikos University, we know the truth: AI replaces mechanical typists, but elevates true Architects into technological nobility!\n\n"
            "[TA James] A single human architect commanding an Antigravity swarm now wields the power of an entire 100-person software engineering department!\n\n"
            "[Prof. Peter] Lead with courage, wisdom, and moral conviction. The future belongs to the Conductors!\n\n"
            "[TA Sarah] Let us inspect the Next Horizon: True AI Science on Slide 42!"
        ),
        "koreanGuide": {
            "summary": "지휘관의 시대: 미래 소프트웨어 생태계를 주도하라 (두려움의 극복)",
            "points": [
                "시대착오적 공포: 'AI가 개발자를 대체할 것이다' ➔ 진실: 기계적 타이피스트는 사라지고 진정한 아키텍트는 귀족으로 격상",
                "새로운 지적 귀족: 93개 멀티에이전트 스웜을 지휘하는 1명의 아키텍트가 100명 규모의 IT 조직 역량을 발휘",
                "소명 중심 리더십: 아름다움과 무결성, 인간 번영을 위해 인공지능 교향악단을 당당히 지휘"
            ],
            "tips": "피터 교수가 학생들에게 지휘관으로서의 자긍심과 미래 기술 리더십의 비전을 심어줍니다."
        },
        "keyTerms": [
            {
                "term": "Architectural Nobility",
                "def": "The elite professional status of software architects possessing the vision and discipline to direct autonomous AI fleets.",
                "defKo": "아키텍처적 지적 리더십"
            },
            {
                "term": "100-Person Leverage Multiplier",
                "def": "The radical productivity amplification allowing a single human architect to achieve enterprise departmental output.",
                "defKo": "100인분 조직 레버리지 승수"
            }
        ]
    },
    # Slide 42: Next Horizon: True AI Science & HeurekaBench
    {
        "num": 42,
        "type": "content",
        "title": "NEXT HORIZON: TRUE AI SCIENCE & HEUREKABENCH",
        "subtitle": "Moving beyond synthetic coding benchmarks to autonomous scientific hypothesis discovery",
        "points": [
            "Benchmark Saturation: MMLU and HumanEval hit 99% ceilings; standard coding benchmarks no longer test frontier reasoning.",
            "HeurekaBench Breakthrough: Testing autonomous hypothesis formulation, Think-Act-Observe loops, and physical falsifiability.",
            "Session 11 Preview: Multi-agent scientific discovery in biochemistry, materials science, and antibiotic design."
        ],
        "script": (
            "[TA Sarah] Slide 42 previews our next exciting frontier: \"NEXT HORIZON: TRUE AI SCIENCE & HEUREKABENCH.\"\n\n"
            "[TA James] In Session 11, we take our multi-agent swarms into the laboratory of pure science! We will deconstruct Google's revolutionary HeurekaBench benchmark—testing AI models not on trivia, but on genuine scientific hypothesis discovery and mathematical proofs!\n\n"
            "[Prof. Peter] We will see how AI swarms discover new antibiotics and stabilize fusion reactors.\n\n"
            "[TA Sarah] Let us inspect our capstone enterprise case study on Slide 44!"
        ),
        "koreanGuide": {
            "summary": "다음 지평 예고: Session 11 진정한 AI 과학(True AI Science)과 휴레카벤치(HeurekaBench)",
            "points": [
                "벤치마크 포화의 한계: MMLU 99% 달성으로 기존 상식 퀴즈 벤치마크의 변별력 상실",
                "휴레카벤치(HeurekaBench): 가설 수립, Think-Act-Observe 관찰 루프, 물리적 반증 가능성을 평가하는 참된 과학 벤치마크",
                "Session 11 연계: 신약 바이오 항생제 발견 및 핵융합 플라즈마 안정화 알고리즘 탐구 예고"
            ],
            "tips": "사라 조교와 제임스 조교가 다음 강의(Session 11: True AI Science)의 과학적 스케일을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "HeurekaBench (HurekaBench)",
                "def": "Google's frontier scientific evaluation benchmark measuring an AI model's ability to discover novel empirical truths.",
                "defKo": "휴레카벤치 (진정한 과학 발견 평가 벤치마크)"
            },
            {
                "term": "Think-Act-Observe Loop",
                "def": "The scientific method executed by AI agents: formulating hypotheses, running lab simulations, and observing falsifications.",
                "defKo": "Think-Act-Observe 과학 탐구 루프"
            }
        ]
    },
    # Slide 43: The Architect's Unwavering Faithfulness
    {
        "num": 43,
        "type": "content",
        "title": "THE ARCHITECT'S UNWAVERING FAITHFULNESS",
        "subtitle": "Stewarding immense computational scale with humility, ethical rigor, and faithful service",
        "points": [
            "Power Demands Humility: Wielding 93-agent swarms requires profound ethical grounding and self-discipline.",
            "Faithful in the Small: Luke 16:10: Excellence in small lines of code prepares us for massive global architectures.",
            "Eternal Horizon: Building software systems that will stand the test of time and glorify our Creator."
        ],
        "script": (
            "[Prof. Peter] Slide 43 reflects on \"THE ARCHITECT'S UNWAVERING FAITHFULNESS.\" In Scripture, Luke 16:10 teaches us: 'Whoever is faithful in very little is also faithful in much.'\n\n"
            "[TA Sarah] When we command swarms that write millions of lines of code, we must remain faithful in every single detail—every security check, every privacy rule, and every human relationship.\n\n"
            "[TA James] We build systems that reflect the incorruptible truth and beauty of God.\n\n"
            "[Prof. Peter] Let us inspect our capstone enterprise case study on Slide 44!"
        ),
        "koreanGuide": {
            "summary": "지능 건축가의 변함없는 신실함: 누가복음 16장 10절과 작은 일에 충성하는 청지기직",
            "points": [
                "권능에 걸맞은 겸손: 93개 에이전트 군단을 부릴수록 더욱 깊은 윤리적 성찰과 겸손함 유지",
                "작은 것에 충성(누가복음 16:10): 작은 코드 한 줄의 무결성을 지키는 자가 거대한 글로벌 시스템을 총괄",
                "영원한 지평: 세월의 풍파를 견디고 하나님께 영광을 돌리는 견고한 소프트웨어 대성당 건축"
            ],
            "tips": "피터 교수가 누가복음 말씀을 인용하며 성실한 장인정신과 영적 신실함을 감동적으로 선포합니다."
        },
        "keyTerms": [
            {
                "term": "Architectural Faithfulness",
                "def": "The moral and technical consistency required to steward massive computational systems with integrity.",
                "defKo": "아키텍처적 신실함"
            },
            {
                "term": "Scriptural Humility",
                "def": "Recognizing that technological genius is a divine gift entrusted for the humble service of humanity.",
                "defKo": "성경적 청지기적 겸손"
            }
        ]
    },
    # Slide 44: Case Study 5: 35X Enterprise Engineering Velocity ROI
    {
        "num": 44,
        "type": "casestudy",
        "title": "CASE STUDY 5: 35X ENGINEERING VELOCITY ROI",
        "subtitle": "Global Enterprise Software Leader deploys Antigravity 2.0 across 4,500 engineers in 18 countries",
        "company": "Top-3 Global Enterprise SaaS Conglomerate",
        "problem": "4,500 enterprise software engineers spent 35% of sprint capacity writing repetitive boilerplate APIs and tests, causing major product delivery delays.",
        "solution": "Deployed Antigravity 2.0 swarm architecture with centralized skill vaults, `/grill-me` requirement hardening, and RDD diff gates.",
        "impact": "35X measured engineering velocity on feature delivery; sprint cycle time dropped from 21 days to 1.8 days; generated $140M in expanded annual engineering capacity.",
        "script": (
            "[Prof. Peter] Slide 44 presents our capstone enterprise case study: \"CASE STUDY 5: 35X ENTERPRISE ENGINEERING VELOCITY ROI BLUEPRINT.\"\n\n"
            "[TA Sarah] A top-3 global enterprise software conglomerate with 4,500 software engineers across 18 countries had a massive velocity crisis: feature release cycles took 21 days per sprint, and backlog debt was growing exponentially!\n\n"
            "[TA James] They rolled out Antigravity 2.0 to all 4,500 engineers: integrating shared enterprise skill vaults, enforcing `/grill-me` planning gates, and automating browser WebP test recordings across all repositories!\n\n"
            "[Prof. Peter] Look at the enterprise numbers: measured feature delivery velocity surged by 35X! Sprint cycle time collapsed from 21 days down to 1.8 days, creating 140 million dollars in expanded annual engineering capacity!\n\n"
            "[TA Sarah] That is the ultimate enterprise transformation.\n\n"
            "[TA James] Now let us deploy your own Antigravity Swarm in Lab 10 on Slide 45!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 5: 글로벌 4,500명 엔지니어 조직의 35배 속도 혁신 및 1억 4천만 달러 가치 창출",
            "points": [
                "문제 상황: 18개국 4,500명 엔지니어 조직이 21일의 스프린트 주기에 갇혀 극심한 개발 적체 겪음",
                "솔루션: 안티그래비티 2.0 전사 도입(사내 전용 스킬 금고, /grill-me 기획 게이트, RDD diff 감사 체계)",
                "성과: 기능 개발 속도 35배 가속, 스프린트 주기 21일 ➔ 1.8일로 압축, 연간 1억 4,000만 달러 개발 가치 창출"
            ],
            "tips": "사라 조교와 제임스 조교가 35배 가속과 1억 4천만 달러 가치 창출의 압도적 성과를 전하며 실습으로 유도합니다."
        },
        "keyTerms": [
            {
                "term": "35X Velocity Multiplier",
                "def": "The compounding speed acceleration achieved across an entire enterprise engineering organization via swarm automation.",
                "defKo": "35배 개발 속도 승수"
            },
            {
                "term": "Sprint Cycle Compression",
                "def": "The dramatic reduction in calendar days required to bring features from planning to live production release.",
                "defKo": "스프린트 주기 극적 압축"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 45: Hands-on Lab 10 & Conclusion
    {
        "num": 45,
        "type": "lab",
        "title": "🛠️ HANDS-ON LAB 10 & CONCLUSION",
        "subtitle": "Deploying an Antigravity 2.0 Swarm & Artifacts Verification Pipeline",
        "mission": "Initialize a new project using `agy plan`, execute an interactive `/grill-me` session, approve the generated `implementation_plan.md`, launch a parallel subagent swarm with Coder and Reviewer roles, and verify results in `walkthrough.md` with test proofs.",
        "steps": [
            "Step 1: Open terminal in workspace and run `agy plan 'Build complete task management API with JWT auth'`.",
            "Step 2: Run `/grill-me` to answer 5 interactive architectural questions and lock the specification.",
            "Step 3: Review the generated `implementation_plan.md` artifact and type `agy run --approved`.",
            "Step 4: Watch live Coder and Reviewer subagents mutate files and resolve unit tests in the split-view cockpit.",
            "Step 5: Inspect the published `walkthrough.md`, audit the git diffs, and celebrate your first swarm deployment!"
        ],
        "script": (
            "[TA Sarah] Here we are at Slide 45: \"🛠️ HANDS-ON LAB 10 & SESSION CONCLUSION!\"\n\n"
            "[TA James] Tonight's hands-on lab turns you into an Antigravity Swarm Commander! Step 1: Run `agy plan`. Step 2: Answer 5 questions in `/grill-me`. Step 3: Approve `implementation_plan.md`. Step 4: Watch Coder and Reviewer subagents refactor your code and fix bugs live! Step 5: Read `walkthrough.md`, audit the diffs, and merge your project!\n\n"
            "[Prof. Peter] Once you experience commanding an autonomous 93-agent swarm, you will never look back at traditional coding.\n\n"
            "[TA Sarah] In our next session, Session 11, we enter the frontier of pure science: True AI Science, HeurekaBench, and Autonomous Discovery!\n\n"
            "[Prof. Peter] On behalf of TA Sarah Jenkins, TA James Wilson, and the entire Smart Insight Lab, congratulations on mastering Session 10! Soli Deo Gloria, and we will see you in Session 11!"
        ),
        "koreanGuide": {
            "summary": "실습 과제 10 및 세션 마무리: Antigravity 2.0 스웜 배포 및 아티팩트 검증 파이프라인 구축",
            "points": [
                "실습 미션: agy plan 및 /grill-me 인터뷰를 통한 JWT 인증 태스크 관리 API 아키텍처 수립",
                "implementation_plan.md 검토 및 agy run --approved 실행",
                "분할 뷰 콕핏에서 코더와 리뷰어의 실시간 협업 관전 후 walkthrough.md 최종 감사 및 머지"
            ],
            "tips": "3인의 강사진이 오늘 수업의 성취를 축하하고 다음 세션(Session 11: True AI Science & HeurekaBench)에 대한 기대감을 높이며 마무리합니다."
        },
        "keyTerms": [
            {
                "term": "Hands-on Milestone",
                "def": "The practical engineering completion of a functioning technical artifact fulfilling the session's learning objectives.",
                "defKo": "실습 달성 마일스톤"
            },
            {
                "term": "Swarm Commander Certification",
                "def": "The formal mastery of multi-agent planning, execution, and artifact auditing within the Antigravity ecosystem.",
                "defKo": "스웜 총괄 지휘관 마스터 인증"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    }
]

def generate_session10_md(slides):
    lines = []
    lines.append("# Session 10: Escaping Developer Gravity: Antigravity 2.0 & Multi-Agent Orchestration Blueprint")
    lines.append("**Course:** The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom  ")
    lines.append("**Instructors:** Professor Peter Kim (Director), TA Sarah Jenkins (Senior AI Fellow) & TA James Wilson (DevOps TA) • Oikos University (www.oikos.edu)  ")
    lines.append("**Lecture Format:** Full 75-Minute Broadcast Trio Master Dialogue (4x Modules with 5 Enterprise Case Studies)  ")
    lines.append("**Total Slides:** 45 Slides (Expanded Multi-Presenter Master Edition)  ")
    lines.append("**Motto:** Soli Deo Gloria  ")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 📌 Table of Contents (목차)")
    
    for s in slides:
        num_str = f"{s['num']:02d}"
        title = s['title']
        slug = f"slide-{num_str}-{title.lower().replace(' ', '-').replace(':', '').replace('.', '').replace('&', 'and').replace('(', '').replace(')', '').replace('•', '').replace('\'', '').replace('’', '').replace('/', '-')}"
        slug = re.sub(r'-+', '-', slug).strip('-')
        lines.append(f"- [Slide {num_str}: {title}](#{slug})")
        
    lines.append("")
    lines.append("---")
    lines.append("")
    
    for s in slides:
        num_str = f"{s['num']:02d}"
        lines.append(f"## Slide {num_str}: {s['title']}")
        if s.get('subtitle'):
            lines.append(f"**Subtitle:** {s['subtitle']}")
        lines.append(f"**Instructor:** Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab")
        lines.append("")
        
        lines.append("### 🎙️ English Lecture Script (Full 75-Min Broadcast Trio Dialogue)")
        lines.append(s['script'])
        lines.append("")
        
        lines.append("### 🇰🇷 한국어 강의 가이드 및 핵심 요약")
        kg = s['koreanGuide']
        lines.append(f"**개요 요약:** {kg['summary']}")
        lines.append("")
        lines.append("**핵심 티칭 포인트:**")
        for pt in kg.get('points', []):
            lines.append(f"- {pt}")
        lines.append("")
        lines.append(f"**강의 전달 팁:** {kg.get('tips', '')}")
        lines.append("")
        
        if s.get('keyTerms'):
            lines.append("### 📚 Key Technical Terms (핵심 용어)")
            for kt in s['keyTerms']:
                lines.append(f"- **{kt['term']}** ({kt['defKo']}): {kt['def']}")
            lines.append("")
            
        lines.append("---")
        lines.append("")
        
    return "\n".join(lines)

def update_slides_data_js(slides):
    with open(SLIDES_DATA_JS, 'r', encoding='utf-8') as f:
        content = f.read()

    slides_json = json.dumps(slides, ensure_ascii=False, indent=2)
    new_export = f"export const SLIDES_SESSION_10 = {slides_json};"
    
    pattern = r"export\s+const\s+SLIDES_SESSION_10\s*=\s*\[[\s\S]*?\];"
    if re.search(pattern, content):
        updated_content = re.sub(pattern, lambda m: new_export, content, count=1)
        with open(SLIDES_DATA_JS, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Successfully updated SLIDES_SESSION_10 in slidesData.js!")
    else:
        print("Could not find SLIDES_SESSION_10 pattern in slidesData.js!")

def main():
    print(f"Total slides configured: {len(SLIDES_45_SESSION_10)}")
    
    # Verify part dividers
    part_slides = [s for s in SLIDES_45_SESSION_10 if s['type'] == 'section']
    print(f"Total PART Section Slides: {len(part_slides)}")
    for ps in part_slides:
        print(f"  Slide {ps['num']:02d}: {ps['title']}")
        
    # Verify case studies
    case_slides = [s for s in SLIDES_45_SESSION_10 if 'CASE STUDY' in s['title']]
    print(f"Total Case Study Slides: {len(case_slides)}")
    for cs in case_slides:
        print(f"  Slide {cs['num']:02d}: {cs['title']}")

    # 1. Write session10.md
    session10_md_content = generate_session10_md(SLIDES_45_SESSION_10)
    with open(SESSION10_MD, 'w', encoding='utf-8') as f:
        f.write(session10_md_content)
    print(f"Successfully generated and saved {SESSION10_MD} ({len(session10_md_content)} bytes)")
    
    # 2. Update slidesData.js
    update_slides_data_js(SLIDES_45_SESSION_10)
    
    print("Session 10 generation completed successfully!")

if __name__ == '__main__':
    main()
