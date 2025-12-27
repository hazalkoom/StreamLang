# Future Idea: Language Server Protocol (LSP)

**Target Version**: Post-v0.2
**Goal**: VS Code Support
**Tech Stack**: `pygls` (Python Generic Language Server)

---

## 1. Why?

A language without IDE support is dead on arrival. Users need:

1. Syntax Highlighting.
2. "Red Squiggles" for type errors.
3. Autocomplete (Intellisense).

---

## 2. Architecture

StreamLang will implement the standard **Language Server Protocol (LSP)**.

```
[ VS Code ] <-- JSON-RPC --> [ StreamLang LSP (Python) ]
                                │
                                ▼
                        [ StreamLang Compiler ]
                      (Reuses Parser & Type Checker)
```

---

## 3. Features Breakdown

### A. Syntax Highlighting
- **Method**: TextMate Grammar (JSON regexes).
- **Delivery**: A simple VS Code Extension `.vsix`.

### B. Diagnostics (Errors)
- **Trigger**: On File Save.
- **Action**: Run the `TypeVisitor`.
- **Output**: Map StreamLang errors to LSP `Diagnostic` objects.

### C. Hover Information
- **Trigger**: Mouse over a variable/function.
- **Action**: Look up the symbol in the `SymbolTable`.
- **Output**: Show type info (e.g., `add(a: Int, b: Int) -> Int`).

---

## 4. Implementation Plan

1. Create a `vscode-extension/` folder in the repo.
2. Use `pygls` to wrap the existing V1 Parser/Checker.
3. **Do NOT rewrite the parser**. The LSP must use the exact same code as the CLI to ensure consistency.

```python
# Pseudo-code for LSP server
@server.feature(TEXT_DOCUMENT_DID_SAVE)
def check_errors(ls, params):
    ast = parse(params.content)
    errors = type_check(ast)
    ls.publish_diagnostics(params.uri, errors)
```
