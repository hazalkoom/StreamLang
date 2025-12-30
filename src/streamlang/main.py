import sys
from antlr4 import InputStream, CommonTokenStream
from streamlang.parser.StreamLangLexer import StreamLangLexer
from streamlang.parser.StreamLangParser import StreamLangParser
from streamlang.ast.builder import ASTBuilder
from streamlang.typechecker.checker import TypeChecker
from streamlang.interpreter.interpreter import Interpreter

def run(source_code: str):
    # 1. Lexing
    input_stream = InputStream(source_code)
    lexer = StreamLangLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # 2. Parsing
    parser = StreamLangParser(stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("❌ Syntax Error: Giving up.")
        sys.exit(1)

    # 3. AST Building
    builder = ASTBuilder()
    ast = builder.visit(tree)

    # 4. Type Checking
    checker = TypeChecker()
    errors = checker.check(ast)
    if errors:
        for e in errors:
            print(f"❌ {e}")
        sys.exit(1)

    # 5. Execution
    print("🚀 Running StreamLang...")
    print("-" * 32)
    
    try:
        interpreter = Interpreter()
        interpreter.interpret(ast)
        print("-" * 32)
        print("✅ Done.")
    except Exception as e:
        print("-" * 32)
        print(f"🔥 CRASH: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        try:
            with open(filename, 'r') as f:
                code = f.read()
            run(code)
        except FileNotFoundError:
            print(f"❌ Error: Could not find file '{filename}'")
            sys.exit(1)
    else:
        print("⚠️ No file provided.")