# Textos no programa e na tela

O tipo dos valores que representam texto, palavras, letras ou glifos em geral, é chamado *string*, ou *cadeia de caracteres* numa tradução acadêmica para o português que raramente você vai ouvir.

```
frase = 'Eu me chamo Alexandre'
nome = "Alexandre 'o grande' bobo"
```

Podemos usar tanto aspas duplas `"`  como aspas simples `'` e dentro de uma string com aspas duplas podemos ter aspas simples e vice-versa. Também podem ser usasdas triplas de aspas: `'''` ou `"""` especialmente para strings com quebras de linha como veremos mais adiante.

### Letras com acentos e outros glifos

O `u` antes da string pode ser necessário para usar caracteres não-ASCII, como letras acentuadas (tem uma explicação disto [aqui](https://github.com/villares/material-aulas/blob/master/Processing-Python/futuro.md)) .

### Quebras de linha e caracteres especiais 

Em Python o `\` em uma string é chamado de 'caractere de escape' permite obter elementos especiais, por meio de uma 'sequência de escape', como por exemplo uma tabulação (`\t`) ou um sol ☀ (`\u2600`). Se precisar usar a própria barra invertida na string escreva `\\`.

Usamos `\n` no meio da string para obter uma quebra de linha. Como no exemplo a seguir:

```python
print(u'frutas frescas:\nmaça\nbanana')
```
Resultado:
```
frutas frescas:
maçã
banana
```

Uma outra maneira de indicar uma string com quebras de linha é com aspas triplas `'''` ou `"""`:
```python
print(
u"""frutas frescas:
maçã
banana
""")
```
