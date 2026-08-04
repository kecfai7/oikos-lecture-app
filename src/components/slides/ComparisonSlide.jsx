import React from 'react';
import { motion } from 'framer-motion';
import { CheckCircle2, XCircle, ArrowRightLeft } from 'lucide-react';

export default function ComparisonSlide({ slideData }) {
  return (
    <div className="h-full flex flex-col justify-between p-8 md:p-12 relative">
      {/* Slide Header */}
      <div>
        <div className="flex items-center gap-2 text-amber-400 font-mono text-sm font-bold tracking-widest uppercase">
          <ArrowRightLeft className="w-5 h-5 text-amber-400" />
          <span>{slideData.title}</span>
        </div>
        <h2 className="text-2xl md:text-4xl font-black text-white mt-2 leading-snug">
          {slideData.subtitle}
        </h2>
      </div>

      {/* Two Comparison Cards */}
      <div className="my-auto grid grid-cols-1 md:grid-cols-2 gap-8">
        {/* Left Card */}
        <motion.div 
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          className="glass-card p-8 md:p-10 flex flex-col justify-between space-y-6 border-slate-700"
        >
          <div>
            <span className="text-xs font-bold px-3 py-1.5 rounded bg-slate-800 text-slate-200 border border-slate-700 uppercase tracking-wider inline-block mb-3">
              {slideData.leftCard.tag}
            </span>
            <h3 className="text-2xl md:text-3xl font-bold text-cyan-300">
              {slideData.leftCard.title}
            </h3>
          </div>

          <ul className="space-y-4">
            {slideData.leftCard.points.map((pt, idx) => (
              <li key={idx} className="flex items-start gap-3 text-lg md:text-xl text-slate-100 font-medium leading-relaxed">
                <XCircle className="w-6 h-6 text-slate-400 shrink-0 mt-0.5" />
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
          className="glass-card-gold p-8 md:p-10 flex flex-col justify-between space-y-6"
        >
          <div>
            <span className="text-xs font-bold px-3 py-1.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 uppercase tracking-wider inline-block mb-3">
              {slideData.rightCard.tag}
            </span>
            <h3 className="text-2xl md:text-3xl font-bold text-amber-300">
              {slideData.rightCard.title}
            </h3>
          </div>

          <ul className="space-y-4">
            {slideData.rightCard.points.map((pt, idx) => (
              <li key={idx} className="flex items-start gap-3 text-lg md:text-xl text-white font-semibold leading-relaxed">
                <CheckCircle2 className="w-6 h-6 text-amber-400 shrink-0 mt-0.5" />
                <span>{pt}</span>
              </li>
            ))}
          </ul>
        </motion.div>
      </div>

      <div className="text-xs text-slate-500 font-mono">
        Slide #{slideData.num} • High Visibility Comparison
      </div>
    </div>
  );
}
