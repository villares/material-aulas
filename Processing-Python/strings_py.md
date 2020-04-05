# Textos: no programa, no console e na tela

O tipo dos valores que representam texto, palavras, letras ou glifos em geral, é chamado *string*, ou *cadeia de caracteres* numa tradução para o português acadêmica que raramente você vai ouvir.

Para expressar strings no corpo de um programa podemos o envolver em aspas duplas `"`  ou aspas simples `'`, dentro de um texto envolto por aspas duplas podemos ter aspas simples e vice-versa. Também podem ser usasdas triplas de aspas: `'''` ou `"""` especialmente para strings com quebras de linha como veremos mais adiante. 

```pyde
frase = 'Eu me chamo Alexandre'
meu_nome = "Alexandre 'o grande' bobo"
```

Podemos *concatenar*, isto é somar strings pela justaposição, com o operador `+`:

```pyde
primeiro_nome = 'Alexandre'
sobrenome = 'Villares'
nome = primeiro_nome + ' ' + sobrenome
# resultado: nome = 'Alexandre Villares'
```

Mas é não é possível somar um número a um texto ou o contrário. Note neste caso como `'10'` é entendido como texto, string, e não como o número `10`:

```pyde
a = '10' + 5  # TypeError: cannot concatenate 'str' and 'int' objects
```

### Mostrando texto no console

Usamos `print()` ou `println()` para *imprimir* texto na parte de baixo do IDE, o chamado console. 

```pyde
print("Oi mundo!") # Resultado no console: Oi mundo!
print(100 + 50)    # Resultado no console: 150

```

Como não podemos concatenar strings e números para mostrar de uma vez só é comum convertermos os números em strings das seguintes maneiras: 

```pyde
def setup():
    size(400, 400)
    println("largura da tela: {} - altura da tela: {}".format(width, height) # usando "{}".format(valor)

def draw():
    println("x: " + str(mouseX) + " y: " + str(mouseY))  # convertendo o valor em string com str()
```

### Mostando texto na tela

```pyde
def setup():
    size(400, 400)

def draw():
    background(100)
    texto_mouse = "x: " + str(mouseX) + " y: " + str(mouseY) 
    text(texto_mouse, 50, 50) #  text("texto" , x, y) 
```

### Letras com acentos, caracteres especiais e outros glifos

Em Python 2 um `u` antes de cada literal string (string no corpo do programa) é necessário para permitir letras acentuadas e outros caracteres não-ASCII. Uma outra solução é incluir no começo do seu programa,na primeira linha de código:

```pyde
from __future__ import unicode_literals
```

Você pode ler mais sobre isso na página [Python 2 e Python 3](https://github.com/villares/material-aulas/blob/master/Processing-Python/futuro.md).

Em Python o `\` em uma string é chamado de 'caractere de escape' permite obter elementos especiais, por meio de uma 'sequência de escape', como por exemplo uma tabulação (`\t`) ou um sol ☀ (`\u2600`). Se precisar usar a própria barra invertida na string escreva `\\`.

Usamos `\n` no meio da string para obter uma quebra de linha. Como no exemplo a seguir:

```pyde
print(u'frutas frescas:\nmaça\nbanana')
```
Resultado:
```
frutas frescas:
maçã
banana
```

Uma outra maneira de indicar uma string com quebras de linha é com aspas triplas `'''` ou `"""`:
```pyde
print(
u"""frutas frescas:
maçã
banana
""")
```
