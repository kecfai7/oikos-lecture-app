# 🎬 2-Presenter Duo Lecture MP4 Video Generator Guide

Oikos University **"The Architect of Intelligence"** Session 1의 **남녀 2인 듀오 (Prof. Peter Kim & TA Sarah Jenkins)** 강의를 초고화질 1080p MP4 영상으로 자동 렌더링하는 통합 파이프라인 가이드입니다.

---

## 🎙️ 페르소나 및 음성 사양
| 역할 | 인물 | 나이 | 음성 엔진 & 음색 변조 기술 | 특성 |
| :--- | :--- | :--- | :--- | :--- |
| **Lead Instructor** | **Prof. Peter Kim** | 54세 | **RVC-style Voice Morphing Engine**<br>(`files_cleaned/clean_*.wav` 교수님 실제 육성 프로필 적용) | 교수님 고유의 중저음 흉성 울림(120Hz)과 마이크 음향 공간감을 실시간 덧입힌 실제 맞춤형 음색 |
| **Research TA** | **TA Sarah Jenkins** | 31세 | `en-US-JennyNeural` | 지적이고 밝고 생동감 넘치는 스마트 조교 톤 (Rate +3%, Pitch +1Hz) |

---

## 🚀 사용 방법 (Usage)

### 1. 학생 2인 1조 과제: 지정 세션 및 슬라이드 영상 제작
```bash
# Session 4의 Slide 1 영상 제작
python build_duo_lecture_mp4.py --session 4 --slide 1

# Session 2의 Slide 1, 8, 20번 선택 제작
python build_duo_lecture_mp4.py --session 2 --slides 1,8,20
```

### 2. 특정 세션 40개 슬라이드 전체 60분 마스터 합본 영상 제작
```bash
# Session 2 전체 40슬라이드 마스터 영상 제작
python build_duo_lecture_mp4.py --session 2 --all

# Session 4 전체 40슬라이드 마스터 영상 제작
python build_duo_lecture_mp4.py --session 4 --all
```

---

## 📁 산출물 디렉토리 (`c:\Oikos Univ\duo_videos\`)
- 🎞️ `Session1_Slide_XX_DuoLecture.mp4`: 1080p 고화질 슬라이드 영상 (H.264 + AAC 192k)
- 📝 `Slide_XX_Subtitles.srt`: 발화자 태그가 포함된 정밀 싱크 자막 파일
- 📸 `slide_images/slide_XX.png`: 웹 앱에서 캡처한 1920x1080 고해상도 슬라이드 원본
- 🎙️ `audio_segments/`: 발화자별 및 턴별 합성된 MP3 오디오 트랙
- 🏆 `Session1_Full_60Min_DuoLecture_Master.mp4`: 40개 슬라이드 전체를 하나로 합친 60분 마스터 강의 비디오 ( `--all` 실행 시 자동 생성)
