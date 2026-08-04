import React from 'react';
import { motion } from 'framer-motion';
import { Triangle, Shield, Check } from 'lucide-react';

export default function TriadSlide({ slideData }) {
  return (
    <div className="h-full flex flex-col justify-between p-6 md:p-10 relative">
      {/* Header */}
      <div>
        <div className="flex items-center gap-2 text-amber-400 font-mono text-xs font-bold tracking-widest uppercase">
          <Triangle className="w-4 h-4 text-amber-400" />
          <span>{slideData.title}</span>
        </div>
        <h2 className="text-xl md:text-3xl font-black text-white mt-1">
          {slideData.subtitle}
        </h2>
      </div>

      {/* Three Cards */}
      <div className="my-auto grid grid-cols-1 md:grid-cols-3 gap-5">
        {slideData.cards.map((card, idx) => (
          <motion.div 
            key={idx}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: idx * 0.1 }}
            className={`glass-card p-6 flex flex-col justify-between space-y-4 ${
              idx === 1 ? "border-amber-500/40 shadow-lg shadow-amber-500/10" : ""
            }`}
          >
            <div className="space-y-2">
              <div className="w-8 h-8 rounded-lg bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400 text-xs font-bold font-mono">
                0{idx + 1}
              </div>
              <h3 className="text-lg font-bold text-cyan-300">
                {card.title}
              </h3>
            </div>

            <p className="text-sm text-slate-300 leading-relaxed">
              {card.desc}
            </p>
          </motion.div>
        ))}
      </div>

      <div className="text-xs text-slate-500 font-mono">
        Slide #{slideData.num} • Triad Architecture
      </div>
    </div>
  );
}
