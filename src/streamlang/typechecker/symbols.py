from dataclasses import dataclass
from streamlang.ast.nodes import TypeAnnotation

@dataclass
class Symbol:
    name: str
    type: TypeAnnotation
    is_mutable: bool
    params: list[TypeAnnotation] | None = None

class SymbolTable:
    def __init__(self, parent: 'SymbolTable | None' = None):
        self.symbols: dict[str, Symbol] = {}
        self.parent = parent

    def define(self, name: str, type_: TypeAnnotation, is_mutable: bool = False, params: list[TypeAnnotation] | None = None):
        """Define a new variable in the CURRENT scope."""
        if name in self.symbols:
            raise Exception(f"Variable '{name}' is already defined in this scope.")
        self.symbols[name] = Symbol(name, type_, is_mutable, params)

    def resolve(self, name: str) -> Symbol | None:
        """Look up a variable. If not here, recursively check parent scopes."""
        return self.symbols.get(name) or (self.parent.resolve(name) if self.parent else None)