from ..ply import lex


class ExprLexer:
    # List of tokens to parse
    tokens = (
        "IDENTIFIER",
        "ENDL",
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
    t_IDENTIFIER = r"[a-zA-Z_][a-zA-Z0-9_]*"
    t_ENDL = r"\\n"
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

    def t_newline(self, t):
        r"\n+"
        self.lexer.lineno += len(t.value)

    def t_error(self, t):
        raise Exception(
            "Illegal character {} at {}:{}".format(
                t.value[0], self.lexer.lineno, self.find_column(self.lexer.lexdata, t)
            )
        )
        t.lexer.skip(1)

    def find_column(self, input, token):
        line_start = input.rfind("\n", 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1

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
