
# Valores e seus tipos

em computação existe uma classificação dos valores armazenados na memória do computador, dizemos que os valores tem um * tipo*.

quando fazemos uma atribuição, criando ou alterando uma variável, por exemplo `i = 10`, o `i` é um nome que aponta para um valor na memória, `10`, um número ** inteiro**, do tipo * integer * que é normalmente abreviado como `int`.

Já `10.5`, `0.2` que tem uma parte fracionária, ou até mesmo `10.` (dez seguido de um ponto), são considerados ** números de ponto flutuante**, *floating point * ou abreviadamente `float`. valores numéricos em python são, na maior parte das vezes, dos tipos ** *inteiro*** ou ** *ponto flutuante***. Há também outros tipos como ** *número complexo*** ([mais detalhes na documentação do python](https: // docs.python.org/pt-br/3/library/stdtypes.html  # numeric-types-int-float-complex)).

textos, que aparecem entre aspas quando no meio do código de um programa, como por exemplo `'hello'` ou `"Eric Idle"`, são do tipo ** *string*** (cadeia de caracteres em português) que abreviamos como `str`. repare que `"1010"` é um * string * enquanto `1010` é um número inteiro, `int`, e `1010.0` é `float`.

outro tipo importante que já encontramos é o ** booleano ** (*boolean*), com apenas os dois valores `True` ou `False` (verdadeiro ou falso), é o tipo dos valores resultantes das operações lógicas(como `and`,  `or` e `not`), comparações(como `==`, `!=`,  `>`, `<`, `>=` e etc.) ou ainda valores que indicam um estado(como `mouse_pressed` é verdadeiro ou falso dependendo do estado dos botões do mouse)

# Objetos, tipos e classes

em linguagens de programação que trabalham com a ideia de * orientação a objetos*, e especialmente em python, os valores são * objetos * e usamos o termo * classe * e * tipo * de maneira mais ou menos intercambiável. A definição de uma classe estabelece as propriedades e comportamentos dos objetos de um certo tipo.

# Inspecionando os tipos dos valores

é comum dizer que em python as variáveis não tem tipo(como em java, por exemplo) mas sim os valores para os quais apontam. podemos descobrir a classe/tipo de um objeto/valor usando a função embutida `type()`

```python
a=1
print(type(a))
# resultado no console: <type 'int'>

a="oi"
print(type(a))
# resultado no consol<type 'str'>
```

# Conversão, tipos dos argumentos e dos valores devolvidos for funções

os valores que usamos entre parênteses em uma chamada de função(argumentos, dentro da função são chamados parâmetros) frequentemente precisar ser de tipos específicos. por exemplo `range()` só aceita como argumentos números inteiros. A função `text()`, precisa de um * string * e dois números(para as coordenadas): `text("Texto", x, y)`.

é necessário então converter os dados de um tipo para outro, como por exemplo o número 'sorteado' pela função `random()` que é um `float` pode ser convertido em `int`, sendo truncado(encurtado) perdendo a parte não inteira. Números podem ser convertidos em texto(*string*) usando `str(num)` ou com `'{}'.format(num)`.

```python
r=int(random(256))
print("Red: " + str(r))  # ou println("Red: {}".format(r))
```
# Como saber os tipos dos argumentos

para descobrir quais são os tipos dos argumentos que devemos usar com uma determinada função, precisamos ler a documentação(no caso de funções embutidas, pré-definidas, ou de bibliotecas externas) ou então olhar a definição da função.

# Tipos dos valores devolvidos

da mesma forma, é do nosso interesse saber o tipo dos valores devolvidos por uma função. isso também pode ser descoberto lendo a documentação, a definição da função, ou ainda usando `print(type(valor))`.

algumas funções executam operações mas não devolvem nenhum valor, como `setup()`, `draw()`, `no_stroke()` e `rect()`, por exemplo. sendo mais precisos, em python, essas funções devolvem o valor especial `None` (que poderíamos imaginar como "nada" ou "nenhum").

mas muitas funções devolvem algum valor como resultado. além da função `random()` que devolve um número * float * como acabamos de comentar, `color()`, por exemplo, devolve um número que representa uma cor, e podemos nós também construir funções que devolvem valores:

```python
def cor_sorteada(alpha):
   r=int(random(256)
   g=int(random(256)
   b=int(random(256)
   return color(r, g, b, alpha)

minha_cor=cor_sorteada(255)  # sorteia uma cor
```

# Alguns tipos/classes de valores/objetos

nesta tabela apresento apenas alguns dos tipos que vamos encontrar programando com processing modo python, vou marcar com * py * os que são naturais do python, mesmo que existam equivalentes no processing modo java, e * P5 * os que vem do processing, e não existem no python sozinho.

| tipo / classe | descrição | origem |
| --- | --- | --- |
| `int` | número inteiro, como `- 5`, `0` ou `42`| py |
| `float` | número de ponto flutante, como `.5` `3.` ou `6.267` (note que o separador decimal é o ponto) | py |
| `bool`| booleano é o tipo dos valores `True` ou `False`| py |
| `string`/`unicode` | cadeia de caracteres, são sequencias de glifos, podem ser criados com aspas: `“texto”` ou `u"maçã"` (este último um string unicode) | py |
| `list` | lista, coleção ordenada de itens, construída com `list(itens)` ou com colchetes no código `[, ]` | py |
| `tuple` | coleção ordenada e imutável de itens, construída com `tuple(itens)` ou com parenteses no código `(,)` | py |
| `set` | conjunto não ordenado de itens 'hasheáveis', com `set(itens)` ou com chaves no código `{, }` | py |
| `dict` | dicionário um 'mapeamento' de chaves(*keys*) e valores, criado com `dict()` ou pares `{chave: valor, }` | py |
| `None` | o "nenhum" é de um tipo especial único `None`e é devolvido por funções que não devolvem nada | py |
| `Py5Image` | imagens raster/bitmap, podem ser criadas/carregadas na memória com `load_image(arquivo_de_imagem)` | P5 |
| `Py5Shape` | contém formas vetorais, como as descritas num SVG, pode ser criado com `load_shape(arquivo)`| P5 |
| `p_vector`| vetor, usado geralmente para descrever posição, velocidade ou aceleração(em 2 ou 3 dimensões) | P5 |
| `color`< sup >＊</sup > | uma cor é um `int` disfarçado, que pode ser construídao com `color(R, G, B)` ou `color(R, G, B, alfa)`| P5 |

> ＊ preciso contar que a as cores não são um tipo 'de verdade', independente, são um jeito do processing deixar as coisas mais elegantes pra nós, tem um termo em programação pra isso: 'açucar sintático' (*syntatic sugar*). por baixo do capô as cores do processing são apenas números inteiros grandes, com 4 bytes, para R, G, B e alpha(opacidade) respectivamente, a função `color()` monta esse número grande pra nós. é útil(mais fácil) pensar em cores como um tipo especial de valores, no processing modo java você declara o tipo `color` para variáveis e funções e parâmetros que vão trabalhar com cores.

existe uma discussão relativamente complexa mas na qual eu não vou entrar aqui, o tipo `bytes` do processing lembra um * string * mas só com caracteres * ASCII*, e isso dá uma certa confusão, especialmente por estarmos usando python 2, em que os * strings * não são necessariamente * unicode*, como no python 3, mas essa é uma questão avançada que eu queria evitar neste primeiro momento.

quando você for converter em * string*, por exemplo, um objeto que descreve um nome de arquivo vindo do java, use `unicode()` em vez de `str()`, de forma a obter um `string unicode` do python 2.

# Glossário

[**valor**](https: // penseallen.github.io/pense_python2e/01-jornada.html  # termo:valor) Uma das unidades básicas de dados, como um número ou *string*, que um programa manipula.

[**tipo**](https: // penseallen.github.io/pense_python2e/01-jornada.html  # termo:tipo) Uma categoria de valores. Alguns tipos que vimos por enquanto são números inteiros (tipo `int`), números de ponto flutuante (tipo `float`) e *strings* (tipo `str`).

[**inteiro**](https: // penseallen.github.io/pense_python2e/01-jornada.html  # termo:inteiro) Um tipo que representa números inteiros.

[**ponto flutuante**](https: // penseallen.github.io/pense_python2e/01-jornada.html  # termo:ponto%20flutuante) Um tipo que representa números com partes fracionárias.

[**string**](https: // penseallen.github.io/pense_python2e/01-jornada.html  # termo:string) Um tipo que representa sequências de caracteres.

- --
este material é baseado no mate_mrial do curso https: // arteprog.space/programacao-criativa /

---
texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.