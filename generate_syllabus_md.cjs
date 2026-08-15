const fs = require('fs');
const path = require('path');
const { COURSE_INFO, SESSIONS_CURRICULUM } = require('./src/data/courseCurriculum.js');

let md = `# ${COURSE_INFO.courseTitle}\n`;
md += `## ${COURSE_INFO.courseTitleKo}\n\n`;
md += `**Institution:** ${COURSE_INFO.institution}  \n`;
md += `**Motto:** ${COURSE_INFO.motto}  \n`;
md += `**Instructor:** ${COURSE_INFO.instructor}  \n`;
md += `**Total Scale:** ${COURSE_INFO.totalSessions} Sessions • ${COURSE_INFO.totalSlides} Slides (60 Minutes per Session)  \n\n`;
md += `> ${COURSE_INFO.descriptionKo}\n\n`;
md += `---\n\n## 📌 Master Course Navigation (전체 강좌 종합 목차)\n\n`;

SESSIONS_CURRICULUM.forEach((s) => {
  const numStr = String(s.sessionNum).padStart(2, '0');
  md += `- [**Session ${numStr}: ${s.titleKo}**](#session-${s.sessionNum}-${s.titleKo.toLowerCase().replace(/[^a-z0-9가-힣]+/g, '-')})\n`;
  s.parts.forEach((p) => {
    md += `  - **Part ${p.partNum}:** ${p.titleKo} (${p.slideRange})\n`;
  });
});

md += `\n---\n\n## 📚 Detailed 15-Session Curriculum & Learning Objectives\n\n`;

SESSIONS_CURRICULUM.forEach((s) => {
  const numStr = String(s.sessionNum).padStart(2, '0');
  md += `### Session ${numStr}: ${s.titleKo}\n`;
  md += `**English Title:** ${s.title}  \n`;
  md += `**Theme:** \`${s.theme}\`  \n\n`;

  md += `#### 🎯 Core Learning Objectives (핵심 학습 목표)\n`;
  s.learningObjectivesKo.forEach((objKo, i) => {
    md += `1. **${objKo}**  \n   _${s.learningObjectives[i]}_\n`;
  });
  md += `\n`;

  md += `#### 🏛️ 4-Part Structural Roadmap (대단원 4부 구조)\n\n`;
  s.parts.forEach((p) => {
    md += `##### [${p.slideRange}] Part ${p.partNum}: ${p.titleKo}\n`;
    md += `- **Original Title:** ${p.title}\n`;
    md += `- **Summary:** ${p.summaryKo}\n`;
    md += `- **English Summary:** _${p.summary}_\n`;
    if (p.keyTopics && p.keyTopics.length > 0) {
      md += `- **Key Topics:** \`${p.keyTopics.join('` • `')}\`\n`;
    }
    md += `\n`;
  });

  md += `#### 🛠️ Hands-on Lab & Capstone (실습 과제)\n`;
  md += `- **과제명:** ${s.labMissionKo}\n`;
  md += `- **Mission:** _${s.labMission}_\n\n`;
  md += `---\n\n`;
});

const out1 = path.join(__dirname, 'SYLLABUS.md');
const out2 = path.join(__dirname, 'files', 'SYLLABUS.md');
fs.writeFileSync(out1, md, 'utf8');
fs.writeFileSync(out2, md, 'utf8');
console.log('Successfully generated SYLLABUS.md and files/SYLLABUS.md!');
