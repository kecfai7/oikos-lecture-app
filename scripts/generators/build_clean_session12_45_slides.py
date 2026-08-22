# -*- coding: utf-8 -*-
"""
Oikos University - Session 12 Clean 45-Slide Master Generator
Course: The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom
Session 12: World Models: Genie 3 Simulation & Waymo Autonomous Training
Features:
- Full 45 Slides with 3-Presenter Trio (Prof. Peter Kim, TA Sarah Jenkins, TA James Wilson)
- Clean 4-Part Structure (Part 1: Slide 2, Part 2: Slide 12, Part 3: Slide 23, Part 4: Slide 34)
- 5 Practical Enterprise Case Studies:
    1. Slide 11: Waymo Autonomous Fleet Zero-Fatalities Training on 500M Genie 3 Miles
    2. Slide 22: Humanitarian Disaster Response: Simulating Category 5 Hurricane Flooding
    3. Slide 33: Global Defense Drone Swarm Combat Flight Simulator
    4. Slide 40: Industrial Robotics Factory Digital Twin: Zero-Downtime Retooling
    5. Slide 44: 50X Autonomous Physical AI Training Velocity ROI Blueprint
- Full sync with session12.md and slidesData.js (SLIDES_SESSION_12)
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
SESSION12_MD = os.path.join(BASE_DIR, "session12.md")

SLIDES_45_SESSION_12 = [
    # Slide 1: Course Title
    {
        "num": 1,
        "type": "title",
        "title": "OIKOS UNIVERSITY • SOLI DEO GLORIA",
        "subtitle": "THE ARCHITECT OF INTELLIGENCE: Mastering Agentic IT & Strategic Wisdom",
        "detail": "Session 12: World Models: Genie 3 Simulation & Waymo Autonomous Training",
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab",
        "script": (
            "[Prof. Peter] Welcome back, global scholars and architects, to Oikos University! I am Professor Peter Kim, Director of Smart Insight Lab. Today on Slide 1, we enter the physical simulation frontier: \"Session 12: World Models: Genie 3 Simulation & Waymo Autonomous Training.\"\n\n"
            "[TA Sarah] Hello everyone! I am Sarah Jenkins, Senior AI Fellow. Until recently, AI was trapped inside 2D text and pixels. But with World Models, artificial intelligence now learns the physical laws of space, gravity, friction, and continuous time!\n\n"
            "[TA James] And I am James Wilson, your DevOps TA! Google Genie 3 represents the pinnacle of generative simulation: converting 280 billion Street View images into real-time, controllable 3D worlds at 60 FPS, training 10,000 Waymo autonomous driving agents simultaneously in extreme edge cases!\n\n"
            "[Prof. Peter] Under our founding motto, \"SOLI DEO GLORIA—To God Alone Be the Glory,\" let us master spatial world models to build safe, noble, and life-saving physical systems.\n\n"
            "[TA Sarah] Let us open Part 1 and explore World Models beyond next-token prediction on Slide 2!"
        ),
        "koreanGuide": {
            "summary": "Session 12 개요 및 Oikos University 3인 강사진(피터 교수, 사라 수석조교, 제임스 개발조교) 환영 인사",
            "points": [
                "강의 주제: 월드 모델(World Models): 지니 3(Genie 3) 시뮬레이션과 웨이모(Waymo) 자율주행 훈련",
                "2D 텍스트 예측을 넘어 3차원 물리 법칙(중력, 마찰력, 연속 시간)을 학습한 공간 지능의 도래",
                "구글 스트리트뷰 2,800억 장 데이터 기반 60 FPS 실시간 상호작용 시뮬레이터 아키텍처"
            ],
            "tips": "피터 교수의 공간 물리 철학과 사라 조교의 VMC 아키텍처 분석, 제임스 조교의 웨이모 대규모 가상 훈련 관점을 결합하세요."
        },
        "keyTerms": [
            {
                "term": "World Model",
                "def": "An AI system learning an internal physical model of spatial geometry, dynamics, and causality to simulate future states.",
                "defKo": "월드 모델 (공간 물리 지능)"
            },
            {
                "term": "Google Genie 3",
                "def": "Google's real-time generative physical world simulator generating controllable 3D environments from images and text.",
                "defKo": "구글 지니 3 (Genie 3)"
            }
        ]
    },
    # Slide 2: Part 1 Section Divider
    {
        "num": 2,
        "type": "section",
        "title": "PART 1: WORLD MODELS: BEYOND NEXT-TOKEN PREDICTION",
        "subtitle": "Transitioning from 2D pixel generation to 3D physical world state dynamics under Soli Deo Gloria",
        "script": (
            "[TA Sarah] Look at Slide 2: \"PART 1: WORLD MODELS: BEYOND NEXT-TOKEN PREDICTION.\" Professor, why is predicting the next token insufficient for robotics and autonomous driving?\n\n"
            "[Prof. Peter] Because a language model knows that 'an apple falls', but it has no physical intuition of momentum, trajectory, or kinetic impact! If an autonomous vehicle or surgical robot relies only on text probability, catastrophic physical accidents occur!\n\n"
            "[TA James] World models understand physical causality: if you turn the steering wheel 15 degrees to the left at 60 MPH on black ice, the world model predicts the exact skidding trajectory across 3D space in real time!\n\n"
            "[TA Sarah] In Part 1, we deconstruct the VMC architecture and the 280-billion-image Google Street View data moat.\n\n"
            "[Prof. Peter] Let us examine breaking the 2D frame on Slide 3."
        ),
        "koreanGuide": {
            "summary": "Part 1 섹션 전환: 토큰 예측을 넘어 3D 물리 인과성 학습으로",
            "points": [
                "토큰 예측의 한계: '사과가 떨어진다'는 글자는 알지만 운동량, 궤적, 충돌 에너지를 물리적으로 계산하지 못함",
                "월드 모델의 인과성: 빙판길에서 시속 60마일로 핸들을 15도 꺾었을 때의 미끄러짐 궤적을 3D 시공간에서 정확히 예측",
                "VMC(Vision, Memory, Controller) 아키텍처와 구글의 2,800억 장 스트리트뷰 데이터 해자"
            ],
            "tips": "사라 조교가 텍스트와 물리 공간의 차이를 짚고 제임스가 실전 자율주행 물리 시뮬레이션의 위력을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Physical Causality Intuition",
                "def": "The internal AI representation of momentum, mass, friction, and fluid dynamics governing physical objects.",
                "defKo": "물리적 인과성 직관"
            },
            {
                "term": "Continuous Time-Space Latent",
                "def": "A multi-dimensional latent representation modeling time and 3D spatial coordinates as continuous mathematical manifolds.",
                "defKo": "연속 시공간 잠재 공간"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 3: Breaking the 2D Frame: Moving to Active Interaction
    {
        "num": 3,
        "type": "content",
        "title": "BREAKING THE 2D FRAME: ACTIVE INTERACTION",
        "subtitle": "Why passive video generators (Sora, Runway) fail at physical simulation and agent training",
        "points": [
            "Passive Video Illusion: Video models generate pretty pixels, but users CANNOT steer the camera or interact with objects.",
            "Interactive World Simulators: Genie 3 allows real-time keyboard/controller input, recalculating physics 60 times per second.",
            "Closed-Loop Action-Perception: The agent takes an action, the world model renders the consequence, and the agent learns from feedback."
        ],
        "script": (
            "[Prof. Peter] Slide 3 explores \"BREAKING THE 2D FRAME: ACTIVE INTERACTION.\"\n\n"
            "[TA Sarah] Many people confuse video generation models like OpenAI Sora with World Models! Video models generate passive movies—you hit play and watch. But you cannot steer the car, open a door, or drop a ball!\n\n"
            "[TA James] Google Genie 3 is an Interactive World Simulator! You plug in a joystick or an AI driving agent: when you press 'Accelerate', Genie 3 renders the forward motion, calculates tire friction, and updates the environment at 60 FPS!\n\n"
            "[Prof. Peter] That closed-loop interaction is where true physical intelligence is born.\n\n"
            "[TA Sarah] Let us inspect Google Genie 3 architecture on Slide 4."
        ),
        "koreanGuide": {
            "summary": "2D 프레임의 파괴: 수동적 비디오 생성에서 능동적 상호작용으로",
            "points": [
                "수동적 비디오의 한계: Sora나 Runway는 감상용 영상을 만들 뿐, 카메라를 돌리거나 물체와 상호작용 불가",
                "지니 3(Genie 3)의 능동 시뮬레이터: 조이스틱이나 에이전트 명령에 따라 초당 60회 물리 연산 및 렌더링 갱신",
                "행동-지각 폐루프(Closed-Loop): 에이전트가 행동을 취하면 월드 모델이 물리적 결과를 반환하고 피드백 학습"
            ],
            "tips": "사라 조교와 제임스 조교가 수동적 감상 영상(Movie)과 실시간 상호작용 세계(Simulator)의 본질적 차이를 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Action-Perception Closed Loop",
                "def": "The continuous feedback cycle where an agent acts within an environment, observes the state change, and refines policy.",
                "defKo": "행동-지각 폐루프"
            },
            {
                "term": "Interactive Generative Simulator",
                "def": "A neural model generating photorealistic, physically consistent visual frames in real-time response to control inputs.",
                "defKo": "대화형 생성 시뮬레이터"
            }
        ]
    },
    # Slide 4: Google Genie 3: The World's First Generative Simulator
    {
        "num": 4,
        "type": "content",
        "title": "GOOGLE GENIE 3: GENERATIVE SIMULATOR",
        "subtitle": "Generating infinite playable, physically consistent 3D environments from a single prompt or photograph",
        "points": [
            "Single-Image World Genesis: Upload a single smartphone photo of Tokyo; Genie 3 generates a fully explorable 3D city.",
            "Physics Consistency: Rigid bodies bounce, water splashes with fluid mechanics, and lighting obeys ray-tracing optics.",
            "Zero Hand-Crafted Polygons: Built without 3D artists, meshes, or manual game engine rigging."
        ],
        "script": (
            "[Prof. Peter] Slide 4 presents \"GOOGLE GENIE 3: THE WORLD'S FIRST GENERATIVE SIMULATOR.\"\n\n"
            "[TA Sarah] Imagine uploading a single photograph of a bustling street in Seoul or a sketch of an alien planet. In under 3 seconds, Genie 3 generates an entire interactive 3D world that you can walk through!\n\n"
            "[TA James] Look at the physics consistency: When a virtual ball bounces off a wall, it preserves momentum. When water splashes, fluid dynamics calculate viscosity—all generated purely by neural weights with zero manual 3D modeling!\n\n"
            "[Prof. Peter] Let us inspect the 3-phase interactive pipeline on Slide 5."
        ),
        "koreanGuide": {
            "summary": "구글 지니 3: 사진 한 장으로 완성되는 무한한 생성형 3D 시뮬레이터",
            "points": [
                "단일 사진으로 세계 창조: 스마트폰으로 찍은 서울 거리 사진 한 장을 넣으면 3초 만에 걸어 다닐 수 있는 3D 세계 완성",
                "물리 법칙 내재화: 강체 충돌 반발력, 유체 역학적 물보라, 광선 추적 조명 반사를 신경망이 자체 연산",
                "3D 그래픽 노가다의 종말: 수작업 폴리곤 모델링이나 리깅 없이 순수 뉴럴 가중치로 시뮬레이션 완결"
            ],
            "tips": "사라 조교가 3D 그래픽스 업계의 패러다임 전환을 사진 한 장의 세계 생성 시연과 함께 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Zero-Shot World Genesis",
                "def": "Instantiating fully navigable 3D physics environments from a single 2D image prompt without manual asset authoring.",
                "defKo": "제로샷 3D 세계 생성"
            },
            {
                "term": "Neural Physics Simulation",
                "def": "Predicting physical dynamics and kinematics directly through trained transformer representations rather than classical physics solvers.",
                "defKo": "신경망 물리 시뮬레이션"
            }
        ]
    },
    # Slide 5: The 3-Phase Interactive Pipeline: Sketch, Explore, Remix
    {
        "num": 5,
        "type": "content",
        "title": "THE 3-PHASE PIPELINE: SKETCH, EXPLORE, REMIX",
        "subtitle": "The standardized authoring workflow for virtual classrooms, robotic trials, and urban design",
        "points": [
            "Phase 1: SKETCH (Provide prompt, 2D napkin sketch, or satellite map bounding box).",
            "Phase 2: EXPLORE (Drive agents or avatars through the generated world at 60 FPS).",
            "Phase 3: REMIX (Inject real-time dynamic prompt events: 'Trigger sudden blizzard and black ice')."
        ],
        "script": (
            "[TA Sarah] Slide 5 outlines \"THE 3-PHASE INTERACTIVE PIPELINE: SKETCH, EXPLORE, REMIX.\"\n\n"
            "[TA James] Step 1 is SKETCH: You input a prompt or satellite coordinate. Step 2 is EXPLORE: Your AI autonomous agents navigate the terrain at 60 frames per second!\n\n"
            "[Prof. Peter] Step 3 is REMIX: While the agent is driving, you type: 'Trigger a blinding blizzard with falling power lines!' Genie 3 recalculates the atmospheric rendering and tire friction in 100 milliseconds!\n\n"
            "[TA Sarah] Let us inspect the 280-billion-image Google Street View data moat on Slide 6."
        ),
        "koreanGuide": {
            "summary": "3단계 대화형 파이프라인: 스케치(Sketch), 탐험(Explore), 리믹스(Remix)",
            "points": [
                "1단계 SKETCH: 냅킨 스케치, 텍스트 프롬프트, 위성 GPS 좌표로 기본 지형 생성",
                "2단계 EXPLORE: 60 FPS 고속 렌더링으로 에이전트와 아바타가 실시간 주행 및 탐험",
                "3단계 REMIX: 실시간 프롬프트 이벤트 주입 ('갑작스러운 눈보라와 전신주 붕괴 유발') ➔ 0.1초 만에 물리 재계산"
            ],
            "tips": "제임스 조교와 피터 교수가 실시간 돌발 상황을 주입하는 'REMIX' 기능의 박진감을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Dynamic Prompt Event",
                "def": "Injecting real-time semantic instructions into an active simulation to mutate physical parameters and environmental hazards.",
                "defKo": "동적 실시간 프롬프트 이벤트"
            },
            {
                "term": "Sub-100ms Physics Recalculation",
                "def": "Updating environmental lighting, friction, and fluid mechanics within milliseconds of a control prompt.",
                "defKo": "0.1초 미만 초고속 물리 재계산"
            }
        ]
    },
    # Slide 6: 20 Years of Street View: 280 Billion Image Data Moat
    {
        "num": 6,
        "type": "content",
        "title": "20 YEARS OF STREET VIEW: 280B IMAGE DATA MOAT",
        "subtitle": "Why Google possesses an insurmountable competitive monopoly in real-world spatial training",
        "points": [
            "The 280B Moat: 20 years of Street View cars driving 100+ countries, capturing multi-angle photogrammetry.",
            "Complete Terrestrial Grounding: Real-world GPS, elevation maps, sun angles, and road surface textures.",
            "Synthetic Generalization: Transforming real New York streets into cyberpunk cities or post-apocalyptic terrain effortlessly."
        ],
        "script": (
            "[Prof. Peter] Slide 6 explains Google's unfair advantage: \"20 YEARS OF STREET VIEW: THE 280-BILLION IMAGE DATA MOAT.\"\n\n"
            "[TA Sarah] Why can no other tech company easily replicate Genie 3? Because for 20 years, Google Street View cars have driven billions of miles across 100 countries, capturing over 280 billion high-resolution 360-degree images!\n\n"
            "[TA James] That data moat contains every real-world intersection, asphalt texture, sun angle, and traffic sign on Earth! Genie 3 was trained on the real physical planet!\n\n"
            "[Prof. Peter] Let us compare Game Engines vs. Generative World Models on Slide 7."
        ),
        "koreanGuide": {
            "summary": "20년간 축적된 구글 스트리트뷰: 2,800억 장의 난공불락 데이터 해자",
            "points": [
                "2,800억 장의 독점 데이터: 20년간 100개국 도로를 누빈 스트리트뷰의 전방위 360도 공간 데이터",
                "지구 표면의 완전한 접지: 실제 GPS, 고도 데이터, 태양 고도각, 아스팔트 노면 텍스처를 전수 학습",
                "합성 일반화: 실제 뉴욕 거리를 사이버펑크 도시나 극한 설산 지형으로 자유자재로 변환"
            ],
            "tips": "사라 조교와 제임스 조교가 20년간 축적된 스트리트뷰 데이터가 왜 타사가 넘볼 수 없는 해자인지 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Terrestrial Data Moat",
                "def": "An insurmountable proprietary dataset of real-world physical imagery, GPS coordinates, and spatial geometry.",
                "defKo": "지구 공간 데이터 해자"
            },
            {
                "term": "Multi-Angle Photogrammetry",
                "def": "Extracting 3D geometric structures and depth maps from overlapping multi-view 2D photographic arrays.",
                "defKo": "다각도 사진 측량 기법"
            }
        ]
    },
    # Slide 7: Game Engines (Unreal) vs. Generative World Models
    {
        "num": 7,
        "type": "comparison",
        "title": "GAME ENGINES VS. GENERATIVE WORLD MODELS",
        "subtitle": "Comparing hand-crafted 3D polygons (Unreal Engine 5) with neural generative physical simulation",
        "leftCard": {
            "tag": "GAME ENGINES (UNREAL 5)",
            "title": "Hand-Crafted Polygon Mesh",
            "points": [
                "Requires 50 3D artists & $20M budget.",
                "Takes 2 years to build a virtual city.",
                "Rigid deterministic rules & physics bugs.",
                "Limited to pre-built assets and boundaries."
            ]
        },
        "rightCard": {
            "tag": "WORLD MODELS (GENIE 3)",
            "title": "Neural Generative Simulation",
            "points": [
                "Requires 1 prompt or photo; 0 artists.",
                "Generates infinite variations in 3 seconds.",
                "Learned physical intuition (gravity, friction).",
                "Boundless procedural exploration."
            ]
        },
        "script": (
            "[TA Sarah] Slide 7 contrasts \"GAME ENGINES (UNREAL 5) VS. GENERATIVE WORLD MODELS (GENIE 3).\"\n\n"
            "[TA James] Look at the economics: Building a virtual city in Unreal Engine 5 takes 50 3D artists, 2 years of manual polygon modeling, and 20 million dollars! In Genie 3, you type a prompt or give a GPS coordinate, and an infinite photorealistic world generates in 3 seconds!\n\n"
            "[Prof. Peter] It shatters the economic barrier of 3D simulation forever.\n\n"
            "[TA Sarah] Let us inspect the VMC Architecture on Slide 8."
        ),
        "koreanGuide": {
            "summary": "전통 게임 엔진(Unreal 5) vs 생성형 월드 모델(Genie 3) 비교",
            "points": [
                "언리얼 엔진 5: 3D 아티스트 50명, 2년의 제작 기간, 2,000만 달러 비용이 드는 수작업 폴리곤 방식",
                "지니 3 월드 모델: 프롬프트 하나로 3초 만에 무한한 실시간 3D 가상 세계 절차적 생성",
                "3D 시뮬레이션 제작 비용의 99.9% 절감과 무한한 시나리오 탐색 가능성"
            ],
            "tips": "제임스 조교가 2천만 달러 수작업 모델링과 3초 신경망 생성의 압도적 경제성을 비교합니다."
        },
        "keyTerms": [
            {
                "term": "Procedural Neural World Generation",
                "def": "The continuous on-the-fly synthesis of 3D visual environments driven by deep generative models.",
                "defKo": "신경망 기반 절차적 세계 생성"
            },
            {
                "term": "Polygon Mesh Economics",
                "def": "The heavy capital and labor costs traditionally required to manually model, texture, and rig 3D virtual environments.",
                "defKo": "폴리곤 수작업 제작 비용 한계"
            }
        ]
    },
    # Slide 8: The VMC Architecture: Vision, Memory, Controller
    {
        "num": 8,
        "type": "content",
        "title": "THE VMC ARCHITECTURE: VISION, MEMORY, CONTROLLER",
        "subtitle": "The tripartite neural engine governing real-time spatial simulation",
        "points": [
            "Vision Module: Encodes 2D video frames into compact 3D spatial latent representations.",
            "Memory Module: Maintains long-term temporal consistency across minutes of navigation (preventing world morphing).",
            "Controller Module: Maps keyboard, steering wheel, and agent velocity actions into next-latent state transitions."
        ],
        "script": (
            "[Prof. Peter] Slide 8 diagrams \"THE VMC ARCHITECTURE: VISION, MEMORY, CONTROLLER.\"\n\n"
            "[TA Sarah] Under the hood, Genie 3 operates as a Tripartite Engine: First, the Vision Module encodes pixels into 3D spatial latent vectors. Second, the Memory Module stores previous street corners in a long-term memory buffer so the building doesn't morph when you turn around!\n\n"
            "[TA James] Third, the Controller Module maps agent steering inputs into the exact mathematical transition to the next physical state!\n\n"
            "[Prof. Peter] Let us inspect Spatio-Temporal Tokenizers on Slide 10."
        ),
        "koreanGuide": {
            "summary": "VMC 아키텍처: 비전(Vision), 메모리(Memory), 컨트롤러(Controller)",
            "points": [
                "비전(Vision) 모듈: 2D 픽셀을 3차원 공간 잠재 벡터로 고속 압축 인코딩",
                "메모리(Memory) 모듈: 뒤돌아보았을 때 건물이 왜곡되거나 사라지지 않도록 시공간 일관성 영구 유지",
                "컨트롤러(Controller) 모듈: 스티어링 휠 및 속도 입력을 다음 잠재 상태 전이 행렬로 즉시 매핑"
            ],
            "tips": "사라 조교와 제임스 조교가 3대 모듈의 유기적 결합으로 세계의 항상성(Consistency)이 유지되는 원리를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "VMC Architecture",
                "def": "The foundational world model design integrating Vision encoding, Memory persistence, and Action Controller dynamics.",
                "defKo": "VMC 아키텍처 (비전-메모리-컨트롤러)"
            },
            {
                "term": "World Morphing Prevention",
                "def": "The architectural property ensuring previously observed landmarks remain geometrically stable when revisited.",
                "defKo": "가상 세계 기하 왜곡 방지"
            }
        ]
    },
    # Slide 9: Unified Transformer: Latent Synchronization
    {
        "num": 9,
        "type": "content",
        "title": "THE UNIFIED TRANSFORMER: LATENT SYNCHRONIZATION",
        "subtitle": "Cross-attending visual patches, audio acoustic reflections, and physical control tokens",
        "points": [
            "Multimodal Latent Fusion: Fusing camera pixels, LiDAR depth point clouds, and motor torque signals.",
            "Cross-Attention Synchronization: Aligning audio echoes with room geometry in real-time acoustic space.",
            "Unified Spatio-Temporal Latent: A single tensor describing the complete physical state of the universe."
        ],
        "script": (
            "[TA Sarah] Slide 9 explores \"THE UNIFIED TRANSFORMER: LATENT SYNCHRONIZATION.\"\n\n"
            "[TA James] Genie 3 does not just simulate visual pixels; it synchronizes multimodal physics! It fuses camera visuals, LiDAR point clouds, motor torque, and even spatial 3D audio echoes in a single Unified Transformer tensor!\n\n"
            "[Prof. Peter] If you enter a virtual concrete tunnel, the engine automatically simulates the acoustic reverb of your vehicle's engine!\n\n"
            "[TA Sarah] Let us inspect Part 1 transition on Slide 10."
        ),
        "koreanGuide": {
            "summary": "통합 트랜스포머: 다중 모달 잠재 공간 동기화 및 3D 공간 음향 연동",
            "points": [
                "다중 모달 융합: 카메라 픽셀, 라이다(LiDAR) 포인트 클라우드, 모터 토크 신호를 단일 텐서로 통합",
                "시공간 교차 어텐션: 방의 기하학적 구조에 맞춰 3D 공간 음향 잔향(Reverb)을 실시간 합성",
                "완전한 물리 세계 상태를 단일 잠재 텐서(Unified Latent Tensor)로 완벽히 기술"
            ],
            "tips": "제임스 조교가 시각뿐만 아니라 3D 공간 음향까지 함께 시뮬레이션되는 통합 트랜스포머의 위력을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Unified Spatio-Temporal Transformer",
                "def": "A deep neural architecture cross-attending across visual, acoustic, and physical control modalities.",
                "defKo": "통합 시공간 트랜스포머"
            },
            {
                "term": "Spatial Acoustic Synthesis",
                "def": "Simulating environmental sound reflection and Doppler effects matching real-time 3D geometry.",
                "defKo": "3D 공간 음향 물리 합성"
            }
        ]
    },
    # Slide 10: Part 1 Transition: Physical Realism & Hardware
    {
        "num": 10,
        "type": "content",
        "title": "PART 1 TRANSITION: ENTERING PHYSICAL REALISM",
        "subtitle": "Connecting simulation theory to TPU v8 optical hardware, 60 FPS WebGL, and Waymo training",
        "points": [
            "From Pixels to Physics: How does Genie 3 maintain 60 FPS interactive latency on web browsers?",
            "Hardware Foundation: Google TPU v8 and Boardfly optical fiber interconnects powering parallel clusters.",
            "The Roadmap Ahead: Master Physical Realism in Part 2, Waymo Training in Part 3, and Governance in Part 4."
        ],
        "script": (
            "[Prof. Peter] Slide 10 bridges our roadmap: \"PART 1 TRANSITION: ENTERING PHYSICAL REALISM.\"\n\n"
            "[TA Sarah] We understand the architecture. But how does Genie 3 render high-definition 3D worlds at 60 frames per second over a standard web browser without lagging?\n\n"
            "[TA James] In Part 2, we inspect the TPU v8 hardware backbone, Boardfly optical interconnects, spatio-temporal patching, and real-time WebGL streaming!\n\n"
            "[Prof. Peter] Let us examine our first enterprise case study on Slide 11!"
        ),
        "koreanGuide": {
            "summary": "Part 1 전환: 물리적 사실성과 TPU v8 하드웨어 인프라 진입",
            "points": [
                "픽셀에서 물리로: 웹 브라우저에서 렉 없이 60 FPS 실시간 3D 시뮬레이션을 돌리는 비결",
                "TPU v8 및 Boardfly 광통신 인터커넥트 하드웨어 기반의 초병렬 분산 클러스터",
                "Part 2~4 로드맵 제시: 물리적 사실성 ➔ 웨이모 가상 훈련 ➔ 거버넌스 및 실습 12"
            ],
            "tips": "제임스 조교가 60 FPS 웹 스트리밍을 지탱하는 TPU v8 광통신 하드웨어의 위력을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "60 FPS Interactive Latency",
                "def": "Generating and streaming novel 3D neural frames within a strict 16.6ms per-frame budget.",
                "defKo": "60 FPS 실시간 상호작용 지연 한계"
            },
            {
                "term": "Optical Interconnect Mesh",
                "def": "Ultra-high-bandwidth optical fiber networking synchronizing thousands of TPU accelerators with sub-microsecond latency.",
                "defKo": "광통신 인터커넥트 분산망"
            }
        ]
    },
    # Slide 11: Case Study 1: Waymo Autonomous Fleet Zero-Fatalities Training
    {
        "num": 11,
        "type": "casestudy",
        "title": "CASE STUDY 1: WAYMO FLEET 500M-MILE TRAINING",
        "subtitle": "Waymo trains autonomous fleet on 500 million virtual Genie 3 miles, achieving zero physical fatalities",
        "company": "Waymo LLC (Alphabet Self-Driving Division)",
        "problem": "Physical road testing of rare edge cases (e.g., a mattress flying off a truck in heavy fog on black ice) is dangerous, illegal, and statistically rare (1 in 10 million miles).",
        "solution": "Generated 500 million miles of extreme edge-case simulation in Genie 3; 10,000 virtual Waymo vehicles tested concurrently across hazardous weather.",
        "impact": "Waymo achieved 100M+ real-world commercial rider miles with zero fatal collisions (85% lower injury rate than human drivers); saved $1.2B in physical crash testing.",
        "script": (
            "[Prof. Peter] Slide 11 presents \"CASE STUDY 1: WAYMO FLEET 500-MILLION-MILE TRAINING.\"\n\n"
            "[TA Sarah] How do you train a self-driving car for rare, deadly hazards—like a mattress flying off a pickup truck into heavy fog on an icy highway? You cannot ethically stage that crash on real public roads with human drivers!\n\n"
            "[TA James] Waymo generated 500 million miles of extreme hazardous driving scenarios inside Genie 3! 10,000 virtual Waymo AI drivers ran through millions of blizzards, flash floods, and sudden pedestrian jaywalkers simultaneously!\n\n"
            "[Prof. Peter] When deployed to real-world streets in Phoenix, San Francisco, and Los Angeles, Waymo achieved over 100 million commercial rider miles with zero fatal collisions—an 85% reduction in injury crashes compared to human drivers, saving 1.2 billion dollars in testing costs!\n\n"
            "[TA Sarah] That proves the life-saving power of World Models.\n\n"
            "[TA James] Now let us open Part 2 and look Under the Hood of Physical Realism on Slide 12!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 1: 웨이모 5억 마일 지니 3 가상 주행 훈련과 사망 사고 0건 달성",
            "points": [
                "문제 상황: 짙은 안갯속 빙판길에서 트럭 매트리스가 날아오는 등의 치명적 엣지 케이스는 실제 도로 실험 불가",
                "솔루션: 지니 3 월드 모델 내에서 5억 마일 분량의 극한 기상 및 돌발 사고 시나리오 생성 ➔ 10,000대 차량 동시 가상 훈련",
                "성과: 실제 도로 1억 마일 상용 주행 중 사망 사고 0건, 인간 운전자 대비 부상 사고 85% 급감, 12억 달러 테스트 비용 절감"
            ],
            "tips": "사라 조교와 제임스 조교가 가상 시뮬레이션 훈련이 실제 도로에서 인명을 구한 압도적 성과를 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Edge-Case Synthesis",
                "def": "Generating statistically rare and physically hazardous driving situations within a safe virtual world model.",
                "defKo": "극한 엣지 케이스 합성 생성"
            },
            {
                "term": "Zero-Fatality Fleet Validation",
                "def": "Achieving flawless passenger safety records by stress-testing autonomous perception systems across billions of simulated miles.",
                "defKo": "무사망 자율주행 안전 검증"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 12: Part 2 Section Divider
    {
        "num": 12,
        "type": "section",
        "title": "PART 2: UNDER THE HOOD OF PHYSICAL REALISM",
        "subtitle": "Spatio-temporal patching, WebGL 60 FPS streaming, real-time physics events, and TPU v8 hardware",
        "script": (
            "[TA Sarah] Look at Slide 12: \"PART 2: UNDER THE HOOD OF PHYSICAL REALISM.\" Now we inspect the deep engineering mechanics!\n\n"
            "[Prof. Peter] Simulating a physically believable universe requires mastery across multiple layers: tensor decomposition, spatio-temporal video patching, low-latency WebGL shaders, and high-density TPU acceleration.\n\n"
            "[TA James] In Part 2, we explore spatio-temporal patch tokenizers, real-time 0.1s prompt event recalculations, maps imagery grounding, and green TPU v8 architectures!\n\n"
            "[TA Sarah] Let us inspect spatio-temporal patching on Slide 13!"
        ),
        "koreanGuide": {
            "summary": "Part 2 섹션 전환: 물리적 사실성과 시공간 렌더링 파이프라인",
            "points": [
                "물리적 세계 시뮬레이션의 공학적 과제: 텐서 분해, 시공간 패치 토큰화, WebGL 셰이더, TPU 하드웨어",
                "2D 비디오에서 3D 잠재 메쉬로의 실시간 변환과 0.1초 물리 재계산",
                "TPU v8 그린 아키텍처와 시뮬레이션 클러스터 안전성"
            ],
            "tips": "피터 교수가 다층적 엔지니어링의 정수를 선언하고 제임스가 시공간 토크나이저를 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Spatio-Temporal Patching",
                "def": "Decomposing 3D video volumes into discrete spatio-temporal cubic tokens for transformer processing.",
                "defKo": "시공간 3D 패치 토큰화"
            },
            {
                "term": "Physical Realism Invariant",
                "def": "The structural requirement that simulated entity interactions must conserve momentum, mass, and energy.",
                "defKo": "물리적 사실성 불변 법칙"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 13: Spatio-Temporal Patching: 2D Video to 3D Latent Mesh
    {
        "num": 13,
        "type": "content",
        "title": "SPATIO-TEMPORAL PATCHING: 2D TO 3D",
        "subtitle": "Converting flat video sequences into continuous 3D volume latent meshes",
        "points": [
            "Cubic Tokenization: Slicing video into $16 \\times 16 \\times 4$ pixel-frame cubes (space + time).",
            "Depth Extrusion: Predicting dense depth maps for every surface to construct an internal neural radiance field.",
            "Volumetric Consistency: Ensuring that shadows and light occlusions calculate correctly across 3D perspective shifts."
        ],
        "script": (
            "[Prof. Peter] Slide 13 diagrams \"SPATIO-TEMPORAL PATCHING: 2D VIDEO TO 3D LATENT MESH.\"\n\n"
            "[TA Sarah] How does Genie 3 understand 3D space from flat video? It slices video streams into $16 \\times 16 \\times 4$ pixel-frame cubes—capturing both spatial width/height and temporal movement in a single token!\n\n"
            "[TA James] It extrudes dense depth maps in real time, building an internal Neural Radiance Field! When your camera pans, the perspective and shadows shift with absolute optical accuracy!\n\n"
            "[Prof. Peter] Let us inspect the 60 FPS WebGL streaming engine on Slide 14."
        ),
        "koreanGuide": {
            "summary": "시공간 패칭: 2D 비디오에서 3D 연속 잠재 메쉬로의 실시간 변환",
            "points": [
                "입방체 토큰화: 비디오를 16x16x4 픽셀-프레임 큐브로 분할하여 공간과 시간 변화를 동시 포착",
                "실시간 뎁스 추출: 모든 표면의 조밀한 깊이 맵을 예측해 내부 뉴럴 래디언스 필드(NeRF) 구성",
                "시점 이동에 따른 완벽한 광학적 그림자 차폐 및 투시 원근법 계산"
            ],
            "tips": "사라 조교와 제임스 조교가 시공간 3D 큐브 토큰화의 기하학적 원리를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Cubic Tokenizer",
                "def": "A vision transformer tokenizer extracting 3D tensor patches spanning both spatial area and temporal duration.",
                "defKo": "입방체 시공간 토크나이저"
            },
            {
                "term": "Neural Radiance Field (NeRF)",
                "def": "A continuous volumetric representation of a 3D scene parameterized by a deep neural network.",
                "defKo": "뉴럴 래디언스 필드 (NeRF)"
            }
        ]
    },
    # Slide 14: WebGL Engine: 60 FPS Simulation on Thin Clients
    {
        "num": 14,
        "type": "content",
        "title": "WEBGL ENGINE: 60 FPS ON THIN CLIENTS",
        "subtitle": "Streaming high-fidelity neural worlds to Chromebooks and mobile devices via WebGL shaders",
        "points": [
            "Thin-Client Architecture: Heavy neural inference runs on cloud TPU clusters; lightweight WebGL decodes latent streams locally.",
            "Sub-16ms Frame Budget: Delivering butter-smooth 60 FPS video with zero input stutter on low-cost hardware.",
            "Universal Accessibility: Any student or engineer can explore interactive worlds directly inside Chrome tabs."
        ],
        "script": (
            "[TA Sarah] Slide 14 covers \"THE WEBGL STREAMING ENGINE: 60 FPS ON THIN CLIENTS.\"\n\n"
            "[TA James] You don't need a $5,000 gaming rig with liquid cooling! The heavy TPU clusters calculate the world in the cloud, and stream compressed latent tensors to a lightweight WebGL shader running inside your standard Chrome tab at 60 FPS!\n\n"
            "[Prof. Peter] A student with a $200 Chromebook can explore a photorealistic simulation of ancient Rome or Mars with zero lag!\n\n"
            "[TA Sarah] Let us inspect Real-Time Prompt Events on Slide 15."
        ),
        "koreanGuide": {
            "summary": "WebGL 엔진: 저가형 크롬북에서도 버벅임 없는 60 FPS 실시간 스트리밍",
            "points": [
                "씬 클라이언트(Thin-Client) 구조: 무거운 신경망 추론은 클라우드 TPU 클러스터가, 로컬 브라우저는 WebGL 셰이더로 디코딩",
                "16.6ms 프레임 예산: 저사양 기기에서도 60 FPS의 매끄러운 반응형 화면 렌더링 유지",
                "200달러짜리 크롬북으로도 고화질 화성 탐사나 고대 로마 3D 시뮬레이션을 완벽 구동"
            ],
            "tips": "제임스 조교가 200달러 크롬북으로 즐기는 고화질 시뮬레이션의 대중화 혁신을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "WebGL Latent Shader",
                "def": "A client-side GPU shader program decoding compressed neural world latent streams into visual display pixels.",
                "defKo": "WebGL 잠재 공간 디코딩 셰이더"
            },
            {
                "term": "Thin-Client Simulation",
                "def": "Offloading heavy computational physics to cloud clusters while rendering responsive interactive views on lightweight clients.",
                "defKo": "씬 클라이언트 기반 시뮬레이션"
            }
        ]
    },
    # Slide 15: Real-Time Prompt Events: 0.1s Physics Recalculation
    {
        "num": 15,
        "type": "content",
        "title": "REAL-TIME PROMPT EVENTS: 0.1S RECALCULATION",
        "subtitle": "Dynamically mutating environmental physics on-the-fly via natural language commands",
        "points": [
            "Instant Environmental Mutation: Typing 'Earthquake magnitude 7.2' instantly shakes buildings and cracks asphalt.",
            "Sub-100ms Latency: Latent diffusion weights update friction coefficients, lighting vectors, and particle emitters in 0.1 seconds.",
            "Stress-Testing Autonomous Policies: Forcing driving agents to react instantly to unexpected fallen trees and mudslides."
        ],
        "script": (
            "[Prof. Peter] Slide 15 explores \"REAL-TIME PROMPT EVENTS: 0.1S PHYSICS RECALCULATION.\"\n\n"
            "[TA Sarah] Imagine you are evaluating a disaster relief robot navigating a mountain road. While the simulation is running, you type: 'Flash flood! River breaches the bank!'\n\n"
            "[TA James] In 0.1 seconds, Genie 3 recalculates the water physics: churning muddy water rushes across the road, reducing tire friction to near zero! The autonomous robot must immediately calculate an emergency escape maneuver!\n\n"
            "[Prof. Peter] That is how we forge unbreakable autonomous policies.\n\n"
            "[TA Sarah] Let us inspect Hardware Backbone: TPU v8 on Slide 18."
        ),
        "koreanGuide": {
            "summary": "실시간 프롬프트 이벤트: 0.1초 만에 돌발 물리 환경 재계산",
            "points": [
                "실시간 환경 변이: 주행 중 '규모 7.2 지진 발생'을 입력하면 건물이 흔들리고 도로가 즉시 갈라짐",
                "0.1초 초고속 갱신: 잠재 확산 가중치가 마찰 계수, 조명 벡터, 입자 물리 효과를 100ms 내에 재계산",
                "자율주행 및 재난 로봇의 위기 대응 제어 알고리즘을 극한으로 스트레스 테스트"
            ],
            "tips": "사라 조교와 제임스 조교가 0.1초 만에 도로가 강물로 변하는 실시간 물리 변이의 박진감을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Environmental Mutation Latency",
                "def": "The time required for a generative simulation engine to recompute physical dynamics following a natural language prompt.",
                "defKo": "환경 변이 처리 지연 시간"
            },
            {
                "term": "Friction Coefficient Recalculation",
                "def": "Dynamically adjusting contact mechanics and traction matrices in response to simulated mud, ice, or water hazards.",
                "defKo": "동적 마찰 계수 재계산"
            }
        ]
    },
    # Slide 16: Hardware Backbone: TPU v8, Boardfly & Fiber Grid
    {
        "num": 16,
        "type": "content",
        "title": "HARDWARE BACKBONE: TPU V8 & FIBER GRID",
        "subtitle": "Google's optical supercomputer clusters delivering exaflop-scale simulation throughput",
        "points": [
            "TPU v8 Compute Pods: 10,000 liquid-cooled TPU accelerators interconnected by Boardfly optical circuit switches.",
            "Sub-Microsecond Latency: Optical circuit switches route inter-chip tensors with zero electronic conversion bottleneck.",
            "Exaflop Supercomputing: Delivering 10 exaflops of dedicated neural simulation capacity per cluster."
        ],
        "script": (
            "[TA Sarah] Slide 16 reveals the physical beast: \"HARDWARE BACKBONE: TPU V8 & FIBER GRID.\"\n\n"
            "[TA James] What powers this massive simulation? Google's TPU v8 supercomputing pods! 10,000 liquid-cooled TPU chips interconnected by Boardfly optical circuit switches—transmitting petabytes of tensor data via pure light beams!\n\n"
            "[Prof. Peter] It delivers 10 exaflops of computational power with sub-microsecond latency, allowing 10,000 Waymo vehicles to inhabit the same virtual world simultaneously!\n\n"
            "[TA Sarah] Let us inspect TPU v8 green architecture on Slide 17."
        ),
        "koreanGuide": {
            "summary": "하드웨어 백본: TPU v8과 Boardfly 광통신 그리드 슈퍼컴퓨터",
            "points": [
                "TPU v8 컴퓨팅 파드: 10,000개의 수랭식 TPU 칩이 Boardfly 광학 회로 스위치(OCS)로 직결",
                "마이크로초 미만 초저지연: 빛의 속도로 칩 간 텐서 데이터를 전송하여 전자식 변환 병목 완전 해소",
                "클러스터당 10 엑사플롭스(Exaflops)의 압도적 연산력으로 10,000대 차량의 동시 시뮬레이션 지원"
            ],
            "tips": "제임스 조교가 순수 빛(광통신)으로 10,000개 칩을 묶은 광학 슈퍼컴퓨터의 경이로움을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Boardfly Optical Circuit Switch (OCS)",
                "def": "Google's proprietary optical switching hardware reconfiguring inter-chip fiber connections without electronic packet conversion.",
                "defKo": "Boardfly 광학 회로 스위치 (OCS)"
            },
            {
                "term": "Exaflop Simulation Pod",
                "def": "A supercomputing cluster capable of executing $10^{18}$ floating-point operations per second for physics simulation.",
                "defKo": "엑사플롭스 시뮬레이션 파드"
            }
        ]
    },
    # Slide 17: TPU v8 Green Architecture: 3X Power Efficiency
    {
        "num": 17,
        "type": "content",
        "title": "TPU V8 GREEN ARCHITECTURE: 3X EFFICIENCY",
        "subtitle": "Sustainable simulation scaling with 3X lower carbon footprint in 100% renewable data centers",
        "points": [
            "3X Energy Efficiency: TPU v8 achieves 3 times higher simulation frames per kilowatt-hour than legacy GPU rigs.",
            "Liquid Cooling: Direct-to-chip water cooling eliminates power-hungry air conditioning fans.",
            "Creation Care: Massive world simulation scaled responsibly to protect God's planetary ecosystem."
        ],
        "script": (
            "[Prof. Peter] Slide 17 highlights \"TPU V8 GREEN ARCHITECTURE: 3X POWER EFFICIENCY.\"\n\n"
            "[TA Sarah] When scaling 500 million miles of virtual testing, electricity consumption is a moral issue! TPU v8 delivers 3 times more simulation frames per kilowatt-hour than traditional GPU servers!\n\n"
            "[TA James] With direct-to-chip liquid cooling and 100% renewable geothermal/solar grids, we train autonomous intelligence while faithfully caring for God's created Earth!\n\n"
            "[Prof. Peter] Let us examine our second enterprise case study on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "TPU v8 친환경 아키텍처: 3배 전력 효율과 탄소 배출 제로 실천",
            "points": [
                "3배 높은 에너지 효율: 기존 GPU 랙 대비 킬로와트시당 3배 많은 시뮬레이션 프레임 렌더링",
                "직접 수랭식 냉각: 칩에 직접 냉각수를 순환시켜 전력 소모가 극심한 에어컨 팬 완전 배제",
                "창조 세계 돌봄(Creation Care): 대규모 자율주행 훈련을 돌리면서도 지구 생태계를 거룩하게 보존"
            ],
            "tips": "피터 교수가 고성능 시뮬레이션과 친환경 창조 세계 보존의 신학적 조화를 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Direct-to-Chip Liquid Cooling",
                "def": "Thermal management circulating chilled liquid directly over processor dies to minimize cooling energy overhead.",
                "defKo": "칩 직결 수랭식 냉각"
            },
            {
                "term": "Carbon-Neutral Simulation",
                "def": "Running high-density AI simulations exclusively in data centers matched 100% by renewable energy generation.",
                "defKo": "탄소 중립 가상 시뮬레이션"
            }
        ]
    },
    # Slide 18: Part 2 Transition: Entering Waymo & Swarm Trials
    {
        "num": 18,
        "type": "content",
        "title": "PART 2 TRANSITION: ENTERING WAYMO & SWARM TRIALS",
        "subtitle": "Connecting hardware and physics to 10,000-agent swarm testing, crash forensics, and robotics",
        "points": [
            "From Engine to Fleet: How does Waymo deploy 10,000 autonomous vehicle agents into Genie 3 in parallel?",
            "Swarm Testing Protocols: Multi-perspective synthesis, collision forensics, and Ed25519 crash receipts.",
            "The Roadmap Ahead: Master Waymo Swarms in Part 3, and Strategic Governance in Part 4."
        ],
        "script": (
            "[Prof. Peter] Slide 18 transitions our roadmap: \"PART 2 TRANSITION: ENTERING WAYMO & SWARM TRIALS.\"\n\n"
            "[TA Sarah] Now, how does an enterprise autonomous vehicle fleet actually use Genie 3? Through the 'Infinite Safe Classroom'!\n\n"
            "[TA James] In Part 3, we explore 10,000-agent parallel swarm testing, multi-perspective synthesis, Human-on-the-Loop veto gates, and Ed25519 cryptographic crash audit receipts!\n\n"
            "[Prof. Peter] Let us examine our second enterprise case study on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "Part 2 전환: 웨이모 가상 교실과 1만 대 스웜 주행 시험 진입",
            "points": [
                "엔진에서 군단으로: 10,000대의 자율주행 에이전트를 지니 3 가상 세계에 동시 투입하는 방법",
                "스웜 테스트 프로토콜: 다관점 합성, 충돌 사고 포렌식, Ed25519 암호화 주행 영수증",
                "Part 3~4 로드맵 제시: 웨이모 가상 훈련 해부 ➔ 전략적 거버넌스 ➔ 실습 12"
            ],
            "tips": "제임스 조교가 10,000대 차량 동시 가상 주행 시험의 스케일을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Infinite Safe Classroom",
                "def": "The concept of training autonomous agents across millions of simulated hazard miles with zero physical danger.",
                "defKo": "무한 안전 가상 교실 (Waymo Virtual Classroom)"
            },
            {
                "term": "Parallel Swarm Simulation",
                "def": "Simultaneously running thousands of independent agent policy instances within synchronized world models.",
                "defKo": "초병렬 스웜 가상 시뮬레이션"
            }
        ]
    },
    # Slide 19: Waymo's Virtual Driving School on Genie 3
    {
        "num": 19,
        "type": "content",
        "title": "WAYMO'S VIRTUAL DRIVING SCHOOL",
        "subtitle": "Generating 100,000 dangerous traffic variations daily with zero physical repair costs",
        "points": [
            "The Problem: A human student driver drives 50 miles before taking a license test. Waymo drives 500 million miles.",
            "Procedural Hazard Generation: Genie 3 generates sudden lane-cutting taxis, hidden potholes, and blinding glare.",
            "Zero Physical Damage: If an agent makes a mistake and collides, it incurs 0 dollars in damage and learns in 1 millisecond."
        ],
        "script": (
            "[Prof. Peter] Slide 19 diagrams \"WAYMO'S VIRTUAL DRIVING SCHOOL ON GENIE 3.\"\n\n"
            "[TA Sarah] A human teenager practices driving for 50 hours before getting a license. Waymo's autonomous driver software trains for 500 million miles inside Genie 3 across 100,000 unique hazard variations every single day!\n\n"
            "[TA James] If a virtual car hits a guardrail in simulation, zero humans are injured, zero metal is bent, and the neural policy updates in 1 millisecond! The agent never repeats the same mistake twice!\n\n"
            "[Prof. Peter] Let us inspect extreme weather simulation on Slide 20."
        ),
        "koreanGuide": {
            "summary": "웨이모 가상 운전 학교: 일일 10만 건의 돌발 위험 상황 무인 훈련",
            "points": [
                "5억 마일의 압도적 수련: 인간이 50시간 연습할 때 웨이모 소프트웨어는 5억 마일의 극한 상황 훈련 완결",
                "절차적 위험 생성: 끼어드는 택시, 보이지 않는 싱크홀, 역광 눈부심을 매일 10만 가지 변형으로 주입",
                "수리비 0원과 즉각 피드백: 가상 충돌 시 0원의 비용으로 1밀리초 만에 정책 신경망을 완벽 보정"
            ],
            "tips": "사라 조교와 제임스 조교가 수리비 0원으로 극한의 충돌 훈련을 소화하는 가상 운전 학교의 위력을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Procedural Hazard Injection",
                "def": "The automated insertion of randomized, high-risk physical obstacles into ongoing simulation tracks.",
                "defKo": "절차적 돌발 위험 주입"
            },
            {
                "term": "Zero-Cost Collision Learning",
                "def": "Updating agent neural driving weights from simulated crashes without financial or physical vehicle damage.",
                "defKo": "무비용 충돌 피드백 학습"
            }
        ]
    },
    # Slide 20: Simulating Extreme Weather: Hardening Edge-Cases
    {
        "num": 20,
        "type": "content",
        "title": "SIMULATING EXTREME WEATHER: HARDENING EDGE-CASES",
        "subtitle": "Generating torrential rain, blinding dust storms, and black ice conditions deterministically",
        "points": [
            "Sensor Degradation Modeling: Simulating water droplets on camera lenses and LiDAR noise in dense blizzards.",
            "Traction Loss Simulation: Accurately calculating hydroplaning thresholds on standing highway puddles.",
            "Policy Hardening: Teaching autonomous vehicles when to slow down, increase following distance, or safely pull over."
        ],
        "script": (
            "[TA Sarah] Slide 20 explores \"SIMULATING EXTREME WEATHER: HARDENING EDGE-CASES.\"\n\n"
            "[TA James] In heavy blizzards, snow reflects LiDAR laser pulses, creating sensor noise. On wet highways, cars hydroplane at 55 MPH!\n\n"
            "[Prof. Peter] Genie 3 simulates droplet refractions on virtual camera lenses and accurately calculates tire hydroplaning dynamics! Autonomous agents learn exactly when to slow down and when to execute safe emergency roadside stops!\n\n"
            "[TA Sarah] Let us inspect Swarm Testing Protocols on Slide 21."
        ),
        "koreanGuide": {
            "summary": "극한 기상 시뮬레이션: 폭우, 눈보라, 빙판길에서의 센서 노이즈 및 수막현상 훈련",
            "points": [
                "센서 저하 모델링: 카메라 렌즈에 맺히는 빗방울 굴절과 폭설 시 라이다 반사 노이즈 정밀 재현",
                "수막현상(Hydroplaning) 계산: 젖은 도로에서 시속 55마일 주행 시 발생하는 타이어 접지력 상실 연산",
                "정책 경질화: 극한 상황에서 안전거리 확보, 감속, 비상 갓길 정차를 스스로 판단하도록 훈련"
            ],
            "tips": "제임스 조교와 피터 교수가 라이다 노이즈와 수막현상까지 재현하는 극도의 물리적 정밀성을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Sensor Degradation Simulation",
                "def": "Modeling physical optical occlusions (rain, fog, mud) on camera and LiDAR sensor representations.",
                "defKo": "센서 노이즈 및 시야 차폐 시뮬레이션"
            },
            {
                "term": "Hydroplaning Dynamics",
                "def": "Calculating fluid dynamic lift forces separating tire rubber from wet pavement during high-speed travel.",
                "defKo": "수막현상 유체역학 계산"
            }
        ]
    },
    # Slide 21: Swarm Testing Protocol: 10,000 Agents in Parallel
    {
        "num": 21,
        "type": "content",
        "title": "SWARM TESTING: 10,000 AGENTS IN PARALLEL",
        "subtitle": "Executing distributed Monte Carlo driving evaluations across thousands of isolated virtual cities",
        "points": [
            "Massive Parallelism: 10,000 virtual Waymo cars driving simultaneously in 10,000 unique procedurally generated cities.",
            "Policy Cross-Pollination: If 1 car discovers an optimal maneuver to avoid a sudden deer, all 10,000 cars inherit the weight update.",
            "Continuous Integration for Physical AI: Automatically benchmarking new autonomous models against 1M virtual miles overnight."
        ],
        "script": (
            "[Prof. Peter] Slide 21 diagrams \"THE SWARM TESTING PROTOCOL: 10,000 AGENTS IN PARALLEL.\"\n\n"
            "[TA Sarah] Look at the collective intelligence of the swarm: 10,000 virtual Waymo vehicles drive in parallel across 10,000 virtual cities!\n\n"
            "[TA James] If Car #4,200 in a virtual Minneapolis blizzard discovers a brilliant steering maneuver to avoid a skidding semi-truck, that neural gradient update is merged into the global model in 10 seconds! Instantly, all 10,000 cars possess that survival instinct!\n\n"
            "[Prof. Peter] That is why autonomous AI evolves millions of times faster than human biology.\n\n"
            "[TA Sarah] Let us examine our second enterprise case study on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "스웜 테스팅 프로토콜: 10,000대 차량의 동시 가상 주행 및 신경망 즉각 공유",
            "points": [
                "10,000대 초병렬 주행: 10,000개의 절차적 도시에서 10,000대의 가상 차량이 동시 다발 훈련",
                "집단 지성 가중치 전파: 4,200번 차량이 눈길 미끄러짐 회피 기술을 터득하면 10초 만에 10,000대 전체에 업데이트",
                "생물학적 진화를 뛰어넘는 초고속 집단 학습 속도"
            ],
            "tips": "사라 조교와 제임스 조교가 1대의 경험이 즉시 1만 대의 본능으로 복제되는 스웜 지능의 경이를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Collective Swarm Learning",
                "def": "Instantly distributing neural policy gradient improvements discovered by a single agent across an entire fleet.",
                "defKo": "집단 스웜 학습 (초고속 가중치 공유)"
            },
            {
                "term": "Continuous Physical AI CI/CD",
                "def": "The automated daily regression testing of autonomous vehicle models against millions of simulated miles.",
                "defKo": "물리 AI 지속적 통합 배포 (Physical CI/CD)"
            }
        ]
    },
    # Slide 22: Case Study 2: Humanitarian Disaster Response: Hurricane Simulation
    {
        "num": 22,
        "type": "casestudy",
        "title": "CASE STUDY 2: HURRICANE DISASTER SIMULATION",
        "subtitle": "Federal Emergency Management Agency simulates Category 5 hurricane flooding in Genie 3, evacuating 85,000 citizens",
        "company": "Federal Emergency Management Agency (FEMA)",
        "problem": "Category 5 hurricane was projected to make landfall in coastal metropolis with 4-meter storm surge; traditional evacuation routing spreadsheets failed to account for flash-flooded bridges and gridlock.",
        "solution": "Built real-time Genie 3 world model using satellite LiDAR and hydro-dynamics: simulated 200,000 fleeing vehicles, flooded roads, and power grid failures.",
        "impact": "Discovered optimal dynamic contraflow lane strategy; safely evacuated 85,000 trapped residents in 6 hours with zero traffic fatalities; saved estimated $450M in emergency costs.",
        "script": (
            "[Prof. Peter] Slide 22 presents \"CASE STUDY 2: HUMANITARIAN DISASTER RESPONSE: HURRICANE SIMULATION.\"\n\n"
            "[TA Sarah] A Category 5 hurricane was barreling toward a coastal metropolis of 1 million residents, threatening a 4-meter catastrophic storm surge! Traditional disaster spreadsheets could not predict which bridges would flood first or where traffic gridlock would trap families!\n\n"
            "[TA James] FEMA engineers fed satellite elevation data and storm surge models into Genie 3: The world model simulated 200,000 fleeing vehicles, rising floodwaters, and collapsing power lines across 50 parallel scenarios!\n\n"
            "[Prof. Peter] In 30 minutes, Genie 3 discovered an optimal dynamic contraflow evacuation route that kept highway bridges open! 85,000 residents were evacuated to safety in 6 hours with zero casualties! World models save lives.\n\n"
            "[TA Sarah] Now let us open Part 3 and master Strategic Governance on Slide 23!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 2: 카테고리 5 초강력 허리케인 침수 시뮬레이션을 통한 85,000명 주민 무사 대피",
            "points": [
                "문제 상황: 4미터 폭풍 해일이 예보된 해안 대도시, 기존 엑셀식 대피 계획으로는 교량 침수와 도로 마비 예측 불가",
                "솔루션: 지니 3 월드 모델에 위성 라이다 및 유체 시뮬레이션 결합 ➔ 20만 대 차량의 실시간 대피 50개 시나리오 연산",
                "성과: 최적의 가변 차로 역주행(Contraflow) 대피로를 찾아내 85,000명을 6시간 만에 인명 피해 0건으로 완전 대피"
            ],
            "tips": "사라 조교와 피터 교수가 허리케인 침수 시뮬레이션이 85,000명의 생명을 구한 감동적 실화를 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Disaster Evacuation Simulation",
                "def": "Modeling mass population movement, infrastructure collapse, and fluid flood dynamics to optimize emergency response routes.",
                "defKo": "재난 대피 물리 시뮬레이션"
            },
            {
                "term": "Dynamic Contraflow Routing",
                "def": "Reversing the flow of inbound highway lanes to double outbound evacuation bandwidth during emergencies.",
                "defKo": "가변 차로 역주행(Contraflow) 대피 경로"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 23: Part 3 Section Divider
    {
        "num": 23,
        "type": "section",
        "title": "PART 3: STRATEGIC GOVERNANCE & CREATIVE SOVEREIGNTY",
        "subtitle": "Human-on-the-loop veto power, crash forensics, 3 commercial verticals, and cybersecurity fortification",
        "script": (
            "[TA Sarah] Look at Slide 23: \"PART 3: STRATEGIC GOVERNANCE & CREATIVE SOVEREIGNTY.\" Now we examine the command, safety, and commercialization frameworks!\n\n"
            "[Prof. Peter] World models wield immense generative power. In Part 3, we master Veto-on-the-Loop human authority, Ed25519 cryptographic crash audit trails, 3 commercial verticals (Robotics, Aviation, Smart Cities), and cybersecurity fortification.\n\n"
            "[TA James] Let us inspect Veto-on-the-Loop Human Sovereignty on Slide 24!"
        ),
        "koreanGuide": {
            "summary": "Part 3 섹션 전환: 전략적 거버넌스와 창조적 주권",
            "points": [
                "월드 모델의 거대한 권능을 통제할 주권적 지휘관 거버넌스 수립",
                "Veto-on-the-Loop 인간 거부권과 Ed25519 충돌 사고 포렌식 감사 로그",
                "3대 상용화 버티컬(로보틱스, 항공, 스마트 시티)과 사이버 요새화"
            ],
            "tips": "피터 교수가 거버넌스의 중요성을 선언하고 제임스가 인간 개입 거부권을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Creative Sovereignty",
                "def": "The human director's supreme authority to shape, constrain, and authorize generative world simulation deployments.",
                "defKo": "창조적 주권 (Creative Sovereignty)"
            },
            {
                "term": "Veto-on-the-Loop (VOTL)",
                "def": "A governance framework granting human supervisors instantaneous single-button override authority over autonomous systems.",
                "defKo": "비토 온 더 루프 (VOTL 즉각 거부권)"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 24: Veto-on-the-Loop: Human Operator Sovereignty
    {
        "num": 24,
        "type": "content",
        "title": "VETO-ON-THE-LOOP: OPERATOR SOVEREIGNTY",
        "subtitle": "Preserving the supreme human safety valve over autonomous vehicles and industrial robot fleets",
        "points": [
            "The Remote Operator Bridge: Human safety tele-operators monitoring 50 autonomous vehicles in real time.",
            "Sub-50ms Remote Intervention: If an autonomous vehicle encounters an ambiguous construction zone, human gives high-level guidance.",
            "Immutable Safety Rule: Automated neural policies propose trajectories; human directors retain ultimate veto power."
        ],
        "script": (
            "[Prof. Peter] Slide 24 establishes \"VETO-ON-THE-LOOP: OPERATOR SOVEREIGNTY.\"\n\n"
            "[TA Sarah] In Waymo and industrial robotics, autonomous vehicles drive themselves 99.99% of the time. But if a car encounters a confusing police hand signal in an active construction zone, the Veto-on-the-Loop bridge activates!\n\n"
            "[TA James] A remote human tele-operator sees the 3D Genie 3 point cloud in real time, clicks the safe path around the police officer in 2 seconds, and the vehicle resumes autonomous travel! Humans hold the ultimate steering authority!\n\n"
            "[Prof. Peter] Let us inspect Crash Audit Trails on Slide 25."
        ),
        "koreanGuide": {
            "summary": "Veto-on-the-Loop: 원격 인간 오퍼레이터의 주권적 안전 밸브",
            "points": [
                "원격 관제 브릿지: 1명의 인간 안전 오퍼레이터가 50대의 자율주행 차량 상태를 실시간 모니터링",
                "50ms 초고속 원격 개입: 공사 현장 경찰관의 수신호 등 애매한 상황 발생 시 2초 만에 안전 경로 지정",
                "불변의 원칙: 신경망 정책이 주행 경로를 제안하되 인간 지휘관이 궁극적 비토(Veto) 권한 보유"
            ],
            "tips": "사라 조교와 제임스 조교가 1명이 50대를 원격 관제하며 위기 시 개입하는 VOTL 안전망을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Tele-Operation Guidance Bridge",
                "def": "A low-latency remote communication link enabling human operators to confirm or override autonomous vehicle decisions.",
                "defKo": "원격 관제 유도 브릿지"
            },
            {
                "term": "Ambiguity Resolution Gate",
                "def": "A safety checkpoint routing low-confidence perception events to human supervisors for instant disambiguation.",
                "defKo": "인식 불확실성 해소 관문"
            }
        ]
    },
    # Slide 25: Crash Audit Trails: Ed25519 Cryptographic Logs
    {
        "num": 25,
        "type": "content",
        "title": "CRASH AUDIT TRAILS: ED25519 LOGS",
        "subtitle": "Tamper-proof black box recording of every sensor packet, neural weight, and trajectory decision",
        "points": [
            "The Black Box Invariant: Every camera frame, LiDAR pulse, steering torque, and model confidence score is hashed.",
            "Ed25519 Cryptographic Sealing: Telemetry logs are sealed onto an immutable append-only ledger every 100 milliseconds.",
            "Legal & Insurance Clarity: In the rare event of an incident, forensic investigators reconstruct the exact state in 5 minutes."
        ],
        "script": (
            "[TA Sarah] Slide 25 presents \"CRASH AUDIT TRAILS: ED25519 CRYPTOGRAPHIC LOGS.\"\n\n"
            "[TA James] In physical transportation, legal liability is paramount! Antigravity records an immutable cryptographic black box: every sensor photon, steering torque command, and neural attention weight is hashed and signed with an Ed25519 key every 100 milliseconds!\n\n"
            "[Prof. Peter] If an accident occurs, insurance and police investigators load the cryptographic receipt into Genie 3, replaying the exact 3D physics down to the millimeter! Total transparency, zero cover-ups.\n\n"
            "[TA Sarah] Let us inspect the 3 Commercial Verticals on Slide 26."
        ),
        "koreanGuide": {
            "summary": "충돌 사고 포렌식 감사 로그: Ed25519 전자서명과 5분 3D 물리 재현",
            "points": [
                "블랙박스 불변식: 모든 카메라 프레임, 라이다 펄스, 스티어링 토크, 모델 확신도를 100ms마다 해싱",
                "Ed25519 암호화 봉인: 위변조가 원천 불가능한 불변 원장에 기록하여 법적/보험적 분쟁 완벽 방어",
                "5분 초정밀 포렌식: 사고 발생 시 암호 영수증을 지니 3에 넣으면 밀리미터 단위로 당시 3D 물리를 100% 재현"
            ],
            "tips": "제임스 조교와 피터 교수가 사고 은폐를 원천 차단하는 암호화 블랙박스의 투명성을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Cryptographic Black Box",
                "def": "An immutable, digitally signed telemetry ledger recording all autonomous perception inputs and actuation outputs.",
                "defKo": "암호화 자율주행 블랙박스"
            },
            {
                "term": "Post-Incident Physics Replay",
                "def": "Deterministic re-simulation of an accident scene within a world model using verified cryptographically signed sensor logs.",
                "defKo": "사고 현장 3D 물리 포렌식 재생"
            }
        ]
    },
    # Slide 26: 3 Commercial Verticals: Robotics, Aviation, Smart Cities
    {
        "num": 26,
        "type": "content",
        "title": "3 COMMERCIAL VERTICALS: ROBOTICS, AVIATION, CITIES",
        "subtitle": "Expanding beyond passenger cars to humanoid warehouse robots, eVTOL aircraft, and urban digital twins",
        "points": [
            "Vertical 1: Humanoid Robotics (Training warehouse robots to grasp 50,000 fragile items with tactile physics).",
            "Vertical 2: Urban Air Mobility & eVTOL (Simulating drone flight turbulence, bird strikes, and rooftop landings).",
            "Vertical 3: Smart Cities (Simulating city-wide power grids, water flows, and traffic signal optimization)."
        ],
        "script": (
            "[Prof. Peter] Slide 26 outlines the massive commercial market: \"3 COMMERCIAL VERTICALS: ROBOTICS, AVIATION, SMART CITIES.\"\n\n"
            "[TA Sarah] Vertical 1 is Humanoid Robotics: Training factory robots to fold clothes and pack fragile glass bottles in simulation before touching real objects! Vertical 2 is Urban Air Mobility: Testing electric vertical takeoff (eVTOL) air taxis against severe rooftop wind shears!\n\n"
            "[TA James] And Vertical 3 is Smart Cities: Running complete digital twins of Chicago or Tokyo to optimize traffic lights and slash municipal electricity waste by 25%!\n\n"
            "[TA Sarah] Let us inspect Cybersecurity Risks in Simulation on Slide 27."
        ),
        "koreanGuide": {
            "summary": "월드 모델의 3대 상용화 버티컬: 휴머노이드 로보틱스, eVTOL 도심 항공, 스마트 시티",
            "points": [
                "버티컬 1 (휴머노이드 로보틱스): 50,000가지 깨지기 쉬운 물품의 촉각 물리 파지 훈련을 가상 공간에서 완결",
                "버티컬 2 (eVTOL 도심 항공 모빌리티): 빌딩풍 돌풍과 조류 충돌 속 드론 및 에어택시 옥상 착륙 시험",
                "버티컬 3 (스마트 시티 디지털 트윈): 도시 전체 교통 신호 최적화로 지체 시간 25% 단축 및 전력 절감"
            ],
            "tips": "사라 조교와 제임스 조교가 자율주행을 넘어 로봇, 항공, 도시 전체로 뻗어가는 월드 모델의 거대한 시장을 제시합니다."
        },
        "keyTerms": [
            {
                "term": "Humanoid Tactile Simulation",
                "def": "Modeling friction, elasticity, and fragile contact physics to train multi-fingered robot dexterous manipulation.",
                "defKo": "휴머노이드 촉각 물리 시뮬레이션"
            },
            {
                "term": "eVTOL Micro-Turbulence Modeling",
                "def": "Simulating localized aerodynamic wind sheer vortices around high-rise buildings for urban flight certification.",
                "defKo": "도심 항공 미세 난류 기류 모델링"
            }
        ]
    },
    # Slide 27: 3 Severe Cybersecurity Risks in Simulation
    {
        "num": 27,
        "type": "content",
        "title": "3 SEVERE CYBERSECURITY RISKS IN SIMULATION",
        "subtitle": "Adversarial simulation poisoning, toposecret exfiltration, and phantom obstacle injection",
        "points": [
            "Risk 1: Simulation Poisoning (Adversaries injecting flawed physics into world models to teach robots bad policies).",
            "Risk 2: Topographical Exfiltration (Rogue agents leaking classified military/corporate facility 3D meshes).",
            "Risk 3: Phantom Obstacle Injection (Spoofing fake stop signs or invisible pedestrians into sensor streams)."
        ],
        "script": (
            "[TA Sarah] Slide 27 covers \"3 SEVERE CYBERSECURITY RISKS IN SIMULATION.\"\n\n"
            "[TA James] When physical AI trains in virtual worlds, hacking the simulator is catastrophic! Risk 1: Simulation Poisoning—a hacker tweaks gravity by 2%, causing warehouse robots to drop heavy machinery! Risk 2: Toposecret Exfiltration—stealing high-res 3D scans of defense facilities! Risk 3: Phantom Obstacles—spoofing fake stop signs into perception networks!\n\n"
            "[Prof. Peter] We must fortify the simulation sandbox with cryptographic network armor.\n\n"
            "[TA Sarah] Let us inspect Cybernetic Fortification on Slide 28."
        ),
        "koreanGuide": {
            "summary": "가상 시뮬레이션 환경의 3대 중대 사이버 보안 위협",
            "points": [
                "위협 1 (시뮬레이션 오염 공격): 물리 파라미터를 2% 조작하여 로봇이 현실에서 오작동하도록 유도",
                "위협 2 (지형 기밀 유출): 국가 보안 시설이나 첨단 반도체 공장의 3D 정밀 스캔 데이터 탈취 시도",
                "위협 3 (유령 장애물 주입): 센서 스트림에 가짜 정지 표지판이나 유령 보행자를 주입해 급정거 유발"
            ],
            "tips": "제임스 조교가 가상 시뮬레이터를 타깃으로 하는 신종 사이버 공격의 위험성을 경고합니다."
        },
        "keyTerms": [
            {
                "term": "Simulation Poisoning",
                "def": "The covert corruption of training environment physical parameters designed to induce dangerous real-world failure modes.",
                "defKo": "가상 시뮬레이션 오염 공격"
            },
            {
                "term": "Phantom Obstacle Injection",
                "def": "The spoofing of synthetic sensory artifacts into autonomous perception pipelines to trigger erratic braking maneuvers.",
                "defKo": "유령 장애물 신호 주입 공격"
            }
        ]
    },
    # Slide 28: Cybernetic Fortification: DNR Filters & Micro-VPC
    {
        "num": 28,
        "type": "content",
        "title": "CYBERNETIC FORTIFICATION: DNR & MICRO-VPC",
        "subtitle": "Network isolation, signed model weights, and ephemeral memory bounds for simulation clusters",
        "points": [
            "Micro-VPC Isolation: Running simulation pods in isolated virtual private clouds with zero public internet egress.",
            "Signed Weight Verification: Validating Ed25519 digital signatures on all world model checkpoint weights before loading.",
            "DeclarativeNetRequest (DNR) Firewalls: Blocking all telemetry leakage to untrusted third-party endpoints."
        ],
        "script": (
            "[Prof. Peter] Slide 28 presents \"CYBERNETIC FORTIFICATION: DNR FILTERS & MICRO-VPC.\"\n\n"
            "[TA Sarah] To secure our world models, we deploy 3 ironclad defenses: First, all simulation pods run in Micro-VPC network isolation with zero external internet routing. Second, every model checkpoint requires an Ed25519 digital signature verified against hardware Secure Enclaves!\n\n"
            "[TA James] Third, DNR packet filtering blocks unauthorized data exfiltration! The simulation fortress remains completely sealed.\n\n"
            "[Prof. Peter] Let us inspect the Conductor Model on Slide 29."
        ),
        "koreanGuide": {
            "summary": "사이버네틱 요새화: Micro-VPC 네트워크 격리와 모델 가중치 서명 검증",
            "points": [
                "Micro-VPC 완벽 격리: 시뮬레이션 파드를 외부 인터넷 라우팅이 차단된 가상 사설망에서 폐쇄 구동",
                "Ed25519 서명 검증: 모든 월드 모델 체크포인트 가중치의 암호 서명을 하드웨어 보안 칩으로 검증",
                "DNR 패킷 필터링: 인가되지 않은 외부 엔드포인트로의 텔레메트리 유출을 0ms 단위로 원천 차단"
            ],
            "tips": "사라 조교와 제임스 조교가 가상 세계 시뮬레이터를 외부 해킹으로부터 지키는 3중 방어선을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Micro-VPC Sandbox",
                "def": "A dedicated, tightly constrained virtual private cloud network restricting cluster communication to authorized nodes.",
                "defKo": "Micro-VPC 폐쇄 격리망"
            },
            {
                "term": "Signed Model Checkpoint",
                "def": "A neural weight binary file verified by a cryptographic signature to guarantee origin authenticity and weight integrity.",
                "defKo": "전자서명된 모델 체크포인트"
            }
        ]
    },
    # Slide 29: The Conductor Model: Human Spirit as the Sole Source
    {
        "num": 29,
        "type": "content",
        "title": "THE CONDUCTOR: HUMAN SPIRIT AS SOURCE",
        "subtitle": "Why mathematical world models remain empty reflections without the spark of human creative vision",
        "points": [
            "The Mirror of Nature: World models reflect the physics of creation, but CANNOT originate purpose, beauty, or love.",
            "The Human Spark: Human architects define what worlds should be built, what challenges should be solved, and why.",
            "Leading with Sovereignty: Directing simulation technology to protect human life and advance the Kingdom of God."
        ],
        "script": (
            "[Prof. Peter] Slide 29 reflects on \"THE CONDUCTOR: THE HUMAN SPIRIT AS THE SOLE SOURCE.\"\n\n"
            "[TA Sarah] Genie 3 can simulate a thousand worlds, but it cannot create a single moral purpose. A world model is a mathematical mirror; it reflects the laws of physics, but the breath of purpose comes only from the human soul!\n\n"
            "[TA James] The human architect decides which worlds to explore, which diseases to cure, and how to safely navigate our cities!\n\n"
            "[Prof. Peter] We conduct these physical simulations under the sovereign wisdom of God.\n\n"
            "[TA Sarah] Let us inspect Soli Deo Gloria on Slide 30!"
        ),
        "koreanGuide": {
            "summary": "지휘관 모델: 모든 목적과 아름다움의 유일한 원천인 인간의 영혼",
            "points": [
                "자연의 거울: 월드 모델은 물리 법칙을 완벽히 반사하지만 목적, 아름다움, 사랑을 스스로 창출하지 못함",
                "인간의 불꽃: 어떤 세계를 창조하고 어떤 문제를 해결할지 결정하는 주권적 의지는 인간의 영혼에서만 발현",
                "주권적 리더십: 인간 생명을 구하고 하나님의 나라를 확장하기 위해 시뮬레이션 기술을 지혜롭게 지휘"
            ],
            "tips": "피터 교수가 기계는 거울일 뿐 목적과 생명의 원천은 인간 영혼에 있음을 감동적으로 설파합니다."
        },
        "keyTerms": [
            {
                "term": "Mathematical Mirror",
                "def": "The philosophical recognition that world models simulate external physical phenomena without possessing intrinsic moral intentionality.",
                "defKo": "물리적 현상의 수학적 거울"
            },
            {
                "term": "Human Creative Primacy",
                "def": "The foundational principle that purposeful intent, ethics, and aesthetic beauty originate exclusively from human consciousness.",
                "defKo": "인간 창의성의 절대적 우위"
            }
        ]
    },
    # Slide 30: Soli Deo Gloria: The Architecture of the Cosmos
    {
        "num": 30,
        "type": "content",
        "title": "SOLI DEO GLORIA: COSMIC ARCHITECTURE",
        "subtitle": "Colossians 1:16-17: In Him all things were created, and in Him all things hold together",
        "points": [
            "Soli Deo Gloria: The supreme cornerstone of Oikos University and Smart Insight Lab.",
            "Colossians 1:17: 'He is before all things, and in Him all things hold together.'",
            "The True Physicist: Exploring the divine cohesion, gravity, and beauty holding the cosmos in harmony."
        ],
        "script": (
            "[Prof. Peter] Slide 30 declares our foundation: \"SOLI DEO GLORIA: COSMIC ARCHITECTURE: To God Alone Be the Glory.\"\n\n"
            "[TA Sarah] In Colossians 1:16-17, Scripture reveals: 'For by Him all things were created... He is before all things, and in Him all things hold together.'\n\n"
            "[TA James] When our neural world models calculate gravity, friction, light reflection, and fluid viscosity, we are observing the divine laws by which Christ holds the entire universe together!\n\n"
            "[Prof. Peter] May our physical simulations always reflect the majesty and glory of the Master Architect of the Cosmos.\n\n"
            "[TA Sarah] Let us inspect our 6-step World Model Deployment Blueprint on Slide 31!"
        ),
        "koreanGuide": {
            "summary": "Soli Deo Gloria: 우주의 대건축가이신 그리스도의 창조 질서 탐구",
            "points": [
                "골로새서 1장 16~17절: '만물이 그로 말미암아... 그가 만물보다 먼저 계시고 만물이 그 안에 함께 섰느니라'",
                "만물을 붙드시는 섭리: 신경망이 중력과 마찰력, 빛을 연산할 때 그리스도께서 우주를 붙드시는 물리 법칙을 목도",
                "모든 물리 시뮬레이션 연구를 우주의 대건축가이신 하나님께 온전히 바치는 예배적 공학"
            ],
            "tips": "3인의 강사진이 골로새서 말씀을 인용하며 물리 시뮬레이션의 웅장한 신학적 의미를 선포합니다."
        },
        "keyTerms": [
            {
                "term": "Soli Deo Gloria",
                "def": "The foundational theological motto dedicating all intellectual and technological mastery to the Glory of God Alone.",
                "defKo": "솔리 데오 글로리아 (오직 하나님께 영광)"
            },
            {
                "term": "Cosmic Cohesion Principle",
                "def": "The theological and scientific understanding that physical constants and natural laws reflect divine sustaining order.",
                "defKo": "우주적 결합과 질서의 원리"
            }
        ]
    },
    # Slide 31: The 6-Step World Model Deployment Blueprint
    {
        "num": 31,
        "type": "content",
        "title": "THE 6-STEP WORLD MODEL BLUEPRINT",
        "subtitle": "The standardized pipeline from raw sensory capture to certified physical AI deployment",
        "points": [
            "Step 1: Environmental Capture (Ingest Street View imagery, satellite LiDAR, or photos into VMC Vision module).",
            "Step 2: Spatio-Temporal Generation (Generate 3D neural radiance volume with rigid-body and fluid physics).",
            "Step 3: Swarm Policy Injection (Deploy 1,000 parallel autonomous agents into procedurally generated worlds).",
            "Step 4: Dynamic Hazard Stress-Testing (Inject real-time prompt events: blizzards, black ice, and falling debris).",
            "Step 5: Cryptographic Crash Forensics (Hash telemetry into Ed25519 signed append-only black box ledgers).",
            "Step 6: Human-on-the-Loop Release (PI review, safety certification, and physical deployment to real fleets)."
        ],
        "script": (
            "[TA Sarah] Slide 31 presents our master operational methodology: \"THE 6-STEP WORLD MODEL BLUEPRINT.\"\n\n"
            "[TA James] Follow this exact 6-step engineering pipeline: Step 1: Ingest multi-angle imagery. Step 2: Generate 3D neural physics volumes. Step 3: Launch 1,000-agent swarm training. Step 4: Stress-test with real-time prompt hazards! Step 5: Seal Ed25519 black box crash logs. Step 6: Certify with Human-on-the-Loop approval!\n\n"
            "[Prof. Peter] This structured blueprint guarantees physical safety and world-class autonomous performance.\n\n"
            "[TA Sarah] Let us inspect our Pre-Deployment Production Checklist on Slide 32."
        ),
        "koreanGuide": {
            "summary": "월드 모델 배포 6단계 표준 구현 청사진",
            "points": [
                "1단계: 환경 캡처 (스트리트뷰, 위성 라이다, 사진을 VMC 비전 모듈에 수용)",
                "2단계: 시공간 3D 생성 (강체 및 유체 물리가 적용된 3D 공간 볼륨 합성)",
                "3단계: 스웜 정책 주입 (1,000대 에이전트를 가상 세계에 동시 투입 훈련)",
                "4단계: 동적 위험 스트레스 테스트 (눈보라, 빙판, 낙하물 실시간 주입)",
                "5단계: 암호화 사고 포렌식 (Ed25519 전자서명 블랙박스 원장 봉인)",
                "6단계: Human-on-the-Loop 최종 승인 및 실물 로봇/차량 현장 배포"
            ],
            "tips": "제임스 조교가 6단계 절차를 완벽한 물리 AI 배포 지침으로 일목요연하게 정리합니다."
        },
        "keyTerms": [
            {
                "term": "World Model Blueprint",
                "def": "The formal 6-stage engineering process governing 3D environment synthesis, agent swarm training, and safety validation.",
                "defKo": "월드 모델 배포 표준 청사진"
            },
            {
                "term": "Physical Fleet Deployment",
                "def": "Transitioning autonomous neural policies trained in virtual simulation into real physical machines and vehicles.",
                "defKo": "실물 물리 로봇/차량 현장 배포"
            }
        ]
    },
    # Slide 32: Production Checklist: Pre-Deployment Verification
    {
        "num": 32,
        "type": "content",
        "title": "PRODUCTION CHECKLIST: PRE-DEPLOYMENT VERIFICATION",
        "subtitle": "The 6-gate audit every autonomous world model policy must pass before physical rollout",
        "points": [
            "Gate 1: Minimum 10,000,000 simulated collision-free hazard miles across extreme weather scenarios.",
            "Gate 2: 100% of physical prompt events (friction loss, obstacles) handled within 50ms control SLA.",
            "Gate 3: Tele-operation Veto-on-the-Loop latency tested under 40ms round-trip over 5G/satellite.",
            "Gate 4: Micro-VPC network isolation and Ed25519 signed checkpoint verification verified active.",
            "Gate 5: Cryptographic black box logging validated with 100% telemetry replay fidelity.",
            "Gate 6: Dual-Key safety certification signed by Lead Robotics Architect and Biosafety Officer."
        ],
        "script": (
            "[TA James] Slide 32 presents our \"PRODUCTION CHECKLIST: PRE-DEPLOYMENT VERIFICATION.\"\n\n"
            "[TA Sarah] Before releasing any autonomous policy to real-world roads or factories, audit all 6 gates: Gate 1: 10M collision-free hazard miles. Gate 2: 50ms control SLA. Gate 3: Sub-40ms tele-op veto bridge. Gate 4: Micro-VPC isolation. Gate 5: 100% black box replay fidelity. Gate 6: Dual-Key sign-off!\n\n"
            "[Prof. Peter] Strict verification gates protect human life on physical highways.\n\n"
            "[TA Sarah] Let us inspect our third enterprise case study on Slide 33!"
        ),
        "koreanGuide": {
            "summary": "프로덕션 체크리스트: 물리 AI 현장 배포 전 6대 검증 관문",
            "points": [
                "1관문: 극한 기상 엣지 케이스 포함 1,000만 마일 무사고 가상 주행 달성",
                "2관문: 마찰력 상실 및 돌발 장애물 대응 제어 50ms SLA 100% 충족",
                "3관문: 5G/위성 기반 원격 비토(VOTL) 지연 시간 40ms 미만 확인",
                "4관문: Micro-VPC 폐쇄망 격리 및 Ed25519 체크포인트 전자서명 확인",
                "5관문: 블랙박스 암호화 영수증의 100% 밀리미터 단위 물리 재현 검증",
                "6관문: 수석 로보틱스 아키텍트와 안전 책임자의 이중 서명 완료"
            ],
            "tips": "제임스 조교가 6대 검증 관문을 단호하게 체크리스트로 확인합니다."
        },
        "keyTerms": [
            {
                "term": "Pre-Rollout Verification Gate",
                "def": "A mandatory operational quality checkpoint ensuring physical AI policies satisfy safety invariants prior to real deployment.",
                "defKo": "실물 배포 전 사전 검증 관문"
            },
            {
                "term": "Control Loop SLA",
                "def": "The non-negotiable temporal latency budget within which an autonomous system must process sensors and actuate controls.",
                "defKo": "제어 루프 응답 시간 SLA"
            }
        ]
    },
    # Slide 33: Case Study 3: Global Defense Drone Swarm Combat Flight Simulator
    {
        "num": 33,
        "type": "casestudy",
        "title": "CASE STUDY 3: DEFENSE DRONE SWARM SIMULATOR",
        "subtitle": "Allied Defense Aerospace simulates 5,000-drone autonomous tactical swarm in contested GPS-denied terrain",
        "company": "Allied Aerospace Defense Technology Consortium",
        "problem": "Modern electronic warfare disables GPS satellites and radio communications; testing autonomous drone flocking in physical flight ranges costs $2M per live-fire exercise.",
        "solution": "Built high-fidelity Genie 3 world model simulating mountain radar shadows, electronic jamming, and dynamic wind gusts for 5,000 autonomous drones.",
        "impact": "Trained swarm to execute vision-based optical navigation and decentralized target tracking with 99.4% mission success in GPS-denied environments; saved $85M in flight test costs.",
        "script": (
            "[Prof. Peter] Slide 33 presents \"CASE STUDY 3: DEFENSE DRONE SWARM COMBAT FLIGHT SIMULATOR.\"\n\n"
            "[TA Sarah] In modern electronic warfare, adversaries jam GPS satellites and sever radio links! Developing autonomous drone swarms that navigate purely by optical vision and local peer mesh networking is essential, but live-fire range tests cost 2 million dollars per flight!\n\n"
            "[TA James] Allied Aerospace deployed Genie 3: simulating complex mountain terrain, electronic jamming noise, anti-aircraft radar shadows, and sudden wind gusts across 5,000 autonomous drones simultaneously!\n\n"
            "[Prof. Peter] The swarm learned decentralized optical navigation, achieving a 99.4% mission success rate without GPS, saving 85 million dollars in live-fire flight testing!\n\n"
            "[TA Sarah] Let us open Part 4 and review Session 12 Key Takeaways on Slide 34!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 3: GPS 전파 방해 상황 5,000대 군집 드론 광학 비행 시뮬레이터",
            "points": [
                "문제 상황: 전자전으로 GPS와 무선 통신이 두절되는 전장 환경, 실사격 비행 시험에 회당 200만 달러 소요",
                "솔루션: 지니 3 월드 모델 내에 산악 레이더 음영, 전파 교란, 돌풍 기류를 구현해 5,000대 드론 동시 가상 훈련",
                "성과: GPS 없이 순수 광학 비전과 분산 메쉬 통신만으로 99.4% 작전 성공률 달성, 8,500만 달러 실사격 시험비 절감"
            ],
            "tips": "사라 조교와 제임스 조교가 GPS 없는 극한 전장 환경을 월드 모델로 극복한 국방 항공 혁신을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "GPS-Denied Optical Navigation",
                "def": "Autonomous spatial positioning and guidance achieved entirely through visual landmark recognition and optical flow tracking.",
                "defKo": "GPS 두절 광학 비전 항법"
            },
            {
                "term": "Decentralized Swarm Mesh",
                "def": "Peer-to-peer inter-agent coordination maintaining formation flight and objective execution without centralized command.",
                "defKo": "탈중앙 분산형 스웜 메쉬 통신"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 34: Part 4 Section Divider
    {
        "num": 34,
        "type": "section",
        "title": "PART 4: SYNTHESIS, BENCHMARKS & WORKSTATIONS",
        "subtitle": "Key takeaways, the Life OS Spatial Cockpit, future horizons, and Hands-on Lab 12",
        "script": (
            "[TA Sarah] Look at Slide 34: \"PART 4: SYNTHESIS, BENCHMARKS & WORKSTATIONS.\" Now we integrate spatial intelligence into our daily development workflow!\n\n"
            "[Prof. Peter] World models are not just for Silicon Valley giants; every Intelligence Architect can configure spatial simulation tools to design future robotics, games, and urban architectures.\n\n"
            "[TA James] In Part 4, we review Session 12 key takeaways, build the Life OS Spatial Cockpit, explore Industrial Robotics digital twins, dedicate our craft to Soli Deo Gloria, and execute Lab 12!\n\n"
            "[TA Sarah] Let us review Session 12 Summary on Slide 35!"
        ),
        "koreanGuide": {
            "summary": "Part 4 섹션 전환: 종합 합성, 공간 콕핏 및 산업용 디지털 트윈",
            "points": [
                "공간 지능의 일상 개발 워크플로우 통합 및 지휘관 콕핏 구축",
                "Session 12 핵심 요약 및 산업용 로보틱스 디지털 트윈(Digital Twin) 분석",
                "다음 지평(Session 13: SVG·LaTeX 수학 시각화) 예고 및 실습 12"
            ],
            "tips": "피터 교수가 공간 지능의 일상화를 선언하고 제임스가 종합 실습을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Spatial Intelligence Workflow",
                "def": "The unified developer process integrating generative 3D simulation into daily software and robotics engineering.",
                "defKo": "공간 지능 개발 워크플로우"
            },
            {
                "term": "Industrial Digital Twin",
                "def": "A real-time, physically accurate virtual simulation mirroring physical factory equipment and manufacturing lines.",
                "defKo": "산업용 디지털 트윈 (Digital Twin)"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 35: Session 12 Summary & Key Takeaways
    {
        "num": 35,
        "type": "content",
        "title": "SESSION 12 SUMMARY & KEY TAKEAWAYS",
        "subtitle": "Synthesizing the 4 foundational pillars of World Models and Genie 3 Simulation",
        "points": [
            "Pillar 1: Beyond 2D Tokens (Mastered 3D spatial physics, mass, momentum, and continuous time dynamics).",
            "Pillar 2: Google Genie 3 Engine (280B Street View moat, VMC architecture, and 60 FPS WebGL streaming).",
            "Pillar 3: Waymo Swarm Trials (500M virtual miles, extreme weather hardening, and zero-fatality validation).",
            "Pillar 4: Sovereign Governance (Veto-on-the-Loop operator control, Ed25519 black box crash forensics)."
        ],
        "script": (
            "[TA Sarah] Slide 35 synthesizes our \"SESSION 12 SUMMARY & 4 FOUNDATIONAL PILLARS.\"\n\n"
            "[TA James] Pillar 1: We moved beyond 2D tokens to physical 3D world dynamics! Pillar 2: The Genie 3 VMC engine renders worlds at 60 FPS! Pillar 3: Waymo trains 10,000 vehicles across 500 million virtual miles! And Pillar 4: Sovereign Veto-on-the-Loop governance guarantees passenger safety!\n\n"
            "[Prof. Peter] When these four pillars unite, artificial intelligence steps boldly into the physical universe as a faithful servant of human flourishing.\n\n"
            "[TA Sarah] Let us inspect the Life OS Spatial Cockpit on Slide 36!"
        ),
        "koreanGuide": {
            "summary": "Session 12 요약 및 4대 핵심 축 총정리",
            "points": [
                "1대 축: 2D 토큰을 넘어선 3D 공간 물리 역학(질량, 운동량, 연속 시간) 통달",
                "2대 축: 구글 지니 3 엔진 (2,800억 장 해자, VMC 아키텍처, 60 FPS WebGL 스트리밍)",
                "3대 축: 웨이모 스웜 훈련 (5억 마일 가상 주행, 극한 기상 경질화, 무사망 안전 검증)",
                "4대 축: 주권적 거버넌스 (VOTL 원격 거부권 및 Ed25519 암호화 블랙박스 감사 원장)"
            ],
            "tips": "제임스 조교가 4대 축을 리듬감 있게 요약하여 학습 효과를 극대화합니다."
        },
        "keyTerms": [
            {
                "term": "Architectural Synthesis",
                "def": "The unified integration of generative 3D physics, optical supercomputing, distributed swarm validation, and safety governance.",
                "defKo": "아키텍처 통합 합성"
            },
            {
                "term": "Physical AI Mastery",
                "def": "The engineering capability to design, simulate, verify, and deploy autonomous models into real physical hardware.",
                "defKo": "물리 AI 마스터리"
            }
        ]
    },
    # Slide 36: Life OS Spatial Simulation Cockpit
    {
        "num": 36,
        "type": "content",
        "title": "LIFE OS SPATIAL SIMULATION COCKPIT",
        "subtitle": "Setting up your personal world model workstation: WebGL viewport + Python Gym telemetry",
        "points": [
            "Cockpit Setup: 60 FPS WebGL simulation viewport on left monitor; Python Gym / ROS2 telemetry on right monitor.",
            "Joystick / Controller Binding: Mapping physical gamepad inputs directly to VMC controller latent tokens.",
            "Local Synthetic Dataset Vault: Exporting procedurally generated sensor streams to `.agents/datasets/`."
        ],
        "script": (
            "[Prof. Peter] Slide 36 outlines your personal workstation: \"LIFE OS SPATIAL SIMULATION COCKPIT.\"\n\n"
            "[TA Sarah] How do you configure your daily world model development environment? Keep the 60 FPS WebGL interactive simulation open on your primary monitor. On your secondary monitor, stream real-time ROS2 robot telemetry and sensor heatmaps!\n\n"
            "[TA James] Bind your physical USB gamepad directly to Genie 3's controller token stream, and export procedurally generated edge-case datasets directly into your local training vault!\n\n"
            "[TA Sarah] Let us inspect Project Evaluation Rubric on Slide 37."
        ),
        "koreanGuide": {
            "summary": "라이프 OS 공간 시뮬레이션 콕핏: 듀얼 모니터 세팅과 USB 조이스틱 연동",
            "points": [
                "개발 콕핏 구성: 메인 모니터에 60 FPS WebGL 시뮬레이션 + 서브 모니터에 ROS2 로봇 텔레메트리 스트림",
                "물리 컨트롤러 바인딩: USB 게임패드 입력을 VMC 컨트롤러 잠재 토큰에 1:1 직결",
                "로컬 합성 데이터 금고: 절차적으로 생성된 센서 스트림 데이터를 .agents/datasets/에 자동 저장"
            ],
            "tips": "사라 조교와 제임스 조교가 실전 로보틱스 개발자가 사용하는 듀얼 모니터 콕핏 세팅법을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Spatial Simulation Cockpit",
                "def": "A developer layout integrating real-time 3D neural rendering viewports with robotic operating system (ROS) telemetry.",
                "defKo": "공간 시뮬레이션 워크스테이션 콕핏"
            },
            {
                "term": "ROS2 Telemetry Streaming",
                "def": "Real-time communication protocols transmitting actuator states, velocity vectors, and sensor data between robots and simulators.",
                "defKo": "ROS2 로봇 텔레메트리 스트리밍"
            }
        ]
    },
    # Slide 37: Project Evaluation Rubric for Session 12
    {
        "num": 37,
        "type": "content",
        "title": "PROJECT EVALUATION RUBRIC FOR SESSION 12",
        "subtitle": "Grading criteria: 3D world consistency (30%), Real-time prompt event handling (30%), Ed25519 receipt (40%)",
        "points": [
            "Criterion 1 (30%): Stable 3D world generation from 2D prompt maintaining spatial landmark consistency at 60 FPS.",
            "Criterion 2 (30%): Successful real-time prompt event mutation (e.g., triggering rain/obstacles) within 100ms SLA.",
            "Criterion 3 (40%): Valid Ed25519 signed black box crash log recording telemetry, torque, and model confidence scores."
        ],
        "script": (
            "[TA Sarah] Slide 37 presents our \"PROJECT EVALUATION RUBRIC FOR SESSION 12.\"\n\n"
            "[TA James] Your lab assignment will be evaluated on 3 strict criteria: 30% for 3D spatial landmark consistency at 60 FPS. 30% for handling real-time dynamic prompt events within 100ms. And 40% for a valid Ed25519 signed black box telemetry receipt!\n\n"
            "[Prof. Peter] Rigorous engineering standards prepare you to build certified autonomous systems.\n\n"
            "[TA Sarah] Let us inspect Next Horizon: Calculated Visuals on Slide 38!"
        ),
        "koreanGuide": {
            "summary": "Session 12 프로젝트 평가 루브릭: 3D 항상성(30%), 0.1초 이벤트(30%), 암호 영수증(40%)",
            "points": [
                "기준 1 (30%): 60 FPS에서 건물이 왜곡되지 않는 안정적인 3D 공간 랜드마크 항상성 유지",
                "기준 2 (30%): 100ms 이내에 비/장애물을 발생시키는 실시간 동적 프롬프트 이벤트 처리",
                "기준 3 (40%): 조향각, 토크, 모델 확신도를 봉인한 유효한 Ed25519 암호화 블랙박스 영수증 제출"
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
                "term": "Spatial Consistency Proof",
                "def": "Empirical verification that 3D world landmarks retain geometric coordinates across 360-degree camera rotations.",
                "defKo": "3D 공간 항상성 실증"
            }
        ]
    },
    # Slide 38: Next Horizon: Calculated Visuals, SVG & LaTeX
    {
        "num": 38,
        "type": "content",
        "title": "NEXT HORIZON: CALCULATED VISUALS & LATEX",
        "subtitle": "Moving from neural 3D raster pixels to crisp, deterministic mathematical vector graphics",
        "points": [
            "From Raster to Vectors: Why pixel images blur on 4K screens while mathematical vector SVGs remain infinitely crisp.",
            "Sub-Kilobyte Visual Assets: Generating complex architectural diagrams and CAD schematics in 2KB of pure SVG code.",
            "Session 13 Preview: HTML5 Canvas, WebGL parametric equations, and publication-grade LaTeX mathematical rendering."
        ],
        "script": (
            "[TA Sarah] Slide 38 previews our next exciting horizon: \"NEXT HORIZON: CALCULATED VISUALS, SVG & LATEX SYSTEMS.\"\n\n"
            "[TA James] In Session 13, we transition from heavy 3D neural pixels to crisp, lightweight mathematical vectors! We will deconstruct Calculated Visuals—writing sub-kilobyte Scalable Vector Graphics (SVG), HTML5 Canvas parametric equations, and publication-ready LaTeX mathematical typography!\n\n"
            "[Prof. Peter] We will see how vector mathematics delivers infinite crisp resolution with zero pixel blur.\n\n"
            "[TA Sarah] Let us inspect the Architect's Spatial Reverence on Slide 39!"
        ),
        "koreanGuide": {
            "summary": "다음 지평 예고: Session 13 계산된 시각화(Calculated Visuals), SVG 및 LaTeX 수학 시스템",
            "points": [
                "래스터에서 벡터로: 4K 화면에서 깨지는 픽셀 비트맵을 극복하는 무한 해상도의 수학적 SVG 벡터",
                "1KB 미만 초경량 그래픽: 복잡한 건축 다이어그램과 CAD 도면을 단 2KB의 순수 SVG 코드로 작성",
                "Session 13 연계: HTML5 캔버스 매개변수 방정식과 논문 조판용 정밀 LaTeX 수식 렌더링 예고"
            ],
            "tips": "사라 조교와 제임스 조교가 다음 강의(Session 13: SVG & LaTeX)의 경이로운 수학적 벡터 미학을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Calculated Visuals",
                "def": "The programmatic generation of visual charts, diagrams, and CAD schematics using exact mathematical vector formulas.",
                "defKo": "계산된 시각화 (Calculated Visuals)"
            },
            {
                "term": "Resolution-Independent Vector",
                "def": "Graphical assets defined by mathematical coordinate curves maintaining razor-sharp rendering at any zoom level.",
                "defKo": "무한 해상도 벡터 그래픽"
            }
        ]
    },
    # Slide 39: The Architect's Spatial Reverence
    {
        "num": 39,
        "type": "content",
        "title": "THE ARCHITECT'S SPATIAL REVERENCE",
        "subtitle": "Treating simulated and physical space as a sacred domain of divine order, beauty, and safety",
        "points": [
            "Reverence for Creation: Recognizing that spatial physics, light, and gravity reflect the eternal wisdom of God.",
            "Building Safe Sanctuaries: Refusing to build reckless physical systems that endanger human life or degrade human dignity.",
            "Eternal Vocation: Exercising humble stewardship over autonomous machines to protect, heal, and serve humanity."
        ],
        "script": (
            "[Prof. Peter] Slide 39 reflects on \"THE ARCHITECT'S SPATIAL REVERENCE.\" In an age of autonomous machines, reverence is our guide.\n\n"
            "[TA Sarah] When we design spatial world models and autonomous robots that share physical space with human beings, we treat human life and creation with absolute sacred reverence.\n\n"
            "[TA James] We build autonomous systems that are gentle, reliable, and worthy of human trust.\n\n"
            "[Prof. Peter] Let us inspect our fourth enterprise case study on Slide 40!"
        ),
        "koreanGuide": {
            "summary": "지능 건축가의 공간적 경외감: 인간 생명과 창조 질서를 향한 거룩한 청지기직",
            "points": [
                "창조 세계를 향한 경외: 공간 물리, 빛, 중력 속에 깃든 하나님의 영원한 지혜를 겸손히 인정",
                "안전한 안식처 구축: 인간의 생명을 위태롭게 하거나 존엄성을 훼손하는 무모한 기계 설계 단호히 배격",
                "영원한 소명: 인간을 보호하고 치유하며 섬기기 위해 자율 기계를 지혜롭게 다스리는 청지기직 수행"
            ],
            "tips": "피터 교수가 자율 기계와 인간이 공존하는 공간 윤리와 신앙적 경외감을 감동적으로 선포합니다."
        },
        "keyTerms": [
            {
                "term": "Spatial Reverence",
                "def": "The ethical and philosophical commitment to designing physical AI systems that prioritize human safety and ecological sanctity.",
                "defKo": "공간 윤리적 경외감"
            },
            {
                "term": "Sacred Space Invariant",
                "def": "The non-negotiable rule that autonomous machines must never violate human bodily safety or physical autonomy.",
                "defKo": "인간 신체 불가침 안전 불변식"
            }
        ]
    },
    # Slide 40: Case Study 4: Industrial Robotics Factory Digital Twin
    {
        "num": 40,
        "type": "casestudy",
        "title": "CASE STUDY 4: FACTORY DIGITAL TWIN",
        "subtitle": "Global Automotive Mega-Factory uses Genie 3 Digital Twin for zero-downtime assembly line retooling",
        "company": "Top Global Electric Vehicle Manufacturer",
        "problem": "Retooling physical factory assembly lines for a new EV model traditionally required 6 weeks of factory shutdown, costing $90M in lost vehicle production.",
        "solution": "Built high-fidelity Genie 3 digital twin of 2,000 industrial robot arms, conveyor belts, and tactile weld grippers: simulated 1,000 retooling variations.",
        "impact": "Completed 100% of robot calibration in simulation; reduced physical factory retooling shutdown from 6 weeks to 36 hours; saved $84M in production losses.",
        "script": (
            "[Prof. Peter] Slide 40 presents \"CASE STUDY 4: INDUSTRIAL ROBOTICS FACTORY DIGITAL TWIN.\"\n\n"
            "[TA Sarah] A top electric vehicle mega-factory needed to retool its entire assembly line for a new battery architecture. Traditionally, retooling 2,000 industrial robotic arms requires shutting down the factory for 6 weeks, costing 90 million dollars in lost vehicle output!\n\n"
            "[TA James] They built a complete Genie 3 Digital Twin of the factory: simulating conveyor speeds, robotic arm torque limits, and tactile welding physics across 1,000 parallel variations!\n\n"
            "[Prof. Peter] Every robotic arm's trajectory was 100% calibrated in simulation! When the physical factory stopped, retooling took only 36 hours over a weekend rather than 6 weeks—saving 84 million dollars and getting new EVs onto roads instantly!\n\n"
            "[TA Sarah] Let us inspect our capstone enterprise case study on Slide 44!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 4: 전기차 공장 2,000대 로봇의 지니 3 디지털 트윈 캘리브레이션 (8,400만 달러 절감)",
            "points": [
                "문제 상황: 신형 전기차 배터리 라인 교체를 위해 2,000대 로봇을 재조정하는 데 6주간 공장 가동 중단 및 9,000만 달러 손실",
                "솔루션: 지니 3 디지털 트윈에서 컨베이어 속도, 로봇 팔 토크 한계, 용접 물리 시뮬레이션 1,000회 사전 가동",
                "성과: 시뮬레이션에서 100% 사전 보정 완료 ➔ 실제 라인 교체 기간 6주에서 주말 36시간으로 단축, 8,400만 달러 손실 방어"
            ],
            "tips": "사라 조교와 제임스 조교가 6주간의 공장 셧다운을 36시간 만에 끝낸 디지털 트윈의 경제성을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Zero-Downtime Factory Retooling",
                "def": "Pre-calibrating physical industrial robotics within a digital twin to minimize manufacturing facility downtime.",
                "defKo": "무중단 공장 라인 재조정"
            },
            {
                "term": "Robotic Kinematic Twin",
                "def": "A high-fidelity simulation model accurately reproducing the mass, gear backlash, and trajectory kinematics of industrial robots.",
                "defKo": "로봇 기구학적 디지털 트윈"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 41: The Economics of Physical Simulation
    {
        "num": 41,
        "type": "content",
        "title": "THE ECONOMICS OF PHYSICAL SIMULATION",
        "subtitle": "Compressing $100M physical prototyping budgets into $10,000 cloud simulation runs",
        "points": [
            "The 10,000X Cost Collapse: A physical crash test costs $250,000; a simulated crash test in Genie 3 costs $0.02.",
            "Safety without Sacrifice: Testing catastrophic failure boundaries that would be lethal in physical reality.",
            "Democratizing Innovation: Allowing small startups and university labs to build aerospace-grade autonomous systems."
        ],
        "script": (
            "[Prof. Peter] Slide 41 analyzes \"THE ECONOMICS OF PHYSICAL SIMULATION: The 10,000X Cost Collapse.\"\n\n"
            "[TA Sarah] Look at the economic numbers: Destroying a physical car in an automotive crash test costs $250,000. Running that exact same crash test in Genie 3 costs 2 cents in cloud compute!\n\n"
            "[TA James] That is a 10,000X cost collapse! It allows small startups and university scholars to build autonomous physical systems with the same safety standards as aerospace defense contractors!\n\n"
            "[Prof. Peter] Let us inspect Redeeming Time on Slide 42."
        ),
        "koreanGuide": {
            "summary": "물리 시뮬레이션의 경제학: 10,000배의 비용 붕괴 (25만 달러 ➔ 2센트)",
            "points": [
                "10,000배 비용 절감: 실제 차량 파괴 충돌 시험 1회당 25만 달러 ➔ 지니 3 가상 충돌 1회당 단 2센트(0.02달러)",
                "희생 없는 절대 안전: 현실에서는 위험해서 불가능한 극한 파괴 한계선까지 무한 스트레스 테스트",
                "혁신의 민주화: 소규모 스타트업과 대학 연구실도 항공우주 대기업 수준의 첨단 자율 시스템 구축 가능"
            ],
            "tips": "제임스 조교가 25만 달러짜리 충돌 시험이 2센트로 줄어드는 1만 배 비용 혁신을 통쾌하게 설명합니다."
        },
        "keyTerms": [
            {
                "term": "10,000X Cost Collapse",
                "def": "The radical financial efficiency achieved by replacing destructive physical testing with high-fidelity neural simulation.",
                "defKo": "10,000배 물리 테스트 비용 붕괴"
            },
            {
                "term": "Democratized Physical Prototyping",
                "def": "Enabling resource-constrained developers to build aerospace-grade physical AI systems via low-cost cloud simulation.",
                "defKo": "물리 프로토타이핑 민주화"
            }
        ]
    },
    # Slide 42: Redeeming the Time: Asynchronous Delegation
    {
        "num": 42,
        "type": "content",
        "title": "REDEEMING THE TIME: ASYNCHRONOUS DELEGATION",
        "subtitle": "Ephesians 5:16: Delegating 10,000-mile simulation runs overnight to wake up to verified autonomous policies",
        "points": [
            "Overnight Fleet Validation: Launching 5,000 virtual driving runs at 8:00 PM; reviewing audited Pareto frontiers at 8:00 AM.",
            "Reclaiming Focus: Liberating engineers from manual test-track driving to concentrate on novel algorithmic breakthroughs.",
            "The Divine Calling: Dedicating our redeemed life bandwidth to honoring God and loving our neighbor."
        ],
        "script": (
            "[TA Sarah] Slide 42 proclaims \"REDEEMING THE TIME: ASYNCHRONOUS FLEET DELEGATION.\"\n\n"
            "[TA James] As Intelligence Architects, we launch 5,000 virtual vehicle simulation runs before going to bed. While we rest peacefully, the TPU cluster tests millions of hazard miles!\n\n"
            "[Prof. Peter] In the morning, we inspect the audited Pareto frontier of safety metrics and deploy verified models with total peace of mind. We redeem finite time for God's eternal glory.\n\n"
            "[TA Sarah] Let us inspect the Future of Physical AI on Slide 43!"
        ),
        "koreanGuide": {
            "summary": "세월을 아끼라: 비동기 위임을 통한 밤샘 5,000대 시뮬레이션과 생애 시간 구속",
            "points": [
                "밤샘 비동기 위임: 저녁 8시에 5,000대 가상 주행 실행 ➔ 아침 8시에 파레토 최적 안전 곡선 검토",
                "테스트 트랙 노역 해방: 하루 종일 주행 트랙을 운전하던 수작업에서 벗어나 알고리즘 설계에 몰입",
                "구속된 생애 시간: 확보된 시간과 지적 에너지를 하나님을 영화롭게 하고 이웃을 섬기는 데 온전히 투자"
            ],
            "tips": "피터 교수가 밤샘 비동기 위임의 신학적 시간 구속 가치를 에베소서 말씀과 연결합니다."
        },
        "keyTerms": [
            {
                "term": "Asynchronous Fleet Delegation",
                "def": "Initiating large-scale autonomous simulation workloads that execute unattended across cloud clusters.",
                "defKo": "비동기 가상 함대 위임"
            },
            {
                "term": "Pareto Safety Frontier",
                "def": "The optimal curve balancing autonomous vehicle speed, comfort, and safety margins under uncertainty.",
                "defKo": "파레토 최적 안전 곡선"
            }
        ]
    },
    # Slide 43: The Future of Physical AI: The Sovereign Horizon
    {
        "num": 43,
        "type": "content",
        "title": "THE FUTURE OF PHYSICAL AI: SOVEREIGN HORIZON",
        "subtitle": "Uniting Spatial World Models, True AI Science, and Multi-Agent Swarms under Soli Deo Gloria",
        "points": [
            "The Grand Convergence: Swarms (Session 10) + Scientific Deduction (Session 11) + World Models (Session 12).",
            "Autonomous Planetary Guardianship: Directing intelligent systems to monitor climate, prevent disasters, and build sustainable cities.",
            "The Architect's Victory: Leading the technological era with wisdom, ethical courage, and uncompromising truth."
        ],
        "script": (
            "[Prof. Peter] Slide 43 unveils \"THE FUTURE OF PHYSICAL AI: THE SOVEREIGN HORIZON.\"\n\n"
            "[TA Sarah] Look at the magnificent convergence of our masterclass: In Session 10, we mastered Multi-Agent Swarms. In Session 11, we mastered True AI Science. And today in Session 12, we mastered 3D Spatial World Models!\n\n"
            "[TA James] When these three powers unite, you possess the capability to build autonomous planetary guardians—systems that protect human life, eliminate energy waste, and reflect divine excellence!\n\n"
            "[Prof. Peter] Let us inspect our capstone enterprise case study on Slide 44!"
        ),
        "koreanGuide": {
            "summary": "물리 AI의 미래: 3대 거대 축의 융합과 주권적 지평",
            "points": [
                "거대한 융합(Convergence): 93개 스웜(Session 10) + 과학적 연역(Session 11) + 3D 월드 모델(Session 12)",
                "지구 행성 수호 지능: 기후 변화 감시, 재난 구호, 지속 가능한 스마트 시티를 이끄는 자율 지능 군단",
                "지능 건축가의 승리: 지혜와 도덕적 용기, 비타협적 진실성으로 무장하여 미래 기술 문명을 주도"
            ],
            "tips": "사라 조교와 피터 교수가 10, 11, 12강이 하나로 결합하는 거대한 기술적 정점을 웅장하게 선언합니다."
        },
        "keyTerms": [
            {
                "term": "Grand AI Convergence",
                "def": "The unified integration of multi-agent swarm concurrency, scientific deduction engines, and 3D physical world models.",
                "defKo": "인공지능 대통합 (Grand Convergence)"
            },
            {
                "term": "Planetary AI Guardianship",
                "def": "Deploying autonomous physical intelligence systems to steward Earth's ecological health and human safety.",
                "defKo": "지구 생태 수호 지능"
            }
        ]
    },
    # Slide 44: Case Study 5: 50X Physical AI Training Velocity ROI Blueprint
    {
        "num": 44,
        "type": "casestudy",
        "title": "CASE STUDY 5: 50X PHYSICAL AI VELOCITY ROI",
        "subtitle": "Global Autonomous Logistics Conglomerate deploys Genie 3 across 12,000 autonomous delivery robots",
        "company": "Top Global Autonomous Logistics & Delivery Conglomerate",
        "problem": "Company operated 12,000 sidewalk delivery robots across 40 metropolitan campuses; pedestrian navigation failures caused 200 service disruptions daily, costing $15M annually.",
        "solution": "Deployed centralized Genie 3 world simulation cluster: trained 12,000 robot policies across 100 million simulated sidewalk pedestrian congestion scenarios.",
        "impact": "50X measured autonomous navigation training velocity; sidewalk delivery failures dropped by 96%; expanded delivery capacity by 300%; generated $58M in annual operating profit.",
        "script": (
            "[Prof. Peter] Slide 44 presents our capstone enterprise case study: \"CASE STUDY 5: 50X PHYSICAL AI TRAINING VELOCITY ROI BLUEPRINT.\"\n\n"
            "[TA Sarah] A global autonomous logistics leader with 12,000 sidewalk delivery robots had a major reliability crisis: crowded university sidewalks and complex pedestrian crosswalks caused 200 robot freeze-ups every day, losing 15 million dollars in failed deliveries!\n\n"
            "[TA James] They deployed our centralized Genie 3 World Model blueprint: training all 12,000 robots across 100 million procedurally generated sidewalk congestion scenarios with erratic bicyclists and running pedestrians!\n\n"
            "[Prof. Peter] Look at the enterprise outcome: navigation training velocity surged by 50X! Sidewalk freeze-ups collapsed by 96%, delivery capacity tripled, and the company generated 58 million dollars in new annual operating profit!\n\n"
            "[TA Sarah] That is the transformative power of World Models.\n\n"
            "[TA James] Now let us build your own Genie 3 World Simulation in Lab 12 on Slide 45!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 5: 12,000대 자율 배송 로봇의 50배 훈련 속도 혁신 및 5,800만 달러 영업이익",
            "points": [
                "문제 상황: 12,000대 인도 배송 로봇이 혼잡한 보행자와 자전거로 인해 일일 200회 멈춤 장애 발생 (연 1,500만 달러 손실)",
                "솔루션: 지니 3 월드 모델을 통해 1억 건의 극한 보행자 혼잡 시나리오를 초병렬 가상 훈련",
                "성과: 훈련 속도 50배 가속, 인도 멈춤 장애 96% 급감, 배송 처리량 3배 확장, 연간 5,800만 달러 신규 영업이익 창출"
            ],
            "tips": "사라 조교와 제임스 조교가 12,000대 로봇 군단의 압도적 영업이익 창출 성과를 전하며 실습으로 유도합니다."
        },
        "keyTerms": [
            {
                "term": "50X Training Velocity Multiplier",
                "def": "The exponential acceleration of physical robot policy training achieved via high-density neural world simulation.",
                "defKo": "50배 물리 AI 훈련 속도 승수"
            },
            {
                "term": "Sidewalk Congestion Navigation",
                "def": "Autonomous robotic path-planning safely negotiating dense, erratic human pedestrian environments.",
                "defKo": "고밀도 인도 보행자 혼잡 자율 주행"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 45: Hands-on Lab 12 & Conclusion
    {
        "num": 45,
        "type": "lab",
        "title": "🛠️ HANDS-ON LAB 12 & CONCLUSION",
        "subtitle": "Constructing an Interactive Genie 3 3D World Simulation & Waymo Agent",
        "mission": "Build a playable 3D world simulation using Google Genie 3 APIs, ingest a satellite elevation bounding box, deploy a virtual driving agent, inject real-time dynamic weather prompt events, and verify collision-free navigation with an Ed25519 cryptographic receipt.",
        "steps": [
            "Step 1: Ingest a satellite GPS bounding box or 2D photograph into the Genie 3 VMC Vision module.",
            "Step 2: Generate the 3D spatio-temporal neural volume with rigid-body terrain physics at 60 FPS.",
            "Step 3: Connect a virtual driving agent policy to the VMC Controller token stream.",
            "Step 4: Execute a real-time prompt event mutation: 'Trigger sudden torrential rainstorm and road puddle hydroplaning'.",
            "Step 5: Verify that the agent slows down, recovers traction, and export the Ed25519 signed black box telemetry packet!"
        ],
        "script": (
            "[TA Sarah] Here we are at Slide 45: \"🛠️ HANDS-ON LAB 12 & SESSION CONCLUSION!\"\n\n"
            "[TA James] Tonight's hands-on lab turns you into a World Model Architect! Step 1: Ingest your satellite GPS coordinates. Step 2: Generate your 60 FPS 3D neural world. Step 3: Connect your autonomous driving agent! Step 4: Trigger a sudden torrential rainstorm via real-time prompt events! Step 5: Verify that your agent survives without crashing and export your Ed25519 signed black box receipt!\n\n"
            "[Prof. Peter] Once you master constructing interactive 3D world simulations, you hold the keys to the future of robotics and physical artificial intelligence.\n\n"
            "[TA Sarah] In our next session, Session 13, we master Calculated Visuals: Scalable Vector Graphics (SVG), HTML5 Canvas, and LaTeX Mathematical Systems!\n\n"
            "[Prof. Peter] On behalf of TA Sarah Jenkins, TA James Wilson, and the entire Smart Insight Lab, congratulations on mastering Session 12! Soli Deo Gloria, and we will see you in Session 13!"
        ),
        "koreanGuide": {
            "summary": "실습 과제 12 및 세션 마무리: 대화형 지니 3 3D 월드 시뮬레이션 및 자율주행 에이전트 구축",
            "points": [
                "실습 미션: 위성 GPS 좌표 또는 사진을 넣어 지니 3 60 FPS 3D 신경망 세계 생성",
                "가상 주행 에이전트 연결 및 '갑작스러운 폭우 및 수막현상' 실시간 프롬프트 이벤트 주입",
                "감속 및 접지력 회복 확인 후 Ed25519 암호화 블랙박스 영수증 내보내기"
            ],
            "tips": "3인의 강사진이 오늘 수업의 성취를 축하하고 다음 세션(Session 13: Calculated Visuals & LaTeX)에 대한 기대감을 높이며 마무리합니다."
        },
        "keyTerms": [
            {
                "term": "Hands-on Milestone",
                "def": "The practical engineering completion of a functioning technical artifact fulfilling the session's learning objectives.",
                "defKo": "실습 달성 마일스톤"
            },
            {
                "term": "World Model Architect Certification",
                "def": "The formal mastery of generative 3D simulation authoring, real-time physics event handling, and cryptographic safety verification.",
                "defKo": "월드 모델 아키텍트 마스터 인증"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    }
]

def generate_session12_md(slides):
    lines = []
    lines.append("# Session 12: World Models: Genie 3 Simulation & Waymo Autonomous Training")
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
    new_export = f"export const SLIDES_SESSION_12 = {slides_json};"
    
    pattern = r"export\s+const\s+SLIDES_SESSION_12\s*=\s*\[[\s\S]*?\];"
    if re.search(pattern, content):
        updated_content = re.sub(pattern, lambda m: new_export, content, count=1)
        with open(SLIDES_DATA_JS, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Successfully updated SLIDES_SESSION_12 in slidesData.js!")
    else:
        print("Could not find SLIDES_SESSION_12 pattern in slidesData.js!")

def main():
    print(f"Total slides configured: {len(SLIDES_45_SESSION_12)}")
    
    # Verify part dividers
    part_slides = [s for s in SLIDES_45_SESSION_12 if s['type'] == 'section']
    print(f"Total PART Section Slides: {len(part_slides)}")
    for ps in part_slides:
        print(f"  Slide {ps['num']:02d}: {ps['title']}")
        
    # Verify case studies
    case_slides = [s for s in SLIDES_45_SESSION_12 if 'CASE STUDY' in s['title']]
    print(f"Total Case Study Slides: {len(case_slides)}")
    for cs in case_slides:
        print(f"  Slide {cs['num']:02d}: {cs['title']}")

    # 1. Write session12.md
    session12_md_content = generate_session12_md(SLIDES_45_SESSION_12)
    with open(SESSION12_MD, 'w', encoding='utf-8') as f:
        f.write(session12_md_content)
    print(f"Successfully generated and saved {SESSION12_MD} ({len(session12_md_content)} bytes)")
    
    # 2. Update slidesData.js
    update_slides_data_js(SLIDES_45_SESSION_12)
    
    print("Session 12 generation completed successfully!")

if __name__ == '__main__':
    main()
