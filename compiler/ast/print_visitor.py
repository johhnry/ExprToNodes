from .ast_visitor import ASTVisitor


class PrintVisitor(ASTVisitor):
    def visit_BinOp(self, node):
        return " ".join([node.left.accept(self), node.op, node.right.accept(self)])

    def visit_Number(self, node):
        return str(node.value)
