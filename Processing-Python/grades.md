# Grades

Para produzir uma grade retangular de elementos (filas e colunas) podemos utilizar laços de repetição 'encaixados' ou 'aninhados' (*nested*).

```python
for x in range(0, 80, 10):
  for y in range(0, 80, 10): 
    ellipse(x, y, 5, 5) 
```
