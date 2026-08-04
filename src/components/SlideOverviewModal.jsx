import React from 'react';
import { X, Check } from 'lucide-react';

export default function SlideOverviewModal({ slides, currentSlide, onSelectSlide, onClose }) {
  return (
    <div className="fixed inset-0 bg-slate-950/90 backdrop-blur-xl z-50 p-6 flex flex-col justify-between overflow-hidden">
      {/* Header */}
      <div className="flex items-center justify-between pb-4 border-b border-slate-800">
        <div>
          <h2 className="text-xl font-bold text-white tracking-wide">40-SLIDE OVERVIEW GRID</h2>
          <p className="text-xs text-cyan-400">Select any slide to jump directly</p>
        </div>
        <button 
          onClick={onClose}
          className="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition"
        >
          <X className="w-5 h-5" />
        </button>
      </div>

      {/* Grid List */}
      <div className="flex-1 overflow-y-auto my-4 grid grid-cols-2 sm:grid-cols-4 md:grid-cols-5 lg:grid-cols-8 gap-3 pr-2">
        {slides.map((s) => {
          const isActive = s.num === currentSlide;
          return (
            <button
              key={s.num}
              onClick={() => {
                onSelectSlide(s.num);
                onClose();
              }}
              className={`p-3 rounded-xl border text-left flex flex-col justify-between transition h-28 relative overflow-hidden group ${
                isActive
                  ? "bg-cyan-500/20 border-cyan-400 shadow-lg shadow-cyan-500/30"
                  : "bg-slate-900/80 border-slate-800 hover:border-slate-600 hover:bg-slate-800"
              }`}
            >
              <div className="flex items-center justify-between w-full">
                <span className={`text-[10px] font-bold px-1.5 py-0.5 rounded ${
                  isActive ? "bg-cyan-400 text-slate-950" : "bg-slate-800 text-slate-400"
                }`}>
                  #{s.num}
                </span>
                {isActive && <Check className="w-3.5 h-3.5 text-cyan-400" />}
              </div>

              <div>
                <p className="text-[11px] font-bold text-white line-clamp-2 leading-tight">
                  {s.title}
                </p>
                <p className="text-[9px] text-slate-400 truncate mt-1">
                  {s.type.toUpperCase()}
                </p>
              </div>
            </button>
          );
        })}
      </div>

      {/* Footer */}
      <div className="pt-3 border-t border-slate-800 flex justify-end">
        <button
          onClick={onClose}
          className="px-5 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-white text-xs font-semibold"
        >
          Close Overview
        </button>
      </div>
    </div>
  );
}
