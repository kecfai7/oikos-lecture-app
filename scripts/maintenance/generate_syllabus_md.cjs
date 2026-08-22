const fs = require('fs');
const path = require('path');
const { COURSE_INFO, SESSIONS_CURRICULUM } = require('./src/data/courseCurriculum.js');

let md = `# ${COURSE_INFO.courseTitle}\n\n`;
md += `**Course Code:** ${COURSE_INFO.courseCode}  \n`;
md += `**Institution:** ${COURSE_INFO.institution}  \n`;
md += `**Department:** ${COURSE_INFO.department}  \n`;
md += `**Motto:** ${COURSE_INFO.motto}  \n`;
md += `**Instructor:** ${COURSE_INFO.instructor}  \n`;
md += `**Total Structure:** ${COURSE_INFO.duration}  \n\n`;
md += `> **Course Overview:** ${COURSE_INFO.description}\n\n`;
md += `---\n\n## 📌 Master Course Navigation & Table of Contents\n\n`;

SESSIONS_CURRICULUM.forEach((s) => {
  const numStr = String(s.sessionNum).padStart(2, '0');
  const slug = `session-${s.sessionNum}-${s.title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '')}`;
  md += `- [**Session ${numStr}: ${s.title}**](#${slug})\n`;
  s.parts.forEach((p) => {
    md += `  - **Part ${p.partNum}:** ${p.title} (${p.slideRange})\n`;
  });
});

md += `\n---\n\n## 📚 Detailed 15-Week Curriculum & Learning Objectives\n\n`;

SESSIONS_CURRICULUM.forEach((s) => {
  const numStr = String(s.sessionNum).padStart(2, '0');
  md += `### Session ${numStr}: ${s.title}\n\n`;
  md += `**Theme:** \`${s.theme}\`  \n`;
  md += `**Total Slides:** 40 Slides (60 Minutes)  \n\n`;

  md += `#### 🎯 Core Learning Objectives\n`;
  s.learningObjectives.forEach((obj, i) => {
    md += `${i + 1}. ${obj}\n`;
  });
  md += `\n`;

  md += `#### 🏛️ 4-Part Architecture & Slide Breakdown\n\n`;
  s.parts.forEach((p) => {
    md += `##### [${p.slideRange}] ${p.title}\n`;
    md += `- **Summary:** ${p.summary}\n`;
    if (p.keyTopics && p.keyTopics.length > 0) {
      md += `- **Key Topics:** \`${p.keyTopics.join('` • `')}\`\n`;
    }
    md += `\n`;
  });

  md += `#### 🛠️ Hands-on Lab & Capstone Assignment\n`;
  md += `- **Mission:** ${s.labMission}\n\n`;
  md += `---\n\n`;
});

const out1 = path.join(__dirname, 'SYLLABUS.md');
const out2 = path.join(__dirname, 'files', 'SYLLABUS.md');
fs.writeFileSync(out1, md, 'utf8');
fs.writeFileSync(out2, md, 'utf8');
console.log('Successfully generated pure English SYLLABUS.md and files/SYLLABUS.md!');
