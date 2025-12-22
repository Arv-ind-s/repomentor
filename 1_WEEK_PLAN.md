# RepoMentor: 1-Week Implementation Plan (Streamlit Edition)

This document outlines a revised 7-day strategy to build **RepoMentor** as a Streamlit web application.

**Core User Flow:**
1.  User opens the RepoMentor Streamlit app.
2.  User pastes a GitHub Repository URL.
3.  System clones/fetches the repo.
4.  System analyzes the code (AST + LLM).
5.  System displays/allows download of:
    *   Human-readable Documentation (Markdown).
    *   AI-Code Context (XML/JSON).

---

## 🏗 System Architecture

### Core Components
1.  **Web Interface (`ui/`)**: Built with **Streamlit**. Handles user input (URL) and displays results.
2.  **Repo Ingestion (`ingest/`)**:
    *   Uses `GitPython` or subprocess to clone repositories to a temporary directory.
    *   Handles cleanup of temporary files after analysis.
3.  **Parser & Analyzer (`analysis/`)**:
    *   AST extraction (Classes, Functions, Docstrings).
    *   Dependency graph building.
4.  **Knowledge Core (`core/`)**:
    *   LLM Integration (Gemini/OpenAI) for summarizing code and architecture.
5.  **Generators (`generators/`)**:
    *   Outputs for the UI (interactive view) and downloadable files (zip/md).

---

## 📅 Daily Schedule

### Day 1: Foundation, Git & Streamlit Setup
**Objective:** Create the basic UI and ability to clone a repo from a URL.

*   **Implementation:**
    *   **Project Setup:** Poetry/requirements.txt (add `streamlit`, `gitpython`).
    *   **UI Skeleton:** Create `app.py` with a text input field for "GitHub URL" and a "Analyze" button.
    *   **Git Service:** Implement a module to `git clone <url>` into a temp folder (using `tempfile` lib).
    *   **Persistence:** Ensure the cloned repo persists for the session duration.
*   **Deliverable:** A running Streamlit app where I can paste a URL, and it confirms "Repository cloned successfully to /tmp/xyz".

### Day 2: AST Parsing & Structural Analysis
**Objective:** Parse the cloned code into structured data.

*   **Implementation:**
    *   **Walker:** Traverse the cloned local folder (respecting `.gitignore` if present).
    *   **AST Visitor:** Extract defined classes, functions, and global constants from Python files.
    *   **Display:** Show a rudimentary file tree in the Streamlit sidebar to prove parsing works.
*   **Deliverable:** The UI displays a list of files found in the repo and their basic statistics (line count, number of functions).

### Day 3: Dependency Graph & "Knowledge Core"
**Objective:** Understand how files relate to each other.

*   **Implementation:**
    *   **Import Parsing:** Analyze `import` statements to build a dependency graph.
    *   **Visualization:** Use `streamlit-agraph` or `graphviz` to render a basic dependency graph in the browser.
    *   **Topology:** Identify "Core" vs "Utility" modules based on connectivity.
*   **Deliverable:** A Visual Graph in the UI showing the structure of the cloned repo.

### Day 4: LLM Integration (The Brain)
**Objective:** Connect the structured data to an LLM to generate explanations.

*   **Implementation:**
    *   **LLM Service:** Integration with `litellm` (or direct API) to handle prompts.
    *   **Prompting Strategy:** Run summaries for each file using the AST data (signatures + docstrings) as context to save tokens.
    *   **Progress UI:** Add a progress bar in Streamlit to show "Analyzing file X of Y...".
*   **Deliverable:** Valid LLM summaries generated for each file in the repo.

### Day 5: Artifact Generation (The Output)
**Objective:** Generate the actual deliverables (Human Docs & AI Context).

*   **Implementation:**
    *   **Human Doc Generator:** Compile file summaries and architecture info into a structured Markdown string.
    *   **AI Context Generator:** Create the compressed JSON representation.
    *   **UI Integration:** Add tabs in Streamlit: "Read Docs" (rendered Markdown) and "AI Context" (JSON view).
*   **Deliverable:** User can read the generated docs directly in the web app.

### Day 6: Download & "Chat with Repo"
**Objective:** Allow exporting artifacts and asking follow-up questions.

*   **Implementation:**
    *   **Download Buttons:** "Download README.md", "Download Context.json".
    *   **Chat Interface:** Use `st.chat_message` to create a Q&A section.
    *   **Context Injection:** Inject the newly generated "AI Context" into the chat session's system prompt so the LLM can answer questions about the specific repo.
*   **Deliverable:** A full end-to-end loop: Clone -> Analyze -> Download -> Chat.

### Day 7: Polish, Error Handling & Deployment Prep
**Objective:** Make it robust and pretty.

*   **Tasks:**
    *   **Error Handling:** Handle private repos (auth errors), invalid URLs, or empty repos.
    *   **Cleanup:** robust deletion of temp folders to prevent disk bloat.
    *   **Styling:** Make the Streamlit app look professional (layout, typography).
    *   **Demo:** Prepare a demo video using a popular open-source repo (e.g., `requests` or `flask`).
*   **Deliverable:** A stable v0.1.0 ready for demo.

---

## 🛠 Tech Stack

*   **Frontend:** `Streamlit`
*   **Core Logic:** Python 3.10+
*   **Git Operations:** `GitPython`
*   **Analysis:** `ast`, `networkx`
*   **Visualization:** `graphviz` or `streamlit-agraph`
*   **LLM Client:** `litellm`
