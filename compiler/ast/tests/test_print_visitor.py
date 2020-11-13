import pytest

from ...parser.expr_parser import ExprParser
from ..bin_op import BinOp
from ..number import Number
from ..print_visitor import PrintVisitor


@pytest.fixture
def print_visitor():
    yield PrintVisitor()


@pytest.fixture
def parser():
    parser = ExprParser()
    parser.build()
    yield parser


def test_visit_number(print_visitor, parser):
    expr = "0.0"
    assert parser.parse(expr).accept(print_visitor) == expr


def test_visit_bin_op(print_visitor, parser):
    expr = "3.0 + 5.0 - 7.0 * 2.0"
    assert parser.parse(expr).accept(print_visitor) == expr
