import React from 'react';
import {
  LayoutDashboard,
  Map,
  Code2,
  Bookmark,
  Repeat,
  FileEdit,
  ChevronRight,
  Sparkles,
  BookOpen,
} from 'lucide-react';
import { ROADMAP_MODULES } from '../../data/modules';

interface SidebarProps {
  activePage: string;
  onNavigate: (page: string, params?: any) => void;
  isOpen: boolean;
  onClose: () => void;
}

export const Sidebar: React.FC<SidebarProps> = ({
  activePage,
  onNavigate,
  isOpen,
  onClose,
}) => {
  const navItems = [
    { id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard },
    { id: 'roadmap', label: 'Roadmap', icon: Map },
    { id: 'problems', label: 'All Problems', icon: Code2 },
    { id: 'bookmarks', label: 'Bookmarks', icon: Bookmark },
    { id: 'revision', label: 'Revision Mode', icon: Repeat },
    { id: 'notes', label: 'Notes', icon: FileEdit },
  ];

  return (
    <>
      {/* Mobile backdrop */}
      {isOpen && (
        <div
          className="fixed inset-0 z-40 bg-black/60 backdrop-blur-xs md:hidden"
          onClick={onClose}
        />
      )}

      <aside
        className={`fixed md:sticky top-16 z-40 w-64 h-[calc(100vh-4rem)] bg-slate-900/95 md:bg-slate-900/60 border-r border-slate-800 flex flex-col transition-transform duration-300 ease-in-out ${
          isOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'
        }`}
      >
        <div className="p-4 flex-1 overflow-y-auto space-y-6 custom-scrollbar">
          {/* Main Navigation */}
          <div>
            <div className="text-[11px] uppercase tracking-wider font-semibold text-slate-400 px-3 mb-2">
              Platform Navigation
            </div>
            <nav className="space-y-1">
              {navItems.map((item) => {
                const Icon = item.icon;
                const isActive = activePage === item.id;
                return (
                  <button
                    key={item.id}
                    onClick={() => {
                      onNavigate(item.id);
                      onClose();
                    }}
                    className={`w-full flex items-center justify-between px-3 py-2.5 rounded-xl text-sm font-medium transition-all ${
                      isActive
                        ? 'bg-blue-600 text-white shadow-md shadow-blue-600/20'
                        : 'text-slate-300 hover:text-white hover:bg-slate-800/80'
                    }`}
                  >
                    <span className="flex items-center gap-3">
                      <Icon className={`w-4 h-4 ${isActive ? 'text-white' : 'text-slate-400'}`} />
                      {item.label}
                    </span>
                    {item.id === 'revision' && (
                      <span className="flex items-center text-[10px] px-1.5 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 font-semibold border border-indigo-500/30">
                        <Sparkles className="w-2.5 h-2.5 mr-0.5" /> Fast
                      </span>
                    )}
                  </button>
                );
              })}
            </nav>
          </div>

          {/* Core Roadmap Modules 1-5 */}
          <div>
            <div className="text-[11px] uppercase tracking-wider font-semibold text-slate-400 px-3 mb-2 flex items-center justify-between">
              <span>Active Modules</span>
              <span className="text-[10px] text-blue-400 font-bold bg-blue-500/10 px-1.5 py-0.5 rounded">1–5</span>
            </div>
            <div className="space-y-1">
              {ROADMAP_MODULES.slice(0, 5).map((mod) => (
                <button
                  key={mod.id}
                  onClick={() => {
                    onNavigate('module-detail', { moduleId: mod.id });
                    onClose();
                  }}
                  className="w-full flex items-center justify-between px-3 py-2 rounded-lg text-xs font-medium text-slate-300 hover:text-white hover:bg-slate-800 transition-colors text-left group"
                >
                  <span className="flex items-center gap-2 truncate">
                    <span className="w-5 h-5 rounded bg-slate-800 border border-slate-700 flex items-center justify-center text-[11px] font-mono text-slate-400 group-hover:text-blue-400 group-hover:border-blue-500/30">
                      {mod.id}
                    </span>
                    <span className="truncate">{mod.title}</span>
                  </span>
                  <ChevronRight className="w-3.5 h-3.5 text-slate-600 group-hover:text-slate-300 shrink-0" />
                </button>
              ))}
            </div>
          </div>

          {/* Modules 6-20 Preview */}
          <div className="pt-2 border-t border-slate-800/80">
            <div className="text-[11px] uppercase tracking-wider font-semibold text-slate-500 px-3 mb-2 flex items-center justify-between">
              <span>Advanced Modules</span>
              <span className="text-[10px] text-slate-500">6–20</span>
            </div>
            <button
              onClick={() => {
                onNavigate('roadmap');
                onClose();
              }}
              className="w-full px-3 py-2 rounded-lg bg-slate-950/40 border border-slate-800 hover:border-slate-700 text-slate-400 hover:text-slate-200 text-xs flex items-center gap-2 transition-all"
            >
              <BookOpen className="w-3.5 h-3.5 text-slate-500" />
              <span>Browse Full 20-Step Roadmap</span>
            </button>
          </div>
        </div>

        {/* Sidebar Footer */}
        <div className="p-4 border-t border-slate-800 text-[11px] text-slate-500 flex items-center justify-between bg-slate-950/40">
          <span>Striver A2Z Platform</span>
          <span className="text-emerald-500 flex items-center gap-1 font-mono">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
            Backend Active
          </span>
        </div>
      </aside>
    </>
  );
};
