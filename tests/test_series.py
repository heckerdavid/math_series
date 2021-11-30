from math_series.series import fibonacci, lucas, sum_series
import pytest

def test_fib_import():
    assert fibonacci

fib = [0, 1, 1, 2, 3, 5, 8, 13, ]
lucas_nums = [2, 1, 3, 4, 7, 11, 18, 29, ]


def test_fib():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fib_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fib_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fib_7():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected

def test_fib_6():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected

def test_lucas_import():
    assert lucas



def test_lucas():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_2():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_3():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_4():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test_lucas_5():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_sum_import():
    assert sum_series

def test_sum_0_fib():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_sum_1_fib():
    actual = sum_series(1)
    expected = 1
    assert actual == expected
    

def test_sum_2_fib():
    actual = sum_series(2)
    expected = 1
    assert actual == expected
    

def test_sum_3_fib():
    actual = sum_series(3)
    expected = 2
    assert actual == expected

def test_sum_4_fib():
    actual = sum_series(4)
    expected = 3
    assert actual == expected

def test_sum_0_lucas():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected

def test_sum_1_lucas():
    actual = sum_series(1, 2, 1)
    expected = 1
    assert actual == expected

def test_sum_2_lucas():
    actual = sum_series(2, 2, 1)
    expected = 3
    assert actual == expected

def test_sum_3_lucas():
    actual = sum_series(3, 2, 1)
    expected = 4
    assert actual == expected

def test_sum_3_lucas():
    actual = sum_series(4, 2, 1)
    expected = 7
    assert actual == expected