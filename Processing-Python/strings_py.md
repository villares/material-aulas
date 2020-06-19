# Textos no programa, no console e na tela (*strings*)

O tipo dos valores que representam texto, palavras, letras ou glifos em geral, é chamado *string*, ou *cadeia de caracteres* numa tradução para o português acadêmica que raramente você vai ouvir.

Para expressar strings no corpo de um programa podemos os envolver em aspas duplas `"`  ou aspas simples `'`. Dentro de um texto envolto em aspas duplas podemos ter um texto que contém aspas simples, e vice-versa. Também podemos usasr triplas de aspas: `'''` ou `"""`, fazemos isso especialmente para expressar strings com quebras de linha, como veremos mais adiante. 

```pyde
frase = 'Ideias verdes incolores dormem furiosamente'
autor = "Noam Chomsky"
```

Podemos *concatenar*, isto é somar strings em justaposição, com o operador `+`:

```pyde
primeiro_nome = 'John'
sobrenome = 'Conway'
nome = primeiro_nome + ' ' + sobrenome
# resultado: nome = 'John Conway'
```

Mas é não é possível somar um número a um texto ou o contrário. Note neste caso como `'10'` é entendido como texto, *string*, e não como o número `10`:

```pyde
a = '10' + 5  # TypeError: cannot concatenate 'str' and 'int' objects
```

### Mostrando valores no console

Usamos `print()` ou `println()` para *exibir* na parte de baixo do IDE, o chamado console. Essas funções convertem automaticamente outros tipos de valores em string, uma representação textual ou uma referência ao objeto passado.

```pyde
def setup():           # Resultado no console:
    print("Oi mundo!") # Oi mundo!
    print(100 + 50)    # 150
    print(setup)       # <function setup at 0x3>
```

Como não podemos concatenar strings e números, por exemplo, para os mostrarmos juntos, é comum convertermos os números em strings. Veja aqui duas maneiras: 

```pyde
def setup():
    size(400, 400)
    println("largura da tela: {} - altura da tela: {}".format(width, height) # usando "{}".format(valor)

def draw():
    println("x: " + str(mouseX) + " y: " + str(mouseY))  # convertendo o valor em string com str()
```

### Os *métodos* dos objetos *string*

*Strings* são um *tipo* de dado armazenado na memória do computador, e mais, em Python, são acompanhados de uma série de funções e que podem ser acionadas com a *sintaxe do ponto* (*dot syntax*).

<sub>Na programação orientada a objetos veremos que funções que acompanham objetos de uma determinada classe são conhecidas como métodos.</sub>

```python
# str.lower() devolve string com a versão em caixa baixa
print('Alexandre'.lower())  # exibe: alexandre

# str.upper() devolve string com a versão em caixa alta
print('Alexandre'.upper())  # exibe: ALEXANDRE

# str.endswith(sufixo) informa se o texto termina com um certo sufixo
nome_arquivo = "imagem3434.jpg"
print(nome_arquivo.endswith(".jpg"))  # exibe: True
print(nome_arquivo.endswith(".gif"))  # exibe: False

# str.startswith(prefixo) informa se o texto inicia com um certo prefixo
nome_arquivo = "imagem1212.jpg"
print(nome_arquivo.startswith("image"))  # exibe: True
print(nome_arquivo.startswith("a"))  # exibe: False

# str.format(valor, outro) substitui valores em pontos especiais do texto
nome = 'Alexandre'
print(u"Olá, meu nome é {}, qual o seu?".format(nome)) 
# exibe: Olá, meu nome é Alexandre, qual o seu?

# str.split(delimitador_opcional) devolve uma lista cujos itens são trechos do texto "divididos"
itens = "A a B b".split()  # usado sem argumentos divide nos espaços
print(itens)
# exibe: ['A', 'a', 'B', 'b']
# pode ser informado um delimitador:
print("a/b/c".split("/"))
# exibe: ['a', 'b', 'c']
# Confira também str.splitlines() que divide em quebras de linha!

# str.join(coisas) use um texto como delimitador para juntar uma coleção de textos!
coisas = ('a', 'b', 'c')
print('-'.join(coisas))
# exibe: a-b-c

# str.replace(velho, novo) # substitui todas as ocorrências de um texto dentro de outro, se houver
frase = u'as pessoas são estranhas'.replace('as', 'a')
frase = frase.replace(u'são', u'é')
print(frase)  # exibe: a pessoa é estranha
```
 É possível 'encadear' métodos, como no exemplo abaixo.
 
 ```python
# identifica arquivos que terminam tanto com .png como com .PNG
if nome_arquivo.lower().endswith('.png'):
     print("Arquivo tipo PNG")
``` 

É possível controlar a formatação da conversão de números em string, como o número de casas decimais ou com zeros à esquerda para garantir um certo número de dígitos:

```python
print("ângulo calculado: {:02f}".format(ang)) # Exibindo valor com duas casas decimais

nome_arquivo = "forma{:0>5}.svg".format(123) # Produz um nome_arquivo: "forma00123.svg"
```

Voocê pode ler mais na Documentação do Python sobre os [métodos de String](https://docs.python.org/pt-br/2.7/library/stdtypes.html#string-methods) e a [mini-linguagem de formatação](https://docs.python.org/pt-br/3.6/library/string.html#formatstrings).

### Mostando texto na área de desenho

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

### Letras com acentos, caracteres especiais e outros glifos

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

### Assuntos relacionados

- [Trabalhando com fontes e outros ajustes do texto](tipografia.md)
- [Lendo e escrevendo texto em arquivos](file_IO.md)
- [Sobre o Python 2 e alguns recursos do Python 3](futuro.md)
