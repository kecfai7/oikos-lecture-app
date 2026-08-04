import React from 'react';
import { motion } from 'framer-motion';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from 'recharts';
import { BarChart3, Clock, Zap } from 'lucide-react';

export default function EfficiencyChartSlide({ slideData }) {
  // Case Study Virgin Voyages Data (Minutes)
  const virginData = [
    { name: 'Manual Process', minutes: 360, fill: '#64748b', label: '6 Hours (360 mins)' },
    { name: 'Gemini Agent', minutes: 11, fill: '#00e5ff', label: '11 Minutes' },
  ];

  // TPU Generation Data
  const tpuData = [
    { name: 'TPU v7 (Old)', perf: 100, energy: 100, fill: '#64748b' },
    { name: 'TPU v8 (New)', perf: 300, energy: 33, fill: '#f4c430' },
  ];

  const isTpu = slideData.num === 20;

  return (
    <div className="h-full flex flex-col justify-between p-6 md:p-10 relative">
      {/* Header */}
      <div>
        <div className="flex items-center gap-2 text-amber-400 font-mono text-xs font-bold tracking-widest uppercase">
          <BarChart3 className="w-4 h-4 text-amber-400" />
          <span>{slideData.title}</span>
        </div>
        <h2 className="text-xl md:text-3xl font-black text-white mt-1">
          {slideData.subtitle}
        </h2>
      </div>

      {/* Main Chart Card */}
      <div className="my-auto grid grid-cols-1 md:grid-cols-12 gap-6 items-center">
        {/* Interactive Chart Container */}
        <motion.div 
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          className="md:col-span-7 glass-card p-6 h-[320px] flex flex-col justify-between"
        >
          <div className="flex items-center justify-between border-b border-slate-700 pb-2">
            <span className="text-xs font-bold text-cyan-300 uppercase tracking-wider font-mono">
              {slideData.chartTitle}
            </span>
            <span className="text-[10px] px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-semibold">
              Live Animated Rechart
            </span>
          </div>

          <div className="h-[220px] w-full mt-2">
            <ResponsiveContainer width="100%" height="100%">
              {!isTpu ? (
                <BarChart data={virginData} layout="vertical" margin={{ left: 20, right: 30, top: 10, bottom: 10 }}>
                  <XAxis type="number" stroke="#94a3b8" unit=" min" />
                  <YAxis type="category" dataKey="name" stroke="#ffffff" width={120} tick={{ fontSize: 12 }} />
                  <Tooltip 
                    contentStyle={{ backgroundColor: '#0f172a', borderColor: '#00e5ff', borderRadius: '8px', color: '#fff' }}
                  />
                  <Bar dataKey="minutes" radius={[0, 8, 8, 0]}>
                    {virginData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.fill} />
                    ))}
                  </Bar>
                </BarChart>
              ) : (
                <BarChart data={tpuData} margin={{ left: 10, right: 10, top: 10, bottom: 10 }}>
                  <XAxis dataKey="name" stroke="#ffffff" />
                  <YAxis stroke="#94a3b8" unit="%" />
                  <Tooltip 
                    contentStyle={{ backgroundColor: '#0f172a', borderColor: '#f4c430', borderRadius: '8px', color: '#fff' }}
                  />
                  <Bar dataKey="perf" name="Performance vs v7" fill="#00e5ff" radius={[6, 6, 0, 0]} />
                  <Bar dataKey="energy" name="Energy Usage vs v7" fill="#f4c430" radius={[6, 6, 0, 0]} />
                </BarChart>
              )}
            </ResponsiveContainer>
          </div>
        </motion.div>

        {/* Side Metrics & Takeaways */}
        <motion.div 
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.2 }}
          className="md:col-span-5 glass-card-gold p-6 space-y-4 flex flex-col justify-between h-[320px]"
        >
          <div>
            <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30 uppercase tracking-widest">
              CASE STUDY IMPACT
            </span>
            <h3 className="text-xl font-bold text-white mt-2">
              {!isTpu ? "97% Reduction in Time" : "3x Compute, 67% Less Energy"}
            </h3>
          </div>

          <p className="text-sm text-slate-200 leading-relaxed">
            {!isTpu 
              ? "Rescheduling a cruise booking used to take human operators 6 hours of manual spreadsheet checking and phone calls. Deploying Gemini agents reduced execution time to 11 minutes."
              : "Google TPU v8 delivers triple the inference performance while consuming 67% less energy per token compared to TPU v7, establishing green computing leadership."
            }
          </p>

          <div className="p-3 rounded-lg bg-slate-900/80 border border-amber-500/30 flex items-center gap-3">
            <Zap className="w-6 h-6 text-amber-400 shrink-0" />
            <span className="text-xs text-amber-200 font-medium">
              {!isTpu ? "From 360 mins ➔ 11 mins autonomous workflow" : "High speed with eco-friendly infrastructure"}
            </span>
          </div>
        </motion.div>
      </div>

      <div className="text-xs text-slate-500 font-mono">
        Slide #{slideData.num} • Recharts Interactive Data
      </div>
    </div>
  );
}
