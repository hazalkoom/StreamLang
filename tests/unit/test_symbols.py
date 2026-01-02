import pytest
from streamlang.typechecker.symbols import SymbolTable
from streamlang.ast.nodes import TypeAnnotation

# Helper to create a dummy type
def T(name): return TypeAnnotation(name)

def test_symbol_define_and_resolve():
    scope = SymbolTable()
    scope.define("x", T("Int"), is_mutable=False)
    
    sym = scope.resolve("x")
    assert sym is not None
    assert sym.name == "x"
    assert sym.type.name == "Int"

def test_symbol_scope_inheritance():
    # Global Scope
    global_scope = SymbolTable()
    global_scope.define("g", T("String"))
    
    # Local Scope (child of global)
    local_scope = SymbolTable(parent=global_scope)
    local_scope.define("l", T("Int"))
    
    # Child should see Global
    assert local_scope.resolve("g") is not None
    # Global should NOT see Child
    assert global_scope.resolve("l") is None

def test_symbol_shadowing():
    parent = SymbolTable()
    parent.define("x", T("Int"))
    
    child = SymbolTable(parent=parent)
    child.define("x", T("String")) # Shadowing 'x'
    
    # Child sees its own 'x'
    assert child.resolve("x").type.name == "String"
    # Parent still has old 'x'
    assert parent.resolve("x").type.name == "Int"

def test_symbol_redefinition_error():
    scope = SymbolTable()
    scope.define("x", T("Int"))
    
    # Defining 'x' again in SAME scope should crash
    with pytest.raises(Exception) as e:
        scope.define("x", T("Bool"))
    assert "already defined" in str(e.value)