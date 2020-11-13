from ..ply import lex


class ExprLexer:
    # List of tokens to parse
    tokens = (
        "NUMBER",
        "PLUS",
        "MINUS",
        "TIMES",
        "DIVIDE",
        "LPAREN",
        "RPAREN",
        "MODULO",
    )

    # Regular expressions
    t_PLUS = r"\+"
    t_MINUS = r"-"
    t_TIMES = r"\*"
    t_DIVIDE = r"/"
    t_LPAREN = r"\("
    t_RPAREN = r"\)"
    t_MODULO = r"%"

    # Ignore space characters
    t_ignore = " \t"

    def t_NUMBER(self, t):
        r"-?\d+(\.\d*)?"
        t.value = float(t.value)
        return t

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def parse(self, data):
        self.lexer.input(data)

        tokens = []
        while True:
            token = self.lexer.token()

            if not token:
                break

            tokens.append(token)

        return tokens
