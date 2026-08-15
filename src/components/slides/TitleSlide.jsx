import React from 'react';
import { motion } from 'framer-motion';
import { ShieldCheck, Sparkles, Award } from 'lucide-react';

export default function TitleSlide({ slideData }) {
  return (
    <div className="h-full flex flex-col justify-between p-8 md:p-14 relative overflow-hidden">
      {/* Background Neon Orbs */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-amber-500/10 rounded-full blur-3xl pointer-events-none" />

      {/* Header Motto */}
      <motion.div 
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="flex items-center gap-3"
      >
        <div className="px-4 py-1.5 rounded-full bg-amber-500/20 border border-amber-500/40 text-amber-300 font-bold text-sm md:text-base tracking-wider flex items-center gap-2 shadow-lg">
          <Award className="w-5 h-5 text-amber-400" />
          <span>OIKOS UNIVERSITY • SOLI DEO GLORIA</span>
        </div>
      </motion.div>

      {/* Main Center Title */}
      <motion.div 
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ delay: 0.2 }}
        className="my-auto max-w-5xl space-y-6"
      >
        <h1 className="text-5xl md:text-7xl font-black text-white leading-tight tracking-tight drop-shadow-lg">
          THE ARCHITECT OF <span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-sky-300 to-blue-500">INTELLIGENCE</span>
        </h1>
        
        <p className="text-2xl md:text-4xl text-cyan-300 font-bold max-w-4xl leading-snug">
          Mastering Agentic IT & Strategic Wisdom
        </p>

        <div className="p-5 md:p-6 rounded-2xl bg-slate-900/90 border-2 border-cyan-500/40 text-slate-100 text-xl md:text-2xl font-semibold max-w-3xl shadow-2xl backdrop-blur-md">
          {slideData.detail}
        </div>
      </motion.div>

      {/* Instructor Footer */}
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4 }}
        className="pt-6 border-t border-slate-800 flex flex-wrap items-center justify-between gap-4 text-sm md:text-base text-slate-300"
      >
        <div className="flex items-center gap-2.5">
          <ShieldCheck className="w-5 h-5 text-cyan-400" />
          <span className="font-bold text-white text-base md:text-lg">{slideData.instructor}</span>
        </div>
        <span className="text-slate-400 font-mono font-bold text-sm md:text-base">
          Session {slideData.sessionNum || slideData.detail?.match(/Session (\d+)/i)?.[1] || '1'} of 15 Master Course
        </span>
      </motion.div>
    </div>
  );
}
