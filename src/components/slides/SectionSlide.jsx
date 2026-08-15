import React from 'react';
import { motion } from 'framer-motion';
import { Layers, ArrowRight } from 'lucide-react';

export default function SectionSlide({ slideData }) {
  return (
    <div className="h-full flex items-center justify-center p-8 md:p-14 relative overflow-hidden">
      {/* Background Glowing Grid */}
      <div className="absolute inset-0 bg-[radial-gradient(#00e5ff_1px,transparent_1px)] [background-size:32px_32px] opacity-10" />

      <motion.div 
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        className="w-full max-w-4xl glass-card p-12 md:p-16 text-center space-y-8 relative z-10 border-2 border-cyan-500/50 shadow-2xl shadow-cyan-500/30"
      >
        <div className="w-20 h-20 rounded-2xl bg-cyan-500/20 border-2 border-cyan-400 mx-auto flex items-center justify-center shadow-lg shadow-cyan-500/40">
          <Layers className="w-10 h-10 text-cyan-300 animate-pulse" />
        </div>

        <div>
          <span className="text-sm md:text-base font-mono font-bold text-amber-400 uppercase tracking-widest block mb-3">
            PART DIVIDER
          </span>
          <h2 className="text-4xl md:text-6xl font-black text-white tracking-wide leading-tight">
            {slideData.title}
          </h2>
        </div>

        <p className="text-2xl md:text-3xl text-cyan-200 font-bold max-w-2xl mx-auto leading-relaxed">
          {slideData.subtitle}
        </p>

        <div className="pt-4 flex justify-center">
          <div className="inline-flex items-center gap-3 px-6 py-3 rounded-full bg-cyan-500/20 border border-cyan-400 text-sm md:text-base font-bold text-cyan-300 shadow-md">
            <span>Entering Next Phase</span>
            <ArrowRight className="w-5 h-5" />
          </div>
        </div>
      </motion.div>
    </div>
  );
}
