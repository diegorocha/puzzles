# coding: utf-8

def same_structure_as(original,other):
    if type(original) == list:
        if type(original) != type(other):
            return False
        if len(original) != len(other):
            return False
        for i in range(len(original)):
            if not same_structure_as(original[i], other[i]):
                return False
    return True
