# coding: utf-8
from puzzles.code_wars.kata.memoized_fibonacci import fibonacci


def test_fibonacci():
    assert fibonacci(50) == 12586269025
    assert fibonacci(60) == 1548008755920
    assert fibonacci(70) == 190392490709135
    assert fibonacci(100) == 354224848179261915075
