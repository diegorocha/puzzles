# coding: utf-8


def is_valid_IP(input):
    return [int(p) < 256 for p in input.split('.') if not p.startswith('0') and
            p.isdigit()] == [True, True, True, True]
