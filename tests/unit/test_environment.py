import pytest
from streamlang.interpreter.interpreter import Environment

def test_env_define_and_get():
    env = Environment()
    env.define("x", 42)
    assert env.get("x") == 42

def test_env_scope_lookup():
    parent = Environment()
    parent.define("a", 100)
    
    child = Environment(parent=parent)
    child.define("b", 200)
    
    # Child finds parent's variable
    assert child.get("a") == 100
    assert child.get("b") == 200

def test_env_assignment_update():
    env = Environment()
    env.define("x", 10)
    env.assign("x", 20)
    assert env.get("x") == 20

def test_env_assignment_to_parent():
    parent = Environment()
    parent.define("global", 1)
    
    child = Environment(parent=parent)
    # Assigning to 'global' from child should update PARENT
    child.assign("global", 99)
    
    assert parent.get("global") == 99
    assert child.get("global") == 99

def test_env_assign_undefined_error():
    env = Environment()
    with pytest.raises(Exception) as e:
        env.assign("z", 50)
    assert "Undefined variable" in str(e.value)