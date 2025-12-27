# StreamLang V1 Standard Library

**Version**: v0.1-dev
**Status**: Draft

This document defines the built-in functions available in the global scope. These are implemented directly in Python (`src/stdlib.py`).

---

## 1. Math Module

All operations are for the `Int` type only.

| Signature | Description | Error Case |
| :--- | :--- | :--- |
| `add(a: Int, b: Int) -> Int` | Returns `a + b` | - |
| `sub(a: Int, b: Int) -> Int` | Returns `a - b` | - |
| `mul(a: Int, b: Int) -> Int` | Returns `a * b` | - |
| `div(a: Int, b: Int) -> Int` | Returns `a / b` (Integer division) | **RuntimeError**: If `b == 0` |
| `mod(a: Int, b: Int) -> Int` | Returns `a % b` | **RuntimeError**: If `b == 0` |

**Example**:
```streamlang
let x = 10 |> div(2)  // 5
let y = 10 |> div(0)  // Runtime Error
```

---

## 2. String Module

String operations are immutable (return new strings).

| Signature | Description |
| :--- | :--- |
| `length(s: String) -> Int` | Returns number of characters. |
| `toUpper(s: String) -> String` | Converts to uppercase. |
| `toLower(s: String) -> String` | Converts to lowercase. |
| `concat(s1: String, s2: String) -> String` | Concatenates s1 + s2. |

**Example**:
```streamlang
let greeting = "hello" |> toUpper() |> concat(" WORLD")
// Result: "HELLO WORLD"
```

---

## 3. List Module

List functions support internal generics (`<T>`).

| Signature | Description | Error Case |
| :--- | :--- | :--- |
| `length<T>(list: List<T>) -> Int` | Returns element count. | - |
| `head<T>(list: List<T>) -> T` | Returns first element. | **RuntimeError**: If list is empty `[]` |
| `tail<T>(list: List<T>) -> List<T>` | Returns list without first element. | **RuntimeError**: If list is empty `[]` |
| `get<T>(list: List<T>, idx: Int) -> T` | Returns element at index. | **RuntimeError**: If index out of bounds |

### Higher-Order Functions

These functions take other functions as arguments.

| Signature | Description |
| :--- | :--- |
| `map<T, U>(list: List<T>, fn: (T) -> U) -> List<U>` | Applies fn to every element. |
| `filter<T>(list: List<T>, fn: (T) -> Bool) -> List<T>` | Returns elements where fn returns true. |
| `reduce<T, U>(list: List<T>, init: U, fn: (U, T) -> U) -> U` | Accumulates a value. |

**Example**:
```streamlang
fn double(x: Int) -> Int { x * 2 }

let nums = [1, 2, 3] |> map(double)
// Result: [2, 4, 6]
```

---

## 4. I/O Module

Synchronous console output.

| Signature | Description |
| :--- | :--- |
| `print(val: Any) -> Unit` | Prints val to stdout. |
| `println(val: Any) -> Unit` | Prints val + newline to stdout. |