import React from 'react';
import { motion } from 'framer-motion';
import { Folder, HardDrive, Shield, Terminal } from 'lucide-react';

export default function ArchitectureSlide({ slideData }) {
  return (
    <div className="h-full flex flex-col justify-between p-8 md:p-12 relative">
      {/* Header */}
      <div>
        <div className="flex items-center gap-2 text-amber-400 font-mono text-sm font-bold tracking-widest uppercase">
          <Terminal className="w-5 h-5 text-amber-400" />
          <span>{slideData.title}</span>
        </div>
        <h2 className="text-2xl md:text-4xl font-black text-white mt-2 leading-snug">
          {slideData.subtitle}
        </h2>
      </div>

      {/* Directory & Flow Architecture */}
      <div className="my-auto grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
        {/* Interactive Directory Tree */}
        <motion.div 
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          className="md:col-span-7 glass-card p-8 space-y-4 font-mono"
        >
          <div className="flex items-center justify-between border-b border-slate-700 pb-3 mb-4">
            <div className="flex items-center gap-3">
              <HardDrive className="w-5 h-5 text-cyan-400" />
              <span className="font-bold text-white text-base md:text-lg">Google Drive Persistent Root</span>
            </div>
            <span className="text-xs text-cyan-300 bg-cyan-500/20 px-3 py-1 rounded-full border border-cyan-500/30 font-bold">
              Cloud Native Path
            </span>
          </div>

          {slideData.tree?.map((item, idx) => (
            <motion.div 
              key={idx}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: idx * 0.1 }}
              className="p-4 rounded-xl bg-slate-900/90 border border-slate-700 flex items-center justify-between hover:border-cyan-400 transition group shadow-md"
            >
              <div className="flex items-center gap-3">
                <Folder className={`w-6 h-6 ${idx === 0 ? "text-amber-400" : "text-cyan-400"}`} />
                <span className={`font-bold ${idx === 0 ? "text-amber-300 text-lg md:text-xl" : "text-slate-100 text-base md:text-lg"}`}>
                  {item.folder}
                </span>
              </div>
              <span className="text-xs md:text-sm text-slate-300 group-hover:text-cyan-200 transition font-medium">
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
          className="md:col-span-5 glass-card-gold p-8 space-y-6"
        >
          <div className="flex items-center gap-3 text-amber-300">
            <Shield className="w-6 h-6 text-amber-400" />
            <h3 className="font-bold text-xl md:text-2xl text-white">Persistent Workspace Home</h3>
          </div>

          <p className="text-base md:text-lg text-slate-100 font-medium leading-relaxed">
            The agent maintains continuous state across sessions by reading from and writing to your dedicated <code className="bg-slate-900 px-2 py-1 rounded text-amber-300 font-mono text-base">/Spark_OS/</code> folder inside Google Drive.
          </p>

          <div className="p-4 rounded-xl bg-slate-900/90 border border-amber-500/40 space-y-2 text-sm md:text-base">
            <span className="font-bold text-amber-400 block uppercase tracking-wider">HANDS-ON LAB REQUIREMENT:</span>
            <p className="text-slate-200 font-medium">
              Students will set up this exact directory structure in Google Drive during Week 1 assignment.
            </p>
          </div>
        </motion.div>
      </div>

      <div className="text-xs text-slate-500 font-mono">
        Slide #{slideData.num} • High Visibility Directory Architecture
      </div>
    </div>
  );
}
