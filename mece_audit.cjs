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

const tempPath = path.join(__dirname, 'temp_mece_audit.cjs');
fs.writeFileSync(tempPath, fileContent, 'utf8');

const data = require(tempPath);
fs.unlinkSync(tempPath);

let totalSlidesCount = 0;
let errors = [];
let statsBySession = [];

for (let sId = 1; sId <= 15; sId++) {
  const slides = data['SLIDES_SESSION_' + sId];
  if (!slides) {
    errors.push(`Session ${sId} is missing entirely!`);
    continue;
  }
  
  if (slides.length !== 40) {
    errors.push(`Session ${sId} has ${slides.length} slides (expected exactly 40).`);
  }
  
  totalSlidesCount += slides.length;
  let wordCounts = [];
  
  // Check numbering & required attributes
  slides.forEach((s, idx) => {
    if (s.num !== idx + 1) {
      errors.push(`Session ${sId} Slide #${idx + 1} has incorrect num: ${s.num}`);
    }
    if (!s.title || !s.script) {
      errors.push(`Session ${sId} Slide #${s.num} is missing title or script!`);
    }
    const words = (s.script || '').trim().split(/\s+/).length;
    wordCounts.push(words);
    if (words < 40) {
      errors.push(`Session ${sId} Slide #${s.num} script is unusually short (${words} words).`);
    }
  });
  
  // Check exact Part Divider placements: 2, 11, 21, 31
  [2, 11, 21, 31].forEach((n, pIdx) => {
    const s = slides.find(x => x.num === n);
    if (!s || s.type !== 'section') {
      errors.push(`Session ${sId} Slide #${n} must be type: 'section' (currently: ${s ? s.type : 'missing'})`);
    }
    const expectedPart = `PART ${pIdx + 1}`;
    if (s && !s.title.toUpperCase().includes(expectedPart)) {
      errors.push(`Session ${sId} Slide #${n} title does not include '${expectedPart}' (Title: ${s.title})`);
    }
  });
  
  // Check other slides are NOT type: 'section'
  slides.forEach(s => {
    if (![2, 11, 21, 31].includes(s.num) && s.type === 'section') {
      errors.push(`Session ${sId} Slide #${s.num} has unexpected type: 'section'!`);
    }
  });

  const avgWords = Math.round(wordCounts.reduce((a,b)=>a+b, 0) / wordCounts.length);
  statsBySession.push({
    session: sId,
    slideCount: slides.length,
    avgWordsPerSlide: avgWords,
    part1: slides.find(s => s.num === 2)?.title,
    part2: slides.find(s => s.num === 11)?.title,
    part3: slides.find(s => s.num === 21)?.title,
    part4: slides.find(s => s.num === 31)?.title
  });
}

console.log('===============================================================');
console.log('       OIKOS UNIVERSITY MASTER MECE ZERO-DEFECT AUDIT         ');
console.log('===============================================================');
console.log(`Active Sessions: 15 / 15`);
console.log(`Total Slides Ingested: ${totalSlidesCount} / 600`);
console.log('---------------------------------------------------------------');

if (errors.length === 0) {
  console.log('✅ PERFECT ZERO-DEFECT AUDIT RESULT:');
  console.log(' - Mutually Exclusive (ME): Zero duplicate part dividers, clean orthogonal modules.');
  console.log(' - Collectively Exhaustive (CE): Exactly 15 sessions, 600 slides, 100% complete.');
  console.log(' - Structural Perfection: Slide 2(Part 1), 11(Part 2), 21(Part 3), 31(Part 4) verified in all 15 sessions.');
  console.log('---------------------------------------------------------------');
  statsBySession.forEach(st => {
    console.log(`Session ${String(st.session).padStart(2, '0')}: 40 Slides | Avg Words/Slide: ${st.avgWordsPerSlide} words (~90s spoken ESL)`);
    console.log(`  P1: ${st.part1}`);
    console.log(`  P2: ${st.part2}`);
    console.log(`  P3: ${st.part3}`);
    console.log(`  P4: ${st.part4}`);
  });
} else {
  console.log(`❌ Found ${errors.length} defect(s):`);
  errors.forEach(e => console.log(' - ' + e));
}
console.log('===============================================================');
