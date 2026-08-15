const fs = require('fs');
const path = require('path');

const slidesDataPath = path.join(__dirname, 'src', 'data', 'slidesData.js');
let fileContent = fs.readFileSync(slidesDataPath, 'utf8');

// Transpile export const to module.exports for node evaluation
fileContent = fileContent.replace(/export const SESSIONS =/g, 'const SESSIONS =');
fileContent = fileContent.replace(/export const SLIDES_SESSION_1 =/g, 'const SLIDES_SESSION_1 =');
fileContent = fileContent.replace(/export const SLIDES_SESSION_2 =/g, 'const SLIDES_SESSION_2 =');
fileContent = fileContent.replace(/export const SLIDES_SESSION_3 =/g, 'const SLIDES_SESSION_3 =');
fileContent = fileContent.replace(/export const SLIDES_SESSION_4 =/g, 'const SLIDES_SESSION_4 =');
fileContent = fileContent.replace(/export const SLIDES_SESSION_5 =/g, 'const SLIDES_SESSION_5 =');
fileContent = fileContent.replace(/export const SLIDES_SESSION_6 =/g, 'const SLIDES_SESSION_6 =');
fileContent = fileContent.replace(/export const SLIDES_SESSION_7 =/g, 'const SLIDES_SESSION_7 =');
fileContent = fileContent.replace(/export const SLIDES_SESSION_8 =/g, 'const SLIDES_SESSION_8 =');
fileContent = fileContent.replace(/export const SLIDES_SESSION_9 =/g, 'const SLIDES_SESSION_9 =');
fileContent += '\nmodule.exports = { SESSIONS, SLIDES_SESSION_1, SLIDES_SESSION_2, SLIDES_SESSION_3, SLIDES_SESSION_4, SLIDES_SESSION_5, SLIDES_SESSION_6, SLIDES_SESSION_7, SLIDES_SESSION_8, SLIDES_SESSION_9 };';

// Write temp file to require
const tempPath = path.join(__dirname, 'temp_slides_data9.cjs');
fs.writeFileSync(tempPath, fileContent, 'utf8');

const { SESSIONS, SLIDES_SESSION_9 } = require(tempPath);

// Delete temp file
if (fs.existsSync(tempPath)) {
  fs.unlinkSync(tempPath);
}

console.log(`Loaded ${SLIDES_SESSION_9.length} slides for Session 9.`);

let mdContent = `# Session 9: Browser Security Fortress: Demystifying Chrome V8 Engine & Manifest V3's Ad-Blocker Suppression
**Course:** The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom  
**Instructor:** Professor Peter Kim, Director of Smart Insight Lab • Oikos University (www.oikos.edu)  
**Total Slides:** 40 Slides (60 Minutes)  
**Motto:** Soli Deo Gloria  

---

## 📌 Table of Contents (목차)
`;

SLIDES_SESSION_9.forEach((slide) => {
  const numStr = String(slide.num).padStart(2, '0');
  const title = slide.title;
  const slug = `slide-${numStr}-${title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '')}`;
  mdContent += `- [Slide ${numStr}: ${title}](#${slug})\n`;
});

mdContent += '\n---\n\n';

SLIDES_SESSION_9.forEach((slide) => {
  const numStr = String(slide.num).padStart(2, '0');
  mdContent += `## Slide ${numStr}: ${slide.title}\n`;
  if (slide.subtitle) {
    mdContent += `**Subtitle:** ${slide.subtitle}\n\n`;
  }

  mdContent += `### 🎙️ English Lecture Script\n\n`;
  mdContent += `${slide.script.trim()}\n\n`;

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

const outputPath1 = path.join(__dirname, 'session09.md');
const outputPath2 = path.join(__dirname, 'files', 'session09.md');

fs.writeFileSync(outputPath1, mdContent, 'utf8');

const filesDir = path.join(__dirname, 'files');
if (!fs.existsSync(filesDir)) {
  fs.mkdirSync(filesDir, { recursive: true });
}
fs.writeFileSync(outputPath2, mdContent, 'utf8');

console.log('Generated session09.md successfully!');
console.log(`Path 1: ${outputPath1}`);
console.log(`Path 2: ${outputPath2}`);
