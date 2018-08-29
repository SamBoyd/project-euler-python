from typing import *

def gen_fib(limit: int = 6) -> Iterator[int]:
    output = range(limit)
    for i in output:
        if i == 0 or i == 1:
            output[i] = i + 1
        else:
            output[i] = output[i - 1] + output[i - 2]
    return iter(list(filter(lambda x: x < limit, output)))

def sum_fib(limit: int = 6, f: Callable = lambda x: x) -> int:
    fib = gen_fib(limit)
    filtered_fib = filter(f, fib)
    return sum(filtered_fib)

def sum_even_fib(limit: int = 6) -> int:
    return sum_fib(limit, lambda x: (x % 2) == 0)
