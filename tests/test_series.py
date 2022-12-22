import pytest

from series.series import fibonacci, lucas

# pytest tests must start with "test_"
def test_one():
    assert fibonacci


# @pytest.mark.skip()
def test_fibonacci_3():
    actual = fibonacci(3)
    expected = "2"
    assert actual == expected


def test_fibonacci_0():
    actual = fibonacci(0)
    expected = "0"
    assert actual == expected


def test_fibonacci_12():
    actual = fibonacci(12)
    expected = "144"
    assert actual == expected


def test_lucas_5():
    actual = lucas(5)
    expected = "11"
    assert actual == expected