
import pytest

from ejercicios.operaciones import div

class TestClass:

    # Test para la operación div
    def test_div(self):
        assert div(5,5) == 1
        assert div(6,2) == 3
        assert div(10,5) == 2
        assert div(8,2) == 4
