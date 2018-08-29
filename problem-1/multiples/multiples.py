from typing import *
def get_multiples_of(x: int):
    list_of_3s: List[int] = [(i * x) for i in range(1, int(1000 / x) + 2)]
    return iter(list_of_3s)

def get_sums_of_multiples_of_3_and_5_below(n: int):
    iter_3: Iterable[int] = get_multiples_of(3)
    iter_5: Iterable[int] = get_multiples_of(5)

    sum_3s: int = sum([x for x in iter_3 if x < n])
    sum_5s: int = sum([x for x in iter_5 if x < n])

    return sum_3s + sum_5s