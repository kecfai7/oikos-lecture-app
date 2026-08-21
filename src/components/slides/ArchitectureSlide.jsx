import React from 'react';
import { motion } from 'framer-motion';
import { Folder, HardDrive, Shield, Terminal, Cpu, ArrowRight, CheckCircle2 } from 'lucide-react';

export default function ArchitectureSlide({ slideData }) {
  const hasLayers = Array.isArray(slideData.layers) && slideData.layers.length > 0;
  const hasTree = Array.isArray(slideData.tree) && slideData.tree.length > 0;

  return (
    <div className="h-full flex flex-col justify-between p-6 md:p-10 relative overflow-y-auto">
      {/* Header */}
      <div>
        <div className="flex items-center gap-2 text-amber-400 font-mono text-xs md:text-sm font-bold tracking-widest uppercase">
          <Terminal className="w-4 h-4 text-amber-400" />
          <span>{slideData.title}</span>
        </div>
        <h2 className="text-xl md:text-3xl font-black text-white mt-1 leading-snug">
          {slideData.subtitle}
        </h2>
      </div>

      {/* Main Architecture Content */}
      <div className="my-auto py-4">
        {hasLayers ? (
          <div className={`grid grid-cols-1 ${slideData.layers.length === 4 ? 'md:grid-cols-4' : 'md:grid-cols-3'} gap-5`}>
            {slideData.layers.map((layer, idx) => (
              <motion.div
                key={idx}
                initial={{ opacity: 0, y: 15 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: idx * 0.1 }}
                className="glass-card p-6 rounded-2xl border border-cyan-500/30 flex flex-col justify-between hover:border-cyan-400 transition-all group shadow-lg shadow-cyan-950/40 relative overflow-hidden"
              >
                <div className="absolute top-0 right-0 w-24 h-24 bg-cyan-500/5 rounded-full blur-2xl group-hover:bg-cyan-500/10 transition-all pointer-events-none" />
                
                <div>
                  <div className="flex items-center justify-between mb-4">
                    <span className="text-xs font-mono font-black text-cyan-300 bg-cyan-500/20 px-3 py-1 rounded-full border border-cyan-500/40">
                      {layer.step || `LAYER 0${idx + 1}`}
                    </span>
                    <Cpu className="w-5 h-5 text-cyan-400 group-hover:rotate-12 transition-transform" />
                  </div>
                  
                  <h3 className="text-lg md:text-xl font-black text-white group-hover:text-cyan-200 transition-colors mb-3 leading-tight">
                    {layer.name}
                  </h3>
                </div>

                <p className="text-sm md:text-base text-slate-200 font-medium leading-relaxed mt-2 pt-3 border-t border-slate-700/60">
                  {layer.role}
                </p>
              </motion.div>
            ))}
          </div>
        ) : hasTree ? (
          <div className="grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
            {/* Interactive Directory Tree */}
            <motion.div 
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              className="md:col-span-7 glass-card p-6 md:p-8 space-y-3 font-mono rounded-2xl border border-slate-700"
            >
              <div className="flex items-center justify-between border-b border-slate-700 pb-3 mb-2">
                <div className="flex items-center gap-3">
                  <HardDrive className="w-5 h-5 text-cyan-400" />
                  <span className="font-bold text-white text-base md:text-lg">Persistent File Tree</span>
                </div>
                <span className="text-xs text-cyan-300 bg-cyan-500/20 px-3 py-1 rounded-full border border-cyan-500/30 font-bold">
                  Spark OS Root
                </span>
              </div>

              {slideData.tree.map((item, idx) => (
                <motion.div 
                  key={idx}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: idx * 0.1 }}
                  className="p-3.5 rounded-xl bg-slate-900/90 border border-slate-700 flex items-center justify-between hover:border-cyan-400 transition group shadow-md"
                >
                  <div className="flex items-center gap-3">
                    <Folder className={`w-5 h-5 ${idx === 0 ? "text-amber-400" : "text-cyan-400"}`} />
                    <span className={`font-bold ${idx === 0 ? "text-amber-300 text-base md:text-lg" : "text-slate-100 text-sm md:text-base"}`}>
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
              className="md:col-span-5 glass-card-gold p-6 md:p-8 space-y-5 rounded-2xl border border-amber-500/40"
            >
              <div className="flex items-center gap-3 text-amber-300">
                <Shield className="w-6 h-6 text-amber-400" />
                <h3 className="font-bold text-lg md:text-xl text-white">Persistent Workspace Home</h3>
              </div>

              <p className="text-sm md:text-base text-slate-100 font-medium leading-relaxed">
                The agent maintains continuous state across sessions by reading from and writing to your dedicated <code className="bg-slate-900 px-2 py-1 rounded text-amber-300 font-mono text-sm">/Spark_OS/</code> environment.
              </p>

              <div className="p-4 rounded-xl bg-slate-900/90 border border-amber-500/40 space-y-2 text-xs md:text-sm">
                <span className="font-bold text-amber-400 block uppercase tracking-wider">LAB REQUIREMENT:</span>
                <p className="text-slate-200 font-medium">
                  Initialize this exact directory architecture with pre-commit hooks during your hands-on lab.
                </p>
              </div>
            </motion.div>
          </div>
        ) : null}
      </div>

      {/* Footer */}
      <div className="text-xs text-slate-500 font-mono flex items-center justify-between pt-2 border-t border-slate-800">
        <span>Slide #{slideData.num} • {slideData.type.toUpperCase()} ARCHITECTURE</span>
        <span className="text-cyan-400 font-bold">Oikos University Smart Insight Lab</span>
      </div>
    </div>
  );
}
