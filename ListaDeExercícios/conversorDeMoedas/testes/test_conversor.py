from run import *
import pytest

#Implemente funções para converter diferentes moedas (por exemplo, dólar para
#euro, real para dólar, etc).

def test_dolar_to_euro():
    # 1 dolar -> 0.95 euro
    assert dolar_to_euro(10, 0.95) == round(10 / 0.95, 2)

def test_euro_to_dolar():
    assert euro_to_dolar(10, 1.05) == round(10 * 1.05, 2)

#Real para dolar 1 dolar -> 5,77 reais
def test_real_to_dolar():
    assert real_to_dolar(10, 5.77) == round(10 / 5.77, 2)

def test_dolar_to_real():
    assert dolar_to_real(10, 5.77) == round(10 * 5.77, 2)