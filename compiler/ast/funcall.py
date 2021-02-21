import operator

from .ast_node import ASTNode


class FunCall(ASTNode):
    def __init__(self, fun, args):
        self.fun = fun
        self.args = args

    def expand(self):
        pass

    def accept(self, visitor):
        return visitor.visit_FunCall(self)

    def __repr__(self):
        return "FunCall[{}, {}]".format(self.fun, self.args)
