# StreamLang Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased] - v0.1-dev

### 🚀 Added
- **Grammar**: Initial ANTLR4 grammar (`StreamLang.g4`) supporting `fn`, `let`, and `|>`.
- **Docs**: Complete V1 Scope, Syntax Guide, StdLib spec, and Architecture overview.
- **StdLib**: Defined specifications for `Math`, `String`, `List`, and `I/O` modules.
- **Core**: Defined `Int`, `String`, `Bool`, and `List<T>` types.

### 🔧 Fixed
- Clarified that `if/else` is an expression, not a statement.
- Removed "Hindley-Milner" from vision docs; replaced with "Bidirectional Local Inference".
- Explicitly excluded `async/await` and `loops` from V1 scope.

---

## [Planned] - v0.2

### 🔮 Proposed
- **HTTP Module**: Synchronous `get`, `post`, `put`, `delete`.
- **File I/O**: Read/Write local files.
- **JSON**: Native JSON parsing support.
- **Pattern Matching**: `match` expression for control flow.