import pytest
from streamlang.ast import nodes
from streamlang.interpreter.interpreter import Interpreter, ReturnException

# Helper to run
def run(node):
    interp = Interpreter()
    return interp.visit(node)

# --- MATH & LOGIC ---

def test_eval_binary_math():
    # 10 / 2
    node = nodes.BinaryExpr(nodes.IntLit(10), '/', nodes.IntLit(2))
    assert run(node) == 5

def test_eval_precedence_manual():
    # AST determines precedence, but let's check complex logic
    # true || (false && true) -> true
    # We construct the tree that the parser WOULD produce
    inner = nodes.BinaryExpr(nodes.BoolLit(False), '&&', nodes.BoolLit(True))
    outer = nodes.BinaryExpr(nodes.BoolLit(True), '||', inner)
    assert run(outer) is True

def test_eval_unary():
    assert run(nodes.UnaryExpr('-', nodes.IntLit(5))) == -5
    assert run(nodes.UnaryExpr('!', nodes.BoolLit(True))) is False

# --- CONTROL FLOW ---

def test_eval_if_else():
    # if true { 10 } else { 20 }
    node = nodes.IfExpr(
        condition=nodes.BoolLit(True),
        then_block=nodes.Block([], return_expr=nodes.IntLit(10)),
        else_block=nodes.Block([], return_expr=nodes.IntLit(20))
    )
    assert run(node) == 10

def test_eval_while_loop():
    # var x = 0; while x < 3 { x = x + 1 }
    interp = Interpreter()
    interp.current_env.define("x", 0)
    
    # Condition: x < 3
    cond = nodes.BinaryExpr(nodes.VarRef("x"), '<', nodes.IntLit(3))
    # Body: x = x + 1
    body_stmt = nodes.AssignStmt(
        "x", 
        nodes.BinaryExpr(nodes.VarRef("x"), '+', nodes.IntLit(1))
    )
    loop = nodes.WhileStmt(cond, nodes.Block([body_stmt]))
    
    interp.visit(loop)
    assert interp.current_env.get("x") == 3

# --- FUNCTIONS ---

def test_eval_function_call():
    # Manually define a function in the interpreter
    # function double(n) { return n * 2 }
    interp = Interpreter()
    
    body = nodes.Block([], return_expr=nodes.ReturnStmt(
        nodes.BinaryExpr(nodes.VarRef("n"), '*', nodes.IntLit(2))
    ))
    
    func = nodes.FunctionDecl(
        "double",
        [nodes.Param("n", nodes.TypeAnnotation("Int"))],
        nodes.TypeAnnotation("Int"),
        body
    )
    
    # Register function
    interp.functions["double"] = func
    
    # Call it: double(5)
    call = nodes.FunctionCall("double", [nodes.IntLit(5)])
    assert interp.visit(call) == 10