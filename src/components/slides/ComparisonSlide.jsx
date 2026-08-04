import React from 'react';
import { motion } from 'framer-motion';
import { CheckCircle2, XCircle, ArrowRightLeft } from 'lucide-react';

export default function ComparisonSlide({ slideData }) {
  return (
    <div className="h-full flex flex-col justify-between p-6 md:p-10 relative">
      {/* Slide Header */}
      <div>
        <div className="flex items-center gap-2 text-amber-400 font-mono text-xs font-bold tracking-widest uppercase">
          <ArrowRightLeft className="w-4 h-4 text-amber-400" />
          <span>{slideData.title}</span>
        </div>
        <h2 className="text-xl md:text-3xl font-black text-white mt-1">
          {slideData.subtitle}
        </h2>
      </div>

      {/* Two Comparison Cards */}
      <div className="my-auto grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Left Card */}
        <motion.div 
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          className="glass-card p-6 md:p-8 flex flex-col justify-between space-y-4 border-slate-700"
        >
          <div>
            <span className="text-[10px] font-bold px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700 uppercase tracking-wider inline-block mb-3">
              {slideData.leftCard.tag}
            </span>
            <h3 className="text-xl font-bold text-cyan-300">
              {slideData.leftCard.title}
            </h3>
          </div>

          <ul className="space-y-3">
            {slideData.leftCard.points.map((pt, idx) => (
              <li key={idx} className="flex items-start gap-2.5 text-sm text-slate-200">
                <XCircle className="w-4 h-4 text-slate-500 shrink-0 mt-0.5" />
                <span>{pt}</span>
              </li>
            ))}
          </ul>
        </motion.div>

        {/* Right Card */}
        <motion.div 
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.1 }}
          className="glass-card-gold p-6 md:p-8 flex flex-col justify-between space-y-4"
        >
          <div>
            <span className="text-[10px] font-bold px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30 uppercase tracking-wider inline-block mb-3">
              {slideData.rightCard.tag}
            </span>
            <h3 className="text-xl font-bold text-amber-300">
              {slideData.rightCard.title}
            </h3>
          </div>

          <ul className="space-y-3">
            {slideData.rightCard.points.map((pt, idx) => (
              <li key={idx} className="flex items-start gap-2.5 text-sm text-white font-medium">
                <CheckCircle2 className="w-4 h-4 text-amber-400 shrink-0 mt-0.5" />
                <span>{pt}</span>
              </li>
            ))}
          </ul>
        </motion.div>
      </div>

      <div className="text-xs text-slate-500 font-mono">
        Slide #{slideData.num} • Comparison Layout
      </div>
    </div>
  );
}
