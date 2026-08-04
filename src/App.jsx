import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import SlideDeck from './components/SlideDeck';
import PresenterMode from './components/PresenterMode';
import SlideOverviewModal from './components/SlideOverviewModal';
import { SLIDES_SESSION_1 } from './data/slidesData';
import { Info, Keyboard } from 'lucide-react';

export default function App() {
  const [selectedSession, setSelectedSession] = useState(1);
  const [currentSlideIndex, setCurrentSlideIndex] = useState(0);
  const [isPresenterOpen, setIsPresenterOpen] = useState(false);
  const [isOverviewOpen, setIsOverviewOpen] = useState(false);
  const [showShortcutHint, setShowShortcutHint] = useState(true);

  const totalSlides = SLIDES_SESSION_1.length;
  const currentSlideData = SLIDES_SESSION_1[currentSlideIndex];
  const nextSlideData = currentSlideIndex < totalSlides - 1 ? SLIDES_SESSION_1[currentSlideIndex + 1] : null;

  const handlePrev = () => {
    if (currentSlideIndex > 0) {
      setCurrentSlideIndex(i => i - 1);
    }
  };

  const handleNext = () => {
    if (currentSlideIndex < totalSlides - 1) {
      setCurrentSlideIndex(i => i + 1);
    }
  };

  const handleSelectSlide = (num) => {
    setCurrentSlideIndex(num - 1);
  };

  // Keyboard Shortcuts Listener
  useEffect(() => {
    const handleKeyDown = (e) => {
      // Avoid shortcuts if typing in input fields
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName)) return;

      if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') {
        e.preventDefault();
        handleNext();
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        e.preventDefault();
        handlePrev();
      } else if (e.key.toLowerCase() === 'p') {
        e.preventDefault();
        setIsPresenterOpen(prev => !prev);
      } else if (e.key.toLowerCase() === 'm') {
        e.preventDefault();
        setIsOverviewOpen(prev => !prev);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [currentSlideIndex, totalSlides]);

  // Hide shortcut hint after 8 seconds
  useEffect(() => {
    const timer = setTimeout(() => setShowShortcutHint(false), 8000);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="w-screen h-screen flex flex-col bg-[#0B132B] text-white overflow-hidden font-sans select-none">
      {/* Header Bar */}
      <Header
        currentSlide={currentSlideIndex + 1}
        totalSlides={totalSlides}
        onPrev={handlePrev}
        onNext={handleNext}
        onTogglePresenter={() => setIsPresenterOpen(prev => !prev)}
        isPresenterOpen={isPresenterOpen}
        onToggleOverview={() => setIsOverviewOpen(prev => !prev)}
        selectedSession={selectedSession}
        onSelectSession={setSelectedSession}
      />

      {/* Main Slide Presentation Area */}
      <main className="flex-1 relative overflow-hidden">
        <SlideDeck slideData={currentSlideData} />

        {/* Presenter Teleprompter Sidebar Mode */}
        {isPresenterOpen && (
          <PresenterMode
            slideData={currentSlideData}
            nextSlideData={nextSlideData}
            currentSlide={currentSlideIndex + 1}
            totalSlides={totalSlides}
            onPrev={handlePrev}
            onNext={handleNext}
            onClose={() => setIsPresenterOpen(false)}
          />
        )}
      </main>

      {/* Keyboard Shortcut Hint Toast */}
      {showShortcutHint && (
        <div className="fixed bottom-4 left-4 bg-slate-900/90 border border-cyan-500/30 text-xs text-slate-300 px-3 py-2 rounded-xl backdrop-blur-md shadow-lg flex items-center gap-2 z-20">
          <Keyboard className="w-4 h-4 text-cyan-400" />
          <span>Use <b>← →</b> arrows for slides | <b>P</b> for Presenter Script | <b>M</b> for Overview</span>
          <button 
            onClick={() => setShowShortcutHint(false)}
            className="text-slate-500 hover:text-white ml-1 font-bold"
          >
            ×
          </button>
        </div>
      )}

      {/* 40-Slide Grid Overview Modal */}
      {isOverviewOpen && (
        <SlideOverviewModal
          slides={SLIDES_SESSION_1}
          currentSlide={currentSlideIndex + 1}
          onSelectSlide={handleSelectSlide}
          onClose={() => setIsOverviewOpen(false)}
        />
      )}
    </div>
  );
}
