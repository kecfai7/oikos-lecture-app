import React from 'react';
import { motion } from 'framer-motion';
import { TrendingUp, CheckCircle2 } from 'lucide-react';

export default function MetricSlide({ slideData }) {
  // Support both 3-metrics array and single metric + points
  const hasMetricsArray = Array.isArray(slideData.metrics) && slideData.metrics.length > 0;

  return (
    <div className="h-full flex flex-col justify-between p-8 md:p-12 relative">
      {/* Header */}
      <div>
        <div className="flex items-center gap-2 text-amber-400 font-mono text-sm font-bold tracking-widest uppercase">
          <TrendingUp className="w-5 h-5 text-amber-400" />
          <span>{slideData.title}</span>
        </div>
        <h2 className="text-2xl md:text-4xl font-black text-white mt-2 leading-snug">
          {slideData.subtitle}
        </h2>
      </div>

      {/* Metric Content */}
      <div className="my-auto">
        {hasMetricsArray ? (
          /* 3-Cards Metric Grid */
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {slideData.metrics.map((m, idx) => (
              <motion.div
                key={idx}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: idx * 0.15 }}
                className="glass-card p-8 rounded-2xl border border-amber-500/30 text-center flex flex-col justify-between hover:border-amber-400/60 transition-all shadow-xl bg-slate-900/60"
              >
                <div className="text-sm font-bold text-amber-400 uppercase tracking-widest font-mono mb-2">
                  {m.label}
                </div>
                <div className="text-5xl md:text-6xl font-black text-transparent bg-clip-text bg-gradient-to-r from-amber-300 via-yellow-200 to-amber-500 my-4 tracking-tight">
                  {m.value}
                </div>
                <div className="text-base text-slate-300 leading-relaxed font-medium">
                  {m.desc}
                </div>
              </motion.div>
            ))}
          </div>
        ) : (
          /* Single Highlight Box + Bullets */
          <div className="grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
            <motion.div 
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              className="md:col-span-5 glass-card-gold p-10 text-center flex flex-col justify-center items-center space-y-3 border-2 border-amber-500/50 shadow-2xl shadow-amber-500/30"
            >
              <span className="text-sm font-bold text-amber-300 uppercase tracking-widest font-mono">
                KEY PERFORMANCE METRIC
              </span>
              <div className="text-5xl md:text-7xl font-black text-transparent bg-clip-text bg-gradient-to-r from-amber-300 via-yellow-200 to-amber-500 my-3 tracking-tight">
                {slideData.metric || (slideData.stat && slideData.stat.value) || "100X"}
              </div>
              <span className="text-lg md:text-2xl font-bold text-slate-100">
                {slideData.metricLabel || (slideData.stat && slideData.stat.label) || "Key Metric"}
              </span>
            </motion.div>

            <motion.div 
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.2 }}
              className="md:col-span-7 glass-card p-10 space-y-6"
            >
              <h3 className="text-xl md:text-2xl font-bold text-cyan-300 border-b border-slate-700 pb-3">
                Key Strategic Insights
              </h3>
              <ul className="space-y-4">
                {(slideData.points || []).map((pt, idx) => (
                  <li key={idx} className="flex items-start gap-3.5 text-lg md:text-xl text-slate-100 font-medium leading-relaxed">
                    <CheckCircle2 className="w-6 h-6 text-cyan-400 shrink-0 mt-0.5" />
                    <span>{pt}</span>
                  </li>
                ))}
              </ul>
            </motion.div>
          </div>
        )}
      </div>

      <div className="text-xs text-slate-500 font-mono">
        Slide #{slideData.num} • High Visibility Metric
      </div>
    </div>
  );
}
