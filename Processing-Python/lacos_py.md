# Iteração / laços de repetição (loops)

## Sintaxe

O `for` permite controlar uma seqüência de repetições. Pegando de um em um itens fornecidos (de uma coleção, de um objeto iterável ou gerador). 

```python   
lista_de_palavras = ["abacate", "uva", "frango"]
for palavra in lista_de_palavras:
  print(palavra)
```

É muito comum ser usado em conjunto com `range()` que produz uma sequência de números.

```python   
for n in range(10):
  print(n)
```

## Exemplos

### contator 
```python
for i in range(10, 80, 5):
  line(30, i, 80, i) 
```

### laços "aninhados" par fazer uma grade

```python
for i in range(0, 80, 10):
  for j in range(0, 80, 10): 
    ellipse(i, j, 5, 5) 
```
