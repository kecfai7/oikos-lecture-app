import React, { useState, useEffect } from 'react';
import { 
  X, 
  Play, 
  Pause, 
  RotateCcw, 
  ChevronLeft, 
  ChevronRight, 
  BookOpen, 
  Clock, 
  Sparkles,
  Volume2
} from 'lucide-react';

export default function PresenterMode({ 
  slideData, 
  nextSlideData,
  currentSlide, 
  totalSlides, 
  onPrev, 
  onNext, 
  onClose 
}) {
  // Timer State
  const [seconds, setSeconds] = useState(0);
  const [isActive, setIsActive] = useState(true);

  useEffect(() => {
    let interval = null;
    if (isActive) {
      interval = setInterval(() => {
        setSeconds(s => s + 1);
      }, 1000);
    } else if (!isActive && seconds !== 0) {
      clearInterval(interval);
    }
    return () => clearInterval(interval);
  }, [isActive, seconds]);

  const formatTime = (totalSeconds) => {
    const mins = Math.floor(totalSeconds / 60);
    const secs = totalSeconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const handleResetTimer = () => {
    setSeconds(0);
    setIsActive(false);
  };

  return (
    <div className="fixed inset-y-0 right-0 w-full md:w-[480px] bg-slate-950/95 border-l border-cyan-500/30 backdrop-blur-xl shadow-2xl z-50 flex flex-col justify-between overflow-hidden">
      {/* Presenter Header */}
      <div className="p-4 bg-slate-900/90 border-b border-slate-800 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="w-2.5 h-2.5 rounded-full bg-cyan-400 animate-ping" />
          <h2 className="text-sm font-bold text-white tracking-wide">PRESENTER TELEPROMPTER</h2>
        </div>
        
        {/* Timer Control */}
        <div className="flex items-center gap-2 bg-slate-800/80 px-3 py-1 rounded-full border border-slate-700">
          <Clock className="w-3.5 h-3.5 text-cyan-400" />
          <span className="font-mono text-xs font-bold text-amber-300">{formatTime(seconds)}</span>
          <button 
            onClick={() => setIsActive(!isActive)}
            className="text-slate-400 hover:text-white transition"
          >
            {isActive ? <Pause className="w-3 h-3" /> : <Play className="w-3 h-3" />}
          </button>
          <button 
            onClick={handleResetTimer}
            className="text-slate-400 hover:text-white transition"
          >
            <RotateCcw className="w-3 h-3" />
          </button>
        </div>

        <button 
          onClick={onClose}
          className="p-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white transition"
        >
          <X className="w-4 h-4" />
        </button>
      </div>

      {/* Main Content Area */}
      <div className="flex-1 overflow-y-auto p-5 space-y-6">
        {/* Current Slide Info */}
        <div className="flex items-center justify-between bg-slate-900/60 p-3 rounded-xl border border-slate-800">
          <div>
            <span className="text-[10px] font-bold text-cyan-400 uppercase tracking-widest">
              CURRENT SLIDE {currentSlide} / {totalSlides}
            </span>
            <h3 className="text-sm font-bold text-white truncate max-w-[280px]">
              {slideData?.title}
            </h3>
          </div>
          <div className="flex items-center gap-1">
            <button 
              onClick={onPrev} 
              disabled={currentSlide === 1}
              className="p-1.5 rounded bg-slate-800 hover:bg-cyan-500/20 text-white disabled:opacity-30"
            >
              <ChevronLeft className="w-4 h-4" />
            </button>
            <button 
              onClick={onNext} 
              disabled={currentSlide === totalSlides}
              className="p-1.5 rounded bg-slate-800 hover:bg-cyan-500/20 text-white disabled:opacity-30"
            >
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Professor's Spoken Script */}
        <div className="space-y-2">
          <div className="flex items-center gap-2 text-cyan-300 text-xs font-bold uppercase tracking-wider">
            <Volume2 className="w-4 h-4 text-cyan-400" />
            <span>Professor's Spoken Script (ESL Friendly)</span>
          </div>
          
          <div className="p-4 rounded-xl bg-slate-900/80 border border-cyan-500/30 text-white text-base leading-relaxed font-normal shadow-inner space-y-3">
            <p className="text-cyan-100 font-medium">
              "{slideData?.script}"
            </p>
          </div>
        </div>

        {/* Key Vocabulary Terms */}
        {slideData?.keyTerms && slideData.keyTerms.length > 0 && (
          <div className="space-y-2">
            <div className="flex items-center gap-2 text-amber-300 text-xs font-bold uppercase tracking-wider">
              <BookOpen className="w-4 h-4 text-amber-400" />
              <span>Key Terms (Vocabulary Definitions)</span>
            </div>
            
            <div className="grid gap-2">
              {slideData.keyTerms.map((kt, idx) => (
                <div key={idx} className="p-3 rounded-lg bg-amber-500/10 border border-amber-500/20">
                  <span className="font-bold text-amber-300 text-xs block">{kt.term}</span>
                  <span className="text-slate-300 text-xs mt-0.5 block">{kt.def}</span>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Next Slide Preview */}
        {nextSlideData && (
          <div className="pt-2 border-t border-slate-800 space-y-1.5">
            <span className="text-[11px] font-bold text-slate-500 uppercase tracking-wider block">
              NEXT SLIDE PREVIEW ({nextSlideData.num})
            </span>
            <div className="p-3 rounded-lg bg-slate-900/40 border border-slate-800 opacity-70">
              <p className="text-xs font-bold text-slate-300">{nextSlideData.title}</p>
              <p className="text-[11px] text-slate-400 truncate mt-0.5">{nextSlideData.subtitle}</p>
            </div>
          </div>
        )}
      </div>

      {/* Footer Navigation Bar */}
      <div className="p-4 bg-slate-900 border-t border-slate-800 flex items-center justify-between">
        <button 
          onClick={onPrev}
          disabled={currentSlide === 1}
          className="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-white text-xs font-medium disabled:opacity-30 transition flex items-center gap-1"
        >
          <ChevronLeft className="w-4 h-4" />
          <span>Previous</span>
        </button>

        <span className="text-xs font-mono text-slate-400">
          Slide {currentSlide} of {totalSlides}
        </span>

        <button 
          onClick={onNext}
          disabled={currentSlide === totalSlides}
          className="px-4 py-2 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-slate-950 text-xs font-bold disabled:opacity-30 transition flex items-center gap-1 shadow-lg shadow-cyan-500/20"
        >
          <span>Next</span>
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
}
