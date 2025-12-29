from dataclasses import dataclass
from typing import List, Optional, Union

# BASE CLASSES
@dataclass
class ASTNode:
    pass

@dataclass
class Expr(ASTNode):
    pass

@dataclass
class Stmt(ASTNode):
    pass

# TYPES

@dataclass
class TypeAnnotation(ASTNode):
    name: str
    generic_arg : Optional['TypeAnnotation'] = None

    def __repr__(self):
        if self.generic_arg:
            return f"{self.name}<{self.generic_arg}>"
        return self.name

# LITERALS (Atoms)

@dataclass
class IntLit(Expr):
    value: int

@dataclass
class StringLit(Expr):
    value: str

@dataclass
class BoolLit(Expr):
    value: bool

@dataclass
class ListLit(Expr):
    elements: List[Expr]

@dataclass
class VarRef(Expr):
    name: str

# EXPRESSIONS (Logic)

@dataclass
class BinaryExpr(Expr):
    left: Expr
    op : str
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
    else_block: 'Block'

# STATEMENTS & DECLARATIONS

@dataclass
class VarDecl(Stmt):
    name: str
    initializer: Expr

@dataclass
class ExprStmt(Stmt):
    """A wrapper for when an expression is used as a statement."""
    expr: Expr

@dataclass
class Param(ASTNode):
    name: str
    param_type: TypeAnnotation

@dataclass
class Block(ASTNode):
    statements: List[Stmt]
    # The final expression is the implicit return value
    return_expr: Optional[Expr] = None

@dataclass
class FunctionDecl(Stmt):
    name: str
    params: List[Param]
    return_type: TypeAnnotation
    body: Block

@dataclass
class Program(ASTNode):
    declarations: List[Union[FunctionDecl, Stmt]]