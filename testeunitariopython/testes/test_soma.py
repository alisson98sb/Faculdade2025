from run import *
import pytest

def test_soma():
    assert soma(2, 3) == 5


def teste_entrada_invalida():
    pytest.raises(TypeError)
    assert soma('a' + 2) == 5
    