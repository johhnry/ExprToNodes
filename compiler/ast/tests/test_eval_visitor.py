import pytest

from ...parser.expr_parser import ExprParser
from ..bin_op import BinOp
from ..eval_visitor import EvalVisitor
from ..number import Number


@pytest.fixture
def eval_visitor():
    yield EvalVisitor()


@pytest.fixture
def parser():
    parser = ExprParser()
    parser.build()
    yield parser


def test_visit_number(eval_visitor, parser):
    ast = parser.parse("0")
    assert ast.accept(eval_visitor) == 0


def test_visit_bin_op(eval_visitor, parser):
    ast = parser.parse("3 + 5 - 7 * 2")
    assert ast.accept(eval_visitor) == (3 + 5 - 7 * 2)


def add(a: int, b: int) -> int:
    return "hh"
