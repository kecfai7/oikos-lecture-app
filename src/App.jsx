import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import SlideDeck from './components/SlideDeck';
import PresenterMode from './components/PresenterMode';
import SlideOverviewModal from './components/SlideOverviewModal';
import PrintSlidesView from './components/PrintSlidesView';
import { SLIDES_SESSION_1, SLIDES_SESSION_2, SLIDES_SESSION_3, SLIDES_SESSION_4, SLIDES_SESSION_5, SLIDES_SESSION_6, SLIDES_SESSION_7, SLIDES_SESSION_8, SLIDES_SESSION_9, SLIDES_SESSION_10, SLIDES_SESSION_11, SLIDES_SESSION_12, SLIDES_SESSION_13, SLIDES_SESSION_14, SLIDES_SESSION_15 } from './data/slidesData';
import { Keyboard } from 'lucide-react';

export default function App() {
  const [selectedSession, setSelectedSession] = useState(15);
  const [currentSlideIndex, setCurrentSlideIndex] = useState(0);
  const [isPresenterOpen, setIsPresenterOpen] = useState(false);
  const [isOverviewOpen, setIsOverviewOpen] = useState(false);
  const [showShortcutHint, setShowShortcutHint] = useState(true);
  const [isPrinting, setIsPrinting] = useState(false);

  const currentSlides = 
    selectedSession === 1 ? SLIDES_SESSION_1 : 
    selectedSession === 2 ? SLIDES_SESSION_2 : 
    selectedSession === 3 ? SLIDES_SESSION_3 : 
    selectedSession === 4 ? SLIDES_SESSION_4 : 
    selectedSession === 5 ? SLIDES_SESSION_5 : 
    selectedSession === 6 ? SLIDES_SESSION_6 : 
    selectedSession === 7 ? SLIDES_SESSION_7 : 
    selectedSession === 8 ? SLIDES_SESSION_8 : 
    selectedSession === 9 ? SLIDES_SESSION_9 : 
    selectedSession === 10 ? SLIDES_SESSION_10 : 
    selectedSession === 11 ? SLIDES_SESSION_11 : 
    selectedSession === 12 ? SLIDES_SESSION_12 : 
    selectedSession === 13 ? SLIDES_SESSION_13 : 
    selectedSession === 14 ? SLIDES_SESSION_14 : 
    (SLIDES_SESSION_15 || SLIDES_SESSION_1);













  const totalSlides = currentSlides.length;
  const currentSlideData = currentSlides[currentSlideIndex] || currentSlides[0];
  const nextSlideData = currentSlideIndex < totalSlides - 1 ? currentSlides[currentSlideIndex + 1] : null;

  const handleSelectSession = (sessionId) => {
    setSelectedSession(sessionId);
    setCurrentSlideIndex(0);
  };

  // BroadcastChannel for Dual-Monitor Multi-Window Sync
  useEffect(() => {
    const channel = new BroadcastChannel('oikos_slide_sync');
    channel.onmessage = (event) => {
      if (typeof event.data?.slideIndex === 'number') {
        setCurrentSlideIndex(event.data.slideIndex);
      }
    };
    return () => channel.close();
  }, []);

  const broadcastSlideChange = (newIndex) => {
    setCurrentSlideIndex(newIndex);
    try {
      const channel = new BroadcastChannel('oikos_slide_sync');
      channel.postMessage({ slideIndex: newIndex });
      channel.close();
    } catch (e) {
      console.log('BroadcastChannel error:', e);
    }
  };

  const handlePrev = () => {
    if (currentSlideIndex > 0) {
      broadcastSlideChange(currentSlideIndex - 1);
    }
  };

  const handleNext = () => {
    if (currentSlideIndex < totalSlides - 1) {
      broadcastSlideChange(currentSlideIndex + 1);
    }
  };

  const handleSelectSlide = (num) => {
    broadcastSlideChange(num - 1);
  };

  const handleExportPDF = () => {
    setIsPrinting(true);
    setTimeout(() => {
      window.print();
      // Keep isPrinting true briefly during print dialog
      setTimeout(() => setIsPrinting(false), 2000);
    }, 800);
  };

  // Keyboard Shortcuts Listener
  useEffect(() => {
    const handleKeyDown = (e) => {
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

  useEffect(() => {
    const timer = setTimeout(() => setShowShortcutHint(false), 8000);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="w-screen h-screen flex flex-col bg-[#0B132B] text-white overflow-hidden font-sans select-text">
      {/* Printable All 40 Slides View (Rendered only during PDF Export / Print) */}
      {isPrinting && <PrintSlidesView slides={currentSlides} />}

      {/* Header Bar */}
      <Header
        currentSlide={currentSlideIndex + 1}
        totalSlides={totalSlides}
        onPrev={handlePrev}
        onNext={handleNext}
        onTogglePresenter={() => setIsPresenterOpen(prev => !prev)}
        isPresenterOpen={isPresenterOpen}
        onToggleOverview={() => setIsOverviewOpen(prev => !prev)}
        onExportPDF={handleExportPDF}
        selectedSession={selectedSession}
        onSelectSession={handleSelectSession}
      />

      {/* Main Slide Presentation Area */}
      <main className="no-print flex-1 relative overflow-hidden">
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
        <div className="no-print fixed bottom-4 left-4 bg-slate-900/90 border border-cyan-500/30 text-xs text-slate-300 px-3 py-2 rounded-xl backdrop-blur-md shadow-lg flex items-center gap-2 z-20">
          <Keyboard className="w-4 h-4 text-cyan-400" />
          <span>Use <b>← →</b> arrows for slides | <b>P</b> for Presenter Script | <b>Export PDF</b> to save slides</span>
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
          slides={currentSlides}
          currentSlide={currentSlideIndex + 1}
          onSelectSlide={handleSelectSlide}
          onClose={() => setIsOverviewOpen(false)}
        />
      )}
    </div>
  );
}

