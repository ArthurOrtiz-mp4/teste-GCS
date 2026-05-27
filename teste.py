print('Hello World')


import pytest
from calc_basico import (
    somar,
    subtrair,
    multiplicar,
    dividir
)


# =========================
# TESTES SOMAR
# =========================

def test_somar_positivos():
    assert somar(2, 3) == 5


def test_somar_negativos():
    assert somar(-2, -3) == -5


# =========================
# TESTES SUBTRAIR
# =========================

def test_subtrair():
    assert subtrair(10, 4) == 6


def test_subtrair_negativo():
    assert subtrair(5, 10) == -5


# =========================
# TESTES MULTIPLICAR
# =========================

def test_multiplicar():
    assert multiplicar(3, 4) == 12


def test_multiplicar_por_zero():
    assert multiplicar(10, 0) == 0


# =========================
# TESTES DIVIDIR
# =========================

def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_float():
    assert dividir(5, 2) == 2.5


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)