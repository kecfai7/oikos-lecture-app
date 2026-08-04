import React from 'react';
import { motion } from 'framer-motion';
import { TrendingUp, Clock, CheckCircle2 } from 'lucide-react';

export default function MetricSlide({ slideData }) {
  return (
    <div className="h-full flex flex-col justify-between p-6 md:p-10 relative">
      {/* Header */}
      <div>
        <div className="flex items-center gap-2 text-amber-400 font-mono text-xs font-bold tracking-widest uppercase">
          <TrendingUp className="w-4 h-4 text-amber-400" />
          <span>{slideData.title}</span>
        </div>
        <h2 className="text-xl md:text-3xl font-black text-white mt-1">
          {slideData.subtitle}
        </h2>
      </div>

      {/* Metric Content */}
      <div className="my-auto grid grid-cols-1 md:grid-cols-12 gap-6 items-center">
        {/* Metric Highlight Box */}
        <motion.div 
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          className="md:col-span-5 glass-card-gold p-8 text-center flex flex-col justify-center items-center space-y-2 border-2 border-amber-500/50 shadow-2xl shadow-amber-500/20"
        >
          <span className="text-xs font-bold text-amber-300 uppercase tracking-widest font-mono">
            KEY PERFORMANCE METRIC
          </span>
          <div className="text-4xl md:text-6xl font-black text-transparent bg-clip-text bg-gradient-to-r from-amber-300 via-yellow-200 to-amber-500 my-2">
            {slideData.metric}
          </div>
          <span className="text-sm font-semibold text-slate-200">
            {slideData.metricLabel}
          </span>
        </motion.div>

        {/* Bullet Points */}
        <motion.div 
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.2 }}
          className="md:col-span-7 glass-card p-8 space-y-4"
        >
          <h3 className="text-lg font-bold text-cyan-300 border-b border-slate-700 pb-2">
            Key Strategic Insights
          </h3>
          <ul className="space-y-3">
            {slideData.points.map((pt, idx) => (
              <li key={idx} className="flex items-start gap-3 text-sm md:text-base text-slate-200">
                <CheckCircle2 className="w-5 h-5 text-cyan-400 shrink-0 mt-0.5" />
                <span>{pt}</span>
              </li>
            ))}
          </ul>
        </motion.div>
      </div>

      <div className="text-xs text-slate-500 font-mono">
        Slide #{slideData.num} • Metric Impact
      </div>
    </div>
  );
}
