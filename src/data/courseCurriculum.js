// Master Course Syllabus and 15-Session Curriculum Data
// Course: The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom
// Oikos University (www.oikos.edu) • Soli Deo Gloria • Prof. Peter Kim

export const COURSE_INFO = {
  courseTitle: "The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom",
  courseTitleKo: "지능의 아키텍트: 에이전틱 IT와 전략적 지혜 마스터",
  institution: "Oikos University (www.oikos.edu)",
  motto: "Soli Deo Gloria (오직 하나님께 영광을)",
  instructor: "Professor Peter Kim, Director of Smart Insight Lab",
  totalSessions: 15,
  totalSlides: 600,
  description: "A comprehensive 15-week masterclass bridging cutting-edge autonomous AI systems, Google Cloud architectures, multi-agent swarms, world simulation, and sovereign human governance under the eternal banner of Soli Deo Gloria.",
  descriptionKo: "최첨단 자율 AI 시스템, 구글 클라우드 아키텍처, 다중 에이전트 군집, 월드 시뮬레이션, 그리고 Soli Deo Gloria 신앙관 아래 인간 주권 거버넌스를 집대성한 15주 완성 마스터 커리큘럼입니다."
};

export const SESSIONS_CURRICULUM = [
  {
    sessionNum: 1,
    title: "Session 1: From Waiting Chatbots to Sleep-Free Personal Avatars",
    titleKo: "1강. 대기형 챗봇에서 24시간 잠들지 않는 개인 아바타로",
    theme: "Autonomous Agent Paradigm Shift",
    learningObjectives: [
      "Deconstruct the paradigm shift from passive synchronous chatbot waiting to proactive, asynchronous cloud agents.",
      "Understand the 3-layer asynchronous event loop (Ingestion ➔ Reasoning ➔ Dispatch) inside Gemini Spark.",
      "Master Google Workspace API connectivity and establish immutable security guardrails for autonomous delegation."
    ],
    learningObjectivesKo: [
      "수동적 챗봇 대기 화면을 넘어 24시간 비동기로 자율 실행되는 개인 아바타 패러다임 이해",
      "Gemini Spark의 3계층(수집-추론-실행) 비동기 이벤트 루프 아키텍처 습득",
      "구글 워크스페이스 연동 및 에이전트 위임 시의 다층 보안 가드레일 확립"
    ],
    parts: [
      {
        partNum: 1,
        slideRange: "Slides 02–10",
        title: "PART 1: THE PARADIGM SHIFT: CHATBOTS TO AVATARS",
        titleKo: "패러다임 대전환: 챗봇에서 수면 없는 아바타로",
        summary: "From passive question-answering chatbots to proactive, goal-driven agents that execute multi-step real-world workflows without human waiting.",
        summaryKo: "텍스트 답변만 주는 수동 챗봇을 벗어나 인간의 대기 시간 없이 실무를 완수하는 자율 실행 에이전트로의 전환",
        keyTopics: ["'Ask Me' vs. 'Run It For Me'", "Reclaiming the Ultimate Currency of Time", "Soli Deo Gloria Foundation"]
      },
      {
        partNum: 2,
        slideRange: "Slides 11–20",
        title: "PART 2: UNDER THE HOOD OF AUTONOMOUS REASONING",
        titleKo: "자율 추론 엔진의 내부 메커니즘",
        summary: "Analyzing Google's TPU v8 clusters, Gemini 3.5 Flash sub-50ms inference loops, and non-blocking asynchronous cloud event triggers.",
        summaryKo: "TPU v8 클러스터와 Gemini 3.5 Flash의 초고속 추론 루프 및 24시간 비동기 백그라운드 이벤트 처리 구조",
        keyTopics: ["TPU v8 Hardware Acceleration", "Synchronous vs. Asynchronous Workflows", "Gemini 3.5 Flash Brain"]
      },
      {
        partNum: 3,
        slideRange: "Slides 21–30",
        title: "PART 3: THE CONNECTED WORKSPACE: APPS SCRIPT & DRIVE",
        titleKo: "연결된 워크스페이스: Apps Script & Drive 연동",
        summary: "Connecting agents natively to Google Drive, Docs, Sheets, and Gmail via Google Apps Script and persistent directory setups.",
        summaryKo: "Google Apps Script(GAS)를 통해 드라이브, 시트, 문서, 지메일을 유기적으로 연결하는 네이티브 워크스페이스 통합",
        keyTopics: ["Spark OS Directory Setup", "Dual Memory Engine", "Virgin Voyages Enterprise Case Study"]
      },
      {
        partNum: 4,
        slideRange: "Slides 31–39",
        title: "PART 4: WISDOM SYNTHESIS: SOLI DEO GLORIA",
        titleKo: "지혜의 통합: Soli Deo Gloria & 인간 주권",
        summary: "Enforcing Human-on-the-Loop governance, prompt injection defenses, and the Sovereign Conductor paradigm under Soli Deo Gloria.",
        summaryKo: "에이전트 다층 방어망, 프롬프트 인젝션 방어, 거부권(Veto Power)을 쥔 인간 주권 거버넌스와 안식의 회복",
        keyTopics: ["The Sovereign Conductor Model", "Prompt Injection Defense", "Human-on-the-Loop (HOTL) Governance"]
      }
    ],
    labMission: "Lab 1: Architect your first 24/7 personal assistant in Google Drive with persistent Spark OS folders.",
    labMissionKo: "Lab 1. 구글 드라이브 내 Spark OS 영속 폴더를 구축하고 24시간 개인 비서 아키텍처 설계"
  },
  {
    sessionNum: 2,
    title: "Session 2: 24/7 Sleep-Free Guardian: Gemini Spark Architecture",
    titleKo: "2강. 24/7 잠들지 않는 수호자: Gemini Spark 아키텍처",
    theme: "Cloud Persistence & Autonomous Event Triggers",
    learningObjectives: [
      "Master the persistent cloud architecture of Gemini Spark running on Google Cloud TPU v8 infrastructure.",
      "Build native cross-application automation connecting Gmail triage, Calendar time-blocking, and Docs report generation.",
      "Deploy cryptographic AP2 digital spending mandates and zero-trust security safeguards."
    ],
    learningObjectivesKo: [
      "Google Cloud TPU v8 기반의 Gemini Spark 클라우드 영속 아키텍처 완전 정복",
      "지메일 자동 분류, 캘린더 시간 블록 확보, 문서 자동 생성을 잇는 크로스 앱 파이프라인 구축",
      "AP2 암호화 결제 위임장과 제로 트러스트 보안 거버넌스 배치"
    ],
    parts: [
      {
        partNum: 1,
        slideRange: "Slides 02–10",
        title: "PART 1: THE 24/7 SLEEP-FREE GUARDIAN PARADIGM",
        titleKo: "24/7 잠들지 않는 수호자 패러다임",
        summary: "Redeeming time (Ephesians 5:16) by delegating round-the-clock email and calendar monitoring to persistent cloud guardians.",
        summaryKo: "24시간 내 메일함과 일정을 감시하고 분류해주는 클라우드 수호자를 통해 거룩한 시간을 구속하는 신앙적 사명",
        keyTopics: ["Ephesians 5:16 Time Redemption", "The Continuous Guardian", "Cognitive Bandwidth Dividend"]
      },
      {
        partNum: 2,
        slideRange: "Slides 11–20",
        title: "PART 2: UNDER THE HOOD OF THE ASYNCHRONOUS ENGINE",
        titleKo: "비동기 엔진의 내부 기술 분석",
        summary: "Deconstructing TPU v8 hardware, Gemini 3.6 Flash reasoning pipelines, and non-blocking background workers.",
        summaryKo: "TPU v8 하드웨어와 Gemini 3.6 Flash 추론 파이프라인, 그리고 논블로킹 백그라운드 워커의 기술적 심층 분석",
        keyTopics: ["TPU v8 Hardware Acceleration", "Sub-50ms Inference Loops", "Asynchronous Event Scheduling"]
      },
      {
        partNum: 3,
        slideRange: "Slides 21–30",
        title: "PART 3: THE CONNECTED WORKSPACE: NATIVE CROSS-APP WORKFLOWS",
        titleKo: "연결된 워크스페이스: 네이티브 크로스 앱 워크플로우",
        summary: "Automating end-to-end business workflows across Gmail, Google Calendar, Google Docs, and Google Sheets without API lag.",
        summaryKo: "지메일 파싱, 캘린더 블록 예약, 구글 문서 생성, 시트 업데이트가 연쇄적으로 작동하는 원스톱 업무 자동화",
        keyTopics: ["Cross-App Data Pipes", "Automated Triage", "Persistent Cloud Context"]
      },
      {
        partNum: 4,
        slideRange: "Slides 31–39",
        title: "PART 4: SECURING THE DIGITAL VAULT: GOVERNANCE & SAFETY",
        titleKo: "디지털 금고 보안: 거버넌스와 안전망",
        summary: "Implementing the AP2 payment protocol, single-use spending mandates, prompt injection sanitization, and audit trails.",
        summaryKo: "AP2 에이전트 결제 프로토콜, 단발성 예산 위임장, 악성 프롬프트 정화 및 불변의 활동 감사 원장 구축",
        keyTopics: ["AP2 Protocol", "Digital Mandate Spending Caps", "Defense-in-Depth"]
      }
    ],
    labMission: "Lab 2: Construct an end-to-end Gemini Spark workflow that ingests student inquiries and updates spreadsheets.",
    labMissionKo: "Lab 2. 학생 문의 메일을 분석하여 구글 시트에 자동 기록하고 회신 초안을 작성하는 Spark 워크플로우 구현"
  },
  {
    sessionNum: 3,
    title: "Session 3: OS Shell Control & 1.2GB Local AI Armor",
    titleKo: "3강. OS 쉘 통제권과 1.2GB 로컬 AI 아머",
    theme: "Local-First AI & Operating System Automation",
    learningObjectives: [
      "Master command-line shell automation using Windows PowerShell and lightweight local LLMs.",
      "Analyze the hardware trade-offs of 1.2GB local models (Gemma 3.5 2B) vs. cloud APIs (RAM, battery, latency).",
      "Deploy Google Lens visual intelligence and secure local directory governance."
    ],
    learningObjectivesKo: [
      "파워쉘(PowerShell) 환경에서 로컬 경량 AI를 결합하여 OS 파일과 프로세스를 직접 제어",
      "1.2GB 로컬 모델(Gemma 3.5 2B)과 클라우드 API의 메모리, 배터리, 레이턴시 하드웨어 트레이드오프 분석",
      "Google Lens 시각 지능 결합 및 로컬 디렉토리 보안 거버넌스 수립"
    ],
    parts: [
      {
        partNum: 1,
        slideRange: "Slides 02–10",
        title: "PART 1: THE LOCAL-FIRST PARADIGM & SHELL CONTROL",
        titleKo: "로컬 퍼스트 패러다임과 쉘 통제권",
        summary: "The First Keystroke Paradigm: Reclaiming terminal command-line sovereignty from restrictive web GUIs under Soli Deo Gloria.",
        summaryKo: "웹 GUI의 한계를 벗어나 검은 터미널 창에서 직접 OS를 지휘하는 첫 번째 키스트로크 주권 회복",
        keyTopics: ["First Keystroke Paradigm", "Terminal vs. Web GUI", "Zero Cloud Data Leakage"]
      },
      {
        partNum: 2,
        slideRange: "Slides 11–20",
        title: "PART 2: DECONSTRUCTING THE 1.2GB HEAVY ARMOR",
        titleKo: "1.2GB 로컬 아머의 하드웨어 분석",
        summary: "Analyzing WebView2 baselines, 1.2GB RAM footprints, GPU acceleration, and local model quantization techniques.",
        summaryKo: "1.2GB 모델의 RAM 점유율, GPU 가속, 배터리 소모 최적화 및 로컬 양자화 기술 심층 분석",
        keyTopics: ["Gemma 3.5 2B Quantization", "RAM & Battery Baselines", "Local Inference Benchmarks"]
      },
      {
        partNum: 3,
        slideRange: "Slides 21–30",
        title: "PART 3: THE OMNISCIENT EYE: LENS & GEMINI",
        titleKo: "모든 것을 보는 눈: Lens & Gemini 결합",
        summary: "Combining screen OCR, real-time image understanding, and multimodal reasoning to automate repetitive desktop workflows.",
        summaryKo: "화면 캡처 OCR과 멀티모달 추론을 결합하여 복잡한 데스크톱 파일 정리 및 서식 변환 자동화",
        keyTopics: ["Screen Scraping Intelligence", "Multimodal OCR Pipelines", "Automated File Sorting"]
      },
      {
        partNum: 4,
        slideRange: "Slides 31–39",
        title: "PART 4: GOVERNANCE AND THE SHADOW KINGDOM",
        titleKo: "거버넌스와 섀도우 킹덤 방어",
        summary: "Eliminating local Shadow IT risks, preventing accidental file deletion, and enforcing human-signed shell scripts.",
        summaryKo: "로컬 섀도우 IT 위험 차단, 무단 파일 삭제 방지, 인간 서명 기반의 안전한 쉘 스크립트 실행 체계",
        keyTopics: ["Local Sandbox Isolation", "Accidental Deletion Guards", "Human Veto Shell Scripts"]
      }
    ],
    labMission: "Lab 3: Build a PowerShell script integrating Gemma 3.5 to auto-sort and categorize 100 messy desktop files.",
    labMissionKo: "Lab 3. Gemma 3.5 로컬 AI와 파워쉘을 연동하여 바탕화면의 난잡한 파일 100개를 자동 분류하는 스크립트 작성"
  },
  {
    sessionNum: 4,
    title: "Session 4: Honest Intelligence: NotebookLM RAG Revolution",
    titleKo: "4강. 정직한 지능: NotebookLM과 RAG 혁명",
    theme: "Grounded RAG & Hallucination Elimination",
    learningObjectives: [
      "Deconstruct why probabilistic LLMs hallucinate and how Retrieval-Augmented Generation (RAG) enforces honest truth.",
      "Master Google NotebookLM's source-grounded vector embedding architecture and audio overview generation.",
      "Establish enterprise Shared Drive knowledge governance with 100% verifiable citations."
    ],
    learningObjectivesKo: [
      "확률적 언어 모델의 치명적 환각 원인 규명 및 검색 증강 생성(RAG)의 무환각 원리 습득",
      "Google NotebookLM의 출처 기반 벡터 임베딩 아키텍처 및 오디오 개요(Deep Dive) 합성 마스터",
      "100% 검증 가능한 인용 출처 기반의 엔터프라이즈 공유 드라이브 지식 거버넌스 수립"
    ],
    parts: [
      {
        partNum: 1,
        slideRange: "Slides 02–10",
        title: "PART 1: THE CRISIS OF HALLUCINATION & HONEST INTELLIGENCE",
        titleKo: "환각의 위기와 정직한 지능",
        summary: "The Core Mission: Soli Deo Gloria and why probabilistic AI hallucinations destroy corporate, legal, and academic trust.",
        summaryKo: "출처 없는 가짜 정보와 환각이 초래하는 신뢰의 붕괴를 진단의 진실과 출처 중심의 정직한 지능 추구",
        keyTopics: ["Probabilistic Next-Token Risk", "The Cost of Hallucination", "Grounded Truth under Soli Deo Gloria"]
      },
      {
        partNum: 2,
        slideRange: "Slides 11–20",
        title: "PART 2: SYSTEM ARCHITECTURE: INSIDE THE RAG ENGINE",
        titleKo: "RAG 엔진의 내부 시스템 아키텍처",
        summary: "How document chunking, high-dimensional vector embeddings, and cosine similarity search retrieve exact source truths.",
        summaryKo: "문서 청킹, 고차원 벡터 임베딩, 코사인 유사도 검색을 통해 정확한 출처 본문만을 모델에 주입하는 RAG 원리",
        keyTopics: ["Vector Embeddings", "Cosine Similarity Search", "Sub-Second Ingestion Pipelines"]
      },
      {
        partNum: 3,
        slideRange: "Slides 21–30",
        title: "PART 3: TRUST, PRIVACY, AND ENTERPRISE GOVERNANCE",
        titleKo: "신뢰, 프라이버시, 그리고 기업 거버넌스",
        summary: "Ensuring company confidential PDFs are never leaked to public training pools; enterprise zero-retention policies.",
        summaryKo: "기업 기밀 문서가 외부 모델 재학습에 쓰이지 않도록 보장하는 제로 리텐션 프라이버시와 권한 격리",
        keyTopics: ["Zero Data Retention", "Shared Drive Sovereignty", "Granular Access Control"]
      },
      {
        partNum: 4,
        slideRange: "Slides 31–39",
        title: "PART 4: WISDOM SYNTHESIS: RECLAIMING SOVEREIGNTY",
        titleKo: "지혜의 통합: 인간 주권과 지식 청지기직",
        summary: "Using NotebookLM to transform dense academic papers into conversational podcasts and verified executive briefs.",
        summaryKo: "수백 페이지의 논문과 법률 문서를 신뢰할 수 있는 팟캐스트 요약과 브리핑으로 변환하는 학술 청지기직",
        keyTopics: ["Audio Overview Generation", "Scholar's Deep Dive", "Permanent Knowledge Vaults"]
      }
    ],
    labMission: "Lab 4: Create a NotebookLM Grounded Knowledge Vault containing 10 complex PDFs and generate verified study guides.",
    labMissionKo: "Lab 4. 10개의 복잡한 전공 논문/교재를 NotebookLM에 탑재하여 100% 출처가 인용된 시험 대비 요약본 생성"
  },
  {
    sessionNum: 5,
    title: "Session 5: Enterprise Drive Mastery & GAS Automation",
    titleKo: "5강. 엔터프라이즈 드라이브 마스터리와 GAS 자동화",
    theme: "Cloud Knowledge Taxonomy & Google Apps Script",
    learningObjectives: [
      "Transform disorganized cloud storage into a secure, structured Enterprise Knowledge Vault.",
      "Master Google Apps Script (GAS) to automate file streaming, metadata tagging, and auto-archiving.",
      "Enforce the Principle of Least Privilege and prevent corporate data exfiltration."
    ],
    learningObjectivesKo: [
      "무질서한 클라우드 저장소를 체계적이고 안전한 전사적 지식 볼트(Vault)로 재구축",
      "Google Apps Script(GAS)를 작성하여 파일 스트리밍, 메타데이터 태깅, 자동 아카이빙 구현",
      "최소 권한의 원칙(Least Privilege)을 적용하여 기업 데이터 유출 원천 차단"
    ],
    parts: [
      {
        partNum: 1,
        slideRange: "Slides 02–10",
        title: "PART 1: THE ENTERPRISE DRIVE REVOLUTION & KNOWLEDGE VAULT",
        titleKo: "엔터프라이즈 드라이브 혁명과 지식 볼트",
        summary: "Soli Deo Gloria: Bringing divine order out of enterprise file chaos; designing strict taxonomies and naming conventions.",
        summaryKo: "폴더와 파일의 난잡한 무질서를 하늘의 법인 질서로 재편하는 표준 디렉토리 택소노미 설계",
        keyTopics: ["Order Out of Chaos", "Strict File Taxonomies", "Collaborative Knowledge Fortresses"]
      },
      {
        partNum: 2,
        slideRange: "Slides 11–20",
        title: "PART 2: DECONSTRUCTING THE SYSTEM VAULT",
        titleKo: "시스템 볼트의 내부 구조 분석",
        summary: "File Streaming vs. Mirroring, metadata schemas, and automated background indexing with Google Drive APIs.",
        summaryKo: "파일 스트리밍 대 미러링의 차이, 메타데이터 스키마 설계 및 구글 드라이브 API 백그라운드 색인",
        keyTopics: ["File Streaming Architecture", "Metadata Schema Design", "Search Index Optimization"]
      },
      {
        partNum: 3,
        slideRange: "Slides 21–30",
        title: "PART 3: STRATEGIC IMPERATIVES & RISK GOVERNANCE",
        titleKo: "전략적 필수 과제와 위험 거버넌스",
        summary: "Enforcing the Least Privilege Principle, preventing unauthorized external link sharing, and audit logging.",
        summaryKo: "최소 권한의 원칙 적용, 무단 외부 링크 공유 방지, 비인가 파일 접근 실시간 감사 추적",
        keyTopics: ["Least Privilege Principle", "Exfiltration Prevention", "Role-Based Access Control"]
      },
      {
        partNum: 4,
        slideRange: "Slides 31–39",
        title: "PART 4: WISDOM SYNTHESIS & APPS SCRIPT AUTOMATION",
        titleKo: "지혜의 통합과 Apps Script 자동화",
        summary: "Writing lightweight Google Apps Scripts to auto-archive stale documents, clean temp folders, and notify team leaders.",
        summaryKo: "오래된 문서를 자동 보관하고 임시 파일을 청소하며 부서장에게 주간 브리핑을 보내는 GAS 코드 작성",
        keyTopics: ["GAS Auto-Archiving", "Time-Driven Cron Triggers", "Reclaiming Administrative Time"]
      }
    ],
    labMission: "Lab 5: Build a GAS script that automatically catalogs incoming invoices in Google Drive and updates a master Sheet.",
    labMissionKo: "Lab 5. 특정 폴더에 인보이스가 업로드되면 메타데이터를 추출해 마스터 시트에 자동 등록하는 GAS 스크립트 작성"
  },
  {
    sessionNum: 6,
    title: "Session 6: 1M Token Context & Vibe Coding",
    titleKo: "6강. 100만 토큰 컨텍스트와 바이브 코딩",
    theme: "Massive Context Windows & Natural Language Development",
    learningObjectives: [
      "Master the 1-million-token horizon of Gemini 3.5 Pro to ingest entire codebases and books simultaneously.",
      "Understand Many-Shot In-Context Learning (ICL) and how providing 50+ examples guarantees deterministic outputs.",
      "Deploy FinOps Context Caching to slash API inference costs and latency by 87%."
    ],
    learningObjectivesKo: [
      "Gemini 3.5 Pro의 100만 토큰 컨텍스트 창을 활용하여 거대한 코드베이스와 책 전체를 한 번에 주입",
      "50개 이상의 예시를 제공하여 모델의 결정론적 정확도를 극대화하는 매니샷 인컨텍스트 러닝(ICL) 습득",
      "클라우드 API 비용과 지연 시간을 87% 절감하는 FinOps 컨텍스트 캐싱 전략 배치"
    ],
    parts: [
      {
        partNum: 1,
        slideRange: "Slides 02–10",
        title: "PART 1: THE 1M-TOKEN HORIZON & THE END OF FRAGMENTATION",
        titleKo: "100만 토큰의 지평선과 데이터 파편화의 종말",
        summary: "Transcending small context windows under Soli Deo Gloria; loading 750,000 words into a single prompt without chunking.",
        summaryKo: "자르고 쪼개던 작은 창의 한계를 벗어나 책 수십 권과 대규모 저장소를 통째로 읽어들이는 1M 토큰 혁명",
        keyTopics: ["The 1M-Token Window", "Ending Vector Chunking Lag", "Divine Creative Synthesis"]
      },
      {
        partNum: 2,
        slideRange: "Slides 11–20",
        title: "PART 2: MANY-SHOT IN-CONTEXT LEARNING (ICL)",
        titleKo: "매니샷 인컨텍스트 러닝 (ICL)",
        summary: "Injecting 50 to 100 input-output exemplars into the prompt to lock the model into exact domain-specific behavior.",
        summaryKo: "50~100개의 입출력 예시를 프롬프트에 제공하여 파인튜닝 없이도 완벽한 맞춤형 코드를 생성하는 매니샷 기법",
        keyTopics: ["Many-Shot Exemplar Set Design", "Wireframes to React in 1 Shot", "Zero Fine-Tuning Overhead"]
      },
      {
        partNum: 3,
        slideRange: "Slides 21–30",
        title: "PART 3: FINOPS & CONTEXT CACHING STRATEGIES",
        titleKo: "FinOps와 컨텍스트 캐싱 전략",
        summary: "Using Google Cloud Context Caching to freeze static system tokens in GPU memory, cutting repeat costs by 87%.",
        summaryKo: "정적 데이터와 거대 코드베이스를 GPU 메모리에 캐싱하여 반복 쿼리 비용과 속도를 87% 절감하는 FinOps 전략",
        keyTopics: ["87% Cost Reduction via Caching", "Model Routing (Pro vs. Flash)", "Temperature Dial Tuning"]
      },
      {
        partNum: 4,
        slideRange: "Slides 31–39",
        title: "PART 4: VIBE CODING & ENTERPRISE GOVERNANCE",
        titleKo: "바이브 코딩과 엔터프라이즈 거버넌스",
        summary: "Using natural language to generate disposable bespoke micro-utilities; rapid deployment with strict review gates.",
        summaryKo: "자연어로 1회성 맞춤 마이크로 도구를 즉석 제작하는 바이브 코딩과 휴먼 리뷰 게이트 거버넌스",
        keyTopics: ["Natural Language Vibe Coding", "Bespoke Disposable Tools", "Human Review-Driven Development"]
      }
    ],
    labMission: "Lab 6: Build an Instant Expert Forge in Google AI Studio using 50 exemplars and Context Caching.",
    labMissionKo: "Lab 6. Google AI Studio에서 50개의 예시와 컨텍스트 캐싱을 적용한 나만의 맞춤 도메인 전문가 봇 구축"
  },
  {
    sessionNum: 7,
    title: "Session 7: WebMCP Protocol & HTML Token Diet",
    titleKo: "7강. WebMCP 프로토콜과 HTML 토큰 다이어트",
    theme: "AI-Native Web Protocols & Lightweight Data Extraction",
    learningObjectives: [
      "Deconstruct why legacy visual HTML causes 95% token bloat and financial drain for autonomous AI agents.",
      "Master the Web Model Context Protocol (WebMCP) and declarative JSON-LD agent discovery schemas.",
      "Deploy the Split-Layer Web architecture to serve human browsers and AI agents simultaneously."
    ],
    learningObjectivesKo: [
      "인간용 시각 HTML 태그 파싱이 초래하는 95%의 토큰 낭비와 연산 지연 원인 분석",
      "에이전트가 데이터만 즉시 교환하는 Web Model Context Protocol(WebMCP) 및 llms.txt 디스커버리 마스터",
      "인간에게는 UI를, AI에게는 초경량 JSON 스트림을 동시 서빙하는 분리 계층 웹(Split-Layer Web) 구축"
    ],
    parts: [
      {
        partNum: 1,
        slideRange: "Slides 02–10",
        title: "PART 1: THE HTML BOTTLENECK & THE TOKEN CRISIS",
        titleKo: "HTML 병목 현상과 토큰 낭비의 위기",
        summary: "Redeeming time in the web matrix: Why scraping CSS, ads, and tracking scripts wastes millions of AI tokens.",
        summaryKo: "광고 스크립트와 수만 줄의 CSS로 뒤덮인 웹페이지를 억지로 크롤링하느라 발생하는 극심한 토큰 낭비 진단",
        keyTopics: ["The HTML Token Trap", "95% Scraping Bandwidth Waste", "Redeeming Time in the Web Matrix"]
      },
      {
        partNum: 2,
        slideRange: "Slides 11–20",
        title: "PART 2: WEBMCP: THE AI-NATIVE MAP",
        titleKo: "WebMCP: AI 네이티브 웹 지도",
        summary: "Publishing `llms.txt` and `agents.md` declarative directory manifests to give agents a direct semantic road map.",
        summaryKo: "웹사이트 루트에 `llms.txt`와 `agents.md`를 발행하여 에이전트에게 직통 시맨틱 도로망을 제공하는 WebMCP 표준",
        keyTopics: ["llms.txt Standard", "Structured JSON-LD Endpoints", "Sub-100 Token Page Manifests"]
      },
      {
        partNum: 3,
        slideRange: "Slides 21–30",
        title: "PART 3: CRYPTOGRAPHIC SECURITY & GUARDRAILS",
        titleKo: "암호학적 보안과 가드레일",
        summary: "Mutual TLS handshakes, ephemeral Docker container sandboxing, and zero-trust permission policies for web agents.",
        summaryKo: "웹 서버와 에이전트 간의 상호 TLS 암호 인증, 일회용 샌드박스 격리 및 무단 접근 차단 가드레일",
        keyTopics: ["Mutual TLS Authentication", "Ephemeral Docker Quarantine", "Zero-Trust Web Permissions"]
      },
      {
        partNum: 4,
        slideRange: "Slides 31–39",
        title: "PART 4: AI-NATIVE ARCHITECTURE & E-COMMERCE",
        titleKo: "AI 네이티브 아키텍처와 전자상거래",
        summary: "The Split-Layer Web architecture, WooCommerce WebMCP integration, and Green Computing reducing bandwidth by 90%.",
        summaryKo: "인간과 기계를 동시에 만족시키는 분리 계층 웹, 우커머스 실전 쇼핑몰 연동 및 대역폭 90% 절감의 친환경 웹",
        keyTopics: ["Split-Layer Web Serving", "WooCommerce Agent Endpoints", "Green Web Efficiency"]
      }
    ],
    labMission: "Lab 7: Author and deploy an `llms.txt` and WebMCP endpoint schema for an enterprise e-commerce catalog.",
    labMissionKo: "Lab 7. 전자상거래 쇼핑몰 카탈로그를 위한 `llms.txt` 및 WebMCP JSON 엔드포인트 명세서 배포"
  },
  {
    sessionNum: 8,
    title: "Session 8: Agentic Commerce: UCP & AP2 Autonomous Checkout",
    titleKo: "8강. 에이전틱 커머스: UCP와 AP2 자율 결제",
    theme: "M2M Commerce & Cryptographic Financial Mandates",
    learningObjectives: [
      "Understand the rise of Machine-to-Machine (M2M) Agentic Commerce and Universal Commerce Protocol (UCP).",
      "Master Agent Payment Protocol (AP2) digital mandates, cryptographic budgets, and single-use virtual cards.",
      "Architect Human-on-the-Loop financial checkout safety valves to prevent runaway billing."
    ],
    learningObjectivesKo: [
      "기계 대 기계(M2M) 자율 상거래와 범용 커머스 프로토콜(UCP)의 원리 이해",
      "AP2 결제 프로토콜의 디지털 위임장, 암호학적 지출 한도 및 일회용 가상 카드 발급 체계 습득",
      "자율 결제 시의 과금 사고를 원천 차단하는 휴먼-온-더-루프 금융 안전 밸브 구축"
    ],
    parts: [
      {
        partNum: 1,
        slideRange: "Slides 02–10",
        title: "PART 1: THE AGENTIC COMMERCE REVOLUTION & FRICTIONLESS CHECKOUT",
        titleKo: "에이전틱 커머스 혁명과 마찰 없는 결제",
        summary: "Redeeming time from commercial friction: Delegating coupon hunting, stock checks, and checkout clicks to agents.",
        summaryKo: "최저가 비교, 쿠폰 검색, 결제창 입력의 피로한 상거래 마찰을 에이전트에 위임하여 매주 3~4시간을 구속",
        keyTopics: ["Frictionless Commerce", "Ending Manual Checkout Loops", "The Human Not Present (HNP) Economy"]
      },
      {
        partNum: 2,
        slideRange: "Slides 11–20",
        title: "PART 2: UNIVERSAL COMMERCE PROTOCOL (UCP)",
        titleKo: "범용 커머스 프로토콜 (UCP)",
        summary: "Decoupling product discovery from web UIs; native REST endpoints allowing buyer agents to transact directly.",
        summaryKo: "웹 화면 렌더링 없이 판매자 서버와 구매자 에이전트가 직접 상품 규격과 가격을 교환하는 UCP REST 스키마",
        keyTopics: ["UCP Schema Architecture", "Product Catalog Vectorization", "M2M Direct Negotiation"]
      },
      {
        partNum: 3,
        slideRange: "Slides 21–30",
        title: "PART 3: FINANCIAL PROTECTION VIA AP2 & DIGITAL MANDATES",
        titleKo: "AP2와 디지털 위임장을 통한 금융 보호",
        summary: "Cryptographic digital mandates establishing strict spending caps, merchant white-lists, and single-use virtual tokens.",
        summaryKo: "암호학적으로 서명된 디지털 위임장으로 지출 상한선과 가맹점을 지정하여 무단 결제를 원천 차단하는 AP2",
        keyTopics: ["AP2 Protocol Handshake", "Single-Use Virtual Tokens", "Deterministic Budget Ceilings"]
      },
      {
        partNum: 4,
        slideRange: "Slides 31–39",
        title: "PART 4: GOVERNANCE, PRIVACY & THE AGENTIC FLYWHEEL",
        titleKo: "거버넌스, 프라이버시, 그리고 에이전틱 플라이휠",
        summary: "Human-on-the-Loop financial veto power, zero-data retention, and the accelerating operational flywheel of AI commerce.",
        summaryKo: "인간 주권의 최종 결제 승인권, 거래 데이터 무보존 정책, 그리고 압도적 비용 절감을 이끄는 플라이휠 효과",
        keyTopics: ["The Agentic Flywheel", "Zero-Data Retention Privacy", "Human Veto Checkout Valves"]
      }
    ],
    labMission: "Lab 8: Design a cryptographically signed AP2 Digital Mandate with a $50 hard ceiling for an autonomous grocery agent.",
    labMissionKo: "Lab 8. 생필품 구매 에이전트를 위한 $50 한도 및 특정 가맹점 전용 AP2 디지털 위임장 JSON 작성"
  },
  {
    sessionNum: 9,
    title: "Session 9: Chrome V8 Security & Manifest V3 Fortress",
    titleKo: "9강. 크롬 V8 보안과 Manifest V3 요새",
    theme: "Browser Sandboxing & Extension Architecture",
    learningObjectives: [
      "Analyze the modern web browser as a full-fledged multi-process operating system running Chrome V8.",
      "Understand generational garbage collection, Site Isolation, and Specter-level memory vulnerability defense.",
      "Master Manifest V3 service worker architecture and declarativeNetRequest extension security."
    ],
    learningObjectivesKo: [
      "크롬 V8 엔진이 구동되는 현대 웹 브라우저를 하나의 독립된 멀티프로세스 운영체제로 분석",
      "세대별 가비지 컬렉션, 사이트 격리(Site Isolation), 스펙터(Spectre)급 메모리 보안 취약점 방어 이해",
      "Manifest V3 서비스 워커 구조와 declarativeNetRequest 규칙 기반의 안전한 확장 프로그램 개발"
    ],
    parts: [
      {
        partNum: 1,
        slideRange: "Slides 02–10",
        title: "PART 1: THE BROWSER AS THE OPERATING SYSTEM",
        titleKo: "운영체제로서의 웹 브라우저와 보안 매트릭스",
        summary: "Soli Deo Gloria: Guarding intellectual boundaries; analyzing the browser as the primary gateway running billions of lines of code.",
        summaryKo: "모든 지적 데이터의 관문인 브라우저를 수호하는 신앙적 사명과 복잡한 자바스크립트 실행 환경 분석",
        keyTopics: ["The Browser OS Reality", "Multi-Process Architecture", "Guarding the Fortress of the Mind"]
      },
      {
        partNum: 2,
        slideRange: "Slides 11–20",
        title: "PART 2: MEMORY, SANDBOXING & SITE ISOLATION",
        titleKo: "메모리 관리, 샌드박싱, 그리고 사이트 격리",
        summary: "Generational Garbage Collection (Orinoco), OS-level process sandboxing, and Site Isolation preventing cross-tab memory theft.",
        summaryKo: "Orinoco 가비지 컬렉터, 탭별 독립 프로세스 샌드박싱, 탭 간 메모리 탈취를 막는 사이트 격리 메커니즘",
        keyTopics: ["Chrome V8 Engine Pipelines", "Site Isolation Process Boundaries", "Spectre Mitigation"]
      },
      {
        partNum: 3,
        slideRange: "Slides 21–30",
        title: "PART 3: THE MANIFEST V3 EXTENSION REVOLUTION",
        titleKo: "Manifest V3 확장 프로그램 혁명",
        summary: "Why Manifest V3 banned arbitrary remote code execution; ephemeral Service Workers and declarativeNetRequest rules.",
        summaryKo: "원격 악성 코드 실행을 금지하고 임시 서비스 워커와 선언적 네트워크 차단 규칙을 강제한 Manifest V3 혁신",
        keyTopics: ["Manifest V2 vs. V3", "Ephemeral Service Workers", "declarativeNetRequest Rules"]
      },
      {
        partNum: 4,
        slideRange: "Slides 31–39",
        title: "PART 4: PLATFORM HEGEMONY & COGNITIVE SOVEREIGNTY",
        titleKo: "플랫폼 패권과 인지적 주권",
        summary: "Balancing enterprise ad-blocking needs with browser vendor monopolies; sovereign control over your browser window.",
        summaryKo: "거대 플랫폼의 광고 독점과 사용자 프라이버시 간의 충돌 속에서 인지적 자유와 보안 주권을 사수하는 지혜",
        keyTopics: ["Browser Monopolies vs. Open Standards", "Privacy-Preserving Extensions", "Sovereign Browser Armor"]
      }
    ],
    labMission: "Lab 9: Develop a Manifest V3 Chrome extension using declarativeNetRequest to block data trackers and scrub headers.",
    labMissionKo: "Lab 9. declarativeNetRequest를 적용하여 악성 추적 스크립트를 차단하고 헤더를 세척하는 Manifest V3 확장 프로그램 제작"
  },
  {
    sessionNum: 10,
    title: "Session 10: Antigravity 2.0 & 93-Agent Swarm Orchestration",
    titleKo: "10강. Antigravity 2.0과 93개 에이전트 군집 오케스트레이션",
    theme: "Autonomous Swarm Engineering & Subagent Governance",
    learningObjectives: [
      "Master Antigravity 2.0's 150MB native Go CLI and multi-agent coordination engine.",
      "Understand how 93 specialized subagents execute code planning, testing, security audits, and deployment concurrently.",
      "Enforce Review-Driven Development (RDD), structured Artifacts, and the Sovereign Conductor paradigm."
    ],
    learningObjectivesKo: [
      "Antigravity 2.0의 150MB 초경량 Go CLI 엔진 및 다중 에이전트 협업 메커니즘 완전 정복",
      "93개의 전문 서브에이전트가 기획, 코딩, 테스트, 보안 감사를 병렬로 자율 완수하는 군집 지능 제어",
      "리뷰 주도 개발(RDD), 정밀 산출물(Artifacts) 시스템, 지휘관 페르소나를 통한 최종 통제권 사수"
    ],
    parts: [
      {
        partNum: 1,
        slideRange: "Slides 02–10",
        title: "PART 1: THE RISE OF 93-AGENT SWARMS",
        titleKo: "93개 에이전트 군집의 출현과 다중 에이전트 오케스트레이션",
        summary: "Soli Deo Gloria: Redeeming human time from repetitive line-by-line coding; coordinating specialized digital minion fleets.",
        summaryKo: "단순 문법 타이핑의 반복 노역에서 벗어나 93명의 정예 개발 군단을 지휘하는 최고기술책임자(CTO)로의 도약",
        keyTopics: ["The 93-Agent Swarm", "Ephesians 5:16 Time Redemption", "From Typist to Conductor"]
      },
      {
        partNum: 2,
        slideRange: "Slides 11–20",
        title: "PART 2: UNDER THE HOOD OF ANTIGRAVITY 2.0",
        titleKo: "Antigravity 2.0의 내부 시스템 구조",
        summary: "150MB native Go binary CLI, subagent memory isolation, deterministic state machines, and parallel task scheduling.",
        summaryKo: "150MB 네이티브 Go 바이너리, 서브에이전트 메모리 격리, 상태 머신 관리 및 병렬 태스크 스케줄링 기술",
        keyTopics: ["150MB Native Go CLI", "Subagent Task Isolation", "Zero Inter-Agent Race Conditions"]
      },
      {
        partNum: 3,
        slideRange: "Slides 21–30",
        title: "PART 3: COMMAND LINE MASTERY & STATE CONTROL",
        titleKo: "명령줄 마스터리와 상태 제어",
        summary: "Driving the `agy` CLI, utilizing `/grill-me` design interviews, executing `/goal` autonomous loops, and state diff tracking.",
        summaryKo: "`agy` 터미널 명령, 설계 결정을 위한 `/grill-me` 인터뷰, 자율 완수를 위한 `/goal` 루프 및 상태 추적",
        keyTopics: ["The `agy` CLI Interface", "The `/grill-me` Interactive Command", "Deterministic File Replace Tools"]
      },
      {
        partNum: 4,
        slideRange: "Slides 31–39",
        title: "PART 4: TRUST, SAFETY & CONDUCTOR SOVEREIGNTY",
        titleKo: "신뢰, 안전성, 그리고 지휘관의 주권",
        summary: "Enforcing Review-Driven Development (RDD), sandboxing production writes, and holding the supreme veto baton.",
        summaryKo: "리뷰 주도 개발(RDD), 운영 환경 격리, 인간 서명 없이는 코드가 배포되지 않는 절대적 거부권 사수",
        keyTopics: ["Review-Driven Development (RDD)", "The Artifacts System", "Supreme Human Veto Baton"]
      }
    ],
    labMission: "Lab 10: Orchestrate a 10-subagent Antigravity swarm to plan, write, test, and containerize a full-stack React app.",
    labMissionKo: "Lab 10. Antigravity 10개 서브에이전트 군집을 지휘하여 풀스택 React 앱의 기획, 코딩, 테스트, 컨테이너화를 완수"
  },
  {
    sessionNum: 11,
    title: "Session 11: True AI Science: HurekaBench & Fact Verification",
    titleKo: "11강. 진정한 AI 과학: HeurekaBench와 사실 검증",
    theme: "Deductive Scientific Reasoning & Atomic Fact Verification",
    learningObjectives: [
      "Expose the crisis of benchmark saturation (MMLU contamination) and contrast rote memorization with true deductive science.",
      "Understand Google's HeurekaBench methodology: testing active hypothesis formulation through THINK-ACT-OBSERVE loops.",
      "Deploy Atomic Fact Verification pipelines and Critic Modules with Ed25519 cryptographic receipts."
    ],
    learningObjectivesKo: [
      "MMLU 등 기존 객관식 족보 암기 벤치마크의 포화와 오염을 규명하고 진정한 연역적 과학 추론의 차이 파악",
      "Google HeurekaBench의 가설 검증 방법론: THINK-ACT-OBSERVE 반복 루프를 통한 미지의 물리 법칙 유도",
      "원자 단위 사실 검증(Atomic Fact Verification)과 크리틱(Critic) 모듈 및 Ed25519 암호 서명 검증 배치"
    ],
    parts: [
      {
        partNum: 1,
        slideRange: "Slides 02–10",
        title: "PART 1: THE CRISIS OF BENCHMARK SATURATION & TRUE AI SCIENCE",
        titleKo: "벤치마크 포화의 위기와 진정한 AI 과학",
        summary: "Soli Deo Gloria: Stewardship of truth; why memorizing multiple-choice answers is not genuine scientific intelligence.",
        summaryKo: "단순 족보 암기로 부풀려진 AI 마케팅 거품을 걷어내고, 진리의 청지기로서 엄정한 과학적 추론 능력 검증",
        keyTopics: ["Benchmark Saturation & Contamination", "Rote Memory vs. Deductive Science", "Stewardship of Truth"]
      },
      {
        partNum: 2,
        slideRange: "Slides 11–20",
        title: "PART 2: HEUREKABENCH & THINK-ACT-OBSERVE",
        titleKo: "HeurekaBench와 THINK-ACT-OBSERVE 루프",
        summary: "Evaluating autonomous agents inside sandbox scientific simulators: formulating hypotheses, running trials, and deducing laws.",
        summaryKo: "가상 물리 시뮬레이터 안에서 에이전트가 가설을 세우고, 실험을 수행하고, 관찰하여 법칙을 발견하는 HeurekaBench 원리",
        keyTopics: ["HeurekaBench Sandbox Trials", "THINK-ACT-OBSERVE Paradigm", "Deducing Hidden Physical Laws"]
      },
      {
        partNum: 3,
        slideRange: "Slides 21–30",
        title: "PART 3: FACT VERIFICATION & GOVERNANCE",
        titleKo: "사실 검증과 거버넌스 파이프라인",
        summary: "Deconstructing outputs into atomic factual claims, verifying each with dedicated Critic modules, and sealing logs with Ed25519.",
        summaryKo: "답변을 개별 원자 명제로 분해하여 크리틱 모듈로 교차 검증하고 Ed25519 공개키로 봉인하는 무환각 파이프라인",
        keyTopics: ["Atomic Claim Extraction", "The Critic Verification Module", "Ed25519 Cryptographic Receipts"]
      },
      {
        partNum: 4,
        slideRange: "Slides 31–39",
        title: "PART 4: CO-EVOLUTION & ACTIVE STEWARDSHIP",
        titleKo: "공진화와 능동적 청지기직",
        summary: "Avoiding the intellectual sloth of uncritical AI acceptance; cultivating human discernment alongside autonomous fact-checkers.",
        summaryKo: "기계의 답변을 무비판적으로 수용하는 지적 나태를 경계하고 인간의 비판적 안목과 AI 검증망을 결합하는 지혜",
        keyTopics: ["Intellectual Sloth Defense", "The Impartial LLM Grader", "Human-Machine Scientific Co-Evolution"]
      }
    ],
    labMission: "Lab 11: Build an Atomic Fact Verification pipeline that extracts claims from an AI response and validates against a ground truth corpus.",
    labMissionKo: "Lab 11. AI 생성 답변에서 원자 명제를 자동 추출하고 기준 말뭉치(Ground Truth)와 대조 검증하는 파이프라인 구현"
  },
  {
    sessionNum: 12,
    title: "Session 12: World Models: Genie 3 Simulation & Waymo Training",
    titleKo: "12강. 월드 모델: Genie 3 시뮬레이션과 Waymo 자율주행 학습",
    theme: "3D Physical Simulation & Infinite Synthetic Training",
    learningObjectives: [
      "Understand the conceptual leap from next-token text prediction to continuous 3D Spatio-Temporal World Models.",
      "Analyze Google's Genie 3 interactive 3D world simulator running at 30 FPS backed by a 280-billion Street View dataset moat.",
      "Understand how Waymo trains 10,000 parallel vehicle swarms on hazardous edge cases inside simulated worlds."
    ],
    learningObjectivesKo: [
      "단순 다음 텍스트 토큰 예측을 넘어 연속적인 3차원 시공간을 시뮬레이션하는 월드 모델의 패러다임 도약 이해",
      "구글의 2,800억 장 스트리트 뷰 데이터 해자에 기반하여 초당 30프레임으로 상호작용하는 Genie 3 월드 모델 분석",
      "Waymo가 10,000대의 가상 차량 군집을 가상 세계에 투입하여 극한의 위험 사고를 무한 학습하는 메커니즘 습득"
    ],
    parts: [
      {
        partNum: 1,
        slideRange: "Slides 02–10",
        title: "PART 1: WORLD MODELS: BEYOND NEXT-TOKEN PREDICTION",
        titleKo: "월드 모델: 다음 토큰 예측을 넘어 3D 시뮬레이션으로",
        summary: "The Spiritual Mandate: Reclaiming human time for sacred creation; ascending from text tokens to simulating physical creation.",
        summaryKo: "글자 조합을 넘어 중력, 마찰, 충돌 등 하나님의 물리적 창조 세계 법칙을 인과적으로 이해하는 월드 모델의 서막",
        keyTopics: ["Beyond Next-Token Generation", "Spatio-Temporal Causality", "The 3D World Simulation Frontier"]
      },
      {
        partNum: 2,
        slideRange: "Slides 11–20",
        title: "PART 2: UNDER THE HOOD OF PHYSICAL REALISM",
        titleKo: "물리적 현실감의 내부 메커니즘",
        summary: "Spatio-Temporal Video Tokenizers, Video-Masked-Conditioning (VMC), and Google's 280-billion Street View panoramic image moat.",
        summaryKo: "시공간 비디오 토크나이저, VMC 아키텍처, 그리고 수 킬로미터를 주행해도 일그러지지 않는 2,800억 장의 스트리트 뷰 데이터 해자",
        keyTopics: ["Spatio-Temporal Video Volume", "VMC Architecture", "The 280B Street View Moat"]
      },
      {
        partNum: 3,
        slideRange: "Slides 21–30",
        title: "PART 3: WAYMO AND THE INFINITE SAFE CLASSROOM",
        titleKo: "웨이모(Waymo)와 무한한 안전 교실",
        summary: "Eliminating physical highway hazards by generating 10,000 parallel swarm vehicles training on blizzards and brake failures in simulation.",
        summaryKo: "실제 도로에서 사람 목숨을 걸지 않고 10,000대의 차량 군집이 눈보라, 급정거, 돌발 보행자를 가상 학습하는 안전 교실",
        keyTopics: ["Simulated Fleet Clusters", "Hazardous Edge-Case Training", "Zero Real-World Collision Risk"]
      },
      {
        partNum: 4,
        slideRange: "Slides 31–39",
        title: "PART 4: STRATEGIC GOVERNANCE & CREATIVE SOVEREIGNTY",
        titleKo: "전략적 거버넌스와 창조적 주권",
        summary: "Enterprise privacy sandboxes, anti-training seals, and the human architect's role as the sovereign ethical conductor of virtual worlds.",
        summaryKo: "가상 세계 모델의 기밀 유출을 막는 데이터 샌드박스와 안티 트레이닝 봉인, 그리고 인간 지휘관의 도덕적 청지기 사명",
        keyTopics: ["Topography Data Sandboxes", "Anti-Training Seals", "Sovereign Ethical World Governance"]
      }
    ],
    labMission: "Lab 12: Prompt and benchmark a Genie 3 interactive 3D simulation trajectory, analyzing physical consistency across 30 seconds.",
    labMissionKo: "Lab 12. Genie 3 대화형 3D 시뮬레이션 궤적을 생성하고 30초 동안의 물리적 기하학 일관성을 정량 분석"
  },
  {
    sessionNum: 13,
    title: "Session 13: Calculated Art: SVG Vector Engineering & LaTeX Math",
    titleKo: "13강. 계산된 예술: SVG 벡터 엔지니어링과 LaTeX 수식",
    theme: "Mathematical Visuals & Scientific Typography",
    learningObjectives: [
      "Understand the tragedy of raster scaling (pixelation and quadratic file bloat) and master deterministic SVG vector mathematics.",
      "Master Cubic Bezier curve calculus, viewBox coordinate manipulation, and DOM-integrated CSS/JS vector animation.",
      "Orchestrate LaTeX mathematical typography, handwriting transcription, and pre-rendered SVG mathematical web pipelines."
    ],
    learningObjectivesKo: [
      "확대하면 깨지고 용량이 폭증하는 래스터(픽셀)의 비극을 극복하고 결정론적 SVG 벡터 수학 완전 정복",
      "3차 베지에(Bezier) 곡선 미적분, viewBox 좌표계 제어 및 브라우저 DOM과 직접 결합되는 CSS/JS 벡터 애니메이션 마스터",
      "LaTeX 수식 조판, 손글씨 수식 자동 전사 및 5배 빠른 사전 렌더링 SVG 수식 웹 서비스 파이프라인 구축"
    ],
    parts: [
      {
        partNum: 1,
        slideRange: "Slides 02–10",
        title: "PART 1: THE TRAGEDY OF RASTER SCALE & CALCULATED VECTOR ART",
        titleKo: "래스터 스케일의 비극과 계산된 벡터 예술",
        summary: "Soli Deo Gloria: Perfect forms in mathematical order; why mathematical vectors scale infinitely to 8K in mere kilobytes.",
        summaryKo: "수학적 질서와 완전성의 추구: 몇 킬로바이트의 가벼운 수학 방정식으로 8K 화면까지 영원히 깨지지 않는 벡터 그래픽",
        keyTopics: ["The Raster Scale Tragedy", "Quadratic Byte Bloat vs. Vector Math", "Infinite Scalability under Soli Deo Gloria"]
      },
      {
        partNum: 2,
        slideRange: "Slides 11–20",
        title: "PART 2: THE XML FABRIC OF SVG",
        titleKo: "SVG의 XML 구조와 베지에 미적분",
        summary: "DOM integration, Cubic Bezier curve equations (`C x1 y1, x2 y2, x y`), responsive viewBox scaling, and path optimization.",
        summaryKo: "HTML DOM에 직접 결합되는 XML 노드 구조, 부드러운 S자 곡선을 그리는 3차 베지에 매개변수 방정식과 viewBox 제어",
        keyTopics: ["The XML Node Fabric", "Cubic Bezier Curve Calculus", "Responsive viewBox Coordinate Systems"]
      },
      {
        partNum: 3,
        slideRange: "Slides 21–30",
        title: "PART 3: GEMINI-POWERED VISUAL ENGINEERING",
        titleKo: "Gemini 기반 시각 엔지니어링 & DOM 제어",
        summary: "Multimodal sketch-to-vector compilation, DOMPurify SVG sanitization against XSS, and real-time CSS vector animations.",
        summaryKo: "냅킨 스케치를 2초 만에 프로덕션 리액트 SVG로 합성하고, XSS 공격을 차단하는 DOMPurify 살균 및 CSS 실시간 애니메이션",
        keyTopics: ["Sketch-to-Vector Compilation", "SVG Cybersecurity & DOMPurify", "Dynamic CSS/JS Vector Styling"]
      },
      {
        partNum: 4,
        slideRange: "Slides 31–39",
        title: "PART 4: LATEX MATHEMATICAL ORCHESTRATION",
        titleKo: "LaTeX 수식 오케스트레이션",
        summary: "LaTeX scientific typography standard, handwriting OCR transcription, and pre-rendering equations to SVG for 5x faster loads.",
        summaryKo: "흐릿한 캡처 수식을 퇴출하는 글로벌 LaTeX 표준, 손글씨 수식 자동 전사 및 브라우저 렌더링 지연 없는 사전 렌더링 SVG",
        keyTopics: ["LaTeX Mathematical Grammar", "Multimodal Formula OCR", "Pre-Rendered SVG vs. Runtime MathJax"]
      }
    ],
    labMission: "Lab 13: Engineer a responsive, animated SVG system architecture diagram and embed 3 verified LaTeX equations.",
    labMissionKo: "Lab 13. 반응형 인터랙티브 SVG 시스템 아키텍처 다이어그램을 코딩하고 3개의 검증된 LaTeX 수식을 결합"
  },
  {
    sessionNum: 14,
    title: "Session 14: Cinematic AI Pipelines: Flow AI vs Runway ML",
    titleKo: "14강. 시네마틱 AI 파이프라인: Google Flow AI 대 Runway ML",
    theme: "Generative Cinema & Multi-Model Hybrid Strategy",
    learningObjectives: [
      "Deconstruct the paradigm shift from physical camera capture to generative multi-model curation.",
      "Master Google Flow AI's Trinity Engine (Gemini, Imagen 4, Veo 3.1) with native 48kHz synced audio and Ingredients identity locks.",
      "Master Runway ML Gen-4.5's 5-channel Motion Brush, 3D camera vector trajectories, and Act-Two performance capture.",
      "Assemble a 3-step hybrid cinematic pipeline combining Flow AI, Runway ML, and traditional NLE editors."
    ],
    learningObjectivesKo: [
      "물리적 카메라 촬영의 중력에서 벗어나 생성형 멀티 모델을 지휘하는 큐레이터로의 패러다임 전환",
      "Google Flow AI 트리니티 엔진(Gemini-Imagen-Veo)의 48kHz 네이티브 오디오 동기화 및 '재료(Ingredients)' 외형 고정 마스터",
      "Runway ML Gen-4.5의 5채널 독립 모션 브러시, 3D 카메라 벡터 궤적, 그리고 Act-Two 인간 연기 이식 기술 습득",
      "Flow AI ➔ Runway ML ➔ NLE 타임라인 최종 조립으로 이어지는 3단계 하이브리드 영화 제작 파이프라인 완성"
    ],
    parts: [
      {
        partNum: 1,
        slideRange: "Slides 02–10",
        title: "PART 1: DROPPING THE CAMERA: FROM CAPTURE TO GENERATIVE CURATION",
        titleKo: "카메라를 내려놓고 생성형 큐레이션으로 도약",
        summary: "Soli Deo Gloria: Reclaiming creative time; overcoming the 'casino trap' of random prompt generation through structural constraints.",
        summaryKo: "자본과 장비의 중력을 탈출하여 무작위 슬롯머신 도박식 생성을 극복하고 80%의 제작 비용을 절감하는 엔지니어링 파이프라인",
        keyTopics: ["Dropping Physical Camera Gravity", "The Interface Trap vs. SOPs", "80% Rendering Cost Reduction"]
      },
      {
        partNum: 2,
        slideRange: "Slides 11–20",
        title: "PART 2: INSIDE THE ENGINE ROOM OF GOOGLE FLOW AI",
        titleKo: "Google Flow AI의 내부 엔진 룸",
        summary: "The Trinity Architecture (Gemini, Imagen 4, Veo 3.1), native 48kHz audio synthesis, Lyria 3 Pro beat-syncing, and Ingredients identity lock.",
        summaryKo: "삼위일체 엔진의 원스톱 동기화, 입술 립싱크 및 공간 음향 동시 생성, 음악 비트 싱크, 캐릭터 얼굴을 100% 고정하는 재료 시스템",
        keyTopics: ["Trinity Engine Orchestration", "Native 48kHz Audio & Lip-Sync", "Ingredients Identity Lock (@Tags)"]
      },
      {
        partNum: 3,
        slideRange: "Slides 21–30",
        title: "PART 3: PRECISION 연출 WITH RUNWAY ML",
        titleKo: "Runway ML을 통한 초정밀 시네마틱 연출",
        summary: "Rank 1 on Video Arena Elo (1510), 5-channel vector Motion Brush painting, smooth 3D camera vector curves, and Act-Two performance capture.",
        summaryKo: "비디오 아레나 1위의 정밀도, 5개 영역 독립 속도 벡터 브러시, 떨림 없는 달링/팬 카메라 궤적, 실제 배우 감정을 이식하는 Act-Two",
        keyTopics: ["Video Arena ELO (1510)", "5-Channel Vector Motion Brush", "Act-Two Performance Capture"]
      },
      {
        partNum: 4,
        slideRange: "Slides 31–39",
        title: "PART 4: THE HYBRID CINEMATIC PIPELINE",
        titleKo: "하이브리드 시네마틱 마스터 파이프라인",
        summary: "Flow AI rapid storyboarding ➔ Runway ML motion precision ➔ NLE timeline color grading & multi-track sound master assembly.",
        summaryKo: "Flow AI 고속 콘티 검증 ➔ Runway 카메라 정밀 연출 ➔ 프리미어/다빈치 타임라인 조립 및 다중 음향 믹싱으로 60초 단편영화 완성",
        keyTopics: ["The 3-Step Hybrid Architecture", "The Conductor Persona", "Democratized Global Cinema"]
      }
    ],
    labMission: "Lab 14: Produce a 60-second high-fidelity cinematic short film using the hybrid Flow AI ➔ Runway ML ➔ NLE pipeline.",
    labMissionKo: "Lab 14. Flow AI, Runway ML, NLE 편집기를 결합한 3단계 하이브리드 파이프라인으로 60초 시네마틱 단편영화 제작"
  },
  {
    sessionNum: 15,
    title: "Session 15: IT Wisdom Peak: Human-on-the-Loop & Life OS Board",
    titleKo: "15강. IT 지혜의 정점: 휴먼-온-더-루프와 Life OS 이사회",
    theme: "Capstone Integration, Cognitive Hygiene & Soli Deo Gloria",
    learningObjectives: [
      "Confront the cognitive tax of digital obesity and awaken the dormant Frontal Lobe Director through analog sensory grounding.",
      "Understand the neuro-biological power of physical exercise, fine motor crafts, paper reading, and the sacred Sabbath rest.",
      "Master Human-on-the-Loop (HOTL) governance, 3-Pillar bounding, and cryptographic Ed25519 audit verification.",
      "Synthesize all 15 sessions into a sovereign, lifelong personal Life Operating System under Soli Deo Gloria."
    ],
    learningObjectivesKo: [
      "스마트폰 미세 알림의 도파민 중독과 디지털 비만을 극복하고 신체 감각 접지를 통해 잠든 전두엽 디렉터 각성",
      "땀 흘리는 운동, 수공예/악기 연주, 종이책 3차원 공간 독서, 그리고 에베소서 5:16에 기반한 24시간 안식의 회복",
      "휴먼-온-더-루프(HOTL) 주권 체계, 3대 거버넌스 기둥(Task-Schedule-Skill), Ed25519 암호학적 영수증 감사 완비",
      "15주간의 모든 배움을 총집약하여 오직 하나님께 영광을 돌리는(Soli Deo Gloria) 평생의 Life OS 청사진 완성"
    ],
    parts: [
      {
        partNum: 1,
        slideRange: "Slides 02–10",
        title: "PART 1: THE TRAP OF DIGITAL OBESITY",
        titleKo: "디지털 비만의 덫과 잠든 전두엽",
        summary: "Confronting dopamine sedation, attention fragmentation (23-minute penalty), and the Cognitive Adaptation Valley of unmonitored automation.",
        summaryKo: "스마트폰 알림의 도파민 마취, 23분의 주의력 전환 페널티, 기계에 전권을 넘겼을 때 닥치는 인지 적응 계곡의 위기 진단",
        keyTopics: ["Digital Obesity & Dopamine Sedation", "The 23-Minute Distraction Penalty", "The Cognitive Adaptation Valley"]
      },
      {
        partNum: 2,
        slideRange: "Slides 11–20",
        title: "PART 2: RECLAIMING ANALOG SENSES",
        titleKo: "아날로그 감각의 회복과 신체적 닻",
        summary: "Physical sweating, manual crafts, the scent of paper books, spatial 3D text mapping, and the infinitely scalable Vectorized Mind.",
        summaryKo: "땀 흘리는 운동(BDNF), 손을 쓰는 악기/공작, 종이책 3D 공간 기억 매핑 및 무한히 선명한 벡터화된 지혜(SVG)의 구축",
        keyTopics: ["Analog Magic (Sweating, Craft, Paper)", "Spatial Text Mapping in Books", "Rasterized Mind vs. Vectorized Wisdom"]
      },
      {
        partNum: 3,
        slideRange: "Slides 21–30",
        title: "PART 3: HUMAN-ON-THE-LOOP SOVEREIGNTY",
        titleKo: "휴먼-온-더-루프(HOTL) 주권 거버넌스",
        summary: "The Conductor Model, supreme Veto Power, 3-Pillar bounding (Task, Schedule, Skill), and Ed25519 cryptographic receipts.",
        summaryKo: "오케스트라 지휘자 모델, 인간의 최종 거부권(Veto Power), 3대 통제 울타리 및 Ed25519 불변의 암호 서명 감사 원장",
        keyTopics: ["Human-on-the-Loop (HOTL) vs. HITL/HOOTL", "The Supreme Veto Principle", "Ed25519 Cryptographic Receipts"]
      },
      {
        partNum: 4,
        slideRange: "Slides 31–39",
        title: "PART 4: SOLI DEO GLORIA - THE ZENITH OF WISDOM",
        titleKo: "Soli Deo Gloria - IT 지혜의 최고 정점",
        summary: "Technology as a divine gift, the stewardship of the soul (Imago Dei), Green Computing (87% energy cut), and the 15-week ascent.",
        summaryKo: "주인이 아닌 선물로서의 기술, 하나님의 형상(Imago Dei) 수호, 컨텍스트 캐싱을 통한 87% 그린 컴퓨팅 및 15주 대단원의 완성",
        keyTopics: ["Technology as a Stewardship Gift", "Imago Dei & Soul Stewardship", "Green Computing & 15-Week Ascent"]
      }
    ],
    labMission: "Capstone Lab 15: Author and submit your comprehensive Life OS Strategic Blueprint to `/Spark_OS/Life_OS.md`.",
    labMissionKo: "Capstone Lab 15. 주의력 감사, 몰입의 성소 설계, 워크스페이스 자동화를 망라한 나만의 Life OS 마스터 청사진 제출"
  }
];
