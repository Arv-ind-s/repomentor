# 🧠 RepoMentor

### AI-Powered Code Intelligence for Modern Development Teams

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---

## 🚀 What is RepoMentor?

RepoMentor is a **GenAI-driven code analysis platform** that transforms any codebase into an intelligent, queryable knowledge base. By treating your source code as the single source of truth, RepoMentor generates:

- 📚 **Human-readable documentation** - Architecture overviews, API references, and deep code explanations
- 🤖 **AI-ready context packs** - Compressed, structured code context for safe AI-assisted development

**No outdated READMEs. No manual documentation. Just your code, intelligently analyzed.**

---

## ✨ Key Features

### 🔍 **Intelligent Code Analysis**
- Multi-language AST parsing (Python, JavaScript, TypeScript, Java, Go, and more)
- Semantic code chunking at file, class, function, and block levels
- Automatic dependency graph extraction and call flow analysis

### 🎯 **Context-Aware Explanations**
- Adaptive depth: from 10,000-foot architecture views to line-by-line breakdowns
- Natural language queries: "How does authentication work?" → precise, cited answers
- Grounded responses with file paths and line number citations

### 🛡️ **Safe AI-Assisted Development**
- Read-only, non-invasive analysis (no code execution)
- Hallucination prevention through strict source code grounding
- Token-optimized context packs for AI coding tools

### ⚡ **Production-Ready Architecture**
- Multi-agent system with MCP orchestration
- Vector database-backed semantic search (FAISS/ChromaDB)
- Intelligent caching for sub-second response times
- Stateless API design for horizontal scaling

---

## 🎯 Use Cases

| Scenario | How RepoMentor Helps |
|----------|---------------------|
| **Onboarding New Developers** | Generate instant architecture docs and guided code tours |
| **Legacy Code Maintenance** | Understand undocumented systems through AI-powered analysis |
| **Code Review Assistance** | Get context on changed files and their dependencies |
| **AI Coding Tools** | Provide safe, scoped context to Copilot/ChatGPT/Claude |
| **Technical Documentation** | Auto-generate and maintain API docs from source code |
| **Architectural Planning** | Visualize dependencies and identify refactoring opportunities |

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     User Query Interface                     │
│            (API / CLI / IDE Plugin / Web Dashboard)          │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  MCP Agent Orchestrator                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐      │
│  │ Mapper   │ │Retrieval │ │ Explainer│ │ Context  │      │
│  │ Agent    │ │ Agent    │ │ Agent    │ │ Builder  │      │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘      │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              RAG Pipeline + Vector Database                  │
│   ┌────────────┐        ┌────────────┐                      │
│   │  AST       │───────▶│  Semantic  │                      │
│   │  Parser    │        │  Chunking  │                      │
│   └────────────┘        └────────────┘                      │
│          │                     │                             │
│          ▼                     ▼                             │
│   ┌────────────┐        ┌────────────┐                      │
│   │Dependency  │        │  Vector    │                      │
│   │Graph       │        │ Embeddings │                      │
│   └────────────┘        └────────────┘                      │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                    Source Repository                         │
│              (Git Remote or Local Filesystem)                │
└─────────────────────────────────────────────────────────────┘
```

### Multi-Agent System

RepoMentor employs specialized agents coordinated via Model Context Protocol (MCP):

- **Repository Mapper**: Builds structural overview and dependency graphs
- **Semantic Retrieval**: Finds relevant code chunks via vector similarity
- **Deep Explainer**: Generates detailed, context-aware explanations
- **Context Pack Builder**: Creates token-optimized AI tool inputs
- **Cache Manager**: Optimizes performance through intelligent caching

---

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.10+
Git
OpenAI API key (or compatible LLM endpoint)
```

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/repomentor.git
cd repomentor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your OpenAI API key
```

### Basic Usage

```bash
# Start the API server
uvicorn app.main:app --reload

# In another terminal, analyze a repository
curl -X POST "http://localhost:8000/api/v1/repositories" \
  -H "Content-Type: application/json" \
  -d '{
    "repo_url": "https://github.com/example/project",
    "name": "example-project"
  }'

# Query the codebase
curl -X POST "http://localhost:8000/api/v1/query" \
  -H "Content-Type: application/json" \
  -d '{
    "repo_id": "example-project",
    "query": "How does authentication work?",
    "depth": "detailed"
  }'
```

### Python SDK Example

```python
from repomentor import RepoMentor

# Initialize client
mentor = RepoMentor(api_key="your-openai-key")

# Analyze a repository
repo = mentor.analyze_repository(
    path="/path/to/local/repo",
    name="my-project"
)

# Ask questions
response = mentor.query(
    repo_id="my-project",
    query="Explain the main data flow",
    depth="architectural"
)

print(response.explanation)
print(f"Sources: {response.citations}")

# Generate context pack for AI tools
context_pack = mentor.generate_context_pack(
    repo_id="my-project",
    scope=["src/auth", "src/api"],
    max_tokens=4000
)
```

---

## 📊 API Reference

### Core Endpoints

#### Analyze Repository
```http
POST /api/v1/repositories
Content-Type: application/json

{
  "repo_url": "https://github.com/user/repo",
  "name": "unique-repo-id",
  "branch": "main"  // optional
}
```

#### Query Codebase
```http
POST /api/v1/query
Content-Type: application/json

{
  "repo_id": "unique-repo-id",
  "query": "How does the payment processing work?",
  "depth": "detailed",  // "architectural" | "detailed" | "line-by-line"
  "max_chunks": 10
}
```

#### Generate Context Pack
```http
POST /api/v1/context-pack
Content-Type: application/json

{
  "repo_id": "unique-repo-id",
  "scope": ["src/auth", "src/api"],
  "max_tokens": 4000,
  "format": "json"  // "json" | "yaml"
}
```

Full API documentation available at `http://localhost:8000/docs` when server is running.

---

## 🛠️ Configuration

### Environment Variables

```bash
# LLM Configuration
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4-turbo-preview
EMBEDDING_MODEL=text-embedding-3-small

# Vector Database
VECTOR_DB_TYPE=faiss  # faiss | chroma
VECTOR_DB_PATH=./data/vectors

# Performance
CACHE_ENABLED=true
CACHE_TTL=3600
MAX_WORKERS=4

# Security
READ_ONLY_MODE=true
ALLOWED_EXTENSIONS=.py,.js,.ts,.java,.go
```

### Advanced Configuration

```yaml
# config.yaml
analysis:
  chunk_size: 512
  chunk_overlap: 50
  languages: [python, javascript, typescript, java, go]
  
agents:
  retrieval:
    top_k: 5
    similarity_threshold: 0.7
  explainer:
    max_tokens: 2000
    temperature: 0.3
    
cache:
  type: redis  # memory | redis
  host: localhost
  port: 6379
```

---

## 🧪 Development

### Running Tests

```bash
# Unit tests
pytest tests/unit

# Integration tests
pytest tests/integration

# Coverage report
pytest --cov=app tests/
```

### Code Quality

```bash
# Format code
black app/ tests/

# Linting
ruff check app/ tests/

# Type checking
mypy app/
```

### Building Documentation

```bash
cd docs
mkdocs serve
```

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Ensure all tests pass: `pytest`
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/), [LangChain](https://www.langchain.com/), and [Tree-sitter](https://tree-sitter.github.io/tree-sitter/)
- Inspired by the need for better code comprehension tools in modern development workflows
- Special thanks to the open-source community for foundational technologies

---

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/repomentor&type=Date)](https://star-history.com/#yourusername/repomentor&Date)

---

<div align="center">

**Made with ❤️ by a developer, for developers**


</div>
