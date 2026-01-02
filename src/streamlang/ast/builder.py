from streamlang.parser.StreamLangParser import StreamLangParser
from streamlang.parser.StreamLangVisitor import StreamLangVisitor
from streamlang.ast import nodes

class ASTBuilder(StreamLangVisitor):
    def visitProgram(self, ctx: StreamLangParser.ProgramContext):
        return nodes.Program([self.visit(d) for d in ctx.declaration() if self.visit(d)])

    def visitDeclaration(self, ctx: StreamLangParser.DeclarationContext):
        return self.visit(ctx.getChild(0))

    # =========================================================================
    # FUNCTIONS & BLOCKS
    # =========================================================================

    def visitFunctionDecl(self, ctx: StreamLangParser.FunctionDeclContext):
        params = []
        if ctx.paramList():
            for p in ctx.paramList().param():
                params.append(nodes.Param(p.ID().getText(), self.visit(p.type_())))
        
        return nodes.FunctionDecl(
            name=ctx.ID().getText(),
            params=params,
            return_type=self.visit(ctx.type_()),
            body=self.visit(ctx.block())
        )

    def visitBlock(self, ctx: StreamLangParser.BlockContext):
        statements = []
        return_expr = None
        
        for child in ctx.getChildren():
            if isinstance(child, StreamLangParser.StatementContext):
                statements.append(self.visit(child))
            elif isinstance(child, StreamLangParser.ExprContext):
                return_expr = self.visit(child)
        
        # Handle Implicit Returns (if last stmt is an ExprStmt, unwrap it)
        if return_expr is None and statements and isinstance(statements[-1], nodes.ExprStmt):
            return_expr = statements.pop().expr

        return nodes.Block(statements, return_expr)

    # =========================================================================
    # TYPES & STATEMENTS
    # =========================================================================

    def visitBaseType(self, ctx: StreamLangParser.BaseTypeContext):
        return nodes.TypeAnnotation(ctx.ID().getText())

    def visitGenericType(self, ctx: StreamLangParser.GenericTypeContext):
        return nodes.TypeAnnotation(ctx.ID().getText(), self.visit(ctx.type_()))

    def visitVarDecl(self, ctx: StreamLangParser.VarDeclContext):
        return nodes.VarDecl(
            name=ctx.ID().getText(),
            initializer=self.visit(ctx.expr()),
            is_mutable=(ctx.VAR() is not None)
        )

    def visitAssignStmt(self, ctx: StreamLangParser.AssignStmtContext):
        return nodes.AssignStmt(ctx.ID().getText(), self.visit(ctx.expr()))

    def visitExprStmt(self, ctx: StreamLangParser.ExprStmtContext):
        return nodes.ExprStmt(self.visit(ctx.expr()))

    def visitWhileStmt(self, ctx: StreamLangParser.WhileStmtContext):
        return nodes.WhileStmt(self.visit(ctx.expr()), self.visit(ctx.block()))

    def visitReturnStmt(self, ctx: StreamLangParser.ReturnStmtContext):
        return nodes.ReturnStmt(self.visit(ctx.expr()) if ctx.expr() else None)
    
    def visitBreakStmt(self, ctx: StreamLangParser.BreakStmtContext):
        return nodes.BreakStmt()

    def visitForStmt(self, ctx: StreamLangParser.ForStmtContext):
        # 1. Parse Initializer (VarDecl or AssignStmt)
        init_stmt = None
        if ctx.varDecl(): init_stmt = self.visit(ctx.varDecl())
        elif ctx.assignStmt() and ctx.assignStmt(0).start.tokenIndex < ctx.SEMI(0).symbol.tokenIndex:
             init_stmt = self.visit(ctx.assignStmt(0))

        # Determine "Pivot" Semicolon to find Condition/Step
        pivot_idx = ctx.SEMI(1 if ctx.getChild(2).getText() == ';' else 0).symbol.tokenIndex

        # 2. Parse Condition (Expr before pivot)
        cond_expr = next((self.visit(e) for e in ctx.expr() if e.stop.tokenIndex < pivot_idx), None)
        
        # 3. Parse Step (Assign or Expr after pivot)
        step_stmt = None
        if ctx.assignStmt():
            step_stmt = next((self.visit(a) for a in ctx.assignStmt() if a.start.tokenIndex > pivot_idx), None)
        if not step_stmt and ctx.expr():
            step_stmt = next((self.visit(e) for e in ctx.expr() if e.start.tokenIndex > pivot_idx), None)

        return nodes.ForStmt(init_stmt, cond_expr, step_stmt, self.visit(ctx.block()))
    
    def visitStatement(self, ctx: StreamLangParser.StatementContext):
        res = self.visit(ctx.getChild(0))
        return nodes.ExprStmt(res) if isinstance(res, nodes.Expr) else res

    # =========================================================================
    # EXPRESSIONS
    # =========================================================================

    def _visitBinary(self, ctx, op_text=None):
        """Helper to reduce code duplication for binary operators."""
        return nodes.BinaryExpr(
            left=self.visit(ctx.expr(0)),
            op=op_text or ctx.getChild(1).getText(),
            right=self.visit(ctx.expr(1))
        )

    def visitIntLit(self, ctx: StreamLangParser.IntLitContext):
        return nodes.IntLit(int(ctx.getText()))

    def visitStringLit(self, ctx: StreamLangParser.StringLitContext):
        return nodes.StringLit(ctx.getText()[1:-1])

    def visitBoolLit(self, ctx: StreamLangParser.BoolLitContext):
        return nodes.BoolLit(ctx.getText() == 'true')
    
    def visitListLit(self, ctx: StreamLangParser.ListLitContext):
        elements = [self.visit(e) for e in ctx.exprList().expr()] if ctx.exprList() else []
        return nodes.ListLit(elements)

    def visitVarRef(self, ctx: StreamLangParser.VarRefContext):
        return nodes.VarRef(ctx.getText())

    def visitParenExpr(self, ctx: StreamLangParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitUnaryMinusExpr(self, ctx: StreamLangParser.UnaryMinusExprContext):
        return nodes.UnaryExpr('-', self.visit(ctx.expr()))

    def visitNotExpr(self, ctx: StreamLangParser.NotExprContext):
        return nodes.UnaryExpr('!', self.visit(ctx.expr()))

    # Consolidated Binary Visitors
    def visitAddSubExpr(self, ctx): return self._visitBinary(ctx)
    def visitMulDivModExpr(self, ctx): return self._visitBinary(ctx)
    def visitComparisonExpr(self, ctx): return self._visitBinary(ctx)
    def visitEqualityExpr(self, ctx): return self._visitBinary(ctx)
    def visitLogicalAndExpr(self, ctx): return self._visitBinary(ctx, '&&')
    def visitLogicalOrExpr(self, ctx): return self._visitBinary(ctx, '||')

    def visitFunctionCallExpr(self, ctx: StreamLangParser.FunctionCallExprContext):
        args = [self.visit(arg) for arg in ctx.argList().expr()] if ctx.argList() else []
        return nodes.FunctionCall(ctx.ID().getText(), args)

    def visitPipeExpr(self, ctx: StreamLangParser.PipeExprContext):
        left, right = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        if isinstance(right, nodes.FunctionCall):
            right.args.insert(0, left)
            return right
        elif isinstance(right, nodes.VarRef):
            return nodes.FunctionCall(right.name, args=[left])
        raise Exception("Syntax Error: Pipe must flow into Function or ID.")
    
    def visitIfExpr(self, ctx: StreamLangParser.IfExprContext):
        return nodes.IfExpr(
            condition=self.visit(ctx.expr()),
            then_block=self.visit(ctx.block(0)),
            else_block=self.visit(ctx.block(1)) if ctx.block(1) else None
        )