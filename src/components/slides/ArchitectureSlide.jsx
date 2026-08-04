import React from 'react';
import { motion } from 'framer-motion';
import { Folder, HardDrive, Shield, Terminal, ArrowRight } from 'lucide-react';

export default function ArchitectureSlide({ slideData }) {
  return (
    <div className="h-full flex flex-col justify-between p-6 md:p-10 relative">
      {/* Header */}
      <div>
        <div className="flex items-center gap-2 text-amber-400 font-mono text-xs font-bold tracking-widest uppercase">
          <Terminal className="w-4 h-4 text-amber-400" />
          <span>{slideData.title}</span>
        </div>
        <h2 className="text-xl md:text-3xl font-black text-white mt-1">
          {slideData.subtitle}
        </h2>
      </div>

      {/* Directory & Flow Architecture */}
      <div className="my-auto grid grid-cols-1 md:grid-cols-12 gap-6 items-center">
        {/* Interactive Directory Tree */}
        <motion.div 
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          className="md:col-span-7 glass-card p-6 space-y-3 font-mono text-xs"
        >
          <div className="flex items-center justify-between border-b border-slate-700 pb-2 mb-3">
            <div className="flex items-center gap-2">
              <HardDrive className="w-4 h-4 text-cyan-400" />
              <span className="font-bold text-white">Google Drive Persistent Root</span>
            </div>
            <span className="text-[10px] text-cyan-300 bg-cyan-500/20 px-2 py-0.5 rounded border border-cyan-500/30">
              Cloud Native Path
            </span>
          </div>

          {slideData.tree?.map((item, idx) => (
            <motion.div 
              key={idx}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: idx * 0.1 }}
              className="p-3 rounded-lg bg-slate-900/80 border border-slate-800 flex items-center justify-between hover:border-cyan-500/40 transition group"
            >
              <div className="flex items-center gap-2.5">
                <Folder className={`w-4 h-4 ${idx === 0 ? "text-amber-400" : "text-cyan-400"}`} />
                <span className={`font-bold ${idx === 0 ? "text-amber-300 text-sm" : "text-slate-200"}`}>
                  {item.folder}
                </span>
              </div>
              <span className="text-[11px] text-slate-400 group-hover:text-cyan-200 transition">
                {item.desc}
              </span>
            </motion.div>
          ))}
        </motion.div>

        {/* Right Info Box */}
        <motion.div 
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.2 }}
          className="md:col-span-5 glass-card-gold p-6 space-y-4"
        >
          <div className="flex items-center gap-2 text-amber-300">
            <Shield className="w-5 h-5 text-amber-400" />
            <h3 className="font-bold text-base">Persistent Workspace Home</h3>
          </div>

          <p className="text-xs text-slate-200 leading-relaxed">
            The agent maintains continuous state across sessions by reading from and writing to your dedicated <code className="bg-slate-900 px-1.5 py-0.5 rounded text-amber-300">/Spark_OS/</code> folder inside Google Drive.
          </p>

          <div className="p-3 rounded-lg bg-slate-900/90 border border-amber-500/30 space-y-1.5 text-xs">
            <span className="font-bold text-amber-400 block">HANDS-ON LAB REQUIREMENT:</span>
            <p className="text-slate-300">
              Students will set up this exact directory structure in Google Drive during Week 1 assignment.
            </p>
          </div>
        </motion.div>
      </div>

      <div className="text-xs text-slate-500 font-mono">
        Slide #{slideData.num} • System Directory Architecture
      </div>
    </div>
  );
}
