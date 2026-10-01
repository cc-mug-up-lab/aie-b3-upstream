from calculator import add

import pytest


def test_add_rejects_non_numeric():
    with pytest.raises(TypeError):
        add("2", 3)
