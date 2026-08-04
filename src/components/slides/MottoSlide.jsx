import React from 'react';
import { motion } from 'framer-motion';
import { Award, CheckCircle2, Sparkles } from 'lucide-react';

export default function MottoSlide({ slideData }) {
  return (
    <div className="h-full flex flex-col justify-between p-6 md:p-10 relative">
      {/* Header */}
      <div>
        <div className="flex items-center gap-2 text-amber-400 font-mono text-xs font-bold tracking-widest uppercase">
          <Award className="w-4 h-4 text-amber-400" />
          <span>{slideData.title}</span>
        </div>
        <h2 className="text-xl md:text-3xl font-black text-white mt-1">
          {slideData.subtitle}
        </h2>
      </div>

      {/* Main Container */}
      <motion.div 
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        className="my-auto glass-card-gold p-8 md:p-10 max-w-4xl mx-auto w-full space-y-6 border-2 border-amber-500/40 shadow-2xl shadow-amber-500/10"
      >
        <div className="flex items-center gap-3 border-b border-amber-500/30 pb-4">
          <div className="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-400 flex items-center justify-center">
            <Sparkles className="w-5 h-5 text-amber-300" />
          </div>
          <div>
            <h3 className="text-lg font-bold text-white">STRATEGIC IMPERATIVES & WISDOM</h3>
            <p className="text-xs text-amber-300 font-mono">Soli Deo Gloria Guidance</p>
          </div>
        </div>

        <ul className="space-y-4">
          {slideData.points?.map((pt, idx) => (
            <motion.li 
              key={idx}
              initial={{ opacity: 0, x: -10 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: idx * 0.1 }}
              className="flex items-start gap-3.5 text-base md:text-lg text-slate-100 font-medium"
            >
              <CheckCircle2 className="w-5 h-5 text-amber-400 shrink-0 mt-0.5" />
              <span>{pt}</span>
            </motion.li>
          ))}
        </ul>
      </motion.div>

      <div className="text-xs text-slate-500 font-mono">
        Slide #{slideData.num} • Strategic Wisdom Core
      </div>
    </div>
  );
}
