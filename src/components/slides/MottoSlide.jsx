import React from 'react';
import { motion } from 'framer-motion';
import { Award, CheckCircle2, Sparkles } from 'lucide-react';

export default function MottoSlide({ slideData }) {
  return (
    <div className="h-full flex flex-col justify-between p-8 md:p-12 relative">
      {/* Header */}
      <div>
        <div className="flex items-center gap-2 text-amber-400 font-mono text-sm font-bold tracking-widest uppercase">
          <Award className="w-5 h-5 text-amber-400" />
          <span>{slideData.title}</span>
        </div>
        <h2 className="text-2xl md:text-4xl font-black text-white mt-2 leading-snug">
          {slideData.subtitle}
        </h2>
      </div>

      {/* Main Container */}
      <motion.div 
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        className="my-auto glass-card-gold p-10 md:p-12 max-w-5xl mx-auto w-full space-y-8 border-2 border-amber-500/50 shadow-2xl shadow-amber-500/20"
      >
        <div className="flex items-center gap-4 border-b border-amber-500/40 pb-5">
          <div className="w-12 h-12 rounded-2xl bg-amber-500/20 border border-amber-400 flex items-center justify-center shadow-lg">
            <Sparkles className="w-6 h-6 text-amber-300" />
          </div>
          <div>
            <h3 className="text-xl md:text-2xl font-black text-white">STRATEGIC IMPERATIVES & WISDOM</h3>
            <p className="text-sm text-amber-300 font-mono font-bold">Soli Deo Gloria Guidance</p>
          </div>
        </div>

        <ul className="space-y-6">
          {slideData.points?.map((pt, idx) => (
            <motion.li 
              key={idx}
              initial={{ opacity: 0, x: -10 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: idx * 0.1 }}
              className="flex items-start gap-4 text-xl md:text-2xl text-white font-semibold leading-relaxed"
            >
              <CheckCircle2 className="w-7 h-7 text-amber-400 shrink-0 mt-0.5" />
              <span>{pt}</span>
            </motion.li>
          ))}
        </ul>
      </motion.div>

      <div className="text-xs text-slate-500 font-mono">
        Slide #{slideData.num} • High Visibility Strategic Wisdom
      </div>
    </div>
  );
}
