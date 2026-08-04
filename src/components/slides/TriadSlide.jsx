import React from 'react';
import { motion } from 'framer-motion';
import { Triangle } from 'lucide-react';

export default function TriadSlide({ slideData }) {
  return (
    <div className="h-full flex flex-col justify-between p-8 md:p-12 relative">
      {/* Header */}
      <div>
        <div className="flex items-center gap-2 text-amber-400 font-mono text-sm font-bold tracking-widest uppercase">
          <Triangle className="w-5 h-5 text-amber-400" />
          <span>{slideData.title}</span>
        </div>
        <h2 className="text-2xl md:text-4xl font-black text-white mt-2 leading-snug">
          {slideData.subtitle}
        </h2>
      </div>

      {/* Three Cards */}
      <div className="my-auto grid grid-cols-1 md:grid-cols-3 gap-6">
        {slideData.cards.map((card, idx) => (
          <motion.div 
            key={idx}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: idx * 0.1 }}
            className={`glass-card p-8 flex flex-col justify-between space-y-6 ${
              idx === 1 ? "border-amber-500/50 shadow-xl shadow-amber-500/20" : ""
            }`}
          >
            <div className="space-y-3">
              <div className="w-10 h-10 rounded-xl bg-cyan-500/20 border border-cyan-400 flex items-center justify-center text-cyan-300 text-base font-bold font-mono shadow-md">
                0{idx + 1}
              </div>
              <h3 className="text-xl md:text-2xl font-bold text-cyan-300">
                {card.title}
              </h3>
            </div>

            <p className="text-base md:text-xl text-slate-100 font-medium leading-relaxed">
              {card.desc}
            </p>
          </motion.div>
        ))}
      </div>

      <div className="text-xs text-slate-500 font-mono">
        Slide #{slideData.num} • High Visibility Triad
      </div>
    </div>
  );
}
