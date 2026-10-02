from calculator import add, multiply

import pytest


def test_add_rejects_non_numeric():
    with pytest.raises(TypeError):
        add("2", 3)


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(4, 5) == 20
    assert multiply(1, 7) == 7


def test_multiply_negative():
    assert multiply(-2, 3) == -6


def test_multiply_rejects_non_integer():
    with pytest.raises(TypeError):
        multiply(2.5, 4)
