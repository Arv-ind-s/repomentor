# System Architecture

## Overview
RepoMentor follows a modular architecture designed for clear separation of concerns between the UI, Ingestion, Analysis, and Intelligence layers.

## High-Level Data Flow

```mermaid
graph TD
    User[User] -->|Input: Repo URL| UI[Streamlit UI]
    UI -->|Trigger| Ingest[Ingestion Service]
    
    subgraph Core System
        Ingest -->|Clone| FS[FileSystem (Temp)]
        FS -->|Read| Parser[AST Parser]
        Parser -->|Extract Nodes| Graph[Dependency Graph Builder]
        
        Parser & Graph -->|Structured Data| Models[Data Models (Pydantic)]
        Models -->|Context| LLM[LLM Service (Gemini)]
    end
    
    LLM -->|Summaries| Artifacts[Artifact Generator]
    Artifacts -->|Markdown/JSON| UI
```

## Module Responsibilities

### 1. `ui/` (Frontend)
- **Tech**: Streamlit
- **Role**: Handles user interaction, state management (`st.session_state`), and visualization.
- **Key Components**:
    - `app.py`: Main entry point.
    - `components.py`: Reusable widgets (File Tree, Chat Box).

### 2. `core/ingest` (Ingestion)
- **Tech**: GitPython
- **Role**: Securely clones remote repositories to temporary directories.
- **Key Classes**:
    - `GitIngestor`: Manages cloning and cleanup.

### 3. `core/parser` (Analysis)
- **Tech**: Python `ast`
- **Role**: Static analysis of source code.
- **Key Classes**:
    - `PythonParser`: Visits AST nodes to extract metadata (functions, classes, imports).

### 4. `core/graph` (Knowledge)
- **Tech**: NetworkX
- **Role**: Builds a directed graph of file dependencies.
- **Key Classes**:
    - `DependencyBuilder`: Resolves imports to file paths.

### 5. `core/llm` (Intelligence)
- **Tech**: Google Gemini API (`google-generativeai`)
- **Role**: Generates natural language summaries and insights.
- **Key Classes**:
    - `GeminiClient`: Handles API communication and rate limiting.

## Data Models (Pydantic)

The system relies on strict typing for data passing:

- **`Repository`**: Root object containing a list of `FileNode`s.
- **`FileNode`**: Represents a single file (path, content, AST metadata).
- **`FunctionNode`**: Metadata for functions (name, args, docstring).
- **`ClassNode`**: Metadata for classes (methods, bases).
