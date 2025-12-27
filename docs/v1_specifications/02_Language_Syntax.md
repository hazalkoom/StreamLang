# StreamLang V1 Syntax Guide

**Version**: v0.1-dev
**Status**: Draft
**Prerequisite**: Python 3.11+

This document defines the surface syntax for StreamLang V1. It corresponds strictly to the `StreamLang.g4` grammar.

---

## 1. Comments

Comments are ignored by the parser.

```streamlang
// This is a single-line comment

/*
  This is a
  block comment
*/
```

---

## 2. Basic Types & Literals

V1 supports four primitive types. All values are immutable.

| Type | Syntax | Example |
|------|--------|---------|
| Int | Decimal integers | `42`, `-10`, `0` |
| String | Double-quoted text (JSON-style escapes) | `"hello\nworld"`, `"result: \"ok\""` |
| Bool | `true` or `false` | `true` |
| List&lt;T&gt; | Square brackets | `[1, 2, 3]`, `["a", "b"]` |

❌ Invalid: `[1, "a"]` (Mixed types are not allowed), `'hello'` (Single quotes are not supported)

---

## 3. Variable Declarations

Variables are declared with `let`. They are immutable.

**Syntax**: `let <identifier> = <expression>`

**Examples**:

```streamlang
// ✅ Valid
let x = 10
let name = "StreamLang"
```

```streamlang
// ❌ Invalid
let x = 10
x = 11  // Error: Reassignment is forbidden
let y: Int = 10 // Error: Explicit type annotations on 'let' are not in V1
```

---

## 4. Functions

Functions must be defined at the top level.

**Syntax**:
```streamlang
fn <name>(<param>: <Type>, ...) -> <ReturnType> {
  <statement>*
  <expression>?
}
```

**Rules**:
- Explicit Types: You must type-hint arguments and return values.
- Implicit Return: The last expression is the return value.

**Example**:
```streamlang
fn add(a: Int, b: Int) -> Int {
  a + b
}
```

❌ Invalid:
- `fn add(a, b) { ... }` (Missing types)
- `fn add(a: Int) -> Int { return a }` (No return keyword in V1)

---

## 5. The Pipe Operator (|&gt;)

The value on the left is injected as the first argument of the function on the right.

| Pipe Syntax | Equivalent Standard Call |
|-------------|--------------------------|
| `x |> f()` | `f(x)` |
| `x |> f(y)` | `f(x, y)` |
| `x |> f(y, z)` | `f(x, y, z)` |

**Example**:
```streamlang
let res = 10 |> mul(2) |> add(5)
// Equivalent to: add(mul(10, 2), 5)
```

---

## 6. Control Flow (if / else)

`if` is an expression, not a statement. It must return a value.

**Syntax**:
```streamlang
if <condition> { <expr> } else { <expr> }
```

❌ Invalid:
- `if x > 10 { "big" }` (Missing else block)
- `if x > 10 { 1 } else { "small" }` (Type mismatch between branches)

---

## 7. Operator Precedence

Ordered from highest (evaluates first) to lowest.

| Precedence | Operator | Description | Associativity |
|------------|----------|-------------|---------------|
| 1 | `()` | Parentheses | - |
| 2 | `f(...)` | Function Call | - |
| 3 | `-`, `!` | Unary Minus, Logical Not | Right |
| 4 | `*`, `/`, `%` | Multiplication, Division | Left |
| 5 | `+`, `-` | Addition, Subtraction | Left |
| 6 | `==`, `!=`, `<`, `>`, `<=`, `>=` | Comparisons | Left |
| 7 | `&&` | Logical AND | Left |
| 8 | `\|\|` | Logical OR | Left |
| 9 | `\|>` | Pipe | Left |

---

## 8. Reserved Keywords

`fn`, `let`, `if`, `else`, `true`, `false`
