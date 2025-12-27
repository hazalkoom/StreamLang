# V1 Scope Definition (v0.1)

**Goal**: Prove the core concept—pipeline-based transformations with strong typing.

---

## 🎯 Mission

Build a **minimal, working interpreter** that executes `.sl` files with:
- Variables and functions
- The pipe operator (`|>`)
- Basic types with inference
- Synchronous execution only

**Success**: Run `python -m streamlang run demo.sl` and see correct output.

---

## ✅ What's In

### Types
- `Int`, `String`, `Bool`
- `List<T>` (Internal generics only; users cannot define generic types)
- Type inference from assignment
- Explicit function return types

### Syntax
- `let` (immutable variables)
- `fn` (function definitions)
- `|>` (pipe operator)
- `if/else` expressions
- Arithmetic: `+`, `-`, `*`, `/`, `%`
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical: `&&`, `||`, `!`

### Standard Library
- **Math**: `add`, `sub`, `mul`, `div`, `mod`
- **String**: `toUpper`, `toLower`, `concat`, `length`
- **List**: `map`, `filter`, `reduce`, `length`, `head`, `tail`
- **I/O**: `print`, `println`

### Tools
- CLI: `python -m streamlang run file.sl`
- REPL: `python -m streamlang repl`

---

## ❌ What's Out

Hard boundaries to keep scope tight:

- ❌ HTTP calls
- ❌ File I/O
- ❌ Classes/Objects
- ❌ Async/Await
- ❌ For/While loops (use map/filter/recursion)
- ❌ Mutable variables
- ❌ User-defined modules / imports
- ❌ User-defined Generics (StdLib only)
- ❌ Pattern matching (comes in v0.2)
- ❌ Closures
- ❌ Error handling types (Result/Option)

---

## 🔄 Pipeline Mechanics

The pipe operator desugars left-to-right at the AST level:

```
x |> f()     → f(x)
x |> f(y)    → f(x, y)
x |> f(y, z) → f(x, y, z)
```

**Rule**: Piped value becomes the **first argument**.

**Example**:
```streamlang
// These are identical:
let result1 = add(mul(5, 2), 10)
let result2 = 5 |> mul(2) |> add(10)
```

---

## 📊 Component Checklist

### Phase 1: Parsing
- [ ] ANTLR4 grammar (`StreamLang.g4`)
- [ ] Generate Python parser
- [ ] AST node classes (Visitor Pattern)

### Phase 2: Type System
- [ ] Type representation (classes)
- [ ] Symbol table (scopes)
- [ ] Type checker (Bidirectional / Local Inference)
- [ ] Error reporting (line numbers)

### Phase 3: Interpreter
- [ ] Environment/scope manager
- [ ] Expression evaluator (AST walker)
- [ ] Function call handling
- [ ] Pipe operator desugaring
- [ ] Built-in function registry

### Phase 4: CLI
- [ ] `run` command
- [ ] REPL with multi-line support
- [ ] Error output formatting (Stack trace + Exit Code 1)

---

## 🧪 Acceptance Tests

### Type Safety:
- [ ] Reject `let x: Int = "hello"`
- [ ] Reject mismatched `if/else` branches

### Pipe Operator:
- [ ] `5 |> add(3)` → `8`
- [ ] `[1,2,3] |> map(double) |> reduce(0, add)` → `12`

### Scoping:
- [ ] Inner scope reads outer variables
- [ ] Shadowing doesn't leak

### Errors:
- [ ] Division by zero prints error and exits (Code 1)
- [ ] Undefined variable/function prints error and exits (Code 1)

---

## 📈 Definition of Done

V1 ships when:

1. All checkboxes above are ✅
2. Example programs in `examples/` run correctly
3. Test suite passes (unit + integration)
4. REPL handles multi-line input
5. CLI errors show line numbers
6. Documentation covers all syntax

---

## 🔜 Next (v0.2)

Not in V1, but coming:

- File I/O (`file.read`, `file.write`)
- HTTP module (sync GET/POST)
- JSON parsing
- `Result<T, E>` and `match` expressions