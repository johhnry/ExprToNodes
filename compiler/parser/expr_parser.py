from ..ast.bin_op import BinOp
from ..ast.number import Number
from ..lexer.expr_lexer import ExprLexer
from ..ply import yacc


class ExprParser:
    def p_expression_plus(self, p):
        "expression : expression PLUS term"
        p[0] = BinOp("+", p[1], p[3])

    def p_expression_minus(self, p):
        "expression : expression MINUS term"
        p[0] = BinOp("-", p[1], p[3])

    def p_expression_term(self, p):
        "expression : term"
        p[0] = p[1]

    def p_term_times(self, p):
        "term : term TIMES factor"
        p[0] = BinOp("*", p[1], p[3])

    def p_term_div(self, p):
        "term : term DIVIDE factor"
        p[0] = BinOp("/", p[1], p[3])

    def p_term_modulo(self, p):
        "term : term MODULO factor"
        p[0] = BinOp("%", p[1], p[3])

    def p_term_factor(self, p):
        "term : factor"
        p[0] = p[1]

    def p_factor_num(self, p):
        "factor : NUMBER"
        p[0] = Number(p[1])

    def p_factor_expr(self, p):
        "factor : LPAREN expression RPAREN"
        p[0] = p[2]

    def p_error(self, p):
        print("Syntax error in input!")

    def build(self, **kwargs):
        self.lexer = ExprLexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(module=self, **kwargs)

    def parse(self, expr):
        return self.parser.parse(expr)
