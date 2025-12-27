# Future Idea: Async Event Loop

**Target Version**: v1.0
**Status**: Concept / Long-term
**Complexity**: Extreme

---

## 1. The Challenge

StreamLang V1 is a synchronous tree-walker. It executes strictly top-to-bottom.
To support high-concurrency API orchestration (the ultimate goal), we need non-blocking I/O.

**The Problem**: You cannot simply "add async" to a recursive tree-walker without rewriting the entire host interpreter to be async-aware (the "Function Coloring" problem).

---

## 2. Proposed Architecture (v1.0)

We will likely need to move away from the simple Tree-Walker and towards a **Bytecode Virtual Machine** or an **Async AST Walker**.

### Option A: Async Tree Walker (Python `asyncio`)

We rewrite every `visit` method in the interpreter to be `async def visit...`.

- **Pros**: Easier to implement in Python.
- **Cons**: Python's recursion limit still bites us; slower.

### Option B: Bytecode VM (The Professional Way)

We compile `.sl` source code into flat bytecode instructions, then run a loop that executes them.

- **Pros**: Pausable execution (yield), no recursion limit, easy to integrate an Event Loop.
- **Cons**: Much harder to build.

---

## 3. Syntax Proposal

```streamlang
// Defining an async task
async fn fetchUser(id: Int) -> User {
  "https://api.example.com/users/"
    |> concat(id)
    |> http.get()  // Non-blocking yield
}

// Consuming it
let user = await fetchUser(42)
```

---

## 4. The "Concurrency" Module

Future primitive for running pipelines in parallel.

```streamlang
let ids = [1, 2, 3]

// Run 3 requests in parallel, wait for all
let users = ids |> map(fetchUser) |> await.all()
```

---

## 5. Migration Strategy

- **v0.1 - v0.2**: Strictly Synchronous.
- **v1.0**: Introduce the `async` keyword.
- **Internal**: The Interpreter execution loop must wrap Python's `asyncio.run()`.
