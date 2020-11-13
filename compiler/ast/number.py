from .ast_node import ASTNode


class Number(ASTNode):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def expand(self):
        pass

    def accept(self, visitor):
        return visitor.visit_Number(self)

    def __repr__(self):
        return "Number[{}]".format(self.value)
