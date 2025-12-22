# RepoMentor 🧠📚

<div align="center">
  <h3>AI-Powered Code Comprehension & Safe AI Context for Modern Development Teams</h3>
  <p>Making every codebase understandable — for humans and AI</p>

  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
  [![Status: Active Development](https://img.shields.io/badge/status-active_development-orange.svg)]()
</div>

---

## 📖 Overview
**RepoMentor** is a GenAI-driven, code-first platform that helps developers and AI coding tools understand, navigate, and safely work within unfamiliar codebases.

By treating **source code as the single source of truth**, RepoMentor analyzes repositories directly—rather than relying on READMEs or manually maintained documentation—to generate:

* 📚 **Human-readable documentation** and explanations for fast onboarding and comprehension.
* 🤖 **Compressed, machine-consumable context** that enables AI coding tools to make changes without breaking system-wide invariants.

RepoMentor is designed to ensure that a developer joining today can understand the system quickly, and an AI coding tool operating locally has enough global context to behave like a senior engineer.

---

## ⚠️ The Problem
Modern software development faces a growing documentation and safety gap:

* **Rapid Development** – AI tools enable faster code generation than teams can understand.
* **Documentation Debt** – Documentation is frequently missing, outdated, or inconsistent.
* **Onboarding Friction** – New developers spend weeks understanding large codebases.
* **Knowledge Silos** – Senior engineers become implicit documentation providers.
* **Unsafe AI Coding** – AI tools lack global context and unknowingly violate architectural constraints.

> Most tools today focus on either **explaining code** or **writing code**, but rarely both — and almost never safely.

---

## 💡 Our Solution
RepoMentor acts as an **always-available, code-aware mentor** that derives understanding directly from the codebase.

### Human Knowledge Layer
* On-demand documentation generated from code.
* Architecture and dependency explanations.
* Function-level, block-level, and line-by-line walkthroughs.
* Conversational Q&A strictly grounded in source code.

### AI Coding Context Layer
* A compressed, enforceable context artifact for AI coding tools.
* Encodes system invariants, public contracts, dependencies, and high-risk zones.
* Enables safe “vibe coding” without loading the entire repository.

**Note:** RepoMentor **does not trust** READMEs, wikis, or markdown files as inputs. Documentation and AI context are generated outputs, always consistent with the actual code.

---

## 🎯 Core Design Philosophy
**Code is truth.** Documentation and AI context are derived artifacts.

| Aspect | RepoMentor Approach |
| :--- | :--- |
| **Trust Source** | ❌ Does not rely on README files or comments as authoritative sources |
| **Repository Impact** | ❌ Does not mutate or modify repositories |
| **Analysis Method** | ✅ Performs AST-level and structural analysis of source code |
| **Syncing** | ✅ Keeps human documentation and AI context always in sync |

---

## ✨ Features

### 📚 Intelligent Documentation Generation
* **File-Level Summaries** – Responsibilities and intent of each module.
* **Dependency Analysis** – How files and components interact.
* **Architecture Overviews** – Inferred system design and structure.
* **Onboarding Guides** – End-to-end explanations for new developers.

### 🔍 Deep Code Comprehension
* **Function Walkthroughs** – Step-by-step logic breakdowns.
* **Block-Level Analysis** – Logical grouping explanations.
* **Adaptive Depth** – Beginner-friendly to expert-level explanations.

### 💬 Conversational Interface
Ask natural-language questions about your codebase:
* *"What does this authentication module do?"*
* *"Why is Redis used in the caching layer?"*
* *"How do these services communicate?"*

---

## 🏗 Architecture



```mermaid
graph TD
  Codebase --> Ingestion[Repo Ingestion & AST Parsing]
  Ingestion --> Analysis[Structural & Semantic Analysis]
  Analysis --> Core{RepoMentor Knowledge Core}
  Core --> HumanDocs[Human Documentation Layer]
  Core --> AIContext[AI Coding Context Pack]
