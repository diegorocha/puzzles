# coding: utf-8
from puzzles.code_wars.kata.ip_validation import is_valid_IP


def test_is_valid_IP():
    assert is_valid_IP('12.255.56.1')
    assert is_valid_IP('') is False
    assert is_valid_IP('abc.def.ghi.jkl') is False
    assert is_valid_IP('123.045.067.089') is False
