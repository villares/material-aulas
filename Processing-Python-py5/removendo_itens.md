# Removendo itens de coleções

<!-- thumb para o sumário
![](assets/thumb-removendo.png)
-->
## Removendo itens de uma lista

Imagine que temos uma lista com números. Podemos obter o número em uma determinada posição (índice) ao mesmo tempo que o removemos, como o método `.pop()`. Se chamarmos `.pop()` sem nenhum argumento removemos o último item da lista. Passando um índice a operação se torna um pouco menos eficiente para listas muito grandes mas funciona também. 

```python
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]
a = numeros.pop() # remove o 90, a = 90
b = nomeros.pop(0) # remove o 10, b = 10 
print(numeros) # exibe [20, 30, 40, 50, 60, 70, 80]
```
Também é possível usar a instrução `del` com o índice. 

```python
numeros = [100, 200, 300]
del numeros[1]
print(numeros) # exibe [100, 300]
del numeros[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
```
Tanto com `del lista[indice]` como com `lista.pop(indice)` é preciso garantir que o índice cai dentro da lista!

Outra maneira de remover itens de uma lista é o método `.remove(valor)`, nesse caso a primeira instância encontrada do valor vai ser removida. 

```python
numeros = [2, 5, 2, 5, 2, 5, 2]
numeros.remove(5)
print(numeros) # exibe [2, 2, 5, 2, 5, 2]
numeros.remove(6)
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: list.remove(x): x not in list
```
Tentar remover um valor que não está contido na lista produz um erro, você pode checar antes com `if x in numeros: numeros.remove(x)`.

## Não remova itens ao mesmo tempo em que percorre uma coleção

Quando queremos remover itens de uma estrutura de dados "dinâmica" isto é com número variável de itens, como uma lista, se tentarmos remover itens em uma iteração (como um laço for) que percorre a mesma estrutura que vamos modificar, acabamos por ter problemas.

Um exemplo comum na programação criativa é termos um sistema de partículas que são objetos que interagem e se desenham na tela, mas precisamos remover alguns deles depois de algum tempo, por "decaimento"/morte ou caso saiam da tela. O exemplo a seguir é bem mais simples que isso, são só alguns números em uma lista e queremos remover os zeros:

```python
# errado

numeros = [1, 2, 4, 0, 0, 0, 0, 8, 0, 9, 0]
for n in numeros:
    print(n)
    if  n == 0:
        numeros.remove(n)

print(numeros)  # exibe: [1, 2, 4, 8, 0, 9, 0]
```

Uma das soluções possíveis é copiar a estrutura e "andar" pela cópia enquanto se remove itens da estrutura original. 

```python
# certo

numeros = [1, 2, 4, 0, 0, 0, 0, 8, 0, 9, 0]
for n in numeros.copy():
    if  n == 0:
        numeros.remove(n)
        
print(numeros)  # exibe  [1, 2, 4, 8, 9]
``` 
Em vez `numeros.copy()` é possível também usar `numeros[:]`, que é uma 'fatia' contendo uma cópia da lista toda, ou ainda a função embutida `reversed()`, que cria um objeto iterável e também pode ser usada neste caso. Essa última forma lembra a estratégia de iteração do final para o começo usada em outras linguagens que necessitam de um índice para consultar os itens da coleção.

```python
numeros = [1, 2, 4, 0, 0, 0, 0, 8, 0, 9, 0]
for n in reversed(numeros):
    if  n == 0:
        numeros.remove(n) 
        
print(numeros)  # exibe  [1, 2, 4, 8, 9]

# experimente também: `for i, n in reversed(list(enumerate(numeros))):`
# E nesse caso é possível usar `del numeros[i]` ou `numeros.pop(i)`
```

## Criando uma nova lista filtrando os valores a serem removidos

Uma outra solução é construir uma nova lista sem os itens que você quer remover, seja com um laço também ou com uma compreensão de listas como no exemplo abaixo:

```python
numeros = [1, 2, 4, 0, 0, 0, 0, 8, 0, 9, 0]
numeros = [n for n in numeros if n != 0]   # compreensão de listas
```
Em caso de listas grandes isso pode fazer boa diferença em termos de performance, uma vez que remover itens do meio de uma lista não é muito eficiente.
