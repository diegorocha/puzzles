# coding: utf-8
from puzzles.code_wars.kata.valid_braces import validBraces


def test_validBraces():
    assert validBraces('(){}[]')
    assert validBraces('(}') is False
    assert validBraces('[(])') is False
    assert validBraces('([{}])')
    assert validBraces('([{') is False
    assert validBraces('}') is False
