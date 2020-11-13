import pytest

from ..expr_parser import ExprParser


def test_build():
    parser = ExprParser()
    parser.build()
