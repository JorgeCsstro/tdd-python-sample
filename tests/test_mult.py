
import pytest

from ejercicios.operaciones import mult

class TestClass:

    # Test para la operación mult
    def test_mult(self):
        assert mult(4,5) == 20
        assert mult(1,2) == 2
        assert mult(7,5) == 35
        assert mult(7,9) == 63
