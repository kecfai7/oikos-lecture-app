const fs = require('fs');
const path = require('path');

const slidesDataPath = path.join(__dirname, 'src', 'data', 'slidesData.js');
let fileContent = fs.readFileSync(slidesDataPath, 'utf8');

// Transpile export const to module.exports for node evaluation
fileContent = fileContent.replace(/export const SESSIONS =/g, 'const SESSIONS =');
for (let i = 1; i <= 15; i++) {
  const re = new RegExp(`export const SLIDES_SESSION_${i} =`, 'g');
  fileContent = fileContent.replace(re, `const SLIDES_SESSION_${i} =`);
}

fileContent += '\nmodule.exports = { SESSIONS, ' + Array.from({length: 15}, (_, i) => 'SLIDES_SESSION_' + (i+1)).join(', ') + ' };';

const tempPath = path.join(__dirname, 'temp_unify_data.cjs');
fs.writeFileSync(tempPath, fileContent, 'utf8');

const allData = require(tempPath);
fs.unlinkSync(tempPath);

const updatesBySession = {
  1: {
    2: {
      num: 2,
      type: "section",
      title: "PART 1: THE PARADIGM SHIFT: CHATBOTS TO AVATARS",
      subtitle: "Soli Deo Gloria: Reclaiming human time from mechanical chatbot waiting loops",
      script: `We now open Part 1 of Session 1: "The Paradigm Shift: From Waiting Chatbots to Sleep-Free Personal Avatars."

Under our sacred motto, Soli Deo Gloria—Glory to God alone—we explore how technology can redeem our precious time. 

For the past two years, the entire world interacted with AI through a "chat window"—typing a prompt, staring at the screen, and waiting for the cursor to finish. That waiting loop is an enormous waste of human potential!

In this first module, we deconstruct the paradigm shift from passive chatbot waiting to proactive, autonomous personal avatars that execute complex workflows 24/7 while you sleep. Let us begin Part 1!`,
      koreanGuide: {
        summary: "Part 1 섹션 전환: 대기형 챗봇에서 24시간 수면 없는 개인 아바타로의 패러다임 전환",
        points: [
          "Soli Deo Gloria와 시간 구속의 사명: 단순 대기 화면을 쳐다보며 버려지는 인간의 시간 구출",
          "질문-대답의 수동적 챗봇 시대를 넘어, 비동기적으로 스스로 작업을 완수하는 개인 아바타의 탄생"
        ],
        tips: "더 이상 화면 앞에서 깜빡이는 커서를 기다릴 필요가 없는 아바타 혁명의 서막을 힘차게 선포하세요."
      },
      keyTerms: [
        {
          term: "Autonomous Personal Avatar",
          def: "A continuous AI agent that executes multi-step digital workflows proactively without waiting for line-by-line user input.",
          defKo: "자율형 개인 아바타 (Sleep-Free AI 에이전트)"
        }
      ]
    },
    11: {
      num: 11,
      type: "section",
      title: "PART 2: UNDER THE HOOD OF AUTONOMOUS REASONING",
      subtitle: "TPU v8, Gemini 3.6 Flash, and Asynchronous Execution Engines",
      script: `We now cross the threshold into Part 2: "Under the Hood of Autonomous Reasoning."

How does an AI agent maintain logical coherence and execute multi-step workflows without human intervention?

In this section, we analyze the hardware and software architecture powering autonomous agents: Google's TPU v8 clusters, Gemini 3.6 Flash reasoning loops, and asynchronous event triggers that monitor your emails, documents, and calendars in real time. Let us look inside the machine!`,
      koreanGuide: {
        summary: "Part 2 섹션 전환: 자율 추론 엔진의 내부 메커니즘",
        points: [
          "TPU v8 하드웨어와 Gemini 3.6 Flash 추론 루프의 결합",
          "인간의 개입 없이도 이메일과 문서를 스스로 감시하고 처리하는 비동기 이벤트 트리거 구조"
        ],
        tips: "자율 에이전트가 어떻게 스스로 판단하고 멈춤 없이 돌아가는지 기술적 깊이를 전달하세요."
      },
      keyTerms: [
        {
          term: "Asynchronous Reasoning",
          def: "Autonomous execution of AI reasoning loops triggered by background events rather than immediate human prompts.",
          defKo: "비동기 자율 추론 (이벤트 기반 자동 실행)"
        }
      ]
    },
    21: {
      num: 21,
      type: "section",
      title: "PART 3: THE CONNECTED WORKSPACE: APPS SCRIPT & DRIVE",
      subtitle: "Native Workspace Integration, Cross-App Automation, and Contextual Pipelines",
      script: `We now enter Part 3: "The Connected Workspace: Apps Script & Drive Integration."

An intelligent agent is useless if it is trapped in an isolated chat sandbox. It must be connected natively to where your work actually lives!

In this section, we explore how Google Apps Script (GAS) and Google Drive act as the nervous system of your digital workplace. You will learn how agents read spreadsheets, generate presentation slides, and manage calendar schedules automatically. Let us connect the workspace!`,
      koreanGuide: {
        summary: "Part 3 섹션 전환: 연결된 워크스페이스 - Apps Script 및 Drive 연동",
        points: [
          "고립된 챗봇을 벗어나 구글 워크스페이스(Drive, Docs, Sheets, Calendar)에 직접 결합되는 에이전트",
          "Google Apps Script를 신경망 삼아 부서 간 데이터를 실시간으로 자동 가공·전송하는 파이프라인"
        ],
        tips: "에이전트가 내 실제 업무 도구들과 손발을 맞추어 일하는 통합 생산성을 강조하세요."
      },
      keyTerms: [
        {
          term: "Native Workspace Integration",
          def: "Connecting AI agents directly into enterprise productivity tools via native APIs and script engines.",
          defKo: "네이티브 워크스페이스 연동"
        }
      ]
    },
    31: {
      num: 31,
      type: "section",
      title: "PART 4: WISDOM SYNTHESIS: SOLI DEO GLORIA",
      subtitle: "Human-on-the-Loop Governance, Sacred Rest, and Master Stewardship",
      script: `We now enter our final chapter, Part 4: "Wisdom Synthesis: Soli Deo Gloria & Human Sovereignty."

Everything we engineer must be governed by wisdom and moral purpose. Technology is a powerful lever, but the human remains the sovereign master.

In this concluding section, we establish the principles of Human-on-the-Loop governance, ethical stewardship, and the sacred Sabbath rest. We do not automate to become idle, but to reclaim our focus for eternal callings. Soli Deo Gloria!`,
      koreanGuide: {
        summary: "Part 4 섹션 전환: 지혜의 통합 - Soli Deo Gloria와 인간 주권",
        points: [
          "기술을 부리는 청지기로서의 인간 주권과 휴먼-온-더-루프(HOTL) 거버넌스",
          "에베소서 5:16의 시간 구속과 거룩한 안식을 통한 영적·창의적 재충전"
        ],
        tips: "1강의 대미를 장식하며 기술의 주인이 되어 하나님께 영광을 돌리는 삶의 자세를 심어주세요."
      },
      keyTerms: [
        {
          "term": "Human Sovereignty",
          "def": "The ethical principle that human wisdom, moral discernment, and intentional governance must always supersede machine autonomy.",
          "defKo": "인간 주권 (도덕적·전략적 통제권)"
        }
      ]
    }
  },
  2: {
    2: {
      num: 2,
      type: "section",
      title: "PART 1: THE 24/7 SLEEP-FREE GUARDIAN PARADIGM",
      subtitle: "Divine Trust & Reclaiming the Sabbath under Soli Deo Gloria and Ephesians 5:16",
      script: `We begin Part 1 of Session 2: "The 24/7 Sleep-Free Guardian Paradigm."

Under our guiding light of Soli Deo Gloria, we are commanded in Ephesians 5:16 to "redeem the time." 

Why do we design a 24/7 asynchronous agent like Gemini Spark? 
Not to become lazy consumers, but to liberate our minds from repetitive administrative drudgery!

In this opening module, we analyze how a persistent cloud guardian watches over your inbox, calendar, and document flows continuously. By delegating the mechanical routine to Spark OS, we purchase back precious hours for deep study, prayer, and sacred rest. Let us explore Part 1!`,
      koreanGuide: {
        summary: "Part 1 섹션 전환: 24/7 수면 없는 수호자 패러다임",
        points: [
          "에베소서 5:16 세월을 아끼라: 기계적 행정 노역에서 벗어나 거룩한 시간을 구속하는 신앙적 사명",
          "24시간 잠들지 않고 내 이메일과 일정을 지켜주는 Gemini Spark 클라우드 가디언 아키텍처의 도입"
        ],
        tips: "잠자는 동안에도 나를 대신해 빈틈없이 시스템을 지켜주는 든든한 AI 수호자의 개념을 선포하세요."
      },
      keyTerms: [
        {
          term: "Sleep-Free Guardian",
          def: "An autonomous, continuously running AI agent monitoring enterprise events and executing workflows 24/7.",
          defKo: "잠들지 않는 수호자 (24/7 자율 에이전트)"
        }
      ]
    }
  },
  3: {
    2: {
      num: 2,
      type: "section",
      title: "PART 1: THE LOCAL-FIRST PARADIGM & SHELL CONTROL",
      subtitle: "The First Keystroke Paradigm: Reclaiming command-line sovereignty under Soli Deo Gloria",
      script: `We open Part 1 of Session 3: "The Local-First Paradigm & OS Shell Control."

Under Soli Deo Gloria, we recognize that true digital mastery begins where your fingers touch the keyboard!

For decades, big tech platforms boxed users inside restrictive graphical user interfaces. But the true architect commands the operating system directly through the command-line shell!

In this opening module, we examine the First Keystroke Paradigm—how a 1.2GB lightweight local AI running in Windows PowerShell grants you instant, sovereign control over your file system, processes, and local data without cloud leaks. Let us take command of the shell!`,
      koreanGuide: {
        summary: "Part 1 섹션 전환: 로컬 퍼스트 패러다임과 OS 쉘 통제권",
        points: [
          "첫 번째 키스트로크 패러다임: GUI의 감옥을 벗어나 파워쉘 터미널에서 직접 OS를 지휘하는 주권 회복",
          "1.2GB 경량 로컬 AI 아머를 장착하여 클라우드 유출 없이 내 PC의 파일과 프로세스를 초고속 통제"
        ],
        tips: "마우스 클릭질에서 벗어나 검은 터미널 창에서 명령을 내리는 진정한 엔지니어의 자신감을 심어주세요."
      },
      keyTerms: [
        {
          term: "Local-First Shell Architecture",
          def: "Running lightweight AI models locally to execute operating system commands directly without cloud latency or data transmission.",
          defKo: "로컬 퍼스트 쉘 아키텍처 (온디바이스 OS 제어)"
        }
      ]
    }
  },
  4: {
    2: {
      num: 2,
      type: "section",
      title: "PART 1: THE CRISIS OF HALLUCINATION & HONEST INTELLIGENCE",
      subtitle: "The Core Mission: Soli Deo Gloria and grounding AI in immutable truth",
      script: `We begin Part 1 of Session 4: "The Crisis of Hallucination & Honest Intelligence."

Under Soli Deo Gloria, truth is our sacred bedrock. Yet, general-purpose chatbots suffer from a fatal flaw: hallucination—confidently fabricating false facts and fake citations!

In enterprise, legal, and academic environments, a single hallucination can destroy an entire career.

In this opening module, we analyze why probabilistic language models hallucinate and introduce the revolutionary solution: Retrieval-Augmented Generation (RAG) and Google NotebookLM. Grounding AI in your verified documents guarantees 100% honest intelligence! Let us explore Part 1!`,
      koreanGuide: {
        summary: "Part 1 섹션 전환: 환각(Hallucination)의 위기와 정직한 지능",
        points: [
          "Soli Deo Gloria와 진리의 청지기직: 거짓과 날조를 용납하지 않는 엄격한 정직성 추구",
          "확률적 언어 모델의 치명적 환각 문제를 해결하는 NotebookLM과 RAG(검색 증강 생성)의 진실 보장 원리"
        ],
        tips: "신뢰할 수 없는 화려한 말장난 대신 100% 출처가 검증된 정직한 AI의 절대적 가치를 역설하세요."
      },
      keyTerms: [
        {
          term: "Honest Intelligence",
          def: "AI reasoning strictly bounded by and cited from verified source documents, eliminating ungrounded hallucinations.",
          defKo: "정직한 지능 (출처 기반 무환각 AI)"
        }
      ]
    }
  },
  5: {
    2: {
      num: 2,
      type: "section",
      title: "PART 1: THE ENTERPRISE DRIVE REVOLUTION & KNOWLEDGE VAULT",
      subtitle: "Soli Deo Gloria: Bringing divine order out of enterprise data chaos",
      script: `We now open Part 1 of Session 5: "The Enterprise Drive Revolution & Knowledge Architecture."

Order is the first law of heaven. Under our motto, Soli Deo Gloria, we are called to bring structural clarity out of chaotic data sprawl.

In modern organizations, thousands of unorganized files, duplicated folders, and broken permissions create a massive intellectual swamp that drains team productivity.

In this first module, we deconstruct how to transform Google Drive into an enterprise knowledge fortress—establishing strict folder taxonomies, file streaming protocols, and role-based permissions. Let us build our knowledge vault!`,
      koreanGuide: {
        summary: "Part 1 섹션 전환: 엔터프라이즈 드라이브 혁명과 지식 볼트(Vault)",
        points: [
          "질서는 하늘의 첫 번째 법칙: 어지럽게 널려 있는 기업 문서의 혼돈을 거룩한 질서로 재편",
          "구글 드라이브를 단순 저장소를 넘어 전사적 지식 요새로 탈바꿈시키는 폴더 분류 체계와 권한 거버넌스"
        ],
        tips: "파일을 찾아 헤매는 시간 낭비를 끝내고 체계적인 지식 금고를 구축하는 쾌감을 전하세요."
      },
      keyTerms: [
        {
          term: "Enterprise Knowledge Vault",
          def: "A structured, secure cloud document architecture governed by strict role permissions and automated indexing.",
          defKo: "엔터프라이즈 지식 볼트 (전사적 지식 요새)"
        }
      ]
    }
  },
  6: {
    2: {
      num: 2,
      type: "section",
      title: "PART 1: THE 1M-TOKEN HORIZON & THE END OF FRAGMENTATION",
      subtitle: "Divine Creative Capacity & Soli Deo Gloria: Transcending narrow context windows",
      script: `We begin Part 1 of Session 6: "The 1M-Token Horizon & The End of Fragmentation."

Under Soli Deo Gloria, human intellect reflects the divine capacity to synthesize vast universes of wisdom. 

For years, developers were crippled by tiny 4,000-token context windows, forcing them to chop books and codebases into fragile vector fragments.

In this opening module, we celebrate the 1-million-token horizon of Gemini 3.5 Pro and Google AI Studio! 
You can feed entire software repositories, thousands of PDF pages, and hours of video into a single context window! Let us cross the 1-million token frontier!`,
      koreanGuide: {
        summary: "Part 1 섹션 전환: 100만 토큰의 지평선과 데이터 파편화의 종말",
        points: [
          "Soli Deo Gloria와 방대한 지적 종합: 쪼개고 자르던 작은 창의 굴레를 벗어난 1M 토큰 혁명",
          "두꺼운 책 수십 권, 거대한 깃허브 코드베이스 전체를 한 번에 프롬프트에 통째로 집어넣는 거대한 컨텍스트 창"
        ],
        tips: "정보를 조각조각 잘라 먹이던 답답함에서 벗어나 전체를 통째로 조망하는 시원한 해방감을 전달하세요."
      },
      keyTerms: [
        {
          term: "1M-Token Context Window",
          def: "The ability of an AI model to ingest and reason over one million tokens (~750,000 words) simultaneously.",
          defKo: "100만 토큰 컨텍스트 창 (초대용량 단일 처리)"
        }
      ]
    }
  },
  7: {
    2: {
      num: 2,
      type: "section",
      title: "PART 1: THE HTML BOTTLENECK & THE TOKEN CRISIS",
      subtitle: "Redeeming human time in the web matrix under Soli Deo Gloria",
      script: `We now open Part 1 of Session 7: "The HTML Bottleneck & The Token Crisis."

Under Soli Deo Gloria, we are commanded to eliminate computational waste and redeem our time.

When AI agents attempt to browse the web today, they are forced to parse massive, bloated HTML files filled with advertising tracking scripts, complex styling, and thousands of lines of JavaScript noise. This causes severe token bloat and financial drain!

In this opening module, we analyze the structural failure of legacy HTML for AI agents and introduce the revolutionary WebMCP protocol! Let us inspect the HTML bottleneck!`,
      koreanGuide: {
        summary: "Part 1 섹션 전환: HTML 병목 현상과 토큰 낭비의 위기",
        points: [
          "웹 매트릭스에서의 시간 구속: 불필요한 광고 스크립트와 수만 줄의 HTML 태그 파싱으로 인한 극심한 토큰 낭비 진단",
          "인간용 시각 웹페이지를 기계가 억지로 읽으려다 발생하는 고비용·저속도 병목을 해결하는 WebMCP의 필요성"
        ],
        tips: "인간을 위한 화려한 웹페이지가 AI에게는 얼마나 비효율적인 쓰레기 더미인지 명확히 짚어주세요."
      },
      keyTerms: [
        {
          term: "HTML Token Bloat",
          def: "The massive consumption of AI context tokens caused by parsing irrelevant web formatting, ads, and CSS scripts.",
          defKo: "HTML 토큰 팽창 (웹 소음 데이터 낭비)"
        }
      ]
    },
    21: {
      num: 21,
      type: "section",
      title: "PART 3: CRYPTOGRAPHIC SECURITY & GUARDRAILS",
      subtitle: "Cryptographic Handshakes, Ephemeral Sandboxes, and Zero-Trust Protection",
      script: `We now enter Part 3: "Cryptographic Security & Guardrails."

When AI agents connect directly to web servers via WebMCP endpoints, security becomes our paramount concern!

In this section, we analyze the cryptographic security architecture of WebMCP: mutual TLS authentication, ephemeral Docker sandboxing, and strict permission boundaries that prevent rogue agents from executing malicious code. Let us fortify our security guardrails!`,
      koreanGuide: {
        summary: "Part 3 섹션 전환: 암호학적 보안과 가드레일",
        points: [
          "에이전트가 서버와 직접 통신할 때 발생할 수 있는 보안 취약점 차단",
          "상호 TLS 인증, 일회용 샌드박스 격리, 제로 트러스트 기반의 권한 통제 메커니즘"
        ],
        tips: "고속 연결만큼이나 철저한 보안 방패가 필수적임을 강조하세요."
      },
      keyTerms: [
        {
          term: "WebMCP Security Guardrails",
          def: "The cryptographic authentication and container sandboxing protocols protecting AI-native web endpoints.",
          defKo: "WebMCP 보안 가드레일"
        }
      ]
    },
    31: {
      num: 31,
      type: "section",
      title: "PART 4: AI-NATIVE ARCHITECTURE & E-COMMERCE",
      subtitle: "The Split-Layer Web, WooCommerce Integration, and Green Web Engineering",
      script: `We now enter our final chapter, Part 4: "AI-NATIVE ARCHITECTURE & E-COMMERCE."

How does WebMCP transform real-world businesses? 
Through the Split-Layer Web!

In this concluding section, we demonstrate how e-commerce stores serve human users with beautiful visuals while providing lightning-fast WebMCP JSON streams to AI agents. We analyze WooCommerce case studies and explore green web computing that slashes bandwidth by 90%! Soli Deo Gloria!`,
      koreanGuide: {
        summary: "Part 4 섹션 전환: AI 네이티브 아키텍처와 전자상거래",
        points: [
          "분리 계층 웹(Split-Layer Web): 인간에게는 미려한 화면을, AI에게는 초경량 WebMCP 데이터를 동시 서빙",
          "우커머스 실제 적용 사례와 대역폭 90% 절감의 친환경 그린 웹 엔지니어링"
        ],
        tips: "실제 상거래 비즈니스가 어떻게 10배 빠르게 변혁되는지 미래의 웹 표준을 선언하세요."
      },
      keyTerms: [
        {
          term: "Split-Layer Web Architecture",
          def: "Serving rich visual UI to human browsers while serving structured, lightweight WebMCP endpoints to AI agents simultaneously.",
          defKo: "분리 계층 웹 아키텍처 (인간-기계 이중 서빙)"
        }
      ]
    }
  },
  8: {
    2: {
      num: 2,
      type: "section",
      title: "PART 1: THE AGENTIC COMMERCE REVOLUTION & FRICTIONLESS CHECKOUT",
      subtitle: "Redeeming our time from the friction of commerce under Soli Deo Gloria",
      script: `We begin Part 1 of Session 8: "The Agentic Commerce Revolution & Frictionless Checkout."

Under Soli Deo Gloria, our goal is to liberate human energy from tedious transaction friction!

Today, shopping online requires endless tab searching, manual coupon hunting, and filling out credit card forms repeatedly. This friction drains three to four hours of executive attention every week!

In this opening module, we explore the rise of Agentic Commerce—where autonomous AI agents negotiate prices, verify stock, and execute purchases programmatically via UCP and AP2 protocols. Let us step into the future of commerce!`,
      koreanGuide: {
        summary: "Part 1 섹션 전환: 에이전틱 커머스 혁명과 마찰 없는 결제",
        points: [
          "상거래 마찰로부터의 시간 구속: 최저가 검색, 쿠폰 입력, 카드 결제의 피로한 반복 노역 해방",
          "에이전트가 프로그래밍 방식으로 가격을 협상하고 안전하게 결제를 완료하는 자율 상거래 패러다임"
        ],
        tips: "쇼핑의 번거로운 결제 과정을 AI가 알아서 안전하게 끝내주는 혁신의 문을 엽니다."
      },
      keyTerms: [
        {
          term: "Agentic Commerce",
          def: "Autonomous electronic commerce where AI agents search, negotiate, and execute financial transactions on behalf of users.",
          defKo: "에이전틱 커머스 (AI 자율 상거래)"
        }
      ]
    },
    11: {
      num: 11,
      type: "section",
      title: "PART 2: UNIVERSAL COMMERCE PROTOCOL (UCP)",
      subtitle: "Decoupling Execution from Web Interfaces & Native REST Endpoints",
      script: `We now cross into Part 2: "Universal Commerce Protocol (UCP)."

How do AI agents discover products and negotiate purchases without scraping web pages? 
Through UCP—the Universal Commerce Protocol!

In this section, we analyze the RESTful schema of UCP endpoints, product catalog vectorization, and how merchants expose structured JSON inventory directly to autonomous buyer agents. Let us unpack UCP!`,
      koreanGuide: {
        summary: "Part 2 섹션 전환: 범용 커머스 프로토콜 (UCP)",
        points: [
          "웹 화면 긁기(Scraping)를 벗어나 표준 REST 엔드포인트로 상품 재고와 가격을 즉시 교환하는 UCP 구조",
          "판매자와 구매자 에이전트 간의 기계 대 기계(M2M) 직통 통신 프로토콜 분석"
        ],
        tips: "화면을 거치지 않고 데이터 대 데이터로 거래가 성사되는 UCP의 강력한 효율을 전하세요."
      },
      keyTerms: [
        {
          term: "Universal Commerce Protocol (UCP)",
          def: "The open standard enabling AI agents to discover, negotiate, and transact goods directly with merchants via structured APIs.",
          defKo: "범용 커머스 프로토콜 (UCP)"
        }
      ]
    },
    21: {
      num: 21,
      type: "section",
      title: "PART 3: FINANCIAL PROTECTION VIA AP2 & DIGITAL MANDATES",
      subtitle: "Cryptographic Handshakes, Cart Lockouts, and Single-Use Virtual Cards",
      script: `We now enter Part 3: "Financial Protection via AP2 & Digital Mandates."

When we give AI agents authority to spend money, how do we prevent unauthorized runaway charges? 
Through AP2—Agent Payment Protocol!

In this section, we explore cryptographic Digital Mandates, budget ceiling lockouts, and single-use virtual token cards. Your agent can only spend up to your pre-authorized budget, with 100% cryptographic receipts! Let us inspect the financial vault!`,
      koreanGuide: {
        summary: "Part 3 섹션 전환: AP2와 디지털 위임장을 통한 금융 보호",
        points: [
          "에이전트의 무단 결제 및 예산 초과를 원천 봉쇄하는 AP2 프로토콜",
          "암호학적으로 서명된 디지털 위임장(Digital Mandate)과 일회용 가상 카드 토큰 결제 체계"
        ],
        tips: "돈을 쓰는 에이전트를 안심하고 부릴 수 있는 절대적인 금융 안전장치를 소개하세요."
      },
      keyTerms: [
        {
          term: "Agent Payment Protocol (AP2)",
          def: "The secure financial transaction protocol governing AI agent purchases via cryptographic mandates and strict budget limits.",
          defKo: "에이전트 결제 프로토콜 (AP2)"
        }
      ]
    },
    31: {
      num: 31,
      type: "section",
      title: "PART 4: GOVERNANCE, PRIVACY & THE AGENTIC FLYWHEEL",
      subtitle: "Human-on-the-Loop Governance, Zero-Data Retention, and Strategic Execution",
      script: `We now enter our final chapter, Part 4: "Governance, Privacy & The Agentic Flywheel."

How do early adopters build an insurmountable competitive moat using autonomous commerce? 
Through the Agentic Flywheel!

In this concluding section, we synthesize Human-on-the-Loop financial oversight, zero-data retention privacy policies, and the self-reinforcing flywheel of speed and cost reduction. Soli Deo Gloria!`,
      koreanGuide: {
        summary: "Part 4 섹션 전환: 거버넌스, 프라이버시, 그리고 에이전틱 플라이휠",
        points: [
          "인간 주권의 최종 결제 감독권과 개인정보 무보존 보안 정책",
          "거래 속도와 비용 절감이 선순환을 이루며 압도적 경쟁 우위를 창출하는 에이전틱 플라이휠 효과"
        ],
        tips: "자율 상거래 생태계의 선두주자가 되어 비즈니스를 승리로 이끄는 지혜를 전수하세요."
      },
      keyTerms: [
        {
          term: "Agentic Flywheel",
          def: "The accelerating operational advantage gained by deploying autonomous commerce agents that continuously compound cost and time savings.",
          defKo: "에이전틱 플라이휠 (자율 상거래 선순환)"
        }
      ]
    }
  },
  9: {
    2: {
      num: 2,
      type: "section",
      title: "PART 1: THE BROWSER AS THE OPERATING SYSTEM",
      subtitle: "Soli Deo Gloria: Reclaiming intellectual boundaries and browser security",
      script: `We begin Part 1 of Session 9: "The Browser as the Operating System & Security Matrix."

Under Soli Deo Gloria, guarding the fortress of the mind requires securing the digital gateway through which all data flows: the web browser.

Today, the web browser is no longer a simple document viewer; it is a full-fledged operating system running billions of lines of complex JavaScript and WebAssembly!

In this opening module, we analyze the browser security matrix—how Chrome V8 executes untrusted code, isolates processes, and guards against memory exploits. Let us explore the browser fortress!`,
      koreanGuide: {
        summary: "Part 1 섹션 전환: 운영체제로서의 웹 브라우저와 보안 매트릭스",
        "points": [
          "지적 경계선 수호와 Soli Deo Gloria: 모든 데이터의 관문인 웹 브라우저의 보안 요새화",
          "단순 문서 뷰어를 넘어 복잡한 코드가 실행되는 현대 브라우저(V8 엔진)의 구조와 보안 위협 분석"
        ],
        tips: "우리가 매일 쓰는 크롬 브라우저가 사실상 하나의 거대한 운영체제임을 깨닫게 해주세요."
      },
      keyTerms: [
        {
          term: "Browser OS Matrix",
          def: "The architectural reality where the modern web browser functions as an operating system running complex multi-process applications.",
          defKo: "브라우저 OS 매트릭스 (브라우저의 운영체제화)"
        }
      ]
    }
  },
  10: {
    2: {
      num: 2,
      type: "section",
      title: "PART 1: THE RISE OF 93-AGENT SWARMS",
      subtitle: "Soli Deo Gloria: Redeeming time for eternal higher calling under Ephesians 5:16",
      script: `We open Part 1 of Session 10: "The Rise of 93-Agent Swarms & Multi-Agent Orchestration."

Under our sacred motto, Soli Deo Gloria, we are called in Ephesians 5:16 to redeem our time. 

Why should a human developer write repetitive boilerplates, manual unit tests, and documentation files line by line? That mechanical syntax work steals your creative calling!

In this opening module, we explore the breakthrough of Antigravity 2.0 and the coordination of 93 specialized subagents executing code in parallel. Let us step onto the podium as sovereign conductors!`,
      koreanGuide: {
        summary: "Part 1 섹션 전환: 93개 에이전트 군집의 출현과 다중 에이전트 오케스트레이션",
        points: [
          "에베소서 5:16 세월을 아끼라: 반복적인 코드 타이핑 노역에서 개발자의 영혼을 구속하는 사명",
          "Antigravity 2.0의 93개 전문 서브에이전트가 병렬로 소프트웨어를 구축하는 군집 지능의 서막"
        ],
        tips: "1인 개발자가 93명의 정예 개발팀을 거느린 최고기술책임자(CTO)로 도약하는 감동을 전하세요."
      },
      keyTerms: [
        {
          term: "93-Agent Swarm",
          def: "The coordinated fleet of specialized AI subagents executing software architecture, testing, and debugging concurrently in Antigravity 2.0.",
          defKo: "93-에이전트 군집 (병렬 소프트웨어 개발 함대)"
        }
      ]
    }
  },
  11: {
    2: {
      num: 2,
      type: "section",
      title: "PART 1: THE CRISIS OF BENCHMARK SATURATION & TRUE AI SCIENCE",
      subtitle: "Soli Deo Gloria: Stewardship of truth and scientific verification",
      script: `We begin Part 1 of Session 11: "The Crisis of Benchmark Saturation & True AI Science."

Under Soli Deo Gloria, we are stewards of objective truth. 

Today, AI marketing is plagued by saturated benchmarks—models memorizing multiple-choice questions to score 95% on MMLU while failing at simple real-world reasoning!

In this opening module, we deconstruct the difference between rote memorization and true scientific deduction. We introduce Google's HeurekaBench—testing whether an AI can deduce hidden scientific laws through genuine hypothesis testing! Let us uncover True AI Science!`,
      koreanGuide: {
        summary: "Part 1 섹션 전환: 벤치마크 포화의 위기와 진정한 AI 과학",
        points: [
          "진리의 청지기직과 Soli Deo Gloria: 단순 객관식 족보 암기로 부풀려진 AI 벤치마크 거품 비판",
          "기억력 테스트를 넘어 실제 가설을 세우고 실험을 통해 물리 법칙을 유도해내는 HeurekaBench의 참된 과학 지능"
        ],
        tips: "마케팅 숫자에 속지 않고 기계의 진짜 연역적 추론 능력을 검증하는 엄정한 학문적 안목을 전수하세요."
      },
      keyTerms: [
        {
          term: "True AI Science",
          def: "The rigorous evaluation of an AI model's ability to deduce undiscovered scientific principles through active hypothesis experimentation.",
          defKo: "진정한 AI 과학 (연역적 법칙 유도 지능)"
        }
      ]
    }
  },
  12: {
    2: {
      num: 2,
      type: "section",
      title: "PART 1: WORLD MODELS: BEYOND NEXT-TOKEN PREDICTION",
      subtitle: "The Spiritual Mandate: Reclaiming human time for sacred creation under Soli Deo Gloria",
      script: `We open Part 1 of Session 12: "World Models: Beyond Next-Token Prediction to 3D Simulation."

Under Soli Deo Gloria, we explore how computing ascends from manipulating text to simulating the physical creation itself!

For years, AI was limited to next-token text prediction. But language cannot capture the physics of gravity, fluid dynamics, and 3D collisions.

In this opening module, we explore World Models and Google's Genie 3—simulating photorealistic 3D interactive virtual worlds in real time at 30 frames per second. Let us step into the simulated universe!`,
      koreanGuide: {
        summary: "Part 1 섹션 전환: 월드 모델 - 다음 토큰 예측을 넘어 3D 시뮬레이션으로",
        points: [
          "영적 소명과 창조 세계의 시뮬레이션: 텍스트 글자 놀이를 넘어 물리 법칙이 지배하는 가상 세계 합성",
          "초당 30프레임으로 상호작용 가능한 3차원 입체 시공간을 생성하는 Google Genie 3 월드 모델의 등장"
        ],
        tips: "단순한 챗봇을 넘어 기계가 물리적 현실 세계의 인과관계를 이해하기 시작한 대격변을 선언하세요."
      },
      keyTerms: [
        {
          term: "World Model (월드 모델)",
          def: "An AI architecture that constructs an internal 3D simulation of physical reality, predicting continuous spatio-temporal consequences.",
          defKo: "월드 모델 (물리 시뮬레이션 신경망)"
        }
      ]
    },
    11: {
      num: 11,
      type: "section",
      title: "PART 2: UNDER THE HOOD OF PHYSICAL REALISM",
      subtitle: "Spatio-Temporal Video Tokenizers and the 280-Billion Street View Moat",
      script: `We now cross into Part 2: "Under the Hood of Physical Realism."

How does a neural network simulate continuous 3D environments without losing geometric consistency?

In this section, we analyze Spatio-Temporal Video Tokenizers, the Video-Masked-Conditioning (VMC) architecture, and Google's 280-billion Street View panoramic image moat. We discover how agents maintain persistent 3D spatial memory across kilometers of continuous motion! Let us look under the hood!`,
      koreanGuide: {
        summary: "Part 2 섹션 전환: 물리적 현실감의 내부 메커니즘",
        points: [
          "시공간 비디오 토크나이저와 VMC 아키텍처를 통한 3D 기하학적 일관성 유지",
          "구글이 수십 년간 축적한 2,800억 장의 스트리트 뷰 파노라마 데이터 해자(Moat)"
        ],
        tips: "기억상실증 없이 수 킬로미터를 주행해도 배경이 일그러지지 않는 압도적 기술력을 설명하세요."
      },
      keyTerms: [
        {
          term: "Spatio-Temporal Consistency",
          def: "Maintaining stable 3D geometry and object persistence across long-duration continuous video generation.",
          defKo: "시공간 기하학적 일관성"
        }
      ]
    },
    21: {
      num: 21,
      type: "section",
      title: "PART 3: WAYMO AND THE INFINITE SAFE CLASSROOM",
      subtitle: "Simulating Dangerous Edge Cases and Eliminating Real-World Highway Hazards",
      script: `We now enter Part 3: "Waymo and the Infinite Safe Classroom."

Why is testing autonomous vehicles on real physical highways slow, expensive, and dangerous?

In this section, we analyze Waymo's simulation paradigm: generating 10,000 parallel swarm vehicles inside Genie 3 simulators! We test extreme edge cases—blizzards, jaywalkers, and brake failures—without endangering a single human life! Let us step into the infinite classroom!`,
      koreanGuide: {
        summary: "Part 3 섹션 전환: 웨이모(Waymo)와 무한한 안전 교실",
        points: [
          "실제 고속도로에서 사람 목숨을 걸고 자율주행을 훈련하는 위험성 탈피",
          "Genie 3 가상 시뮬레이터 안에서 10,000대의 웨이모 차량을 동시 기동하여 극한의 돌발 사고를 무한 학습"
        ],
        tips: "가상 세계 시뮬레이션이 어떻게 인간의 생명을 지키고 개발 속도를 10,000배 높이는지 역설하세요."
      },
      keyTerms: [
        {
          term: "Infinite Safe Classroom",
          def: "High-fidelity 3D simulation environments where autonomous AI agents train on hazardous edge cases without real-world risk.",
          defKo: "무한한 안전 교실 (가상 위험 훈련장)"
        }
      ]
    },
    31: {
      num: 31,
      type: "section",
      title: "PART 4: STRATEGIC GOVERNANCE & CREATIVE SOVEREIGNTY",
      subtitle: "Data Privacy Sandboxes, Anti-Training Seals, and Human Conductor Stewardship",
      script: `We now enter our final chapter, Part 4: "Strategic Governance & Creative Sovereignty."

When World Models can synthesize hyper-realistic 3D realities, how do we prevent deepfakes and intellectual property theft?

In this concluding section, we establish enterprise privacy sandboxes, cryptographic anti-training seals, and define the human architect's role as the sovereign ethical conductor of simulated worlds. Soli Deo Gloria!`,
      koreanGuide: {
        summary: "Part 4 섹션 전환: 전략적 거버넌스와 창조적 주권",
        points: [
          "가상 세계 모델의 기밀 유출과 악용을 방지하는 데이터 프라이버시 샌드박스와 안티 트레이닝 봉인",
          "가상 세계를 윤리적이고 창의적으로 지휘하는 인간 아키텍트의 주권적 청지기 사명"
        ],
        tips: "현실과 구별되지 않는 가상 세계를 다루는 아키텍트의 높은 도덕적 책무를 천명하세요."
      },
      keyTerms: [
        {
          term: "World Model Governance",
          def: "The ethical and security frameworks ensuring photorealistic 3D simulations are used safely with zero IP leakage.",
          defKo: "월드 모델 거버넌스"
        }
      ]
    }
  },
  13: {
    2: {
      num: 2,
      type: "section",
      title: "PART 1: THE TRAGEDY OF RASTER SCALE & CALCULATED VECTOR ART",
      subtitle: "Soli Deo Gloria: Perfect forms in mathematical order and infinite precision",
      script: `We begin Part 1 of Session 13: "The Tragedy of Raster Scale & Calculated Vector Art."

Under Soli Deo Gloria, we pursue the divine perfection of mathematical order. 

For decades, digital graphics relied on raster pixels—static grids of dots. But when you zoom into a raster image, it collapses into blurry jagged blocks, and file sizes explode quadratically!

In this opening module, we celebrate Calculated Art: SVG Vector Engineering! Instead of storing colored dots, SVG stores pure mathematical equations. A few kilobytes scale infinitely to 8K and beyond with razor-sharp clarity! Let us explore Part 1!`,
      koreanGuide: {
        summary: "Part 1 섹션 전환: 래스터 스케일의 비극과 계산된 벡터 예술",
        points: [
          "수학적 질서와 Soli Deo Gloria: 확대하면 깨지고 용량이 폭증하는 래스터(픽셀)의 비극 극복",
          "몇 킬로바이트의 가벼운 수학 방정식으로 8K 디스플레이까지 무한히 선명하게 뻗어 나가는 SVG 벡터 엔지니어링"
        ],
        tips: "픽셀의 한계를 뛰어넘어 영원히 깨지지 않는 수학적 벡터의 아름다움을 선포하세요."
      },
      keyTerms: [
        {
          term: "Calculated Vector Art",
          def: "Digital visual graphics rendered via deterministic mathematical geometry rather than static pixel grids.",
          defKo: "계산된 벡터 예술 (SVG 수학 렌더링)"
        }
      ]
    }
  },
  14: {
    2: {
      num: 2,
      type: "section",
      title: "PART 1: DROPPING THE CAMERA: FROM CAPTURE TO GENERATIVE CURATION",
      subtitle: "Soli Deo Gloria: Reclaiming time for higher artistic callings under Ephesians 5:16",
      script: `We now open Part 1 of Session 14: "Dropping the Camera: From Capture to Generative Curation."

Under our sacred banner of Soli Deo Gloria, we are called in Ephesians 5:16 to redeem our time. 

For over a century, filmmaking was bound by the physical gravity of camera lenses, lighting trucks, and multimillion-dollar budgets.

In this opening module, we cross the threshold into Generative Curation! 
The modern filmmaker writes specifications and directs AI pipelines to synthesize photorealistic 3D cinematic scenes with native audio! Let us drop the camera and take the director's chair!`,
      koreanGuide: {
        summary: "Part 1 섹션 전환: 카메라를 내려놓고 생성형 큐레이션으로 도약",
        points: [
          "에베소서 5:16과 예술적 소명: 무거운 카메라 장비와 물리적 자본의 중력에서 벗어나는 시네마 민주화",
          "카메라를 쥐고 헤매는 대신 프롬프트 명세서를 통해 헐리우드급 3D 장면을 합성·지휘하는 큐레이터로의 진화"
        ],
        tips: "100년간의 전통 영화 제작 문법을 깨부수고 AI 파이프라인의 지휘관으로 등극하는 서막을 여세요."
      },
      keyTerms: [
        {
          term: "Generative Curation",
          def: "The modern filmmaking paradigm where creators specify constraints and select optimal outputs from generative AI engines.",
          defKo: "생성형 큐레이션 (Generative Curation)"
        }
      ]
    }
  }
};

// Apply updates
for (let sessId = 1; sessId <= 14; sessId++) {
  const updates = updatesBySession[sessId];
  if (updates) {
    const slides = allData['SLIDES_SESSION_' + sessId];
    if (slides) {
      for (const [slideNum, newSlide] of Object.entries(updates)) {
        const num = parseInt(slideNum, 10);
        const idx = slides.findIndex(s => s.num === num);
        if (idx !== -1) {
          slides[idx] = Object.assign({}, slides[idx], newSlide);
          console.log(`Updated Session ${sessId} Slide ${num} -> [${newSlide.type}] ${newSlide.title}`);
        }
      }
    }
  }
}

// Generate new slidesData.js content
let newFileContent = '// Session 1 to 15 Master Slide Data (40 Slides per session, 600 Slides total)\n';
newFileContent += '// Designed for 60-minute English lectures with easy-to-read ESL scripts and Korean teaching guides\n\n';
newFileContent += 'export const SESSIONS = ' + JSON.stringify(allData.SESSIONS, null, 2) + ';\n\n';

for (let i = 1; i <= 15; i++) {
  newFileContent += `export const SLIDES_SESSION_${i} = ` + JSON.stringify(allData['SLIDES_SESSION_' + i], null, 2) + ';\n\n';
}

fs.writeFileSync(slidesDataPath, newFileContent, 'utf8');
console.log('Successfully wrote updated slidesData.js with consistent Part 1, 2, 3, 4 dividers across all 15 sessions!');
