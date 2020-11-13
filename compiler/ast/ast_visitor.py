from abc import ABC, abstractmethod

from .bin_op import BinOp
from .number import Number


class ASTVisitor(ABC):
    @abstractmethod
    def visit_BinOp(self, node):
        pass

    @abstractmethod
    def visit_Number(self, node):
        pass
