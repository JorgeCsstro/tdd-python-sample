
import pytest

from ejercicios.operaciones import suma

class TestClass:

    # Test para la operación suma
    def test_suma(self):
        assert suma(4,5) == 9
        assert suma(-1,-2) == -3
        assert suma(-7,5) == -2
        assert suma(-7,9) == 2
