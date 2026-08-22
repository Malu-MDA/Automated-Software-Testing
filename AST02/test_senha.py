import pytest
from senha import cadastrar_senha

def test_cadastrar_senha_valida():
    # Arrange
    senha = "1234567890"

    # Act
    resultado = cadastrar_senha(senha)

    # Assert
    assert resultado == senha



def test_cadastrar_senha_curta():
    # Arrange
    senha = "123"

    # Act / Assert
    with pytest.raises(ValueError):
        cadastrar_senha(senha) 


def test_mensagem_senha_curta():
    # Arrange
    senha = "123"

    # Act
    with pytest.raises(ValueError) as exc_info:
        cadastrar_senha(senha)

    # Assert
    assert str(exc_info.value) == "Senha muito curta"   