import React from 'react';
import TitleSlide from './slides/TitleSlide';
import SectionSlide from './slides/SectionSlide';
import ComparisonSlide from './slides/ComparisonSlide';
import TriadSlide from './slides/TriadSlide';
import MetricSlide from './slides/MetricSlide';
import EfficiencyChartSlide from './slides/EfficiencyChartSlide';
import InteractivePollSlide from './slides/InteractivePollSlide';
import ArchitectureSlide from './slides/ArchitectureSlide';
import MottoSlide from './slides/MottoSlide';

export default function PrintSlidesView({ slides }) {
  const renderSlideContent = (slideData) => {
    switch (slideData.type) {
      case 'title':
        return <TitleSlide slideData={slideData} />;
      case 'section':
        return <SectionSlide slideData={slideData} />;
      case 'comparison':
        return <ComparisonSlide slideData={slideData} />;
      case 'triad':
        return <TriadSlide slideData={slideData} />;
      case 'metric':
        return <MetricSlide slideData={slideData} />;
      case 'chart_efficiency':
      case 'chart_case_study':
        return <EfficiencyChartSlide slideData={slideData} />;
      case 'poll':
        return <InteractivePollSlide slideData={slideData} />;
      case 'architecture':
        return <ArchitectureSlide slideData={slideData} />;
      case 'motto':
      default:
        return <MottoSlide slideData={slideData} />;
    }
  };

  return (
    <div className="print-slides-container bg-[#0B132B] text-white">
      {slides.map((s) => (
        <div key={s.num} className="print-slide-page w-[16in] h-[9in] relative overflow-hidden bg-[#0B132B] page-break">
          {renderSlideContent(s)}
        </div>
      ))}
    </div>
  );
}
