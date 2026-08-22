import React, { useState, useMemo } from 'react';
import { motion } from 'framer-motion';
import { 
  X, 
  Search, 
  BookOpen, 
  Target, 
  Layers, 
  FlaskConical, 
  ArrowRight, 
  Sparkles, 
  CheckCircle2, 
  Compass,
  ChevronDown,
  ChevronUp
} from 'lucide-react';
import { COURSE_INFO, SESSIONS_CURRICULUM } from '../data/courseCurriculum';

export default function CurriculumModal({ isOpen, onClose, onSelectSession, currentSessionId }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [expandedSession, setExpandedSession] = useState(currentSessionId || 1);

  // Sync expandedSession when modal opens or currentSessionId changes
  React.useEffect(() => {
    if (isOpen) {
      setExpandedSession(currentSessionId || 1);
    }
  }, [isOpen, currentSessionId]);

  // ESC key to close
  React.useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape' && isOpen) {
        onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  // Filter sessions by search term
  const filteredSessions = useMemo(() => {
    if (!searchTerm.trim()) return SESSIONS_CURRICULUM;
    const term = searchTerm.toLowerCase();
    return SESSIONS_CURRICULUM.filter(sess => {
      const matchTitle = sess.title.toLowerCase().includes(term);
      const matchTheme = (sess.theme || '').toLowerCase().includes(term);
      const matchObjectives = (sess.learningObjectives || []).some(o => o.toLowerCase().includes(term));
      const matchParts = (sess.parts || []).some(p => 
        p.title.toLowerCase().includes(term) ||
        p.summary.toLowerCase().includes(term) ||
        (p.keyTopics || []).some(k => k.toLowerCase().includes(term))
      );
      const matchLab = (sess.labMission || '').toLowerCase().includes(term);
      return matchTitle || matchTheme || matchObjectives || matchParts || matchLab;
    });
  }, [searchTerm]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 overflow-hidden">
      {/* Backdrop */}
      <motion.div 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        onClick={onClose}
        className="absolute inset-0 bg-slate-950/85 backdrop-blur-md"
      />

      {/* Modal Container */}
      <motion.div 
        initial={{ opacity: 0, scale: 0.95, y: 20 }}
        animate={{ opacity: 1, scale: 1, y: 0 }}
        exit={{ opacity: 0, scale: 0.95, y: 20 }}
        transition={{ duration: 0.2 }}
        className="relative w-full max-w-6xl max-h-[92vh] bg-[#0c1427]/95 border border-cyan-500/30 rounded-2xl shadow-2xl shadow-cyan-500/20 flex flex-col overflow-hidden z-10"
      >
        {/* Header */}
        <div className="p-6 border-b border-slate-800/80 bg-slate-900/60 flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div className="flex items-start gap-3.5">
            <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-cyan-400 to-blue-600 flex items-center justify-center shadow-lg shadow-cyan-500/30 shrink-0">
              <BookOpen className="w-6 h-6 text-white" />
            </div>
            <div>
              <div className="flex items-center gap-2 flex-wrap">
                <span className="text-xs font-mono font-bold text-amber-400 uppercase tracking-wider px-2 py-0.5 rounded bg-amber-500/10 border border-amber-500/30">
                  {COURSE_INFO.motto}
                </span>
                <span className="text-xs text-cyan-300 font-semibold">
                  {COURSE_INFO.institution} • {COURSE_INFO.totalSessions} Sessions (600 Slides)
                </span>
              </div>
              <h2 className="text-xl sm:text-2xl font-black text-white tracking-wide mt-1">
                {COURSE_INFO.courseTitle}
              </h2>
              <p className="text-xs text-slate-400 font-mono">
                {COURSE_INFO.department} • {COURSE_INFO.instructor}
              </p>
            </div>
          </div>

          {/* Controls: Search & Close */}
          <div className="flex items-center gap-3 w-full md:w-auto">
            <div className="relative flex-1 md:w-64">
              <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
              <input 
                type="text"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                placeholder="Search topics (e.g., RAG, WebMCP, AP2, Genie 3...)"
                className="w-full bg-slate-800/80 border border-slate-700 text-white placeholder-slate-500 text-xs rounded-xl pl-9 pr-3 py-2 focus:outline-none focus:border-cyan-400 transition"
              />
              {searchTerm && (
                <button 
                  onClick={() => setSearchTerm('')}
                  className="absolute right-2.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white"
                >
                  <X className="w-3.5 h-3.5" />
                </button>
              )}
            </div>

            <button 
              onClick={onClose}
              className="p-2 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700 transition"
              title="Close [ESC]"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Quick Session Jump Pill Bar */}
        <div className="px-6 py-2.5 bg-slate-950/60 border-b border-slate-800/80 overflow-x-auto flex items-center gap-1.5 scrollbar-thin">
          <span className="text-[11px] font-mono text-slate-400 font-semibold shrink-0 mr-1.5 flex items-center gap-1">
            <Compass className="w-3 h-3 text-cyan-400" />
            JUMP TO:
          </span>
          {SESSIONS_CURRICULUM.map(s => {
            const isSelected = expandedSession === s.sessionNum;
            const isCurrent = currentSessionId === s.sessionNum;
            return (
              <button
                key={s.sessionNum}
                onClick={() => setExpandedSession(s.sessionNum)}
                className={`px-2.5 py-1 rounded-lg text-xs font-mono font-bold transition shrink-0 ${
                  isSelected 
                    ? 'bg-cyan-500 text-slate-950 shadow-md shadow-cyan-500/30' 
                    : isCurrent
                      ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40 hover:bg-amber-500/30'
                      : 'bg-slate-800/80 text-slate-300 hover:bg-slate-700 border border-slate-700/60'
                }`}
              >
                Session {s.sessionNum} {isCurrent ? '★' : ''}
              </button>
            );
          })}
        </div>

        {/* Scrollable Curriculum Content */}
        <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-4">
          {filteredSessions.length === 0 ? (
            <div className="text-center py-16">
              <Search className="w-12 h-12 text-slate-600 mx-auto mb-3" />
              <p className="text-slate-400 text-sm font-medium">No results found matching: "{searchTerm}"</p>
              <button 
                onClick={() => setSearchTerm('')}
                className="mt-3 px-4 py-1.5 text-xs text-cyan-400 bg-cyan-500/10 border border-cyan-500/30 rounded-lg hover:bg-cyan-500/20 transition"
              >
                Clear Search
              </button>
            </div>
          ) : (
            filteredSessions.map((session) => {
              const isExpanded = expandedSession === session.sessionNum || searchTerm.trim().length > 0;
              const isCurrent = currentSessionId === session.sessionNum;

              return (
                <div 
                  key={session.sessionNum}
                  className={`rounded-2xl border transition overflow-hidden ${
                    isCurrent 
                      ? 'bg-slate-900/90 border-cyan-500/60 shadow-lg shadow-cyan-500/10' 
                      : 'bg-slate-900/60 border-slate-800/80 hover:border-slate-700'
                  }`}
                >
                  {/* Session Header Card Bar */}
                  <div 
                    onClick={() => setExpandedSession(isExpanded && !searchTerm ? null : session.sessionNum)}
                    className="p-4 sm:p-5 flex flex-col md:flex-row md:items-center justify-between gap-3 cursor-pointer hover:bg-slate-800/40 transition"
                  >
                    <div className="flex items-start gap-3.5">
                      <div className={`w-10 h-10 rounded-xl flex items-center justify-center font-black text-sm shrink-0 shadow-md ${
                        isCurrent 
                          ? 'bg-gradient-to-br from-cyan-400 to-blue-600 text-slate-950 font-black ring-2 ring-cyan-400' 
                          : 'bg-slate-800 text-cyan-300 border border-cyan-500/30'
                      }`}>
                        {String(session.sessionNum).padStart(2, '0')}
                      </div>

                      <div>
                        <div className="flex items-center gap-2 flex-wrap">
                          <span className="text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-cyan-500/10 text-cyan-300 border border-cyan-500/30">
                            SESSION {session.sessionNum} • 40 SLIDES
                          </span>
                          {isCurrent && (
                            <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 animate-pulse">
                              NOW VIEWING
                            </span>
                          )}
                          <span className="text-xs text-slate-400 font-mono">
                            {session.theme}
                          </span>
                        </div>
                        <h3 className="text-base sm:text-lg font-bold text-white mt-1">
                          {session.title}
                        </h3>
                      </div>
                    </div>

                    {/* Right side: Action Button & Expand Toggle */}
                    <div className="flex items-center gap-2 self-end md:self-center shrink-0">
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          onSelectSession(session.sessionNum);
                          onClose();
                        }}
                        className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 text-xs font-bold transition shadow-md shadow-cyan-500/30"
                      >
                        <span>Open Session</span>
                        <ArrowRight className="w-3.5 h-3.5" />
                      </button>

                      <div className="p-1 text-slate-400 hover:text-white">
                        {isExpanded ? <ChevronUp className="w-5 h-5" /> : <ChevronDown className="w-5 h-5" />}
                      </div>
                    </div>
                  </div>

                  {/* Expanded Body: Objectives, 4 Parts, Lab */}
                  {isExpanded && (
                    <div className="p-4 sm:p-6 border-t border-slate-800/80 bg-slate-950/40 space-y-6">
                      {/* 1. Core Learning Objectives */}
                      <div className="bg-slate-900/80 border border-cyan-500/20 rounded-xl p-4 sm:p-5">
                        <div className="flex items-center gap-2 mb-3">
                          <Target className="w-4 h-4 text-cyan-400" />
                          <h4 className="text-xs font-mono font-bold text-cyan-300 uppercase tracking-wider">
                            CORE LEARNING OBJECTIVES
                          </h4>
                        </div>
                        <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                          {session.learningObjectives.map((obj, idx) => (
                            <div key={idx} className="flex items-start gap-2.5 bg-slate-950/60 p-3 rounded-lg border border-slate-800">
                              <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                              <p className="text-xs font-medium text-slate-200 leading-relaxed">
                                {obj}
                              </p>
                            </div>
                          ))}
                        </div>
                      </div>

                      {/* 2. Four-Part Structural Roadmap */}
                      <div>
                        <div className="flex items-center gap-2 mb-3">
                          <Layers className="w-4 h-4 text-amber-400" />
                          <h4 className="text-xs font-mono font-bold text-amber-300 uppercase tracking-wider">
                            4-PART ARCHITECTURE & SLIDE ROADMAP
                          </h4>
                        </div>

                        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
                          {session.parts.map((part) => (
                            <div 
                              key={part.partNum}
                              className="bg-slate-900/80 border border-slate-800 hover:border-cyan-500/40 rounded-xl p-4 flex flex-col justify-between transition group"
                            >
                              <div>
                                <div className="flex items-center justify-between gap-1.5 mb-2">
                                  <span className="text-[10px] font-mono font-black px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">
                                    PART {part.partNum}
                                  </span>
                                  <span className="text-[10px] font-mono text-slate-400 font-semibold">
                                    {part.slideRange}
                                  </span>
                                </div>

                                <h5 className="text-xs font-bold text-white group-hover:text-cyan-200 transition leading-snug">
                                  {part.title.replace(`PART ${part.partNum}: `, '')}
                                </h5>

                                <p className="text-xs text-slate-300 leading-relaxed mt-2 font-sans">
                                  {part.summary}
                                </p>
                              </div>

                              {/* Key Topics Badges */}
                              {part.keyTopics && part.keyTopics.length > 0 && (
                                <div className="pt-3 mt-3 border-t border-slate-800/80 flex flex-wrap gap-1">
                                  {part.keyTopics.map((kt, kIdx) => (
                                    <span 
                                      key={kIdx} 
                                      className="text-[10px] px-1.5 py-0.5 rounded bg-slate-800/80 text-slate-400 border border-slate-700/60 font-mono"
                                    >
                                      #{kt}
                                    </span>
                                  ))}
                                </div>
                              )}
                            </div>
                          ))}
                        </div>
                      </div>

                      {/* 3. Hands-on Lab & Capstone */}
                      <div className="bg-amber-500/10 border border-amber-500/30 rounded-xl p-3.5 flex items-start gap-3">
                        <div className="w-8 h-8 rounded-lg bg-amber-500/20 border border-amber-500/40 flex items-center justify-center shrink-0 text-amber-300">
                          <FlaskConical className="w-4 h-4" />
                        </div>
                        <div>
                          <span className="text-[10px] font-mono font-bold text-amber-300 uppercase tracking-widest block">
                            HANDS-ON LAB / CAPSTONE MISSION
                          </span>
                          <p className="text-xs font-semibold text-white mt-0.5">
                            {session.labMission}
                          </p>
                        </div>
                      </div>
                    </div>
                  )}
                </div>
              );
            })
          )}
        </div>

        {/* Footer */}
        <div className="p-4 border-t border-slate-800/80 bg-slate-950/80 flex items-center justify-between text-xs text-slate-400">
          <div className="flex items-center gap-2">
            <Sparkles className="w-3.5 h-3.5 text-cyan-400" />
            <span>Oikos University Smart Insight Lab • 15 Sessions Full Curriculum</span>
          </div>
          <button 
            onClick={onClose}
            className="px-4 py-1.5 bg-slate-800 hover:bg-slate-700 text-white rounded-lg transition"
          >
            Close
          </button>
        </div>
      </motion.div>
    </div>
  );
}
