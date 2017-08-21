# coding: utf-8


def validBraces(input):
    braces = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for ch in input:
        if ch in braces:  # Opening
            stack.append(ch)
        if ch in braces.values():  # Closing
            if not stack or braces[stack.pop()] != ch:
                return False  # Wrong closing
    return len(stack) == 0  # Everthing opened was closed
