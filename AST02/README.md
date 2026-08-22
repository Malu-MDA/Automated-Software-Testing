# AST02 - Testes Unitários com Pytest

## Objetivo

Praticar a criação de testes unitários utilizando Python e o framework Pytest.

## Exercícios

### Exercício 1 - Verificação de Idade

Criação de uma função para verificar se uma pessoa pode dirigir com base na idade.

Testes realizados:

- Pessoa maior de idade pode dirigir.
- Pessoa menor de idade não pode dirigir.

### Exercício 2 - Cálculo de Desconto

Criação de uma função para calcular o valor de um produto após a aplicação de um desconto.

Testes realizados:

- Cálculo de desconto comum.
- Desconto no limite de 50%.
- Desconto decimal.

### Exercício 3 - Validação de Senha

Criação de uma função para validar senhas com base no número mínimo de caracteres.

Testes realizados:

- Senha válida.
- Senha curta.
- Verificação da mensagem retornada para senha curta.

### Exercício 4 - Gerenciador de Carrinho de Compras

Criação da classe `CarrinhoDeCompras` utilizando uma lista para armazenar os itens.

Funcionalidades:

- Adicionar itens ao carrinho.
- Remover itens existentes.
- Listar os itens do carrinho.
- Gerar um `ValueError` ao tentar remover um item inexistente.

Testes realizados:

- Adicionar e verificar se um item está presente na lista.
- Remover e verificar se um item não está mais na lista.
- Verificar se um `ValueError` é disparado ao remover um item inexistente.

## Tecnologias utilizadas

- Python
- Pytest
- Git
- GitHub

## Como executar os testes

No terminal, na pasta principal do projeto, execute:

```bash
pytest -v
```

## Integração Contínua (CI)

Além da execução local dos testes, foi configurada uma **Integração Contínua (CI)** utilizando **GitHub Actions**.

O workflow é executado automaticamente sempre que há um `push` ou `pull request` para a branch `main`. Durante a execução, o GitHub:

1. Baixa o código do repositório;
2. Configura o ambiente Python;
3. Instala o `pytest`;
4. Executa automaticamente todos os testes da atividade.

Dessa forma, é possível verificar diretamente pelo GitHub Actions se os testes estão sendo executados corretamente.

### Resultado dos testes

Atualmente, todos os **11 testes** da AST02 estão passando com sucesso no ambiente de CI.

📌 Os resultados podem ser consultados na aba **Actions** do repositório.
