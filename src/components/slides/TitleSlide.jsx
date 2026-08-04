import React from 'react';
import { motion } from 'framer-motion';
import { ShieldCheck, Sparkles, Award } from 'lucide-react';

export default function TitleSlide({ slideData }) {
  return (
    <div className="h-full flex flex-col justify-between p-8 md:p-12 relative overflow-hidden">
      {/* Background Neon Orbs */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-amber-500/10 rounded-full blur-3xl pointer-events-none" />

      {/* Header Motto */}
      <motion.div 
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="flex items-center gap-3"
      >
        <div className="px-3 py-1 rounded-full bg-amber-500/20 border border-amber-500/30 text-amber-300 font-bold text-xs tracking-wider flex items-center gap-1.5">
          <Award className="w-4 h-4 text-amber-400" />
          <span>OIKOS UNIVERSITY • SOLI DEO GLORIA</span>
        </div>
      </motion.div>

      {/* Main Center Title */}
      <motion.div 
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ delay: 0.2 }}
        className="my-auto max-w-4xl space-y-6"
      >
        <h1 className="text-4xl md:text-6xl font-black text-white leading-tight tracking-tight">
          THE ARCHITECT OF <span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500">INTELLIGENCE</span>
        </h1>
        
        <p className="text-xl md:text-2xl text-cyan-300 font-semibold max-w-3xl">
          Mastering Agentic IT & Strategic Wisdom
        </p>

        <div className="p-4 rounded-xl bg-slate-900/80 border border-cyan-500/30 text-slate-300 text-base md:text-lg max-w-2xl shadow-xl backdrop-blur-md">
          {slideData.detail}
        </div>
      </motion.div>

      {/* Instructor Footer */}
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4 }}
        className="pt-6 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-4 text-xs text-slate-400"
      >
        <div className="flex items-center gap-2">
          <ShieldCheck className="w-4 h-4 text-cyan-400" />
          <span className="font-semibold text-slate-200">{slideData.instructor}</span>
        </div>
        <span className="text-slate-500 font-mono">Session 1 of 15 Master Course</span>
      </motion.div>
    </div>
  );
}
