# -*- coding: utf-8 -*-
"""
Oikos University - Session 14 Clean 45-Slide Master Generator
Course: The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom
Session 14: Cinematic AI Pipelines: Google Flow AI vs. Runway ML Hybrid Strategy
Features:
- Full 45 Slides with 3-Presenter Trio (Prof. Peter Kim, TA Sarah Jenkins, TA James Wilson)
- Clean 4-Part Structure (Part 1: Slide 2, Part 2: Slide 12, Part 3: Slide 23, Part 4: Slide 34)
- 5 Practical Enterprise Case Studies:
    1. Slide 11: Hollywood Studio 4K Feature Film Teaser Produced in 72 Hours for $15K
    2. Slide 22: Global Luxury Automaker Multi-Country Commercial Video Campaign
    3. Slide 33: International Crisis Journalism Documentary Synthesized in 24 Hours
    4. Slide 40: AAA Video Game Studio Interactive Cinematic Cutscenes at 1/100th Cost
    5. Slide 44: 80% Production Cost Slicing & Enterprise Video ROI Blueprint
- Full sync with session14.md and slidesData.js (SLIDES_SESSION_14)
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
SESSION14_MD = os.path.join(BASE_DIR, "session14.md")

SLIDES_45_SESSION_14 = [
    # Slide 1: Course Title
    {
        "num": 1,
        "type": "title",
        "title": "OIKOS UNIVERSITY • SOLI DEO GLORIA",
        "subtitle": "THE ARCHITECT OF INTELLIGENCE: Mastering Agentic IT & Strategic Wisdom",
        "detail": "Session 14: Cinematic AI Pipelines: Google Flow AI vs. Runway ML Hybrid Strategy",
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab",
        "script": (
            "[Prof. Peter] Welcome back, global scholars, creators, and architects, to Oikos University! I am Professor Peter Kim, Director of Smart Insight Lab. Today on Slide 1, we step into the director's chair of the visual media revolution: \"Session 14: Cinematic AI Pipelines: Google Flow AI vs. Runway ML Hybrid Strategy.\"\n\n"
            "[TA Sarah] Hello everyone! I am Sarah Jenkins, Senior AI Fellow. For over a century, filmmaking required millions of dollars in physical cameras, lighting rigs, soundstages, and months of post-production. Today, we drop the physical camera and transition to Generative Multi-Model Curation!\n\n"
            "[TA James] And I am James Wilson, your DevOps TA! In Session 14, we deconstruct the clash and synergy of the two visual titans: Google Flow AI's Trinity architecture (Gemini + Imagen + Veo 3.1 + Lyria 3 Pro audio) and Runway ML's precision motion cockpit (Gen-3 Alpha, Motion Brush, and Act-Two performance transfer)!\n\n"
            "[Prof. Peter] Under our founding motto, \"SOLI DEO GLORIA—To God Alone Be the Glory,\" let us master cinematic generative pipelines to broadcast messages of truth, hope, and divine beauty to the ends of the Earth.\n\n"
            "[TA Sarah] Let us open Part 1 and explore Dropping the Camera on Slide 2!"
        ),
        "koreanGuide": {
            "summary": "Session 14 개요 및 Oikos University 3인 강사진(피터 교수, 사라 수석조교, 제임스 개발조교) 환영 인사",
            "points": [
                "강의 주제: 시네마틱 AI 파이프라인: 구글 Flow AI vs 런웨이(Runway) ML 하이브리드 전략",
                "물리적 카메라의 종말과 생성형 멀티모델 큐레이션(Generative Multi-Model Curation)으로의 패러다임 전환",
                "구글 Flow AI(Veo 3.1 + Lyria 3 Pro 네이티브 오디오)와 Runway Gen-3 Alpha(모션 브러시 + Act-Two)의 정밀 비교"
            ],
            "tips": "피터 교수의 시네마틱 스토리텔링 철학, 사라 조교의 멀티모델 아키텍처 분석, 제임스 조교의 80% 제작비 절감 파이프라인 관점을 결합하세요."
        },
        "keyTerms": [
            {
                "term": "Generative Cinema Pipeline",
                "def": "An end-to-end video production workflow driven entirely by multimodal AI generation without physical camera capture.",
                "defKo": "생성형 시네마틱 파이프라인"
            },
            {
                "term": "Google Flow AI",
                "def": "Google's unified creative studio integrating Gemini storyboarding, Imagen 4 visuals, Veo 3.1 video, and Lyria 3 Pro audio.",
                "defKo": "구글 Flow AI"
            }
        ]
    },
    # Slide 2: Part 1 Section Divider
    {
        "num": 2,
        "type": "section",
        "title": "PART 1: DROPPING THE CAMERA: FROM CAPTURE TO GENERATIVE CURATION",
        "subtitle": "Transcending the slot-machine randomness of single prompts and establishing deterministic cinematic control",
        "script": (
            "[TA Sarah] Look at Slide 2: \"PART 1: DROPPING THE CAMERA: FROM CAPTURE TO GENERATIVE CURATION.\" Professor, why do amateur creators get frustrated with AI video generators?\n\n"
            "[Prof. Peter] Because they treat AI video like a casino slot machine! They type a single vague text prompt, pull the lever, get an uncontrollable random 4-second clip with mutating fingers, and wonder why they cannot make a coherent movie!\n\n"
            "[TA James] Professional Intelligence Architects do not gamble! We build deterministic multi-stage pipelines: locking character facial identities, scripting camera dolly and pan trajectories, and syncing 48kHz spatial audio to exact musical beat drops!\n\n"
            "[TA Sarah] In Part 1, we deconstruct the 2026 video landscape and slice production costs by 80%.\n\n"
            "[Prof. Peter] Let us examine mechanical capture vs. generative curation on Slide 3."
        ),
        "koreanGuide": {
            "summary": "Part 1 섹션 전환: 카메라 촬영에서 생성형 큐레이션으로의 도약",
            "points": [
                "아마추어의 슬롯머신 도박 탈출: 막연한 프롬프트로 기형 손가락 클립을 뽑아내는 랜덤성 극복",
                "전문가의 결정론적 시네마틱 제어: 캐릭터 얼굴 일관성 고정, 카메라 패닝/트래킹 궤적 통제, 48kHz 비트 싱크 오디오",
                "제작 비용 80% 절감과 상업용 영상 파이프라인의 산업적 표준 수립"
            ],
            "tips": "사라 조교가 슬롯머신 도박의 한계를 짚고 제임스가 결정론적 제어의 쾌감을 선언합니다."
        },
        "keyTerms": [
            {
                "term": "Slot-Machine Generation Trap",
                "def": "The naive practice of relying on randomized text prompts without structured camera, character, or audio constraints.",
                "defKo": "슬롯머신형 프롬프트 생성의 덫"
            },
            {
                "term": "Deterministic Cinematic Control",
                "def": "The precise programmatic orchestration of camera angles, lighting vectors, actor identities, and timeline pacing.",
                "defKo": "결정론적 시네마틱 제어"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 3: From Mechanical Capture to Generative Curation
    {
        "num": 3,
        "type": "content",
        "title": "FROM MECHANICAL CAPTURE TO GENERATIVE CURATION",
        "subtitle": "Why the film industry is moving from hardware logistics to prompt-directed latent exploration",
        "points": [
            "The Hardware Heavyweight Era: Transporting 20 tons of cameras, cranes, lighting trucks, and catering to remote locations.",
            "The Generative Latent Frontier: Generating photorealistic 4K cinematic scenes in seconds from the director's laptop.",
            "The Director as Sovereign Conductor: Curating the infinite latent possibilities into a cohesive narrative vision."
        ],
        "script": (
            "[Prof. Peter] Slide 3 examines \"FROM MECHANICAL CAPTURE TO GENERATIVE CURATION.\"\n\n"
            "[TA Sarah] For 120 years, shooting a movie required enormous physical logistics: renting soundstages, flying 100 crew members to Iceland, hauling 20 tons of lighting cranes, and waiting 8 hours for the sunset!\n\n"
            "[TA James] Today, you open your browser: In Google Flow AI or Runway, you command: '4K anamorphic lens, golden hour sunset over volcanic black sand beach, dramatic drone tracking shot following lone samurai.' The entire scene renders in 30 seconds!\n\n"
            "[Prof. Peter] You are no longer constrained by budget or weather; you are limited only by the depth of your vision.\n\n"
            "[TA Sarah] Let us inspect the real-world 2026 landscape on Slide 4."
        ),
        "koreanGuide": {
            "summary": "물리적 촬영에서 생성형 큐레이션으로: 20톤 장비와 100명 스태프를 대체하는 랩톱 스튜디오",
            "points": [
                "하드웨어 노역 시대: 아이슬란드 로케이션, 20톤 조명 크레인, 8시간의 일몰 대기",
                "잠재 공간 탐색: 랩톱에서 '화산재 해변 위 황금빛 일몰 드론 트래킹'을 30초 만에 4K로 렌더링",
                "지휘관으로서의 감독: 물리적 예산과 날씨의 한계를 부수고 오직 서사적 비전에만 집중"
            ],
            "tips": "사라 조교와 피터 교수가 거대한 영화 촬영 현장이 랩톱 한 대로 압축되는 영화사의 대격변을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Generative Curation",
                "def": "The creative process of directing, selecting, pruning, and synthesizing AI-generated video and audio streams.",
                "defKo": "생성형 큐레이션 (Generative Curation)"
            },
            {
                "term": "Anamorphic Cinematic Rendering",
                "def": "Simulating the wide aspect ratio, oval bokeh, and blue horizontal lens flares of high-end cinematic camera lenses.",
                "defKo": "아나모픽 시네마틱 렌더링"
            }
        ]
    },
    # Slide 4: Sora 2 and Beyond: The Real-World 2026 Landscape
    {
        "num": 4,
        "type": "content",
        "title": "SORA 2 AND BEYOND: THE 2026 LANDSCAPE",
        "subtitle": "Analyzing the competitive landscape: Google Flow AI, Runway Gen-3 Alpha, Kling, and Sora 2",
        "points": [
            "Google Flow AI: Best for unified storyboards, actor facial identity locks, and integrated 48kHz audio/music.",
            "Runway ML (Gen-3): Best for granular Director Mode (5-channel Motion Brush, camera velocity vectors, Act-Two).",
            "Sora 2 & Kling: High visual fidelity but hindered by opaque API walls and lack of granular motion brush controls."
        ],
        "script": (
            "[Prof. Peter] Slide 4 maps \"SORA 2 AND BEYOND: THE REAL-WORLD 2026 LANDSCAPE.\"\n\n"
            "[TA Sarah] How do the top video AI platforms compare in 2026? Google Flow AI leads the world in All-in-One Storyboarding, Actor Identity Lock, and Native 48kHz Audio generation. Runway ML leads in Granular Motion Brush and Camera Direction Controls!\n\n"
            "[TA James] While Sora 2 produces pretty demo clips, it lacks developer APIs and granular motion brushes. Professional directors combine Flow AI for story/audio and Runway for precise camera trajectories!\n\n"
            "[Prof. Peter] Let us examine the interface trap and the casino of randomness on Slide 5."
        ),
        "koreanGuide": {
            "summary": "2026년 생성형 비디오 플랫폼 지형도: Flow AI, Runway, Sora 2, Kling 비교",
            "points": [
                "구글 Flow AI: 올인원 스토리보드, 배우 얼굴 일관성 고정, 48kHz 네이티브 오디오 및 음악 합성 최강",
                "Runway Gen-3: 5채널 모션 브러시, 카메라 속도 벡터 제어, Act-Two 연기 이식 등 정밀 연출 최강",
                "Sora 2 & Kling: 고화질 데모는 화려하나 개발자 API와 미세 모션 브러시 제어가 부족하여 상업용 파이프라인에 한계"
            ],
            "tips": "사라 조교와 제임스 조교가 실무에서 Flow AI와 Runway를 조합하는 하이브리드 전략의 당위성을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Multi-Model Hybrid Strategy",
                "def": "Combining the distinct specialized strengths of multiple generative AI models across a single production pipeline.",
                "defKo": "멀티모델 하이브리드 영상 전략"
            },
            {
                "term": "Actor Identity Lock",
                "def": "Preserving the precise facial geometry and clothing features of a character across dozens of distinct video scenes.",
                "defKo": "배우 얼굴 및 의상 일관성 고정"
            }
        ]
    },
    # Slide 5: The Interface Trap: Overcoming the Casino of Randomness
    {
        "num": 5,
        "type": "content",
        "title": "THE INTERFACE TRAP: CASINO OF RANDOMNESS",
        "subtitle": "Escaping prompt gambling through structured keyframe choreography and multi-image anchors",
        "points": [
            "The Randomness Trap: Typing 100 prompts to get 1 usable 3-second shot burns credits and creative energy.",
            "Multi-Image Anchor Pipeline: Feeding 3 reference images (Actor Face, Lighting Reference, Environment Mesh).",
            "Predictable Cinematic Yield: Increasing production-ready shot yield from 5% to 85% on the first take."
        ],
        "script": (
            "[TA Sarah] Slide 5 exposes \"THE INTERFACE TRAP: OVERCOMING THE CASINO OF RANDOMNESS.\"\n\n"
            "[TA James] If you just prompt 'A beautiful girl running through a cyber city', the AI invents a different face in every single generation! You waste $100 in credits and cannot assemble a sequence!\n\n"
            "[Prof. Peter] The professional solution is the Multi-Image Anchor Pipeline: You provide 3 visual anchors: Image A (Actor's Face), Image B (Lighting Moodboard), Image C (3D Environment). The generative model interpolates between anchors, boosting usable shot yield from 5% to 85%!\n\n"
            "[TA Sarah] Let us inspect Slicing Generation Costs by 80% on Slide 6."
        ),
        "koreanGuide": {
            "summary": "인터페이스의 덫: 프롬프트 도박을 극복하는 3중 다중 이미지 앵커 파이프라인",
            "points": [
                "랜덤성의 덫: 프롬프트를 100번 돌려 쓸 만한 1컷 건지느라 크레딧과 창작 에너지를 탕진하는 비극",
                "다중 이미지 앵커: 배우 얼굴(A), 조명 무드보드(B), 3D 배경 메쉬(C)의 3대 기준 이미지 주입",
                "결정론적 수율: 첫 렌더링에서 프로덕션 즉시 투입 가능한 컷 수율을 5%에서 85%로 수직 상승"
            ],
            "tips": "제임스 조교와 피터 교수가 3중 이미지 앵커로 크레딧 낭비를 막고 85% 수율을 달성하는 비결을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Multi-Image Anchoring",
                "def": "Conditioning video diffusion models on multiple synchronized reference images to constrain character and lighting consistency.",
                "defKo": "다중 이미지 앵커링"
            },
            {
                "term": "First-Take Production Yield",
                "def": "The percentage of AI-generated video shots that meet commercial broadcast standards on the initial generation run.",
                "defKo": "초회 렌더링 프로덕션 수율"
            }
        ]
    },
    # Slide 6: The Strategic Metric: Slicing Generation Costs by 80%
    {
        "num": 6,
        "type": "content",
        "title": "THE STRATEGIC METRIC: SLICING COSTS BY 80%",
        "subtitle": "Comparing traditional commercial video budgets ($250,000) with hybrid AI pipelines ($1,500)",
        "points": [
            "Traditional 60s Commercial: $250,000 budget, 45 crew members, 6 weeks of production and editing.",
            "Hybrid AI Pipeline: $1,500 total compute cost, 1 Intelligence Architect, 48 hours delivery.",
            "The 99.4% Economic Collapse: Democratizing high-end cinema for startups, churches, and non-profits worldwide."
        ],
        "script": (
            "[Prof. Peter] Slide 6 analyzes \"THE STRATEGIC METRIC: SLICING GENERATION COSTS BY 80%.\"\n\n"
            "[TA Sarah] Look at the economic numbers: A standard 60-second national television commercial traditionally costs $250,000, takes 6 weeks of filming, and requires 45 crew members!\n\n"
            "[TA James] With our Google Flow AI and Runway hybrid pipeline, a single Intelligence Architect produces a broadcast-quality 4K 60-second commercial in 48 hours for $1,500 in cloud compute credits!\n\n"
            "[Prof. Peter] That is a 99.4% economic collapse! It empowers small organizations and ministries to produce Hollywood-grade storytelling.\n\n"
            "[TA Sarah] Let us inspect Google Flow AI on Slide 7."
        ),
        "koreanGuide": {
            "summary": "전략적 지표: 25만 달러 상업 광고 제작비를 1,500달러로 99.4% 비용 절감",
            "points": [
                "전통 60초 TV 광고: 25만 달러(약 3억 3천만 원), 45명 스태프, 6주의 긴 제작 기간",
                "하이브리드 AI 파이프라인: 단 1,500달러(약 200만 원), 1명의 지능 건축가, 48시간 내 완결",
                "99.4% 비용 붕괴를 통해 스타트업과 비영리 단체, 선교 기관에 헐리우드급 영상 제작력 부여"
            ],
            "tips": "사라 조교와 제임스 조교가 25만 달러에서 1,500달러로 줄어드는 영상 제작비 혁명을 제시합니다."
        },
        "keyTerms": [
            {
                "term": "Commercial Video Cost Collapse",
                "def": "The radical reduction in media production expenditures achieved by substituting physical shooting with AI generative pipelines.",
                "defKo": "상업 영상 제작비 붕괴"
            },
            {
                "term": "Sovereign Director Productivity",
                "def": "The amplified creative output enabling a single individual to execute complete studio-grade film production.",
                "defKo": "1인 지휘관의 스튜디오급 생산성"
            }
        ]
    },
    # Slide 7: Google Flow AI: The All-in-One Creative Playground
    {
        "num": 7,
        "type": "content",
        "title": "GOOGLE FLOW AI: ALL-IN-ONE PLAYGROUND",
        "subtitle": "The integrated studio environment uniting scriptwriting, storyboarding, video synthesis, and audio scoring",
        "points": [
            "The Infinite Storyboard Canvas: Dragging prompt nodes to build complete narrative timelines.",
            "Unified Multimodal Backbone: Gemini 2.5 Pro writes the script, Imagen 4 paints keyframes, Veo 3.1 animates video.",
            "Native Audio Integration: Lyria 3 Pro generates synchronous sound effects (footsteps, explosions) and cinematic soundtracks."
        ],
        "script": (
            "[TA Sarah] Slide 7 introduces \"GOOGLE FLOW AI: THE ALL-IN-ONE CREATIVE PLAYGROUND.\"\n\n"
            "[TA James] Google Flow AI is not just a video generator; it is a full virtual studio! You write your script in Gemini, which automatically generates a 12-scene visual storyboard in Imagen 4, animates them with Veo 3.1, and scores the soundtrack with Lyria 3 Pro!\n\n"
            "[Prof. Peter] Everything is synchronized in a single unified workspace. No switching between 5 different disjointed tools!\n\n"
            "[TA Sarah] Let us inspect Runway ML on Slide 8."
        ),
        "koreanGuide": {
            "summary": "구글 Flow AI: 각본, 스토리보드, 비디오, 오디오가 통합된 가상 영화 스튜디오",
            "points": [
                "무한 스토리보드 캔버스: 프롬프트 노드를 연결하여 12개 씬의 서사 타임라인 구축",
                "통합 멀티모달 백본: Gemini 각본 작성 ➔ Imagen 4 키프레임 작화 ➔ Veo 3.1 4K 비디오 생성",
                "네이티브 오디오 통합: Lyria 3 Pro가 발소리, 폭발음, 시네마틱 배경음악을 타임라인에 자동 작곡"
            ],
            "tips": "제임스 조교와 피터 교수가 각본부터 오디오 작곡까지 단일 툴에서 끝나는 Flow AI의 통합성을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Unified Storyboard Canvas",
                "def": "An interactive node-based timeline interface synchronizing text scripts, visual keyframes, and audio tracks.",
                "defKo": "통합 스토리보드 캔버스"
            },
            {
                "term": "Multimodal Studio Synthesis",
                "def": "The automated coordination of text, image, video, and audio generative models within a single creative suite.",
                "defKo": "멀티모달 통합 스튜디오 합성"
            }
        ]
    },
    # Slide 8: Runway ML: The Precision-Control Cockpit
    {
        "num": 8,
        "type": "content",
        "title": "RUNWAY ML: THE PRECISION-CONTROL COCKPIT",
        "subtitle": "Mastering Gen-3 Alpha, 5-channel Motion Brush, and Director Camera Trajectories",
        "points": [
            "Gen-3 Alpha: Exceptional temporal motion stability and fluid physics simulation.",
            "5-Channel Motion Brush: Painting separate speed and direction vectors for water, smoke, characters, and clouds.",
            "Camera Controls: Exact pan, tilt, zoom, dolly, and roll sliders translated directly into 3D camera matrices."
        ],
        "script": (
            "[Prof. Peter] Slide 8 presents \"RUNWAY ML: THE PRECISION-CONTROL COCKPIT.\"\n\n"
            "[TA Sarah] Where Google Flow AI provides the broad story canvas, Runway ML gives you surgical camera precision! Look at the 5-Channel Motion Brush: You can paint Brush 1 on ocean waves to move left at speed 5, and Brush 2 on smoke to rise upward at speed 8!\n\n"
            "[TA James] And with Camera Controls, you dial in: 'Dolly Forward +3, Pan Right -15°, Roll 5°'—giving you the exact cinematic tracking shot of an Oscar-winning cinematographer!\n\n"
            "[TA Sarah] Let us launch an interactive poll on Slide 9."
        ),
        "koreanGuide": {
            "summary": "Runway ML: 5채널 모션 브러시와 정밀 카메라 궤적 제어 콕핏",
            "points": [
                "Gen-3 Alpha: 뛰어난 시간적 모션 안정성과 유체 역학적 물리 시뮬레이션",
                "5채널 모션 브러시: 파도는 왼쪽으로(속도 5), 연기는 위쪽으로(속도 8) 분리 페인팅",
                "카메라 궤적 제어: 돌리(Dolly), 팬(Pan), 틸트(Tilt), 롤(Roll)을 3D 매트릭스 수치로 완벽 통제"
            ],
            "tips": "사라 조교와 제임스 조교가 오스카 촬영감독의 카메라 무빙을 구현하는 런웨이의 정밀성을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "5-Channel Motion Brush",
                "def": "Runway's precision tool allowing users to paint distinct directional velocity vectors onto up to 5 scene layers.",
                "defKo": "5채널 모션 브러시 (Motion Brush)"
            },
            {
                "term": "Camera Dolly & Roll Matrix",
                "def": "Mathematical parameters dictating 3D virtual camera translation and rotational trajectory across video frames.",
                "defKo": "카메라 돌리 및 롤 3D 제어"
            }
        ]
    },
    # Slide 9: Interactive Poll: Where Does Your Video Pipeline Jam?
    {
        "num": 9,
        "type": "poll",
        "title": "📨 INTERACTIVE POLL: VIDEO PRODUCTION BOTTLENECK",
        "subtitle": "What is the biggest hurdle in your current video and multimedia creation workflow?",
        "pollOptions": [
            "Option A: Character face morphing and inconsistency across different scenes",
            "Option B: Uncontrollable camera movements and random unwanted object mutations",
            "Option C: High credit consumption and cloud rendering subscription costs",
            "Option D: Finding synchronized cinematic music, Foley sound effects, and voiceovers"
        ],
        "script": (
            "[Prof. Peter] Slide 9 is our \"INTERACTIVE POLL: VIDEO PRODUCTION BOTTLENECKS.\" Grab your smartphones and vote right now!\n\n"
            "[TA Sarah] The question is: \"What is the most frustrating hurdle in your current video creation and multimedia pipelines?\"\n\n"
            "[TA James] Option A: Character face morphing across scenes. Option B: Uncontrollable camera movements. Option C: Burning expensive credits. Or Option D: Missing audio and music sound effects!\n\n"
            "[TA Sarah] Option A (Face Morphing) and Option D (Missing Audio) have over 75% of the live votes!\n\n"
            "[Prof. Peter] Let us examine how Google Flow AI's Trinity architecture solves character identity and native audio on Slide 10."
        ),
        "koreanGuide": {
            "summary": "실시간 수강생 설문: 영상 제작 파이프라인의 최대 병목은?",
            "points": [
                "수강생 참여를 통해 AI 영상 제작 현장의 가장 심각한 고통 진단",
                "얼굴 왜곡(Face Morphing), 카메라 통제 불능, 비싼 크레딧, 효과음/음악 부재 중 식별",
                "구글 Flow AI와 런웨이 하이브리드 파이프라인이 해결할 구체적 솔루션 예고"
            ],
            "tips": "3인의 강사진이 얼굴 일관성과 오디오 결핍이라는 실제 고통을 짚으며 2부 엔진룸으로 이끕니다."
        },
        "keyTerms": [
            {
                "term": "Production Bottleneck Audit",
                "def": "Identifying friction points in video synthesis pipelines that impede commercial broadcast deployment.",
                "defKo": "영상 제작 병목 감사"
            },
            {
                "term": "Character Consistency Deficit",
                "def": "The unintended transformation of actor facial geometry between sequential video generation prompts.",
                "defKo": "캐릭터 일관성 결핍 결함"
            }
        ]
    },
    # Slide 10: Part 1 Transition: Inside the Engine Room of Google Flow AI
    {
        "num": 10,
        "type": "content",
        "title": "PART 1 TRANSITION: ENTERING THE ENGINE ROOM",
        "subtitle": "Connecting video philosophy to Veo 3.1 physics, Lyria 3 Pro audio, and actor identity locking",
        "points": [
            "From Tools to Synergy: How do Gemini, Imagen, Veo, and Lyria coordinate inside a single generative loop?",
            "Native 48kHz Audio: Generating authentic spatial Foley sounds matching on-screen physical impacts.",
            "The Roadmap Ahead: Master Flow AI in Part 2, Runway in Part 3, and Hybrid Pipelines in Part 4."
        ],
        "script": (
            "[Prof. Peter] Slide 10 bridges our roadmap: \"PART 1 TRANSITION: ENTERING THE ENGINE ROOM OF GOOGLE FLOW AI.\"\n\n"
            "[TA Sarah] We know the vision. Now, how does Google's Trinity architecture actually work under the hood?\n\n"
            "[TA James] In Part 2, we dissect Veo 3.1's spatio-temporal physics, Lyria 3 Pro's 48kHz native audio synthesis, Ingredients-to-Video actor locking, and the programmatic Interactions API!\n\n"
            "[Prof. Peter] Let us examine our first real-world Hollywood enterprise case study on Slide 11!"
        ),
        "koreanGuide": {
            "summary": "Part 1 전환: 구글 Flow AI 엔진룸 진입 (Veo 3.1과 Lyria 3 Pro)",
            "points": [
                "도구에서 시너지로: Gemini, Imagen, Veo, Lyria 4대 엔진이 단일 루프 안에서 작동하는 원리",
                "48kHz 네이티브 오디오: 화면 속 물리적 충돌과 완벽히 일치하는 공간 효과음 자동 생성",
                "Part 2~4 로드맵 제시: Flow AI 심층 해부 ➔ Runway 정밀 연출 ➔ 하이브리드 파이프라인"
            ],
            "tips": "제임스 조교가 4대 엔진의 유기적 결합과 48kHz 오디오 합성의 놀라움을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Engine Room Synergy",
                "def": "The seamless data exchange between distinct multimodal foundation models within a single execution runtime.",
                "defKo": "멀티모델 엔진룸 시너지"
            },
            {
                "term": "Native 48kHz Spatial Foley",
                "def": "High-fidelity audio sound effects synthesized directly from video visual physics without manual sound library search.",
                "defKo": "48kHz 네이티브 공간 효과음"
            }
        ]
    },
    # Slide 11: Case Study 1: Hollywood Studio 4K Feature Film Teaser
    {
        "num": 11,
        "type": "casestudy",
        "title": "CASE STUDY 1: HOLLYWOOD 4K FILM TEASER",
        "subtitle": "Major Hollywood Studio produces 4K sci-fi blockbuster teaser trailer in 72 hours for $15,000",
        "company": "Major Independent Hollywood Film Studio",
        "problem": "Studio needed a high-concept 4K sci-fi teaser trailer to pitch investors at Cannes; traditional VFX pre-visualization required $350,000 and 8 weeks of CGI studio rendering.",
        "solution": "Built Flow AI & Runway hybrid pipeline: locked 3 lead actors' faces using Ingredients-to-Video; directed 18 cinematic VFX shots with 5-channel Motion Brush and Lyria 3 Pro score.",
        "impact": "Completed 90-second 4K teaser in 72 hours for $15,000 (95% cost reduction); secured $40M production financing from international distributors.",
        "script": (
            "[Prof. Peter] Slide 11 presents \"CASE STUDY 1: HOLLYWOOD STUDIO 4K FEATURE FILM TEASER.\"\n\n"
            "[TA Sarah] An independent Hollywood studio needed a 90-second 4K teaser for a sci-fi blockbuster to pitch investors at the Cannes Film Festival. Traditional CGI VFX houses quoted $350,000 and 8 weeks of rendering time—far too slow!\n\n"
            "[TA James] The director used our Flow AI and Runway hybrid pipeline: locking 3 lead actor facial identities, directing spaceship battle trajectories with Motion Brush, and scoring an orchestral soundtrack with Lyria 3 Pro in 72 hours for $15,000!\n\n"
            "[Prof. Peter] When presented at Cannes, the teaser received a standing ovation and secured $40 million in international distribution financing! That is the power of Generative Cinema.\n\n"
            "[TA Sarah] Now let us open Part 2 and step Inside the Engine Room of Flow AI on Slide 12!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 1: 헐리우드 독립 스튜디오 72시간 만에 15,000달러로 4K SF 티저 완성 (4,000만 달러 투자 유치)",
            "points": [
                "문제 상황: 칸 영화제 투자 유치용 90초 4K SF 티저 필요, 기존 CG 외주 시 35만 달러와 8주 소요",
                "솔루션: Flow AI와 Runway 하이브리드 구축 ➔ 3인 주연 배우 얼굴 고정, 모션 브러시 우주선 전투, Lyria 3 Pro 오케스트라 작곡",
                "성과: 72시간 만에 15,000달러로 완성(95% 비용 절감), 칸 영화제 기립박수 및 4,000만 달러(약 530억 원) 제작비 펀딩 성공"
            ],
            "tips": "사라 조교와 피터 교수가 35만 달러짜리 외주를 15,000달러로 끝내고 4천만 달러 투자를 따낸 헐리우드 성공 신화를 전달합니다."
        },
        "keyTerms": [
            {
                "term": "VFX Pre-Visualization",
                "def": "The preliminary digital prototyping of complex cinematic visual effects prior to principal photography.",
                "defKo": "VFX 프리비주얼라이제이션"
            },
            {
                "term": "Production Financing Pitch",
                "def": "Using high-fidelity teaser media to demonstrate project commercial viability to film investors and distributors.",
                "defKo": "영화 제작 투자 피칭"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 12: Part 2 Section Divider
    {
        "num": 12,
        "type": "section",
        "title": "PART 2: INSIDE THE ENGINE ROOM OF GOOGLE FLOW AI",
        "subtitle": "Deconstructing the Trinity architecture, Veo 3.1 physics, native 48kHz Lyria audio, and Ingredients-to-Video",
        "script": (
            "[TA Sarah] Look at Slide 12: \"PART 2: INSIDE THE ENGINE ROOM OF GOOGLE FLOW AI.\" Now we dissect the neural mechanics!\n\n"
            "[Prof. Peter] Google Flow AI represents the pinnacle of multi-model coordination: fusing language reasoning, diffusion visual synthesis, continuous video physics, and neural audio composition into one heartbeat.\n\n"
            "[TA James] In Part 2, we explore the Trinity architecture, Veo 3.1 physics simulation, Lyria 3 Pro 48kHz audio generation, Ingredients-to-Video identity locking, and programmatic Interactions APIs!\n\n"
            "[TA Sarah] Let us inspect the Trinity Architecture on Slide 13!"
        ),
        "koreanGuide": {
            "summary": "Part 2 섹션 전환: 구글 Flow AI 엔진룸 해부",
            "points": [
                "4대 파운데이션 모델의 유기적 융합: 언어 추론 + 비주얼 확산 + 비디오 물리 + 오디오 작곡",
                "Veo 3.1 시공간 물리 시뮬레이터와 Lyria 3 Pro 48kHz 네이티브 오디오",
                "배우 정체성을 완벽 고정하는 Ingredients-to-Video와 프로그래밍 방식의 Interactions API"
            ],
            "tips": "피터 교수가 멀티모델 융합의 기술적 깊이를 선언하고 제임스가 4대 엔진 해부를 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Trinity Foundation Architecture",
                "def": "Google's coordinated suite integrating Gemini (scripting), Imagen (keyframes), and Veo (spatio-temporal dynamics).",
                "defKo": "트리니티 파운데이션 아키텍처"
            },
            {
                "term": "Neural Audio-Visual Co-Generation",
                "def": "The simultaneous synthesis of synchronized video frames and high-resolution spatial sound effects.",
                "defKo": "신경망 시청각 동시 생성"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 13: The Trinity Architecture: Gemini, Imagen, and Veo
    {
        "num": 13,
        "type": "content",
        "title": "THE TRINITY ARCHITECTURE: GEMINI, IMAGEN, VEO",
        "subtitle": "The 3-layer neural stack governing narrative logic, visual aesthetics, and physical motion",
        "points": [
            "Layer 1: Gemini 2.5 Pro (The Director) - Deconstructs prompts into scene beats, camera cues, and character arcs.",
            "Layer 2: Imagen 4 (The Cinematographer) - Paints ultra-crisp 4K keyframe images with photorealistic lighting.",
            "Layer 3: Veo 3.1 (The Physics Engine) - Interpolates keyframes into continuous 60 FPS video adhering to gravity and momentum."
        ],
        "script": (
            "[Prof. Peter] Slide 13 diagrams \"THE TRINITY ARCHITECTURE: GEMINI, IMAGEN, AND VEO.\"\n\n"
            "[TA Sarah] Look at how the three layers coordinate: Layer 1 is Gemini 2.5 Pro—acting as the Director, writing scene beats and camera directions. Layer 2 is Imagen 4—acting as the Cinematographer, rendering photorealistic 4K starting and ending keyframes!\n\n"
            "[TA James] And Layer 3 is Veo 3.1—acting as the Physics Engine, interpolating smooth, continuous 60 FPS motion adhering to gravity, wind friction, and light reflections!\n\n"
            "[Prof. Peter] Let us inspect Veo 3.1 physics realism on Slide 14."
        ),
        "koreanGuide": {
            "summary": "트리니티 3계층 아키텍처: Gemini(연출) ➔ Imagen(작화) ➔ Veo(물리)",
            "points": [
                "1계층 (Gemini 2.5 Pro - 총괄 감독): 프롬프트를 씬 단위 비트, 카메라 큐, 인물 동선으로 분해",
                "2계층 (Imagen 4 - 촬영 감독): 완벽한 광원과 질감을 지닌 초고화질 4K 시작/종료 키프레임 작화",
                "3계층 (Veo 3.1 - 물리 엔진): 키프레임 사이를 중력, 관성, 빛 반사 법칙에 따라 60 FPS로 부드럽게 보간"
            ],
            "tips": "사라 조교와 제임스 조교가 3대 신경망이 영화 제작의 각 파트를 분담하는 완벽한 협업 체계를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Director-Cinematographer-Physics Triad",
                "def": "The specialized division of labor where language models direct, image models frame, and video models animate.",
                "defKo": "감독-촬영-물리 3단 협업 체계"
            },
            {
                "term": "Keyframe Latent Interpolation",
                "def": "The continuous generation of intermediate video frames bridging two static visual anchor states.",
                "defKo": "키프레임 잠재 공간 보간"
            }
        ]
    },
    # Slide 14: Veo 3.1 Physics Simulator: Spatio-Temporal Realism
    {
        "num": 14,
        "type": "content",
        "title": "VEO 3.1: SPATIO-TEMPORAL REALISM",
        "subtitle": "Generating rigid-body collisions, fluid splashes, fabric cloth dynamics, and optical lens flares",
        "points": [
            "Rigid-Body Mechanics: Bouncing basketballs preserve momentum without squishing or morphing unnaturally.",
            "Fluid Dynamics: Water pouring from a glass splashes with realistic turbulent surface foam.",
            "Optical Flare Simulation: Sun flares across anamorphic lenses streak horizontally with authentic optical physics."
        ],
        "script": (
            "[TA Sarah] Slide 14 explores \"VEO 3.1 PHYSICS SIMULATOR: SPATIO-TEMPORAL REALISM.\"\n\n"
            "[TA James] Early AI video looked like a bad dream—people walked through walls and coffee cups melted into hands! Veo 3.1 enforces strict spatio-temporal physics: basketballs bounce preserving kinetic energy, and poured water splashes with authentic fluid foam!\n\n"
            "[Prof. Peter] Optical lens flares streak across the screen with real anamorphic physics! That is why audiences perceive the footage as real cinema.\n\n"
            "[TA Sarah] Let us inspect Native 48kHz Audio Generation on Slide 15."
        ),
        "koreanGuide": {
            "summary": "Veo 3.1 물리 시뮬레이터: 강체 충돌, 유체 물보라, 천 시뮬레이션, 아나모픽 광선 플레어",
            "points": [
                "강체 역학 준수: 튀는 농구공이 찌그러지거나 왜곡되지 않고 운동량을 정확히 보존",
                "유체 역학: 컵에서 쏟아지는 물이 사실적인 난류 거품을 일으키며 튀는 물리 구현",
                "광학 렌즈 플레어: 역광 시 카메라 렌즈에 맺히는 수평 아나모픽 플레어 광학 완벽 모사"
            ],
            "tips": "제임스 조교와 피터 교수가 흐물거리던 초기 AI 영상을 극복한 Veo 3.1의 물리적 단단함을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Spatio-Temporal Physics Consistency",
                "def": "The mathematical enforcement of physical conservation laws across generated video frame volumes.",
                "defKo": "시공간 물리 법칙 일관성"
            },
            {
                "term": "Anamorphic Optical Simulation",
                "def": "Generating realistic photographic artifacts including lens distortion, chromatic aberration, and streak flares.",
                "defKo": "아나모픽 광학 수차 시뮬레이션"
            }
        ]
    },
    # Slide 15: The Sound of Realism: Native 48kHz Audio Generation
    {
        "num": 15,
        "type": "content",
        "title": "THE SOUND OF REALISM: NATIVE 48KHZ AUDIO",
        "subtitle": "Generating synchronized sound effects, dialogue reverberations, and Foley impacts in Lyria 3 Pro",
        "points": [
            "Zero Silent Movies: Veo 3.1 generates video AND synchronous 48kHz audio tracks simultaneously.",
            "Acoustic Spatial Reverberation: Footsteps in a cathedral echo with 2.4s reverb; footsteps in a carpeted room sound dry.",
            "Sub-Frame Audio Synchronization: Gunshots, car crashes, and glass breaking sync to the exact video millisecond."
        ],
        "script": (
            "[Prof. Peter] Slide 15 reveals a major breakthrough: \"THE SOUND OF REALISM: NATIVE 48KHZ AUDIO GENERATION.\"\n\n"
            "[TA Sarah] Until now, AI video was a silent movie! You had to manually search audio libraries for hours to find a matching door slam or footsteps!\n\n"
            "[TA James] Google Flow AI synthesizes video AND 48kHz broadcast-quality audio simultaneously in Lyria 3 Pro! When a glass drops in the video, the audio engine generates the exact shattering sound at the millisecond of impact, matched to the acoustic reverb of the room!\n\n"
            "[Prof. Peter] Let us inspect Ingredients-to-Video on Slide 16."
        ),
        "koreanGuide": {
            "summary": "사실성의 소리: Lyria 3 Pro를 통한 48kHz 네이티브 시청각 동시 생성",
            "points": [
                "무성영화 시대의 종말: 비디오 생성과 동시에 48kHz 고화질 오디오 트랙을 단일 파이프라인에서 합성",
                "공간 음향 잔향(Reverb): 대성당 발소리는 2.4초 울림, 카펫 방 발소리는 건조하게 자동 공간 매핑",
                "서브프레임 밀리초 싱크: 유리잔이 깨지는 영상의 정확한 순간에 파편 소리가 오차 없이 동기화"
            ],
            "tips": "사라 조교와 제임스 조교가 무성영화에서 유성영화로의 진화에 비견되는 48kHz 동시 생성의 위력을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Native 48kHz Audio Synthesis",
                "def": "The direct generation of studio-grade acoustic waveforms synchronized with visual diffusion frames.",
                "defKo": "48kHz 네이티브 스튜디오 오디오 합성"
            },
            {
                "term": "Acoustic Geometry Reverberation",
                "def": "Simulating environmental sound reflection matching the physical materials and volume of the rendered scene.",
                "defKo": "공간 기하학적 음향 잔향"
            }
        ]
    },
    # Slide 16: Ingredients-to-Video: Identity Lock for Actors & Sets
    {
        "num": 16,
        "type": "content",
        "title": "INGREDIENTS-TO-VIDEO: IDENTITY LOCK",
        "subtitle": "Locking actor facial geometry, wardrobe, and recurring props across an entire 2-hour movie",
        "points": [
            "The Ingredient Vault: Storing reference embeddings for Actor Face (`@Alex`), Sci-Fi Pistol (`@WeaponX`), and Cyber Car (`@Car9`).",
            "Cross-Scene Consistency: Referencing `@Alex walks into tavern and draws @WeaponX` preserves 100% visual identity.",
            "Cross-Attention Injection: Injecting actor facial latent vectors directly into Veo diffusion layers at every timestep."
        ],
        "script": (
            "[TA Sarah] Slide 16 reveals our secret weapon: \"INGREDIENTS-TO-VIDEO: IDENTITY LOCK FOR ACTORS & SETS.\"\n\n"
            "[TA James] How do you make a full 10-scene movie with the same character? You create an Ingredient Vault! You define `@CaptainZara` with 3 reference photos, `@PlasmaRifle` with 2 angles, and `@DesertRover`!\n\n"
            "[Prof. Peter] In your scene prompts, you simply reference `@CaptainZara fires @PlasmaRifle while driving @DesertRover`! Veo's cross-attention layers inject the exact facial geometry and prop textures into every frame! Zero identity drift!\n\n"
            "[TA Sarah] Let us inspect the Multi-Image Pipeline on Slide 17."
        ),
        "koreanGuide": {
            "summary": "재료-비디오(Ingredients-to-Video): 2시간 영화 전체에서 배우 얼굴과 소품 완벽 고정",
            "points": [
                "재료 금고(Ingredient Vault): 주연 배우(@Zara), 특수 무기(@Rifle), 차량(@Rover)의 잠재 벡터 등록",
                "씬 간 100% 일관성: '@Zara가 @Rover를 몰며 @Rifle을 발사한다' 프롬프트만으로 동일 인물/소품 완벽 묘사",
                "교차 어텐션 주입: 디퓨전 매 타임스텝마다 얼굴 특징 벡터를 직접 주입해 얼굴 변형 원천 차단"
            ],
            "tips": "제임스 조교와 피터 교수가 @태그 하나로 10개 씬의 주연 배우 얼굴을 고정하는 마법을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Ingredients-to-Video",
                "def": "Google's framework for binding persistent identity tokens to characters, props, and environments across video sequences.",
                "defKo": "재료 기반 비디오 합성 (Ingredients-to-Video)"
            },
            {
                "term": "Latent Identity Injection",
                "def": "Injecting frozen feature embeddings into diffusion cross-attention maps to maintain structural object invariance.",
                "defKo": "잠재 특징 정체성 불변 주입"
            }
        ]
    },
    # Slide 17: The Multi-Image Pipeline: Weaving Scattered Assets
    {
        "num": 17,
        "type": "content",
        "title": "THE MULTI-IMAGE PIPELINE: WEAVING ASSETS",
        "subtitle": "Combining brand logos, real product CADs, and AI environments into seamless commercial shots",
        "points": [
            "Asset Ingestion: Feeding an official 3D CAD render of a luxury perfume bottle + moodboard photograph.",
            "Seamless Composition: Veo renders a model holding the EXACT authentic perfume bottle with correct glass refractions.",
            "Zero CGI Artifacts: Real commercial product placement synthesized with photorealistic biological hands."
        ],
        "script": (
            "[Prof. Peter] Slide 17 covers \"THE MULTI-IMAGE PIPELINE: WEAVING SCATTERED ASSETS.\"\n\n"
            "[TA Sarah] In commercial advertising, clients demand that their real physical product appear in the video with 100% brand accuracy!\n\n"
            "[TA James] With the Multi-Image Pipeline, you upload the brand's exact CAD rendering of a luxury watch. Veo places that exact watch onto the wrist of a virtual fashion model walking through Paris in the rain—calculating real glass reflections and water droplets on the watch face!\n\n"
            "[Prof. Peter] Let us examine our second enterprise case study on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "다중 이미지 파이프라인: 실제 브랜드 제품 CAD와 가상 모델의 완벽한 융합",
            "points": [
                "실물 자산 수용: 명품 향수병이나 시계의 실제 3D CAD 이미지와 배경 무드보드 주입",
                "매끄러운 합성: 가상 패션 모델의 손목에 정확한 실물 시계를 착용시키고 빗방울 반사 계산",
                "CGI 이질감 제로: 실제 제품 디테일과 자연스러운 인체 손가락 상호작용의 완벽한 상업적 결합"
            ],
            "tips": "사라 조교와 제임스 조교가 광고주의 엄격한 실물 제품 배치 요구를 100% 충족하는 합성 기술을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Commercial Product Insertion",
                "def": "The seamless compositing of authentic proprietary product models into generative video environments.",
                "defKo": "상업용 제품 자연 합성"
            },
            {
                "term": "Refraction-Aware Compositing",
                "def": "Rendering dynamic optical refractions through transparent product glass matching ambient scene lighting.",
                "defKo": "굴절 반응형 실시간 합성"
            }
        ]
    },
    # Slide 18: Stateful Editing: Overcoming Generative Amnesia
    {
        "num": 18,
        "type": "content",
        "title": "STATEFUL EDITING: OVERCOMING AMNESIA",
        "subtitle": "Maintaining scene state across iterations: Modifying the actor's jacket while preserving background geometry",
        "points": [
            "Generative Amnesia: Changing one word in a prompt traditionally rerolled the entire scene into something unrecognizable.",
            "Masked Inpainting Latents: Freezing the background and re-synthesizing ONLY the targeted bounding box.",
            "Stateful Continuity: Modifying lighting from noon to dusk while preserving camera angle and character pose."
        ],
        "script": (
            "[TA Sarah] Slide 18 explores \"STATEFUL EDITING: OVERCOMING GENERATIVE AMNESIA.\"\n\n"
            "[TA James] The greatest frustration in early AI video was 'Generative Amnesia'—if you asked to change the character's leather jacket from brown to red, the AI generated a completely different room, different weather, and a different person!\n\n"
            "[Prof. Peter] Stateful Editing freezes the latent background mesh and in-paints only the jacket! The room, the lighting, and the actor's face remain 100% frozen while the jacket color updates in 5 seconds!\n\n"
            "[TA Sarah] Let us inspect the Interactions API on Slide 19."
        ),
        "koreanGuide": {
            "summary": "상태 유지 편집(Stateful Editing): 생성형 건망증을 극복하는 국소 인페인팅",
            "points": [
                "생성형 건망증(Generative Amnesia): 단어 하나 바꿨더니 방 구조와 인물 얼굴이 통째로 바뀌던 고통",
                "마스크 잠재 인페인팅: 배경과 인물 얼굴을 완벽히 동결(Freeze)하고 오직 가죽 재킷 영역만 국소 재합성",
                "상태 지속성: 카메라 앵글과 인물 포즈를 100% 보존한 채 조명만 한낮에서 석양으로 전환"
            ],
            "tips": "제임스 조교와 피터 교수가 원하는 부위만 콕 집어 수정하는 상태 유지 편집의 실전 가치를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Generative Amnesia",
                "def": "The failure of stateless generative models to preserve unedited scene elements during prompt refinement.",
                "defKo": "생성형 건망증 (Generative Amnesia)"
            },
            {
                "term": "Masked Latent Inpainting",
                "def": "Constraining neural diffusion updates to a localized spatial bounding box while freezing surrounding latent tensors.",
                "defKo": "마스크 잠재 공간 인페인팅"
            }
        ]
    },
    # Slide 19: Interactions API: Programmatic State Edits
    {
        "num": 19,
        "type": "content",
        "title": "INTERACTIONS API: PROGRAMMATIC EDITS",
        "subtitle": "Driving video synthesis via Python/REST APIs: Batch generating 1,000 personalized commercial variations",
        "points": [
            "Automated Video Pipeline: Running `flow.generate_scene(script_id, camera_config, ingredients)` from code.",
            "Hyper-Personalized Ads: Generating 1,000 unique localized video ads (different cities, languages, names) overnight.",
            "Real-Time CI/CD for Video: Automatically compiling new product demo videos whenever a software release is tagged."
        ],
        "script": (
            "[Prof. Peter] Slide 19 diagrams the \"INTERACTIONS API: PROGRAMMATIC STATE EDITS.\"\n\n"
            "[TA Sarah] Professional studios do not click buttons by hand; we automate via code! With the Interactions API, you write a Python script that iterates through a database of 1,000 customers.\n\n"
            "[TA James] Overnight, the cluster generates 1,000 personalized 4K video ads—calling each customer by name and showing their local city skyline! Personalized advertising at planetary scale!\n\n"
            "[Prof. Peter] Let us examine our second enterprise case study on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "Interactions API: 파이썬 코드로 1,000개 맞춤형 광고를 밤샘 일괄 생성",
            "points": [
                "비디오 자동화 파이프라인: flow.generate_scene() 함수 호출로 스크립트와 카메라 설정을 코드로 제어",
                "초개인화 맞춤 광고: 1,000명 고객의 이름과 거주 도시 스카이라인이 반영된 4K 광고 밤샘 자동 렌더링",
                "비디오 CI/CD: 소프트웨어 신규 릴리스가 태그될 때마다 프로모션 데모 영상을 자동 컴파일"
            ],
            "tips": "사라 조교와 제임스 조교가 코드로 영상을 대량 생산하는 Interactions API의 엔터프라이즈 확장성을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Interactions REST API",
                "def": "Google Flow AI's developer interface enabling automated programmatic video scene creation and state editing.",
                "defKo": "Interactions 비디오 개발자 API"
            },
            {
                "term": "Hyper-Personalized Video Synthesis",
                "def": "The dynamic programmatic rendering of unique customized video assets tailored to individual user demographics.",
                "defKo": "초개인화 동적 비디오 합성"
            }
        ]
    },
    # Slide 20: Part 2 Transition: Entering Runway ML & Precision Control
    {
        "num": 20,
        "type": "content",
        "title": "PART 2 TRANSITION: ENTERING RUNWAY PRECISION",
        "subtitle": "Connecting storyboarding and world models to Motion Brush, Camera Matrices, and Act-Two",
        "points": [
            "From Story to Camera: How do we achieve millimeter-precise motion control in fast action sequences?",
            "Runway Gen-3 Alpha: 5-channel velocity vectors and performance capture transfer.",
            "The Roadmap Ahead: Master Runway Controls in Part 3, and Assemble the Hybrid Pipeline in Part 4."
        ],
        "script": (
            "[Prof. Peter] Slide 20 transitions our roadmap: \"PART 2 TRANSITION: ENTERING RUNWAY PRECISION CONTROLS.\"\n\n"
            "[TA Sarah] We have mastered Flow AI's narrative world-building and native audio. Now, how do we direct complex physical action sequences with exact camera dollies and velocity vectors?\n\n"
            "[TA James] Through Runway ML! In Part 3, we master Gen-3 Alpha, the 5-channel Motion Brush, camera velocity matrices, Act-Two facial performance transfer, and credit ROI budgeting!\n\n"
            "[Prof. Peter] Let us examine our second enterprise case study on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "Part 2 전환: 런웨이 정밀 제어와 카메라 매트릭스 진입",
            "points": [
                "스토리에서 카메라로: 빠른 액션 씬에서 밀리미터 단위의 카메라 궤적과 속도 벡터 제어 달성",
                "Runway Gen-3 Alpha: 5채널 모션 브러시와 실제 배우 연기 이식(Act-Two)",
                "Part 3~4 로드맵 제시: 런웨이 정밀 연출 ➔ 하이브리드 파이프라인 통합 ➔ 실습 14"
            ],
            "tips": "제임스 조교가 런웨이의 정밀 카메라 제어와 모션 브러시의 위력을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Precision Camera Trajectory",
                "def": "The deterministic mathematical translation and rotation of virtual camera coordinates across time.",
                "defKo": "정밀 카메라 궤적 제어"
            },
            {
                "term": "Act-Two Performance Transfer",
                "def": "Runway's architecture mapping real human actor facial expressions directly onto generative AI avatars.",
                "defKo": "Act-Two 실사 연기 이식"
            }
        ]
    },
    # Slide 21: Video Arena ELO: Deciphering Real Usability
    {
        "num": 21,
        "type": "content",
        "title": "VIDEO ARENA ELO: DECIPHERING USABILITY",
        "subtitle": "Analyzing blind community benchmarks: Prompt Adherence, Motion Quality, and Cinematic Tone",
        "points": [
            "LMSYS Video Arena: Blind side-by-side human voting on 50,000 generated video prompts.",
            "Flow AI vs. Gen-3 ELO Ratings: Flow AI dominates narrative and audio; Runway dominates motion dynamics.",
            "Strategic Takeaway: Never lock yourself into a single model; always direct a multi-model hybrid symphony."
        ],
        "script": (
            "[Prof. Peter] Slide 21 analyzes the empirical benchmarks: \"VIDEO ARENA ELO: DECIPHERING REAL USABILITY.\"\n\n"
            "[TA Sarah] Look at the LMSYS Video Arena ELO ratings based on 50,000 blind human evaluations: Google Flow AI scores highest in Prompt Adherence, Photorealism, and Synchronous Audio!\n\n"
            "[TA James] But Runway Gen-3 Alpha scores highest in Complex Action Motion and Camera Steering! That proves why single-model reliance is foolish: True architects use Flow AI for scene setup and Runway for camera choreography!\n\n"
            "[Prof. Peter] Let us examine our second enterprise case study on Slide 22!"
        ),
        "koreanGuide": {
            "summary": "비디오 아레나 ELO 벤치마크: 5만 건 블라인드 테스트 실측 데이터 분석",
            "points": [
                "LMSYS 비디오 아레나: 50,000건의 블라인드 투표로 검증된 파운데이션 모델 ELO 점수",
                "Flow AI vs Gen-3 강점: Flow AI는 프롬프트 충실도·화질·오디오 1위, Runway는 모션 역학·카메라 1위",
                "전략적 결론: 단일 모델 종속을 버리고 각 모델의 강점을 결합하는 하이브리드 지휘관이 될 것"
            ],
            "tips": "사라 조교와 제임스 조교가 실측 ELO 점수를 근거로 하이브리드 파이프라인의 필연성을 증명합니다."
        },
        "keyTerms": [
            {
                "term": "LMSYS Video Arena ELO",
                "def": "The global competitive ranking of video generative models derived from blinded pairwise human preferences.",
                "defKo": "LMSYS 비디오 아레나 ELO 랭킹"
            },
            {
                "term": "Hybrid Model Symphony",
                "def": "The architectural practice of distributing distinct video generation tasks to their highest-scoring specialized models.",
                "defKo": "하이브리드 멀티모델 심포니"
            }
        ]
    },
    # Slide 22: Case Study 2: Global Luxury Automaker Commercial Campaign
    {
        "num": 22,
        "type": "casestudy",
        "title": "CASE STUDY 2: LUXURY AUTOMAKER CAMPAIGN",
        "subtitle": "Global German Luxury Automaker creates 20 localized commercial videos across 12 countries in 5 days",
        "company": "Top Tier German Luxury Automotive Group",
        "problem": "Launching a new electric supercar across 12 global markets required filming in the Swiss Alps, Tokyo neon streets, and Dubai dunes; physical production was quoted at $2.2M and 3 months.",
        "solution": "Built Flow AI & Runway hybrid pipeline: ingested exact CAD car model; choreographed high-speed drift camera tracking in Runway; generated native 48kHz engine roar in Flow AI.",
        "impact": "Delivered 20 localized 4K commercial videos in 5 days for $32,000 (98.5% cost reduction); campaign drove 15,000 pre-orders in the first 48 hours.",
        "script": (
            "[Prof. Peter] Slide 22 presents \"CASE STUDY 2: GLOBAL LUXURY AUTOMAKER COMMERCIAL CAMPAIGN.\"\n\n"
            "[TA Sarah] A premier German luxury automaker was launching a flagship electric supercar across 12 countries simultaneously. They needed commercial footage of the car drifting through the Swiss Alps, neon Tokyo highways, and Dubai desert dunes! Physical filming was estimated at $2.2 million and 3 months of shooting!\n\n"
            "[TA James] They deployed our hybrid pipeline: ingesting the car's exact 3D CAD model, choreographing 120 MPH drift tracking shots in Runway Gen-3 with Motion Brush, and generating realistic electric motor whines and tire squeals in Flow AI's Lyria engine!\n\n"
            "[Prof. Peter] All 20 localized 4K commercials were completed in 5 days for $32,000! The campaign went viral, driving 15,000 supercar pre-orders in 48 hours! That is sovereign marketing velocity.\n\n"
            "[TA Sarah] Now let us open Part 3 and master Runway ML Precision 연출 on Slide 23!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 2: 독일 명품 전기 슈퍼카 12개국 20개 광고 5일 만에 완성 (15,000대 완판)",
            "points": [
                "문제 상황: 스위스 알프스, 도쿄 네온, 두바이 사막 로케이션 촬영 필요 ➔ 220만 달러(약 30억 원)와 3개월 소요",
                "솔루션: 실물 CAD 차량 주입 ➔ Runway 시속 120마일 드리프트 트래킹 ➔ Flow AI 전기 모터 사운드 합성",
                "성과: 5일 만에 32,000달러로 20편 완성(98.5% 비용 절감), 48시간 만에 15,000대 사전 계약 완판 기적 달성"
            ],
            "tips": "사라 조교와 제임스 조교가 30억 원짜리 글로벌 자동차 광고를 4천만 원에 끝내고 15,000대를 완판시킨 성과를 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Multi-Country Localization",
                "def": "Generating region-specific commercial video variations tailored to local cultural landmarks and languages.",
                "defKo": "글로벌 다국가 로컬라이제이션"
            },
            {
                "term": "High-Speed Vehicle Tracking",
                "def": "Simulating dynamic low-angle chase camera trajectories capturing high-velocity automotive physics.",
                "defKo": "고속 주행 차량 추적 카메라 연출"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 23: Part 3 Section Divider
    {
        "num": 23,
        "type": "section",
        "title": "PART 3: PRECISION 연출 WITH RUNWAY ML",
        "subtitle": "5-channel Motion Brush, camera velocity matrices, Act-Two performance capture, and credit ROI budgeting",
        "script": (
            "[TA Sarah] Look at Slide 23: \"PART 3: PRECISION 연출 WITH RUNWAY ML.\" Now we master director-level cinematography!\n\n"
            "[Prof. Peter] Directing is the art of precise intentionality. In Part 3, we examine the 5-channel Motion Brush, camera coordinate matrices, Act-Two performance transfer, credit anxiety management, and cybersecurity defenses against spoofed video assets.\n\n"
            "[TA James] Let us inspect the 5-Channel Motion Brush on Slide 24!"
        ),
        "koreanGuide": {
            "summary": "Part 3 섹션 전환: 런웨이 ML 정밀 연출과 모션 브러시 제어",
            "points": [
                "감독의 예술: 우연에 기대지 않는 정밀한 연출적 의도성(Intentionality) 확립",
                "5채널 모션 브러시, 카메라 속도 행렬, Act-Two 실사 연기 이식",
                "크레딧 불안 관리 및 위조 비디오 에셋에 대한 사이버 보안 방어선"
            ],
            "tips": "피터 교수가 감독의 연출적 의도성을 선언하고 제임스가 5채널 모션 브러시를 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Directorial Intentionality",
                "def": "The deliberate orchestration of every visual and acoustic element to serve a specific dramatic narrative.",
                "defKo": "감독의 연출적 의도성"
            },
            {
                "term": "5-Channel Velocity Mapping",
                "def": "Assigning independent velocity vectors ($V_x, V_y, V_z$) to multiple distinct masked regions in a video frame.",
                "defKo": "5채널 속도 벡터 매핑"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 24: The Motion Brush: 5-Channel Vector Velocity
    {
        "num": 24,
        "type": "content",
        "title": "THE MOTION BRUSH: 5-CHANNEL VELOCITY",
        "subtitle": "Painting independent speed and directional vectors onto up to 5 scene layers simultaneously",
        "points": [
            "Brush 1 (Foreground Hero): Moving forward at speed +4 with subtle organic swaying.",
            "Brush 2 (Background Clouds): Drifting right at speed +1 with slow volumetric dissipation.",
            "Brush 3 (Campfire Smoke): Rising upward at speed +7 with turbulent spiral curl physics.",
            "Brush 4 & 5 (Water & Sparks): Cascading down and outward with realistic particle dispersion."
        ],
        "script": (
            "[Prof. Peter] Slide 24 diagrams \"THE MOTION BRUSH: 5-CHANNEL VECTOR VELOCITY.\"\n\n"
            "[TA Sarah] Look at the surgical control: You paint Brush 1 on your hero character to walk forward slowly. You paint Brush 2 on background storm clouds to drift to the right. You paint Brush 3 on campfire smoke to billow upward!\n\n"
            "[TA James] You paint Brush 4 on sparks to fly outward! You control all 5 independent velocity vectors in a single shot! No other tool gives you this level of physical layer independence!\n\n"
            "[Prof. Peter] Let us inspect Camera Controls on Slide 25."
        ),
        "koreanGuide": {
            "summary": "5채널 모션 브러시: 5개 독립 레이어에 서로 다른 속도와 방향 벡터 부여",
            "points": [
                "브러시 1 (주인공): 앞으로 천천히 전진(속도 +4)",
                "브러시 2 (배경 구름): 오른쪽으로 완만하게 이동(속도 +1)",
                "브러시 3 (모닥불 연기): 위쪽으로 소용돌이치며 상승(속도 +7)",
                "브러시 4 & 5 (강물 및 불꽃 파편): 하강 및 방사형 입자 분산 물리 부여"
            ],
            "tips": "사라 조교와 제임스 조교가 5개 레이어의 물리 속도를 독립 통제하는 모션 브러시의 위력을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Multi-Layer Velocity Painting",
                "def": "The manual application of directional speed maps to isolated image segments using raster brush masks.",
                "defKo": "다층 속도 벡터 브러시 페인팅"
            },
            {
                "term": "Particle Dispersion Physics",
                "def": "Simulating the natural turbulent movement of sparks, smoke, and water droplets across animated frames.",
                "defKo": "입자 분산 난류 물리"
            }
        ]
    },
    # Slide 25: Camera Controls: Cinematography Translated to Code
    {
        "num": 25,
        "type": "content",
        "title": "CAMERA CONTROLS: CINEMATOGRAPHY TO CODE",
        "subtitle": "Translating Hollywood crane and gimbal maneuvers into exact mathematical 3D camera matrices",
        "points": [
            "Horizontal Pan (`Pan: +3.5`): Sweeping camera horizontally across a wide landscape.",
            "Vertical Tilt (`Tilt: -2.0`): Tilting down from a cathedral ceiling to the altar.",
            "Dolly Zoom (`Zoom: +4.0, Dolly: -4.0`): The Hitchcock Vertigo effect warping background perspective.",
            "Dutch Roll (`Roll: +15°`): Tilting the camera horizon to induce psychological vertigo in thriller scenes."
        ],
        "script": (
            "[TA Sarah] Slide 25 explores \"CAMERA CONTROLS: CINEMATOGRAPHY TRANSLATED TO CODE.\"\n\n"
            "[TA James] In Runway, cinematography is code! You want the famous Alfred Hitchcock 'Vertigo' effect? Set `Zoom: +4` and `Dolly: -4` simultaneously! The background warps while the character stays frozen in terror!\n\n"
            "[Prof. Peter] You want a tense psychological thriller look? Dial in a 15-degree Dutch Roll tilt! Every classic Hollywood camera move is at your fingertips without renting a 50,000-dollar techno-crane!\n\n"
            "[TA Sarah] Let us inspect Act-Two performance capture on Slide 26."
        ),
        "koreanGuide": {
            "summary": "카메라 컨트롤: 헐리우드 촬영 기법을 3D 수학 매트릭스로 완벽 번역",
            "points": [
                "수평 팬(Pan: +3.5) 및 수직 틸트(Tilt: -2.0)로 웅장한 공간감 연출",
                "돌리 줌(Dolly Zoom): 줌 인(+4)과 돌리 아웃(-4)을 동시 실행해 히치콕의 현기증(Vertigo) 왜곡 효과 재현",
                "더치 롤(Dutch Roll: +15°): 카메라 수평선을 기울여 심리 스릴러의 긴장감 극대화"
            ],
            "tips": "제임스 조교와 피터 교수가 5만 달러짜리 테크노 크레인 없이 수치 입력으로 히치콕 샷을 완성하는 마법을 설명합니다."
        },
        "keyTerms": [
            {
                "term": "Hitchcock Vertigo Effect",
                "def": "The optical illusion produced by simultaneously zooming in while moving the camera backward (dolly zoom).",
                "defKo": "히치콕 돌리 줌 효과 (Vertigo Effect)"
            },
            {
                "term": "Dutch Angle Roll",
                "def": "A camera shot where the horizon is tilted relative to the bottom of the frame to convey unease or tension.",
                "defKo": "더치 앵글 롤 (Dutch Roll)"
            }
        ]
    },
    # Slide 26: Act-Two: Transferring Human Acting to Avatars
    {
        "num": 26,
        "type": "content",
        "title": "ACT-TWO: HUMAN ACTING TO AVATARS",
        "subtitle": "Mapping real actor smartphone webcam performances directly onto photorealistic AI characters",
        "points": [
            "Performance Capture: Record yourself speaking and emoting into your standard iPhone selfie camera.",
            "Subtle Micro-Expressions: Act-Two maps eyebrow twitches, pupil dilation, and lip micro-movements to the avatar.",
            "Preserving the Soul: The nuance, comedic timing, and emotional tears come from a real human being."
        ],
        "script": (
            "[Prof. Peter] Slide 26 highlights \"ACT-TWO: TRANSFERRING HUMAN ACTING TO AVATARS.\"\n\n"
            "[TA Sarah] Why do purely synthetic AI characters sometimes look creepy and soulless? Because they lack the micro-expressions of a human actor!\n\n"
            "[TA James] With Runway Act-Two, you record yourself speaking with emotion on your phone webcam. Act-Two transfers every subtle eyebrow twitch, lip trembling, and eye blink directly onto a photorealistic alien, robotic, or historical character in 4K!\n\n"
            "[Prof. Peter] The emotional soul of the performance remains 100% human.\n\n"
            "[TA Sarah] Let us inspect Credit Anxiety & Studio ROI on Slide 27."
        ),
        "koreanGuide": {
            "summary": "Act-Two: 스마트폰 셀카 영상의 인간 배우 감정 연기를 AI 아바타로 100% 이식",
            "points": [
                "모션 캡처의 대중화: 스마트폰 웹캠으로 연기한 표정과 대사 영상을 즉각 캡처",
                "미세 표정 매핑: 눈썹 떨림, 눈동자 확장, 입술 미세 경련을 4K AI 캐릭터에 실시간 전이",
                "인간 영혼의 보존: 불쾌한 골짜기(Uncanny Valley)를 극복하고 진정한 희로애락의 감정 연기 완성"
            ],
            "tips": "사라 조교와 피터 교수가 AI의 껍데기에 인간 배우의 진정한 영혼을 불어넣는 Act-Two의 감동을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Act-Two Performance Transfer",
                "def": "Runway's facial motion retargeting pipeline transferring video-captured human acting onto arbitrary generative avatars.",
                "defKo": "Act-Two 실사 연기 리타게팅"
            },
            {
                "term": "Uncanny Valley Mitigation",
                "def": "Overcoming unnatural synthetic character rendering through high-precision human biometric micro-expression tracking.",
                "defKo": "불쾌한 골짜기 극복 기술"
            }
        ]
    },
    # Slide 27: Navigating Credit Anxiety: Studio Rendering ROI
    {
        "num": 27,
        "type": "content",
        "title": "CREDIT ANXIETY: STUDIO RENDERING ROI",
        "subtitle": "Managing generation costs with low-res draft previews and calculating $250/mo Studio ROI",
        "points": [
            "The 2-Stage Rendering Rule: Always render 720p 4-second draft previews (5 credits) before committing to 4K upscaling.",
            "Studio Plan ROI: $250/month Unlimited Pro plan replaces a $20,000/month visual effects contractor.",
            "Credit Allocation Discipline: Allocating 30% for storyboards, 40% for motion refinement, and 30% for 4K mastering."
        ],
        "script": (
            "[TA Sarah] Slide 27 tackles a real creator challenge: \"NAVIGATING CREDIT ANXIETY: STUDIO RENDERING ROI.\"\n\n"
            "[TA James] Never render 4K video on your first try—that is burning money! Follow the 2-Stage Rule: Generate a 720p 4-second preview for 5 credits. Check the camera motion and lighting. Once approved, upscale to 4K 60 FPS!\n\n"
            "[Prof. Peter] A $250/month Studio plan gives you the rendering power of a $20,000/month VFX agency. Budget your credits wisely as faithful stewards.\n\n"
            "[TA Sarah] Let us inspect Cybersecurity & Deepfake Defenses on Slide 28."
        ),
        "koreanGuide": {
            "summary": "크레딧 불안 극복 및 스튜디오 렌더링 ROI: 2단계 렌더링 원칙",
            "points": [
                "2단계 렌더링 불변식: 처음엔 720p 4초 프리뷰(5크레딧)로 모션 확인 ➔ 최종 승인 후 4K 60 FPS 업스케일",
                "스튜디오 플랜의 압도적 ROI: 월 250달러 구독으로 월 2만 달러(약 2,700만 원)짜리 외주 VFX 인력 대체",
                "크레딧 배분 규율: 스토리보드 30%, 모션 미세조정 40%, 4K 최종 마스터링 30%"
            ],
            "tips": "제임스 조교가 크레딧을 절약하는 2단계 렌더링 원칙과 월 250달러의 가성비를 명쾌히 제시합니다."
        },
        "keyTerms": [
            {
                "term": "Two-Stage Rendering Pipeline",
                "def": "The cost-control practice of generating low-resolution preview drafts before executing high-resolution 4K final renders.",
                "defKo": "2단계 저비용 렌더링 원칙"
            },
            {
                "term": "VFX Subscription ROI",
                "def": "The financial return of replacing expensive traditional post-production contracts with cloud generative studio tiers.",
                "defKo": "VFX 클라우드 렌더링 ROI"
            }
        ]
    },
    # Slide 28: Adversarial Spoofing & Video Asset Injection
    {
        "num": 28,
        "type": "content",
        "title": "ADVERSARIAL SPOOFING & VIDEO INJECTION",
        "subtitle": "Defending against deepfake impersonation, malicious frame injections, and C2PA provenance tracking",
        "points": [
            "The Deepfake Threat: Malicious actors generating fake CEO announcements or political disinformation videos.",
            "C2PA Cryptographic Watermarking: Embedding immutable cryptographic provenance metadata in every frame.",
            "SynthID Verification: Google's invisible digital watermark embedded directly into pixel latent representations."
        ],
        "script": (
            "[Prof. Peter] Slide 28 addresses a vital ethical defense: \"ADVERSARIAL SPOOFING & VIDEO ASSET INJECTION.\"\n\n"
            "[TA Sarah] In an era where AI can generate photorealistic videos of world leaders, deepfakes and CEO impersonation scams pose severe risks to society and enterprise security!\n\n"
            "[TA James] We enforce mandatory C2PA cryptographic provenance and Google SynthID watermarking: embedding an invisible mathematical signature directly into video latents! Any altered frame is instantly flagged by verification scanners!\n\n"
            "[Prof. Peter] Truth must be protected with unyielding vigilance.\n\n"
            "[TA Sarah] Let us inspect the Conductor Persona on Slide 29."
        ),
        "koreanGuide": {
            "summary": "적대적 스푸핑 및 딥페이크 방어: C2PA 암호화 출처 증명과 SynthID 워터마크",
            "points": [
                "딥페이크 위협: 가짜 CEO 성명서 및 정치적 허위 조작 영상의 급증 위험",
                "C2PA 암호화 출처 추적: 모든 영상 프레임에 위변조 불가능한 원본 생성 메타데이터 전자서명 날인",
                "구글 SynthID 워터마크: 픽셀 잠재 공간에 직접 보이지 않는 수학적 서명을 각인하여 1초 만에 진위 판별"
            ],
            "tips": "사라 조교와 제임스 조교가 딥페이크를 무력화하는 C2PA와 SynthID의 암호학적 방어 원리를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "C2PA Provenance Standard",
                "def": "The open technical specification enabling cryptographic asset tracking and tamper detection for digital media.",
                "defKo": "C2PA 디지털 미디어 출처 증명 표준"
            },
            {
                "term": "SynthID Latent Watermarking",
                "def": "Google's imperceptible digital watermarking technique embedded directly into generative AI pixel latents.",
                "defKo": "구글 SynthID 잠재 공간 워터마킹"
            }
        ]
    },
    # Slide 29: The Conductor Persona: Active Ethical Stewardship
    {
        "num": 29,
        "type": "content",
        "title": "THE CONDUCTOR: ACTIVE ETHICAL STEWARDSHIP",
        "subtitle": "Directing visual generative technology to inspire truth, human dignity, and cultural flourishing",
        "points": [
            "The Power of the Image: Visual cinema shapes the worldview, values, and hearts of millions of human beings.",
            "The Ethical Sovereign: Refusing to create degraded, exploitative, or deceitful synthetic media.",
            "Noble Storytelling: Using cinematic AI to tell stories of courage, redemption, sacrifice, and truth."
        ],
        "script": (
            "[Prof. Peter] Slide 29 reflects on \"THE CONDUCTOR PERSONA: ACTIVE ETHICAL STEWARDSHIP.\"\n\n"
            "[TA Sarah] The moving image is the most emotionally powerful medium ever invented—it shapes how millions of people view justice, love, family, and God.\n\n"
            "[TA James] As Intelligence Architects, we hold the conductor's baton: We reject cheap, degraded, sensationalist AI muck, and choose to produce noble cinema that uplifts the human spirit!\n\n"
            "[Prof. Peter] Let us inspect Soli Deo Gloria on Slide 30!"
        ),
        "koreanGuide": {
            "summary": "지휘관 페르소나: 인간 존엄성과 문화적 번영을 이끄는 능동적 윤리적 청지기직",
            "points": [
                "이미지의 힘: 영화와 영상은 수백만 사람들의 세계관, 가치관, 마음에 가장 강력한 영향을 미침",
                "윤리적 주권자: 저급하고 착취적이며 기만적인 합성 미디어 제작을 단호히 거부",
                "고결한 스토리텔링: 용기, 구속, 희생, 진리를 선포하는 고품격 시네마틱 서사 창출"
            ],
            "tips": "피터 교수와 사라 조교가 영상 미디어의 거대한 영향력과 창작자의 윤리적 소명감을 강조합니다."
        },
        "keyTerms": [
            {
                "term": "Ethical Visual Stewardship",
                "def": "The moral responsibility to produce media that honors human dignity, truthfulness, and cultural virtue.",
                "defKo": "윤리적 시각 청지기직"
            },
            {
                "term": "Redemptive Storytelling",
                "def": "Narrative architecture structured around themes of reconciliation, hope, sacrifice, and divine truth.",
                "defKo": "구속적 시네마틱 스토리텔링"
            }
        ]
    },
    # Slide 30: Soli Deo Gloria: The Visual Symphony of Truth
    {
        "num": 30,
        "type": "content",
        "title": "SOLI DEO GLORIA: VISUAL SYMPHONY",
        "subtitle": "Psalm 19:1: The heavens declare the glory of God; the skies proclaim the work of His hands",
        "points": [
            "Soli Deo Gloria: The supreme cornerstone of Oikos University and Smart Insight Lab.",
            "Psalm 19:1: 'The heavens declare the glory of God; the skies proclaim the work of His hands.'",
            "The Visual Symphony: Channeling cinematic AI to showcase the grandeur, beauty, and redemption of God."
        ],
        "script": (
            "[Prof. Peter] Slide 30 declares our sacred foundation: \"SOLI DEO GLORIA: THE VISUAL SYMPHONY OF TRUTH: To God Alone Be the Glory.\"\n\n"
            "[TA Sarah] In Psalm 19:1, Scripture sings: 'The heavens declare the glory of God; the skies proclaim the work of His hands.'\n\n"
            "[TA James] When we choreograph cinematic camera dollies, render golden hour sunlight, and score orchestral soundtracks, we are reflecting the glorious majesty of the Master Director who created the visual symphony of the universe!\n\n"
            "[Prof. Peter] May our generative cinema always reflect the beauty, love, and truth of God.\n\n"
            "[TA Sarah] Let us inspect our 6-step Hybrid Cinematic Blueprint on Slide 31!"
        ),
        "koreanGuide": {
            "summary": "Soli Deo Gloria: 시편 19편 1절과 진리의 시네마틱 시각 심포니",
            "points": [
                "시편 19편 1절: '하늘이 하나님의 영광을 선포하고 궁창이 그의 손으로 하신 일을 나타내는도다'",
                "우주의 최고 감독이신 하나님: 황금빛 석양과 오케스트라 사운드를 조율할 때 창조주의 웅장한 예술성을 반영",
                "모든 영상 창작물을 하나님의 영광과 그리스도의 복음을 전하는 도구로 헌정"
            ],
            "tips": "3인의 강사진이 시편 말씀을 낭독하며 시네마틱 영상 예술의 신학적 숭고함을 선포합니다."
        },
        "keyTerms": [
            {
                "term": "Soli Deo Gloria",
                "def": "The foundational theological motto dedicating all intellectual and technological mastery to the Glory of God Alone.",
                "defKo": "솔리 데오 글로리아 (오직 하나님께 영광)"
            },
            {
                "term": "Visual Symphony Principle",
                "def": "The theological framework viewing visual cinematography and audio composition as expressions of divine order.",
                "defKo": "시각적 심포니 창조 원리"
            }
        ]
    },
    # Slide 31: The 6-Step Hybrid Cinematic Blueprint
    {
        "num": 31,
        "type": "content",
        "title": "THE 6-STEP HYBRID CINEMATIC BLUEPRINT",
        "subtitle": "The standardized professional pipeline uniting Flow AI narrative with Runway camera precision",
        "points": [
            "Step 1: Script & Storyboard (Draft 12 scene beats and 4K keyframe images in Google Flow AI).",
            "Step 2: Ingredient Identity Locking (Lock actor faces, wardrobe, and hero props in Ingredient Vault).",
            "Step 3: Precision Camera Choreography (Export keyframes to Runway Gen-3; apply 5-channel Motion Brush).",
            "Step 4: Native 48kHz Audio & Music Synthesis (Generate synchronized Foley sound effects and score in Lyria 3 Pro).",
            "Step 5: Non-Linear Assembly (Import 4K clips and audio stems into Premiere/DaVinci for pacing cuts).",
            "Step 6: C2PA Cryptographic Provenance Sealing (Seal video with Ed25519 provenance watermark and publish)."
        ],
        "script": (
            "[TA Sarah] Slide 31 presents our master operational methodology: \"THE 6-STEP HYBRID CINEMATIC BLUEPRINT.\"\n\n"
            "[TA James] Follow this exact 6-step Hollywood pipeline: Step 1: Script in Flow AI. Step 2: Lock actor identities in the Ingredient Vault. Step 3: Choreograph camera trajectories in Runway Gen-3 with Motion Brush! Step 4: Generate 48kHz Foley audio and score in Lyria 3 Pro! Step 5: Assemble in DaVinci Resolve! Step 6: Seal with C2PA cryptographic provenance!\n\n"
            "[Prof. Peter] This structured 6-step blueprint guarantees Hollywood-grade cinematic quality at 1/100th the cost.\n\n"
            "[TA Sarah] Let us inspect our Pre-Release Production Checklist on Slide 32."
        ),
        "koreanGuide": {
            "summary": "하이브리드 시네마틱 6단계 표준 구현 청사진",
            "points": [
                "1단계: 각본 및 스토리보드 (Flow AI에서 12개 씬 비트 및 4K 키프레임 생성)",
                "2단계: 재료 정체성 고정 (Ingredient Vault에 배우 얼굴 및 소품 잠재 벡터 고정)",
                "3단계: 정밀 카메라 안무 (Runway Gen-3로 넘겨 5채널 모션 브러시 및 카메라 궤적 부여)",
                "4단계: 48kHz 오디오 합성 (Lyria 3 Pro로 효과음 및 오케스트라 배경음악 작곡)",
                "5단계: NLE 종합 편집 (다빈치 리졸브/프리미어에서 4K 컷 편집 및 사운드 믹싱)",
                "6단계: C2PA 암호화 출처 봉인 (Ed25519 워터마크 서명 날인 후 배포)"
            ],
            "tips": "제임스 조교가 6단계 절차를 완벽한 시네마틱 영상 제작 지침으로 일목요연하게 정리합니다."
        },
        "keyTerms": [
            {
                "term": "Hybrid Cinematic Blueprint",
                "def": "The standardized 6-stage engineering process governing multi-model video generation, camera control, and audio scoring.",
                "defKo": "하이브리드 시네마틱 표준 청사진"
            },
            {
                "term": "NLE Assembly Workflow",
                "def": "The post-production integration of AI-generated video and audio stems into non-linear editing software.",
                "defKo": "NLE 종합 편집 워크플로우"
            }
        ]
    },
    # Slide 32: Production Checklist: Pre-Release Verification
    {
        "num": 32,
        "type": "content",
        "title": "PRODUCTION CHECKLIST: PRE-RELEASE VERIFICATION",
        "subtitle": "The 6-gate audit every AI video project must pass before broadcast release",
        "points": [
            "Gate 1: Character facial identity consistency validated across 100% of scene cuts (zero morphing).",
            "Gate 2: Camera trajectory motion velocity verified free of jitter, stutter, or warped perspective.",
            "Gate 3: Native 48kHz audio and Foley impacts synchronized within 1-frame tolerance (33ms).",
            "Gate 4: 4K 60 FPS video mastering rendered with zero compression macro-blocking artifacts.",
            "Gate 5: C2PA cryptographic provenance metadata and SynthID watermark verified active.",
            "Gate 6: Final Director Cut approved and signed with Ed25519 master release key."
        ],
        "script": (
            "[TA James] Slide 32 presents our \"PRODUCTION CHECKLIST: PRE-RELEASE VERIFICATION.\"\n\n"
            "[TA Sarah] Before releasing any commercial video, audit all 6 gates: Gate 1: 100% actor facial consistency. Gate 2: Smooth camera velocity. Gate 3: Sub-frame 33ms audio synchronization. Gate 4: Zero 4K macro-blocking artifacts. Gate 5: C2PA provenance active. Gate 6: Ed25519 Director Cut sign-off!\n\n"
            "[Prof. Peter] Strict verification gates ensure that your films stand out with world-class excellence.\n\n"
            "[TA Sarah] Let us inspect our third enterprise case study on Slide 33!"
        ),
        "koreanGuide": {
            "summary": "프로덕션 체크리스트: 상업용 영상 배포 전 6대 검증 관문",
            "points": [
                "1관문: 씬 전체에서 주연 배우 얼굴 변형률 0% (완벽한 일관성 검증)",
                "2관문: 지터 및 화면 떨림 없는 매끄러운 카메라 속도 벡터 확인",
                "3관문: 1프레임(33ms) 이내의 완벽한 48kHz 효과음/오디오 싱크 일치",
                "4관문: 픽셀 뭉개짐(Macro-blocking) 없는 4K 60 FPS 마스터링 완결",
                "5관문: C2PA 디지털 출처 메타데이터 및 SynthID 워터마크 주입 확인",
                "6관문: 총괄 감독의 Ed25519 마스터 릴리스 전자서명 완료"
            ],
            "tips": "제임스 조교가 6대 검증 관문을 단호하게 체크리스트로 확인합니다."
        },
        "keyTerms": [
            {
                "term": "Pre-Release Broadcast Gate",
                "def": "A mandatory quality assurance gate auditing video temporal consistency, audio sync, and cryptographic provenance.",
                "defKo": "상업 방송 배포 전 검증 관문"
            },
            {
                "term": "Macro-Blocking Artifact",
                "def": "Visual compression distortion where video frames break into visible square pixel blocks.",
                "defKo": "매크로블록 압축 왜곡 결함"
            }
        ]
    },
    # Slide 33: Case Study 3: International Crisis Journalism Documentary
    {
        "num": 33,
        "type": "casestudy",
        "title": "CASE STUDY 3: CRISIS JOURNALISM DOCUMENTARY",
        "subtitle": "International Investigative Consortium synthesizes 20-minute humanitarian documentary in 24 hours",
        "company": "Global Investigative Journalism Consortium",
        "problem": "War zone conflict broke out in remote landlocked country; journalists could not safely enter, but world needed urgent humanitarian crisis visualization for UN emergency session.",
        "solution": "Built Flow AI & Runway pipeline from verified satellite imagery, eye-witness smartphone audio, and GPS coordinates: synthesized accurate 3D scene recreations.",
        "impact": "Produced 20-minute 4K documentary in 24 hours for $4,500; broadcast at UN Security Council, mobilizing $120M in emergency humanitarian aid.",
        "script": (
            "[Prof. Peter] Slide 33 presents \"CASE STUDY 3: INTERNATIONAL CRISIS JOURNALISM DOCUMENTARY.\"\n\n"
            "[TA Sarah] When a sudden humanitarian conflict erupted in a landlocked war zone, physical broadcast crews could not enter safely. Yet the United Nations Security Council was meeting in 24 hours to vote on emergency relief!\n\n"
            "[TA James] Investigative journalists used our Flow AI and Runway pipeline: feeding verified satellite radar maps, eye-witness smartphone audio recordings, and ground GPS coordinates to recreate photorealistic 3D battle scenes and refugee movements with 100% forensic accuracy!\n\n"
            "[Prof. Peter] The 20-minute documentary was produced in 24 hours for $4,500 and screened directly inside the UN chamber—mobilizing $120 million in life-saving humanitarian aid! That is the noble calling of Generative Cinema.\n\n"
            "[TA Sarah] Let us open Part 4 and review Session 14 Key Takeaways on Slide 34!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 3: 종군 취재 불가 분쟁 지역 24시간 만에 4K 다큐 완성 (UN 1억 2천만 달러 구호기금 유치)",
            "points": [
                "문제 상황: 접근 불가능한 분쟁 지역 발생, 24시간 뒤 UN 안보리 긴급 구호 표결에 제시할 영상 부재",
                "솔루션: 검증된 위성 레이더와 목격자 음성을 Flow AI 및 Runway에 주입 ➔ 100% 포렌식 정밀 3D 씬 재구성",
                "성과: 24시간 만에 4,500달러로 20분 다큐 완성 ➔ UN 안보리 상영 후 1억 2,000만 달러 긴급 구호기금 결의"
            ],
            "tips": "사라 조교와 피터 교수가 진실을 알리고 1억 2천만 달러 구호기금을 끌어낸 저널리즘 다큐의 위력을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Crisis Forensic Visualization",
                "def": "The ethical reconstruction of inaccessible conflict zones using verified multi-source sensor data and AI simulation.",
                "defKo": "위기 분쟁 포렌식 시각화"
            },
            {
                "term": "Humanitarian Relief Mobilization",
                "def": "Using high-impact cinematic documentary media to secure international funding and emergency assistance.",
                "defKo": "인도주의 구호기금 유치"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 34: Part 4 Section Divider
    {
        "num": 34,
        "type": "section",
        "title": "PART 4: THE HYBRID CINEMATIC PIPELINE & MASTERY",
        "subtitle": "Assembling the full studio, video game cutscenes, future horizons, and Hands-on Lab 14",
        "script": (
            "[TA Sarah] Look at Slide 34: \"PART 4: THE HYBRID CINEMATIC PIPELINE & MASTERY.\" Now we integrate all elements into our daily creative studio!\n\n"
            "[Prof. Peter] The future belongs not to the prompt gambler, but to the Master Conductor who coordinates multiple specialized AI models with artistic discipline.\n\n"
            "[TA James] In Part 4, we review Session 14 key takeaways, explore AAA video game cutscene synthesis, build the Life OS Studio Cockpit, dedicate our craft to Soli Deo Gloria, and execute Lab 14!\n\n"
            "[TA Sarah] Let us review Session 14 Summary on Slide 35!"
        ),
        "koreanGuide": {
            "summary": "Part 4 섹션 전환: 하이브리드 시네마틱 파이프라인 완성 및 종합 마스터리",
            "points": [
                "프롬프트 도박사를 넘어 다중 AI 모델을 예술적으로 조율하는 마스터 지휘관으로의 완성",
                "Session 14 핵심 요약 및 AAA 비디오 게임 실시간 시네마틱 컷씬 분석",
                "최종 대단원(Session 15: Soli Deo Gloria Zenith & Life OS Board) 예고 및 실습 14"
            ],
            "tips": "피터 교수가 하이브리드 스튜디오 완성을 선언하고 제임스가 종합 실습을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Hybrid Pipeline Mastery",
                "def": "The unified operational orchestration of multi-model generative video, motion tracking, and non-linear editing.",
                "defKo": "하이브리드 파이프라인 마스터리"
            },
            {
                "term": "Interactive Game Cinematics",
                "def": "Rendering dynamic AAA video game story cutscenes using real-time generative video neural models.",
                "defKo": "대화형 게임 시네마틱 컷씬"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 35: Session 14 Summary & Key Takeaways
    {
        "num": 35,
        "type": "content",
        "title": "SESSION 14 SUMMARY & KEY TAKEAWAYS",
        "subtitle": "Synthesizing the 4 foundational pillars of Cinematic AI and Multi-Model Hybrid Strategy",
        "points": [
            "Pillar 1: Dropping the Camera (Mastered generative curation, 3-image anchoring, and 80% cost reduction).",
            "Pillar 2: Google Flow AI Engine (Veo 3.1 4K physics, Lyria 3 Pro 48kHz audio, and Ingredients-to-Video).",
            "Pillar 3: Runway ML Precision (5-channel Motion Brush, Hitchcock camera controls, and Act-Two transfer).",
            "Pillar 4: Sovereign Hybrid Symphony (Assembling Flow AI world + Runway camera into certified C2PA cinema)."
        ],
        "script": (
            "[TA Sarah] Slide 35 synthesizes our \"SESSION 14 SUMMARY & 4 FOUNDATIONAL PILLARS.\"\n\n"
            "[TA James] Pillar 1: We dropped the physical camera for 80% cheaper generative curation! Pillar 2: Flow AI locks actor identities with native 48kHz audio! Pillar 3: Runway gives us surgical 5-channel Motion Brush camera control! And Pillar 4: The Hybrid Pipeline combines both into certified C2PA cinema masterpieces!\n\n"
            "[Prof. Peter] When these four pillars unite, you hold the power of an entire Hollywood movie studio in the palm of your hand.\n\n"
            "[TA Sarah] Let us inspect the Life OS Cinema Cockpit on Slide 36!"
        ),
        "koreanGuide": {
            "summary": "Session 14 요약 및 4대 핵심 축 총정리",
            "points": [
                "1대 축: 카메라를 내려놓고 생성형 큐레이션 및 3중 이미지 앵커링으로 80% 비용 절감",
                "2대 축: 구글 Flow AI 엔진 (Veo 3.1 4K 물리, Lyria 3 Pro 48kHz 오디오, 인물 일관성 고정)",
                "3대 축: Runway ML 정밀 제어 (5채널 모션 브러시, 히치콕 카메라 매트릭스, Act-Two)",
                "4대 축: 주권적 하이브리드 심포니 (Flow AI 월드 + Runway 카메라의 C2PA 암호화 마스터링)"
            ],
            "tips": "제임스 조교가 4대 축을 리듬감 있게 요약하여 학습 효과를 극대화합니다."
        },
        "keyTerms": [
            {
                "term": "Architectural Synthesis",
                "def": "The unified integration of generative storyboarding, physical motion choreography, and high-fidelity spatial audio.",
                "defKo": "아키텍처 통합 합성"
            },
            {
                "term": "Hollywood Studio Equivalence",
                "def": "Achieving the visual fidelity, narrative complexity, and acoustic richness of major film studios via AI pipelines.",
                "defKo": "헐리우드 스튜디오급 제작 역량"
            }
        ]
    },
    # Slide 36: Life OS Cinema & Video Production Cockpit
    {
        "num": 36,
        "type": "content",
        "title": "LIFE OS CINEMA & VIDEO COCKPIT",
        "subtitle": "Setting up your personal virtual movie studio: Flow AI canvas on left + DaVinci Resolve on right",
        "points": [
            "Cockpit Setup: Flow AI Storyboard & Runway controls on primary monitor; DaVinci Resolve timeline on secondary monitor.",
            "Local Actor & Asset Vault: Maintaining persistent character embeddings and CAD meshes in `.agents/cinema/`.",
            "Batch Scripting Engine: Driving overnight video generation runs via Python Interactions API scripts."
        ],
        "script": (
            "[Prof. Peter] Slide 36 outlines your personal setup: \"LIFE OS CINEMA & VIDEO PRODUCTION COCKPIT.\"\n\n"
            "[TA Sarah] How do you configure your daily video production environment? Keep Flow AI's storyboard and Runway's Motion Brush on your primary monitor. On your secondary monitor, maintain DaVinci Resolve for multi-track audio mixing and 4K color grading!\n\n"
            "[TA James] Maintain your persistent Actor Ingredient Vault in your `.agents/cinema/` directory, and launch batch rendering runs overnight via Python API scripts!\n\n"
            "[TA Sarah] Let us inspect the Project Evaluation Rubric on Slide 37."
        ),
        "koreanGuide": {
            "summary": "라이프 OS 시네마 콕핏: 듀얼 모니터 세팅과 배우 잠재 벡터 금고",
            "points": [
                "개발 콕핏 구성: 메인 모니터에 Flow AI/Runway 캔버스 + 서브 모니터에 다빈치 리졸브 타임라인",
                "로컬 배우 및 에셋 금고: 캐릭터 임베딩과 CAD 메쉬를 .agents/cinema/에 영구 축적",
                "배치 스크립팅 엔진: 파이썬 Interactions API로 밤샘 비디오 자동 렌더링 파이프라인 가동"
            ],
            "tips": "사라 조교와 제임스 조교가 실전 영화 감독의 듀얼 모니터 가상 스튜디오 세팅법을 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Virtual Cinema Cockpit",
                "def": "A multi-screen studio layout integrating generative AI web canvases with professional NLE video editing timelines.",
                "defKo": "가상 시네마 제작 콕핏"
            },
            {
                "term": "Actor Ingredient Vault",
                "def": "A local database of frozen facial embeddings and prop geometries used for recurring multi-shot video generation.",
                "defKo": "배우 인그리디언트 금고"
            }
        ]
    },
    # Slide 37: Project Evaluation Rubric for Session 14
    {
        "num": 37,
        "type": "content",
        "title": "PROJECT EVALUATION RUBRIC FOR SESSION 14",
        "subtitle": "Grading criteria: Character consistency (30%), Motion Brush camera precision (30%), 48kHz Audio sync (40%)",
        "points": [
            "Criterion 1 (30%): 100% actor facial identity preservation across minimum 3 distinct scene shots.",
            "Criterion 2 (30%): Verified multi-layer Motion Brush and deliberate 3D camera trajectory movements.",
            "Criterion 3 (40%): Synchronous 48kHz Foley sound effects, musical score integration, and valid Ed25519 receipt."
        ],
        "script": (
            "[TA Sarah] Slide 37 presents our \"PROJECT EVALUATION RUBRIC FOR SESSION 14.\"\n\n"
            "[TA James] Your lab submission will be graded on 3 strict criteria: 30% for actor facial identity preservation across 3 shots. 30% for verified Motion Brush and camera trajectory control. And 40% for synchronous 48kHz audio and score integration with an Ed25519 receipt!\n\n"
            "[Prof. Peter] Rigorous grading standards prepare you to build broadcast-certified media.\n\n"
            "[TA Sarah] Let us inspect the Grand Final Zenith on Slide 38!"
        ),
        "koreanGuide": {
            "summary": "Session 14 프로젝트 평가 루브릭: 인물 일관성(30%), 모션 브러시(30%), 48kHz 오디오(40%)",
            "points": [
                "기준 1 (30%): 최소 3개 이상의 서로 다른 컷에서 주연 배우 얼굴 일관성 100% 유지",
                "기준 2 (30%): 5채널 모션 브러시 활용 및 의도된 3D 카메라 궤적 연출 확인",
                "기준 3 (40%): 밀리초 단위 48kHz 효과음/배경음악 싱크 및 Ed25519 암호 서명 영수증 제출"
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
                "term": "Cinematic Proof of Mastery",
                "def": "Empirical verification demonstrating that a generated film sequence satisfies professional narrative and technical standards.",
                "defKo": "시네마틱 마스터리 실증"
            }
        ]
    },
    # Slide 38: Next Horizon: The Soli Deo Gloria Zenith & Life OS Board
    {
        "num": 38,
        "type": "content",
        "title": "NEXT HORIZON: SOLI DEO GLORIA ZENITH",
        "subtitle": "The Grand Capstone: Building your 9-Agent Personal Board of Directors and Future IT Ministry",
        "points": [
            "The 15-Session Summit: Uniting all 15 sessions (Agents, Search, RAG, Swarms, True Science, World Models, Cinema).",
            "The 9-Agent Life OS Board: 9 specialized AI advisors (Visionary, Architect, DevOps, Auditor, Health, Spiritual Conductor).",
            "Session 15 Preview: 100-hour weekly time redemption, final portfolio defense, and commissioning the Sovereign Architect."
        ],
        "script": (
            "[TA Sarah] Slide 38 previews our ultimate summit: \"NEXT HORIZON: THE SOLI DEO GLORIA ZENITH & LIFE OS BOARD OF DIRECTORS.\"\n\n"
            "[TA James] In Session 15, we reach the glorious mountain summit of our entire masterclass! We will synthesize all 15 sessions: building your Personal 9-Agent Life OS Board of Directors, redeeming 100 hours of life bandwidth every single week, and consecrating our IT mastery to Soli Deo Gloria!\n\n"
            "[Prof. Peter] It is the crowning capstone of the Sovereign Intelligence Architect.\n\n"
            "[TA Sarah] Let us inspect the Director's Aesthetic Reverence on Slide 39!"
        ),
        "koreanGuide": {
            "summary": "다음 지평 예고: 최종 대단원 Session 15 Soli Deo Gloria Zenith & 라이프 OS 이사회",
            "points": [
                "15강 대단원의 정점: 1강부터 14강까지의 모든 지능 기술(에이전트, RAG, 스웜, 과학, 월드 모델, 시네마) 총집결",
                "9인 에이전트 라이프 OS 이사회: 비전, 아키텍트, 데브옵스, 보안, 법률, 건강, 영적 지휘관 9대 자문단 구축",
                "주당 100시간의 생애 시간 구속(에베소서 5:16)과 지능 건축가 최종 임관식 예고"
            ],
            "tips": "사라 조교와 제임스 조교가 마지막 15강(최종 정상)의 웅장한 비전과 9인 이사회 구축을 예고합니다."
        },
        "keyTerms": [
            {
                "term": "Soli Deo Gloria Zenith",
                "def": "The ultimate capstone synthesis uniting all technical, operational, and spiritual dimensions of the curriculum.",
                "defKo": "솔리 데오 글로리아 제니스 (최종 대단원)"
            },
            {
                "term": "Life OS Board of Directors",
                "def": "A multi-agent autonomous advisory framework assisting human leaders across strategic, technical, and personal domains.",
                "defKo": "라이프 OS 9인 에이전트 이사회"
            }
        ]
    },
    # Slide 39: The Director's Aesthetic Reverence
    {
        "num": 39,
        "type": "content",
        "title": "THE DIRECTOR'S AESTHETIC REVERENCE",
        "subtitle": "Treating cinematic storytelling as a sacred medium to communicate truth, beauty, and redemption",
        "points": [
            "Reverence for Beauty: Recognizing that light, harmony, and dramatic redemption reflect divine craftsmanship.",
            "Refusing Cultural Degradation: Standing firm against cynical, vulgar, or nihilistic media trends.",
            "Broadcasting Hope: Illuminating dark corners of the world with stories of light, faith, and reconciliation."
        ],
        "script": (
            "[Prof. Peter] Slide 39 reflects on \"THE DIRECTOR'S AESTHETIC REVERENCE.\" In an age of synthetic noise, reverence is our north star.\n\n"
            "[TA Sarah] When we direct cinematic AI pipelines, we treat beauty and truth with sacred honor. We refuse to feed the world cynical or destructive media.\n\n"
            "[TA James] We craft films that ignite hope, inspire courage, and point human hearts toward the eternal light of God!\n\n"
            "[Prof. Peter] Let us inspect our fourth enterprise case study on Slide 40!"
        ),
        "koreanGuide": {
            "summary": "영화 감독의 미학적 경외감: 진리와 아름다움, 구속을 전하는 거룩한 매체로서의 시네마",
            "points": [
                "아름다움을 향한 경외: 빛, 화음, 극적 구속 서사 속에 깃든 하나님의 거룩한 솜씨를 겸손히 인정",
                "문화적 타락 거부: 냉소적이고 저급하며 허무주의적인 미디어 유행을 단호히 거부",
                "희망의 선포: 빛과 믿음, 화해의 시네마틱 서사로 세상의 어두운 구석을 환하게 밝힘"
            ],
            "tips": "피터 교수가 시네마틱 영상 예술을 통한 진리 선포와 문화적 변혁의 영적 소명을 감동적으로 선포합니다."
        },
        "keyTerms": [
            {
                "term": "Aesthetic Reverence",
                "def": "The artistic commitment to cultivating beauty, narrative integrity, and moral virtue in visual media.",
                "defKo": "미학적 경외감과 예술적 품격"
            },
            {
                "term": "Cultural Restoration",
                "def": "The strategic revitalization of arts, entertainment, and digital media through truth-centered storytelling.",
                "defKo": "문화 회복과 변혁"
            }
        ]
    },
    # Slide 40: Case Study 4: AAA Video Game Studio Interactive Cinematic Cutscenes
    {
        "num": 40,
        "type": "casestudy",
        "title": "CASE STUDY 4: AAA VIDEO GAME CUTSCENES",
        "subtitle": "Global Gaming Studio generates 120 minutes of 4K cinematic cutscenes in 3 weeks for $45,000",
        "company": "Top Global AAA Video Game Studio",
        "problem": "Developing 120 minutes of high-end 4K narrative cutscenes for an open-world RPG required 14 months of motion capture and $12M in outsourced CGI rendering budgets.",
        "solution": "Built Flow AI & Runway hybrid pipeline: fed game 3D character rigs; directed complex martial arts fights using Act-Two performance capture and Motion Brush.",
        "impact": "Generated all 120 minutes of 4K cinematic cutscenes in 3 weeks for $45,000 (99.6% cost reduction); game shipped 6 months ahead of schedule, generating $280M launch revenue.",
        "script": (
            "[Prof. Peter] Slide 40 presents \"CASE STUDY 4: AAA VIDEO GAME INTERACTIVE CINEMATIC CUTSCENES.\"\n\n"
            "[TA Sarah] A major video game studio creating an epic open-world RPG needed 120 minutes of cinematic story cutscenes. Traditional motion capture and CGI animation was budgeted at $12 million and 14 months of grueling crunch time!\n\n"
            "[TA James] They deployed our hybrid generative pipeline: feeding their 3D game character models into Flow AI, using Act-Two for martial arts fight acting, and Motion Brush for dynamic camera angles!\n\n"
            "[Prof. Peter] All 120 minutes of 4K cutscenes were produced in 3 weeks for $45,000! The game shipped 6 months ahead of schedule, generating $280 million in launch revenue! That is the revolutionary speed of Generative Cinema.\n\n"
            "[TA Sarah] Let us inspect our capstone enterprise case study on Slide 44!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 4: AAA 대작 게임 120분 4K 시네마틱 컷씬을 3주 만에 45,000달러로 완성 (2억 8천만 달러 매출)",
            "points": [
                "문제 상황: 120분 분량의 RPG 스토리 컷씬 제작에 14개월의 크런치와 1,200만 달러(약 160억 원) 모션캡처 비용 책정",
                "솔루션: 3D 캐릭터 모델을 Flow AI에 주입 ➔ Act-Two 무술 액션 연기 이식 ➔ Runway 모션 브러시 카메라 연출",
                "성과: 3주 만에 45,000달러로 120분 완성(99.6% 비용 절감), 출시일 6개월 앞당겨 2억 8,000만 달러(약 3,700억 원) 매출 달성"
            ],
            "tips": "사라 조교와 제임스 조교가 1,200만 달러 모션캡처를 45,000달러로 끝낸 게임 산업의 혁명적 사례를 전달합니다."
        },
        "keyTerms": [
            {
                "term": "Real-Time Cutscene Synthesis",
                "def": "The rapid generation of narrative cinematic sequences for video games using neural video models.",
                "defKo": "실시간 게임 컷씬 합성"
            },
            {
                "term": "Game Crunch Elimination",
                "def": "Shattering long development overtime cycles by automating complex CGI animation and rendering workflows.",
                "defKo": "게임 개발 크런치 근절"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 41: The Economics of Generative Media Production
    {
        "num": 41,
        "type": "content",
        "title": "THE ECONOMICS OF GENERATIVE MEDIA",
        "subtitle": "Compressing multi-million dollar film production barriers into accessible cloud compute budgets",
        "points": [
            "The 100X Studio Multiplier: A 3-person creative team produces the output of a 300-person Hollywood post-production studio.",
            "Democratizing Global Voices: Enabling African, Asian, and Latin American storytellers to produce 4K blockbusters.",
            "Eliminating Capital Gatekeepers: Creators retain 100% intellectual property ownership and financial independence."
        ],
        "script": (
            "[Prof. Peter] Slide 41 analyzes \"THE ECONOMICS OF GENERATIVE MEDIA PRODUCTION: The 100X Studio Multiplier.\"\n\n"
            "[TA Sarah] In the old world, only 5 Hollywood conglomerate studios controlled film distribution because only they could afford $100M production budgets!\n\n"
            "[TA James] Generative AI breaks that monopoly forever: A 3-person team with Flow AI and Runway produces the same visual fidelity as a 300-person studio! Independent filmmakers retain 100% of their IP and profits!\n\n"
            "[Prof. Peter] Let us inspect Redeeming Time on Slide 42."
        ),
        "koreanGuide": {
            "summary": "생성형 미디어의 경제학: 100배 스튜디오 생산성 승수와 글로벌 창작자 해방",
            "points": [
                "100배 스튜디오 승수: 3명의 크리에이터 팀이 300명 규모 헐리우드 대형 포스트 프로덕션의 결과물 산출",
                "글로벌 목소리의 민주화: 아시아, 아프리카, 남미의 독립 창작자들도 4K 글로벌 블록버스터 직접 제작",
                "자본 게이트키퍼 붕괴: 거대 투자 배급사에 종속되지 않고 창작자가 지식재산권(IP)과 수익 100% 보유"
            ],
            "tips": "제임스 조교가 거대 영화 자본의 독점을 깨뜨리는 생성형 미디어의 민주화 파워를 설명합니다."
        },
        "keyTerms": [
            {
                "term": "100X Studio Multiplier",
                "def": "The exponential amplification of creative productivity allowing micro-teams to match legacy studio output.",
                "defKo": "100배 스튜디오 생산성 승수"
            },
            {
                "term": "IP Sovereign Creator",
                "def": "An independent filmmaker retaining total ownership of copyright and commercial monetization rights.",
                "defKo": "지식재산권(IP) 주권 창작자"
            }
        ]
    },
    # Slide 42: Redeeming the Time: Asynchronous Rendering Mastery
    {
        "num": 42,
        "type": "content",
        "title": "REDEEMING THE TIME: ASYNCHRONOUS RENDERING",
        "subtitle": "Ephesians 5:16: Launching 50 scene render jobs overnight and waking up to completed 4K timelines",
        "points": [
            "Overnight Batch Rendering: Queueing 50 Runway and Flow AI scene variations at 10:00 PM; reviewing at 7:00 AM.",
            "Liberating Human Soul: Eliminating endless hours of waiting for render progress bars to finish.",
            "The Consecrated Life: Investing our redeemed time into mentorship, prayer, family, and strategic ministry."
        ],
        "script": (
            "[TA Sarah] Slide 42 proclaims \"REDEEMING THE TIME: ASYNCHRONOUS RENDERING MASTERY.\"\n\n"
            "[TA James] In legacy film editing, editors sat in dark rooms staring at render progress bars for 10 hours straight! In our hybrid pipeline, you queue 50 scene generation runs before bed!\n\n"
            "[Prof. Peter] You sleep peacefully while the cloud TPU clusters render your movie. In the morning, you review the completed 4K timeline in DaVinci Resolve. We redeem finite hours for eternal kingdom purpose.\n\n"
            "[TA Sarah] Let us inspect the Future of Cinematic AI on Slide 43!"
        ),
        "koreanGuide": {
            "summary": "세월을 아끼라: 비동기 렌더링을 통한 밤샘 50개 씬 자동 완성과 생애 시간 구속",
            "points": [
                "밤샘 배치 렌더링: 밤 10시에 50개 씬 생성 큐 실행 ➔ 아침 7시에 완성된 4K 타임라인 검토",
                "렌더링 진행바 노역 해방: 하루 종일 컴퓨터 모니터의 진행바만 쳐다보던 소모적 시간 종식",
                "구속된 생애 시간: 확보된 시간과 지적 에너지를 멘토링, 기도, 가족, 전략적 사역에 온전히 헌신"
            ],
            "tips": "피터 교수가 밤샘 비동기 렌더링의 시간 구속 가치를 에베소서 말씀과 연결합니다."
        },
        "keyTerms": [
            {
                "term": "Asynchronous Batch Video Queuing",
                "def": "Submitting multi-scene generation jobs to execute in parallel across cloud clusters without manual intervention.",
                "defKo": "비동기 일괄 비디오 렌더링 큐"
            },
            {
                "term": "Life Bandwidth Consecration",
                "def": "The intentional dedication of reclaimed professional hours toward higher spiritual, familial, and strategic pursuits.",
                "defKo": "생애 대역폭 성별 및 헌신"
            }
        ]
    },
    # Slide 43: The Future of Cinematic AI: The Sovereign Horizon
    {
        "num": 43,
        "type": "content",
        "title": "THE FUTURE OF CINEMATIC AI: SOVEREIGN HORIZON",
        "subtitle": "Uniting Generative Video, World Models, and Autonomous Swarms under Soli Deo Gloria",
        "points": [
            "The Ultimate Creative Convergence: Swarms (Session 10) + World Models (Session 12) + Cinema (Session 14).",
            "Real-Time Interactive Holodecks: Interactive movies where viewers step into the 3D scene and speak with characters.",
            "The Intelligence Architect: Standing as a visionary leader who harmonizes technology and human wisdom."
        ],
        "script": (
            "[Prof. Peter] Slide 43 unveils \"THE FUTURE OF CINEMATIC AI: THE SOVEREIGN HORIZON.\"\n\n"
            "[TA Sarah] Look at the summit we have climbed: Multi-Agent Swarms in Session 10, True AI Science in Session 11, World Models in Session 12, Calculated Vectors in Session 13, and Cinematic Pipelines in Session 14!\n\n"
            "[TA James] In the near future, cinema and interactive world models will merge: viewers will step directly inside the movie, exploring 3D physical sets and conversing with characters in real time!\n\n"
            "[Prof. Peter] Let us inspect our capstone enterprise case study on Slide 44!"
        ),
        "koreanGuide": {
            "summary": "시네마틱 AI의 미래: 5대 거대 지능의 융합과 대화형 홀로덱 시네마의 도래",
            "points": [
                "거대한 융합(Convergence): 93개 스웜(10강) + 참된 과학(11강) + 월드 모델(12강) + 벡터(13강) + 시네마(14강)",
                "실시간 대화형 홀로덱 시네마: 관객이 3D 영화 속으로 직접 걸어 들어가 등장인물과 실시간 대화하는 미래",
                "지능 건축가의 비전: 기술 문명의 최첨단에서 인간의 존엄성과 하나님의 영광을 선포하는 리더십"
            ],
            "tips": "사라 조교와 피터 교수가 지금까지 배운 모든 세션이 하나로 융합되는 미래 영화의 경이로운 지평을 선언합니다."
        },
        "keyTerms": [
            {
                "term": "Interactive Holodeck Cinema",
                "def": "The convergence of generative 3D world simulation and cinematic storytelling allowing audiences to enter narrative spaces.",
                "defKo": "대화형 홀로덱 시네마"
            },
            {
                "term": "Holistic Intelligence Mastery",
                "def": "The comprehensive integration of autonomous multi-agent engineering, physical simulation, and generative media.",
                "defKo": "전인적 지능 마스터리"
            }
        ]
    },
    # Slide 44: Case Study 5: 80% Production Cost Slicing & Enterprise Video ROI
    {
        "num": 44,
        "type": "casestudy",
        "title": "CASE STUDY 5: 80% VIDEO COST SLICING ROI",
        "subtitle": "Global Fortune 500 Consumer Brand produces 500 commercial videos yearly, saving $14.2M annually",
        "company": "Global Fortune 500 Consumer Packaged Goods Conglomerate",
        "problem": "Company managed 40 consumer food/beverage brands; producing 500 commercial social media videos annually across global agencies cost $18M and took 9 months.",
        "solution": "Deployed centralized 6-step Hybrid Cinematic blueprint: standardized on Flow AI for storyboarding/audio and Runway for camera choreography.",
        "impact": "Production cost sliced by 82% ($14.2M annual savings); average video turnaround collapsed from 6 weeks to 3 days; brand engagement jumped by 64%.",
        "script": (
            "[Prof. Peter] Slide 44 presents our capstone enterprise case study: \"CASE STUDY 5: 80% PRODUCTION COST SLICING & ENTERPRISE VIDEO ROI BLUEPRINT.\"\n\n"
            "[TA Sarah] A global Fortune 500 consumer conglomerate managing 40 food and beverage brands was spending 18 million dollars every year on advertising agencies to produce 500 video commercials worldwide, with a sluggish 6-week turnaround per video!\n\n"
            "[TA James] They deployed our centralized 6-step Hybrid Cinematic blueprint: establishing an in-house team of 4 Intelligence Architects who directed Flow AI for product storyboards and native audio, and Runway for high-speed dynamic camera movements!\n\n"
            "[Prof. Peter] Look at the enterprise ROI: annual video production costs collapsed by 82%—saving 14.2 million dollars every single year! Video turnaround dropped from 6 weeks to 3 days, and social media consumer engagement jumped by 64%!\n\n"
            "[TA Sarah] That is the ultimate enterprise transformation.\n\n"
            "[TA James] Now let us direct your own 60-Second Hybrid Masterpiece in Lab 14 on Slide 45!"
        ),
        "koreanGuide": {
            "summary": "케이스 스터디 5: 포춘 500대 기업 500편 광고 82% 비용 절감 (연간 1,420만 달러 순이익)",
            "points": [
                "문제 상황: 40개 소비재 브랜드의 연간 500편 광고 제작에 외주 대행사 비용 1,800만 달러(약 240억 원)와 9개월 소요",
                "솔루션: 6단계 하이브리드 청사진 사내 도입 ➔ 4명의 지능 건축가가 Flow AI와 Runway로 전사 영상 전담 제작",
                "성과: 제작비 82% 절감(연간 1,420만 달러 / 약 190억 원 절감), 제작 기간 6주 ➔ 3일 단축, 브랜드 참여도 64% 급증"
            ],
            "tips": "사라 조교와 제임스 조교가 190억 원 절감과 3일 제작의 압도적 엔터프라이즈 성과를 전하며 실습으로 유도합니다."
        },
        "keyTerms": [
            {
                "term": "80% Production Cost Slicing",
                "def": "The radical reduction in corporate video production expenditure achieved by transitioning to internal AI hybrid studios.",
                "defKo": "80% 영상 제작비 절감 승수"
            },
            {
                "term": "Enterprise Video Turnaround",
                "def": "Compressing commercial advertising development cycles from multiple weeks to mere days.",
                "defKo": "엔터프라이즈 영상 제작 주기 단축"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    },
    # Slide 45: Hands-on Lab 14 & Conclusion
    {
        "num": 45,
        "type": "lab",
        "title": "🛠️ HANDS-ON LAB 14 & CONCLUSION",
        "subtitle": "Directing a 60-Second Multi-Model Hybrid Cinematic Masterpiece",
        "mission": "Direct a complete 60-second broadcast-ready cinematic trailer using Google Flow AI and Runway ML: lock 2 character identities, choreograph 5-channel Motion Brush camera trajectories, synthesize synchronous 48kHz audio/music in Lyria 3 Pro, and export a C2PA signed master.",
        "steps": [
            "Step 1: Write a 4-scene narrative script in Google Flow AI and generate 4K storyboard keyframes.",
            "Step 2: Lock your lead actor's facial identity in the Ingredient Vault using 2 reference portraits.",
            "Step 3: Export keyframes to Runway Gen-3: apply 5-channel Motion Brush and camera velocity matrices.",
            "Step 4: Generate synchronous 48kHz Foley sound effects and an orchestral score in Lyria 3 Pro.",
            "Step 5: Assemble in DaVinci Resolve, verify sub-frame 33ms sync, and sign with an Ed25519 C2PA master receipt!"
        ],
        "script": (
            "[TA Sarah] Here we are at Slide 45: \"🛠️ HANDS-ON LAB 14 & SESSION CONCLUSION!\"\n\n"
            "[TA James] Tonight's hands-on lab turns you into a Hollywood Generative Film Director! Step 1: Script your 4-scene story in Flow AI. Step 2: Lock your actor's face in the Ingredient Vault! Step 3: Choreograph camera moves in Runway with Motion Brush! Step 4: Generate 48kHz Foley audio and score in Lyria 3 Pro! Step 5: Assemble in DaVinci Resolve and export your C2PA signed master video!\n\n"
            "[Prof. Peter] Once you master this hybrid cinematic pipeline, you hold the power to move human hearts and inspire the world.\n\n"
            "[TA Sarah] In our next and final session, Session 15, we reach the glorious mountain peak: The Soli Deo Gloria Zenith & The 9-Agent Life OS Board of Directors!\n\n"
            "[Prof. Peter] On behalf of TA Sarah Jenkins, TA James Wilson, and the entire Smart Insight Lab, congratulations on mastering Session 14! Soli Deo Gloria, and we will see you at the grand summit in Session 15!"
        ),
        "koreanGuide": {
            "summary": "실습 과제 14 및 세션 마무리: 60초 하이브리드 시네마틱 명작 연출 및 마스터링",
            "points": [
                "실습 미션: Flow AI와 Runway를 조합하여 60초 상업 방송용 시네마틱 트레일러 연출",
                "배우 얼굴 일관성 고정, 5채널 모션 브러시 카메라 연출, 48kHz 효과음/오케스트라 배경음악 합성",
                "다빈치 리졸브 종합 편집, 서브프레임 싱크 검증 및 C2PA 암호화 서명 마스터 비디오 내보내기"
            ],
            "tips": "3인의 강사진이 오늘 수업의 성취를 축하하고 마지막 최종 세션(Session 15: The Soli Deo Gloria Zenith)의 정상 등극을 예고하며 마무리합니다."
        },
        "keyTerms": [
            {
                "term": "Hands-on Milestone",
                "def": "The practical engineering completion of a functioning technical artifact fulfilling the session's learning objectives.",
                "defKo": "실습 달성 마일스톤"
            },
            {
                "term": "Generative Cinema Director Certification",
                "def": "The formal mastery of multi-model video synthesis, camera choreography, spatial audio composition, and C2PA provenance.",
                "defKo": "생성형 시네마 총괄 감독 마스터 인증"
            }
        ],
        "instructor": "Prof. Peter Kim • TA Sarah Jenkins • TA James Wilson • Smart Insight Lab"
    }
]

def generate_session14_md(slides):
    lines = []
    lines.append("# Session 14: Cinematic AI Pipelines: Google Flow AI vs. Runway ML Hybrid Strategy")
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
    new_export = f"export const SLIDES_SESSION_14 = {slides_json};"
    
    pattern = r"export\s+const\s+SLIDES_SESSION_14\s*=\s*\[[\s\S]*?\];"
    if re.search(pattern, content):
        updated_content = re.sub(pattern, lambda m: new_export, content, count=1)
        with open(SLIDES_DATA_JS, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Successfully updated SLIDES_SESSION_14 in slidesData.js!")
    else:
        print("Could not find SLIDES_SESSION_14 pattern in slidesData.js!")

def main():
    print(f"Total slides configured: {len(SLIDES_45_SESSION_14)}")
    
    # Verify part dividers
    part_slides = [s for s in SLIDES_45_SESSION_14 if s['type'] == 'section']
    print(f"Total PART Section Slides: {len(part_slides)}")
    for ps in part_slides:
        print(f"  Slide {ps['num']:02d}: {ps['title']}")
        
    # Verify case studies
    case_slides = [s for s in SLIDES_45_SESSION_14 if 'CASE STUDY' in s['title']]
    print(f"Total Case Study Slides: {len(case_slides)}")
    for cs in case_slides:
        print(f"  Slide {cs['num']:02d}: {cs['title']}")

    # 1. Write session14.md
    session14_md_content = generate_session14_md(SLIDES_45_SESSION_14)
    with open(SESSION14_MD, 'w', encoding='utf-8') as f:
        f.write(session14_md_content)
    print(f"Successfully generated and saved {SESSION14_MD} ({len(session14_md_content)} bytes)")
    
    # 2. Update slidesData.js
    update_slides_data_js(SLIDES_45_SESSION_14)
    
    print("Session 14 generation completed successfully!")

if __name__ == '__main__':
    main()
