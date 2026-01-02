import pytest
from antlr4 import InputStream, CommonTokenStream
from streamlang.parser.StreamLangLexer import StreamLangLexer
from streamlang.parser.StreamLangParser import StreamLangParser
from streamlang.ast.builder import ASTBuilder
from streamlang.ast import nodes

def build(code):
    """Helper to go from Code -> AST Node"""
    input_stream = InputStream(code)
    lexer = StreamLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = StreamLangParser(stream)
    tree = parser.statement() # Parse as a single statement
    builder = ASTBuilder()
    return builder.visit(tree)

def test_builder_precedence():
    # 1 + 2 * 3
    # Should be: (+ 1 (* 2 3))
    node = build("1 + 2 * 3;")
    
    # Top level is +
    assert isinstance(node.expr, nodes.BinaryExpr)
    assert node.expr.op == '+'
    
    # Right side is *
    assert isinstance(node.expr.right, nodes.BinaryExpr)
    assert node.expr.right.op == '*'

def test_builder_pipe_transformation():
    # "hello" |> print
    # Should become: FunctionCall("print", ["hello"])
    node = build('"hello" |> print;')
    
    call = node.expr
    assert isinstance(call, nodes.FunctionCall)
    assert call.func_name == "print"
    assert len(call.args) == 1
    assert call.args[0].value == "hello"

def test_builder_for_loop_parsing():
    # for (var i = 0; i < 10; i = i + 1) { }
    # This tests that complex 'for' logic in builder.py actually finds the pieces
    code = "for (var i = 0; i < 10; i = i + 1) {}"
    node = build(code)
    
    assert isinstance(node, nodes.ForStmt)
    assert isinstance(node.initializer, nodes.VarDecl)
    assert node.initializer.name == "i"
    assert node.condition.op == '<'
    assert node.step.name == "i"

def test_builder_empty_loop():
    # while true {}
    # Ensures blocks handle empty statements correctly
    node = build("while true {}")
    assert isinstance(node, nodes.WhileStmt)
    assert len(node.body.statements) == 0