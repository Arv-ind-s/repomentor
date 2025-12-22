# RepoMentor: 1-Week Implementation Plan (SDLC & Testing Focused)

This document serves as the **Single Source of Truth** for the development of RepoMentor. It follows a rigorous Software Development Life Cycle (SDLC) approach, prioritizing robustness, testing, and architectural integrity.

**Progress Tracking:**
- [ ] Day 1: Requirements, Architecture & Foundation
- [ ] Day 2: Ingestion Core & Parsing Engine
- [ ] Day 3: Static Analysis & Knowledge Graph
- [ ] Day 4: LLM Intelligence Layer
- [ ] Day 5: Frontend Implementation & Integration
- [ ] Day 6: Comprehensive Testing & QA
- [ ] Day 7: Documentation, Polish & Release

---

## 📅 Daily Detailed Breakdown

### Day 1: Requirements, Architecture & Foundation
**Phase:** Planning & Design
**Focus:** Establishing a solid structural foundation to prevent technical debt.

*   **Objectives:**
    *   Finalize system architecture and data flow.
    *   Set up the development environment and CI/CD foundations.
    *   Define core data models (schema) for the application.

*   **Tasks:**
    *   [ ] **Project Scaffolding:** Initialize git, Poetry/pip, and directory structure (`/core`, `/ui`, `/tests`, `/docs`).
    *   [ ] **Architecture Design:** Create a detailed Mermaid diagram in `ARCHITECTURE.md` showing data flow between UI, Ingest, Parser, and LLM modules.
    *   [ ] **Data Modeling:** Define Pydantic models for `Repository`, `FileNode`, `FunctionNode`, `ClassNode`, and `DependencyGraph`.
    *   [ ] **Tooling Setup:** Configure `pytest` for testing, `ruff` for linting, and `pre-commit` hooks.
    *   [ ] **Tech Stack Freeze:** Confirm versions for Streamlit, GitPython, NetworkX, and **Gemini API SDK (`google-generativeai`)**.

*   **Testing Strategy:**
    *   *Verification:* Ensure development environment installs correctly on a fresh isolation (venv).
    *   *Unit:* Write initial "sanity check" tests for the project structure.

*   **Deliverables:**
    *   `ARCHITECTURE.md` (Diagrams + Text).
    *   `requirements.txt` / `pyproject.toml` (Locked versions).
    *   Initial Directory Structure.

---

### Day 2: Ingestion Core & Parsing Engine
**Phase:** Backend Development (Component Level)
**Focus:** Reliable file handling and accurate code extraction.

*   **Objectives:**
    *   Build robust `IngestService` to clone/handle git repositories securely.
    *   Build `ParserService` to extract AST data from Python files.

*   **Tasks:**
    *   [ ] **Ingestion Module:** Implement `GitIngestor` class using `GitPython`. Handle cloning to `tempfile`, standardizing paths, and cleanup (context manager).
    *   [ ] **File Walker:** Implement logic to traverse directories, respecting `.gitignore` recursively.
    *   [ ] **AST Parser:** Implement `PythonParser` using the `ast` library.
        *   Extract: Class names, Function signatures, Docstrings, Global variables, Imports.
        *   Metrics: Line counts, Cyclomatic complexity (optional).
    *   [ ] **Data Mapping:** Map raw AST data to the Pydantic models defined on Day 1.

*   **Testing Strategy (TDD Approach recommended):**
    *   *Unit (Ingestion):* Mock `git.Repo.clone_from` to test success and failure (e.g., auth error) scenarios without hitting GitHub.
    *   *Unit (Parser):* Create sample python strings/files as fixtures. Assert that `PythonParser` correctly extracts functions/classes from these fixtures.

*   **Deliverables:**
    *   `core/ingest.py` & `core/parser.py`.
    *   Passing test suite: `tests/test_ingest.py`, `tests/test_parser.py`.

---

### Day 3: Static Analysis & Knowledge Graph
**Phase:** Backend Development (Logic Level)
**Focus:** Understanding the relationships between code components.

*   **Objectives:**
    *   Build a visualizable dependency graph.
    *   Identify key modules vs. utilities.

*   **Tasks:**
    *   [ ] **Dependency Resolver:** Analyze import statements extracted by the Parser to link nodes.
        *   Resolve relative imports (`from .utils import x`) to absolute paths.
        *   Resolve 3rd party vs. local imports.
    *   [ ] **Graph Construction:** Use `NetworkX` to build a directed graph (File/Module level nodes).
    *   [ ] **Graph Metrics:** Calculate centrality to determine "important" files (for LLM context prioritization).
    *   [ ] **Visualization Data:** Export graph data to a format compatible with `streamlit-agraph` or `graphviz`.

*   **Testing Strategy:**
    *   *Unit (Graph):* Create a mock project structure with known dependencies (A imports B). Assert the graph correctly has an edge A->B.
    *   *Integration:* Feed the output of `ParserService` into `GraphService` to ensure data compatibility.

*   **Deliverables:**
    *   `core/graph.py` & `core/analysis.py`.
    *   `tests/test_graph.py`.

---

### Day 4: LLM Intelligence Layer
**Phase:** Backend Development (AI Integration)
**Focus:** Prompt Engineering and Context Management.

*   **Objectives:**
    *   Integrate LLM client (LiteLLM) for code summarization.
    *   Develop context-aware prompts.

*   **Tasks:**
    *   [ ] **LLM Service:** Integration with `google-generativeai` (Gemini API). Implement error handling for quotas/rate limits.
    *   [ ] **Prompt Templates:** Design prompts for:
        *   `File Summarization`: "Explain this code file..." (Optimize for Gemini 1.5 Flash).
        *   `Architecture Summary`: "Based on these file summaries, explain the whole..."
    *   [ ] **Context Optimization:** Leverage Gemini's large context window (1M+ tokens) to potentially process entire files at once, reducing the need for aggressive truncation.
    *   [ ] **Batch Processing:** Implement async processing (optional) or progress tracking for analyzing multiple files.

*   **Testing Strategy:**
    *   *Unit (LLM):* **CRITICAL** - Mock the LLM API calls. Do not test against real APIs in CI/CD. Verify the prompt construction logic.
    *   *Manual:* Run against a real (small) repo to verify prompt quality and token usage.

*   **Deliverables:**
    *   `core/llm.py`.
    *   `tests/test_llm_prompts.py`.

---

### Day 5: Frontend Implementation & Integration
**Phase:** Frontend Development & System Integration
**Focus:** User Experience and wiring backend to frontend.

*   **Objectives:**
    *   Build the Streamlit Interface.
    *   Connect UI events to Backend Services.

*   **Tasks:**
    *   [ ] **State Management:** Design `st.session_state` schema to hold the `Repository` object, `AnalysisResults`, and `ChatHistory`.
    *   [ ] **UI Layout:**
        *   Sidebar: Configuration (**Gemini API Key** input, Model selection e.g., `gemini-1.5-flash`) + File Tree.
        *   Main Area: Repo URL Input -> Analysis Progress Bar -> Tabs Results.
    *   [ ] **Visualization:** Embed the dependency graph component.
    *   [ ] **Artifact Display:** Render the Markdown summaries and JSON context viewer.
    *   [ ] **Download Handlers:** Buttons to download generated assets as Zip/Text.

*   **Testing Strategy:**
    *   *Manual (UI):* Verify state persistence (does data vanish on refresh?). Verify layout responsiveness.
    *   *Integration:* "Happy Path" test - Paste URL -> Click Analyze -> See Results appear.

*   **Deliverables:**
    *   `app.py` (Main entry point).
    *   `ui/components.py` (Reusable UI blocks).

---

### Day 6: Comprehensive Testing & QA
**Phase:** Quality Assurance
**Focus:** Reliability, Edge Cases, and End-to-End Validation.

*   **Objectives:**
    *   Ensure system handles real-world complexity and failures gracefully.
    *   Achieve high confidence for release.

*   **Tasks:**
    *   [ ] **Unit Test Expansion:** improved coverage for edge cases (empty files, syntax errors in target code, binary files).
    *   [ ] **Mocked E2E Tests:** Simulate a full user flow in a test script (Initialize System -> Ingest Mock Repo -> Analyze -> Generate Output) without using the UI.
    *   [ ] **Error Handling Audit:** Review all `try/except` blocks. Ensure the UI shows friendly errors for:
        *   Invalid URL.
        *   Private Repo (404/403).
        *   API Key missing/invalid.
    *   [ ] **Performance Check:** Measure time-to-analyze for a medium-sized repo. Optimization if needed.

*   **Testing Strategy:**
    *   **The "Gauntlet":** Run the tool against 3 diverse open-source repos:
        1.  *Small:* `requests` (Standard structure).
        2.  *Messy:* A tailored "bad code" repo (Circular imports, bad encoding).
        3.  *Large:* `flask` (Limit test).

*   **Deliverables:**
    *   Full Test Report.
    *   Fixed methodologies for any discovered bugs.

---

### Day 7: Documentation, Polish & Release
**Phase:** Deployment & Handoff
**Focus:** Usability and Professionalism.

*   **Objectives:**
    *   Finalize user-facing and developer documentation.
    *   Polish the visual design.

*   **Tasks:**
    *   [ ] **Documentation:**
        *   `README.md`: Update with screenshots and "How to run".
        *   `DEVELOPMENT.md`: Guide for future contributors.
        *   `USER_GUIDE.md`: Instructions on interpreting the graphs/summaries.
    *   [ ] **UI Polish:** Consistent styling (CSS injection if needed), tooltips for complex buttons.
    *   [ ] **Demo Creation:** Record the specific demo workflow for the final showcase.
    *   [ ] **Code Cleanup:** Remove all `print` debug statements, unused imports, and `TODO` comments.

*   **Testing Strategy:**
    *   *Final Acceptance Test:* Run the Demo scenario from scratch on a clean machine.

*   **Deliverables:**
    *   Release Candidate v1.0.
    *   Demo Video/Screenshots.
