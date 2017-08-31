# coding: utf-8
from puzzles.code_wars.kata.nesting_structure_comparison import same_structure_as


def test_same_structure_as():
    assert same_structure_as([1,1,1],[2, 2]) is False
    assert same_structure_as([1,[1,1]],[2,[2,2]]) is True
    assert same_structure_as([1,[1,1]],[[2,2],2]) is False
    assert same_structure_as([1,'[',']'], ['[',']',1]) is True
