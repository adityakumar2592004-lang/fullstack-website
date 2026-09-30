import { useState, useEffect, useCallback } from 'react';
import type { ProblemStatus, UserNote } from '../types';

const STORAGE_KEYS = {
  SOLVED: 'dsa_solved_problems',
  ATTEMPTED: 'dsa_attempted_problems',
  BOOKMARKED: 'dsa_bookmarked_problems',
  NOTES: 'dsa_user_notes',
  RECENT: 'dsa_recent_problems',
};

export function useProgress() {
  const [solved, setSolved] = useState<string[]>(() => {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.SOLVED);
      return data ? JSON.parse(data) : [];
    } catch {
      return [];
    }
  });

  const [attempted, setAttempted] = useState<string[]>(() => {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.ATTEMPTED);
      return data ? JSON.parse(data) : [];
    } catch {
      return [];
    }
  });

  const [bookmarked, setBookmarked] = useState<string[]>(() => {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.BOOKMARKED);
      return data ? JSON.parse(data) : [];
    } catch {
      return [];
    }
  });

  const [notes, setNotes] = useState<Record<string, UserNote>>(() => {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.NOTES);
      return data ? JSON.parse(data) : {};
    } catch {
      return {};
    }
  });

  const [recent, setRecent] = useState<string[]>(() => {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.RECENT);
      return data ? JSON.parse(data) : [];
    } catch {
      return [];
    }
  });

  // Sync to localStorage
  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEYS.SOLVED, JSON.stringify(solved));
    } catch (e) {
      console.error(e);
    }
  }, [solved]);

  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEYS.ATTEMPTED, JSON.stringify(attempted));
    } catch (e) {
      console.error(e);
    }
  }, [attempted]);

  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEYS.BOOKMARKED, JSON.stringify(bookmarked));
    } catch (e) {
      console.error(e);
    }
  }, [bookmarked]);

  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEYS.NOTES, JSON.stringify(notes));
    } catch (e) {
      console.error(e);
    }
  }, [notes]);

  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEYS.RECENT, JSON.stringify(recent));
    } catch (e) {
      console.error(e);
    }
  }, [recent]);

  const markSolved = useCallback((problemId: string) => {
    setSolved((prev) => (prev.includes(problemId) ? prev : [...prev, problemId]));
    setAttempted((prev) => prev.filter((id) => id !== problemId));
  }, []);

  const markAttempted = useCallback((problemId: string) => {
    setSolved((prev) => {
      if (prev.includes(problemId)) return prev;
      setAttempted((att) => (att.includes(problemId) ? att : [...att, problemId]));
      return prev;
    });
  }, []);

  const toggleBookmark = useCallback((problemId: string) => {
    setBookmarked((prev) =>
      prev.includes(problemId) ? prev.filter((id) => id !== problemId) : [...prev, problemId]
    );
  }, []);

  const isBookmarked = useCallback(
    (problemId: string) => bookmarked.includes(problemId),
    [bookmarked]
  );

  const getStatus = useCallback(
    (problemId: string): ProblemStatus => {
      if (solved.includes(problemId)) return 'Solved';
      if (attempted.includes(problemId)) return 'Attempted';
      return 'Not Started';
    },
    [solved, attempted]
  );

  const saveNote = useCallback(
    (problemId: string, problemTitle: string, content: string) => {
      setNotes((prev) => ({
        ...prev,
        [problemId]: {
          problemId,
          problemTitle,
          content,
          updatedAt: new Date().toISOString(),
        },
      }));
    },
    []
  );

  const getNote = useCallback(
    (problemId: string): string => {
      return notes[problemId]?.content || '';
    },
    [notes]
  );

  const recordVisit = useCallback((problemId: string) => {
    setRecent((prev) => {
      const filtered = prev.filter((id) => id !== problemId);
      return [problemId, ...filtered].slice(0, 10);
    });
  }, []);

  return {
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
  };
}
