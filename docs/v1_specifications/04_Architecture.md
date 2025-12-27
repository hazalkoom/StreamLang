# StreamLang V1 Architecture

**Version**: v0.1-dev
**Type**: Tree-Walking Interpreter
**Pattern**: Visitor Pattern

---

## 1. High-Level Pipeline

Data flows synchronously from source code to execution. There is no intermediate bytecode generation in V1.

```
[ Source Code (.sl) ]
       │
       ▼
[ Lexer (ANTLR) ] ──▶ [ Tokens ]
       │
       ▼
[ Parser (ANTLR) ] ──▶ [ Parse Tree (CST) ]
       │
       ▼
[ AST Builder ] ──▶ [ Abstract Syntax Tree (AST) ]
       │
       ▼
[ Type Checker ] ──▶ [ Validated AST ]
                    (Throws Error if types mismatch)
       ▼
[ Interpreter ] ──▶ [ Output / Side Effects ]
```

---

## 2. Component Breakdown

### A. The Parser (ANTLR4)
- **Input**: Raw string.
- **Output**: ANTLR `ParseTree`.
- **Role**: Validates grammar syntax only. Does NOT check types or variable existence.
- **File**: `streamlang/parser/StreamLangParser.py` (Generated).

### B. The AST Builder (`ASTVisitor`)
- **Role**: Converts the messy ANTLR Parse Tree into clean, typed Python objects (Dataclasses).
- **Why**: We decouple our logic from ANTLR to make the interpreter clean.
- **File**: `streamlang/ast/builder.py`.

### C. The Type Checker (`TypeVisitor`)
- **Role**: A pass over the AST *before* execution.
- **Logic**:
  1. Builds a **Symbol Table** to track variables and their types.
  2. Enforces type safety (e.g., prevents `5 + "hello"`).
  3. Validates function signatures.
- **Algorithm**: Bidirectional Type Checking (Local Inference).
- **File**: `streamlang/typechecker/checker.py`.

### D. The Interpreter (`EvalVisitor`)
- **Role**: Executes the logic.
- **Pattern**: Recursive Tree-Walking.
- **State**: Maintains a `Environment` stack for variable scopes.
- **File**: `streamlang/interpreter/evaluator.py`.

---

## 3. Key Data Structures

### The Symbol Table (Type Checking)

Used during the static analysis phase to map names to types.

```python
class SymbolTable:
    def __init__(self, parent=None):
        self.symbols: Dict[str, Type] = {}
        self.parent: Optional[SymbolTable] = parent

    def define(self, name: str, type_: Type): ...
    def resolve(self, name: str) -> Optional[Type]: ...
```

### The Environment (Runtime)

Used during execution to map names to actual values.

```python
class Environment:
    def __init__(self, parent=None):
        self.values: Dict[str, Any] = {}
        self.parent: Optional[Environment] = parent

    def define(self, name: str, value: Any): ...
    def get(self, name: str) -> Any: ...
```

---

## 4. The Pipe Operator Strategy

The pipe `|>` is handled via Desugaring in the AST Builder phase. The interpreter never sees a "Pipe" node; it only sees nested function calls.

**Transformation Rule**:

```streamlang
// Source
5 |> add(10)

// AST Representation (After transformation)
CallExpr(
    func="add",
    args=[IntLit(5), IntLit(10)]
)
```

**Why**: This keeps the Interpreter simple. It doesn't need to know pipes exist.

---

## 5. Directory Structure Mapping

Where does the code live?

| Component | Path | Description |
|-----------|------|-------------|
| Grammar | `grammar/StreamLang.g4` | The law. |
| Nodes | `streamlang/ast/nodes.py` | dataclass definitions for AST. |
| Builder | `streamlang/ast/builder.py` | ANTLR Visitor -> AST. |
| Checker | `streamlang/check/checker.py` | Type validation logic. |
| Runtime | `streamlang/eval/interpreter.py` | The execution engine. |
| StdLib | `streamlang/stdlib/` | Python implementations of map, print, etc. |

---

## 6. Execution Model (V1 Limitations)

- **Synchronous**: One statement executes after another.
- **Stack Depth**: Limited by Python's recursion limit (no tail-call optimization in V1).
- **Memory**: Variables are stored in Python dictionaries. Inefficient but simple.
