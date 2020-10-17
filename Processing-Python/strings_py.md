# Textos no programa, no console e na tela (*strings*)

O tipo dos valores que representam texto, palavras, letras ou glifos em geral, é chamado *string*, ou *cadeia de caracteres* numa tradução para o português acadêmica que raramente você vai ouvir.

## *Strings* no meio do código

Para expressar strings no corpo de um programa podemos os envolver em aspas duplas `"`  ou aspas simples `'`. Dentro de um texto envolto em aspas duplas podemos ter um texto que contém aspas simples, e vice-versa. Também podemos usar triplas de aspas: `'''` ou `"""`, fazemos isso especialmente para expressar strings com quebras de linha, como veremos mais adiante. 

```pyde
frase = 'Ideias verdes incolores dormem furiosamente'
autor = "Noam Chomsky"
```

## Mostrando valores no console

Usamos `print()` ou `println()` para *exibir* na parte de baixo do IDE, o chamado console. Essas funções convertem automaticamente outros tipos de valores em string, uma representação textual ou uma referência ao objeto passado.

```pyde
def setup():           # Resultado exibido no console:
    print("Oi mundo!") # Oi mundo!
    print(100 + 50)    # 150
    print(setup)       # <function setup at 0x3>
```

## Manipulando *strings*

### O mais básico, concatenando strings e convertendo um número em string

Podemos *concatenar*, isto é somar strings em justaposição, com o operador `+`:

```pyde
primeiro_nome = 'John'
sobrenome = 'Conway'
nome = primeiro_nome + ' ' + sobrenome
# resultado: nome = 'John Conway'
```

Só que não é possível somar um número a um texto ou o contrário. Note neste caso como `'10'` é entendido como texto, *string*, e não como o número `10`:

```pyde
a = '10' + 5  # TypeError: cannot concatenate 'str' and 'int' objects
```

Como não podemos concatenar strings e números, por exemplo, para os mostrarmos juntos, é comum convertermos os números em strings. Veja aqui duas maneiras: 

```pyde
def setup():
    size(400, 400)
    println("largura da tela: {} - altura da tela: {}".format(width, height) # usando "{}".format(valor)

def draw():
    println("x: " + str(mouseX) + " y: " + str(mouseY))  # convertendo o valor em string com str()
```

Mais sobre como formatar a conversão dos números em strings, procurar e substituir sequências de caracteres, checar prefixos e sufixos entre muitas outras coisas você encontra em [Métodos dos objetos string](string_methods.md)

## Mostrando texto na área de desenho

```pyde
def setup():
    size(400, 400)

def draw():
    background(100)
    text("Oi mundo!", 50, 50) #  text(string, x, y) 
    texto_mouse = "x: {} y: {}".format(mouseX, mouseY)  # os valores vão nos {} {}
    text(texto_mouse, 50, 70)
```
![resultado](https://raw.githubusercontent.com/villares/material-aulas/master/Processing-Python/assets/text-na-tela.png)

Mais sobre desenhar texto na tela na página sobre tipografia básica em: [Trabalhando com fontes e outros ajustes do texto](https://github.com/villares/material-aulas/blob/master/Processing-Python/tipografia.md)

## Letras com acentos, caracteres especiais e outros glifos

Em Python 2  é necessário um `u` antes de cada *string literal* (*string* no corpo do programa) para permitir letras acentuadas e outros caracteres não-ASCII, os tornando objetos de texto *unicode*. Uma outra solução é incluir no começo do seu programa, logo na primeira linha, o seguinte código:

```pyde
from __future__ import unicode_literals
```

Você pode ler mais sobre isso na página [sobre Python 2 e Python 3](futuro.md).

Em Python o `\` dentro de strings é chamado de 'caractere de escape' permite obter elementos especiais, por meio de uma 'sequência de escape', como por exemplo uma tabulação (`\t`) ou um sol ☀ (`\u2600`). Se precisar usar a própria barra invertida escreva `\\`.

Usamos `\n` para obter uma quebra de linha. Como no exemplo a seguir:

```pyde
print(u'frutas frescas:\nmaça\nbanana')
```
Resultado:
```
frutas frescas:
maçã
banana
```

Uma outra maneira de indicar uma *string literal* com quebras de linha é usando aspas triplas `'''` ou `"""` o que permite que ela corra por várias linha no próprio código:
```pyde
print(
u"""frutas frescas:
maçã
banana
""")
```

## Assuntos relacionados

- [Métodos dos objetos string](string_methods.md)
- [Trabalhando com fontes e outros ajustes do texto](tipografia.md)
- [Lendo e escrevendo texto em arquivos](file_IO.md)
- [Sobre o Python 2 e alguns recursos do Python 3](futuro.md)
