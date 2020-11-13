from .ast_visitor import ASTVisitor


class EvalVisitor(ASTVisitor):
    def visit_BinOp(self, node):
        return node.operator(node.left.accept(self), node.right.accept(self))

    def visit_Number(self, node):
        return node.value
