grammar StreamLang;

// ======================================================
// PARSER RULES
// ======================================================

program
    : declaration* EOF
    ;

declaration
    : functionDecl
    | statement
    ;

// Function Definition
functionDecl : FN ID '(' paramList? ')' '->' type block ;

paramList
    : param (',' param)*
    ;

param
    : ID ':' type
    ;

type
    : ID                     # BaseType
    | ID '<' type '>'        # GenericType
    ;

// Statements
statement
    : varDecl
    | exprStmt
    ;

// MISSING RULE 1: Variable Declaration
varDecl
    : 'let' ID '=' expr
    ;

// MISSING RULE 2: Expression Statement
exprStmt
    : expr
    ;

block
    : '{' statement* expr? '}'
    ;

// Expressions
expr
    : '(' expr ')'                              # ParenExpr
    | expr '(' argList? ')'                     # FunctionCallExpr
    | '-' expr                                  # UnaryMinusExpr
    | '!' expr                                  # NotExpr
    | expr ('*'|'/'|'%') expr                   # MulDivModExpr
    | expr ('+'|'-') expr                       # AddSubExpr
    | expr ('<'|'>'|'<='|'>=') expr             # ComparisonExpr
    | expr ('=='|'!=') expr                     # EqualityExpr
    | expr '&&' expr                            # LogicalAndExpr
    | expr '||' expr                            # LogicalOrExpr
    | expr '|>' expr                            # PipeExpr
    | 'if' expr block 'else' block              # IfElseExpr
    | INT                                       # IntLit
    | STRING                                    # StringLit
    | (TRUE | FALSE)                            # BoolLit
    | '[' exprList? ']'                         # ListLit
    | ID                                        # VarRef
    ;

argList
    : expr (',' expr)*
    ;

exprList
    : expr (',' expr)*
    ;

// ======================================================
// LEXER RULES
// ======================================================

FN      : 'function';
LET     : 'let';
IF      : 'if';
ELSE    : 'else';
TRUE    : 'true';
FALSE   : 'false';

LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
LBRACK  : '[';
RBRACK  : ']';
COMMA   : ',';
COLON   : ':';
ARROW   : '->';
ASSIGN  : '=';

PIPE    : '|>';
PLUS    : '+';
MINUS   : '-';
STAR    : '*';
SLASH   : '/';
MOD     : '%';
NOT     : '!';
AND     : '&&';
OR      : '||';
EQ      : '==';
NEQ     : '!=';
LT      : '<';
GT      : '>';
LTE     : '<=';
GTE     : '>=';

ID      : [a-zA-Z_] [a-zA-Z0-9_]*;
INT     : [0-9]+;
STRING  : '"' .*? '"';

// Whitespace
WS      : [ \t\r\n]+ -> skip;
COMMENT : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT : '/*' .*? '*/' -> skip;