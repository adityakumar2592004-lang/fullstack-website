import React from 'react';
import { Search, Terminal, Bookmark, Award, Menu, X } from 'lucide-react';

interface NavbarProps {
  onOpenSearch: () => void;
  solvedCount: number;
  totalCount: number;
  bookmarkedCount: number;
  activePage: string;
  onNavigate: (page: string) => void;
  isMobileMenuOpen: boolean;
  setIsMobileMenuOpen: (open: boolean) => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  onOpenSearch,
  solvedCount,
  totalCount,
  bookmarkedCount,
  activePage,
  onNavigate,
  isMobileMenuOpen,
  setIsMobileMenuOpen,
}) => {
  const percentage = totalCount > 0 ? Math.round((solvedCount / totalCount) * 100) : 0;

  return (
    <header className="sticky top-0 z-30 bg-slate-900/90 backdrop-blur-md border-b border-slate-800 text-slate-100">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
        {/* Left: Branding */}
        <div className="flex items-center gap-3">
          <button
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
            className="md:hidden p-2 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800"
            aria-label="Toggle navigation"
          >
            {isMobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>

          <button
            onClick={() => onNavigate('dashboard')}
            className="flex items-center gap-2.5 text-left group focus:outline-none"
          >
            <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-blue-600 via-indigo-600 to-cyan-400 flex items-center justify-center shadow-lg shadow-blue-500/20 group-hover:scale-105 transition-transform">
              <Terminal className="w-5 h-5 text-white" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-bold text-lg tracking-tight bg-gradient-to-r from-white via-slate-100 to-slate-300 bg-clip-text text-transparent">
                  DSA Roadmap
                </span>
                <span className="text-[10px] uppercase font-semibold tracking-wider px-2 py-0.5 rounded-full bg-blue-500/10 text-blue-400 border border-blue-500/20">
                  Practice & Compiler
                </span>
              </div>
              <p className="text-xs text-slate-400 hidden sm:block">Learn. Practice. Track. Improve.</p>
            </div>
          </button>
        </div>

        {/* Center: Search Bar Trigger */}
        <div className="flex-1 max-w-md hidden md:block">
          <button
            onClick={onOpenSearch}
            className="w-full flex items-center justify-between px-3.5 py-2 text-sm text-slate-400 bg-slate-950/60 hover:bg-slate-950 border border-slate-800 hover:border-slate-700 rounded-xl transition-all shadow-inner group"
          >
            <span className="flex items-center gap-2.5">
              <Search className="w-4 h-4 text-slate-500 group-hover:text-blue-400 transition-colors" />
              <span>Search 85+ problems, topics, tags...</span>
            </span>
            <kbd className="hidden sm:inline-block px-2 py-0.5 text-[11px] font-mono font-medium text-slate-400 bg-slate-800 border border-slate-700 rounded-md">
              Ctrl + K
            </kbd>
          </button>
        </div>

        {/* Right: Quick Stats & Actions */}
        <div className="flex items-center gap-2 sm:gap-4">
          <button
            onClick={onOpenSearch}
            className="md:hidden p-2 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800"
            title="Search"
          >
            <Search className="w-5 h-5" />
          </button>

          <button
            onClick={() => onNavigate('bookmarks')}
            className={`p-2 rounded-lg flex items-center gap-1.5 text-xs font-medium border transition-colors ${
              activePage === 'bookmarks'
                ? 'bg-amber-500/10 text-amber-300 border-amber-500/30'
                : 'text-slate-400 hover:text-amber-300 hover:bg-slate-800 border-transparent'
            }`}
            title="Bookmarked Problems"
          >
            <Bookmark className="w-4 h-4" />
            <span className="hidden sm:inline">{bookmarkedCount}</span>
          </button>

          <div
            onClick={() => onNavigate('dashboard')}
            className="cursor-pointer flex items-center gap-2.5 pl-3 border-l border-slate-800"
            title="View Dashboard Progress"
          >
            <div className="w-8 h-8 rounded-lg bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 font-bold text-xs">
              <Award className="w-4 h-4" />
            </div>
            <div className="hidden lg:block text-left">
              <div className="text-xs font-semibold text-slate-200">
                {solvedCount} / {totalCount} Solved
              </div>
              <div className="w-20 bg-slate-800 h-1.5 rounded-full overflow-hidden mt-0.5">
                <div
                  className="bg-gradient-to-r from-emerald-500 to-teal-400 h-full rounded-full transition-all duration-500"
                  style={{ width: `${percentage}%` }}
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};
