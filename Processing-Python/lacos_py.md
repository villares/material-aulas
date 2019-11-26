# Iteração / laços de repetição (loops)

## Sintaxe

O `for` permite controlar uma seqüência de repetições olhando de um em um itens fornecidos por uma sequência (ou de uma coleção, de um objeto iterável ou ainda de um objeto gerador, mas isso não vem ao caso agora). 

```python   
lista_de_palavras = ["abacate", "uva", "frango"]
for palavra in lista_de_palavras:
  print(palavra)

```

Tem como resultado, impresso no console:

```
abacate
uva
franco
```

É muito comum o `for` ser usado em conjunto com `range()` que produz uma sequência de números.

```python   
for n in range(10):
  print(n)
  
Com o seguinte resultado, aqui apresentado truncado com "...", impresso no console:

```
0
1
2
...
8
9
```

## Exemplos

### linhas paralelas 

```python
for y in range(10, 80, 5):
  line(30, y, 80, y) 
```

### laços "aninhados" par fazer uma grade

```python
for i in range(0, 80, 10):
  for j in range(0, 80, 10): 
    ellipse(i, j, 5, 5) 
```

### Glossário

[**loop**](https://penseallen.github.io/PensePython2e/04-caso-interface.html#termo:loop) **(laço)** Parte de um programa que pode ser executada repetidamente.

---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
