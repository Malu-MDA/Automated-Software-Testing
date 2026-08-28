# AST03 - Cobertura de Testes com Pytest

## Objetivo

Praticar a análise de cobertura de testes utilizando Python, Pytest e pytest-cov, trabalhando com cobertura de linhas e cobertura de desvios.

## Exercícios

### Exercício 1 - Cobertura de Linha

Criação de testes para a função `validar_acesso`.

Testes iniciais realizados:

- Acesso permitido para maior de idade com convite.
- Acesso negado para menor de idade.

Cobertura inicial:

- 70% de cobertura de linhas.

### Exercício 2 - Cobertura de Desvio

Análise dos desvios do código utilizando:

```bash
pytest -v --cov=validador --cov-branch
```

Resultado inicial:

- Branch: 8
- BrPart: 3
- Cover: 67%

### Exercício 3 - Relatório de Cobertura

Geração de relatório visual em HTML utilizando:

```bash
coverage html
```

O relatório pode ser encontrado na pasta `htmlcov/`.

Após a análise do relatório, foram identificados os caminhos que ainda não estavam cobertos pelos testes.

### Exercício 4 - Implementação dos Testes Faltantes

Foram adicionados testes para:

- Acesso VIP.
- Maior de idade sem convite.
- Idade inválida utilizando `pytest.raises`.

Resultado final:

- 5 testes realizados.
- 5 testes aprovados.
- 100% de cobertura de linhas.
- 100% de cobertura de desvios.

## Arquivos

- `validador.py` - Função utilizada na atividade.
- `test_validador.py` - Testes automatizados.
- `respostas.md` - Respostas das questões da atividade.
- `htmlcov/` - Relatório visual de cobertura.

## Tecnologias utilizadas

- Python
- Pytest
- pytest-cov
- Coverage
- Git
- GitHub Actions

## Como executar os testes

No terminal, na pasta da atividade, execute:

```bash
pytest -v
```

Para verificar a cobertura de linhas:

```bash
pytest -v --cov=validador
```

Para verificar a cobertura de linhas e desvios:

```bash
pytest -v --cov=validador --cov-branch
```

Para gerar o relatório visual:

```bash
coverage html
```

O relatório será gerado na pasta `htmlcov/`.