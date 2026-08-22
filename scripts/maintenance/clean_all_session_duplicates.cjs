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

const tempPath = path.join(__dirname, 'temp_clean_data.cjs');
fs.writeFileSync(tempPath, fileContent, 'utf8');

const allData = require(tempPath);
fs.unlinkSync(tempPath);

// In Session 3: Rename Section -> Part in summaries
allData.SLIDES_SESSION_3.forEach(s => {
  if (s.title.includes('SECTION 1')) s.title = s.title.replace('SECTION 1', 'PART 1');
  if (s.title.includes('SECTION 2')) s.title = s.title.replace('SECTION 2', 'PART 2');
  if (s.title.includes('SECTION 3')) s.title = s.title.replace('SECTION 3', 'PART 3');
});

// In Session 6: Rename Section -> Part in transitions
allData.SLIDES_SESSION_6.forEach(s => {
  if (s.title.includes('SECTION 1')) s.title = s.title.replace('SECTION 1', 'PART 1');
  if (s.title.includes('SECTION 2')) s.title = s.title.replace('SECTION 2', 'PART 2');
  if (s.title.includes('SECTION 3')) s.title = s.title.replace('SECTION 3', 'PART 3');
});

// In Session 7: Slide 7, 16 were duplicate section slides
const s7_7 = allData.SLIDES_SESSION_7.find(s => s.num === 7);
if (s7_7 && s7_7.type === 'section') {
  s7_7.type = 'comparison';
  s7_7.title = 'THE WEB MATRIX: HUMAN BROWSING VS. AGENTIC EXTRACTION';
  s7_7.subtitle = 'Analyzing the 95% bandwidth waste of visual web crawling vs. direct API extraction';
}

const s7_16 = allData.SLIDES_SESSION_7.find(s => s.num === 16);
if (s7_16 && s7_16.type === 'section') {
  s7_16.type = 'triad';
  s7_16.title = 'AGENTIC DISCOVERY: DEPLOYING LLMS.TXT AT SCALE';
  s7_16.subtitle = 'How enterprise domains publish machine-readable sitemaps for autonomous agents';
}

// In Session 8: Slide 7, 17, 26 were duplicate section slides
const s8_7 = allData.SLIDES_SESSION_8.find(s => s.num === 7);
if (s8_7 && s8_7.type === 'section') {
  s8_7.type = 'comparison';
  s8_7.title = 'THE COMMERCE PARADIGM: MANUAL CHECKOUT VS. UCP AGENTS';
  s8_7.subtitle = 'Eliminating 3-4 weekly hours of shopping friction and repetitive form-filling';
}

const s8_17 = allData.SLIDES_SESSION_8.find(s => s.num === 17);
if (s8_17 && s8_17.type === 'section') {
  s8_17.type = 'triad';
  s8_17.title = 'AGENT FINANCIAL AUTONOMY: WALLET CEILINGS & PERMISSIONS';
  s8_17.subtitle = 'Establishing deterministic financial guardrails before issuing autonomous purchasing rights';
}

const s8_26 = allData.SLIDES_SESSION_8.find(s => s.num === 26);
if (s8_26 && s8_26.type === 'section') {
  s8_26.type = 'architecture';
  s8_26.title = 'AGENTIC COMMERCE ROADMAP: THE 3-STEP INTEGRATION FLYWHEEL';
  s8_26.subtitle = 'How progressive enterprises deploy UCP endpoints to capture machine-driven revenue';
}

// In Session 12: Slide 10, 20, 30 were duplicate section slides
const s12_10 = allData.SLIDES_SESSION_12.find(s => s.num === 10);
if (s12_10 && s12_10.type === 'section') {
  s12_10.type = 'triad';
  s12_10.title = 'SPATIO-TEMPORAL TOKENIZER: 3D VOLUME CONSISTENCY';
  s12_10.subtitle = 'Preserving continuous physical geometry across millions of simulated video frames';
}

const s12_20 = allData.SLIDES_SESSION_12.find(s => s.num === 20);
if (s12_20 && s12_20.type === 'section') {
  s12_20.type = 'comparison';
  s12_20.title = 'REAL-WORLD TESTING RISKS VS. SIMULATED CLUSTER SAFETY';
  s12_20.subtitle = 'Eliminating physical collision hazards by training 10,000 agents in Genie 3 clusters';
}

const s12_30 = allData.SLIDES_SESSION_12.find(s => s.num === 30);
if (s12_30 && s12_30.type === 'section') {
  s12_30.type = 'triad';
  s12_30.title = 'DATA PRIVACY SANDBOXES: SECURING PROPRIETARY TOPOGRAPHY';
  s12_30.subtitle = 'Guaranteed enterprise data isolation and cryptographic anti-training seals';
}

// Write back
let newFileContent = '// Session 1 to 15 Master Slide Data (40 Slides per session, 600 Slides total)\n';
newFileContent += '// Designed for 60-minute English lectures with easy-to-read ESL scripts and Korean teaching guides\n\n';
newFileContent += 'export const SESSIONS = ' + JSON.stringify(allData.SESSIONS, null, 2) + ';\n\n';

for (let i = 1; i <= 15; i++) {
  newFileContent += `export const SLIDES_SESSION_${i} = ` + JSON.stringify(allData['SLIDES_SESSION_' + i], null, 2) + ';\n\n';
}

fs.writeFileSync(slidesDataPath, newFileContent, 'utf8');
console.log('Successfully cleaned all section/part duplicates across all 15 sessions in slidesData.js!');
