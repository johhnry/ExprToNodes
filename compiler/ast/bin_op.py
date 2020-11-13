import operator

from .ast_node import ASTNode


class BinOp(ASTNode):
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "%": operator.mod,
    }

    blend_ops = {
        "+": "ADD",
        "-": "SUBTRACT",
        "*": "MULTIPLY",
        "/": "DIVIDE",
        "%": "MODULO",
    }

    def __init__(self, op, left, right):
        self.op = op
        self.operator = self.ops[op]
        self.blend_op = self.blend_ops[op]
        self.left = left
        self.right = right

    def expand(self):
        pass

    def accept(self, visitor):
        return visitor.visit_BinOp(self)

    def __repr__(self):
        return "BinOp[{}, {}, {}]".format(self.op, self.left, self.right)
