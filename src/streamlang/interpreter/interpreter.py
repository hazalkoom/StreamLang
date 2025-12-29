from typing import Any, Dict, List, Optional
from streamlang.ast import nodes

class Environment:
    def __init__(self, parent: Optional['Environment'] = None):
        self.values: Dict[str, Any] = {}
        self.parent = parent

    def define(self, name: str, value: Any):
        self.values[name] = value

    def get(self, name: str) -> Any:
        if name in self.values:
            return self.values[name]
        if self.parent:
            return self.parent.get(name)
        raise Exception(f"Runtime Error: Undefined variable '{name}'")

class Interpreter:
    def __init__(self):
        self.global_env = Environment()
        self.current_env = self.global_env
        self.functions: Dict[str, nodes.FunctionDecl] = {}

    def interpret(self, node: nodes.ASTNode):
        try:
            return self.visit(node)
        except Exception as e:
            print(f"🔥 CRASH: {e}")

    def visit(self, node: nodes.ASTNode):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f"No interpreter method defined for {type(node).__name__}")


    # STATEMENTS


    def visit_Program(self, node: nodes.Program):
        # 1. Register all functions first (hoisting)
        for decl in node.declarations:
            if isinstance(decl, nodes.FunctionDecl):
                self.functions[decl.name] = decl
        
        # 2. Execute statements
        for decl in node.declarations:
            if not isinstance(decl, nodes.FunctionDecl):
                self.visit(decl)

    def visit_FunctionDecl(self, node: nodes.FunctionDecl):
        # Already handled in Program visit (hoisting)
        pass

    def visit_VarDecl(self, node: nodes.VarDecl):
        val = self.visit(node.initializer)
        self.current_env.define(node.name, val)

    def visit_ExprStmt(self, node: nodes.ExprStmt):
        self.visit(node.expr)

    def visit_Block(self, node: nodes.Block):
        # 1. SCOPE ENTRY: Save current env, create new child env
        previous_env = self.current_env
        self.current_env = Environment(parent=previous_env)

        try:
            # 2. Execute all statements in this new scope
            for stmt in node.statements:
                self.visit(stmt)
            
            # 3. Handle return expression
            if node.return_expr:
                return self.visit(node.return_expr)
        finally:
            # 4. SCOPE EXIT: Restore the original environment
            self.current_env = previous_env


    # EXPRESSIONS


    def visit_IntLit(self, node: nodes.IntLit):
        return node.value

    def visit_StringLit(self, node: nodes.StringLit):
        return node.value

    def visit_BoolLit(self, node: nodes.BoolLit):
        return node.value

    def visit_ListLit(self, node: nodes.ListLit):
        return [self.visit(e) for e in node.elements]

    def visit_VarRef(self, node: nodes.VarRef):
        return self.current_env.get(node.name)

    def visit_BinaryExpr(self, node: nodes.BinaryExpr):
        left = self.visit(node.left)
        right = self.visit(node.right)

        if node.op == '+': return left + right
        if node.op == '-': return left - right
        if node.op == '*': return left * right
        if node.op == '/': return int(left / right) # Integer division
        if node.op == '%': return left % right
        if node.op == '==': return left == right
        if node.op == '!=': return left != right
        if node.op == '<': return left < right
        if node.op == '>': return left > right
        if node.op == '<=': return left <= right
        if node.op == '>=': return left >= right
        
        raise Exception(f"Unknown operator {node.op}")

    def visit_UnaryExpr(self, node: nodes.UnaryExpr):
        val = self.visit(node.operand)
        
        if node.op == '-':
            return -val
        if node.op == '!':
            return not val
            
        raise Exception(f"Runtime Error: Unknown unary operator {node.op}")

    def visit_FunctionCall(self, node: nodes.FunctionCall):
        # 1. Check for Standard Library calls
        if node.func_name == 'print':
            args = [self.visit(arg) for arg in node.args]
            
            # Formatting: Convert Python 'True' to StreamLang 'true'
            formatted_args = []
            for arg in args:
                if isinstance(arg, bool):
                    formatted_args.append(str(arg).lower())
                else:
                    formatted_args.append(arg)
            
            print(*formatted_args)
            return None

        # 2. Look for user-defined function
        if node.func_name not in self.functions:
            raise Exception(f"Undefined function '{node.func_name}'")
        
        func_def = self.functions[node.func_name]
        
        # 3. Check Argument Count
        if len(node.args) != len(func_def.params):
            raise Exception(f"Function '{node.func_name}' expects {len(func_def.params)} args, got {len(node.args)}")

        # 4. Evaluate Arguments
        arg_values = [self.visit(arg) for arg in node.args]

        # 5. Create New Scope (Closure)
        previous_env = self.current_env
        self.current_env = Environment(parent=self.global_env) # Lexical scoping usually uses global as parent for top-level funcs

        # 6. Bind Arguments to Parameters
        for param, value in zip(func_def.params, arg_values):
            self.current_env.define(param.name, value)

        # 7. Execute Body
        result = self.visit(func_def.body)

        # 8. Restore Scope
        self.current_env = previous_env
        
        return result
    
    def visit_IfExpr(self, node: nodes.IfExpr):
        condition_result = self.visit(node.condition)
        
        if condition_result:
            return self.visit(node.then_block)
        else:
            return self.visit(node.else_block)