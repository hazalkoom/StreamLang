# 📝 StreamLang Guide

StreamLang is built for **speed** and **readability**. We focus on how data moves, not how many brackets you can hide it behind.

## 1. Storing Data

### `let`: Constants
Creates a constant. Once you set it, it is locked forever.

```streamlang
let pi = 3.14159;
```

### `var`: Variables
Creates a variable. You can erase and update its value anytime.

```streamlang
var score = 0;
score = 5;
```

## 2. The Pipe Operator (`|>`)

The Pipe is the **heart** of StreamLang. It allows you to write code in the same order that you think. Instead of nesting functions inside each other like a puzzle, you "slide" data through a series of steps.

**The Core Rule:** The value on the left of `|>` becomes the first argument of the function on the right.

### Example 1: Cleaning up Math

**The Ugly Way (Nested):**
```streamlang
print(add(mul(10, 2), 5));
```

**The StreamLang Way:**
```streamlang
10 |> mul(2) |> add(5) |> print;
```

### Example 2: String Pipelines

You can chain as many operations as you want to transform text:

```streamlang
"  hello world  "
  |> trim()
  |> toUpper()
  |> concat("!!!")
  |> print;
// Output: HELLO WORLD!!!
```

### Example 3: Data Processing

Pipes make it easy to see exactly what is happening to your data at every stage:

```streamlang
getUsers()
  |> filter(isActive)
  |> map(getName)
  |> print;
```

## 3. Control Flow

### `if` / `else`
A simple choice. Every `if` must have an `else` because it returns a value.

```streamlang
let result = if (condition) { "yes" } else { "no" };
```

### `while`
Repeats a block of code as long as a condition is true.

```streamlang
var i = 0;
while (i < 10) {
    print(i);
    i = i + 1;
}
```

### `for`
A standard loop for counting or repeating a specific number of times.

```streamlang
for (var i = 0; i < 10; i = i + 1) {
    print(i);
}
```

## 4. Functions

Functions are the machines in your pipeline. Define them with `function`, and always specify what they take and what they return.

```streamlang
function greet(name: String) -> String {
    return "Hello, " + name;
}
```
}
