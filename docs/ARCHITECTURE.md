# 🏗️ System Architecture

StreamLang is built as a **Tree-Walking Interpreter** using a modular pipeline. Each stage is isolated to ensure the code is valid before it ever reaches the processor.

## 1. The Component Pipeline

Data flows linearly through these three core stages:

- **AST Builder** (`builder.py`): Converts raw text into an Abstract Syntax Tree (AST). This organizes the logic into a structure the computer can understand.
- **Type Checker** (`checker.py`): Performs Static Type Checking. It ensures you aren't trying to add a String to an Int or calling functions that don't exist.
- **Interpreter** (`interpreter.py`): The execution engine. It walks through the validated AST and performs the actual calculations and I/O operations.

## 2. Project Blueprint

The directory structure is organized to separate the language definition from the tools that run it.

```
.
├── CHANGELOG.md
├── docs
│   ├── ARCHITECTURE.md
│   ├── LANGUAGE_GUIDE.md
│   └── QUICK_START.md
├── examples
│   ├── factorial.stream
│   ├── logic.stream
│   └── pipeline.stream
├── grammar
│   └── StreamLang.g4
├── LICENSE
├── pyproject.toml
├── pytest.ini
├── README.md
├── sandbox.stream
├── src
│   ├── streamlang
│   │   ├── ast
│   │   │   ├── builder.py
│   │   │   └── nodes.py
│   │   ├── interpreter
│   │   │   └── interpreter.py
│   │   ├── main.py
│   │   ├── parser
│   │   │   ├── StreamLang.interp
│   │   │   ├── StreamLangLexer.interp
│   │   │   ├── StreamLangLexer.py
│   │   │   ├── StreamLangLexer.tokens
│   │   │   ├── StreamLangListener.py
│   │   │   ├── StreamLangParser.py
│   │   │   ├── StreamLang.tokens
│   │   │   └── StreamLangVisitor.py
│   │   ├── streamlang.egg-info
│   │   │   ├── dependency_links.txt
│   │   │   ├── PKG-INFO
│   │   │   ├── requires.txt
│   │   │   ├── SOURCES.txt
│   │   │   └── top_level.txt
│   │   └── typechecker
│   │       ├── checker.py
│   │       └── symbols.py
├── tests
│   ├── e2e
│   │   ├── basics
│   │   ├── control
│   │   ├── functions
│   │   └── math
│   ├── __init__.py
│   ├── negative
│   │   ├── runtime
│   │   ├── semantics
│   │   └── syntax
│   ├── test_runner.py
│   └── unit

```

## 3. Execution Logic

- **Memory Management**: Uses a parent-child Environment stack to handle variable scoping and shadowing.
- **Pipe Desugaring**: The `|>` operator is rewritten into standard function calls during the Builder phase, keeping the Interpreter simple.
- **Static Safety**: If the Type Checker finds a single error, the program exits with Code 1 before a single line of code is executed.