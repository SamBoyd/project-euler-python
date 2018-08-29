from typing import *

from fib_sum import *

class TestFibSum(object):

    def test_should_produce_a_correct_fib_seq(self):
        fib: Iterator[int] = gen_fib()

        assert iter([1,2,3,5]) == fib

    def test_should_produce_a_correct_fib_seq_below_a_limit(self):
        fib: Iterator[int] = gen_fib(5)

        assert iter([1,2,3]) == fib

    def test_should_produce_a_correct_fib_seq_below_a_larger_limit(self):
        fib: Iterator[int] = gen_fib(14)

        assert iter([1,2,3,5,8,13]) == fib

    def test_should_sum_fib_seq(self):
        sum: int = sum_fib()

        assert 11 == sum

    def test_should_sum_fib_seq_below_limit(self):
        sum: int = sum_fib(5)

        assert 6 == sum
    def test_should_sum_even_fib_seq(self):
        sum: int = sum_even_fib()

        assert 2 == sum

    def test_should_sum_even_fib_seq_below_limit(self):
        sum: int = sum_even_fib(14)

        assert 10 == sum

    def test_should_handle_large_limits(self):
        sum: int = sum_even_fib(4000000)

        assert 10 == sum