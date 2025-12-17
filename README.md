# RepoMentor

<div align="center">

**AI-Powered Code Comprehension for Modern Development Teams**

*Making every codebase self-explanatory*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[Features](#features) • [Architecture](#architecture) • [Getting Started](#getting-started) • [Roadmap](#roadmap) • [Contributing](#contributing)

</div>

---

## Overview

RepoMentor is a GenAI-driven platform that transforms how developers understand and navigate unfamiliar codebases. By generating real-time, context-aware documentation and explanations, it eliminates the traditional barriers to code comprehension and accelerates developer onboarding.

### The Problem

Modern software development faces a critical documentation gap:

- **Rapid Development**: AI tools enable faster code generation than ever before
- **Documentation Debt**: Documentation is frequently missing, outdated, or inconsistent
- **Onboarding Friction**: New developers spend weeks understanding codebases that could be explained in hours
- **Knowledge Silos**: Senior engineers become bottlenecks as implicit "documentation providers"

### Our Solution

RepoMentor acts as an always-available, code-aware mentor that:

- Explains what code does, why it exists, and how components connect
- Generates documentation on-demand, not as static artifacts
- Answers questions conversationally with strict grounding in actual source code
- Adapts explanation depth to the developer's experience level

> **Core Philosophy**: If a developer joins your team today, they should understand and contribute to your codebase tomorrow—with minimal external help.

---

## Features

### 📚 Intelligent Documentation Generation

Generate comprehensive documentation on-demand:

- **File-Level Summaries**: High-level overviews of modules and their responsibilities
- **Dependency Analysis**: Understand how files and components interact
- **Architecture Overviews**: System-wide design patterns and structure
- **Onboarding Guides**: Tailored explanations for new team members

### 🔍 Deep Code Comprehension

Multi-level code explanations:

- **Function Walkthroughs**: Step-by-step logic breakdowns
- **Block-Level Analysis**: Explanation of logical segments within functions
- **Line-by-Line Mode**: Optional detailed explanations for complex sections
- **Adaptive Depth**: Beginner-friendly or detailed modes based on user needs

### 💬 Conversational Interface

Natural language interaction with your codebase:

```
"What does this authentication module do?"
"Why is Redis used in the caching layer?"
"Where does user input validation happen?"
"How do these three services communicate?"
```

All answers are strictly grounded in retrieved code context to prevent hallucinations.

### 🧩 Multi-Agent Architecture

Specialized AI agents working in concert:

| Agent | Responsibility |
|-------|----------------|
| **Repo Mapper** | Builds file trees, identifies entry points and dependencies |
| **Context Builder** | Retrieves relevant code chunks using semantic search |
| **Documentation Generator** | Creates structured, readable documentation |
| **Code Explainer** | Produces explanations from high-level to line-by-line |
| **Cache Manager** | Optimizes performance through intelligent caching |

### 🔐 Safe by Design

- **Read-Only**: No automatic writes to repositories
- **Non-Invasive**: No code mutation or modification
- **Privacy-First**: Designed for safe use with proprietary codebases

---

## Architecture

```
┌─────────────────────┐
│ GitHub Repository   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────┐
│ Repo Ingestion & AST Parser │
└──────────┬──────────────────┘
           │
           ▼
┌──────────────────────────┐
│ Semantic Code Chunking   │
└──────────┬───────────────┘
           │
           ▼
┌─────────────────────────┐
│ Vector Embeddings Store │
└──────────┬──────────────┘
           │
           ▼
┌──────────────────────┐
│ Context Builder Agent│
└──────────┬───────────┘
           │
           ▼
┌─────────────────────────┐
│ MCP Multi-Agent System  │
│  ┌───────────────────┐  │
│  │ Mapper            │  │
│  │ Documentor        │  │
│  │ Explainer         │  │
│  │ Cache Manager     │  │
│  └───────────────────┘  │
└──────────┬──────────────┘
           │
           ▼
┌───────────────────────────┐
│ API / Web Interface       │
└───────────────────────────┘
```

### Core Design Principles

1. **On-Demand Generation**: Documentation created when needed, not stored statically
2. **Retrieval Grounding**: All explanations backed by actual code to prevent AI hallucinations
3. **Scoped Explanations**: Token-efficient responses that focus on what's relevant
4. **Cache-First**: Performance optimization through intelligent result caching

---

## Tech Stack

### Backend & API
- **Python 3.10+**: Core language
- **FastAPI**: High-performance API framework
- **Pydantic**: Data validation and settings management

### AI & Machine Learning
- **LLM Integration**: OpenAI API / open-source compatible models
- **RAG Pipeline**: Retrieval-Augmented Generation for grounded responses
- **Code Embeddings**: Semantic understanding of code structure
- **MCP**: Model Context Protocol for multi-agent orchestration

### Code Processing
- **GitHub Integration**: Clone and analyze public/private repositories
- **AST Parsing**: Language-aware syntax tree analysis
- **Semantic Chunking**: File → Class → Function → Block hierarchy

### Storage & Retrieval
- **Vector Database**: FAISS / Chroma (pluggable architecture)
- **Caching Layer**: Local/in-memory for MVP, scalable for production

### Frontend (Planned)
- Modern web interface for repository exploration
- Interactive code browser with inline explanations
- Conversational chat interface

---

## Getting Started

> **Note**: RepoMentor is currently in active development. Installation instructions will be added as the project reaches initial release.

### Prerequisites

```bash
Python 3.10+
Git
OpenAI API key (or compatible LLM endpoint)
```

### Quick Start (Coming Soon)

```bash
# Clone the repository
git clone https://github.com/yourusername/repomentor.git
cd repomentor

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Run the service
python main.py
```

---

## Roadmap

### ✅ Phase 0: Foundation (Current)
- [x] Project architecture design
- [x] Repository initialization
- [x] Documentation structure

### 🚧 Phase 1: Core Backend (In Progress)
- [ ] Repository ingestion pipeline
- [ ] File tree extraction
- [ ] Semantic code chunking
- [ ] Vector store integration

### 📋 Phase 2: RAG + MCP Implementation
- [ ] Context builder agent
- [ ] Documentation generation agent
- [ ] Code explanation agent
- [ ] Retrieval grounding system

### 📋 Phase 3: Real-Time Explanations
- [ ] File-level documentation
- [ ] Function-level walkthroughs
- [ ] Scoped line-by-line mode
- [ ] Adaptive explanation depth

### 📋 Phase 4: User Interface
- [ ] Repository URL input
- [ ] Interactive file explorer
- [ ] Inline code explanations
- [ ] Conversational Q&A interface

### 📋 Phase 5: Advanced Features
- [ ] Export documentation as Markdown
- [ ] Onboarding summary generation
- [ ] Performance optimizations
- [ ] GitHub App integration

### 🔮 Future Vision
- IDE plugins (VS Code, JetBrains)
- PR-based documentation previews
- Enterprise onboarding workflows
- Team knowledge sharing features

---

## Use Cases

### For Individual Developers
- Quickly understand unfamiliar open-source projects
- Navigate legacy codebases with confidence
- Learn from well-structured code examples

### For Teams
- Accelerate new hire onboarding from weeks to days
- Reduce dependency on senior developers for code explanations
- Maintain living documentation that evolves with the codebase

### For Organizations
- Improve knowledge transfer across teams
- Reduce technical debt from poor documentation
- Enable faster feature development on existing systems

---

## Scope & Intentional Limitations

**RepoMentor is NOT:**
- A static analysis security tool (SAST)
- A replacement for human code reviews
- An automatic code generation system

**RepoMentor IS:**
- A code comprehension accelerator
- A documentation-on-demand system
- An onboarding enabler for developers at all levels

---

## Contributing

We welcome contributions from the community! Whether you're fixing bugs, adding features, or improving documentation, your help makes RepoMentor better for everyone.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Philosophy

This project emphasizes:
- **Clear Code**: Readability over cleverness
- **Real-World Engineering**: Production-ready patterns and practices
- **Learning Focus**: Well-documented decisions and trade-offs

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

Built with a focus on making software development more accessible and efficient for developers worldwide.

---

<div align="center">

**[Report Bug](../../issues)** • **[Request Feature](../../issues)** • **[Discussions](../../discussions)**

Made with ❤️ for the developer community

</div>
