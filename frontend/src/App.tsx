import React, { useState, useEffect } from 'react';
import type { Problem } from './types';
import { INITIAL_PROBLEMS } from './data/problems';
import { fetchProblems } from './services/api';
import { useProgress } from './hooks/useProgress';

import { Navbar } from './components/layout/Navbar';
import { Sidebar } from './components/layout/Sidebar';
import { Breadcrumbs } from './components/layout/Breadcrumbs';
import { GlobalSearchModal } from './components/search/GlobalSearchModal';

import { DashboardPage } from './pages/DashboardPage';
import { RoadmapPage } from './pages/RoadmapPage';
import { ModuleDetailPage } from './pages/ModuleDetailPage';
import { ProblemsPage } from './pages/ProblemsPage';
import { ProblemSolvePage } from './pages/ProblemSolvePage';
import { BookmarksPage } from './pages/BookmarksPage';
import { RevisionPage } from './pages/RevisionPage';
import { NotesPage } from './pages/NotesPage';

export const App: React.FC = () => {
  const [problems, setProblems] = useState<Problem[]>(INITIAL_PROBLEMS);
  const [activePage, setActivePage] = useState<string>('dashboard');
  const [selectedProblemId, setSelectedProblemId] = useState<string | null>(null);
  const [selectedModuleId, setSelectedModuleId] = useState<number>(1);
  const [isSearchOpen, setIsSearchOpen] = useState<boolean>(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState<boolean>(false);

  const {
    solved,
    attempted,
    bookmarked,
    notes,
    recent,
    markSolved,
    markAttempted,
    toggleBookmark,
    isBookmarked,
    getStatus,
    saveNote,
    getNote,
    recordVisit,
  } = useProgress();

  // Try fetching fresh problems from FastAPI backend on mount
  useEffect(() => {
    fetchProblems()
      .then((data) => {
        if (data && data.length > 0) {
          setProblems(data);
        }
      })
      .catch((err) => {
        console.warn('Backend /api/problems fetch failed, using local offline dataset:', err);
      });
  }, []);

  const handleNavigate = (page: string, params?: { moduleId?: number }) => {
    setActivePage(page);
    if (params?.moduleId) {
      setSelectedModuleId(params.moduleId);
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleSelectProblem = (problemId: string) => {
    setSelectedProblemId(problemId);
    recordVisit(problemId);
    setActivePage('problem-solve');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const currentProblem =
    problems.find((p) => p.id === selectedProblemId) || problems[0];

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-sans selection:bg-blue-500/30 selection:text-blue-200">
      {/* Top Navbar */}
      <Navbar
        onOpenSearch={() => setIsSearchOpen(true)}
        solvedCount={solved.length}
        totalCount={problems.length}
        bookmarkedCount={bookmarked.length}
        activePage={activePage}
        onNavigate={handleNavigate}
        isMobileMenuOpen={isMobileMenuOpen}
        setIsMobileMenuOpen={setIsMobileMenuOpen}
      />

      {/* Main Container with Sidebar + Page Content */}
      <div className="flex-1 flex max-w-7xl w-full mx-auto">
        <Sidebar
          activePage={activePage}
          onNavigate={handleNavigate}
          isOpen={isMobileMenuOpen}
          onClose={() => setIsMobileMenuOpen(false)}
        />

        {/* Content Area */}
        <main className="flex-1 min-w-0 p-4 sm:p-6 lg:p-8">
          {/* Breadcrumbs for problem solve page */}
          {activePage === 'problem-solve' && currentProblem && (
            <div className="mb-4">
              <Breadcrumbs
                items={[
                  { label: 'Roadmap', onClick: () => handleNavigate('roadmap') },
                  {
                    label: currentProblem.step_title,
                    onClick: () => handleNavigate('module-detail', { moduleId: currentProblem.step_id }),
                  },
                  { label: currentProblem.title },
                ]}
              />
            </div>
          )}

          {/* Active Page Routing */}
          {activePage === 'dashboard' && (
            <DashboardPage
              problems={problems}
              solved={solved}
              attempted={attempted}
              bookmarked={bookmarked}
              recent={recent}
              onNavigate={handleNavigate}
              onSelectProblem={handleSelectProblem}
            />
          )}

          {activePage === 'roadmap' && (
            <RoadmapPage
              problems={problems}
              solved={solved}
              onNavigate={handleNavigate}
            />
          )}

          {activePage === 'module-detail' && (
            <ModuleDetailPage
              moduleId={selectedModuleId}
              problems={problems}
              solved={solved}
              bookmarked={bookmarked}
              getStatus={getStatus}
              onToggleBookmark={toggleBookmark}
              onSelectProblem={handleSelectProblem}
              onNavigate={handleNavigate}
            />
          )}

          {activePage === 'problems' && (
            <ProblemsPage
              problems={problems}
              solved={solved}
              attempted={attempted}
              bookmarked={bookmarked}
              getStatus={getStatus}
              onToggleBookmark={toggleBookmark}
              onSelectProblem={handleSelectProblem}
            />
          )}

          {activePage === 'problem-solve' && currentProblem && (
            <ProblemSolvePage
              problem={currentProblem}
              allProblems={problems}
              status={getStatus(currentProblem.id)}
              isBookmarked={isBookmarked(currentProblem.id)}
              onToggleBookmark={() => toggleBookmark(currentProblem.id)}
              onMarkSolved={markSolved}
              onMarkAttempted={markAttempted}
              userNote={getNote(currentProblem.id)}
              onSaveNote={saveNote}
              onSelectProblem={handleSelectProblem}
              onNavigate={handleNavigate}
            />
          )}

          {activePage === 'bookmarks' && (
            <BookmarksPage
              problems={problems}
              bookmarked={bookmarked}
              getStatus={getStatus}
              onToggleBookmark={toggleBookmark}
              onSelectProblem={handleSelectProblem}
              onNavigate={handleNavigate}
            />
          )}

          {activePage === 'revision' && (
            <RevisionPage
              problems={problems}
              solved={solved}
              attempted={attempted}
              bookmarked={bookmarked}
              getStatus={getStatus}
              onToggleBookmark={toggleBookmark}
              onSelectProblem={handleSelectProblem}
              onNavigate={handleNavigate}
            />
          )}

          {activePage === 'notes' && (
            <NotesPage
              notes={notes}
              onSelectProblem={handleSelectProblem}
              onNavigate={handleNavigate}
            />
          )}
        </main>
      </div>

      {/* Global Search Modal */}
      <GlobalSearchModal
        isOpen={isSearchOpen}
        onClose={() => setIsSearchOpen(false)}
        problems={problems}
        onSelectProblem={handleSelectProblem}
      />
    </div>
  );
};

export default App;
