import pytest

from ..expr_lexer import ExprLexer


@pytest.fixture
def lexer():
    lexer = ExprLexer()
    lexer.build()
    yield lexer


def get_tokens_as_string(tokens):
    return "".join([t.value for t in tokens])


def test_build_parser():
    lexer = ExprLexer()
    lexer.build()


def test_parse_spaces(lexer):
    assert not lexer.parse("    ")


def test_parse_random_numbers(lexer):
    import random

    for i in range(100):
        value = random.randint(0, 10000)
        assert lexer.parse(str(value))[0].value == value


def test_parse_negative_number(lexer):
    assert lexer.parse("-1")[0].value == -1


def test_parse_floating_point_number(lexer):
    floats = [0.0004, -0.1, 0.0, 14.45]
    for f in floats:
        assert lexer.parse(str(f))[0].value == f


def test_parse_parenthesis(lexer):
    string = "((()))"
    assert get_tokens_as_string(lexer.parse(string)) == string


def test_parse_operators(lexer):
    ops = "+-/*%"
    assert get_tokens_as_string(lexer.parse(ops)) == ops
