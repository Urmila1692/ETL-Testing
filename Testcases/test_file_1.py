"""
1. Configure the interpreter

2. Termination Setting:
    # Setting-->Tool-->Terminal-->ShellPath -- > "C:\WINDOWS\system32\cmd.exe"

3. Install libraries:
    i. pip install selenium
    ii. pip install pytest
    iii. pip install pytest-xdist
    iv. pip install openpyxl
    v. pip install pytest-html
    vi. pip install pytest-sugar
    vii. pip install pytest-cov
    viii. pip install allure-pytest
    ix. pip install pytest-rerunfailures
    x. pip install faker


4. Set default test runner:
     Setting-->Tool-->Python integrated Tool --> Default test runner --> "Pytest"


5. Pytest Rules:
    i. Python file name --> prefix --> "test_" or  suffix "_test"
    ii. For pytest test we have to create the class and under the
     class, we have to create the methods, and that methods are nothing but the test cases.
    iii. Class name --> Should start with "Test_"
    iv. Method ame/ Testcase name --> "test_"

6. Test Run commands(Terminal):

    i. If you want to run all testcases  under specific folder:
    command --> "pytest"

    ii. If you want to run the testcases from specific file :
    command --> "pytest filepath"
    e.g. --> pytest "D:\Batch Notes\Automation Testing Dec 2025\03. Python_Pytest_Basic\Testcases\test_file_1.py"
    or
    e.g. --> pytest "Testcases/test_file_1.py"

    iii. If you want to run the specific testcase
    command -- > pytest -k "test_case_name"
    e.g. --> pytest -k "test_sum_001"
    your task --. find more way or method to run specific testcase.

    iv. For standard output (print) and verbose (with detail class, test, file names) :
    command : pytest -v (for verbose)
    command : pytest -s (for standard output)
    use the both:
    command : pytest -v -s

    v. To ignore warning:
    command :  pytest --disable-warnings

    vi. To create html reports: (pip install pytest-html)
    command : pytest --html=folder/my_report.html
    e.g. : pytest --html=Html_report/my_report.html

    vii. To get test coverage report : (pip install pytest-cov)
    e.g. pytest -cov


    viii. For parallel run : (pytest-xdist)
    command --> pytest -n=number
    e.g. pytest -n = 4
    e.g. pytest -n = auto
    (n = no. of worker processor)


    ix. For grouping the testcases use -m (technically calling as marker):
    Command :  pytest -m "group_name"

    e.g. -->pytest -m "group_1 and group_2"
    e.g. -->pytest -m "group_1 or group_2"
    e.g. -->pytest -m "math or web"
    e.g. -->pytest -m "math and sanity"


    To register custom marker create pytest.ini file like below:

        [pytest]
        markers =
            math: for match operations
            sanity: for sanity testcases
            regression: for regression testcases
            web: for web testcases


"""
import pytest


class Test_001:

    @pytest.mark.math
    @pytest.mark.sanity
    def test_sum_001(self, demo_fixture):
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
    def test_mul_002(self, demo_fixture):
        a = 10
        b = 5
        mul = a * b
        print(f"\nThe mul of {a} * {b} = {mul}")
        assert mul == 50


    @pytest.mark.math
    @pytest.mark.skip # we are skipping this for any specific reason
    def test_mul_012(self):
        a = 10
        b = 5
        mul = a * b
        print(f"\nThe mul of {a} * {b} = {mul}")
        assert mul == 50


    @pytest.mark.math
    @pytest.mark.xfail # we are skipping this for any specific reason
    def test_mul_013(self):
        a = 10
        b = 5
        mul = a * b
        print(f"\nThe mul of {a} * {b} = {mul}")
        assert mul == 50


    @pytest.mark.math
    @pytest.mark.xfail # we are skipping this for any specific reason
    def test_mul_014(self):
        a = 10
        b = 5
        mul = a * b
        print(f"\nThe mul of {a} * {b} = {mul}")
        assert mul == 5

    @pytest.mark.math
    def test_mul_015(self):
        a = 10
        b = 5
        mul = a * b
        print(f"\nThe mul of {a} * {b} = {mul}")
        assert mul == 5


    def test_mul_016(self):
        a = 10
        b = 5
        mul = a * b
        print(f"\nThe mul of {a} * {b} = {mul}")
        assert mul == 5


    def Sub(self): # as per pytest rules this is not testcase, won't discover under pytest run
        a = 10
        b = 5
        sub = a - b
        print(f"\nThe sub of {b} from {a} = {sub}")
        assert sub == 5




# pytest -v -s  -n=4 --html=Html_Report/.My_Report.html --cov --disable-warnings
# pytest -v -s -n=auto --browser edge --html=Html_Report/My_Report.html --cov --disable-warnings