# coding: utf-8
from puzzles.code_wars.kata.simplifying_multilinear_polynomials import simplify


def test_simplify():
    assert simplify("dc+dcba") == "cd+abcd"
    assert simplify("2xy-yx") == "xy"
    assert simplify("-a+5ab+3a-c-2a") == "-c+5ab"
    assert simplify("-abc+3a+2ac") == "3a+2ac-abc"
    assert simplify("xyz-xz") == "-xz+xyz"
    assert simplify("a+ca-ab") == "a-ab+ac"
    assert simplify("xzy+zby") == "byz+xyz"
    assert simplify("-y+x") == "x-y"
    assert simplify("y-x") == "-x+y"
    assert simplify("+n-5hn+7tjhn-4nh-3n-6hnjt+2jhn+9hn") == "-2n+2hjn+hjnt"
