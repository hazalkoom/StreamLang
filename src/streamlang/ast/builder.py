from streamlang.parser.StreamLangParser import StreamLangParser
from streamlang.parser.StreamLangVisitor import StreamLangVisitor
from streamlang.ast import nodes

class ASTBuilder(StreamLangVisitor):
    def visitProgram(self, ctx: StreamLangParser.ProgramContext):
        declarations = []
        for decl in ctx.declaration():
            res = self.visit(decl)
            if res: declarations.append(res)
        return nodes.Program(declarations)

    def visitDeclaration(self, ctx: StreamLangParser.DeclarationContext):
        return self.visit(ctx.getChild(0))

    # =========================================================================
    # FUNCTIONS & BLOCKS
    # =========================================================================

    def visitFunctionDecl(self, ctx: StreamLangParser.FunctionDeclContext):
        name = ctx.ID().getText()
        
        # 1. Parse Parameters
        params = []
        if ctx.paramList():
            for p in ctx.paramList().param():
                p_name = p.ID().getText()
                # Visit the type rule
                p_type = self.visit(p.type_())
                params.append(nodes.Param(p_name, p_type))
        
        # 2. Parse Return Type
        return_type = self.visit(ctx.type_())
        
        # 3. Parse Body
        body = self.visit(ctx.block())
        
        return nodes.FunctionDecl(name, params, return_type, body)

    def visitBlock(self, ctx: StreamLangParser.BlockContext):
        statements = []
        return_expr = None
        
        # 1. Collect all statements and the potential trailing expression
        for child in ctx.getChildren():
            if isinstance(child, StreamLangParser.StatementContext):
                stmt = self.visit(child)
                statements.append(stmt)
            elif isinstance(child, StreamLangParser.ExprContext):
                return_expr = self.visit(child)
                
        # 2. THE FIX: Implicit Returns
        # If the parser greedily ate the last expression as a "Statement",
        # we steal it back and make it the "Return Value".
        if return_expr is None and statements:
            last_stmt = statements[-1]
            if isinstance(last_stmt, nodes.ExprStmt):
                # Promote the last ExprStmt to be the return expression
                return_expr = last_stmt.expr
                statements.pop() # Remove it from the statements list

        return nodes.Block(statements, return_expr)

    # =========================================================================
    # TYPES (FIXED FOR YOUR GRAMMAR LABELS)
    # =========================================================================

    # This handles: ID # BaseType
    def visitBaseType(self, ctx: StreamLangParser.BaseTypeContext):
        return nodes.TypeAnnotation(ctx.ID().getText())

    # This handles: ID '<' type '>' # GenericType
    def visitGenericType(self, ctx: StreamLangParser.GenericTypeContext):
        name = ctx.ID().getText()
        inner_type = self.visit(ctx.type_())
        return nodes.TypeAnnotation(name, inner_type)

    # =========================================================================
    # STATEMENTS
    # =========================================================================

    def visitVarDecl(self, ctx: StreamLangParser.VarDeclContext):
        name = ctx.ID().getText()
        initializer = self.visit(ctx.expr())
        return nodes.VarDecl(name, initializer)

    def visitExprStmt(self, ctx: StreamLangParser.ExprStmtContext):
        expr = self.visit(ctx.expr())
        return nodes.ExprStmt(expr)

    # =========================================================================
    # EXPRESSIONS
    # =========================================================================

    def visitIntLit(self, ctx: StreamLangParser.IntLitContext):
        return nodes.IntLit(int(ctx.getText()))

    def visitStringLit(self, ctx: StreamLangParser.StringLitContext):
        raw_text = ctx.getText()
        return nodes.StringLit(raw_text[1:-1])

    def visitBoolLit(self, ctx: StreamLangParser.BoolLitContext):
        return nodes.BoolLit(ctx.getText() == 'true')
    
    def visitListLit(self, ctx: StreamLangParser.ListLitContext):
        elements = []
        if ctx.exprList():
            for e in ctx.exprList().expr():
                elements.append(self.visit(e))
        return nodes.ListLit(elements)

    def visitVarRef(self, ctx: StreamLangParser.VarRefContext):
        return nodes.VarRef(ctx.getText())

    def visitParenExpr(self, ctx: StreamLangParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitAddSubExpr(self, ctx: StreamLangParser.AddSubExprContext):
        return nodes.BinaryExpr(
            left=self.visit(ctx.expr(0)),
            op=ctx.getChild(1).getText(),
            right=self.visit(ctx.expr(1))
        )

    def visitMulDivModExpr(self, ctx: StreamLangParser.MulDivModExprContext):
        return nodes.BinaryExpr(
            left=self.visit(ctx.expr(0)),
            op=ctx.getChild(1).getText(),
            right=self.visit(ctx.expr(1))
        )
    
    def visitComparisonExpr(self, ctx: StreamLangParser.ComparisonExprContext):
        return nodes.BinaryExpr(
            left=self.visit(ctx.expr(0)),
            op=ctx.getChild(1).getText(),
            right=self.visit(ctx.expr(1))
        )

    def visitEqualityExpr(self, ctx: StreamLangParser.EqualityExprContext):
        return nodes.BinaryExpr(
            left=self.visit(ctx.expr(0)),
            op=ctx.getChild(1).getText(),
            right=self.visit(ctx.expr(1))
        )

    def visitFunctionCallExpr(self, ctx: StreamLangParser.FunctionCallExprContext):
        func_expr = self.visit(ctx.expr())
        # In V1, we only allow calling named functions
        if not isinstance(func_expr, nodes.VarRef):
            # Fallback for complex calls (like pipe results)
            # If we can't find a name, it's an error for now
            raise Exception(f"Syntax Error: V1 only supports calling named functions, got {func_expr}")

        args = []
        if ctx.argList():
            for arg in ctx.argList().expr():
                args.append(self.visit(arg))
        
        # Fix the plural 'args' mismatch
        return nodes.FunctionCall(func_expr.name, args)

    def visitPipeExpr(self, ctx: StreamLangParser.PipeExprContext):
        left_node = self.visit(ctx.expr(0))
        right_node = self.visit(ctx.expr(1))

        if isinstance(right_node, nodes.FunctionCall):
            right_node.args.insert(0, left_node)
            return right_node
        
        elif isinstance(right_node, nodes.VarRef):
            return nodes.FunctionCall(right_node.name, args=[left_node])
        
        else:
            raise Exception("Syntax Error: Pipe operator must flow into a Function Call or Identifier.")