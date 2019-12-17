**Work in Progress**

###

O `u` antes da string pode ser necessário para usar caracteres não-ASCII, como letras acentuadas (tem uma explicação disto [aqui](https://github.com/villares/material-aulas/blob/master/Processing-Python/futuro.md)) .

### Quebras de linha

Em Python é possível usar `\n` no meio da string para obter uma quebra de linha. 

```python
print(u'frutas frescas:\nmaça\nbanana')
```
Resultado:
```
frutas frescas:
maçã
banana
```
O `\` é chamado de 'caractere de escape' permite obter elementos especiais, por meio de uma 'sequência de escape', como por exemplo uma tabulação (`\t`) ou um sol ☀ (`\u2600`). Se precisar usar a própria barra invertida na string escreva `\\`.

Uma outra maneira de indicar uma string com quebras de linha é com aspas triplas `'''` ou `"""`:
```python
print(
u"""frutas frescas:
maçã
banana
""")
```

""")
