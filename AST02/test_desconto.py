import pytest
from desconto import calcular_desconto

def test_calcular_desconto_comum():
    # Arrange
    valor = 100
    percentual = 10
    esperado = 90

    # Act
    resultado = calcular_desconto(valor, percentual)

    # Assert
    assert resultado == esperado


def test_calcular_desconto_limite_50():
    # Arrange
    valor = 100
    percentual = 70
    esperado = 50

    # Act
    resultado = calcular_desconto(valor, percentual)

    # Assert
    assert resultado == esperado


def test_calcular_desconto_decimal():
    # Arrange
    valor = 10.50
    percentual = 15
    esperado = 8.925

    # Act
    resultado = calcular_desconto(valor, percentual)

    # Assert
    assert resultado == pytest.approx(esperado)

