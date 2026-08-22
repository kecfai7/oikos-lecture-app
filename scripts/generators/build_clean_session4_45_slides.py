# -*- coding: utf-8 -*-
"""
Oikos University - Session 4 Clean 45-Slide Master Generator
Course: The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom
Session 4: Grounded Intelligence on My Data: The RAG Revolution and Private Knowledge Factories
Features:
- Full 45 Slides with 3-Presenter Trio (Prof. Peter Kim, TA Sarah Jenkins, TA James Wilson)
- Clean 4-Part Structure (Part 1: Slide 2, Part 2: Slide 12, Part 3: Slide 23, Part 4: Slide 30)
- 5 Practical Enterprise Case Studies:
    1. Slide 11: Wall Street Equity Research Triage (10-Hour Miracle)
    2. Slide 22: Big Pharma FDA 10,000-Page Clinical Trial Audit
    3. Slide 29: Global Law Firm M&A Discovery & Privilege Isolation
    4. Slide 36: Semiconductor Patent Infringement Prior-Art Defense
    5. Slide 44: 15X Enterprise Research ROI & 5-Step RAG Deployment Blueprint
- Full sync with session4.md and slidesData.js (SLIDES_SESSION_4)
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
SESSION4_MD = os.path.join(BASE_DIR, "session4.md")

SLIDES_45_SESSION_4 = [
    # Slide 1: Course Title
    {
        "num": 1,
        "type": "title",
        "title": "OIKOS UNIVERSITY • SOLI DEO GLORIA",
        "subtitle": "THE ARCHITECT OF INTELLIGENCE: Mastering Agentic IT & Strategic Wisdom",
        "detail": "Session 4: Grounded Intelligence on My Data: The RAG Revolution and Private Knowledge Factories",
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab",
        "script": (
            "[Prof. Peter] Welcome back, global leaders and scholars, to Oikos University! I am Professor Peter Kim, Director of Smart Insight Lab. Today, we step into one of the most critical milestones of our entire masterclass on Slide 1: \"Session 4: Grounded Intelligence on My Data: The RAG Revolution and Private Knowledge Factories.\"\n\n"
            "[TA Sarah] Hello everyone! I am Sarah Jenkins, your Senior AI Research Fellow. In the previous sessions, we unlocked autonomous background daemons and OS shell execution. But today, we confront the single greatest crisis in artificial intelligence: hallucination and truth verification!\n\n"
            "[TA James] And I am James Wilson, your DevOps & Infrastructure TA! Out in enterprise production, a chatbot that fabricates fake API endpoints, hallucinates false legal citations, or leaks proprietary data will get your company sued in 24 hours. Today, we show you how to build an unbreakable, zero-hallucination private knowledge factory!\n\n"
            "[Prof. Peter] Under our sacred motto, \"SOLI DEO GLORIA—To God Alone Be the Glory,\" truth is our non-negotiable bedrock. We do not build lying stochastic parrots; we architect grounded, citation-anchored intelligence.\n\n"
            "[TA Sarah] Let us open Part 1 and explore how to defeat the crisis of hallucination on Slide 2!"
        ),
        "koreanGuide": {
            "summary": "Session 4 개요 및 Oikos University 3인 강사진(피터 교수, 사라 수석조교, 제임스 개발조교) 환영 인사",
            "points": [
                "강의 주제: RAG(검색 증강 생성) 혁명과 프라이빗 지식 공장 구축",
                "일반 퍼블릭 LLM의 치명적 환각(Hallucination) 문제를 근절하는 그라운디드 지능(Grounded Intelligence) 소개",
                "출처 인용(Citations) 기반 100% 검증 가능한 엔터프라이즈 AI 아키텍처 수립"
            ],
            "tips": "피터 교수의 진리 철학과 사라 조교의 RAG 시스템 분석, 제임스 조교의 프로덕션 보안 관점을 조화롭게 전달하세요."
        },
        "keyTerms": [
            {
                "term": "Grounded Intelligence",
                "def": "AI reasoning strictly anchored to verified, private user source documents with verifiable citations.",
                "defKo": "그라운디드 지능 (근거 기반 지능)"
            },
            {
                "term": "RAG (Retrieval-Augmented Generation)",
                "def": "An architecture combining vector retrieval with LLMs to ground generative output in authoritative factual sources.",
                "defKo": "RAG (검색 증강 생성)"
            }
        ]
    },
    # Slide 2: Part 1 Section Divider
    {
        "num": 2,
        "type": "section",
        "title": "PART 1: THE CRISIS OF HALLUCINATION & HONEST INTELLIGENCE",
        "subtitle": "Defeating the lying parrot and establishing the sacred bedrock of verifiable truth under Soli Deo Gloria",
        "script": (
            "[TA Sarah] Look at Slide 2: \"PART 1: THE CRISIS OF HALLUCINATION & HONEST INTELLIGENCE.\" Professor, why do general-purpose LLMs hallucinate so aggressively even when they have trillions of parameters?\n\n"
            "[Prof. Peter] Because fundamentally, a vanilla language model is a probabilistic next-token predictor! It has no intrinsic concept of ontological truth—it only optimizes for statistical plausibility. When it doesn't know an answer, it fabricates a convincing lie with supreme confidence.\n\n"
            "[TA James] In enterprise software engineering, probabilistic guessing is totally unacceptable. If an engineer asks for a database migration script and the model hallucinates a non-existent parameter, the production cluster drops immediately!\n\n"
            "[TA Sarah] That is why Part 1 is dedicated to Honest Intelligence: shifting from unconstrained creative generation to strictly bounded, source-anchored reasoning.\n\n"
            "[Prof. Peter] Let us examine the overwhelming crisis of information obesity that knowledge workers face on Slide 3."
        ),
        "koreanGuide": {
            "summary": "Part 1 섹션 전환: 환각의 위기와 정직한 지능(Honest Intelligence)의 절대적 필요성",
            "points": [
                "환각의 원인: 언어 모델의 본질은 진리 판별기가 아닌 확률적 다음 토큰 예측기(Stochastic Predictor)",
                "엔터프라이즈 리스크: 잘못된 법률 인용이나 파라미터 날조는 서비스 중단과 법적 책임 야기",
                "정직한 지능: 알지 못하는 것은 모른다고 선언하고 오직 주어진 원천 문서에만 기반해 답변"
            ],
            "tips": "사라 조교가 일반 챗봇의 날조 문제를 짚고, 제임스가 인프라 장애 리스크를 경고하며 피터 교수가 정직한 지능의 철학을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Probabilistic Predictor",
                "def": "A model designed to predict statistically probable token sequences rather than evaluate absolute factual truth.",
                "defKo": "확률적 토큰 예측기"
            },
            {
                "term": "Honest Intelligence",
                "def": "AI reasoning constrained strictly by verified source facts, declaring explicit ignorance when evidence is absent.",
                "defKo": "정직한 지능 (무환각 AI)"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 3: The Crisis of Information Obesity
    {
        "num": 3,
        "type": "content",
        "title": "THE CRISIS OF INFORMATION OBESITY",
        "subtitle": "Knowledge workers drowning in unindexed documents, research papers, and disconnected silos",
        "points": [
            "Global enterprise data grows at 28% CAGR, yet over 80% remains unstructured and unsearchable.",
            "Knowledge workers spend 2.5 hours daily searching for internal documentation across fragmented silos.",
            "Information overload leads to severe cognitive fatigue, shallow synthesis, and duplicated work."
        ],
        "script": (
            "[TA Sarah] Slide 3 highlights \"THE CRISIS OF INFORMATION OBESITY.\" Modern professionals are not starving for data—they are drowning in it!\n\n"
            "[TA James] Look at the metrics: enterprise data is exploding at 28% annually, but 80% is trapped in PDFs, Slack channels, Google Docs, and messy shared drives. Engineers and managers spend nearly a third of their day just searching for lost files!\n\n"
            "[Prof. Peter] When you consume massive quantities of unindexed, low-signal data without synthesis, your mind suffers from cognitive obesity. You become exhausted, unable to discern vital strategic signals.\n\n"
            "[TA Sarah] We need an intelligent filtering mechanism that transforms this chaotic sea of data into structured, actionable wisdom.\n\n"
            "[TA James] That is exactly what Google NotebookLM and modern RAG pipelines achieve on Slide 4!"
        ),
        "koreanGuide": {
            "summary": "정보 비만의 위기: 비정형 데이터의 폭증과 지식 근로자의 인지적 고갈 실태",
            "points": [
                "엔터프라이즈 데이터의 80%가 검색 불가능한 비정형 PDF, 문서, 슬랙 메시지에 고립",
                "지식 근로자가 매일 2.5시간 이상을 내부 문서와 자료 검색에 낭비",
                "무분별한 정보 수집은 인지적 피로를 유발하며 핵심 전략 신호를 놓치게 만듦"
            ],
            "tips": "수강생들이 겪는 실무적인 문서 검색 스트레스를 3인의 대화로 공감대 형성하세요."
        },
        "keyTerms": [
            {
                "term": "Information Obesity",
                "def": "The cognitive paralysis resulting from the overwhelming accumulation of unstructured, unverified data.",
                "defKo": "정보 비만 (인지 과부하)"
            },
            {
                "term": "Unstructured Data Silo",
                "def": "Isolated repositories of documents and messages lacking uniform metadata and centralized semantic searchability.",
                "defKo": "비정형 데이터 사일로"
            }
        ]
    },
    # Slide 4: The Grounded Frontier
    {
        "num": 4,
        "type": "content",
        "title": "THE GROUNDED FRONTIER: ZERO HALLUCINATION",
        "subtitle": "Anchoring generative intelligence strictly inside your private, verified knowledge boundary",
        "points": [
            "Zero-Hallucination Architecture: The LLM is strictly prohibited from answering outside provided context.",
            "Source-First Reasoning: Every sentence in the generated output is linked to a cryptographic source pointer.",
            "Private Enclave: User data is processed in a secure sandbox without external model training leakage."
        ],
        "script": (
            "[Prof. Peter] Slide 4 introduces \"THE GROUNDED FRONTIER: ZERO HALLUCINATION.\" Sarah, what is the core architectural principle here?\n\n"
            "[TA Sarah] The core rule is simple yet revolutionary: the model is explicitly forbidden from pulling ungrounded facts from its pre-training weights! It must synthesize answers ONLY from the verified source documents you provide.\n\n"
            "[TA James] Think of it as placing an unbreakable sandbox around the model's reasoning engine. If the answer is not inside your uploaded PDFs or Google Docs, the model returns: 'Based on the provided sources, this information is not available.' No guessing allowed!\n\n"
            "[Prof. Peter] That simple behavioral constraint restores absolute trust in enterprise AI.\n\n"
            "[TA Sarah] Let us deconstruct why legacy chatbots act like lying parrots on Slide 5."
        ),
        "koreanGuide": {
            "summary": "그라운디드 프론티어: 제로 환각(Zero Hallucination)과 프라이빗 지식 경계 설정",
            "points": [
                "프리트레이닝 가중치 기반의 근거 없는 추론을 차단하고 오직 제공된 문서 내에서만 답변",
                "문서에 없는 내용은 지어내지 않고 '제공된 출처에 없음'을 명확히 고지",
                "사용자 데이터가 외부 학습에 유출되지 않는 안전한 프라이빗 샌드박스 보장"
            ],
            "tips": "사라 조교가 그라운딩의 원리를 명확히 짚고, 제임스가 샌드박스 격리 개념을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Grounded Reasoning",
                "def": "An inference mode where generation is strictly conditioned on explicitly retrieved source passages.",
                "defKo": "근거 기반 추론"
            },
            {
                "term": "Zero-Hallucination Boundary",
                "def": "A strict system constraint forcing the model to decline answering when verified factual evidence is missing.",
                "defKo": "무환각 경계 (엄격한 사실 제약)"
            }
        ]
    },
    # Slide 5: Deconstructing the Probabilistic Parrot
    {
        "num": 5,
        "type": "comparison",
        "title": "DECONSTRUCTING THE PROBABILISTIC PARROT",
        "subtitle": "Contrasting ungrounded generative LLMs with grounded knowledge assistants",
        "leftCard": {
            "tag": "VANILLA LLM (PARROT)",
            "title": "Stochastic Guessing",
            "points": [
                "Generates text based on broad statistical web training data.",
                "Confidently fabricates non-existent citations, dates, and numbers.",
                "Cannot explain WHERE a specific factual claim originated."
            ]
        },
        "rightCard": {
            "tag": "NOTEBOOKLM / RAG",
            "title": "Grounded Scholar",
            "points": [
                "Generates text strictly anchored to user-uploaded source files.",
                "Every factual claim includes an inline clickable citation link.",
                "Declares explicit uncertainty if facts are absent from sources."
            ]
        },
        "script": (
            "[TA Sarah] Look at Slide 5: \"DECONSTRUCTING THE PROBABILISTIC PARROT.\" On the left, we have the vanilla consumer chatbot.\n\n"
            "[TA James] It acts like a brilliant but reckless parrot. It read the entire public internet, but it cannot tell you where it learned a specific fact, and when pressured, it invents fake journal citations that look 100% real!\n\n"
            "[Prof. Peter] On the right, we have the Grounded Scholar—powered by Google NotebookLM and RAG. It acts like a meticulous research assistant who sits with your exact binder of documents, reads every line, and provides exact page citations for every single claim.\n\n"
            "[TA Sarah] If a claim cannot be verified in the source binder, the Grounded Scholar refuses to invent it.\n\n"
            "[TA James] Let us inspect the absolute boundary of grounded truth on Slide 6!"
        ),
        "koreanGuide": {
            "summary": "확률적 앵무새 vs 그라운디드 학자: 비근거 LLM과 검색 증강 지능의 비교",
            "points": [
                "일반 챗봇: 인터넷 전체를 읽었으나 출처를 입증하지 못하고 가짜 논문 인용을 그럴듯하게 날조",
                "그라운디드 RAG(NotebookLM): 사용자가 제공한 문서 바인더만을 철저히 분석하고 클릭 가능한 인용 제공",
                "출처 불명확 시 스스로 불확실성을 인정하는 학자적 정직성 구현"
            ],
            "tips": "제임스 조교의 위트 있는 '앵무새' 비유와 피터 교수의 '학자' 비유를 대비해 흥미를 유발하세요."
        },
        "keyTerms": [
            {
                "term": "Stochastic Parrot",
                "def": "A critical metaphor for large language models that mimic linguistic patterns without comprehension or factual grounding.",
                "defKo": "확률적 앵무새 (모방형 언어 모델)"
            },
            {
                "term": "Inline Citation",
                "def": "A verifiable reference embedded directly in text pointing to the exact source chunk or document page.",
                "defKo": "인라인 인용 (본문 내 출처 링크)"
            }
        ]
    },
    # Slide 6: Grounded Truth: The Absolute Boundary
    {
        "num": 6,
        "type": "content",
        "title": "GROUNDED TRUTH: THE ABSOLUTE BOUNDARY",
        "subtitle": "Architecting an unbreachable wall between pre-trained language fluency and factual knowledge",
        "points": [
            "Decoupled Architecture: LLM provides linguistic grammar; private database provides factual truth.",
            "Context Window Containment: System prompt injects retrieved chunks into isolated system boundaries.",
            "Verifiable Truth: Every answer can be audited against original PDF page numbers and paragraph hashes."
        ],
        "script": (
            "[Prof. Peter] Slide 6 illustrates \"GROUNDED TRUTH: THE ABSOLUTE BOUNDARY.\" In classical computing, code and data are strictly separated. In modern RAG, we apply the exact same wisdom!\n\n"
            "[TA Sarah] Exactly, Professor! We decouple the LLM's language fluency from its memory. We use the model purely as a linguistic processor, while our private database serves as the sole source of truth.\n\n"
            "[TA James] Look at how that works in production: the user prompt pulls 5 relevant chunks from Google Drive, injects them into the prompt container, and commands the model: 'Answer using ONLY these 5 chunks.' The model's internet memories are completely muted!\n\n"
            "[TA Sarah] This guarantees that every answer can be audited down to the exact paragraph hash and PDF page number.\n\n"
            "[Prof. Peter] Let us examine the immense power of verifiable citations on Slide 7."
        ),
        "koreanGuide": {
            "summary": "그라운디드 진실: 언어 처리 능력과 지식 데이터베이스의 엄격한 분리 아키텍처",
            "points": [
                "언어 모델의 역할 제한: 지식 기억 장치가 아닌 오직 언어적 문법/추론 처리기로만 활용",
                "데이터 주권: 프라이빗 데이터베이스 및 구글 드라이브 문서가 유일한 진실의 원천(Single Source of Truth)",
                "프롬프트 컨테이너 격리를 통해 외부 인터넷 기억의 개입을 완벽히 차단"
            ],
            "tips": "사라 조교가 코드와 데이터의 분리라는 전통 컴퓨터 과학 원리를 RAG에 적용해 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Decoupled Fluency",
                "def": "Separating a model's natural language comprehension abilities from its stored factual knowledge base.",
                "defKo": "언어 능력과 지식의 분리"
            },
            {
                "term": "Source of Truth",
                "def": "The authoritative data repository designated as the sole trusted basis for factual generation.",
                "defKo": "진실의 단일 원천 (신뢰 기준점)"
            }
        ]
    },
    # Slide 7: The Power of Verifiable Citations
    {
        "num": 7,
        "type": "content",
        "title": "THE POWER OF VERIFIABLE CITATIONS",
        "subtitle": "Clickable footnotes that eliminate audit friction and build enterprise credibility",
        "points": [
            "Instant Verification: Hovering or clicking a citation instantly displays the exact source snippet.",
            "Eliminating Audit Lag: Legal and compliance teams verify 100-page reports in minutes rather than days.",
            "Cryptographic Traceability: Source chunks are tagged with immutable SHA-256 document identifiers."
        ],
        "script": (
            "[TA Sarah] Slide 7 demonstrates \"THE POWER OF VERIFIABLE CITATIONS.\" In Google NotebookLM, every synthesized response contains interactive numerical citations.\n\n"
            "[TA James] When you click citation [1], NotebookLM doesn't just give you a filename—it opens the original PDF, highlights the exact three sentences in yellow, and shows the timestamp! That transforms auditing from a nightmare into a 2-second click.\n\n"
            "[Prof. Peter] Think about what this means for enterprise governance. In legal discovery, financial auditing, or scientific peer review, trust is not built on smooth words; trust is built on verifiable evidence!\n\n"
            "[TA Sarah] When an AI system can prove every word it speaks, human architects can deploy it with total confidence.\n\n"
            "[TA James] Let us contrast the operational workflows of chatbots versus grounded assistants on Slide 8!"
        ),
        "koreanGuide": {
            "summary": "검증 가능한 인용(Citations)의 힘: 감사 시간 단축과 기업 신뢰성 구축",
            "points": [
                "클릭 한 번으로 원본 PDF의 해당 문단과 페이지를 노란색 하이라이트로 즉시 확인",
                "법률 검토, 금융 감사, 학술 연구 시 수일이 걸리던 진위 검증을 수 분 내로 단축",
                "문서 청크별 SHA-256 해시 태깅을 통한 암호화된 추적 가능성 확보"
            ],
            "tips": "제임스 조교가 실제 감사 현장에서 인용 링크 클릭 기능이 주는 생산성 혁신을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Verifiable Citation",
                "def": "An interactive citation linking model generation directly to the exact source text passage and visual coordinate.",
                "defKo": "검증 가능한 인용 (출처 직결 링크)"
            },
            {
                "term": "Audit Friction",
                "def": "The labor-intensive delay and difficulty required for humans to manually verify the accuracy of AI-generated claims.",
                "defKo": "감사 저항 (검증 지연 비용)"
            }
        ]
    },
    # Slide 8: Comparing the Landscapes
    {
        "num": 8,
        "type": "comparison",
        "title": "COMPARING THE LANDSCAPES: PARROT VS. ASSISTANT",
        "subtitle": "Evaluating speed, hallucinations, hallucination risk, and enterprise auditability",
        "leftCard": {
            "tag": "REACTIVE CHATBOT",
            "title": "Ungrounded Generic Chat",
            "points": [
                "Hallucination Rate: High (15% - 25% on niche data).",
                "Audit Trail: None (black box text generation).",
                "Privacy Risk: High (prompts may leak into public training corpora).",
                "Business Use: Brainstorming, drafting fiction, casual chat."
            ]
        },
        "rightCard": {
            "tag": "GROUNDED KNOWLEDGE FACTORY",
            "title": "NotebookLM / Private RAG",
            "points": [
                "Hallucination Rate: Near Zero (< 0.5% with strict citations).",
                "Audit Trail: 100% Cryptographic citation mapping.",
                "Privacy Risk: Zero (data isolated in enterprise boundary).",
                "Business Use: Executive synthesis, legal analysis, research."
            ]
        },
        "script": (
            "[TA Sarah] Slide 8 presents \"COMPARING THE LANDSCAPES: PARROT VS. ASSISTANT.\" Look at the stark contrast in metrics.\n\n"
            "[TA James] A generic public chatbot has a 15% to 25% hallucination rate when answering complex proprietary questions. In contrast, a grounded RAG factory like NotebookLM drops hallucination below 0.5% by enforcing strict citation constraints!\n\n"
            "[Prof. Peter] Notice also the privacy dimension. Public chat tools often reserve rights to retrain models on your confidential prompts. In our enterprise RAG architecture, your data stays within an isolated enterprise boundary.\n\n"
            "[TA Sarah] That difference is what separates a toy entertainment tool from a mission-critical enterprise engine.\n\n"
            "[TA James] Let us launch an interactive poll on Slide 9 to see how our students experience this challenge!"
        ),
        "koreanGuide": {
            "summary": "풍경 비교: 수동적 챗봇 vs 프라이빗 지식 공장의 성능 및 보안 지표 비교",
            "points": [
                "환각률 비교: 퍼블릭 챗봇 15~25% vs 그라운디드 RAG 0.5% 미만",
                "감사 추적성: 블랙박스 텍스트 생성 vs 100% 암호화 인용 매핑",
                "데이터 프라이버시: 공개 학습 데이터 유출 위험 vs 엔터프라이즈 테넌트 격리"
            ],
            "tips": "표와 수치를 바탕으로 피터 교수와 조교들이 엔터프라이즈 환경에서의 불가결한 선택임을 명확히 합니다."
        },
        "keyTerms": [
            {
                "term": "Hallucination Rate",
                "def": "The statistical frequency at which a generative model fabricates incorrect or unverified factual statements.",
                "defKo": "환각 발생률"
            },
            {
                "term": "Enterprise Tenant Boundary",
                "def": "A dedicated, logically isolated cloud perimeter ensuring enterprise data is never accessed or trained upon externally.",
                "defKo": "엔터프라이즈 테넌트 격리 경계"
            }
        ]
    },
    # Slide 9: Interactive Student Poll
    {
        "num": 9,
        "type": "poll",
        "title": "📨 INTERACTIVE STUDENT POLL",
        "subtitle": "How many hours do you spend verifying AI outputs or searching through unorganized documents?",
        "pollOptions": [
            "Option A: Under 2 hours weekly (I have clean, indexed document vaults)",
            "Option B: 2 to 5 hours weekly (I frequently double-check AI hallucinations)",
            "Option C: 5 to 10 hours weekly (I drown in unindexed PDFs and lost files)",
            "Option D: Over 10 hours weekly (I spend half my working life hunting for files)"
        ],
        "script": (
            "[Prof. Peter] Slide 9 is our \"INTERACTIVE STUDENT POLL.\" Take out your mobile devices or open your course dashboard and vote right now!\n\n"
            "[TA Sarah] The question is: \"How many hours do you spend every week verifying AI outputs or searching through unorganized documents?\"\n\n"
            "[TA James] Option A: Under 2 hours weekly. Option B: 2 to 5 hours. Option C: 5 to 10 hours. Or Option D: Over 10 hours weekly—essentially losing a full working day every week just searching for files and fixing AI lies!\n\n"
            "[TA Sarah] The live results are streaming in on our monitor, and the distribution is eye-opening.\n\n"
            "[Prof. Peter] Let us analyze the poll results and uncover the root bottleneck on Slide 10."
        ),
        "koreanGuide": {
            "summary": "실시간 수강생 설문: 문서 검색 및 AI 출력 검증에 소모되는 주간 시간 측정",
            "points": [
                "수강생 실시간 참여를 통한 문서 관리 및 환각 검증 스트레스 정량화",
                "주당 5~10시간 이상을 파일 검색과 검증에 허비하는 현실 환기",
                "비동기 RAG 파이프라인 도입을 통한 시간 구속의 필요성 부각"
            ],
            "tips": "사라와 제임스 조교가 실시간 투표를 유도하고 흥미로운 진행 톤을 유지하세요."
        },
        "keyTerms": [
            {
                "term": "Verification Overhead",
                "def": "The time and cognitive labor required by humans to cross-check AI responses against primary sources.",
                "defKo": "검증 오버헤드 (진위 확인 부담)"
            },
            {
                "term": "Interactive Polling",
                "def": "A pedagogical mechanism engaging global students in real-time architectural self-assessment.",
                "defKo": "실시간 상호작용 설문"
            }
        ]
    },
    # Slide 10: Poll Analysis & Insight
    {
        "num": 10,
        "type": "content",
        "title": "POLL ANALYSIS & COGNITIVE DRAG",
        "subtitle": "Over 68% of knowledge workers waste 6+ hours weekly on manual search and fact-checking",
        "points": [
            "Survey Insight: 68% of students select Options C & D (wasting 6 to 12+ hours weekly).",
            "The Cost of Verification: Blind AI outputs force humans into exhausting manual cross-checking loops.",
            "The RAG Remedy: Automated semantic indexing and inline citations reclaim over 80% of wasted time."
        ],
        "script": (
            "[TA Sarah] Slide 10 reveals the \"POLL ANALYSIS & COGNITIVE DRAG.\" Over 68% of our global cohort voted for Options C and D!\n\n"
            "[TA James] That means the majority of professionals waste between 6 and 12 hours every single week! That is more than 300 to 500 hours a year lost to manual search and fear of AI hallucinations.\n\n"
            "[Prof. Peter] When you cannot trust your AI tool, you become its full-time babysitter! You spend more time checking its work than it took to generate the text in the first place.\n\n"
            "[TA Sarah] By building a private knowledge factory with grounded citations, that verification friction drops to near zero.\n\n"
            "[TA James] Let us examine our first real-world enterprise case study on Slide 11 to see this in action!"
        ),
        "koreanGuide": {
            "summary": "설문 결과 분석: 연간 300~500시간의 검증 손실과 RAG 기반 해결책",
            "points": [
                "수강생의 68%가 매주 6시간 이상을 단순 파일 찾기와 AI 생성물 진위 확인에 소모",
                "신뢰할 수 없는 AI는 인간을 'AI 베이비시터'로 전락시켜 생산성을 심각하게 저해",
                "NotebookLM 기반 RAG 팩토리를 통해 검증 시간을 80% 이상 단축하고 본질적 연구에 집중"
            ],
            "tips": "피터 교수가 'AI 베이비시터'라는 비유를 사용하여 수강생들에게 강한 동기를 부여합니다."
        },
        "keyTerms": [
            {
                "term": "Cognitive Drag",
                "def": "The mental fatigue and loss of momentum resulting from constant friction in locating and validating information.",
                "defKo": "인지적 저항 (검증 피로)"
            },
            {
                "term": "Verification Friction",
                "def": "The resistance encountered when checking untrusted AI outputs against primary authoritative records.",
                "defKo": "검증 마찰 비용"
            }
        ]
    },
    # Slide 11: Case Study 1: Wall Street Equity Research Triage
    {
        "num": 11,
        "type": "casestudy",
        "title": "CASE STUDY 1: WALL STREET EQUITY RESEARCH TRIAGE",
        "subtitle": "How a tier-1 investment bank compressed 10-hour earnings call synthesis into 4 minutes",
        "company": "Wall Street Tier-1 Equity Research Group",
        "problem": "Senior analysts spent 10+ hours per company manually parsing 200-page 10-K filings, earnings transcripts, and SEC disclosures, missing market opening deadlines.",
        "solution": "Deployed a private Google NotebookLM & Gemini RAG pipeline ingesting 50 filings simultaneously with strict citation anchoring and instant financial table extraction.",
        "impact": "10-hour manual analysis compressed into 4.2 minutes; 100% factual accuracy audited via inline citations; zero compliance violations over 12 months.",
        "script": (
            "[Prof. Peter] Slide 11 presents \"CASE STUDY 1: WALL STREET EQUITY RESEARCH TRIAGE.\" Look at this landmark enterprise implementation.\n\n"
            "[TA Sarah] A top-tier Wall Street investment bank faced an impossible bottleneck: during earnings season, analysts had to parse dozens of 200-page 10-K filings, financial disclosures, and audio transcripts. It took 10 hours per company to write an equity briefing!\n\n"
            "[TA James] They couldn't use public ChatGPT because of strict SEC compliance and hallucination risk. So they deployed a private RAG knowledge factory using NotebookLM and Gemini 3.5 Flash.\n\n"
            "[Prof. Peter] Look at the results on screen: the 10-hour analysis pipeline was compressed into 4.2 minutes! Every single revenue number, EBIT margin, and guidance quote had a clickable citation linked directly to the SEC filing page.\n\n"
            "[TA Sarah] The compliance team audited every briefing in under 5 minutes with zero regulatory violations.\n\n"
            "[TA James] Now let us open Part 2 and look inside the mechanical engine room of RAG on Slide 12!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 1: 월스트리트 증권 리서치 10시간 분석의 4분 압축 기적",
            "points": [
                "문제 상황: 실적 발표 시즌마다 200페이지 10-K 공시 서류 분석에 애널리스트당 10시간 이상 소모",
                "솔루션: SEC 규제 준수 및 제로 환각을 위한 NotebookLM & Gemini RAG 사설 파이프라인 구축",
                "성과: 10시간 작업을 4.2분으로 단축, 인라인 인용을 통해 감사 5분 내 완료 및 규정 위반 0건"
            ],
            "tips": "사라 조교와 제임스 조교가 현장감 있게 금융권의 실제 문제와 해결 성과를 숫자로 전달합니다."
        },
        "keyTerms": [
            {
                "term": "SEC 10-K Filing",
                "def": "A comprehensive annual financial report required by the U.S. Securities and Exchange Commission detailing corporate performance.",
                "defKo": "SEC 10-K 사업보고서"
            },
            {
                "term": "Synthesis Compression",
                "def": "The radical acceleration of distilling massive document corpora into actionable insights without losing accuracy.",
                "defKo": "합성 압축률 (분석 속도 혁신)"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 12: Part 2 Section Divider
    {
        "num": 12,
        "type": "section",
        "title": "PART 2: SYSTEM ARCHITECTURE: INSIDE THE RAG ENGINE",
        "subtitle": "Deconstructing the 3-step mechanics: ingestion, semantic vectorization, and prompt augmentation",
        "script": (
            "[TA Sarah] Look at Slide 12: \"PART 2: SYSTEM ARCHITECTURE: INSIDE THE RAG ENGINE.\" Now we open the hood and explore the exact technical pipeline!\n\n"
            "[Prof. Peter] In Part 2, we move from conceptual benefits to rigorous software engineering. How does unstructured text transform into high-dimensional vector embeddings, and how does the model retrieve the exact sentence in 50 milliseconds?\n\n"
            "[TA James] We will break down the entire 3-step pipeline: Ingestion and smart chunking, Semantic Vectorization via embedding models, and Prompt Augmentation in the context window.\n\n"
            "[TA Sarah] We will also explore the revolutionary Audio Overview engine and dual-memory persistence.\n\n"
            "[Prof. Peter] Let us examine the Triad of RAG Architecture on Slide 13!"
        ),
        "koreanGuide": {
            "summary": "Part 2 섹션 전환: RAG 시스템의 3단계 내부 공학 아키텍처 완전 분해",
            "points": [
                "3단계 핵심 메커니즘: 데이터 수집 및 청킹 ➔ 고차원 벡터화 ➔ 프롬프트 증강 및 생성",
                "초저지연 검색: 50ms 이내에 수만 페이지에서 정확한 문장을 찾아내는 임베딩 원리",
                "오디오 오버뷰(Audio Overview)와 듀얼 메모리 엔진의 결합"
            ],
            "tips": "피터 교수가 공학적 엄밀성을 선언하고 제임스 조교가 3단계 파이프라인의 명확한 흐름을 제시합니다."
        },
        "keyTerms": [
            {
                "term": "Vector Retrieval Engine",
                "def": "A specialized database subsystem locating relevant document chunks using high-dimensional cosine similarity.",
                "defKo": "벡터 검색 엔진"
            },
            {
                "term": "Pipeline Triad",
                "def": "The fundamental 3-stage RAG architecture comprising Ingestion, Vectorization, and Prompt Augmentation.",
                "defKo": "RAG 3계층 파이프라인 트라이어드"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 13: The Triad of RAG System Architecture
    {
        "num": 13,
        "type": "content",
        "title": "THE TRIAD OF RAG SYSTEM ARCHITECTURE",
        "subtitle": "The end-to-end pipeline connecting raw enterprise data to grounded generative intelligence",
        "points": [
            "Stage 1: Ingestion & Smart Chunking (Recursive parsing, OCR, multi-modal audio/video conversion).",
            "Stage 2: Vectorization & Indexing (768-dim embeddings stored in HNSW vector indices).",
            "Stage 3: Retrieval & Prompt Augmentation (Cosine similarity match injected into Gemini 3.5 Flash context)."
        ],
        "script": (
            "[Prof. Peter] Slide 13 diagrams \"THE TRIAD OF RAG SYSTEM ARCHITECTURE.\" This is the master blueprint for every private knowledge factory.\n\n"
            "[TA Sarah] Examine Stage 1 on the left: \"INGESTION & SMART CHUNKING.\" Raw files—PDFs, Google Docs, spreadsheets, YouTube URLs, and MP3 recordings—are ingested, sanitized, and segmented into semantic paragraphs.\n\n"
            "[TA James] Look at Stage 2 in the center: \"VECTORIZATION & INDEXING.\" Each chunk is converted into a 768-dimensional dense vector using Google's text-embedding models and stored in an indexed vector database like Vertex AI Vector Search.\n\n"
            "[TA Sarah] And Stage 3 on the right: \"RETRIEVAL & AUGMENTATION.\" When the user asks a question, the system finds the top 5 most similar vectors, injects them into Gemini 3.5 Flash, and generates a citation-backed response in under 400 milliseconds!\n\n"
            "[Prof. Peter] Let us inspect Step 1 in detail on Slide 14."
        ),
        "koreanGuide": {
            "summary": "RAG 시스템 아키텍처 3계층 트라이어드: 수집, 벡터화, 증강의 엔드투엔드 흐름",
            "points": [
                "1단계 수집: PDF, 구글 문서, 스프레드시트, 유튜브, 오디오를 의미 단위 문단으로 스마트 분할",
                "2단계 벡터화: 768차원 고밀도 벡터 임베딩 생성 및 초고속 HNSW 벡터 인덱스 적재",
                "3단계 증강: 코사인 유사도 매칭으로 최적 청크를 추출하여 제미나이 컨텍스트에 주입 후 400ms 내 응답"
            ],
            "tips": "사라 조교가 1단계와 3단계를, 제임스 조교가 2단계 벡터 인덱스를 기술적으로 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Smart Semantic Chunking",
                "def": "Splitting documents based on grammatical paragraph boundaries and topic transitions rather than arbitrary character counts.",
                "defKo": "스마트 의미 단위 청킹"
            },
            {
                "term": "Cosine Similarity",
                "def": "A mathematical metric measuring the directional similarity between two high-dimensional semantic vectors.",
                "defKo": "코사인 유사도 (벡터 의미 유사성)"
            }
        ]
    },
    # Slide 14: Step 1: Multi-Format Ingestion & Chunking
    {
        "num": 14,
        "type": "content",
        "title": "STEP 1: MULTI-FORMAT INGESTION & CHUNKING",
        "subtitle": "Handling PDFs, Docs, audio, video, and web links with semantic boundary preservation",
        "points": [
            "Recursive Splitting: Preserving header hierarchies (H1/H2/H3) and markdown tables without truncation.",
            "Multi-Modal Extraction: Automatic speech-to-text for audio/video and OCR for scanned documents.",
            "Chunk Metadata: Stamping each chunk with document ID, page number, author, and timestamp."
        ],
        "script": (
            "[TA Sarah] Slide 14 covers \"STEP 1: MULTI-FORMAT INGESTION & CHUNKING.\" In legacy RAG, people chopped text every 500 characters blindly.\n\n"
            "[TA James] That was a disaster! If you chop a sentence in half, or split a financial table down the middle, the embedding model has no idea what the numbers mean! In our architecture, we use recursive semantic splitting that preserves table structures and header hierarchies.\n\n"
            "[Prof. Peter] Furthermore, modern ingestion is natively multi-modal. Google NotebookLM takes an hour-long audio lecture, a 50-page PDF, a Google Sheet, and a YouTube link, transcribing and normalizing them into a unified knowledge fabric!\n\n"
            "[TA Sarah] Each chunk is stamped with rich metadata—page number, timestamp, and document UUID—ensuring total auditability.\n\n"
            "[TA James] Let us see how these chunks become mathematical coordinates on Slide 15!"
        ),
        "koreanGuide": {
            "summary": "1단계: 멀티 포맷 수집 및 의미 보존 청킹 기법",
            "points": [
                "단순 글자 수 자르기의 한계: 문맥 파괴 및 표 데이터 손실 방지를 위한 재귀적 의미 분할",
                "멀티모달 통합: PDF, 구글 시트, 유튜브 영상, 녹음 음성을 단일 지식망으로 표준화",
                "메타데이터 스탬핑: 페이지 번호, 작성자, 문서 UUID를 청크마다 부여하여 추적성 확보"
            ],
            "tips": "제임스 조교가 무지성 글자 자르기(Blind Chunker)의 위험성을 지적하고 스마트 청킹의 중요성을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Recursive Chunking",
                "def": "An advanced text segmentation algorithm dividing text hierarchically along natural syntactic boundaries.",
                "defKo": "재귀적 의미 분할"
            },
            {
                "term": "Chunk Metadata",
                "def": "Contextual attributes (page numbers, section headers, timestamps) attached to text chunks for accurate retrieval.",
                "defKo": "청크 메타데이터 (출처 추적 속성)"
            }
        ]
    },
    # Slide 15: Step 2: Semantic Vectorization
    {
        "num": 15,
        "type": "content",
        "title": "STEP 2: SEMANTIC VECTORIZATION & EMBEDDINGS",
        "subtitle": "Mapping textual and conceptual meaning into 768-dimensional mathematical coordinates",
        "points": [
            "Vector Space Geometry: Words with similar conceptual meanings cluster together in vector space.",
            "Sub-Millisecond Search: Hierarchical Navigable Small World (HNSW) indexing achieves < 5ms lookup.",
            "Cross-Lingual Matching: English queries retrieve Korean or Spanish document chunks seamlessly."
        ],
        "script": (
            "[Prof. Peter] Slide 15 explores \"STEP 2: SEMANTIC VECTORIZATION & EMBEDDINGS.\" How does a machine understand that 'King' and 'Queen' share a conceptual relationship?\n\n"
            "[TA Sarah] Through vector geometry! An embedding model projects text into a high-dimensional vector space—typically 768 or 1,536 dimensions. Sentences with similar meanings are placed physically close to each other.\n\n"
            "[TA James] And in production, we index these vectors using algorithms like HNSW—Hierarchical Navigable Small World graphs. Even across 10 million document pages, finding the 5 closest paragraphs takes under 5 milliseconds!\n\n"
            "[TA Sarah] What is amazing is cross-lingual retrieval: you can ask a question in Korean, and the vector engine instantly retrieves the relevant English technical whitepaper paragraph because their semantic coordinates align!\n\n"
            "[Prof. Peter] Let us see how retrieved vectors feed into model generation on Slide 16."
        ),
        "koreanGuide": {
            "summary": "2단계: 의미론적 벡터화 및 고차원 임베딩 검색 원리",
            "points": [
                "벡터 공간 기하학: 768차원 고차원 공간에 단어와 문장의 의미적 관계를 좌표로 배치",
                "HNSW 인덱싱: 1,000만 페이지의 방대한 문서에서도 5ms 이내에 유사 청크를 탐색하는 초고속 알고리즘",
                "다국어 교차 검색: 한국어로 질문해도 의미 공간이 일치하는 영문/일문 원천 문서를 정확히 인출"
            ],
            "tips": "사라 조교가 기하학적 임베딩을 시각적으로 설명하고 제임스가 HNSW의 속도를 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Dense Vector Embedding",
                "def": "A continuous numerical vector representation capturing the semantic meaning of a text segment.",
                "defKo": "고밀도 벡터 임베딩"
            },
            {
                "term": "HNSW (Hierarchical Navigable Small World)",
                "def": "A state-of-the-art graph-based indexing algorithm enabling logarithmic-time approximate nearest neighbor search.",
                "defKo": "HNSW 초고속 근사 최근접 인덱스"
            }
        ]
    },
    # Slide 16: Step 3: Prompt Augmentation & Generation
    {
        "num": 16,
        "type": "content",
        "title": "STEP 3: PROMPT AUGMENTATION & GENERATION",
        "subtitle": "Synthesizing retrieved source chunks with strict system instructions in Gemini 3.5 Flash",
        "points": [
            "Context Packaging: Injecting retrieved snippets with explicit source indices into the prompt payload.",
            "Constrained Reasoning: Enforcing system prompt guardrails ('Cite [1], [2] for every factual statement').",
            "Fast Sub-400ms Generation: Gemini 3.5 Flash synthesizes clean, cited prose with zero latency lag."
        ],
        "script": (
            "[TA Sarah] Slide 16 completes the loop: \"STEP 3: PROMPT AUGMENTATION & GENERATION.\"\n\n"
            "[TA James] Once the vector engine returns the top 5 chunks, our orchestration daemon packages them into a structured prompt envelope. We tag Chunk 1 as Source [1], Chunk 2 as Source [2], and attach the strict instruction: 'Answer the user query using ONLY Sources [1] through [5], adding inline brackets after every fact.'\n\n"
            "[Prof. Peter] Then Gemini 3.5 Flash executes the synthesis. Because Gemini Flash has sub-400 millisecond latency, the entire process—query embedding, vector search, and token generation—completes in less than one second!\n\n"
            "[TA Sarah] The user receives an executive answer with verifiable footnotes that can be audited immediately.\n\n"
            "[TA James] Let us examine how our dual-memory engine overcomes conversational amnesia on Slide 17!"
        ),
        "koreanGuide": {
            "summary": "3단계: 프롬프트 증강 및 제미나이 3.5 플래시 기반 생성",
            "points": [
                "컨텍스트 패키징: 추출된 5개 청크에 [출처 1], [출처 2] 태그를 부여하여 프롬프트에 주입",
                "엄격한 제약 지시: '오직 제공된 출처만을 인용하여 답변하고 문장마다 인라인 출처 표기' 명령",
                "초저지연 생성: 제미나이 3.5 플래시의 400ms 미만 속도로 전체 검색-생성 과정을 1초 내 완수"
            ],
            "tips": "제임스 조교가 프롬프트 엔벨로프의 구체적인 구조를 예시와 함께 생생히 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Prompt Augmentation",
                "def": "The process of injecting dynamically retrieved source chunks directly into an LLM's inference prompt.",
                "defKo": "프롬프트 증강 (동적 문맥 주입)"
            },
            {
                "term": "Source Tagging",
                "def": "Assigning structured numerical identifiers to source passages to facilitate precise inline citations.",
                "defKo": "출처 태깅 (인용 식별자 부여)"
            }
        ]
    },
    # Slide 17: Overcoming Amnesia: Dual-Memory Engine
    {
        "num": 17,
        "type": "content",
        "title": "OVERCOMING AMNESIA: DUAL-MEMORY ENGINE",
        "subtitle": "Harmonizing short-term conversational context with persistent long-term vector vaults",
        "points": [
            "Short-Term Working Memory: In-session active scratchpad storing the last 20 conversational turns.",
            "Long-Term Semantic Memory: Persistent vector database containing hundreds of uploaded books and PDFs.",
            "Dynamic Reconciliation: Seamlessly merging ongoing dialogue state with deep historical archives."
        ],
        "script": (
            "[Prof. Peter] Slide 17 addresses a classic challenge in artificial intelligence: \"OVERCOMING AMNESIA: DUAL-MEMORY ENGINE.\"\n\n"
            "[TA Sarah] In vanilla chat sessions, if you close your laptop, the model suffers total amnesia. It forgets who you are, what project you worked on yesterday, and what documents you analyzed last month.\n\n"
            "[TA James] Our Dual-Memory Engine solves this through architectural separation: Short-Term Memory handles the immediate active conversation buffer, while Long-Term Semantic Memory stores years of research papers, PDFs, and code repositories in a permanent vector index!\n\n"
            "[Prof. Peter] When the user asks a question, the agent dynamically queries both: reconciling current conversational intent with years of historical institutional knowledge.\n\n"
            "[TA Sarah] Let us see how multi-format synthesis unlocks cross-document breakthroughs on Slide 18."
        ),
        "koreanGuide": {
            "summary": "대화 기억상실 극복: 단기 작업 메모리와 장기 벡터 메모리의 듀얼 엔진",
            "points": [
                "단기 작업 메모리: 현재 진행 중인 20턴의 대화 흐름과 사용자 의도를 유지하는 스크래치패드",
                "장기 벡터 메모리: 수년간 축적된 수백 권의 책, 논문, 프로젝트 기록이 영구 보관된 사설 벡터 금고",
                "동적 융합: 현재의 대화 맥락과 과거의 깊은 지식 아카이브를 결합하여 답변 생성"
            ],
            "tips": "사라 조교가 챗봇의 기억 상실 문제를 짚고, 제임스가 듀얼 메모리 아키텍처의 구조를 명확히 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Dual-Memory Engine",
                "def": "An architectural pattern combining short-term conversational context with long-term vector indexing.",
                "defKo": "듀얼 메모리 엔진 (이중 기억 체계)"
            },
            {
                "term": "Semantic Persistence",
                "def": "The permanent storage and retrieval capability of institutional knowledge across multiple sessions.",
                "defKo": "의미론적 영속성"
            }
        ]
    },
    # Slide 18: The Magic of Multi-Format Synthesis
    {
        "num": 18,
        "type": "content",
        "title": "THE MAGIC OF MULTI-FORMAT SYNTHESIS",
        "subtitle": "Cross-referencing spreadsheets, PDFs, audio transcripts, and slides in a single prompt",
        "points": [
            "Cross-Modal Fusion: Correlating financial tables in Excel with CEO audio comments and PDF disclosures.",
            "Discrepancy Detection: Automatically flagging contradictions between verbal interviews and written reports.",
            "Unified Knowledge Graph: Connecting disparate media formats into a cohesive relational mental model."
        ],
        "script": (
            "[TA Sarah] Slide 18 illustrates \"THE MAGIC OF MULTI-FORMAT SYNTHESIS.\" In real life, knowledge does not live in a single clean PDF.\n\n"
            "[TA James] Exactly! You have an Excel spreadsheet with budget numbers, a 60-minute recorded audio meeting, a 40-slide presentation deck, and a PDF contract. In traditional software, synthesizing those four formats took a team of junior analysts three full days!\n\n"
            "[Prof. Peter] With Google NotebookLM and Gemini, you drag and drop all four files simultaneously. The engine performs cross-modal synthesis: it detects if the CEO's verbal tone in the audio contradicts the revenue projection in row 42 of the spreadsheet!\n\n"
            "[TA Sarah] That level of cross-format insight gives executives and researchers superpowers.\n\n"
            "[TA James] Let us examine Google's breakthrough Audio Overview architecture on Slide 19!"
        ),
        "koreanGuide": {
            "summary": "멀티 포맷 지능 합성: 엑셀, PDF, 녹음 음성, 슬라이드의 교차 분석 혁신",
            "points": [
                "이종 미디어 융합: 엑셀 재무 수치와 CEO 녹음 음성, PDF 계약서를 단일 지식망으로 연결",
                "모순점 자동 감지: 음성 회의에서 발언한 내용과 서면 보고서 수치 간의 불일치를 자동 탐지",
                "분석 시간 단축: 주니어 연구원 팀이 3일간 작업하던 교차 검증을 수 초 내로 완료"
            ],
            "tips": "피터 교수와 제임스 조교가 멀티모달 교차 분석이 실제 경영 의사결정에서 갖는 위력을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Cross-Modal Synthesis",
                "def": "The ability to analyze, correlate, and draw insights across disparate data modalities (text, audio, video, tables).",
                "defKo": "교차 모달 합성 (이종 데이터 융합 분석)"
            },
            {
                "term": "Discrepancy Detection",
                "def": "Automated identification of conflicting assertions across multi-source document repositories.",
                "defKo": "모순점 자동 탐지"
            }
        ]
    },
    # Slide 19: The Anatomy of Audio Overview
    {
        "num": 19,
        "type": "content",
        "title": "THE ANATOMY OF THE AUDIO OVERVIEW",
        "subtitle": "Deconstructing Google's multi-speaker conversational podcast generation engine",
        "points": [
            "Dual-Presenter Dialogue Engine: Generating natural banter, interruptions, and intuitive metaphors.",
            "Source-Grounded Scripting: Dialogue generation is strictly constrained by user document citations.",
            "Expressive Neural TTS: Sub-second voice synthesis producing human-level prosody and emotional cadence."
        ],
        "script": (
            "[Prof. Peter] Slide 19 explores \"THE ANATOMY OF THE AUDIO OVERVIEW.\" When Google introduced NotebookLM Audio Overviews, the internet was stunned by how lifelike and engaging the two AI hosts sounded!\n\n"
            "[TA Sarah] How does it actually work under the hood? It is a 2-stage pipeline: First, Gemini analyzes your source documents and writes a dynamic conversational podcast script—complete with casual interjections, witty analogies, and natural interruptions.\n\n"
            "[TA James] Second, that script is fed into Google's advanced multi-voice neural Text-to-Speech (TTS) engine. The voices breathe, pause for emphasis, laugh, and bounce ideas back and forth just like two expert podcast hosts!\n\n"
            "[Prof. Peter] But crucially: unlike casual podcasts, every single insight discussed by the AI hosts is grounded 100% in your uploaded documents. You can listen during your morning commute and absorb 100 pages of research effortlessly!\n\n"
            "[TA Sarah] Let us review system latency and throughput limits on Slide 20."
        ),
        "koreanGuide": {
            "summary": "오디오 오버뷰(Audio Overview) 해부: 2인 대화형 팟캐스트 생성 파이프라인의 원리",
            "points": [
                "2단계 파이프라인: 제미나이가 원천 문서를 기반으로 자연스러운 대본 작성 ➔ 고품질 뉴럴 TTS 음성 합성",
                "자연스러운 인간적 대화: 숨소리, 추임새, 유쾌한 비유, 자연스러운 끼어들기(Interruption) 완벽 재현",
                "철저한 출처 기반: 단순 수다가 아닌 사용자 원천 문서에 100% 근거한 학술/경영 팟캐스트 제공"
            ],
            "tips": "사라 조교가 2단계 파이프라인을 짚고, 피터 교수가 출퇴근 시간 지식 습득의 유용성을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Audio Overview",
                "def": "Google's AI feature transforming complex documents into engaging, multi-speaker conversational audio podcasts.",
                "defKo": "오디오 오버뷰 (AI 대화형 팟캐스트)"
            },
            {
                "term": "Neural TTS Prosody",
                "def": "The rhythm, stress, and intonation patterns synthesized by neural speech models to emulate natural human speech.",
                "defKo": "뉴럴 TTS 운율감 (자연스러운 억양과 호흡)"
            }
        ]
    },
    # Slide 20: Part 2 Summary: System Limits and Latency
    {
        "num": 20,
        "type": "content",
        "title": "PART 2 SUMMARY: SYSTEM LIMITS AND LATENCY",
        "subtitle": "Balancing vector index size, embedding dimensions, context window costs, and inference speed",
        "points": [
            "Latency Profile: 50ms vector retrieval + 350ms Gemini Flash generation = 400ms total loop.",
            "Dimension Trade-off: 768-dim embeddings offer 98% accuracy of 1536-dim at 50% memory cost.",
            "Scale Boundary: Google NotebookLM effortlessly supports up to 50 sources and 25 million words per notebook."
        ],
        "script": (
            "[TA Sarah] Slide 20 summarizes Part 2: \"SYSTEM LIMITS AND LATENCY TRADEOFFS.\"\n\n"
            "[TA James] In production engineering, every architectural decision has a trade-off. Look at the latency budget: 50 milliseconds for vector similarity search, 350 milliseconds for Gemini 3.5 Flash inference—total round-trip under 400 milliseconds!\n\n"
            "[Prof. Peter] Notice the scale limits: Google NotebookLM currently supports up to 50 comprehensive sources per notebook, representing over 25 million words of text! That is equivalent to an entire university library shelf in a single workspace.\n\n"
            "[TA Sarah] And by choosing 768-dimension embeddings, we capture 98% of semantic nuances while cutting memory storage costs in half.\n\n"
            "[TA James] Let us see how enterprise vector re-ranking optimizes precision even further on Slide 21!"
        ),
        "koreanGuide": {
            "summary": "Part 2 요약: 시스템 한계 및 레이턴시 최적화 지표",
            "points": [
                "레이턴시 예산: 50ms 벡터 검색 + 350ms 제미나이 플래시 생성 = 총 400ms 초저지연 루프",
                "임베딩 차원 최적화: 768차원 모델로 1536차원 대비 98% 정확도를 유지하며 메모리 비용 50% 절감",
                "노트북당 최대 50개 소스, 2,500만 단어(책 수백 권 분량)의 압도적 지식 수용력"
            ],
            "tips": "제임스 조교가 수치 기반의 시스템 지표를 제시하고 피터 교수가 엔지니어링적 균형 감각을 칭찬합니다."
        },
        "keyTerms": [
            {
                "term": "Latency Budget",
                "def": "The allocated time constraint distributed across retrieval, processing, and generation phases of a system.",
                "defKo": "레이턴시 예산 (단계별 허용 지연 시간)"
            },
            {
                "term": "Scale Boundary",
                "def": "The maximum capacity thresholds (document count, token limits, storage limits) of a deployed architecture.",
                "defKo": "스케일 한계 경계선"
            }
        ]
    },
    # Slide 21: Production Engineering: Re-Ranking
    {
        "num": 21,
        "type": "content",
        "title": "PRODUCTION ENGINEERING: EMBEDDING RE-RANKING",
        "subtitle": "Two-stage retrieval pipelines: Fast approximate search followed by cross-encoder precision ranking",
        "points": [
            "Stage 1 Bi-Encoder: Retrieve top 50 candidate chunks using fast HNSW vector cosine search in 10ms.",
            "Stage 2 Cross-Encoder: Re-rank candidates using full attention to select the top 5 hyper-relevant chunks.",
            "Impact: Eliminates retrieval noise, improves precision by 22%, and reduces token consumption."
        ],
        "script": (
            "[TA James] Slide 21 covers a vital enterprise optimization: \"PRODUCTION ENGINEERING: EMBEDDING RE-RANKING.\"\n\n"
            "[TA Sarah] In production, raw vector search sometimes pulls chunks that share similar vocabulary but lack specific context. To fix this, high-scale enterprise systems use a 2-stage retrieval pipeline.\n\n"
            "[TA James] Stage 1 uses a fast Bi-Encoder to grab the top 50 candidates in 10 milliseconds. Then Stage 2 runs a precision Cross-Encoder Re-Ranker that scores all 50 chunks against the query using full attention, selecting the top 5 gold-standard paragraphs!\n\n"
            "[Prof. Peter] This 2-stage architecture increases answer precision by over 22% while filtering out noise before the prompt reaches Gemini Flash.\n\n"
            "[TA Sarah] Let us inspect our second enterprise case study on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "프로덕션 엔지니어링: 2단계 임베딩 리랭킹(Re-Ranking) 최적화 기법",
            "points": [
                "1단계 바이엔코더(Bi-Encoder): 10ms 내에 HNSW로 상위 50개 후보 청크 초고속 인출",
                "2단계 크로스엔코더(Cross-Encoder): 상위 50개 후보를 전체 어텐션으로 재평가하여 최상위 5개 청크 선별",
                "효과: 검색 정확도 22% 향상 및 불필요한 토큰 낭비와 노이즈 완벽 차단"
            ],
            "tips": "제임스 조교가 2단계 리랭킹 아키텍처의 필요성과 원리를 명확하게 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Cross-Encoder Re-Ranking",
                "def": "A precision scoring model that evaluates query-document pairs jointly to rank retrieval quality accurately.",
                "defKo": "크로스엔코더 리랭킹 (정밀 재순위화)"
            },
            {
                "term": "Two-Stage Retrieval",
                "def": "An information retrieval pattern combining fast approximate candidate generation with deep reranking.",
                "defKo": "2단계 검색 파이프라인"
            }
        ]
    },
    # Slide 22: Case Study 2: Big Pharma FDA 10,000-Page Clinical Trial Audit
    {
        "num": 22,
        "type": "casestudy",
        "title": "CASE STUDY 2: BIG PHARMA FDA 10,000-PAGE AUDIT",
        "subtitle": "Cross-referencing 10,000 pages of clinical trials, patient logs, and biochemical data for FDA filing",
        "company": "Global Top-5 Pharmaceutical Enterprise",
        "problem": "Medical affairs team faced a 3-month deadline to cross-audit 10,000 pages of clinical trial notes, patient adverse event logs, and chemistry reports for FDA New Drug Application.",
        "solution": "Built a multi-notebook Google NotebookLM RAG pipeline with 2-stage re-ranking and automated cross-modality table discrepancy checks.",
        "impact": "Audit timeline slashed from 90 days to 6 days; identified 14 hidden dosage reporting discrepancies before submission; achieved zero-deficiency FDA approval.",
        "script": (
            "[Prof. Peter] Slide 22 presents \"CASE STUDY 2: BIG PHARMA FDA 10,000-PAGE CLINICAL TRIAL AUDIT.\"\n\n"
            "[TA Sarah] A global top-5 pharmaceutical company was preparing a massive New Drug Application for the FDA. They had over 10,000 pages of clinical trial notes, patient adverse event logs, biochemical data sheets, and investigator brochures!\n\n"
            "[TA James] A single dosage discrepancy or conflicting adverse event report could result in FDA rejection and years of costly delay. Their medical affairs team had only 90 days to verify every single data point.\n\n"
            "[Prof. Peter] They deployed an enterprise RAG knowledge factory using NotebookLM and Gemini with 2-stage re-ranking. The system ingested all 10,000 pages across structured notebooks.\n\n"
            "[TA Sarah] Look at the outcome: the audit was completed in just 6 days instead of 90 days! The RAG system caught 14 subtle dosage reporting contradictions that human reviewers had missed.\n\n"
            "[TA James] They submitted the application on time and received zero-deficiency FDA approval!\n\n"
            "[Prof. Peter] Now let us open Part 3 and examine enterprise privacy, trust, and the data fortress on Slide 23."
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 2: 글로벌 제약사의 10,000페이지 FDA 임상시험 감사 성공 사례",
            "points": [
                "문제 상황: 신약 승인을 위해 10,000페이지 분량의 임상 데이터와 환자 이상 반응 일지를 90일 내 완벽 검증 필요",
                "솔루션: 2단계 리랭킹과 교차 모달 표 분석이 적용된 NotebookLM 사설 RAG 팩토리 도입",
                "성과: 90일 소요 작업을 6일로 단축, 인간이 놓친 14건의 용량 표기 불일치 사전 적발 및 FDA 무결점 승인"
            ],
            "tips": "피터 교수와 조교들이 생명과 직결된 임상 데이터 감사에서 정밀 RAG가 발휘한 가치를 생생하게 전달합니다."
        },
        "keyTerms": [
            {
                "term": "FDA New Drug Application (NDA)",
                "def": "The formal proposal submitted to the FDA requesting approval for commercial distribution of a new pharmaceutical.",
                "defKo": "FDA 신약 허가 신청서 (NDA)"
            },
            {
                "term": "Zero-Deficiency Approval",
                "def": "Regulatory clearance granted without requiring corrective action requests or supplementary audit inquiries.",
                "defKo": "무결점 규제 승인"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 23: Part 3 Section Divider
    {
        "num": 23,
        "type": "section",
        "title": "PART 3: TRUST, PRIVACY, AND ENTERPRISE GOVERNANCE",
        "subtitle": "Google's data isolation guarantees, zero-training commitments, and multi-tenant security architecture",
        "script": (
            "[TA Sarah] Look at Slide 23: \"PART 3: TRUST, PRIVACY, AND ENTERPRISE GOVERNANCE.\" Professor, whenever enterprise leaders hear about AI, their first question is always: 'Will my confidential data be used to train Google's models?'\n\n"
            "[Prof. Peter] And that is a completely legitimate question! If an enterprise uploads proprietary source code, patient health records, or merger secrets to an unverified cloud, they violate fiduciary duty and international privacy laws.\n\n"
            "[TA James] In Part 3, we demonstrate why Google's enterprise data architecture provides an ironclad fortress. Your data is isolated in secure tenant enclaves and is NEVER used for model training.\n\n"
            "[TA Sarah] We will inspect access control matrices, compliance firewalls like HIPAA and GDPR, and cryptographic audit trails.\n\n"
            "[Prof. Peter] Let us examine the threat profile of public data leakage on Slide 24."
        ),
        "koreanGuide": {
            "summary": "Part 3 섹션 전환: 신뢰, 프라이버시, 그리고 엔터프라이즈 거버넌스 요새 구축",
            "points": [
                "기업 리더들의 핵심 질문: 내 비밀 문서가 AI 모델 재학습에 쓰이지 않는가?",
                "구글의 데이터 격리 보증: 엔터프라이즈 테넌트 내에서 데이터 완벽 격리 및 무단 학습 금지",
                "HIPAA, GDPR, SOC2 등 글로벌 규제 준수 및 암호화 감사 추적 체계"
            ],
            "tips": "사라 조교가 기업 보안 책임자의 우려를 대변하고 제임스와 피터 교수가 엔터프라이즈 클라우드 요새를 확신 있게 제시합니다."
        },
        "keyTerms": [
            {
                "term": "Zero-Training Commitment",
                "def": "A legally binding enterprise agreement ensuring customer data is never used to train or fine-tune public foundation models.",
                "defKo": "무학습 서약 (고객 데이터 재학습 금지)"
            },
            {
                "term": "Data Isolation Enclave",
                "def": "A cryptographically isolated cloud perimeter guaranteeing complete segregation of tenant data.",
                "defKo": "데이터 격리 엔클레이브"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 24: Threat Profile: Public Data Leakage
    {
        "num": 24,
        "type": "content",
        "title": "THE THREAT PROFILE: PUBLIC DATA LEAKAGE",
        "subtitle": "How consumer AI chatbots expose proprietary source code, financial secrets, and PII",
        "points": [
            "Consumer LLM Risk: Prompts typed into free web chatbots often enter general retraining pipelines.",
            "Model Inversion Attacks: Adversaries can prompt public models to regurgitate memorized training snippets.",
            "Regulatory Penalties: Violating GDPR or HIPAA can trigger enterprise fines exceeding $20 million."
        ],
        "script": (
            "[Prof. Peter] Slide 24 outlines \"THE THREAT PROFILE: PUBLIC DATA LEAKAGE.\" Look at the catastrophic risks of using consumer chat tools for enterprise work.\n\n"
            "[TA Sarah] In consumer chatbots, whatever text or code you paste into the chat box can be stored in training logs and used to train future public checkpoints. Engineers who pasted proprietary semiconductor code into consumer LLMs accidentally leaked IP to the public!\n\n"
            "[TA James] Furthermore, research demonstrates 'model inversion attacks,' where malicious actors craft specific prompts to force public models to regurgitate memorized training snippets—including passwords, API keys, and customer emails!\n\n"
            "[Prof. Peter] Under GDPR and HIPAA, an unencrypted data leak can lead to catastrophic fines exceeding tens of millions of dollars and permanent reputational damage.\n\n"
            "[TA Sarah] Let us inspect Google's formal Data Isolation Policy on Slide 25!"
        ),
        "koreanGuide": {
            "summary": "위협 프로필: 퍼블릭 데이터 유출과 소비자용 챗봇의 위험성",
            "points": [
                "소비자용 챗봇의 위험: 프롬프트에 입력한 소스코드와 재무 문서가 공공 모델 재학습에 사용될 위험",
                "모델 인버전 공격: 악의적 프롬프트 조작을 통해 모델이 암기한 비밀키나 고객 정보를 뱉어내는 취약점",
                "규제 위반 벌금: GDPR, HIPAA 등 개인정보 유출 시 수천만 달러의 징벌적 과징금 부과"
            ],
            "tips": "제임스 조교가 과거 대기업들의 실제 소스코드 유출 사고 사례를 언급하며 경각심을 고취합니다."
        },
        "keyTerms": [
            {
                "term": "Model Inversion Attack",
                "def": "An adversarial exploit extracting sensitive private training data by systematically probing model outputs.",
                "defKo": "모델 인버전 공격 (학습 데이터 탈취 기법)"
            },
            {
                "term": "PII (Personally Identifiable Information)",
                "def": "Any information that can be used to distinguish or trace an individual's identity, protected by global privacy laws.",
                "defKo": "개인 식별 정보 (PII)"
            }
        ]
    },
    # Slide 25: The Safe Boundary: Google's Data Isolation Policy
    {
        "num": 25,
        "type": "content",
        "title": "THE SAFE BOUNDARY: DATA ISOLATION POLICY",
        "subtitle": "Ironclad commitments: Your private files, embeddings, and queries remain exclusively yours",
        "points": [
            "No Model Training: Google Workspace and NotebookLM Enterprise never train models on customer data.",
            "Customer-Managed Encryption: Data encrypted at rest (AES-256) and in transit (TLS 1.3) with CMEK keys.",
            "Strict Tenant Isolation: Virtual Private Cloud (VPC) service controls prevent cross-tenant data leakage."
        ],
        "script": (
            "[TA Sarah] Slide 25 details \"THE SAFE BOUNDARY: GOOGLE'S DATA ISOLATION POLICY.\"\n\n"
            "[TA James] Under Google Workspace and Google Cloud enterprise terms, customer data is strictly isolated. Rule number one: your data is NEVER used to train or tune foundation models. Rule number two: your data is encrypted at rest with AES-256 and in transit with TLS 1.3!\n\n"
            "[Prof. Peter] Even more importantly, enterprise customers can use Customer-Managed Encryption Keys (CMEK). That means you hold the cryptographic master key—not even Google engineers can inspect your files without your explicit authorization!\n\n"
            "[TA Sarah] This gives enterprise compliance officers absolute peace of mind.\n\n"
            "[TA James] Let us see how Shared Google Drives serve as system sovereignty vaults on Slide 26!"
        ),
        "koreanGuide": {
            "summary": "안전한 경계: 구글의 데이터 격리 정책 및 고객 관리 암호화 키(CMEK)",
            "points": [
                "모델 재학습 금지: 엔터프라이즈 워크스페이스 및 NotebookLM 데이터는 절대 모델 학습에 사용되지 않음",
                "CMEK(고객 관리 암호화 키): 기업이 마스터 키를 직접 보유하여 클라우드 제공자도 무단 열람 불가",
                "AES-256 저장 암호화 및 TLS 1.3 전송 암호화를 통한 완벽한 테넌트 격리"
            ],
            "tips": "사라 조교와 제임스 조교가 CMEK의 강력한 암호화 통제권을 수강생들에게 알기 쉽게 설명합니다."
        },
        "keyTerms": [
            {
                "term": "CMEK (Customer-Managed Encryption Keys)",
                "def": "A cloud security capability allowing enterprises to control and manage their own encryption keys for data at rest.",
                "defKo": "고객 관리 암호화 키 (CMEK)"
            },
            {
                "term": "VPC Service Controls",
                "def": "Google Cloud security perimeters preventing unauthorized data exfiltration across tenant boundaries.",
                "defKo": "VPC 서비스 통제 (데이터 유출 방지선)"
            }
        ]
    },
    # Slide 26: Shared Google Drives for System Sovereignty
    {
        "num": 26,
        "type": "content",
        "title": "SHARED GOOGLE DRIVES FOR SYSTEM SOVEREIGNTY",
        "subtitle": "Centralizing knowledge vaults in institutional shared drives rather than fragile personal accounts",
        "points": [
            "Institutional Ownership: Files belong to the enterprise organization, preventing data loss on staff turnover.",
            "Granular Permissions: Role-Based Access Control (Manager, Content Manager, Contributor, Viewer).",
            "Automatic RAG Ingestion: Adding a document to a Shared Drive instantly updates the connected agent index."
        ],
        "script": (
            "[Prof. Peter] Slide 26 explores \"SHARED GOOGLE DRIVES FOR SYSTEM SOVEREIGNTY.\" James, what happens when an employee stores vital research in a personal Google Drive and then leaves the company?\n\n"
            "[TA James] Total disaster, Professor! When their personal account is deactivated, all internal knowledge links break, scripts lose authentication, and the team loses months of intellectual property.\n\n"
            "[TA Sarah] That is why our architecture mandates Shared Google Drives! Files belong to the institution, not to an individual employee's inbox. Permissions are managed centrally through Role-Based Access Control (RBAC).\n\n"
            "[TA James] And whenever a researcher drops a new PDF into the Shared Drive folder, a Google Apps Script webhook fires, indexing the file into your private RAG notebook automatically!\n\n"
            "[Prof. Peter] Let us examine the Access Control Matrix on Slide 27."
        ),
        "koreanGuide": {
            "summary": "공유 드라이브를 통한 시스템 주권 확보 및 자동 RAG 인덱싱 연동",
            "points": [
                "개인 계정 종속 탈피: 직원의 퇴사나 계정 삭제 시에도 기업 지적 자산이 영구 보존되는 공유 드라이브 구조",
                "역할 기반 접근 제어(RBAC): 관리자, 콘텐츠 관리자, 기여자, 뷰어로 세분화된 권한 통제",
                "자동 연동 웹훅: 공유 드라이브에 새 문서를 넣는 즉시 RAG 인덱스에 자동 반영"
            ],
            "tips": "제임스 조교가 실무에서 흔히 일어나는 퇴사자 계정 삭제로 인한 데이터 유실 사고를 경고합니다."
        },
        "keyTerms": [
            {
                "term": "Institutional Shared Drive",
                "def": "An enterprise Google Drive repository where file ownership is maintained by the organization rather than individual users.",
                "defKo": "조직 공유 드라이브 (기관 소유 드라이브)"
            },
            {
                "term": "RBAC (Role-Based Access Control)",
                "def": "A security model restricting network and file access based on the roles of individual users within an enterprise.",
                "defKo": "역할 기반 접근 제어 (RBAC)"
            }
        ]
    },
    # Slide 27: The Access Control Matrix
    {
        "num": 27,
        "type": "content",
        "title": "THE ACCESS CONTROL MATRIX",
        "subtitle": "Mapping user roles, document classifications, API permissions, and agent access tiers",
        "points": [
            "Classification Tiers: Public, Internal, Confidential, Restricted (Secret).",
            "Agent Token Scopes: Read-only RAG scopes strictly segregated from destructive write permissions.",
            "Zero Trust Validation: Re-authenticating token validity on every single retrieval transaction."
        ],
        "script": (
            "[TA Sarah] Slide 27 outlines \"THE ACCESS CONTROL MATRIX.\" Even inside a single enterprise, not every employee or agent should have access to every document.\n\n"
            "[TA James] Look at the matrix on screen: we classify data into four clear tiers—Public, Internal, Confidential, and Restricted. Our RAG agents receive strictly scoped OAuth 2.0 tokens: Read-Only access to specific folders, with zero permission to delete or overwrite source records!\n\n"
            "[Prof. Peter] If a junior analyst queries the system, the RAG engine checks their identity token against the matrix. The model cannot retrieve or cite documents from the 'Restricted Executive' tier unless the user has verified credentials.\n\n"
            "[TA Sarah] Zero Trust means never assuming access rights blindly.\n\n"
            "[TA James] Let us see how compliance firewalls like HIPAA and GDPR operate on Slide 28!"
        ),
        "koreanGuide": {
            "summary": "접근 제어 매트릭스(Access Control Matrix)와 제로 트러스트 보안 원칙",
            "points": [
                "4단계 데이터 분류: 공개, 내부, 기밀, 극비(Restricted) 등급으로 명확히 구분",
                "에이전트 권한 최소화: 파괴적 쓰기/삭제 권한을 차단하고 오직 읽기 전용 RAG 스코프만 부여",
                "제로 트러스트 검증: 사용자의 자격 증명(OAuth 토큰)을 매 검색 쿼리마다 실시간 대조하여 무단 인출 방지"
            ],
            "tips": "사라 조교와 제임스 조교가 권한 통제 매트릭스를 도식화하여 명쾌하게 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Access Control Matrix",
                "def": "A formal table defining the precise permissions granted to specific users and automated agents across data assets.",
                "defKo": "접근 제어 매트릭스"
            },
            {
                "term": "Least Privilege Principle",
                "def": "The computer security concept requiring that users and agents are given only the minimum permissions necessary.",
                "defKo": "최소 권한의 원칙"
            }
        ]
    },
    # Slide 28: Compliance Firewalls: HIPAA & GDPR
    {
        "num": 28,
        "type": "content",
        "title": "COMPLIANCE FIREWALLS: HIPAA & GDPR",
        "subtitle": "Deploying zero-knowledge PII sanitization and automated compliance guardrails",
        "points": [
            "Automated PII Redaction: Scrubbing Social Security numbers, names, and patient IDs prior to embedding.",
            "Right to Erasure (GDPR): Immediate cryptographic deletion of vector points when source files are removed.",
            "HIPAA BAA Contracts: Executing formal Business Associate Agreements for healthcare data enclaves."
        ],
        "script": (
            "[Prof. Peter] Slide 28 covers \"COMPLIANCE FIREWALLS: HIPAA & GDPR.\" In healthcare, finance, and government, compliance is not optional—it is a legal requirement.\n\n"
            "[TA Sarah] Before documents are ingested into the vector pipeline, our automated preprocessing worker runs a PII Redaction filter. It detects Social Security numbers, credit card numbers, and patient names, replacing them with anonymized cryptographic tokens.\n\n"
            "[TA James] Furthermore, to comply with GDPR's 'Right to be Forgotten,' our vector index links every embedding back to its Document UUID. If a user requests deletion, our daemon purges both the source file and its corresponding vector embeddings within 60 seconds!\n\n"
            "[Prof. Peter] Formal compliance contracts like HIPAA BAAs ensure that your enterprise RAG factory is legally protected.\n\n"
            "[TA Sarah] Let us inspect our third enterprise case study on Slide 29!"
        ),
        "koreanGuide": {
            "summary": "컴플라이언스 방화벽: HIPAA, GDPR 및 자동 개인정보 마스킹(PII Redaction)",
            "points": [
                "자동 개인정보 비식별화: 벡터화 전 주민번호, 환자 이름, 카드번호를 감지하여 익명 토큰으로 대체",
                "GDPR 잊힐 권리(Right to Erasure): 원본 문서 삭제 시 60초 이내에 연계된 모든 벡터 임베딩 영구 삭제",
                "의료 데이터 규제 준수: HIPAA BAA 정식 계약 체결을 통한 법적 안전성 확보"
            ],
            "tips": "제임스 조교가 PII 마스킹 처리와 GDPR 즉시 삭제 파이프라인의 실무 구현을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "PII Redaction",
                "def": "The automated process of masking or removing personally identifiable information from datasets prior to processing.",
                "defKo": "개인정보 자동 비식별화 (마스킹)"
            },
            {
                "term": "GDPR Right to Erasure",
                "def": "The European Union legal mandate requiring enterprises to permanently delete personal data upon user request.",
                "defKo": "GDPR 잊힐 권리 (삭제권)"
            }
        ]
    },
    # Slide 29: Case Study 3: Global Law Firm M&A Discovery
    {
        "num": 29,
        "type": "casestudy",
        "title": "CASE STUDY 3: GLOBAL LAW FIRM M&A DISCOVERY",
        "subtitle": "Analyzing 50,000 merger documents in 48 hours while maintaining strict client privilege isolation",
        "company": "International Top-10 Corporate Law Firm",
        "problem": "During a $4B cross-border acquisition, legal team had 72 hours to audit 50,000 confidential contracts across 12 data rooms without risking client privilege cross-contamination.",
        "solution": "Built isolated Google NotebookLM RAG workspaces on Google Cloud with strict CMEK encryption keys, RBAC matrix, and automated privilege log generator.",
        "impact": "50,000 contracts reviewed in 36 hours; zero cross-tenant data leaks; identified 8 hidden indemnity liability clauses saving client $45M.",
        "script": (
            "[Prof. Peter] Slide 29 presents \"CASE STUDY 3: GLOBAL LAW FIRM M&A DISCOVERY.\" Look at this high-stakes legal deployment.\n\n"
            "[TA Sarah] An international top-10 law firm was handling a 4-billion-dollar cross-border acquisition. They were given exactly 72 hours to review 50,000 highly confidential supplier contracts, employment agreements, and IP licenses across 12 separate virtual data rooms!\n\n"
            "[TA James] If a single document from Target Company A leaked into the database of Target Company B, the law firm would face catastrophic legal disbarment. So they architected 12 isolated NotebookLM enclaves, each protected with its own Customer-Managed Encryption Key (CMEK).\n\n"
            "[Prof. Peter] Look at the results: the legal team completed the review in 36 hours! The RAG system automatically generated a privilege log with exact citations and uncovered 8 hidden indemnity liability clauses, saving their client 45 million dollars in purchase price adjustments!\n\n"
            "[TA Sarah] That is the power of precision-grounded intelligence.\n\n"
            "[TA James] Now let us open Part 4 and explore the synthesis of wisdom and governance on Slide 30!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 3: 글로벌 대형 로펌 5만 건 M&A 계약서 36시간 정밀 분석",
            "points": [
                "문제 상황: 40억 달러 규모 기업 인수합병에서 72시간 내 50,000건의 비밀 계약서 검토 및 비밀 특권 보호 필수",
                "솔루션: CMEK 암호화 키로 완벽 격리된 12개 NotebookLM 엔클레이브 및 RBAC 접근 제어 구축",
                "성과: 36시간 만에 검토 완료, 데이터 유출 0건, 숨겨진 배상 책임 조항 8건 적발로 4,500만 달러 절감"
            ],
            "tips": "사라 조교와 피터 교수가 법률 비밀 특권(Attorney-Client Privilege) 보호의 엄중함과 RAG의 경제적 성과를 연결합니다."
        },
        "keyTerms": [
            {
                "term": "Attorney-Client Privilege",
                "def": "A legal principle protecting confidential communications between lawyers and clients from compelled disclosure.",
                "defKo": "변호사-의뢰인 비밀 특권"
            },
            {
                "term": "M&A Due Diligence",
                "def": "The comprehensive legal and financial appraisal of a target business prior to signing a merger or acquisition.",
                "defKo": "M&A 기업 실사 (Due Diligence)"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 30: Part 4 Section Divider
    {
        "num": 30,
        "type": "section",
        "title": "PART 4: WISDOM SYNTHESIS, GOVERNANCE & LIFE OS",
        "subtitle": "Human-on-the-Loop sovereignty, intellectual humility, and honoring truth under Soli Deo Gloria",
        "script": (
            "[TA Sarah] Look at Slide 30: \"PART 4: WISDOM SYNTHESIS, GOVERNANCE & LIFE OS.\" Professor, we have mastered RAG mechanics and enterprise security. How do we translate this into human wisdom and daily leadership?\n\n"
            "[Prof. Peter] That is the ultimate capstone of Oikos University! Technology without wisdom is dangerous; intelligence without integrity is destructive. Under Soli Deo Gloria, our goal is not to produce lazy thinkers who outsource their minds to machines, but to empower sovereign architects who steward knowledge with humility and purpose.\n\n"
            "[TA James] In Part 4, we examine Human-on-the-Loop governance, cryptographic audit trails, how to build your Life OS knowledge vault, and execute our Hands-on Lab!\n\n"
            "[TA Sarah] Let us inspect how cryptographic audit trails seal every retrieval on Slide 31."
        ),
        "koreanGuide": {
            "summary": "Part 4 섹션 전환: 지혜의 통합, 거버넌스 및 라이프 OS(Life OS) 완성",
            "points": [
                "기술을 넘어선 지혜: 지능에 인격과 윤리가 결합할 때 비로소 진정한 리더십 완성",
                "Soli Deo Gloria의 청지기직: 생각을 기계에 외주 주는 게으른 인간이 아닌, 시스템을 통솔하는 주권적 건축가 양성",
                "Human-on-the-Loop 거버넌스와 개인 라이프 OS 지식 공장 구축"
            ],
            "tips": "피터 교수의 학문적/영적 비전을 중심으로 사라와 제임스가 결의를 다지는 톤으로 Part 4를 엽니다."
        },
        "keyTerms": [
            {
                "term": "Wisdom Synthesis",
                "def": "The high-level integration of factual knowledge, ethical discernment, and strategic human judgment.",
                "defKo": "지혜의 통합 (전략적 판단력)"
            },
            {
                "term": "Sovereign Stewardship",
                "def": "The active, ethical oversight and responsible governance of automated intelligence systems.",
                "defKo": "주권적 청지기직 (책임 거버넌스)"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 31: Cryptographically Sealed Audit Trails
    {
        "num": 31,
        "type": "content",
        "title": "CRYPTOGRAPHICALLY SEALED AUDIT TRAILS",
        "subtitle": "Immutable SHA-256 retrieval logging for regulatory compliance and forensic verification",
        "points": [
            "Immutable Logging: Every query, retrieved chunk hash, and prompt response is recorded with a SHA-256 hash.",
            "Append-Only Ledger: Audit records are written to write-once-read-many (WORM) storage.",
            "Forensic Replay: Enables auditors to replay exact historical reasoning states for any past decision."
        ],
        "script": (
            "[TA James] Slide 31 presents \"CRYPTOGRAPHICALLY SEALED AUDIT TRAILS.\" In enterprise systems, 'trust me' is not a security policy!\n\n"
            "[TA Sarah] Exactly, James! Every time our RAG agent retrieves a chunk and generates an answer, the system creates a cryptographic block: the user ID, timestamp, exact query, the SHA-256 hashes of the retrieved chunks, and the full model output.\n\n"
            "[Prof. Peter] These blocks are appended to an immutable WORM ledger—Write Once, Read Many. If an auditor asks two years from now: 'Why did the executive make this investment decision on March 14?', you can replay the exact chunks and model state with forensic precision!\n\n"
            "[TA James] That eliminates all ambiguity and protects both the human and the enterprise.\n\n"
            "[TA Sarah] Let us see how to defeat shadow IT in enterprise environments on Slide 32!"
        ),
        "koreanGuide": {
            "summary": "암호화로 봉인된 감사 추적(Audit Trail)과 WORM 불변 로그 체계",
            "points": [
                "SHA-256 불변 로깅: 사용자 질의, 인출된 청크 해시, 모델 생성 결과를 암호화 블록으로 기록",
                "WORM 저장소(Write Once Read Many): 변조 및 임의 삭제가 불가능한 영구 감사 원장 구축",
                "포렌식 리플레이: 수년 후에도 특정 의사결정 시점의 AI 입력과 출력을 완벽히 재현 검증 가능"
            ],
            "tips": "제임스 조교가 엔터프라이즈 보안 감사(Forensic Audit)의 필수 요건을 명확히 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Cryptographic Audit Trail",
                "def": "An unalterable, cryptographically signed record of all system queries, retrievals, and generated responses.",
                "defKo": "암호화 감사 추적 원장"
            },
            {
                "term": "WORM Storage (Write Once, Read Many)",
                "def": "A data storage technology that prevents stored data from being modified or erased after initial writing.",
                "defKo": "WORM 불변 저장소 (위변조 방지 스토리지)"
            }
        ]
    },
    # Slide 32: The Corporate Paradox of Shadow IT
    {
        "num": 32,
        "type": "content",
        "title": "THE CORPORATE PARADOX OF SHADOW IT",
        "subtitle": "Why banning AI increases risk, and how private knowledge factories eliminate shadow adoption",
        "points": [
            "The Ban Paradox: Banning AI causes employees to use unmonitored personal smartphones and consumer accounts.",
            "The Safe Alternative: Providing enterprise NotebookLM environments channels demand into secure enclaves.",
            "Visibility & Control: Compliance officers gain centralized telemetry while workers enjoy 10X productivity."
        ],
        "script": (
            "[TA Sarah] Slide 32 explores \"THE CORPORATE PARADOX OF SHADOW IT.\" When generative AI first exploded, many corporate IT departments reacted with total bans.\n\n"
            "[TA James] And what happened? Employees didn't stop using AI—they just copied secret company memos onto their personal iPhones and pasted them into free consumer web apps over cellular networks! The blanket ban made security 100 times worse!\n\n"
            "[Prof. Peter] That is the paradox: human desire for leverage cannot be suppressed by prohibitions. The only secure solution is to provide an enterprise-grade, grounded knowledge factory that is safer, faster, and better than consumer alternatives!\n\n"
            "[TA Sarah] When employees have Google NotebookLM within their Google Workspace, they get 10X productivity, and IT retains full security oversight.\n\n"
            "[TA James] Let us analyze strategic trade-offs on Slide 33."
        ),
        "koreanGuide": {
            "summary": "섀도우 IT(Shadow IT)의 기업적 역설과 프라이빗 지식 공장을 통한 해결",
            "points": [
                "무조건적 금지의 역설: AI 사용을 금지하면 직원들이 개인 스마트폰으로 기밀을 복사해 외부 챗봇에 입력",
                "안전한 대안 제시: 엔터프라이즈 NotebookLM을 공식 제공하여 안전한 사내 엔클레이브로 유도",
                "보안과 생산성의 양립: 중앙 통제 및 텔레메트리 가시성을 확보하면서 10배 생산성 지원"
            ],
            "tips": "사라 조교와 제임스 조교가 금지 정책의 부작용과 공식 사내 AI 인프라 구축의 필연성을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Shadow IT",
                "def": "The use of unauthorized information technology hardware, software, or cloud services by employees without IT department approval.",
                "defKo": "섀도우 IT (비인가 IT 서비스 무단 사용)"
            },
            {
                "term": "Enterprise Enclave Alternative",
                "def": "Providing official, secure internal AI tools to eliminate employee incentives for unapproved shadow tools.",
                "defKo": "엔터프라이즈 공식 안전 대안"
            }
        ]
    },
    # Slide 33: Strategic Trade-Offs: Precision vs. Creativity
    {
        "num": 33,
        "type": "content",
        "title": "STRATEGIC TRADE-OFFS: PRECISION VS. CREATIVITY",
        "subtitle": "Choosing the right temperature, top-k parameters, and grounding constraints for each task",
        "points": [
            "Strict Grounding Mode: Temperature 0.0, Top-k 3, strict citations (Legal, Financial, Medical).",
            "Exploratory Synthesis Mode: Temperature 0.5, Top-k 10, cross-modal brainstorming (Strategy, Marketing).",
            "Context Window Balancing: High-density chunks for analytical rigor vs. broad summaries for high-level briefs."
        ],
        "script": (
            "[Prof. Peter] Slide 33 outlines \"STRATEGIC TRADE-OFFS: PRECISION VS. CREATIVITY.\" As an intelligence architect, you must select the right operational mode for each domain.\n\n"
            "[TA Sarah] Look at the left column: \"STRICT GROUNDING MODE.\" For legal discovery, FDA audits, or financial reporting, we set model temperature to 0.0, restrict top-k chunks, and enforce 100% citation coverage. There is zero room for creative embellishment!\n\n"
            "[TA James] But look at the right column: \"EXPLORATORY SYNTHESIS MODE.\" When you are designing a new market strategy or brainstorming product ideas across 20 research whitepapers, you slightly raise temperature to 0.5 and allow broader cross-document synthesis!\n\n"
            "[Prof. Peter] Matching the architectural configuration to the task requirement is the hallmark of professional maturity.\n\n"
            "[TA Sarah] Let us see how to move beyond basic retrieval to high-level action on Slide 34!"
        ),
        "koreanGuide": {
            "summary": "전략적 트레이드오프: 정밀성(Precision)과 창의성(Creativity)의 모드별 설정",
            "points": [
                "엄격한 그라운딩 모드: 온도(Temperature) 0.0, Top-k 제한, 100% 인용 강제로 법률/의료/금융 무환각 보장",
                "탐색적 합성 모드: 온도 0.5 설정으로 20여 편의 논문 간 창의적 전략 교차 통찰 도출",
                "업무 성격에 따른 아키텍처 파라미터 튜닝의 중요성"
            ],
            "tips": "사라 조교가 온도(Temperature) 값에 따른 동작 차이를 실무적으로 알기 쉽게 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Model Temperature",
                "def": "A hyperparameter controlling the randomness of language model token selection (0.0 = deterministic, 1.0 = creative).",
                "defKo": "모델 온도 (무작위성 조절 계수)"
            },
            {
                "term": "Top-K Sampling",
                "def": "A generation parameter restricting the token or chunk search space to the top K highest-scoring candidates.",
                "defKo": "Top-K 샘플링 (상위 K개 후보 제한)"
            }
        ]
    },
    # Slide 34: Beyond Information Retrieval
    {
        "num": 34,
        "type": "content",
        "title": "BEYOND INFORMATION RETRIEVAL",
        "subtitle": "Moving from passive search engines to proactive insight synthesizers and decision engines",
        "points": [
            "Passive Search (Yesterday): Returns 10 blue links; human must read and manually synthesize all 10 pages.",
            "Proactive Synthesis (Today): Distills 100 documents into a 1-page structured executive decision memo.",
            "Automated Workflows: Triggers calendar time-blocks, drafts client emails, and updates database records."
        ],
        "script": (
            "[TA Sarah] Slide 34 illustrates \"BEYOND INFORMATION RETRIEVAL: From Search Engines to Decision Engines.\"\n\n"
            "[TA James] In the old world of search engines, you typed a keyword and got 10 blue links. Then you had to spend 4 hours clicking every link, reading 50 pages, and typing your own summary.\n\n"
            "[Prof. Peter] In modern grounded AI, you ask: 'What are the top 3 competitive risks to our cloud expansion based on Q3 competitor earnings?', and the knowledge factory synthesizes the 1-page executive decision memo with citations in 5 seconds!\n\n"
            "[TA Sarah] And through our Spark OS agent triggers, it can automatically draft an email to the leadership team or schedule a follow-up review.\n\n"
            "[TA James] Let us examine how this cultivates the scholar's mind on Slide 35!"
        ),
        "koreanGuide": {
            "summary": "단순 정보 검색을 넘어서: 의사결정 엔진과 능동적 통찰 합성으로의 진화",
            "points": [
                "과거 검색 엔진: 10개의 파란색 링크를 던져주고 인간이 일일이 읽고 요약해야 했던 비효율",
                "현재 지식 공장: 100개 문서를 5초 만에 1페이지 핵심 전략 브리핑으로 인용과 함께 압축 합성",
                "에이전트 연동: 요약에 그치지 않고 이메일 초안 작성 및 캘린더 등록까지 자동 수행"
            ],
            "tips": "피터 교수가 단순 검색과 의사결정 지능의 본질적 차이를 명쾌하게 대비합니다."
        },
        "keyTerms": [
            {
                "term": "Decision Engine",
                "def": "An AI architecture that synthesizes multi-source data directly into structured actionable recommendations.",
                "defKo": "의사결정 엔진 (행동 지향 지능)"
            },
            {
                "term": "Executive Synthesis",
                "def": "The concise summarization of extensive data into high-priority strategic briefing formats.",
                "defKo": "경영진 핵심 요약 브리핑"
            }
        ]
    },
    # Slide 35: Cultivating the Scholar's Mind
    {
        "num": 35,
        "type": "content",
        "title": "CULTIVATING THE SCHOLAR'S MIND",
        "subtitle": "Intellectual humility, deep reading, and honoring verified truth in an age of shallow synthesis",
        "points": [
            "Intellectual Humility: Recognizing that AI outputs are drafts to be verified, not infallible oracles.",
            "Deep Analog Reading: Using reclaimed time to read primary philosophical, theological, and foundational texts.",
            "Truth Stewardship: Refusing to circulate unverified rumors or fabricated AI soundbites."
        ],
        "script": (
            "[Prof. Peter] Slide 35 presents \"CULTIVATING THE SCHOLAR'S MIND: Intellectual Humility and Truth Stewardship.\" Sarah, what is the greatest danger when students use AI tools?\n\n"
            "[TA Sarah] The greatest danger is intellectual arrogance and superficial skimming! People think that because an AI summarized a 500-page book in 10 bullet points, they now understand the subject deeply without doing the cognitive work.\n\n"
            "[Prof. Peter] That is a tragic illusion. A summary gives you the outline; true wisdom comes from wrestling with deep principles! At Oikos University, we use RAG to eliminate mechanical document search so that you can invest your reclaimed hours in deep analog reading, serious contemplation, and prayer.\n\n"
            "[TA James] A true scholar uses AI as an assistant, but maintains rigorous critical thinking and verifies every claim!\n\n"
            "[TA Sarah] Let us inspect our fourth enterprise case study on Slide 36!"
        ),
        "koreanGuide": {
            "summary": "학자의 마음가짐: 지적 겸손, 깊은 읽기, 그리고 진리의 청지기직",
            "points": [
                "가장 큰 위험: 10줄 요약만 보고 500페이지 책을 다 이해했다고 착각하는 지적 오만과 피상성",
                "진정한 지혜: 기계적 검색 시간을 아껴 일차 원전(Primary Text)을 깊이 읽고 사색하는 데 투자",
                "학자의 청지기직: AI를 보조자로 활용하되 최종 진위 판별과 비판적 사고의 칼날을 유지"
            ],
            "tips": "피터 교수가 학문과 신앙의 본질을 진정성 있게 설파하여 깊은 울림을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Intellectual Humility",
                "def": "The conscious recognition of the limits of one's knowledge and the deliberate verification of technological outputs.",
                "defKo": "지적 겸손 (한계 인식과 검증 태도)"
            },
            {
                "term": "Deep Contemplation",
                "def": "The sustained, focused cognitive engagement with complex foundational ideas and theological truths.",
                "defKo": "심층 사색 (몰입적 지적 탐구)"
            }
        ]
    },
    # Slide 36: Case Study 4: Semiconductor Patent Infringement Prior-Art Defense
    {
        "num": 36,
        "type": "casestudy",
        "title": "CASE STUDY 4: SEMICONDUCTOR PATENT DEFENSE",
        "subtitle": "Finding prior-art needle in 500,000 global patent filings to dismiss a $120M lawsuit",
        "company": "Silicon Valley Semiconductor Fabrication Enterprise",
        "problem": "Patent troll filed a $120M infringement suit against client's flagship 3nm chip architecture; legal team had 3 weeks to locate prior-art invalidation evidence across 500,000 multi-lingual global patents.",
        "solution": "Built a multi-lingual vector RAG knowledge factory with HNSW cross-modal patent diagram extraction and recursive chunking across USPTO, EPO, and JPO databases.",
        "impact": "Located exact 2014 prior-art diagram in Japanese patent archive within 48 hours; lawsuit dismissed with prejudice, saving $120M in licensing damages.",
        "script": (
            "[Prof. Peter] Slide 36 presents \"CASE STUDY 4: SEMICONDUCTOR PATENT INFRINGEMENT PRIOR-ART DEFENSE.\"\n\n"
            "[TA Sarah] A leading Silicon Valley semiconductor fab was hit with a 120-million-dollar patent infringement lawsuit threatening their flagship 3-nanometer chip production line. The plaintiff claimed exclusive rights to a specific transistor gate layout!\n\n"
            "[TA James] Their legal defense team had exactly three weeks to find 'prior art'—a published document anywhere in the world proving the invention was already public before the patent filing date. Searching through 500,000 global patent filings in English, German, Japanese, and Chinese was humanly impossible!\n\n"
            "[Prof. Peter] They deployed a specialized multi-lingual RAG pipeline using Gemini's multi-modal embeddings across global patent databases.\n\n"
            "[TA Sarah] In just 48 hours, the system retrieved an obscure 2014 Japanese Patent Office filing containing the exact transistor diagram! The court dismissed the lawsuit with prejudice, saving the company 120 million dollars.\n\n"
            "[TA James] Let us see how university research bridges to market leadership on Slide 37!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 4: 반도체 1억 2천만 달러 특허 소송을 기각시킨 선행기술 검색",
            "points": [
                "문제 상황: 3나노 반도체 트랜지스터 특허 침해 소송 발생, 3주 내 전 세계 50만 건 특허에서 선행기술(Prior Art) 발굴 필수",
                "솔루션: 다국어(영/독/일/중) 특허 도면 및 청구항을 동시 분석하는 제미나이 멀티모달 RAG 구축",
                "성과: 48시간 만에 2014년 일본 특허청 선행 도면 발견, 소송 완전 기각(Dismissed with Prejudice) 및 1억 2천만 달러 방어"
            ],
            "tips": "사라 조교와 제임스 조교가 전 세계 특허 데이터 검색의 기술적 난이도와 극적인 승소 결과를 흥미진진하게 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Prior Art",
                "def": "Any evidence that an invention was already known or published before a patent's filing date, invalidating the patent.",
                "defKo": "선행 기술 (특허 무효화 증거)"
            },
            {
                "term": "Multi-Lingual Patent Retrieval",
                "def": "Vector-based cross-language search mapping patents in diverse languages into a single conceptual embedding space.",
                "defKo": "다국어 특허 교차 검색"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 37: The Career Bridge: Classroom to Market
    {
        "num": 37,
        "type": "content",
        "title": "THE CAREER BRIDGE: CLASSROOM TO MARKET",
        "subtitle": "How mastering enterprise RAG architecture elevates students into high-demand AI engineers",
        "points": [
            "High-Value Skillset: Enterprise RAG engineering is among the most sought-after competencies globally.",
            "Portfolio Artifacts: Building private knowledge factories provides tangible, verifiable proof of mastery.",
            "Strategic Leadership: Positioning yourself not as a prompt typist, but as an enterprise knowledge architect."
        ],
        "script": (
            "[TA Sarah] Slide 37 highlights \"THE CAREER BRIDGE: CLASSROOM TO MARKET.\" For every student in this course, what you learn today transforms your professional career!\n\n"
            "[TA James] Right now, companies in every industry—finance, healthcare, legal, logistics, and tech—are desperate for engineers who know how to build secure, zero-hallucination RAG pipelines. Anyone can type a ChatGPT prompt, but very few know how to configure CMEK keys, HNSW indices, and compliance firewalls!\n\n"
            "[Prof. Peter] When you build your private knowledge factory in tonight's lab, you create a living portfolio artifact. You can demonstrate to future employers and executive boards that you are an architect of intelligence.\n\n"
            "[TA Sarah] Let us inspect the Sovereign Conductor paradigm and Human-on-the-Loop governance on Slide 38."
        ),
        "koreanGuide": {
            "summary": "커리어 브릿지: 강의실의 배움을 시장 최고의 고부가가치 AI 아키텍트로 연결",
            "points": [
                "엔터프라이즈 RAG 엔지니어의 폭발적 수요: 단순 프롬프트 작성자를 넘어선 보안/인프라/RAG 아키텍트",
                "포트폴리오 자산화: 오늘 실습에서 구축할 사설 지식 공장이 취업과 이직의 결정적 실증 증거가 됨",
                "기업 지식 총괄 설계자로서의 전략적 리더십 확립"
            ],
            "tips": "제임스 조교가 채용 시장의 실제 수요를 전달하며 수강생들의 학업 성취욕을 고취합니다."
        },
        "keyTerms": [
            {
                "term": "Enterprise RAG Engineer",
                "def": "A high-demand technical specialist designing secure, scalable, and citation-anchored retrieval systems.",
                "defKo": "엔터프라이즈 RAG 엔지니어"
            },
            {
                "term": "Portfolio Artifact",
                "def": "A verifiable, functioning technical project demonstrating hands-on architectural competence to stakeholders.",
                "defKo": "실증 포트폴리오 산출물"
            }
        ]
    },
    # Slide 38: The Sovereign Conductor: Human-on-the-Loop
    {
        "num": 38,
        "type": "content",
        "title": "THE SOVEREIGN CONDUCTOR: HUMAN-ON-THE-LOOP",
        "subtitle": "Maintaining supreme human governance over automated retrieval, reasoning, and synthesis",
        "points": [
            "Conductor Metaphor: The human conducts the orchestra of agents, deciding tempo, harmony, and final approval.",
            "HOTL Governance: Autonomous pipelines run background synthesis; humans validate executive actions.",
            "Unconditional Accountability: Moral, legal, and theological responsibility remains forever with the human architect."
        ],
        "script": (
            "[Prof. Peter] Slide 38 diagrams \"THE SOVEREIGN CONDUCTOR: HUMAN-ON-THE-LOOP (HOTL).\" Look at the conductor standing before the orchestra.\n\n"
            "[TA Sarah] The conductor does not play the violin, the trumpet, or the drums. Each musician—each specialized AI agent—executes their specialized part with virtuosity. But the conductor shapes the tempo, balances the harmony, and ensures the entire symphony serves the master composer!\n\n"
            "[TA James] In our IT architecture, the human architect is the Sovereign Conductor! The agents handle ingestion, vectorization, and draft synthesis 24/7. But when an executive action, client proposal, or financial decision is made, the human on the loop reviews the cited evidence and provides final signature authorization.\n\n"
            "[Prof. Peter] You never abdicate moral or legal responsibility to an algorithm.\n\n"
            "[TA Sarah] Let us explore how time redemption restores true rest on Slide 39!"
        ),
        "koreanGuide": {
            "summary": "주권적 지휘자: 인간 중심 거버넌스(HOTL)와 오케스트라 메타포",
            "points": [
                "지휘자 메타포: 직접 모든 악기를 연주하지 않고 각 에이전트의 화음과 템포를 조율하고 최종 승인",
                "Human-on-the-Loop(HOTL): 백그라운드 합성은 에이전트가 수행하되 핵심 결정은 인간 지휘자가 서명",
                "도덕적/법적 책임의 불변성: 알고리즘에 책임을 떠넘기지 않는 주권적 청지기 거버넌스"
            ],
            "tips": "피터 교수가 오케스트라 지휘자 비유를 통해 수강생들에게 시스템 총괄자로서의 품격을 심어줍니다."
        },
        "keyTerms": [
            {
                "term": "Sovereign Conductor",
                "def": "The human architect who orchestrates, governs, and authorizes the workflows of multiple autonomous AI agents.",
                "defKo": "주권적 지휘자 (시스템 총괄 감독관)"
            },
            {
                "term": "HOTL (Human-on-the-Loop)",
                "def": "A governance model where humans monitor automated processes and intervene only for critical decision milestones.",
                "defKo": "HOTL (루프 상의 인간 감독 체계)"
            }
        ]
    },
    # Slide 39: Reclaiming the Sabbath: Deep Peace
    {
        "num": 39,
        "type": "content",
        "title": "RECLAIMING THE SABBATH: DEEP PEACE",
        "subtitle": "Liberating human life from non-stop digital burnout to enjoy restorative rest and worship",
        "points": [
            "The Burning Trap: Constant connectivity leads to spiritual exhaustion, broken families, and anxiety.",
            "Automated Guardians: Trusting your grounded knowledge factory to protect institutional continuity.",
            "Restorative Rest: Experiencing the biblical peace of Sabbath rest while systems run securely."
        ],
        "script": (
            "[Prof. Peter] Slide 39 reflects on \"RECLAIMING THE SABBATH: DEEP PEACE.\" Why did God give humanity the commandment of Sabbath rest?\n\n"
            "[TA Sarah] Because we are created as relational, spiritual beings—not as mechanical production cogs! When professionals work 7 days a week, staring at email alerts at 2 AM on Sunday, their souls burn out and their creative spirit dies.\n\n"
            "[TA James] When you build a bulletproof private knowledge factory with grounded citations, your systems monitor your data, answer routine queries, and triage incoming reports with total fidelity. You can turn off your laptop on Friday evening and rest completely in peace!\n\n"
            "[Prof. Peter] Redeeming human time to enjoy true peace and worship God is the ultimate fruit of faithful engineering.\n\n"
            "[TA Sarah] Let us declare our eternal motto on Slide 40: Soli Deo Gloria!"
        ),
        "koreanGuide": {
            "summary": "안식의 회복: 24시간 번아웃에서 벗어나 진정한 쉼과 예배를 누리는 삶",
            "points": [
                "안식일의 영적 본질: 인간은 끊임없이 돌아가는 기계 톱니바퀴가 아니라 존엄한 영적 존재",
                "시스템의 든든한 수호: 견고한 지식 공장이 배경 업무를 지켜주므로 주말에 스크린을 끄고 온전히 쉼",
                "회복된 시간의 영적 가치: 가족과의 교제, 기도, 예배에 온전히 몰입하는 평안"
            ],
            "tips": "피터 교수와 조교들이 기술의 궁극적 목적이 인간의 평안과 하나님께 영광을 돌리는 데 있음을 전합니다."
        },
        "keyTerms": [
            {
                "term": "Sabbath Rest",
                "def": "The intentional cessation of mechanical labor to cultivate spiritual renewal, worship, and family restoration.",
                "defKo": "안식의 회복 (거룩한 쉼)"
            },
            {
                "term": "Digital Detachment",
                "def": "The deliberate discipline of unplugging from digital networks enabled by trustworthy automated systems.",
                "defKo": "디지털 단절과 회복"
            }
        ]
    },
    # Slide 40: Soli Deo Gloria: The Zenith of Truth
    {
        "num": 40,
        "type": "content",
        "title": "SOLI DEO GLORIA: THE ZENITH OF TRUTH",
        "subtitle": "Dedicating our intellectual mastery, technological precision, and grounded knowledge to God Alone",
        "points": [
            "Soli Deo Gloria: To God Alone Be the Glory—the bedrock philosophy of Oikos University.",
            "The Sanctity of Truth: Building truthful, uncorrupted systems that reflect divine integrity in code.",
            "Eternal Calling: Transforming daily engineering work into a holy calling of stewardship and excellence."
        ],
        "script": (
            "[Prof. Peter] Slide 40 proclaims our foundation: \"SOLI DEO GLORIA: THE ZENITH OF TRUTH: To God Alone Be the Glory.\"\n\n"
            "[TA Sarah] In everything we build—from high-dimensional vector embeddings to cryptographic audit logs—we pursue excellence because truth is sacred.\n\n"
            "[TA James] When we write clean code that protects privacy, eliminates lies, and redeems wasted hours, our engineering becomes an act of worship and stewardship!\n\n"
            "[Prof. Peter] Let our knowledge factories always serve truth, empower the vulnerable, and glorify our Creator.\n\n"
            "[TA Sarah] Let us inspect how to structure your personal Life OS knowledge factory on Slide 41!"
        ),
        "koreanGuide": {
            "summary": "Soli Deo Gloria: 오직 하나님께 영광을 돌리는 진리의 정점",
            "points": [
                "오직 하나님께 영광(Soli Deo Gloria): Oikos University와 스마트 인사이트 랩의 영원한 기초",
                "진리의 거룩함: 거짓과 날조를 배격하고 정직한 코드로 신적 진실성을 구현",
                "엔지니어링의 성화: 일상의 코딩과 시스템 구축을 거룩한 청지기적 소명으로 승화"
            ],
            "tips": "3명의 강사진이 한마음으로 진리와 신앙의 일치를 엄숙하고 웅장하게 선언합니다."
        },
        "keyTerms": [
            {
                "term": "Soli Deo Gloria",
                "def": "The foundational theological motto dedicating all intellectual and technological mastery to the Glory of God Alone.",
                "defKo": "솔리 데오 글로리아 (오직 하나님께 영광)"
            },
            {
                "term": "Truth Sanctity",
                "def": "The ethical conviction that truth and factual integrity must be uncompromisingly preserved across all software systems.",
                "defKo": "진리의 거룩성 (무결성 원칙)"
            }
        ]
    },
    # Slide 41: Life OS Knowledge Factory: Structuring Your Vault
    {
        "num": 41,
        "type": "content",
        "title": "LIFE OS KNOWLEDGE FACTORY: STRUCTURING YOUR VAULT",
        "subtitle": "Practical directory setup: 01_Sources, 02_Notebooks, 03_Audio_Briefs, 04_Exports",
        "points": [
            "01_Sources: Raw verified PDFs, audio files, spreadsheets, and literature notes.",
            "02_Notebooks: Topic-specific Google NotebookLM enclaves with customized system personas.",
            "03_Audio_Briefs: Automated conversational MP3 podcast overviews generated weekly.",
            "04_Exports: Final verified decision memos, research papers, and slide decks."
        ],
        "script": (
            "[TA Sarah] Slide 41 provides the concrete blueprint: \"LIFE OS KNOWLEDGE FACTORY: STRUCTURING YOUR VAULT.\"\n\n"
            "[TA James] Look at the 4-folder structure on screen: Folder `01_Sources` holds your clean raw files—PDFs, spreadsheets, and reading notes. Folder `02_Notebooks` contains your topic-specific NotebookLM enclaves—Finance, Engineering, Theology, and Strategy.\n\n"
            "[TA Sarah] Folder `03_Audio_Briefs` collects your generated MP3 podcast overviews for on-the-go listening during your morning walk. And Folder `04_Exports` archives your final cited decision memos and slide decks!\n\n"
            "[Prof. Peter] When your digital life is structured into clean modular vaults, friction disappears and creative synthesis thrives.\n\n"
            "[TA James] Let us review our Pre-Deployment Production Checklist on Slide 42!"
        ),
        "koreanGuide": {
            "summary": "라이프 OS 지식 공장: 4대 디렉터리(Sources, Notebooks, Audio, Exports) 구축 가이드",
            "points": [
                "01_Sources: 검증된 원본 PDF, 스프레드시트, 연구 논문 보관소",
                "02_Notebooks: 주제별(금융, 엔지니어링, 신학, 전략)로 격리된 NotebookLM 엔클레이브",
                "03_Audio_Briefs: 출퇴근 및 산책 시 청취할 주간 자동 생성 MP3 팟캐스트 저장소",
                "04_Exports: 최종 인용 검증이 완료된 의사결정 메모 및 발표 자료 아카이브"
            ],
            "tips": "제임스 조교가 수강생들이 당장 오늘 밤 자신의 구글 드라이브에 구축할 수 있도록 실용적으로 안내합니다."
        },
        "keyTerms": [
            {
                "term": "Life OS Vault",
                "def": "A modular, organized personal directory framework integrating raw sources, active notebooks, audio synthesis, and final exports.",
                "defKo": "라이프 OS 지식 금고 (개인 지식 공장)"
            },
            {
                "term": "Modular Enclave",
                "def": "Isolated topical partitions preventing cross-domain noise and preserving clean semantic context.",
                "defKo": "모듈식 주제별 엔클레이브"
            }
        ]
    },
    # Slide 42: Production Checklist: Pre-Deployment Verification
    {
        "num": 42,
        "type": "content",
        "title": "PRODUCTION CHECKLIST: PRE-DEPLOYMENT VERIFICATION",
        "subtitle": "The 6-step quality and security gate every private knowledge factory must pass",
        "points": [
            "Gate 1: Zero-Training policy verified across enterprise tenant agreements.",
            "Gate 2: CMEK customer encryption keys active on all storage buckets.",
            "Gate 3: PII redaction filters tested and validated against synthetic test data.",
            "Gate 4: Source citation enforcement verified with 100% footnote coverage.",
            "Gate 5: SHA-256 immutable audit logging active on SQLite/BigQuery ledger.",
            "Gate 6: Human-on-the-Loop review protocols established for executive outputs."
        ],
        "script": (
            "[TA James] Slide 42 presents our \"PRODUCTION CHECKLIST: PRE-DEPLOYMENT VERIFICATION.\"\n\n"
            "[TA Sarah] Before any RAG knowledge factory is approved for enterprise production, it must pass all 6 security and quality gates!\n\n"
            "[TA James] Gate 1: Zero-Training policy confirmed. Gate 2: CMEK encryption keys active. Gate 3: PII redaction verified. Gate 4: 100% citation enforcement active. Gate 5: SHA-256 audit logging enabled. And Gate 6: Human-on-the-Loop review sign-offs established!\n\n"
            "[Prof. Peter] If any single gate fails, the system stays in staging. Rigorous verification is what builds enduring enterprise trust.\n\n"
            "[TA Sarah] Let us inspect the Architect's Ethical Mandate on Slide 43."
        ),
        "koreanGuide": {
            "summary": "프로덕션 체크리스트: 엔터프라이즈 RAG 배포 전 6대 품질/보안 관문",
            "points": [
                "1관문: 무학습 정책(Zero-Training) 엔터프라이즈 계약 확인",
                "2관문: CMEK 고객 관리 암호화 키 활성화",
                "3관문: 개인정보(PII) 자동 마스킹 필터 검증",
                "4관문: 100% 인라인 인용 및 각주 강제화",
                "5관문: SHA-256 불변 감사 로그 적재 확인",
                "6관문: Human-on-the-Loop 인간 최종 승인 절차 수립"
            ],
            "tips": "제임스 조교가 6대 관문을 체크리스트 형태로 단호하고 정확하게 짚어줍니다."
        },
        "keyTerms": [
            {
                "term": "Quality Gate",
                "def": "A mandatory verification checkpoint that a software system must satisfy before progressing to production deployment.",
                "defKo": "품질/보안 관문 (배포 전 검증 체크포인트)"
            },
            {
                "term": "Staging Perimeter",
                "def": "An isolated pre-production environment used to stress-test software security and accuracy before live release.",
                "defKo": "스테이징 검증 환경"
            }
        ]
    },
    # Slide 43: The Architect's Ethical Mandate
    {
        "num": 43,
        "type": "content",
        "title": "THE ARCHITECT'S ETHICAL MANDATE",
        "subtitle": "Protecting truth, elevating human dignity, and building incorruptible systems",
        "points": [
            "Fiduciary Responsibility: Treating user and organizational data with absolute confidentiality.",
            "Anti-Hallucination Integrity: Rejecting fabricated or unverified claims in public and private reporting.",
            "Human Flourishing: Designing IT architectures that restore human vitality rather than draining attention."
        ],
        "script": (
            "[Prof. Peter] Slide 43 defines \"THE ARCHITECT'S ETHICAL MANDATE.\" Knowledge is power, and power without ethical constraints inevitably leads to corruption.\n\n"
            "[TA Sarah] As certified Intelligence Architects from Oikos University, we hold a sacred fiduciary trust: to protect confidentiality, to speak truth, and to reject unverified AI fabrications.\n\n"
            "[TA James] We build systems that liberate our colleagues from burnout, protect our organizations from legal hazards, and elevate human dignity across every line of code!\n\n"
            "[Prof. Peter] Let us inspect our final enterprise case study on Slide 44!"
        ),
        "koreanGuide": {
            "summary": "지능 건축가의 윤리적 사명: 진리 수호, 인간 존엄성 증진, 무결한 시스템 구축",
            "points": [
                "수탁자 책임: 사용자 및 기업 데이터를 절대적 비밀로 보호하는 직업 윤리",
                "무환각 무결성: 날조되거나 검증되지 않은 AI 생성물을 공공 및 사내에 유포하지 않는 정직성",
                "인간 번영: 인간의 주의력을 고갈시키는 것이 아닌, 활력과 존엄성을 회복시키는 기술 설계"
            ],
            "tips": "피터 교수와 조교들이 지능 건축가로서의 긍지와 윤리적 소명 의식을 고취합니다."
        },
        "keyTerms": [
            {
                "term": "Ethical Mandate",
                "def": "The moral obligation of software architects to design honest, secure, and human-affirming technical systems.",
                "defKo": "윤리적 사명 (건축가 윤리 강령)"
            },
            {
                "term": "Human Flourishing",
                "def": "The ultimate social objective of technology: enhancing human health, wisdom, relationships, and well-being.",
                "defKo": "인간의 온전한 번영 (휴먼 플로리싱)"
            }
        ]
    },
    # Slide 44: Case Study 5: 15X Enterprise Research ROI & Deployment Blueprint
    {
        "num": 44,
        "type": "casestudy",
        "title": "CASE STUDY 5: 15X ENTERPRISE ROI BLUEPRINT",
        "subtitle": "Global Consulting Group deploys 500 NotebookLM private knowledge factories worldwide",
        "company": "Global Top-3 Management Consulting Firm",
        "problem": "3,000 global strategy consultants spent 30% of billable hours searching through 15 years of past engagement decks, case studies, and proprietary industry benchmarks.",
        "solution": "Deployed 500 centralized Google NotebookLM enterprise vaults integrated with Shared Google Drives, role-based RBAC, and automated weekly Audio Overview synthesis.",
        "impact": "15X measured research ROI; reclaimed 450,000 billable consulting hours annually ($135M value); client proposal win-rate surged by 28%.",
        "script": (
            "[Prof. Peter] Slide 44 presents our capstone enterprise case study: \"CASE STUDY 5: 15X ENTERPRISE ROI BLUEPRINT.\"\n\n"
            "[TA Sarah] A global top-3 management consulting firm with 3,000 strategy consultants faced a massive knowledge reuse problem. They had 15 years of brilliant past engagement decks, benchmarks, and frameworks, but consultants were constantly reinventing the wheel because the archives were unsearchable!\n\n"
            "[TA James] They deployed 500 private NotebookLM knowledge factories connected to Shared Google Drives with strict RBAC access controls. Every Monday morning, the system generates custom 10-minute Audio Overview briefings for practice leaders on newly completed projects worldwide!\n\n"
            "[Prof. Peter] Look at the enterprise metrics: 15X measured ROI! They reclaimed over 450,000 consulting hours annually—worth 135 million dollars in billable capacity—and their client proposal win-rate jumped by 28% because pitches were backed by 15 years of cited proof!\n\n"
            "[TA Sarah] That is the ultimate validation of Grounded Intelligence.\n\n"
            "[TA James] Now, let us roll up our sleeves and build your own private knowledge factory in Lab 4 on Slide 45!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 5: 글로벌 전략 컨설팅사의 15배 ROI 및 5단계 배포 청사진",
            "points": [
                "문제 상황: 3,000명의 컨설턴트가 15년간 축적된 과거 프로젝트 자료를 찾지 못해 바퀴를 재발명하며 청구 가능 시간의 30%를 낭비",
                "솔루션: 500개의 사설 NotebookLM 지식 금고 구축 및 매주 월요일 맞춤형 오디오 브리핑 자동 발송",
                "성과: 연간 45만 시간(1억 3,500만 달러 상당) 회복, 15배 ROI 달성, 제안서 수주율 28% 상승"
            ],
            "tips": "사라 조교와 제임스 조교가 15배 ROI의 구체적인 수치와 비즈니스 효과를 강조하며 실습으로 유도합니다."
        },
        "keyTerms": [
            {
                "term": "Knowledge Reuse Leverage",
                "def": "The multiplication of organizational productivity achieved by effortlessly surfacing and repurposing historical intellectual assets.",
                "defKo": "지식 재활용 레버리지"
            },
            {
                "term": "Billable Hour Recovery",
                "def": "The monetary value recaptured by liberating professional workers from non-billable administrative search tasks.",
                "defKo": "청구 가능 시간 회수 가치"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 45: Hands-on Lab 4 & Conclusion
    {
        "num": 45,
        "type": "lab",
        "title": "🛠️ HANDS-ON LAB 4 & CONCLUSION",
        "subtitle": "Architecting your private Google NotebookLM knowledge factory with verified citations",
        "mission": "Deploy your first private knowledge factory in Google NotebookLM: Ingest 5 diverse sources (PDF, Docs, YouTube), generate an Audio Overview, test strict citation queries, and audit verifiable footnotes.",
        "steps": [
            "Step 1: Open Google NotebookLM and create a new notebook titled 'Life_OS_Knowledge_Factory'.",
            "Step 2: Upload 3 diverse PDFs (research papers, reports) and attach 1 YouTube lecture URL.",
            "Step 3: Generate a 2-Presenter Audio Overview podcast and listen to the conversational synthesis.",
            "Step 4: Execute 3 complex factual queries and verify that every response includes clickable source citations.",
            "Step 5: Export a 1-page executive decision memo to Google Docs with full footnote integrity."
        ],
        "script": (
            "[TA Sarah] Here we are at Slide 45: \"🛠️ HANDS-ON LAB 4 & SESSION CONCLUSION!\"\n\n"
            "[TA James] Tonight's mission is hands-on and thrilling! Step 1: Open Google NotebookLM and create a notebook named `Life_OS_Knowledge_Factory`. Step 2: Upload 3 PDFs and a YouTube lecture URL. Step 3: Generate your first 2-Presenter Audio Overview podcast! Step 4: Run 3 complex queries and audit the clickable citations. Step 5: Export a verified 1-page executive memo to Google Docs!\n\n"
            "[Prof. Peter] As we always proclaim at Oikos University: theory informs, but engineering transforms! Once you build your first grounded knowledge factory, you will never look at AI the same way again.\n\n"
            "[TA Sarah] In our next session, Session 5, we will take this knowledge factory and connect it directly to Enterprise Google Drive and Google Apps Script automation!\n\n"
            "[Prof. Peter] On behalf of TA Sarah Jenkins, TA James Wilson, and the entire Smart Insight Lab, congratulations on mastering Session 4! Soli Deo Gloria, and we will see you in Session 5!"
        ),
        "koreanGuide": {
            "summary": "실습 과제 4 및 세션 마무리: 나만의 사설 NotebookLM 지식 공장 구축",
            "points": [
                "실습 미션: 구글 NotebookLM에 'Life_OS_Knowledge_Factory'를 개설하고 5개 이상의 다양한 소스(PDF, 유튜브 등) 적재",
                "오디오 오버뷰 팟캐스트 생성 및 청취를 통한 멀티모달 합성 체험",
                "복합 질의를 수행하고 클릭 가능한 인용 각주의 정확성을 직접 검증 후 구글 문서로 최종 브리핑 내보내기"
            ],
            "tips": "3인의 강사진이 오늘 수업의 성취를 축하하고 다음 세션(Session 5: 드라이브 & GAS 자동화)에 대한 기대감을 높이며 마무리합니다."
        },
        "keyTerms": [
            {
                "term": "Hands-on Milestone",
                "def": "The practical engineering completion of a functioning technical artifact fulfilling the session's learning objectives.",
                "defKo": "실습 달성 마일스톤"
            },
            {
                "term": "Executive Memo Export",
                "def": "The formal generation and export of a verified, citation-backed decision document into Google Docs.",
                "defKo": "경영 의사결정 메모 내보내기"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    }
]

def generate_session4_md(slides):
    lines = []
    lines.append("# Session 4: Grounded Intelligence on My Data: The RAG Revolution and Private Knowledge Factories")
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
    new_export = f"export const SLIDES_SESSION_4 = {slides_json};"
    
    pattern = r"export\s+const\s+SLIDES_SESSION_4\s*=\s*\[[\s\S]*?\];"
    if re.search(pattern, content):
        updated_content = re.sub(pattern, lambda m: new_export, content, count=1)
        with open(SLIDES_DATA_JS, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Successfully updated SLIDES_SESSION_4 in slidesData.js!")
    else:
        print("Could not find SLIDES_SESSION_4 pattern in slidesData.js!")

def main():
    print(f"Total slides configured: {len(SLIDES_45_SESSION_4)}")
    
    # Verify part dividers
    part_slides = [s for s in SLIDES_45_SESSION_4 if s['type'] == 'section']
    print(f"Total PART Section Slides: {len(part_slides)}")
    for ps in part_slides:
        print(f"  Slide {ps['num']:02d}: {ps['title']}")
        
    # Verify case studies
    case_slides = [s for s in SLIDES_45_SESSION_4 if 'CASE STUDY' in s['title']]
    print(f"Total Case Study Slides: {len(case_slides)}")
    for cs in case_slides:
        print(f"  Slide {cs['num']:02d}: {cs['title']}")

    # 1. Write session4.md
    session4_md_content = generate_session4_md(SLIDES_45_SESSION_4)
    with open(SESSION4_MD, 'w', encoding='utf-8') as f:
        f.write(session4_md_content)
    print(f"Successfully generated and saved {SESSION4_MD} ({len(session4_md_content)} bytes)")
    
    # 2. Update slidesData.js
    update_slides_data_js(SLIDES_45_SESSION_4)
    
    print("Session 4 generation completed successfully!")

if __name__ == '__main__':
    main()
