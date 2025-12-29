import sys
from antlr4 import InputStream, CommonTokenStream
from streamlang.parser.StreamLangLexer import StreamLangLexer
from streamlang.parser.StreamLangParser import StreamLangParser
from streamlang.ast.builder import ASTBuilder
from streamlang.typechecker.checker import TypeChecker
from streamlang.interpreter.interpreter import Interpreter

def run(source_code: str):
    # 1. Lexing (Text -> Tokens)
    input_stream = InputStream(source_code)
    lexer = StreamLangLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # 2. Parsing (Tokens -> Parse Tree)
    parser = StreamLangParser(stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("❌ Syntax Error: Giving up.")
        return

    # 3. AST Building (Parse Tree -> AST)
    builder = ASTBuilder()
    ast = builder.visit(tree)

    # 4. Type Checking (Analysis)
    checker = TypeChecker()
    errors = checker.check(ast)
    if errors:
        for e in errors:
            print(f"❌ {e}")
        return

    # 5. Execution (Run!)
    print("🚀 Running StreamLang...")
    print("--------------------------------")
    interpreter = Interpreter()
    interpreter.interpret(ast)
    print("--------------------------------")
    print("✅ Done.")

if __name__ == '__main__':
    # Check if the user provided a filename
    if len(sys.argv) > 1:
        # User ran: python -m src.streamlang.main sandbox.stream
        filename = sys.argv[1]
        try:
            with open(filename, 'r') as f:
                code = f.read()
            print(f"📂 Reading file: {filename}...")
            run(code)
        except FileNotFoundError:
            print(f"❌ Error: Could not find file '{filename}'")
    else:
        # Default Mode: Run the hardcoded test string
        print("⚠️ No file provided. Running default test code.")
        
        code = """
        function add(a: Int, b: Int) -> Int {
            a + b
        }
        let x = 10
        let result = x |> add(20)
        print("Default Test Result:", result)
        """
        run(code)