import React, { useState, useMemo } from 'react';
import type { Problem, ProblemStatus } from '../types';
import { ProblemCard } from '../components/problem/ProblemCard';
import { FilterBar } from '../components/problem/FilterBar';
import { Code2 } from 'lucide-react';

interface ProblemsPageProps {
  problems: Problem[];
  solved: string[];
  attempted: string[];
  bookmarked: string[];
  getStatus: (id: string) => ProblemStatus;
  onToggleBookmark: (id: string) => void;
  onSelectProblem: (id: string) => void;
}

export const ProblemsPage: React.FC<ProblemsPageProps> = ({
  problems,
  solved,
  attempted,
  bookmarked,
  getStatus,
  onToggleBookmark,
  onSelectProblem,
}) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedDifficulty, setSelectedDifficulty] = useState('All');
  const [selectedStatus, setSelectedStatus] = useState('All');
  const [selectedTopic, setSelectedTopic] = useState('All');
  const [sortBy, setSortBy] = useState('order');

  // Collect distinct topics from problems
  const topicsList = useMemo(() => {
    const set = new Set<string>();
    problems.forEach((p) => {
      if (p.subtopic) set.add(p.subtopic);
    });
    return Array.from(set).sort();
  }, [problems]);

  const filteredProblems = useMemo(() => {
    return problems
      .filter((p) => {
        // Search
        if (searchQuery.trim()) {
          const q = searchQuery.toLowerCase().trim();
          const matchTitle = p.title.toLowerCase().includes(q);
          const matchTopic = p.subtopic.toLowerCase().includes(q);
          const matchTags = p.tags?.some((t: string) => t.toLowerCase().includes(q));
          if (!matchTitle && !matchTopic && !matchTags) return false;
        }

        // Difficulty
        if (selectedDifficulty !== 'All' && p.difficulty !== selectedDifficulty) {
          return false;
        }

        // Status
        if (selectedStatus !== 'All') {
          const status = getStatus(p.id);
          if (status !== selectedStatus) return false;
        }

        // Topic
        if (selectedTopic !== 'All' && p.subtopic !== selectedTopic) {
          return false;
        }

        return true;
      })
      .sort((a, b) => {
        if (sortBy === 'order') return a.order - b.order;
        if (sortBy === 'title') return a.title.localeCompare(b.title);
        if (sortBy === 'difficulty') {
          const orderMap: Record<string, number> = { Easy: 1, Medium: 2, Hard: 3 };
          return (orderMap[a.difficulty] || 0) - (orderMap[b.difficulty] || 0);
        }
        if (sortBy === 'status') {
          const statusOrder: Record<ProblemStatus, number> = {
            Solved: 1,
            Attempted: 2,
            'Not Started': 3,
          };
          return statusOrder[getStatus(a.id)] - statusOrder[getStatus(b.id)];
        }
        return 0;
      });
  }, [
    problems,
    searchQuery,
    selectedDifficulty,
    selectedStatus,
    selectedTopic,
    sortBy,
    getStatus,
  ]);

  const handleResetFilters = () => {
    setSearchQuery('');
    setSelectedDifficulty('All');
    setSelectedStatus('All');
    setSelectedTopic('All');
    setSortBy('order');
  };

  return (
    <div className="space-y-6 pb-12">
      {/* Header */}
      <div>
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-semibold uppercase tracking-wider mb-2">
          <Code2 className="w-3.5 h-3.5" /> Problem Directory
        </div>
        <h1 className="text-3xl font-extrabold text-white tracking-tight">
          DSA Practice Problems
        </h1>
        <p className="text-sm text-slate-400 mt-1">
          Explore all {problems.length} curated problems across Beginner Problems, Sorting, Arrays, Hashing, and Binary Search &bull; {solved.length} Solved &bull; {attempted.length} In Progress.
        </p>
      </div>

      {/* Filter Bar */}
      <FilterBar
        searchQuery={searchQuery}
        onSearchChange={setSearchQuery}
        selectedDifficulty={selectedDifficulty}
        onDifficultyChange={setSelectedDifficulty}
        selectedStatus={selectedStatus}
        onStatusChange={setSelectedStatus}
        selectedTopic={selectedTopic}
        onTopicChange={setSelectedTopic}
        topicsList={topicsList}
        sortBy={sortBy}
        onSortByChange={setSortBy}
        onResetFilters={handleResetFilters}
        totalFiltered={filteredProblems.length}
      />

      {/* Problem Cards List */}
      {filteredProblems.length === 0 ? (
        <div className="p-12 text-center rounded-2xl bg-slate-900/40 border border-slate-800 space-y-3">
          <Code2 className="w-10 h-10 text-slate-600 mx-auto" />
          <h3 className="text-base font-semibold text-slate-300">No problems match your filters</h3>
          <p className="text-xs text-slate-500">
            Try resetting your difficulty, search term, or status filters to view problems.
          </p>
          <button
            onClick={handleResetFilters}
            className="px-4 py-2 text-xs font-semibold text-blue-400 hover:text-white bg-slate-800 hover:bg-slate-700 rounded-xl transition-colors"
          >
            Clear All Filters
          </button>
        </div>
      ) : (
        <div className="grid grid-cols-1 gap-3">
          {filteredProblems.map((prob) => (
            <ProblemCard
              key={prob.id}
              problem={prob}
              status={getStatus(prob.id)}
              isBookmarked={bookmarked.includes(prob.id)}
              onToggleBookmark={() => onToggleBookmark(prob.id)}
              onSelect={() => onSelectProblem(prob.id)}
            />
          ))}
        </div>
      )}
    </div>
  );
};
