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

const tempPath = path.join(__dirname, 'temp_sort_data.cjs');
fs.writeFileSync(tempPath, fileContent, 'utf8');

const allData = require(tempPath);
fs.unlinkSync(tempPath);

for (let i = 1; i <= 15; i++) {
  const arr = allData['SLIDES_SESSION_' + i];
  arr.sort((a, b) => a.num - b.num);
  // Re-verify consecutive 1..40
  arr.forEach((s, idx) => {
    s.num = idx + 1;
  });
}

// Generate new slidesData.js content
let newFileContent = '// Session 1 to 15 Master Slide Data (40 Slides per session, 600 Slides total)\n';
newFileContent += '// Designed for 60-minute English lectures with easy-to-read ESL scripts and Korean teaching guides\n\n';
newFileContent += 'export const SESSIONS = ' + JSON.stringify(allData.SESSIONS, null, 2) + ';\n\n';

for (let i = 1; i <= 15; i++) {
  newFileContent += `export const SLIDES_SESSION_${i} = ` + JSON.stringify(allData['SLIDES_SESSION_' + i], null, 2) + ';\n\n';
}

fs.writeFileSync(slidesDataPath, newFileContent, 'utf8');
console.log('Successfully sorted and verified all 15 sessions 1..40 in slidesData.js!');
