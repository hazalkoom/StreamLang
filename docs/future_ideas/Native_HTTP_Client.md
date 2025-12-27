# Future Idea: Native HTTP Client

**Target Version**: v0.2
**Status**: Draft / RFC
**Dependency**: Requires stable V1 Interpreter

---

## 1. The Problem

StreamLang is designed for "API Orchestration," but V1 has no network capabilities. V2 must introduce HTTP without introducing the complexity of an Async Event Loop (which is saved for V1.0).

---

## 2. The Solution (Synchronous HTTP)

We will wrap Python's `requests` library (or `urllib`) to provide a **blocking** HTTP client. This keeps the interpreter simple (no `await` needed yet).

---

## 3. Proposed Syntax

### The `http` Module

```streamlang
// GET Request
let response = "https://api.example.com/users"
  |> http.get()

// POST Request with JSON
let payload = "{ \"name\": \"Alice\" }"
let response = "https://api.example.com/users"
  |> http.post(payload)
```

---

## 4. The Response Type

Since we don't have Classes, the Response will likely be a structured Map or a specific opaque type.

**Draft Structure**:

```streamlang
// Accessing fields (Syntax TBD in v0.2)
let code = response |> http.statusCode()
let body = response |> http.body()
```

---

## 5. Error Handling

V0.2 introduces `Result<T, E>`. HTTP calls will return a `Result`, forcing the user to handle network failures.

```streamlang
// Hypothetical V0.2 Syntax
let result = url |> http.get()

match result {
  Ok(res) -> print(res)
  Err(e)  -> print("Network error")
}
```

---

## 6. Constraints

- **Blocking**: The interpreter halts until the request finishes.
- **No Streaming**: Responses are fully buffered into memory.
- **Timeout**: Must have a default timeout (e.g., 30s) to prevent hanging.
