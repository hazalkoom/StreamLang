from dataclasses import dataclass
from typing import Dict, Optional
from streamlang.ast.nodes import TypeAnnotation

@dataclass
class Symbol:
    name: str
    type: TypeAnnotation

class SymbolTable:
    def __init__(self, parent: Optional['SymbolTable'] = None):
        self.symbols: Dict[str, Symbol] = {}
        self.parent = parent

    def define(self, name: str, type_: TypeAnnotation):
        """Define a new variable in the CURRENT scope."""
        self.symbols[name] = Symbol(name, type_)

    def resolve(self, name: str) -> Optional[Symbol]:
        """Look up a variable. If not here, check the parent scope."""
        if name in self.symbols:
            return self.symbols[name]
        
        if self.parent:
            return self.parent.resolve(name)
        
        return None