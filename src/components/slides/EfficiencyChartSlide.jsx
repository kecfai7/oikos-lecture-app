import React from 'react';
import { motion } from 'framer-motion';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from 'recharts';
import { BarChart3, Zap } from 'lucide-react';

export default function EfficiencyChartSlide({ slideData }) {
  const virginData = [
    { name: 'Manual Process', minutes: 360, fill: '#64748b', label: '6 Hours (360 mins)' },
    { name: 'Gemini Agent', minutes: 11, fill: '#00e5ff', label: '11 Minutes' },
  ];

  const tpuData = [
    { name: 'TPU v7 (Old)', perf: 100, energy: 100, fill: '#64748b' },
    { name: 'TPU v8 (New)', perf: 300, energy: 33, fill: '#f4c430' },
  ];

  const isTpu = slideData.num === 20;

  return (
    <div className="h-full flex flex-col justify-between p-8 md:p-12 relative">
      {/* Header */}
      <div>
        <div className="flex items-center gap-2 text-amber-400 font-mono text-sm font-bold tracking-widest uppercase">
          <BarChart3 className="w-5 h-5 text-amber-400" />
          <span>{slideData.title}</span>
        </div>
        <h2 className="text-2xl md:text-4xl font-black text-white mt-2 leading-snug">
          {slideData.subtitle}
        </h2>
      </div>

      {/* Main Chart Card */}
      <div className="my-auto grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
        {/* Interactive Chart Container */}
        <motion.div 
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          className="md:col-span-7 glass-card p-8 h-[380px] flex flex-col justify-between"
        >
          <div className="flex items-center justify-between border-b border-slate-700 pb-3">
            <span className="text-sm font-bold text-cyan-300 uppercase tracking-wider font-mono">
              {slideData.chartTitle}
            </span>
            <span className="text-xs px-3 py-1 rounded-full bg-cyan-500/20 text-cyan-300 font-bold border border-cyan-500/30">
              Interactive Chart
            </span>
          </div>

          <div className="h-[270px] w-full mt-2">
            <ResponsiveContainer width="100%" height="100%">
              {!isTpu ? (
                <BarChart data={virginData} layout="vertical" margin={{ left: 30, right: 40, top: 10, bottom: 10 }}>
                  <XAxis type="number" stroke="#94a3b8" unit=" min" tick={{ fontSize: 14 }} />
                  <YAxis type="category" dataKey="name" stroke="#ffffff" width={150} tick={{ fontSize: 16, fontWeight: 'bold' }} />
                  <Tooltip 
                    contentStyle={{ backgroundColor: '#0f172a', borderColor: '#00e5ff', borderRadius: '12px', color: '#fff', fontSize: '16px' }}
                  />
                  <Bar dataKey="minutes" radius={[0, 10, 10, 0]}>
                    {virginData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.fill} />
                    ))}
                  </Bar>
                </BarChart>
              ) : (
                <BarChart data={tpuData} margin={{ left: 10, right: 10, top: 10, bottom: 10 }}>
                  <XAxis dataKey="name" stroke="#ffffff" tick={{ fontSize: 16, fontWeight: 'bold' }} />
                  <YAxis stroke="#94a3b8" unit="%" tick={{ fontSize: 14 }} />
                  <Tooltip 
                    contentStyle={{ backgroundColor: '#0f172a', borderColor: '#f4c430', borderRadius: '12px', color: '#fff', fontSize: '16px' }}
                  />
                  <Bar dataKey="perf" name="Performance vs v7" fill="#00e5ff" radius={[8, 8, 0, 0]} />
                  <Bar dataKey="energy" name="Energy Usage vs v7" fill="#f4c430" radius={[8, 8, 0, 0]} />
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
          className="md:col-span-5 glass-card-gold p-8 space-y-6 flex flex-col justify-between h-[380px]"
        >
          <div>
            <span className="text-xs font-bold px-3 py-1.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 uppercase tracking-widest">
              CASE STUDY IMPACT
            </span>
            <h3 className="text-2xl md:text-3xl font-black text-white mt-3">
              {!isTpu ? "97% Reduction in Time" : "3x Compute, 67% Less Energy"}
            </h3>
          </div>

          <p className="text-lg md:text-xl text-slate-100 font-medium leading-relaxed">
            {!isTpu 
              ? "Rescheduling a cruise booking used to take human operators 6 hours of manual calls and spreadsheet checks. Deploying Gemini agents reduced execution time to 11 minutes."
              : "Google TPU v8 delivers triple the inference performance while consuming 67% less energy per token compared to TPU v7, establishing green computing leadership."
            }
          </p>

          <div className="p-4 rounded-xl bg-slate-900/90 border border-amber-500/40 flex items-center gap-3">
            <Zap className="w-7 h-7 text-amber-400 shrink-0" />
            <span className="text-base md:text-lg text-amber-200 font-bold">
              {!isTpu ? "From 360 mins ➔ 11 mins workflow" : "High speed with eco-friendly infrastructure"}
            </span>
          </div>
        </motion.div>
      </div>

      <div className="text-xs text-slate-500 font-mono">
        Slide #{slideData.num} • High Visibility Data Visuals
      </div>
    </div>
  );
}
