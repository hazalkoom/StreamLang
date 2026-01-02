# Generated from StreamLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .StreamLangParser import StreamLangParser
else:
    from StreamLangParser import StreamLangParser

# This class defines a complete listener for a parse tree produced by StreamLangParser.
class StreamLangListener(ParseTreeListener):

    # Enter a parse tree produced by StreamLangParser#program.
    def enterProgram(self, ctx:StreamLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by StreamLangParser#program.
    def exitProgram(self, ctx:StreamLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by StreamLangParser#declaration.
    def enterDeclaration(self, ctx:StreamLangParser.DeclarationContext):
        pass

    # Exit a parse tree produced by StreamLangParser#declaration.
    def exitDeclaration(self, ctx:StreamLangParser.DeclarationContext):
        pass


    # Enter a parse tree produced by StreamLangParser#functionDecl.
    def enterFunctionDecl(self, ctx:StreamLangParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by StreamLangParser#functionDecl.
    def exitFunctionDecl(self, ctx:StreamLangParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by StreamLangParser#paramList.
    def enterParamList(self, ctx:StreamLangParser.ParamListContext):
        pass

    # Exit a parse tree produced by StreamLangParser#paramList.
    def exitParamList(self, ctx:StreamLangParser.ParamListContext):
        pass


    # Enter a parse tree produced by StreamLangParser#param.
    def enterParam(self, ctx:StreamLangParser.ParamContext):
        pass

    # Exit a parse tree produced by StreamLangParser#param.
    def exitParam(self, ctx:StreamLangParser.ParamContext):
        pass


    # Enter a parse tree produced by StreamLangParser#BaseType.
    def enterBaseType(self, ctx:StreamLangParser.BaseTypeContext):
        pass

    # Exit a parse tree produced by StreamLangParser#BaseType.
    def exitBaseType(self, ctx:StreamLangParser.BaseTypeContext):
        pass


    # Enter a parse tree produced by StreamLangParser#GenericType.
    def enterGenericType(self, ctx:StreamLangParser.GenericTypeContext):
        pass

    # Exit a parse tree produced by StreamLangParser#GenericType.
    def exitGenericType(self, ctx:StreamLangParser.GenericTypeContext):
        pass


    # Enter a parse tree produced by StreamLangParser#statement.
    def enterStatement(self, ctx:StreamLangParser.StatementContext):
        pass

    # Exit a parse tree produced by StreamLangParser#statement.
    def exitStatement(self, ctx:StreamLangParser.StatementContext):
        pass


    # Enter a parse tree produced by StreamLangParser#ifExpr.
    def enterIfExpr(self, ctx:StreamLangParser.IfExprContext):
        pass

    # Exit a parse tree produced by StreamLangParser#ifExpr.
    def exitIfExpr(self, ctx:StreamLangParser.IfExprContext):
        pass


    # Enter a parse tree produced by StreamLangParser#returnStmt.
    def enterReturnStmt(self, ctx:StreamLangParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by StreamLangParser#returnStmt.
    def exitReturnStmt(self, ctx:StreamLangParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by StreamLangParser#breakStmt.
    def enterBreakStmt(self, ctx:StreamLangParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by StreamLangParser#breakStmt.
    def exitBreakStmt(self, ctx:StreamLangParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by StreamLangParser#varDecl.
    def enterVarDecl(self, ctx:StreamLangParser.VarDeclContext):
        pass

    # Exit a parse tree produced by StreamLangParser#varDecl.
    def exitVarDecl(self, ctx:StreamLangParser.VarDeclContext):
        pass


    # Enter a parse tree produced by StreamLangParser#assignStmt.
    def enterAssignStmt(self, ctx:StreamLangParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by StreamLangParser#assignStmt.
    def exitAssignStmt(self, ctx:StreamLangParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by StreamLangParser#exprStmt.
    def enterExprStmt(self, ctx:StreamLangParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by StreamLangParser#exprStmt.
    def exitExprStmt(self, ctx:StreamLangParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by StreamLangParser#whileStmt.
    def enterWhileStmt(self, ctx:StreamLangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by StreamLangParser#whileStmt.
    def exitWhileStmt(self, ctx:StreamLangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by StreamLangParser#forStmt.
    def enterForStmt(self, ctx:StreamLangParser.ForStmtContext):
        pass

    # Exit a parse tree produced by StreamLangParser#forStmt.
    def exitForStmt(self, ctx:StreamLangParser.ForStmtContext):
        pass


    # Enter a parse tree produced by StreamLangParser#block.
    def enterBlock(self, ctx:StreamLangParser.BlockContext):
        pass

    # Exit a parse tree produced by StreamLangParser#block.
    def exitBlock(self, ctx:StreamLangParser.BlockContext):
        pass


    # Enter a parse tree produced by StreamLangParser#VarRef.
    def enterVarRef(self, ctx:StreamLangParser.VarRefContext):
        pass

    # Exit a parse tree produced by StreamLangParser#VarRef.
    def exitVarRef(self, ctx:StreamLangParser.VarRefContext):
        pass


    # Enter a parse tree produced by StreamLangParser#ComparisonExpr.
    def enterComparisonExpr(self, ctx:StreamLangParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by StreamLangParser#ComparisonExpr.
    def exitComparisonExpr(self, ctx:StreamLangParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by StreamLangParser#ListLit.
    def enterListLit(self, ctx:StreamLangParser.ListLitContext):
        pass

    # Exit a parse tree produced by StreamLangParser#ListLit.
    def exitListLit(self, ctx:StreamLangParser.ListLitContext):
        pass


    # Enter a parse tree produced by StreamLangParser#LogicalAndExpr.
    def enterLogicalAndExpr(self, ctx:StreamLangParser.LogicalAndExprContext):
        pass

    # Exit a parse tree produced by StreamLangParser#LogicalAndExpr.
    def exitLogicalAndExpr(self, ctx:StreamLangParser.LogicalAndExprContext):
        pass


    # Enter a parse tree produced by StreamLangParser#StringLit.
    def enterStringLit(self, ctx:StreamLangParser.StringLitContext):
        pass

    # Exit a parse tree produced by StreamLangParser#StringLit.
    def exitStringLit(self, ctx:StreamLangParser.StringLitContext):
        pass


    # Enter a parse tree produced by StreamLangParser#LogicalOrExpr.
    def enterLogicalOrExpr(self, ctx:StreamLangParser.LogicalOrExprContext):
        pass

    # Exit a parse tree produced by StreamLangParser#LogicalOrExpr.
    def exitLogicalOrExpr(self, ctx:StreamLangParser.LogicalOrExprContext):
        pass


    # Enter a parse tree produced by StreamLangParser#FunctionCallExpr.
    def enterFunctionCallExpr(self, ctx:StreamLangParser.FunctionCallExprContext):
        pass

    # Exit a parse tree produced by StreamLangParser#FunctionCallExpr.
    def exitFunctionCallExpr(self, ctx:StreamLangParser.FunctionCallExprContext):
        pass


    # Enter a parse tree produced by StreamLangParser#EqualityExpr.
    def enterEqualityExpr(self, ctx:StreamLangParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by StreamLangParser#EqualityExpr.
    def exitEqualityExpr(self, ctx:StreamLangParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by StreamLangParser#MulDivModExpr.
    def enterMulDivModExpr(self, ctx:StreamLangParser.MulDivModExprContext):
        pass

    # Exit a parse tree produced by StreamLangParser#MulDivModExpr.
    def exitMulDivModExpr(self, ctx:StreamLangParser.MulDivModExprContext):
        pass


    # Enter a parse tree produced by StreamLangParser#PipeExpr.
    def enterPipeExpr(self, ctx:StreamLangParser.PipeExprContext):
        pass

    # Exit a parse tree produced by StreamLangParser#PipeExpr.
    def exitPipeExpr(self, ctx:StreamLangParser.PipeExprContext):
        pass


    # Enter a parse tree produced by StreamLangParser#IfExprAlt.
    def enterIfExprAlt(self, ctx:StreamLangParser.IfExprAltContext):
        pass

    # Exit a parse tree produced by StreamLangParser#IfExprAlt.
    def exitIfExprAlt(self, ctx:StreamLangParser.IfExprAltContext):
        pass


    # Enter a parse tree produced by StreamLangParser#NotExpr.
    def enterNotExpr(self, ctx:StreamLangParser.NotExprContext):
        pass

    # Exit a parse tree produced by StreamLangParser#NotExpr.
    def exitNotExpr(self, ctx:StreamLangParser.NotExprContext):
        pass


    # Enter a parse tree produced by StreamLangParser#ParenExpr.
    def enterParenExpr(self, ctx:StreamLangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by StreamLangParser#ParenExpr.
    def exitParenExpr(self, ctx:StreamLangParser.ParenExprContext):
        pass


    # Enter a parse tree produced by StreamLangParser#IntLit.
    def enterIntLit(self, ctx:StreamLangParser.IntLitContext):
        pass

    # Exit a parse tree produced by StreamLangParser#IntLit.
    def exitIntLit(self, ctx:StreamLangParser.IntLitContext):
        pass


    # Enter a parse tree produced by StreamLangParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:StreamLangParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by StreamLangParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:StreamLangParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by StreamLangParser#BoolLit.
    def enterBoolLit(self, ctx:StreamLangParser.BoolLitContext):
        pass

    # Exit a parse tree produced by StreamLangParser#BoolLit.
    def exitBoolLit(self, ctx:StreamLangParser.BoolLitContext):
        pass


    # Enter a parse tree produced by StreamLangParser#UnaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:StreamLangParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by StreamLangParser#UnaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:StreamLangParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by StreamLangParser#argList.
    def enterArgList(self, ctx:StreamLangParser.ArgListContext):
        pass

    # Exit a parse tree produced by StreamLangParser#argList.
    def exitArgList(self, ctx:StreamLangParser.ArgListContext):
        pass


    # Enter a parse tree produced by StreamLangParser#exprList.
    def enterExprList(self, ctx:StreamLangParser.ExprListContext):
        pass

    # Exit a parse tree produced by StreamLangParser#exprList.
    def exitExprList(self, ctx:StreamLangParser.ExprListContext):
        pass



del StreamLangParser