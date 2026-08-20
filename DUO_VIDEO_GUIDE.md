# 🎬 2-Presenter Duo Lecture MP4 Video Generator Guide

Oikos University **"The Architect of Intelligence"** Session 1의 **남녀 2인 듀오 (Prof. Peter Kim & TA Sarah Jenkins)** 강의를 초고화질 1080p MP4 영상으로 자동 렌더링하는 통합 파이프라인 가이드입니다.

---

## 🎙️ 페르소나 및 음성 사양
| 역할 | 인물 | 나이 | Microsoft Neural Voice | 특성 |
| :--- | :--- | :--- | :--- | :--- |
| **Lead Instructor** | **Prof. Peter Kim** | 54세 | `en-US-ChristopherNeural` | 중후하고 신뢰감 있는 석학 교수 톤 (Rate -2%, Pitch -2Hz) |
| **Research TA** | **TA Sarah Jenkins** | 31세 | `en-US-JennyNeural` | 지적이고 밝고 생동감 넘치는 스마트 조교 톤 (Rate +3%, Pitch +1Hz) |

---

## 🚀 사용 방법 (Usage)

### 1. 단일 슬라이드 비디오 생성
```bash
# Slide 1 비디오 생성
python build_duo_lecture_mp4.py --slide 1

# Slide 8 비디오 생성
python build_duo_lecture_mp4.py --slide 8
```

### 2. 특정 슬라이드 다중 선택 생성
```bash
python build_duo_lecture_mp4.py --slides 1,2,8,14,40
```

### 3. 전체 40개 슬라이드 일괄 생성 & 60분 마스터 합본 영상 제작
```bash
python build_duo_lecture_mp4.py --all
```

---

## 📁 산출물 디렉토리 (`c:\Oikos Univ\duo_videos\`)
- 🎞️ `Session1_Slide_XX_DuoLecture.mp4`: 1080p 고화질 슬라이드 영상 (H.264 + AAC 192k)
- 📝 `Slide_XX_Subtitles.srt`: 발화자 태그가 포함된 정밀 싱크 자막 파일
- 📸 `slide_images/slide_XX.png`: 웹 앱에서 캡처한 1920x1080 고해상도 슬라이드 원본
- 🎙️ `audio_segments/`: 발화자별 및 턴별 합성된 MP3 오디오 트랙
- 🏆 `Session1_Full_60Min_DuoLecture_Master.mp4`: 40개 슬라이드 전체를 하나로 합친 60분 마스터 강의 비디오 ( `--all` 실행 시 자동 생성)
