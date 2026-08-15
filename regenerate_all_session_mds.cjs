const fs = require('fs');
const path = require('path');

const slidesDataPath = path.join(__dirname, 'src', 'data', 'slidesData.js');
let fileContent = fs.readFileSync(slidesDataPath, 'utf8');

fileContent = fileContent.replace(/export const SESSIONS =/g, 'const SESSIONS =');
for (let i = 1; i <= 15; i++) {
  const re = new RegExp(`export const SLIDES_SESSION_${i} =`, 'g');
  fileContent = fileContent.replace(re, `const SLIDES_SESSION_${i} =`);
}
fileContent += '\nmodule.exports = { SESSIONS, ' + Array.from({length: 15}, (_, i) => 'SLIDES_SESSION_' + (i+1)).join(', ') + ' };';

const tempPath = path.join(__dirname, 'temp_regen_all.cjs');
fs.writeFileSync(tempPath, fileContent, 'utf8');

const allData = require(tempPath);
fs.unlinkSync(tempPath);

const filesDir = path.join(__dirname, 'files');
if (!fs.existsSync(filesDir)) {
  fs.mkdirSync(filesDir, { recursive: true });
}

for (let sessId = 1; sessId <= 15; sessId++) {
  const slides = allData['SLIDES_SESSION_' + sessId];
  const sessMeta = allData.SESSIONS.find(s => s.id === sessId);
  const title = sessMeta ? sessMeta.title : `Session ${sessId}`;

  let mdContent = `# ${title}\n`;
  mdContent += `**Course:** The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom  \n`;
  mdContent += `**Instructor:** Professor Peter Kim, Director of Smart Insight Lab • Oikos University (www.oikos.edu)  \n`;
  mdContent += `**Total Slides:** 40 Slides (60 Minutes)  \n`;
  mdContent += `**Motto:** Soli Deo Gloria  \n\n`;
  mdContent += `---\n\n## 📌 Table of Contents (목차)\n`;

  slides.forEach((slide) => {
    const numStr = String(slide.num).padStart(2, '0');
    const sTitle = slide.title;
    const slug = `slide-${numStr}-${sTitle.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '')}`;
    mdContent += `- [Slide ${numStr}: ${sTitle}](#${slug})\n`;
  });

  mdContent += '\n---\n\n';

  slides.forEach((slide) => {
    const numStr = String(slide.num).padStart(2, '0');
    mdContent += `## Slide ${numStr}: ${slide.title}\n`;
    if (slide.subtitle) {
      mdContent += `**Subtitle:** ${slide.subtitle}\n\n`;
    }

    mdContent += `### 🎙️ English Lecture Script\n\n`;
    mdContent += `${(slide.script || '').trim()}\n\n`;

    if (slide.koreanGuide) {
      mdContent += `### 🇰🇷 Korean Teaching Guide (강의 가이드)\n`;
      if (slide.koreanGuide.summary) {
        mdContent += `- **강의 요약:** ${slide.koreanGuide.summary}\n`;
      }
      if (slide.koreanGuide.points && slide.koreanGuide.points.length > 0) {
        mdContent += `- **핵심 포인트:**\n`;
        slide.koreanGuide.points.forEach((pt) => {
          mdContent += `  - ${pt}\n`;
        });
      }
      if (slide.koreanGuide.tips) {
        mdContent += `- **강의 전달 팁:** ${slide.koreanGuide.tips}\n`;
      }
      mdContent += '\n';
    }

    if (slide.keyTerms && slide.keyTerms.length > 0) {
      mdContent += `### 📚 Key Terms (주요 용어)\n`;
      slide.keyTerms.forEach((kt) => {
        mdContent += `- **${kt.term}**: ${kt.def} (${kt.defKo})\n`;
      });
      mdContent += '\n';
    }

    mdContent += `---\n\n`;
  });

  const out1 = path.join(__dirname, `session${sessId}.md`);
  const out2 = path.join(filesDir, `session${sessId}.md`);
  fs.writeFileSync(out1, mdContent, 'utf8');
  fs.writeFileSync(out2, mdContent, 'utf8');
  console.log(`Generated session${sessId}.md and files/session${sessId}.md`);
}
console.log('All 15 session markdown files generated successfully!');
