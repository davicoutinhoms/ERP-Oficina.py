# ERP Oficina

Projeto acadêmico desenvolvido em Python com o objetivo de criar um sistema ERP para gerenciamento de uma oficina mecânica, aplicando conceitos de estruturas de dados e algoritmos.

O sistema está sendo desenvolvido em equipe e contempla funcionalidades relacionadas a ordens de serviço, clientes, estoque, atendimento e demais processos de uma oficina.

## Objetivo do projeto

Desenvolver um ERP funcional utilizando estruturas de dados e algoritmos implementados manualmente, conforme os requisitos da disciplina.

Entre os principais conceitos utilizados estão:

* Lista
* Pilha
* Fila de Prioridade
* Algoritmo de busca manual
* Algoritmo de ordenação manual

Não serão utilizadas funções prontas do Python que realizem automaticamente a busca ou a ordenação dos dados.

## Funcionalidades de Ordens de Serviço

O módulo de Ordens de Serviço será responsável por:

* Cadastro de ordem de serviço
* Consulta de ordem de serviço
* Alteração de ordem de serviço
* Remoção de ordem de serviço
* Registro do problema do veículo
* Registro dos serviços necessários
* Definição e alteração da prioridade
* Alteração do status da ordem
* Cálculo do valor total da ordem
* Processamento das ordens de serviço
* Geração de relatórios ordenados

## Fila de Prioridade

As ordens de serviço serão processadas de acordo com o nível de urgência do problema.

| Prioridade | Descrição                        |
| ---------- | -------------------------------- |
| 5          | Problema crítico                 |
| 4          | Veículo impossibilitado de rodar |
| 3          | Problema moderado                |
| 2          | Manutenção necessária            |
| 1          | Manutenção preventiva            |

Ordens com maior prioridade serão processadas antes das ordens com menor prioridade.

Caso duas ordens possuam a mesma prioridade, será mantida a ordem de chegada.

## Algoritmo de Busca

Será implementado manualmente um algoritmo de busca para localizar ordens de serviço cadastradas no sistema.

Inicialmente será utilizada a **Busca Linear**, percorrendo a lista de ordens até localizar o registro desejado.

A busca poderá ser utilizada em funcionalidades como:

* Consulta de ordem
* Alteração de ordem
* Remoção de ordem
* Alteração de status
* Alteração de prioridade
* Registro de serviços

## Algoritmo de Ordenação

Será implementado manualmente um algoritmo de ordenação, sem utilização de `sort()` ou `sorted()`.

Inicialmente será utilizado o algoritmo **Bubble Sort**.

A ordenação poderá ser utilizada para gerar relatórios como:

* Ordens por valor
* Ordens por prioridade
* Peças por quantidade em estoque

## Estrutura do projeto

```text
ERP-Oficina/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   └── ordem_servico.py
│
├── dados/
│   ├── __init__.py
│   └── ordens.py
│
├── estruturas/
│   ├── __init__.py
│   └── fila_prioridade.py
│
├── algoritmos/
│   ├── __init__.py
│   ├── busca.py
│   └── ordenacao.py
│
└── services/
    ├── __init__.py
    └── ordem_service.py
```

## Organização dos arquivos

### `main.py`

Arquivo principal do sistema.

Será responsável por apresentar o menu e permitir que o usuário escolha as funcionalidades do ERP.

### `models/`

Contém as classes que representam as entidades do sistema.

O arquivo `ordem_servico.py`, por exemplo, contém a classe responsável por representar uma Ordem de Serviço.

### `dados/`

Responsável pelo armazenamento dos dados utilizados durante a execução do sistema.

A lista de ordens de serviço ficará armazenada nesta camada.

### `estruturas/`

Contém as estruturas de dados implementadas no projeto.

O arquivo `fila_prioridade.py` será responsável pelo gerenciamento da fila de atendimento das ordens de serviço.

### `algoritmos/`

Contém os algoritmos implementados manualmente.

* `busca.py`: algoritmo de busca.
* `ordenacao.py`: algoritmo de ordenação.

### `services/`

Contém as principais regras e funcionalidades do sistema.

Nesta camada ficarão operações como cadastro, consulta, alteração, remoção e processamento das ordens de serviço.

## Tecnologias utilizadas

* Python
* Git
* GitHub
* GitHub Codespaces

## Status do projeto

🚧 Projeto em desenvolvimento.

Atualmente está sendo construída a estrutura inicial do ERP e o módulo de Ordens de Serviço.

## Requisitos acadêmicos

O projeto deve utilizar:

* Estruturas de dados de forma coerente com seus comportamentos
* Fila de prioridade para processamento das ordens
* Algoritmo de busca implementado manualmente
* Algoritmo de ordenação implementado manualmente
* Organização modular do código

Não é permitido utilizar funções prontas que realizem automaticamente os algoritmos de busca ou ordenação.
