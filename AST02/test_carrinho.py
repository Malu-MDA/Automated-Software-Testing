import pytest
from carrinho import CarrinhoDeCompras

def test_adicionar_item():
    # Arrange
    carrinho = CarrinhoDeCompras()
    item = "Notebook"

    # Act
    carrinho.adicionar_item(item)

    # Assert
    assert item in carrinho.listar_itens()


def test_remover_item():
    # Arrange
    carrinho = CarrinhoDeCompras()
    item = "Notebook"
    carrinho.adicionar_item(item)

    # Act
    carrinho.remover_item(item)

    # Assert
    assert item not in carrinho.listar_itens()


def test_remover_item_inexistente():
    # Arrange
    carrinho = CarrinhoDeCompras()
    item = "Notebook"

    # Act + Assert
    with pytest.raises(ValueError):
        carrinho.remover_item(item)