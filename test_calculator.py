from calculator import add, multiply

import pytest


def test_add_rejects_non_numeric():
    with pytest.raises(TypeError):
        add("2", 3)


def test_multiply_positive_integers():
    assert multiply(2, 3) == 6
    assert multiply(5, 4) == 20
    assert multiply(10, 10) == 100
    assert multiply(1, 42) == 42


def test_multiply_rejects_non_numeric():
    with pytest.raises(TypeError):
        multiply("2", 3)
    with pytest.raises(TypeError):
        multiply(2, "3")
