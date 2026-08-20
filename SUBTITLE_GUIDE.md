# 🎬 Oikos University 강의 동영상 자막 제작 & 싱크 파이프라인 가이드

이 문서는 **대학 LMS 탑재용 고화질 강의 영상(Session 1~15)**에 대해 **Presenter Mode의 정본 스크립트**와 **실제 녹화 음성의 발화 타임라인**을 100% 일치시켜 자막을 생성하고 합성(Burn-in)하는 전체 워크플로우와 운영 지침을 정리한 가이드입니다.

---

## 📌 1. 핵심 원칙 (Core Principles)

1. **텍스트(Text)**: **Presenter Mode(`src/data/slidesData.js`)의 정본 스크립트 100% 적용**
   * 음성 인식기(ASR)의 발음 오탈자나 단어 왜곡을 배제하고, 교수님께서 사전에 집필하신 **표준 영문법, 전문 학술 어휘, `Oikos University`, `Soli Deo Gloria`, `The Architect of Intelligence` 등 정본 텍스트**만을 화면에 출력합니다.
2. **타임스탬프(Sync)**: **각 슬라이드 녹화 클립의 실제 음성 발화 구간 1:1 동기화**
   * 단순 시간 균등 분할이 아닌, 각 문장이 발화되는 실제 호흡 구간(시작 초 ~ 종료 초)에 문장을 배치하여 **슬라이드 첫 시작부터 마지막 1초까지 자연스럽게 완주**되도록 동기화합니다.
3. **하드서브(Burn-in) 인코딩**:
   * 대학 LMS의 비디오 플레이어 호환성 및 모바일/태블릿 환경에 구애받지 않도록 **반투명 블랙 박스(`BorderStyle=4`) + 선명한 흰색 폰트** 스타일로 영상 자체에 자막을 구워 넣습니다.

---

## 🔍 2. 씽크 불일치 원인 분석 및 교훈 (Lessons Learned)

| 문제 유형 | 발생 원인 | 해결 및 예방 대책 |
| :--- | :--- | :--- |
| **슬라이드 누락** | 녹화 완료 후 슬라이드 덱에 새로운 슬라이드(예: Part 1 간지 슬라이드)를 추가하여 **녹화된 클립 수(39개)와 슬라이드 덱(40개) 불일치** | 녹화 전 슬라이드 번호(1~40)와 Presenter Mode 스크립트 번호가 1:1로 일치하는지 최종 확인 후 녹화 |
| **내용 불일치** | 문서 기획안(`session1.md`)과 웹 앱 화면(`slidesData.js`)의 스크립트가 다를 때 발생 | **녹화 시 화면에 띄워둔 Presenter Mode 스크립트(`slidesData.js`)**를 단일 진실 공급원(SSOT)으로 지정하여 자막 추출 |
| **자막 조기 종료** | 단순 시간 균등 분할 시, 슬라이드가 끝나기도 전에 자막이 먼저 소진되는 현상 | **단어별 발화 타임스탬프(Word Timestamps) 비례 매핑**을 적용하여 슬라이드 마지막 발화 시점까지 균형 있게 표시 |

---

## 🚀 3. 재녹화 후 원클릭 자막 생성 & 비디오 합성 워크플로우

슬라이드를 새롭게 녹화하신 후 아래의 순서대로 실행하시면 클릭 한 번으로 모든 자막과 영상이 완성됩니다.

### Step 1. 슬라이드별 40개 클립 녹화
* [https://oikos-lecture-app-nu.vercel.app/](https://oikos-lecture-app-nu.vercel.app/) 의 **Presenter Mode**를 보시며 슬라이드 1번부터 40번까지 순서대로 녹화합니다.
* 원본 파일들을 `c:\Oikos Univ\files\` 폴더에 배치합니다.

### Step 2. 마우스 클릭 잡음 제거 & 클립 클리닝
```bash
python process_all_clips_declick.py
```
* 40개 클립의 마우스 클릭 잡음을 무음 처리하고 `files_cleaned/slide_01_clean.mp4` ~ `slide_40_clean.mp4`를 생성합니다.

### Step 3. Presenter Mode 최신 스크립트 추출
```bash
node -e "
import('./src/data/slidesData.js').then(m => {
  const fs = require('fs');
  const slides = m.SLIDES_SESSION_1;
  const scriptMap = {};
  slides.forEach(s => { scriptMap[s.num] = { num: s.num, title: s.title, script: s.script }; });
  fs.writeFileSync('files_analysis/presenter_mode_session1_scripts.json', JSON.stringify(scriptMap, null, 2), 'utf-8');
  console.log('Presenter scripts exported!');
});
"
```

### Step 4. 정밀 자막 생성 & 최종 비디오 합성 (원클릭)
```bash
python build_presenter_mode_subtitles.py
```
* **동작 내용**:
  1. 40개 슬라이드의 오디오 발화 구간을 분석
  2. Presenter Mode 스크립트 문장들을 각 슬라이드 구간에 1:1로 정밀 매핑
  3. `Session1_Lecture.srt` 및 `Session1_Lecture.vtt` 생성
  4. FFmpeg 비디오 필터(`subtitles`)를 적용하여 1080p 고화질 하드서브 영상(`Session1_Full_Lecture_Subtitled.mp4`) 자동 렌더링

---

## 📁 4. 최종 산출물 명세

* **`Session1_Full_Lecture_Subtitled.mp4`** (약 66~68 MB / 45분)
  * **대학 LMS 메인 탑재용 최종 비디오** (별도 설정 없이 재생 시 고화질 자막 100% 출력)
* **`Session1_Lecture.srt`**
  * 표준 타임코드 자막 파일
* **`Session1_Lecture.vtt`**
  * LMS 플레이어의 CC(자막 선택 켜기/끄기) 기능 탑재 시 업로드용 WebVTT 파일

---

## 🎨 5. 자막 디자인 스타일 가이드

* **폰트**: Arial / Pretendard (1080p 해상도 기준 `FontSize=20`)
* **색상**: `PrimaryColour=&H00FFFFFF` (선명한 화이트)
* **배경 박스**: `BackColour=&H80000000` (50% 반투명 블랙) + `BorderStyle=4` (Opaque Box)
* **위치**: `Alignment=2` (하단 중앙), `MarginV=30` (하단 슬라이드 내용 가림 방지 30px 여백)
