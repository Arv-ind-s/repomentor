# RepoMentor 🧠📚

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Status: Active Development](https://img.shields.io/badge/status-active_development-orange.svg)]()

**Making every codebase understandable — for humans and AI.**

RepoMentor is a GenAI-driven platform that treats source code as the single source of truth. It analyzes your repository's structure and logic (via AST) to generate high-fidelity documentation for developers and safety-first context for AI coding tools.

[The Problem](#the-problem) • [Key Features](#key-features) • [Architecture](#architecture) • [Getting Started](#getting-started) • [Use Cases](#use-cases)

---

## 🚀 The Core Innovation: Two-Layer Understanding

Unlike tools that simply summarize files, RepoMentor builds a **Knowledge Core** directly from code structure to serve two distinct audiences:

### 1. Human Knowledge Layer
* **On-Demand Docs:** Fresh documentation that never goes out of date.
* **Multi-Level Walkthroughs:** Explanations ranging from high-level architecture to line-by-line logic.
* **Grounded Q&A:** A conversational interface that answers questions based *only* on the code, eliminating hallucinations.

### 2. AI Coding Context Pack (The Differentiator)
* **Safety Guardrails:** A compressed artifact that tells AI tools what they *cannot* break (system invariants, public contracts).
* **Global Awareness:** Provides AI agents with the "Senior Engineer's intuition" without needing to ingest the entire multi-GB codebase.

---

## 🛠 Features

* **🔍 AST-Level Analysis:** Goes beyond text to understand actual code relationships and dependencies.
* **🤖 Multi-Agent Orchestration:** Uses the **Model Context Protocol (MCP)** to coordinate specialized agents (Repo Mapper, Context Builder, etc.).
* **🚫 Zero-Trust Documentation:** Ignores potentially outdated READMEs or comments; if it's not in the code, RepoMentor doesn't claim it as truth.
* **💬 Interactive Mentorship:** Natural language queries like *"Where does user input validation happen?"* provide instant, cited answers.

---

## 🏗 Architecture

RepoMentor utilizes a sophisticated pipeline to ensure consistency between human explanations and AI context.

```mermaid
graph TD
    A[Source Codebase] --> B[Ingestion & AST Parsing]
    B --> C[Structural & Semantic Analysis]
    C --> D{RepoMentor Knowledge Core}
    D --> E[📚 Human Documentation Layer]
    D --> F[🤖 AI Coding Context Pack]
    style D fill:#f96,stroke:#333,stroke-width:2px
Tech Stack
Language: Python 3.10+

Frameworks: FastAPI, Pydantic

AI/ML: OpenAI API, RAG, Semantic Embeddings

Orchestration: Model Context Protocol (MCP)

Vector DB: FAISS / Chroma

🏁 Getting Started
Warning: RepoMentor is currently in Active Development. Features are being rolled out weekly.

Prerequisites

Python 3.10+

Git

OpenAI API Key

Installation

Clone the repository
Bash
git clone [https://github.com/yourusername/repomentor.git](https://github.com/yourusername/repomentor.git)
cd repomentor

Set up environment

Bash
pip install -r requirements.txt
cp .env.example .env # Add your API Key here
Run the analysis

Bash
python main.py
🎯 Use Cases
Onboarding: New hires go from "cloning" to "contributing" in days, not weeks.

Legacy Systems: Understand the "why" behind complex, undocumented codebases.

Safe AI Development: Enable junior developers or AI agents to work on sensitive modules with automated guardrails.

🤝 Contributing
We value clear code and thoughtful engineering. To contribute:

Fork the project.

Create your Feature Branch (git checkout -b feature/AmazingFeature).

Commit your changes.

Push to the Branch.

Open a Pull Request.

📜 License
Distributed under the MIT License. See LICENSE for more information.

<div align="center"> <sub>Built with ❤️ by developers, for developers.</sub> </div>
