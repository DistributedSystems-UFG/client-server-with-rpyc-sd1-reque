# Atividade de Programação - Cliente-Servidor com RPC integrado na linguagem - Sistema Distribuído

**Aluno:** Ian Marcos da Cruz Chaves  
**Matrícula:** 201802684  

Este repositório contém um exemplo simples de uma aplicação cliente-servidor utilizando a biblioteca RPyC (Remote Python Call) para comunicação remota em um sistema distribuído.

## Funcionamento

O código neste repositório demonstra um sistema cliente-servidor, onde o cliente e o servidor estão conectados através da biblioteca RPyC. O servidor mantém uma lista que pode ser manipulada pelo cliente através de operações como adicionar elementos, inserir elementos em uma posição específica, pesquisar elementos, remover elementos e ordenar a lista.

Para executar o exemplo, siga os passos abaixo:

1. Inicie o servidor: Execute o arquivo `server.py` para iniciar o servidor RPC.

  ```bash
  python server.py
```
2. Execute o cliente: Execute o arquivo client.py para interagir com o servidor RPC.
  ```bash
  python client.py
```
O cliente realizará chamadas de procedimentos remotos para executar várias operações na lista do servidor, como adicionar, inserir, pesquisar, remover e ordenar elementos. Os resultados dessas operações serão exibidos no terminal.

## Exemplo de Uso
Suponhamos que você queira adicionar, inserir, pesquisar, remover e ordenar elementos em uma lista remota:
### 1. Adicionar elementos:
```python
print(conn.root.exposed_append(5))
print(conn.root.exposed_append(6))
```
### 2. Inserir elemento em uma posição específica (ex.: inserir o número 7 na segunda posição):
```python
print(conn.root.exposed_insert(1, 7))
```
### 3. Pesquisar um elemento (ex.: pesquisar o número 5):
```python
print(conn.root.exposed_find(5))
```

### 4. Remover um elemento (ex.: remover o número 5):

```python
print(conn.root.exposed_remove(5))
```

### 5. Ordenar a lista:

```python
print(conn.root.exposed_sort())
```

Os resultados de cada operação serão exibidos no terminal.

## Notas
Certifique-se de ter a biblioteca RPyC instalada. Você pode instalá-la usando o seguinte comando:
``` bash
pip install rpyc
```

