import React from 'react';
import { motion } from 'framer-motion';
import { Layers, ArrowRight } from 'lucide-react';

export default function SectionSlide({ slideData }) {
  return (
    <div className="h-full flex items-center justify-center p-8 relative overflow-hidden">
      {/* Background Glowing Grid */}
      <div className="absolute inset-0 bg-[radial-gradient(#00e5ff_1px,transparent_1px)] [background-size:32px_32px] opacity-10" />

      <motion.div 
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        className="w-full max-w-3xl glass-card p-10 md:p-14 text-center space-y-6 relative z-10 border-2 border-cyan-500/40 shadow-2xl shadow-cyan-500/20"
      >
        <div className="w-16 h-16 rounded-2xl bg-cyan-500/20 border border-cyan-400 mx-auto flex items-center justify-center shadow-lg shadow-cyan-500/30">
          <Layers className="w-8 h-8 text-cyan-300 animate-pulse" />
        </div>

        <div>
          <span className="text-xs font-mono font-bold text-amber-400 uppercase tracking-widest block mb-2">
            CHAPTER DIVIDER
          </span>
          <h2 className="text-3xl md:text-5xl font-black text-white tracking-wide">
            {slideData.title}
          </h2>
        </div>

        <p className="text-lg md:text-xl text-cyan-200 font-medium max-w-xl mx-auto leading-relaxed">
          {slideData.subtitle}
        </p>

        <div className="pt-4 flex justify-center">
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-xs font-semibold text-cyan-300">
            <span>Entering Next Phase</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </div>
        </div>
      </motion.div>
    </div>
  );
}
