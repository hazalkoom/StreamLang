# StreamLang

> A strongly-typed language for backend data pipelines and API orchestration.

---

## 🎯 The Mission

Backend engineers waste time writing brittle glue code between APIs, databases, and file systems. StreamLang treats data pipelines as a first-class language construct with native pipe operators (`|>`), strong typing, and built-in HTTP primitives.

**No nested callbacks. No framework hell. Just clean, composable transformations.**

---

## 🧬 Core Philosophy

- **Pipeline-First**: The `|>` operator is the primary composition mechanism
- **Strongly Typed**: Compile-time type checking with inference
- **Explicit I/O**: All side effects (HTTP, File) are clearly marked
- **Sync-First**: V1 is synchronous—async comes later
- **Predictable Execution**: No hidden magic; desugaring is transparent and consistent

---

## ⚙️ Architecture

**Implementation**: Python 3.11+  
**Parser**: ANTLR4 (grammar-driven)  
**Execution**: Tree-walking interpreter (V1)  
**Type System**: Static with Local Type Inference (Bidirectional)

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│  .sl     │────▶│  ANTLR4  │────▶│   AST    │────▶│   Type   │
│  Source  │     │  Parser  │     │          │     │  Checker │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
                                                          │
                                                          ▼
                                                    ┌──────────┐
                                                    │   Tree   │
                                                    │  Walker  │
                                                    │          │
                                                    └──────────┘
```

See [`docs/architecture/`](docs/architecture/) for component design.

---

## 🗺️ Roadmap

### **v0.1** — The Engine
**Status**: `🟡 In Progress`

Core runtime: variables, functions, pipes, basic types.

**Delivers**:
- ANTLR4 grammar and parser
- Type inference engine (Local/Bidirectional)
- Tree-walking interpreter
- CLI + REPL

**Spec**: [`docs/v1_specifications/01_V1_Scope.md`](docs/v1_specifications/01_V1_Scope.md)

---

### **v0.2** — The I/O
**Status**: `⚪ Planned`

File operations and HTTP (synchronous only).

**Delivers**:
- File module (read/write/exists)
- HTTP module (GET/POST/PUT/DELETE)
- JSON parsing
- `Result<T, E>` error handling

---

### **v1.0** — The Async
**Status**: `⚪ Future`

Concurrency and performance optimizations.

**Delivers**:
- Event loop
- `async`/`await` syntax
- Concurrent HTTP
- Bytecode compiler

---

## 🚀 Quick Start

```bash
# Clone and install
git clone https://github.com/yourusername/streamlang.git
cd streamlang
pip install -r requirements.txt

# Run REPL
python -m streamlang repl

# Execute a file
python -m streamlang run examples/hello.sl
```

---

## 📁 Project Structure

```
streamlang/
├── README.md                      # You are here
├── CHANGELOG.md                   # Version history
├── LICENSE                        # MIT License
├── CONTRIBUTING.md                # Contribution guidelines
├── requirements.txt               # Python dependencies
├── grammar/
│   └── StreamLang.g4              # ANTLR grammar definition
├── streamlang/
│   ├── parser/                    # Generated ANTLR parsers
│   ├── ast/                       # AST node definitions
│   ├── typechecker/               # Type inference engine
│   ├── interpreter/               # Tree-walking interpreter
│   ├── stdlib/                    # Built-in functions
│   └── cli/                       # REPL + CLI entry points
├── tests/                         # Unit and integration tests
├── examples/                      # Sample .sl programs
└── docs/
    ├── v1_specifications/         # V1 implementation details
    │   ├── 01_V1_Scope.md
    │   ├── 02_Language_Syntax.md
    │   ├── 03_Std_Lib.md
    │   └── 04_Architecture.md
    └── future_ideas/              # Post-v1.0 concepts
        ├── Async_Event_Loop.md
        ├── LSP_Extension.md
        └── Native_HTTP_Client.md
```

**Documentation Links:**
- [V1 Scope](docs/v1_specifications/01_V1_Scope.md) - What's in/out for v0.1
- [Language Syntax](docs/v1_specifications/02_Language_Syntax.md) - Grammar + examples  
- [Standard Library](docs/v1_specifications/03_Std_Lib.md) - Built-in functions
- [Architecture](docs/v1_specifications/04_Architecture.md) - System design
- [Future Ideas](docs/future_ideas/) - Post-v1.0 concepts

---

## 📚 Documentation Index

| Document | Purpose |
|----------|---------|
| [`01_V1_Scope.md`](docs/v1_specifications/01_V1_Scope.md) | What's in/out for v0.1 |
| [`02_Language_Syntax.md`](docs/v1_specifications/02_Language_Syntax.md) | Grammar + examples |
| [`03_Std_Lib.md`](docs/v1_specifications/03_Std_Lib.md) | Standard Library reference |
| [`04_Architecture.md`](docs/v1_specifications/04_Architecture.md) | System architecture |

---

## 🧪 Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage report
pytest --cov=streamlang tests/

# Type check the codebase
mypy streamlang/
```

---

## 🤝 Contributing

Active development. Contributions welcome after v0.1 stabilizes.

**Current Focus**: Completing v0.1 interpreter.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines.

---

## 📄 License

MIT - See [`LICENSE`](LICENSE) file for details.

---

## 🔗 Links

- **Documentation**: [`docs/`](docs/)
- **Issue Tracker**: `github.com/yourusername/streamlang/issues`
- **Discussions**: `github.com/yourusername/streamlang/discussions`

---

**Version**: v0.1-dev  
**Status**: Pre-alpha  
**Last Updated**: December 2025
