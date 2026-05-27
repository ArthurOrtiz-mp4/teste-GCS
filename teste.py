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


# =========================
# TESTES PERCENTUAL
# =========================
from calc_percentual import (
    percentual,
    acrescimo,
    desconto
)

def test_percentual():
    assert percentual(25, 200) == 12.5

def test_percentual_total_zero():
    with pytest.raises(ValueError):
        percentual(10, 0)

def test_acrescimo():
    assert acrescimo(100, 10) == 110.0

def test_acrescimo_percentual_negativo():
    with pytest.raises(ValueError):
        acrescimo(100, -5)

def test_desconto():
    assert desconto(200, 15) == 170.0

def test_desconto_percentual_invalido():
    with pytest.raises(ValueError):
        desconto(200, 110)