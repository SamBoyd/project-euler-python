from multiples import *

class TestMultiples(object):
    def test_should_give_multiples_of_3_up_to_1000(self):
        multiples_3 = get_multiples_of(3)

        assert 3 == next(multiples_3)

        reached_1000 = False

        for x in multiples_3:
            assert x % 3 == 0
            if x > 1000:
                reached_1000 = True
                continue

        assert True == reached_1000

    def test_should_give_multiples_of_5_up_to_1000(self):
        multiples_5 = get_multiples_of(5)

        assert 5 == next(multiples_5)

        reached_1000 = False

        for x in multiples_5:
            assert x % 5 == 0
            if x > 1000:
                reached_1000 = True
                continue

        assert True == reached_1000

    def test_should_calculate_the_correct_sum(self):

        test_cases = {5: 3,
                      10: 23,
                      15: 45,
                      20: 93,
                      1000: 266333}

        for k in  test_cases:
            sum: int  = get_sums_of_multiples_of_3_and_5_below(k)
            assert test_cases[k] == sum
