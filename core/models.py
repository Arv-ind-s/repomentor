from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class FunctionNode(BaseModel):
    name: str
    start_line: int
    end_line: int
    docstring: Optional[str] = None
    args: List[str] = Field(default_factory=list)
    complexity: int = 1

class ClassNode(BaseModel):
    name: str
    start_line: int
    end_line: int
    docstring: Optional[str] = None
    methods: List[FunctionNode] = Field(default_factory=list)
    bases: List[str] = Field(default_factory=list)

class FileNode(BaseModel):
    path: str
    content: str
    classes: List[ClassNode] = Field(default_factory=list)
    functions: List[FunctionNode] = Field(default_factory=list)
    imports: List[str] = Field(default_factory=list)
    summary: Optional[str] = None
    loc: int = 0

class Repository(BaseModel):
    root_path: str
    files: List[FileNode] = Field(default_factory=list)
    name: str = "Unknown Repo"

class DependencyEdge(BaseModel):
    source: str
    target: str
    type: str = "import" # direct, dynamic, etc.

class DependencyGraph(BaseModel):
    nodes: List[str] = Field(default_factory=list) # File paths
    edges: List[DependencyEdge] = Field(default_factory=list)
