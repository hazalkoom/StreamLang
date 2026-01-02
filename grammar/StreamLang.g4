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
// Format: function name(arg: type) -> type { body }
functionDecl 
    : FN ID '(' paramList? ')' '->' type block 
    ;

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
    | assignStmt
    | ifExpr        
    | whileStmt
    | breakStmt
    | forStmt
    | block
    | returnStmt    
    | exprStmt
    ;


ifExpr
    : IF expr block (ELSE block)?
    ;

// NEW: Top-level rule for Return
returnStmt
    : 'return' expr? ';'
    ;

breakStmt
    : BREAK ';'
    ;

// Variable Declaration
// Covers: let x = 10; OR var y = 20;
varDecl
    : (LET | VAR) ID '=' expr ';'
    ;

// Assignment Statement
// Covers: x = x + 1;
assignStmt
    : ID '=' expr ';'
    ;

// Expression Statement
// Covers: print("hello");
exprStmt
    : expr ';'
    ;

// While Loop
// Covers: while (x < 10) { ... }
whileStmt
    : WHILE '(' expr ')' block
    ;

// For Loop
// Covers: for (var i = 0; i < 10; i = i + 1) { ... }
forStmt
    : FOR '(' (varDecl | assignStmt | ';') expr? ';' (assignStmt | expr)? ')' block
    ;

block
    : '{' statement* expr? '}'
    ;

// Expressions
expr
    : '(' expr ')'                              # ParenExpr
    | ID '(' argList? ')'                       # FunctionCallExpr
    | '-' expr                                  # UnaryMinusExpr
    | '!' expr                                  # NotExpr
    | expr ('*'|'/'|'%') expr                   # MulDivModExpr
    | expr ('+'|'-') expr                       # AddSubExpr
    | expr ('<'|'>'|'<='|'>=') expr             # ComparisonExpr
    | expr ('=='|'!=') expr                     # EqualityExpr
    | expr '&&' expr                            # LogicalAndExpr
    | expr '||' expr                            # LogicalOrExpr
    | expr '|>' expr                            # PipeExpr
    | ifExpr                                    # IfExprAlt  // Uses the shared rule
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
VAR     : 'var';
IF      : 'if';
ELSE    : 'else';
WHILE   : 'while';
FOR     : 'for';
BREAK   : 'break';
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
SEMI    : ';';
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