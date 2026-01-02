from dataclasses import dataclass

# =============================================================================
# BASE CLASSES
# =============================================================================

@dataclass
class ASTNode: pass
@dataclass
class Expr(ASTNode): pass
@dataclass
class Stmt(ASTNode): pass

# =============================================================================
# TYPES & PARAMETERS
# =============================================================================

@dataclass
class TypeAnnotation(ASTNode):
    name: str
    generic_arg: 'TypeAnnotation | None' = None

    def __repr__(self):
        return f"{self.name}<{self.generic_arg}>" if self.generic_arg else self.name

@dataclass
class Param(ASTNode):
    name: str
    param_type: TypeAnnotation

# =============================================================================
# LITERALS (Values)
# =============================================================================

@dataclass
class IntLit(Expr):    value: int
@dataclass
class StringLit(Expr): value: str
@dataclass
class BoolLit(Expr):   value: bool
@dataclass
class VarRef(Expr):    name: str

@dataclass
class ListLit(Expr):
    elements: list[Expr]

# =============================================================================
# EXPRESSIONS (Logic & Math)
# =============================================================================

@dataclass
class BinaryExpr(Expr):
    left: Expr
    op: str
    right: Expr

@dataclass
class UnaryExpr(Expr):
    op: str
    operand: Expr

@dataclass
class FunctionCall(Expr):
    func_name: str
    args: list[Expr]

@dataclass
class IfExpr(Expr):
    condition: Expr
    then_block: 'Block'
    else_block: 'Block | None' = None

# =============================================================================
# STATEMENTS & DECLARATIONS
# =============================================================================

@dataclass
class ExprStmt(Stmt):
    """Wraps an expression so it can be used as a statement."""
    expr: Expr

@dataclass
class VarDecl(Stmt):
    name: str
    initializer: Expr
    is_mutable: bool 

@dataclass
class AssignStmt(Stmt):
    name: str
    value: Expr

@dataclass
class ReturnStmt(Stmt):
    value: Expr | None

@dataclass
class BreakStmt(Stmt):
    pass

@dataclass
class WhileStmt(Stmt):
    condition: Expr
    body: 'Block'

@dataclass
class ForStmt(Stmt):
    initializer: Stmt | None
    condition: Expr | None
    step: Stmt | Expr | None
    body: 'Block'

# =============================================================================
# STRUCTURES
# =============================================================================

@dataclass
class Block(ASTNode):
    statements: list[Stmt]
    return_expr: Expr | None = None

@dataclass
class FunctionDecl(Stmt):
    name: str
    params: list[Param]
    return_type: TypeAnnotation
    body: Block

@dataclass
class Program(ASTNode):
    declarations: list[FunctionDecl | Stmt]