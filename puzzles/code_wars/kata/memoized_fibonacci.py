# coding: utf-8
fib = {0: 0, 1: 1}


def fibonacci(n):
    cache = fib.get(n)
    if cache is not None:
        return cache
    fibonacci_n = fibonacci(n - 1) + fibonacci(n - 2)
    fib[n] = fibonacci_n
    return fibonacci_n
