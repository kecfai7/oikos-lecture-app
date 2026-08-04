import React from 'react';
import { 
  BookOpen, 
  ChevronLeft, 
  ChevronRight, 
  Grid, 
  Monitor, 
  Maximize, 
  RotateCcw,
  Sparkles
} from 'lucide-react';
import { SESSIONS } from '../data/slidesData';

export default function Header({ 
  currentSlide, 
  totalSlides, 
  onPrev, 
  onNext, 
  onTogglePresenter, 
  isPresenterOpen,
  onToggleOverview,
  selectedSession,
  onSelectSession
}) {
  const toggleFullScreen = () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => console.log(err));
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      }
    }
  };

  return (
    <header className="h-16 bg-[#0B132B]/90 backdrop-blur-md border-b border-cyan-500/20 px-4 flex items-center justify-between z-30 sticky top-0">
      {/* Brand & Logo */}
      <div className="flex items-center gap-3">
        <div className="w-9 h-9 rounded-lg bg-gradient-to-br from-cyan-400 to-blue-600 flex items-center justify-center shadow-lg shadow-cyan-500/30">
          <Sparkles className="w-5 h-5 text-white animate-pulse" />
        </div>
        <div>
          <div className="flex items-center gap-2">
            <span className="font-bold text-white tracking-wide text-sm">OIKOS UNIVERSITY</span>
            <span className="text-[10px] px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 font-semibold border border-amber-500/30">
              SOLI DEO GLORIA
            </span>
          </div>
          <p className="text-[11px] text-cyan-400 font-medium">Smart Insight Lab • Prof. Peter Kim</p>
        </div>
      </div>

      {/* Session Selector & Progress */}
      <div className="hidden md:flex items-center gap-4">
        <select 
          value={selectedSession} 
          onChange={(e) => onSelectSession(Number(e.target.value))}
          className="bg-slate-800/80 border border-cyan-500/30 text-xs text-white rounded-lg px-3 py-1.5 focus:outline-none focus:border-cyan-400 transition"
        >
          {SESSIONS.map(s => (
            <option key={s.id} value={s.id} disabled={!s.active}>
              {s.title} {!s.active ? "(Upcoming)" : ""}
            </option>
          ))}
        </select>

        {/* Counter Badge */}
        <div className="px-3 py-1 rounded-full bg-slate-800 border border-slate-700 text-xs font-semibold text-cyan-400 flex items-center gap-1.5">
          <span>Slide</span>
          <span className="text-white font-bold">{currentSlide}</span>
          <span className="text-slate-500">/</span>
          <span className="text-slate-400">{totalSlides}</span>
        </div>
      </div>

      {/* Action Controls */}
      <div className="flex items-center gap-2">
        {/* Navigation Buttons */}
        <button 
          onClick={onPrev} 
          disabled={currentSlide === 1}
          className="p-2 rounded-lg bg-slate-800/80 hover:bg-cyan-500/20 text-white disabled:opacity-30 disabled:hover:bg-slate-800 transition border border-slate-700"
          title="Previous Slide (Left Arrow)"
        >
          <ChevronLeft className="w-4 h-4" />
        </button>

        <button 
          onClick={onNext} 
          disabled={currentSlide === totalSlides}
          className="p-2 rounded-lg bg-slate-800/80 hover:bg-cyan-500/20 text-white disabled:opacity-30 disabled:hover:bg-slate-800 transition border border-slate-700"
          title="Next Slide (Right Arrow)"
        >
          <ChevronRight className="w-4 h-4" />
        </button>

        <div className="h-5 w-px bg-slate-800 mx-1" />

        {/* Grid Overview */}
        <button 
          onClick={onToggleOverview}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-white border border-slate-700 transition"
          title="View All Slides [M]"
        >
          <Grid className="w-3.5 h-3.5 text-cyan-400" />
          <span className="hidden sm:inline">Overview</span>
        </button>

        {/* Presenter Teleprompter Mode Toggle */}
        <button 
          onClick={onTogglePresenter}
          className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold border transition ${
            isPresenterOpen 
              ? "bg-cyan-500 text-slate-950 border-cyan-400 shadow-lg shadow-cyan-500/30" 
              : "bg-slate-800 hover:bg-cyan-500/20 text-cyan-400 border-cyan-500/30"
          }`}
          title="Toggle Presenter Teleprompter View [P]"
        >
          <Monitor className="w-3.5 h-3.5" />
          <span>Presenter Mode [P]</span>
        </button>

        {/* Fullscreen Toggle */}
        <button 
          onClick={toggleFullScreen}
          className="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition border border-slate-700"
          title="Toggle Fullscreen [F]"
        >
          <Maximize className="w-4 h-4" />
        </button>
      </div>
    </header>
  );
}
