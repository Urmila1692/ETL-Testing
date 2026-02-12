import pytest


class Test_002:

    @pytest.mark.math
    @pytest.mark.regression
    def test_sum_003(self):
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
    @pytest.mark.regression
    def test_mul_004(self):
        a = 10
        b = 5
        mul = a * b
        print(f"\nThe mul of {a} * {b} = {mul}")
        assert mul == 50


    def Sub(self): # as per pytest rules this is not testcase, won't discover under pytest run
        a = 10
        b = 5
        sub = a - b
        print(f"\nThe sub of {b} from {a} = {sub}")
        assert sub == 5




