# � StreamLang Documentation

StreamLang is a statically-typed, pipe-forward programming language designed for engineers who think in data pipelines.

*"Don't nest it. Pipe it."*

## 📑 Table of Contents

- [Getting Started](#-getting-started)
- [Variables & Constants](#-variables--constants)
- [The Pipe Operator (|>](#-the-pipe-operator)
- [Functions](#-functions)
  - [Declaration](#declaration)
  - [Implicit vs Explicit Return](#implicit-vs-explicit-return)
  - [Recursion](#recursion)
- [Control Flow](#-control-flow)
  - [If / Else](#if--else)
  - [While Loops](#while-loops)
  - [For Loops](#for-loops)
- [Operators & Math](#-operators--math)
- [Scoping & Shadowing](#-scoping--shadowing)

## 🚀 Getting Started

StreamLang code can be executed in the Online Playground or via the CLI.

**The Golden Rule:** StreamLang favors clarity. Expressions return values. Data flows from Left to Right.

## 📦 Variables & Constants

StreamLang is statically typed, but often infers types for you.

### let (Immutable)

Use `let` for values that should never change.

```streamlang
let pi = 3.14159;
// pi = 3.14; // ❌ Error: Cannot assign to constant
```

### var (Mutable)

Use `var` for counters or state that changes over time.

```streamlang
var score = 0;
score = score + 10; // ✅ OK
```

## 🛁 The Pipe Operator

The signature feature of StreamLang. The pipe operator `|>` passes the result of the left expression as the first argument to the function on the right.

Stop writing "inside-out" code. Write it how you read it.

### Syntax

```streamlang
value |> function(arg2, arg3)
```

Is equivalent to:

```streamlang
function(value, arg2, arg3)
```

### Example

Instead of nesting calls:

```streamlang
// The "Old" Way (Hard to read)
print(add(double(add(5, 5)), 80));
```

Use a pipeline:

```streamlang
// The StreamLang Way
5
  |> add(5)    // Becomes 10
  |> double    // Becomes 20
  |> add(80)   // Becomes 100
  |> print;    // Prints 100
```

## ƒ Functions

Functions are first-class citizens. You must define argument types and return types.

### Declaration

Use the `function` keyword.

```streamlang
function add(a: Int, b: Int) -> Int {
    a + b
}
```

### Implicit vs Explicit Return

StreamLang expressions evaluate to a value.

**Implicit:** The last line of a block is automatically returned.

**Explicit:** Use `return` to exit early.

```streamlang
function check(n: Int) -> Int {
    // Early exit
    if n < 0 {
        return -1;
    }
    
    // Implicit return (no 'return' keyword needed)
    n
}
```

### Recursion

Functions can call themselves.

```streamlang
// Factorial Example
function factorial(n: Int) -> Int {
    if n <= 1 {
        1
    } else {
        n * factorial(n - 1)
    }
}
```

## 🔀 Control Flow

### If / Else

`if` statements are expressions. They evaluate to a value.

```streamlang
let age = 18;

// Basic Usage
if age >= 18 {
    print("Adult");
} else {
    print("Minor");
}
```

### While Loops

Standard loop that runs while the condition is true.

```streamlang
var i = 0;
while (i < 3) {
    print(i);
    i = i + 1;
}
```

### For Loops

C-style iteration. Note that the update statement requires a trailing semicolon within the parentheses.

```streamlang
// Prints 0, 2, 4
for (var k = 0; k <= 4; k = k + 2;) {
    print(k);
}
```

## 🧮 Operators & Math

StreamLang respects standard mathematical precedence (PEMDAS).

### Arithmetic

- `+` (Add)
- `-` (Subtract)
- `*` (Multiply)
- `/` (Integer Division)
- `%` (Modulus/Remainder)

```streamlang
// Precedence Example:
// 2 + (3 * 4) - ((5 / 1) % 2)
print(2 + 3 * 4 - 5 / 1 % 2); // Result: 13
```

### Logical & Comparison

- `&&` (AND)
- `||` (OR)
- `!` (NOT)
- `==`, `!=`, `<`, `>`, `<=`, `>=`

```streamlang
// Unary Stacking
print(!!true);  // true
print(-(-10));  // 10
```

## 👻 Scoping & Shadowing

StreamLang supports variable shadowing in nested scopes. A variable declared inside an `if` block or loop with the same name as an outer variable will "shadow" it, but only within that block.

```streamlang
let x = 10;

if true {
    let x = 99; // Shadows the outer 'x'
    print(x);   // Prints 99
}

print(x); // Prints 10 (Original value remains untouched)
```
}
