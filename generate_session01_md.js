const fs = require('fs');
const path = require('path');

// Read slidesData.js content
const slidesDataPath = path.join(__dirname, 'src', 'data', 'slidesData.js');
let fileContent = fs.readFileSync(slidesDataPath, 'utf8');

// Transpile export const to module.exports for node evaluation
fileContent = fileContent.replace('export const SESSIONS =', 'const SESSIONS =');
fileContent = fileContent.replace('export const SLIDES_SESSION_1 =', 'const SLIDES_SESSION_1 =');
fileContent += '\nmodule.exports = { SESSIONS, SLIDES_SESSION_1 };';

// Write temp file to require
const tempPath = path.join(__dirname, 'temp_slides_data.cjs');
fs.writeFileSync(tempPath, fileContent, 'utf8');

const { SESSIONS, SLIDES_SESSION_1 } = require(tempPath);

// Delete temp file
fs.unlinkSync(tempPath);

console.log(`Loaded ${SLIDES_SESSION_1.length} slides for Session 1.`);

let mdContent = `# Session 1: From Waiting Chatbots to Sleep-Free Personal Avatars
**Course:** The Architect of Intelligence: Mastering Agentic IT & Strategic Wisdom  
**Instructor:** Professor Peter Kim, Director of Smart Insight Lab • Oikos University  
**Total Slides:** 40 Slides  

---

## 📌 Table of Contents (목차)
`;

SLIDES_SESSION_1.forEach(slide => {
  mdContent += `- [Slide ${String(slide.num).padStart(2, '0')}: ${slide.title}](#slide-${String(slide.num).padStart(2, '0')}-${slide.title.toLowerCase().replace(/[^a-z0-9]+/g, '-')})\n`;
});

mdContent += `\n---\n\n`;

SLIDES_SESSION_1.forEach(slide => {
  mdContent += `## Slide ${String(slide.num).padStart(2, '0')}: ${slide.title}\n`;
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
      slide.koreanGuide.points.forEach(pt => {
        mdContent += `  - ${pt}\n`;
      });
    }
    if (slide.koreanGuide.tips) {
      mdContent += `- **강의 전달 팁:** ${slide.koreanGuide.tips}\n`;
    }
    mdContent += `\n`;
  }
  
  if (slide.keyTerms && slide.keyTerms.length > 0) {
    mdContent += `### 📚 Key Terms (주요 용어)\n`;
    slide.keyTerms.forEach(kt => {
      mdContent += `- **${kt.term}**: ${kt.def} (${kt.defKo})\n`;
    });
    mdContent += `\n`;
  }
  
  mdContent += `---\n\n`;
});

const outputMdPath = path.join(__dirname, 'session01.md');
fs.writeFileSync(outputMdPath, mdContent, 'utf8');

// Also write copy to files directory
const outputFilesMdPath = path.join(__dirname, 'files', 'session01.md');
fs.writeFileSync(outputFilesMdPath, mdContent, 'utf8');

console.log(`✅ Generated session01.md successfully!`);
console.log(`Path 1: ${outputMdPath}`);
console.log(`Path 2: ${outputFilesMdPath}`);
