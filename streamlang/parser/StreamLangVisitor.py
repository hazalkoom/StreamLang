# Generated from grammar/StreamLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .StreamLangParser import StreamLangParser
else:
    from StreamLangParser import StreamLangParser

# This class defines a complete generic visitor for a parse tree produced by StreamLangParser.

class StreamLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StreamLangParser#program.
    def visitProgram(self, ctx:StreamLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#declaration.
    def visitDeclaration(self, ctx:StreamLangParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#functionDecl.
    def visitFunctionDecl(self, ctx:StreamLangParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#paramList.
    def visitParamList(self, ctx:StreamLangParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#param.
    def visitParam(self, ctx:StreamLangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#BaseType.
    def visitBaseType(self, ctx:StreamLangParser.BaseTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#GenericType.
    def visitGenericType(self, ctx:StreamLangParser.GenericTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#statement.
    def visitStatement(self, ctx:StreamLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#varDecl.
    def visitVarDecl(self, ctx:StreamLangParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#exprStmt.
    def visitExprStmt(self, ctx:StreamLangParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#block.
    def visitBlock(self, ctx:StreamLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#VarRef.
    def visitVarRef(self, ctx:StreamLangParser.VarRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#ComparisonExpr.
    def visitComparisonExpr(self, ctx:StreamLangParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#ListLit.
    def visitListLit(self, ctx:StreamLangParser.ListLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#LogicalAndExpr.
    def visitLogicalAndExpr(self, ctx:StreamLangParser.LogicalAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#StringLit.
    def visitStringLit(self, ctx:StreamLangParser.StringLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#LogicalOrExpr.
    def visitLogicalOrExpr(self, ctx:StreamLangParser.LogicalOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#EqualityExpr.
    def visitEqualityExpr(self, ctx:StreamLangParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#FunctionCallExpr.
    def visitFunctionCallExpr(self, ctx:StreamLangParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#MulDivModExpr.
    def visitMulDivModExpr(self, ctx:StreamLangParser.MulDivModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#PipeExpr.
    def visitPipeExpr(self, ctx:StreamLangParser.PipeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#NotExpr.
    def visitNotExpr(self, ctx:StreamLangParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#ParenExpr.
    def visitParenExpr(self, ctx:StreamLangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#IntLit.
    def visitIntLit(self, ctx:StreamLangParser.IntLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:StreamLangParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#IfElseExpr.
    def visitIfElseExpr(self, ctx:StreamLangParser.IfElseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#BoolLit.
    def visitBoolLit(self, ctx:StreamLangParser.BoolLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#UnaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:StreamLangParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#argList.
    def visitArgList(self, ctx:StreamLangParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamLangParser#exprList.
    def visitExprList(self, ctx:StreamLangParser.ExprListContext):
        return self.visitChildren(ctx)



del StreamLangParser