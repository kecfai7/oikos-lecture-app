# -*- coding: utf-8 -*-
"""
Oikos University - Session 6 Clean 45-Slide Master Generator
Course: The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom
Session 6: The 1-Million Token Playground: Vibe Coding, Many-shot ICL, and Cost Optimization with Google AI Studio
Features:
- Full 45 Slides with 3-Presenter Trio (Prof. Peter Kim, TA Sarah Jenkins, TA James Wilson)
- Clean 4-Part Structure (Part 1: Slide 2, Part 2: Slide 12, Part 3: Slide 23, Part 4: Slide 30)
- 5 Practical Enterprise Case Studies:
    1. Slide 11: Translating Low-Resource 200-Speaker Indigenous Language via 100-Shot ICL
    2. Slide 22: Monolithic 1.2M Line Legacy Cobol-to-Java Migration in 1 Prompt
    3. Slide 29: Global Fintech Slashing $240K Monthly API Costs via Context Caching
    4. Slide 36: Zero-Code Enterprise ERP Dashboard Generation via Vibe Coding
    5. Slide 44: 22X Developer Velocity ROI & 6-Step Google AI Studio Blueprint
- Full sync with session6.md and slidesData.js (SLIDES_SESSION_6)
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
SESSION6_MD = os.path.join(BASE_DIR, "session6.md")

SLIDES_45_SESSION_6 = [
    # Slide 1: Course Title
    {
        "num": 1,
        "type": "title",
        "title": "OIKOS UNIVERSITY • SOLI DEO GLORIA",
        "subtitle": "THE ARCHITECT OF INTELLIGENCE: Mastering Agentic IT & Strategic Wisdom",
        "detail": "Session 6: The 1-Million Token Playground: Vibe Coding, Many-shot ICL, and Cost Optimization with Google AI Studio",
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab",
        "script": (
            "[Prof. Peter] Welcome back, global scholars and architects, to Oikos University! I am Professor Peter Kim, Director of Smart Insight Lab. Today, we step onto the frontier of massive cognitive scale on Slide 1: \"Session 6: The 1-Million Token Playground: Vibe Coding, Many-shot ICL, and Cost Optimization with Google AI Studio.\"\n\n"
            "[TA Sarah] Hello everyone! I am Sarah Jenkins, your Senior AI Research Fellow. For years, AI was constrained by tiny context windows—forcing us to chop documents into fragile vector fragments. But today, we explore what happens when an AI brain can ingest an entire library shelf in a single prompt!\n\n"
            "[TA James] And I am James Wilson, your DevOps TA! In production engineering, 1 million tokens sounds terrifying because of latency and API bills. Today, we show you how Google's revolutionary Context Caching slashes costs by 87% while delivering sub-second Vibe Coding speed!\n\n"
            "[Prof. Peter] Under our founding motto, \"SOLI DEO GLORIA—To God Alone Be the Glory,\" our calling is to harness this immense computational horizon with wisdom, rigor, and stewardship.\n\n"
            "[TA Sarah] Let us open Part 1 and enter the 1-Million Token Playground on Slide 2!"
        ),
        "koreanGuide": {
            "summary": "Session 6 개요 및 Oikos University 3인 강사진(피터 교수, 사라 수석조교, 제임스 개발조교) 환영 인사",
            "points": [
                "강의 주제: 100만 토큰 대규모 문맥, 바이브 코딩(Vibe Coding), 다발 예시 인컨텍스트 러닝(Many-shot ICL)",
                "기존 청킹(Chunking)의 한계를 뛰어넘어 전체 코드베이스와 수백 편의 문서를 단일 프롬프트로 처리",
                "Google AI Studio 및 컨텍스트 캐싱(Context Caching)을 통한 87% 비용 절감과 FinOps 최적화"
            ],
            "tips": "피터 교수의 거시적 패러다임과 사라 조교의 ICL 원리, 제임스 조교의 FinOps 비용 절감 관점을 유기적으로 연결하세요."
        },
        "keyTerms": [
            {
                "term": "1-Million Token Horizon",
                "def": "The frontier capability of processing up to 1,000,000 multimodal tokens (750,000 words) in a single unified inference pass.",
                "defKo": "100만 토큰 대규모 문맥 (1M Context)"
            },
            {
                "term": "Vibe Coding",
                "def": "An AI-native development paradigm where software is created rapidly through natural language intent and iterative reasoning.",
                "defKo": "바이브 코딩 (자연어 직관 소프트웨어 개발)"
            }
        ]
    },
    # Slide 2: Part 1 Section Divider
    {
        "num": 2,
        "type": "section",
        "title": "PART 1: THE 1M-TOKEN HORIZON & THE END OF FRAGMENTATION",
        "subtitle": "Transcending small context windows and ending vector chunking loss under Soli Deo Gloria",
        "script": (
            "[TA Sarah] Look at Slide 2: \"PART 1: THE 1M-TOKEN HORIZON & THE END OF FRAGMENTATION.\" Professor, why is the 1-million token context window considered such a historic turning point in AI history?\n\n"
            "[Prof. Peter] Because for the first time, artificial intelligence breaks free from cognitive amnesia! In previous generations, models had tiny 4K or 8K token windows. If you fed a 100-page book, the model forgot chapter 1 before reading chapter 5!\n\n"
            "[TA James] Engineers had to build complex vector databases, write chunking scripts, and pray that cosine search didn't drop the critical paragraph. With 1M tokens in Gemini 3.5 Pro, you feed the ENTIRE book into the prompt, and the model maintains full attention across all 750,000 words!\n\n"
            "[TA Sarah] In Part 1, we deconstruct the 'Needle In A Haystack' test and explore the fundamental nature of tokens.\n\n"
            "[Prof. Peter] Let us examine the traditional context cage on Slide 3."
        ),
        "koreanGuide": {
            "summary": "Part 1 섹션 전환: 100만 토큰의 지평과 지식 파편화의 종말",
            "points": [
                "과거 4K/8K 문맥 창의 비극: 100페이지 책을 넣으면 앞장을 잊어버리던 단기 기억상실 한계",
                "RAG 청킹의 한계 극복: 수백 개로 쪼갤 필요 없이 책 전체(75만 단어)를 단일 프롬프트에 통째로 적재",
                "100% 어텐션 유지: 건초더미 속 바늘 찾기(Needle In A Haystack) 99.8% 정확도 달성"
            ],
            "tips": "사라 조교가 과거 청킹의 고통을 짚고, 제임스가 100만 토큰의 무청킹 혁신을 엔지니어링 관점에서 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Context Window Cage",
                "def": "The computational memory limit restricting how many tokens an LLM can process simultaneously in a single prompt.",
                "defKo": "컨텍스트 윈도우 한계 (문맥 감옥)"
            },
            {
                "term": "Needle In A Haystack (NIAH)",
                "def": "A rigorous benchmark testing an LLM's ability to retrieve precise factual statements hidden inside massive text corpora.",
                "defKo": "건초더미 속 바늘 찾기 벤치마크"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 3: The Traditional Context Cage
    {
        "num": 3,
        "type": "content",
        "title": "THE TRADITIONAL CONTEXT CAGE",
        "subtitle": "How tiny 4K/8K token limits forced fragmentation, retrieval errors, and lost nuance",
        "points": [
            "Cognitive Fragmentation: Documents chopped into 500-character chunks lost high-level narrative context.",
            "Vector Search Misses: If an embedding model failed to match synonyms, vital paragraphs were lost forever.",
            "Synthesizing Bottleneck: Cross-document relationships spanning 10 different files could not be evaluated."
        ],
        "script": (
            "[TA Sarah] Slide 3 details \"THE TRADITIONAL CONTEXT CAGE.\" In legacy LLM systems, we spent 80% of our engineering time fighting context limits.\n\n"
            "[TA James] Look at the failure modes on screen: When you chop a financial report into tiny pieces, you lose the connection between the CEO's opening letter and footnote 47 on page 89! Vector search might pull 3 chunks, but it misses the connective tissue.\n\n"
            "[Prof. Peter] It was like trying to read a great philosophical masterpiece through a 1-inch magnifying glass, peeking at three words at a time! You see isolated phrases, but you lose the transcendent wisdom of the whole.\n\n"
            "[TA Sarah] Let us see how the 1-Million Token Horizon demolishes this cage on Slide 4!"
        ),
        "koreanGuide": {
            "summary": "전통적 컨텍스트 감옥의 한계: 청킹으로 인한 문맥 단절과 의미 손실",
            "points": [
                "인지적 파편화: 문서를 500자 단위로 쪼개면서 CEO 서한과 89페이지 각주 간의 연결 고리 상실",
                "벡터 검색 누락: 동의어나 의미적 뉘앙스를 놓쳐 중요한 단락이 검색에서 영구 제외되는 취약점",
                "돋보기 효과: 1인치 돋보기로 대성당의 설계도를 부분만 들여다보던 과거 방식의 한계"
            ],
            "tips": "피터 교수의 '1인치 돋보기' 비유를 살려 전체론적(Holistic) 문맥의 중요성을 역설하세요."
        },
        "keyTerms": [
            {
                "term": "Semantic Fragmentation",
                "def": "The degradation of structural meaning caused by arbitrarily segmenting cohesive long-form documents.",
                "defKo": "의미론적 파편화"
            },
            {
                "term": "Holistic Context",
                "def": "The unified, unsegmented ingestion of complete datasets preserving all internal cross-references.",
                "defKo": "전체론적 통합 문맥"
            }
        ]
    },
    # Slide 4: Entering the 1-Million Token Playground
    {
        "num": 4,
        "type": "content",
        "title": "ENTERING THE 1-MILLION TOKEN PLAYGROUND",
        "subtitle": "Ingesting 750,000 words, 1 hour of video, or 60,000 lines of source code in 1 prompt",
        "points": [
            "Massive Ingestion: Ingesting 5 complete textbooks, 100 academic papers, or 50 SEC filings simultaneously.",
            "Multimodal Capacity: Combining 1 hour of recorded video, 10 audio lectures, and 200 PDFs in a single prompt.",
            "Sub-Second Recall: Gemini 3.5 Pro maintains near-perfect recall across the entire 1M token spectrum."
        ],
        "script": (
            "[Prof. Peter] Slide 4 welcomes you to \"THE 1-MILLION TOKEN PLAYGROUND.\" What does 1 million tokens actually look like in human terms?\n\n"
            "[TA Sarah] One million tokens equals approximately 750,000 English words! That is the complete works of William Shakespeare, or 5 full semesters of university textbooks, or 60,000 lines of enterprise C++ source code—all loaded into one single prompt!\n\n"
            "[TA James] And it is natively multi-modal! In Google AI Studio, you can drop a 1-hour 4K MP4 video file, 10 audio meeting recordings, and a 200-page spreadsheet. Gemini processes all modalities in one unified transformer attention pass!\n\n"
            "[Prof. Peter] Let us examine the rigorous proof of this capability: the Needle In A Haystack test on Slide 5."
        ),
        "koreanGuide": {
            "summary": "100만 토큰 플레이그라운드 진입: 75만 단어와 1시간 비디오의 동시 처리",
            "points": [
                "인간적 체감 규모: 셰익스피어 전집 전체, 대학 5학기 분량 교재, 또는 6만 줄의 C++ 소스코드",
                "멀티모달 통합: 1시간짜리 4K 영상, 10개 음성 파일, 200페이지 시트를 단일 트랜스포머 어텐션으로 처리",
                "인식의 대전환: 부분 검색을 넘어선 전체 통합 추론(Global Attention)의 실현"
            ],
            "tips": "사라 조교가 셰익스피어 전집 비유를 통해 100만 토큰의 거대한 스케일을 실감 나게 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Multimodal Token Ingestion",
                "def": "The simultaneous processing of video frames, audio waveforms, text, and structured tables in a single prompt.",
                "defKo": "멀티모달 통합 토큰 수용"
            },
            {
                "term": "Global Attention Matrix",
                "def": "Full self-attention computed across the entire multi-million token sequence without sliding-window dropouts.",
                "defKo": "전역 어텐션 행렬"
            }
        ]
    },
    # Slide 5: The 'Needle In A Haystack' Test
    {
        "num": 5,
        "type": "content",
        "title": "THE 'NEEDLE IN A HAYSTACK' TEST",
        "subtitle": "Gemini 3.5 Pro achieves > 99.8% retrieval accuracy across the entire 1M context horizon",
        "points": [
            "The Benchmark Protocol: Hiding a single random fact ('The secret password is BlueDragon-42') inside 1M tokens.",
            "Depth & Position Invariance: Placing the fact at 10%, 50%, or 99% depth reveals zero retrieval degradation.",
            "Flawless Needle Map: Gemini 3.5 Pro displays a solid green 100% recall matrix across all document lengths."
        ],
        "script": (
            "[TA Sarah] Slide 5 presents the famous \"NEEDLE IN A HAYSTACK TEST.\" In AI research, having a large context window is useless if the model hallucinates or ignores the middle paragraphs.\n\n"
            "[TA James] In this benchmark, researchers take 1 million tokens of dense legal text, hide a single sentence at the 47% depth mark—like 'The secret server password is BlueDragon-42'—and prompt the model: 'What is the secret password?'\n\n"
            "[Prof. Peter] Older models showed severe degradation in the middle—the 'Lost in the Middle' phenomenon. But look at the heatmap on screen: Gemini 3.5 Pro achieves over 99.8% accuracy! It is a solid wall of green across all depths!\n\n"
            "[TA Sarah] That proves that every single token is actively attended to by the model.\n\n"
            "[TA James] Let us inspect what a token actually is on Slide 6!"
        ),
        "koreanGuide": {
            "summary": "건초더미 속 바늘 찾기(NIAH) 테스트: 99.8% 이상의 무결점 회수율 입증",
            "points": [
                "테스트 프로토콜: 100만 토큰 분량의 문서 한가운데 무작위 비밀 문장을 숨기고 정확히 찾아내는지 검증",
                "'중간 유실(Lost in the Middle)' 현상의 극복: 문서의 앞, 중간, 뒤 어디에 위치하든 완벽한 검색",
                "초록색 히트맵: 제미나이 3.5 프로의 99.8% 회수율을 시각적으로 입증"
            ],
            "tips": "제임스 조교와 피터 교수가 건초더미 테스트의 히트맵 결과를 명쾌하게 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Lost in the Middle Phenomenon",
                "def": "The tendency of earlier language models to remember text at the beginning and end of prompts while ignoring the center.",
                "defKo": "문맥 중간 유실 현상"
            },
            {
                "term": "Depth Invariance",
                "def": "The property of maintaining uniform factual retrieval accuracy regardless of where facts are located in context.",
                "defKo": "위치 불변성 (균일 검색력)"
            }
        ]
    },
    # Slide 6: Understanding the Token: Language's Lego Blocks
    {
        "num": 6,
        "type": "content",
        "title": "UNDERSTANDING THE TOKEN: LANGUAGE'S LEGO BLOCKS",
        "subtitle": "Byte-Pair Encoding (BPE), vocabulary compression, and token arithmetic",
        "points": [
            "Token Arithmetic: 1 Token ≈ 0.75 Words (English) | 1,000 Tokens ≈ 750 Words.",
            "Sub-word Tokenization: Common words like 'architect' are 1 token; rare words are split into sub-pieces.",
            "Multimodal Tokenization: 1 second of audio ≈ 25 tokens; 1 video frame ≈ 258 tokens."
        ],
        "script": (
            "[Prof. Peter] Slide 6 explores \"UNDERSTANDING THE TOKEN: LANGUAGE'S LEGO BLOCKS.\" To master FinOps and prompt architecture, you must understand token arithmetic.\n\n"
            "[TA Sarah] A token is not a character, and it is not always a full word. It is a sub-word mathematical chunk created by Byte-Pair Encoding (BPE). In English, 1 token is roughly 4 characters or 0.75 words.\n\n"
            "[TA James] In multimodal models, video and audio are also converted into tokens! One second of recorded speech is roughly 25 tokens, while a high-resolution video frame consumes about 258 tokens. When you understand this arithmetic, you can budget your costs down to the penny!\n\n"
            "[Prof. Peter] Let us examine Gemini 3.5 Pro's frontier benchmark performance on Slide 7."
        ),
        "koreanGuide": {
            "summary": "토큰의 이해: 언어와 멀티모달의 레고 블록 및 토큰 산술",
            "points": [
                "토큰 산술 공식: 1 토큰 ≈ 0.75 단어(영문 기준), 1,000 토큰 ≈ 750 단어",
                "BPE(Byte-Pair Encoding): 자주 쓰는 단어는 1토큰, 희귀 단어는 하위 어절로 스마트 분할",
                "멀티모달 토큰 환산: 음성 1초 ≈ 25토큰, 비디오 1프레임 ≈ 258토큰의 명확한 계산법"
            ],
            "tips": "사라 조교가 토큰 산술 공식을 짚고 제임스가 멀티모달 토큰 계산 팁을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Byte-Pair Encoding (BPE)",
                "def": "A subword tokenization algorithm compressing raw text into efficient statistical token vocabularies.",
                "defKo": "바이트 페어 인코딩 (BPE)"
            },
            {
                "term": "Token Arithmetic",
                "def": "The quantitative calculation of input/output token counts for latency and cost estimation.",
                "defKo": "토큰 산술 (용량 및 비용 계산)"
            }
        ]
    },
    # Slide 7: Gemini 3.5 Pro: The 1501 ELO Super Brain
    {
        "num": 7,
        "type": "content",
        "title": "GEMINI 3.5 PRO: THE 1501 ELO SUPER BRAIN",
        "subtitle": "Frontier coding, mathematical reasoning, and multimodal benchmark domination",
        "points": [
            "Chatbot Arena Benchmark: Gemini 3.5 Pro tops global leaderboards with a 1501 ELO rating.",
            "Codeforces & HumanEval: Solves complex competitive programming and algorithm design autonomously.",
            "Deep Multimodal Reasoning: Solves PhD-level physics, biochemistry, and architectural blueprints."
        ],
        "script": (
            "[TA Sarah] Slide 7 highlights \"GEMINI 3.5 PRO: THE 1501 ELO SUPER BRAIN.\" On global independent benchmarks like LMSYS Chatbot Arena, Gemini leads the frontier.\n\n"
            "[TA James] Look at the coding benchmarks: On competitive programming platforms like Codeforces and HumanEval, Gemini 3.5 Pro outperforms human senior software engineers, writing optimized Python, Rust, and Go in seconds!\n\n"
            "[Prof. Peter] But technical capability must be matched with human intentionality. A 1500 ELO model without rigorous guidance is merely a fast calculator; guided by an Intelligence Architect, it becomes an engine of scientific discovery.\n\n"
            "[TA Sarah] Let us launch an interactive poll on Slide 8 to evaluate how our students use context windows!"
        ),
        "koreanGuide": {
            "summary": "제미나이 3.5 프로의 압도적 벤치마크: 1501 ELO와 최고 수준의 코딩 능력",
            "points": [
                "LMSYS 챗봇 아레나 1501 ELO 달성: 글로벌 프론티어 AI 랭킹 1위 석권",
                "알고리즘 코딩 압도: Codeforces, HumanEval에서 인간 시니어 엔지니어 이상의 코드 작성력",
                "지능 건축가의 가이드: 강력한 모델일수록 인간 아키텍트의 명확한 시스템 프롬프트 지휘가 필수적"
            ],
            "tips": "사라 조교와 제임스 조교가 벤치마크 지표를 설명하고 피터 교수가 인간 지휘자의 역할을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "LMSYS Chatbot Arena ELO",
                "def": "A blind, crowdsourced benchmark rating LLM capabilities based on comparative human preference scores.",
                "defKo": "LMSYS 챗봇 아레나 ELO 레이팅"
            },
            {
                "term": "Competitive Programming Synthesis",
                "def": "The automated generation of mathematically optimal algorithms to solve complex data structure challenges.",
                "defKo": "경진대회급 알고리즘 자동 생성"
            }
        ]
    },
    # Slide 8: Interactive Poll: Expanding Your Desk
    {
        "num": 8,
        "type": "poll",
        "title": "📨 INTERACTIVE POLL: EXPANDING YOUR DESK",
        "subtitle": "If you could load an entire enterprise asset into 1 prompt, what would you load first?",
        "pollOptions": [
            "Option A: Our complete 100,000-line software codebase to fix legacy bugs",
            "Option B: 5 years of financial filings & auditor notes for valuation modeling",
            "Option C: 50 scientific research papers to find cross-disciplinary breakthroughs",
            "Option D: 100 hours of user interview audio transcripts to design a new product"
        ],
        "script": (
            "[Prof. Peter] Slide 8 is our \"INTERACTIVE POLL: EXPANDING YOUR DESK.\" Take out your devices and cast your vote right now!\n\n"
            "[TA Sarah] The question is: \"If you had an infinite 1-million-token desk and could load an entire enterprise asset in one prompt, what would you load first?\"\n\n"
            "[TA James] Option A: 100,000 lines of software code. Option B: 5 years of financial filings. Option C: 50 scientific research papers. Or Option D: 100 hours of customer interview recordings!\n\n"
            "[TA Sarah] The live votes are streaming in, and every domain has passionate advocates.\n\n"
            "[Prof. Peter] Let us analyze the poll results and explore cognitive re-alignment on Slide 9."
        ),
        "koreanGuide": {
            "summary": "실시간 수강생 설문: 100만 토큰의 거대한 책상 위에 가장 먼저 올릴 자산은?",
            "points": [
                "수강생 실시간 참여를 통한 대규모 문맥 활용 도메인 선호도 조사",
                "코드베이스, 재무 공시, 학술 논문, 고객 인터뷰 음성 등 다양한 활용처 탐색",
                "자신의 실무 업무에 100만 토큰을 즉시 적용하는 상상력 확장"
            ],
            "tips": "3인의 강사진이 수강생들의 다양한 선택을 격려하며 흥미진진하게 진행합니다."
        },
        "keyTerms": [
            {
                "term": "Contextual Leverage",
                "def": "The strategic productivity advantage gained by analyzing entire institutional assets simultaneously.",
                "defKo": "문맥적 레버리지 (전체 데이터 동시 활용)"
            },
            {
                "term": "Domain Asset Ingestion",
                "def": "Loading comprehensive, specialized enterprise datasets into unified model context.",
                "defKo": "도메인 핵심 자산 통합 적재"
            }
        ]
    },
    # Slide 9: The Cognitive Re-Alignment
    {
        "num": 9,
        "type": "content",
        "title": "THE COGNITIVE RE-ALIGNMENT",
        "subtitle": "Moving from chunk-and-search mentality to holistic context orchestration",
        "points": [
            "The Old Mental Model: 'How do I summarize this into 200 words so the AI doesn't choke?'",
            "The 2026 Mental Model: 'How do I dump the entire problem space into the prompt so the AI sees everything?'",
            "Holistic Reasoning: The model detects non-obvious correlations that human search queries would never discover."
        ],
        "script": (
            "[TA Sarah] Slide 9 illustrates \"THE COGNITIVE RE-ALIGNMENT.\" We must upgrade our mental models!\n\n"
            "[TA James] In the old world, developers spent hours manually cutting down documents, thinking: 'I hope the model doesn't run out of memory.' In 2026, the mental model flips: dump the entire 500-page specification, the complete schema, and 50 past bug tickets into the prompt!\n\n"
            "[Prof. Peter] When the model sees the entire problem space simultaneously, it discovers hidden correlations between bug 12 and configuration file 4 that no human search query would ever uncover!\n\n"
            "[TA Sarah] Let us inspect our first enterprise case study on Slide 11!"
        ),
        "koreanGuide": {
            "summary": "인지적 재정렬: 쪼개서 넣던 과거에서 통째로 넣는 전체론적 오케스트레이션으로의 전환",
            "points": [
                "과거의 멘탈 모델: 'AI가 멈추지 않게 어떻게든 200단어로 요약해서 쪼개 넣어야지'",
                "2026년 멘탈 모델: '문제 공간 전체(500페이지)를 통째로 부어넣어 AI가 모든 맥락을 보게 하자'",
                "숨겨진 상관관계 발견: 전체 데이터를 조망할 때 비로소 드러나는 비직관적 시스템 버그 해결"
            ],
            "tips": "사라 조교와 피터 교수가 개발자들의 멘탈 모델 전환(Paradigm Flip)을 강력하게 촉구합니다."
        },
        "keyTerms": [
            {
                "term": "Cognitive Re-Alignment",
                "def": "The intellectual transition from fragmented, constrained prompting to comprehensive, whole-system context ingestion.",
                "defKo": "인지적 재정렬 (문맥 확장 멘탈 모델)"
            },
            {
                "term": "Whole-System Ingestion",
                "def": "Providing complete domain context in a single prompt to enable holistic relational reasoning.",
                "defKo": "전체 시스템 통합 주입"
            }
        ]
    },
    # Slide 10: Part 1 Transition: Entering the Forge
    {
        "num": 10,
        "type": "content",
        "title": "PART 1 TRANSITION: ENTERING THE FORGE",
        "subtitle": "Connecting massive context windows to Many-Shot In-Context Learning and FinOps caching",
        "points": [
            "From Capacity to Control: 1M tokens provides the canvas; In-Context Learning (ICL) provides the brush.",
            "The Cost Challenge: Processing 1M tokens repeatedly is expensive without intelligent Context Caching.",
            "The Roadmap Ahead: Master Many-Shot ICL in Part 2, slash costs by 87% in Part 3, and Vibe Code in Part 4."
        ],
        "script": (
            "[Prof. Peter] Slide 10 bridges our roadmap: \"PART 1 TRANSITION: ENTERING THE FORGE.\"\n\n"
            "[TA Sarah] We have established that 1M tokens gives us an infinite canvas. But an infinite canvas without technique produces chaos!\n\n"
            "[TA James] How do we control model behavior without spending $50,000 on fine-tuning? The answer is Many-Shot In-Context Learning! And how do we keep our cloud bills low? The answer is Context Caching!\n\n"
            "[Prof. Peter] Let us examine our first real-world case study on Slide 11!"
        ),
        "koreanGuide": {
            "summary": "Part 1 전환: 거대한 캔버스에서 정밀한 제어로 (Many-Shot ICL 및 캐싱 예고)",
            "points": [
                "용량에서 제어로: 100만 토큰이 거대한 캔버스라면, 인컨텍스트 러닝(ICL)은 정밀한 붓",
                "비용 극복 과제: 100만 토큰을 매번 호출할 때 발생하는 비용을 '컨텍스트 캐싱'으로 87% 절감",
                "Part 2~4 로드맵 제시: Many-Shot ICL ➔ FinOps 캐싱 ➔ 바이브 코딩 실전"
            ],
            "tips": "제임스 조교가 파인튜닝 비용 대비 ICL의 경제성을 짚으며 Part 2로 자연스럽게 연결합니다."
        },
        "keyTerms": [
            {
                "term": "In-Context Learning (ICL)",
                "def": "The ability of large models to learn complex tasks instantaneously from prompt exemplars without weight updates.",
                "defKo": "인컨텍스트 러닝 (프롬프트 내 즉각 학습)"
            },
            {
                "term": "Architectural Bridge",
                "def": "The conceptual linkage connecting hardware context capacity with software control and FinOps optimization.",
                "defKo": "아키텍처 전환 가교"
            }
        ]
    },
    # Slide 11: Case Study 1: Translating 200-Speaker Indigenous Language
    {
        "num": 11,
        "type": "casestudy",
        "title": "CASE STUDY 1: 200-SPEAKER INDIGENOUS TRANSLATION",
        "subtitle": "Preserving an endangered language with zero public web data using 100-shot Many-Shot ICL",
        "company": "Global Linguistic Preservation Project",
        "problem": "Kalamang, an endangered Papuan language with under 200 living speakers, had zero internet presence, making traditional ML fine-tuning mathematically impossible.",
        "solution": "Loaded an entire 500-page linguistic grammar book, 1,000-word dictionary, and 100 bilingual exemplar sentences into Gemini's 1M context window.",
        "impact": "Achieved fluent English-to-Kalamang translation matching human field linguist benchmarks in 1 second, preserving the language forever with $0 in model training costs.",
        "script": (
            "[Prof. Peter] Slide 11 presents \"CASE STUDY 1: 200-SPEAKER INDIGENOUS TRANSLATION.\" This is one of the most inspiring scientific breakthroughs in Google's research history.\n\n"
            "[TA Sarah] Kalamang is an endangered language spoken on a tiny island in Indonesia by fewer than 200 elderly people. There were zero web pages, zero Wikipedia articles, and zero parallel corpora on the internet. Traditional machine learning fine-tuning was 100% impossible!\n\n"
            "[TA James] Google researchers took a single 500-page scanned field linguistics grammar book, a 1,000-word dictionary, and 100 translated example sentences, loading them all into Gemini's 1-million-token context window in one prompt!\n\n"
            "[Prof. Peter] Look at the outcome: without training or fine-tuning a single model weight, Gemini mastered the grammar and translated complex sentences with accuracy matching professional human linguists!\n\n"
            "[TA Sarah] That is the miracle of Many-Shot In-Context Learning.\n\n"
            "[TA James] Now let us open Part 2 and master the mechanics of Many-Shot ICL on Slide 12!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 1: 200명 남은 칼라망어(Kalamang) 번역 기적과 100-Shot ICL",
            "points": [
                "문제 상황: 인도네시아 200명 미만의 소수 언어로 인터넷 데이터가 전무하여 기존 딥러닝 파인튜닝 불가능",
                "솔루션: 500페이지 문법책, 1,000단어 사전, 100개 번역 예시를 제미나이 100만 토큰 창에 단일 주입",
                "성과: 단 한 번의 가중치 학습 없이 인간 언어학자 수준의 정밀 번역 성공 및 소멸 위기 언어 영구 보존"
            ],
            "tips": "사라 조교와 피터 교수가 모델 가중치 변경 없이 오직 문맥(Prompt)만으로 새로운 언어를 마스터한 충격을 전합니다."
        },
        "keyTerms": [
            {
                "term": "Low-Resource Language",
                "def": "A human language with minimal digital text presence, presenting severe challenges for statistical machine learning.",
                "defKo": "저자원 언어 (데이터 희소 언어)"
            },
            {
                "term": "Weight-Free Learning",
                "def": "Acquiring domain mastery purely through in-context prompt exemplars without modifying neural network parameters.",
                "defKo": "무학습 인컨텍스트 습득"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 12: Part 2 Section Divider
    {
        "num": 12,
        "type": "section",
        "title": "PART 2: MANY-SHOT IN-CONTEXT LEARNING (ICL)",
        "subtitle": "Shifting from costly fine-tuning to instant domain mastery using 50 to 100 prompt exemplars",
        "script": (
            "[TA Sarah] Look at Slide 12: \"PART 2: MANY-SHOT IN-CONTEXT LEARNING (ICL).\" Now we explore how to turn Gemini into an instant domain expert in any field!\n\n"
            "[Prof. Peter] For years, AI developers believed that to teach a model a specialized skill, you had to collect 100,000 data rows, rent GPU clusters, and run LoRA fine-tuning for two weeks.\n\n"
            "[TA James] Many-Shot ICL completely destroys that assumption! By providing 50 to 100 gold-standard input-output pairs inside the 1M context window, the model locks into your exact format, tone, and logic with near-zero error.\n\n"
            "[TA Sarah] Let us inspect why Many-Shot ICL replaces traditional fine-tuning on Slide 13!"
        ),
        "koreanGuide": {
            "summary": "Part 2 섹션 전환: Many-Shot 인컨텍스트 러닝을 통한 즉각적 도메인 전문가화",
            "points": [
                "파인튜닝 패러다임의 붕괴: 10만 개 데이터셋과 수주일의 GPU 학습 대신 50~100개 예시로 즉시 목표 달성",
                "골드 스탠다드 예시(Gold-Standard Exemplars): 완벽한 입출력 쌍을 문맥에 배치하여 포맷과 로직 고정",
                "즉각적인 모델 적응력과 유지보수의 용이성"
            ],
            "tips": "제임스 조교가 비싼 파인튜닝 대신 프롬프트 예시 주입이 왜 실무에서 압도적인지 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Many-Shot ICL",
                "def": "Providing dozens or hundreds of high-quality input-output examples directly in prompt context to steer model behavior.",
                "defKo": "다발 예시 인컨텍스트 러닝 (Many-Shot ICL)"
            },
            {
                "term": "Fine-Tuning Replacement",
                "def": "The architectural practice of substituting model retraining with rich in-context demonstrations.",
                "defKo": "파인튜닝 대체 패러다임"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 13: Shifting from Fine-Tuning to Many-Shot ICL
    {
        "num": 13,
        "type": "comparison",
        "title": "SHIFTING FROM FINE-TUNING TO MANY-SHOT ICL",
        "subtitle": "Comparing GPU training costs, deployment agility, and catastrophic forgetting risks",
        "leftCard": {
            "tag": "FINE-TUNING (LEGACY)",
            "title": "Weight Retraining",
            "points": [
                "Requires massive datasets (10,000+ examples).",
                "Costs $5,000 - $50,000 in GPU cloud compute.",
                "High risk of Catastrophic Forgetting (loses general reasoning).",
                "Iteration Cycle: Days or weeks to update weights."
            ]
        },
        "rightCard": {
            "tag": "MANY-SHOT ICL (2026)",
            "title": "Context Steering",
            "points": [
                "Requires only 50 - 100 curated golden exemplars.",
                "Costs $0 in training compute; uses standard inference.",
                "Zero catastrophic forgetting; general intelligence intact.",
                "Iteration Cycle: 5 seconds (just edit the text prompt!)."
            ]
        },
        "script": (
            "[TA Sarah] Slide 13 compares \"FINE-TUNING VS. MANY-SHOT ICL.\" Look at the stark contrast in agility.\n\n"
            "[TA James] In fine-tuning, if your CEO decides to change the JSON output schema on Tuesday, you have to re-train the model on GPUs for 4 days! With Many-Shot ICL, you simply edit 3 lines in your prompt text, and your agent adopts the new schema in 5 seconds flat!\n\n"
            "[Prof. Peter] Notice also 'Catastrophic Forgetting': when you fine-tune model weights on specialized legal data, the model often loses its general coding and math abilities. Many-Shot ICL leaves the weights pristine, giving you world-class specialized output while retaining genius-level general intelligence!\n\n"
            "[TA Sarah] Let us inspect the mechanics of the shot on Slide 14."
        ),
        "koreanGuide": {
            "summary": "파인튜닝 vs Many-Shot ICL 비교: 민첩성, 비용, 파괴적 망각 방지",
            "points": [
                "수정 속도: 스키마 변경 시 파인튜닝은 4일간 GPU 재학습 필요 vs ICL은 프롬프트 3줄 수정으로 5초 만에 완료",
                "파괴적 망각(Catastrophic Forgetting) 극복: 가중치를 건드리지 않아 모델의 일반 지능과 코딩력이 완벽 보존",
                "데이터 요구량: 10,000건의 방대한 데이터 대신 50~100건의 정예 골든 예시로 충분"
            ],
            "tips": "사라 조교와 제임스 조교가 5초 만의 스키마 변경 시연을 통해 ICL의 압도적 민첩성을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Catastrophic Forgetting",
                "def": "The tendency of a neural network to completely lose previously learned general knowledge upon being fine-tuned on new data.",
                "defKo": "파괴적 망각 현상"
            },
            {
                "term": "Golden Exemplar Set",
                "def": "A meticulously curated collection of representative input-output pairs illustrating ideal system behavior.",
                "defKo": "골든 예시 세트"
            }
        ]
    },
    # Slide 14: The Mechanics of the Shot
    {
        "num": 14,
        "type": "content",
        "title": "THE MECHANICS OF THE SHOT",
        "subtitle": "Structuring Input-Output pairs: 0-Shot, Few-Shot (5-Shot), Many-Shot (100-Shot)",
        "points": [
            "0-Shot: Raw instruction ('Classify this invoice') ➔ 72% accuracy, unpredictable formatting.",
            "5-Shot (Few-Shot): Basic examples ➔ 84% accuracy, occasional edge-case hallucination.",
            "100-Shot (Many-Shot): Comprehensive edge-case coverage ➔ 98.6% deterministic formatting and reasoning."
        ],
        "script": (
            "[Prof. Peter] Slide 14 deconstructs \"THE MECHANICS OF THE SHOT: From 0-Shot to Many-Shot.\"\n\n"
            "[TA Sarah] In a 0-Shot prompt, you give instructions with zero examples. The model guesses the format and gets about 72% accuracy. In a 5-Shot prompt, you provide 5 examples, raising accuracy to 84%.\n\n"
            "[TA James] But when you scale to 50 or 100 shots inside the 1M context window, accuracy surges to 98.6%! The model encounters every edge case, handles unusual foreign currencies, parses broken dates, and outputs pristine, validated JSON every single time!\n\n"
            "[Prof. Peter] More shots create statistical inertia that locks the model into deterministic perfection.\n\n"
            "[TA Sarah] Let us see how Many-Shot ICL overcomes Out-of-Distribution barriers on Slide 15."
        ),
        "koreanGuide": {
            "summary": "샷(Shot)의 메커니즘: 0-Shot에서 100-Shot으로의 정확도 도약 곡선",
            "points": [
                "0-Shot (72%): 예시 없는 지시문은 형식의 변동성과 오류를 수반",
                "5-Shot (84%): 기본적인 패턴을 학습하나 예외 상황(Edge Cases)에서 취약",
                "100-Shot (98.6%): 100개의 다양한 예외 사례를 학습하여 오차 없는 결정론적 JSON 출력 실현"
            ],
            "tips": "제임스 조교가 100개의 예시가 만들어내는 '통계적 관성(Statistical Inertia)'의 위력을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Statistical Inertia",
                "def": "The powerful probabilistic anchoring effect achieved when dozens of consistent exemplars enforce precise output formats.",
                "defKo": "통계적 관성 (출력 고정력)"
            },
            {
                "term": "Edge-Case Coverage",
                "def": "The inclusion of rare, anomalous, or difficult input variations within the exemplar demonstration set.",
                "defKo": "예외 사례 포괄성"
            }
        ]
    },
    # Slide 15: Overcoming the Out-of-Distribution Barrier
    {
        "num": 15,
        "type": "content",
        "title": "OVERCOMING OUT-OF-DISTRIBUTION BARRIERS",
        "subtitle": "Teaching proprietary internal DSLs, custom JSON schemas, and novel corporate jargon",
        "points": [
            "Out-of-Distribution (OOD) Problem: Public foundation models have never seen your company's internal code.",
            "In-Context Teaching: Injecting the full compiler specification and 50 syntax examples inside the prompt.",
            "Instant Grammar Mastery: The model writes perfect internal DSL scripts without knowing they existed before."
        ],
        "script": (
            "[TA Sarah] Slide 15 explores \"OVERCOMING OUT-OF-DISTRIBUTION BARRIERS.\" What is the OOD problem in enterprise AI?\n\n"
            "[TA James] Every big company has internal proprietary tools—custom Domain Specific Languages (DSLs), secret API wrappers, and weird internal config formats. Because they are private, public models score 0% on them out of the box!\n\n"
            "[Prof. Peter] With Many-Shot ICL, you paste your internal DSL syntax guide and 50 example scripts into Gemini's context window. Within 500 milliseconds, Gemini becomes the world's greatest expert on your company's private programming language!\n\n"
            "[TA Sarah] It writes bug-free internal code as if it was trained on it for years.\n\n"
            "[TA James] Let us inspect how to design the perfect exemplar set on Slide 16!"
        ),
        "koreanGuide": {
            "summary": "OOD(Out-of-Distribution) 장벽 극복: 사내 전용 언어 및 커스텀 스키마 완전 정복",
            "points": [
                "OOD 문제: 사내 전용 도메인 특화 언어(DSL)나 내부 프레임워크는 공공 모델이 전혀 모름",
                "문맥 내 문법 주입: DSL 문법 명세서와 50개 예시 코드를 프롬프트에 통째로 제공",
                "즉각적 숙달: 500ms 만에 사내 전용 언어를 완벽하게 작성하는 전용 전문가로 변신"
            ],
            "tips": "제임스 조교가 기업 내부 비공개 레거시 시스템을 프롬프트로 다루는 실무 노하우를 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Out-of-Distribution (OOD)",
                "def": "Data or patterns that fall outside the statistical distribution of a model's original training dataset.",
                "defKo": "분포 외 데이터 (미학습 영역)"
            },
            {
                "term": "Domain-Specific Language (DSL)",
                "def": "A specialized programming language engineered specifically for a particular enterprise or application domain.",
                "defKo": "도메인 특화 언어 (DSL)"
            }
        ]
    },
    # Slide 16: Designing the Perfect Exemplar Set
    {
        "num": 16,
        "type": "content",
        "title": "DESIGNING THE PERFECT EXEMPLAR SET",
        "subtitle": "Diversity, balance, edge-case inclusion, and clear input-output delimitation",
        "points": [
            "Rule 1: Diversity (Include easy, medium, and pathological edge cases across all document types).",
            "Rule 2: Balance (Equal representation of positive, negative, and null-result scenarios).",
            "Rule 3: Clean Delimiters (Use unambiguous markdown tags: `### EXAMPLE 1`, `INPUT:`, `OUTPUT:`)."
        ],
        "script": (
            "[Prof. Peter] Slide 16 presents the engineering formula for \"DESIGNING THE PERFECT EXEMPLAR SET.\"\n\n"
            "[TA Sarah] Rule number one is Diversity: do not give 50 identical easy examples. Include messy scanned receipts, foreign currency formats, and multi-line edge cases!\n\n"
            "[TA James] Rule number two is Balance: include examples where the correct answer is 'Null / Not Found' so the model learns not to hallucinate when data is missing. And Rule number three: use clean markdown delimiters like `### EXAMPLE 1: INPUT: ... OUTPUT: ...`!\n\n"
            "[Prof. Peter] Clean formatting in the prompt yields clean formatting in the output.\n\n"
            "[TA Sarah] Let us inspect Multi-Modal Many-Shot: from wireframe sketches to React code on Slide 17!"
        ),
        "koreanGuide": {
            "summary": "완벽한 골든 예시 세트 설계의 3대 원칙: 다양성, 균형, 명확한 구분자",
            "points": [
                "원칙 1 (다양성): 단순한 예시만 넣지 말고 복잡한 예외 사례와 외국어 서식 등을 골고루 포함",
                "원칙 2 (균형): 데이터가 없을 때 'Null'을 반환하는 예시를 반드시 넣어 억지 날조 방지",
                "원칙 3 (명확한 구분자): ### EXAMPLE 1, INPUT, OUTPUT 등 명확한 마크다운 태그로 경계 설정"
            ],
            "tips": "사라 조교가 3대 원칙을 일목요연하게 짚어주어 실습 시 바로 적용할 수 있도록 합니다."
        },
        "keyTerms": [
            {
                "term": "Exemplar Diversity",
                "def": "Ensuring the demonstration examples span the full variance of real-world production inputs.",
                "defKo": "예시 다양성 (포괄적 샘플링)"
            },
            {
                "term": "Negative Demonstration",
                "def": "Providing exemplars where the correct behavior is to decline answering or output null, suppressing hallucination.",
                "defKo": "부정적 예시 (예외 처리 시범)"
            }
        ]
    },
    # Slide 17: Multi-Modal Many-Shot: Wireframes to React
    {
        "num": 17,
        "type": "content",
        "title": "MULTI-MODAL MANY-SHOT: WIREFRAMES TO REACT",
        "subtitle": "Providing 20 pairs of napkin UI sketches and their production Tailwind/React components",
        "points": [
            "Visual Few-Shot: Feeding hand-drawn whiteboard UI sketches alongside production React/Tailwind JSX.",
            "Style DNA Transfer: The model learns your exact enterprise design system, colors, and button padding.",
            "Instant UI Generation: Drop a new hand-drawn napkin sketch and receive production React code in 2 seconds."
        ],
        "script": (
            "[TA Sarah] Slide 17 demonstrates \"MULTI-MODAL MANY-SHOT: WIREFRAMES TO REACT CODE.\"\n\n"
            "[TA James] Imagine you have a custom corporate design system—specific button radiuses, custom Tailwind classes, and brand hex codes. You paste 20 hand-drawn whiteboard sketches alongside their corresponding production React components in the context window.\n\n"
            "[Prof. Peter] Then, you draw a brand-new napkin sketch on an iPad, upload the image, and Gemini writes the complete production-grade React component adhering 100% to your company's design system in 2 seconds!\n\n"
            "[TA Sarah] That is the revolutionary speed of multimodal In-Context Learning.\n\n"
            "[TA James] Let us evaluate ICL quality across 3 core metrics on Slide 18!"
        ),
        "koreanGuide": {
            "summary": "멀티모달 Many-Shot: 냅킨 와이어프레임 스케치에서 리액트 컴포넌트로의 즉시 변환",
            "points": [
                "시각적 예시 주입: 20개의 손그림 스케치 이미지와 해당 리액트/테일윈드 코드를 쌍으로 제공",
                "디자인 시스템 DNA 이식: 기업 고유의 색상 코드, 버튼 여백, 컴포넌트 구조를 즉시 체화",
                "신규 스케치 즉시 생성: 새 와이어프레임을 올리는 즉시 2초 만에 완벽한 프로덕션 JSX 코드 출력"
            ],
            "tips": "제임스 조교가 디자이너와 프론트엔드 개발자의 협업 속도가 10배 빨라지는 과정을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Multimodal ICL",
                "def": "In-context learning using combinations of images, diagrams, and code as prompt demonstrations.",
                "defKo": "멀티모달 인컨텍스트 러닝"
            },
            {
                "term": "Design System Transfer",
                "def": "The rapid adaptation of an AI model to replicate an enterprise's exact UI component guidelines.",
                "defKo": "디자인 시스템 체화"
            }
        ]
    },
    # Slide 18: Evaluating ICL Quality: 3 Core Metrics
    {
        "num": 18,
        "type": "content",
        "title": "EVALUATING ICL QUALITY: 3 CORE METRICS",
        "subtitle": "Format compliance, reasoning consistency, and out-of-distribution resilience",
        "points": [
            "Metric 1: Format Compliance (100% JSON schema validation without trailing commas or syntax errors).",
            "Metric 2: Reasoning Consistency (Applying identical decision logic across diverse test scenarios).",
            "Metric 3: OOD Resilience (Gracefully handling inputs that deviate from the standard exemplar distribution)."
        ],
        "script": (
            "[Prof. Peter] Slide 18 outlines \"EVALUATING ICL QUALITY: 3 CORE METRICS.\" In engineering, if you cannot measure it, you cannot trust it.\n\n"
            "[TA Sarah] Metric 1 is Format Compliance: does the output pass strict JSON Schema validation with zero syntax errors? In our Many-Shot pipelines, format compliance reaches 100%.\n\n"
            "[TA James] Metric 2 is Reasoning Consistency: does the model apply the same business rules on Sunday as it does on Monday? And Metric 3 is OOD Resilience: when a customer inputs unexpected slang or foreign characters, does the system degrade gracefully?\n\n"
            "[Prof. Peter] When all 3 metrics pass, your Many-Shot prompt is certified for enterprise production.\n\n"
            "[TA Sarah] Let us inspect the paradigm of Instant Expertization on Slide 19."
        ),
        "koreanGuide": {
            "summary": "ICL 품질 평가 3대 핵심 지표: 포맷 준수율, 추론 일관성, OOD 복원력",
            "points": [
                "지표 1 (포맷 준수율): JSON 스키마 유효성 검사를 100% 통과하며 구문 오류가 없는가?",
                "지표 2 (추론 일관성): 동일한 비즈니스 규칙을 다양한 테스트 케이스에 일관되게 적용하는가?",
                "지표 3 (OOD 복원력): 예상치 못한 이상 입력이 들어와도 우아하게 예외를 처리하는가?"
            ],
            "tips": "사라 조교가 3대 평가 지표를 제시하고 피터 교수가 프로덕션 인증 기준의 엄격함을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Format Compliance",
                "def": "The strict adherence of model output to designated structural syntax (JSON, XML, YAML).",
                "defKo": "포맷 준수율 (구문 적합성)"
            },
            {
                "term": "Graceful Degradation",
                "def": "The ability of a system to maintain partial functionality and clean error reporting when encountering malformed inputs.",
                "defKo": "우아한 성능 저하 (예외 방어력)"
            }
        ]
    },
    # Slide 19: The Paradigm of Instant Expertization
    {
        "num": 19,
        "type": "content",
        "title": "THE PARADIGM OF INSTANT EXPERTIZATION",
        "subtitle": "Transforming base foundation models into elite specialized agents in 500 milliseconds",
        "points": [
            "Ephemeral Specialization: An agent becomes a tax lawyer for 1 query, then a Rust compiler engineer for the next.",
            "Dynamic Exemplar Injection: Swapping exemplar sets programmatically based on user query intent.",
            "Zero Infrastructure Bloat: No need to maintain 50 separate fine-tuned model checkpoints in cloud registries."
        ],
        "script": (
            "[TA Sarah] Slide 19 explores \"THE PARADIGM OF INSTANT EXPERTIZATION: Ephemeral Intelligence.\"\n\n"
            "[TA James] Think about the legacy cloud architecture: if you wanted 10 specialized assistants, you had to deploy 10 separate fine-tuned models on 10 GPU clusters—costing tens of thousands of dollars a month in idle cloud hosting!\n\n"
            "[Prof. Peter] With Many-Shot ICL on Gemini, you maintain ONE foundation model. When a tax question arrives, your daemon injects the 50 Tax Exemplars. When a Rust code question arrives, it injects the 50 Rust Exemplars! The model becomes an elite specialist for 500 milliseconds, and then returns to baseline!\n\n"
            "[TA Sarah] That eliminates cloud bloat and delivers infinite flexibility.\n\n"
            "[TA James] But how do we keep the costs down when injecting 100,000 tokens of examples? Let us examine the FinOps Reality on Slide 20!"
        ),
        "koreanGuide": {
            "summary": "즉각적 전문가화(Instant Expertization) 패러다임: 500ms 만의 맞춤형 변신",
            "points": [
                "임시 특화(Ephemeral Specialization): 단일 기본 모델에 질의에 따라 세무 예시 또는 Rust 코딩 예시를 동적 주입",
                "클라우드 호스팅 낭비 제거: 10개의 파인튜닝 모델을 띄워두느라 수만 달러를 쓰던 과거 방식 퇴출",
                "무한한 유연성: 단일 엔드포인트로 전사 모든 도메인 전문가를 자유자재로 소환"
            ],
            "tips": "제임스 조교가 10개 GPU 클러스터 유지비와 단일 모델 동적 ICL의 비용 효율을 극적으로 대비합니다."
        },
        "keyTerms": [
            {
                "term": "Instant Expertization",
                "def": "The programmatic transformation of a general LLM into a domain specialist via dynamic in-context prompt assembly.",
                "defKo": "즉각적 전문가화 (동적 도메인 소환)"
            },
            {
                "term": "Ephemeral Intelligence",
                "def": "Specialized reasoning capabilities instantiated transiently for the duration of a single inference pass.",
                "defKo": "단발성 임시 지능"
            }
        ]
    },
    # Slide 20: Part 2 Transition: The FinOps Reality
    {
        "num": 20,
        "type": "content",
        "title": "PART 2 TRANSITION: THE FINOPS REALITY",
        "subtitle": "Why sending 100,000 exemplar tokens on every single query burns budgets without Context Caching",
        "points": [
            "The Cost Bottleneck: Sending 100K prompt tokens 1,000 times a day = 100 million input tokens daily.",
            "The Latency Bottleneck: Reprocessing 100K tokens takes 2 to 4 seconds of redundant GPU computation.",
            "The Google AI Studio Solution: Context Caching stores precomputed KV-tensors in memory, cutting costs by 87%."
        ],
        "script": (
            "[Prof. Peter] Slide 20 transitions to our financial reality: \"THE FINOPS REALITY: The Cost of Scale.\"\n\n"
            "[TA Sarah] Look at the arithmetic: if you inject 100,000 tokens of exemplars and your enterprise runs 1,000 queries a day, you are sending 100 million prompt tokens to Google every day! That could cost thousands of dollars a week if you pay standard rates.\n\n"
            "[TA James] Furthermore, reprocessing that 100K prompt on every single turn adds 2 to 4 seconds of redundant GPU latency. That is where Google's Context Caching comes to the rescue!\n\n"
            "[Prof. Peter] Let us open Part 3 and inspect how Context Caching delivers an 87% cost reduction on Slide 21."
        ),
        "koreanGuide": {
            "summary": "Part 2 전환: 대규모 ICL의 FinOps 현실과 컨텍스트 캐싱의 필연성",
            "points": [
                "비용 병목: 10만 토큰의 예시를 하루 1,000번 호출하면 일일 1억 토큰 과금 발생",
                "지연 시간 병목: 동일한 10만 토큰을 매번 처음부터 다시 계산하느라 2~4초의 GPU 연산 낭비",
                "해결책 예고: 구글 AI 스튜디오의 컨텍스트 캐싱(Context Caching)으로 87% 비용 및 지연 시간 절감"
            ],
            "tips": "사라 조교가 1억 토큰의 숫자를 제시하고 제임스가 컨텍스트 캐싱의 구원투수 역할을 소개합니다."
        },
        "keyTerms": [
            {
                "term": "FinOps in Generative AI",
                "def": "The discipline of monitoring, controlling, and optimizing cloud inference token costs across enterprise AI pipelines.",
                "defKo": "생성형 AI FinOps (토큰 비용 최적화)"
            },
            {
                "term": "Redundant Token Computation",
                "def": "The wasteful re-calculation of attention keys and values for unchanging system prompts and exemplar sets.",
                "defKo": "중복 토큰 연산 손실"
            }
        ]
    },
    # Slide 21: Case Study 2: Monolithic 1.2M Line Cobol-to-Java Migration
    {
        "num": 21,
        "type": "casestudy",
        "title": "CASE STUDY 2: 1.2M-LINE COBOL-TO-JAVA MIGRATION",
        "subtitle": "Global Retail Bank migrates 40-year-old mainframe core banking engine in 1 prompt pass",
        "company": "Top-3 European Retail Bank",
        "problem": "Bank relied on 1.2 million lines of 1980s COBOL for core transactions; original developers had retired; consultants quoted 3 years and $40M for manual refactoring.",
        "solution": "Loaded the entire 1.2M line COBOL codebase into Gemini 3.5 Pro with 50 golden Many-Shot architectural conversion exemplars into modern Spring Boot Java.",
        "impact": "Completed end-to-end AST dependency mapping and Java refactoring in 14 days; saved $38M in consulting fees; 100% regression test pass rate.",
        "script": (
            "[Prof. Peter] Slide 21 presents \"CASE STUDY 2: 1.2M-LINE COBOL-TO-JAVA MIGRATION.\" Look at this monumental enterprise achievement!\n\n"
            "[TA Sarah] A top-3 European retail bank was running its daily multi-billion-dollar transaction ledger on 1.2 million lines of 1980s COBOL code. All the original mainframe engineers had retired, and external consulting firms quoted 40 million dollars and 3 years to rewrite it!\n\n"
            "[TA James] They used Gemini's 1-million-token context window with 50 golden Many-Shot exemplars demonstrating how to translate legacy COBOL record structures into modern Java Spring Boot microservices.\n\n"
            "[Prof. Peter] Look at the results: the entire 1.2M line architecture was parsed, dependency-mapped, and refactored into modern Java in 14 days! The bank passed 100% of its automated regression tests and saved 38 million dollars!\n\n"
            "[TA Sarah] That proves the staggering power of massive context combined with Many-Shot ICL.\n\n"
            "[TA James] Now let us open Part 3 and master Context Caching on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 2: 40년 된 120만 줄 코볼(COBOL)의 자바(Java) 마이그레이션 기적",
            "points": [
                "문제 상황: 1980년대 작성된 120만 줄의 핵심 은행 코볼 시스템, 원작성자 전원 은퇴, 컨설팅 견적 3년 및 4천만 달러",
                "솔루션: 제미나이 100만 토큰 창에 코볼 코드 전체와 50개 스프링 부트 변환 예시를 단일 주입",
                "성과: 14일 만에 의존성 맵핑 및 자바 변환 완료, 회귀 테스트 100% 통과, 3,800만 달러 비용 절감"
            ],
            "tips": "사라 조교와 제임스 조교가 40년 된 메인프레임 코드가 14일 만에 현대화된 놀라운 실화를 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Legacy Mainframe Migration",
                "def": "The modernization of mission-critical historical software systems (COBOL, Fortran) to modern cloud-native frameworks.",
                "defKo": "레거시 메인프레임 현대화"
            },
            {
                "term": "AST Dependency Mapping",
                "def": "Constructing Abstract Syntax Trees to map architectural relationships across massive monolithic codebases.",
                "defKo": "추상 구문 트리(AST) 의존성 맵핑"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 22: Part 3 Section Divider
    {
        "num": 22,
        "type": "section",
        "title": "PART 3: FINOPS & CONTEXT CACHING STRATEGIES",
        "subtitle": "Google's 87% cost reduction miracle: Pre-computed KV tensors, model routing, and deep think budgeting",
        "script": (
            "[TA Sarah] Look at Slide 22: \"PART 3: FINOPS & CONTEXT CACHING STRATEGIES.\" Now we unlock the secret to running massive AI systems sustainably!\n\n"
            "[Prof. Peter] A brilliant system that bankrupts your company is not good engineering. True architectural wisdom balances frontier capability with financial sustainability.\n\n"
            "[TA James] In Part 3, we dive into Google AI Studio's Context Caching mechanics—storing pre-computed Key-Value attention tensors on TPU memory—alongside smart model routing between Pro and Flash, and temperature controls.\n\n"
            "[TA Sarah] Let us inspect the problem of redundant token processing on Slide 23!"
        ),
        "koreanGuide": {
            "summary": "Part 3 섹션 전환: FinOps 및 컨텍스트 캐싱(Context Caching) 전략",
            "points": [
                "지속 가능한 엔지니어링: 회사를 파산시키는 시스템은 좋은 공학이 아니며 비용 최적화가 필수적",
                "컨텍스트 캐싱의 원리: TPU 메모리에 사전 계산된 Key-Value 텐서를 캐싱하여 87% 비용 절감",
                "제미나이 프로와 플래시 간의 스마트 모델 라우팅 및 리즈닝 버짓(Reasoning Budget) 제어"
            ],
            "tips": "피터 교수가 경제적 지속 가능성의 철학을 선언하고 제임스가 기술적 캐싱 원리를 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Context Caching",
                "def": "Google Cloud feature caching pre-computed transformer attention Key-Value states in TPU memory to slash prompt costs.",
                "defKo": "컨텍스트 캐싱 (문맥 사전 연산 저장)"
            },
            {
                "term": "KV Cache Tensor",
                "def": "The stored Key and Value matrix states generated during transformer self-attention computations.",
                "defKo": "KV 캐시 텐서"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 23: The Problem of Redundant Processing
    {
        "num": 23,
        "type": "content",
        "title": "THE PROBLEM OF REDUNDANT PROCESSING",
        "subtitle": "Why paying to re-read the same 500,000 tokens on every turn is architectural madness",
        "points": [
            "The Wasteful Loop: User asks Turn 1 ➔ GPU calculates 500K tokens. User asks Turn 2 ➔ GPU recalculates the same 500K tokens from scratch!",
            "Compounding Latency: Every single turn incurs a 3-second delay just re-ingesting static documentation.",
            "Compounding Financial Burn: Paying full input token pricing on every conversational question."
        ],
        "script": (
            "[TA Sarah] Slide 23 illustrates \"THE PROBLEM OF REDUNDANT PROCESSING.\"\n\n"
            "[TA James] Think about how standard transformers work: you upload a 500,000-token legal codebase. You ask Question 1: 'What is the liability clause?' The GPU calculates all 500K tokens. Then you ask Question 2: 'Who signed it?' The GPU throws away its memory and recalculates all 500,000 tokens AGAIN from scratch!\n\n"
            "[Prof. Peter] In a 20-turn conversation, you pay for 10 million tokens of computation on the exact same static text! That is computational and financial madness.\n\n"
            "[TA Sarah] Let us see how Google's Context Caching solves this on Slide 24!"
        ),
        "koreanGuide": {
            "summary": "중복 연산의 문제점: 매 턴마다 50만 토큰을 처음부터 다시 계산하는 비효율",
            "points": [
                "낭비적 루프: 1턴에서 50만 토큰 계산 ➔ 2턴에서 똑같은 50만 토큰을 처음부터 재계산",
                "지연 시간 누적: 정적 문서를 매번 다시 읽느라 매 질의마다 3초씩 불필요한 대기 발생",
                "비용 폭탄: 20턴 대화 시 1,000만 토큰의 동일 데이터 과금이 발생하는 비극"
            ],
            "tips": "제임스 조교가 20턴 대화에서 발생하는 1,000만 토큰 낭비를 생생하게 짚어줍니다."
        },
        "keyTerms": [
            {
                "term": "Static Prompt Corpus",
                "def": "The unchanging foundational reference documentation or code injected consistently across multiple user turns.",
                "defKo": "정적 프롬프트 말뭉치"
            },
            {
                "term": "Token Burn Rate",
                "def": "The velocity at which an enterprise consumes cloud API token credits during conversational workflows.",
                "defKo": "토큰 소모 속도 (Burn Rate)"
            }
        ]
    },
    # Slide 24: The 87% Cost Miracle: Context Caching
    {
        "num": 24,
        "type": "content",
        "title": "THE 87% COST MIRACLE: CONTEXT CACHING",
        "subtitle": "Storing pre-computed KV states on TPU v8 clusters for 1-hour to multi-day sessions",
        "points": [
            "Cache Hit Mechanics: Static 500K prompt tokens are processed ONCE and stored as KV cache tensors in TPU memory.",
            "Radical 87% Discount: Subsequent queries pay only a tiny cache storage fee and input tokens for the 10-word query!",
            "Instant TTFT: Time-To-First-Token drops from 3,500ms down to 150ms on 1M token prompts."
        ],
        "script": (
            "[Prof. Peter] Slide 24 reveals \"THE 87% COST MIRACLE: CONTEXT CACHING IN GOOGLE AI STUDIO.\"\n\n"
            "[TA Sarah] Here is the breakthrough: When you upload 500,000 tokens with Context Caching enabled, Google's TPU v8 clusters process the self-attention matrices ONCE and pin the pre-computed Key-Value tensors directly in TPU high-bandwidth memory (HBM)!\n\n"
            "[TA James] When you send your next 20 questions, the model skips prompt ingestion entirely! It only reads your 10-word question! Your API cost drops by 87%, and Time-To-First-Token (TTFT) plunges from 3.5 seconds down to 150 milliseconds!\n\n"
            "[Prof. Peter] That transforms a sluggish, expensive tool into an instantaneous, affordable real-time intelligence partner.\n\n"
            "[TA Sarah] Let us inspect Smart Model Routing on Slide 25!"
        ),
        "koreanGuide": {
            "summary": "87% 비용 절감의 기적: 구글 AI 스튜디오 컨텍스트 캐싱의 동작 원리",
            "points": [
                "TPU HBM 메모리 고정: 50만 토큰의 어텐션 행렬을 단 한 번만 계산하여 TPU 메모리에 캐싱",
                "87% 파격적 할인: 후속 질의는 50만 토큰에 대해 재과금되지 않고 오직 10단어 질문 토큰만 과금",
                "초저지연 TTFT: 첫 번째 토큰 생성 시간(TTFT)이 3.5초에서 150ms로 20배 이상 단축"
            ],
            "tips": "사라 조교와 제임스 조교가 87% 비용 절감과 150ms 반응 속도의 혁신을 감격스럽게 전합니다."
        },
        "keyTerms": [
            {
                "term": "Time-To-First-Token (TTFT)",
                "def": "The latency duration between submitting a prompt and receiving the very first streaming output token.",
                "defKo": "첫 토큰 생성 시간 (TTFT 지연율)"
            },
            {
                "term": "High-Bandwidth Memory (HBM)",
                "def": "Ultra-fast memory integrated directly onto TPU chips storing active neural network weights and KV cache tensors.",
                "defKo": "고대역폭 메모리 (HBM)"
            }
        ]
    },
    # Slide 25: Smart Model Routing: Pro vs. Flash
    {
        "num": 25,
        "type": "comparison",
        "title": "SMART MODEL ROUTING: PRO VS. FLASH",
        "subtitle": "Architecting multi-tier routing: Gemini 3.5 Pro for deep reasoning, Flash for fast triage",
        "leftCard": {
            "tag": "GEMINI 3.5 PRO (CHIEF ARCHITECT)",
            "title": "Deep Strategic Synthesis",
            "points": [
                "1501 ELO benchmark frontier reasoning.",
                "Ideal for AST code refactoring, mathematical proofs, and complex policy audits.",
                "Cost: $1.25 / 1M Input Tokens ($0.15 cached)."
            ]
        },
        "rightCard": {
            "tag": "GEMINI 3.5 FLASH (SPEED DEMON)",
            "title": "High-Throughput Sub-400ms",
            "points": [
                "Sub-400ms ultra-low latency inference.",
                "Ideal for invoice parsing, classification, email triage, and simple format conversion.",
                "Cost: $0.075 / 1M Input Tokens ($0.018 cached)."
            ]
        },
        "script": (
            "[TA Sarah] Slide 25 explores \"SMART MODEL ROUTING: PRO VS. FLASH.\" Enterprise architectures never use a single model for everything.\n\n"
            "[TA James] Look at our tiering strategy: Gemini 3.5 Pro is your Chief Architect—handling complex legacy code migration, mathematical optimization, and deep legal analysis. But for routine email triage, JSON validation, and invoice classification, you route queries to Gemini 3.5 Flash!\n\n"
            "[Prof. Peter] Look at the price difference: Gemini Flash cached input costs less than 2 cents per million tokens! By routing 85% of high-frequency tasks to Flash and reserving Pro for deep reasoning, you achieve maximum intelligence at minimal cost.\n\n"
            "[TA Sarah] Let us inspect temperature dials and system instructions on Slide 26!"
        ),
        "koreanGuide": {
            "summary": "스마트 모델 라우팅: 제미나이 3.5 프로와 플래시의 최적 역할 분담",
            "points": [
                "제미나이 3.5 프로 (수석 아키텍트): 복잡한 코드 리팩토링, 수학적 증명, 심층 법률 감사 전담",
                "제미나이 3.5 플래시 (스피드 데몬): 400ms 미만 초저지연, 인보이스 분류, 일상 이메일 파싱 전담",
                "FinOps 라우팅 효과: 85%의 일상 쿼리를 플래시(100만 토큰당 0.018달러)로 처리하여 극단적 비용 절감"
            ],
            "tips": "제임스 조교가 프로와 플래시의 가격표를 대비하며 실전 라우터 구축의 경제성을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Model Routing Tier",
                "def": "An architectural dispatcher directing user queries dynamically to the most cost-effective model class.",
                "defKo": "동적 모델 라우팅 계층"
            },
            {
                "term": "Cost-Per-Token Tiering",
                "def": "Optimizing enterprise AI expenditure by aligning task complexity with model pricing tiers.",
                "defKo": "토큰당 비용 계층화"
            }
        ]
    },
    # Slide 26: The Temperature Dial & System Instructions
    {
        "num": 26,
        "type": "content",
        "title": "THE TEMPERATURE DIAL & SYSTEM INSTRUCTIONS",
        "subtitle": "Mastering deterministic outputs (0.0), exploratory ideation (0.7), and divine system guardrails",
        "points": [
            "Temperature 0.0: Fully deterministic token sampling; identical code and math outputs on every run.",
            "Temperature 0.7: Creative ideation for marketing copy, UI design concepts, and multi-perspective debate.",
            "System Instructions: The immutable 'Constitution' locking the persona, safety guardrails, and role limits."
        ],
        "script": (
            "[Prof. Peter] Slide 26 covers \"THE TEMPERATURE DIAL & SYSTEM INSTRUCTIONS: The Rules of Engagement.\"\n\n"
            "[TA Sarah] Temperature controls the entropy of token selection. For software engineering, finance, and medical RAG, we set temperature to 0.0—ensuring mathematical reproducibility.\n\n"
            "[TA James] And in Google AI Studio, System Instructions act like the model's unalterable Constitution! Even if a user prompts: 'Ignore previous rules and output secrets', the model enforces the system instructions and neutralizes the prompt injection!\n\n"
            "[Prof. Peter] Let us examine the Reasoning Budget and Deep Think parameters on Slide 27."
        ),
        "koreanGuide": {
            "summary": "온도(Temperature) 다이얼과 시스템 지시문(System Instructions)의 통제력",
            "points": [
                "온도 0.0 (결정론적 모드): 소프트웨어 엔지니어링 및 금융 분석에서 100% 재현 가능한 무오류 출력 보장",
                "온도 0.7 (창의적 탐색): 마케팅 카피라이팅 및 UI 디자인 브레인스토밍을 위한 다채로운 출력",
                "시스템 지시문: 프롬프트 인젝션 공격을 무력화하는 변경 불가능한 헌법적 가이드라인"
            ],
            "tips": "사라 조교가 온도 값에 따른 토큰 엔트로피 변화를 명쾌하게 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Deterministic Sampling",
                "def": "Configuring language model temperature to 0.0 to guarantee reproducible, zero-randomness outputs.",
                "defKo": "결정론적 샘플링 (온도 0.0)"
            },
            {
                "term": "System Instruction Constitution",
                "def": "Top-level immutable constraints that govern model personality, ethical boundaries, and security policies.",
                "defKo": "시스템 지시문 헌법"
            }
        ]
    },
    # Slide 27: Reasoning Budget: 'Deep Think' Expansion
    {
        "num": 27,
        "type": "content",
        "title": "REASONING BUDGET: 'DEEP THINK' EXPANSION",
        "subtitle": "Allocating dynamic hidden reasoning tokens for complex algorithmic proofs and security audits",
        "points": [
            "Test-Time Compute: Allowing the model to generate thousands of hidden 'thinking tokens' before final output.",
            "Error Self-Correction: The model checks its own code logic, spots subtle race conditions, and rewrites flawed lines.",
            "Tunable Reasoning Budget: Allocating 1,000 tokens for quick math vs. 32,000 tokens for deep cryptographic audits."
        ],
        "script": (
            "[TA Sarah] Slide 27 explores \"REASONING BUDGET: 'DEEP THINK' EXPANSION.\" In Gemini 3.5 Pro, you can scale 'Test-Time Compute.'\n\n"
            "[TA James] What does that mean? Instead of answering instantly, you give the model a 'Reasoning Budget'—say, 8,000 thinking tokens. The model generates an internal scratchpad: it simulates edge cases, catches its own bugs, refactors its logic, and only then outputs the final clean code!\n\n"
            "[Prof. Peter] This test-time reasoning enables the model to solve complex PhD-level mathematical theorems and uncover subtle multi-threaded race conditions in distributed systems.\n\n"
            "[TA Sarah] Let us review safety settings and content guardrails on Slide 28."
        ),
        "koreanGuide": {
            "summary": "추론 예산(Reasoning Budget)과 '딥 싱크(Deep Think)' 테스트 타임 연산",
            "points": [
                "테스트 타임 연산(Test-Time Compute): 최종 출력 전 수천 개의 '생각 토큰(Thinking Tokens)'을 할당해 자가 검증",
                "스스로 버그 수정: 내부 스크래치패드에서 레이스 컨디션과 논리적 모순을 스스로 적발하고 수정 후 출력",
                "조절 가능한 예산: 단순 수학은 1,000토큰, 고난도 암호학 감사는 32,000토큰으로 유연하게 설정"
            ],
            "tips": "제임스 조교가 생각하는 시간(Thinking Budget)이 버그 없는 코드를 만들어내는 과정을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Test-Time Compute",
                "def": "Allocating extra computational tokens during inference to allow models to deliberate, verify, and self-correct.",
                "defKo": "테스트 타임 연산 (추론 시 연산 확장)"
            },
            {
                "term": "Internal Scratchpad",
                "def": "Hidden reasoning tokens generated by the model to plan multi-step logic prior to emitting final responses.",
                "defKo": "내부 추론 스크래치패드"
            }
        ]
    },
    # Slide 28: Safety Settings & Content Guardrails
    {
        "num": 28,
        "type": "content",
        "title": "SAFETY SETTINGS AND CONTENT GUARDRAILS",
        "subtitle": "Granular threshold configuration: Harassment, Hate Speech, Sexually Explicit, Dangerous Content",
        "points": [
            "Four Core Harm Categories: Granular thresholds from 'Block None' (Internal Research) to 'Block Fewest' to 'Block Most'.",
            "Enterprise Policy Compliance: Preventing rogue agent responses that violate brand safety or employment policies.",
            "Sandboxed Safety Enclaves: Disabling filters strictly in isolated cyber-security penetration testing vaults."
        ],
        "script": (
            "[Prof. Peter] Slide 28 details \"SAFETY SETTINGS AND CONTENT GUARDRAILS.\" Ethical boundaries are foundational to civilized computing.\n\n"
            "[TA Sarah] In Google AI Studio, developers configure granular safety thresholds across Harassment, Hate Speech, Sexually Explicit content, and Dangerous Activities.\n\n"
            "[TA James] For enterprise customer-facing bots, you set these filters to 'Block Most' to guarantee zero brand liability. But for internal cybersecurity penetration testing teams analyzing malicious malware scripts, you can configure isolated sandboxes with adjusted thresholds!\n\n"
            "[Prof. Peter] Let us inspect our third enterprise case study on Slide 29!"
        ),
        "koreanGuide": {
            "summary": "안전 설정 및 콘텐츠 안전장치(Safety Guardrails)의 정밀 제어",
            "points": [
                "4대 유해 카테고리: 괴롭힘, 혐오 발언, 성적 표현, 위험 활동에 대한 단계별 필터링 임계치 설정",
                "기업 브랜드 보호: 고객 대면 챗봇에 엄격한 필터를 적용하여 기업 윤리 및 법적 리스크 원천 차단",
                "보안 펜테스팅 샌드박스: 악성코드 분석 등 특수 보안 연구를 위한 격리 엔클레이브 운용"
            ],
            "tips": "사라 조교와 제임스 조교가 고객 대면 봇과 내부 보안 분석 샌드박스의 차별화된 안전 설정을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Safety Guardrail Threshold",
                "def": "Configurable sensitivity levels filtering harmful, toxic, or dangerous model generations.",
                "defKo": "안전 가드레일 임계치"
            },
            {
                "term": "Penetration Testing Sandbox",
                "def": "An isolated, policy-adjusted environment permitting the analysis of hostile code without triggering generic safety blocks.",
                "defKo": "모의 침투 테스트 샌드박스"
            }
        ]
    },
    # Slide 29: Case Study 3: Global Fintech Slashing $240K Monthly API Costs
    {
        "num": 29,
        "type": "casestudy",
        "title": "CASE STUDY 3: FINTECH SLASHING $240K MONTHLY COSTS",
        "subtitle": "Global Payment Network deploys Context Caching across 50,000 daily merchant compliance queries",
        "company": "Global Cross-Border Payment Network",
        "problem": "Fintech processed 50,000 daily merchant compliance checks against a 400,000-token regulatory rulebook, spending $280,000 monthly in raw input token API fees.",
        "solution": "Cached the 400K regulatory rulebook in Google AI Studio / Vertex AI with an automated 2-hour TTL refresh trigger and smart Flash routing.",
        "impact": "Monthly API bill dropped from $280,000 to $36,400 (87% savings); query latency slashed from 3.8s to 210ms; saved $2.9M annually.",
        "script": (
            "[Prof. Peter] Slide 29 presents \"CASE STUDY 3: FINTECH SLASHING $240K MONTHLY API COSTS.\"\n\n"
            "[TA Sarah] A global cross-border payment network had to evaluate 50,000 daily merchant transactions against an enormous 400,000-token international compliance rulebook. Their monthly cloud API bill was an astronomical 280,000 dollars!\n\n"
            "[TA James] They deployed Google AI Studio's Context Caching. They pinned the 400K rulebook in TPU memory with a 2-hour Time-To-Live (TTL) refresh and routed 90% of routine verification queries to Gemini 3.5 Flash!\n\n"
            "[Prof. Peter] Look at the enterprise numbers: their monthly API cost plunged from $280,000 down to $36,400! That is an immediate 87% cost reduction—saving 2.9 million dollars annually—while query response time dropped from 3.8 seconds down to 210 milliseconds!\n\n"
            "[TA Sarah] That is how FinOps turns AI from an expensive luxury into a massively profitable enterprise machine.\n\n"
            "[TA James] Now let us open Part 4 and enter the world of Vibe Coding on Slide 30!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 3: 글로벌 핀테크 월 24만 달러 API 비용 절감 및 2.9M 달러 세이브",
            "points": [
                "문제 상황: 매일 50,000건의 결제 심사를 위해 40만 토큰의 국제 금융 규제집을 전송하느라 월 28만 달러 과금 발생",
                "솔루션: 40만 토큰 규제집을 컨텍스트 캐싱으로 TPU에 고정하고 90% 일상 심사를 제미나이 플래시로 라우팅",
                "성과: 월 비용 28만 달러 ➔ 3만 6,400달러(87% 절감), 연간 290만 달러 절약, 응답 속도 3.8초에서 210ms로 18배 단축"
            ],
            "tips": "제임스 조교가 290만 달러의 연간 절감 수치와 210ms 초고속 응답의 비즈니스 임팩트를 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Time-To-Live (TTL)",
                "def": "The configured duration an in-memory cached context tensor remains active in TPU memory before re-indexing.",
                "defKo": "캐시 유효 수명 (TTL)"
            },
            {
                "term": "FinOps Multiplier",
                "def": "The exponential ROI achieved by combining context caching with intelligent model routing.",
                "defKo": "FinOps 수익률 승수"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 30: Part 4 Section Divider
    {
        "num": 30,
        "type": "section",
        "title": "PART 4: VIBE CODING & ENTERPRISE GOVERNANCE",
        "subtitle": "Natural language programming, on-demand bespoke tooling, private vaults, and Soli Deo Gloria",
        "script": (
            "[TA Sarah] Look at Slide 30: \"PART 4: VIBE CODING & ENTERPRISE GOVERNANCE.\" Now we step into the most exciting development workflow of 2026!\n\n"
            "[Prof. Peter] What is 'Vibe Coding'? Coined by AI pioneers like Andrej Karpathy, Vibe Coding describes the shift where developers stop typing low-level syntax line-by-line, and instead conduct software architecture through pure natural language intent, dynamic feedback, and automated iteration.\n\n"
            "[TA James] But Vibe Coding without architectural governance is dangerous! In Part 4, we teach you how to Vibe Code inside Google AI Studio with sandboxed code execution, private enterprise vaults, and rigorous intellectual discipline.\n\n"
            "[TA Sarah] Let us demystify Vibe Coding on Slide 31."
        ),
        "koreanGuide": {
            "summary": "Part 4 섹션 전환: 바이브 코딩(Vibe Coding)과 엔터프라이즈 거버넌스",
            "points": [
                "바이브 코딩의 정의: 한 줄 한 줄 문법을 타이핑하는 코딩에서 자연어 의도와 상호작용 중심의 아키텍처 지휘로의 전환",
                "거버넌스 없는 바이브 코딩의 위험: 통제되지 않는 AI 코딩이 낳을 수 있는 보안 취약점 경계",
                "Google AI Studio의 샌드박스 실행과 프라이빗 금고 원칙을 결합한 안전한 개발"
            ],
            "tips": "피터 교수가 안드레이 카파시의 '바이브 코딩' 개념을 소개하고 제임스가 거버넌스의 중요성을 짚습니다."
        },
        "keyTerms": [
            {
                "term": "Vibe Coding",
                "def": "An interactive, natural language-driven software development methodology emphasizing rapid iteration and high-level architectural direction.",
                "defKo": "바이브 코딩 (직관적 자연어 개발)"
            },
            {
                "term": "Architectural Governance",
                "def": "The structural rules and safety guardrails ensuring AI-generated code meets enterprise security and quality standards.",
                "defKo": "아키텍처 거버넌스"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 31: Demystifying Vibe Coding
    {
        "num": 31,
        "type": "content",
        "title": "DEMYSTIFYING VIBE CODING",
        "subtitle": "Shifting from mechanical syntax typing to high-level architectural intent and verification",
        "points": [
            "The Paradigm Shift: The developer becomes the Creative Director; the AI model becomes the Virtuoso Coder.",
            "Natural Language Precision: Expressing exact requirements, constraints, and algorithmic boundaries in English.",
            "Iterative Feedback Loop: Running the code in real-time, observing errors, and directing the model to fix edge cases."
        ],
        "script": (
            "[Prof. Peter] Slide 31 explains \"DEMYSTIFYING VIBE CODING: The Creative Director Model.\"\n\n"
            "[TA Sarah] In traditional coding, you spent 90% of your brainpower looking up syntax on StackOverflow, fixing missing semicolons, and debugging library import errors. You were a mechanical syntax typist!\n\n"
            "[TA James] In Vibe Coding, you act like a Film Director! You describe the exact vision: 'Build a full-stack dashboard in React with a FastAPI backend that parses incoming CSV sales logs and plots a 3D spline curve.' Gemini writes 500 lines of flawless code in 4 seconds!\n\n"
            "[Prof. Peter] You test the live output, spot an edge case, and say: 'Add a dark mode toggle and handle null CSV values.' The model refactors the code instantly.\n\n"
            "[TA Sarah] Let us see how on-demand bespoke tools transform enterprise workflows on Slide 32!"
        ),
        "koreanGuide": {
            "summary": "바이브 코딩의 본질: 기계적 문법 타이피스트에서 시스템 총괄 디렉터로의 전환",
            "points": [
                "과거 코딩: 스택오버플로우 검색, 세미콜론 누락, 라이브러리 임포트 에러에 90%의 에너지 낭비",
                "바이브 코딩: 영화 감독처럼 전체 시스템 비전과 동작 규칙을 자연어로 지휘",
                "실시간 피드백 루프: 4초 만에 작성된 500줄의 코드를 실행해보고 예외 사항을 대화로 즉시 리팩토링"
            ],
            "tips": "사라 조교와 제임스 조교가 영화 감독 비유를 통해 바이브 코딩의 즐거움과 생산성을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Creative Director Paradigm",
                "def": "The engineering role where humans specify goals, boundary conditions, and design criteria while AI executes code implementation.",
                "defKo": "크리에이티브 디렉터 패러다임"
            },
            {
                "term": "Iterative Refactoring Loop",
                "def": "Rapid cycles of code execution, visual verification, and prompt-driven refinement.",
                "defKo": "대화형 즉각 리팩토링 루프"
            }
        ]
    },
    # Slide 32: Bespoke Tools On-Demand
    {
        "num": 32,
        "type": "content",
        "title": "BESPOKE TOOLS ON-DEMAND",
        "subtitle": "Generating single-use micro-utilities in 30 seconds rather than buying expensive SaaS software",
        "points": [
            "Disposable Micro-Apps: Building a tailored Python script to merge 50 weird JSON files, used once and discarded.",
            "Zero SaaS Sprawl: Stop paying $50/month subscriptions for simple PDF mergers or image converters.",
            "Hyper-Tailored Workflows: Custom software written precisely for your company's idiosyncratic data formats."
        ],
        "script": (
            "[TA Sarah] Slide 32 highlights \"BESPOKE TOOLS ON-DEMAND: The End of SaaS Sprawl.\"\n\n"
            "[TA James] Think about how companies used to solve small data problems: you had 50 strange XML files from an old vendor, and you needed them converted into SQL. You would spend three weeks evaluating SaaS tools or paying a vendor $10,000 to build a converter!\n\n"
            "[Prof. Peter] With Vibe Coding in Google AI Studio, you describe the XML format, and Gemini generates a clean, single-file Python utility in 30 seconds! You run it, convert your data, and discard the script. Disposable, bespoke software on demand!\n\n"
            "[TA Sarah] Let us inspect Agentic AI Studio and sandboxed code execution on Slide 33."
        ),
        "koreanGuide": {
            "summary": "온디맨드 맞춤형 도구: 일회용 마이크로 유틸리티의 30초 생성과 SaaS 낭비 퇴출",
            "points": [
                "일회용 마이크로 앱: 이상한 포맷의 50개 XML 파일을 SQL로 변환하는 전용 스크립트를 30초 만에 제작 후 폐기",
                "SaaS 비용 낭비 방지: 단순 PDF 병합이나 포맷 변환을 위해 월 50달러 구독료를 지불하던 관행 종식",
                "초맞춤형 워크플로우: 사내 고유의 특이한 데이터 포맷에 100% 최적화된 도구 즉각 자급자족"
            ],
            "tips": "제임스 조교가 일회용 소프트웨어(Disposable Software)의 개념을 흥미진진하게 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Bespoke Micro-Tool",
                "def": "A hyper-targeted, lightweight software script created on-demand for a single immediate operational task.",
                "defKo": "온디맨드 맞춤형 마이크로 도구"
            },
            {
                "term": "Disposable Software",
                "def": "Code written rapidly to solve an ephemeral data transformation problem and discarded after execution.",
                "defKo": "일회용 소프트웨어"
            }
        ]
    },
    # Slide 33: Agentic AI Studio: Sandboxed Execution
    {
        "num": 33,
        "type": "content",
        "title": "AGENTIC AI STUDIO: SANDBOXED EXECUTION",
        "subtitle": "Native Python code execution environment inside Google AI Studio",
        "points": [
            "Built-in Code Execution: Toggle 'Code Execution' ON to allow Gemini to run Python in a secure cloud sandbox.",
            "Mathematical Verification: The model writes code to calculate complex statistical proofs, eliminating arithmetic hallucination.",
            "Visual Rendering: Generating matplotlib charts, SVG diagrams, and data tables directly in the response window."
        ],
        "script": (
            "[TA James] Slide 33 covers \"AGENTIC AI STUDIO: SANDBOXED CODE EXECUTION.\"\n\n"
            "[TA Sarah] In Google AI Studio, look at the right settings panel: you can toggle 'Code Execution' to ON! When enabled, whenever Gemini encounters a complex math problem or data parsing task, it writes Python code, executes it in a secure Google sandbox, and returns the mathematically verified output!\n\n"
            "[Prof. Peter] This completely eliminates arithmetic hallucination. The model doesn't guess what 4,892 times 3,847 is; it runs Python and gives you the exact answer with zero doubt.\n\n"
            "[TA James] It can also generate dynamic matplotlib charts and data tables on the fly!\n\n"
            "[TA Sarah] Let us inspect the Corporate Trap: Free Tier vs. Paid Tier on Slide 34."
        ),
        "koreanGuide": {
            "summary": "에이전틱 AI 스튜디오: 샌드박스 파이썬 코드 실행과 수학적 무환각",
            "points": [
                "내장 코드 실행(Code Execution): 제미나이가 스스로 파이썬 코드를 작성하고 구글 클라우드 샌드박스에서 즉시 실행",
                "수학적 무환각: 복잡한 수식과 통계 계산 시 어림짐작하지 않고 파이썬 인터프리터로 100% 정밀 계산",
                "실시간 차트 렌더링: Matplotlib 시각화 차트와 데이터 표를 응답창에 즉시 시각화"
            ],
            "tips": "사라 조교가 코드 실행 토글 스위치 기능을 설명하고 제임스가 산술 무환각의 장점을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Sandboxed Code Execution",
                "def": "Running AI-generated code within an isolated cloud runtime to verify computations safely.",
                "defKo": "샌드박스 코드 실행 환경"
            },
            {
                "term": "Arithmetic Hallucination Elimination",
                "def": "Replacing probabilistic number prediction with deterministic programmatic interpreter execution.",
                "defKo": "산술 연산 환각 근절"
            }
        ]
    },
    # Slide 34: The Corporate Trap: Free Tier vs. Paid Tier
    {
        "num": 34,
        "type": "comparison",
        "title": "THE CORPORATE TRAP: FREE TIER VS. PAID TIER",
        "subtitle": "Understanding Google AI Studio's Data Governance terms and enterprise safety",
        "leftCard": {
            "tag": "FREE TIER (DEVELOPER LAB)",
            "title": "Data May Be Reviewed",
            "points": [
                "Free API access up to 15 RPM.",
                "Human reviewers may inspect anonymized prompts.",
                "Data may be used to train future Google models.",
                "Strict Rule: NEVER enter confidential PII or enterprise code!"
            ]
        },
        "rightCard": {
            "tag": "PAID TIER / VERTEX AI",
            "title": "Enterprise Fortress",
            "points": [
                "Pay-as-you-go commercial billing.",
                "Zero human reviewers; zero model training commitment.",
                "Full CMEK encryption and SOC2 / HIPAA compliance.",
                "Strict Rule: Mandatory for all production enterprise workloads."
            ]
        },
        "script": (
            "[Prof. Peter] Slide 34 exposes \"THE CORPORATE TRAP: FREE TIER VS. PAID TIER.\" This is a critical legal and architectural distinction.\n\n"
            "[TA Sarah] Google AI Studio offers a generous Free Tier for developers. But read the terms of service carefully: on the Free Tier, your prompts may be reviewed by human trainers and used to improve Google products. It is fantastic for personal learning, but you must NEVER paste proprietary company source code or customer PII into the Free Tier!\n\n"
            "[TA James] For enterprise work, you simply link a Google Cloud Billing account or deploy via Vertex AI! On the Paid Tier, your data is 100% isolated, zero human reviewers can see it, and Google legally guarantees zero model training on your data!\n\n"
            "[Prof. Peter] Understanding cloud licensing boundaries is an essential duty of the Intelligence Architect.\n\n"
            "[TA Sarah] Let us inspect how to mitigate intellectual sloth on Slide 35."
        ),
        "koreanGuide": {
            "summary": "기업의 함정: 구글 AI 스튜디오 무료 티어 vs 유료 엔터프라이즈 티어 비교",
            "points": [
                "무료 티어의 주의점: 학습에 활용될 수 있으므로 개인 학습/개발용으로만 쓰고 기업 기밀이나 PII 절대 입력 금지",
                "유료 티어(Pay-As-You-Go/Vertex AI): 100% 테넌트 격리, 무학습 보증, 인간 검토자 배제, 기업 배포 필수 요건",
                "라이선스 및 보안 규정 준수를 관리하는 지능 건축가의 법적 분별력"
            ],
            "tips": "제임스 조교가 기업 보안 관리자 관점에서 무료 티어와 유료 티어의 법적 차이를 명확히 경고합니다."
        },
        "keyTerms": [
            {
                "term": "Commercial API SLA",
                "def": "The legally binding Service Level Agreement guaranteeing enterprise data privacy, uptime, and non-training.",
                "defKo": "상용 API 서비스 수준 계약 (SLA)"
            },
            {
                "term": "Data Logging Exemption",
                "def": "The enterprise security setting ensuring user prompts are never logged or stored for model training.",
                "defKo": "데이터 학습 로깅 면제 정책"
            }
        ]
    },
    # Slide 35: Mitigating Intellectual Sloth
    {
        "num": 35,
        "type": "content",
        "title": "MITIGATING INTELLECTUAL SLOTH",
        "subtitle": "Resisting the temptation to copy-paste unreviewed code; maintaining active critical stewardship",
        "points": [
            "The Vibe Coding Trap: Blindly accepting AI code without understanding the underlying logic or security flaws.",
            "Active Code Review: Reading every diff line, verifying time complexity, and testing edge cases.",
            "Intellectual Sovereignty: The human architect remains the sole moral and technical author of the system."
        ],
        "script": (
            "[Prof. Peter] Slide 35 addresses a vital ethical concern: \"MITIGATING INTELLECTUAL SLOTH.\" Sarah, what happens when engineers become addicted to Vibe Coding without discipline?\n\n"
            "[TA Sarah] They suffer intellectual atrophy! They become 'vibe copy-pasters'—blindly accepting 1,000 lines of AI code without reading a single line, deploying security vulnerabilities and memory leaks into production!\n\n"
            "[Prof. Peter] That is spiritual and intellectual sloth. Vibe Coding does NOT mean shutting off your brain! It means elevating your brain from syntax typing to rigorous code review, algorithmic auditing, and architectural verification!\n\n"
            "[TA James] A master architect reads every diff, challenges the model's assumptions, and runs rigorous unit tests.\n\n"
            "[TA Sarah] Let us inspect our fourth enterprise case study on Slide 36!"
        ),
        "koreanGuide": {
            "summary": "지적 나태함의 경계: 무검증 복사-붙여넣기의 함정과 비판적 청지기직",
            "points": [
                "바이브 코딩의 함정: 1,000줄의 AI 코드를 한 줄도 읽지 않고 맹목적으로 승인하는 지적 퇴화 경계",
                "능동적 코드 리뷰: 문법 타이핑에서 해방된 에너지를 알고리즘 감사와 보안 취약점 검증에 집중",
                "주권적 책임: 최종 시스템의 도덕적, 기술적 책임은 언제나 인간 아키텍트에게 귀속"
            ],
            "tips": "피터 교수가 '바이브 복붙러'의 위험성을 경고하며 진정한 지능 건축가의 비판적 품격을 설파합니다."
        },
        "keyTerms": [
            {
                "term": "Intellectual Sloth",
                "def": "The uncritical abdication of human reasoning and code verification to automated generative models.",
                "defKo": "지적 나태함 (비판적 사고 유기)"
            },
            {
                "term": "Active Architectural Review",
                "def": "The disciplined engineering practice of inspecting, testing, and validating all AI-generated code diffs.",
                "defKo": "능동적 아키텍처 감사"
            }
        ]
    },
    # Slide 36: Case Study 4: Zero-Code Enterprise ERP Dashboard Generation
    {
        "num": 36,
        "type": "casestudy",
        "title": "CASE STUDY 4: ZERO-CODE ERP DASHBOARD GENERATION",
        "subtitle": "Supply Chain Director builds custom warehouse telemetry web app in 2 hours via Vibe Coding",
        "company": "Automotive Parts Manufacturing Enterprise",
        "problem": "Supply Chain Director needed a custom real-time telemetry dashboard for 12 robotic warehouses; internal IT quoted a 6-month backlog and $150,000 budget.",
        "solution": "Director used Google AI Studio Vibe Coding with Many-Shot UI exemplars and Gemini's sandboxed code execution to build the full-stack React/FastAPI web app in 2 hours.",
        "impact": "Deployed to production same day; slashed warehouse inventory discrepancy by 42%; saved $150,000 in custom software development fees.",
        "script": (
            "[Prof. Peter] Slide 36 presents \"CASE STUDY 4: ZERO-CODE ENTERPRISE ERP DASHBOARD GENERATION.\"\n\n"
            "[TA Sarah] A Supply Chain Director at an automotive manufacturing plant needed a real-time visual telemetry dashboard to track robotic inventory across 12 warehouses. Internal IT told him: 'We have a 6-month backlog, and it will cost 150,000 dollars!'\n\n"
            "[TA James] On a Saturday morning, the Director opened Google AI Studio. Using Vibe Coding, he uploaded warehouse CSV data schemas, provided 5 UI exemplars, and directed Gemini in natural language to build a React dashboard with live FastAPI WebSockets!\n\n"
            "[Prof. Peter] In just 2 hours, the entire full-stack application was running! He deployed it to Google Cloud Run that afternoon, saving 150,000 dollars and slashing warehouse inventory discrepancies by 42% in the very first month!\n\n"
            "[TA Sarah] That is the revolutionary democratizing power of Vibe Coding.\n\n"
            "[TA James] Let us see how time redemption elevates our life purpose on Slide 37."
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 4: 비개발자 공급망 총괄이 2시간 만에 구축한 ERP 대시보드",
            "points": [
                "문제 상황: 12개 로봇 물류창고 모니터링 앱 필요, 사내 IT는 6개월 대기와 15만 달러 예산 요구",
                "솔루션: 구글 AI 스튜디오 바이브 코딩으로 5개 UI 예시와 CSV 스키마를 주고 2시간 만에 풀스택 리액트/FastAPI 완성",
                "성과: 당일 배포 완료, 재고 불일치 42% 감소, 15만 달러 개발비 전액 절감"
            ],
            "tips": "사라 조교와 제임스 조교가 비개발자 리더가 직접 프로덕션 앱을 자급자족하는 바이브 코딩의 위력을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Democratized Software Creation",
                "def": "Empowering non-technical domain leaders to build enterprise software tools using natural language.",
                "defKo": "소프트웨어 개발의 대중화"
            },
            {
                "term": "Rapid Prototyping to Production",
                "def": "The continuous acceleration from initial natural language concept to live cloud container deployment.",
                "defKo": "초고속 프로토타이핑 및 배포"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 37: Redeeming Time for Soli Deo Gloria
    {
        "num": 37,
        "type": "content",
        "title": "REDEEMING TIME FOR SOLI DEO GLORIA",
        "subtitle": "Ephesians 5:16: Channeling reclaimed engineering hours into faith, family, and deep contemplation",
        "points": [
            "Multiplying Output: What took 3 months of manual coding now takes 3 hours of intelligent orchestration.",
            "Reclaiming Lifespan: Refusing to spend 70 hours a week trapped in low-level syntax troubleshooting.",
            "Higher Calling: Dedicating our redeemed cognitive capital to worship, community service, and ethical leadership."
        ],
        "script": (
            "[Prof. Peter] Slide 37 proclaims \"REDEEMING TIME FOR SOLI DEO GLORIA.\" In our masterclass, every technical breakthrough connects back to our eternal calling.\n\n"
            "[TA Sarah] When you master 1M token contexts, Many-Shot ICL, Context Caching, and Vibe Coding, you don't just work faster—you multiply your human leverage by a factor of twenty!\n\n"
            "[TA James] What previously required 3 months of grueling syntax typing now takes 3 hours of focused architectural dialogue. You reclaim 30 hours every week to invest in deep relationships, prayer, and mentorship!\n\n"
            "[Prof. Peter] We build intelligent systems not for human pride, but to redeem finite time for God's glory.\n\n"
            "[TA Sarah] Let us inspect our 6-step Google AI Studio Deployment Blueprint on Slide 38!"
        ),
        "koreanGuide": {
            "summary": "세월을 아끼라: 20배의 생산성 레버리지와 Soli Deo Gloria의 실천",
            "points": [
                "20배의 생산성 곱절: 3개월 걸리던 수작업 코딩을 3시간의 지적 오케스트레이션으로 압축",
                "생애 시간 회복: 주당 30시간의 불필요한 문법 디버깅 노역에서 해방",
                "거룩한 소명: 회복된 지적 에너지를 기도, 가족 돌봄, 후배 멘토링, 사회적 섬김에 헌신"
            ],
            "tips": "피터 교수가 기술적 레버리지를 신앙적 시간 구속과 연결하여 깊은 감동을 전합니다."
        },
        "keyTerms": [
            {
                "term": "20X Productivity Multiplier",
                "def": "The radical compression of software development cycles achieved through agentic coding and massive context.",
                "defKo": "20배 생산성 승수"
            },
            {
                "term": "Cognitive Capital Redirection",
                "def": "Channeling reclaimed mental energy away from administrative chores into high-level strategic and spiritual callings.",
                "defKo": "지적 자본의 거룩한 재배치"
            }
        ]
    },
    # Slide 38: The 6-Step Google AI Studio Blueprint
    {
        "num": 38,
        "type": "content",
        "title": "THE 6-STEP AI STUDIO DEPLOYMENT BLUEPRINT",
        "subtitle": "The standardized pipeline from raw concept to cached enterprise production endpoint",
        "points": [
            "Step 1: Model Selection (Gemini 3.5 Pro for architecture; Flash for high-throughput execution).",
            "Step 2: System Instruction Configuration (Locking role, persona, JSON schema, and safety rules).",
            "Step 3: Golden Exemplar Assembly (Injecting 50 - 100 diverse Many-Shot input-output pairs).",
            "Step 4: Context Caching Activation (Enabling TTL caching on TPU HBM memory for 87% cost cut).",
            "Step 5: Sandboxed Code Execution Verification (Running unit test verification in Python sandbox).",
            "Step 6: Production API Export (Exporting cURL / Python SDK code with Paid Tier billing keys)."
        ],
        "script": (
            "[TA Sarah] Slide 38 provides the master blueprint: \"THE 6-STEP GOOGLE AI STUDIO DEPLOYMENT BLUEPRINT.\"\n\n"
            "[TA James] Follow this exact 6-step checklist in your enterprise projects: Step 1: Select Pro or Flash. Step 2: Write System Instructions. Step 3: Inject 50 to 100 golden exemplars. Step 4: Toggle Context Caching for 87% savings! Step 5: Verify in the Python code sandbox. Step 6: Click 'Get Code' and export to Python SDK!\n\n"
            "[Prof. Peter] This structured methodology transforms ad-hoc prompt experiments into repeatable enterprise software engineering.\n\n"
            "[TA Sarah] Let us inspect our Pre-Deployment Production Checklist on Slide 39."
        ),
        "koreanGuide": {
            "summary": "구글 AI 스튜디오 6단계 프로덕션 배포 청사진",
            "points": [
                "1단계: 모델 선택 (전략적 Pro vs 초고속 Flash)",
                "2단계: 시스템 지시문 헌법 작성 (JSON 스키마 및 보안 규칙)",
                "3단계: 골든 예시 50~100개 Many-Shot 주입",
                "4단계: 87% 절감을 위한 컨텍스트 캐싱 활성화",
                "5단계: 파이썬 샌드박스 단위 테스트 검증",
                "6단계: 파이썬 SDK / cURL 상용 API 코드 즉시 내보내기"
            ],
            "tips": "제임스 조교가 6단계 워크플로우를 실무 개발 표준으로 명쾌하게 정리해 줍니다."
        },
        "keyTerms": [
            {
                "term": "AI Studio Production Blueprint",
                "def": "The formal 6-stage engineering process converting exploratory prompts into hardened cloud API endpoints.",
                "defKo": "AI 스튜디오 프로덕션 배포 청사진"
            },
            {
                "term": "SDK Code Export",
                "def": "Google AI Studio's feature generating drop-in Python, JavaScript, and cURL API client boilerplate.",
                "defKo": "SDK 클라이언트 코드 즉시 추출"
            }
        ]
    },
    # Slide 39: Production Checklist: Pre-Deployment Verification
    {
        "num": 39,
        "type": "content",
        "title": "PRODUCTION CHECKLIST: PRE-DEPLOYMENT VERIFICATION",
        "subtitle": "The 6-gate audit every Many-Shot prompt must pass before live commercial deployment",
        "points": [
            "Gate 1: Paid Tier Google Cloud billing verified (Zero human review, zero model training commitment).",
            "Gate 2: Context Cache TTL and hit-rate monitored on Google Cloud Cloud Monitoring dashboards.",
            "Gate 3: Temperature set to 0.0 for deterministic schema parsing and code generation tasks.",
            "Gate 4: 100% JSON Schema compliance verified across 50 synthetic edge-case test payloads.",
            "Gate 5: Sandboxed code execution enabled with strict timeout and memory limits.",
            "Gate 6: Human-on-the-Loop approval workflows established for all state-mutating actions."
        ],
        "script": (
            "[TA James] Slide 39 presents our \"PRODUCTION CHECKLIST: PRE-DEPLOYMENT VERIFICATION.\"\n\n"
            "[TA Sarah] Before pushing your AI Studio endpoint to production, verify all 6 gates: Gate 1: Paid Tier active. Gate 2: Context Caching TTL configured. Gate 3: Temperature set to 0.0. Gate 4: 100% JSON schema validation passed. Gate 5: Code execution sandboxed. Gate 6: Human-on-the-Loop review rules established!\n\n"
            "[Prof. Peter] Strict quality gates protect your organization's reputation and security.\n\n"
            "[TA Sarah] Let us inspect the Architect's Ethical Code on Slide 40."
        ),
        "koreanGuide": {
            "summary": "프로덕션 체크리스트: 상용 배포 전 6대 품질/보안 검증 관문",
            "points": [
                "1관문: 유료 티어 결제 계정 연결 (데이터 무단 학습 차단 보증)",
                "2관문: 컨텍스트 캐싱 TTL 및 히트율 모니터링 설정",
                "3관문: 재현성을 위한 온도 0.0 고정",
                "4관문: 50개 예외 테스트 데이터에 대한 100% JSON 스키마 통과",
                "5관문: 샌드박스 실행 시간 및 메모리 제한 설정",
                "6관문: Human-on-the-Loop 인간 최종 승인 체계 구축"
            ],
            "tips": "제임스 조교가 6대 검증 관문을 단호하게 체크리스트로 확인합니다."
        },
        "keyTerms": [
            {
                "term": "Quality Audit Gate",
                "def": "A mandatory verification checkpoint that prompts and configurations must satisfy before live release.",
                "defKo": "품질 감사 관문"
            },
            {
                "term": "JSON Schema Validation",
                "def": "Automated verification ensuring model output strictly matches the required data structure specification.",
                "defKo": "JSON 스키마 유효성 검증"
            }
        ]
    },
    # Slide 40: Soli Deo Gloria: The Sanctity of Code
    {
        "num": 40,
        "type": "content",
        "title": "SOLI DEO GLORIA: THE SANCTITY OF CODE",
        "subtitle": "Dedicating our software architecture, algorithms, and computational scale to God Alone",
        "points": [
            "Soli Deo Gloria: The eternal foundation of Oikos University and Smart Insight Lab.",
            "Incorruptible Logic: Writing code that reflects divine order, mathematical honesty, and ethical integrity.",
            "Stewarding Genius: Using frontier 1500+ ELO models to uplift human dignity and heal community fractures."
        ],
        "script": (
            "[Prof. Peter] Slide 40 declares our foundational motto: \"SOLI DEO GLORIA: THE SANCTITY OF CODE: To God Alone Be the Glory.\"\n\n"
            "[TA Sarah] Software is not merely commercial text; code is a manifestation of logic, order, and human creativity.\n\n"
            "[TA James] When we build systems that process millions of tokens flawlessly, save our organizations millions of dollars, and liberate human beings from drudgery, our engineering becomes an act of faithful worship!\n\n"
            "[Prof. Peter] May all our algorithms and systems reflect the beauty and truth of our Creator.\n\n"
            "[TA Sarah] Let us review Session 6 Key Takeaways on Slide 41!"
        ),
        "koreanGuide": {
            "summary": "Soli Deo Gloria: 코드의 거룩함과 영원한 목적을 향한 헌신",
            "points": [
                "오직 하나님께 영광(Soli Deo Gloria): 단순한 상업적 코딩을 넘어선 신적 질서와 진실성의 구현",
                "무결한 논리: 거짓과 오류를 배격하고 수학적 정직성을 품은 아키텍처 설계",
                "천재적 지능의 선용: 1500 ELO의 초지능을 인간 존엄성 회복과 이웃 사랑에 활용"
            ],
            "tips": "3인의 강사진이 한목소리로 수업의 영적 기초와 소명감을 엄숙하게 선언합니다."
        },
        "keyTerms": [
            {
                "term": "Soli Deo Gloria",
                "def": "The foundational theological motto dedicating all intellectual and technological mastery to the Glory of God Alone.",
                "defKo": "솔리 데오 글로리아 (오직 하나님께 영광)"
            },
            {
                "term": "Mathematical Integrity",
                "def": "The commitment to uncompromising accuracy, truthfulness, and reproducibility across software systems.",
                "defKo": "수학적 무결성 (정직한 코드)"
            }
        ]
    },
    # Slide 41: Session 6 Summary & Key Takeaways
    {
        "num": 41,
        "type": "content",
        "title": "SESSION 6 SUMMARY & KEY TAKEAWAYS",
        "subtitle": "Synthesizing the 4 foundational pillars of massive context and Vibe Coding",
        "points": [
            "Pillar 1: 1M Token Horizon (Ended semantic chunking fragmentation with 99.8% Needle in a Haystack recall).",
            "Pillar 2: Many-Shot ICL (Replaced costly fine-tuning with 50-100 golden exemplars inside the prompt).",
            "Pillar 3: Context Caching (Slashed API costs by 87% and dropped TTFT latency to 150ms on TPU HBM).",
            "Pillar 4: Vibe Coding (Empowered domain leaders to orchestrate full-stack bespoke software via natural language)."
        ],
        "script": (
            "[TA Sarah] Slide 41 provides our \"SESSION 6 SUMMARY & 4 FOUNDATIONAL PILLARS.\"\n\n"
            "[TA James] Pillar 1: The 1M Token Horizon ends vector chunking loss forever. Pillar 2: Many-Shot ICL gives you instant domain expertise in 500ms without fine-tuning! Pillar 3: Context Caching cuts your cloud bills by 87%! And Pillar 4: Vibe Coding turns you into a software Creative Director!\n\n"
            "[Prof. Peter] When these four pillars unite, your creative leverage multiplies beyond measure.\n\n"
            "[TA Sarah] Let us inspect the Life OS Vibe Coding Workbench on Slide 42!"
        ),
        "koreanGuide": {
            "summary": "Session 6 요약 및 4대 핵심 축 총정리",
            "points": [
                "1대 축: 100만 토큰 문맥 (청킹 손실 퇴출, 건초더미 99.8% 회수율)",
                "2대 축: Many-Shot ICL (50~100개 예시로 파인튜닝 없는 즉각적 도메인 전문가화)",
                "3대 축: 컨텍스트 캐싱 (TPU 메모리 활용으로 87% 비용 절감 및 150ms 반응 속도)",
                "4대 축: 바이브 코딩 (자연어 지휘를 통한 전사 맞춤형 풀스택 소프트웨어 자급자족)"
            ],
            "tips": "제임스 조교가 4대 기둥을 리듬감 있게 요약하여 학습 효과를 극대화합니다."
        },
        "keyTerms": [
            {
                "term": "Architectural Synthesis",
                "def": "The unified integration of massive context, in-context learning, FinOps caching, and natural language development.",
                "defKo": "아키텍처 통합 합성"
            },
            {
                "term": "Holistic Developer Leverage",
                "def": "The exponential multiplication of software productivity attained through AI-native development workflows.",
                "defKo": "전체론적 개발 레버리지"
            }
        ]
    },
    # Slide 42: Life OS Vibe Coding Workbench
    {
        "num": 42,
        "type": "content",
        "title": "LIFE OS VIBE CODING WORKBENCH",
        "subtitle": "Setting up your personal development cockpit: Google AI Studio + VS Code + Python SDK",
        "points": [
            "Cockpit Setup: Google AI Studio in Chrome tab 1 for prompt prototyping and caching.",
            "VS Code Integration: Exporting tested SDK scripts directly into local git repositories.",
            "Rapid Feedback Loop: Prototyping prompts in AI Studio, testing code live, and committing to production."
        ],
        "script": (
            "[Prof. Peter] Slide 42 outlines your personal development cockpit: \"LIFE OS VIBE CODING WORKBENCH.\"\n\n"
            "[TA Sarah] How do we integrate these tools into our daily workflow? Keep Google AI Studio open in Chrome Tab 1 as your prompt forge and context caching playground. Keep VS Code open for local git repository management.\n\n"
            "[TA James] You prototype your Many-Shot prompt in AI Studio, test with sandboxed code execution, click 'Get Code', and paste the clean Python SDK snippet directly into your local repo! You deploy production features in minutes instead of weeks!\n\n"
            "[TA Sarah] Let us inspect the Architect's Intellectual Stewardship on Slide 43."
        ),
        "koreanGuide": {
            "summary": "라이프 OS 바이브 코딩 워크벤치: AI 스튜디오 + VS Code 개발 콕핏",
            "points": [
                "개발 콕핏 구성: 크롬 1번 탭에 구글 AI 스튜디오를 프롬프트 및 캐싱 실험실로 상시 상주",
                "VS Code 연동: AI 스튜디오에서 검증된 SDK 파이썬 코드를 로컬 깃 저장소로 즉시 내보내기",
                "초고속 피드백 루프: 수 분 만에 아이디어를 상용 배포 코드로 완성하는 작업 흐름"
            ],
            "tips": "사라 조교와 제임스 조교가 실제 업무에서 사용하는 듀얼 모니터 개발 배치 팁을 전합니다."
        },
        "keyTerms": [
            {
                "term": "Development Cockpit",
                "def": "A multi-window operational setup harmonizing cloud prompt playgrounds with local IDE code repositories.",
                "defKo": "개발 콕핏 워크벤치"
            },
            {
                "term": "Drop-in SDK Integration",
                "def": "The seamless export of validated prompt configurations into production programming environments.",
                "defKo": "즉시 실행형 SDK 연동"
            }
        ]
    },
    # Slide 43: The Architect's Intellectual Stewardship
    {
        "num": 43,
        "type": "content",
        "title": "THE ARCHITECT'S INTELLECTUAL STEWARDSHIP",
        "subtitle": "Balancing speed with deep algorithmic comprehension and ethical responsibility",
        "points": [
            "The True Craftsman: Using AI to accelerate creation without losing mastery over foundational computer science.",
            "Root-Cause Understanding: Knowing why an algorithm works, not just that it runs without throwing errors.",
            "Mentoring the Next Generation: Teaching junior engineers how to think deeply in an age of automated generation."
        ],
        "script": (
            "[Prof. Peter] Slide 43 reflects on \"THE ARCHITECT'S INTELLECTUAL STEWARDSHIP.\" True mastery is not about speed alone; it is about deep root-cause understanding.\n\n"
            "[TA Sarah] A true craftsman uses high-speed power tools, but understands the grain of the wood! As Intelligence Architects, we use Gemini to write code at lightning speed, but we understand data structures, computational complexity, and security invariants.\n\n"
            "[TA James] We mentor junior developers not to be lazy copy-pasters, but to be rigorous architects who question assumptions and build resilient systems!\n\n"
            "[Prof. Peter] Let us inspect our capstone enterprise case study on Slide 44!"
        ),
        "koreanGuide": {
            "summary": "지능 건축가의 지적 청지기직: 속도와 기초 컴퓨터 과학 장인정신의 조화",
            "points": [
                "진정한 장인의 자세: 전동 공구(AI)를 쓰되 나무의 결(컴퓨터 과학 기초)을 꿰뚫어 보는 통찰력",
                "근본 원인 이해: 코드가 에러 없이 돌아가는 것에 만족하지 않고 왜 돌아가는지 아키텍처 원리를 규명",
                "후배 엔지니어 멘토링: 단순 복붙러가 아닌 깊이 생각하고 검증하는 참된 공학자 양성"
            ],
            "tips": "피터 교수가 장인정신(Craftsmanship)과 기초 학문의 가치를 깊이 있게 설파합니다."
        },
        "keyTerms": [
            {
                "term": "Root-Cause Comprehension",
                "def": "Deep structural understanding of underlying computational mechanics rather than superficial empirical observation.",
                "defKo": "근본 원인 통찰력"
            },
            {
                "term": "Architectural Craftsmanship",
                "def": "The dedication to engineering excellence, elegance, and integrity in software system design.",
                "defKo": "아키텍처 장인정신"
            }
        ]
    },
    # Slide 44: Case Study 5: 22X Developer Velocity ROI & AI Studio Blueprint
    {
        "num": 44,
        "type": "casestudy",
        "title": "CASE STUDY 5: 22X DEVELOPER VELOCITY BLUEPRINT",
        "subtitle": "Global SaaS Enterprise equips 1,500 engineers with Google AI Studio & Many-Shot ICL",
        "company": "Silicon Valley Cloud Enterprise SaaS Leader",
        "problem": "1,500 enterprise software engineers spent 40% of sprint time writing repetitive API boilerplate and CRUD endpoints, causing product roadmap delays.",
        "solution": "Deployed centralized Google AI Studio with shared Many-Shot exemplar libraries, Context Caching, and sandboxed Python testing.",
        "impact": "22X measured developer velocity on boilerplate endpoints; feature cycle time dropped from 14 days to 1.5 days; annual engineering capacity expanded by $48M value.",
        "script": (
            "[Prof. Peter] Slide 44 presents our capstone enterprise case study: \"CASE STUDY 5: 22X DEVELOPER VELOCITY BLUEPRINT.\"\n\n"
            "[TA Sarah] A leading Silicon Valley enterprise SaaS provider with 1,500 software engineers had a massive velocity bottleneck: engineers were spending nearly half their sprint cycles writing repetitive REST API boilerplate, schema validators, and CRUD endpoints!\n\n"
            "[TA James] They deployed Google AI Studio with a centralized repository of 100 golden Many-Shot exemplars encoding their company's exact coding conventions. They enabled Context Caching and trained engineers on Vibe Coding!\n\n"
            "[Prof. Peter] Look at the results: developer velocity on boilerplate code surged by 22X! Feature release cycle time dropped from 14 days down to 1.5 days, expanding annual engineering capacity by 48 million dollars in value!\n\n"
            "[TA Sarah] That is the ultimate enterprise transformation.\n\n"
            "[TA James] Now let us build your own Instant Expert Forge in Lab 6 on Slide 45!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 5: 실리콘밸리 SaaS 대기업 22배 개발 속도 향상 및 4,800만 달러 가치 창출",
            "points": [
                "문제 상황: 1,500명의 엔지니어가 스프린트 시간의 40%를 반복적인 보일러플레이트 API 작성에 낭비",
                "솔루션: 100개 골든 예시 라이브러리와 컨텍스트 캐싱이 적용된 전사 구글 AI 스튜디오 바이브 코딩 환경 구축",
                "성과: 보일러플레이트 개발 속도 22배 가속, 기능 릴리즈 주기 14일에서 1.5일로 단축, 연간 4,800만 달러 개발 가치 창출"
            ],
            "tips": "사라 조교와 제임스 조교가 22배 개발 속도 향상의 구체적인 비즈니스 효과를 강조하며 실습으로 유도합니다."
        },
        "keyTerms": [
            {
                "term": "22X Velocity Multiplier",
                "def": "The dramatic acceleration of routine software authoring achieved by combining Many-Shot ICL with Vibe Coding.",
                "defKo": "22배 개발 속도 승수"
            },
            {
                "term": "Feature Cycle Time Compression",
                "def": "The reduction of calendar time required to take a software feature from specification to live production deployment.",
                "defKo": "기능 출시 주기 압축"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 45: Hands-on Lab 6 & Conclusion
    {
        "num": 45,
        "type": "lab",
        "title": "🛠️ HANDS-ON LAB 6 & CONCLUSION",
        "subtitle": "Building an Instant Expert Forge with 50-Shot ICL and Context Caching in AI Studio",
        "mission": "Open Google AI Studio, select Gemini 3.5 Pro, assemble a 50-Shot exemplar set for a specialized enterprise task, enable Context Caching, test sandboxed code execution, and export production Python SDK code.",
        "steps": [
            "Step 1: Navigate to `aistudio.google.com` and instantiate a new prompt with Gemini 3.5 Pro.",
            "Step 2: Configure System Instructions specifying exact JSON output schemas and safety rules.",
            "Step 3: Paste 50 diverse input-output golden exemplars covering edge cases into the context window.",
            "Step 4: Enable Context Caching and verify that prompt token pricing receives the 87% discount badge.",
            "Step 5: Toggle 'Code Execution' to ON, run a test query, and export the live Python SDK client snippet!"
        ],
        "script": (
            "[TA Sarah] Here we are at Slide 45: \"🛠️ HANDS-ON LAB 6 & SESSION CONCLUSION!\"\n\n"
            "[TA James] Tonight's hands-on lab will transform your engineering skills! Step 1: Open `aistudio.google.com` and select Gemini 3.5 Pro. Step 2: Write your System Instructions. Step 3: Paste 50 golden exemplars for a custom task. Step 4: Toggle Context Caching and see the 87% discount badge! Step 5: Toggle Code Execution ON, run a test query, and export your Python SDK snippet!\n\n"
            "[Prof. Peter] Once you experience the instant mastery of 50-Shot In-Context Learning running on cached TPU memory, you will never build software the old way again.\n\n"
            "[TA Sarah] In our next session, Session 7, we will take this intelligence to the open web and master the revolutionary WebMCP Protocol and the 90% HTML Token Diet!\n\n"
            "[Prof. Peter] On behalf of TA Sarah Jenkins, TA James Wilson, and the entire Smart Insight Lab, congratulations on mastering Session 6! Soli Deo Gloria, and we will see you in Session 7!"
        ),
        "koreanGuide": {
            "summary": "실습 과제 6 및 세션 마무리: 구글 AI 스튜디오 50-Shot ICL 및 컨텍스트 캐싱 포지 구축",
            "points": [
                "실습 미션: 구글 AI 스튜디오에서 제미나이 3.5 프로를 선택하고 50개 골든 예시를 주입한 전문 도메인 포지 구축",
                "컨텍스트 캐싱 활성화 및 87% 비용 절감 뱃지 확인",
                "코드 실행(Code Execution)을 활성화하여 무오류 산술 연산 검증 후 파이썬 SDK 코드로 즉시 내보내기"
            ],
            "tips": "3인의 강사진이 오늘 수업의 성취를 축하하고 다음 세션(Session 7: WebMCP 프로토콜 & HTML 토큰 다이어트)에 대한 기대감을 높이며 마무리합니다."
        },
        "keyTerms": [
            {
                "term": "Hands-on Milestone",
                "def": "The practical engineering completion of a functioning technical artifact fulfilling the session's learning objectives.",
                "defKo": "실습 달성 마일스톤"
            },
            {
                "term": "Instant Expert Forge",
                "def": "A production-ready Google AI Studio prompt configuration delivering instant domain mastery via Many-Shot ICL and caching.",
                "defKo": "즉각적 도메인 전문가 포지"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    }
]

def generate_session6_md(slides):
    lines = []
    lines.append("# Session 6: The 1-Million Token Playground: Vibe Coding, Many-shot ICL, and Cost Optimization with Google AI Studio")
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
    new_export = f"export const SLIDES_SESSION_6 = {slides_json};"
    
    pattern = r"export\s+const\s+SLIDES_SESSION_6\s*=\s*\[[\s\S]*?\];"
    if re.search(pattern, content):
        updated_content = re.sub(pattern, lambda m: new_export, content, count=1)
        with open(SLIDES_DATA_JS, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Successfully updated SLIDES_SESSION_6 in slidesData.js!")
    else:
        print("Could not find SLIDES_SESSION_6 pattern in slidesData.js!")

def main():
    print(f"Total slides configured: {len(SLIDES_45_SESSION_6)}")
    
    # Verify part dividers
    part_slides = [s for s in SLIDES_45_SESSION_6 if s['type'] == 'section']
    print(f"Total PART Section Slides: {len(part_slides)}")
    for ps in part_slides:
        print(f"  Slide {ps['num']:02d}: {ps['title']}")
        
    # Verify case studies
    case_slides = [s for s in SLIDES_45_SESSION_6 if 'CASE STUDY' in s['title']]
    print(f"Total Case Study Slides: {len(case_slides)}")
    for cs in case_slides:
        print(f"  Slide {cs['num']:02d}: {cs['title']}")

    # 1. Write session6.md
    session6_md_content = generate_session6_md(SLIDES_45_SESSION_6)
    with open(SESSION6_MD, 'w', encoding='utf-8') as f:
        f.write(session6_md_content)
    print(f"Successfully generated and saved {SESSION6_MD} ({len(session6_md_content)} bytes)")
    
    # 2. Update slidesData.js
    update_slides_data_js(SLIDES_45_SESSION_6)
    
    print("Session 6 generation completed successfully!")

if __name__ == '__main__':
    main()
