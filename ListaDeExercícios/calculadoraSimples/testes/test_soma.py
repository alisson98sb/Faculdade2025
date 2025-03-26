from run import *
import pytest

def test_soma():
    assert soma(2, 3) == 5

def test_subt():
    assert subtracao(10, 3) == 7

def test_multiplicacao():
    assert multipicacao(20, 5) == 100

def test_divisao():
    assert divisao(10, 2) == 5