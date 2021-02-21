import pytest

from ..expr_parser import ExprParser


@pytest.fixture
def parser():
    parser = ExprParser()
    parser.build()
    yield parser


def test_build():
    parser = ExprParser()
    parser.build()


def test_func(parser):
    parser.parse("f()")


def test_func_no_args(parser):
    f = parser.parse("f()")
    assert f.args == [0]
