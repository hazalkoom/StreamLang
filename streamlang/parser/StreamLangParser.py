# Generated from grammar/StreamLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing import TextIO

def serializedATN():
    return [
        4,1,37,167,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,5,0,
        28,8,0,10,0,12,0,31,9,0,1,0,1,0,1,1,1,1,3,1,37,8,1,1,2,1,2,1,2,1,
        2,3,2,43,8,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,53,8,3,10,3,12,
        3,56,9,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,68,8,5,1,6,
        1,6,3,6,72,8,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,5,9,83,8,9,10,
        9,12,9,86,9,9,1,9,3,9,89,8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,3,10,113,8,10,1,10,1,10,3,10,117,8,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,143,8,10,1,10,5,10,146,8,
        10,10,10,12,10,149,9,10,1,11,1,11,1,11,5,11,154,8,11,10,11,12,11,
        157,9,11,1,12,1,12,1,12,5,12,162,8,12,10,12,12,12,165,9,12,1,12,
        0,1,20,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,5,1,0,5,6,1,0,20,22,
        1,0,18,19,1,0,28,31,1,0,26,27,181,0,29,1,0,0,0,2,36,1,0,0,0,4,38,
        1,0,0,0,6,49,1,0,0,0,8,57,1,0,0,0,10,67,1,0,0,0,12,71,1,0,0,0,14,
        73,1,0,0,0,16,78,1,0,0,0,18,80,1,0,0,0,20,116,1,0,0,0,22,150,1,0,
        0,0,24,158,1,0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,31,1,0,0,0,29,
        27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,29,1,0,0,0,32,33,5,0,0,
        1,33,1,1,0,0,0,34,37,3,4,2,0,35,37,3,12,6,0,36,34,1,0,0,0,36,35,
        1,0,0,0,37,3,1,0,0,0,38,39,5,1,0,0,39,40,5,32,0,0,40,42,5,7,0,0,
        41,43,3,6,3,0,42,41,1,0,0,0,42,43,1,0,0,0,43,44,1,0,0,0,44,45,5,
        8,0,0,45,46,5,15,0,0,46,47,3,10,5,0,47,48,3,18,9,0,48,5,1,0,0,0,
        49,54,3,8,4,0,50,51,5,13,0,0,51,53,3,8,4,0,52,50,1,0,0,0,53,56,1,
        0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,7,1,0,0,0,56,54,1,0,0,0,57,
        58,5,32,0,0,58,59,5,14,0,0,59,60,3,10,5,0,60,9,1,0,0,0,61,68,5,32,
        0,0,62,63,5,32,0,0,63,64,5,28,0,0,64,65,3,10,5,0,65,66,5,29,0,0,
        66,68,1,0,0,0,67,61,1,0,0,0,67,62,1,0,0,0,68,11,1,0,0,0,69,72,3,
        14,7,0,70,72,3,16,8,0,71,69,1,0,0,0,71,70,1,0,0,0,72,13,1,0,0,0,
        73,74,5,2,0,0,74,75,5,32,0,0,75,76,5,16,0,0,76,77,3,20,10,0,77,15,
        1,0,0,0,78,79,3,20,10,0,79,17,1,0,0,0,80,84,5,9,0,0,81,83,3,12,6,
        0,82,81,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,88,
        1,0,0,0,86,84,1,0,0,0,87,89,3,20,10,0,88,87,1,0,0,0,88,89,1,0,0,
        0,89,90,1,0,0,0,90,91,5,10,0,0,91,19,1,0,0,0,92,93,6,10,-1,0,93,
        94,5,7,0,0,94,95,3,20,10,0,95,96,5,8,0,0,96,117,1,0,0,0,97,98,5,
        19,0,0,98,117,3,20,10,15,99,100,5,23,0,0,100,117,3,20,10,14,101,
        102,5,3,0,0,102,103,3,20,10,0,103,104,3,18,9,0,104,105,5,4,0,0,105,
        106,3,18,9,0,106,117,1,0,0,0,107,117,5,33,0,0,108,117,5,34,0,0,109,
        117,7,0,0,0,110,112,5,11,0,0,111,113,3,24,12,0,112,111,1,0,0,0,112,
        113,1,0,0,0,113,114,1,0,0,0,114,117,5,12,0,0,115,117,5,32,0,0,116,
        92,1,0,0,0,116,97,1,0,0,0,116,99,1,0,0,0,116,101,1,0,0,0,116,107,
        1,0,0,0,116,108,1,0,0,0,116,109,1,0,0,0,116,110,1,0,0,0,116,115,
        1,0,0,0,117,147,1,0,0,0,118,119,10,13,0,0,119,120,7,1,0,0,120,146,
        3,20,10,14,121,122,10,12,0,0,122,123,7,2,0,0,123,146,3,20,10,13,
        124,125,10,11,0,0,125,126,7,3,0,0,126,146,3,20,10,12,127,128,10,
        10,0,0,128,129,7,4,0,0,129,146,3,20,10,11,130,131,10,9,0,0,131,132,
        5,24,0,0,132,146,3,20,10,10,133,134,10,8,0,0,134,135,5,25,0,0,135,
        146,3,20,10,9,136,137,10,7,0,0,137,138,5,17,0,0,138,146,3,20,10,
        8,139,140,10,16,0,0,140,142,5,7,0,0,141,143,3,22,11,0,142,141,1,
        0,0,0,142,143,1,0,0,0,143,144,1,0,0,0,144,146,5,8,0,0,145,118,1,
        0,0,0,145,121,1,0,0,0,145,124,1,0,0,0,145,127,1,0,0,0,145,130,1,
        0,0,0,145,133,1,0,0,0,145,136,1,0,0,0,145,139,1,0,0,0,146,149,1,
        0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,21,1,0,0,0,149,147,1,0,
        0,0,150,155,3,20,10,0,151,152,5,13,0,0,152,154,3,20,10,0,153,151,
        1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,23,1,
        0,0,0,157,155,1,0,0,0,158,163,3,20,10,0,159,160,5,13,0,0,160,162,
        3,20,10,0,161,159,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,
        1,0,0,0,164,25,1,0,0,0,165,163,1,0,0,0,15,29,36,42,54,67,71,84,88,
        112,116,142,145,147,155,163
    ]

class StreamLangParser ( Parser ):

    grammarFileName = "StreamLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'function'", "'let'", "'if'", "'else'", 
                     "'true'", "'false'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "','", "':'", "'->'", "'='", "'|>'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='" ]

    symbolicNames = [ "<INVALID>", "FN", "LET", "IF", "ELSE", "TRUE", "FALSE", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "COMMA", "COLON", "ARROW", "ASSIGN", "PIPE", 
                      "PLUS", "MINUS", "STAR", "SLASH", "MOD", "NOT", "AND", 
                      "OR", "EQ", "NEQ", "LT", "GT", "LTE", "GTE", "ID", 
                      "INT", "STRING", "WS", "COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_functionDecl = 2
    RULE_paramList = 3
    RULE_param = 4
    RULE_type = 5
    RULE_statement = 6
    RULE_varDecl = 7
    RULE_exprStmt = 8
    RULE_block = 9
    RULE_expr = 10
    RULE_argList = 11
    RULE_exprList = 12

    ruleNames =  [ "program", "declaration", "functionDecl", "paramList", 
                   "param", "type", "statement", "varDecl", "exprStmt", 
                   "block", "expr", "argList", "exprList" ]

    EOF = Token.EOF
    FN=1
    LET=2
    IF=3
    ELSE=4
    TRUE=5
    FALSE=6
    LPAREN=7
    RPAREN=8
    LBRACE=9
    RBRACE=10
    LBRACK=11
    RBRACK=12
    COMMA=13
    COLON=14
    ARROW=15
    ASSIGN=16
    PIPE=17
    PLUS=18
    MINUS=19
    STAR=20
    SLASH=21
    MOD=22
    NOT=23
    AND=24
    OR=25
    EQ=26
    NEQ=27
    LT=28
    GT=29
    LTE=30
    GTE=31
    ID=32
    INT=33
    STRING=34
    WS=35
    COMMENT=36
    BLOCK_COMMENT=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(StreamLangParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StreamLangParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(StreamLangParser.DeclarationContext,i)


        def getRuleIndex(self):
            return StreamLangParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = StreamLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 30073686254) != 0):
                self.state = 26
                self.declaration()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(StreamLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDecl(self):
            return self.getTypedRuleContext(StreamLangParser.FunctionDeclContext,0)


        def statement(self):
            return self.getTypedRuleContext(StreamLangParser.StatementContext,0)


        def getRuleIndex(self):
            return StreamLangParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = StreamLangParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.functionDecl()
                pass
            elif token in [2, 3, 5, 6, 7, 11, 19, 23, 32, 33, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FN(self):
            return self.getToken(StreamLangParser.FN, 0)

        def ID(self):
            return self.getToken(StreamLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(StreamLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(StreamLangParser.RPAREN, 0)

        def ARROW(self):
            return self.getToken(StreamLangParser.ARROW, 0)

        def type_(self):
            return self.getTypedRuleContext(StreamLangParser.TypeContext,0)


        def block(self):
            return self.getTypedRuleContext(StreamLangParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(StreamLangParser.ParamListContext,0)


        def getRuleIndex(self):
            return StreamLangParser.RULE_functionDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = StreamLangParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(StreamLangParser.FN)
            self.state = 39
            self.match(StreamLangParser.ID)
            self.state = 40
            self.match(StreamLangParser.LPAREN)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 41
                self.paramList()


            self.state = 44
            self.match(StreamLangParser.RPAREN)
            self.state = 45
            self.match(StreamLangParser.ARROW)
            self.state = 46
            self.type_()
            self.state = 47
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StreamLangParser.ParamContext)
            else:
                return self.getTypedRuleContext(StreamLangParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(StreamLangParser.COMMA)
            else:
                return self.getToken(StreamLangParser.COMMA, i)

        def getRuleIndex(self):
            return StreamLangParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = StreamLangParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.param()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 50
                self.match(StreamLangParser.COMMA)
                self.state = 51
                self.param()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(StreamLangParser.ID, 0)

        def COLON(self):
            return self.getToken(StreamLangParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(StreamLangParser.TypeContext,0)


        def getRuleIndex(self):
            return StreamLangParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = StreamLangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(StreamLangParser.ID)
            self.state = 58
            self.match(StreamLangParser.COLON)
            self.state = 59
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return StreamLangParser.RULE_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class GenericTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(StreamLangParser.ID, 0)
        def LT(self):
            return self.getToken(StreamLangParser.LT, 0)
        def type_(self):
            return self.getTypedRuleContext(StreamLangParser.TypeContext,0)

        def GT(self):
            return self.getToken(StreamLangParser.GT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGenericType" ):
                return visitor.visitGenericType(self)
            else:
                return visitor.visitChildren(self)


    class BaseTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(StreamLangParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseType" ):
                return visitor.visitBaseType(self)
            else:
                return visitor.visitChildren(self)



    def type_(self):

        localctx = StreamLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = StreamLangParser.BaseTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(StreamLangParser.ID)
                pass

            elif la_ == 2:
                localctx = StreamLangParser.GenericTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(StreamLangParser.ID)
                self.state = 63
                self.match(StreamLangParser.LT)
                self.state = 64
                self.type_()
                self.state = 65
                self.match(StreamLangParser.GT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(StreamLangParser.VarDeclContext,0)


        def exprStmt(self):
            return self.getTypedRuleContext(StreamLangParser.ExprStmtContext,0)


        def getRuleIndex(self):
            return StreamLangParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = StreamLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.varDecl()
                pass
            elif token in [3, 5, 6, 7, 11, 19, 23, 32, 33, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.exprStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(StreamLangParser.LET, 0)

        def ID(self):
            return self.getToken(StreamLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(StreamLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(StreamLangParser.ExprContext,0)


        def getRuleIndex(self):
            return StreamLangParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = StreamLangParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(StreamLangParser.LET)
            self.state = 74
            self.match(StreamLangParser.ID)
            self.state = 75
            self.match(StreamLangParser.ASSIGN)
            self.state = 76
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(StreamLangParser.ExprContext,0)


        def getRuleIndex(self):
            return StreamLangParser.RULE_exprStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)




    def exprStmt(self):

        localctx = StreamLangParser.ExprStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exprStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(StreamLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(StreamLangParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StreamLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(StreamLangParser.StatementContext,i)


        def expr(self):
            return self.getTypedRuleContext(StreamLangParser.ExprContext,0)


        def getRuleIndex(self):
            return StreamLangParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = StreamLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(StreamLangParser.LBRACE)
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 81
                    self.statement() 
                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30073686248) != 0):
                self.state = 87
                self.expr(0)


            self.state = 90
            self.match(StreamLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return StreamLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VarRefContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(StreamLangParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarRef" ):
                return visitor.visitVarRef(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StreamLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(StreamLangParser.ExprContext,i)

        def LT(self):
            return self.getToken(StreamLangParser.LT, 0)
        def GT(self):
            return self.getToken(StreamLangParser.GT, 0)
        def LTE(self):
            return self.getToken(StreamLangParser.LTE, 0)
        def GTE(self):
            return self.getToken(StreamLangParser.GTE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpr" ):
                return visitor.visitComparisonExpr(self)
            else:
                return visitor.visitChildren(self)


    class ListLitContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACK(self):
            return self.getToken(StreamLangParser.LBRACK, 0)
        def RBRACK(self):
            return self.getToken(StreamLangParser.RBRACK, 0)
        def exprList(self):
            return self.getTypedRuleContext(StreamLangParser.ExprListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListLit" ):
                return visitor.visitListLit(self)
            else:
                return visitor.visitChildren(self)


    class LogicalAndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StreamLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(StreamLangParser.ExprContext,i)

        def AND(self):
            return self.getToken(StreamLangParser.AND, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpr" ):
                return visitor.visitLogicalAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class StringLitContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(StreamLangParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLit" ):
                return visitor.visitStringLit(self)
            else:
                return visitor.visitChildren(self)


    class LogicalOrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StreamLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(StreamLangParser.ExprContext,i)

        def OR(self):
            return self.getToken(StreamLangParser.OR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpr" ):
                return visitor.visitLogicalOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqualityExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StreamLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(StreamLangParser.ExprContext,i)

        def EQ(self):
            return self.getToken(StreamLangParser.EQ, 0)
        def NEQ(self):
            return self.getToken(StreamLangParser.NEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpr" ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(StreamLangParser.ExprContext,0)

        def LPAREN(self):
            return self.getToken(StreamLangParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(StreamLangParser.RPAREN, 0)
        def argList(self):
            return self.getTypedRuleContext(StreamLangParser.ArgListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpr" ):
                return visitor.visitFunctionCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivModExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StreamLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(StreamLangParser.ExprContext,i)

        def STAR(self):
            return self.getToken(StreamLangParser.STAR, 0)
        def SLASH(self):
            return self.getToken(StreamLangParser.SLASH, 0)
        def MOD(self):
            return self.getToken(StreamLangParser.MOD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivModExpr" ):
                return visitor.visitMulDivModExpr(self)
            else:
                return visitor.visitChildren(self)


    class PipeExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StreamLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(StreamLangParser.ExprContext,i)

        def PIPE(self):
            return self.getToken(StreamLangParser.PIPE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPipeExpr" ):
                return visitor.visitPipeExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(StreamLangParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(StreamLangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(StreamLangParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(StreamLangParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(StreamLangParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntLitContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(StreamLangParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLit" ):
                return visitor.visitIntLit(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StreamLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(StreamLangParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(StreamLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(StreamLangParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class IfElseExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(StreamLangParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(StreamLangParser.ExprContext,0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StreamLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(StreamLangParser.BlockContext,i)

        def ELSE(self):
            return self.getToken(StreamLangParser.ELSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElseExpr" ):
                return visitor.visitIfElseExpr(self)
            else:
                return visitor.visitChildren(self)


    class BoolLitContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(StreamLangParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(StreamLangParser.FALSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolLit" ):
                return visitor.visitBoolLit(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a StreamLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(StreamLangParser.MINUS, 0)
        def expr(self):
            return self.getTypedRuleContext(StreamLangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinusExpr" ):
                return visitor.visitUnaryMinusExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = StreamLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = StreamLangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 93
                self.match(StreamLangParser.LPAREN)
                self.state = 94
                self.expr(0)
                self.state = 95
                self.match(StreamLangParser.RPAREN)
                pass
            elif token in [19]:
                localctx = StreamLangParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 97
                self.match(StreamLangParser.MINUS)
                self.state = 98
                self.expr(15)
                pass
            elif token in [23]:
                localctx = StreamLangParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 99
                self.match(StreamLangParser.NOT)
                self.state = 100
                self.expr(14)
                pass
            elif token in [3]:
                localctx = StreamLangParser.IfElseExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 101
                self.match(StreamLangParser.IF)
                self.state = 102
                self.expr(0)
                self.state = 103
                self.block()
                self.state = 104
                self.match(StreamLangParser.ELSE)
                self.state = 105
                self.block()
                pass
            elif token in [33]:
                localctx = StreamLangParser.IntLitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.match(StreamLangParser.INT)
                pass
            elif token in [34]:
                localctx = StreamLangParser.StringLitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(StreamLangParser.STRING)
                pass
            elif token in [5, 6]:
                localctx = StreamLangParser.BoolLitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 109
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [11]:
                localctx = StreamLangParser.ListLitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 110
                self.match(StreamLangParser.LBRACK)
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30073686248) != 0):
                    self.state = 111
                    self.exprList()


                self.state = 114
                self.match(StreamLangParser.RBRACK)
                pass
            elif token in [32]:
                localctx = StreamLangParser.VarRefContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                self.match(StreamLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 145
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = StreamLangParser.MulDivModExprContext(self, StreamLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 118
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 119
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 120
                        self.expr(14)
                        pass

                    elif la_ == 2:
                        localctx = StreamLangParser.AddSubExprContext(self, StreamLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 121
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 122
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 123
                        self.expr(13)
                        pass

                    elif la_ == 3:
                        localctx = StreamLangParser.ComparisonExprContext(self, StreamLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 124
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 125
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4026531840) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 126
                        self.expr(12)
                        pass

                    elif la_ == 4:
                        localctx = StreamLangParser.EqualityExprContext(self, StreamLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 127
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 128
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 129
                        self.expr(11)
                        pass

                    elif la_ == 5:
                        localctx = StreamLangParser.LogicalAndExprContext(self, StreamLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 130
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 131
                        self.match(StreamLangParser.AND)
                        self.state = 132
                        self.expr(10)
                        pass

                    elif la_ == 6:
                        localctx = StreamLangParser.LogicalOrExprContext(self, StreamLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 133
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 134
                        self.match(StreamLangParser.OR)
                        self.state = 135
                        self.expr(9)
                        pass

                    elif la_ == 7:
                        localctx = StreamLangParser.PipeExprContext(self, StreamLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 136
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 137
                        self.match(StreamLangParser.PIPE)
                        self.state = 138
                        self.expr(8)
                        pass

                    elif la_ == 8:
                        localctx = StreamLangParser.FunctionCallExprContext(self, StreamLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 139
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 140
                        self.match(StreamLangParser.LPAREN)
                        self.state = 142
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30073686248) != 0):
                            self.state = 141
                            self.argList()


                        self.state = 144
                        self.match(StreamLangParser.RPAREN)
                        pass

             
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StreamLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(StreamLangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(StreamLangParser.COMMA)
            else:
                return self.getToken(StreamLangParser.COMMA, i)

        def getRuleIndex(self):
            return StreamLangParser.RULE_argList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = StreamLangParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.expr(0)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 151
                self.match(StreamLangParser.COMMA)
                self.state = 152
                self.expr(0)
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StreamLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(StreamLangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(StreamLangParser.COMMA)
            else:
                return self.getToken(StreamLangParser.COMMA, i)

        def getRuleIndex(self):
            return StreamLangParser.RULE_exprList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = StreamLangParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.expr(0)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 159
                self.match(StreamLangParser.COMMA)
                self.state = 160
                self.expr(0)
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 16)
         




