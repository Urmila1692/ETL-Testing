import pytest


class Test_003:

    @pytest.mark.math
    @pytest.mark.regression
    def test_sum_005(self):
        a = 10
        b = 5
        Sum = a + b
        print(f"\nThe sum of {a} + {b} = {Sum}")
        # if Sum == 14:
        #     assert True
        # else:
        #     assert False
        assert Sum == 15

    @pytest.mark.math
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_mul_006(self):
        a = 10
        b = 5
        mul = a * b
        print(f"\nThe mul of {a} * {b} = {mul}")
        assert mul == 50






