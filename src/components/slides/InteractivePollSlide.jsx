import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Vote, CheckCircle2, Award } from 'lucide-react';

export default function InteractivePollSlide({ slideData }) {
  const [options, setOptions] = useState(slideData.options || []);
  const [votedOption, setVotedOption] = useState(null);

  const handleVote = (idx) => {
    if (votedOption === idx) return;
    const newOptions = [...options];
    newOptions[idx].votes += 1;
    setOptions(newOptions);
    setVotedOption(idx);
  };

  const totalVotes = options.reduce((sum, opt) => sum + opt.votes, 0);

  return (
    <div className="h-full flex flex-col justify-between p-6 md:p-10 relative">
      {/* Header */}
      <div>
        <div className="flex items-center gap-2 text-amber-400 font-mono text-xs font-bold tracking-widest uppercase">
          <Vote className="w-4 h-4 text-amber-400" />
          <span>{slideData.title}</span>
        </div>
        <h2 className="text-xl md:text-3xl font-black text-white mt-1">
          {slideData.subtitle}
        </h2>
      </div>

      {/* Interactive Poll Area */}
      <div className="my-auto grid grid-cols-1 md:grid-cols-12 gap-6 items-center">
        {/* Options Click List */}
        <div className="md:col-span-7 space-y-3">
          <span className="text-xs text-cyan-400 font-mono font-bold block mb-1">
            CLICK AN OPTION TO VOTE IN REAL TIME:
          </span>
          {options.map((opt, idx) => {
            const isSelected = votedOption === idx;
            const percentage = totalVotes > 0 ? Math.round((opt.votes / totalVotes) * 100) : 0;

            return (
              <motion.button
                key={idx}
                onClick={() => handleVote(idx)}
                whileHover={{ scale: 1.01 }}
                whileTap={{ scale: 0.99 }}
                className={`w-full p-4 rounded-xl border text-left flex items-center justify-between transition relative overflow-hidden ${
                  isSelected 
                    ? "bg-cyan-500/20 border-cyan-400 shadow-lg shadow-cyan-500/30" 
                    : "glass-card hover:border-slate-500"
                }`}
              >
                {/* Background Progress Bar */}
                <div 
                  className="absolute inset-y-0 left-0 bg-cyan-500/10 transition-all duration-500 pointer-events-none" 
                  style={{ width: `${percentage}%` }}
                />

                <div className="flex items-center gap-3 relative z-10">
                  <span className={`px-2.5 py-1 rounded font-mono text-xs font-bold ${
                    isSelected ? "bg-cyan-400 text-slate-950" : "bg-slate-800 text-slate-300"
                  }`}>
                    {opt.label}
                  </span>
                  <span className="text-sm font-semibold text-white">
                    {opt.text}
                  </span>
                </div>

                <div className="flex items-center gap-2 relative z-10">
                  <span className="text-xs font-mono font-bold text-cyan-300">
                    {percentage}% ({opt.votes})
                  </span>
                  {isSelected && <CheckCircle2 className="w-4 h-4 text-cyan-400" />}
                </div>
              </motion.button>
            );
          })}
        </div>

        {/* Live Vote Result Card */}
        <div className="md:col-span-5 glass-card-gold p-6 flex flex-col justify-between h-full space-y-4">
          <div>
            <div className="flex items-center justify-between">
              <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 uppercase tracking-widest font-mono">
                LIVE AUDIENCE RESPONSE
              </span>
              <span className="text-xs font-mono text-slate-400">Total: {totalVotes} votes</span>
            </div>
            <h3 className="text-lg font-bold text-white mt-2">
              Reclaiming Time = Reclaiming Humanity
            </h3>
          </div>

          <p className="text-xs text-slate-200 leading-relaxed">
            When routine chores are automated, students invest their reclaimed energy into family, deep academic study, and spiritual growth. Automation serves human fulfillment!
          </p>

          <div className="p-3 rounded-lg bg-slate-900/80 border border-amber-500/30 flex items-center gap-2.5">
            <Award className="w-5 h-5 text-amber-400 shrink-0" />
            <span className="text-xs text-amber-200 font-medium">
              Soli Deo Gloria Mandate: Elevating intellect above repetitive labor.
            </span>
          </div>
        </div>
      </div>

      <div className="text-xs text-slate-500 font-mono">
        Slide #{slideData.num} • Interactive Student Poll Simulator
      </div>
    </div>
  );
}
