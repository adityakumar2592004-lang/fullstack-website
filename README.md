# Striver A2Z DSA Platform & Online Compiler

A comprehensive, production-grade DSA learning, roadmap, explanation, and coding practice platform equipped with an integrated Python code sandbox and test runner.

---

## 🚀 Key Highlights & Architecture

### 1. 20-Module Master Roadmap
- **Modules 1–5 Fully Implemented (85 Original Problems)**:
  - **Module 1: Beginner Problems** (15 problems: Input/Output, conditionals, loops, basic math, Armstrong numbers, prime check, GCD, patterns).
  - **Module 2: Sorting** (10 problems: Selection sort, Bubble sort, Insertion sort, Merge sort, Quick sort, 3-way partition, etc.).
  - **Module 3: Arrays** (25 problems: Two Sum, Majority Element, Kadane's Algorithm, Next Permutation, Spiral Matrix, Pascal's Triangle, 3Sum, etc.).
  - **Module 4: Hashing** (15 problems: Frequency counting, Two Sum Hash, Group Anagrams, Longest Consecutive Sequence, Subarray Sum Equals K, etc.).
  - **Module 5: Binary Search** (20 problems: Lower/Upper bound, Search in Rotated Array, Peak Element, Koko Eating Bananas, Capacity to Ship Packages, etc.).
- **Modules 6–20 Illustrated & Ready**: Displayed with curated syllabus topics and "Coming Soon" badges.

### 2. Comprehensive 9-Part Editorials
Each problem features:
- Problem statement, constraints, input/output formats, and sample test cases.
- Progressive expandable hints (Intuition, Core Invariant, Edge Cases).
- 9-part structured editorial:
  1. High-level intuition
  2. Brute force approach with complexity
  3. Better / optimal approach
  4. Step-by-step dry run trace table
  5. Time complexity analysis
  6. Space complexity analysis
  7. Common mistakes and edge case warnings
  8. Real interview follow-up questions
  9. Multi-language starter code (Python, C++, Java, JavaScript)

### 3. Integrated Online Compiler & Test Sandbox
- **Monaco Editor**: High-fidelity code editor with syntax highlighting, line numbers, and theme switching.
- **FastAPI Python Sandbox**:
  - Sample test case execution (`Run Code`) with stdout capture and timing.
  - Complete test case evaluation (`Submit Code`) including hidden test cases.
  - Strict hidden test case protection: hidden inputs, expected outputs, and actual values are securely masked on the backend before delivery to the browser.
  - Security sandbox: blocks forbidden imports (`os`, `sys`, `subprocess`, file I/O, network sockets).

### 4. Interactive Learning Utilities
- **Progress Tracking**: Tracks Solved, Attempted, and Remaining problems with interactive progress bars.
- **Personal Learning Notes**: Problem-specific note-taking journal saved to LocalStorage with full-text search.
- **Bookmarks & Revisit System**: One-click bookmarking of tricky algorithms for spaced review.
- **Active Revision Mode**: Sequential revision player organizing bookmarked, attempted, and mastered questions.
- **Global Search (`Ctrl+K`)**: Instant search across titles, subtopics, tags, and descriptions.

---

## 🛠️ Running Locally

### 1. Prerequisites
- **Python 3.10+** (with `fastapi`, `uvicorn`, `pydantic`)
- **Node.js 18+** & **npm**

### 2. Backend (FastAPI)
```bash
cd backend
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```
API Documentation will be available at `http://127.0.0.1:8000/docs`.

### 3. Frontend (Vite + React + Tailwind CSS)
```bash
cd frontend
npm install
npm run dev
```
Open **`http://localhost:5173`** in your browser. All API calls to `/api` are automatically proxied by Vite to the FastAPI backend on port 8000.

### 4. Running Verification Tests
```bash
# Run end-to-end integration tests (checks Vite proxy, code execution, hidden cases, security sandbox)
python test_e2e.py

# Run backend unit tests directly
cd backend
python test_runner_verify.py
```
