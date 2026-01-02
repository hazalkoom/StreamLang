from contextlib import contextmanager
from streamlang.ast import nodes
from streamlang.typechecker.symbols import SymbolTable

class TypeChecker:
    def __init__(self):
        self.scope = SymbolTable()
        self.errors = []
        self.current_return_type = None 

    def check(self, node: nodes.ASTNode):
        self.visit(node)
        return self.errors

    def visit(self, node: nodes.ASTNode):
        if not node: return None
        return getattr(self, f'visit_{type(node).__name__}', self.generic_visit)(node)

    def generic_visit(self, node):
        raise Exception(f"No visit_{type(node).__name__} method defined")

    def error(self, msg: str):
        self.errors.append(f"Type Error: {msg}")

    @contextmanager
    def scoped(self):
        prev, self.scope = self.scope, SymbolTable(parent=self.scope)
        try: yield
        finally: self.scope = prev

    # =========================================================================
    # VISITORS
    # =========================================================================

    def visit_Program(self, node: nodes.Program):
        for decl in node.declarations: self.visit(decl)

    def visit_FunctionDecl(self, node: nodes.FunctionDecl):
        param_types = [p.param_type for p in node.params]
        self.scope.define(node.name, node.return_type, is_mutable=False, params=param_types)
        
        prev_return = self.current_return_type
        self.current_return_type = node.return_type

        with self.scoped():
            for param in node.params:
                self.scope.define(param.name, param.param_type, is_mutable=False)
            self.visit(node.body)

        self.current_return_type = prev_return

    def visit_Block(self, node: nodes.Block):
        with self.scoped():
            last_type = nodes.TypeAnnotation("Unit")
            for stmt in node.statements:
                if res := self.visit(stmt): last_type = res
            
            if node.return_expr:
                last_type = self.visit(node.return_expr)
            return last_type

    def visit_VarDecl(self, node: nodes.VarDecl):
        inferred = self.visit(node.initializer)
        self.scope.define(node.name, inferred, is_mutable=node.is_mutable)
        return inferred

    def visit_AssignStmt(self, node: nodes.AssignStmt):
        if not (symbol := self.scope.resolve(node.name)):
            return self.error(f"Undefined variable '{node.name}'")
        if not symbol.is_mutable:
            return self.error(f"Cannot assign to immutable '{node.name}'.")
        
        if (val_type := self.visit(node.value)).name != symbol.type.name:
            self.error(f"Type Mismatch: {val_type} cannot be assigned to {symbol.type}")

    def visit_ExprStmt(self, node: nodes.ExprStmt): self.visit(node.expr)
    
    def visit_ReturnStmt(self, node: nodes.ReturnStmt):
        val_type = self.visit(node.value) if node.value else nodes.TypeAnnotation("Unit")
        
        if self.current_return_type:
            expected = self.current_return_type.name
            actual = val_type.name
            if expected != actual:
                self.error(f"Return type mismatch: Expected {expected}, got {actual}")

        return nodes.TypeAnnotation("Unit")

    def visit_BreakStmt(self, node: nodes.BreakStmt): return nodes.TypeAnnotation("Unit")

    def visit_WhileStmt(self, node: nodes.WhileStmt):
        if self.visit(node.condition).name != "Bool":
            self.error("While condition must be Bool")
        self.visit(node.body)

    def visit_ForStmt(self, node: nodes.ForStmt):
        with self.scoped():
            if node.initializer: self.visit(node.initializer)
            if node.condition and self.visit(node.condition).name != "Bool":
                self.error("For condition must be Bool")
            if node.step: self.visit(node.step)
            self.visit(node.body)

    # =========================================================================
    # EXPRESSIONS
    # =========================================================================

    def visit_IntLit(self, _): return nodes.TypeAnnotation("Int")
    def visit_StringLit(self, _): return nodes.TypeAnnotation("String")
    def visit_BoolLit(self, _): return nodes.TypeAnnotation("Bool")

    def visit_ListLit(self, node: nodes.ListLit):
        if not node.elements: return nodes.TypeAnnotation("List", nodes.TypeAnnotation("Int"))
        first = self.visit(node.elements[0])
        for e in node.elements[1:]:
            if self.visit(e).name != first.name:
                self.error("List elements must be same type")
        return nodes.TypeAnnotation("List", first)

    def visit_VarRef(self, node: nodes.VarRef):
        if symbol := self.scope.resolve(node.name): return symbol.type
        self.error(f"Undefined variable '{node.name}'")
        return nodes.TypeAnnotation("Unknown")

    def visit_BinaryExpr(self, node: nodes.BinaryExpr):
        left, right = self.visit(node.left), self.visit(node.right)
        
        # FIX: Allow String concatenation
        if node.op == '+':
            if left.name == 'Int' and right.name == 'Int': return nodes.TypeAnnotation("Int")
            if left.name == 'String' and right.name == 'String': return nodes.TypeAnnotation("String")
            self.error(f"Operator '+' requires Ints or Strings, got {left.name} and {right.name}")
            return nodes.TypeAnnotation("Int")

        if node.op in {'-', '*', '/', '%'}:
            if left.name == 'Int' and right.name == 'Int': return nodes.TypeAnnotation("Int")
            self.error(f"Operator '{node.op}' requires Ints")
            return nodes.TypeAnnotation("Int")

        if node.op in {'<', '>', '<=', '>=', '==', '!='}:
            if left.name != right.name: self.error("Type mismatch in comparison")
            return nodes.TypeAnnotation("Bool")
            
        if node.op in {'&&', '||'}:
            if left.name == 'Bool' and right.name == 'Bool': return nodes.TypeAnnotation("Bool")
            self.error("Logic operators require Bools")
        
        return nodes.TypeAnnotation("Bool")

    def visit_UnaryExpr(self, node: nodes.UnaryExpr):
        op_type = self.visit(node.operand)
        if node.op == '-' and op_type.name != 'Int': self.error("Unary '-' requires Int")
        if node.op == '!' and op_type.name != 'Bool': self.error("Unary '!' requires Bool")
        return op_type

    def visit_IfExpr(self, node: nodes.IfExpr):
        if self.visit(node.condition).name != "Bool": self.error("If condition must be Bool")
        
        then_t = self.visit(node.then_block)
        else_t = self.visit(node.else_block) if node.else_block else None
        
        t_name = then_t.name if then_t else "Unit"
        e_name = else_t.name if else_t else "Unit"

        if t_name != e_name:
            self.error(f"If branches mismatch: {t_name} vs {e_name}")
            return nodes.TypeAnnotation("Unknown")
        return then_t

    def visit_FunctionCall(self, node: nodes.FunctionCall):
        arg_types = [self.visit(arg) for arg in node.args]

        if node.func_name == "print": return nodes.TypeAnnotation("Unit")
        
        symbol = self.scope.resolve(node.func_name)
        if not symbol:
            return nodes.TypeAnnotation("Unknown")
        
        if symbol.params is not None:
            if len(arg_types) != len(symbol.params):
                self.error(f"Function '{node.func_name}' expects {len(symbol.params)} args, got {len(arg_types)}")
            else:
                for i, (arg_t, param_t) in enumerate(zip(arg_types, symbol.params)):
                    if arg_t.name != param_t.name:
                        self.error(f"Argument {i+1} mismatch: Expected {param_t}, got {arg_t}")

        return symbol.type