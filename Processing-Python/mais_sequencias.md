# Mais sobre sequências e suas fatias

## Strings são sequencias de caracteres

Python trata strings, texto, como uma sequências de caracteres. É possível por exemplo iterar, realizar uma ação para cada caractere de um string:

```python
nome = 'Guido'
for letra in nome:
    print(letra)
    
# resultado no console:
# G 
# u
# i
# d
# o
```

## Consultando itens de uma sequência

Tanto para sequências de letras como em listas ou tuplas podemos consultar seus itens pela posição com a notação `[ ]`:

```python
palavra = 'silly walk'
print(palavre[0])  # 's' a primeira letra
print(palavre[1])  # 'i' a segunda letra
print(palavre[-1])  # 'k' a última letra

alguns_pares = (2, 4, 6, 8, 10, 12)
print(alguns_pares[0])  # 2 o primeiro número
print(alguns_pares[1])  # 4 o segundo número
print(alguns_pares[-1]) # 12 o último número
```
## Alterando itens

Estruturas mutáveis como listas, podem ter seus itens alterados, incluídos ou removidos.

```
lista = [1976, 1980, 1988, 2013]
print(lista[2])  # o resultado é o terceiro número:
# 1988

lista = [1976, 1980, 1988, 2013]
lista[2] = 1994 # muda o segundo item
print(lista) # resultado:
# [1976, 1980, 1994, 2013]

lista.append(2020)
print(lista) # resultado:
# [1976, 1980, 1994, 2013, 2020]

del lista[1] # remove o segundo item
print(lista) # resultado:
# [1976, 1994, 2013, 2020]

a = lista.pop() # remove e devolve o último item
print(a) # 2020
print(lista) # [1976, 1994, 2013]

b = lista.pop(1) # remove e devolve o segundo item
print(b) # 1994
print(lista) # [1976, 2013]
```

Tuplas e strings são imutáveis, não permitem este tipo de operação.

## Fatias

Com a notação `[inicio:parada]`, `[:parada]`, [inicio:], ou ainda `[inicio:parada:passo]`, podemos obter subsequências de uma sequência.

```python
nome = 'Saskia Freeke'
a = nome[:6]
b = nome[7:]
print(a) # 'Saskia'
print(b) # 'Freeke' 

c = nome.split(' ')
print(c) # resultado uma lista com dois strings:
# ['Saskai', 'Freele']
```
A notação `[:]` produz uma cópia da sequência. O que é especialmente útil para sequências mutáveis.




