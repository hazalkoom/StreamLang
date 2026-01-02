import operator
from typing import Any, Dict, Optional
from contextlib import contextmanager
from streamlang.ast import nodes

class BreakException(Exception): pass
class ReturnException(Exception):
    def __init__(self, value: Any): self.value = value

class Environment:
    def __init__(self, parent: Optional['Environment'] = None):
        self.values, self.parent = {}, parent

    def define(self, name: str, value: Any):
        self.values[name] = value

    def assign(self, name: str, value: Any):
        if name in self.values: self.values[name] = value
        elif self.parent: self.parent.assign(name, value)
        else: raise Exception(f"Runtime Error: Undefined variable '{name}'")

    def get(self, name: str) -> Any:
        if name in self.values: return self.values[name]
        if self.parent: return self.parent.get(name)
        raise Exception(f"Runtime Error: Undefined variable '{name}'")

class Interpreter:
    def __init__(self):
        self.global_env = Environment()
        self.current_env = self.global_env
        self.functions: Dict[str, nodes.FunctionDecl] = {}

    def interpret(self, node: nodes.ASTNode): return self.visit(node)

    def visit(self, node: nodes.ASTNode):
        if not node: return None
        return getattr(self, f'visit_{type(node).__name__}', self.generic_visit)(node)

    def generic_visit(self, node):
        raise Exception(f"No interpreter method for {type(node).__name__}")

    @contextmanager
    def scoped(self, env=None):
        prev = self.current_env
        self.current_env = env or Environment(parent=prev)
        try: yield
        finally: self.current_env = prev

    # =========================================================================
    # VISITORS
    # =========================================================================

    def visit_Program(self, node: nodes.Program):
        for decl in node.declarations:
            if isinstance(decl, nodes.FunctionDecl): self.functions[decl.name] = decl
        for decl in node.declarations:
            if not isinstance(decl, nodes.FunctionDecl): self.visit(decl)

    def visit_FunctionDecl(self, _): pass
    def visit_VarDecl(self, node): self.current_env.define(node.name, self.visit(node.initializer))
    def visit_AssignStmt(self, node): self.current_env.assign(node.name, self.visit(node.value))
    def visit_ExprStmt(self, node): self.visit(node.expr)

    def visit_ReturnStmt(self, node: nodes.ReturnStmt):
        raise ReturnException(self.visit(node.value) if node.value else None)
    
    def visit_BreakStmt(self, _): raise BreakException()

    def visit_WhileStmt(self, node: nodes.WhileStmt):
        try:
            while self.visit(node.condition): self.visit(node.body)
        except BreakException: pass

    def visit_ForStmt(self, node: nodes.ForStmt):
        with self.scoped():
            if node.initializer: self.visit(node.initializer)
            try:
                while not node.condition or self.visit(node.condition):
                    self.visit(node.body)
                    if node.step: self.visit(node.step)
            except BreakException: pass

    def visit_Block(self, node: nodes.Block):
        with self.scoped():
            for stmt in node.statements: self.visit(stmt)
            if node.return_expr: return self.visit(node.return_expr)

    # =========================================================================
    # EXPRESSIONS
    # =========================================================================

    def visit_IntLit(self, node): return node.value
    def visit_StringLit(self, node): return node.value
    def visit_BoolLit(self, node): return node.value
    def visit_ListLit(self, node): return [self.visit(e) for e in node.elements]
    def visit_VarRef(self, node): return self.current_env.get(node.name)

    def visit_BinaryExpr(self, node: nodes.BinaryExpr):
        left, right = self.visit(node.left), self.visit(node.right)
        ops = {
            '+': operator.add, '-': operator.sub, '*': operator.mul,
            '/': lambda a, b: int(a / b), '%': operator.mod,
            '==': operator.eq, '!=': operator.ne,
            '<': operator.lt, '>': operator.gt, '<=': operator.le, '>=': operator.ge,
            '&&': lambda a, b: a and b, '||': lambda a, b: a or b
        }
        if node.op in ops: return ops[node.op](left, right)
        raise Exception(f"Unknown operator {node.op}")

    def visit_UnaryExpr(self, node: nodes.UnaryExpr):
        val = self.visit(node.operand)
        if node.op == '-': return -val
        if node.op == '!': return not val
        raise Exception(f"Unknown unary op {node.op}")

    def visit_FunctionCall(self, node: nodes.FunctionCall):
        if node.func_name == 'print':
            args = [self.visit(arg) for arg in node.args]
            print(*(str(a).lower() if isinstance(a, bool) else a for a in args))
            return None

        if node.func_name not in self.functions:
            raise Exception(f"Undefined function '{node.func_name}'")

        func, args = self.functions[node.func_name], [self.visit(a) for a in node.args]
        if len(args) != len(func.params):
            raise Exception(f"Arity mismatch: expected {len(func.params)}, got {len(args)}")

        # Create new env linked to global, define params, run body
        call_env = Environment(parent=self.global_env)
        for param, val in zip(func.params, args): call_env.define(param.name, val)

        try:
            with self.scoped(call_env):
                return self.visit(func.body)
        except ReturnException as e:
            return e.value

    def visit_IfExpr(self, node: nodes.IfExpr):
        if self.visit(node.condition): return self.visit(node.then_block)
        if node.else_block: return self.visit(node.else_block)