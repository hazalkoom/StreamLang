import pytest
from streamlang.ast import nodes
from streamlang.typechecker.checker import TypeChecker

# Helper to run check on a node
def check(node):
    checker = TypeChecker()
    checker.visit(node)
    return checker.errors

# --- EXPRESSIONS ---

def test_check_binary_math_valid():
    # 5 + 5
    node = nodes.BinaryExpr(nodes.IntLit(5), '+', nodes.IntLit(5))
    errors = check(node)
    assert len(errors) == 0

def test_check_binary_math_invalid():
    # 5 + true
    node = nodes.BinaryExpr(nodes.IntLit(5), '+', nodes.BoolLit(True))
    errors = check(node)
    assert len(errors) == 1
    assert "requires Ints" in errors[0]

def test_check_logic_valid():
    # true && false
    node = nodes.BinaryExpr(nodes.BoolLit(True), '&&', nodes.BoolLit(False))
    errors = check(node)
    assert len(errors) == 0

def test_check_logic_invalid():
    # true && 5
    node = nodes.BinaryExpr(nodes.BoolLit(True), '&&', nodes.IntLit(5))
    errors = check(node)
    assert len(errors) == 1
    assert "require Bools" in errors[0]

def test_check_comparison_mismatch():
    # 5 > "hello"
    node = nodes.BinaryExpr(nodes.IntLit(5), '>', nodes.StringLit("hello"))
    errors = check(node)
    assert len(errors) == 1
    assert "Type mismatch" in errors[0]

# --- STATEMENTS ---

def test_check_var_decl_type_inference():
    # var x = 10 (Checker should infer x is Int)
    checker = TypeChecker()
    node = nodes.VarDecl("x", nodes.IntLit(10), is_mutable=True)
    checker.visit(node)
    
    # Verify symbol table
    sym = checker.scope.resolve("x")
    assert sym.type.name == "Int"

def test_check_assign_immutable():
    # let x = 10; x = 20;
    checker = TypeChecker()
    checker.visit(nodes.VarDecl("x", nodes.IntLit(10), is_mutable=False))
    
    assign = nodes.AssignStmt("x", nodes.IntLit(20))
    checker.visit(assign)
    
    assert len(checker.errors) == 1
    assert "immutable" in checker.errors[0]

def test_check_if_branch_mismatch():
    # if true { 5 } else { "hello" }
    node = nodes.IfExpr(
        condition=nodes.BoolLit(True),
        then_block=nodes.Block([nodes.ExprStmt(nodes.IntLit(5))], return_expr=nodes.IntLit(5)),
        else_block=nodes.Block([nodes.ExprStmt(nodes.StringLit("s"))], return_expr=nodes.StringLit("s"))
    )
    errors = check(node)
    assert len(errors) == 1
    # FIX: Updated expected string
    assert "If branches mismatch" in errors[0]