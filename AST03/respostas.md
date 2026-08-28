# Respostas — AST03

## Q1 — Cobertura de Linha (Line Coverage)

A porcentagem de cobertura de linhas apresentada foi de **70%**.

Apesar de existirem 5 resultados/regras de negócio possíveis e apenas 2 testes escritos inicialmente, a cobertura de linhas aparenta ser alta porque essa métrica verifica apenas **quais linhas do código foram executadas**.

Os dois testes executaram várias das mesmas linhas do código, mas não passaram por todos os caminhos possíveis da lógica. Dessa forma, é possível ter uma cobertura de linhas relativamente alta sem que todas as regras de negócio tenham sido testadas.

---

## Q2 — Cobertura de Desvio (Branch Coverage)

Ao executar o comando:

```bash
pytest -v --cov=validador --cov-branch
```

foram apresentados os seguintes valores:

- **Branch:** 8
- **BrPart:** 3
- **Cover:** 67%

O valor de **Branch = 8** representa os desvios/ramificações identificados na lógica do programa.

O valor de **BrPart = 3** indica que existiam 3 ramificações parcialmente cobertas pelos testes realizados naquele momento.

A cobertura caiu de **70% para 67%** porque a análise de desvios é mais abrangente que a cobertura de linhas. Enquanto o Line Coverage verifica se as linhas foram executadas, o Branch Coverage também verifica os diferentes caminhos que as condições podem seguir.

Por exemplo, na condição:

```python
if vip:
```

existem diferentes caminhos possíveis, dependendo do valor de `vip`.

Assim, a análise de desvios conseguiu identificar caminhos que ainda não haviam sido testados, mesmo que algumas das linhas relacionadas já tivessem sido executadas.

---

## Q3 — Relatório Visual em HTML e Diagnóstico

No relatório HTML gerado pelo comando:

```bash
coverage html
```

foi possível visualizar quais partes do código estavam cobertas pelos testes.

### Linha `if idade < 0:`

A linha foi marcada como **amarela**.

Essa marcação indica que a linha foi executada, porém nem todos os seus desvios foram percorridos pelos testes.

### Linha `raise ValueError("Idade inválida")`

A linha foi marcada como **vermelha**.

Isso indica que ela ainda não havia sido executada pelos testes realizados inicialmente. Isso aconteceu porque nenhum dos testes utilizava uma idade negativa.

### Caminhos que precisavam ser testados

Para cobrir os caminhos que ainda não haviam sido executados, foram adicionados testes para:

1. **Idade inválida**
   - `idade = -5`
   - utilização de `pytest.raises(ValueError)`

2. **Acesso VIP**
   - `idade = 25`
   - `possui_convite = False`
   - `vip = True`

3. **Maior de idade sem convite**
   - `idade = 20`
   - `possui_convite = False`
   - `vip = False`

Com esses testes, todas as linhas e ramificações passaram a ser executadas.

### Por que 100% de cobertura de desvios não significa testar todas as combinações?

Atingir 100% de cobertura de desvios significa que todos os caminhos de decisão identificados no código foram exercitados pelos testes.

Isso não significa que todas as combinações possíveis dos argumentos `idade`, `possui_convite` e `vip` foram testadas.

Existem diversas combinações possíveis desses valores, mas o Branch Coverage está interessado em verificar se os diferentes caminhos das decisões do código foram percorridos.

Portanto, é possível atingir **100% de cobertura de desvios** sem testar todas as combinações possíveis de valores dos parâmetros.

---

## Desafio de Implementação Prática

Foram adicionados três novos testes ao arquivo `test_validador.py`:

```python
def test_acesso_vip():
    resultado = validar_acesso(25, False, vip=True)
    assert resultado == "Acesso VIP Liberado"


def test_sem_convite():
    resultado = validar_acesso(20, False)
    assert resultado == "Comprar Ingressos"


def test_idade_invalida():
    with pytest.raises(ValueError):
        validar_acesso(-5, True)
```

Com os dois testes que já existiam, o arquivo passou a possuir **5 testes**.

### Resultado final

Com o comando:

```bash
pytest -v --cov=validador --cov-branch
```

foi obtido:

- **5 testes aprovados**
- **10 statements**
- **0 statements não executados**
- **8 branches**
- **0 branches parcialmente cobertos**
- **100% de cobertura**

O relatório HTML também confirmou:

```text
Coverage for validador.py: 100%

10 statements
10 run
0 missing
0 excluded
0 partial
```

Dessa forma, o arquivo `validador.py` atingiu **100% de cobertura de linhas e 100% de cobertura de desvios**.