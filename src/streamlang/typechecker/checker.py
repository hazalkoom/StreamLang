from streamlang.ast import nodes
from streamlang.typechecker.symbols import SymbolTable

class TypeChecker:
    def __init__(self):
        self.scope = SymbolTable()  # Global scope
        self.errors = []

    def check(self, node: nodes.ASTNode):
        """Entry point for checking the AST."""
        self.visit(node)
        return self.errors

    def visit(self, node: nodes.ASTNode):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f"No visit_{type(node).__name__} method defined")

    def error(self, message: str):
        self.errors.append(f"Type Error: {message}")


    # VISITOR METHODS


    def visit_Program(self, node: nodes.Program):
        for decl in node.declarations:
            self.visit(decl)

    def visit_FunctionDecl(self, node: nodes.FunctionDecl):
        # 1. Define function in current scope (so it can be called recursively)
        # Note: In V1 we treat function names as variables with special types? 
        # Actually, for V1 simplicity, we just won't type-check the *call* to the function itself strictly yet,
        # but we MUST enter a new scope for the body.
        
        self.scope.define(node.name, node.return_type)

        # 2. Create new scope for function body
        previous_scope = self.scope
        self.scope = SymbolTable(parent=previous_scope)

        # 3. Define parameters in the local scope
        for param in node.params:
            self.scope.define(param.name, param.param_type)

        # 4. Check the body
        self.visit(node.body)

        # 5. Restore scope
        self.scope = previous_scope

    def visit_Block(self, node: nodes.Block):
        for stmt in node.statements:
            self.visit(stmt)
        
        if node.return_expr:
            return self.visit(node.return_expr)

    def visit_VarDecl(self, node: nodes.VarDecl):
        # Infer type from the initializer expression
        inferred_type = self.visit(node.initializer)
        
        # Save it to the symbol table
        self.scope.define(node.name, inferred_type)
        return inferred_type

    def visit_ExprStmt(self, node: nodes.ExprStmt):
        self.visit(node.expr)


    # EXPRESSIONS (Must return a TypeAnnotation)


    def visit_IntLit(self, node: nodes.IntLit):
        return nodes.TypeAnnotation("Int")

    def visit_StringLit(self, node: nodes.StringLit):
        return nodes.TypeAnnotation("String")

    def visit_BoolLit(self, node: nodes.BoolLit):
        return nodes.TypeAnnotation("Bool")

    def visit_ListLit(self, node: nodes.ListLit):
        # Assume homogeneous lists (all elements same type)
        if not node.elements:
            # Empty list generic problem... default to List<Any> or Error?
            # For V1, let's say List<Int> default for now or error.
            return nodes.TypeAnnotation("List", nodes.TypeAnnotation("Int"))
            
        first_type = self.visit(node.elements[0])
        for e in node.elements[1:]:
            this_type = self.visit(e)
            if this_type.name != first_type.name:
                self.error(f"List elements must be same type. Found {first_type} and {this_type}")
        
        return nodes.TypeAnnotation("List", first_type)

    def visit_VarRef(self, node: nodes.VarRef):
        symbol = self.scope.resolve(node.name)
        if not symbol:
            self.error(f"Undefined variable '{node.name}'")
            return nodes.TypeAnnotation("Unknown")
        return symbol.type

    def visit_BinaryExpr(self, node: nodes.BinaryExpr):
        left_type = self.visit(node.left)
        right_type = self.visit(node.right)

        # Math Logic
        if node.op in ['+', '-', '*', '/', '%']:
            if left_type.name == 'Int' and right_type.name == 'Int':
                return nodes.TypeAnnotation("Int")
            else:
                self.error(f"Operator '{node.op}' requires Ints, got {left_type} and {right_type}")
                return nodes.TypeAnnotation("Int") # Return dummy to prevent cascade

        # Comparison Logic
        if node.op in ['<', '>', '<=', '>=', '==', '!=']:
            if left_type.name != right_type.name:
                self.error(f"Cannot compare {left_type} with {right_type}")
            return nodes.TypeAnnotation("Bool")
            
        return nodes.TypeAnnotation("Unknown")
    
    def visit_UnaryExpr(self, node: nodes.UnaryExpr):
        type_obj = self.visit(node.operand)
        
        if node.op == '-':
            if type_obj.name != 'Int':
                self.error(f"Cannot use '-' on type {type_obj.name}")
            return type_obj
            
        if node.op == '!':
            if type_obj.name != 'Bool':
                self.error(f"Cannot use '!' on type {type_obj.name}")
            return type_obj
            
        return type_obj

    def visit_IfExpr(self, node: nodes.IfExpr):
        # 1. Check Condition (Must be Bool)
        cond_type = self.visit(node.condition)
        if cond_type.name != "Bool":
            self.error(f"If condition must be Bool, got {cond_type}")

        # 2. Check Both Branches
        then_type = self.visit(node.then_block)
        else_type = self.visit(node.else_block)

        # 3. Handle Void/None types (if a block is empty)
        then_name = then_type.name if then_type else "Void"
        else_name = else_type.name if else_type else "Void"

        # 4. Ensure branches match
        if then_name != else_name:
            self.error(f"If branches must return same type. Got {then_name} and {else_name}")
            return nodes.TypeAnnotation("Unknown")
            
        return then_type

    def visit_FunctionCall(self, node: nodes.FunctionCall):
        # In a real compiler, we would look up the function definition and check args.
        # For V1 MVP, we will assume standard library functions exist.
        
        # Hardcoded StdLib checks for now (Refactor later!)
        if node.func_name == "print":
            return nodes.TypeAnnotation("Unit")
        
        symbol = self.scope.resolve(node.func_name)
        if not symbol:
            # We assume it's a global function we haven't checked or stdlib
            # In V2 we fix this. For now, trust the user or return Unknown.
            return nodes.TypeAnnotation("Unknown")
            
        return symbol.type