# -*- coding: utf-8 -*-
"""
Oikos University - Session 5 Clean 45-Slide Master Generator
Course: The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom
Session 5: From Personal Drawer to System Vault: Enterprise Google Drive Mastery, Apps Script Automation & Governance
Features:
- Full 45 Slides with 3-Presenter Trio (Prof. Peter Kim, TA Sarah Jenkins, TA James Wilson)
- Clean 4-Part Structure (Part 1: Slide 2, Part 2: Slide 12, Part 3: Slide 23, Part 4: Slide 30)
- 5 Practical Enterprise Case Studies:
    1. Slide 11: Lost Aviation Maintenance Manual Instant Recovery via Drive OCR
    2. Slide 22: 50TB Media Studio 0MB File Streaming Deployment
    3. Slide 29: Preventing a $500K Exfiltration Breach via Drive DRM Policy
    4. Slide 36: 24/7 Automated Vendor Invoice Triage & GAS Approval Bot
    5. Slide 44: 18X Enterprise Productivity ROI & 7-Step Drive Vault Blueprint
- Full sync with session5.md and slidesData.js (SLIDES_SESSION_5)
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
SESSION5_MD = os.path.join(BASE_DIR, "session5.md")

SLIDES_45_SESSION_5 = [
    # Slide 1: Course Title
    {
        "num": 1,
        "type": "title",
        "title": "OIKOS UNIVERSITY • SOLI DEO GLORIA",
        "subtitle": "THE ARCHITECT OF INTELLIGENCE: Mastering Agentic IT & Strategic Wisdom",
        "detail": "Session 5: From Personal Drawer to System Vault: Enterprise Google Drive Mastery, Apps Script Automation & Governance",
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab",
        "script": (
            "[Prof. Peter] Welcome back, global leaders and scholars, to Oikos University! I am Professor Peter Kim, Director of Smart Insight Lab. Today on Slide 1, we inaugurate Session 5: \"From Personal Drawer to System Vault: Enterprise Google Drive Mastery, Apps Script Automation & Governance.\"\n\n"
            "[TA Sarah] Hello everyone! I am Sarah Jenkins, Senior AI Fellow. In Session 4, we built private RAG knowledge factories. But an AI engine is only as good as the underlying document repository! Today, we master the enterprise knowledge vault.\n\n"
            "[TA James] And I am James Wilson, your DevOps & Infrastructure TA! Out in enterprise companies, cloud storage is usually a toxic landfill of duplicate files, broken permissions, and tribal knowledge trapped in personal inboxes. Today, we show you how to turn that landfill into a hardened, automated system vault with Google Apps Script!\n\n"
            "[Prof. Peter] Under our founding motto, \"SOLI DEO GLORIA—To God Alone Be the Glory,\" our mission is to transform personal digital chaos into structured institutional assets that endure across generations.\n\n"
            "[TA Sarah] Let us open Part 1 and explore the Enterprise Drive Revolution on Slide 2!"
        ),
        "koreanGuide": {
            "summary": "Session 5 개요 및 Oikos University 3인 강사진(피터 교수, 사라 수석조교, 제임스 개발조교) 환영 인사",
            "points": [
                "강의 주제: 개인 서랍에서 시스템 금고로: 엔터프라이즈 구글 드라이브 마스터리 및 Apps Script 자동화",
                "파편화된 개인 저장소의 한계를 극복하고 기업의 집단 지성을 자산화하는 공유 드라이브 아키텍처 수립",
                "Google Apps Script(GAS)를 활용한 24/7 무중단 파일 수집, 메타데이터 태깅, 자동 아카이빙 파이프라인 구축"
            ],
            "tips": "피터 교수의 제도적 지식 보존 철학과 사라 조교의 시스템적 접근, 제임스 조교의 실전 클라우드 거버넌스 에너지를 결합해 활기차게 시작하세요."
        },
        "keyTerms": [
            {
                "term": "System Vault",
                "def": "An institutional, highly structured enterprise repository engineered for automated indexing, governance, and persistence.",
                "defKo": "시스템 금고 (조직 공용 지식 저장소)"
            },
            {
                "term": "Google Apps Script (GAS)",
                "def": "A cloud-based JavaScript runtime environment for automating workflows across Google Workspace applications.",
                "defKo": "구글 앱스 스크립트 (GAS 자동화 엔진)"
            }
        ]
    },
    # Slide 2: Part 1 Section Divider
    {
        "num": 2,
        "type": "section",
        "title": "PART 1: THE ENTERPRISE DRIVE REVOLUTION & KNOWLEDGE VAULT",
        "subtitle": "Overcoming the tragedy of personal drawers and establishing institutional memory under Soli Deo Gloria",
        "script": (
            "[TA Sarah] Look at Slide 2: \"PART 1: THE ENTERPRISE DRIVE REVOLUTION & KNOWLEDGE VAULT.\" Professor, why do so many highly educated teams struggle with basic cloud file organization?\n\n"
            "[Prof. Peter] Because humans treat digital storage like an infinite physical junk drawer! When storage was physical paper, you had to clean your filing cabinets. With the cloud, people dump everything into 'My Drive' and rely on lazy keyword searches until critical files vanish into the void.\n\n"
            "[TA James] In enterprise IT, 'My Drive' is a ticking liability bomb. Files owned by individuals disappear when they resign, permissions leak externally, and automated scripts crash due to inconsistent folder paths.\n\n"
            "[TA Sarah] In Part 1, we dismantle the 'Personal Drawer' mindset and build a culture of institutional system ownership.\n\n"
            "[Prof. Peter] Let us examine the Smart Insight Lab philosophy of Corporate Memory on Slide 3."
        ),
        "koreanGuide": {
            "summary": "Part 1 섹션 전환: 엔터프라이즈 드라이브 혁명과 개인 서랍 증후군 극복",
            "points": [
                "개인 서랍(My Drive)의 비극: 무한 클라우드 용량이 낳은 무책임한 파일 방치와 검색 마비",
                "엔터프라이즈 리스크: 직원 퇴사 시 문서 유실, 권한 누수, 스크립트 경로 파손 등의 치명적 결함",
                "조직적 소유권: 개인의 소유가 아닌 시스템이 영구 관리하는 공유 드라이브(Shared Drives) 전환"
            ],
            "tips": "사라 조교가 개인 서랍 증후군을 지적하고 제임스가 실무 장애를 경고하며 피터 교수가 제도적 자산화 비전을 제시합니다."
        },
        "keyTerms": [
            {
                "term": "Personal Drawer Syndrome",
                "def": "The counterproductive habit of siloing mission-critical organizational documents inside unmanaged personal drives.",
                "defKo": "개인 서랍 증후군 (문서 고립화)"
            },
            {
                "term": "Institutional Memory",
                "def": "The collective knowledge, historical records, and operational assets preserved systematically within an enterprise.",
                "defKo": "제도적 기억 (기업 집단 지성)"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 3: Smart Insight Lab: Corporate Memory
    {
        "num": 3,
        "type": "content",
        "title": "SMART INSIGHT LAB: CORPORATE MEMORY",
        "subtitle": "Treating institutional knowledge as a living, searchable, and permanent digital asset",
        "points": [
            "Corporate Memory as Capital: Documented intellectual property is more valuable than physical office space.",
            "Zero Knowledge Evaporation: Ensuring that when an employee departs, 100% of their operational wisdom remains.",
            "Autonomous Searchability: Structuring repositories so that AI agents can index and retrieve facts instantly."
        ],
        "script": (
            "[Prof. Peter] Slide 3 highlights \"SMART INSIGHT LAB: CORPORATE MEMORY.\" In the 21st century, the most valuable capital of any enterprise is its intellectual capital!\n\n"
            "[TA Sarah] Yet, in most organizations, corporate memory is completely transient. When a key senior engineer or executive leaves, all their undocumented domain knowledge evaporates overnight.\n\n"
            "[TA James] If your operational workflows are documented inside Google Docs and structured in Shared Drives with automated Apps Script triggers, your company never suffers amnesia. Onboarding a new hire takes 2 days instead of 6 months!\n\n"
            "[Prof. Peter] Knowledge preservation is not a bureaucratic chore; it is an act of ethical stewardship.\n\n"
            "[TA Sarah] Let us inspect the silent drain of tribal knowledge on Slide 4."
        ),
        "koreanGuide": {
            "summary": "스마트 인사이트 랩: 기업 집단 기억(Corporate Memory)의 자산화 철학",
            "points": [
                "지적 자본의 가치: 물리적 부동산보다 체계화된 문서와 지식 자산이 기업의 핵심 경쟁력",
                "지식 증발 방지: 핵심 인력 퇴사 시에도 운영 노하우와 시스템 아키텍처가 100% 보존되는 환경",
                "신규 입사자 온보딩 혁신: 체계적인 지식 금고를 통해 적응 기간을 6개월에서 2일로 단축"
            ],
            "tips": "피터 교수가 지식 보존의 청지기적 가치를 설파하고 제임스가 온보딩 단축의 실무 효과를 입증합니다."
        },
        "keyTerms": [
            {
                "term": "Corporate Memory",
                "def": "The total accumulated intellectual assets, processes, and historical records of an organization.",
                "defKo": "기업 기억 (조직 집단 자산)"
            },
            {
                "term": "Knowledge Evaporation",
                "def": "The permanent loss of vital operational expertise when departing employees take undocumented knowledge with them.",
                "defKo": "지식 증발 현상"
            }
        ]
    },
    # Slide 4: The Silent Drain: Tribal Knowledge
    {
        "num": 4,
        "type": "content",
        "title": "THE SILENT DRAIN: TRIBAL KNOWLEDGE",
        "subtitle": "The invisible cost of unwritten rules, undocumented scripts, and private inbox silos",
        "points": [
            "Tribal Knowledge Trap: Information exists only in the minds of a few veterans, creating severe bottlenecks.",
            "Single Point of Failure (SPOF): If the key person is on vacation or sick, critical business processes grind to a halt.",
            "Systemic Vulnerability: Tribal systems cannot be scaled, automated, or integrated with AI agent swarms."
        ],
        "script": (
            "[TA Sarah] Slide 4 examines \"THE SILENT DRAIN: TRIBAL KNOWLEDGE.\" James, what is tribal knowledge in engineering teams?\n\n"
            "[TA James] Tribal knowledge is when only 'Bob' knows how to deploy the payment gateway, only 'Alice' knows the secret SQL query, and nobody wrote it down! If Bob goes on vacation in Hawaii, the whole company is paralyzed!\n\n"
            "[Prof. Peter] That creates a dangerous Single Point of Failure (SPOF). It breeds anxiety, prevents team scaling, and makes AI automation impossible. An AI agent cannot query a brain sitting on a beach; an agent queries a structured Google Drive vault!\n\n"
            "[TA Sarah] By transforming tribal lore into structured Google Docs, you liberate both the individuals and the company.\n\n"
            "[TA James] Let us analyze the tragedy of personal drawers on Slide 5!"
        ),
        "koreanGuide": {
            "summary": "조용한 지식 누수: 구전 지식(Tribal Knowledge)의 함정과 단일 장애점(SPOF)",
            "points": [
                "구전 지식의 위험: 특정 베테랑 직원 몇 명의 머릿속에만 존재하는 미문서화 노하우",
                "단일 장애점(SPOF): 담당자 휴가나 부재 시 결제 시스템이나 배포가 완전히 마비되는 취약성",
                "AI 연동 불가: 에이전트는 인간의 뇌를 읽을 수 없으며, 오직 체계화된 드라이브 문서만을 검색 가능"
            ],
            "tips": "제임스 조교의 생생한 '하와이 휴가' 예시를 통해 구전 지식의 치명적 리스크를 부각하세요."
        },
        "keyTerms": [
            {
                "term": "Tribal Knowledge",
                "def": "Unwritten information, operational know-how, and organizational habits that are not formally documented.",
                "defKo": "구전 지식 (미문서화 부족 지식)"
            },
            {
                "term": "Single Point of Failure (SPOF)",
                "def": "A component or person whose failure or absence causes the entire system to stop functioning.",
                "defKo": "단일 장애점 (SPOF)"
            }
        ]
    },
    # Slide 5: The Tragedy of Personal Drawers
    {
        "num": 5,
        "type": "comparison",
        "title": "THE TRAGEDY OF PERSONAL DRAWERS",
        "subtitle": "Contrasting fragmented individual storage with centralized enterprise shared vaults",
        "leftCard": {
            "tag": "PERSONAL DRAWER (MY DRIVE)",
            "title": "Fragile Individual Silos",
            "points": [
                "File ownership tied to personal user accounts.",
                "Files deleted permanently when employee account is deprovisioned.",
                "Disorganized folder sprawl with chaotic naming conventions.",
                "Zero automated governance or programmatic webhooks."
            ]
        },
        "rightCard": {
            "tag": "SYSTEM VAULT (SHARED DRIVE)",
            "title": "Institutional Fortress",
            "points": [
                "File ownership held exclusively by the organization.",
                "Files persist permanently regardless of personnel turnover.",
                "Strict taxonomic color coding and ISO naming standards.",
                "Event-driven Apps Script webhooks for auto-indexing."
            ]
        },
        "script": (
            "[TA Sarah] Look at Slide 5: \"THE TRAGEDY OF PERSONAL DRAWERS.\" On the left, we see the traditional 'My Drive'.\n\n"
            "[TA James] It is an operational catastrophe: files are owned by the individual user. When IT disables that account after resignation, the files enter a 30-day deletion countdown, and all shared links across the company break instantly!\n\n"
            "[Prof. Peter] On the right, we have the System Vault—Google Workspace Shared Drives. The organization owns the files! People come and go, but the knowledge fortress remains immutable and eternally accessible.\n\n"
            "[TA Sarah] Furthermore, Shared Drives enforce ISO naming standards and trigger automated Google Apps Script webhooks for real-time indexing.\n\n"
            "[TA James] Let us inspect the terrifying 20-day deletion countdown on Slide 6!"
        ),
        "koreanGuide": {
            "summary": "개인 서랍의 비극 vs 시스템 금고: 개인 드라이브와 공유 드라이브의 구조적 대비",
            "points": [
                "개인 드라이브: 파일 소유권이 개인에게 귀속되어 퇴사 시 30일 삭제 타이머 작동 및 전사 링크 파손",
                "시스템 금고(공유 드라이브): 파일 소유권이 조직에 영구 귀속되어 인사 변동과 무관하게 데이터 보존",
                "ISO 표준 명명 규칙 및 Google Apps Script 웹훅을 통한 자동 인덱싱 지원"
            ],
            "tips": "사라와 제임스가 개인 드라이브의 위험성을 대비하여 공유 드라이브의 안정성을 설득력 있게 제시합니다."
        },
        "keyTerms": [
            {
                "term": "Account Deprovisioning",
                "def": "The administrative process of disabling and deleting a user's corporate credentials and storage access upon departure.",
                "defKo": "계정 비활성화 및 회수"
            },
            {
                "term": "Shared Drive Sovereignty",
                "def": "Enterprise data governance ensuring all assets are owned by the organization rather than individual employees.",
                "defKo": "공유 드라이브 조직 주권"
            }
        ]
    },
    # Slide 6: The 20-Day Countdown
    {
        "num": 6,
        "type": "content",
        "title": "THE 20-DAY COUNTDOWN: AVOIDABLE CATASTROPHE",
        "subtitle": "How corporate files vanish into Google Workspace trash when departing users are deleted",
        "points": [
            "The Deprovisioning Trap: Admin deletes departing employee account; all personal files enter trash.",
            "The 20-Day Purge Window: Admins have only 20 days to manually transfer files before permanent unrecoverable deletion.",
            "The Architectural Vaccine: Mandating Shared Drives prevents 100% of deprovisioning data losses."
        ],
        "script": (
            "[Prof. Peter] Slide 6 details \"THE 20-DAY COUNTDOWN: AN AVOIDABLE CATASTROPHE.\" Many IT administrators don't realize this brutal reality until it is too late.\n\n"
            "[TA James] When an IT admin deletes a user account in Google Workspace, Google gives a 20-day grace period. If nobody manually transfers ownership of those files within 20 days, Google's servers purge them permanently from disk. There is NO backup, NO undo button, and NO support ticket that can restore them!\n\n"
            "[TA Sarah] Imagine losing five years of proprietary research, legal contracts, or customer data because of a simple administrative oversight!\n\n"
            "[Prof. Peter] The architectural vaccine is absolute: never store organizational assets in personal drives. Mandate Shared Drives across your entire institution.\n\n"
            "[TA Sarah] Let us inspect how Shared Drives enforce system ownership on Slide 7."
        ),
        "koreanGuide": {
            "summary": "20일 카운트다운의 비극: 퇴사자 계정 삭제로 인한 영구 데이터 유실 메커니즘",
            "points": [
                "구글 워크스페이스 관리자 함정: 계정 삭제 시 개인 드라이브 문서가 휴지통으로 직행",
                "20일 영구 삭제 유예 기간: 20일 내 소유권 이전을 수동으로 하지 않으면 복구 불가능하게 영구 증발",
                "건축적 백신: 전사 모든 문서를 공유 드라이브에 강제 보관함으로써 계정 삭제 리스크 원천 차단"
            ],
            "tips": "제임스 조교가 20일 카운트다운의 긴박함을 강조하며 수강생들에게 시스템적 예방의 중요성을 일깨웁니다."
        },
        "keyTerms": [
            {
                "term": "20-Day Purge Window",
                "def": "Google Workspace's strict recovery time limit before deleted user account data is permanently erased.",
                "defKo": "20일 영구 삭제 유예 기간"
            },
            {
                "term": "Deprovisioning Vaccine",
                "def": "The architectural practice of using Shared Drives to decouple document persistence from employee account lifecycles.",
                "defKo": "계정 삭제 리스크 백신 아키텍처"
            }
        ]
    },
    # Slide 7: System Ownership: Shared Drives
    {
        "num": 7,
        "type": "content",
        "title": "SYSTEM OWNERSHIP: SHARED DRIVES",
        "subtitle": "Decoupling organizational assets from individual employee lifecycles",
        "points": [
            "Root Ownership: The domain organization owns all files; individual users are merely temporary stewards.",
            "Consistent URI Paths: Folder structures remain stable, preventing broken links in automated scripts.",
            "Centralized Quotas: Storage pool is shared organization-wide, eliminating individual storage cap limits."
        ],
        "script": (
            "[TA Sarah] Slide 7 diagrams \"SYSTEM OWNERSHIP: SHARED DRIVES.\" Look at how ownership is rooted at the organizational domain level.\n\n"
            "[TA James] When you create a Shared Drive—such as `Smart_Insight_Lab_Core`—every document added belongs to the domain. If an engineer resigns, their access is revoked, but the document URL, the folder hierarchy, and the automated Apps Script triggers remain 100% intact!\n\n"
            "[Prof. Peter] This provides continuous stability. Your systems, bots, and research teams operate on permanent foundations rather than shifting sands.\n\n"
            "[TA Sarah] Let us launch an interactive poll on Slide 8 to see where our global students store their files!"
        ),
        "koreanGuide": {
            "summary": "시스템 소유권: 공유 드라이브를 통한 데이터 주권과 지속성 확보",
            "points": [
                "도메인 조직 귀속: 파일 소유권이 최상위 조직에 속하며 개인은 일시적 관리자 역할만 수행",
                "안정적인 URI 경로: 폴더 구조와 문서 링크가 영구 유지되어 자동화 스크립트 장애 방지",
                "중앙 집중식 스토리지 풀: 개인별 용량 제한에 구애받지 않고 조직 단위의 통합 용량 운용"
            ],
            "tips": "사라 조교와 피터 교수가 공유 드라이브가 주는 영구적 연속성과 안정성을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Domain-Level Ownership",
                "def": "Data governance where intellectual property is legally and technically held by the organization's cloud domain.",
                "defKo": "도메인 조직 소유권"
            },
            {
                "term": "URI Stability",
                "def": "The permanence of document web addresses, preventing broken links across scripts and integrations.",
                "defKo": "URI 주소 영속성"
            }
        ]
    },
    # Slide 8: Interactive Poll: Where Are Your Files?
    {
        "num": 8,
        "type": "poll",
        "title": "📨 INTERACTIVE POLL: WHERE ARE YOUR FILES?",
        "subtitle": "Where does your team store its most mission-critical operational documentation?",
        "pollOptions": [
            "Option A: Centralized Shared Drives with strict taxonomy & naming rules",
            "Option B: Mixed setup (some Shared Drives, but mostly messy personal 'My Drive')",
            "Option C: Local desktop folders and laptop hard drives (zero cloud sync)",
            "Option D: Scattered across personal inboxes, Slack DMs, and WhatsApp chats"
        ],
        "script": (
            "[Prof. Peter] Slide 8 is our \"INTERACTIVE POLL: WHERE ARE YOUR FILES?\" Take out your devices and cast your vote right now!\n\n"
            "[TA Sarah] The question is: \"Where does your team store its most mission-critical operational documentation?\"\n\n"
            "[TA James] Option A: Centralized Shared Drives with strict taxonomy. Option B: Mixed setup with messy personal drives. Option C: Local desktop hard drives. Or Option D: Scattered across private Slack DMs and WhatsApp chats!\n\n"
            "[TA Sarah] The responses are flooding in, and the reality is striking.\n\n"
            "[Prof. Peter] Let us analyze the poll results and calculate the cost of search on Slide 9."
        ),
        "koreanGuide": {
            "summary": "실시간 수강생 설문: 팀의 핵심 업무 문서 저장 위치 실태 조사",
            "points": [
                "실시간 투표를 통한 수강생 소속 조직의 문서 보관 방식 진단",
                "개인 드라이브 및 슬랙 DM에 파편화된 문서 저장 실태 정량화",
                "체계적인 공유 드라이브 지식 금고 구축에 대한 학습 동기 부여"
            ],
            "tips": "제임스 조교와 사라 조교가 유쾌하고 솔직한 분위기로 투표를 유도하세요."
        },
        "keyTerms": [
            {
                "term": "Storage Taxonomy",
                "def": "A systematic, hierarchical classification scheme organizing enterprise files into logical categories.",
                "defKo": "스토리지 분류 체계 (택소노미)"
            },
            {
                "term": "Fragmented Sprawl",
                "def": "The uncontrolled dispersion of corporate data across uncoordinated chat channels and personal hard drives.",
                "defKo": "파편화된 데이터 확산"
            }
        ]
    },
    # Slide 9: Analyzing the Poll: The Cost of Search
    {
        "num": 9,
        "type": "content",
        "title": "ANALYZING THE POLL: THE COST OF SEARCH",
        "subtitle": "Over 72% of teams operate in fragmented silos, losing 2.5 hours per employee daily",
        "points": [
            "Survey Insight: 72% of respondents selected Options B, C, & D (fragmented personal sprawl).",
            "The Financial Drag: A 100-person team loses 250 hours every single day hunting for lost files.",
            "The Antidote: A standardized 5-tier folder taxonomy backed by Google Apps Script automation."
        ],
        "script": (
            "[TA Sarah] Slide 9 reveals the \"POLL ANALYSIS: THE COST OF SEARCH.\" Look at that chart: over 72% of teams suffer from fragmented storage sprawl!\n\n"
            "[TA James] Do the arithmetic on a 100-person company: losing 2.5 hours per person per day equals 250 lost hours every day! At an average tech salary, that company burns over 2.5 million dollars every year just paying people to search for lost files!\n\n"
            "[Prof. Peter] Think about the sheer waste of human lifespan and financial resources! That is why we treat file architecture not as minor housekeeping, but as a critical executive strategy.\n\n"
            "[TA Sarah] Let us inspect our full learning roadmap on Slide 10."
        ),
        "koreanGuide": {
            "summary": "설문 결과 분석: 72%가 겪는 파편화 스토리지와 연간 수백만 달러의 검색 비용 손실",
            "points": [
                "수강생의 72%가 개인 드라이브, 로컬 디스크, 슬랙 등에 문서가 분산되어 고통받음",
                "100명 규모 기업 기준 매일 250시간(연간 250만 달러 상당)이 단순 파일 찾기에 소모됨을 계량화",
                "표준화된 5계층 폴더 택소노미와 GAS 자동화 도입의 시급성"
            ],
            "tips": "제임스 조교가 구체적인 비용 계산(250만 달러)을 통해 경영진 관점에서의 심각성을 부각합니다."
        },
        "keyTerms": [
            {
                "term": "Search Friction Cost",
                "def": "The quantifiable financial and operational loss caused by employees spending billable time searching for internal records.",
                "defKo": "검색 마찰 비용 (문서 탐색 손실)"
            },
            {
                "term": "Standardized Taxonomy",
                "def": "A uniform directory naming and folder classification structure enforced across an entire enterprise.",
                "defKo": "표준화된 폴더 분류 체계"
            }
        ]
    },
    # Slide 10: Session 5 Agenda & Roadmap
    {
        "num": 10,
        "type": "content",
        "title": "SESSION 5 AGENDA & ROADMAP",
        "subtitle": "Four operational modules designed to transform cloud storage into an automated knowledge fortress",
        "points": [
            "Part 1: The Enterprise Drive Revolution & Knowledge Vault (Slides 02–11).",
            "Part 2: Deconstructing the System Vault: File Streaming & Taxonomy (Slides 12–22).",
            "Part 3: Strategic Imperatives, Access Control & Risk Governance (Slides 23–29).",
            "Part 4: Wisdom Synthesis, Apps Script Automation & Hands-on Lab (Slides 30–45)."
        ],
        "script": (
            "[Prof. Peter] Slide 10 presents our \"SESSION 5 AGENDA & ROADMAP.\" Here is our master battle plan for today.\n\n"
            "[TA Sarah] In Part 1, we establish the institutional knowledge vault. In Part 2, we deconstruct file streaming, 0MB virtual caching, folder color coding, and Drive AI OCR.\n\n"
            "[TA James] In Part 3, we master the Least Privilege Principle, RBAC roles, data exfiltration defenses, and version history auditing. And in Part 4, we write Google Apps Script automation pipelines and deploy your own live vault in Lab 5!\n\n"
            "[Prof. Peter] Let us examine our first real-world enterprise case study on Slide 11!"
        ),
        "koreanGuide": {
            "summary": "Session 5 아젠다 및 로드맵: 4대 핵심 모듈 안내",
            "points": [
                "Part 1: 엔터프라이즈 드라이브 혁명 및 지식 금고 철학",
                "Part 2: 파일 스트리밍(0MB 가상 드라이브), 폴더 색상 체계, AI OCR 검색",
                "Part 3: 최소 권한 원칙(Least Privilege), RBAC 5단계 역할, 데이터 유출 방지",
                "Part 4: Google Apps Script(GAS) 자동화, 지혜의 라이프 OS, 실습 과제"
            ],
            "tips": "사라 조교와 제임스 조교가 4개 파트의 핵심 포인트를 군더더기 없이 명쾌하게 요약합니다."
        },
        "keyTerms": [
            {
                "term": "Curriculum Roadmap",
                "def": "A structured pedagogical trajectory guiding students systematically from architectural theory to live deployment.",
                "defKo": "커리큘럼 로드맵"
            },
            {
                "term": "Operational Mastery",
                "def": "The demonstrated ability to configure, automate, and govern enterprise cloud infrastructure independently.",
                "defKo": "실무 운영 숙달도"
            }
        ]
    },
    # Slide 11: Case Study 1: Lost Aviation Maintenance Manual Recovery
    {
        "num": 11,
        "type": "casestudy",
        "title": "CASE STUDY 1: LOST AVIATION MANUAL RECOVERY",
        "subtitle": "Global Airline recovers grounded Boeing 777 in 4 minutes using Drive AI OCR & Shared Vaults",
        "company": "International Commercial Airline Fleet",
        "problem": "A Boeing 777 was grounded in Tokyo with an obscure hydraulic valve failure; engineers faced $40,000/hour grounding penalties while searching through 15,000 scanned paper maintenance manuals.",
        "solution": "Connected maintenance fleet to an Enterprise Shared Drive Knowledge Vault powered by Google Drive AI OCR and smart boolean search operators.",
        "impact": "Located the obscure 1998 Japanese valve repair bulletin in 3.8 minutes; aircraft cleared for takeoff in 45 minutes; saved $180,000 in airport delay penalties.",
        "script": (
            "[Prof. Peter] Slide 11 presents \"CASE STUDY 1: LOST AVIATION MANUAL RECOVERY.\" Look at this dramatic real-world mission.\n\n"
            "[TA Sarah] A commercial Boeing 777 was grounded on the tarmac at Tokyo Haneda airport with a rare hydraulic valve malfunction. The airline was losing 40,000 dollars every hour the plane sat on the runway, and passengers were stranded!\n\n"
            "[TA James] The junior mechanics couldn't find the repair guide because it was a 30-year-old scanned PDF buried in an archive of 15,000 maintenance manuals. Searching by filename returned zero results!\n\n"
            "[Prof. Peter] The chief engineer opened the airline's Enterprise Shared Drive, which had Google Drive AI OCR enabled, and typed the search operator: `type:pdf \"hydraulic bypass valve\" site:maintenance`.\n\n"
            "[TA Sarah] In exactly 3.8 minutes, Drive OCR detected the scanned text inside an unindexed 1998 repair bulletin! The mechanics fixed the valve, and the aircraft took off safely in 45 minutes, saving 180,000 dollars in grounding fines!\n\n"
            "[TA James] Now let us open Part 2 and look inside the mechanical engine of file streaming and taxonomy on Slide 12!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 1: 항공사 보잉 777 유압 밸브 매뉴얼 4분 만의 회수와 18만 달러 절감",
            "points": [
                "문제 상황: 도쿄 하네다 공항에 착륙한 보잉 777 항공기가 유압 밸브 고장으로 발이 묶여 시간당 4만 달러 지연 벌금 발생",
                "솔루션: 15,000권의 스캔 문서 속에서 구글 드라이브 AI OCR 및 스마트 검색 연산자를 활용한 초고속 탐색",
                "성과: 3.8분 만에 1998년 스캔된 수리 회람 발견, 45분 내 이륙 완료 및 18만 달러 손실 방어"
            ],
            "tips": "사라 조교와 제임스 조교가 긴박했던 항공기 지연 상황과 AI OCR의 탐색 위력을 생동감 있게 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Drive AI OCR",
                "def": "Google's optical character recognition engine automatically extracting and indexing text inside scanned images and PDFs.",
                "defKo": "구글 드라이브 AI OCR (스캔 텍스트 자동 인덱싱)"
            },
            {
                "term": "Grounding Penalty",
                "def": "The severe financial penalties and airport fees incurred by airlines when commercial aircraft are delayed on runways.",
                "defKo": "항공기 지연 과징금"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 12: Part 2 Section Divider
    {
        "num": 12,
        "type": "section",
        "title": "PART 2: DECONSTRUCTING THE SYSTEM VAULT",
        "subtitle": "File streaming vs. mirroring, 5-tier taxonomy, color-coding standards, and AI OCR indexing",
        "script": (
            "[TA Sarah] Look at Slide 12: \"PART 2: DECONSTRUCTING THE SYSTEM VAULT.\" Now we examine the precise mechanics of cloud storage engineering!\n\n"
            "[Prof. Peter] In Part 2, we teach you how to build a drive architecture that operates with surgical precision. How do you access 50 terabytes of enterprise files without filling up your laptop's 512GB SSD?\n\n"
            "[TA James] We will deconstruct Google Drive's Virtual File Streaming architecture (0MB local footprint), contrast it with Mirroring, establish an unbreakable 5-tier folder taxonomy, and master smart search operators.\n\n"
            "[TA Sarah] Let us inspect File Streaming versus File Mirroring on Slide 13!"
        ),
        "koreanGuide": {
            "summary": "Part 2 섹션 전환: 시스템 금고의 기술적 해부 및 파일 스트리밍 원리",
            "points": [
                "파일 스트리밍(File Streaming) vs 미러링(Mirroring)의 구조적 차이 완전 분석",
                "512GB 랩톱 SSD 용량으로 50TB 기업 데이터를 자유자재로 다루는 가상 파일 시스템 기법",
                "5계층 폴더 택소노미와 색상 코딩 표준화"
            ],
            "tips": "제임스 조교가 로컬 디스크 용량 한계를 극복하는 가상 파일 스트리밍의 편리함을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Virtual File Streaming",
                "def": "A cloud file system mechanism streaming files on-demand without consuming local hard drive storage.",
                "defKo": "가상 파일 스트리밍 (0MB 온디맨드 로딩)"
            },
            {
                "term": "Taxonomic Classification",
                "def": "The deliberate structuring of files into standardized, non-overlapping hierarchical directories.",
                "defKo": "분류학적 계층 체계"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 13: File Streaming: Virtual 0MB Efficiency
    {
        "num": 13,
        "type": "content",
        "title": "FILE STREAMING: VIRTUAL 0MB EFFICIENCY",
        "subtitle": "Accessing petabytes of enterprise assets on-demand through virtual cloud endpoints",
        "points": [
            "Zero Local Footprint: Files appear natively in Windows File Explorer or Mac Finder taking 0 bytes of disk space.",
            "On-Demand Block Streaming: Only the requested bytes are streamed into local RAM when a file is opened.",
            "Instant Sync: Edits are uploaded directly to the cloud without creating orphaned local duplicates."
        ],
        "script": (
            "[TA James] Slide 13 diagrams \"FILE STREAMING: VIRTUAL 0MB EFFICIENCY.\" This is one of Google Drive's greatest engineering features.\n\n"
            "[TA Sarah] When you install Google Drive for Desktop in 'Stream Files' mode, your Shared Drives mount as a virtual drive letter—like `G:\\Shared Drives`. You can browse 500,000 files, and they consume exactly ZERO megabytes on your local hard drive!\n\n"
            "[Prof. Peter] When you double-click a 2GB video file or a 500-page PDF, Google's virtual file driver streams only the requested byte blocks into RAM over TLS 1.3. When you save and close, the file releases local memory.\n\n"
            "[TA James] This completely eliminates hard drive full errors and stops employees from keeping chaotic local copies!\n\n"
            "[TA Sarah] Let us contrast this with File Mirroring on Slide 14."
        ),
        "koreanGuide": {
            "summary": "파일 스트리밍: 0MB 가상 드라이브를 통한 페타바이트급 데이터 액세스",
            "points": [
                "로컬 디스크 점유 0바이트: 윈도우 탐색기/맥 파인더에 가상 드라이브(G:)로 마운트되어 즉시 탐색",
                "온디맨드 블록 스트리밍: 파일을 더블클릭할 때만 필요한 데이터 블록을 RAM으로 초고속 스트리밍",
                "로컬 고아 파일(Orphaned Duplicates) 생성 방지 및 실시간 클라우드 동기화"
            ],
            "tips": "사라 조교가 500,000개 파일이 로컬 디스크 0MB를 차지한다는 점을 명확히 각인시킵니다."
        },
        "keyTerms": [
            {
                "term": "Virtual File Driver",
                "def": "An OS kernel extension that presents remote cloud files as if they were stored locally on the physical disk.",
                "defKo": "가상 파일 시스템 드라이버"
            },
            {
                "term": "On-Demand Caching",
                "def": "The transient loading of remote file blocks into local memory strictly during active read/write operations.",
                "defKo": "온디맨드 임시 캐싱"
            }
        ]
    },
    # Slide 14: File Mirroring: Offline Redundancy
    {
        "num": 14,
        "type": "content",
        "title": "FILE MIRRORING: OFFLINE REDUNDANCY",
        "subtitle": "Strategic offline access for mission-critical travel, fieldwork, and disaster recovery",
        "points": [
            "Full Local Copy: All files are duplicated physically on the local SSD for guaranteed offline availability.",
            "Storage Trade-off: Consumes physical SSD space proportional to the total folder size.",
            "Best Practice: Use Streaming for 95% of enterprise data, and Mirroring strictly for essential flight/field folders."
        ],
        "script": (
            "[TA Sarah] Slide 14 contrasts \"FILE MIRRORING: OFFLINE REDUNDANCY.\" If Streaming is so efficient, why does Mirroring exist?\n\n"
            "[Prof. Peter] Because of physical reality! If you are flying across the Pacific Ocean at 35,000 feet with no Wi-Fi, or working at an isolated archaeological field site, streaming endpoints cannot reach the cloud.\n\n"
            "[TA James] Exactly! In 'Mirror Files' mode, Google Drive maintains an identical physical copy on your SSD. If you edit a slide deck on the airplane, it syncs seamlessly the second you reconnect to the hotel Wi-Fi upon landing.\n\n"
            "[TA Sarah] The master architectural rule: use Virtual Streaming for 95% of your enterprise knowledge vault, and right-click 'Available Offline' (Mirroring) only for the active project you need on your flight!\n\n"
            "[TA James] Let us inspect folder color coding and visual taxonomy on Slide 15!"
        ),
        "koreanGuide": {
            "summary": "파일 미러링: 오프라인 출장과 비상 복구를 위한 물리적 로컬 복제",
            "points": [
                "물리적 SSD 복제: 인터넷이 연결되지 않는 비행기나 격오지 현장에서도 완벽한 작업 보장",
                "지능적 혼합 운용: 전사 데이터의 95%는 가상 스트리밍, 당장 필요한 5% 활성 프로젝트만 '오프라인 사용 가능' 설정",
                "재연결 시 자동 병합: 와이파이 연결 즉시 오프라인 수정 사항을 충돌 없이 클라우드에 반영"
            ],
            "tips": "피터 교수와 제임스가 스트리밍과 미러링의 최적 배분 비율(95:5)을 가이드라인으로 제시합니다."
        },
        "keyTerms": [
            {
                "term": "File Mirroring",
                "def": "Maintaining an identical physical replica of cloud directories on local storage for offline access.",
                "defKo": "파일 미러링 (오프라인 물리 복제)"
            },
            {
                "term": "Offline Availability Pinning",
                "def": "Explicitly marking specific cloud files or folders to remain permanently synchronized on local disk.",
                "defKo": "오프라인 고정 보관 (Pinning)"
            }
        ]
    },
    # Slide 15: Folder Color Coding & Taxonomy
    {
        "num": 15,
        "type": "content",
        "title": "FOLDER COLOR CODING & TAXONOMY",
        "subtitle": "Architecting visual hierarchy: Red (Urgent), Green (Active), Blue (Core Archive), Gray (Trash)",
        "points": [
            "Visual Hierarchy: The human brain processes colors in 13 milliseconds—faster than reading text.",
            "Standardized Palette: Red = Critical Executive, Green = Active Q4 Sprints, Blue = Institutional Vault, Slate = Archives.",
            "Zero Guesswork: Teams instantly recognize folder status and sensitivity without opening subdirectories."
        ],
        "script": (
            "[Prof. Peter] Slide 15 introduces \"FOLDER COLOR CODING & TAXONOMY.\" Cognitive ergonomics is a vital part of system design.\n\n"
            "[TA Sarah] Neuroscience proves that the human visual cortex recognizes color distinctions in under 13 milliseconds—far faster than reading alphanumeric text! When all folders are default gray, your brain experiences cognitive friction scanning every line.\n\n"
            "[TA James] In our lab standard: Red folders indicate Critical Executive approvals. Green folders indicate Active Q4 Sprints. Blue folders indicate Core Institutional Archives. And Slate Gray indicates Read-Only Historical records!\n\n"
            "[TA Sarah] When a new researcher joins the lab, they instantly navigate the hierarchy without reading a manual.\n\n"
            "[Prof. Peter] Let us examine chronological naming conventions on Slide 16."
        ),
        "koreanGuide": {
            "summary": "폴더 색상 코딩 및 시각적 택소노미: 13ms 인지 공학의 적용",
            "points": [
                "13ms 시각 인지: 텍스트를 읽기 전에 뇌가 색상을 먼저 인식하여 폴더 탐색 속도 극대화",
                "표준 색상 팔레트: 빨강(경영진 긴급), 초록(진행 중인 활성 프로젝트), 파랑(핵심 지식 금고), 회색(과거 아카이브)",
                "인지적 마찰 제거: 폴더를 열어보지 않고도 프로젝트의 긴급도와 상태를 직관적으로 파악"
            ],
            "tips": "사라 조교가 뇌과학적 근거(13ms)를 설명하고 제임스가 색상별 표준 정의를 명쾌하게 정리합니다."
        },
        "keyTerms": [
            {
                "term": "Cognitive Ergonomics",
                "def": "Designing digital user interfaces and file systems to minimize mental effort and visual search strain.",
                "defKo": "인지 인체공학 (시각 피로 최소화 설계)"
            },
            {
                "term": "Visual Taxonomy",
                "def": "The use of standardized color palettes and iconography to convey status and directory hierarchy instantly.",
                "defKo": "시각적 분류 체계 (색상 표준화)"
            }
        ]
    },
    # Slide 16: The Art of Chronological Naming
    {
        "num": 16,
        "type": "content",
        "title": "THE ART OF CHRONOLOGICAL NAMING",
        "subtitle": "ISO 8601 Standards: `YYYYMMDD_Project_Type_vXX` eliminates alphabetical chaos",
        "points": [
            "ISO 8601 Sorting: `20261024_Oikos_Syllabus_v03.pdf` automatically sorts in perfect chronological order.",
            "No Spaces or Special Characters: Prevents script encoding bugs and terminal escaping errors in bash/python.",
            "Semantic Tokens: Includes Date, Project Name, Document Type, and Semantic Versioning."
        ],
        "script": (
            "[TA James] Slide 16 presents \"THE ART OF CHRONOLOGICAL NAMING: ISO 8601 STANDARDS.\" This is my personal favorite engineering rule!\n\n"
            "[TA Sarah] How many times have you seen files named `Final_Report.docx`, `Final_Report_v2_really_final.docx`, and `Final_Report_v2_PETER_FINAL.docx`? It is complete chaos!\n\n"
            "[TA James] In our engineering standard, every file follows the ISO formula: `YYYYMMDD_Project_Type_vXX`—for example, `20260823_Oikos_Syllabus_v03.pdf`. In any operating system—Windows, Linux, Mac—the files sort in 100% perfect chronological sequence automatically!\n\n"
            "[Prof. Peter] Never use spaces or weird symbols like hashtags; use clean underscores. That ensures your automated Python and Apps Script daemons never crash on string parsing!\n\n"
            "[TA Sarah] Let us see how to accelerate workflow with `docs.new` shortcuts on Slide 17!"
        ),
        "koreanGuide": {
            "summary": "연대기적 파일 명명 규칙: ISO 8601 표준(YYYYMMDD_Project_Type_vXX)",
            "points": [
                "'최종_진짜최종_최종2.docx'와 같은 무질서한 파일명의 완전한 퇴출",
                "ISO 8601 표준 공식: YYYYMMDD 날짜를 접두사로 사용하여 윈도우/맥/리눅스 어디서나 자동 시간순 정렬",
                "공백(Space) 및 특수문자 금지: 파이썬 및 Apps Script 자동화 파싱 에러를 원천 차단하는 언더스코어(_) 사용"
            ],
            "tips": "제임스 조교의 유머러스한 '진짜최종' 예시로 수강생들의 폭풍 공감을 이끌어내세요."
        },
        "keyTerms": [
            {
                "term": "ISO 8601 Naming Standard",
                "def": "An international standard formatting dates as YYYYMMDD to guarantee universal chronological string sorting.",
                "defKo": "ISO 8601 표준 명명법"
            },
            {
                "term": "Semantic Versioning (SemVer)",
                "def": "A formal versioning convention (e.g., v01, v02) reflecting document revisions and evolutionary milestones.",
                "defKo": "시맨틱 버전 관리"
            }
        ]
    },
    # Slide 17: Web-Native Velocity: docs.new Shortcuts
    {
        "num": 17,
        "type": "content",
        "title": "WEB-NATIVE VELOCITY: DOCS.NEW SHORTCUTS",
        "subtitle": "Bypassing manual browser navigation: `docs.new`, `sheets.new`, `slides.new`",
        "points": [
            "Zero Navigation Friction: Typing `docs.new` in the Chrome address bar creates an instant live document in 300ms.",
            "Domain Scoping: `docs.new/u/1` launches the document directly inside your corporate enterprise profile.",
            "Cognitive Momentum: Eliminates 5 manual clicks through Google Drive folders, preserving intellectual flow."
        ],
        "script": (
            "[Prof. Peter] Slide 17 highlights \"WEB-NATIVE VELOCITY: DOCS.NEW SHORTCUTS.\" Speed in the small things creates massive cumulative momentum.\n\n"
            "[TA Sarah] When you have an urgent idea, opening Google Drive, clicking 'New', selecting 'Google Docs', and waiting for the redirect takes 15 seconds and breaks your mental concentration.\n\n"
            "[TA James] Instead, simply type `docs.new`, `sheets.new`, or `slides.new` directly into your Chrome address bar! In under 300 milliseconds, you are typing on a clean canvas!\n\n"
            "[Prof. Peter] And if you manage multiple Google accounts, `docs.new/u/1` automatically scopes the file to your enterprise domain account. Small architectural habits protect deep focus.\n\n"
            "[TA Sarah] Let us master smart search operators on Slide 18!"
        ),
        "koreanGuide": {
            "summary": "웹 네이티브 속도: docs.new 단축키를 통한 즉각적 집중력 유지",
            "points": [
                "브라우저 주소창에 docs.new, sheets.new, slides.new 입력 시 300ms 만에 새 문서 즉시 생성",
                "다중 계정 지원: docs.new/u/1을 통해 기업용 도메인 계정으로 즉시 스코프 지정 생성",
                "인지적 모멘텀: 마우스 클릭 5단계를 생략하여 아이디어가 떠오른 순간의 몰입 상태(Flow) 보존"
            ],
            "tips": "사라 조교가 단축키 팁을 시연하듯 설명하여 즉각적인 실무 활용을 돕습니다."
        },
        "keyTerms": [
            {
                "term": "Web-Native Shortcut",
                "def": "Top-level domain redirects (such as .new) engineered to instantiate cloud applications instantaneously.",
                "defKo": ".new 웹 네이티브 단축 명령어"
            },
            {
                "term": "Cognitive Momentum",
                "def": "The sustained mental flow state maintained by eliminating micro-frictions in daily software tools.",
                "defKo": "인지적 추진력 (몰입 연속성)"
            }
        ]
    },
    # Slide 18: Beyond File Names: Smart Search Operators
    {
        "num": 18,
        "type": "content",
        "title": "BEYOND FILE NAMES: SMART SEARCH OPERATORS",
        "subtitle": "Mastering boolean filters: `type:`, `owner:`, `before:`, `has:user-email`, `parent:`",
        "points": [
            "Precision Querying: `type:spreadsheet owner:me modified:today \"Q4 Revenue\"` pinpoints exact files in 1 second.",
            "Parent Directory Scoping: `parent:Shared_Vault_ID` restricts search strictly to a specific project folder.",
            "Auditing Stale Assets: `type:pdf before:2024-01-01` finds outdated documents for compliance archiving."
        ],
        "script": (
            "[TA Sarah] Slide 18 explores \"BEYOND FILE NAMES: SMART SEARCH OPERATORS.\" Searching in Google Drive is not just typing random words into a search box!\n\n"
            "[TA James] Look at the boolean power on screen: `type:spreadsheet owner:me modified:today \"Q4 Revenue\"`. Instead of scrolling through 200 files, Drive filters the universe down to the EXACT spreadsheet in 0.5 seconds!\n\n"
            "[Prof. Peter] You can also search by parent folder ID or find all legacy contracts created before 2024 with `before:2024-01-01`. When you master search operators, you never lose a document again.\n\n"
            "[TA Sarah] Let us see how AI OCR unlocks dark scanned archives on Slide 19!"
        ),
        "koreanGuide": {
            "summary": "파일명 검색을 넘어서: 구글 드라이브 스마트 불리언 검색 연산자 마스터",
            "points": [
                "정밀 필터링: type:spreadsheet, owner:me, modified:today 등 복합 연산자로 0.5초 내 타겟팅",
                "부모 폴더 한정 검색: parent:폴더ID 지정을 통해 불필요한 전사 검색 노이즈 완벽 배제",
                "레거시 문서 감사: before:2024-01-01로 보관 기한이 지난 문서를 일괄 식별하여 아카이빙"
            ],
            "tips": "제임스 조교가 검색창에 연산자를 타이핑하는 시나리오를 구체적으로 보여주세요."
        },
        "keyTerms": [
            {
                "term": "Boolean Search Operators",
                "def": "Logical filter commands (type:, owner:, modified:) enabling programmatic precision search across cloud drives.",
                "defKo": "불리언 스마트 검색 연산자"
            },
            {
                "term": "Parent Scoping",
                "def": "Restricting query execution strictly to descendants of a designated folder identifier.",
                "defKo": "부모 폴더 범위 한정 검색"
            }
        ]
    },
    # Slide 19: AI OCR Integration: Dark Images to Live Assets
    {
        "num": 19,
        "type": "content",
        "title": "AI OCR INTEGRATION: DARK IMAGES TO ASSETS",
        "subtitle": "Automated text extraction from receipts, whiteboards, scanned PDFs, and engineering blueprints",
        "points": [
            "Dark Data Awakening: Over 55% of enterprise data is trapped in unindexed images and scanned PDFs.",
            "Native Neural OCR: Google Drive runs automatic background OCR on every uploaded image and PDF.",
            "Full-Text Ingestion: Scanned handwritten notes and whiteboards become searchable by keyword instantly."
        ],
        "script": (
            "[Prof. Peter] Slide 19 covers \"AI OCR INTEGRATION: DARK IMAGES TO LIVE ASSETS.\" What is 'Dark Data'?\n\n"
            "[TA Sarah] Dark data refers to photos of whiteboards, scanned receipts, and paper contracts sitting in cloud folders like dead weight—completely invisible to search algorithms!\n\n"
            "[TA James] Google Drive's neural OCR engine automatically scans every uploaded JPEG, PNG, and PDF in the background. Even if an engineer took a blurry smartphone photo of a whiteboard schematic 3 years ago, typing a word from that whiteboard into the Drive search bar finds the image instantly!\n\n"
            "[Prof. Peter] That transforms dead image archives into active, searchable institutional knowledge.\n\n"
            "[TA Sarah] Let us review storage FinOps and local cache management on Slide 20."
        ),
        "koreanGuide": {
            "summary": "AI OCR 통합: 다크 데이터(스캔 이미지, 화이트보드 사진)의 실시간 자산화",
            "points": [
                "다크 데이터(Dark Data): 전체 기업 데이터의 55%가 검색되지 않는 스캔 PDF 및 이미지 형태로 방치",
                "뉴럴 OCR 백그라운드 구동: 구글 드라이브가 업로드된 모든 이미지와 문서를 자동 텍스트 인덱싱",
                "화이트보드 손글씨 검색: 3년 전 스마트폰으로 찍은 화이트보드 회의 사진 속 단어도 즉시 검색 가능"
            ],
            "tips": "사라 조교와 피터 교수가 방치된 사진 데이터가 어떻게 살아있는 지식 자산으로 부활하는지 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Dark Data",
                "def": "Information assets organizations collect and store but fail to utilize for analytics due to lack of indexing.",
                "defKo": "다크 데이터 (비정형 미인덱싱 자산)"
            },
            {
                "term": "Neural OCR Pipeline",
                "def": "Deep learning models extracting printed and handwritten characters from unstructured graphic files.",
                "defKo": "뉴럴 광학 문자 인식(OCR) 파이프라인"
            }
        ]
    },
    # Slide 20: Storage FinOps: Quotas & Trash Purges
    {
        "num": 20,
        "type": "content",
        "title": "STORAGE FINOPS: QUOTAS & TRASH PURGES",
        "subtitle": "Managing enterprise cloud storage costs, automated 30-day trash cycles, and shared drive pooling",
        "points": [
            "Shared Drive Pooling: Pooled storage prevents individual user quota exhaustion and reduces tier costs.",
            "Automated Trash Purging: Items in Google Drive trash are purged automatically after 30 days.",
            "Storage FinOps Policy: Automated Apps Script scans for orphaned 10GB+ temporary files and archives them."
        ],
        "script": (
            "[TA Sarah] Slide 20 explores \"STORAGE FINOPS: QUOTAS & TRASH PURGES.\" Cloud storage is not free, especially at enterprise scale!\n\n"
            "[TA James] In enterprise Google Workspace, Shared Drives pool storage across the entire domain. But if engineers dump 50GB raw video files or database backups into active folders, your monthly cloud bill can skyrocket.\n\n"
            "[Prof. Peter] We deploy Storage FinOps scripts using Google Apps Script: every Sunday at midnight, a lightweight cron script identifies orphaned files over 5GB that haven't been accessed in 180 days, compresses them, and moves them to Google Cloud Coldline Storage at 90% lower cost!\n\n"
            "[TA Sarah] Let us inspect operational prerequisites on Slide 21."
        ),
        "koreanGuide": {
            "summary": "스토리지 FinOps: 용량 할당, 30일 휴지통 자동 비우기 및 비용 최적화",
            "points": [
                "공유 드라이브 스토리지 풀링: 개인 계정별 용량 부족을 방지하고 조직 단위 통합 비용 관리",
                "30일 자동 휴지통 비우기: 구글 드라이브 휴지통 항목은 30일 후 자동 영구 삭제되는 정책 이해",
                "Apps Script 기반 FinOps: 180일간 미사용된 5GB 이상 대용량 파일을 콜드라인 스토리지로 자동 이관해 90% 절감"
            ],
            "tips": "제임스 조교가 일요일 자정에 돌아가는 자동 FinOps 스크립트의 비용 절감 효과를 수치로 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Storage FinOps",
                "def": "The financial management practice optimizing cloud storage allocation, tiering, and retention costs.",
                "defKo": "스토리지 FinOps (클라우드 용량 비용 최적화)"
            },
            {
                "term": "Coldline Tiering",
                "def": "Migrating infrequently accessed historical data to low-cost archival storage classes.",
                "defKo": "콜드라인 계층화 아카이빙"
            }
        ]
    },
    # Slide 21: Operational Prerequisites Checklist
    {
        "num": 21,
        "type": "content",
        "title": "OPERATIONAL PREREQUISITES CHECKLIST",
        "subtitle": "Pre-flight requirements: Drive for Desktop, Enterprise Domain, OAuth 2.0 Scopes",
        "points": [
            "Prerequisite 1: Google Workspace Business Standard or Enterprise domain account.",
            "Prerequisite 2: Google Drive for Desktop installed in 'Stream Files' mode with virtual G: drive mounted.",
            "Prerequisite 3: Google Apps Script API enabled in Google Cloud Console with DriveApp scopes."
        ],
        "script": (
            "[TA James] Slide 21 outlines the \"OPERATIONAL PREREQUISITES CHECKLIST\" before we begin building automated scripts.\n\n"
            "[TA Sarah] Check off all 3 requirements: First, a Google Workspace domain account with Shared Drive permissions. Second, Google Drive for Desktop installed and configured for Virtual File Streaming. Third, Google Apps Script API toggled 'ON' in your Google Cloud Console!\n\n"
            "[Prof. Peter] When these foundations are solid, your automated bots and scripts execute with zero permission errors.\n\n"
            "[TA Sarah] Let us inspect our second enterprise case study on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "운영 사전 필수 요건 체크리스트: 드라이브 데스크톱, 기업 도메인, OAuth 스코프",
            "points": [
                "요건 1: 공유 드라이브 생성이 가능한 구글 워크스페이스 비즈니스/엔터프라이즈 도메인 계정",
                "요건 2: '파일 스트리밍' 모드로 설치되어 G: 가상 드라이브로 마운트된 구글 드라이브 데스크톱",
                "요건 3: 구글 클라우드 콘솔에서 DriveApp 권한이 활성화된 Google Apps Script API"
            ],
            "tips": "제임스 조교가 실습 전 3대 필수 요건을 점검하도록 명확하게 체크해 줍니다."
        },
        "keyTerms": [
            {
                "term": "DriveApp Scopes",
                "def": "The OAuth 2.0 authorization permissions required by Apps Script to programmatically access Google Drive files.",
                "defKo": "DriveApp OAuth 2.0 권한 스코프"
            },
            {
                "term": "Operational Readiness",
                "def": "The verified configuration state ensuring all software prerequisites are fulfilled prior to production execution.",
                "defKo": "운영 준비 상태 (사전 검증 완료)"
            }
        ]
    },
    # Slide 22: Case Study 2: 50TB Media Studio 0MB File Streaming
    {
        "num": 22,
        "type": "casestudy",
        "title": "CASE STUDY 2: 50TB MEDIA STUDIO 0MB STREAMING",
        "subtitle": "Hollywood Visual Effects studio deploys 50TB Shared Vault across 200 remote editors on 512GB laptops",
        "company": "Hollywood VFX & 4K Post-Production Studio",
        "problem": "200 remote video editors worldwide had 512GB MacBooks but needed daily access to a 50TB 4K footage repository, causing hard drive crashes and fragmented hard-drive courier shipping.",
        "solution": "Deployed Google Drive Virtual File Streaming with standardized 5-tier taxonomic color coding and proxy video transcoding via Apps Script.",
        "impact": "200 editors accessed 50TB footage with 0MB physical hard drive consumption; courier shipping costs eliminated ($120K annual saving); project delivery accelerated by 3 weeks.",
        "script": (
            "[Prof. Peter] Slide 22 presents \"CASE STUDY 2: 50TB MEDIA STUDIO 0MB FILE STREAMING.\"\n\n"
            "[TA Sarah] A Hollywood VFX studio with 200 remote editors worldwide faced an impossible storage bottleneck: their raw 4K footage repository was 50 terabytes, but every editor had a standard MacBook with only 512GB of internal storage!\n\n"
            "[TA James] They used to physically ship encrypted 10TB hard drives via FedEx across the globe—costing 120,000 dollars a year in shipping fees and wasting weeks in shipping transit!\n\n"
            "[Prof. Peter] They deployed Google Drive Virtual File Streaming. All 50TB was mounted as a virtual drive. Editors opened high-res clips on-demand, while an Apps Script worker automatically generated lightweight proxy files in the background.\n\n"
            "[TA Sarah] Every single editor accessed the entire 50TB vault with zero disk full errors, eliminating shipping costs and completing the film 3 weeks ahead of schedule!\n\n"
            "[TA James] Now let us open Part 3 and inspect access control and risk governance on Slide 23!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 2: 헐리우드 VFX 스튜디오 50TB 영상의 0MB 가상 스트리밍 혁신",
            "points": [
                "문제 상황: 200명의 원격 영상 편집자가 512GB 랩톱으로 50TB의 4K 원본 영상에 접근해야 하는 용량 한계",
                "과거 비효율: 물리적 하드디스크를 국제 특송(FedEx)으로 배송하느라 연간 12만 달러와 수주의 시간 낭비",
                "성과: 가상 파일 스트리밍 도입으로 50TB를 0MB 로컬 점유로 원격 작업 완료, 배송비 12만 달러 전액 절감 및 3주 납기 단축"
            ],
            "tips": "사라 조교와 제임스 조교가 50TB 대용량 미디어 스트리밍의 실전 효과를 흥미진진하게 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Proxy Transcoding",
                "def": "The automated conversion of massive high-resolution video assets into lightweight proxy files for fast streaming.",
                "defKo": "프록시 트랜스코딩 (경량 영상 변환)"
            },
            {
                "term": "Courier Shipping Elimination",
                "def": "Replacing physical hardware transport with cloud-native virtual streaming architectures.",
                "defKo": "물리적 특송 배송 제거"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 23: Part 3 Section Divider
    {
        "num": 23,
        "type": "section",
        "title": "PART 3: STRATEGIC IMPERATIVES & RISK GOVERNANCE",
        "subtitle": "The Least Privilege Principle, RBAC roles, DRM exfiltration defense, and forensic version history",
        "script": (
            "[TA Sarah] Look at Slide 23: \"PART 3: STRATEGIC IMPERATIVES & RISK GOVERNANCE.\" Professor, when companies share files in the cloud, how do they stop sensitive data from walking out the front door?\n\n"
            "[Prof. Peter] By enforcing strict architectural boundaries! Trust is not a strategy; cryptography and role-based access control are! Under Soli Deo Gloria, we are faithful stewards of confidential records.\n\n"
            "[TA James] In Part 3, we master the Least Privilege Principle across Google Workspace's 5 Shared Drive roles, configure DRM anti-download locks, and audit forensic version histories.\n\n"
            "[TA Sarah] Let us inspect the Least Privilege Principle on Slide 24."
        ),
        "koreanGuide": {
            "summary": "Part 3 섹션 전환: 전략적 거버넌스 및 리스크 방어 요새 구축",
            "points": [
                "최소 권한의 원칙(Principle of Least Privilege)의 철학적 및 기술적 구현",
                "구글 워크스페이스 공유 드라이브의 5단계 권한 역할(RBAC) 완전 분해",
                "DRM 다운로드 차단, 외부 유출 방지 및 포렌식 버전 이력 감사"
            ],
            "tips": "사라 조교가 기업 보안 관리자의 고민을 묻고 제임스와 피터 교수가 엄격한 거버넌스 체계를 제시합니다."
        },
        "keyTerms": [
            {
                "term": "Least Privilege Principle",
                "def": "A foundational security standard granting users and programs only the minimum access levels required to perform tasks.",
                "defKo": "최소 권한의 원칙"
            },
            {
                "term": "DRM Exfiltration Defense",
                "def": "Digital rights management controls disabling copying, downloading, and printing of proprietary files.",
                "defKo": "DRM 데이터 유출 방지 통제"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 24: The Least Privilege Principle
    {
        "num": 24,
        "type": "content",
        "title": "THE LEAST PRIVILEGE PRINCIPLE",
        "subtitle": "Restricting access to the absolute minimum necessary to eliminate blast radius",
        "points": [
            "Blast Radius Containment: If a compromised user account has only 'Viewer' rights, attackers cannot delete or encrypt files.",
            "Default Deny: New team members start with zero access, receiving specific scoped permissions only upon request.",
            "Time-Bound Access: Granting temporary 24-hour access for external contractors with automated revocation."
        ],
        "script": (
            "[Prof. Peter] Slide 24 outlines \"THE LEAST PRIVILEGE PRINCIPLE.\" In cybersecurity, we always plan for the worst-case scenario.\n\n"
            "[TA James] Look at the concept of 'Blast Radius': if an employee clicks a phishing email and their account is hacked, but they only have 'Viewer' access to the Shared Drive, the hacker CANNOT delete, overwrite, or ransomware your files!\n\n"
            "[TA Sarah] But if that same employee was given 'Manager' rights lazily, the attacker can wipe out your entire company's database in 3 seconds!\n\n"
            "[Prof. Peter] Default Deny and granular scoping are non-negotiable. Let us inspect the exact breakdown of roles on Slide 25."
        ),
        "koreanGuide": {
            "summary": "최소 권한의 원칙: 피해 반경(Blast Radius) 격리와 기본 거부(Default Deny)",
            "points": [
                "피해 반경 억제: 계정이 피싱에 탈취당해도 '뷰어' 권한이면 해커가 문서를 삭제하거나 랜섬웨어로 암호화 불가",
                "관리자 권한 남발의 위험: 불필요한 '관리자' 권한 부여는 전사 데이터 삭제의 백도어가 됨",
                "기본 거부(Default Deny) 및 외부 협력업체 대상 24시간 시한부 임시 권한 부여"
            ],
            "tips": "제임스 조교가 해킹 시나리오와 권한 격리의 방어력을 대비해 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Blast Radius",
                "def": "The maximum scope of damage that can occur when a specific user account or component is compromised.",
                "defKo": "피해 반경 (보안 사고 확산 범위)"
            },
            {
                "term": "Default Deny",
                "def": "A security posture where all access is blocked by default until explicit authorization is granted.",
                "defKo": "기본 차단 원칙 (Default Deny)"
            }
        ]
    },
    # Slide 25: Deconstructing Roles: Viewer to Manager
    {
        "num": 25,
        "type": "comparison",
        "title": "DECONSTRUCTING ROLES: VIEWER TO MANAGER",
        "subtitle": "Mapping the 5 tiers: Viewer, Commenter, Contributor, Content Manager, Manager",
        "leftCard": {
            "tag": "READ-ONLY TIERS",
            "title": "Viewer & Commenter",
            "points": [
                "Viewer: Can view files; cannot edit, comment, or share.",
                "Commenter: Can view and add suggestion comments; cannot modify text.",
                "Use Case: External auditors, clients, junior interns."
            ]
        },
        "rightCard": {
            "tag": "WRITE & ADMIN TIERS",
            "title": "Contributor to Manager",
            "points": [
                "Contributor: Can add and edit files; cannot move or delete files.",
                "Content Manager: Can add, edit, move, and delete files.",
                "Manager: Can manage members, settings, and delete the drive.",
                "Use Case: Strict isolation for team leads and core developers."
            ]
        },
        "script": (
            "[TA Sarah] Slide 25 breaks down \"THE 5 TIERS OF SHARED DRIVE ROLES.\"\n\n"
            "[TA James] Examine the difference: A 'Contributor' can create and edit files, but they CANNOT delete or move files out of the drive! That prevents accidental folder deletion. Only 'Content Managers' can move and delete files.\n\n"
            "[Prof. Peter] And 'Manager' is reserved strictly for 2 or 3 domain administrators who manage memberships and permissions. 90% of your team members should be 'Contributors' or 'Commenters.'\n\n"
            "[TA Sarah] Let us inspect Data Exfiltration Defense and DRM controls on Slide 26!"
        ),
        "koreanGuide": {
            "summary": "공유 드라이브 5대 역할 분석: 뷰어부터 관리자까지의 완벽 매핑",
            "points": [
                "기여자(Contributor): 파일 작성 및 편집은 가능하나, 파일 이동 및 삭제 권한은 박탈되어 실수로 인한 유실 차단",
                "콘텐츠 관리자(Content Manager): 파일의 이동 및 삭제가 가능한 프로젝트 실무 책임자 권한",
                "관리자(Manager): 멤버 추가/삭제 및 드라이브 설정을 총괄하는 소수(2~3명)의 도메인 관리자 전용"
            ],
            "tips": "제임스 조교가 기여자(Contributor) 역할이 왜 파일 삭제 사고를 막아주는지 실무적 팁을 전합니다."
        },
        "keyTerms": [
            {
                "term": "Contributor Role",
                "def": "A safe authoring role allowing users to create and edit documents while blocking destructive delete/move permissions.",
                "defKo": "기여자 권한 (안전 편집자)"
            },
            {
                "term": "Content Manager Role",
                "def": "An operational management tier possessing full file lifecycle control (edit, move, delete) without member admin rights.",
                "defKo": "콘텐츠 관리자 권한"
            }
        ]
    },
    # Slide 26: Data Exfiltration Defense
    {
        "num": 26,
        "type": "content",
        "title": "DATA EXFILTRATION DEFENSE",
        "subtitle": "Locking down Shared Drives: Disabling downloads, prints, copies, and external sharing",
        "points": [
            "Information Rights Management (IRM): Uncheck 'Allow viewers to download, print, and copy'.",
            "External Sharing Lockdown: Restrict file sharing strictly to verified corporate domain users.",
            "Watermarking & DLP: Google Workspace Data Loss Prevention (DLP) flags unauthorized credit card/SSN sharing."
        ],
        "script": (
            "[Prof. Peter] Slide 26 outlines \"DATA EXFILTRATION DEFENSE: LOCKING DOWN THE VAULT.\"\n\n"
            "[TA Sarah] When you share a confidential strategy memo with an external client or contractor, what stops them from clicking 'Download as PDF' and forwarding it to a competitor?\n\n"
            "[TA James] In Shared Drive settings, you check one single checkbox: 'Prevent viewers and commenters from downloading, printing, and copying'! The download button disappears, right-click copy is disabled, and printing produces blank pages!\n\n"
            "[Prof. Peter] Combined with Google Workspace DLP (Data Loss Prevention) rules, your proprietary intelligence remains securely locked within your enterprise perimeter.\n\n"
            "[TA Sarah] Let us inspect forensic version history auditing on Slide 27."
        ),
        "koreanGuide": {
            "summary": "데이터 유출 방지(Exfiltration Defense) 및 정보 권한 관리(IRM)",
            "points": [
                "IRM 복제 차단: '뷰어 및 댓글 작성자의 다운로드, 인쇄, 복사 차단' 체크박스로 원클릭 보안 강화",
                "외부 공유 차단: 사외 이메일 계정으로의 무단 링크 공유 및 권한 부여 원천 통제",
                "구글 DLP(데이터 손실 방지): 카드번호, 주민번호 등 민감 데이터의 사외 유출 시도 실시간 탐지 및 차단"
            ],
            "tips": "사라 조교가 외주 협력사와 일할 때 다운로드 금지 체크박스가 발휘하는 위력을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Information Rights Management (IRM)",
                "def": "Security settings that prevent unauthorized downloading, copying, and printing of confidential digital files.",
                "defKo": "정보 권한 관리 (IRM 다운로드 방지)"
            },
            {
                "term": "Data Loss Prevention (DLP)",
                "def": "Automated security policies detecting and preventing unauthorized sharing of sensitive data outside the enterprise.",
                "defKo": "데이터 손실 방지 (DLP)"
            }
        ]
    },
    # Slide 27: Version History & Forensic Auditing
    {
        "num": 27,
        "type": "content",
        "title": "VERSION HISTORY & FORENSIC AUDITING",
        "subtitle": "Immutable revision trees: Who changed what, when, and one-click rollback to any historical point",
        "points": [
            "Granular Diff Auditing: Every keystroke in Google Docs is stamped with user identity, timestamp, and character diffs.",
            "Named Milestones: Tagging critical milestones (e.g., `20261024_Board_Approved`) for permanent baseline audits.",
            "Zero-Data-Loss Rollback: Instantly reverting malicious edits or corrupted tables in 1 click."
        ],
        "script": (
            "[TA James] Slide 27 explores \"VERSION HISTORY & FORENSIC AUDITING.\"\n\n"
            "[TA Sarah] Have you ever had a junior colleague accidentally select all text in a 100-page document, hit backspace, and close the tab?\n\n"
            "[TA James] In legacy Word files, that was a career-ending disaster. In Google Docs, every single edit is continuously recorded in a granular revision tree! You click 'Version History', see who deleted the text in red highlights, and click 'Restore this version' in 2 seconds!\n\n"
            "[Prof. Peter] You can also name major milestones—such as `20260823_Board_Approved_v01`—establishing clear legal and technical baselines.\n\n"
            "[TA Sarah] Let us inspect Workspace Add-ons and single sources of truth on Slide 28."
        ),
        "koreanGuide": {
            "summary": "버전 이력 및 포렌식 감사: 세밀한 수정 내역 추적과 1클릭 복구",
            "points": [
                "실시간 키스트로크 로깅: 누가, 언제, 어떤 글자를 지우고 수정했는지 색상별 정밀 감사 가능",
                "이름 붙은 버전(Named Milestones): 이사회 승인본, 배포본 등 중요 시점을 영구 깃발로 고정",
                "1클릭 무손실 롤백: 실수로 전체가 삭제되거나 서식이 망가져도 즉각 이전 시점으로 복원"
            ],
            "tips": "제임스 조교의 위트 있는 백스페이스 실수 예시와 즉각적인 복구 시연을 전개하세요."
        },
        "keyTerms": [
            {
                "term": "Granular Revision Tree",
                "def": "The continuous, immutable record of every user edit, addition, and deletion inside a collaborative document.",
                "defKo": "정밀 수정 이력 트리"
            },
            {
                "term": "Named Version Milestone",
                "def": "An explicitly named snapshot representing an official audit baseline within a document's lifecycle.",
                "defKo": "이름 지정 버전 마일스톤"
            }
        ]
    },
    # Slide 28: Single Source of Truth: Workspace Add-ons
    {
        "num": 28,
        "type": "content",
        "title": "SINGLE SOURCE OF TRUTH: WORKSPACE ADD-ONS",
        "subtitle": "Embedding live database records, CRM cards, and Gemini summaries inside Google Docs",
        "points": [
            "Smart Chips: Typing `@` inserts live interactive people cards, files, dates, and dropdown status chips.",
            "Live Database Sync: Embedding Google Sheets tables inside Docs that update automatically when source numbers change.",
            "Single Source of Truth: Eliminates copy-pasting outdated financial tables across 20 different slide decks."
        ],
        "script": (
            "[Prof. Peter] Slide 28 details \"SINGLE SOURCE OF TRUTH: WORKSPACE ADD-ONS & SMART CHIPS.\"\n\n"
            "[TA Sarah] Look at Google Workspace's Smart Chips: typing `@` allows you to embed interactive people cards, document references, and live project status chips directly inside your text.\n\n"
            "[TA James] Even more powerful is linked tables: when you link a Google Sheets financial table inside a Google Doc, updating Q3 revenue in the spreadsheet displays an 'Update' button in the Doc. One click synchronizes the numbers across 20 different executive memos!\n\n"
            "[Prof. Peter] That guarantees single-source truth across your entire organization.\n\n"
            "[TA Sarah] Let us inspect our third enterprise case study on Slide 29!"
        ),
        "koreanGuide": {
            "summary": "단일 진실 원천(Single Source of Truth)과 스마트 칩 연동",
            "points": [
                "스마트 칩(@): 문서 내에 담당자, 일정, 파일, 드롭다운 상태 칩을 실시간 대화형으로 삽입",
                "연동된 표(Linked Tables): 구글 시트의 재무 데이터 수정 시 문서 내 표가 '업데이트' 버튼 하나로 일괄 동기화",
                "수작업 복사-붙여넣기 제거: 20개 부서 보고서 간 수치 불일치와 오류를 근본적으로 차단"
            ],
            "tips": "사라 조교와 피터 교수가 스마트 칩과 연동 표가 만들어내는 단일 진실 원천의 가치를 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Smart Chips",
                "def": "Interactive metadata objects (@mentions, dates, files) embedded natively into Google Docs.",
                "defKo": "스마트 칩 (대화형 메타데이터 객체)"
            },
            {
                "term": "Linked Table Sync",
                "def": "A dynamic connection maintaining real-time data consistency between spreadsheets and executive documents.",
                "defKo": "연동 표 실시간 동기화"
            }
        ]
    },
    # Slide 29: Case Study 3: Preventing a $500K Exfiltration Breach
    {
        "num": 29,
        "type": "casestudy",
        "title": "CASE STUDY 3: PREVENTING A $500K DATA BREACH",
        "subtitle": "Automated Drive DLP & IRM rules block rogue contractor from downloading proprietary source code",
        "company": "Fintech Mobile Banking Enterprise",
        "problem": "A rogue external contractor attempted to bulk-download 400 confidential algorithm design specifications and API schemas on their final contract day.",
        "solution": "Enforced Shared Drive IRM 'No-Download' restrictions and Google Workspace DLP policy triggering an automated Apps Script security alert.",
        "impact": "Bulk download attempt instantly blocked; security team notified via Telegram in 1.2 seconds; contractor account auto-quarantined; zero IP loss ($500K damages prevented).",
        "script": (
            "[Prof. Peter] Slide 29 presents \"CASE STUDY 3: PREVENTING A $500K DATA EXFILTRATION BREACH.\"\n\n"
            "[TA Sarah] A fintech mobile banking enterprise employed an external contractor who had access to core algorithm specifications. On their final day before contract termination, the contractor attempted to bulk-download 400 confidential design documents to a personal USB drive!\n\n"
            "[TA James] Because the fintech had enforced our Shared Drive IRM policies, the download was blocked instantly. Furthermore, Google Workspace DLP detected the bulk-export trigger, and our automated Apps Script sent a high-priority security alert to the CISO's Telegram in 1.2 seconds!\n\n"
            "[Prof. Peter] The contractor's session was automatically quarantined, and zero proprietary IP was leaked, preventing an estimated 500,000 dollars in trade secret damages!\n\n"
            "[TA Sarah] Now let us open Part 4 and learn to write automated Google Apps Script pipelines on Slide 30!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 3: 50만 달러 규모 지적재산 유출 시도를 원천 차단한 드라이브 보안",
            "points": [
                "문제 상황: 계약 종료 당일 외주 개발자가 400건의 핵심 알고리즘 및 API 설계 문서를 개인 USB로 대량 다운로드 시도",
                "솔루션: 공유 드라이브 IRM 다운로드 금지 설정 및 구글 DLP 감지 시 Apps Script 텔레그램 경보 자동 발송",
                "성과: 다운로드 즉시 차단, 1.2초 만에 보안팀 경보 및 계정 자동 격리, 50만 달러 상당의 영업비밀 유출 방어"
            ],
            "tips": "제임스 조교가 실시간 경보와 계정 자동 격리 파이프라인의 실무적 통쾌함을 생생히 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Data Exfiltration",
                "def": "The unauthorized copy, transfer, or retrieval of confidential data from an enterprise computer or server.",
                "defKo": "데이터 무단 유출 (Exfiltration)"
            },
            {
                "term": "Automated Security Quarantine",
                "def": "The immediate programmatic revocation of credentials and active sessions upon detecting anomalous activity.",
                "defKo": "자동 보안 격리 조치"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 30: Part 4 Section Divider
    {
        "num": 30,
        "type": "section",
        "title": "PART 4: WISDOM SYNTHESIS & APPS SCRIPT AUTOMATION",
        "subtitle": "Google Apps Script pipelines, time-driven event triggers, and dedicating work to Soli Deo Gloria",
        "script": (
            "[TA Sarah] Look at Slide 30: \"PART 4: WISDOM SYNTHESIS & APPS SCRIPT AUTOMATION.\" Now we write the code that transforms static drives into living automation engines!\n\n"
            "[Prof. Peter] In Part 4, we bring everything together: Google Apps Script (GAS), time-driven triggers, collaborative suggestion workflows, and the spiritual wisdom of redeeming time under Soli Deo Gloria.\n\n"
            "[TA James] We will inspect real JavaScript code that monitors folders, auto-generates documents, and triages incoming emails around the clock.\n\n"
            "[TA Sarah] Let us inspect Google Apps Script: The Invisible Laborer on Slide 31."
        ),
        "koreanGuide": {
            "summary": "Part 4 섹션 전환: 지혜의 통합 및 Google Apps Script(GAS) 자동화 구현",
            "points": [
                "정적 저장소를 살아있는 자동화 엔진으로 전환하는 구글 앱스 스크립트(GAS) 코딩",
                "시간 기반(Time-Driven) 트리거 및 폴더 감지 이벤트 파이프라인 수립",
                "Soli Deo Gloria의 청지기 정신과 협업 속도 극대화"
            ],
            "tips": "피터 교수가 지혜의 완성 비전을 제시하고 제임스가 실전 자바스크립트 코드 작성을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Serverless Trigger",
                "def": "An event-driven cloud mechanism executing code automatically in response to file changes, edits, or timer intervals.",
                "defKo": "서버리스 이벤트 트리거"
            },
            {
                "term": "Workflow Automation",
                "def": "The programmatic orchestration of repetitive multi-step tasks across enterprise cloud applications.",
                "defKo": "워크플로우 자동화"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 31: Google Apps Script: The Invisible Laborer
    {
        "num": 31,
        "type": "content",
        "title": "GOOGLE APPS SCRIPT: THE INVISIBLE LABORER",
        "subtitle": "Zero-server, cloud-native JavaScript automation connecting Drive, Gmail, Docs, and Sheets",
        "points": [
            "Zero Infrastructure: Runs directly inside Google's cloud servers with zero local node.js or server setup.",
            "Native Workspace Integration: Built-in classes like `DriveApp`, `DocumentApp`, `SpreadsheetApp`, and `GmailApp`.",
            "Free Enterprise Quotas: Executes up to 6 minutes per script execution and 90 minutes of daily runtime for free."
        ],
        "script": (
            "[Prof. Peter] Slide 31 introduces \"GOOGLE APPS SCRIPT: THE INVISIBLE LABORER.\" What makes Apps Script so uniquely powerful for developers and managers?\n\n"
            "[TA James] Zero server maintenance! You don't need to rent an AWS EC2 instance, manage Docker containers, or configure SSL certificates. You write modern JavaScript directly in your browser, and Google runs it on their world-class infrastructure for free!\n\n"
            "[TA Sarah] Look at the native APIs: `DriveApp` manages files and folders, `DocumentApp` generates reports, `SpreadsheetApp` calculates financial formulas, and `GmailApp` sends automated notifications.\n\n"
            "[Prof. Peter] It is an entire enterprise integration engine built right into your Google Workspace.\n\n"
            "[TA Sarah] Let us inspect trigger-based automation pipelines on Slide 32!"
        ),
        "koreanGuide": {
            "summary": "Google Apps Script(GAS): 인프라 관리 없는 보이지 않는 디지털 노동자",
            "points": [
                "제로 인프라: 서버 임대나 도커 설정 없이 구글 클라우드에서 직접 구동되는 자바스크립트 런타임",
                "네이티브 워크스페이스 클래스: DriveApp, DocumentApp, SpreadsheetApp, GmailApp의 유기적 결합",
                "무료 엔터프라이즈 쿼터: 실행당 최대 6분, 일일 90분의 풍부한 무료 클라우드 연산 지원"
            ],
            "tips": "제임스 조교가 복잡한 서버 배포 없이 브라우저에서 즉시 돌아가는 GAS의 편리함을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Google Apps Script (GAS)",
                "def": "A rapid application development platform powered by cloud JavaScript integrating Google Workspace APIs.",
                "defKo": "구글 앱스 스크립트 (GAS)"
            },
            {
                "term": "DriveApp API",
                "def": "The core Apps Script service allowing programmatic creation, search, and permission management for Drive files.",
                "defKo": "DriveApp 파일 관리 인터페이스"
            }
        ]
    },
    # Slide 32: Trigger-Based Automation Pipelines
    {
        "num": 32,
        "type": "content",
        "title": "TRIGGER-BASED AUTOMATION PIPELINES",
        "subtitle": "Event-driven execution: `onEdit`, `onFormSubmit`, `time-driven cron`, and Webhook listeners",
        "points": [
            "Time-Driven Triggers: Hourly or daily cron heartbeats executing background folder cleanups automatically.",
            "Edit-Driven Triggers: Firing instant workflows whenever a manager approves a row in Google Sheets.",
            "Form Submission Triggers: Ingesting client applications and generating PDF contracts in 2 seconds."
        ],
        "script": (
            "[TA James] Slide 32 diagrams \"TRIGGER-BASED AUTOMATION PIPELINES: Event-Driven Automation.\"\n\n"
            "[TA Sarah] In Apps Script, you don't need a human to click 'Run Script'. You configure Triggers: Time-driven triggers run every night at 3 AM to archive stale folders. Edit triggers fire the instant an executive marks a cell as 'Approved' in Google Sheets!\n\n"
            "[TA James] And Form Submission triggers listen to Google Forms: a customer submits an onboarding form, and within 2 seconds, Apps Script creates a Google Doc contract, inserts their name, converts it to PDF, and emails it to them automatically!\n\n"
            "[Prof. Peter] That is how you build zero-latency enterprise operations.\n\n"
            "[TA Sarah] Let us see how this overcomes human cognitive fatigue on Slide 33."
        ),
        "koreanGuide": {
            "summary": "트리거 기반 자동화 파이프라인: 시간 및 이벤트 구동 방식의 무중단 실행",
            "points": [
                "시간 기반 트리거(Time-Driven): 매일 새벽 3시 정기 폴더 정리 및 데이터 압축 크론 작업",
                "수정 기반 트리거(onEdit): 구글 시트에서 '승인' 선택 즉시 다음 워크플로우 자동 점화",
                "폼 제출 트리거(onFormSubmit): 고객 신청서 접수 즉시 2초 만에 PDF 계약서 생성 및 자동 발송"
            ],
            "tips": "사라 조교와 제임스 조교가 이벤트 트리거의 무인 자동화 시나리오를 경쾌하게 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Time-Driven Trigger",
                "def": "A cloud scheduler executing scripts automatically at specified clock times or recurring intervals.",
                "defKo": "시간 기반 트리거 (클라우드 크론)"
            },
            {
                "term": "Event-Driven Webhook",
                "def": "An automated HTTP notification mechanism invoking script execution immediately upon a state change.",
                "defKo": "이벤트 기반 웹훅"
            }
        ]
    },
    # Slide 33: Overcoming Cognitive Fatigue
    {
        "num": 33,
        "type": "content",
        "title": "OVERCOMING COGNITIVE FATIGUE",
        "subtitle": "Delegating repetitive mechanical tasks to cloud scripts to reclaim executive clarity",
        "points": [
            "Eliminating Mental Clutter: Stop worrying about renaming files, moving invoices, or sending reminder emails.",
            "Preserving Creative Bandwidth: Directing 100% of human attention toward strategic leadership and research.",
            "Error-Free Consistency: Cloud scripts execute with 100% mathematical reliability, immune to fatigue."
        ],
        "script": (
            "[Prof. Peter] Slide 33 reflects on \"OVERCOMING COGNITIVE FATIGUE.\" Human decision fatigue is one of the greatest obstacles to creative breakthroughs.\n\n"
            "[TA Sarah] When a professional has to manually check 30 invoices, rename 15 files, and email 10 reminders every single day, their mental energy is completely depleted before lunchtime!\n\n"
            "[TA James] By delegating those mechanical chores to Google Apps Script daemons, the computer does what computers do best: execute with 100% consistency 24 hours a day without ever getting tired or making a typo!\n\n"
            "[Prof. Peter] You reclaim your mental clarity to lead, innovate, and think deeply.\n\n"
            "[TA Sarah] Let us inspect collaborative velocity with @mentions and comments on Slide 34."
        ),
        "koreanGuide": {
            "summary": "인지적 피로 극복: 기계적 반복 작업의 완전한 위임과 창의적 대역폭 회복",
            "points": [
                "결정 피로(Decision Fatigue) 제거: 파일 이름 바꾸기, 인보이스 분류 등 잡무에서 해방",
                "창의적 에너지 보존: 인간의 주의력을 오직 전략적 판단과 심층 연구에 100% 재투자",
                "무결점 일관성: 피로를 모르는 클라우드 스크립트가 오타와 누락 없이 완벽한 업무 수행"
            ],
            "tips": "피터 교수가 지식인의 정신적 피로를 위로하며 자동화가 가져다주는 해방감을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Cognitive Bandwidth",
                "def": "The finite mental capacity available to an individual for deep reasoning, problem-solving, and decision-making.",
                "defKo": "인지적 대역폭 (집중 용량)"
            },
            {
                "term": "Decision Fatigue",
                "def": "The deteriorating quality of decisions made by an individual after a long session of repetitive micro-choices.",
                "defKo": "의사결정 피로"
            }
        ]
    },
    # Slide 34: Collaborative Velocity: @Mentions & Comments
    {
        "num": 34,
        "type": "content",
        "title": "COLLABORATIVE VELOCITY: @MENTIONS & COMMENTS",
        "subtitle": "Asynchronous communication directly inside documents, replacing chaotic email chains",
        "points": [
            "Inline Task Assignment: `@username please review section 3` assigns explicit accountability in the doc.",
            "Actionable Email Integration: Assigned collaborators receive email alerts and can reply directly from Gmail.",
            "Resolving Feedback Loops: Comment threads preserve historical deliberation without cluttering final prose."
        ],
        "script": (
            "[TA Sarah] Slide 34 covers \"COLLABORATIVE VELOCITY: @MENTIONS & ACTION ITEMS.\"\n\n"
            "[TA James] Instead of sending a messy 20-email thread with 5 different attachments, you highlight a paragraph in Google Docs, type `@sarah.jenkins please verify this code snippet`, and check 'Assign to Sarah'!\n\n"
            "[TA Sarah] Sarah receives an instant notification, types her response directly inside the comment bubble, and clicks 'Resolve'. The discussion is permanently archived in the document history without adding a single byte of clutter to the final report!\n\n"
            "[Prof. Peter] That is modern asynchronous collaboration at maximum velocity.\n\n"
            "[TA Sarah] Let us see how Suggestion Mode enables non-destructive editing on Slide 35!"
        ),
        "koreanGuide": {
            "summary": "협업 가속화: 문서 내 @멘션 및 작업 할당을 통한 이메일 스팸 퇴출",
            "points": [
                "문서 내 직결 할당: @담당자 지정을 통해 이메일 핑퐁 없이 해당 문단에서 직접 피드백 요청",
                "지메일 연동 답장: 지메일 알림창에서 문서를 열지 않고도 댓글로 즉각 회신 및 승인",
                "의사결정 이력 보존: 해결(Resolve)된 댓글 스레드가 문서 이력에 남아 토론 과정 영구 보존"
            ],
            "tips": "사라 조교와 제임스 조교가 @멘션 기능의 실제 시나리오를 핑퐁 대화로 생생하게 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Inline Task Assignment",
                "def": "Assigning explicit action items to collaborators directly within collaborative document paragraphs.",
                "defKo": "본문 내 작업 직결 할당"
            },
            {
                "term": "Asynchronous Deliberation",
                "def": "Collaborative discussion occurring asynchronously within document comments without requiring meetings.",
                "defKo": "비동기 문서 토론"
            }
        ]
    },
    # Slide 35: Suggestion Mode: Non-Destructive Editing
    {
        "num": 35,
        "type": "content",
        "title": "SUGGESTION MODE: NON-DESTRUCTIVE EDITING",
        "subtitle": "Tracked changes with green diffs, preserving author sovereignty and preventing accidental deletion",
        "points": [
            "Green Diff Tracking: Proposed additions and deletions appear as colored markup for one-click approval.",
            "Author Sovereignty: Lead authors retain exclusive authority to accept or reject collaborator proposals.",
            "Psychological Safety: Reviewers feel free to propose bold edits without fear of ruining the original draft."
        ],
        "script": (
            "[Prof. Peter] Slide 35 examines \"SUGGESTION MODE: NON-DESTRUCTIVE EDITING.\" How do we maintain editorial harmony across multi-author teams?\n\n"
            "[TA Sarah] By using Google Docs 'Suggesting Mode'! When reviewers propose changes, their additions appear in green text and their deletions appear with strike-through lines.\n\n"
            "[TA James] The original text is NEVER destroyed. The lead architect reviews the green diffs and clicks the checkmark to accept or the 'X' to reject in one second!\n\n"
            "[Prof. Peter] This gives reviewers psychological safety to suggest bold improvements while preserving author sovereignty.\n\n"
            "[TA Sarah] Let us inspect our fourth enterprise case study on Slide 36!"
        ),
        "koreanGuide": {
            "summary": "제안 모드(Suggesting Mode): 비파괴적 편집과 저자 주권의 보존",
            "points": [
                "초록색 디프(Green Diffs) 추적: 제안된 추가/삭제 사항이 원본을 훼손하지 않고 마크업으로 표시",
                "저자 주권: 최종 책임자가 원클릭으로 제안을 수락(체크)하거나 거절(X)할 수 있는 완벽한 통제권",
                "심리적 안전감: 원본을 망칠 위험 없이 자유롭게 과감한 수정안을 제안할 수 있는 협업 환경"
            ],
            "tips": "사라 조교가 제안 모드가 주는 협업의 평화와 원본 보존의 가치를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Non-Destructive Editing",
                "def": "A collaborative editing paradigm where proposed changes are layered as reversible suggestions.",
                "defKo": "비파괴적 제안 편집"
            },
            {
                "term": "Author Sovereignty",
                "def": "The principle ensuring the designated document lead retains ultimate decision rights over all suggested edits.",
                "defKo": "저자 주권 (최종 수락 권한)"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 36: Case Study 4: 24/7 Automated Vendor Invoice Triage Bot
    {
        "num": 36,
        "type": "casestudy",
        "title": "CASE STUDY 4: 24/7 VENDOR INVOICE TRIAGE BOT",
        "subtitle": "Enterprise Retailer deploys Google Apps Script bot processing 2,000 invoices monthly with zero human labor",
        "company": "E-Commerce Multi-Brand Retailer",
        "problem": "Finance department spent 120 hours monthly manually downloading PDF invoices from vendor emails, renaming files, and typing totals into Google Sheets.",
        "solution": "Deployed a serverless Google Apps Script daemon with `GmailApp` triggers, Drive OCR PDF parsing, and automated Google Sheets ledger updating.",
        "impact": "2,000 monthly invoices processed in 1.8 seconds each; 120 hours of monthly finance labor eliminated; 100% accounting accuracy with zero duplicate payments.",
        "script": (
            "[Prof. Peter] Slide 36 presents \"CASE STUDY 4: 24/7 VENDOR INVOICE TRIAGE BOT.\"\n\n"
            "[TA Sarah] An e-commerce retail enterprise received over 2,000 vendor PDF invoices every single month via email. The finance team spent 120 hours every month downloading PDFs, renaming them manually, and typing payment totals into spreadsheets!\n\n"
            "[TA James] They built a lightweight Google Apps Script bot running on a 5-minute time trigger. It scans incoming emails with PDF attachments, extracts the invoice number, total amount, and due date via Drive OCR, moves the PDF into `Shared_Drives/2026_Invoices/`, and appends a row into the Master Ledger in 1.8 seconds!\n\n"
            "[Prof. Peter] Over 120 hours of monthly accounting drag was eliminated completely, with zero lost invoices and zero duplicate payments across two years of operation!\n\n"
            "[TA Sarah] Let us see how we shift from personal ego to system assets on Slide 37."
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 4: 월 2,000건 인보이스를 무인 자동 처리한 GAS 파이프라인",
            "points": [
                "문제 상황: 매월 2,000건의 거래처 인보이스를 수동으로 다운로드, 이름 변경, 장부 기입하느라 120시간 낭비",
                "솔루션: 5분 주기 GAS 트리거로 이메일 첨부파일 감지 ➔ OCR 파싱 ➔ 공유 드라이브 저장 ➔ 시트 자동 기입",
                "성과: 건당 1.8초 처리, 월 120시간 회계 잡무 완전 소멸, 2년간 중복 결제 및 누락 사고 0건"
            ],
            "tips": "제임스 조교가 1.8초 만에 이메일에서 구글 시트로 연결되는 자동화 루프를 생생히 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Automated Invoice Triage",
                "def": "The end-to-end programmatic extraction, classification, and ledger recording of incoming financial invoices.",
                "defKo": "자동 인보이스 분류 파이프라인"
            },
            {
                "term": "Master Accounting Ledger",
                "def": "A centralized Google Sheets database tracking enterprise revenue, expenses, and automated audit logs.",
                "defKo": "통합 회계 원장"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 37: From Personal Ego to System Asset
    {
        "num": 37,
        "type": "content",
        "title": "FROM PERSONAL EGO TO SYSTEM ASSET",
        "subtitle": "The philosophical shift from hoarding private knowledge to building enduring institutional legacy",
        "points": [
            "The Trap of Knowledge Hoarding: Thinking that keeping secrets makes you indispensable in an organization.",
            "The True Leader: The leader who builds automated, documented systems that thrive even in their absence.",
            "Enduring Stewardship: Creating intellectual assets that bless colleagues, clients, and future generations."
        ],
        "script": (
            "[Prof. Peter] Slide 37 reflects on a profound leadership transformation: \"FROM PERSONAL EGO TO SYSTEM ASSET.\" Sarah, why do some professionals resist documenting their workflows?\n\n"
            "[TA Sarah] Because of fear and ego! Insecure workers think: 'If only I know how to do this, my boss can never fire me.' They hoard information like a private fortress.\n\n"
            "[Prof. Peter] That is a tragic, short-sighted illusion. If your job can only run when you are suffering at your desk, you can never be promoted, you can never take a peaceful vacation, and you can never build anything lasting!\n\n"
            "[TA James] A true Intelligence Architect builds automated, documented systems that run smoothly even in their absence. That is what creates true organizational value!\n\n"
            "[TA Sarah] Let us explore how time redemption restores true cognitive freedom on Slide 38."
        ),
        "koreanGuide": {
            "summary": "개인의 에고에서 시스템 자산으로: 지식 독점을 넘어선 영구적 유산 구축",
            "points": [
                "지식 독점의 함정: 자신만이 알아야 대체 불가능하다는 불안과 에고가 낳은 비극",
                "진정한 리더의 척도: 자신이 자리에 없어도 시스템이 원활히 돌아가도록 문서화하고 자동화하는 역량",
                "승진과 확장의 기회: 잡무에 매이지 않고 시스템을 구축한 사람만이 더 큰 전략적 리더십으로 도약"
            ],
            "tips": "피터 교수가 지식 독점의 허망함을 짚고 시스템 구축자의 자유와 품격을 전합니다."
        },
        "keyTerms": [
            {
                "term": "Knowledge Hoarding",
                "def": "The deliberate withholding of operational information to create an artificial, fragile sense of job security.",
                "defKo": "지식 독점 (비문서화의 함정)"
            },
            {
                "term": "Systemic Legacy",
                "def": "The enduring organizational value and automated infrastructure that continues functioning independently of the creator.",
                "defKo": "시스템적 유산 (지속 가능 자산)"
            }
        ]
    },
    # Slide 38: Redeeming the Time: Cognitive Freedom
    {
        "num": 38,
        "type": "content",
        "title": "REDEEMING THE TIME: COGNITIVE FREEDOM",
        "subtitle": "Ephesians 5:16: Reclaiming hours from administrative friction for research, prayer, and family",
        "points": [
            "Reclaiming 10+ Hours Weekly: Automated Drive and GAS pipelines return over 500 hours annually.",
            "Restoring Focus: Spending uninterrupted morning blocks on complex mathematical modeling and strategy.",
            "Living with Purpose: Freeing human energy to serve community, worship God, and love one's family."
        ],
        "script": (
            "[Prof. Peter] Slide 38 proclaims \"REDEEMING THE TIME: COGNITIVE FREEDOM.\" In Ephesians 5:16, the Apostle Paul instructs us to 'redeem the time, because the days are evil.'\n\n"
            "[TA Sarah] Time is our most sacred non-renewable stewardship. When we deploy Google Workspace automation and Shared Drives, we reclaim 10 to 15 hours every single week!\n\n"
            "[TA James] That is 500 hours a year! That is time you can spend playing with your children, reading foundational theological texts, mentoring younger students, or resting in deep peace.\n\n"
            "[Prof. Peter] Technology finds its highest dignity when it liberates human beings to love God and serve their neighbors with joy.\n\n"
            "[TA Sarah] Let us dedicate our craft on Slide 39: Soli Deo Gloria!"
        ),
        "koreanGuide": {
            "summary": "세월을 아끼라(에베소서 5:16): 인지적 자유와 인간 본연의 소명 회복",
            "points": [
                "에베소서 5:16 실천: 주당 10~15시간, 연간 500시간 이상의 행정 잡무 시간을 회복",
                "방해 없는 몰입: 심층 연구, 창의적 전략, 기도의 아침 시간을 지켜내는 인지적 자유",
                "기술의 거룩한 목적: 가족을 사랑하고 이웃을 섬기며 하나님을 영화롭게 하는 삶으로의 회복"
            ],
            "tips": "피터 교수가 성경 말씀과 공학의 연결점을 깊은 은혜와 진정성으로 설파합니다."
        },
        "keyTerms": [
            {
                "term": "Time Redemption (Ephesians 5:16)",
                "def": "The deliberate, ethical reclamation of finite human lifespan from mechanical labor for higher spiritual and creative callings.",
                "defKo": "시간 구속 (세월을 아끼라)"
            },
            {
                "term": "Cognitive Liberation",
                "def": "The mental freedom attained when administrative tasks are executed flawlessly by background automation.",
                "defKo": "인지적 해방 (사유의 자유)"
            }
        ]
    },
    # Slide 39: Soli Deo Gloria: Committing Work to Eternal Purpose
    {
        "num": 39,
        "type": "content",
        "title": "SOLI DEO GLORIA: COMMITTING WORK TO ETERNAL PURPOSE",
        "subtitle": "Dedicating our file structures, automated scripts, and intellectual assets to the Glory of God Alone",
        "points": [
            "Soli Deo Gloria: The foundational banner of Oikos University and Smart Insight Lab.",
            "Sanctity in the Small Details: Building clean, organized folder hierarchies as an act of faithful stewardship.",
            "Eternal Impact: Designing enterprise systems that stand the test of time and reflect divine order."
        ],
        "script": (
            "[Prof. Peter] Slide 39 declares our bedrock: \"SOLI DEO GLORIA: COMMITTING WORK TO ETERNAL PURPOSE: To God Alone Be the Glory.\"\n\n"
            "[TA Sarah] Whether you are configuring an Apps Script trigger, organizing a Shared Drive, or writing a corporate charter, we do all things with excellence because God is a God of order and truth.\n\n"
            "[TA James] When your code runs reliably in the middle of the night without crashing, and your colleagues find peace because the files are organized, your engineering reflects divine integrity!\n\n"
            "[Prof. Peter] May all our intellectual and technical achievements bring glory to our Creator.\n\n"
            "[TA Sarah] Let us inspect our 5-tier Enterprise Drive Vault Blueprint on Slide 40!"
        ),
        "koreanGuide": {
            "summary": "Soli Deo Gloria: 모든 작업을 영원한 목적에 바치는 청지기적 소명",
            "points": [
                "오직 하나님께 영광(Soli Deo Gloria): 작은 폴더 정리와 코드 한 줄에도 하나님의 질서와 진실성을 반영",
                "작은 일의 성실함: 보이지 않는 곳에서 돌아가는 완벽한 자동화 스크립트를 통한 이웃 섬김",
                "시간의 시험을 견디는 견고한 엔터프라이즈 시스템 구축"
            ],
            "tips": "3인의 강사진이 한목소리로 진실한 사명감을 선포하며 수업의 영적 정점을 이룹니다."
        },
        "keyTerms": [
            {
                "term": "Soli Deo Gloria",
                "def": "The foundational theological motto dedicating all intellectual and technological mastery to the Glory of God Alone.",
                "defKo": "솔리 데오 글로리아 (오직 하나님께 영광)"
            },
            {
                "term": "Divine Order in Architecture",
                "def": "The intentional reflection of divine precision, reliability, and beauty across technical system designs.",
                "defKo": "아키텍처 속의 신적 질서"
            }
        ]
    },
    # Slide 40: The 5-Tier Enterprise Vault Blueprint
    {
        "num": 40,
        "type": "content",
        "title": "THE 5-TIER ENTERPRISE VAULT BLUEPRINT",
        "subtitle": "01_Inbox_Ingestion, 02_Active_Projects, 03_Knowledge_Vault, 04_Executive_Exports, 05_Cold_Archive",
        "points": [
            "01_Inbox_Ingestion (Yellow): Temporary staging area for raw uploads and incoming webhooks.",
            "02_Active_Projects (Green): Active sprint workspaces with Contributor access.",
            "03_Knowledge_Vault (Blue): Core immutable institutional knowledge and reference manuals.",
            "04_Executive_Exports (Red): Final client deliverables and board decision memos with IRM locks.",
            "05_Cold_Archive (Slate): Historical completed project archives with Read-Only permissions."
        ],
        "script": (
            "[TA Sarah] Slide 40 provides the exact architectural blueprint: \"THE 5-TIER ENTERPRISE VAULT BLUEPRINT.\"\n\n"
            "[TA James] Look at the 5 standardized root folders: `01_Inbox_Ingestion` in Yellow is where incoming webhooks drop raw files. `02_Active_Projects` in Green contains active team sprint folders. `03_Knowledge_Vault` in Blue holds immutable technical manuals!\n\n"
            "[TA Sarah] `04_Executive_Exports` in Red stores final board decision memos with DRM download restrictions. And `05_Cold_Archive` in Slate Gray holds read-only historical records.\n\n"
            "[Prof. Peter] This 5-tier taxonomy solves 100% of organizational storage confusion.\n\n"
            "[TA James] Let us review our Pre-Deployment Governance Checklist on Slide 41!"
        ),
        "koreanGuide": {
            "summary": "5계층 엔터프라이즈 금고 청사진: 수집부터 활성, 지식, 경영 산출물, 아카이브까지",
            "points": [
                "01_Inbox_Ingestion (노랑): 웹훅 및 외부 업로드 파일의 임시 수집 스테이징 구역",
                "02_Active_Projects (초록): 팀원들이 활발히 협업하는 기여자 권한 중심의 활성 프로젝트",
                "03_Knowledge_Vault (파랑): 변조되지 않는 핵심 기술 매뉴얼 및 기업 정책 저장소",
                "04_Executive_Exports (빨강): IRM 다운로드 방지가 적용된 최종 이사회 승인 보고서",
                "05_Cold_Archive (회색): 읽기 전용으로 보관되는 완료된 프로젝트 아카이브"
            ],
            "tips": "제임스 조교가 5개 폴더의 역할과 색상 표준을 일목요연하게 정리해 줍니다."
        },
        "keyTerms": [
            {
                "term": "5-Tier Vault Taxonomy",
                "def": "A standardized enterprise directory structure partitioning ingestion, active work, reference vaults, exports, and archives.",
                "defKo": "5계층 엔터프라이즈 금고 택소노미"
            },
            {
                "term": "Staging Ingestion Buffer",
                "def": "A transient directory receiving raw files before validation, renaming, and programmatic routing.",
                "defKo": "임시 수집 버퍼 구역"
            }
        ]
    },
    # Slide 41: Production Checklist: Pre-Deployment Governance
    {
        "num": 41,
        "type": "content",
        "title": "PRODUCTION CHECKLIST: PRE-DEPLOYMENT GOVERNANCE",
        "subtitle": "The 6-step audit gate every enterprise Google Drive deployment must pass",
        "points": [
            "Gate 1: Domain-level Shared Drives enabled with 0% personal 'My Drive' usage for enterprise assets.",
            "Gate 2: 5-Tier taxonomic folder structure deployed with standardized color coding.",
            "Gate 3: Role-Based Access Control (RBAC) configured (90% Contributor, <5% Manager).",
            "Gate 4: IRM Anti-Download restrictions active on Executive and Financial folders.",
            "Gate 5: Automated Apps Script triggers active for file renaming and trash monitoring.",
            "Gate 6: Google Drive for Desktop verified in 'Stream Files' mode across all employee workstations."
        ],
        "script": (
            "[TA James] Slide 41 presents our \"PRODUCTION CHECKLIST: PRE-DEPLOYMENT GOVERNANCE.\"\n\n"
            "[TA Sarah] Before releasing an enterprise Drive environment to your organization, you must pass all 6 audit gates!\n\n"
            "[TA James] Gate 1: Shared Drives enforced. Gate 2: 5-tier taxonomy with color coding. Gate 3: RBAC roles locked down. Gate 4: IRM anti-download rules active. Gate 5: Apps Script automation verified. Gate 6: Drive for Desktop in Streaming mode!\n\n"
            "[Prof. Peter] When all 6 gates pass, your cloud storage becomes an unbreachable corporate fortress.\n\n"
            "[TA Sarah] Let us inspect the live Google Apps Script code snippet on Slide 42!"
        ),
        "koreanGuide": {
            "summary": "프로덕션 체크리스트: 엔터프라이즈 드라이브 배포 전 6대 거버넌스 관문",
            "points": [
                "1관문: 전사 자산의 공유 드라이브 100% 보관 원칙 수립",
                "2관문: 5계층 택소노미 및 색상 코딩 표준 적용",
                "3관문: RBAC 역할 통제(90% 기여자, 관리자 최소화)",
                "4관문: IRM 다운로드 방지 정책 활성화",
                "5관문: Apps Script 자동화 트리거 정상 구동 검증",
                "6관문: 전 직원 워크스테이션의 파일 스트리밍 모드 확인"
            ],
            "tips": "제임스 조교가 6대 체크포인트를 명쾌하고 단호하게 체크리스트로 확인합니다."
        },
        "keyTerms": [
            {
                "term": "Governance Audit Gate",
                "def": "A mandatory verification checklist ensuring security, taxonomy, and automation rules are enforced.",
                "defKo": "거버넌스 감사 관문"
            },
            {
                "term": "Workstation Compliance",
                "def": "Verifying that client endpoint machines comply with enterprise streaming and encryption policies.",
                "defKo": "워크스테이션 규정 준수성"
            }
        ]
    },
    # Slide 42: Production Code: Google Apps Script Auto-Router
    {
        "num": 42,
        "type": "content",
        "title": "PRODUCTION CODE: GAS AUTO-ROUTER DAEMON",
        "subtitle": "Live JavaScript snippet: Ingesting files, renaming via ISO 8601, and moving to target folders",
        "points": [
            "Folder Monitoring: `DriveApp.getFolderById(INBOX_ID).getFiles()` retrieves incoming files.",
            "ISO 8601 Formatting: `Utilities.formatDate(new Date(), 'UTC', 'yyyyMMdd') + '_' + file.getName()`.",
            "Atomic Move: `file.moveTo(targetFolder)` relocates the file in 50 milliseconds with zero duplication."
        ],
        "script": (
            "[TA James] Slide 42 displays real production code: \"PRODUCTION CODE: GAS AUTO-ROUTER DAEMON.\"\n\n"
            "[TA Sarah] Look at how concise and readable Google Apps Script is! In just 12 lines of clean JavaScript: Line 1 connects to our Inbox folder via `DriveApp.getFolderById`. Line 4 loops through each uploaded file.\n\n"
            "[TA James] Line 6 formats today's timestamp as `YYYYMMDD` using `Utilities.formatDate`. Line 8 renames the file with our ISO standard, and Line 10 calls `file.moveTo(targetFolder)` to move the file into the secure vault in 50 milliseconds!\n\n"
            "[Prof. Peter] With a 5-minute time trigger, this script runs completely unattended 24 hours a day, 365 days a year!\n\n"
            "[TA Sarah] Let us inspect the Architect's Stewardship Mandate on Slide 43."
        ),
        "koreanGuide": {
            "summary": "프로덕션 코드: Google Apps Script 파일 자동 분류 및 명명 라우터",
            "points": [
                "12줄의 자바스크립트로 구현된 강력한 무인 드라이브 자동화 라우터 코드 분해",
                "DriveApp.getFolderById를 통한 인박스 폴더 감지 및 파일 순회",
                "Utilities.formatDate를 통한 ISO 8601 날짜 스탬프 부착 및 file.moveTo를 통한 50ms 즉각 이관"
            ],
            "tips": "제임스 조교가 화면에 보이는 실제 코드 한 줄 한 줄의 동작 원리를 명쾌하게 해설합니다."
        },
        "keyTerms": [
            {
                "term": "Atomic File Move",
                "def": "The instantaneous reallocation of a file pointer across cloud directories without copying data.",
                "defKo": "원자적 파일 이동 (file.moveTo)"
            },
            {
                "term": "Utilities.formatDate",
                "def": "Apps Script's native timezone-aware date formatting utility supporting ISO 8601 string generation.",
                "defKo": "Utilities.formatDate 날짜 포맷터"
            }
        ]
    },
    # Slide 43: The Architect's Stewardship Mandate
    {
        "num": 43,
        "type": "content",
        "title": "THE ARCHITECT'S STEWARDSHIP MANDATE",
        "subtitle": "Order, discipline, and intentionality as reflections of divine wisdom in digital systems",
        "points": [
            "Order vs. Entropy: Natural physical systems devolve into chaos unless sustained by intentional design.",
            "Faithful in the Small Things: Honoring God through clean directory trees, secure permissions, and robust code.",
            "Blessing Others: Building transparent, reliable knowledge vaults that empower colleagues to thrive."
        ],
        "script": (
            "[Prof. Peter] Slide 43 defines \"THE ARCHITECT'S STEWARDSHIP MANDATE.\" In physics, the Second Law of Thermodynamics tells us that entropy—disorder—naturally increases in the universe unless deliberate energy and intelligent design are applied.\n\n"
            "[TA Sarah] In digital computing, a messy, chaotic file system is the textbook definition of software entropy! It drains energy, breeds anxiety, and destroys productivity.\n\n"
            "[TA James] As Intelligence Architects, we apply deliberate architectural design to establish order, peace, and security across our digital environments.\n\n"
            "[Prof. Peter] Let us inspect our capstone enterprise case study on Slide 44!"
        ),
        "koreanGuide": {
            "summary": "지능 건축가의 청지기적 사명: 엔트로피를 이기는 질서와 섬김의 설계",
            "points": [
                "열역학 제2법칙과 소프트웨어 엔트로피: 의도적인 설계 에너지를 투입하지 않으면 디지털 환경은 무질서로 퇴보",
                "작은 일의 충성: 폴더 정리와 권한 통제를 통해 동료들에게 평안과 질서를 선물하는 영적 청지기직",
                "하나님의 질서를 반영하는 견고하고 아름다운 엔터프라이즈 시스템 구축"
            ],
            "tips": "피터 교수가 물리학의 엔트로피 개념과 영적 청지기직을 결합하여 감동적인 통찰을 전합니다."
        },
        "keyTerms": [
            {
                "term": "Software Entropy",
                "def": "The tendency of software systems and file repositories to become increasingly disorganized and chaotic over time.",
                "defKo": "소프트웨어 엔트로피 (무질서도 증가)"
            },
            {
                "term": "Stewardship Mandate",
                "def": "The ethical duty of architects to maintain disciplined order, integrity, and beauty across all technical systems.",
                "defKo": "청지기적 사명 (질서 수호 의무)"
            }
        ]
    },
    # Slide 44: Case Study 5: 18X Enterprise ROI & 7-Step Vault Blueprint
    {
        "num": 44,
        "type": "casestudy",
        "title": "CASE STUDY 5: 18X ENTERPRISE ROI BLUEPRINT",
        "subtitle": "Global Logistics Conglomerate transforms 1,200 shared folders across 14 countries",
        "company": "Global Multi-Modal Logistics Conglomerate",
        "problem": "10,000 employees across 14 countries had 1,200 disconnected Google Drive folders, losing 25,000 hours weekly in customs document searches and duplicate billing errors.",
        "solution": "Deployed centralized 5-Tier Shared Drive Knowledge Vault with automated Google Apps Script ISO router daemons, IRM access controls, and Drive OCR search.",
        "impact": "18X measured ROI; customs document retrieval compressed from 45 minutes to 8 seconds; 1.2M annual hours reclaimed ($36M value); billing error rate dropped by 94%.",
        "script": (
            "[Prof. Peter] Slide 44 presents our capstone case study: \"CASE STUDY 5: 18X ENTERPRISE ROI BLUEPRINT.\"\n\n"
            "[TA Sarah] A global logistics conglomerate operating across 14 countries had 10,000 employees drowning in 1,200 chaotic Google Drive folders. Customs agents and logistics managers were losing 25,000 hours every single week searching for export declarations and shipping manifests!\n\n"
            "[TA James] They deployed our standardized 5-Tier Shared Drive Vault powered by Google Apps Script auto-routers and Drive AI OCR. Whenever an air manifest arrives in any language, the script renames it with ISO standards, tags the customs ID, and routes it to `03_Knowledge_Vault` in 2 seconds!\n\n"
            "[Prof. Peter] Look at the enterprise metrics: customs document search was compressed from 45 minutes to 8 seconds! They reclaimed 1.2 million working hours annually—worth 36 million dollars in operational value—and billing errors plunged by 94%!\n\n"
            "[TA Sarah] That is an extraordinary 18X return on investment.\n\n"
            "[TA James] Now let us deploy your own live GAS-powered vault in Lab 5 on Slide 45!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 5: 글로벌 물류 대기업 18배 ROI 및 7단계 지식 금고 청사진",
            "points": [
                "문제 상황: 14개국 10,000명의 직원이 1,200개 파편화된 폴더 속에서 통관 서류 검색으로 주당 25,000시간 낭비",
                "솔루션: 5계층 공유 드라이브 금고 및 Google Apps Script ISO 자동 라우터, AI OCR 검색 전사 구축",
                "성과: 통관 서류 검색 45분에서 8초로 단축, 연간 120만 시간(3,600만 달러 가치) 회복, 청구 오류 94% 감소, 18배 ROI 달성"
            ],
            "tips": "사라 조교와 제임스 조교가 18배 ROI의 압도적인 수치를 강조하며 실습으로 힘차게 전환합니다."
        },
        "keyTerms": [
            {
                "term": "18X Enterprise ROI",
                "def": "The quantifiable multiplier of operational savings and reclaimed productivity achieved through enterprise cloud vault standardization.",
                "defKo": "18배 엔터프라이즈 투자 수익률 (ROI)"
            },
            {
                "term": "Customs Manifest Indexing",
                "def": "The automated ingestion and OCR indexing of international trade and shipping documentation.",
                "defKo": "통관 서류 자동 인덱싱"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 45: Hands-on Lab 5 & Conclusion
    {
        "num": 45,
        "type": "lab",
        "title": "🛠️ HANDS-ON LAB 5 & CONCLUSION",
        "subtitle": "Deploying a GAS-Powered Shared Drive Knowledge Vault with ISO 8601 Auto-Routers",
        "mission": "Create a 5-Tier Enterprise Shared Drive structure in Google Drive, configure Virtual File Streaming, write a Google Apps Script auto-router with time-driven triggers, and verify automated ISO renaming.",
        "steps": [
            "Step 1: Open Google Drive and create a new Shared Drive titled `Enterprise_System_Vault`.",
            "Step 2: Create the 5 standardized root folders: 01_Inbox (Yellow), 02_Active (Green), 03_Vault (Blue), 04_Exports (Red), 05_Archive (Slate).",
            "Step 3: Open `script.google.com`, paste the GAS Auto-Router daemon, and insert your `01_Inbox` and `03_Vault` folder IDs.",
            "Step 4: Configure a 5-minute time-driven trigger and test dropping a messy PDF into `01_Inbox`.",
            "Step 5: Verify that the script renames the file to `YYYYMMDD_filename.pdf` and moves it automatically into `03_Vault`!"
        ],
        "script": (
            "[TA Sarah] Here we are at Slide 45: \"🛠️ HANDS-ON LAB 5 & SESSION CONCLUSION!\"\n\n"
            "[TA James] Tonight's mission is pure engineering! Step 1: Create a Shared Drive named `Enterprise_System_Vault`. Step 2: Build the 5 color-coded folders: Inbox, Active, Vault, Exports, Archive. Step 3: Open Apps Script, paste our Auto-Router code, and set folder IDs. Step 4: Set a 5-minute trigger. Step 5: Drop a messy test PDF into Inbox and watch it get automatically renamed and moved into Vault in 50 milliseconds!\n\n"
            "[Prof. Peter] Once you experience your first automated cloud daemon moving and organizing files while you sleep, you cross the boundary from consumer user to true Intelligence Architect!\n\n"
            "[TA Sarah] In our next session, Session 6, we will dive into the massive 1-Million Token Context Playground and master Vibe Coding with Google AI Studio!\n\n"
            "[Prof. Peter] On behalf of TA Sarah Jenkins, TA James Wilson, and the entire Smart Insight Lab, congratulations on mastering Session 5! Soli Deo Gloria, and we will see you in Session 6!"
        ),
        "koreanGuide": {
            "summary": "실습 과제 5 및 세션 마무리: GAS 기반 공유 드라이브 지식 금고 및 자동 라우터 구축",
            "points": [
                "실습 미션: 'Enterprise_System_Vault' 공유 드라이브 개설 및 5대 색상 폴더 구축",
                "Google Apps Script에 자동 라우터 코드를 붙여넣고 5분 주기 시간 트리거 설정",
                "임의의 지저분한 PDF를 인박스에 드롭하여 50ms 만에 ISO 명명 규칙으로 변환되어 금고로 자동 이동하는 무인 자동화 검증"
            ],
            "tips": "3인의 강사진이 오늘 수업의 성취를 축하하고 다음 세션(Session 6: 100만 토큰 & 바이브 코딩)에 대한 기대감을 높이며 마무리합니다."
        },
        "keyTerms": [
            {
                "term": "Hands-on Milestone",
                "def": "The practical engineering completion of a functioning technical artifact fulfilling the session's learning objectives.",
                "defKo": "실습 달성 마일스톤"
            },
            {
                "term": "Automated Cloud Daemon",
                "def": "A serverless background script running continuously on cloud infrastructure to manage enterprise data assets.",
                "defKo": "자동화 클라우드 데몬 (무인 스크립트)"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    }
]

def generate_session5_md(slides):
    lines = []
    lines.append("# Session 5: From Personal Drawer to System Vault: Enterprise Google Drive Mastery, Apps Script Automation & Governance")
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
    new_export = f"export const SLIDES_SESSION_5 = {slides_json};"
    
    pattern = r"export\s+const\s+SLIDES_SESSION_5\s*=\s*\[[\s\S]*?\];"
    if re.search(pattern, content):
        updated_content = re.sub(pattern, lambda m: new_export, content, count=1)
        with open(SLIDES_DATA_JS, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Successfully updated SLIDES_SESSION_5 in slidesData.js!")
    else:
        print("Could not find SLIDES_SESSION_5 pattern in slidesData.js!")

def main():
    print(f"Total slides configured: {len(SLIDES_45_SESSION_5)}")
    
    # Verify part dividers
    part_slides = [s for s in SLIDES_45_SESSION_5 if s['type'] == 'section']
    print(f"Total PART Section Slides: {len(part_slides)}")
    for ps in part_slides:
        print(f"  Slide {ps['num']:02d}: {ps['title']}")
        
    # Verify case studies
    case_slides = [s for s in SLIDES_45_SESSION_5 if 'CASE STUDY' in s['title']]
    print(f"Total Case Study Slides: {len(case_slides)}")
    for cs in case_slides:
        print(f"  Slide {cs['num']:02d}: {cs['title']}")

    # 1. Write session5.md
    session5_md_content = generate_session5_md(SLIDES_45_SESSION_5)
    with open(SESSION5_MD, 'w', encoding='utf-8') as f:
        f.write(session5_md_content)
    print(f"Successfully generated and saved {SESSION5_MD} ({len(session5_md_content)} bytes)")
    
    # 2. Update slidesData.js
    update_slides_data_js(SLIDES_45_SESSION_5)
    
    print("Session 5 generation completed successfully!")

if __name__ == '__main__':
    main()
